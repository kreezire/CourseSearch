
# coding: utf-8

# In[1]:

import nltk
import graphlab
import os
import sys


# In[ ]:
#parseCommandLineArguments: parse arguments passed to the program
#returns -1 if it fails

def readCommandLineArgs(argv):
	#print len(argv)
	opts = {}  # Empty dictionary to store key-value pairs.
	hasArgs = False
	while argv:  # While there are arguments left to parse...
		if argv[0][0] == '-':  # Found a "-name value" pair.
			hasArgs = True
			opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
		argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
	if hasArgs == False:
		return -1
	return opts

def printHelp():
	print "Usage: python search.py -d [folderPath]"
	sys.exit(0)
# In[2]:

# readFiles reads files from the specified path.
# param: path
# return (file list, file test) as SFrame
def readFiles(path):
    filesDataSFrame = graphlab.SFrame()
    try:
        files = [path+"/"+f for f in os.listdir(path) ]
        fileText = []
        for f in files:
            fileText.append(open(f).read())
        filesDataSFrame["File"]=files
        filesDataSFrame["Text"]=fileText
    except:
        return filesDataSFrame
    return filesDataSFrame


# In[3]:

# computerTfIdf takes SFrame and field containing text in SFrame, and computer TF-IDF
# params: SFrame, field Label
# returns word count and tdidf added in sframe
def computerTfIdf(filesDataSFrame, textField):
    filesDataSFrame['word_count'] = graphlab.text_analytics.count_words(filesDataSFrame[textField])
    filesDataSFrame['tfidf'] = graphlab.text_analytics.tf_idf(filesDataSFrame['word_count']).dict_trim_by_keys(graphlab.text_analytics.stopwords(), True)
    return filesDataSFrame


# In[5]:
stop_words = set(nltk.corpus.stopwords.words('english'))

### Main task
if __name__ == '__main__':
	from sys import argv
	print "\n\n training ..."
	transcripts = ""
	#print "dubug1"
	myargs = readCommandLineArgs(argv)
	if myargs == -1:
		printHelp()
	if '-d' in myargs:  
		transcripts = myargs['-d']
	else:
		printHelp()
	filesDataSFrame=readFiles(transcripts)
	print (filesDataSFrame.num_rows())
	if(not (filesDataSFrame.num_rows())):
		print "Error in reading transcripts."
		printHelp()
	filesDataSFrame = computerTfIdf(filesDataSFrame, "Text")
	print "\n\n"
	query = ""
	while True:
		query = raw_input('Enter query: ')
		if (query == "quit" or query == "q"):
			sys.exit(0)
		query_strip = query.strip()
		query_tokens = nltk.tokenize.word_tokenize(query_strip)
		query_FilteredSet= [w for w in query_tokens if not w in stop_words]
		result = False
		printString = ""
		if len(query_FilteredSet)>0:
			ranking = graphlab.text_analytics.bm25(filesDataSFrame["word_count"], query_FilteredSet)
			if ranking.num_rows()>0:
				if ranking[0]["bm25"]>0.5:
					result = True
					printString = "\n<query>"+query+"</query>"
					count = 1;
					printString = printString+"\n<result>"
					for id in ranking["doc_id"]:
						printString += "\n<"+str(count)+"> "
						printString += transcripts+"\\"+filesDataSFrame[id]["File"]
						printString += " </"+str(count)+">"
						count = count + 1
					printString = printString+"\n</result>"
						
		
		if not result:
			print "\nCould not retrieve study material for this query. Please try another query."
		else:
			print printString
		#print query_FilteredSet
		
		
	sys.exit(0)

# In[6]:

filesDataSFrame.head()


# In[13]:

graphlab.text_analytics.bm25(filesDataSFrame["word_count"], ['linear', 'regression'])


# In[14]:

print filesDataSFrame[0]["Text"]


# In[ ]:



