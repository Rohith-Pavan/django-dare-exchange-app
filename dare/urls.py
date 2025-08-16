from django.urls import path
from . import views

urlpatterns = [
    path('', views.DareListView.as_view(), name='dare_list'),
    path('dare/<int:pk>/', views.DareDetailView.as_view(), name='dare_detail'),
    path('dare/new/', views.DareCreateView.as_view(), name='dare_create'),
    path('dare/<int:pk>/edit/', views.DareUpdateView.as_view(), name='dare_update'),
    path('dare/<int:pk>/delete/', views.DareDeleteView.as_view(), name='dare_delete'),
    path('dare/<int:pk>/accept/', views.accept_dare, name='accept_dare'),
    path('dare/<int:pk>/complete/', views.complete_dare, name='complete_dare'),
    path('dare/<int:pk>/rate/', views.rate_dare, name='rate_dare'),
    path('signup/', views.signup, name='signup'),
    path('health/', views.health_check, name='health_check'),
]