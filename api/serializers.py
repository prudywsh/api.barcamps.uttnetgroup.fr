from rest_framework import serializers
from .models import Barcamp, Speaker, Talk, Admin

class SpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speaker
        fields = ('id', 'firstname', 'lastname', 'email')

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ('id', 'email')

class TalkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talk
        fields = ('id', 'title', 'description', 'slides_name', 'barcamp', 'speaker')

class BarcampSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barcamp
        fields = ('id', 'title', 'description', 'date', 'talks')
