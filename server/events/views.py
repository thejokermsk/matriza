from rest_framework.generics import (ListAPIView, )
from rest_framework.response import (Response, )
# Create your views here.

from django.db.models import Q

from .models import *
from .serializers import *


class EventListAPIView(ListAPIView):
  queryset = Event.objects.filter().order_by('-date_events')
  serializer_class = EventSerializer


class DetailListAPIView(ListAPIView):
  queryset = Event.objects.filter()
  serializer_class = EventSerializer

  def list(self, request, *args, **kwargs):
    event_id = self.kwargs['pk']

    queryset = Event.objects.get(id=event_id)
    serializer_class = EventSerializer(instance=queryset, many=False)

    title = serializer_class.data['name']

    data = []

    russia = EventCompony.objects.filter(event_id=event_id)
    russia = EventCompanySerializer(instance=russia, many=True).data.copy()

    times = EventTime.objects.filter(event_id=event_id)
    times = EventTimeSerializer(instance=times, many=True).data.copy()

    for time in times:
      time['time'] = time['time'][:-3]

    for company in russia:
      obj = company['russia_company']
      obj['events'] = []
      for time in times:
        try:
          elem = CompanyTime.objects.get(Q(event_company_id=company['id']) & Q(event_time_id=time['id']) & Q(event_id=event_id))
          elem = CompanyTimeSerializer(instance=elem)
          obj['events'].append({
            "time": time['time'],
            "company": elem.data['company']['name']
          })
        except CompanyTime.DoesNotExist:
          obj['events'].append({
            "time": time['time'],
            "company": ""
          })
        


      data.append(obj)
    

    if len(data) != 0 and len(times) != 0:
      for item in data:
        error = 0
        for event in item['events']:
          if len(event['company']) == 0:
            error = error + 1

        if error == len(times):
          item['status'] = False
        else:
          item['status'] = True

    return Response(data={
      "title": title,
      "times": times,
      "data": data
    })
