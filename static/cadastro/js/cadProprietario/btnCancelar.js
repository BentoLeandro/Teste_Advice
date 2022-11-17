function btn_cancelar_proprietario() {
    desabilita_campos(".hab-campos-prop");    
    limpa_campos(".limpar-campos-prop");     

    //limpando todos os campos de busca que utilizam select2                            
    $('select.select2').val('').trigger('change');
    
    var myForm = document.getElementById("formCadastroProp");
    clearValidation(myForm);

    document.getElementById("btn-novo-prop").disabled = false;
    document.getElementById("btn-salvar-prop").disabled = true;    
    document.getElementById("btn-excluir-prop").disabled = true;
    document.getElementById("cod-proprietario").readOnly = false;
    document.getElementById("cod-proprietario").value = '';
    document.getElementById("bib-pontos-prop").disabled = false;
    document.getElementById("cod-proprietario").focus();
}

function btn_cancelar_veiculo() {
    desabilita_campos(".hab-campos-veiculo");    
    limpa_campos(".limpar-campos-veiculo");    

    //limpando todos os campos de busca que utilizam select2                            
    $('select.select2').val('').trigger('change');
    
    var myForm = document.getElementById("formCadastroVeiculo");
    clearValidation(myForm);

    document.getElementById("btn-novo-veiculo").disabled = false;
    document.getElementById("btn-salvar-veiculo").disabled = true;    
    document.getElementById("btn-excluir-veiculo").disabled = true;
    document.getElementById("cod-veiculo").readOnly = false;
    document.getElementById("cod-veiculo").value = '';
    document.getElementById("bib-pontos-veiculo").disabled = false;
    document.getElementById("cod-veiculo").focus();
}
       