function ajax(url,data,foo){
	var xmlhttp=new XMLHttpRequest();
	xmlhttp.onreadystatechange=function(){
		if (xmlhttp.readyState==4 && xmlhttp.status==200) {
			foo(xmlhttp.responseText);
		};
	};
	xmlhttp.open('POST',url,true);
	xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
	xmlhttp.send('shell='+data);
}

function keyProcess(ev){
	var input=document.querySelector('input');
	if (ev.keyCode==13) {
		input.parentNode.innerHTML=input.value;
		if (input.value=='clear') {
			document.querySelector('.terminal').innerHTML='';
		};
		ajax('http://127.0.0.1/shell.php',input.value,resultProcess);
	};
}

function resultProcess(res){
	var termin=document.querySelector('.terminal');
	if (res) {
		var tmp1=document.createElement("div");
		tmp1.innerHTML='<pre>'+res+'</pre>';
		termin.appendChild(tmp1);
	}
	var tmp2=document.createElement("div");
	tmp2.innerHTML="localhost:~ eular$ <span><input name=\"shell\"></span>";
	termin.appendChild(tmp2);

	terminal();
}
function setLayout(){
	var termin=document.querySelector('.terminal');
	if(termin.offsetHeight>=343){
		termin.style.top=(340-termin.offsetHeight)+'px';
	}
}

var terminal=function(){
	setLayout();
	var input=document.querySelector('input');
	input.size=55;
	input.focus();
	input.addEventListener('keypress',keyProcess);
}

window.addEventListener('load',function(){
	var time=new Date();
	document.querySelector('span').innerHTML=time;
	terminal();
});