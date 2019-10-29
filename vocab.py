import json
import numpy as np

class wordvec:
	id=0
	vector=(np.random.random((1,100))*2-1)
	def __init__(self,id):
		self.id=id

class vocab:
	vocab_size=0
	article_len=0
	article=[]
	vocab_table={}
	output_matrix=np.zeros(1)
	#在词典内增加一个词
	def append(self, word):
		self.vocab_table[word] = wordvec(self.vocab_size)
		self.vocab_size += 1

	#将词典保存到.json文件中
	def save_article(self):
		with open('article.json','w') as art:
			json.dump(self.article,art)
			print('The article table has been saved as "article.json"')
	
	def get_windowed_words(self, center_word_index, window_size=5):
		windowed_word=[]
		if window_size < 1:
			print('The windows size can not be smaller than 1, default value is 5.')
		#插入中心词左侧的词
		if center_word_index != 0:
			#不是第一个词
			if center_word_index < window_size:
				for i in range(0, center_word_index):
					windowed_word.append(self.article[i])
			else:
				for i in range((center_word_index - window_size), center_word_index):
					windowed_word.append(self.article[i])
		#插入中心词右侧的词
		if center_word_index != self.article_len - 1:
			#不是最后一个词
			if center_word_index > self.article_len - 1 - window_size:
				for i in range((center_word_index + 1), self.article_len):
					windowed_word.append(self.article[i])
			else:
				for i in range((center_word_index + 1), (center_word_index + window_size + 1)):
					windowed_word.append(self.article[i])
		return windowed_word

	def get_content_vector(self, center_word_index, window_size=5):
		windowed_word = self.get_windowed_words(center_word_index = center_word_index, window_size=window_size)
		vector=np.zeros((1,100))
		for each_word in windowed_word:
			vector += self.vocab_table[each_word].vector
		vector = vector/windowed_word.__len__()
		return vector

	def __init__(self, filename):
		with open(filename) as fileread:
			context=fileread.read()
		self.article=context.lower().replace('*',' ').replace('"',' ').replace('-',' ').replace('\\',' ')\
		.replace('.',' ').replace(':',' ').replace(',',' ').replace('!',' ').replace('?',' ')\
		.replace("' ",' ').replace(" '",' ').replace('(',' ').replace(')',' ').replace('`',' ').split()
		for each in self.article:
			if each not in self.vocab_table:
				self.append(each)
		self.article_len=self.article.__len__()
		self.output_matrix=np.random.random((100,self.vocab_size))

