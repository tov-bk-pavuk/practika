console.log('Я загрузился');

but_send.click = (function () {
    console.log('Перед запросом');
    $.ajax({
        type: 'post',
        dataType: 'json',
        data: $('form').serialize(),
        url: $('.form_s').attr('action'),
        success: function (data) {
            $('.d').html(data.html_form);
        }
    });
    console.log('После запроса');
    })

console.log('Финальный лог');