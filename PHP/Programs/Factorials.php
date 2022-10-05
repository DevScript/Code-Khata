<?php  

//User input value
$num = 6;

//initial values
$factorial = 1;  

//Count Factorial
for ( $x=$num; $x>=1; $x--)   
{  
  $factorial = $factorial * $x;  
}  

echo "Factorial of $num is $factorial";  

?> 