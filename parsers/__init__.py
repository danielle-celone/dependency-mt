from parsers.parse_en import parse_en_sentence
from parsers.parse_fr import parse_fr_sentence

def parse_sentence(lang:str, sentence:str) -> list[dict]:
    '''
    Depending on the input language, route sentence parse to the correct parser
    
    Args: 
        lang (str) : the code of the input language
        sentence (str) : the input sentence
    '''
    if lang == 'en':
        return parse_en_sentence(sentence)
    elif lang == 'fr':
        return parse_fr_sentence(sentence)
    else:
        raise ValueError("The language specified is not supported")