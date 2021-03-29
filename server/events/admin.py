from django.contrib import admin

from .models import *

# Register your models here.
class CompanyTimeInline(admin.TabularInline):
  model = CompanyTime

class RussiaCompanyInline(admin.TabularInline):
  model = EventCompony

class TimeInline(admin.TabularInline):
  model = EventTime


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
  inlines = (RussiaCompanyInline, TimeInline, CompanyTimeInline)



@admin.register(RussiaCompany)
class RussiaCompanyAdmin(admin.ModelAdmin):
  pass


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
  pass