from vocab import vocab
#取得初始化向量，维度为100
vt=vocab('alice')
print(vt.vocab_table['alice'].vector)