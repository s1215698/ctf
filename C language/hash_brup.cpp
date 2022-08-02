#include <stdio.h>
#include <stdlib.h>
#include <string.h> 
#include <cmath>
#include <iostream>

using namespace std;

char myhash(char a1[], int gg);
/* run this program using the console pauser or add your own getch, system("pause") or input loop */


int main(int argc, char** argv) {
	char aa[]   = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa";
	char temp[] = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa";
	char hash[] = "dwjzhaxwnndwjzhaxwnndwjzhaxwnndw";
	
	for(int i=0;i<32;i++){
		for(int x=0;x<32;x++){
			temp[x] = aa[x];
		}
		for(int j=0;j<26;j++){
			temp[i] = aa[i]+j;
			char test_hash = myhash(temp,i);
			char compare_val = hash[i];
			if(test_hash == compare_val){
				aa[i] = temp[i];
				printf("%c",aa[i]);
			}
		}
	}
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

