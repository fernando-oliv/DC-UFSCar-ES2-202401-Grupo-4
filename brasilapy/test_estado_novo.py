from client import BrasilAPI

conector = BrasilAPI()

sp = conector.get_ibge_estado('sp')
print(sp)