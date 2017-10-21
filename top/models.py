#coding: utf8
import datetime
from django.db.models.aggregates import Count
from django.db import models
from django.utils import timezone


# Create your models here.

class KeywordLogManager(models.Manager):
    def top_hourly(self):
        now = timezone.now()
        time_begin = now - datetime.timedelta(hours=1)
        cursor = self.filter(log_time__gte=time_begin).values('keyword').annotate(
            pv=Count('keyword', distinct=True)).order_by('-pv')
        return cursor

    def top_daily(self):
        now = timezone.now()
        time_begin = now - datetime.timedelta(days=30)
        cursor = self.filter(log_time__gte=time_begin).values('keyword').annotate(
            pv=Count('keyword', distinct=True)).order_by('-pv')
        return cursor

    def latest(self):
        now = timezone.now()
        time_begin = now - datetime.timedelta(hours=1)
        return self.filter(log_time__gte=time_begin).order_by('-log_time')


class KeywordLog(models.Model):
    objects = KeywordLogManager()
    log_time = models.DateTimeField(auto_now_add=True, db_index=True)
    keyword = models.CharField(max_length=100)
    ip = models.CharField(max_length=30)

    def __unicode__(self):
        return self.keyword


class HashLogManager(models.Manager):
    def top_hourly(self):
        now = timezone.now()
        time_begin = now - datetime.timedelta(hours=1)
        cursor = self.filter(log_time__gte=time_begin).values('hash_id').annotate(
            pv=Count('hash_id', distinct=True)).order_by('-pv')
        return cursor

    def top_daily(self):
        now = timezone.now()
        time_begin = now - datetime.timedelta(days=30)
        cursor = self.filter(log_time__gte=time_begin).values('hash_id', 'hash_name').annotate(
            pv=Count('hash_id', distinct=True)).order_by('-pv')
        return cursor

class HashLog(models.Model):
    objects = HashLogManager()
    log_time = models.DateTimeField(auto_now_add=True, db_index=True)
    hash_id = models.PositiveIntegerField()
    hash_name = models.CharField('资源名称', max_length=255)
    ip = models.CharField(max_length=30)

    def __unicode__(self):
        return self.hash_name