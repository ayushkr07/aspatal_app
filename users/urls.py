from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name="users"

urlpatterns = [
    path('register/',views.register,name="register"),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path("profile/", views.UpdatedUserProfile, name="profile"),
    path("profile/create/", views.CreateUserProfile, name="profile-create"),
    path("profile/<int:pk>/", views.UpdatedUserProfilePk, name="profile-pk"),
    path("profile/doc/<int:pk>/", views.UpdatedDocProfilePk, name="doc-profile-pk"),
    path("profile/<int:pk>/delete/", views.DeleteUserProfilePk, name="profile-delete"),
    path("profile/doc/<int:pk>/delete/", views.DeleteDocProfilePk, name="doc-profile-delete"),
]