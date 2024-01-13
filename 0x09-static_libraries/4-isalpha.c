#include "main.h"

int _isalpha(int c)
{
    return ((_islower(c) || _isupper(c)) ? 1 : 0);
}

