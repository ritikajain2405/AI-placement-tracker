from django.urls import path
from . import views



urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('topics/', views.topic_list, name='topic_list'),
    path('topics/add/', views.topic_create, name='topic_create'),
    path('topics/<int:pk>/edit/', views.topic_update, name='topic_update'),
    path('topics/<int:pk>/delete/', views.topic_delete, name='topic_delete'),
   
    path('companies/', views.company_list, name='company_list'),
    path('companies/add/', views.company_create, name='company_create'),
    path('companies/<int:pk>/edit/', views.company_update, name='company_update'),
    path('companies/<int:pk>/delete/', views.company_delete, name='company_delete'),

    path("delete/<int:pk>/", views.delete_topic, name="delete_topic"),
    path("entry/<int:pk>/update/", views.update_entry, name="update_entry"),
    path("toggle/<int:topic_id>/", views.toggle_complete, name="toggle_complete"),
    path("entry/<int:pk>/delete/", views.delete_entry, name="delete_entry"),
    path('topic/<int:pk>/toggle/', views.toggle_topic_status, name='topic_toggle'),
    path('mock-interview/', views.mock_interview, name='mock_interview'),
]
