
    function increaseQuantity(productId){
    const quantityInput=document.getElementById('quantity-'+productId)
    let currentQuantity=parseInt(quantityInput.value)
    currentQuantity++
    quantityInput.value=currentQuantity
    if(currentQuantity>0){
        const addToCartButton=document.querySelector('button[onclick="addToCart(\''+productId+'\')"]')
        addToCartButton.removeAttribute('disabled')
    }
    else{
        const addToCartButton=document.querySelector('button[onclick="addToCart(\''+productId+'\')"]')
        addToCartButton.setAttribute('disabled', 'true')
    }
}

function decreaseQuantity(productId){
    const quantityInput=document.getElementById('quantity-'+productId)
    let currentQuantity=parseInt(quantityInput.value)
    if(currentQuantity>0){
        currentQuantity--
        quantityInput.value=currentQuantity
    }
    if(currentQuantity>0){
        const addToCartButton=document.querySelector('button[onclick="addToCart(\''+productId+'\')"]')
        addToCartButton.removeAttribute('disabled')
    }
    else{
        const addToCartButton=document.querySelector('button[onclick="addToCart(\''+productId+'\')"]')
        addToCartButton.setAttribute('disabled', 'true')
    }
}

function addToCart(productId){
    const quantityInput=document.getElementById('quantity-'+productId)
    
    let currentQuantity=parseInt(quantityInput.value)
    fetch('/cart/add/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': '{{ csrf_token }}'
        },
        body: JSON.stringify({
            product_id: productId,
            quantity: currentQuantity
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log('productId', productId)
        if(data.success){
            alert('Product added to cart')
        }else{
            alert('Failed to add product to cart')
        }
    })
}


