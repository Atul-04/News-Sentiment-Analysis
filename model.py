from imports import*
from data_preprocessing import*

def delete_files():
    files_to_delete = ['label_encoder.pkl', 'logreg_model.pkl', 'max_length.pkl', 'tokenizer.pkl']
    for file in files_to_delete:
        try:
            os.remove(file)
            print(f"Deleted {file}")
        except FileNotFoundError:
            print(f"{file} not found")
        except Exception as e:
            print(f"Error deleting {file}: {e}")

# Delete the files before training the model
delete_files()

df = pd.read_csv('Train_Dataset.csv')
df['sentiment'] = df['sentiment'].fillna("neutral")
df['text'] = df['text'].apply(clean)
train_tokenizer,train_pad_sequence,max_length = preprocess_texts_train(df['text'])
label_encoder = LabelEncoder()
labels = label_encoder.fit_transform(df['sentiment'])

logreg = LogisticRegression(max_iter=1000)
logreg.fit(train_pad_sequence,labels)

joblib.dump(logreg, 'logreg_model.pkl')
with open('tokenizer.pkl', 'wb') as handle:
    pickle.dump(train_tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)
with open('max_length.pkl', 'wb') as handle:
    pickle.dump(max_length, handle, protocol=pickle.HIGHEST_PROTOCOL)
with open('label_encoder.pkl', 'wb') as handle:
    pickle.dump(label_encoder, handle, protocol=pickle.HIGHEST_PROTOCOL)