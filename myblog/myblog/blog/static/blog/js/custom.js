$(document).ready(function(){
	$.get("/article/edit/(?P<pk>[0-9]+)/$", function(data, status){
		if(status == 'success')
		    $("#title").val(data['title']);
		    $("#body").val(data['body']);
		    $("#error").text(data['error'])
		else
		    $("#error").text("文章内容加载失败！")
	});

	$("#submit").click(function(){
        $.post("/article/edit/(?P<pk>[0-9]+)/$",
        {
            title:title,
            body:body,
            category:category,
            tags:tags
        },
        function(data, status){
            if(status == 'success')
                $("#title").val(data['title']);
                $("#body").val(data['body']);
            else
                $("#error").text("文章内容加载失败！")
        });
	});
});