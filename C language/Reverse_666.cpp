#include <stdio.h>
#include <stdlib.h>
#include <string>
using namespace std; 

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {

char i;
int key = 18; //�w�o��key������ ��18 bits 
char a1[key]; //�إߪŦr�� ���׬� 18 
char a2[]="izwhroz\"\"w\"v.K\".Ni"; //�إߤw���[�K��enflag 

for(i=0;i<18;i+=3){  //�T�ӤT�Ӥ@��  ����ϦV�B��   ^�N��XOR   A^B^A = B  

    a1[i]=(a2[i]^18)-6;

    a1[i+1]=(a2[i+1]^18)+6;

    a1[i+2]=(a2[i+2]^18)^6;

}

for(int i=0;i<18;i++){   //��X�쥻����r�� 
	printf("%c",a1[i]);
}
printf("\n");
system("pause");
return 0;
}
