#include <stdio.h>
#include <string.h>

char    S[1000000];
char    str[4][10] = {"dream", "dreamer", "erase", "eraser"};

int
scmp(int n, int size){
    int i;
    for(i = 0; i < 4; i ++){
        if (0 == strncmp(&S[n], &str[i][0], strlen(str[i]))){
            if (n + strlen(str[i]) >= size){
                return 0;
            }
            if (0 == scmp(n + strlen(str[i]), size)){
                return 0;
            }
        }
    }
    return 1;
}

int
main(){
    scanf("%s", &S[0]);
    fprintf(stderr, "S:[%s] len=%d\n", S, strlen(S));

    if (0 == scmp(0, strlen(S))){ 
        printf("YES\n");
        return 0;
    }

    printf("NO\n");
    return 0;
}
