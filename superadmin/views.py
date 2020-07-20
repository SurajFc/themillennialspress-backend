from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from .serializers import (
     SuperAdminCreateSerializer, CategorySerializer,ArticleSerializer,
     ArticleImageSerializer,GetArticleSerializer,SuperUserSerializer,
     SuperUserPasswordSerializer
)
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from news.prevents import *
from news.baseclass import AbstractBaseClassApiView
from articles.models import ( 
    Category, Articles,ArticleImages
 )
from django.db.models import F
import json
from enum import IntEnum
from users.models import User
import json
from django.http import Http404
from rest_framework.pagination import PageNumberPagination
from rest_framework.settings import api_settings


class LoginStatus(IntEnum):
    wrong = 0
    good = 1
    deleted = 2


class SuperAdminLoginView(APIView):
    permission_classes = (AllowAny,)
    # throttle_classes = (UserLoginRateThrottle,)

    def post(self, request):

        user = authenticate(
            email=request.data["email"], password=request.data["password"]
        )

        if user is not None and user.is_active and user.is_superuser:
            update_last_login(None, user)
            token, _ = Token.objects.get_or_create(user=user)

            return Response({"token": token.key})
        return Response(
            {"msg": "Wrong Email or Password ", "status": LoginStatus.wrong},
            status=status.HTTP_400_BAD_REQUEST,
        )


class SuperAdminCreateView(AbstractBaseClassApiView):
    serializer_class = SuperAdminCreateSerializer
    permission_classes = (IsAdminUser,)
    http_method_names = ("post",)


class SuperAdminLogoutView(APIView):
    permission_classes = (IsAdminUser,)

    def post(self, request):
        return Response()


class GetUserView(APIView):
    permission_classes = (IsAdminUser,)

    def get(self, request):
        token1 = request.META["HTTP_AUTHORIZATION"]
        token = token1.split(" ")[1]
        data = Token.objects.filter(key=token).values(email=F("user__email"))
        return Response({"data": data})


class CategoryView(AbstractBaseClassApiView):
    serializer_class = CategorySerializer
    permission_classes = (IsAdminUser,)
    model = Category
    http_method_names = ("get", "post")
    
    def get(self,request):
        try:
            x = self.model.objects.all().order_by('-updated_at')
            ser = self.serializer_class(x,many=True)
            return Response(ser.data)
        except:
            return Response(status=status.HTTP_204_NO_CONTENT)
        

#Editing Articles
class EditCategoryView(APIView):
    serializer_class = CategorySerializer
    permission_classes = (IsAdminUser,)

    def post(self, request):
        try:
            print("=======>", request.data)
            cat = request.data["cat"]
            obj = Category.objects.get(id=cat)
            serializer = self.serializer_class(obj, data=request.data, partial=True)
            print(serializer.is_valid())
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(status=status.HTTP_200_OK)
            print(serializer.errors)
            return Response(serializer.errors)
        except Category.DoesNotExist:
            raise Http404

#Deleteing Article
class DeleteCategoryView(APIView): 
    permission_classes = (IsAdminUser,)

    def post(self, request):
        try:
            print("=======>", request.data)
            cat = request.data["cat"]
            obj = Category.objects.get(id=cat)
            obj.delete()
            return Response(status=status.HTTP_200_OK)

        except Category.DoesNotExist:
            raise Http404


#Article Add
class AddArticleView(AbstractBaseClassApiView):
    serializer_class = ArticleSerializer
    permission_classes = (IsAdminUser,)
    http_method_names = ('post',)
   

#Article Images
class ArticleImagesView(AbstractBaseClassApiView):
    serializer_class  = ArticleImageSerializer
    permission_classes = (IsAdminUser,)
    model = ArticleImages


#Get aRticles by sorting and pagination
class GetArticlesView(ListAPIView):
    permission_classes = (IsAdminUser,)
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS 
    serializer_class = GetArticleSerializer

    queryset = Articles.objects.all().order_by('-updated_at')


#PAgination with APIVIEW

    # def get(self,request):
    #     # try:
    #         instance = self.model.objects.values('id','updated_at','category__name','title','cover','category','tags','author_name','user','realease','is_active').order_by('-updated_at')
    #         page = self.paginate_queryset(instance)
    #         if page is not None:

    #             serializer = self.get_paginated_response(self.serializer_class(page,many=True).data)
    #         else:
    #             serializer =  self.serializer_class(instance,many=True)
    #         return Response(serializer.data)
    # def get(self, request):
    #     ...
    #     page = self.paginate_queryset(self.queryset)
    #     if page is not None:
    #         serializer = self.serializer_class(page, many=True)
    #         return self.get_paginated_response(serializer.data)
    #     # except:
        #     return Response(status=status.HTTP_204_NO_CONTENT)
        

    # queryset =  Articles.objects.values('id','updated_at','title','cover','category','tags','author_name','user','realease','is_active').order_by('-updated_at')

