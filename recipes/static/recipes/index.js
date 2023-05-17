
// Need to setup JQuery

// Need to setup AJAX request for "Favorite" button
// When clicked, the button needs to also toggle to "Unfavorite"

$(document).ready(function() {

    $("button").click(function(){
        $.ajax({url: "demo_test.txt", success: function(result){
            $("#div1").html(result);
        }});
    });
})

