from django.urls import path
from .views import (
    getLatesNews,
    getTrendingNews,
    getPoliticsNews,
    RazorPayOrderId,
    GetAllTrendingNews,
    # RazorpayVerifySignature
    NewsLetterView,
    InstaFeedView
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
    path('instafeed', InstaFeedView.as_view())
]
