import pandas
import plotly.express as plot_creation

df = pandas.read_csv("Statistics103/ProjectPlot/Coviddata.csv")
CovidPlot = plot_creation.scatter(df,x="date",y = "cases", color= 'country',size_max=100)
CovidPlot.show()