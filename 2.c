#include <stdio.h>

// #todo incorporate the audio code directly
// and/or be able to write to stdin separate from outputting audio stream

int main(){
	int t;
	for (t=0;;t++) {
		fputc(
			(t*(t>>5|t>>8))>>(t>>16)
		, stdout);
	}
	return 0;
}
