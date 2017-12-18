
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

### Main task
if __name__ == '__main__':
	from sys import argv
	transcripts = ""
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
	query = ""
	while not (query == "quit" or query == "q"):
		query = raw_input('Enter query: ')
	sys.exit(0)

# In[6]:

filesDataSFrame.head()


# In[13]:

graphlab.text_analytics.bm25(filesDataSFrame["word_count"], ['linear', 'regression'])


# In[14]:

print filesDataSFrame[0]["Text"]


# In[ ]:



