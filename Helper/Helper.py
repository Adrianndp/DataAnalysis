import json


def sort_dict_by_key(dict_input):
    dict_output = {}
    for key in sorted(dict_input):
        dict_output[key] = dict_input[key]
    return json.dumps(dict_output)


def get_risk_from_market_cap(market_cap):
    # 10 billion
    if market_cap > 10000000000:
        return "low"
    if market_cap > 3000000000:
        return "middle"
    return "high"
