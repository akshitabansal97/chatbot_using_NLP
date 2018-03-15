import nltk
import numpy as np
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import PorterStemmer
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import json
import random

from pprint import pprint
_end='_end'
def make_trie(words):
        root = dict()
        for word in words:
           current_dict = root
           for letter in word:
              current_dict = current_dict.setdefault(letter, {})
           current_dict[_end] = _end
        return root

def add_word(root,word):
         current_dict=root
         for letter in word:
               current_dict = current_dict.setdefault(letter, {})
         current_dict[_end] = _end
         return root
               
    

def in_trie(trie, word):
     current_dict = trie
     for letter in word:
         if letter in current_dict:
             current_dict = current_dict[letter]
         else:
             return False
     else:
         if _end in current_dict:
                return True
         else:
            return False
# with open('data.json') as data_file:

# result = []
# for item in data:
#     my_dict={}
#     my_dict['intent']=item.get('intent')
#     print (my_dict)
#     result.append(my_dict)
# pprint(data[1])
input_file=open('greetings.json','r')
json_decode = json.load(input_file)
input_file1=open('aboutjaypee.json','r')
json_decode1 = json.load(input_file1)
input_file2=open('contact.json','r')
json_decode2 = json.load(input_file2)
input_file3=open('farewell.json','r')
json_decode3 = json.load(input_file3)
print("done loading")
                
