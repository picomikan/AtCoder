#include <stdio.h>

int
main()
{
  int a,b,c;
  char s[256];
  scanf("%d%d%d%s", &a, &b, &c, &s[0]);
  printf("%d %s\n", a+b+c, s);
  return 0;
}
