// This is a scratch file for testing random c code
// compile and run with gcc test.c -o test && ./test 

#include <stdio.h>
#include <string.h>

typedef struct {
    u_int32_t type;
    char data[14];
} DataStruct;

int main() {
    const char* source = "Hello, world!";
    DataStruct myStruct;

    strncpy(myStruct.data, source, 14);
    myStruct.data[sizeof(myStruct.data) - 1] = '\0';

    printf("Copied string: %s\n", myStruct.data);
    return 0;
}
