function openModal() {
    $('#form-modal').css('display', 'block');
}

function closeModal() {
    $('#contact-form')[0].reset()
    $('#form-modal').css('display', 'none');
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$("#contact-form").on('submit', function (e) {
    e.preventDefault()

    $.ajax({
        method: $(this).attr('method'),
        url: $(this).attr('action'),
        headers: {"X-CSRFToken": getCookie("csrftoken")},
        data: $(this).serialize(),
        dataType: 'json',
        processData: false,
        success: function (data) {
            if (data.success) {
                window.location.href = '/'
            }
        }
    })
})
