# History of sports... Which one is for me?

![portada](https://github.com/Jorge-Solana/What-is-the-best-sport-for-you-ROI-of-abilities-in-each-sport/blob/main/images/deportes.jpg)

## Scope

This project was born with the desire of exploration the history of the sports in the last 30 years.

Another idea was also born alongside the main one which was, given an input data of a user, recomend a sport which may suit his/hers abilities the best.

## Steps for achieving my two main ideas

- Downloaded two datasets from [Kaggle](https://www.kaggle.com/datasets), one containnig the earnings of each sport and the other containing the rating of each ability (there are 10 abilities evaluated in total).

- After that, it was done all the cleaning necessary to have an impecable two datasets.

- All the diving and exploration of the data was made afeter that as well as the first grpahs to understand the data up to the milimiter.

- After understanding the data, the graphs began to blossom as flower in the srping.

- Having done all my graphs it was time for some prediction models.
    
    - For the prediction of the earnigns in the next 10 years in the to sports, I used a polynomic regression.


- For my second idea, I developed an approximation approach based on the input of the ratings of the abilities. I compared all the abilities of each sport with the input and then the difference between them was multiplied by a vector. This vector is an array of numbers based on the difficulty of getting better at a certain ability.

- After all this was done, the develop of my super awesome Streamlit web page took place.


## Results

Talking about results in this project in kind of weird since this is mainly an investigation project.

What we can say though, is that the tendency for the next 10 years in sports is mainly a growing tendency (only few exceptions like golf and some others). 

Another curious thing worth to mention is the rate of increase some sports have made in the last years. See boxing for example the huge increase in the last 5 years due to the ammount of money a single fight can make.

## Project flow

For the best understand of this project you should follow the following path:

- cleaning_plotting.py : for all the code made for the cleaning od the datasets and the code made for all the graphs

- modelling.py : for all the code made for the polynomic regession and clustering

- All graphics+Story.ipynb : here you can find all the graphics with all the storytelling pretty detailed. It is a super clean notebook!

- src : in here exist 2 .py files, model_functions.py which contains the functions used in the main code and support.py, containing the functions used for the streamlit construction.

- multipage.py : here lies the code for the construction for the different pages in streamlit.

- streamlit.py is the main streamlit page

- streamlit_pages contains 3 files, graphs.py which has the streamlit code for the graphs' page, home.py contins the code for the home page and your_sport.py contains the code for the sport prediction page. 


## Libraries used

- [numpy](https://numpy.org/)

- [pandas](https://pandas.pydata.org/)

- [pickle](https://docs.python.org/3/library/pickle.html)

- [plotly](https://plotly.com/)

- [plotly_express](https://plotly.com/python/plotly-express/)

- [scikit-learn](https://scikit-learn.org/stable/)

- [streamlit](https://streamlit.io/)








