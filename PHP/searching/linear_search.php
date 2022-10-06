<?php
//Linear searching in PHP

function linearSearch(Array $arr, $item) {
    foreach ($arr as $val) { 
        if($val === $item)
            return true; 
    }
    return false;
}


$countries = array('pakistan', 'india', 'turkey', 'bangladesh', 'dubai', 'iran', 'china');

//for true
$search = 'turkey';
echo linearSearch($countries, $search) ? 'Exist' : 'not Exist';
echo PHP_EOL; 
echo '<br />';

//for false
$search = 'england';
echo linearSearch($countries, $search) ? 'Exist' : 'not Exist';
echo PHP_EOL;

?>