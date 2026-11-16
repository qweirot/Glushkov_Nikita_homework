def add_attribute(data, field_name, calc_func):
    for record in data:
        record[field_name] = calc_func(record)

    return data
