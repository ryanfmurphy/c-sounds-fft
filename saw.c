#include <stdio.h>

// USAGE: ./1 | speakerpipe -r 4000 -b
// ALSO COOL: ./1 | speakerpipe -r "44.1 kHz" (sounds weird and rhythmic)

int main(){
    #define NUM_MULTS 5
    int mults[NUM_MULTS] = {1,2,4,8,16};
    for (int j=0;j<NUM_MULTS;j++) {
        for (int t=0;t<256*100;t++) {
            putchar(
                t*mults[j] % 256
            );
        }
    }
	return 0;
}
