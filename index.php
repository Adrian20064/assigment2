<?php

echo "<h1>Assigment #2</h1>"; #Title of the page
echo "<h2>Adrian Carrasco</h2>"; #my name
if (isset($_GET['a']) && isset($_GET['b']) && isset($_GET['c'])) { #get the values from thhe python
    $a = $_GET['a']; 
    $b = $_GET['b'];
    $c = $_GET['c'];

    $command = escapeshellcmd("python3 /var/www/html/calculate.py $b $a $c"); #create a varible inside the python 
    $output = shell_exec($command); #execute the variable

    echo "<pre>" . nl2br($output) . "</pre>"; #this will put line breaks in the output 
} else {
?>
<form method="get">
    A: <input type="text" name="a"><br> 
    B: <input type="text" name="b"><br>
    C: <input type="text" name="c"><br>
    <input type="submit" value="Calculate">
</form>
<?php
}
?>