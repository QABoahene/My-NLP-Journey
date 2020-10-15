# Natural Language Processing Techniques on US Presidential Debate 2020


## Introduction
In this project, I used the Google Cloud Language Python API to perform sentiment analysis and entity recognition analysis on the transcript of the debate between President Donald Trump and Vice President (Former) and Presidential candidate Joe Biden. 
The idea was to practice codes for the above tasks  and also get to see how the outputs of the tasks above can summarize the debate.  
The data is a transcript of the debate from Kaggle (https://www.kaggle.com/gpreda/usa-presidential-debate-2020)

### Tasks/Techniques
* Entity Analysis

* Sentiment Analysis

### Technologies used
* Pandas

* Google Cloud Language Python API

* Plotly

* WordCloud

* Matplotlib

## Sentiment Analysis
From the sentiment analysis on the document, the debate was flagged as **negative** (see below).

![Image of Sentiment Analysis](https://github.com/QABoahene/My-NLP-Journey/blob/main/NLP%20-%20Presidential%20Debate/Images/Sentiment%20Analysis%20Result.png?raw=true)

## Entity Recognition Analysis
In performing the entity recognition analysis, six (6) entities were considered, they are: Persons, Numbers, Consumers, Events, Locations and Organizations. This insight will further give us an idea what was talked about in terms of these entities and how much of it dominated the debate. 

The pie chart below shows the percentage of entities present in the debate. It shows that a lot of persons were talked about in the debate.

![Pie Chart](https://github.com/QABoahene/My-NLP-Journey/blob/main/NLP%20-%20Presidential%20Debate/Images/Pie%20Chart%20-%20Entity%20Recognition.png)

**Person Entity** basically brings our anything that can be referred to as a person, including names, titles, etc. The word cloud below shows the person entities present in the debate, keep in mind that the biggest words have the highest occurrence in the debate. 

![Person Entity](https://github.com/QABoahene/My-NLP-Journey/blob/main/NLP%20-%20Presidential%20Debate/Images/Person%20Entity.png)

**Number Entities** helps highlight numbers that were mentioned during the debate, this will especially be important for any research into the numbers mentioned in the debate for referencing purposes. The whole idea of this is to be able to do in a short time something that will take hours to do because the transcript of the debate is a large and long document. See below the numbers that were dropped in the debate.

![Number Entity](https://github.com/QABoahene/My-NLP-Journey/blob/main/NLP%20-%20Presidential%20Debate/Images/Numbers%20Entity.png)

To keep it short, the rest of the images will be about the other entities mentioned, you'll be able to see what was talked about the most by following the above structure.

**Organization Entity**

![Organization Entity](https://github.com/QABoahene/My-NLP-Journey/blob/main/NLP%20-%20Presidential%20Debate/Images/Organization%20Entity.png)

**Locations Entity**

![Locations Entity](https://github.com/QABoahene/My-NLP-Journey/blob/main/NLP%20-%20Presidential%20Debate/Images/Locations%20Entity.png)

**Event Entity**

![Event Entity](https://github.com/QABoahene/My-NLP-Journey/blob/main/NLP%20-%20Presidential%20Debate/Images/Event%20Entity.png)

**Consumer Entity**

![Consumer Entity](https://github.com/QABoahene/My-NLP-Journey/blob/main/NLP%20-%20Presidential%20Debate/Images/Consumer%20Entity.png)
