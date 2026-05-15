#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int a, int b, int c, int d) {
    int answer = 0, qr = 1;
    int dice[6] = {0,0,0,0,0,0}; //0,2,0,0,1,1
    dice[a-1]++;
    dice[b-1]++;
    dice[c-1]++;
    dice[d-1]++;
    if(a!=b && a!=c && a!=d && b!=c && b!=d && c!=d){
        for(int i = 0; i<6; i++){
            if(dice[i]==1){
                answer = i+1;
                break;
            }
        }
    }
    else{
        for(int i = 0; i<6; i++){
            if(dice[i] == 4){
                answer = 1111 * (i+1);
                break;
            }
            else if (dice[i] == 3){
                for(int j = 0; j<6; j++){
                    if(dice[j]==1){
                        answer = (10*(i+1) + (j+1)) * (10*(i+1) + (j+1));
                        break;
                    }
                }
            }
            else if (dice[i] == 2){
                for(int j = 0; j<6; j++){
                    if (dice[j] == 1){
                        qr *= j+1;
                    }
                    else if(dice[j] == 2 && i!=j){
                        answer = (i+1+j+1) * abs(i-j);
                        break;
                    }
                }
                if(qr > 1)
                    answer = qr;
                break;
            }
            if(answer > 0){
                break;
            }
        }
    }
    return answer;
}