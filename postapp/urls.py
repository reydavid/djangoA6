from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('addpost',views.addPost),
    path('editpost/<id>',views.editPost, name="editPost"),
    path('removepost/<id>',views.removePost, name="removePost")
]