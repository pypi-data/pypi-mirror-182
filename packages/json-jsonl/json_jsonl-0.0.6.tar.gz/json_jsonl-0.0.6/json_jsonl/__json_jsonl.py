import json

base_encoding = "utf-8-sig"

def json_load(fname, encoding= base_encoding) :
    with open(fname, 'r', encoding= encoding) as f:
        json_data = json.load(f)
    return json_data

def json_save(fname, row_data, encoding= base_encoding) :
    with open(fname, 'w', encoding= encoding) as f:
        json.dump(row_data, fp= f, ensure_ascii=False)

def jsonl_load(fname, encoding= base_encoding) :
    with open(fname, encoding= encoding) as f:
        json_list = [json.loads(line) for line in f.readlines()]
    return json_list

def jsonl_save(fname, row_data, encoding= base_encoding) :
    with open(fname, encoding= encoding, mode="w") as f: 
        for i in row_data: 
            f.write(json.dumps(i, ensure_ascii=False) + "\n")