from django.urls import path
from . import views

app_name = 'items'

urlpatterns = [
    path('', views.ItemsList.as_view(), name='list'),
    path('create', views.ItemsCreate.as_view(), name='create'),
    path('detail/<int:pk>', views.ItemsDetail.as_view(), name='detail'),
    path('update/<int:pk>', views.ItemsUpdate.as_view(), name='update'),
    path('delete/<int:pk>', views.ItemsDelete.as_view(), name='delete'),
]
