1. Convert hex to base 64:

		decode given hex string to ascii using .decode('hex)
		then encode it to base64 using .encode('base64')
		# refer 1.py

2. Fixed Xor

		given two hex strings to produce their Xor convert each hex string to base10 and 
		then xor both base 10 numbers then convert to hex
		# refer 2.py

5. Implement repeating-key XOR

		task is to xor a given string 'a' with given key 'b'
		here we can use
				"".join(chr(ord(i)^ord(j)) for i,j in zip(a,cycle(b)))
		so what above line does is cycle(b) will create a string of length 'a' by repeatedly adding the string b 
		now since both lengths are equal zip will pair every character of 'a' with every character of 'b' and 
		return each pair as tuples (zip basically returns iterator of tuples)
		(think 'a' and 'b' as sets containing characters and zip is something like one-one function)
		# refer 5.py
		
