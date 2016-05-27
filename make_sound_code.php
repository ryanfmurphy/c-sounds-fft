<?php
    { # template out c code
        ob_start();
        require_once('1.c.php');
        $cCode = ob_get_clean();
    }

    { # build and exec
        file_put_contents('1php.c', $cCode);
        echo "Done make_sound_code\n";

        exec('make 1php');
        echo "Done make 1php\n";

        exec('./1php | ./play_sound.sh');
        echo "Done ./1php\n";
    }
?>
