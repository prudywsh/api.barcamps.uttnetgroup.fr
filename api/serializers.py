from rest_framework import serializers
from .models import Barcamp, Speaker, Talk, Admin

# define unrelated serializers
class BarcampUnrelatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barcamp
        fields = ('id', 'title', 'description', 'date', 'talks_ids')

class TalkUnrelatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talk
        fields = ('id', 'title', 'description', 'slides_name', 'barcamp_id', 'speaker_id')

class SpeakerUnrelatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speaker
        fields = ('id', 'firstname', 'lastname', 'email')

# custom serializers
class TalkWithSpeakerSerializer(TalkUnrelatedSerializer):
    speaker = SpeakerUnrelatedSerializer(source='speaker_id', read_only=True)
    class Meta(TalkUnrelatedSerializer.Meta):
        fields = (*TalkUnrelatedSerializer.Meta.fields, 'speaker')

class TalkWithBarcampSerializer(TalkUnrelatedSerializer):
    barcamp = BarcampUnrelatedSerializer(source='barcamp_id', read_only=True)
    class Meta(TalkUnrelatedSerializer.Meta):
        fields = (*TalkUnrelatedSerializer.Meta.fields, 'barcamp')

# define serializers
class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ('id', 'email')

class SpeakerSerializer(SpeakerUnrelatedSerializer):
    talks = TalkWithBarcampSerializer(source="talks_ids", many=True, read_only=True)
    class Meta(SpeakerUnrelatedSerializer.Meta):
        fields = (*SpeakerUnrelatedSerializer.Meta.fields, 'talks')

class TalkSerializer(TalkUnrelatedSerializer):
    speaker = SpeakerUnrelatedSerializer(source='speaker_id', read_only=True)
    barcamp = BarcampUnrelatedSerializer(source='barcamp_id', read_only=True)
    class Meta(TalkUnrelatedSerializer.Meta):
        fields = (*TalkUnrelatedSerializer.Meta.fields, 'barcamp', 'speaker')

class BarcampSerializer(BarcampUnrelatedSerializer):
    talks = TalkWithSpeakerSerializer(source='talks_ids', many=True, read_only=True)
    class Meta(BarcampUnrelatedSerializer.Meta):
        fields = (*BarcampUnrelatedSerializer.Meta.fields, 'talks')
