#include<stdio.h>
#include<string.h>

int main(){
    char a[] = {1,22,3,4,5,6,};

    long b = strlen(a);

    printf(b);
    printf("\n");

    for(int i=0;i<strlen(a);i++){
        printf("char[%i] --> %i\n",i,a[i]);
    }
}