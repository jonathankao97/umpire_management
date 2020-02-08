# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import models
from django.utils import timezone
# Create your models here.

class Auth_code(models.Model):
    code_text = models.CharField(max_length=8)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.code_text

    def active(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)