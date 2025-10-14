work_dir = 'E:/Documents/NamHoc2025_2026/MayHocUngDung/work/'
vocab_file = 'vocab_181.txt'
vocab = []
for word in open(work_dir + vocab_file, encoding= 'utf-8', mode='r'):
    vocab.append(word.replace('\n', ''))
print(vocab)
print(len(vocab))