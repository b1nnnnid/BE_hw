from django.urls import path
from . import views

app_name="posts"

urlpatterns = [
    path('', views.main, name='main'),  # 메인 페이지
]
