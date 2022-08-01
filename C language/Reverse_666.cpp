#include <stdio.h>
#include <stdlib.h>
#include <string>
using namespace std; 

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {

char i;
int key = 18; //已得知key為長度 為18 bits 
char a1[key]; //建立空字串 長度為 18 
char a2[]="izwhroz\"\"w\"v.K\".Ni"; //建立已知加密後enflag 

for(i=0;i<18;i+=3){  //三個三個一組  執行反向運算   ^代表XOR   A^B^A = B  

    a1[i]=(a2[i]^18)-6;

    a1[i+1]=(a2[i+1]^18)+6;

    a1[i+2]=(a2[i+2]^18)^6;

}

for(int i=0;i<18;i++){   //輸出原本明文字串 
	printf("%c",a1[i]);
}
printf("\n");
system("pause");
return 0;
}
