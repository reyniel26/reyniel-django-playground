from django.urls import path

from . import views

# Namespacing URL names


app_name = 'polls'
urlpatterns = [
    # # eg: /polls/
    # path('', views.index, name='index'),
    # # eg: /polls/5/
    # path('specifics/<int:question_id>/',views.detail, name='detail'),
    # # eg: /polls/5/results/
    # path('<int:question_id>/results/',views.results, name='results'),

    # Generic View
    path('',views.IndexView.as_view(),name='index'),
    path('<int:pk>/',views.DetailView.as_view(),name='detail'),
    path('<int:pk>/results/',views.ResultsView.as_view(),name='results'),

    # eg: /polls/5/vote
    path('<int:question_id>/vote/',views.vote,name='vote'),

]