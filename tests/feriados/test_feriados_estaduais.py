from unittest import mock
import pytest
from brasilapy import BrasilAPI
from brasilapy.models.general import Feriado
from brasilapy.processor import RequestsProcessor


class TestFeriadosEstaduais:
    def test_get_feriados_estaduais_with_invalid_uf(self, brasil_api: BrasilAPI):
        # Simula uma exceção quando uma UF inválida é passada
        with mock.patch(
            "brasilapy.client.RequestsProcessor.get_feriados_estaduais",
            side_effect=TypeError("A UF não existe")
        ), pytest.raises(TypeError):
            brasil_api.get_feriados_estaduais("xx")

    def test_get_feriados_estaduais_valid_uf(self, brasil_api: BrasilAPI):
        # Dados simulados de feriados estaduais
        mock_feriados_estaduais = [
            ["23 de janeiro", "Dia do evangélico"],
            ["08 de março", "Alusivo ao Dia Internacional da Mulher"]
        ]

        with mock.patch(
            "brasilapy.client.RequestsProcessor.get_feriados_estaduais",
            return_value=mock_feriados_estaduais,
        ) as get_data_mock:

            # Chama o método com uma UF válida (Acre - "ac")
            feriados = brasil_api.get_feriados_estaduais("ac")

            # Verifica se a função foi chamada uma vez
            get_data_mock.assert_called_once()

            # Converte o mock para a estrutura de Feriado
            expected_feriado = Feriado(data="23 de janeiro", descricao="Dia do evangélico")
            assert feriados[0].dict() == expected_feriado.dict()

            # Verifica o tipo do objeto retornado
            assert isinstance(feriados[0], Feriado)

    def test_get_feriados_estaduais_empty(self, brasil_api: BrasilAPI):
        # Simula o retorno vazio para um estado sem feriados
        with mock.patch(
            "brasilapy.client.RequestsProcessor.get_feriados_estaduais",
            return_value=[]
        ) as get_data_mock:
            feriados = brasil_api.get_feriados_estaduais("sp")
            get_data_mock.assert_called_once()
            assert len(feriados) == 0  # Verifica que não há feriados

    def test_get_feriados_estaduais_no_uf(self):
        requests_processor = RequestsProcessor()
        with pytest.raises(TypeError, match="A UF must be defined"):
            requests_processor.get_feriados_estaduais(None)

    def test_get_feriados_estaduais_invalid_uf(self):
        requests_processor = RequestsProcessor()
        with pytest.raises(TypeError, match="A UF não existe"):
            requests_processor.get_feriados_estaduais("xx")  # UF inválida
