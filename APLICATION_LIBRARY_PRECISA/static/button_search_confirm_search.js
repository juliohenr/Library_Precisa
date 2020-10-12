function searchConfirm () {


    var text = $(".input-search-bar").val()


    dados = {name_book:text}

    $.post("http://localhost:3000/results",dados).fail(function(){console.log("FAIL....")}).done(




    function(){

        console.log("DONE....");
        location.reload();

    }
    )


    

}
