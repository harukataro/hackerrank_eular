#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int  sum_prime[100001] ={0,0,2};

int make_prime_list(){
    
    bool prime[100001];
    
    for(int j = 2; j < 100001; j++){
        prime[j] = true;
    }
    
    for(int i = 2; i < 100001; i++){
        if(prime[i] == true){
            printf("%d\n",i);
            sum_prime[i] = sum_prime[i-1] + i;
            for (int k = 2;i * k < 100001; k++){
                prime[i*k] = false;
            }
        }
        else{
           sum_prime[i] = sum_prime[i-1]; 
        }
    }
    return 0;
}


int main(){
    int t;
    int r;
    r = make_prime_list(); 
    scanf("%d",&t);
    for(int a0 = 0; a0 < t; a0++){
        int n; 
        scanf("%d",&n);
        printf("%d\n",sum_prime[n]);
    }
    return 0;
}