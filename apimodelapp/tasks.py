#!/usr/bin/env python
# coding:utf-8
from __future__ import absolute_import

from celery import task
from celery import shared_task


@task
def add(x, y):
    return x + y