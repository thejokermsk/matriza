from rest_framework.generics import (ListAPIView, )
from rest_framework.response import (Response, )
# Create your views here.

from .models import *
from .serializers import *


class EventListAPIView(ListAPIView):
  queryset = Event.objects.filter()
  serializer_class = EventSerializer


class DetailListAPIView(ListAPIView):
  queryset = Event.objects.all()
  serializer_class = EventSerializer

  def list(self, request, *args, **kwargs):
    event_id = self.kwargs['pk']

    data = []

    russia = EventCompony.objects.filter(event_id=event_id)
    russia = EventCompanySerializer(instance=russia, many=True).data.copy()

    times = EventTime.objects.filter(event_id=event_id)
    times = EventTimeSerializer(instance=times, many=True).data.copy()

    for company in russia:
      obj = company['russia_company']

      for time in times:
        elem = CompanyTime.objects.filter(event_id=event_id, event_company_id=obj['id'])
        elem = CompanyTimeSerializer(instance=elem, many=True)
        obj['events'] = elem.data

      data.append(obj)
      

    return Response(data={
      "times": times,
      "data": data
    })
      





