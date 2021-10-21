console.log('Я загрузился');
let but_send = document.querySelector('#send')

// but_send.onclick()

but_send.onmouseover = function () {  // Эксперименты с JS
        but_send.style.background = 'red';
        but_send.style.color = 'white';
    };

function batik () {
    $('but_send');
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
    return false;
    }

// $('but_send').on("submit", 'form_s', batik);
console.log('Финальный лог');
