// This is a scratch file for testing random c code
// compile and run with gcc test.c -o test && ./test 

#include <stdio.h>
#include <string.h>

#define DIRSIZ 14

static char *skipelem(char *path, char *name)
{

    // 1 skip initial slashes for np
    // 2 go through letters
    //      if /, go to 3
    //      if 0, go to 3
    //      if dirsiz-1, go to 2.9
    //      normal: add letter to np and n
    // 2.9 skip until slash or 0, go to 3
    // 3 add 0 to end of n; skip trailing slashes for np, return np

    // TODO
    // skip leading slashes
    char *new_path = path;
    while (new_path[0] == '/') {
        new_path += sizeof(char);
    }

    // get name
    for (int i=0; i < DIRSIZ; i++) {
        // name too long, cut the rest off
        if (i == DIRSIZ - 1) {
            name[i] = 0;
            while (new_path[0] != '/' && new_path[0] != 0) {
                new_path += sizeof(char);
            }
            break;
        }
        // slash or null reached, name is finished
        if (new_path[0] == 0 || new_path[0] == '/') {
            name[i] = 0;
            break;
        } 
        // normal case: add to name and increment new_path
        name[i] = new_path[0];
        new_path += sizeof(char);
    }

    // skip ending slashes
    while (new_path[0] == '/') {
        new_path += sizeof(char);
    }

    return new_path;
}

int main() {
    char* path = "aa/c/bb";
    char name[DIRSIZ];
    char* new_path = skipelem(path, name);
    printf("path %s name %s\n", new_path, name);
    char* new_path2 = skipelem(new_path, name);
    printf("path %s name %s\n", new_path2, name);
    char* new_path3 = skipelem(new_path2, name);
    printf("path %s name %s\n", new_path3, name);
    char* new_path4 = skipelem(new_path3, name);
    printf("path %s name %s\n", new_path4, name);
    // char* new_path4 = skipelem(new_path3, name);
    // char* new_path5 = skipelem(new_path4, name);
    // char* new_path6 = skipelem(new_path5, name);
    // char* new_path7 = skipelem(new_path5, name);

    // printf("path %s -> %s; path %s; %s %s\n", path, name, new_path, new_path2, new_path3, n`);
    return 0;
}