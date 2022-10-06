
<?php
// Binary Search in PHP
function binarySearch(Array $arr, $item) {
    $low = 0;
    $high = count($arr) - 1;
	$got = false;

	while ($low <= $high) {
		$mid = $low + ($high - $low) / 2;

		if ($arr[$mid] === $item) { 
			$got = true;
			break;
		} else {
			if ($item < $arr[$mid]) { 
				$high = $mid - 1;
			} else { 
				$low = $mid + 1;
			}
		}
	}

	return $got;
}

$array = array(0, 1, 3, 5, 15, 16, 35, 48, 56, 73, 98 );

//for true
$search = 16;
echo binarySearch($array, $search) ? 'Found' : 'Not Found';
echo PHP_EOL;

echo '<br />';

//for false
$search = 6;
echo binarySearch($array, $search) ? 'Found' : 'Not Found';
echo PHP_EOL;

?>