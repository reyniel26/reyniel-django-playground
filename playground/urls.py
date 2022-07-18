from django.urls import path
from . import views

# URL Pattern objects
# URL Conf
urlpatterns = [
    # path('playground/hello/',views.say_hello),
    # hello/ only because the playground/ is already added in main urls
    path('hello/',views.say_hello)
]