#include <stdio.h>
 
int
main(){
    int n, a, b, i, work, sum=0;
    scanf("%d %d %d", &n, &a, &b);
    for(i=1; i<=n; i++){
        work = i/10000 + (i/1000)%10 + (i/100)%10 + (i/10)%10 + i%10;
        if(a <= work && work <=b){
            sum += i;
        }
    }
    
    printf("%d\n", sum);
    return 0;
}
