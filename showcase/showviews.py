# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render


# Create your views here.
def base(request):
    return render(request, 'showcase/base.html')
