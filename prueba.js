//Iniciamos con un mensaje
alert('Bienvenido a las pruebas');

//Pruebas de Formulas mátemáticas sencillas del tipo c = a op b
c = b + 5;
cont = cont + 1;
resultado = 12.7 + 3.14;

//Pruebas de Formulas más complejas del tipo c = a op ( b op d) 
y = 9  *  (2 + x);
resultado = (a - 5) / 2;

//Pruebas de expresiones con estructuras de control

//Ejemplo de for
for (var i = 0; i < 9; i++) {
  cont = cont + 1;
}

// Ejemplo de While
num1 = 0;
num2 = 8.5;
while (num1 < 3) {

  cont = num1 + num2;
}

// Ejemplo de Switch Case
switch (diaSemana){
  case 1:
      alert('Hoy es lunes');
      break;
  case 2:
      alert('Hoy es martes');
      break;
  case 3:
      alert('Hoy es miercoles');
      break;
  case 4:
      alert('Hoy es jueves');
      break;
  case 5:
      alert('Hoy es viernes');
      break;
  case 6:
      alert('Es fin de semana');
      break;
  case 7:
      alert('Es fin de semana');
      break;
  default:
      alert('Ese dia no existe');
      break;
}

//Ejemplo de If
if ( (n == 0) || (n == 1) ) {
  return 1;
} else {
  return (n * factorial);
}