from Bai5_1 import vocab
work_dir = 'E:/Documents/NamHoc2025_2026/MayHocUngDung/work/'
f = open(work_dir + 'vocab_' + str(len(vocab)) + '.txt', encoding= 'utf-8', mode ='w')
for word in vocab:
    f.write(word + '\n')
f.close()
