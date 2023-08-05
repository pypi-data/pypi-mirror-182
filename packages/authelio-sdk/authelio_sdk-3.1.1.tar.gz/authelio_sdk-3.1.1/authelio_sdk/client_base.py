from typing import Optional, Any, Dict

import urllib3
from b_lambda_layer_common.util.http_endpoint import HttpEndpoint

from authelio_sdk.config import Config


class ClientBase:
    def __init__(
            self,
            api_key: str,
            api_secret: str,
            config: Config
    ) -> None:
        self.api_key = api_key
        self.api_secret = api_secret
        self.config = config

    @property
    def basic_auth_header(self) -> Dict[str, str]:
        return urllib3.make_headers(basic_auth=f'{self.api_key}:{self.api_secret}')

    def http_endpoint(
            self,
            path: str,
            method: str = 'GET',
            body: Any = None,
            fields: Optional[Any] = None
    ) -> HttpEndpoint:
        """
        Calls endpoint with given HTTP method and path.

        :param path: Path to append to domain name of the API.
        :param method: HTTP method, e.g. POST, GET, etc.
        :param body: Body of an HTTP request.
        :param fields: HTTP query parameters.

        :return: HTTP response object.
        """
        return HttpEndpoint(
            endpoint_url=f'{self.config.public_api_url}{path}',
            method=method,
            body=body,
            fields=fields,
            headers=self.basic_auth_header
        )
