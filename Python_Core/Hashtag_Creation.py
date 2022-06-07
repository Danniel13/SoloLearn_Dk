#hashtag Generator and remove spaces:

s = input()

def hashtagGen(text):
	#your code goes here
	text= text.replace(" ","")
	return  ("#"+text )

print(hashtagGen(s))