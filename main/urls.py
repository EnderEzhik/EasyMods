from django.urls import path
from . import views


urlpatterns = [
    path("", views.redirect_to_page),
    path("page/<int:pk>", views.ModListView.as_view(), name="mod-detail")
]