var names = []


var tableRegisters = $(".div-names")


for (var i=0; i < tableRegisters.find(".text-element-carousel-name").length; i++) {
  // Look no need to do list[i] in the body of the loop

  names.push({name:tableRegisters.find(".text-element-carousel-name")[i].innerHTML})
  console.log("Looping: index ", i, "item: " + tableRegisters.find(".text-element-carousel-name")[i].innerHTML);
}





//tableRegisters.each(function(){names.push({name:$(this).find(".text-element-carousel").text()[0]})})

var searchInput = $(".input-search-bar");

var suggestionsPanel = $(".suggestions");

var buttonSearch = $(".button-confirm-search")


$(".button-confirm-search").click(searchConfirm)



function searchConfirm () {var text = $(".input-search-bar").val()

dados = {name_book:text}

    $.post("http://localhost:3000/results",dados).fail(function(){console.log("FAIL....")}).done(




    function(){

        console.log("DONE....");
        location.reload();

    }
    )


    

}



searchInput.on("input", function(){


    console.log(names)


    
    tableRegisters.each(function(){

        
        if ($(this).find(".text-element-carousel").text()!=$(".input-search-bar").val()){


            $(this).show()


        }



    
    
    
    
    
    })
    
    
    
    
    
    suggestionsPanel.text('')

    const input = searchInput.val()



    if(input!=""){


    const input = searchInput.val()


    var suggestions = names.filter(function(name){


        var digitado = input.toLowerCase()
    
        var comparavel = name.name.toLowerCase().substr(0,digitado.length)
    
        
        return digitado==comparavel


        //return country.name.toLowerCase().startsWith(input)

    })



  
    suggestions.forEach(function(suggested){

        var singleSuggestion = $('<div></div>').text(suggested.name).click(function(){
            
            searchInput.val(suggested.name)

            suggestionsPanel.text('')

        });

        singleSuggestion.text(suggested.name)

        suggestionsPanel.append(singleSuggestion)


    });}

})




searchInput.on("focus", function(){


    
    tableRegisters.each(function(){


        
        
        if ($(this).find(".text-element-carousel-name").text()!=$(".input-search-bar").val()){


            $(this).show()


        }

    
    })
    
    
    
    
    
    suggestionsPanel.text('')

    const input = searchInput.val()



    if(input!=""){


    const input = searchInput.val()


    var suggestions = names.filter(function(name){


        var digitado = input.toLowerCase()
    
        var comparavel = name.name.toLowerCase().substr(0,digitado.length)
    
        
        return digitado==comparavel


        //return country.name.toLowerCase().startsWith(input)

    })



  
    suggestions.forEach(function(suggested){

        var singleSuggestion = $('<div></div>').text(suggested.name).click(function(){
            
            searchInput.val(suggested.name)

            suggestionsPanel.text('')

        });

        singleSuggestion.text(suggested.name)

        suggestionsPanel.append(singleSuggestion)


    });}

})



$(".input-search-bar").on("focusout",function(){


    setTimeout(function(){suggestionsPanel.text("")},500)
    

})