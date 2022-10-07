<?php
//Selection Sort in PHP

function selection_sort($data)
{
for($i=0; $i<count($data)-1; $i++) {
	$min = $i;
	for($j=$i+1; $j<count($data); $j++) {
		if ($data[$j]<$data[$min]) {
			$min = $j;
		}
	}
    $data = swap_positions($data, $i, $min);
}
return $data;
}

function swap_positions($data1, $left, $right) {
	$old_data = $data1[$right];
	$data1[$right] = $data1[$left];
	$data1[$left] = $old_data;
	return $data1;
}
$array = array(-5, 3, 0, 7, 5, -1, 4, 1 , 9, 2);
echo "Input Array :";
echo "<br />";
echo implode(', ',$array );
echo "<br />";
echo "After Sort :";
echo "<br />";
echo implode(', ',selection_sort($array)). PHP_EOL;
?>