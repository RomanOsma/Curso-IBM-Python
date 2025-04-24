
<h3 id="demo"></h3>
<h3 id="demo2"></h3>
<script>
function funcionPrincipal(callback1, callback2, callback3){
    //código de la función principal
    callback1();
    //más código de la función principal
    var miVar = setInterval(function(){ callback2() }, 1000);
    //más código de la función principal
    var miVar2 = setInterval(function(){ callback3() }, 3000);
    //más código si fuera necesario
}
 
function callback1(){
        alert('primer callback');
    }
 
function callback2(){
        var d = new Date();
        var t = d.toLocaleTimeString();
        document.getElementById("demo").innerHTML = t;  
    }
 
function callback3(){
        document.getElementById("demo2").innerHTML = 'Esto es el callback3';
    }   
 
funcionPrincipal(callback1, callback2, callback3);
</script>



