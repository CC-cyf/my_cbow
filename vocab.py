import json
import numpy as np

class wordvec:
	id=0
	vector=np.random.random((1,100))
	def __init__(self,id):
		self.id=id

class vocab:
	index=0
	article={}
	vocab_table={}
	#在词典内增加一个词
	def append(self,word):
		self.vocab_table[word] = wordvec(self.index)
		self.index += 1

	#将词典保存到.json文件中
	def save_to_file(self):
		with open('vocab_table.json','w') as vt:
			json.dump(self.vocab_table,vt)
			print('The vocaburary table has been saved as "vocab_table.json"')
		with open('article.json','w') as art:
			json.dump(self.article,art)
			print('The article table has been saved as "article.json"')

	def get_id(self,word):
		return self.vocab_table[word]

	def __init__(self,filename):
		with open(filename) as fileread:
			context=fileread.read()
		self.article=context.lower().replace('*',' ').replace('"',' ').replace('-',' ').replace('\\',' ')\
		.replace('.',' ').replace(':',' ').replace(',',' ').replace('!',' ').replace('?',' ')\
		.replace("' ",' ').replace(" '",' ').replace('(',' ').replace(')',' ').replace('`',' ').split()
		for each in self.article:
			if each not in self.vocab_table:
				self.append(each)
