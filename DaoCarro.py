from models import Carro

SQL_CRIA_CARRO = """INSERT into 
                    carford.tbcarro(id_proprietario, id_carro, placa,
                                    descricao, modelo, cor, situacao)
                    values(%s, %s, %s,   
                           %s, %s, %s, %s)               
                 """

SQL_ATLZ_CARRO = """UPDATE carford.tbcarro C
                    SET C.descricao = %s, C.modelo = %s, 
                        C.cor = %s, C.situacao = %s
                    WHERE C.id_proprietario = %s AND
                          C.id_carro = %s
                 """

SQL_DELETA_CARRO = """DELETE
                      FROM carford.tbcarro C
                      WHERE C.id_proprietario = %(id_prop)s AND
                            C.id_carro = %(id_carro)s
                   """ 

SQL_DELETAR_CARROS_PROP = """DELETE
                             FROM carford.tbcarro C
                             WHERE C.id_proprietario = %(id_prop)s
                          """

SQL_VERIF_QTDE_CARRO = """SELECT COUNT(1)
                          FROM carford.tbcarro C
                          WHERE C.id_proprietario = %(id_prop)s                                 
                       """

SQL_BUSCA_CARRO = """SELECT C.id_proprietario, C.id_carro, C.placa,
                            C.descricao, C.modelo, C.cor, C.situacao
                     FROM carford.tbcarro C 
                     WHERE C.id_proprietario = %(id_prop)s AND
                           C.id_carro = %(id_carro)s                                                              
                  """

SQL_BUSCA_TODOS_CARRO = """SELECT C.id_proprietario, C.id_carro, C.placa,
                                  C.descricao, C.modelo, C.cor, C.situacao
                           FROM carford.tbcarro C 
                           WHERE C.id_proprietario = %(id_prop)s                                  
                        """

class CarroDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, carro):
        cursor = self.__db.cursor()
              
        if carro.id_carro:                              
            cursor.execute(SQL_ATLZ_CARRO, (carro.descricao, carro.modelo, 
                                            carro.cor, carro.situacao,
                                            carro.id_proprietario, 
                                            carro.id_carro,))                                                   
        else:            
            cursor.execute(SQL_CRIA_CARRO, (carro.id_proprietario, 
                                            carro.id_carro, carro.placa,
                                            carro.descricao, carro.modelo,
                                            carro.cor, carro.situacao,))              

            carro.id_carro = cursor.lastrowid                                              
        self.__db.commit()
        return carro

    def deletar(self, id_proprietario, id_carro):
        cursor = self.__db.cursor()
        cursor.execute(SQL_DELETA_CARRO,{'id_prop': id_proprietario,
                                         'id_carro': id_carro})
        self.__db.commit() 

    def deletar_veiculos_prop(self, id_proprietario):
        cursor = self.__db.cursor()
        cursor.execute(SQL_DELETAR_CARROS_PROP, {'id_prop': id_proprietario})
        self.__db.commit()    

    def verifica_qtde_veiculo_cadastrato(self, id_proprietario):
        cursor = self.__db.cursor()        
        cursor.execute(SQL_VERIF_QTDE_CARRO, {'id_prop': id_proprietario}) 
        
        ret = cursor.fetchone()        
        if ret:                                    
            qtde_veiculos = ret[0]                                                                                                                                     
            return qtde_veiculos
        else:
            return None 

    def listar_todos_veiculos_prop(self, id_proprietario):
        cursor = self.__db.cursor()
        cursor.execute(SQL_BUSCA_TODOS_CARRO,{'id_prop': id_proprietario})
        carros = converte_db_veiculos(cursor.fetchall())
        return carros

    def busca_veiculo_prop(self, id_proprietario, id_carro):       
        cursor = self.__db.cursor()        

        cursor.execute(SQL_BUSCA_CARRO, {'id_prop': id_proprietario,
                                         'id_carro': id_carro}) 
        
        ret = cursor.fetchone()        
        if ret:                                    
            id_prop  = ret[0] 
            id_carro = ret[1]                     
            carro = Carro(id_prop, ret[2], ret[3], ret[4], 
                          ret[5], ret[6], id_carro=id_carro)                    
                                                                                                                        
            return carro
        else:
            return None 

def converte_db_veiculos(carros):
    def cria_veiculos(vlr):
        id_prop  = vlr[0] 
        id_carro = vlr[1]                     
        
        carro = Carro(id_prop, vlr[2], vlr[3], vlr[4], 
                      vlr[5], vlr[6], id_carro=id_carro)
        return carro.__dict__()                         

    resultado = map(cria_veiculos, carros)
    return list(resultado)

