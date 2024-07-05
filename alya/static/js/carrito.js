function addToCart(workCode, title, author, image) {
    let cart = JSON.parse(localStorage.getItem('cart')) || {};
    cart[workCode] = {
        title: title,
        author: author,
        image: image
    };

    localStorage.setItem('cart', JSON.stringify(cart));

    $('#alert').empty();
    $("#alert").append(`
        <button type="button" class="btn-close" onclick="hideAlert()" aria-label="Close"></button>
        "${title}" agregado al carrito
    `);
    $("#alert").addClass('show');

    updateCart();
}

function removeFromCart(workCode, title) {
    let cart = JSON.parse(localStorage.getItem('cart')) || {};

    if (cart[workCode]) {
        $('#alert').empty();
        $("#alert").append(`
            <button type="button" class="btn-close" onclick="hideAlert()" aria-label="Close"></button>
            "${title}" eliminado del carrito
        `);
        $("#alert").addClass('show');

        delete cart[workCode];
        localStorage.setItem('cart', JSON.stringify(cart));

        updateCart();
    }
}

function updateCart() {
    let cart = JSON.parse(localStorage.getItem('cart')) || {};
    let cartDiv = $("#cart");
    cartDiv.empty();

    $.each(cart, function(workCode, item) {
        if (!($('body').attr('id') == 'carrito')) {
            cartDiv.append(
                "<li class='list-group-item d-flex justify-content-between align-items-center'>" +
                    "<span>" + item.title + "</span>" +
                    `<button class='btn btn-danger btn-sm' onclick='removeFromCart("${workCode}", "${item.title.replace(/'/g, '')}")'>Eliminar</button>` +
                "</li>"
            );
        } else {
            cartDiv.append(`
                <tr>
                  <td class="align-middle"><img src="${item.image}" class="rounded-2 border border-2 border-dark" alt="?" width="120" height="180"></td>
                  <td class="align-middle"><h3>${item.title}</h3></td>
                  <td class="align-middle"><h4>${item.author}</h4></td>
                  <td class="align-middle"><button class='btn btn-danger btn-sm' onclick='removeFromCart("${workCode}", "${item.title.replace(/'/g, '')}")'>Eliminar</button></td>
                </tr>`
            );
        }
    });
}

function hideAlert() {
    var alertDiv = document.getElementById('alert');
    alertDiv.classList.remove('show');
  }

$(document).ready(function () {
    updateCart()

    $("#confirmarBtn").click(function(e) {
        e.preventDefault(); 
        localStorage.removeItem('cart');
        
        window.location.href = $(this).attr("href");
    });
});