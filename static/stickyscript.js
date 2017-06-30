var stickyColor;
var noteid;
/* Selecting Color*/
$( "#dropdown" ).change(function() {
    if($("#dropdown").val()==="pink"){
        //$(this).css({"background-color": "pink"});
        $("input").css({"background-color": "pink"});
    }
    if($("#dropdown").val()==="orange"){
        //$(this).css({"background-color": "pink"});
        $("input").css({"background-color": "orange"});
    }
    if($("#dropdown").val()==="yellow"){
        //$(this).css({"background-color": "pink"});
        $("input").css({"background-color": "yellow"});
    }
});

/*$("ul").on("click", "span", function(event){
	$(this).parent().fadeOut(500,function(){
		$(this).remove();
	});
	event.stopPropagation();
});*/


/*$("ul").on("click", "span", function(event){
	noteid = $(this).parent().attr('id')
    console.log(noteid);
    $.ajax({
        type:"GET",
        url:$SCRIPT_ROOT+"/deletenotes",
        data:{valid:noteid},
        success:function (notes) {
            console.log('data sent');

        }

    });
	});*/

/*