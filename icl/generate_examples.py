from write_prompts import generate_prompt_dataset

input_file = "../data/processed/example_sentences.jsonl"   
output_file = "../data/processed/icl_examples.jsonl"
source_lang_code = "en"
target_lang_code = "fr"

generate_prompt_dataset(input_file, output_file, source_lang_code, target_lang_code)
