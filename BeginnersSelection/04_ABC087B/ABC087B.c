#include <stdio.h>
 
int
main(){
    int a,b,c,x, i,j,k, count;
    scanf("%d", &a);
    scanf("%d", &b);
    scanf("%d", &c);
    scanf("%d", &x);
    
    x /= 50;
    
    count = 0;
    for (i = 0; i <= a && i*10 <= x; i ++){
        for (j = 0; j <= b && i*10 + j*2 <=x; j ++){
            if ((x - (i*10 + j*2)) <= c){
                count ++;
            }
        }
    }
    
    printf("%d\n", count);
    return 0;
}