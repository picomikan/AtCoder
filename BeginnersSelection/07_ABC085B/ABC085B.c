#include <stdio.h>

int
main(){
    int n, a[256], i, j, same;
    scanf("%d", &n);
    for(i=0; i<n; i++){
        scanf("%d", &a[i]);
    }

    //sort
    same = 0;
    for(j=n; j >=2; j--){
        for(i=1; i< j; i++){
            if (a[i-1] > a[i]){
                //swap
                int tmp = a[i];
                a[i] = a[i-1];
                a[i-1] = tmp;
            }
        }
    }

    for(j=n; j >=2; j--){
        if (a[j - 1] == a[j - 2]){
            same ++;
        }
    }

    printf("%d\n", n - same);
    return 0;
}

