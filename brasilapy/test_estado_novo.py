from client import BrasilAPI
from utils import feriados_estaduais

conector = BrasilAPI()

ac = conector.get_feriados_estaduais('ac')
print(ac)
#teste_cnpj = conector.get_cnpj('11111000002222')
#print(teste_cnpj)
