from elasticsearch import Elasticsearch
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated


es = Elasticsearch()



class ElasticSearchView(APIView):
    permission_classes = (AllowAny,)

    def get(self,request,query):
        q = {
            "query":{
                "multi_match": {
                            "query": 'vue',
                                "fields": ["title","tags","cover"],
                                "fuzziness": "2",

                        }
            }
        }

        res = es.search(index="articles", body=q)
        print('res=>',res)
        final = []
        for hit in res['hits']['hits']:
            print(hit)
            final.append(hit['_source'])
        print(final)
        return Response(final)