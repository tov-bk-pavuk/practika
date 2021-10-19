let button = document.querySelector('#contact_button')

function but_funcs () {
    button.onclick = function () {
        button.style.color = 'red'; // Эксперименты с работой JS
        $(button);
        $.ajax({  // Заполняем поля Аякс-запроса
            url: $(button).attr("data-url"), // берём ссылку из атрибута "data-url" тега с id "contact_button"
            type: 'get',
            dataType: 'json',
            // beforeSend: function () {  // Хитрое ветвление "Перед отправкой запроса" показываем модальное окно
            //     $('.modal .modal-content').html(''); //  Очищаем содержимое тегов с классами ".modal .modal-content"
            //     $('.modal').modal-content('show'); //  При помощи jquery метода "show" наверно показываем модальное окно
            //     },
            success: function (data) { // Если ответ от сервера получен
                //$('.modal .modal-content').html(data.html_form); //  Создаём из пришедшего словаря "data" кусок html-кода с формой
                $('.d').html(data.html_form) // в тег с селектором '.d' загружаем хоть целый отдельную страницу - HTML код переданный одной строкой

            },
            });
        }
    button.onmouseover = function () {  // Эксперименты с JS
        button.style.background = 'red';
        button.style.color = 'white';
    };
    button.onmouseout = function () {  // Эксперименты с JS
        button.style.background = 'green';
    };

}

but_funcs()  // Вызываем ВСЕЯ функцию. Знаю, что можно просто всё поместить внутрь.

let saveForm = function () {
    let form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $(".d").html(data.html_success);
        }
        else {
          $(".d").html(data.html_form);
        }
      }
    });
    // return false;
}

$(".send").on("submit", ".form_s", saveForm);
