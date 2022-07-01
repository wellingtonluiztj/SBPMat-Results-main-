#!/bin/bash

git add .

echo "número do commit: "
read $number.

git commit -m "commit $number"

git push origin B-SBPMat
