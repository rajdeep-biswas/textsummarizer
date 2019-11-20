import pandas as pd

def csv2str(filename, columnName):
    df = pd.read_csv(filename + '.csv')
    st = ''
    for sent in df[columnName].sample(n = 500):
        if 'http' not in sent:
            st += sent + '. '
    # st.replace('\'b', '')
    # st.replace('"b', '')
    with open(filename + '.txt', 'w') as txtfile:
        txtfile.write(st)

csv2str('elonmusk_tweets')
