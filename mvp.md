# MVP
The MVP for this project is a Streamlit app displaying the top 5 fastballs, curveballs, and sliders based on RPM from MLB games on September 1, 2021.

https://share.streamlit.io/ddoberne/metis_project_7/main/display.py

Statcast data was scraped from https://baseballsavant.mlb.com for all pitches on this date. The Streamlit app displays the top five pitches based on pitch type, ordered by RPM, that resulted in a swinging strike. In the future, I would like to include other types of pitches, as well as to have a better metric for what makes a pitch "filthy", as splitters and knuckleballs benefit from decreased spin rate. Time allowing, I will scrape data from all pitches in the 2021 season to train a random forest or XGBoost model that can be deployed to yield the results displayed on the webapp.

Originally I had planned to display pitches from opening day 2021, but there appear to be videos missing from earlier in the season. There are some other issues with the video display, such as the fact that some of the clips appear to have the wrong date on the MLB site, and the difficulty of finding the URL to embed directly in the webapp.

While the MVP shows just one day's worth of pitches, the goal is to update the database daily with the previous day's games. MLB's opening day is April 7 this year, one day before this project is due, so if all goes well I will be able to update with the top pitches from opening day for my presentation.
