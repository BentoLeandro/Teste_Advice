function habilita_campos(classe_campos) {
    //document.getElementsByClassName("form-control")[0].disabled = false;
    var campos = document.querySelectorAll(classe_campos);
    for (var i = 0; i < campos.length; i++){
        campos[i].disabled = false;
    }
    //".hab-campos-prop"
    //hab-campos-veiculo
}

function desabilita_campos(classe_campos) {
    //document.getElementsByClassName("form-control")[0].disabled = true;
    var campos = document.querySelectorAll(classe_campos);
    for (var i=0; i < campos.length; i++){
        campos[i].disabled = true;
    }
} 

function limpa_campos(classe_campos) {
    var campos = document.querySelectorAll(classe_campos);
    for (var i = 0; i < campos.length; i++){
          campos[i].value = '';
    }
}

function mostra_alerta_qtde_veiculos(mostra_alerta) {    
    //var situacao = document.querySelector("#sit-lote").value;

    if (mostra_alerta == 'N') {
        document.querySelector("#obs-qtde-veiculo").style.visibility = "hidden";
    } else {
        document.querySelector("#obs-qtde-veiculo").style.visibility = "visible";
    }
}

function remove_ponto_vlr(pvalor) {            
    var nvlr = parseFloat(pvalor.replace(/[^0-9,]*/g, '').replace(',', '.')).toFixed(2);
    return nvlr;
}

function formato_moeda(pvalor, pcampo) {
    if (pcampo == 'S') 
        var nvlr = pvalor.value.replace(/\D/g, '');
    else
        var nvlr = pvalor.replace(/\D/g, '');
            
    nvlr = (nvlr/100).toFixed(2)+'';
    nvlr = nvlr.replace('.', ',');
    nvlr = nvlr.replace(/(\d)(\d{3})(\d{3}),/g, "$1.$2.$3,");
    nvlr = nvlr.replace(/(\d)(\d{3}),/g, "$1.$2,");

    if (pcampo == 'S')           
        pvalor.value = nvlr;	        
    else            
        return nvlr;                                           
}

function clearValidation(formElement){
    //Internal $.validator is exposed through $(form).validate()
    var validator = $(formElement).validate();
    //Iterate through named elements inside of the form, and mark them as error free
    $('[name]',formElement).each(function(){
        validator.successList.push(this);//mark as error free
        validator.showErrors();//remove error messages if present
    });

    $('.is-invalid').removeClass('is-invalid');
    $('.field-error').removeClass('field-error');

    validator.resetForm();//remove error class on name elements and clear history
    validator.reset();//remove all error and success data
}

$.validator.addMethod("qtde_codbarras", function(value, element){
    if (isNaN(value) == false) {                                           
        if (value.length < 12 ){                    
            return false; //quando o retorno for false ser?? exibido a msg de erro...
        }
        else {
            return true;
        }                            
    }    
    else{
        return true;
    }

}, "O c??digo de barras ?? menor que 12 caracteres!")

$.validator.addMethod("valor_fator_conversao", function(value, element){
    var sunid_compra = $('#unidCompra').val(); 
    var sunid_venda = $('#unidVenda').val(); 
    var ifator_conver = $('#fator-conversao').val();
            
    if (sunid_compra != sunid_venda) {                
        if (value <= 1){                    
            return false; //quando o retorno for false ser?? exibido a msg de erro...
        }                    
        else
            return true;    
    }
    else
        return true;        
}, "O Campo deve ser maior do que 1 !")

//valida????o dos campos
//depois que carregar a pagina ser?? adicionada as valida????es
//$(function(){        
$("#formCadastroProp").validate({
    rules: {        
        nome: {
            required: true
        },
        logradouro: {
            required: true
        },
        numero: {
            required: true
        },
        telefone: {
            required: true           
        }
    },
    messages: {        
        nome: {
            required: "O Nome precisa ser informado!"
        },
        logradouro: {
            required: "O Logradouro precisa ser informado!"
        },
        numero: {
            required: "O N??mero precisa ser informado!"
        },
        telefone: {
            required: "O Telefone precisa ser informado!"
            //,number: "Digite somente n??meros inteiros!"
        }
    },
    errorElement: 'span',
    errorPlacement: function (error, element) {
        error.addClass('invalid-feedback');
        element.closest('.form-group-sm').append(error);
    },
    highlight: function (element, errorClass, validClass) {
        $(element).addClass('is-invalid');
    },
    unhighlight: function (element, errorClass, validClass) {
        $(element).removeClass('is-invalid');
    }
})
                
$("#formCadastroVeiculo").validate({
    rules: {        
        placa: {
            required: true
        },
        descricaoVeiculo: {
            required: true
        },
        situacaoVeiculo: {
            required: true
        },
        modeloVeiculo: {
            required: true           
        },
        corVeiculo: {
            required: true
        }
    },
    messages: {        
        placa: {
            required: "A Placa precisa ser informada!"
        },
        descricaoVeiculo: {
            required: "A Descri????o precisa ser informada!"
        },
        situacaoVeiculo: {
            required: "A Situa????o precisa ser informada!"
        },
        modeloVeiculo: {
            required: "O Modelo precisa ser informado!"            
        },
        corVeiculo: {
            required: "A Cor precisa ser informada!"            
        }
    },
    errorElement: 'span',
    errorPlacement: function (error, element) {
        error.addClass('invalid-feedback');
        element.closest('.form-group-sm').append(error);
    },
    highlight: function (element, errorClass, validClass) {
        $(element).addClass('is-invalid');
    },
    unhighlight: function (element, errorClass, validClass) {
        $(element).removeClass('is-invalid');
    }
})
