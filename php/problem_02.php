<?php
$fib_sequence = [0, 1];
$last_number = 1;
$i = 2;
while (true) {
    $last_number = $fib_sequence[$i-1] + $fib_sequence[$i-2];
    if ($last_number > 4000000) {
        break;
    }
    $fib_sequence[] = $last_number;
    $i++;
}
echo array_sum(array_filter($fib_sequence, static function($x) {
    return $x % 2 === 0;
}));