my_dict = {}
my_dict['msg']=json_decode['msg']
f= [item for sublist in list(my_dict.values()) for item in sublist]
#my_dict['response']=json_decode['response']
my_dict1 = {}
my_dict1['msg']=json_decode1['msg']
f1= [item for sublist in list(my_dict1.values()) for item in sublist]
#my_dict1['response']=json_decode1['response']
# print(my_dict1['msg'])
my_dict2 = {}
my_dict2['msg']=json_decode2['msg']
f2= [item for sublist in list(my_dict2.values()) for item in sublist]
my_dict3 = {}
my_dict3['msg']=json_decode3['msg']
f3= [item for sublist in list(my_dict3.values()) for item in sublist]
#my_dict2['response']=json_decode2['response']
gres=["Hi ! how may i help you ","Hey good to see you ! How can i help","Hello What help do you need ","hi! what can i do for you","greetings how can i be of assistance today"]
cres=["24X7 Helpline No:1-911-2024-00973    Contact number: +91-120-2400973    Email Id:webadmin@jiit.ac.in   Location/Address: A-10, Sector-62, ,Noida-201 309, Uttar Pradesh, India."]
fres=["Bye !Hope to see you again"," Tata! Good day", "Farewell my friend"]
ares=["Jaypee Institute of Information Technology, Noida was established in the year 2001 and has been declared as a Deemed to be University","JIIT’s state-of-the-art, environmentally conditioned campus comprises smart buildings with Wi-Fi connectivity covering the Academic Block, Business School cum Research Block, Faculty Residences, Student Hostels and Annapurna","JIIT has been constantly ranked amongst the top engineering Institutes in Delhi NCR. Recently it has been ranked among top Engineering Institutes in India by Edu Rand 2014 Engineering College Rankings.","Mission:To develop as a benchmark University in emerging technologies.","The streams offered in Btech are: CSE,IT,ECE and BIOTECH"]
# print(nnp)
count=0
root=make_trie(f)
root1=make_trie(f1)
root2=make_trie(f2)
root3=make_trie(f3)
fbye=0
while 1:
    example=input("enter string")
    #example="Hello Mrs. Akshita. I have queries related to admission."
    # print "---------------sent_tokenize--------------"
    # print(sent_tokenize(example))
    # print "---------------word_tokenize--------------"
    # print(word_tokenize(example))
    # print "---------------loop--------------"
    # for i in word_tokenize(example):
    #     print(i)
    # print "---------------stop_words--------------"
    # stop_words=set(stopwords.words("english"))

    # words=word_tokenize(example)
    #
    # filtered_sentence = []
    # for w in words:
    #     if w not in stop_words:
    #         filtered_sentence.append(w)
    # #print(filtered_sentence)
    #
    # print "---------------stemming--------------"
    # ps = PorterStemmer()
    #
    # example_words = ["python","pythoner","pythoning","pythoned","pythonly"]
    # for w in example_words:
    #     #print(ps.stem(w))
    # print "---------------stemming sentence--------------"
    # new_text="it is very important to be pythonly while you are pythoning with python. All pythoners have pythoned once."
    # words=word_tokenize(new_text)
    # for w in words:
    #     #print(ps.stem(w))
    #
    # print "---------------parts of speech--------------"
    # train_text = state_union.raw("2005-GWBush.txt")
    # sample_text = state_union.raw("2006-GWBush.txt")

    # custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
    #
    # tokenized = custom_sent_tokenizer.tokenize(example)

    def process_content():
        try:
            #for i in tokenized:
                # words = nltk.word_tokenize(i)

                stop_words=set(stopwords.words("english"))

                words=word_tokenize(example)

                filtered_sentence = []
                for w in words:
                    if w not in stop_words:
                        filtered_sentence.append(w)
                # print(filtered_sentence)

                tagged = nltk.pos_tag(filtered_sentence)
                # print(tagged)


                # print "---------------chunking + chinking --------------"
                # chunkGram = r"""Chunk: {<VBN.?>*<NNP>+<NN>?}
                #                             """
                #
                # chunkParser = nltk.RegexpParser(chunkGram)
                # print("----------------------------")
                # chunked = chunkParser.parse(tagged)
                noun=[]
                vbn=[]
                pos_a=[]
                pos_1=[]
                for word,pos in tagged:
                    pos_a.append(pos)
                # for p in pos_a:
                #     for p not in pos_1:
                #         pos_1.append(p)
                    # if (pos=='NNP'):
                    #     noun.append(word)

                # pos_l=list(set(pos_a))
                # # print(pos_l)
                # # for word,pos in tagged:
                # for l in pos_l:
                #     for word in tagged:
                #     # print(l)
                #         if l=='NN':
                #             noun.append(word)
                #         if l=='VBN':
                #             vbn.append(word)
                count_nn=0
                count_nnp=0
                count_vbn=0
                count_nns=0
                # list=range (4)
                # def fun(x):
                #     x=1
                #     y=x*2
                # wefunc=np.vectorize(fun)
                # print(wefunc )
                # print(tagged)
                nnp=[]
                nn=[]
                vbn=[]
                nns=[]
                all1=[]
                for f,pos in tagged:
                    all1.append(f)
                    if pos =='NN':
                        # print(f)
                        count_nn=count_nn+1
                        nn.append(f)
                    if pos=='NNP':
                        count_nnp=count_nnp+1
                        nnp.append(f)

                    if pos=='VBN':
                        count_vbn=count_vbn+1
                        vbn.append(f)
                        # print(f)
                    if pos=='NNS':
                        count_nns=count_nns+1
                        nns.append(f)
                        # print(f)
                    # if count_nnp > 1:
                    #     print(f)
                # print(count_nnp)
                #print(nnp)
                #print(nn)
                #print(nns)
                #print(vbn)
                # if count_vbn>1:
                #     print(f[0][0])
                # else:
                #     print(f)
                # if count_nnp>1:
                #     print(f[0][0])
                # else:
                #     print(f)

                # print(count_nn)
                # print(count_nnp)
                # print(count_vbn)
                # print(count_prp)
                # print(tagged)
                # print(vbn)

                
                #checking and searching
                #print(root1)
                flag=0
                secure_random = random.SystemRandom()
                print(all1)
                for v in all1:
                    #print(v)
                    if (in_trie(root,v.lower())):
                        flag=1
                        print(secure_random.choice(gres))
                        

                    elif (in_trie(root1,v.lower())):
                        flag=1
                        print(secure_random.choice(ares))
                       

                    elif (in_trie(root2,v.lower())):
                        flag=1
                        print(secure_random.choice(cres))

                    elif (in_trie(root3,v.lower())):
                        flag=1
                        fbye=1
                        print("fbye ",fbye)
                        print(secure_random.choice(fres))
                        return 1
                        break

                if(flag==0):
                    print("Sorry i am unable to interpret ",secure_random.choice(cres))
            
                       

                # print(my_dict['msg'])

                # print(json_decode['msg'])
                # for g in nnp:
                #     print(g)
                #     if g in json_decode['msg']:
                #         print(g)
                #         print('yes')
                #     else:
                #         print('no')
                # for m,n in enumerate(noun):
                #     pos_l=set(n[1])
                    # print(pos_l)

                # print(".................")
                # print(vbn)
                # nltk.chunk.conllstr2tree(chunked, chunk_types=['NP']).draw()
                # # k=[]
                # #
                # # k.append(chunked)
                # # #print(k)
                # count=0
                # for m in chunked:
                #     for g in m:

                #print(chunked)
                # tree=nltk.Tree('PRP',['I'])
                # print(tree)



                # print(chunked[0][0][0])
                # print(chunked[1])
                # print(chunked[2])
                # print(chunked[3])
                # print(chunked[4])
                # print(chunked[5][0][0])
                #chunked.draw()
                # print "---------------named entity recognition--------------"
                # namedEnt = nltk.ne_chunk(tagged)
                # print(namedEnt)
                # print "---------------named entity recognition without specifically telling org,date, etc.----------"
                # namedEnt = nltk.ne_chunk(tagged, binary=True)
                # y=namedEnt[0]
                # print(y)
                # return y
                # # namedEnt.draw()





    
             
        except Exception as e:
            print(str(e))
    
    
    
    fbye=process_content()
    #print("value of fbye ",fbye)
    if(fbye==1):
        break

    # print(x)
    # # print "---------------wordnet--------------"
    # syns = wordnet.synsets("x")
    # #
    # # #synsets-list
    # print(syns)
    # # #synsets
    # # print(syns[0].name())
    # # #lemma
    # print(syns[0].lemmas())
    # # # #just the word
    # # print(syns[0].lemmas()[0].name())
    # # # #definition
    # # # print(syns[0].definition())
    # # # #examples
    # # print(syns[0].examples())
