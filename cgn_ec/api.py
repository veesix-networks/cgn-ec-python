from httpx import Client, Response, Auth

from cgn_ec.models import (
    NATSessionMapping,
    NATAddressMapping,
    NATPortMapping,
    NATPortBlockMapping,
)


class API:
    def __init__(
        self,
        url: str,
        api_key: str,
        api_key_header: str = "x-api-key",
        client: Client = None,
        timeout: int = 10,
    ) -> None:
        self.url = url
        self.api_key_header = api_key_header
        self.auth = APIKeyAuth(self.api_key_header, api_key)
        self.timeout = timeout
        self.client = (
            client
            if client
            else Client(auth=self.auth, base_url=self.url, timeout=self.timeout)
        )
        self.version = "v1"

    def get(self, endpoint: str, **kwargs) -> Response:
        """GET HTTP Operation."""
        response = self.client.get(
            url=endpoint,
            **kwargs,
        )

        response.raise_for_status()
        return response

    def post(self, endpoint: str, data: dict = {}, **kwargs) -> Response:
        """POST HTTP Operation."""
        response = self.client.post(
            url=endpoint,
            json=data,
            **kwargs,
        )

        response.raise_for_status()
        return response

    def delete(self, endpoint: str, **kwargs) -> Response:
        """DELETE HTTP Operation."""
        response = self.client.delete(
            url=endpoint,
            **kwargs,
        )

        response.raise_for_status()
        return response

    def patch(self, endpoint: str, data: dict = {}, **kwargs) -> Response:
        """PATCH HTTP Operation."""
        response = self.client.patch(
            url=endpoint,
            json=data,
            **kwargs,
        )

        response.raise_for_status()
        return response

    def put(self, endpoint: str, data: dict | str = {}, **kwargs) -> Response:
        """PUT HTTP Operation."""
        response = self.client.put(
            url=endpoint,
            headers=self.headers,
            json=data if isinstance(data, (dict, list)) else None,
            data=data if isinstance(data, str) else None,
            timeout=self.timeout,
            **kwargs,
        )

        response.raise_for_status()
        return response

    def get_session_mappings(
        self,
        x_ip: str = "",
        x_port: str = "",
        timestamp_gt: str = "",
        timestamp_lt: str = "",
        **kwargs,
    ) -> list[NATSessionMapping]:
        params = {
            "x_ip": x_ip,
            "x_port": x_port,
            "timestamp_gt": timestamp_gt,
            "timestamp_lt": timestamp_lt,
            **kwargs,
        }

        mappings = self.get(
            f"/{self.version}/session_mappings/", params=self._build_params(**params)
        )
        return [NATSessionMapping(**data) for data in mappings.json()]

    def get_address_mapping(
        self, x_ip: str = "", timestamp_gt: str = "", timestamp_lt: str = "", **kwargs
    ) -> list[NATAddressMapping]:
        params = {
            "x_ip": x_ip,
            "timestamp_gt": timestamp_gt,
            "timestamp_lt": timestamp_lt,
            **kwargs,
        }

        mappings = self.get(
            f"/{self.version}/address_mappings/", params=self._build_params(**params)
        )
        return [NATAddressMapping(**data) for data in mappings.json()]

    def get_port_mapping(
        self,
        x_ip: str = "",
        x_port: int = None,
        timestamp_gt: str = None,
        timestamp_lt: str = None,
        **kwargs,
    ) -> list[NATPortMapping]:
        params = {
            "x_ip": x_ip,
            "x_port": x_port,
            "timestamp_gt": timestamp_gt,
            "timestamp_lt": timestamp_lt,
            **kwargs,
        }

        mappings = self.get(
            f"/{self.version}/port_mappings/", params=self._build_params(**params)
        )
        return [NATPortMapping(**data) for data in mappings.json()]

    def get_port_block_mapping(
        self,
        x_ip: str = "",
        start_port: int = None,
        end_port: int = None,
        timestamp_gt: str = None,
        timestamp_lt: str = None,
        **kwargs,
    ) -> list[NATPortBlockMapping]:
        params = {
            "x_ip": x_ip,
            "start_port": start_port,
            "end_port": end_port,
            "timestamp_gt": timestamp_gt,
            "timestamp_lt": timestamp_lt,
            **kwargs,
        }

        mappings = self.get(
            f"/{self.version}/port_block_mappings/", params=self._build_params(**params)
        )
        return [NATPortBlockMapping(**data) for data in mappings.json()]

    def _build_params(self, **kwargs):
        params = {}
        for k, v in kwargs.items():
            if v is None or v == "":
                continue

            params[k] = v
        return params


class APIKeyAuth(Auth):
    def __init__(self, api_key_header: str, api_key: str):
        self.api_key_header = api_key_header
        self.api_key = api_key

    def auth_flow(self, request):
        request.headers[self.api_key_header] = self.api_key
        yield request
