/**
 * Created by cav on 28.05.19.
 */
function sendUserNumber(event) {
    console.log("SUBMIT");
    $theform = $("#user_number_form");
    console.log($theform.serialize());
    $.ajax({
        url:"api/user_value",
        type:"POST",
        data:$theform.serialize()
    }).done(function (data) {
        console.log(data)
    }).fail(function (xhr, status, errorThrown){
        console.log(errorThrown);
    });
    return false;
}

function getExtrasense(event) {
    console.log("Click");
    $.ajax({
        url:"api/get_extrasense_value",
        type:"POST"
    }).done(function(data){
        console.log(data);
        $("#user_block").html(data);
        $("#user_number_form").submit(sendUserNumber);
    }).fail(function (xhr, status, errorThrown) {
        console.log(errorThrown);
    });
}

window.onload = function () {
    console.log("START");
    $("#number_set").click(getExtrasense);
}
