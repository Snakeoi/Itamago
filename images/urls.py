from django.urls import path
from . import views

app_name = 'images'

urlpatterns = [
    path('', views.ImagesList.as_view(), name='list'),
    path('upload', views.upload_image, name='upload'),
    path('delete/<int:pk>', views.ImagesDelete.as_view(), name='delete'),
    path('detail/<int:pk>', views.ImageDetail.as_view(), name='detail'),
]