#include <stdio.h>
 
int
main(){
    int a,b,c;
    a = getchar();
    b = getchar();
    c = getchar();
    printf("%d\n", a-'0' + b-'0' + c-'0');
    return 0;
}