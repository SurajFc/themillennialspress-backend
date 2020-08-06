from rest_framework.serializers import ModelSerializer
from .models import Donation, NewsLetter


class DonationSerializers(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Donation


class NewsLetterSerializer(ModelSerializer):
    class Meta:
        fields = ['email']
        model = NewsLetter
