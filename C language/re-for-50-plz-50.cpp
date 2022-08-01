#include <stdio.h>
#include <stdlib.h>
#include <string>
using namespace std; 

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	
  	char encry[] = {99,98,116,99,113,76,85,66,67,104,69,82,86,91,91,78,104,64,95,88,94,68,93,88,95,89,80,86,91,67,74};
  	
	for(int i=0;i<31;i++){
  		encry[i] = encry[i] ^ 0x37;
  		printf("%c",encry[i]);
	  }
    printf("\n");
    system("PAUSE");
    return 0;

}