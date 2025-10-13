import json
from Bai5_1 import vocab
work_dir = 'E:/Documents/NamHoc2025_2026/MayHocUngDung/work/'
with open(work_dir + 'vocab_' + str(len(vocab)) + '.json', encoding='utf-8', mode = 'w') as f:
    json.dump(vocab,f,ensure_ascii=False)