#include <stdio.h>

// USAGE: mikepipe | ./in+1+0 | speakerpipe

int main(){
	while (1) {
		for (int mod=1;mod<10;mod++) {
			for (int t=0;t<1000;t++) {
				//putchar( t*((t>>12|t>>8)&/*63*/getchar()&t>>4));

				for (int x=0;x<500;x++) {
					putchar(getchar()*((t%mod)+1));
				}
			}
		}
	}
	return 0;
}
