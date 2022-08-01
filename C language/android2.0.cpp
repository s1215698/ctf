#include <stdio.h>
#include <stdlib.h>
#include <string> 


using namespace std;



/* run this program using the console pauser or add your own getch, system("pause") or input loop */
char* Init(char* res1, char* res2, char* res3, char* str, int len);


int main(void) {
	
	char res1[] = /*(char *) malloc(1)*/ {0x4c,0x4e,0x5e,0x64,0x6c};
	char res2[] = /*(char *) malloc(10)*/ {0x20,0x35,0x2D,0x16,0x61};
	char res3[] = /*(char *) malloc(1)*/{0x41,0x46,0x42,0x6f,0x7d};
	
	
	char temp[15];
	int i=0,j= 3;
	
	
	do{
		res3[i] ^= res2[i];
		res2[i] ^= res1[i];
		res1[i] = ((res1[i] ^ 0x80) / 2);
		
		
		temp[i*j] =  res1[i];
		temp[(i*j)+1] = res2[i];
		temp[(i*j)+2] = res3[i];
		++i;
	}while(i!=4);

	temp[i*j] =  res1[i];
	temp[(i*j)+1] = res2[i];
	temp[(i*j)+2] = res3[i];
	

	for(i=0;i<15;i++){
        printf("%c",temp[i]);
    }
    printf("\n");
    system("PAUSE");
    return 0;
}
/*

char* Init(char* res1, char* res2, char* res3, char* str, int len)
{
  int v5; // r5
  int v6; // r10

  if ( len < 1 )
  {
    v6 = 0;
  }
  else
  {
    v5 = 0;
    v6 = 0;
    do
    {
      if ( v5 % 3 == 2 )
      {
        res3[v5 / 3u] = str[v5];
      }
      else if ( v5 % 3 == 1 )
      {
        res2[v5 / 3u] = str[v5];
      }
      else if ( v5 == 3 * (v5 / 3) )
      {
        ++v6;
        *(res1 + v5 / 3u) = str[v5];
      }
      ++v5;
    }
    while ( len != v5 );
  }
  *(res1 + v6) = 0;
  res2[v6] = 0;
  res3[v6] = 0;
  return res1;
}*/