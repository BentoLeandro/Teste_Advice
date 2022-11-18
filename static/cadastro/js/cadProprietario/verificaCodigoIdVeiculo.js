
function carrega_veiculo() {
    var myForm = document.querySelector("#formCadastroVeiculo");             
    var codProp = myForm.descProprietario.value;    
    var retorno = '';   

    retorno = consulta_cod_proprietario_banco(myForm, codProp, 'D'); 
        
    busca_veiculos_prop(codProp);
}

function verifica_cod_veiculo() { 
    var myForm = document.querySelector("#formCadastroVeiculo");             
    var codProp = myForm.descProprietario.value;    
    var codVeiculo = myForm.codVeiculo.value;
    var retorno = '';      
    
    codVeiculo = codVeiculo.toString();
    codVeiculo = codVeiculo.trim(); 
    
    $('#situacao-veiculo').val("A");
    if (codVeiculo != "") {        
        retorno = consulta_cod_veiculo_banco(myForm, codProp, codVeiculo);                              
    } 
    
    if (retorno == 'error') {
        alert("Código do Veículo não encontrado!");
        myForm.codVeiculo.focus();               
    } else if (codVeiculo != "" || myForm.descQtdeVeiculo.value < 3){                                                                                                    
        habilita_campos(".hab-campos-veiculo");
        $("#formCadastroVeiculo").validate(); 

        myForm.btnNovoVeiculo.disabled = true;
        myForm.codVeiculo.readOnly = true;
        myForm.bibPontosVeiculo.disabled = true;
        myForm.btnSalvarVeiculo.disabled = false;
        myForm.placa.focus();
    }
    return;
}

function consulta_cod_veiculo_banco(form, id_proprietario, id_veiculo) {    
    var retorno = '';   
    var dados = {
        id_proprietario: id_proprietario,
        id_veiculo: id_veiculo               
    }
    $.ajax({
        type: 'POST',
        url: '/buscarveiculo',
        data: dados,        
        dataType: 'text',
        async: false,
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
                retorno = "success";                                                                                   
            } else {                                
                retorno = "error";                                 
            }                                                 
        }
    }); 
    return retorno;   
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
        var descQtdeVeiculo = document.querySelector("#desc-qtde-veiculo");           
        var tableVeiculo = document.querySelector("#table-veiculo");          
        var qtdeLinhas = tableVeiculo.rows.length - 1; 

        for (var i=0; i < qtdeLinhas; i++) {
            tableVeiculo.deleteRow(1);                    
        }
                                                                     
        var seq = 0;
        for (var veiculo of veiculos) { 
            seq++;                                                    
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
            
            var cel7 = linha.insertCell(6);
            var button = document.createElement("button"); 
            button.type = "button";
            button.removeAttribute("aria-invalid");
            button.classList.add("btn", "btn-block", "btn-outline-primary", "alterar-veiculo");            
            button.value = veiculo.id_carro; 
            button.textContent = "Alterar";
            cel7.appendChild(button);            
        }

        if (descQtdeVeiculo.value != seq){
            descQtdeVeiculo.value = seq           
        }  
        
        var btnAlterVeiculo = document.querySelectorAll(".alterar-veiculo");
        btnAlterVeiculo.forEach(alterar => {
            alterar.addEventListener('click', () => {
                var myForm = document.querySelector("#formCadastroVeiculo");                                
                var idVeiculo = alterar.value;
               
                myForm.codVeiculo.value = idVeiculo;
                verifica_cod_veiculo();                                                
            })
        });        
    }
    else {
        //
    }
}