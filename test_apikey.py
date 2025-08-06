import requests
import pytest
import responses

BASE_URL = "https://adjutor.lendsqr.com/v2"


# API KEY MODULE TEST CASES 


@responses.activate
def test_retrieve_api_key_with_valid_token():
    """
    TC_APIKEY_01:
    Retrieve API Key with valid token
    """
    token = "mocked_valid_token"
    headers = {"Authorization": f"Bearer {token}"}

    responses.add(
        responses.GET,
        f"{BASE_URL}/apikey",
        json={"api_key": "1234567890abcdef1234567890abcdef"},
        status=200
    )

    response = requests.get(f"{BASE_URL}/apikey", headers=headers)
    assert response.status_code == 200
    assert len(response.json().get("api_key", "")) == 32

    print("Status Code:", response.status_code)
    print("Response Text:", response.text)


@responses.activate
def test_retrieve_api_key_without_token():
    """
    TC_APIKEY_02:
    Retrieve API Key without sending token
    """
    responses.add(
        responses.GET,
        f"{BASE_URL}/apikey",
        json={"error": "Unauthorized"},
        status=401
    )

    response = requests.get(f"{BASE_URL}/apikey")
    assert response.status_code == 401

    print("Status Code:", response.status_code)
    print("Response Text:", response.text)


@responses.activate
def test_retrieve_api_key_after_session_timeout():
    """
    TC_APIKEY_03:
    Retrieve API Key with expired token
    """
    expired_token = "expired_token_example"
    headers = {"Authorization": f"Bearer {expired_token}"}

    responses.add(
        responses.GET,
        f"{BASE_URL}/apikey",
        json={"error": "Token expired"},
        status=401
    )

    response = requests.get(f"{BASE_URL}/apikey", headers=headers)
    assert response.status_code == 401

    print("Status Code:", response.status_code)
    print("Response Text:", response.text)


@responses.activate
def test_retrieve_api_key_multiple_requests():
    """
    TC_APIKEY_04:
    Retrieve API Key multiple times with same valid token
    """
    token = "mocked_valid_token"
    headers = {"Authorization": f"Bearer {token}"}

    for _ in range(3):
        responses.add(
            responses.GET,
            f"{BASE_URL}/apikey",
            json={"api_key": "1234567890abcdef1234567890abcdef"},
            status=200
        )

        response = requests.get(f"{BASE_URL}/apikey", headers=headers)
        assert response.status_code == 200

        print("Status Code:", response.status_code)
        print("Response Text:", response.text)
