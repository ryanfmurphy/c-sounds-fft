#include <stdio.h>

// #todo incorporate the audio code directly
// and/or be able to write to stdin separate from outputting audio stream

int main(){
	int t;
	for (t=0;;t++) {
		putchar(
			(t*(t>>5|t>>11))>>(t>>16)
		);
	}
	return 0;
}
