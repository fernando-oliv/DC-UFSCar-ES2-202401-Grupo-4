from datetime import date

from .general import BaseReturnModel


class CNAE(BaseReturnModel):
    codigo: int
    descricao: str


class SocioAdmin(BaseReturnModel):
    pais: str or None
    nome_socio: str
    codigo_pais: str or None
    faixa_etaria: str
    cnpj_cpf_do_socio: str  # with a filter
    qualificacao_socio: str
    codigo_faixa_etaria: int
    data_entrada_sociedade: date
    identificador_de_socio: int
    cpf_representante_legal: str
    nome_representante_legal: str
    codigo_qualificacao_socio: int
    qualificacao_representante_legal: str
    codigo_qualificacao_representante_legal: int


class CNPJ(BaseReturnModel):
    uf: str
    cep: str
    qsa: list
    cnpj: str
    pais: str or None
    email: str or None
    porte: str
    bairro: str
    numero: str
    ddd_fax: str
    municipio: str
    logradouro: str
    cnae_fiscal: int
    codigo_pais: int or None
    complemento: str
    codigo_porte: int
    razao_social: str
    nome_fantasia: str
    capital_social: int
    ddd_telefone_1: str
    ddd_telefone_2: str
    opcao_pelo_mei: bool or None
    descricao_porte: str
    codigo_municipio: int
    cnaes_secundarios: list
    natureza_juridica: str
    situacao_especial: str
    opcao_pelo_simples: bool or None
    situacao_cadastral: int
    data_opcao_pelo_mei: date or None
    data_exclusao_do_mei: date or None
    cnae_fiscal_descricao: str
    codigo_municipio_ibge: int
    data_inicio_atividade: date or None
    data_situacao_especial: str or None
    data_opcao_pelo_simples: date or None
    data_situacao_cadastral: date or None
    nome_cidade_no_exterior: str
    codigo_natureza_juridica: int
    data_exclusao_do_simples: date or None
    motivo_situacao_cadastral: int
    ente_federativo_responsavel: str
    identificador_matriz_filial: int
    qualificacao_do_responsavel: int
    descricao_situacao_cadastral: str
    descricao_tipo_de_logradouro: str
    descricao_motivo_situacao_cadastral: str
    descricao_identificador_matriz_filial: str
