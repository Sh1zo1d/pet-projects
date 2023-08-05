import pandas as pd
import nltk
import re
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from nltk import word_tokenize, pos_tag
from nltk.corpus import stopwords
import streamlit as st
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')
nltk.download('tagsets')
st.title('Автоматическая классификация уровня сложности видеоматериалов на английском языке по субтитрам')
file = st.file_uploader('Загрузите субтитры в формате ".srt" ', type='srt')
CLEANR_HTML = re.compile(r'\<[^>]*\>')


def cleanhtml(raw_html):
    cleantext = re.sub(CLEANR_HTML, ' ', raw_html)
    return cleantext


CLEANR_BRACK = re.compile(r'[\([{})\]]')


# CLEANR_BRACK = re.compile(r'\(.*?\)()')
def cleanbrack(raw_brack):
    cleantext = re.sub(CLEANR_BRACK, ' ', raw_brack)
    return cleantext

#
# def list_n_to_list(row):
#     return ' '.join(row).split('\n')


# def strip_punkt(row_punkt):
#     return list(map(lambda x: x.strip(',.<>/?\\!@#$%^&*\'()_++?:%:;№!",{}[]-'), row_punkt))


CLEANR_SLASH = re.compile(r'/|,')


# def slash_dot(raw_lash):
#     return re.sub(CLEANR_SLASH, ' ', raw_lash)


rs = 7




def to_set(row):
    return set(row)


sw_lst = stopwords.words('english')


def stopw_count(row):
    stop_c = 0
    for i in range(len(row)):
        if row[i] in sw_lst:
            stop_c += 1
    return stop_c


dct = {'A1': '0', 'A2+': '1.5', 'A2': '1', 'B1': '2', 'B2': '3', 'C1': '4', 'C2': '5'}
dct_verse = {"0.0": "A1",
             "1.0": "A2",
             "1.25": "A2+",
             "1.5": "A2+",
             "2.0": "B1",
             "3.0": "B2",
             "4.0": "C1",
             "5.0": "C2"}
import io
import pickle
def lr(features):
    global predicted_numeric
    predicted_numeric = lr_model.predict(features)
def rfc(features):
    global predicted_class
    predicted_class = rfc_model.predict(features)
CLEANR_NUMBERS = "\d+"
CLEANR_SS = r'[,:->--]'
if file is not None:
    data = pd.DataFrame()

    stringio = io.StringIO(file.getvalue().decode("utf-8"))
    string_data = stringio.read()
    # st.write(string_data)
    # file_read = file.read().decode('utf-8')
    lst_column = []
    clean_text = cleanbrack(cleanhtml(string_data).strip(',.<>/?!-♪')).lower()
    lst_column.append(clean_text)
    # st.text(lst_column)
    # st.text(lst_column[0])
    # st.markdown(lst_column[0])

    data.loc[0, 'sub_list'] = lst_column[0]
    data.loc[0, 'sub_list'] = re.sub(CLEANR_NUMBERS, "", data['sub_list'][0])
    data.loc[0, 'sub_list'] = re.sub(CLEANR_SS, " ", data['sub_list'][0])
    data.loc[0, 'sub_list'] = cleanbrack(cleanhtml(data['sub_list'][0]).strip('<>/-♪')).lower().split()

    data['sub_set'] = data['sub_list'].apply(to_set)
    data['sub_big_string'] = data['sub_list'].apply(lambda x: ' '.join(x))
    data['sent_tokenise'] = data['sub_big_string'].apply(sent_tokenize)

    data['conjunction'] = 0
    data['cardinal'] = 0
    data['determiner'] = 0
    data['existential'] = 0
    data['foreign_word'] = 0
    data['preposition'] = 0
    data['modal'] = 0
    data['adjective'] = 0
    data['noun'] = 0
    data['genitive'] = 0
    data['pronoun'] = 0
    data['adverb'] = 0
    data['particle'] = 0
    data['to'] = 0
    data['interjection'] = 0
    data['verb'] = 0
    conjunction_lst = ['CC']
    cardinal_lst = ['CD']
    determiner_lst = ['DT', 'PDT', 'WDT']
    existential_lst = ['EX']
    foreign_word_lst = ['FW']
    preposition_lst = ['IN']
    modal_lst = ['MD']
    adjective_lst = ['JJ', 'JJR', 'JJS']
    noun_lst = ['NNP', 'NNPS', 'NN', 'NNS']
    genitive_lst = ['POS']
    pronoun_lst = ['PRP', 'PRP$', 'WP', 'WP$']
    adverb_lst = ['RB', 'RBR', 'RBS']
    particle_lst = ['RP']
    to_lst = ['TO']
    interjection_lst = ['UH']
    verb_lst = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
    #
    #
    text = word_tokenize(re.sub(r'[,.?!&]', ' ', data['sub_big_string'][0]))
    tagged = pos_tag(text)
    for word, tag in tagged:
        if tag in conjunction_lst:
            data.loc[0, 'conjunction'] += 1
        if tag in cardinal_lst:
            data.loc[0, 'cardinal'] += 1
        if tag in determiner_lst:
            data.loc[0, 'determiner'] += 1
        if tag in existential_lst:
            data.loc[0, 'existential'] += 1
        if tag in foreign_word_lst:
            data.loc[0, 'foreign_word'] += 1
        if tag in preposition_lst:
            data.loc[0, 'preposition'] += 1
        if tag in modal_lst:
            data.loc[0, 'modal'] += 1
        if tag in adjective_lst:
            data.loc[0, 'adjective'] += 1
        if tag in noun_lst:
            data.loc[0, 'noun'] += 1
        if tag in genitive_lst:
            data.loc[0, 'genitive'] += 1
        if tag in pronoun_lst:
            data.loc[0, 'pronoun'] += 1
        if tag in adverb_lst:
            data.loc[0, 'adverb'] += 1
        if tag in particle_lst:
            data.loc[0, 'particle'] += 1
        if tag in to_lst:
            data.loc[0, 'to'] += 1
        if tag in interjection_lst:
            data.loc[0, 'interjection'] += 1
        if tag in verb_lst:
            data.loc[0, 'verb'] += 1
    data['stopwords_count'] = stopw_count(text)
    with open('lr_model.pkl', 'rb') as file:
        lr_model = pickle.load(file)
    with open('rfc_model.pkl', 'rb') as file:
        rfc_model = pickle.load(file)
    st.write(f'Категории уровней сложностей и их численные значения:')
    st.write(dct_verse)
    lr(data.loc[:, 'conjunction':'stopwords_count'])
    rfc(data.loc[:, 'conjunction':'stopwords_count'])
    st.write(predicted_class[0])
    st.write(
        f'Сложность данного видеоматериала по шкале CERF равна категории {dct_verse[str(predicted_class[0])]}, а ее дискретное значение равно {predicted_numeric}.')
    st.write(f"Усредненное предсказание двух моделей равно {(float(predicted_class[0])+predicted_numeric)/2}")
