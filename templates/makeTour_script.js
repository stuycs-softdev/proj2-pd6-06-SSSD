window.onload = function () {
    alert ("loaded");
    for (var i=1;i<={{locLen}};i++) {
	strIt = i.toString();
	divName = "myDiv" + strIt
	img = document.getElementById(divName);
	img.onclick = function () {
	    $( "#dialog" ).dialog({modal:true, draggable: true });
	    var modal = $( "#dialog" ).dialog( "option", "modal" );

	};
    };
};
