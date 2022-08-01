#include <stdio.h>
#include <stdlib.h>
#include <string>
using namespace std; 

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	
	char v3[3][8]={"Dufhbmf","pG`imos","ewUglpt"};
	string a1;  
	
	for ( int i = 0; i <= 11; ++i )
  {
     
      a1[i]  = (v3[i % 3][2 * (i / 3)]) - 1;
      printf("%c",a1[i]);
  }
  printf("\n");
  system("PAUSE");
  return 0;

}