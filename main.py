import requests
import configuration


def test_create_user_service():
    # Realiza la petición al servicio mock
    response = requests.post(
        f"{configuration.URL_SERVICE}{configuration.CREATE_USER_PATH}",
        json={"firstName": "Aa"}
    )
    # Valida respuesta exitosa
    assert response.status_code == 200