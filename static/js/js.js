let but = document.querySelector('#contact_button')
let di = document.querySelector('.d')

but.onclick = function () {  //but.onclick = function () {
    $(but);
    di.style.visibility = 'visible'
    $.ajax({
        url: $(but).attr("data-url"),
        type: 'get',
        dataType: 'json',
        success: formLoaded
        });
    }
function formLoaded(data) {
    $('.d').html(data.html_form);
    // console.log($('#form-s'), document.querySelector('#form-s'))
    // document.querySelector('#form-s').addEventListener('onclick', function (event)
    $('#form-s').on('submit', function(event) {
        // console.log(event, event.target)
        event.preventDefault();

        $.ajax({
            type: 'post',
            dataType: 'json',
            data: $(event.target).serialize(),
            url: $(event.target).attr('action'),
            success: function (data) {
                console.log(data)
                $('.d').html(data.html_form);
            }
        });
    })
}
