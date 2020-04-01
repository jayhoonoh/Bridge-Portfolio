from django.urls import path
from Bridge import views

urlpatterns = [
    path("Bridge/", views.clientindex.as_view(), name="clientindex"),
    path("Bridge/<str:clientname>/", views.clientview.as_view(), name="clientview"),
    ]