$(".button-element-carousel").click(sendInfoReadMore)



function sendInfoReadMore(){


    
    var values_div = $(this).parent()

    var name_book = values_div.find(".text-element-carousel-name").text() 

    var author_book = values_div.find(".text-element-carousel-author").text() 

    var volume_book =  values_div.find(".text-element-carousel-volume").text() 

    var edition_book =  values_div.find(".text-element-carousel-edition").text() 

    var synopsis_book =  values_div.find(".text-element-carousel-synopsis").text()
    
    var img_url_book =  values_div.find(".text-element-carousel-img_url").text()


    
    data = {

        name:name_book,
        author:author_book,
        volume:volume_book,
        edition:edition_book,
        synopsis:synopsis_book,
        url_image:img_url_book

    }

    console.log(data)
    

    $.post("http://localhost:3000/persist_read_more",data).fail(function(){console.log("FAIL....")}).done(


    function(){

        console.log("DONE....");

    }
    )

    }
