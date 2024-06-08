<HTML>
<HEAD>
 <TITLE>New Document</TITLE>
 <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</HEAD>

<BODY bgcolor="black" text="white">
<center>
<h2> Utilizando Condicional com switch()</h2>
<hr><b><font face="arial" size="4" color="white">

<?php


//atribuir um valor numeric qualquer para a quantidade
$dia= 1;
//utilizando a condicional com switch()
echo ' Que dia e hoje? <br>';
  switch ($dia)
{
    case 1:
  echo "Domingo !";
  break;

    case 2:
  echo "Segunda-feira !";
  break;

    case 3:
  echo "Terca-feira !";
  break;

    case 4:
  echo "Quarta-feira !";
  break;

    case 5:
  echo "Quinta-feira !";
  break;

    case 6:
  echo "Sexta-feira !";
  break;

    case 7:
  echo "Sabado !";
  break;
  
  default:
  echo "Nao e um dia de semana";
  break;
}
?>
</BODY>
</HTML>
