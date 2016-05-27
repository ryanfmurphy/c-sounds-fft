
#call php with vars
#popen executing the c code
import random
import subprocess
import json

vars = json.dumps({'which': random.randint(1,2),
        'shifts': [0,19,2,10]})

subprocess.call(['php', 'make_sound_code.php', vars])
our_process = subprocess.Popen(['./1php'])
stdout,stderr = our_process.communicate()

with open('test.pcm','wb') as fh:
        for x in range(1):
            data = stdout.read(1024)
            fh.write(data)
            sys.stdout.write(data)

"""


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
"""
