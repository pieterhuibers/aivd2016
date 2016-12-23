def cypher_test() :
	c = 'c'
	h = 'h'
	y = 'y'
	klinker = ['a','e','i','o','u']
	medeklinker = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']

	# for id in range(26) :
	# 	d = chr(ord(d)+1)
	# 	if(d == '{') :
	# 		d = 'a'
	for c in medeklinker :
		for h in ['e'] :
			for y in medeklinker :
				word = c+h+y+h
				if(c != y) :
					print(word)

def main():
	cypher_test()

if __name__ == "__main__":
	main()
