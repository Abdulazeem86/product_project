
// document.addEventListener('DOMContentLoaded', function() {
//     var product_card = document.getElementById('product-card');

//     product_card.addEventListener('click', function() {
//         // Navigate to the desired page
//         window.location.href = '/productspec/';
//     });
    
// });

// Using jquery to minimise/simplify the above code

$(document).ready(function() {
    $('#product-card').on('click', function () {
        window.location.href = '/productspec/';
    })
})


$(document).ready(function(){
    $('.product-card-class').on('click', function(){
        window.location.href = '/productspec/'
    })
})














































// Using document.querySelectorAll for multiple items

// document.addEventListener('DOMContentLoaded', function() {
//     // Get all elements with the class name 'product-card'
//     var product_cards = document.querySelectorAll('.product-card-class');

//     // Loop through each product card
//     product_cards.forEach(function(product_card) {
//         // Add click event listener to each product card
//         product_card.addEventListener('click', function() {
//             // Navigate to the desired page
//             window.location.href = '/productspec/';
//         });
//     });
// });




// Using getElementsByClassName instead of document.querySelectorAll

// document.addEventListener('DOMContentLoaded', function() {
//     // Get all elements with the class name 'product-card'
//     var product_cards = document.getElementsByClassName('product-card-class');

//     // Loop through each product card
//     for (var i = 0; i < product_cards.length; i++) {
//         // Add click event listener to each product card
//         product_cards[i].addEventListener('click', function() {
//             // Navigate to the desired page
//             window.location.href = '/productspec/';
//         });
//     }
// });






// document.addEventListener('DOMContentLoaded', function() {
//     var product_card = document.getElementsByClassName('product-card-class');

//     product_card.addEventListener('click', function() {
//         // Navigate to the desired page
//         window.location.href = '/productspec/';
//     });
    
// });