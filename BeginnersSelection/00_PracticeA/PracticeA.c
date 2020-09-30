#include <stdio.h>
 
int
main(){
    int     a, b, c;
    char    str[256];
    scanf("%d", &a);
    scanf("%d", &b);
    scanf("%d", &c);
    scanf("%s", str);
    printf("%d %s\n", a+b+c, str);
    return 0;
}
