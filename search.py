
# coding: utf-8

# In[1]:

import nltk
import graphlab
import os


# In[ ]:




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
transcripts = "transcripts"
filesDataSFrame=readFiles("transcripts")
if(not len(filesDataSFrame)):
    print "Error in reading transcripts"
filesDataSFrame = computerTfIdf(filesDataSFrame, "Text")


# In[6]:

filesDataSFrame.head()


# In[13]:

graphlab.text_analytics.bm25(filesDataSFrame["word_count"], ['linear', 'regression'])


# In[14]:

print filesDataSFrame[0]["Text"]


# In[ ]:



