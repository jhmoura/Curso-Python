#!/bin/bash
echo
echo "###############################"
echo "Criando arquivos de exercícios"
echo "###############################"
echo
echo "Quantos arquivos devem ser criados?: "
read n1
echo "Qual a extensão dos arquivos?: "
read e1
for i in $(seq $n1)
do
touch $i.$e1
done

echo "###############################"
echo "      Arquivos Criados         "
echo "###############################"