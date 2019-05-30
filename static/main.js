/**
 * Created by cav on 28.05.19.
 */

function refreshUserHistory() {
    $.ajax({
        url:"api/user_history",
        type:"POST"
    }).done(function (data) {
         $("#table_user_his_panel").html(data);
    }).fail(function (xhr, status, errorThrown) {
        console.log(errorThrown);
    });
}

function refreshExtrasensHistory() {
    $.ajax({
        url:"api/extrasense_history",
        type:"POST"
    }).done(function (data) {
        $("#table_exp_his").html(data)
    }).fail(function (xhr, status, errorThrown) {
        console.log(errorThrown);
    });
}

function refreshExtrasens() {
    $.ajax({
        url:"api/extrasense_raiting",
        type:"POST"
    }).done(function (data) {
        $("#table_extra_raiting").html(data);
    }).fail(function (xhr, status, errorThrown) {
        console.log(errorThrown);
    });
}

function sendUserNumber(event) {
    console.log("SUBMIT");
    $theform = $("#user_number_form");
    console.log($theform.serialize());
    $.ajax({
        url:"api/user_value",
        type:"POST",
        data:$theform.serialize()
    }).done(function (data) {
        $("#user_block").html(data);

        refreshExtrasens();
        refreshUserHistory();
        refreshExtrasensHistory();

        $("#number_set").click(getExtrasense);
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
        $("#user_block").html(data);
        $("#user_number_form").submit(sendUserNumber);
    }).fail(function (xhr, status, errorThrown) {
        console.log(errorThrown);
    });
}


(function ($,window) {
    console.log("YESS");
    $("#number_set").click(getExtrasense);
})(jQuery,this)