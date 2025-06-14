import json

'''
Function to build the prompt telling the model to use the dependncy parse info
    Args: 
        unparsed source text (str)
        parsed source text (dict)
        source lang (str)
        target lang (str)
        raw

'''
#sort out the translation direction and string
def make_prompt(raw_source, parsed_source, source_lang_code, target_lang_code):
    if source_lang_code == 'en' and target_lang_code == 'fr':
        raw_target = parsed_source["en_raw"]
        source_lang = 'English'
        target_lang = 'French'
    elif source_lang_code == 'fr' and target_lang_code == 'en':
        raw_target = parsed_source["fr_raw"]
        source_lang = "French"
        target_lang = "English"
    else:
        raise ValueError("language pair not recognized. language pair must be en/fr or fr/en")
    
    #build the prompt
    prompt = f'Translate the following {source_lang} into {target_lang} using the dependency parse information provided to guide decisions about sentence structure.\n\n'
    prompt += f'Source sentence: {raw_source}\nDependency parse: {parsed_source}\n{target_lang} translation:'
    return {"prompt":prompt, "gold translation":raw_target}


'''
Function to generate a file of prompts
Args:
    input_file: a file containing a list of sentence to use in prompts (str)
    output_file: a file to write to (str)
    source_lang_code: the lang code of the source language
    target_lang_code: the lang code of the target language
'''
def generate_prompt_dataset(input_file, output_file, source_lang_code, target_lang_code):
    with open(input_file, 'r') as in_file, open(output_file, 'w') as out_file:
        for line in in_file:
            data = json.loads(line)
            prompt = make_prompt(data[f"{source_lang_code}_raw"], data[f"{source_lang_code}_parsed"], source_lang_code, target_lang_code)
            out_file.write(json.dumps(prompt) + '\n\n')