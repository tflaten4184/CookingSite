
// Need to setup JQuery

// Need to setup AJAX request for "Favorite" button
// When clicked, the button needs to also toggle to "Unfavorite"

$(document).ready(function() {
    console.log("ready");

    $("#fav-btn-container").on("click", "#btn-fav-js", function(e){
        console.log("fav clicked");
        e.preventDefault();
        var recipeId = $(this).data("recipe-id");
        console.log("recipeId is ", recipeId)
        var url = $(this).data("url")
        console.log("url will be ", url)
        $.ajax({
            type: 'POST',
            url: url, // **** Replaced this by passing data from HTML, url function
            data: {
                csrfmiddlewaretoken: window.CSRF_TOKEN,
                recipeId: recipeId,
                action: 'post'
            },
            success: function(json){
                if (json.success === true) {
                    console.log("success")
                    $("#fav-btn-container").load(document.URL + ' #fav-btn-container > *');
                } else {
                    console.log("fail")
                    console.log(json)
                    console.log(json.success)

                }
        }});
    });
})

