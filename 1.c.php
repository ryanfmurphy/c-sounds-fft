#include <stdio.h>

// USAGE: ./1 | speakerpipe -r 4000 -b
// ALSO COOL: ./1 | speakerpipe -r "44.1 kHz" (sounds weird and rhythmic)

<?php
    $shifts = array(0,9,2,10);
    $n = 0;

    function rotate_array(&$array) {
        $backItem = array_pop($array);
        array_unshift($array, $backItem);
        return $array;
    }

    $nShifts = rand(0,3);
    for ($i=0;$i<$nShifts;$i++) {
        rotate_array($shifts);
    }
?>

int main(){
	int t;
	for (t=0;;t++) {
		putchar(
			//t*((t>>12|t>>8)&63&t>>4)
			t*
            (
                (t >> <?= $shifts[$n]; $n++; ?>
                |t >> <?= $shifts[$n]; $n++; ?>
                )
                & <?= $shifts[$n]; $n++; ?>
                & t >> <?= $shifts[$n]; $n++; ?>
            )
		);
	}
	return 0;
}
