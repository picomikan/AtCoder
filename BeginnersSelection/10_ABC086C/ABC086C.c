#include <stdio.h>
#include <string.h>

#define delta(a,b)  ((a)>(b)?(a)-(b):(b)-(a))

int
canMoved(int t_old, int x_old, int y_old, int t, int x, int y){
    int dt, dx, dy;

    dt = t - t_old;
    dx = abs(x - x_old);
    dy = abs(y - y_old);

    if (dx + dy == dt){
        return 1;
    }

    if (dx + dy > dt){
        return 0;
    }

    if ((dx + dy) % 2 == dt % 2){
        return 1;
    }

    return 0;
}

int
main(){
    int N, i;
    int t=0, t_old, x=0, y=0, x_old, y_old;

    scanf("%d", &N);
    for (i = 0; i < N; i ++){
        t_old = t;
        x_old = x;
        y_old = y;
        scanf("%d %d %d", &t, &x, &y);
        if (!canMoved(t_old, x_old, y_old, t, x, y)){
            printf("No\n");
            return 0;
        }
    }
    printf("Yes\n");
    return 0;
}
