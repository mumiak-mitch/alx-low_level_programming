#!/bin/bash

# Compile each .c file to a corresponding .o file
gcc -Wall -Werror -Wextra -pedantic -std=gnu89 -c *.c

# Create the static library liball.a
ar -rc liball.a *.o

# Clean up the .o files
rm *.o

