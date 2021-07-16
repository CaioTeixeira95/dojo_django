import pytest
from django.core.exceptions import ValidationError

from restaurants.models import Restaurant


def test_restaurant_name(db):
    restaurant = Restaurant(name="FIFOLINO")
    restaurant.full_clean()  # valida os dados baseado em que entra na model
    restaurant.save()  # adiciona no banco


def test_restaurant_name_too_long(db):
    restaurant = Restaurant(name="FIFOLINO FIFOLINO")
    with pytest.raises(ValidationError):
        restaurant.full_clean()  # valida os dados baseado em que entra na model
    restaurant.save()  # adiciona no banco
