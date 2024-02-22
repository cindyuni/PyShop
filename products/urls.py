"""url mapping
map the url to the view function
此檔只可以叫做url"""
from django.urls import path
from . import views  # . means current folder

# Our app is /products
# /products/new
# /products/1/detail

# urlpatterns不可改
"""the root of this app; 不是call function index()只是給一個reference, 當client端傳送網址(http request)過來才會run 這個funciton"""
urlpatterns = [
    path('', views.index),
    path('new', views.new)
]