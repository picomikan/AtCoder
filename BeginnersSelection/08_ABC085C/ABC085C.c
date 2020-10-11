#include <stdio.h>

int
main(){
    int     n, y; // y <= 20000000
    int     i; // 10000yen
    int     j; // 5000yen
    int     k; // 1000yen
    long    yy;

    scanf("%d %ld", &n, &yy);
    if (yy % 1000){
        fprintf(stderr, "yy = %d\n", yy);
        printf("-1 -1 -1\n");
        return 0;
    }

    y = yy / 1000;
    fprintf(stderr, "y = %d\n", y);

    for (i = 0; i <= n && i*10 <= y; i++){
        for (j = 0; j <= (n - i) && i*10 + j*5 <= y; j++){
            k = n - i - j; 
            if (i*10 + j*5 + k == y){
                printf("%d %d %d\n", i, j, k);
                return 0;
            }
        }
    }

    printf("-1 -1 -1\n");
    return 0;
}
