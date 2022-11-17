
function carrega_veiculo() {
    var myForm = document.querySelector("#formCadastroVeiculo");             
    var codprop = myForm.descProprietario.value;    
    var encontrou_prop = false;   

    encontrou_prop = consulta_cod_proprietario_banco(myForm, codprop, 'D'); 
    
    busca_veiculos_prop(codprop);
}

function verifica_cod_veiculo() { 
    var myForm = document.querySelector("#formCadastroVeiculo");             
    var codProp = myForm.descProprietario.value;
    var codVeiculo = myForm.codVeiculo.value;
    var encontrou_veiculo = false; 
    var encontrou_prop = false;   
   
    codVeiculo = codVeiculo.toString();
    codVeiculo = codVeiculo.trim(); 
    
    $('#sit-prop').val("A");
    if (codVeiculo != "") {
        //$('#cod-proprietario').valid();
        //myForm.codProprietario.focus();
        consulta_cod_veiculo_banco(myForm, codProp, codVeiculo);        
    }                                                                                               
    habilita_campos(".hab-campos-veiculo");
    
    
    myForm.btnNovoVeiculo.disabled = true;
    myForm.codVeiculo.readOnly = true;
    myForm.bibPontosVeiculo.disabled = true;
    myForm.btnSalvarVeiculo.disabled = false;
    myForm.placa.focus();
}

function consulta_cod_veiculo_banco(form, id_proprietario, id_veiculo) {
    var dados = {
        id_proprietario: id_proprietario,
        id_veiculo: id_veiculo               
    }
    $.ajax({
        type: 'POST',
        url: '/buscarveiculo',
        data: dados,        
        dataType: 'text',
        error: function(ret){
            console.log(ret);
        },
        success: function(ret){                        
            var veiculo = JSON.parse(ret);

            if (!('retorno' in veiculo)){                                  
                form.codVeiculo.value = veiculo.id_carro;
                form.situacaoVeiculo.value = veiculo.situacao;
                             
                form.placa.value = veiculo.placa;
                form.descricaoVeiculo.value = veiculo.descricao;
                form.modeloVeiculo.value = veiculo.modelo
                form.corVeiculo.value = veiculo.cor; 

                document.querySelector('#btn-excluir-veiculo').disabled = false;                            
                $('select.select2').trigger('change');                                                                                    
            }                                                 
        }
    });    
}

function busca_veiculos_prop(id_proprietario) {
    var dados = {
        id_proprietario: id_proprietario           
    }   
    $.ajax({
        type: 'POST',                
        url: '/buscartodosveiculosprop',
        data: dados,
        dataType: 'text',
        error: function(ret){
            console.log(ret);
        },
        success: function(ret){            
            var veiculos = JSON.parse(ret);
            carrega_tabela_veiculos(veiculos); 
        }
    });
}

function carrega_tabela_veiculos(veiculos) {
    if (!('retorno' in veiculos)) {                
        var tableVeiculo = document.querySelector("#table-veiculo"); 
        var qtde_linhas = tableVeiculo.rows.length - 1; 

        for (var i=0; i < qtde_linhas; i++) {
            tableVeiculo.deleteRow(1);                    
        }
                                                                     
        var seq = 1;
        for (var veiculo of veiculos) {                                                      
            var linha = tableVeiculo.insertRow(seq);                   
            
            var cel1 = linha.insertCell(0);
            cel1.textContent = veiculo.id_carro;

            var cel2 = linha.insertCell(1);
            cel2.textContent =  veiculo.placa;

            var cel3 = linha.insertCell(2);
            cel3.textContent =  veiculo.descricao;

            var cel4 = linha.insertCell(3);
            cel4.textContent =  veiculo.modelo;

            var cel5 = linha.insertCell(4);
            cel5.textContent =  veiculo.cor;

            var cel6 = linha.insertCell(5);
            cel6.textContent =  veiculo.situacao;            
                               
            seq++;                                                                                                                     
        }                
    }
    else {
        //
    }
}