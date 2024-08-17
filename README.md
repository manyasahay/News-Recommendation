## News-Recommendation
This is a basic news recommendation app. The data has been collected from google news via web scraping using Selenium. KMeans clustering was used to assign genre to each article.
The app runs on streamlit for a clean look, it starts by displaying 5 random articles each with a like button. Each time user likes the article, the genre of that article gets appended to a list which is then used for displaying the next news article (i.e. the genre with the majority likes). Liking an article is mandatory to keep viewing lol :P
