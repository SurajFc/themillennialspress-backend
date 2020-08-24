from news.prevents import UserLoginRateThrottle
from news.baseclass import AbstractBaseClassApiView
from rest_framework.settings import api_settings
from rest_framework.generics import ListAPIView
import hashlib
import hmac
import razorpay
import uuid
import json
import requests
from elasticsearch import Elasticsearch
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,  IsAuthenticated
from superadmin.serializers import (
    GetArticleSerializer,
)
from .models import (
    Articles, Donation, NewsLetter, ArticlesCount
)
from .serializers import DonationSerializers, NewsLetterSerializer, DetailedArticleSerializer, ArticlesCountSerializer
from datetime import datetime
# es = Elasticsearch()
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class getLatesNews(APIView):
    permission_classes = (AllowAny,)
    serilizer_class = GetArticleSerializer

    def get(self, request):
        try:

            obj = Articles.objects.filter(
                is_active=True, realease__lt=datetime.now()).order_by('-created_at')[:5]
            serializer = self.serilizer_class(obj, many=True)

            return Response(serializer.data)
            # return Response(serializer.errors)
        except:
            return Response(status=400)


class getTrendingNews(APIView):
    permission_classes = (AllowAny,)
    serilizer_class = GetArticleSerializer

    def get(self, request):
        try:
            obj = Articles.objects.filter(is_active=True, realease__lt=datetime.now(),
                                          tags__contains=['trending'])
            serializer = self.serilizer_class(obj, many=True)
            return Response(serializer.data)
        except:
            return Response(status=400)


class getPoliticsNews(APIView):
    permission_classes = (AllowAny,)
    serilizer_class = GetArticleSerializer

    def get(self, request):
        try:
            obj = Articles.objects.filter(realease__lt=datetime.now(),
                                          is_active=True, category__slug="politics")

            serializer = self.serilizer_class(obj, many=True)
            return Response(serializer.data)
        except:
            return Response(status=400)


razpay_secret = 'QyZ4I5tw3WmneR23Hua9bAnW'
client = razorpay.Client(
    auth=("rzp_test_e1ZiqTgqw1ljs0", razpay_secret))


class RazorPayOrderId(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, id=None):

        if id is None:
            payload = {"amount": request.data['amount']*100,  "currency": "INR",
                       "receipt": "receipt#" + str(uuid.uuid1())[:8],  "payment_capture": 1}

            response = client.order.create(data=payload)

            serializer = DonationSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save(order_id=response['id'])

                response['other'] = serializer.data

                return Response(response)
            return Response("error")

            try:

                obj = Donation.objects.get(order_id=request.data['order_id'])
                obj.status = True
                obj.save()
                return Response(status=200)
            except:
                return Response(status=400)

        else:
            try:
                obj = Donation.objects.get(order_id=id)
                obj.status = True
                obj.save()
                return Response(status=200)
            except:
                return Response(status=400)

# def hmac_sha256(val):
#     h = hmac.new(razpay_secret.encode("ASCII"), val.encode(
#         "ASCII"), digestmod=hashlib.sha256).hexdigest()
#     print(h)
#     return h


# class RazorpayVerifySignature(APIView):
#     permission_classes = (AllowAny,)

#     def post(self, request):
#         print(request.data['verify'])

#         reqData = request.data['verify']
#         # print(type(params_dict), type(params_dict['razorpay_signature']))
#         # x = client.utility.verify_payment_signature(params_dict)
#         # print(x)
#         # return Response(x)
#         generated_signature = hmac_sha256(
#             reqData["razorpay_order_id"] + "|" + reqData["razorpay_payment_id"])
#         if (generated_signature == reqData["razorpay_signature"]):
#             print("here verified")
#             return Response()

#         else:
#             print("not ")
#             return Response(status=400)


# Get All Trending News
class GetAllTrendingNews(ListAPIView):
    permission_classes = (AllowAny,)

    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS
    serializer_class = GetArticleSerializer
    queryset = Articles.objects.filter(is_active=True, realease__lt=datetime.now(),
                                       tags__contains=['trending'])


# NewsLetter
class NewsLetterView(AbstractBaseClassApiView):
    throttle_scope = "newsletter"
    serializer_class = NewsLetterSerializer
    permission_classes = (AllowAny,)
    http_method_names = ("post",)


# class InstaFeedView(APIView):
#     permision_classes = (AllowAny,)

#     def get(self, request):
#         instagram = Instagram()

#         medias = instagram.get_medias("unpaid_media", 50)
#         print(medias)
#         media = medias[6]
#         print(media)
#         return Response(media)

# Get All Political News
class GetAllPoliticalNews(ListAPIView):
    permission_classes = (AllowAny,)

    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS
    serializer_class = GetArticleSerializer
    queryset = Articles.objects.filter(is_active=True, realease__lt=datetime.now(),
                                       category__slug="politics")

# For sitemaps


class SiteMapView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        try:
            x = Articles.objects.filter(
                is_active=True, realease__lt=datetime.now())

            ser = GetArticleSerializer(x, many=True)
            return Response(ser.data)
        except:
            pass


class ViewArticleDetail(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, slug1, slug2):

        try:
            x = Articles.objects.get(
                category__slug=slug1, slug=slug2, is_active=True, realease__lt=datetime.now())
            ser = DetailedArticleSerializer(x)
            return Response(ser.data)

        except Articles.DoesNotExist:
            return Response(status=400)


class ArticleElasticSearchMainView(APIView):
    permission_classes = (AllowAny,)
    throttle_scope = "search"

    def get(self, request):
        try:
            es = Elasticsearch()
            request = self.request
            query = request.GET.get('q', None)
            page = int(request.GET.get('page', 1))

            PerPage = 10
            q = {
                "from": ((page-1)*PerPage),
                "size": PerPage,
                "query": {
                    "bool": {
                        "must": {
                            "multi_match": {
                                "query": query,
                                "fields": ["title^3", "subtitle^3", "tags^3", 'category.name^2', "author_name^2", 'user'],
                                "fuzziness": "AUTO",
                            }
                        },
                        "must_not": [{
                            "match": {
                                "is_active": "false",
                            }
                        }],
                    }
                }
            }

            res = es.search(index="articles", body=q)
            count = res['hits']['total']['value']
            final = []
            for hit in res['hits']['hits']:
                final.append(hit['_source'])

            send_data = {
                "count": count,
                "results": final
            }

            return Response(send_data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ArticleCountView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        article = request.data['article']
        try:
            x = ArticlesCount.objects.get(article=article)
            x.counter += 1
            x.save()
            return Response()
        except ArticlesCount.DoesNotExist:
            return Response(status=400)


class MostViewedView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        try:
            obj = Articles.objects.filter(
                is_active=True, realease__lt=datetime.now()).order_by('-articlescount__counter')[:5]
            ser = GetArticleSerializer(obj, many=True)

            return Response(ser.data)

        except Articles.DoesNotExist:
            return Response(status=400)


class RelatedArticleView(APIView):
    permission_classes = (AllowAny,)
    serilizer_class = GetArticleSerializer

    def get(self, request):
        try:
            slug = request.GET.get('slug', None)
            obj = Articles.objects.filter(
                is_active=True, realease__lt=datetime.now(), category__slug=slug).order_by('-created_at')[:10]
            print("here", obj)
            serializer = self.serilizer_class(obj, many=True)

            return Response(serializer.data)

        except:
            return Response(status=400)
