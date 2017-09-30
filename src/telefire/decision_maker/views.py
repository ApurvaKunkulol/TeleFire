# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    """
    Function to take decisions about severity of the fire and take appropriate actions.
    """
    return HttpResponse("Index View - Decision maker.")