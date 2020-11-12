#!/bin/sh

a=0
while [ $a -lt 120 ]
do
    #echo $a
    python ./B_question.py $a -s < aaa | $1 > aaa
    a=`expr $a + 1`
done
