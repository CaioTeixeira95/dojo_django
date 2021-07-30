from django.urls import reverse


def test_list(client, db):
    response = client.get(reverse("restaurant-list"))
    assert response.status_code == 200
