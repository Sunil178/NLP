from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import string
paragraph = "london england liverpool football club one england prestigious teams announced wednesday board agreed sell team new england sports ventures company owns baseball boston red sox sale conditional approval premier league liverpool belongs resolution dispute board membership matters liverpool said offer nesv one two club said tuesday received repay long term debt called board meeting tuesday review bids approve sale amount sale immediately disclosed size debt reported million million pounds sale mean liverpool liverpool huge fan base around world currently owned two americans tom hicks george gillett took loans club name buy february liverpool position english premier league slipped owners become targets angry fans liverpool failed qualify season lucrative european champions league team currently th english league seven matches worst start season decades liverpool chairman martin broughton said board met nesv representatives past several weeks boston london liverpool praised company vision english team think sale sound ireport nesv philosophy winning fully demonstrated red sox broughton said revealed problems board hicks gillett saying pair tried everything prevent sale blog jumping frying pan fire removing burden acquisition debt offer allows us focus investment team disappointed owners tried everything prevent deal happening need go legal proceedings order complete sale broughton said history liverpool images tuesday meeting two owners sought remove two board members replace mack hicks reported liverpool echo tom hicks son lori kay mccutcheon newspaper said vice president financial controller hicks holdings second bidder asia linked kenny huang led chinese consortium interested investing liverpool summer echo reported nicky robertson atlanta georgia contributed report."

punctuation = list(string.punctuation)
stop_words = list(stopwords.words('english'))
sentence = sent_tokenize(paragraph)

words = []
for sent in sentence:
	word = word_tokenize(sent)
	for element in word:
		words.append(element)
words_without_punctuation = []
for i in words:
	if i not in punctuation:
		words_without_punctuation.append(i)
words_after_stop = []
for stop in words_without_punctuation:
	if stop not in stop_words:
		words_after_stop.append(stop)
print(words_after_stop)