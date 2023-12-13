from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListStudyAPIView.as_view(), name='list_study'),
    path('<int:pk>/', views.DetailStudyAPIView.as_view(), name='detail_study'),
    path('create/', views.CreateStudyAPIView.as_view(), name='create_study'),
    path('delete/<int:pk>/', views.DeleteStudyAPIView.as_view(), name='delete_study')
]