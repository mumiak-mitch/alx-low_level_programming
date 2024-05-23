#!/bin/bash

echo -e '#include <stdio.h>\nint rand() { return 9; }\nvoid srand(unsigned int seed) {}' > rand.c
gcc -fPIC -shared -o rand.so rand.c
rm rand.c

LD_PRELOAD=./rand.so ./gm 9 8 10 24 75 9

