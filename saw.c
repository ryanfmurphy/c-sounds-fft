#include <stdio.h>

// USAGE: ./1 | speakerpipe -r 4000 -b
// ALSO COOL: ./1 | speakerpipe -r "44.1 kHz" (sounds weird and rhythmic)

int main(){
    #define NUM_MODS 5
    int mods[NUM_MODS] = {256,128,64,32,16};
    for (int j=0;j<NUM_MODS;j++) {
        for (int t=0;t<256*100;t++) {
            putchar(
                t % mods[j]
            );
        }
    }
	return 0;
}
