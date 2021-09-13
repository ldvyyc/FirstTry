"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('content',views.ShowContent, name="content"),
    path('',views.NoneToShowContent, name="NoneToContent"),

    path('Search',views.Search_base, name="Search_base"),
    path('Search/content',views.Search_content, name="Search_content"),
    path('Search/contentshow',views.Search_Content_Show, name="Search_content//"),
    path('Search/contentshow?page=<pages>',views.Search_Content_Show_Pages, name="Search_content///"),
    path('Search/author',views.Search_author, name="Search_author"),
    path('Search/authorshow',views.Search_Author_Show, name="Search_author//"),
    path('Search/authorshow?page=<pages>',views.Search_Author_Show_Pages, name="Search_author///"),

    path('authorlist',views.ShowFirstAuthorList, name="FirstAuthorList"),

    path('content/<Search_ID>',views.TurnTo,name='TurnTo'),
    path('content/detail/<Search_ID>',views.DetailShow,name='Detail'),
    path('content/author/<Search_Author>',views.AuthorShow,name="AuthorPage"),

    path('authorlist/<Author_ID>',views.AuthorLists,name="AuthorLists"),

    path('author/<Search_Author>',views.AuthorShow,name="AuthorShow"),

]
