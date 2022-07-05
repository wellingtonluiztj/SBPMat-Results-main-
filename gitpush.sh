#!/bin/bash

git add .
 
git log | grep "commit"

read -p 'numero do commit: ' number

git commit -m "commit $number"

git push origin B-SBPMat
