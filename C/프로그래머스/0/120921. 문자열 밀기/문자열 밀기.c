#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* A, const char* B) {
    int answer = -1;
    int len = strlen(A);
    char* c_A = (char*) malloc(len+1);
    strcpy(c_A, A);
    char* next = (char*) malloc(len+1);
    next[len] = '\0';
    for(int i = 0; i < len-1; i++){
        if(strcmp(c_A,B) == 0){
            answer = i;
            break;
        }
        next[0] = c_A[len-1];
        for (int j=0; j < len-1;j++){
            next[j+1] = c_A[j]; 
        }
        if(strcmp(next,B) == 0){
            answer = i+1;
            break;
        }
        strcpy(c_A, next);
    }
    return answer;
}