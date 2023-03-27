import spacy
# REF - https://realpython.com/natural-language-processing-spacy-python/

nlp = spacy.load('en_core_web_sm')

# Produce a list of garden path sentences and store in a list called 'gardenpathSentences'
gardenpathSentences =['When Fred eats food gets thrown.',
                      'The cotton clothing is made of grows in Mississippi.',
                      'The old man the boat.',
                      'The man who hunts ducks out on weekends.',
                      'Mary gave the child the dog bit a Band-Aid.']


# Produce a list of tokenized sentences in the list 'gardenpathSentences'.
# Loop through the 'gardenpathSentences' and then tokenize and perform entity recognition.
for sentence in gardenpathSentences:
    doc = nlp(sentence) 
    print([token.text for token in doc])
    print([(ent.text, ent.label_) for ent in doc.ents])

    # Print it more neatly:
    print(f'Sentence: {sentence}')
    print(f'Tokens: {([token.text for token in doc])}')
    entity = [(ent.text, ent.label_) for ent in doc.ents]
    print(f'Entities: {entity}\n')    

# Two entities were found in the gardenpathSentences, these are: GPE and Person.
# Use spacy.explain to print the explanation.
gpe_explanation = spacy.explain("GPE")
print(f'GPE Explanation: {gpe_explanation}')

person_explanation = spacy.explain("PERSON")
print(f'PERSON Explanation: {person_explanation}')

'''The senetence "The cotton clothing is made of grows in Mississippi.", the recognised entity is "Mississippi" which is a geopolitical entity (GPE)
    The sentence "Mary gave the child the dog bit a Band-Aid.", the recognised entity is "Mary" which is a Person, typically referring to a person or group of people, including fictional characters.

    Other entity examples are:
    NOP: Nationalities or religious or political groups.
    LOC: Non-GPE locations, mountain ranges, bodies of water
    PRODUCT: Objects, vehicles, foods, ect. (Not services)

    REF - https://towardsdatascience.com/explorations-in-named-entity-recognition-and-was-eleanor-roosevelt-right-671271117218

'''