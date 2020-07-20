from django.urls import path
from .views import (
    SuperAdminLoginView,
    SuperAdminCreateView,
    GetUserView,
    SuperAdminLogoutView,
    CategoryView,
    EditCategoryView,
    DeleteCategoryView,
    AddArticleView,
    ArticleImagesView,
    GetArticlesView,
    GetDetailedArticle,
    EditArticleStatusView,
    # SearchArticleView,
    EditArticleView,
    GetSuperUserView,
    EditSuperUserStatusView,
    EditSuperUserPassword,
    AddSuperUserView,
    GetTotalOverview
)

app_name = "superadmin"

urlpatterns = [
    path("login", SuperAdminLoginView.as_view()),
    path("createadmin", SuperAdminCreateView.as_view()),
    path("user", GetUserView.as_view()),
    path("logout", SuperAdminLogoutView.as_view()),
    path("category", CategoryView.as_view()),
    path("editcategory", EditCategoryView.as_view()),
    path('deletecategory',DeleteCategoryView.as_view()),
    path('addarticle',AddArticleView.as_view()),
    path('article/images',ArticleImagesView.as_view()),
    path('article/getall',GetArticlesView.as_view()),
    path('article/view/<str:slug>',GetDetailedArticle.as_view()),
    path('changestatus',EditArticleStatusView.as_view()),
    # path('article',SearchArticleView.as_view()),
    path('editarticle',EditArticleView.as_view()),
    path('getUsers',GetSuperUserView.as_view()),
    path('editsuperuser',EditSuperUserStatusView.as_view()),
    path('superuserpass',EditSuperUserPassword.as_view()),
    path('addsuperuser',AddSuperUserView.as_view()),
    path('totalOverview',GetTotalOverview.as_view()),



]
