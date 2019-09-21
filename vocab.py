import json
class vocab:
	index=0
	vocab_table={}
	#在词典内增加一个词
	def append(self,word):
		self.vocab_table[word] = self.index
		self.index += 1

	#将词典保存到.json文件中
	def save_to_file(self):
		with open('vocab_table.json','w') as vt:
			json.dump(self.vocab_table,vt)
		print('The vocaburary table has been saved as "vocab_table.json"')

	def get_id(self,word):
		return self.vocab_table[word]

	def __init__(self,filename):
		with open(filename) as fileread:
			context=fileread.read()
		words=context.lower().replace('*',' ').replace('"',' ').replace('-',' ').replace('\\',' ')\
		.replace('.',' ').replace(':',' ').replace(',',' ').replace('!',' ').replace('?',' ')\
		.replace('(',' ').replace(')',' ').replace('`',' ').split()
		for each in words:
			if each not in self.vocab_table:
				self.append(each)
