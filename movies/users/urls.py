from django.urls import include, path

from rest_framework import routers
from .views import MoviesViewSet,UserViewSet



router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'movies', MoviesViewSet)

from movies.users.views import (
    user_list_view,
    user_redirect_view,
    user_update_view,
    user_detail_view,
)

app_name = "users"
urlpatterns = [
    path('', include(router.urls)),

    # path("", view=user_list_view, name="list"),
    # path("~redirect/", view=user_redirect_view, name="redirect"),
    # path("~update/", view=user_update_view, name="update"),
    # path("<str:username>/", view=user_detail_view, name="detail"),
]
