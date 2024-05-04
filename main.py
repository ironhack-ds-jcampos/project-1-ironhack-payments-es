import pandas as pd
import plotly.express as px

# Read the Excel file into a DataFrame
df = pd.read_csv("project_dataset/extract - cash request - data analyst.csv")
df['created_at'] = pd.to_datetime(df['created_at'])
df['day'] = df['created_at'].dt.day
df = df.groupby('day').size().reset_index(name="count")

# Now you can use Plotly to create visualizations
fig = px.bar(df, x='day', y='count', title='Your Plot Title')
fig.show()