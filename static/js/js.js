let but = document.querySelector('#contact_button') // для понимания \/
let di = document.querySelector('.d')  // объявление аналогичное jquery $('#contact_button')

but.onclick = function () {  //  при нажатии на кнопку, определённую в первой строке
    //$(but);
    di.style.visibility = 'visible'
    $.ajax({
        url: $(but).attr("data-url"),
        type: 'get',
        dataType: 'json',
        success: function again (data) { // тут ответ сервера приезжает либо с пустой формой либо с полной
            $('.d').html(data.html_form); // formLoaded //  Предположительно ветвление нужно сделать тут
            $('#form_s').on('submit', function (event){ // при нажатии на "Отправить"
                console.log(event) // консоль отображает перехваченное событие с формой
                $.ajax({ // делаем запрос с данными формы, может быть ошибка того, что мы передаём
                    url: $(but).attr("data-url"), // $.attr('action'), // тут может быть ошибка с обращением к полю формы
                    type: 'post',
                    data: $('#form_s').serialize(), // серелизуем содержимое формы, можно поменять на event.serialize()
                    dataType: 'json',
                    success: function (data){  // принимаем ответ сервера
                        $('.d').html(data.html_form); // помещаем ответ сервера в div с классом ".d"
                        if (data.form_is_valid) { // если посе словаря равно Истина
                            $('.d').html(data.html_form); // $('.d').p.innerHTML('Форма отправлена успешно') // суём в абзац текст
                            // alert('Форма отправлена');
                            setTimeout(function() {di.style.visibility = 'hidden'}, 2000);
                        }
                        else { // если что-то другое
                            return again(data)  // вызываем снова функцию загрузки первичной формы
                        }
                    }
                })
                return false; //  отправка формы на сервер перехватывается JS и не происходит
            });
        }
    });
}
// нужно быть внимательным с загрузкой DOM, и перехватчиком событий
// имеет значение место подключения скрипта в HTML странице
// JS может "не видеть" элементы, созданные другим куском кода JS из-за очередёности загрузки
// событие submit JS исполняет один раз, если не поместить его в цикл или не навесить
// если на странице грузится HTML-код в строку, значит событие отправки формы не перехвачено