from models import Proprietario

SQL_CRIA_PROPRIETARIO = """INSERT into 
                           carford.tbproprietario(id_proprietario, nome,  
                                                  logradouro, numero, telefone, 
                                                  possui_carro, situacao,
                                                  qtde_carros)
                           values(%s, %s,   
                                  %s, %s, %s,
                                  %s, %s,
                                  %s)               
                        """



SQL_ATLZ_PROPRIETARIO = """UPDATE carford.tbproprietario P
                           SET P.nome = %s, P.logradouro = %s, P.numero = %s, 
                               P.telefone = %s, P.situacao = %s
                           WHERE P.id_proprietario = %s 
                        """
SQL_DELETA_PROPRIETARIO = """DELETE
                             FROM carford.tbproprietario P
                             WHERE P.id_proprietario = %(id_prop)s
                          """                        

SQL_ADICIONA_VEICULOS = """UPDATE carford.tbproprietario P
                           SET P.qtde_carros = qtde_carros + 1,
                               P.possui_carro = 'S'
                           WHERE P.id_proprietario = %(id_prop)s                                  
                        """

SQL_RETIRA_VEICULOS = """UPDATE carford.tbproprietario P
                         SET P.qtde_carros = qtde_carros - 1
                         WHERE P.id_proprietario = %(id_prop)s                                  
                      """

SQL_BUSCA_QTDE_VEICULOS = """SELECT P.qtde_carros
                             FROM carford.tbproprietario P 
                             WHERE P.id_proprietario = %(id_prop)s                          
                          """

SQL_ALTERA_POSSUI_CARRO = """UPDATE carford.tbproprietario P
                             SET P.possui_carro = 'N'
                             WHERE P.id_proprietario = %(id_prop)s
                          """

SQL_BUSCA_PROPRIETARIO = """SELECT P.id_proprietario, P.nome, P.logradouro, 
                                   P.numero, P.telefone, P.possui_carro,
                                   P.situacao, P.qtde_carros
                            FROM carford.tbproprietario P 
                            WHERE P.id_proprietario = %(id_prop)s                                                               
                         """
                         
SQL_BUSCA_TODOS_PROPRIETARIO = """SELECT P.id_proprietario, P.nome, 
                                         P.logradouro, P.numero, P.telefone, 
                                         P.possui_carro, P.situacao, 
                                         P.qtde_carros
                                  FROM carford.tbproprietario P                                    
                                """

class ProprietarioDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, prop):
        cursor = self.__db.cursor()
              
        if prop.id_proprietario:                              
            cursor.execute(SQL_ATLZ_PROPRIETARIO, (prop.nome, prop.logradouro,
                                                   prop.numero, prop.telefone,
                                                   prop.situacao, 
                                                   prop.id_proprietario,))
        else:            
            cursor.execute(SQL_CRIA_PROPRIETARIO,(prop.id_proprietario,
                                                  prop.nome, prop.logradouro,
                                                  prop.numero, prop.telefone,
                                                  'N', prop.situacao, 0))
            prop.id_proprietario = cursor.lastrowid                                              
        self.__db.commit()
        return prop

    def deletar(self, id_proprietario):            
        cursor = self.__db.cursor()
        cursor.execute(SQL_DELETA_PROPRIETARIO,{'id_prop': id_proprietario})
        self.__db.commit() 

    def adiciona_qtde_veiculos(self, id_proprietario):
        cursor = self.__db.cursor()
        cursor.execute(SQL_ADICIONA_VEICULOS,{'id_prop': id_proprietario})
        self.__db.commit()

    def retira_qtde_veiculos(self, id_proprietario):
        cursor = self.__db.cursor()
        cursor.execute(SQL_RETIRA_VEICULOS,{'id_prop': id_proprietario})
        self.__db.commit() 

        qtde_carros = self.busca_qtde_veiculos(id_proprietario)
        if qtde_carros == 0:
            self.altera_possui_carro(id_proprietario)     

    def busca_qtde_veiculos(self, id_proprietario):       
        cursor = self.__db.cursor()        
        cursor.execute(SQL_BUSCA_QTDE_VEICULOS, {'id_prop': id_proprietario}) 
        
        ret = cursor.fetchone()        
        if ret:                        
            qtde_veiculos = ret[0]                                                                                                                                                          
            return qtde_veiculos
        else:
            return None  

    def altera_possui_carro(self, id_proprietario):
        cursor = self.__db.cursor()
        cursor.execute(SQL_ALTERA_POSSUI_CARRO,{'id_prop': id_proprietario})
        self.__db.commit()           

    def listar_todos_proprietarios(self):
        cursor = self.__db.cursor()
        cursor.execute(SQL_BUSCA_TODOS_PROPRIETARIO)
        props = converte_db_proprietarios(cursor.fetchall())
        return props

    def busca_proprietario(self, id_proprietario):       
        cursor = self.__db.cursor()        

        cursor.execute(SQL_BUSCA_PROPRIETARIO, {'id_prop': id_proprietario}) 
        
        ret = cursor.fetchone()        
        if ret:                        
            id_prop  = ret[0]                      
            prop = Proprietario(ret[1], ret[2], ret[3], ret[4], 
                                ret[5], ret[6], ret[7], id_prop=id_prop)
                                                                                                                        
            return prop
        else:
            return None 

def converte_db_proprietarios(prop):
    def cria_proprietarios(vlr):
        id_prop  = vlr[0]                      
        return Proprietario(vlr[1], vlr[2], vlr[3], vlr[4], 
                            vlr[5], vlr[6], vlr[7], id_prop=id_prop)
                                    
    resultado = map(cria_proprietarios, prop)
    return list(resultado)

