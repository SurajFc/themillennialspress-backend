from rest_framework.serializers import ModelSerializer,CharField,Serializer
from users.models import User
from articles.models import (
    Category,Articles,ArticleImages,
) 


#SuperAdmin Serializer
class SuperAdminCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password"]

    def create(self, validated_data):

        user = User.objects.create_superuser(
            email=validated_data["email"], password=validated_data["password"]
        )
        user.save()
        return user


#Category Serializer
class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


#Add Articles Serializer
class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Articles
        # fields = '__all__'
        fields = ('title','subtitle','cover','content','tags','category','author_name','user','realease','slug')    



#Article Image Serializer
class ArticleImageSerializer(ModelSerializer):
    class Meta:
        model = ArticleImages
        fields = '__all__'

#GEt Article Serializer
class GetArticleSerializer(ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Articles
        fields = ('id','updated_at','category','subtitle','title','cover','tags','author_name','user','realease','is_active','slug')

    #For Media files
    def to_representation(self, instance):
        response = super(GetArticleSerializer, self).to_representation(instance)
        if instance.cover:
            response['cover'] = instance.cover.url
        return response


class SuperUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields =('user_id','email','date_joined','password','is_active','last_login')


class SuperUserPasswordSerializer(Serializer):
    old_password = CharField(required=True)
    password = CharField(required=True)
    
    class Meta:
        model = User
