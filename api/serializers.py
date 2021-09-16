from django.db.models import fields
from homepage.models import Favorites
from rest_framework.serializers import ModelSerializer


class FavoritesSerializer(ModelSerializer):
    class Meta:
        model = Favorites
        fields = [
            "image_url",
        ]
