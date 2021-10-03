import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression  
from sklearn.preprocessing import PolynomialFeatures 
from sklearn.metrics import mean_squared_error, r2_score


money = pd.read_csv('money_sports_clean.csv', index_col=0)
sports = pd.read_csv('abilities_sports_clean.csv',index_col=0)

def extract_df(df, sport):
    '''
    Transforms a dataframe into a smaller and grouped one
    Args:
        df(pd.DataFrame)
        sport(str): the name of the sport we want to group
    Returns:
        pd.DataFrame: grouped by year and with the average of earnings of that year
    '''
    sport = money[money.Sport == f'{sport}']
    df_grouped = sport.groupby(['Year'], as_index = False).agg({'earnings_million':'mean'})
    
    return df_grouped

def polynomial_plot(df,sport):
    '''
    Draws a degree 3 polynomic regression for a desired dataframe
    Args:
        df(pd.DataFrame):the desire dataframe were we want the polynomic regression to be done
        sport(str): the name of the sport of the individual plynomial regression
    Returns:
        matplotlib.pyplot: plot with the data scatterd and the polynomic regression line up to 2030
    '''
    x = np.array(df.Year)
    y = np.array(df.earnings_million)

    x = x[:,np.newaxis]
    y = y[:,np.newaxis]

    plt.scatter(x, y)

    nb_degree = 3
    polynomial_features = PolynomialFeatures(degree = nb_degree)
    X_TRANSF = polynomial_features.fit_transform(x)

    model = LinearRegression()
    model.fit(X_TRANSF, y)

    Y_NEW = model.predict(X_TRANSF)
    rmse = np.sqrt(mean_squared_error(y,Y_NEW))
    r2 = r2_score(y,Y_NEW)
    print('RMSE: ', rmse)
    print('R2: ', r2)

    x_new_min = 1990
    x_new_max = 2030


    X_NEW = np.linspace(x_new_min, x_new_max, 100)
    X_NEW = X_NEW[:,np.newaxis]


    X_NEW_TRANSF = polynomial_features.fit_transform(X_NEW)
    Y_NEW = model.predict(X_NEW_TRANSF)
    plt.plot(X_NEW, Y_NEW, color='coral', linewidth=3)
    plt.grid()
    plt.xlim(x_new_min,x_new_max)

    plt.title(f'Prediction of the evolution of {sport} in the next 10 years')
    plt.xlabel('Year')
    plt.ylabel('Earnings (Million USD)')

    plt.show()

