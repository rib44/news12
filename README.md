# News12

#### Video Demo: https://youtu.be/SbSVaqiAWKc

#### Description:

My project is a news aggregator which fetches the news through an api known as 'newsapi' and displays it after formatting using HTML and CSS, which has been implemented using bootstrap.

API:

[Newsapi](https://newsapi.org) is used in the implementation of this project. Using the API we can get the news around the world from all major publications at a near instant publishing time. 

It provides the data in JSON format in which top headlines has been accessed from BBC. The data it provides in JSON are as follows:

* source - It has two parts 'id' and 'name' of the publisher of the article.
* author - It represents the person covering the story or article.
* title - Title of the story.
* description - A brief overview of the story.
* url - It redirects to the original story posted on the publisher's website for further reading.
* urtToImage - It redirects to the link of the photo associated with the story.
* publishedAt - Timestamp of publishing of the story.
* content - Contains more descriptive information about the story.

### Initialization

**Step 1:** Create a profile on https://newsapi.org/ and note down your API_KEY.

**Step 2:** We first import the requirements mentioned in the file 'requirements.txt'.

**Step 3:** Setup 'TEMPLATES_AUTO_RELOAD' as True

> It helps us in debugging of the program as after every edit the templates of the file also gets updated and we do not need to again re-run our server.

**Step 4:** Here, we would initialize the newsapi native client for python which we have installed in Step 2, using the API_KEY obtained in Step 1.

### Processing

After making a proper call to the API, it returns a string of JSON text with the top ten news headlines along with the other details and links mentioned above. Here we need to process the data and extract the useful information from it to make it available to the user for easy consumption.

**Step 1:** First choose the news provider and input their code in a variable for which the news has to be fetched. In our case we have chose BBC news.

**Step 2:** Initialize the command statement for fetching the newsapi and the top headlines along with other details.

**Step 3:** After observing the JSON through a reader, it has an extra parent on top of it, so we need to remove it and only keep the articles portion of it in a new variable.

**Step 4:** To store the data from the JSON we have initialized several list data holders to store individual data, which are as follows:

* news - stores the title
* desc - description is stored in it
* img - link to the image is available here.
* p_date - refers to the timestamp of publishing of the article
* url - redirect link to the original article is available here.

**Step 5:** Then we would append each news element to their respective categories.

**Step 6:** Since we need to pass it to the HTML document, we need to zip the data into a simple variable. That's where 'zip' keyword works, to combine all the data into once.

**Step  7:** Finally that data is passed to the HTML file, which renders it and displays it properly in our browser.



Using Jinja templating, HTML processes this data and then represents it in the browser.

The formatting has been done mainly using Bootstrap with some custom CSS.





Thank You

Hope you will like it.