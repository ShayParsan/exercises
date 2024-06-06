def merge_dictionaries(dict1, dict2, merge_function):
    result = dict(dict1)
    for key, value in dict2.items():
        if key in result:
            new_key = merge_function(result[key], value)
            result[key] = new_key
        else:
            result[key] = value
    return result
