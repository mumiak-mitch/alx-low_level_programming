#include "main.h"
#include <stddef.h>

char *_strpbrk(char *s, char *accept)
{
    while (*s != '\0')
    {
        while (*accept != '\0')
        {
            if (*s == *accept)
                return s;
            accept++;
        }
        s++;
    }

    return NULL;
}

