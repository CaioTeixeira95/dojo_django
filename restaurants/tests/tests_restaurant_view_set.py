from django.urls import reverse
from restaurants.models import Restaurant


def test_list(client, db, make_restaurant):
    make_restaurant()
    response = client.get(reverse("restaurant-list"))
    assert response.status_code == 200
    assert response.json() == [{"name": "Fifolino"}]


def test_post(client, db):
    data = {"name": "Fifocoin"}
    response = client.post(reverse("restaurant-list"), data=data)
    assert response.status_code == 201
    assert response.json() == data


def test_put(client, db, make_restaurant):
    restaurant = make_restaurant()
    data = {"name": "Fifocoins"}
    response = client.put(
        reverse("restaurant-detail", kwargs={"pk": restaurant.id}),
        data=data,
        content_type="application/json",
    )
    assert response.status_code == 200
    assert response.json() == data


def test_delete(client, db, make_restaurant):
    restaurant = make_restaurant()
    response = client.delete(
        reverse("restaurant-detail", kwargs={"pk": restaurant.id}),
    )
    assert response.status_code == 204
