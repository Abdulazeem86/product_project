
document.addEventListener('DOMContentLoaded', function() {
    var product_card = document.getElementById('product-card');

    product_card.addEventListener('click', function() {
        // Navigate to the desired page
        window.location.href = '/productspec/';
    });
});