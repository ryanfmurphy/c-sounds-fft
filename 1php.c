#include <stdio.h>

// USAGE: ./1 | speakerpipe -r 4000 -b
// ALSO COOL: ./1 | speakerpipe -r "44.1 kHz" (sounds weird and rhythmic)


int main(){
	int t;
	for (t=0;;t++) {
		putchar(
			//t*((t>>12|t>>8)&63&t>>4)
			t*
            (
                (t >> 10                |t >> 0                )
                & 19                & t >> 2            )
		);
	}
	return 0;
}
