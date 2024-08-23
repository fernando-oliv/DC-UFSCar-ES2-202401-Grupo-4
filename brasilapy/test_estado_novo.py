from .client import BrasilAPI

conector = BrasilAPI()

sp = conector.get_ibge_estado('df')
print(sp)
#teste_cnpj = conector.get_cnpj('11111000002222')
#print(teste_cnpj)