import stanza

parser = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos,lemma,depparse')

def parse_en_sentence(sentence:str) -> list[dict]:
    parse_data = parser(sentence)
    parsed_sentence = []

    for sent in parse_data.sentences:
        for token in sent.words:
            d = {
                'text': token.text,
                'dep relation': token.deprel, #dependency relation
                'head':token.head

            }
            parsed_sentence.append(d)
    return parsed_sentence