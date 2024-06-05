from imports import *

def clean(text):
    text = re.sub(r'[^a-zA-Z\s]', '', str(text))
    text = re.sub('https?://\S+', '', text)
    # Conver to lower
    text = text.lower()
    # Remove extra whitespaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def preprocess_texts(texts):
    # Tokenize the texts
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(texts)
    sequences = tokenizer.texts_to_sequences(texts)

    # Padding the sequences
    max_length = max([len(seq) for seq in sequences])
    padded_sequences = pad_sequences(sequences, maxlen=max_length, padding='post')

    return tokenizer, padded_sequences,max_length