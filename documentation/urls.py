from django.urls import path
from . import views
urlpatterns = [
    path('',views.Student.as_view(),name="sendemail")
]