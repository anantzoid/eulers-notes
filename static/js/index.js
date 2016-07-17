(function() {
    console.log("herer");
    $('.fetchData').fileupload({
        dataType: 'json',
        done: function (e, data) {
            $.each(data.result.files, function (index, file) {
                $('<p/>').text(file.name).appendTo(document.body);
            });
        }
    });

    $(".filename-tag-link").on("click", function(e){
        e.preventDefault();
    	var file_id = $(this).data("id");
    	$.ajax({
    		url: '/get_data?file='+file_id,
    		success: function(response) {
    			
    		}
    	})
    });

    function highlight_text() {
        console.log("here");
        var txt = $(.textarea).html();
        for(var key in entities) {
            txt.replace(key, "<span class='highlight'>"+key+"</span>");
        } 
        $(this).html(txt);
        console.log(txt);
    }
})();
