from . import client, type_contract_indeterminato

contract_type_id = type_contract_indeterminato["name"]
contract_type_info = type_contract_indeterminato["info"]
contract_type_id = type_contract_indeterminato["id_contract_type"]


def test_get_all_contract_type():
    response = client.get("/type/contract")
    assert response.status_code == 200


def test_get_contract_type_by_id():
    response = client.post(f"/type/contract/{contract_type_id}")
    assert response.status_code == 200


def test_create_contract_type():
    response = client.post("/type/contract/create/", json={
        "name": "pytest_create_contract_type",
        "info": "pytest made this contract type"
    })
    assert response.status_code == 200


def test_update_contract_type_by_ID():
    response = client.post("/type/contract/update/", json={
        "name": "pytest_update_contract_type_by_ID",
        "info": "pytest updated this contract type",
        "id_contract_type": contract_type_id
    })
    assert response.status_code == 200


def test_delete_contract_type_by_ID():
    response = client.post("/type/contract/delete/", params={
        "id_contract": contract_type_id + 1
    })
    assert response.status_code == 200
