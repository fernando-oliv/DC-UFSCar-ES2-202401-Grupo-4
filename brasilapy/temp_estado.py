class RequestsProcessor(ClientProcessor):

    handler: RequestSession = RequestSession()
    base_url = "https://brasilapi.com.br/api"

    def get_data(self, endpoint: str, params: dict | None = None) -> dict:
        response: requests.Response = self.handler.get(
            f"{self.base_url}{endpoint}", params=params
        )

        if response.status_code == 200:
            return response.json()
        else:
            raise ProcessorException(
                status_code=response.status_code, response_text=response.text
            )
