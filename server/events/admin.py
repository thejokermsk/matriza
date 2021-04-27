from django.contrib import admin

from .models import *

# Register your models here.
class RussiaCompanyInline(admin.TabularInline):
  model = EventCompony
  fk_name = 'event'

class TimeInline(admin.TabularInline):
  model = EventTime
  fk_name = 'event'

class CompanyTimeInline(admin.TabularInline):
  model = CompanyTime
  fk_name = 'event'
  extra = 1

  def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
    if request.path.split('/')[4] == 'add':
      return
    idx = request.path.split('/')[4]

    if db_field.name == 'event_company':
      kwargs['queryset'] = EventCompony.objects.filter(event_id = int(idx)) 

    if db_field.name == 'event_time':
      kwargs['queryset'] = EventTime.objects.filter(event_id = int(idx)) 

    return super(CompanyTimeInline, self).formfield_for_foreignkey(db_field, request, **kwargs)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
  inlines = (RussiaCompanyInline, TimeInline, CompanyTimeInline)


@admin.register(RussiaCompany)
class RussiaCompanyAdmin(admin.ModelAdmin):
  pass


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
  pass