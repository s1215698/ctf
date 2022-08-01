#include <stdio.h>
#include <stdlib.h>

using namespace std;


int main(int argc, char** argv) {
	
	
	
	char encry[] = {120,73,114,67,106,126,60,114,124,50,116,87,115,118,51,80,116,73,127,122,110,100,107,97};
  	char flag[24];
	for(int i=0;i<24;i++){              //Reverse 步驟二
  		flag[i] = (encry[i] ^ 6) - 1;  
  			
	  }
	for(int i=23;i>=0;i--){ 			//Reverse 步驟一
		printf("%c",flag[i]);	
	}	  
	  
  printf("\n");
  system("PAUSE");
  return 0;

}