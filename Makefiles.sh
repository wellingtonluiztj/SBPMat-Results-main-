#!/bin/bash

for i in {1..5};do
	mkdir R-$i
	cd R-$i
	echo>file$i.txt	
	for j in 0.00 0.05 0.10 0.50 1.00 1.72;do
		mkdir $j
		cd $j
		echo>file$j.txt
		cd ..
done
cd ..
done


