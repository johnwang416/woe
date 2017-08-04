# coding=utf8

from __future__ import print_function, absolute_import, division
import pandas as pd
pd.options.mode.chained_assignment = None
import requests

from quechao import dict_to_json, json_to_dict, post_json

# 测试数据
loc = 'api_model_sample.txt'

with open(loc) as f:
    js_input = f.read()

import pickle
with open('mobile_20160805_111656.pkl') as f:
    df_model = pickle.load(f)
df_model['credit_score_quechao'] = -1
df_model['credit_score_quechao_yici'] = -1
df_model['credit_score_quechao_guodu'] = -1
df_model['credit_score_quechao_pdl'] = -1

for i in range(len(df_model.index)):
    # 将数据封装为标准格式
    userid = df_model['userid'].ix[i]
    dict_model = {
        'AppId': -1,
        'UserId': userid,
        # 以上为标准key；以下自定义key
        'DataModel': df_model[df_model['userid'] == userid],
        'DataAntifraud': json_to_dict(js_input)['DataAntifraud']
    }

    # 发送前 dict转json
    js_input = dict_to_json(dict_model)

    # 发送给打分API
    js_output = post_json(js_input, 'http://127.0.0.1:8002/api_model?mark=sample')
    # js_output = post_json(js_input, 'http://172.17.16.25:8100/api_model?mark=mobile')

    # 接收后 json转dict
    dict_output = json_to_dict(js_output)

    # 逐个输出的结果，可以自定义地用
    df_model['credit_score_quechao'].ix[i] = dict_output['DataModel']['credit_score'].ix[0]
    df_model['credit_score_quechao_yici'].ix[i] = dict_output['DataModel']['credit_score_yici'].ix[0]
    df_model['credit_score_quechao_guodu'].ix[i] = dict_output['DataModel']['credit_score_guodu'].ix[0]
    df_model['credit_score_quechao_pdl'].ix[i] = dict_output['DataModel']['credit_score_pdl'].ix[0]

print(df_model[['credit_score', 'credit_score_quechao']])
print(df_model[['credit_score_yici', 'credit_score_quechao_yici']])
print(df_model[['credit_score_guodu', 'credit_score_quechao_guodu']])
print(df_model[['credit_score_pdl', 'credit_score_quechao_pdl']])