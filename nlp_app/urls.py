from django.conf.urls import url,include
from django.contrib import admin
from nlp_app.views import MyDescription

urlpatterns = [
    url(r'',MyDescription.as_view()),

]