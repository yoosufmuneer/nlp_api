# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import JsonResponse
from django.http import HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from textblob import TextBlob



class MyDescription(View):
    def get(self, request):
        return HttpResponse({"Hello"}, content_type='text/json')


    # To turn off CSRF validation
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(MyDescription, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        data = request.body.decode('utf8')
        data = json.loads(data)
        try:
            field = data['description_field']
            blob1 = TextBlob(field)

            response = json.dumps({"polarity": blob1.sentiment.polarity})
        except:
            response = json.dumps({"Error": "Invalid Description"})
            
        return HttpResponse(response, content_type='text/json')