
function abrir_modal_edit_check(url){

    $('#editar_checklist').load(url, function(){
        $(this).modal('show');
    })
}

function abrir_modal_eliminar_check(url){

$('#modalEliminar').load(url, function(){
$(this).modal('show');
})
}


function abrir_modal_crear_act(url){

    $('#modalCrear').load(url, function(){
        $(this).modal('show');
    })
}


function abrir_modal_editar_act(url){

    $('#modalEditar').load(url, function(){
        $(this).modal('show');
    })
}

function abrir_modal_eliminar_act(url){

$('#modalEliminar').load(url, function(){
$(this).modal('show');
})
}

function abrir_modal_updateuncheck(url){

    $('#modificarUncheck').load(url, function(){
        $(this).modal('show');

        
})
}
function abrir_modal_updatecheck(url){

$('#modificarCheck').load(url, function(){
    $(this).modal('show');
})
}
