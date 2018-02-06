from django.http import HttpResponse
from .models import Barcamp, Speaker, Talk, Admin
from .serializers import BarcampSerializer, TalkSerializer, SpeakerSerializer
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from urllib.request import urlopen
from urllib.parse import urlencode
import json
import os

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
        """ Return the OAuth login link
        """
        uri = os.environ.get('ETUUTT_BASE_URI') \
            + 'oauth/authorize?client_id=' \
            + os.environ.get('ETUUTT_CLIENT_ID') \
            + '&scope=public%20private_user_account&response_type=code&state=xyz'
        return Response(uri)

    def post(self, request, format=None):
        """ Send the authorization_code to EtuUTT to get an access token
        """
        authorization_code = request.POST.get('authorization_code')

        if not authorization_code: # no authorization_code
            return Response("Missing authorization_code", status=status.HTTP_400_BAD_REQUEST)

        # prepare request
        body = {
            'client_id': os.environ.get('ETUUTT_CLIENT_ID'),
            'client_secret': os.environ.get('ETUUTT_CLIENT_SECRET'),
            'authorization_code': authorization_code,
            'grant_type': 'authorization_code'
        }
        encoded_body = bytes(urlencode(body).encode())
        uri = os.environ.get('ETUUTT_BASE_URI') + 'oauth/token'
        # make request
        etuutt_res = urlopen(uri, encoded_body)
        # parse response and get access_token and token_token
        etuutt_res_body = json.loads(etuutt_res.read().decode(etuutt_res.info().get_param('charset') or 'utf-8'))
        access_token = etuutt_res_body['access_token']
        refresh_token = etuutt_res_body['refresh_token']

        return HttpResponse(json.dumps(etuutt_res_body), content_type="application/json")
