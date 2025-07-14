import pytest

@pytest.mark.parametrize("person_id, expected_status", [
    (111, 200),        # Happy path
    ("invalid", 400),  # Sad path: string
    (None, 400),       # Sad path: missing
])
def test_import_person(api_client, person_id, expected_status):
    response = api_client.post_person(person_id)
    assert response is not None, "No se recibió respuesta"
    print(f"Status: {response.status_code}, Body: {response.text}")
    assert response.status_code == expected_status

def test_person_inserted_in_db(api_client, db_conn):
    person_id = 111
    response = api_client.post_person(person_id)
    assert response.status_code == 200

    cursor = db_conn.cursor()
    cursor.execute("SELECT DISTINCT * FROM Test.Worldsys WHERE personId = %s", (person_id,))
    result = cursor.fetchone()
    assert result is not None, "personId no encontrado en la base de datos"