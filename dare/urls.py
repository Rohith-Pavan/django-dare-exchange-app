from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.DareListView.as_view(), name='dare_list'),
    path('health/', views.health_check, name='health_check'),
    path('dare/<int:pk>/', views.DareDetailView.as_view(), name='dare_detail'),
    path('dare/new/', views.DareCreateView.as_view(), name='dare_create'),
    path('dare/<int:pk>/edit/', views.DareUpdateView.as_view(), name='dare_update'),
    path('dare/<int:pk>/delete/', views.DareDeleteView.as_view(), name='dare_delete'),
    path('dare/<int:pk>/accept/', views.dare_accept, name='dare_accept'),
    path('dare/<int:pk>/complete/', views.dare_complete, name='dare_complete'),
    path('dare/<int:pk>/verify/', views.dare_verify, name='dare_verify'),
    path('dare/<int:pk>/rate/', views.dare_rate, name='dare_rate'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(next_page='dare_list'), name='logout'),
]