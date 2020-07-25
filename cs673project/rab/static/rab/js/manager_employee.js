$(document).ready(function() {
    
    loadData();

     $("#add-item-btn").on("click", function(){
        sessionStorage.removeItem("employeeID");
        $("#employee-detail").attr("src", "manager_employee_detail");
        $(".selected").removeClass("selected");
    });
});

function loadData(){
    
    //todo: ajax to load the list of dishes
    //sample return:
    let employees = {
        0:{id: 25,
        name: "Ali Baba"},
        1:{id: 26,
        name: "Cindy Douglas"},
        2:{id: 29,
        name: "Eli Fantine"},
        3:{id: 41,
        name: "Gloria Hernandez"}
    };
    
    let employeeListRoot = $("#employee-list-items-container");
    employeeListRoot.empty();
    
    Object.keys(employees).forEach(key => {
        employeeListRoot.append('<div id = "employee-' + key + '" class="employee-item"><p>' + employees[key].name + '</p><span id = "url" style="display: none">manager_employee_detail</span><span id = "dish-id" style = "display:none">' + employees[key].id + '</span></div>');
    });
    
    $(".employee-item").on("click", function(){
        sessionStorage.setItem("employeeID", $(this).children("span#dish-id").text());
        $("#employee-detail").attr("src", $(this).children("span#url").text());
        $(".selected").removeClass("selected");
        $(this).addClass("selected");
    });
}