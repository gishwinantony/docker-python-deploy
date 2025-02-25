from .views import ProductCreateApiView
from django.urls import path

urlpatterns = [
    path('create',ProductCreateApiView.as_view())
]