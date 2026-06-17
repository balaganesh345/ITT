[23bcs164@mepcolinux itt]$cat valid_parenthesis.c
#include<stdio.h>
#include<string.h>

int main(){
   char input[30];
   int n;
   printf("Enter the no.of expression :");
   scanf("%d",&n);
   for(int i=0;i<n;i++){
      scanf(" %c",&input[i]);
   }
   for(int i=0;i<n;i++){
      printf("%3c",input[i]);
   }
   printf("\n");

   int flag = 0;
   for(int i=0;i<n;i++){
      if ( "{" == input[i]){
         for(int j=i;j<n;j++){
            if("}" == input[i]){
               flag = 1;
            }
         }
      }
      if ( "[" == input[i]){
          for(int j=i;j<n;j++){
             if("]" == input[i]){
               flag = 1;
            }
          }
      }
  if (flag == 1){
     printf("Valid Expression");
  }else{
     printf("Not a Valid Expression");
  }

  return 0;
}
