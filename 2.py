# python -u 2.py | speakerpipe -b -r 4000

import sys, pygame

def vals_gen():
	t = 0
	while True:
		yield ((t*(t>>5|t>>8))>>(t>>16))
		t += 1

def gfx_init():
	pygame.init()
	S = pygame.display.set_mode([800,800])
	up = pygame.display.update
	A = pygame.surfarray.pixels2d(S)
	return S, A, up

def binstr(v):
	return bin(v)[2:].rjust(8,'0')

# 1 pixel for each bit - black/white
def binpix(v):
	strn = binstr(v)
	return tuple(0xffffff00 if ch=='1' else 0 for ch in strn)

# 1 pixel the shade of the whole byte
def bytepix(v):
	return (v << 8) + (v << 16) + (v << 24)

if __name__=='__main__':
	S, A, up = gfx_init()
	vals = vals_gen()
	x, y, t = 0, 0, 0
	while True:
		v = vals.next() % 256
		sys.stdout.write(chr(v))
		A[x:x+8,y] = bytepix(v)
		if t % 4000 == 0: up()
		
		x += 8
		if x >= 512:
			x = 0; y += 1
			if y >= 512: y = 0
		t += 1

	exit(0)

