import requests
import pytest
import responses

BASE_URL = "https://adjutor.lendsqr.com/v2"


# LOGIN MODULE TEST CASES

@responses.activate
def test_login_with_valid_credentials():

    payload = {
        "email": "davidgreat_test1@example.com",
        "password": "StrongPass123!"
    }

    responses.add(
        responses.POST,
        f"{BASE_URL}/login",
        json={"token": "mocked_token_123"},
        status=200
    )

    response = requests.post(f"{BASE_URL}/login", json=payload)
    assert response.status_code == 200
    assert "token" in response.json()

    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())


@responses.activate
def test_login_with_incorrect_password():
    
    payload = {
        "email": "davidgreat_test1@example.com",
        "password": "WrongPassword123!"
    }

    responses.add(
        responses.POST,
        f"{BASE_URL}/login",
        json={"error": "Invalid credentials"},
        status=401
    )

    response = requests.post(f"{BASE_URL}/login", json=payload)
    assert response.status_code == 401
    assert "error" in response.json()

    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())
