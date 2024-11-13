from django.urls import path

from app.views import CreateApplicationView, DetailApplicationView

urlpatterns = [
    path('application/add/', CreateApplicationView.as_view()),
    path('application/get/', DetailApplicationView.as_view()),
]
