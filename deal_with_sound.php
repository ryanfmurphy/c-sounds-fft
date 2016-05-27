<?php
    $vars = array(
        'which' => rand(1,2),
        'shifts' => array(0,19,2,10)
    );
    echo "Got vars\n";

    function runCommandInBackground($cmd) {
        exec("bash -c 'exec nohup setsid $cmd > /dev/null 2>&1 &'");
    }

    { #todo make background task
        require_once('make_sound_code.php');
        /*runCommandInBackground(
            "php make_sound_code.php "
            .escapeshellarg(json_encode($vars))
        );*/
    }

    { # log
        { # connect to db
            $dbPath="db.sqlite";
            $db = new PDO("sqlite:$dbPath");
        }

        { # ask rating
            echo "How awesome was that [0-9]?\n";
            #$rating = (int)readline();
            $rating = 3;
        }

        { # save to db - #todo get rating later
            { # sound
                $name = 'test';
                $db->query("
                    insert into sound
                        (id, name, rating)
                    values
                        (
                            '".uniqid()."',
                            '$name',
                            $rating
                        );
                ");
                $soundId = $db->lastInsertId();
            }

            { # vars
                foreach ($vars as $name => $val) {
                    $db->query("
                        insert into var
                            (id, name, val, sound_id)
                        values
                            (
                            '".uniqid()."',
                            '$name',
                            '".json_encode($val)."',
                            '$soundId'
                            );
                    ");
                }
            }
        }
    }
?>
