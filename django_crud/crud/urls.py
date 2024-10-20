
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'), # home
    path('read', views.read, name = 'read'), # read
    path('create', views.create, name = 'create'), # create
    path('update/<int:member_id>/', views.update, name='update'),  # update
    path('delete/<int:member_id>/', views.delete, name='delete'),  #  delete
]
