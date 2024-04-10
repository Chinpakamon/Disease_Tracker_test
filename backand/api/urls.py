from django.urls import include, re_path as url, path

from rest_framework.routers import DefaultRouter

from .views import UserViewSet, user_registration

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')


urlpatterns = [
    path('', include(router.urls)),
    path('register/', user_registration),
    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.authtoken')),
]
