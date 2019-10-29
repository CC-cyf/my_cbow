from vocab import vocab
import numpy as np

vt=vocab('alice')
learning_rate=0.5
center_vecor=np.zeros((1,100))
windowed_words=[]
content_vector=np.zeros((1,100))
result=np.zeros((vt.vocab_size))
standard_result=np.zeros((vt.vocab_size))
for i in range(0,5):
    for each_word_index in range(0,vt.article_len):
        each_word=vt.article[each_word_index]
        windowed_words=vt.get_windowed_words(center_word_index=each_word_index)
        content_vector=vt.get_content_vector(center_word_index=each_word_index)
        result=np.matmul(content_vector,vt.output_matrix)
        standard_result=np.zeros(vt.vocab_size)
        standard_result[vt.vocab_table[each_word].id]=1
        diff_output_matrix=np.matmul(content_vector.T,(result-standard_result))
        vt.output_matrix=vt.output_matrix-learning_rate*diff_output_matrix
        diff_content_vector=np.matmul((result-standard_result),vt.output_matrix.T)
        for each in windowed_words:
            vt.vocab_table[each].vector=vt.vocab_table[each].vector-learning_rate*diff_content_vector
        #print("learning...",((i+1)/5*(each_word_index+1)/vt.article_len))
    learning_rate=learning_rate-0.1
    print("loop ",i," done")
v1=vt.vocab_table['alice'].vector
v2=vt.output_matrix[:,vt.vocab_table['was'].id]
np.shape(v1)
np.shape(v2)
res=float((np.matmul(v1,v2.T))/(np.sum(v1*v1*v2*v2)))
print("the similarity between 'alice' and 'was' is ",res)


