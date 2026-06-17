[23bcs164@mepcolinux itt]$cat pat.c
#include <stdio.h>

int main() {
   int n = 5;
   for (int i = 0; i < n + 1; i++) {
      for (int j = n - i + 1; j <= n; j++) {
         printf("%d ", j);
      }
      printf("0");
      for (int j = n; j >= n - i + 1; j--) {
         printf(" %d", j);
      }
      printf("\n");
   }
   return 0;
}
[23bcs164@mepcolinux itt]$./a.out
0
5 0 5
4 5 0 5 4
3 4 5 0 5 4 3
2 3 4 5 0 5 4 3 2
1 2 3 4 5 0 5 4 3 2 1
