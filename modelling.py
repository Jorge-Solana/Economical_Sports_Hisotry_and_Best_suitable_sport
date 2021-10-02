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

import src.poly_functions as poly

money = pd.read_csv('money_sports_clean.csv', index_col=0)
sports = pd.read_csv('abilities_sports_clean.csv',index_col=0)


# Polynomial regession for each sport

boxing = poly.extract_df(money, "Boxing")
auto_racing = poly.extract_df(money, "Auto Racing")
golfing = poly.extract_df(money, "Golf")
basketball = poly.extract_df(money, "Basketball")
tennis = poly.extract_df(money, "Tennis")
football = poly.extract_df(money, "American Football")
baseball = poly.extract_df(money, "Baseball")
hockey = poly.extract_df(money, "Hockey")
soccer = poly.extract_df(money, "Soccer")
cycling = poly.extract_df(money, "Cycling")
moto = poly.extract_df(money, "Moto GP")


df_sport = [boxing, auto_racing, golfing, basketball, tennis, football, baseball, hockey, soccer, cycling, moto]

for i in df_sport:
    poly.polynomial_plot(i)

# K-Means (Clustering)

# we want to cluster our sports based on the cualification of each ability

sports_kmeans = sports.drop(columns=['Total', 'Rank'], axis = 1) # no useful data

sports_kmeans_d = pd.get_dummies(sports_kmeans, columns = ["Sport"]) # because sport is categorical, we want it as a number

sports_kmeans_s = sports_kmeans.drop(["Sport"], axis = 1) # we drop the sports colun because being categorical (just in case)
model = KMeans()
visualizer = KElbowVisualizer(
    model, k=(3,12), metric='silhouette')
visualizer.fit(sports_kmeans_s)
visualizer.show()

# optimal K (clusters) = 4

model = KMeans(n_clusters = 4)
model.fit(sports_kmeans_s)
y_pred = model.predict(sports_kmeans_s)

df_kmeans = pd.DataFrame(sports_kmeans_s, columns = sports_kmeans_s.columns)
df_kmeans["cluster_pred"] = y_pred

# we just created a dataframe with the cluster predictions. We have sports as well, so cluster and sports are related

# now, for understanding the clusters...

df_kmeans['Sport'] = sports.Sport
df_kmeans_1 = df_kmeans.groupby('cluster_pred').mean()

# here we have done a dataframe with only 4 clusters and the mean of each ability

# lets save this dataframe
df_kmeans_1.to_csv('clusters_mean.csv')

# PCA (Principal Component Analysis)

# here we want to plot the results of our clusters, for some visual comprehension

pca = PCA(n_components=2)
principalComponents = pca.fit_transform(df_kmeans.drop(["Sport"], axis = 1))
principalDf = pd.DataFrame(data = principalComponents, columns = ['principal component 1', 'principal component 2'])

pca_plot = sns.scatterplot(principalDf["principal component 1"],principalDf["principal component 2"],
                           hue= df_kmeans["cluster_pred"], palette='Spectral')
plt.savefig('pca.png')

# SAVING THE MODEL

pickle.dump(model, open("model_k-means", 'wb'))

# SOME CLUSTERS PLOTS
# to have some viasulization of the abilities in each cluster 
# the mean is chosen to be the method for getting an idea of the abilities of each cluster

df_kmeans_1.reset_index(inplace=True)
t_km = df_kmeans_1.iloc[:4].T.reset_index().iloc[1:]

figc = make_subplots(rows=2, cols=2, subplot_titles=('Cluster 0', 'Cluster 1', 'Cluster 2', 'Cluster 3'))

figc.add_trace(go.Bar(x=t_km['index'],
                      y=t_km[0]), row=1, col=1)
figc.add_trace(go.Bar(x=t_km['index'],
                      y=t_km[1]), row=1, col=2)
figc.add_trace(go.Bar(x=t_km['index'],
                      y=t_km[2]), row=2, col=1)
figc.add_trace(go.Bar(x=t_km['index'],
                      y=t_km[3]), row=2, col=2)

figc.update_xaxes(tickangle=45)

figc.update_layout(showlegend=False) 

figc.update_layout(height=800, width=700,
                  title_text = 'EACH ABILITY FOR THE DIFFERENT CLUSTERS')
plt.savefig('ability_cluster.png')

# the following is the sports present in each cluster

cluster0 = ['Boxing', 'Ice Hockey', 'Football', 'Basketball', 'Wrestling',
       'Martial Arts', 'Tennis', 'Baseball/Softball', 'Soccer',
       'Skiing: Alpine', 'Water Polo', 'Rugby', 'Lacrosse',
       'Field Hockey', 'Volleyball', 'Racquetball/Squash', 'Fencing',
       'Team Handball', 'Badminton']

clutser1 = ['Table Tennis', 'Golf', 'Equestrian', 'Archery', 'Curling',
       'Bowling', 'Shooting', 'Billiards', 'Fishing']

cluster2 = ['Speed Skating', 'Figure Skating', 'Cycling: Distance',
       'Cycling: Sprints', 'Skiing: Nordic', 'Track and Field: High Jump',
       'Track and Field: Long, Triple jumps',
       'Swimming (all strokes): Distance', 'Track and Field: Sprints',
       'Rowing', 'Track and Field: Distance',
       'Track and Field: Middle Distance', 'Weight-Lifting',
       'Swimming (all strokes): Sprints', 'Track and Field: Weights',
       'Canoe/Kayak', 'Roller Skating']

cluster3 = ['Gymnastics', 'Rodeo: Steer Wrestling',
       'Track and Field: Pole Vault', 'Surfing', 'Skiing: Freestyle',
       'Bobsledding/Luge', 'Ski Jumping', 'Auto Racing', 'Diving',
       'Skateboarding', 'Rodeo: Calf Roping',
       'Rodeo: Bull/Bareback/Bronc Riding', 'Water Skiing',
       'Horse Racing', 'Cheerleading']

