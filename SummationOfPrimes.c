#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

  
int main(){
    int t;
    int n;
    long long int sum = 2;
    long long int sum_prime[1000001]={0};    
    sum_prime[2]=2;
    
    for(int i = 3; i <= 1000000; i=i+2){
        if(sum_prime[i] == 0){
            for (int k = i+i;k <= 1000000; k=k+i){
                sum_prime[k] = 1;                
            }
            sum = sum + i;
        }
    sum_prime[i]=sum;
    sum_prime[i+1]=sum;
    }  
    
    scanf("%d",&t);
    for(int a0 = 0; a0 < t; a0++){ 
        scanf("%d",&n);
        printf("%lld\n",sum_prime[n]);
    }
    return 1;
}
