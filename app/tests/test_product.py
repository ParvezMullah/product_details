import json
from fastapi import status


def test_wrong_endpoint(client):
    response = client.get("some_product_details")
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_get_products_without_param(client):
    response = client.get("product_details")
    assert response.status_code == status.HTTP_200_OK


def test_get_products_with_all_params(client):
    params = {
        "manufacturer_name": "manufacturer_name",
        "category_name": "category_name",
        "model_number": "model_number",
        "part_category_name": "part_category_name",
        "part_number": "part_number",
        "page": 1,
        "size": 30
    }
    response = client.get("product_details", params=params)
    response.status_code = status.HTTP_200_OK


def test_get_products_with_some_params(client):
    params = {
        "manufacturer_name": "manufacturer_name",
        "category_name": "category_name",
        "model_number": "model_number",
    }
    response = client.get("product_details", params=params)
    response.status_code = status.HTTP_200_OK
