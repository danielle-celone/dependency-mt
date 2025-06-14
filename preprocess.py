import pandas as pd
import json
from parsers import parse_sentence 

def preprocess(parquet_file:str, output_path:str):
    '''
    load datasets, parse sentences, write to output
    '''
    print("loading data")
    df = pd.read_parquet(parquet_file).head(2000)

    with open(output_path, 'w') as file:
        for i, row in df.iterrows():
            en_text = row["english"]
            fr_text = row["non_english"]

            try:
                en_parse = parse_sentence('en', en_text)
                fr_parse = parse_sentence('fr', fr_text)
            except Exception as error:
                print(f"could parse row {i}: {error}")
                continue

            output_data = {
                "en_raw": en_text,
                "en_parse": en_parse,
                "fr_raw": fr_text,
                "fr_parse": fr_parse
            }
            file.write(json.dumps(output_data) + '\n')
            if i % 100 == 0:
                print(f"processed {i} rows")
    print("done!")

if __name__ == "__main__":
    parquet_file = 'data/raw/train-00000-of-00002.parquet'
    output_file = 'data/processed/parsed_data.jsonl'
    preprocess(parquet_file, output_file)
