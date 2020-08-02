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
    GetArticleSerializer
)
from .models import (
    Articles, Donation
)
from .serializers import DonationSerializers
from datetime import datetime
# es = Elasticsearch()

cur_time = datetime.now()


class getLatesNews(APIView):
    permission_classes = (AllowAny,)
    serilizer_class = GetArticleSerializer

    def get(self, request):
        try:
            obj = Articles.objects.filter(
                is_active=True, realease__lt=cur_time).order_by('-created_at')[:5]
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
            obj = Articles.objects.filter(is_active=True,
                                          tags__contains=['trending'])
            print(obj)
            serializer = self.serilizer_class(obj, many=True)
            return Response(serializer.data)
        except:
            return Response(status=400)


class getPoliticsNews(APIView):
    permission_classes = (AllowAny,)
    serilizer_class = GetArticleSerializer

    def get(self, request):
        try:
            obj = Articles.objects.filter(
                is_active=True, category__slug="politics")
            print(obj)
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
            print(response)

            serializer = DonationSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save(order_id=response['id'])

                response['other'] = serializer.data

                return Response(response)
            return Response("error")

            print("res--->",  request.data)
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
