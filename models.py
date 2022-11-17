from datetime import datetime

class Proprietario:
    def __init__(self, nome, logradouro, numero, telefone, 
                       possui_carro, situacao, qtde_carros, id_prop=None):
        self._id_proprietario = id_prop
        self._nome = nome
        self._logradouro = logradouro
        self._numero = numero
        self._telefone = telefone
        self._possui_carro = possui_carro 
        self._situacao = situacao
        self._qtde_carros = qtde_carros

    def __dict__(self):
        retorno = {'id_proprietario': self.id_proprietario,
                   'nome':self.nome,
                   'logradouro':self.logradouro,
                   'numero':self.numero,
                   'telefone':self.telefone,
                   'possui_carro':self.possui_carro,
                   'situacao':self.situacao,
                   'qtde_carros': self.qtde_carros
                  }
        return retorno                                                    

    @property
    def id_proprietario(self):
        return self._id_proprietario

    @id_proprietario.setter 
    def id_proprietario(self, vlr):
        self._id_proprietario = vlr 

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, vlr):
        self._nome = vlr     

    @property
    def logradouro(self):
        return self._logradouro

    @logradouro.setter
    def logradouro(self, vlr):
        self._logradouro = vlr

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, vlr):
        self._numero = vlr 

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, vlr):
        self._telefone = vlr       
    
    @property
    def possui_carro(self):
        return self._possui_carro

    @possui_carro.setter
    def possui_carro(self, vlr):
        self._possui_carro = vlr

    @property
    def situacao(self):
        return self._situacao

    @situacao.setter
    def situacao(self, vlr):
        self._situacao = vlr 
    
    @property
    def qtde_carros(self):
        return self._qtde_carros

    @qtde_carros.setter
    def qtde_carros(self, vlr):
        self._qtde_carros = vlr 
        

class Carro:
    def __init__(self, id_proprietario, placa, descricao, modelo,
                       cor, situacao, id_carro=None):
        self._id_proprietario = id_proprietario
        self._id_carro = id_carro
        self._placa = placa 
        self._descricao = descricao
        self._modelo = modelo 
        self._cor = cor 
        self._situacao = situacao

    def __dict__(self):
        retorno = {'id_proprietario': self.id_proprietario,
                   'id_carro': self.id_carro,
                   'placa': self.placa, 
                   'descricao': self.descricao,
                   'modelo': self.modelo, 
                   'cor': self.cor, 
                   'situacao': self.situacao
                  }
        return retorno

    @property
    def id_proprietario(self):
        return self._id_proprietario

    @id_proprietario.setter 
    def id_proprietario(self, vlr):
        self._id_proprietario = vlr

    @property
    def id_carro(self):
        return self._id_carro

    @id_carro.setter 
    def id_carro(self, vlr):
        self._id_carro = vlr

    @property
    def placa(self):
        return self._placa

    @placa.setter 
    def placa(self, vlr):
        self._placa = vlr

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter 
    def descricao(self, vlr):
        self._descricao = vlr

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter 
    def modelo(self, vlr):
        self._modelo = vlr

    @property
    def cor(self):
        return self._cor

    @cor.setter 
    def cor(self, vlr):
        self._cor = vlr

    @property
    def situacao(self):
        return self._situacao

    @situacao.setter 
    def situacao(self, vlr):
        self._situacao = vlr                                                       

