import json
work_dir = 'E:/Documents/NamHoc2025_2026/MayHocUngDung/work/'
vocab_file = 'vocab_181.json'
vocab =[]
with open(work_dir + vocab_file, encoding='utf-8', mode='r') as f:
    vocab = json.load(f)
print(vocab)
print(len(vocab))