from statistics import mean


def get_values(data, field):
    values = []

    for record in data:
        value = record.get(field)

        if value is not None:
            values.append(value)

    return values


def calc_mean(data, field):
    return mean(get_values(data, field))


def calc_top_n(data, field, n):

    clear_data = [record for record in data if record.get(field) is not None]

    sorted_data = sorted(clear_data,
                         key=lambda record: record[field], reverse=True)

    return (sorted_data[:n])
