from Bai5_7 import vocab
work_dir = 'E:/Documents/NamHoc2025_2026/MayHocUngDung/work/'
f = open(work_dir + 'vocab_' + str(len(vocab)) + '._txt', encoding='utf-8', mode='w')
for word,idx in vocab.items():  
    f.write(f"{word}: {idx}\n")
f.close()