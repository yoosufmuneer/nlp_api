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


from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

#from .models import MyDescriptionList


class MyDescription(View):
    def get(self, request):
        #description_list = list(MyDescriptionList.objects.values())
        #return JsonResponse(description_list, safe=False) 
        return HttpResponse({""}, content_type='text/json')


    # To turn off CSRF validation (not recommended in production)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(MyDescription, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        data = request.body.decode('utf8')
        data = json.loads(data)
        try:
            field = data['description_field']
            blob1 = TextBlob(field)
            #tokens = word_tokenize(data["description_field"])

            response = json.dumps({"polarity": blob1.sentiment.polarity})
        except:
            response = json.dumps({"Error": "Invalid Description"})
            
        return HttpResponse(response, content_type='text/json')

        # data = request.body.decode('utf8')
        # data = json.loads(data)

        # try:
        #     new_description = MyDescriptionList(description_field=data["description_field"])
        #     new_description.save()
            
        #     return JsonResponse({"tags": data}, safe=False)
        #     #return JsonResponse({"created": response}, safe=False)
        # except:
        #     return JsonResponse({"error": "not a valid data"}, safe=False)
