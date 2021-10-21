console.log('Я загрузился');
let but_send = document.querySelector('#send')

// but_send.onclick()

but_send.onmouseover = function () {  // Эксперименты с JS
        but_send.style.background = 'red';
        but_send.style.color = 'white';
        console.log('ssss')
    };

function batik () {
    $('but_send');
    console.log('Перед запросом');

    return false;
    }

// $('but_send').on("submit", 'form_s', batik);
console.log('Финальный лог');
