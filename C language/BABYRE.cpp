#include <stdio.h>
#include <stdlib.h>
#include <string>
using namespace std; 

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	
    char encry[] = {102,109,99,100,127,107,55,100,59,86,96,59,110,112};
    for(int i=0;i<14;i++){
        encry[i] ^= i;
        printf("%c",encry[i]);
    }
    printf("\n");
    system("PAUSE");
    return 0;

}