import json
class vocab:
	index=0
	vocab_table={}
	#在词典内增加一个词
	def append(self,word):
		self.vocab[word] = self.index
		self.index += self.index

	#将词典保存到.json文件中
	def save_to_file(self):
		with open('vocab_table.json','w') as vt:
			json.dump(self.vocab_table,vt)
		print('The vocaburary table has been saved as "vocab_table.json"')

	def __init__(self,filename):
		with open(filename) as fileread:
			context=fileread.read()
		words=context.replace('*','').split()
		for each in words:
			if each not in words:
				self.append(each)
