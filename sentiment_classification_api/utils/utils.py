import re
import string
import json
import pickle5


class CleanText:
    def __init__(self, stopwords):
        self.stopwords = stopwords
    
    def clean_stopwords(self, content):
        # content: str
        content = content.split(" ")
        filtered_list = []
        stopwords = self.stopwords
        for word in content:
            if word not in stopwords:
                filtered_list.append(word)

        text = ' '.join(filtered_list)
        return text
    
    def remove_emoji(self, string):
        emoji_pattern = re.compile("["
                            u"\U0001F600-\U0001F64F"  # emoticons
                            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                            u"\U0001F680-\U0001F6FF"  # transport & map symbols
                            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                            u"\U00002702-\U000027B0"
                            u"\U000024C2-\U0001F251"
                            "]+", flags=re.UNICODE)
        return emoji_pattern.sub(r'', string)
    
    #  cleaning punctuation
    def clean_punctuation(self, content):
        #regex = re.compile('[%s]' % re.escape(string.punctuation))
        #content = regex.sub(" ", content)
        content = content.translate(content.maketrans("", "", string.punctuation))
        return content
    
    #  cleaning digits
    def clean_numbers(self, content):
        remove_digits = str.maketrans('', '', string.digits)
        text = content.translate(remove_digits)
        return text
    
    #  cleaning e-mails
    def clean_email(self, content):
        reg_email='\S*@\S*\s?'
        pattern_email = re.compile(reg_email)
        content = pattern_email.sub('',content)
        return content

    # clean links, hastag and mentions
    def clean_content(self, text):
        text = self.clean_email(text)
        text = re.sub("@[A-Za-z0-9_]+"," ", text)
        text = re.sub("#[A-Za-z0-9_]+"," ", text)
        text = re.sub(r'http\S+', ' ', text)
        text = re.sub(r'www\S+', ' ', text)
        text = text.replace('RT', ' ')
        text = text.replace('\n', ' ')
        text = text.replace('\t', ' ')
        text = self.clean_stopwords(text)
        text = self.remove_emoji(text)
        text = self.clean_punctuation(text)
        text = self.clean_numbers(text)

        filtered_sentence = []
        for word in text.split(" "):
            if len(word) > 1:
                word = word.strip()
                filtered_sentence.append(word)
        
        text = ' '.join(filtered_sentence)
        return text


def load_json(load_path):
    # read from path
    with open(load_path) as json_file:
        data = json.load(json_file)
    return data

def load_vectorizer(path):
    with open(path, 'rb') as handle:
        vectorizer = pickle5.load(handle)
        return vectorizer

def load_model(path):
    #  load model
    with open(path, 'rb') as handle:
        model = pickle5.load(handle)
        return model
