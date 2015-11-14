#include <stdio.h>

// USAGE: ./1 | speakerpipe
// ALSO COOL: ./1 | speakerpipe -r "44.1 kHz" (sounds weird and rhythmic)

int main(){
	int t;
	for (t=0;;t++) {
		putchar(
			t*((t>>12|t>>8)&63&t>>4)
		);
	}
	return 0;
}
