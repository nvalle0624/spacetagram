from django.conf.urls import include, url
from django.urls import path
from api.views import FavoritesViewSet

from rest_framework import routers
from api.views import api_add_favorite_view, api_delete_favorite_view

router = routers.DefaultRouter()

router.register('favorites', FavoritesViewSet)

urlpatterns = [
    url(r"^api/", include(router.urls)),
    path('api/favrites/', api_add_favorite_view, name='addView'),
    path('api/delete/<str:image_url>',
         api_delete_favorite_view, name='deleteView')
]
