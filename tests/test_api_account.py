from . import client, id_account, id_employee_bruno


def test_get_all_accounts():
    response = client.get("/account")
    assert response.status_code == 200


def test_get_accounts_by_uuid():
    response = client.get(f"/account/{id_account}")
    assert response.status_code == 200


def test_create_account():
    response = client.post("/account/signin/")
    assert response.status_code == 422


def test_update_account():
    response = client.post("/account/update/")
    assert response.status_code == 422


def test_reset_password():
    response = client.patch("/account/reset_passowrd", json={
        "password_employee": "pop",
        "id_employee": id_employee_bruno,
        "session_admin": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZF9hY2NvdW50IjoiMjhkYWE3NWItN2VhMi00ZjJjLWI3NzEtNTI1YTA2Y2Q3ZDlmIiwidXNlciI6ImJydW5vIiwiYWJpbGl0YXRlIjoiMSIsImFjY291bnRUeXBlIjoiN2U1NTQ5NGMtMDhmNC0xMWVkLTg2MWQtMDI0MmFjMTIwMDAyIiwiYWNjb3VudFR5cGVOYW1lIjoiYWRtaW5pc3RyYXRvciIsImFjY291bnRMaXN0RnVuY3Rpb24iOiJhZG1pbiIsImlkX2VtcGxveWVlIjoiMTI0ZTQ1NjctZTg1Yi0xZmQzLWE0NTYtMzMzMzIyMjMzNDEyIiwiZW1wbG95ZWVfZmlyc3RfbmFtZSI6IkJydW5vIiwiZW1wbG95ZWVfbGFzdF9uYW1lIjoiQm9zcyIsImVtcGxveWVlX2VtYWlsIjoiYnJ1bm9AZW1haWwuY29tIiwiZW1wbG95ZWVfcGhvbmVfbnVtYmVyIjoiMDEyNDU2NzgwIiwiYnVzaW5lc3NfbmFtZSI6Im1hcmt1cCIsImJ1c2luZXNzX3BfaXZhIjoiMzIzNTU2NjA5MDYiLCJidXNpbmVzc19hZGRyZXNzIjoidmlhIGxvbWJhcmRpYSAxNSIsImJ1c2luZXNzX2NhcCI6IjAwMTgwIiwiYnVzaW5lc3NfaWJhbiI6IklUOTRMMDMwMDIwMzI4MDcyNjM0Njg0ODMyMSIsImJ1c2luZXNzX3Bob25lIjoiMDYxMjM0NTY3OCIsImJ1c2luZXNzX2VtYWlsIjoibWFya3VwQGdtYWlsLmNvbSIsImJ1c2luZXNzX3BlYyI6Im1pb25vbWVAcGVjYXppZW5kYS5pdCIsImJ1c2luZXNzX2ZheCI6IjA2MTIzNDU2NzgiLCJidXNpbmVzc19pZCI6IjEyNGU0NTY3LWU4NWItMWZkMy1hNDU2LTQyNjYxNDQ3NDAwMCJ9.QUtC-W-rBVkmDoyvu5VkyDv3OUzQma_C83rVkSsHFPc"
    })
    assert response.status_code == 200


def test_get_session():
    response = client.post("/account/login", json={
        "user": "bruno",
        "password": "pop"
    })
    assert response.status_code == 200


def test_delete_account():
    response = client.post("/account/delete/")
    assert response.status_code == 422


def test_jwt_verify():
    response = client.post("/account/verify_account")
    assert response.status_code == 422
