$('.plus-cart').click(function(){
    var id = $(this).attr("pid").toString();
    var temp = this.parentNode.children[2]
    $.ajax({
        type:"GET",
        url:"/increment",
        data:{
            item_id : id
        },
        success: function(data)
        {
            console.log(data)
            console.log("Success")
            temp.innerText = data.quantity
            document.getElementById("amount").innerText = data.amount
            document.getElementById("total_amt").innerText = data.total_amount
        }
    })
})

$('.minus-cart').click(function(){
    var id = $(this).attr("pid").toString();
    var temp = this.parentNode.children[2]
    console.log(id)
    $.ajax({
        type:"GET",
        url:"/decrement",
        data:{
            item_id : id
        },
        success: function(data)
        {
            console.log(data)
            console.log("Success")
            temp.innerText = data.quantity
            document.getElementById("amount").innerText = data.amount
            document.getElementById("total_amt").innerText = data.total_amount
        }
    })
})

$('.remove-cart').click(function(){
    var id = $(this).attr("pid").toString();
    temp=this
    console.log("temp:",temp)
    console.log("id:",id)
    $.ajax({
        type:"GET",
        url:"/remove_item",
        data:{
            item_id : id
        },
        success: function(data)
        {
            console.log(data)
            console.log("Success")
            document.getElementById("amount").innerText = data.amount
            document.getElementById("total_amt").innerText = data.total_amount
            temp.parentNode.parentNode.parentNode.remove()
        }
    })
})

