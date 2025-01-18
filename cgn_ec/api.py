from requests import Session, Response

class API:
    def __init__(self, url: str, token: str, session: Session = None, timeout: int = 10) -> None:
        self.url = url
        self.token = token
        self.headers = {"x-api-token": token}
        self.session = session if session else Session()
        self.timeout = timeout


    def get(self, endpoint: str, **kwargs) -> Response:
        """GET HTTP Operation."""
        response = self.session.get(
            url=self.url + endpoint,
            timeout=self.timeout,
            **kwargs,
        )
        return response

    def post(self, endpoint: str, data: dict = {}, **kwargs) -> Response:
        """POST HTTP Operation."""
        response = self.session.post(
            url=self.url + endpoint,
            json=data,
            timeout=self.timeout,
            **kwargs,
        )
        return response

    def delete(self, endpoint: str, **kwargs) -> Response:
        """DELETE HTTP Operation."""
        response = self.session.delete(
            url=self.url + endpoint,
            timeout=self.timeout,
            **kwargs,
        )
        return response

    def patch(self, endpoint: str, data: dict = {}, **kwargs) -> Response:
        """PATCH HTTP Operation."""
        response = self.session.patch(
            url=self.url + endpoint,
            json=data,
            timeout=self.timeout,
            **kwargs,
        )
        return response

    def put(self, endpoint: str, data: dict | str = {}, **kwargs) -> Response:
        """PUT HTTP Operation."""
        response = self.session.put(
            url=self.url + endpoint,
            json=data if isinstance(data, (dict, list)) else None,
            data=data if isinstance(data, str) else None,
            timeout=self.timeout,
            **kwargs,
        )
        return response
    
    def get_session_mapping(self) -> None:
        raise NotImplementedError
    
    def get_address_mapping(self) -> None:
        raise NotImplementedError
    
    def get_port_mapping(self) -> None:
        raise NotImplementedError
    
    def get_port_block_mapping(self) -> None:
        raise NotImplementedError