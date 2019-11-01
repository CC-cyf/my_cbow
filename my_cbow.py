from vocab import vocab
import numpy as np
import math

vt=vocab('alice')
learning_rate=0.5
e=math.e
center_vecor=np.zeros((1,100))
windowed_words=[]
content_vector=np.zeros((1,100))
y_layer=np.zeros((1,vt.vocab_size))
r_layer=np.zeros((1,vt.vocab_size))
standard_result=np.zeros((1,vt.vocab_size))
for i in range(0,5):
    for each_word_index in range(0,vt.article_len):
        each_word=vt.article[each_word_index]
        windowed_words=vt.get_windowed_words(center_word_index=each_word_index)
        content_vector=vt.get_content_vector(center_word_index=each_word_index)
        y_layer=np.dot(content_vector,vt.output_matrix)
        r_layer=pow(e,y_layer)
        temp=np.sum(r_layer)
        r_layer=r_layer/temp
        standard_result=np.zeros(vt.vocab_size)
        standard_result[vt.vocab_table[each_word].id]=1
        diff=r_layer-standard_result
        vt.output_matrix-=learning_rate*np.dot(diff.T,content_vector).T
        diff_content_vector=np.sum(diff)*np.dot(vt.output_matrix,np.ones((vt.vocab_size,1))).T
        for each in windowed_words:
            vt.vocab_table[each].vector-=learning_rate*diff_content_vector
        #print(each_word_index)#just for debug
    learning_rate=learning_rate-0.1
    print("loop ",i," done")
v1=vt.vocab_table['alice'].vector
v2=vt.output_matrix[:,vt.vocab_table['was'].id]
np.shape(v1)
np.shape(v2)
res=float((np.dot(v1,v2.T))/math.sqrt((np.sum(v1*v1*v2*v2))))
print("the similarity between 'alice' and 'was' is ",res)


