#include <stdio.h>

#define SWAP(x, y) {int tmp = (x); (x) = (y); (y) = tmp;}

int N;  // 26 or 5
int Q = 0;
int count = 0;
char c[26];
char cache[26][26] = {0};

void
add_cache(char C1, char C2, char s){
  int i, j;
  char s2 = (s == '>')? '<':'>';

  cache[C1 - 'A'][C2 - 'A'] = s;
  cache[C2 - 'A'][C1 - 'A'] = s2;

  // 自明なものを更新
  for (i = 0; i < N; i ++){
    // ex. C1 < C2 and C2 < x  => C1 < x
    if ((cache[C1 - 'A'][i] == 0) && (cache[C2 - 'A'][i] == s)){
      add_cache(C1, i + 'A', s);
    }
    if ((cache[C2 - 'A'][i] == 0) && (cache[C1 - 'A'][i] == s2)){
      add_cache(C2, i + 'A', s2);
    }
  }
}

int
cmp(char C1, char C2){
  // 0: '<', 1: '>'
  if (cache[C1 - 'A'][C2 - 'A'] == 0){
    char s[8];

    // クエリ
    //if (++count > Q)  return -1;
    printf("? %c %c\n", C1, C2);
    fflush(stdout);
    scanf("%s", s);
    fprintf(stderr, "Query: %c %c %c\n", C1, s[0], C2);
    
    // キャッシュに追加
    add_cache(C1, C2, s[0]);
  }
  return (cache[C1 - 'A'][C2 - 'A'] == '>');
}

void
merge(char *a0, int sizea, char *b0, int sizeb, char *c){
  char a[13], b[13];
  int i, j;
  for (i = 0; i < sizea; i ++) a[i] = a0[i];
  for (i = 0; i < sizeb; i ++) b[i] = b0[i];

  i = 0, j = 0;
  while (i + j < sizea + sizeb){
    if (i >= sizea){
      *c++ = b[j++];
      continue;
    }
    if (j >= sizeb){
      *c++ = a[i++];
      continue;
    }
    if (cmp(a[i], b[j])){
      *c++ = b[j++];
    }
    else{
      *c++ = a[i++];
    }
  }
}

void
msort(char *d, int size){
  int i, j;
  if (size == 1){
    // NOP
  }
  else if (size == 2){
    if (cmp(d[0], d[1])){
      SWAP(d[0], d[1]);
    }
  }
  /*
  else if (size == 5){
    // 先頭3つをソート
    msort(d, 3);
    // d[3]を２分探索で配置
  }*/
  else{
    int m = (size + 1) / 2;
    msort(&d[0], m);
    msort(&d[m], size - m);
    merge(&d[0], m, &d[m], size - m, d);
  }
}

int
main()
{
  int i;

  scanf("%d%d", &N, &Q);
  // 最初は'A'から順に並べておく
  for (i = 0; i < N; i ++){
    c[i] = 'A' + i;
  }
  
  //　ソート
  msort(&c[0], N);
  
  // !ans
  printf("! ");
  for (i = 0; i < N; i ++)  printf("%c", c[i]);
  printf("\n");
  fflush(stdout);
  return 0;
}