
#EXPLORATORY DATA ANALYSIS ON NETFLIX



import numpy as np 
import pandas as pd 
import seaborn as sns
from matplotlib import pyplot as plt


netflix = pd.read_csv("../input/netflix-shows/netflix_titles.csv")

# %%
netflix.info()

# %%
netflix.describe()

# %%
netflix.isnull().sum()

# %%
netflix.director.fillna(value="unknown", inplace = True)
netflix.director

# %%
netflix.cast.fillna(value = "unknown", inplace = True)
netflix.cast

# %%
netflix.country.fillna(value="unknown", inplace =True)
netflix.country

# %%
netflix.date_added.fillna(value = "unknown", inplace = True)
netflix.date_added

# %%
netflix.isnull().sum()

# %%
netflix.dropna(inplace = True)

# %%
netflix.isnull().sum()

# %%
netflix.type.value_counts().index

# %%
netflix.type.unique

# %%
netflix.type.value_counts()

# %%
#visualizing the type
plt.figure(figsize=(10,8))

plt.pie(netflix.type.value_counts(), 
        labels = netflix.type.value_counts().index, 
        labeldistance = None, autopct="%.2f", 
        textprops = {'fontsize': 16,}, 
        colors = ['lightsteelblue','lightsalmon' ] )
plt.legend()
plt.show()

# %% [markdown]
# Result: The number of movie content on netflix in 2.33 times the TV Shows.

# %%
last_decade = netflix[["type", "release_year"]]
last_decade = last_decade.rename(columns = {"release_year" : "Release Year"})
last_decade = last_decade[last_decade["Release Year"]>=2010]
last_decade

# %%
last_decade_df = last_decade.groupby("Release Year")["type"].size().reset_index()
last_decade_df = pd.DataFrame(last_decade_df)
last_decade_df

# %%
last_decade_df.rename(columns = {"type": "Total Content"}, inplace = True)

# %%
last_decade.groupby("Release Year")["type"].value_counts()

# %%
plt.figure(figsize = (10,6))
count_plot = sns.countplot(x = "Release Year", data = last_decade, hue="type",
             palette= "pastel")
count_plot.set(title = "Trend of each type of content Released over the years")
;

# %%
plt.figure(figsize = (10,6))
plot_total_content= sns.lineplot(x= "Release Year", y = "Total Content", data = last_decade_df, 
                                linewidth = 3)
plot_total_content.set(xlabel = "Release Year", ylabel = "Total Content", 
                      title = "Trend of content on netflix")
plt.show()

# %% [markdown]
# Result: It is seen that most content on netflix was released in year 2018, the amount of content is decreasing since then.

# %%
top_10_countries= netflix.country.value_counts().head(10)
top_10_countries = pd.DataFrame(top_10_countries)
top_10_countries

# %%
plt.figure(figsize = (10,8))
country_plot = sns.barplot(x = netflix.country.value_counts()[:10].values, 
                           y= netflix.country.value_counts()[:10].index,palette = "pastel")
for i in country_plot.containers:
    country_plot.bar_label(i);  

# %% [markdown]
# Result: About 32% of content on Netflix is produced in the USA.

# %%
netflix.rating.unique()

# %%
new_catgs = {
    'TV-PG': 'Parental Guidance',
    'TV-MA' : 'Mature Audience',
    'TV-Y7-FV': 'Teens',
    'TV-Y7': 'Teens',
    'TV-14': 'Teens',
    'R': 'Mature Audience',
    'TV-Y': 'General Audience',
    'NR': 'Mature Audience',
    'PG-13': 'Teens',
    'TV-G': 'General Audience',
    'PG': 'Teens',
    'G': 'General Audience',
    'UR': 'Mature Audience',
    'NC-17': 'Mature Audience'
}
netflix['rating']=netflix['rating'].replace(new_catgs)
netflix.head()

# %%
plt.figure(figsize= (10,6))
sns.countplot(x="rating", data=netflix, palette="pastel",)
plt.title("count of Rating by Movie and Shows");

# %% [markdown]
# Result: It is seen that Netflix has more content for Mature audience.


