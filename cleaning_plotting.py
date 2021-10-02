import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
warnings.simplefilter('ignore')

from sklearn.linear_model import LinearRegression  
from sklearn.preprocessing import PolynomialFeatures 
from sklearn.metrics import mean_squared_error, r2_score

from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer

from sklearn.decomposition import PCA

import pickle

# FIRST WE ARE GOING TO IMPORT OUR TWO DATASETS AND START THE CLEANING (a previous explorations has been made in a Notebook)

sports = pd.read_excel('./Toughest Sport by Skill.xlsx')
money = pd.read_csv('./Forbes Richest Atheletes (Forbes Richest Athletes 1990-2020).csv')

# we have no nulls in sports, so the first cleaning is done in this dataset
# we don't care about that row in money

money.drop('Previous Year Rank', axis = 1, inplace = True)

# the nulls are deleted now, lets gropu the sports, we have 'basketball' and 'Basketball' and similar things, we want them to be the same
# lets map

sports = {
    'Golf': 'Golf',
    'golf': 'Golf',
    'Basketball': 'Basketball',
    'NBA': 'Basketball',
    'basketball': 'Basketball',
    'Auto Racing': 'Auto Racing',
    'auto racing': 'Auto Racing',
    'Auto racing': 'Auto Racing',
    'Soccer': 'Soccer',
    'soccer': 'Soccer',
    'F1 racing': 'Auto Racing',
    'F1 Motorsports': 'Auto Racing',
    'American Football': 'American Football',
    'NFL': 'American Football',
    'Baseball': 'Baseball',
    'baseball': 'Baseball',
    'Hockey': 'Hockey',
    'Ice Hockey': 'Hockey',
    'ice hockey': 'Hockey',
    'Boxing': 'Boxing',
    'boxing': 'Boxing',
    'Tennis': 'Tennis',
    'tennis': 'Tennis',
    'American Football / Baseball': 'Baseball',
    'motorcycle gp': 'Moto GP',
    'cycling': 'Cycling',
    'NASCAR': 'Nascar',
    'Auto Racing (Nascar)': 'Nascar',
    'MMA': 'MMA',
    
}

money.Sport = money.Sport.map(sports)

# now lets rename the earnings column

money['earnings_million'] = money['earnings ($ million)']
money.drop('earnings ($ million)', axis = 1, inplace = True)

# let's export our clean datasets 

sports.to_csv('abilities_sports_clean.csv')
money.to_csv('money_sports_clean.csv')


# SECOND, WE START WITH THE VISUALIZATION

# FIRST: an histogram showing were the sports lie in terms of 'difficulty'

histogram = sns.histplot(data=sports, x=sports.Total).set(title='FREQUENCY OF DISTRIBUTION OF THE "DIFFICULTY" OF THE SPORTS')
plt.savefig('histogram.png')

# SECOND: we want to check allthe sports rated by it total 'difficuty'

figa = go.Figure([go.Bar(x=sports.Sport, y=sports.Total)])
figa.update_layout(
    autosize=False,
    width=1100,
    height=800
)
figa.update_layout(title='SUM OF ALL THE VALUES OF THE CHARACTERISTICS OF EACH SPORT')
plt.savefig('sports_difficulty.png')


# THIRD: I want to see the total  earnings of each sport in the last 30 years

agrupado = money.groupby(['Sport'],as_index=False).agg({'earnings_million' : 'sum'})
figu = go.Figure([go.Bar(x=agrupado.Sport, y=agrupado.earnings_million )])
figu.update_layout(title='TOTAL EARNINGS OF EACH SPORT (IN MILLION USD) IN THE LAST 30 YEARS')
plt.savefig('sum_earnings.png')

# FOURTH: I want to see the change in sport earnings in the last 30 years (the rate of chhange of a singular sport in the last 30 years)

agrupado3 = money.groupby(['Sport', 'Year']).mean()
agrupado3.reset_index(inplace = True)

figi = px.line(agrupado3, x='Year', y='earnings_million', color='Sport')
figi.update_layout(title='CHANGE IN EACH SPORT EARNINGS (IN MILLION USD) IN THE LAST 30 YEARS')
plt.savefig('rate_change_sports')

# FIFTH: check each individaul ability for every sport. PLotting a single ability to see how it is measured in each sport 

