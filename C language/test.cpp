#include <stdio.h>
#include <stdlib.h>
#include <string.h> 
#include <cmath>
#include <iostream>

using namespace std;

char myhash(char a1[], int gg);
/* run this program using the console pauser or add your own getch, system("pause") or input loop */


int main(int argc, char** argv) {
	char lib[] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
	char* input ;

	scanf("%s",&input);

	for(int i=0;i<input)
	printf("%s",input);
    system("PAUSE");
    printf("\n");
  return 0;

}
char myhash(char a1[], int gg) {
	int v2 = strlen(a1);
	char v3[31];
  	for(int i = 0; i <= 31; ++i) {
  		v3[i] = (a1[i % v2] + 3) % 26 + 97;
	}
	return v3[gg];
}

