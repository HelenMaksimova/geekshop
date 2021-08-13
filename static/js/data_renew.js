let _quantity, _price;
let orderitemNum, deltaQuantity, orderitemQuantity, deltaCost, itemTotalPrice;
let quantityArray = [];
let priceArray = [];
let totalForms = parseInt($('input[name="orderitems-TOTAL_FORMS"]').val());
let orderTotalQuantity = parseInt($('.order_total_quantity').text()) || 0;
let orderTotalCost = parseFloat($('.order_total_cost').text().replace(',', '.')) || 0;

function basketSuccess(data) {
    $('.basket_list').html(data.result);
}

function orderPriceSuccess(data) {
    $('input[name="orderitems-' + orderitemNum + '-price"]').val(data.result['price']);
    priceArray[orderitemNum] = data.result['price'];
}

function basketChange() {
    let t_href = event.target
    $.ajax({
        url: '/baskets/edit/' + t_href.name + '/' + t_href.value + '/',
        success: basketSuccess
    })
    event.preventDefault()
}

function renewOrderData() {
    for (let i = 0; i < totalForms; i++) {
        _quantity = parseInt($('input[name="orderitems-' + i + '-quantity"]').val());
        _price = parseFloat($('input[name="orderitems-' + i + '-price"]').val());
        quantityArray[i] = _quantity;
        if (_price) {
            priceArray[i] = _price;
        } else {
            priceArray[i] = 0;
        }
    }
}

function orderSummaryUpdate(orderitemPrice, deltaQuantity) {
    deltaCost = orderitemPrice * deltaQuantity;
    orderTotalCost = Number((orderTotalCost + deltaCost).toFixed(2));
    orderTotalQuantity += deltaQuantity;
    $('.order_total_quantity').html(orderTotalQuantity);
    $('.order_total_cost').html(orderTotalCost);
}

function orderItemUpdate() {
    let target = event.target;
    let namePartsArray = target.name.split('-');
    orderitemNum = parseInt(namePartsArray[1]);
    if (namePartsArray[2] === 'quantity') {
        if (priceArray[orderitemNum]) {
            orderitemQuantity = parseInt(target.value);
            deltaQuantity = orderitemQuantity - quantityArray[orderitemNum];
            quantityArray[orderitemNum] = orderitemQuantity;
            orderSummaryUpdate(priceArray[orderitemNum], deltaQuantity);
        }
    }

    if (namePartsArray[2] === 'product') {
        let t_href = event.target
        $.ajax({
            url: '/orders/order_item_price/' + t_href.value + '/',
            success: orderPriceSuccess
        })
        event.preventDefault()
    }

    itemTotalPrice = Number((quantityArray[orderitemNum] * priceArray[orderitemNum]).toFixed(2));
    $('input[name="orderitems-' + orderitemNum + '-total_price"]').val(itemTotalPrice);
}

function deleteOrderItem(row) {
    let namePartsArray = row[0].querySelector('input[type=number]').name.split('-');
    orderitemNum = parseInt(namePartsArray[1]);
    deltaQuantity = -quantityArray[orderitemNum];
    orderSummaryUpdate(priceArray[orderitemNum], deltaQuantity)
}

window.onload = function () {
    renewOrderData()
    $('.basket_list').on('click', 'input[type="number"]', basketChange)
    $('.order_form').on('click', '.formset_td', orderItemUpdate);
    $('.formset_row').formset({
            addText: 'Добавить товар',
            deleteText: 'Удалить',
            prexix: 'orderitems',
            removed: deleteOrderItem
        }
    )
}
