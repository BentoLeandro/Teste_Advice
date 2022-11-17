function verifica_btn_salvar_proprietario() {                  
    $("#formCadastroProp").valid();            
}

function verifica_btn_salvar_veiculo() {
    var myForm = document.querySelector("#formCadastroVeiculo");
    $("#formCadastroVeiculo").valid();
    
    grava_excluir_veiculo(myForm, 'gravar');
    btn_cancelar_veiculo();
}

function btn_excluir_veiculo(){
    var myForm = document.querySelector("#formCadastroVeiculo");
    grava_excluir_veiculo(myForm, 'excluir');    
    $('#modal-veiculo').modal('hide');
    btn_cancelar_veiculo();
}

function grava_excluir_veiculo(form, metodo) {
    var dados = {
        id_proprietario: form.descProprietario.value,                       
        id_carro: form.codVeiculo.value,
        placa: form.placa.value, 
        descricao: form.descricaoVeiculo.value,
        modelo: form.modeloVeiculo.value, 
        cor: form.corVeiculo.value, 
        situacao: form.situacaoVeiculo.value,
        metodo: metodo 
    }
    $.ajax({
        type: 'POST',
        url: '/gravarexcluirveiculo',
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

