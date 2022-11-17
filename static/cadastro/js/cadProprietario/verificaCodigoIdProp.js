function verifica_cod_proprietario() { 
    var myForm = document.querySelector("#formCadastroProp");             
    var codprop = myForm.codProprietario.value;
    var encontrou_prop = false;    

    codprop = codprop.toString();
    codprop = codprop.trim();
    
    $('#sit-prop').val("A");
    if (codprop != "") {
        //$('#cod-proprietario').valid();
        //myForm.codProprietario.focus();
        encontrou_prop = consulta_cod_proprietario_banco(myForm, codprop, 'C');        
    }                                                                                               
    habilita_campos(".hab-campos-prop");
    
    myForm.btnNovoProp.disabled = true;
    myForm.codProprietario.readOnly = true;
    myForm.bibPontosProp.disabled = true;
    myForm.btnSalvarProp.disabled = false;
    myForm.nome.focus();
}

function consulta_cod_proprietario_banco(form, id_proprietario, tipo_campo) {
    var dados = {
        id_proprietario: id_proprietario               
    }
    $.ajax({
        type: 'POST',
        url: '/buscarproprietario',
        data: dados,        
        dataType: 'text',
        error: function(ret){
            console.log(ret);
        },
        success: function(ret){    
            console.log(ret);        
            var prop = JSON.parse(ret);

            if (!('retorno' in prop)){ 
                if (tipo_campo == "C") {                                 
                    form.nome.value = prop.nome;
                    form.SitProp.value = prop.situacao;
                             
                    form.logradouro.value = prop.logradouro;
                    form.numero.value = prop.numero;
                    form.telefone.value = prop.telefone;                                                                                                                                                 
                
                    if (id_proprietario != "1") {
                        document.querySelector('#btn-excluir-prop').disabled = false;
                    }                
                    $('select.select2').trigger('change');                                                                                    
                }
                else {
                    form.descProprietario.value = prop.id_proprietario
                    form.descNome.value = prop.nome;
                    form.descSituacao.value = prop.situacao;
                             
                    form.descLogradouro.value = prop.logradouro;
                    form.descNumero.value = prop.numero;
                    form.descTelefone.value = prop.telefone;  
                    form.descQtdeVeiculo.value = prop.qtde_carros;  
                }
            } 
            return true;                         
        }
    });    
}



