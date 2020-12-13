<?php

echo "Petroleum Marketing Monthly\n";

// var entry ------------------------
/* $questions = [
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
// print_r(readline_info());
 */
// -------------------------------------
$dir = "TXT_DATA";

function dirToArray($dir) {
    $txt_file_list = array();

    $cdir = scandir($dir);
    foreach ($cdir as $key => $value)
   {
      if (!in_array($value,array(".","..")))
      {
         if (is_dir($dir . DIRECTORY_SEPARATOR . $value))
         {
            $result[$value] = dirToArray($dir . DIRECTORY_SEPARATOR . $value);
         }
         else
         {
            $result[] = $value;
         }
      }
   }
  
   return $result;
}

$txt_list = dirToArray($dir);

print_r($txt_list);