<?php
//Quick Sorting in PHP

function quick_sort($array)
 {
	$lower = $great = array();
	if(count($array) < 2)
	{
		return $array;
	}
	$pivot_key = key($array);
	$pivot = array_shift($array);
	foreach($array as $value)
	{
		if($value <= $pivot)
		{
			$lower[] = $value;
		}elseif ($value > $pivot)
		{
			$great[] = $value;
		}
	}
	return array_merge(quick_sort($lower),array($pivot_key=>$pivot),quick_sort($great));
}
 
$array = array(-5, 3, 0, 7, 5, -1, 4, 1 , 9, 2);
echo '<br />';
echo 'Input Array : '.implode(',',$array);
echo '<br />';
$array = quick_sort($array);
echo '<br />';
echo 'After Sorting : '.implode(',',$array);


?>
