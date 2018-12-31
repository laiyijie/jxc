def set_dict_to_model(dict_data, obj, fields=None):
    if fields is None:
        fields = dict_data.keys()
    for key in fields:
        setattr(obj, key, dict_data.get(key))
