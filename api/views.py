from django.http import HttpResponse
from .models import Barcamp, Speaker, Talk, Admin
from .serializers import BarcampSerializer, TalkSerializer, SpeakerSerializer
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from.lib.etuutt import get_redirect_link, get_access_code

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

class OauthToken(APIView):

    def get(self, request, format=None):
        """ Return auth link
        """
        return Response(get_redirect_link())

    def post(self, request, format=None):
        """ Send the authorization_code to EtuUTT to get an access token
        """
        authorization_code = request.POST.get('authorization_code')

        if not authorization_code: # no authorization_code
            return Response("Missing authorization_code", status=status.HTTP_400_BAD_REQUEST)

        access_token, refresh_token = get_access_code(authorization_code)

        return Response(access_token)
