#include <stdio.h>

int
main(){
    int N, i, a, cnt, min = -1;
    scanf("%d", &N);
    for (i = 0; i < N; i ++){
        scanf("%d", &a);
        cnt = 0;
        while(a != 0){
            if ((a & 1) != 0){
                break;
            }
            cnt ++;
            a >>= 1;
        }
        if (cnt < min || min == -1) min = cnt;
    }
    printf("%d\n", min);
    return 0;
}