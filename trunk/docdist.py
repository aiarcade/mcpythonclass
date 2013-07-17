import math

def readFile(filename):
	f=open(filename,'r')
	return f.readlines()

#implementation of document distance alogrithm

def findWordCount(listn):
	words=[]
	for line in listn:
		wordsInLine=line.split(" ")
		for word in wordsInLine:
			word=word.replace("\n","").replace(" ","").lower()
			if word is "":
				continue
			for entry in words:
				if word==entry[0]:
					entry[1]=entry[1]+1
					break
			else:
				words.append([word,1])
	return words

def findInnerProduct(List1,List2):
	sum = 0.0
	for word1, count1 in List1:
		for word2, count2 in List2:
			if word1 == word2:
				sum += count1 * count2
	return sum

def vectorAngle(List1,List2):
	numerator = findInnerProduct(List1,List2)
	denominator = math.sqrt(findInnerProduct(List1,List1)*findInnerProduct(List2,List2))
	print numerator,denominator
	return math.acos(numerator/denominator)






file1cont=readFile("hello1.txt")
file2cont=readFile("hello2.txt")
List1=findWordCount(file1cont)
List2=findWordCount(file2cont)

print vectorAngle(List1,List2)


