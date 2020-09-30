#include <stdio.h>

int
main(){
    int n, a[256], i, j, sum_a, sum_b;
    scanf("%d", &n);
    for(i=0; i<n; i++){
        scanf("%d", &a[i]);
    }

    //sort
    for(j=n; j >=1; j--){
        for(i=1; i< j; i++){
            if (a[i-1] > a[i]){
                //swap
                int tmp = a[i];
                a[i] = a[i-1];
                a[i-1] = tmp;
            }
        }
    }

    sum_a = 0;
    sum_b = 0;
    for(i=0; i<n; i++){
        fprintf(stderr, "%d:%d\n", i, a[i]);
        if ((i & 1) == 0){
            // 偶数
            sum_a += a[n - 1 - i];
        }
        else{
            sum_b += a[n - 1 - i];
        }
    }
    printf("%d\n", sum_a - sum_b);
    return 0;
}
