# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from umpires.models import Umpire
from django.contrib import admin
from .models import Auth_code

admin.site.register(Auth_code)
admin.site.register(Umpire)

# Register your models here.
