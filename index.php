<?php

echo "Petroleum Marketing Monthly\n";

$questions = [
    "Question one: ",
    "Question two: ",
    "Question three "
];
//get 3 commands from user
for ($i=0; $i < 3; $i++) {
        // $line = readline("Command: ");
        $line = readline($questions[$i]);
        readline_add_history($line);
}

//dump history
print_r(readline_list_history());

//dump variables
print_r(readline_info());