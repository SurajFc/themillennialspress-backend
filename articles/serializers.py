from rest_framework.serializers import ModelSerializer
from .models import Donation, NewsLetter, Articles


class DonationSerializers(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Donation


class NewsLetterSerializer(ModelSerializer):
    class Meta:
        fields = ['email']
        model = NewsLetter


class DetailedArticleSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Articles
