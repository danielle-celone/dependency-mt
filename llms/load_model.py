from llama_cpp import Llama
import json
import time


llm = Llama.from_pretrained(
	repo_id="TheBloke/Llama-2-7B-32K-Instruct-GGUF",
	filename="llama-2-7b-32k-instruct.Q2_K.gguf",
    n_ctx=16000,
)

'''Function to load the icl examples so we can pass the prompt to the mode'''
def load_icl_examples(icl_filename):
    prompts = []
    with open(icl_filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            data = json.loads(line)
            prompts.append(data['prompt'])
    out_file = '\n'.join(prompts)
    return out_file        

source_lang = input("enter source language code (ex: en): ").strip()
target_lang = input("enter target language code (ex: fr): ").strip()
sentence = input("enter the sentence to translate: ").strip()

test_prompt = f"Given these examples, translate the following sentence from {source_lang} into {target_lang}. \n Source sentence: {sentence}\n Target sentence:"

prompt = load_icl_examples('../data/processed/icl_examples.jsonl') + '\n\n' + test_prompt

start_time = time.time() 

output = llm(
    prompt,
    max_tokens=100,
    seed=5432,
    temperature=0.7,
    echo=False
)

end_time = time.time()


with open("output.txt", "a") as f:
    f.write(str({"sentence": sentence, "translation":output["choices"][0]["text"].strip() + "\n", "time elapsed":f"{end_time-start_time}s"}) + '\n')

print("done!")