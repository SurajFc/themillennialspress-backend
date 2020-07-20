from django.urls import path
from .views import (
    ElasticSearchView,
)

app_name = "articles"

urlpatterns= [
    path("search/<str:query>",ElasticSearchView.as_view())
]