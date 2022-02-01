import requests

class ConsultaCep:

    def tratar_cep(self,codigo):
        self.codigo = codigo
        if len(self.codigo) == 8 and self.codigo.isnumeric():
            self.request = requests.get('https://viacep.com.br/ws/{}/json/'.format(self.codigo))

            def filtro(self):
                data = self.request.json()
                naoEncontrado = "CEP Não localizado"
                caracteres = "{}"
                if "erro" not in data:
                    result = []
                    for dict in data.keys():
                        chave = dict
                        result.append(chave.upper() + ': ' + data[dict] + '\n')
                    print(result)
                    result = ''.join(x for x in result if x not in caracteres)
                    return result
                else:
                    return naoEncontrado

            resultadoFiltro = filtro(self)

            return resultadoFiltro

        else:
            erro = "Digitos inválidos, favor verificar"
            return erro

