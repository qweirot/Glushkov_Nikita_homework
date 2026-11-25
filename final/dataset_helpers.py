def filter_cond(data, field, condition):
    result = []

    for record in data:
        value = record.get(field)

        if condition(value):
            result.append(record)

    return result


def group_by(data, fields):
    groups = {}

    for record in data:
        group_cond = tuple(record.get(field) for field in fields)

        if group_cond not in groups:
            groups[group_cond] = []

        groups[group_cond].append(record)

    return groups


def aggregate_groups(groups, aggregate_func):
    res = {}

    for group_cond, records in groups.items():
        res[group_cond] = aggregate_func(records)

    return res
