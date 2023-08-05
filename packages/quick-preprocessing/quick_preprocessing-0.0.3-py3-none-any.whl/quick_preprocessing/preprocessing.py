from ensure import ensure_annotations
from quick_preprocessing.manual_exception import InvalidListException
from quick_preprocessing.logger import logger
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
from nltk.stem import WordNetLemmatizer


@ensure_annotations
def text_preprocessing(main_list: list):
    try:
        if main_list is None:
            raise InvalidListException("list cannot be null")
        else:
            corpus = []
            lemmatizer = WordNetLemmatizer()
            for i in range(0, len(main_list)):
                review = re.sub('[^a-zA-Z]', ' ', main_list[i])
                #logger.info(f"removing punctuations: {review}")
                review = review.lower()
                #logger.info(f"lowering the sentence: {review}")
                review = ' '.join([lemmatizer.lemmatize(word) for word in review.split() if word not in stopwords.words('english')])
                corpus.append(review)
                #logger.info(f"successfully preprocessed")
        return corpus
    except Exception as e:
        raise e
