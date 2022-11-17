import re
from flask import render_template, request, redirect 
from flask import flash, send_from_directory, session
from flask.helpers import url_for
import json
from decimal import Decimal
from datetime import date

from models import Carro, Proprietario
from DaoProprietario import ProprietarioDao
from DaoCarro import CarroDao

from run import app, db

proprietario_dao = ProprietarioDao(db)
carro_dao = CarroDao(db)

class CustomJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        if isinstance(obj, date):                    
            return str(obj)
        return super(CustomJsonEncoder, self).default(obj)

@app.route('/')
def index():
    lista_props = proprietario_dao.listar_todos_proprietarios()    
    return render_template('cad_prop_veiculo.html', proprietarios=lista_props)

@app.route('/buscarproprietario', methods=['POST'])
def buscar_proprietario():
    id_proprietario = request.form.get('id_proprietario')
    
    try:
        if id_proprietario is None or id_proprietario == '0':
            raise ValueError('ID do Proprietário não informado!','error') 
    except ValueError as error:
        flash('Erro ao tentar buscar as informações do Proprietário!','error')
        flash(f'Erro.: {error}','error')
        return redirect(url_for('index')) 

    try:                                                        
        proprietario = proprietario_dao.busca_proprietario(id_proprietario)
                    
        if proprietario != None:            
            ret_prop = proprietario.__dict__()        
        else:               
            ret_prop = {"retorno": 99, "descricao":"select sem retorno"}
         
        retorno = app.response_class(
            response = json.dumps(ret_prop, indent=4, ensure_ascii=False, 
                                  cls=CustomJsonEncoder),
            status=200,
            mimetype='application/json'
        )       
        return retorno        
    except Exception as error:
        flash('Erro ao buscar as informações do Proprietário!','error')
        flash(f'Erro.: {error}','error')
        return redirect(url_for('index'))

@app.route('/gravarproprietario', methods=['POST'])
def gravar_proprietario():  
    id_prop = request.form.get('codProprietario') or None
    nome = request.form.get('nome') or None 
    situacao = request.form.get('SitProp') or None 
    logradouro = request.form.get('logradouro') or None
    numero = request.form.get('numero') or None
    telefone = request.form.get('telefone') or None 

    try:         
        if nome == None:
            raise ValueError('O Nome precisa ser informado!','error') 

        if situacao == None:
            raise ValueError('A Situação precisa ser informada!','error') 

        if logradouro == None:
            raise ValueError('O Logradouro precisa ser informado!','error') 

        if numero == None:
            raise ValueError('O Número precisa ser informado!','error') 

        if telefone == None:
            raise ValueError('O Número precisa ser informado!','error')                                                                  
    except ValueError as error:
        flash('Erro ao tentar Salvar/Deletar o registro!','error')
        flash(f'Erro.: {error}','error')
        return redirect(url_for('index')) 

    try:       
        if request.form.get('btnExcluirProp'):                      
            proprietario_dao.deletar(id_prop)
            flash('O proprietário foi excluído com sucesso!','success')            
        else:                                                             
            proprietario = Proprietario(nome, logradouro, numero, telefone, 
                                        None, situacao, None, id_prop=id_prop) 

            proprietario = proprietario_dao.salvar(proprietario) 
            flash('O proprietário foi salvo com sucesso!','success')        
    except Exception as error:
        flash('Erro ao tentar Salvar/Deletar o registro!','error')
        flash(f'Erro.: {error}','error')        
         
    return redirect(url_for('index'))


@app.route('/buscarveiculo', methods=['POST'])
def buscar_veiculo():
    id_prop    = request.form.get('id_proprietario')
    id_veiculo = request.form.get('id_veiculo')
    
    try:
        if id_veiculo is None or id_veiculo == '0':
            raise ValueError('ID do Veículo não informado!','error') 
    except ValueError as error:
        flash('Erro ao tentar buscar as informações do Veículo!','error')
        flash(f'Erro.: {error}','error')
        return redirect(url_for('index')) 

    try:                                                        
        carro = carro_dao.busca_veiculo_prop(id_prop, id_veiculo)
                    
        if carro != None:            
            ret_prop = carro.__dict__()        
        else:               
            ret_prop = {"retorno": 99, "descricao":"select sem retorno"}
         
        retorno = app.response_class(
            response = json.dumps(ret_prop, indent=4, ensure_ascii=False, 
                                  cls=CustomJsonEncoder),
            status=200,
            mimetype='application/json'
        )       
        return retorno        
    except Exception as error:
        flash('Erro ao buscar as informações do Proprietário!','error')
        flash(f'Erro.: {error}','error')
        return redirect(url_for('index'))

@app.route('/buscartodosveiculosprop', methods=['POST'])
def buscar_todos_veiculos_prop():
    id_prop = request.form.get('id_proprietario')   
    
    try:
        if id_prop is None or id_prop == '0':
            raise ValueError('ID do Proprietário não informado!','error') 
    except ValueError as error:
        flash('Erro ao tentar buscar as informações do Proprietário!','error')
        flash(f'Erro.: {error}','error')
        return redirect(url_for('index')) 

    try:                                                                
        carros = carro_dao.listar_todos_veiculos_prop(id_prop)
                   
        if carros != None:            
            ret_carros = carros       
        else:               
            ret_carros = {"retorno": 99, "descricao":"select sem retorno"}
                 
        retorno = app.response_class(
            response = json.dumps(ret_carros, indent=4, ensure_ascii=False, 
                                  cls=CustomJsonEncoder),
            status=200,
            mimetype='application/json'
        )       
        return retorno      
    except Exception as error:
        flash('Erro ao buscar as informações do Proprietário!','error')
        flash(f'Erro.: {error}','error')
        return redirect(url_for('index'))
               
@app.route('/gravarexcluirveiculo', methods=['POST'])
def gravar_veiculo():         
    id_proprietario = request.form.get('id_proprietario') 
    id_carro = request.form.get('id_carro') or None
    placa = request.form.get('placa') or None
    descricao = request.form.get('descricao') or None
    modelo = request.form.get('modelo') or None
    cor = request.form.get('cor') or None
    situacao = request.form.get('situacao') or None
    metodo = request.form.get('metodo')

    try:         
        if placa == None:
            raise ValueError('A Placa precisa ser informada!','error') 

        if descricao == None:
            raise ValueError('A Descrição precisa ser informada!','error') 

        if modelo == None:
            raise ValueError('O Modelo precisa ser informado!','error') 

        if cor == None:
            raise ValueError('A Cor precisa ser informada!','error') 

        if situacao == None:
            raise ValueError('A Situação precisa ser informada!','error')                                                                  
    except ValueError as error:
        flash('Erro ao tentar Salvar/Deletar o registro!','error')
        flash(f'Erro.: {error}','error')
        return redirect(url_for('index'))

    try:       
        if metodo == 'excluir':                      
            carro_dao.deletar(id_proprietario, id_carro)  
            proprietario_dao.retira_qtde_veiculos(id_proprietario)          
        else:                                                             
            carro = Carro(id_proprietario, placa, descricao, modelo, 
                          cor, situacao, id_carro=id_carro) 
                                  
            carro = carro_dao.salvar(carro)  
            if id_carro == None:                       
                proprietario_dao.adiciona_qtde_veiculos(id_proprietario)                    
    except Exception as error:
        flash('Erro ao tentar Salvar/Deletar o registro!','error')
        flash(f'Erro.: {error}','error')        
         
    return buscar_todos_veiculos_prop()  
                            

       