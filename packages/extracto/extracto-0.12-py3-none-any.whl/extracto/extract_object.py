from collections import namedtuple
from .extract_table import extract_table

_Column = namedtuple('_Column', ['path', 'row', 'many', 'column', 'optional', 'conversions'])
_GroupedParams = namedtuple('_GroupedParams', ['path', 'selector', 'many', 'columns', 'paths'])

def _get_objects(top, paths):
    print('top={}'.format(top))

    for path in paths:
        if path == '$':
            return top

        top = top[path]

    return top

def extract_object(url, tree, recipe):
    # Collect the set of objects to be walked
    columns = _collect_table_columns(recipe)

    params = _extract_table_params(columns)

    print(params[0])
    print(params[0].path)

    # Ok... how the hell do we do this? Maybe:
    # Split into array and non-array parts.

    top = {}

    # 1. Find all the prefixes for arrays.
    # 2. Evaluate the many=True rules, this gives the "seed" objects.
    # 3. Enrich with the many=False
    # 4. Graft these onto `top` if needed.
    #    a. You may need to create things along the way, eg intermediate notes.
    # 5. Evaluate the non arrays, grafting on to `top` if needed.

    non_array_entries = [x for x in params if [y for y in x.paths if not '$' in y]]
    array_entries = [x for x in params if [y for y in x.paths if '$' in y]]
    print('! array')
    for entry in [x for x in array_entries if x.many]:
        print(entry)
        rv = extract_table(
            url,
            tree,
            {
                'selector': entry.selector,
                'columns': entry.columns
            }
        )

        if entry.path == () and entry.paths == [['$']]:
            return [x[0] for x in rv]

        rows = []
        for r in rv:
            if len(entry.paths) == 1 and entry.paths[0][-1] == '$':
                rows.append(r[0])
            else:
                obj = {}
                for i, path in enumerate(entry.paths):
                    obj[path[-1]] = r[i]

                rows.append(obj)

        # Insert this set of rows into `top`. Special case: if the path is $, re-write top
        # to be the array and return.
        if entry.path == ('$',):
            top = rows
        else:
            top[entry.path[0]] = rows

    for entry in [x for x in array_entries if not x.many]:
        rv = extract_table(
            url,
            tree,
            {
                'selector': entry.selector,
                'columns': entry.columns
            }
        )


        print(rv)
        for i, paths in enumerate(entry.paths):
            for obj in _get_objects(top, paths):
                obj[paths[-1]] = rv[0][i]

    if isinstance(top, list):
        return top

    print('! non-array')
    for entry in non_array_entries:
        print(entry)
        rv = extract_table(
            url,
            tree,
            {
                'selector': entry.selector,
                'columns': entry.columns
            }
        )

        if entry.path == () and entry.paths == [[]]:
            return rv[0][0]

        for i, path in enumerate(entry.paths):
            root = top
            for j, component in enumerate(path):
                if len(path) == j + 1:
                    root[component] = rv[0][i]
                else:
                    root = root[component]


    return top

EndOfObject = ('___DONE___', '___DONE___')

def _extract_table_params(columns):
    _ParamsKey = namedtuple('_ParamsKey', ['path', 'row', 'many'])
    accumulator = {}

    for column in columns:
        key = _ParamsKey(path=tuple(column.path[0:-1]), row=column.row, many=column.many)

        if not key in accumulator:
            accumulator[key] = []

        new_column = {}

        if column.column:
            new_column['selector'] = column.column

        if column.optional:
            new_column['optional'] = True

        if column.conversions:
            new_column['conversions'] = column.conversions

        accumulator[key].append({
            'path': column.path,
            'column': new_column
        })

    params = []
    for (key, item) in accumulator.items():
        params.append(_GroupedParams(
            path=key.path,
            selector=key.row,
            many= key.many,
            columns=[x['column'] for x in item],
            paths=[x['path'] for x in item]
        ))
        pass

    print('! params')
    params.sort(key=lambda x: (len(x.path), x.path))
    for x in params:
        print(x)

    return params

def _prune_metas(path, metas):
    rv = {}

    for i in range(len(path) + 1):
        search_path = path[0:i]
        current = metas.get(tuple(search_path), {})

        for (k, v) in current.items():
            rv[k] = v

            if k == '$row':
                rv['$many'] = False
                if search_path and search_path[-1] == '$':
                    rv['$many'] = True

    return rv

# Reconstitute the data necessary to make extract_table calls.
# As you descend down the tree, collect all the $... variables.
# goal: emit a set of tuples of (row, selector, many, optional, $conversions)
# These will then get grouped by row to produce the extract_table calls.
def _collect_table_columns(recipe):
    to_visit = [([], EndOfObject)]
    to_visit.extend([([], x) for x in sorted(list(recipe.items()), key=lambda x: x[0])])

    # Track the metavariables like $many, $optional, $row, $selector.
    # This may contain values seen in a sibling tree; those get pruned out
    # at read-time
    metas = {}

    rv = []
    groups = {}

    while to_visit:
        (path, item) = to_visit.pop()
        (key, value) = item

        if key != '$' and key.startswith('$'):
            if key != '$row' and key != '$column' and key != '$optional' and key != '$conversions':
                raise Exception('unknown $-directive: {}'.format(key))

            opts = metas.get(tuple(path), {})
            opts[key] = value
            metas[tuple(path)] = opts


        if item == EndOfObject:
            data = _prune_metas(path, metas)
            print(data)

            if '$row' in data and '$column' in data:
                #print('metas: {}'.format(metas['$row']))
                rv.append(_Column(
                    path = path,
                    row = data['$row'],
                    column = data['$column'],
                    many = data['$many'],
                    optional = data.get('$optional', False),
                    conversions = data.get('$conversions', [])
                ))
            else:
                # TODO: error handling
                # 1) it's an error if we're not in a $ node
                # 2) it's an error if a $ node failed to emit any columns
                # 3) it's an error if a given path 
                pass

        if isinstance(value, dict):
            new_path = []
            new_path.extend(path)
            new_path.append(key)

            to_add = sorted(list(value.items()), key=lambda x: x[0])
            to_add.reverse()

            # Insert a sentinel to say that we've reached the end of the values
            # in the dict, and we should see if there's a valid set of instructions
            to_visit.append((new_path, EndOfObject))

            for x in to_add:
                to_visit.append((new_path, x))

    return rv



