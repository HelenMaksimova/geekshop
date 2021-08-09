window.onload = function () {
    var _quantity, _price;
    var orderitemNum, deltaQuantity, orderitemQuantity, deltaCost;
    var quantityArray = [];
    var priceArray = [];
    var totalForms = parseInt($('input[name="orderitems-TOTAL_FORMS"]').val());
    var orderTotalQuantity = parseInt($('.order_total_quantity').text()) || 0;
    var orderTotalCost = parseFloat($('.order_total_cost').text().replace(',', '.')) || 0;
    for (let i = 0; i < totalForms; i++) {
        _quantity = parseInt($('input[name="orderitems-' + i + '-quantity"]').val());
        _price = parseFloat($('.orderitems-' + i + '-price').text().replace(',', '.'));
        quantityArray[i] = _quantity;
        if (_price) {
            priceArray[i] = _price;
        } else {
            priceArray[i] = 0;
        }
    }

    $('.order_form').on('click', 'input[type="number"]', function() {
        var target = event.target;
        orderitemNum = parseInt(target.name.replace('orderitems-', '').replace('-quantity', ''));
        if (priceArray[orderitemNum]) {
            orderitemQuantity = parseInt(target.value);
            deltaQuantity = orderitemQuantity - quantityArray[orderitemNum];
            quantityArray[orderitemNum] = orderitemQuantity;
            orderSummaryUpdate(priceArray[orderitemNum], deltaQuantity)
        }
    });

    function orderSummaryUpdate(orderitemPrice, deltaQuantity) {
        deltaCost = orderitemPrice * deltaQuantity;
        orderTotalCost = Number((orderTotalCost + deltaCost).toFixed(2));
        orderTotalQuantity += deltaQuantity;

        $('.order_total_quantity').html(orderTotalQuantity);
        $('.order_total_cost').html(orderTotalCost);

    }
}
