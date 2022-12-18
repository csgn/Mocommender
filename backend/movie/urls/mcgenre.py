from django.urls import path

from movie.views import mcgenre


urlpatterns = [
    path('<int:pk>/', mcgenre.mcgenre_retrieve_api_view),
    path('', mcgenre.mcgenre_list_api_view),
]
