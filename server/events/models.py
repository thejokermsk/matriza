from django.db import models

# Create your models here.
class Event(models.Model):
  name = models.CharField(max_length=255, verbose_name="Название события")
  date_events = models.DateField(verbose_name="Дата события")
  date_added = models.DateTimeField(auto_now_add=True, editable=False)

  def __str__(self):
    return f'{self.date_events} -> {self.name}'

  class Meta:
    verbose_name = 'Событие'
    verbose_name_plural = 'События'


class RussiaCompany(models.Model):
  name = models.CharField(max_length=255, verbose_name="Название компании")
  fullname_representative = models.CharField(max_length=255, verbose_name="Полное имя представителя")
  position_representative = models.CharField(max_length=255, verbose_name="Долженость представителя")
  phone = models.CharField(max_length=50, verbose_name="Номер телефона")
  email = models.EmailField(verbose_name="Email")
  site = models.CharField(max_length=100, verbose_name="Сайт")
  
  def __str__(self):
    return f'{self.name}'

  class Meta:
    verbose_name = 'Русская компания'
    verbose_name_plural = 'Русские компании'


class Company(models.Model):
  name = models.CharField(max_length=255, verbose_name="Названия компании")

  def __str__(self):
    return f'{self.name}'

  class Meta:
    verbose_name = 'Компания'
    verbose_name_plural = 'Компании'


class EventTime(models.Model):
  event = models.ForeignKey(to='events.Event', on_delete=models.CASCADE)
  time = models.TimeField(verbose_name="Время проведения")

  def __str__(self):
    return f'{self.time}'

  class Meta:
    verbose_name = 'Время'
    verbose_name_plural = 'Время'


class EventCompony(models.Model):
  event = models.ForeignKey(to='events.Event', on_delete=models.CASCADE)
  russia_company = models.ForeignKey(to="events.RussiaCompany", on_delete=models.CASCADE, verbose_name="Русская компания")

  def __str__(self):
    return f'{self.russia_company}'

  class Meta:
    verbose_name = 'Русская компания'
    verbose_name_plural = 'Русские компании'


class CompanyTime(models.Model):
  event = models.ForeignKey(to='events.Event', on_delete=models.CASCADE)
  event_company = models.ForeignKey(to='events.EventCompony', on_delete=models.CASCADE, verbose_name="Русская компания")
  event_time = models.ForeignKey(to='events.EventTime', on_delete=models.CASCADE, verbose_name="Время проведения")
  company = models.ForeignKey(to='events.Company', on_delete=models.CASCADE, verbose_name="Компания")

  def __str__(self):
    return f'{self.event_company}'
