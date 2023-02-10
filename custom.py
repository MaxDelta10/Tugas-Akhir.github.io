import re, string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

def preprocess(text):
    text = text.lower()
    text = text.strip()
    text = re.compile('<.*?>').sub(' ', text)
    text = re.compile('[%s]'% re.escape(string.punctuation)).sub(' ', text)
    text = re.sub('\s+',' ', text)
    text = re.sub(r'\[[0-9]*\]',' ', text)
    text = re.sub(r'[^\w\s]',' ',str(text).lower().strip())
    text = re.sub(r'\d',' ',text)
    text = re.sub(r'\s+',' ',text)
    text = re.sub(r'[^\x00-\x7F]+',' ', text)
    return text

    #stopword removal english
def stopword(string):
    a = [i for i in string.split() if i not in stopwords.words('english')]
    return ' '.join(a)

    #Lemmatizer
wl = WordNetLemmatizer()

def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

def lemmatizer(string):
    word_pos_tags = nltk.pos_tag(word_tokenize(string)) # Get Position tags
    a = [wl.lemmatize(tag[0], get_wordnet_pos(tag[1])) for idx, tag in enumerate(word_pos_tags)]
    return " ".join(a)

def finalpreprocess(string):
    string = str(string)
    return lemmatizer(stopword(preprocess(string)))
