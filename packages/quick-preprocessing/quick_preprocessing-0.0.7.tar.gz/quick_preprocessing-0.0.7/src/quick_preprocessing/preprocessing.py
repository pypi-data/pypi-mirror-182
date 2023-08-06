from ensure import ensure_annotations
from quick_preprocessing.manual_exception import InvalidListException
from quick_preprocessing.logger import logger
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
import pkg_resources
from symspellpy import SymSpell, Verbosity


@ensure_annotations
def lemmatize_preprocessing(main_list: list):
    try:
        if main_list is None:
            raise InvalidListException("list cannot be null")
        else:
            corpus = []
            lemmatizer = WordNetLemmatizer()
            for i in range(0, len(main_list)):
                review = re.sub('[^a-zA-Z]', ' ', main_list[i])
                # logger.info(f"removing punctuations: {review}")
                review = review.lower()
                # logger.info(f"lowering the sentence: {review}")
                review = ' '.join(
                    [lemmatizer.lemmatize(word) for word in review.split() if word not in stopwords.words('english')])
                corpus.append(review)
                # logger.info(f"successfully preprocessed")
        return corpus
    except Exception as e:
        raise e


@ensure_annotations
def stemming_preprocessing(main_list: list):
    try:
        if main_list is None:
            raise InvalidListException("list cannot be null")
        else:
            corpus = []
            ps = PorterStemmer()
            for i in range(0, len(main_list)):
                review = re.sub('[^a-zA-Z]', ' ', main_list[i])
                review = review.lower()
                review = ' '.join([ps.stem(word) for word in review.split() if word not in stopwords.words('english')])
                corpus.append(review)
        return corpus
    except Exception as e:
        raise e


sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)
dictionary_path = pkg_resources.resource_filename("quick_preprocessing", "frequency_dictionary_en_82_765.txt")
bigram_path = pkg_resources.resource_filename("quick_preprocessing", "frequency_bigramdictionary_en_243_342.txt")


def spell_corrector(input_term):
    sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1)
    sym_spell.load_bigram_dictionary(bigram_path, term_index=0, count_index=2)

    suggestions = sym_spell.lookup_compound(input_term, max_edit_distance=2)

    # display suggestion term, edit distance, and term frequency
    sent = []
    for suggestion in suggestions:
        sent.append(suggestion)

    predicted_sentence = str(sent[0])
    splitter = predicted_sentence[:-6]
    return splitter

# output = spell_corrector(input_term='The yougn boy finaly understod the diffrence betwen paralell and perpendcular.')
# print(output)
