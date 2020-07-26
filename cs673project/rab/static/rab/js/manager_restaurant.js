
$(document).ready(function() {

    $("#manager-restaurant-form").on("submit", function(e){
        e.preventDefault()
            //todo: ajax to update user info
            let data = $(this).serialize();
            let url = $(this).attr("action");
            //let form = $(this)
            $.post(url, data, (result) => {
                loadData(result);
            },'json'
            );
    }); 


});

function loadData(restaurant){
    console.log("load");
    //todo: load restaurant data by id
    
    $("input#name").val(restaurant.name);
    $("input#address").val(restaurant.address);
    $("input#phone").val(restaurant.phone);
    $("input#open-time").val(restaurant.open_time);
    $("input#close-time").val(restaurant.close_time);
    
}