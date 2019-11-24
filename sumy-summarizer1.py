import sumy

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

txtfile = 'elonmusk_tweets.txt'

parser = PlaintextParser.from_file(txtfile, Tokenizer("english"))

summarizer = LexRankSummarizer()
summary = summarizer(parser.document, 20)


with open('donaldtweetsummary' + '.txt', 'w') as txtfile:
	for sentence in summary:
        txtfile.write(sentence)
        #txtfile.write(str(st.encode('utf-8')))
