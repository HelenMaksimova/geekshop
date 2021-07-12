function success_func(data) {
    $('.basket_list').html(data.result)
}

function basket_change () {
    let t_href = event.target
    $.ajax({
            url: '/baskets/edit/' + t_href.name + '/' + t_href.value + '/',
            success: success_func
        })
    event.preventDefault()
}

window.onload = function () {
    $('.basket_list').on('click', 'input[type="number"]', basket_change)
}
