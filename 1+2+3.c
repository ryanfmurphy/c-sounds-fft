#include <stdio.h>

int main(){
	int t;
	for (t=0;;t++) {
		putchar(
			t*((t>>12|t>>8)&63&t>>4)
		);
		putchar(
			(t*(t>>5|t>>8))>>(t>>16)
		);
		putchar(
			t*((t>>9|t>>13)&25&t>>6)
		);
	}
	return 0;
}
