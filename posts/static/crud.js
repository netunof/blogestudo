$(function () {

    let modalCreate = $('#modalCreate');
    let modalLogin = $('#modalLogin');
    let modalUpdate = $('#modalUpdate');
    let fecharModal = $('#fecharModal');
    let conteudoModal = $('#conteudoModal');
    let fora = $('#fora');
    let modal = $('#modal');

    $(modalCreate).on('click', function () {
        $.ajax({
            type: "get",
            url: "../posts/create",
            success: function (response) {
                $(modal).show();
                $(conteudoModal).html(response);
            }
        });
    });
    $(modalUpdate).on('click', function () {
        let id = $(this).val();
        $.ajax({
            type: "get",
            url: id+"/update",
            success: function (response) {
                $(modal).show();
                $(conteudoModal).html(response);
            }
        });
    });
    // infelizmente o jquery não está aceitando array de seletores, por isso a função repetida
    $(modal).on('click', fecharModal, function () {
        $(modal).hide();
        $(conteudoModal).html("");
        return false;
    });
    $(modal).on('click', fora, function () {
        $(modal).hide();
        $(conteudoModal).html("");
        return false;
    });
});