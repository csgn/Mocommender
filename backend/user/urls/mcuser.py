from django.urls import path


from user.views import mcuser

urlpatterns = [
    path('<int:pk>/movies/<int:fk>', mcuser.retrieve_user_movie_api_view),
    path('<int:pk>/movies/', mcuser.list_user_movie_api_view),
    path('<int:pk>/', mcuser.retrieve_api_view),
    path('', mcuser.list_api_view),
]
