//AIS3 2017 pre-exam Crypto1
/*
題目給
#include <stdio.h>
#include <string.h>

int main()
{
	int val1 = ?????????, val2 = ?????????, val3 = ???????, val4 = ??????, i, *ptr;
	char flag[29] = "????????????????????????????"; // Hint: The flag begins with AIS3
	
	for(i = 0, ptr = (int*)flag ; i < 7 ; ++i)
		printf("%d\n", ptr[i] ^ val1 ^ val2 ^ val3 ^ val4);
	
	
	964600246
	1376627084
	1208859320
	1482862807
	1326295511
	1181531558
	2003814564

	
	return 0;
}
*/



#include <stdio.h>
#include <string.h>

int main(){
  	int result[] ={964600246,1376627084,1208859320,1482862807,1326295511,1181531558,2003814564};
    char flag[29];
    flag[0] = 'A';
    flag[1] = 'I';
    flag[2] = 'S';
    flag[3] = '3';
    flag[4] = '{';
    int *ptr;
    ptr = (int*)flag;
    int key = result[0] ^ ptr[0];
    int i ;
    for(i = 0, ptr = (int*)flag ; i < 7 ; ++i)
        ptr[i] = key ^ result[i];
    flag[28] = '\0';
    printf("%s\n",flag);
	return 0;
}