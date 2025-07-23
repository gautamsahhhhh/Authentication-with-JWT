from django.urls import path
from .views import SignUpView, SignInView, SignOutView,home_view

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='login'),
    path('signout/', SignOutView.as_view(), name='logout'),
    path('home/', home_view, name='home')

]
