def lookup_key(data, value):
    list_keys = []
    for k, v in data.items():
        if v == value:
            list_keys.append(k)
    return list_keys
        
            
    return [k for k, v in data.items() if v == value]