# 🔨 ml-nlp-tk 🔧

Tools for NLP using Python

This repertory used to handle file io and string cleaning/parsing

## Usage

Install:

```
pip install ml_nlp_tk
```

Before using :
```
from ml_nlp_tk import *
```


# Features
*   [File Handling](#file)  
*   [Text cleaning/parsing](#text)  
*   [Random  Utility](#random)  
*   [Vectorize](#vectorize)  

<h2 id="file">File Handling</h2>    

### get_folders_form_dir(path)
Arguments  
- `path(String)` : getting all folders under this path (string)

Returns  
- `path(String)(generator)` : path of folders under arguments path
Examples  
```
for i in get_folders_form_dir('./corpus/')
    print(i)

'./corpus/kdd'
'./corpus/nycd'
```

### get_files_from_dir(path)
Arguments  
- `path(String)` : getting all files under this path (string)

Returns  
- `path(String)(generator)` : path of files under arguments path
Examples  
```
for i in get_files_from_dir('./data/')
    print(i)

'./data/kdd.txt'
'./data/nycd.txt'
```

###  read_dir_files_yield_lines(path)
Arguments  
- `path(String)` : getting all files line by lines under this path (string)  

Returns  
- `line(String)(generator)` : files line under arguments path  
Examples  
```
for i in read_dir_files_into_lines('./data/')
    print(i)

'file1 sent1'
'file1 sent2'
...
'file2 sent1'
...
```

### read_dir_files_into_lines(path)
Arguments  
- `path(String)` : getting all files line by lines under this path (string)  

Returns  
- `line(String)(generator)` : files line under arguments path  
Examples  
```
i = read_dir_files_into_lines('./data/')
print(i)

['file1 sent1','file1 sent2'...'file2 sent1'...]
```

### read_files_yield_lines(path)
Arguments  
- `path(String)` : getting content in input file path (string)  

Returns  
- `path(String)(generator)` : file line under arguments path  
Examples  
```
for i in read_dir_files_into_lines('./data/kdd.txt')
    print(i)

'sent1'
'sent2'
...
```

### read_files_into_lines(path)
Arguments  
- `path(String)` : getting content in input file path (string)  

Returns  
- `path(String)(generator)` : file line under arguments path  
Examples  
```
i = read_dir_files_into_lines('./data/kdd.txt')
print(i)

['sent1','sent2'...]
```

###  create_new_dir_always(dirPath)
it will replace old dir if exist,or create a new one  
Arguments  
- `dirPath(String)` : dir location  
Examples  
```
create_new_dir_always('./data/')
```

###  get_dir_with_notexist_create(dirPath):
it will create a new dir if not exist  
Arguments  
- `dirPath(String)` : dir location that you want to make sure

Returns  
- `path(String)` : dir location with surely exist
Examples  
```
i = get_dir_with_notexist_create('./data/kdd')
print(i)

'./data/kdd'
```

###  write_json_to_file(json_str, loc)
Arguments  
- `json_str(String)` : json context in string

Returns  
- `path(String)` : output file path
Examples  
```
i = write_json_to_file("{"sent":"hi"}",'./data/kdd.json')
print(i)

"'./data/kdd.json'"
```

###  is_file_exist(path)
Arguments  
- `path(String)` : file location

Returns  
- `result(Boolean)` : file exist or not,true will be exist 
Examples  
```
i = is_file_exist('./data/kdd.txt')
print(i)

true
```

### is_dir_exist(file_dir)
Arguments  
- `path(String)` : dir location

Returns  
- `result(Boolean)` : dir exist or not,true will be exist 
Examples  
```
i = is_dir_exist('./data/kdd')
print(i)

false
```

### download_file(url,save_dir)  
Arguments  
- `url;(String)` : download link  
- `save_dir;(String)` : save location    
Returns  
- `result(string)` : file downloaded location  
Examples  
```
i = download_file('https://raw.githubusercontent.com/voidful/voidful_blog/master/assets/post_src/nninmath_3/img1','./data/')
print(i)

./data/img1
```

<h2 id="text">Text cleaning/parsing</h2>
   
### remove_httplink(string)  
remove http link in context  
Arguments  
- `string(String)` : a string may contain http link   

Returns  
- `result(String)` : string without any http link 

Examples  
```
y = remove_httplink("http://news.IN1802020028.htm 今天天氣http://news.we028.晴朗"))
print(y)

今天天氣 晴朗
```

### split_lines_by_punc(lines)
make lines in array form into sentences array  
it split line base on any punctuation  
Arguments  
- `lines(String Array)` : lines array   

Returns  
- `sentences(String Array)` : split all line base on punctuations  
Examples  
```
y = split_lines_by_punc(["你好啊.hello，me"]))
print(y)

['你好啊', 'hello', 'me']
```

### split_sentence_to_ngram(sentence)
it will split sentence into n-grams as many it can  
##### be careful with sentence length,long sentence will have worse performance  
Arguments
- `sentence(String)` : a string with no punctuation
 
Returns
- `ngrams(String Array)` : ngrams array  

Examples  
```
split_sentence_to_ngram("加州旅館")

['加','加州',"加州旅","加州旅館","州","州旅","州旅館","旅","旅館","館"]
```

### split_sentence_to_ngram_in_part(sentence)
it will split sentence into n-grams with diff start point as many it can  
##### be careful with sentence length,long sentence will have worse performance    
Arguments
- `sentence(String)` : a string with no punctuation
 
Returns
- `ngrams(Array)` : 2D array with diff start in ngram  

Examples  
```
split_sentence_to_ngram_in_part("加州旅館")

[['加','加州',"加州旅","加州旅館"],["州","州旅","州旅館"],["旅","旅館"],["館"]]
```

### spilt_text_in_all_ways(sentence)
it will try to find all possible segments way to split sentence  
Arguments
- `sentence(String)` : input sentence

Returns
- `seg list(String Array)` : all segments in a array  

Examples  
```
spilt_text_in_all_ways("加州旅館")

['加 州 旅 館', '加 州 旅館', '加 州旅 館', '加 州旅館', '加州 旅館', '加州旅 館', '加州旅館']
```

### spilt_sentence_to_array(sentence,splitText=False)
use to split sentences in different kind of language
Arguments
- `sentence(String)` : input sentence
- `splitText(boolean,optional)` : split Chinese in char

Returns
- `segment array(String Array)` : word array

```
spilt_sentence_to_array('你好 are  u 可以')

['你好', 'are', 'u', '可以']

spilt_sentence_to_array('你好 are  u 可以',True)

['你', '好', 'are', 'u', '可', '以']
```

###  join_words_array_to_sentence(words_array):
Arguments
- `words_array(String Array)` : input array

Returns
- `sentence(String)` : output sentence
Examples  
```
join_words_array_to_sentence(['你好', 'are', "可以"])

你好are可以
```

###  passage_into_chunk(passage, chunk_size):
split a passage in particular size  
if part of a sentence excite chunk size, it still put hole sentence into it  
Arguments
- `passage(String)` : input passage
- `num_of_paragraphs(int)` : num of character in one chunk

Returns
- `chunk array(String Array)` : passage in chunk size
Examples  
```
passage_into_chunk("xxxxxxxx\noo\nyyzz\ngggggg\nkkkk\n",10)

['xxxxxxxx\noo\n', 'yyzz\ngggggg\n']
```

### is_all_english(text)
Arguments
- `text(String)` : input text
Returns
- `result(Boolean)` : whether the text is all English or not
Examples  
```
is_all_english("1SGD")
is_all_english("1SG哦")

True
False
```

### is_contain_number(text)
Arguments
- `text(String)` : input text

Returns
- `result(Boolean)` : whether the text contain number or not
Examples  
```
is_contain_number("1SGD")
is_contain_number("SG哦")

True
False
```

### is_contain_english(text)
Arguments
- `text(String)` : input text  
Returns  
- `result(Boolean)` : whether the text contain english or not
Examples  
```
is_contain_english("1SGD")
is_contain_english("123哦")

True
False
```

### is_list_contain_string(text)
Arguments
- `str(String)` : input text  
- `list(String list)` : input string    
Returns  
- `result(Boolean)` : whether the text is a part of list item  
Examples  
```
is_list_contain_string("a", ['a', 'dcd'])
is_list_contain_string("a", ['abcd', 'dcd'])
is_list_contain_string("a", ['bdc', 'dcd'])

True
True
False
```


### full2half(text)
Arguments
- `string(String)` : input string which needs turn to half

Returns
- `(String)` : a half-string

Examples  
```
full2half("，,")

,,
```

### half2full(text)
Arguments
- `text(String)` : input string which needs turn to full

Returns
- `(String)` : a full-string
Examples  
```
half2full("，,")

，，
```
<h2 id="vectorize">Vectorize</h2>   

Vectorize implemented following paper ：  
Baseline Needs More Love:On Simple Word-Embedding-Based Models and Associated Pooling Mechanisms    

###  doc2vec_aver(pretrained_emb, emb_size, context)     
average pooling    
Arguments    
- `pretrained_emb(object)` : pre-trained word embedding that able to get vector in this form : ``pretrained_emb['word']``   
- `emb_size(int)` : size of pre-trained word embedding     
- `context(list)` : input doc in list - each item of list must able to gain vector in pretrained_emb like : ``pretrained_emb[context[0]]``   

Returns    
- `document vector(list)` : vectorized context  

Examples    
```python 
from gensim.models import Word2Vec
pretrain_wordvec = gensim.models.KeyedVectors.load_word2vec_format('wiki.vec', encoding='utf-8')
size = pretrain_wordvec.vector_size
context = "測試文本哈哈哈"
ml_nlp_tk.doc2vec_aver(pretrain_wordvec, size, jieba.lcut(context))
```

###  doc2vec_max(pretrained_emb, emb_size, context)  
max pooling in each dim   
Arguments   
- `pretrained_emb(object)` : pre-trained word embedding that able to get vector in this form : ``pretrained_emb['word']``  
- `emb_size(int)` : size of pre-trained word embedding   
- `context(list)` : input doc in list - each item of list must able to gain vector in pretrained_emb like : ``pretrained_emb[context[0]]`` 

Returns  
- `document vector(list)` : vectorized context
Examples  
```python 
from gensim.models import Word2Vec
pretrain_wordvec = gensim.models.KeyedVectors.load_word2vec_format('wiki.vec', encoding='utf-8')
size = pretrain_wordvec.vector_size
context = "測試文本哈哈哈"
ml_nlp_tk.doc2vec_max(pretrain_wordvec, size, jieba.lcut(context))
```

###  doc2vec_concat(pretrained_emb, emb_size, context)
concat average pooling and max pooling result  
Arguments  
- `pretrained_emb(object)` : pre-trained word embedding that able to get vector in this form : ``pretrained_emb['word']``  
- `emb_size(int)` : size of pre-trained word embedding   
- `context(list)` : input doc in list - each item of list must able to gain vector in pretrained_emb like : ``pretrained_emb[context[0]]`` 

Returns  
- `document vector(list)` : vectorized context
Examples  
```python 
from gensim.models import Word2Vec
pretrain_wordvec = gensim.models.KeyedVectors.load_word2vec_format('wiki.vec', encoding='utf-8')
size = pretrain_wordvec.vector_size
context = "測試文本哈哈哈"
ml_nlp_tk.doc2vec_concat(pretrain_wordvec, size, jieba.lcut(context))
```

###  doc2vec_hier(pretrained_emb, emb_size, context, windows)
average pooling in sliding windows then max pooling   
Arguments  
- `pretrained_emb(object)` : pre-trained word embedding that able to get vector in this form : ``pretrained_emb['word']``  
- `emb_size(int)` : size of pre-trained word embedding    
- `context(list)` : input doc in list - each item of list must able to gain vector in pretrained_emb like : ``pretrained_emb[context[0]]``   
- `windows(int)` : size of sliding windows in array   

Returns  
- `document vector(list)` : vectorized context
Examples  
```python 
from gensim.models import Word2Vec
pretrain_wordvec = gensim.models.KeyedVectors.load_word2vec_format('wiki.vec', encoding='utf-8')
size = pretrain_wordvec.vector_size
context = "測試文本哈哈哈"
ml_nlp_tk.doc2vec_hier(pretrain_wordvec, size, jieba.lcut(context))
```

###  cosine_similarity(vector 1, vector 2)
cal cosine similarity between two vector
Arguments  
- `vector(list)` : vector

Returns  
- `cos similarity(float)` : similarity of two vector
Examples  
```
from gensim.models import Word2Vec
pretrain_wordvec = gensim.models.KeyedVectors.load_word2vec_format('wiki.vec', encoding='utf-8')
size = pretrain_wordvec.vector_size

input1 = ml_nlp_tk.doc2vec_concat(pretrain_wordvec, size, "DC")
input2 = ml_nlp_tk.doc2vec_concat(pretrain_wordvec, size, "漫威")
ml_nlp_tk.cosine_similarity(input1,input2)
```


<h2 id="random">Random  Utility</h2>    

###  random_string(length)
Arguments  
- `length(int)` : length with random string

Returns  
- `randstr(String)` : size will be length in "0123456789ABCDEF"
Examples  
```
random_string(10)

D6857CE0F4
```

### random_string_with_timestamp(length)
Arguments  
- `length(int)` : length with random string

Returns  
- `randstr(String)` : size will be length + timestamp length(10)
Examples  
```
random_string_with_timestamp(1)

1435474326D
```

### random_value_in_array_form(array)
random value with range in array form  
int,float : [min,max]  
string : [candidate1,candidate2...]   

Arguments  
- `range(array)` : range in array form

Returns  
- `random result(depend on input)` : a random value under input condition
Examples  
```
# for string
y = random_value_in_array_form(["SGD","ADAM","XDA"])
print(y)

'ADAM'

# for int
y = random_value_in_array_form([1,12])
print(y)

4

# for float
y = random_value_in_array_form([0.01,1.00])
print(y)

0.34
```