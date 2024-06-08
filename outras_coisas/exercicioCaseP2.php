<HTML>
<HEAD>
 <TITLE>New Document</TITLE>
</HEAD>

<BODY bgcolor="black" text="white">
<center>
<h2> Utilizando Condicional com switch()</h2>
<hr><b><font face="arial" size="4" color="white">
<h1> Opcoes: <font face="arial" color="yellow">um, dois, tres, quatro, cinco.</font> Caso contrario ira dar errado. </h1>
<h2> Maximo 5 </h1>

<form method="post">
  <label> Digite a quantidade </label>
  <input type="text" name="qtd"><br><br>
  <input type="submit">
</form>

<?php
//Atribuir um valor numeric qualquer para a quantidade
$qtd = $_POST['qtd'] ;
$qtd_lower = strtolower($qtd);

//Utilizando condicional com switch()
switch ($qtd_lower){
    case 0 :
  echo "$qtd Nao e uma equipe, e necessario pelomenos 1 !";
  break;
  
     case 'um': case 'dois': case 'tres': case 'quatro': case 'cinco':
  echo " A Equipe com $qtd alunos foi aceita !";
  break;

    default:
  echo " '$qtd' Nao e uma quantidade valida";
  break;
  }
  

?>
</center>
</BODY>
</HTML>
