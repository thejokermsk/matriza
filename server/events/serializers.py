from django.db.models import fields
from rest_framework import serializers

from .models import *

class EventSerializer(serializers.ModelSerializer):
  class Meta:
    model = Event
    fields = '__all__'


class RussiaCompanySerializer(serializers.ModelSerializer):
  class Meta:
    model = RussiaCompany
    fields = ('id', 'name', )


class CompanySerializer(serializers.ModelSerializer):
  class Meta:
    model = Company
    fields = ('name', 'id',)


class EventTimeSerializer(serializers.ModelSerializer):

  class Meta:
    model = EventTime
    fields = ('time', 'id',)


class EventCompanySerializer(serializers.ModelSerializer):
  russia_company = RussiaCompanySerializer()

  class Meta:
    model = EventCompony
    fields = ('russia_company', 'id',)


class CompanyTimeSerializer(serializers.ModelSerializer):
  event_time = EventTimeSerializer()
  company = CompanySerializer()
  
  class Meta:
    model = CompanyTime
    fields = '__all__'