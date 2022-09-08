from . import client


def test_get_all_contract_type():
    response = client.get("/type/contract")
    assert response.status_code == 200


def test_get_contract_type_by_id():
    response = client.post(f"/type/contract/{}")
    assert response.status_code == 200


def test_create_contract_type():
    response = client.post("/type/contract/create/")
    assert response.status_code == 422


def test_update_contract_type_by_ID():
    response = client.post("/type/contract/update/")
    assert response.status_code == 422


def test_delete_contract_type_by_ID():
    response = client.post("/type/contract/delete/")
    assert response.status_code == 422
