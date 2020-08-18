from rest_framework.serializers import ModelSerializer
from .models import Donation, NewsLetter, Articles, ArticlesCount
from superadmin.serializers import CategorySerializer


class DonationSerializers(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Donation


class NewsLetterSerializer(ModelSerializer):
    class Meta:
        fields = ['email']
        model = NewsLetter


class DetailedArticleSerializer(ModelSerializer):
    category = CategorySerializer()

    class Meta:
        fields = '__all__'
        model = Articles


class ArticlesCountSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ArticlesCount
