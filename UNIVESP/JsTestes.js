function soma(){
   numero1 = 2;
   numero2 = 5;
   var soma = 0;
   soma = numero1+numero2;
   return soma;   
}

function mostraSituação(media){
   if (media >= 6){
      alert("Aprovado");
   }
   else{
      alert("Reprovado");
   }
}

function entrada(){
   nome = prompt("Nome: ");
   return nome;
}

function alerta(){
   alert("Alerta!")
}

function HabilitarCampo(opcao){
   if(opcao){
      document.formulario.nome.disabled = false;
   }
   else{
      document.formulario.nome.value = "";
      document.formulario.nome.disabled = true;
   }
}

function CalculaImc(){
   peso = parseFloat(document.CalculoIMC.peso.value);
   altura = parseFloat(document.CalculoIMC.altura.value);
   IMC = peso / (altura*altura);
   IMC = IMC.toFixed(2);
   alert("Seu imc é: " + IMC);
}