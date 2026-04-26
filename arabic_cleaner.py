import re
import emoji
from camel_tools.disambig.mle import MLEDisambiguator
from camel_tools.tokenizers.morphological import MorphologicalTokenizer

# 1. Boot up the linguistic brain (Global Scope)
print("Loading CAMeL Tools database...")
mle_brain = MLEDisambiguator.pretrained('calima-msa-r13')
smart_tokenizer = MorphologicalTokenizer(mle_brain, scheme='d3tok')
print("Database loaded successfully!")

# 2. Define our custom pipeline function
def arabic_cleaning_process(raw_sentence):
    # Strip English and punctuation
    no_english = re.sub(r'[a-zA-Z0-9!#.]', '', raw_sentence)
    
    # Strip Emojis
    no_emoji = emoji.replace_emoji(no_english, replace='')
    
    # Split into a list of words for CAMeL Tools
    word_splitted = no_emoji.split()
    
    # Morphological Tokenization
    final_tokens = smart_tokenizer.tokenize(word_splitted)
    
    return final_tokens

# 3. Test the function
test_sentence = "مرحبا بك!!! 123 في الورشة 😂"
my_result = arabic_cleaning_process(test_sentence)

print("---")
print("Raw Input:", test_sentence)
print("Cleaned & Tokenized Output:", my_result)
