from abc import ABC, abstractmethod

import requests
from requests import Session as RequestSession
from pydantic import BaseModel, ValidationError


from .exceptions import ProcessorException
from .utils import CodigosEstados


class ClientProcessor(ABC):

    handler: any
    base_url: str

    @abstractmethod
    def get_data(
        self,
        endpoint: str,
        queryset_params: dict[str, str] | list[dict[str, str]] | None = None,
    ) -> dict:
        raise NotImplementedError("A get_data method must be created")


class ProcessorException(Exception):
    def __init__(self, status_code: int, response_text: str):
        self.status_code = status_code
        self.response_text = response_text
        super().__init__(f"Error {status_code}: {response_text}")

class RequestSession:
    def get(self, url: str, params: dict | None = None) -> requests.Response:
        return requests.get(url, params=params)


class IbgeEstado(BaseModel):
    id: int
    nome: str
    sigla: str
    regiao: dict


class EstadoClima(BaseModel):
    temperature: float
    humidity: int
    description: str

class EstadoEconomia(BaseModel):
    gdp: float
    inflation: float


def parse_estado(ibge_estado_obj : IbgeEstado, area_consulta, densidade_demografica_consulta):
    EstadoGeral = {}
    estado_base = IbgeEstado.parse_obj(ibge_estado_obj)
    EstadoGeral['nome'] = estado_base.nome
    EstadoGeral['id'] = estado_base.id
    EstadoGeral['regiao'] = estado_base.regiao['nome']
    EstadoGeral['area_km2'] = float(area_consulta[0]['res'][0]['res']['2022'])
    EstadoGeral['densidade_demografica_por_km2'] = float(densidade_demografica_consulta[0]['res'][0]['res']['2022'])
    return EstadoGeral

class RequestsProcessor(ClientProcessor):
    handler: RequestSession = RequestSession()
    brasil_api_base_url = "https://brasilapi.com.br/api"
    openweather_api_base_url = "http://api.openweathermap.org/data/2.5/weather"
    bcb_api_base_url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs."
    openweather_api_key = "YOUR_API_KEY"
    area_ibge_estado_base_url = "https://servicodados.ibge.gov.br/api/v1/pesquisas/10102/indicadores/122230/resultados/"
    densidade_demografica_base_url = "https://servicodados.ibge.gov.br/api/v1/pesquisas/10102/indicadores/122231/resultados/"
    #é necessário acrescentar o id do estado no final, ex.: o de sp é 35

    def get_data(self, base_url: str, endpoint: str, params: dict | None = None) -> dict:
        response: requests.Response = self.handler.get(
            f"{base_url}{endpoint}", params=params
        )

        if response.status_code == 200:
            return response.json()
        else:
            raise ProcessorException(
                status_code=response.status_code, response_text=response.text
            )

    def get_ibge_estado(self, state_uf: str) -> IbgeEstado:
        if not state_uf:
            raise TypeError("A UF must be defined")
        if state_uf not in CodigosEstados:
            raise TypeError("A UF não existe")

        estado = self.get_data(self.brasil_api_base_url, f"/ibge/uf/v1/{state_uf}")
        area_consulta = self.get_data(self.area_ibge_estado_base_url, f"{CodigosEstados[state_uf]}")
        densidade = self.get_data(self.densidade_demografica_base_url, f"{CodigosEstados[state_uf]}")
        geral = parse_estado(estado, area_consulta, densidade)
    

        #return IbgeEstado.parse_obj(estado)
        return geral


    def get_estado_clima(self, state_name: str) -> EstadoClima:
        params = {
            "q": state_name,
            "appid": self.openweather_api_key,
            "units": "metric"
        }
        clima_data = self.get_data(self.openweather_api_base_url, "", params=params)
        return EstadoClima(
            temperature=clima_data['main']['temp'],
            humidity=clima_data['main']['humidity'],
            description=clima_data['weather'][0]['description']
        )

    def get_estado_economia(self, state_uf: str) -> EstadoEconomia:
        # Exemplo de endpoint para pegar o PIB de um estado específico
        # Vamos assumir que há um indicador de PIB (Produto Interno Bruto) para cada estado na API do Banco Central
        gdp_data = self.get_data(self.bcb_api_base_url, f"{state_uf}")
        # Vamos também assumir que a inflação está no mesmo endpoint ou em outro similar
        inflation_data = self.get_data(self.bcb_api_base_url, f"{state_uf}_inflation")
        return EstadoEconomia(
            gdp=gdp_data['valor'],
            inflation=inflation_data['valor']
        )