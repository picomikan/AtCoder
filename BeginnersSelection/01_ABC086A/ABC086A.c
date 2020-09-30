#include <stdio.h>
 
int
main(){
    int     a, b;
    scanf("%d", &a);
    scanf("%d", &b);
    if (((0x01 & a) == 0) || ((0x01 & b) == 0)){
        printf("Even\n");
    }
    else{
        printf("Odd\n");
    }
    return 0;
}