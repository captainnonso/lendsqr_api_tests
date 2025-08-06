# Lendsqr Adjutor API Test Scripts

This repository contains automated test scripts for the Adjutor API modules as part of the QA Engineer assessment for Lendsqr.

## 📌 Overview

As part of the assessment, this project covers automated testing for three critical functionalities of the Adjutor platform:

1. **Signup Module**
2. **Login Module**
3. **API Key Retrieval Module**

Each module includes both positive and negative test cases to verify API behavior and response validation.

---

## 🔧 Tech Stack

- **Python 3.12**
- **Pytest** – For test execution
- **Requests** – For HTTP requests
- **Responses** – For mocking API behavior where needed

---

## 📁 Project Structure

.
├── test_signup.py # Test cases for Signup
├── test_login.py # Test cases for Login
├── test_apikey.py # Test cases for API Key retrieval
└── README.md # Project documentation


---

## ✅ Test Modules & Coverage

### 🔐 Signup
- Valid signup
- Signup with empty fields
- Signup with duplicate email
- Signup with weak password

### 🔐 Login
- Valid login
- Login with incorrect credentials

### 🔐 API Key Retrieval
- With valid token
- Without token
- With expired token
- Multiple retrieval requests

---

## 🧪 How to Run Tests

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/lendsqr-api-tests.git
   cd lendsqr-api-tests

2. **Run all tests**

pytest

3. **Run specific test module**

pytest test_signup.py

**Test Summary**
1. All tests were executed locally using pytest

2. Response times were logged under 1 second (~830ms)

3. All test cases passed successfully (100% pass rate)

## Notes
1. The tests used mocked or dummy responses as instructed, since authentication tokens were not provided.

2. URLs used are based on the Adjutor API base path.

3. All tests are built with reusability and clarity in mind.

#Submission Details
This repository fulfills Task 2 of the QA assessment.

Tasks 1, 3, and 4 are documented in the provided Google Sheet.

For more details, refer to the full QA Report and Loom video submission.


**David Great**
QA Engineer – Lendsqr Technical Assessment
📧 softwaretestingmachine@gmail.com

