import pytest
from pages.import_api import ImportAPI

@pytest.fixture
def api_client():
    base_url = "https://api.test.worldsys.ar"
    token = "api-test-challenge-token"  
    return ImportAPI(base_url, token)

import psycopg2

#@pytest.fixture
#def db_conn():
#    conn = psycopg2.connect(
#        host="localhost",
#        user="usuario",
#        password="password",
#        dbname="nombre_bd"
#    )
#    yield conn
#    conn.close()
