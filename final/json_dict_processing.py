def extract_nested_value(obj, keys):
    temp = obj
    for key in keys:
        if not isinstance(temp, dict):
            return None
        temp = temp.get(key)

    return temp


def process_dictionary_with_config(dictionary, config):
    res = {}

    for field, rules in config.items():
        if isinstance(rules, tuple):
            keys, type_of_field = rules
            value = extract_nested_value(dictionary, keys)

            if value is not None:
                value = type_of_field(value)
        else:
            value = extract_nested_value(dictionary, rules)

        res[field] = value

    return res


def process_list_of_dicts_with_config(list_of_dicts, config):
    res = []

    for dictionary in list_of_dicts:
        res.append(process_dictionary_with_config(dictionary, config))

    return res


def create_processor(config):

    def processor(data):
        if isinstance(data, dict):
            return process_dictionary_with_config(data, config)

        if isinstance(data, list):
            return process_list_of_dicts_with_config(data, config)

    return processor
