import pytest
from restaurants.models import Restaurant
from restaurants.serializers import RestaurantSerializer
from rest_framework.exceptions import ValidationError


def test_json_to_restaurant_model_instance(db):
    serializer = RestaurantSerializer(data={"name": "FIFOLINO"})
    serializer.is_valid(raise_exception=True)
    restaurant = serializer.save()
    assert isinstance(restaurant, Restaurant)


def test_json_to_restaurant_model_instance_with_name_too_long(db):
    serializer = RestaurantSerializer(
        data={"name": "FIFOLINO FIFOLINO FIFOLINO FIFOLINO"}
    )
    with pytest.raises(ValidationError):
        serializer.is_valid(raise_exception=True)
