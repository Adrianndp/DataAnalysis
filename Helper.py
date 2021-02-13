import json


def sort_dict_by_key(dict_input):
    dict_output = {}
    for key in sorted(dict_input):
        dict_output[key] = dict_input[key]
    return json.dumps(dict_output)


