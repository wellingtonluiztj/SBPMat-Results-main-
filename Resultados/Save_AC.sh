#!/bin/bash


read -p 'Valor de Salinidade: ' salinidade
echo "Salinidade = $salinidade" >> Angulos.txt
python3 Artigo_AC.py >> Angulos.txt
