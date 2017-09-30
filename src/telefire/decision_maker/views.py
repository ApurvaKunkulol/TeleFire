# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
import pdb


class CallUser(View):
    @csrf_exempt
    def post(self, request):
        pdb.set_trace()
        return HttpResponse("This is a response from the class based view.")