import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('/home/gero/Escritorio/Free code camp/Data analytics with python certification/project 5/epa-sea-level.csv')

    # Create scatter plot
    fig = plt.subplot()
    plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    resultado = linregress(df['Year'],df['CSIRO Adjusted Sea Level']) # tanto x e y deben tener el mismo tamanio.   
    x_pred = pd.Series([i for i in range (1880,2051)])  #creamos una serie de los anios. 
    y_pred = resultado.intercept + resultado.slope * x_pred 
    #slope of the regression line. #Intercept of the regression line.
    plt.plot(x_pred,y_pred,'g')

    # Create second line of best fit
    df_new = df.loc[df['Year'] >= 2000] #filtramos el data frame.
    nuevo_resultado = linregress(df_new['Year'],df_new['CSIRO Adjusted Sea Level'])    
    
    x_pred_new = pd.Series([i for i in range (2000,2051)])   
    y_pred_new = nuevo_resultado.intercept + nuevo_resultado.slope * x_pred_new 

    
    plt.plot(x_pred_new,y_pred_new,'r')

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()