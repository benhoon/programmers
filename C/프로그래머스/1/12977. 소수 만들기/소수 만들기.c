#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int isPrime(int num){
    int res = 1;
    int i = 2;
    while(i < num){
        if (num % i == 0){
            return 0;
        }
        i++;
    }
    return res;
}

// nums_len은 배열 nums의 길이입니다.
int solution(int nums[], size_t nums_len) {
    int answer = 0;
    for(int i = 0; i < nums_len-2; i++){
        for(int j = i+1; j < nums_len-1; j++){
            for (int k = j+1; k < nums_len; k++){
                int chk = nums[i]+nums[j]+nums[k];
                if(isPrime(chk) == 1){
                    answer += 1;
                }
            }
        }
    }
    return answer;
}