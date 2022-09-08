from . import client, business_markup

business_name = business_markup["name"]
business_p_iva = business_markup["p_iva"]
business_address = business_markup["address"]
business_cap = business_markup["cap"]
business_iban = business_markup["iban"]
business_phone = business_markup["phone"]
business_email = business_markup["email"]
business_pec = business_markup["pec"]
business_fax = business_markup["fax"]
business_id = business_markup["id_business"]


def test_get_all_business():
    response = client.get("/business")
    assert response.status_code == 200


def test_get_business_by_id():
    response = client.get(f"/business/{business_id}")
    assert response.status_code == 200


def test_filter_by_business():
    response = client.post("/business/", json={
        "name": business_name,
        "p_iva": business_p_iva,
        "address": business_address,
        "cap": business_cap,
        "iban": business_iban,
        "phone": business_phone,
        "email": business_email,
        "pec": business_pec,
        "fax": business_fax,
        "id_business": business_id
    })
    assert response.status_code == 200


def test_create_business():
    response = client.post("/business/create/", json={
        "name": business_name + 1,
        "p_iva": business_p_iva + 1,
        "address": business_address + 1,
        "cap": business_cap + 1,
        "iban": business_iban + 1,
        "phone": business_phone + 1,
        "email": business_email + 1,
        "pec": business_pec + 1,
        "fax": business_fax + 1
    })
    assert response.status_code == 200


def test_update_business():
    response = client.post("/business/update/")
    assert response.status_code == 422


def test_delete_business():
    response = client.post("/business/delete/")
    assert response.status_code == 422


def test_get_all_business_by_customer_id():
    response = client.post("/business/customer/")
    assert response.status_code == 422
