from datetime import datetime


def parse_date(date: str) -> datetime:
    return datetime.strptime(date, "%Y-%m-%d")

CodigosEstadosIbge = {
    'ro' : 11,
    'ac' : 12,
    'am' : 13,
    'rr' : 14,
    'pa' : 15,
    'ap' : 16,
    'to' : 17,
    'ma' : 21,
    'pi' : 22,
    'ce' : 23,
    'rn' : 24,
    'pb' : 25,
    'pe' : 26,
    'al' : 27,
    'se' : 28,
    'ba' : 29,
    'mg' : 31,
    'es' : 32,
    'rj' : 33,
    'sp' : 35,
    'pr' : 41,
    'sc' : 42,
    'rs' : 43,
    'ms' : 50,
    'mt' : 51,
    'go' : 52,
    'df' : 53
}


feriados_estaduais = {
    'ac': [
        ['23 de janeiro', 'Dia do evangélico'],
        ['08 de março', 'Alusivo ao Dia Internacional da Mulher'],
        ['15 de junho', 'Aniversário do estado (Data Magna)'],
        ['5 de setembro', 'Dia da Amazônia'],
        ['17 de novembro', 'Assinatura do Tratado de Petrópolis']
    ],
    'al': [
        ['24 de junho', 'São João'],
        ['29 de junho', 'São Pedro'],
        ['16 de setembro', 'Emancipação política (Data Magna)']
    ],
    'ap': [
        ['19 de março', 'Dia de São José, santo padroeiro do Estado do Amapá'],
        ['13 de setembro', 'Criação do Território Federal (data magna)']
    ],
    'am': [
        ['5 de setembro', 'Dia não especificado'],
        ['8 de dezembro', 'Dia não especificado']
    ],
    'ba': [
        ['2 de julho', 'Independência da Bahia (Data Magna)']
    ],
    'ce': [
        ['19 de março', 'Dia de São José (Padroeiro do Ceará)'],
        ['25 de março', 'Abolição da escravidão no Ceará (data magna)'],
        ['15 de agosto', 'Dia de Nossa Senhora da Assunção (Padroeira de Fortaleza)']
    ],
    'df': [
        ['21 de abril', 'Fundação de Brasília (Data Magna)'],
        ['30 de novembro', 'Dia do evangélico']
    ],
    'es': [
        ['Segunda-Feira, Oitavo Dia Após o Domingo de Páscoa', 'Dia de Nossa Senhora da Penha, padroeira do estado (data magna)']
    ],
    'go': [
        ['24 de maio', 'Dia da Nossa Senhora Auxiliadora (Padroeira de Goiânia)'],
        ['26 de julho', 'Dia da Nossa Senhora de Sant\'Anna (Padroeira de Goiás)'],
        ['24 de outubro', 'Pedra fundamental de Goiânia (Data Magna)']
    ],
    'ma': [
        ['28 de julho', 'Adesão do Maranhão à independência do Brasil (Data Magna)']
    ],
    'ms': [
        ['11 de outubro', 'Criação do estado (Data Magna)']
    ],
    'mg': [
        ['21 de abril', 'Execução de Tiradentes (Data Magna)']
    ],
    'pa': [
        ['15 de agosto', 'Adesão do Pará à independência do Brasil (Data Magna)']
    ],
    'pb': [
        ['5 de agosto', 'Fundação do Estado em 1585 e dia da sua padroeira, Nossa Senhora das Neves (Data Magna)']
    ],
    'pr': [
        ['15 de novembro', 'Dia de Nossa Senhora do Rocio, padroeira do estado'],
        ['19 de dezembro', 'Emancipação política do estado do Paraná (Data Magna)']
    ],
    'pe': [
        ['6 de março', 'Revolução Pernambucana de 1817 (Data Magna)'],
        ['24 de junho', 'Festa de São João (Festa Junina)']
    ],
    'pi': [
        ['19 de outubro', 'Dia do Piauí (Data Magna)']
    ],
    'rj': [
        ['Terça de Carnaval', 'Carnaval'],
        ['23 de abril', 'Dia de São Jorge']
    ],
    'rn': [
        ['7 de agosto', 'Dia do Rio Grande do Norte'],
        ['3 de outubro', 'Mártires de Cunhaú e Uruaçu (data magna)']
    ],
    'rs': [
        ['20 de setembro', 'Dia do Gaúcho (Data Magna)']
    ],
    'ro': [
        ['4 de janeiro', 'Criação do estado (Data Magna)'],
        ['18 de junho', 'Dia do evangélico']
    ],
    'rr': [
        ['5 de outubro', 'Criação do estado (Data Magna)']
    ],
    'sc': [
        ['11 de agosto', 'Dia de Santa Catarina (criação da capitania, separando-se de São Paulo) (Data Magna)'],
        ['25 de novembro', 'Dia de Santa Catarina de Alexandria']
    ],
    'sp': [
        ['9 de julho', 'Revolução Constitucionalista de 1932 (Data Magna)']
    ],
    'se': [
        ['8 de julho', 'Emancipação política de Sergipe (Data Magna)']
    ],
    'to': [
        ['5 de outubro', 'Criação do estado (Data Magna)'],
        ['18 de março', 'Autonomia do Estado (criação da Comarca do Norte)'],
        ['8 de setembro', 'Padroeira do Estado (Nossa Senhora da Natividade)']
    ]
}
