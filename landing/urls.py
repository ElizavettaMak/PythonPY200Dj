from django.urls import path
from .views import MyFormView #MyTemplView
app_name = 'landing'
urlpatterns = [
    path('form', MyFormView.as_view() ),
    #path('template', MyTemplView.as_view()),
]