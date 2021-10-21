let button = document.querySelector('#contact_button')

function but_funcs () {
    button.onclick = function () {
        $(button);
        $.ajax({
            url: $(button).attr("data-url"), // берём ссылку из атрибута "data-url" тега с id "contact_button"
            type: 'get',
            dataType: 'json',
            success: function (data) {
                $('.d').html(data.html_form)
            },
            });
        }
}

but_funcs()  // Вызываем функцию.
