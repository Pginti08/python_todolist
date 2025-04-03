from django.urls import path
from .views import signup, login_view  # Ensure 'login' is imported

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),  # Ensure this line exists
]
