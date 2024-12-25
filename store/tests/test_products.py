import pytest
from model_bakery import baker
from store.models import Product, Collection
from rest_framework import status


@pytest.fixture
def create_product(api_client):
    def do_create_product(bad_request=False):
        collection = baker.make(Collection)
        return api_client.post(
            "/store/products/",
            {
                "title": "" if bad_request else "a",
                "description": "a",
                "slug": "a",
                "inventory": 1,
                "unit_price": 1,
                "collection": collection.id,
            },
        )

    return do_create_product


@pytest.mark.django_db
class TestCreateProduct:
    def test_if_user_anonymous_returns_401(self, create_product):
        response = create_product()

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_returns_403(self, create_product, authenticate):
        authenticate()
        response = create_product()

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_data_is_invalid_returns_400(self, create_product, authenticate):
        authenticate(is_staff=True)
        response = create_product(bad_request=True)

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_if_data_is_valid_returns_201(self, create_product, authenticate):
        authenticate(is_staff=True)
        response = create_product()

        assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
class TestRetrieveProduct:
    def test_if_dont_exist_returns_400(Self, api_client):
        fake_id = 1
        response = api_client.get(f"/store/products/{fake_id}/")

        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_if_product_exists_returns_200(self, api_client):
        product = baker.make(Product)

        response = api_client.get(f"/store/products/{product.id}/")

        assert response.status_code == status.HTTP_200_OK
