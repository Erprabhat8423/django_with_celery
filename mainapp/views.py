from celery.schedules import crontab
from django.http.response import HttpResponse
from django.shortcuts import render
from .tasks import test_func
from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json
# Create your views here.
def test(request):
    test_func.delay()
    return HttpResponse("Done")
