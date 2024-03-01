import requests
import unittest
uri = "http://127.0.0.1:8080"

class PlaidTestCase(unittest.TestCase):
    def test_create_link(self):
        response = requests.post(f"{uri}/api/info")
        print(response.json())
        response = requests.post(f"{uri}/api/create_link_token")
        print(response.json())
    def test_get_info(self):
        response = requests.get(f"{uri}/api/balance")
        print(response.json()["accounts"][0])
    def test_create_payment(self):
        response = requests.post(f"{uri}/api/create_payment_recipient")
        recipient_id = response.json()["recipient_id"]
        response = requests.post(f"{uri}/api/create_payment_initiation",json={"recipient_id":recipient_id})
        payment_id = response.json()["payment_id"]
        response = requests.post(f"{uri}/api/get_payment_initiation",json={"payment_id":payment_id})
        response = requests.post(f"{uri}/api/create_payment_consent",json={"recipient_id":recipient_id})
        print(response.json())



if __name__ == "__main__":
    unittest.main()