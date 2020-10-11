#include <stdio.h>

int
main()
{
  int N;  // 26 or 5
  int Q = 0;        // クエリ回数 MAX
  int count = 0;    // クエリ回数
  char c[26] = {0}; // 26個の文字
  int i, j;
  char s[256];

  scanf("%d%d", &N, &Q);
  // 最初は'A'から順に並べておく
  for (i = 0; i < N; i ++){
    c[i] = 'A' + i;
  }
  
  //　ソート
  for (i = N; i > 0; i --){
    // 0...i までの最大を求める。
    for (j = 0; j < i - 1; j ++){
      // クエリ
      if (++count > Q)  return -1;
      printf("? %c %c\n", c[j], c[j + 1]);
      fflush(stdout);
      scanf("%s", s);
      fprintf(stderr, "Query: %c %c %c\n", c[j], s[0], c[j + 1]);

      if (s[0] == '>'){
        // swap
        char tmp = c[j + 1]; c[j + 1] = c[j]; c[j] = tmp;
      }
    }
  }
  
  // !ans
  printf("! ");
  for (i = 0; i < N; i ++)  printf("%c", c[i]);
  printf("\n");
  fflush(stdout);
  return 0;
}
