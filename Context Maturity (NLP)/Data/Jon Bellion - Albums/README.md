# Data Gathering

When gathering the data for the albums on genius, I first used *Beautiful Soup,* this presented an issue of not being able to scrape every song using URLs of albums and looping through them. Another attempt at researching helped me find a Genius API. This made things easier and once again as a somewhat beginner programmer, I was mad at my silly attempts before this discovery. 

I will be taking you through getting a new client API from Genius. 

First visit [https://genius.com/api-clients/new](https://genius.com/api-clients/new), Enter the name of the app, the icon url of your app if available (this is optional) and then enter the app website url, in this case I used my GitHub link ([https://github.com/QABoahene](https://github.com/QABoahene)) because that's where this project is.

![New API Client Image](https://github.com/QABoahene/My-NLP-Journey/blob/main/Context%20Maturity%20(NLP)/images/New%20API%20Client%20Image.png)

You can read the documentation about the resources needed to carry out tasks you need here. Luckily, there is a package created in python which can help with the first tasks we need to perform for this project which is the data gathering. The package is called lyricsgenius. 
