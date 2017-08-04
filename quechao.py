# coding=utf8

from __future__ import print_function, absolute_import, division
import pandas as pd
import json
import requests


def json_merge(js_model, js_type):
    dict_input = {
        'js_model': js_model,
        'js_type': js_type
    }
    js_input = json.dumps(dict_input)
    return js_input


def json_split(js_input):
    dict_input = json.loads(js_input)
    return dict_input['js_model'], dict_input['js_type']


def dict_to_json(dict_model):
    for k in dict_model.keys():
        if isinstance(dict_model[k], pd.DataFrame):
            dict_model[k] = dict_model[k].to_json(orient='records', date_format='iso', force_ascii=0)
        else:
            pass
    return json.dumps(dict_model)


def json_to_dict(js_input):
    dict_model = json.loads(js_input)
    for k in dict_model.keys():
        try:
            dict_model[k] = pd.read_json(dict_model[k])
        except Exception as e:
            pass
    return dict_model


def post_json(js, url):
    headers = {'content-encoding': 'utf-8', 'content-type': 'application/json'}
    return requests.post(url=url,
                         data=js,
                         headers=headers
                         ).content
