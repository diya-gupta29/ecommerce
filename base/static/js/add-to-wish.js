$('.remove-wish').click(function(){
    var id = $(this).attr("pid").toString();
    temp=this
    console.log("temp:",temp)
    console.log("id:",id)
    $.ajax({
        type:"GET",
        url:"/remove_wish",
        data:{
            item_id : id
        },
        success: function(data)
        {
            // console.log(data)
            console.log("Success")
            temp.parentNode.parentNode.parentNode.remove()
        }
    })
})

$('.bag').submit(function(){
    var id = $(this).attr("pid").toString();
    temp=this
    console.log("temp:",temp)
    console.log("id:",id)
    $.ajax({
        type:"GET",
        url:"/remove_wish",
        data:{
            item_id : id
        },
        success: function(data)
        {
            // console.log(data)
            console.log("Success")
            temp.parentNode.parentNode.parentNode.remove()
        }
    })
})