let but = document.querySelector('#contact_button')
let but_send = document.querySelector('#send')
let di = document.querySelector('.d')

console.log('Перед вызовом кнопки Инфо');

but.onclick = function () {  //but.onclick = function () {
    $(but);
    di.style.visibility = 'visible'
    $.ajax({
        url: $(but).attr("data-url"),
        type: 'get',
        dataType: 'json',
        success: function (data) {
            $('.d').html(data.html_form);
            },
        });
    console.log('Форма вызвана');
    }

//$("#modal-book").on("submit", ".js-book-create-form", saveForm);

// $(".send").submit(function( event ) {
//   alert( "Handler for .submit() called." );
//   event.preventDefault();
// });