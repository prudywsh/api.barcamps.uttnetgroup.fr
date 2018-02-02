from django.http import HttpResponse
from .models import Barcamp, Speaker, Talk, Admin
from .serializers import BarcampSerializer, TalkSerializer, SpeakerSerializer
from rest_framework import generics

# Create your views here.
def index(request):
    return HttpResponse("Barcamps API.")

class BarcampList(generics.ListCreateAPIView):
    queryset = Barcamp.objects.all()
    serializer_class = BarcampSerializer

class BarcampDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Barcamp.objects.all()
    serializer_class = BarcampSerializer

class TalkList(generics.ListCreateAPIView):
    queryset = Talk.objects.all()
    serializer_class = TalkSerializer

class TalkDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Talk.objects.all()
    serializer_class = TalkSerializer

class SpeakerList(generics.ListCreateAPIView):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer

class SpeakerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer
