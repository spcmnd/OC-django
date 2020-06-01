from django.urls import path
from . import views

urlpatterns = [
    path('', views.generate_redirection, name="form"),
    path('r/<code>', views.redirect_user),
    path('list', views.redirection_list)
]
