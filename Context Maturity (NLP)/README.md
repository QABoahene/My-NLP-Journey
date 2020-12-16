# Context Maturity
## Background
Listening to Busta Rhyme's new album in 2020, I had a thought. The lyrics of the songs on the album caught my attention because of what he was talking about. Things he talked about were about social justice, politics, black live movements and events surrounding these things. I have been a fan of Busta Rhymes ever since I started listening to Hip Hop, which is a long time ago. This made me wonder how much his lyrics have changed since his first album, mixtape or EP.

So I had an idea, how about analysing the lyrics of each song on his albums and eventually his discography? Maybe that will tell me what I wanted to know and probably why I liked his new album so much. Looking at this discography, he had a lot of projects so I decided to start simple. 

The idea is to pick an artist with an 'ok' amount of albums and have songs that were diverse enough to run experiments on. I ended up with [Jon Bellion](http://www.jonbellion.com/). I am a huge fan so this is still good for me.

![Jon Bellion's Picture](https://static.billboard.com/files/media/02-jon-bellion-press-2020-cr-Dexter-Findley-billboard-1548-compressed.jpg)

## Questions
How has the lyrical content and context changed over time in an artist's discography? What can this say about the *context maturity** of their discography?

* Context maturity is a term I've coined for the study of the changes of the changes in the lyrics of the albums over time contextually.

This can help us ask and answer a lot of questions. Here are a few that was contributed after discussing this project with fellow a data scientist.

Take Kendrick Lamar, he recently won a Pulitzer Award for his Damn album. Taking a look into the context of the lyrics, how does his previous album compare to DAMN and are they worth a Pulitzer? (This depends on how the old albums compare to DAMN) 

Let’s take Kanye West. If you’re a Kanye fan or even not, there’s a chance you’ve come across the argument about how the old Kanye is better, well in terms of musically and personally, or both. But this project can help us understand how different his albums have been and that can give us an insight that can help explain why people likes his old albums than his new ones.

## What Do I Need?
Jon Bellion has a total of five(5) albums. 

- I will need the lyrics of each song on each album. This will be text files containing the lyrics of the songs.
- The complete data should be folders according to the albums with test files of each song in their respective album folders.
- A website to scrape the lyrics of the songs.
- [Genius](https://genius.com/)

## What To Do?
First, I need the data, this will mean I have to scrape it from Genius using the Genius API. 

Put the data together and clean it.

Exploratory Data Analysis with visualisations.

Sentiment Analysis. (Emotions)

Entity Recognition. 

Use Empath model on it. 

Topic Modelling.

## Data Gathering
When gathering the data for the albums on genius, I first used *Beautiful Soup,* this presented an issue of not being able to scrape every song using URLs of albums and looping through them. Another attempt at researching helped me find a Genius API. This made things easier and once again as a somewhat beginner programmer, I was mad at my silly attempts before this discovery. 

I will be taking you through getting a new client API from Genius. 

First visit [https://genius.com/api-clients/new](https://genius.com/api-clients/new), Enter the name of the app, the icon url of your app if available (this is optional) and then enter the app website url, in this case I used my GitHub link ([https://github.com/QABoahene](https://github.com/QABoahene)) because that's where this project is.

![genius API Picture](https://github.com/QABoahene/My-NLP-Journey/blob/main/Context%20Maturity%20(NLP)/images/New%20API%20Client%20Image.png)

You can read the documentation about the resources needed to carry out tasks you need [here](https://docs.genius.com/). Luckily, there is a package created in python which can help with the first tasks we need to perform for this project which is the data gathering. The package is called *lyricsgenius.*

## Data Cleaning
Fortunately for me, this data looks mostly clean in terms of spelling mistakes and grammar. The source of the  data works on crowd-sourcing in terms of getting the right lyrics for songs. Cleaning the data is pretty simple and follows the usual process to clean the lyrics to be ready for exploratory data analysis but, there's a catch.

The usual processes for cleaning the lyrics were lemmatisation, removing stop words, removing punctuations and numbers. In the code below, I start by getting rid of all the lines of text that has an item in a square bracket. This is usually the name of the artists or the verse numbers or choruses. This is followed by processes like making the texts lowercases, splitting and lemmatising the words, removing punctuations and removing stop words which doesn't end there. In the lyrics, there are numeric values and at the moment, numbers will not contribute greatly to any insights I'm trying to draw so there is a line of code to take that out. After this, there were some words that still had apostrophes and other punctuations so I manually found them and took them out. You can achieve all this by using the re and nltk packages.

Here's the tricky part, although the output of this was great and looking at the data, the texts seemed clean but there were still some words that made it into the output that I deemed unnecessary, in other words, because of the type of literature of this data, there are bound to be some words that carry almost no meaning and will only make our data a bit unclean to work with. In music, you'll often see these words in the lyrics because of the nature of the diction and also how the artist end up harmonising or the nature of their ad-libs. I manually went through to spot some or most of these words and removed them from the corpus. Some of these words found in Jon Bellion's lyrics are: 'yeah', 'bum', 'la', 'da', 'ba', 'oh', 'ohh', 'ooh', 'mama', 'nana', 'yah', 'uh', 'ew', 'dum', 'ho', 'ya', 'nay', 'nan', 'yo', 'nanana', 'uhuh', 'badem', 'buhda', 'dadada', and 'dadum'. ('This makes me dread working on the lyrics from the rap sub-genre; mumble rap.)

Now that these words were removed, the data looks better and ready to be explored.
