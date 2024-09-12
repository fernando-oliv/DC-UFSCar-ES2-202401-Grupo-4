from unittest import mock

import pytest

from brasilapy import BrasilAPI
from brasilapy.models.general import IbgeEstado, IbgeMunicipio


class TestIBGE:
    def test_get_ibge_municipios_invalid_payload(self, brasil_api: BrasilAPI):

        with pytest.raises(TypeError):
            brasil_api.get_ibge_municipios(state_uf=None)

        with pytest.raises(TypeError) as exc:
            brasil_api.get_ibge_municipios(state_uf="pb", providers=None)

        assert "A list of providers must be defined" in str(exc)

    def test_get_ibge_municipios(self, brasil_api: BrasilAPI, ibge_municipios_json):
        with mock.patch(
            "brasilapy.client.RequestsProcessor.get_data",
            return_value=ibge_municipios_json,
        ) as get_data_mock:

            ibge_municipios = brasil_api.get_ibge_municipios(state_uf="pb")

            get_data_mock.assert_called_once()

            assert ibge_municipios[0].dict() == ibge_municipios_json[0]
            assert type(ibge_municipios[0]) is IbgeMunicipio

    def test_get_ibge_estados_completo(self, brasil_api: BrasilAPI, ibge_estados_json):
        # Mock da resposta da API para os estados
        mock_ibge_estado = ibge_estados_json

        # Mock para área e densidade demográfica para um estado específico
        mock_area_consulta = [
            {
                "res": [
                    {
                        "res": {
                            "2022": "248209.426"  # Valor fictício da área em km2
                        }
                    }
                ]
            }
        ]

        mock_densidade_consulta = [
            {
                "res": [
                    {
                        "res": {
                            "2022": "93.5"  # Valor fictício da densidade demográfica
                        }
                    }
                ]
            }
        ]

        # Mock da primeira chamada para buscar todos os estados
        with mock.patch("brasilapy.client.RequestsProcessor.get_data", return_value=mock_ibge_estado):
            # Chama o método para buscar todos os estados
            ibge_estados = brasil_api.get_ibge_estados()

            # Agora, para cada estado, chamamos a API para buscar as informações detalhadas
            for estado in ibge_estados:
                # Mock para a chamada get_ibge_estado com base na sigla correta (em letras minúsculas)
                with mock.patch(
                    "brasilapy.client.RequestsProcessor.get_data",
                    side_effect=[mock_ibge_estado[0], mock_area_consulta, mock_densidade_consulta]  # Retorna detalhes para o estado específico
                ):
                    # Chama o método para buscar detalhes de um estado específico
                    estado_detalhado = brasil_api.get_ibge_estado(estado.sigla.lower())  # Usa a sigla em letras minúsculas

                    # Verifica se os valores foram corretamente atribuídos
                    assert estado_detalhado.area_km2 == 248209.426
                    assert estado_detalhado.densidade_demografica_por_km2 == 93.5




    def test_get_ibge_estado_with_invalid_state(self, brasil_api: BrasilAPI):
        with pytest.raises(TypeError) as exc:
            brasil_api.get_ibge_estado(state_uf=None)

        assert "A UF must be defined" in str(exc)

    def test_get_ibge_estado_with_a_defined_state(
        self, brasil_api: BrasilAPI, ibge_estados_json
    ):
        with mock.patch(
            "brasilapy.client.RequestsProcessor.get_data",
            return_value=ibge_estados_json[0],
        ):
            # Chama o método para buscar detalhes de um estado específico
            ibge_estado = brasil_api.get_ibge_estado("pb")

            # Compara os dicionários excluindo os campos opcionais que não estão no mock
            assert ibge_estado.dict(exclude={"area_km2", "densidade_demografica_por_km2"}) == ibge_estados_json[0]
            
           
            
            # Verifica se o tipo do retorno é IbgeEstado
            assert type(ibge_estado) is IbgeEstado
