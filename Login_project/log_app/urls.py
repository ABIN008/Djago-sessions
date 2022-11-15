from django.urls import path

from log_app import views

urlpatterns = [
    # path("visit-count/", views.visit_count, name="visit-count"),
    # path("clear-count/", views.clear_count, name="clear-count"),
    
   path("login/", views.email_login, name="login"),
    path("profile/", views.profile, name="profile"),
    path("logout/", views.logout, name="logout"),
]