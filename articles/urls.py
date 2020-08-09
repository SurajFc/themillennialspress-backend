from django.urls import path
from .views import (
    getLatesNews,
    getTrendingNews,
    getPoliticsNews,
    RazorPayOrderId,
    GetAllTrendingNews,
    # RazorpayVerifySignature
    NewsLetterView,
    GetAllPoliticalNews,
    SiteMapView

)

app_name = "articles"

urlpatterns = [
    path('getLatestnews', getLatesNews.as_view()),
    path('getTrendingNews', getTrendingNews.as_view()),
    path('getPoliticsNews', getPoliticsNews.as_view()),
    path('razorpay', RazorPayOrderId.as_view()),
    path('razorpay/<str:id>', RazorPayOrderId.as_view()),
    path('trending/all', GetAllTrendingNews.as_view()),
    # path('razorverify', RazorpayVerifySignature.as_view()),
    path('newsletter', NewsLetterView.as_view()),
    path('political/all', GetAllPoliticalNews.as_view()),
    path('mysitemaps', SiteMapView.as_view()),

]
