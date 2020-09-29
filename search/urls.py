from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='search_index'),  
    path("<str:UserChoice>/", views.detail, name='search_detail'), 
    path("<str:UserChoice>/<int:UserId>", views.register_substitute, name='search_register_substitute')
]
