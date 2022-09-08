from fastapi.testclient import TestClient
from slack import app

client = TestClient(app)
jwt_bruno = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZF9hY2NvdW50IjoiMjhkYWE3NWItN2VhMi00ZjJjLWI3NzEtNTI1YTA2Y2Q3ZDlmIiwidXNlciI6ImJydW5vIiwiYWJpbGl0YXRlIjoiMSIsImFjY291bnRUeXBlIjoiN2U1NTQ5NGMtMDhmNC0xMWVkLTg2MWQtMDI0MmFjMTIwMDAyIiwiYWNjb3VudFR5cGVOYW1lIjoiYWRtaW5pc3RyYXRvciIsImFjY291bnRMaXN0RnVuY3Rpb24iOiJhZG1pbiIsImlkX2VtcGxveWVlIjoiMTI0ZTQ1NjctZTg1Yi0xZmQzLWE0NTYtMzMzMzIyMjMzNDEyIiwiZW1wbG95ZWVfZmlyc3RfbmFtZSI6IkJydW5vIiwiZW1wbG95ZWVfbGFzdF9uYW1lIjoiQm9zcyIsImVtcGxveWVlX2VtYWlsIjoiYnJ1bm9AZW1haWwuY29tIiwiZW1wbG95ZWVfcGhvbmVfbnVtYmVyIjoiMDEyNDU2NzgwIiwiYnVzaW5lc3NfbmFtZSI6Im1hcmt1cCIsImJ1c2luZXNzX3BfaXZhIjoiMzIzNTU2NjA5MDYiLCJidXNpbmVzc19hZGRyZXNzIjoidmlhIGxvbWJhcmRpYSAxNSIsImJ1c2luZXNzX2NhcCI6IjAwMTgwIiwiYnVzaW5lc3NfaWJhbiI6IklUOTRMMDMwMDIwMzI4MDcyNjM0Njg0ODMyMSIsImJ1c2luZXNzX3Bob25lIjoiMDYxMjM0NTY3OCIsImJ1c2luZXNzX2VtYWlsIjoibWFya3VwQGdtYWlsLmNvbSIsImJ1c2luZXNzX3BlYyI6Im1pb25vbWVAcGVjYXppZW5kYS5pdCIsImJ1c2luZXNzX2ZheCI6IjA2MTIzNDU2NzgiLCJidXNpbmVzc19pZCI6IjEyNGU0NTY3LWU4NWItMWZkMy1hNDU2LTQyNjYxNDQ3NDAwMCJ9.QUtC-W-rBVkmDoyvu5VkyDv3OUzQma_C83rVkSsHFPc"
account_bruno = {
    "id_account": "28daa75b-7ea2-4f2c-b771-525a06cd7d9f",
    "user": "bruno",
    "abilitato": 0,
    "id_tipo_account": "7e55494c-08f4-11ed-861d-0242ac120002",
}
business_markup = {
    "name": "markup",
    "p_iva": "32355660906",
    "address": "via lombardia 15",
    "cap": "00180",
    "iban": "IT94L0300203280726346848321",
    "phone": "0612345678",
    "email": "markup@gmail.com",
    "pec": "mionome@pecazienda.it",
    "fax": "0612345678",
    "id_business": "124e4567-e85b-1fd3-a456-426614474000"
}
orders_pippo = {
    "description": None,
    "id_customer": "123e4567-e89b-12d3-a456-426614174000",
    "id_business": "124e4567-e85b-1fd3-a456-426614474000",
    "startDate": "2022-01-01",
    "endDate": "2022-03-30",
    "id_order": "124e4567-e44f-1fd3-a456-330002223341"
}
customers_pippo = {
    "name": "pippo",
    "p_iva": "11122233321",
    "address": "via antani 12",
    "cap": "00123",
    "iban": "IT94L0300203280726346848123",
    "phone": "06987654321",
    "email": "pippi@mail.it",
    "pec": "pippo@pec.it",
    "fax": "06987654321",
    "id_business": None,
    "id_customer": "123e4567-e89b-12d3-a456-426614174000"
}
employee_bruno = {
    "first_name": "bruno",
    "last_name": "rossi",
    "cf": "123",
    "iban": "696",
    "id_contractType": "198ef11d-cf73-4245-8469-2ddfa9979acf",
    "email": "brunorossi@gmail.com",
    "phoneNumber": "1234",
    "id_employee": "124e4567-e85b-1fd3-a456-333322233412",
}
type_account_admin = {
    "accountTypeName": "administrator",
    "function": "admin",
    "id_account_type": "7e55494c-08f4-11ed-861d-0242ac120002"
}
type_contract_indeterminato = {
    "name": "indeterminato",
    "info": None,
    "id_contract_type": "198ef11d-cf73-4245-8469-2ddfa9979acf"
}
presence_bruno = {
    "id_employee": "124e4567-e85b-1fd3-a456-333322233412",
    "date_presence": "2022-01-01",
    "id_tipoPresenza": "b867b283-38a0-4eb3-8df1-55ccb5f310df",
    "id_order": "124e4567-e44f-1fd3-a456-330002223341",
    "hours": 50,
    "id_presence": "221e4567-e85b-1fd3-a456-333000003412"
}
typt_presence_malattia = {
    "name": "malattia",
    "percentage_increase": 0,
    "hourly_pay": None,
    "id_presence_type": "b867b283-38a0-4eb3-8df1-55ccb5f310df"
}
order_employee = {
    "id_order": "124e4567-e44f-1fd3-a456-330002223341",
    "id_employee": "124e4567-e85b-1fd3-a456-333322233412",
    "rate": "200"
}
# id_account = "28daa75b-7ea2-4f2c-b771-525a06cd7d9f"
# id_order = "124e4567-e44f-1fd3-a456-330002223341"
# id_employee_bruno = "124e4567-e85b-1fd3-a456-333322233412"
# id_customer = "123e4567-e89b-12d3-a456-426614174000"
# id_account_type = "7e55494c-08f4-11ed-861d-0242ac120002"
# id_contract = "198ef11d-cf73-4245-8469-2ddfa9979acf"
# id_presence = "0adabf8e-dd83-4a4d-b2c8-9e3e0c2ab801"
# id_presence_type = "ca34d37e-600c-452e-a8e4-2efb53161812"
