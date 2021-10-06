import streamlit as st
import pandas as pd
import plotly_express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def load_money():
    df = pd.read_csv('money_sports_clean.csv', index_col=0)
    return df

def load_sports():
    df = pd.read_csv('abilities_sports_clean.csv',index_col=0)
    return df

def all_sports():
    df = load_sports()
    figa = go.Figure([go.Bar(x=df.Sport, y=df.Total)])
    figa.update_layout(
    autosize=False,
    width=1100,
    height=800
    )
    figa.update_layout(title='SUM OF ALL THE VALUES OF THE CHARACTERISTICS OF EACH SPORT')
    return figa

def sum_earnings():
    df = load_money()
    agrupado = df.groupby(['Sport'],as_index=False).agg({'earnings_million' : 'sum'})
    figu = go.Figure([go.Bar(x=agrupado.Sport, y=agrupado.earnings_million )])
    figu.update_layout(title='TOTAL EARNINGS OF EACH SPORT (IN MILLION USD) IN THE LAST 30 YEARS')
    figu.update_layout(yaxis_title="Earnings in Million USD")

    return figu

def change_sports():
    df = load_money()
    agrupado3 = df.groupby(['Sport', 'Year']).mean()
    agrupado3.reset_index(inplace = True)
    figi = px.line(agrupado3, x='Year', y='earnings_million', color='Sport')
    figi.update_layout(title='CHANGE IN EACH SPORT EARNINGS (IN MILLION USD) IN THE LAST 30 YEARS')

    return figi

def abilities_xsports():
    deportes = ['Boxing', 'Ice Hockey', 'Basketball', 'Tennis', 'Soccer', 'American Football', 'Cycling: Distance', 'Auto Racing', 'Golf']
    sports = load_sports()
    sports_cropped = sports[(sports.Sport == 'Boxing')|(sports.Sport == 'Auto Racing')|(sports.Sport == 'Golf')|
                       (sports.Sport == 'Basketball')|(sports.Sport == 'Tennis')|(sports.Sport == 'American Football')|
                       (sports.Sport == 'Baseball')|(sports.Sport == 'Hockey')|(sports.Sport == 'Nascar')|
                       (sports.Sport == 'Soccer')|(sports.Sport == 'Cycling')|(sports.Sport == 'Moto GP')|
                       (sports.Sport == 'Ice Hockey')|(sports.Sport == 'Cycling: Distance')|(sports.Sport == 'Rugby')]
    sports_cropped.reset_index(inplace=True)
    sports_cropped.drop('index', axis = 1, inplace = True)
    sports_cropped.drop(columns=['Total', 'Rank'], inplace=True)
    sports_cropped.drop('Sport', axis = 1, inplace = True)

    sports_cropped['Sports'] = deportes
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
    return fige

def sports_xabilities():
    sports = load_sports()
    deportes = ['Boxing', 'Ice Hockey', 'Basketball', 'Tennis', 'Soccer', 'American Football', 'Cycling: Distance', 'Auto Racing', 'Golf']
    sports_cropped = sports[(sports.Sport == 'Boxing')|(sports.Sport == 'Auto Racing')|(sports.Sport == 'Golf')|
                       (sports.Sport == 'Basketball')|(sports.Sport == 'Tennis')|(sports.Sport == 'American Football')|
                       (sports.Sport == 'Baseball')|(sports.Sport == 'Hockey')|(sports.Sport == 'Nascar')|
                       (sports.Sport == 'Soccer')|(sports.Sport == 'Cycling')|(sports.Sport == 'Moto GP')|
                       (sports.Sport == 'Ice Hockey')|(sports.Sport == 'Cycling: Distance')|(sports.Sport == 'Rugby')]
    sports_cropped.reset_index(inplace=True)
    sports_cropped.drop('index', axis = 1, inplace = True)
    sports_cropped.drop(columns=['Total', 'Rank'], inplace=True)
    sports_cropped.drop('Sport', axis = 1, inplace = True)
    sports_cropped['Sports'] = deportes
    transpose = sports_cropped.T.reset_index()
    transpose = sports_cropped.drop('Sports', axis =1).T.reset_index()
    figs = make_subplots(rows=5, cols=2, subplot_titles=('Boxing', 'Ice Hockey', 'Basketball', 'Tennis',
                                                    'Soccer', 'American Football', 'Cycling: distance', 'Auto Racing', 'Golf'
                                                    ))

    figs.add_trace(go.Bar(x=transpose['index'], y=transpose[0]), row=1, col=1)
    figs.add_trace(go.Bar(x=transpose['index'], y=transpose[1]), row=1, col=2)
    figs.add_trace(go.Bar(x=transpose['index'], y=transpose[2]), row=2, col=1)
    figs.add_trace(go.Bar(x=transpose['index'], y=transpose[3]), row=2, col=2)
    figs.add_trace(go.Bar(x=transpose['index'], y=transpose[4]), row=3, col=1)
    figs.add_trace(go.Bar(x=transpose['index'], y=transpose[5]), row=3, col=2)
    figs.add_trace(go.Bar(x=transpose['index'], y=transpose[6]), row=4, col=1)
    figs.add_trace(go.Bar(x=transpose['index'], y=transpose[7]), row=4, col=2)
    figs.add_trace(go.Bar(x=transpose['index'], y=transpose[8]), row=5, col=1)

    figs.update_xaxes(tickangle=45)

    figs.update_layout(showlegend=False) 

    figs.update_layout(height=1600, width=700,
                    title_text = 'THE 9 MOST PROFITEABLE SPORTS')
    return figs

def user_input():
    endurance = st.sidebar.slider('Endurance ', 0.0, 10.0, 5.0)
    strength = st.sidebar.slider('Strength', 0.0, 10.0, 5.0)
    power = st.sidebar.slider('Power', 0.0, 10.0, 5.0)
    speed = st.sidebar.slider('Speed', 0.0, 10.0, 5.0)
    agility = st.sidebar.slider('Agility', 0.0, 10.0, 5.0)
    fleixibility = st.sidebar.slider('Flexibility', 0.0, 10.0, 5.0)
    nerve = st.sidebar.slider('Nerve', 0.0, 10.0, 5.0)
    durability = st.sidebar.slider('Durability', 0.0, 10.0, 5.0)
    hand_eye_coord = st.sidebar.slider('Hand-Eye Coordination', 0.0, 10.0, 5.0)
    analytical_aptitude = st.sidebar.slider('Analytical Aptitude', 0.0, 10.0, 5.0)

    data = {
        "Endurance": endurance,
        "Strength": strength,
        "Power": power,
        "Speed": speed,
        "Agility": agility,
        "Flexibility": fleixibility,
        "Nerve": nerve,
        "Durability": durability,
        "Hand-Eye Coordination": hand_eye_coord,
        "Analytical Aptitude": analytical_aptitude
        
    }
    
    return pd.DataFrame(data, index=[0])
