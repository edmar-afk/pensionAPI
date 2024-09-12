from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChatbotViewSet, CreateUserView, UserDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Create a router and register the ChatbotViewSet
api_router = DefaultRouter()
api_router.register(r'chatbot', ChatbotViewSet, basename='chatbot')

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
    path('user/', UserDetailView.as_view(), name='user_detail'),
    path('token/', TokenObtainPairView.as_view(), name='get_token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),

    # Include the router URLs here without an additional 'api/' prefix
    path('', include(api_router.urls)),
]
