#/usr/bin/env python
# coding:utf-8

from __future__ import print_function, absolute_import, division
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import pdb

# 每个模型，单独import一个.py文件
import model.model_sample.model_main as model_sample
# import model.mobile.model_main as model_mobile


@csrf_exempt
def api_model(request):
    if request.method == "GET":
        return HttpResponse('[Error] Please use post method')
    elif request.method == "POST":
        # if not request.POST.get():
        #     return HttpResponse(400)
        mark = request.GET.get('mark')
        data = request.body
        # 根据参数发送到不同的模型中
        if mark == 'sample':
            r = model_sample.model_main(data)
        # elif mark == 'mobile':
            # r = model_mobile.model_main(data)
        else:
            pass
        return HttpResponse(r)
