from django.urls import path

from movie.views import mcmetadata


urlpatterns = [
    path('<int:pk>/', mcmetadata.retrieve_api_view),
    path('', mcmetadata.list_api_view),
]
