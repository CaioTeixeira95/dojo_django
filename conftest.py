import pytest
from restaurants.models import Restaurant


@pytest.fixture
def make_restaurant(db):
    def _restaurant(name="Fifolino"):
        return Restaurant.objects.create(name=name)

    return _restaurant
