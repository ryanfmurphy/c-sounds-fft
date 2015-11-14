#include <stdio.h>

int main(){
	int t;
	for (t=0;;t++) {
		putchar(
			t*((t>>12|t>>8)&63&t>>4)
		);
		for (int x=0;x<500;x++) { 
			putchar('\0');
		}
	}
	return 0;
}
