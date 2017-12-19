# Course Search

## Overview (Function)

Learning on e-learning platforms is not very interactive. This is the problem this project tries to target by providing a mechanism for interactive information retrieval within the study material. 

Searching relevant resource within a course is not interactive and time consuming. Imagine that we are pursuing an online course on an e-learning portal. For example, a machine learning course. Now, let us say that this course contains a couple of videos and we have gone through some of them. We are now studying our next video. This video mentions a topic which we have already studied in the course. However, it happens many times that we don’t remember details of the topic we have already studied. So, we would wish to review that topic before we can progress in the course. How do we know which video discusses this topic, if we don’t remember? Do we go to each video and look for the relevant content? Video titles are sometimes not enough to figure out the details of the material discussed. Imagine if we had a real professor, he/she would guide us to where we can find exactly the information we are looking for.

Interactive information retrieval can solve this problem.

This program lets user to train over a fixed dataset, and then run queries to find best study material that discusses the topic in query. 

## Usage 

### Initial Set-up
Before running the script, you need to install following dependencies:
1. [NLTK](http://www.nltk.org/install.html)
2. [GraphLab](https://turi.com/download/install-graphlab-create.html)

### Running
Usage: python search.py -d [folderPath]
[folderPath] is the path containing training documents (txt files).

To test with sample data-set, run: python search.py -d transcripts

It will then prompt and ask user to enter search query. Result of query is totally context dependent. For the sample data-set in this repository, documents are related to machine learning. Following queries will result valid result:
1) What is regression
2) Explain clustering
so on...



### Dataset
The repository contains a small dataset for course text (subtitles) from a Coursera case. The dataset can be found in "transcripts" folder. Idea here that each text file here represents a study material, and we want to search the best on for the query. 

User can create their own dataset by compiling all text files into a single folder.

