# coding=utf8

from __future__ import print_function, absolute_import, division
import pandas as pd
import json
import traceback

from quechao import json_to_dict, dict_to_json


def model_run(df_model, df_af):
    df_model['credit_score'] = df_model['userid'] % 2
    # df_model['credit_score'] = 1 / 0
    return df_model['credit_score']


def model_main(js_input):
    # 接收后 json转dict
    dict_model = json_to_dict(js_input)

    # 根据需要，取出各变量
    df_model = dict_model['DataModel']
    df_af = dict_model['DataAntifraud']
    userid = df_model['userid'].ix[0]

    # 打分并将数据封装为标准格式
    try:
        df_model['credit_score'] = model_run(df_model, df_af)
        dict_result = {
            'AppId': -1,
            'UserId': userid,
            'Result': 1,
            # 以上为标准key；以下自定义key
            'DataModel': df_model,
            'DataAntifraud': df_af
        }
    except Exception as e:
        errorinfo = traceback.format_exc()
        dict_result = {
            'AppId': -1,
            'UserId': userid,
            'Result': 2,
            'ErrorInfo': errorinfo,
            # 以上为标准key；以下自定义key
            'DataModel': df_model,
            'DataAntifraud': df_af
        }
        print('== [errorinfo] ==')
        print(errorinfo)

    # 发送前 dict转json
    js_output = dict_to_json(dict_result)
    return js_output