# lets create a new dataframe based on the sports dataframe but only containing the sports present in money
# because those are the only profiteable sports in the last 30 years

sports_cropped = sports[(sports.Sport == 'Boxing')|(sports.Sport == 'Auto Racing')|(sports.Sport == 'Golf')|
                       (sports.Sport == 'Basketball')|(sports.Sport == 'Tennis')|(sports.Sport == 'American Football')|
                       (sports.Sport == 'Baseball')|(sports.Sport == 'Hockey')|(sports.Sport == 'Nascar')|
                       (sports.Sport == 'Soccer')|(sports.Sport == 'Cycling')|(sports.Sport == 'Moto GP')|
                       (sports.Sport == 'Ice Hockey')|(sports.Sport == 'Cycling: Distance')|(sports.Sport == 'Rugby')]

sports_cropped.reset_index(inplace=True)
sports_cropped.drop('index', axis = 1, inplace = True)
sports_cropped.drop(columns=['Total', 'Rank'], inplace=True) # this columns doesn't add value
# we end up having 9 . MMA is in Boxing, moto GP and Nascar is in Auto Racing and American Football kind of like Rugby

fige = make_subplots(rows=5, cols=2, subplot_titles=('Endurance', 'Strength', 'Power', 'Speed',
                                                    'Agility', 'Flexibility', 'Nerve', 'Durability', 'Hand-Eye Coordination',
                                                    'Analytical Aptitude'))

fige.add_trace(go.Bar(x=sports_cropped.Sports, y=sports_cropped.Endurance), row=1, col=1)
fige.add_trace(go.Bar(x=sports_cropped.Sports, y=sports_cropped.Strength), row=1, col=2)
fige.add_trace(go.Bar(x=sports_cropped.Sports, y=sports_cropped.Power), row=2, col=1)
fige.add_trace(go.Bar(x=sports_cropped.Sports, y=sports_cropped.Speed), row=2, col=2)
fige.add_trace(go.Bar(x=sports_cropped.Sports, y=sports_cropped.Agility), row=3, col=1)
fige.add_trace(go.Bar(x=sports_cropped.Sports, y=sports_cropped.Flexibility), row=3, col=2)
fige.add_trace(go.Bar(x=sports_cropped.Sports, y=sports_cropped.Nerve), row=4, col=1)
fige.add_trace(go.Bar(x=sports_cropped.Sports, y=sports_cropped.Durability), row=4, col=2)
fige.add_trace(go.Bar(x=sports_cropped.Sports, y=sports_cropped['Hand-Eye Coordination']), row=5, col=1)
fige.add_trace(go.Bar(x=sports_cropped.Sports, y=sports_cropped['Analytical Aptitude']), row=5, col=2)

fige.update_xaxes(tickangle=45)

fige.update_layout(showlegend=False) 

fige.update_layout(height=1600, width=700,
                  title_text = 'EACH ABILITY FOR THE 9 MOST PROFITEABLE SPORTS')
plt.savefig('ability_sport.png')

# SIXTH : Change in abilities (money-wise) in the last 30 years

# That means, check which sports has been the most dominant every single year, then, 
# extract the most dominan ability of that sport and then, plot the variability of the of the abilities throughout the lsat 30 years.

max_usd_year = money[["Year", "earnings_million"]].groupby(by="Year", as_index=False).max()
all_year = pd.merge(max_usd_year, money, on=["Year","earnings_million"], how="left")
year_sport_earnings = all_year.drop(columns=['S.NO', 'Name', 'Nationality', 'Current Rank'], axis = 1) # not usable information

# now I need to map the sports
sports_dict = {
'Boxing': 'Nerve',
'Ice Hockey': 'Durability',
'Basketball': 'Agility',
'Tennis': 'Hand-Eye Coordination',
'Soccer': 'Agility',
'American Football': 'Durability',
'Cycling: Distance': 'Endurance',
'Auto Racing': 'Nerve',
'Golf': 'Analytical Aptitude'
}
year_sport_earnings.Sport = year_sport_earnings.Sport.map(sports_dict)

figx = px.line(year_sport_earnings, x='Year', y='earnings_million', color='Sport')

figx.update_layout(title='CHANGE IN THE EARNINGS OF ABILITIES BASED ON THE MAX EARNINGS PER YEAR')
plt.savefig('ability_years.png')



