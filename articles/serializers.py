from rest_framework.serializers import ModelSerializer
from .models import Donation, NewsLetter, Articles, ArticlesCount
from superadmin.serializers import CategorySerializer, GetArticleSerializer


class DonationSerializers(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Donation


class NewsLetterSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = NewsLetter


class DetailedArticleSerializer(ModelSerializer):
    category = CategorySerializer()

    class Meta:
        fields = '__all__'
        model = Articles


class ArticlesCountSerializer(ModelSerializer):
    article = GetArticleSerializer

    def to_representation(self, instance):
        response = super(ArticlesCountSerializer,
                         self).to_representation(instance)
        count = response['counter']
        response = GetArticleSerializer(
            Articles.objects.get(id=response['article'])).data
        response['count'] = count
        return response

    class Meta:
        fields = '__all__'
        model = ArticlesCount
