#!/bin/bash

git add .
read -p "Núemro do commit: " i>>j

git commit -m "commit ${j}"

git push origin B-SBPMat
