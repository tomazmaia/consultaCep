from src.cabecalho import Cabecalho #view.consultaCep
from src.consulta import ConsultaCep #view.consultaCep
#from cabecalho import Cabecalho  #src.main
#from consulta import ConsultaCep #src.main

logo = Cabecalho()
print(logo.head + '\n' + logo.head)
print(logo.logo)
print(logo.head + '\n' + logo.head)

verificarCep = ConsultaCep()
verificarCep.tratar_cep(input('Informar o CEP: '))

