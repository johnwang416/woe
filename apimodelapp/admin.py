from django.contrib import admin

# Register your models here.
from kombu.transport.django import models as kombu_models
from djcelery.models import (TaskState,WorkerState,PeriodicTask,IntervalSchedule,CrontabSchedule)



admin.site.register(kombu_models.Message)
admin.site.register(IntervalSchedule)
admin.site.register(CrontabSchedule)
admin.site.register(PeriodicTask,PeriodicTaskAdmin)
admin.site.register(TaskState)
admin.site.register(WorkerState)