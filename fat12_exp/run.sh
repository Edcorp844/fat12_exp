#!/bin/bash

#created by Frost Edson,
#bash run.sh, run this command to run everything

printf "\033[41m[+] Executing Makefile\033[0m\n";
make 
printf "\033[42m[+] making executable\033[0m\n";
printf "chmod +x ./build/main.o"
chmod +x ./build/main.o
./build/main.o build/img hello
