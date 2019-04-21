from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from rest_framework import viewsets,permissions
from .serializers import UserSerializer, GroupSerializer,MoviesSerializer
from .models import Movies
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS,IsAdminUser



class IsAdminOrOwnProfileOrReadOnly(BasePermission):
    """
    Only safe request is authenticated as a normal user or he can view his data and edit that, all methods are allowed for superuser only.
    """
    def has_permission(self, request, view):
        if (request.method != 'POST' and request.user):
            return True
        elif(request.method not in SAFE_METHODS and request.user.is_superuser ):
            return True
        else:
            return False

    def has_object_permission(self, request, view,obj):
        if (request.method in SAFE_METHODS and request.user):
            return True
        elif (request.method not in SAFE_METHODS and obj.username == request.user.username and request.method != 'DELETE'):
            return True
        elif(request.method not in SAFE_METHODS and request.user.is_superuser ):
            return True
        else:
            return False


class IsAuthenticatedOrReadOnly(BasePermission):
    """
    Only safe request is authenticated as a normal user, all methods are allowed for superuser only.
    """

    def has_permission(self, request, view):
        if (request.method in SAFE_METHODS and request.user):
            return True
        elif(request.method not in SAFE_METHODS and request.user.is_superuser ):
            return True
        else:
            return False


User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserListView(LoginRequiredMixin, ListView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_list_view = UserListView.as_view()


class UserUpdateView(LoginRequiredMixin, UpdateView):

    model = User
    fields = ["name"]

    def get_success_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})

    def get_object(self):
        return User.objects.get(username=self.request.user.username)


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminOrOwnProfileOrReadOnly,)
    def get_queryset(self):
        """
      search for users
        """
        queryset = User.objects.all()

        username = self.request.query_params.get('username', None)
        if username is not None:

            queryset = User.objects.filter(username__icontains="per")

        return queryset



class MoviesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows movies to be viewed or edited.
    """
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def get_queryset(self):
        """
        search for movies
        """
        queryset = Movies.objects.all()

        moviename = self.request.query_params.get('movie', None)
        if moviename is not None:

            queryset = Movies.objects.filter(name__icontains = moviename)
        return queryset
