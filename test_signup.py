import requests
import pytest
import responses

BASE_URL = "https://adjutor.lendsqr.com/v2"


# SIGNUP MODULE TEST CASES


@responses.activate
def test_signup_with_valid_details():
    responses.add(
        responses.POST,
        f"{BASE_URL}/signup",
        json={"user_id": "abc123", "auth_token": "token_1234567890"},
        status=201
    )

    payload = {
        "name": "David Great",
        "email": "davidgreat_test1@example.com",
        "password": "StrongPass123!"
    }
    response = requests.post(f"{BASE_URL}/signup", json=payload)
    assert response.status_code == 201
    assert "user_id" in response.json()
    assert "auth_token" in response.json()

    print("Status Code:", response.status_code)
    print("Response Text:", response.text)

@responses.activate
def test_signup_with_empty_fields():
    responses.add(
        responses.POST,
        f"{BASE_URL}/signup",
        json={"error": "Fields cannot be empty"},
        status=400
    )

    payload = {"name": "", "email": "", "password": ""}
    response = requests.post(f"{BASE_URL}/signup", json=payload)
    assert response.status_code == 400
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)

@responses.activate
def test_signup_with_duplicate_email():
    responses.add(
        responses.POST,
        f"{BASE_URL}/signup",
        json={"error": "Email already exists"},
        status=400
    )

    payload = {
        "name": "David Great",
        "email": "davidgreat_test1@example.com",  # previously used email
        "password": "StrongPass123!"
    }
    response = requests.post(f"{BASE_URL}/signup", json=payload)
    assert response.status_code == 400
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)

@responses.activate
def test_signup_with_invalid_password_format():
    responses.add(
        responses.POST,
        f"{BASE_URL}/signup",
        json={"error": "Password too weak"},
        status=400
    )

    payload = {
        "name": "David Great",
        "email": "invalidpass@example.com",
        "password": "123"  # tthis password is too weak
    }
    response = requests.post(f"{BASE_URL}/signup", json=payload)
    assert response.status_code == 400
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)
