let radio = 140;
let radio2 = 100; 
let radio3 = 50;
let radio4 = 0;
let d = 10;
let xcenter1 = 200;
let ycenter1 = 20;
let expansionRate = 0.5; // Tasa de expansión de la circunferencia

function setup() {
  createCanvas(400, 400);
  background(0, 191, 255);
}

function draw() {
  background("a05d00"); // Limpiar el lienzo en cada frame
  fill(255, 255, 0); // Amarillo
  ellipse(xcenter1, ycenter1, d / 2, d / 2); // Círculo en la parte superior central
  
  drawLines(height/2,2)
  
  drawCircles(xcenter1,ycenter1,expansionRate,height/2);
  drawCircles(width / 2 - 3*d,height/2,expansionRate,height);
  drawCircles(width / 2 + 3*d,height/2,expansionRate,height);
  stroke(0); // Color negro
  strokeWeight(2); // Grosor de la línea
  line(0,height-20, width,height-20); // Línea izquierda
  
    textAlign(CENTER, BOTTOM);

    textSize(20); // Tamaño del texto
  text("Pantalla", width / 2, height); // Mostrar el texto en el centro inferior

}

function drawCircles(xcenter, ycenter, expansionRate, limit) {
  // Circunferencia que se expande y se disipa
  noFill(); // Sin relleno
  stroke(255, 50, 10); // Color rojo
  strokeWeight(2.5); // Grosor de la línea

  // Dibujar las semicircunferencias
  arc(xcenter, ycenter, radio * 2, radio * 2, 0, PI); // Semicircunferencia 1
  arc(xcenter, ycenter, radio2 * 2, radio2 * 2, 0, PI); // Semicircunferencia 2
  arc(xcenter, ycenter, radio3 * 2, radio3 * 2, 0, PI); // Semicircunferencia 3
  arc(xcenter, ycenter, radio4 * 2, radio4 * 2, 0, PI); // Semicircunferencia 4

  // Incrementar los radios para el siguiente frame
  radio += expansionRate;
  radio2 += expansionRate;
  radio3 += expansionRate;
  radio4 += expansionRate;

  // Reiniciar los radios si alcanzan el límite
  if (radio >= limit - ycenter) {
    radio = 0;
  }
  if (radio2 >= limit - ycenter) {
    radio2 = 0;
  }
  if (radio3 >= limit - ycenter) {
    radio3 = 0;
  }
  if (radio4 >= limit - ycenter) {
    radio4 = 0;
  }
}



function drawLines(lineHeight,numSlides) {
  if (numSlides == 1){
  // Lineas horizontales
  stroke(0); // Color negro
  strokeWeight(2); // Grosor de la línea
  line(0 - d, lineHeight, width / 2 - d, lineHeight); // Línea izquierda
  line(width / 2 + d, lineHeight, width, lineHeight); // Línea derecha
  }
  
  if (numSlides == 2){
  // Lineas horizontales
  stroke(0); // Color negro
  strokeWeight(2); // Grosor de la línea
  line(0 , lineHeight, width / 2 - 3*d, lineHeight); // Línea izquierda
  line(width/2-d,lineHeight,width/2+d,lineHeight)
  line(width / 2 + 3*d, lineHeight, width, lineHeight); // Línea derecha

  }
}
