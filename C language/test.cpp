#include <iostream>
#include <cstring>

using namespace std;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */
char myhash(char a1[], int gg);
char *dehash();

int main(int argc, char** argv) {
	char aa[]   = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa";
	char cc[]   = "universitiruniversitiruniversiti";
	char hash[] = "lwcqrpvchiekrfigvvggmzdirsckrujm";
	//cout << dehash() << endl;
	for(int i = 0; i < 32; i++) {
		for(int x = 0; x < 32; x++) {
			cc[x] = aa[x];
		}
		for(int j = 0; j < 26; j++) {
			cc[i] = (aa[i] + j);
			char a = myhash(cc, i);
			char b = hash[i];
			char c = cc[i];
			if (a == b) {
				cout << c;
				aa[i] = cc[i];
				break;
                system("PASUE");
			}
		}
	}
    
	return 0;
}

char myhash(char a1[], int gg) {
	int v2 = strlen(a1);
	char aApksfckljfakls[] = "apksfckljfaklshctepekrijnfomlhth";
	char v4 = 112;
	char v3[31];
  	for(int i = 0; i <= 31; ++i) {
  		v3[i] = (aApksfckljfakls[i] + a1[i % v2] + a1[i % v2]) % 26 + 97;
    	v4 = v3[i];
	}
	return v3[gg];
}

char *dehash() {
	char hash[] = "lwcqrpvchiekrfigvvggmzdirsckrujm";
	int v2 = strlen(hash);
	char aApksfckljfakls[] = "apksfckljfaklshctepekrijnfomlhth";
	char v4 = 112;
	char v3[32];
  	for(int i = 31; i > 0; --i) {
  		int t1 = hash[i] - 97;
  		while (t1 <= (hash[i - 1] + 97 + aApksfckljfakls[i]))
  		{
  			t1 += 26;	
		}
		int t2 = t1 - hash[i - 1] - aApksfckljfakls[i];
		if (t2 < 97)
			t2 += 26;
		
		v3[i] = t2;
  		//v3[i] = (aApksfckljfakls[i] + a1[i % v2] + v4) % 26 + 97;
    	//v4 = v3[i];
	}
	
	int t1 = hash[0] - 97;
	while (t1 <= (112 + 97 + aApksfckljfakls[0]))
	{
		t1 += 26;	
	}
	int t2 = t1 - 112 - aApksfckljfakls[0];
	if (t2 < 97)
		t2 += 26;
	v3[0] = t2;
	return v3;
}