#one article detailed view
class GetDetailedArticle(APIView):
    permission_classes = (IsAdminUser,)


    def get(self,request,slug):
        try:
            x = Articles.objects.filter(slug=slug).values('updated_at','subtitle','title','cover','category','tags','author_name','user','realease','is_active','slug','content',category_name=F('category__name'))
            return Response(x)
        except:
            return Response(status=status.HTTP_204_NO_CONTENT)
        


class EditArticleStatusView(APIView):
    permission_classes = (IsAdminUser,)

    def post(self,request):
        try:
           Articles.objects.filter(id=request.data['id']).update(is_active=request.data['active'])
           return Response({"status":"1"})
        except Articles.DoesNotExist:
           return  Response(status=status.HTTP_400_BAD_REQUEST)


#Temporary Search for admin
# TODO Implement elasticsearch later
# class SearchArticleView(ListAPIView):
#     permission_classes = (IsAdminUser,)
#     pagination_class = api_settings.DEFAULT_PAGINATION_CLASS 
#     serializer_class = GetArticleSerializer



#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         context['count'] = self.count or 0
#         context['query'] = self.request.GET.get('q')
#         return context

#     def get_queryset(self):
#         request = self.request
#         query = request.GET.get('q', None)
        
#         if query is not None:
#             qs = Articles.objects.filter(title__icontains=query).all()

#             self.count = len(qs) # since qs is actually a list
#             return qs
#         return Articles.objects.none() 


#Edit Article View
class EditArticleView(APIView):

    serializer_class = ArticleSerializer
    permission_classes = (IsAdminUser,)

    def post(self, request):
        try:
            request = self.request
            slug = request.GET.get('q', None)
            if slug:
                obj = Articles.objects.get(slug=slug)
                serializer = self.serializer_class(obj, data=request.data, partial=True)
                print(serializer.is_valid())
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(status=status.HTTP_200_OK)
                print(serializer.errors)
                return Response(serializer.errors)
            else:
                return Response(serializer.errors)
        except Category.DoesNotExist:
            raise Http404



#Get User SuperAdminView
class GetSuperUserView(ListAPIView):
    permission_classes = (IsAdminUser,)
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS 
    serializer_class = SuperUserSerializer

    queryset = User.objects.filter(is_superuser=True).order_by('-date_joined')



class EditSuperUserStatusView(APIView):

    serializer_class = SuperUserSerializer
    permission_classes = (IsAdminUser,)

    def post(self, request):
        try:
            request = self.request
            user_id = request.GET.get('q', None)
            if user_id:
                obj = User.objects.get(user_id=user_id)
                serializer = self.serializer_class(obj, data=request.data, partial=True)
                
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(status=status.HTTP_200_OK)
                
                return Response(serializer.errors)
            else:
                return Response(serializer.errors)
        except Category.DoesNotExist:
            raise Http404

    
    # def put(self, request):
    #     try:
    #         obj = User.objects.get(user_id=request.data['user_id'])
    #         serializer = self.serializer_class(obj, data=request.data, partial=True)
            
    #         if serializer.is_valid(raise_exception=True):
    #             serializer.save()
    #             return Response(status=status.HTTP_200_OK)
            
    #             return Response(serializer.errors)
            
    #     except Category.DoesNotExist:
    #         raise Http404

#Edit SuperUsers PAssword
class EditSuperUserPassword(APIView):
    permission_classes = (IsAdminUser,)
    serializer_class = SuperUserPasswordSerializer
    model = User

    def post(self,request):
        obj = self.model.objects.get(user_id=request.data['user_id'])
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
                # Check old password
                if not obj.check_password(serializer.data.get("old_password")):
                    return Response({"old_password": ["Wrong password."],"status":'0'}, status=status.HTTP_400_BAD_REQUEST)
                # set_password also hashes the password that the user will get
                obj.set_password(serializer.data.get("password"))
                obj.save()
                response = {
                    'status': '1',
                    'code': status.HTTP_200_OK,
                    'message': 'Password updated successfully',
                    
                }

                return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#register SuperUser
class AddSuperUserView(APIView):
    permission_classes = (IsAdminUser,)

    def post(self,request):
        try:
            email = request.data['email']
            password = request.data['password']
            User.objects.create_superuser(email=email,password=password)
            return Response({'status':'1'})
        except User.DoesNotExist:
             return Response({'status':'0'}, status=status.HTTP_400_BAD_REQUEST)

import json       

#Total Overview
class GetTotalOverview(APIView):
    permission_classes = (IsAdminUser,)

    def get(self,request):
        
        data ={
            'users':User().get_total_users,
            'articles':Articles().get_total_articles
        }
      
        return Response(data)