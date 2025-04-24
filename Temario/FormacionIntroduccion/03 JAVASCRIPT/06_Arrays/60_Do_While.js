
    //Creamos un número aleatorio entre 0 y 1.
     // Despues lo multiplicamos por 100 para que esté entre 0-100
    //Lo redondeamos para que sea entero

        // var numero = parseInt(Math.random() * 100);

 // Pedir al usuario que adivine el número generado.
 // Si el ususario se pasa, advertírselo
 // Si el ususario se queda corto, advertírselo
 // Repetir el proceso hasta que el usuario lo adivine
 // Contar el número de intentos requeridos.




// CON WHILE:

//  var numero = 40;
//  var contador = 0;
//  var numero_introducido = prompt("Introduce número: ");

//  while(numero != numero_introducido) {
//    numero_introducido = prompt("Introduce número: ");
//    contador++;

//    if (numero_introducido > numero) {
//      alert("Demasiado alto");
//    }else if (numero_introducido < numero) {
//      alert("Demasiado bajo");
//    }
//  } 

//  alert("CORRECTO¡¡¡, el número era el " + numero + ". Has acertado en " + contador + " intentos.");


// CON DO...WHILE

    var numero = 40;
    var numero_introducido;
    var contador = 0;

    do {
      numero_introducido = prompt("Introduce número: ");
      contador++;
      if (numero_introducido > numero) {
        alert("Demasiado alto");
      }
      if (numero_introducido < numero) {
        alert("Demasiado bajo");
      }
    } while (numero != numero_introducido);


    alert("CORRECTO¡¡¡, el número era el " + numero + ". Has acertado en " + contador + " intentos.");


    
    


  
