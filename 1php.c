#include <stdio.h>

// USAGE: ./1 | speakerpipe -r 4000 -b
// ALSO COOL: ./1 | speakerpipe -r "44.1 kHz" (sounds weird and rhythmic)

#include <stdio.h>

// #todo incorporate the audio code directly
// and/or be able to write to stdin separate from outputting audio stream

int main(){
	int t;
	for (t=0;;t++) {
		putchar(
			(t*(t>>5|t>>8))>>(t>>16)
		);
	}
	return 0;
}
