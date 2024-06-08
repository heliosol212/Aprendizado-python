<HTML>
<HEAD>
 <TITLE>New Document</TITLE>
</HEAD>
<BODY bgcolor="black" text="white">
<center>
<h1>Exercicio - PARES de 0 a 100</h1>
<h2> Utilizando Loop com for() </h2>
<hr><b><font face= "arial" size="4" color="white">

<form method="post">
<label> digite o numero inicial 1
<input type="text" name="i">
<label> digite o numero inicial 2
<input type="text" name="i2">
<input type="submit">
 <br><br>

<?php
//inicial um loop que será executado enquanto.
//for ($i = 2; $i <= 100; $i = $i + 2 ) // inicio; fim; intervalo;


for ($i = $_POST['i']; $i <= 100; $i = $i + 2)
{
echo "$i -  ";
}
echo "<br> Fim ! " ;

echo"
<hr><b><font face= 'arial' size='4' color='white'>
<h1>Exercicio - IMPARES de 0 a 100</h1>
<h2> Utilizando Loop com for() </h2>
<hr><b><font face= 'arial' size='4' color='white'> ";


for ($i2 = $_POST['i2']; $i2 <=100; $i2 = $i2 + 2){
echo "$i2 -  ";
}
echo"<br> Fim !";
?>


</BODY>
</HTML>
