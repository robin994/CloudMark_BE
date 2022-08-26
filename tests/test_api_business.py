from . import client, id_business


def test_get_all_business():
    response = client.get("/business")
    assert response.status_code == 200


def test_get_business_by_id():
    response = client.get(f"/business/{id_business}")
    assert response.status_code == 200


def test_filter_by_business():
    response = client.post("/business/")
    assert response.status_code == 422


def test_create_business():
    response = client.post("/business/create/")
    assert response.status_code == 422


def test_update_business():
    response = client.post("/business/update/")
    assert response.status_code == 422


def test_delete_business():
    response = client.post("/business/delete/")
    assert response.status_code == 422


def test_get_all_business_by_customer_id():
    response = client.post("/business/customer/")
    assert response.status_code == 422
