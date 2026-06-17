[23bcs164@mepcolinux datatype]$cat mat.c
#include<stdio.h>
#include<stdlib.h>

int main(){
   int r,c;
   printf("Enter the row and column for the matrix :");
   scanf("%d %d",&r,&c);
   int mat[r][c];
   for (int i =0;i<r;i++){
      for(int j=0;j<c;j++){
         scanf("%d",&mat[i][j]);
      }
   }
   for (int i =0;i<r;i++){
      for(int j=0;j<c;j++){
        //printf("%3d",mat[i][j]);
     }
     //printf("\n");
   }
   for(int i =0;i<r;i++){
     for(int j=0;j<c;j++){
      if( 0 == mat[i][j]){
         for(int k=0;k<r;k++){
            mat[k][j]=0;
            //mat[i][k]=0;
         }
         for(int row = 0;row < c;row++){
            mat[i][row]=0;
         }

      }
   }}
   for (int i =0;i<r;i++){
       for(int j=0;j<c;j++){
         printf("%3d",mat[i][j]);
    }
  printf("\n");
  }
   return 0;
}
[23bcs164@mepcolinux datatype]$cat p1.c
#include<stdio.h>
#include<stdlib.h>

int main(){
   int r,c;
   printf("Enter the row and column for the matrix :");
   scanf("%d %d",&r,&c);
   int mat[r][c];
   for (int i =0;i<r;i++){
      for(int j=0;j<c;j++){
         scanf("%d",&mat[i][j]);
      }
   }
   for (int i =0;i<r;i++){
      for(int j=0;j<c;j++){
        //printf("%3d",mat[i][j]);
     }
     //printf("\n");
   }
   for(int i =0;i<r;i++){
     for(int j=0;j<c;j++){
      if( 0 == mat[i][j]){
         for(int k=0;k<r;k++){
            if(mat[k][j] != 0) {
                mat[k][j] = -9999;
            }
         }
         for(int row = 0;row < c;row++){
            if(mat[i][row] != 0) {
                mat[i][row] = -9999;
            }
         }
      }
   }}
   for (int i =0;i<r;i++){
       for(int j=0;j<c;j++){
         if (mat[i][j] == -9999) {
             mat[i][j] = 0;
         }
         printf("%3d",mat[i][j]);
    }
    printf("\n");
  }
   return 0;
}

[23bcs164@mepcolinux datatype]$
