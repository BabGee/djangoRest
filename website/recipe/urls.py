from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='recipe-index'),
    path('recipe/<int:pk>', views.recipe_detail, name='recipe-detail')
]