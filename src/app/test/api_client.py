from django.utils.functional import cached_property
from rest_framework.test import APIClient


class AppTestClient:
    @cached_property
    def api_client(self) -> APIClient:
        return APIClient()

    def get(self, *args, expected_status_code=200, **kwargs):
        result = self.api_client.get(*args, **kwargs)

        assert result.status_code == 200

        return result.json()
