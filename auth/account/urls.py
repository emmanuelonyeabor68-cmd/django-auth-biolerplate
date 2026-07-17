from django.urls import path
from .views import CustomLoginView, CustomRefreshView, CustomLogoutView, google_callback

urlpatterns = [
    path('login/', CustomLoginView.as_view()),
    path('refresh/', CustomRefreshView.as_view()),
    path('logout/', CustomLogoutView.as_view()),
    path('google/callback/', google_callback),
]