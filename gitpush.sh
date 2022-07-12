#!/bin/bash

git add .
 
git log | head

read -p 'numero do commit: ' number

git commit -m "commit $number"

git push origin B-SBPMat
