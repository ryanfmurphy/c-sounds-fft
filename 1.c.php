#include <stdio.h>

// USAGE: ./1 | speakerpipe -r 4000 -b
// ALSO COOL: ./1 | speakerpipe -r "44.1 kHz" (sounds weird and rhythmic)

<?php
    if ($vars->which == 1) {
        $n = 0;

        function rotate_array(&$array) {
            $backItem = array_pop($array);
            array_unshift($array, $backItem);
            return $array;
        }

        $vars->nShifts = rand(0,3);
        for ($i=0;$i<$vars->nShifts;$i++) {
            rotate_array($vars->shifts);
        }

        function shift_array() {
            global $vars, $n;
            $result = $vars->shifts[$n];
            $n++;
            return $result;
        }
?>

int main(){
	int t;
	for (t=0;;t++) {
		putchar(
			//t*((t>>12|t>>8)&63&t>>4)
			t*
            (
                (t >> <?= shift_array() ?>
                |t >> <?= shift_array() ?>
                )
                & <?= shift_array() ?>
                & t >> <?= shift_array() ?>
            )
		);
	}
	return 0;
}
<?php
    }
    elseif ($vars->which == 2) {
        echo file_get_contents('2.c');
    }
    else {
        throw new Exception("Unexpected 'which' value");
    }
?>
