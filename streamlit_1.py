import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt


@st.cache_data
def load_data(file_name):
    df = pd.read_csv(file_name)
    return df


data = load_data("gapminder_with_codes.csv")
data_2007 = data[data['year'] == 2007]

st.subheader("Separate Violin Plots for GDP per Capita, Life Expectancy, and Population")

sns.set_style("darkgrid")

fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(20, 6))

sns.violinplot(y="gdpPercap", data=data_2007, ax=axes[0])
axes[0].set_title("GDP per Capita")

sns.violinplot(y="lifeExp", data=data_2007, ax=axes[1])
axes[1].set_title("Life Expectancy")

sns.violinplot(y="pop", data=data_2007, ax=axes[2])
axes[2].set_title("Population")

# Calculate the average of gdpPercap
mean_gdp = data_2007["gdpPercap"].mean()

# Create the Classes_gdp column
data_2007["Classes_gdp"] = data_2007["gdpPercap"].apply(lambda x: "High" if x > mean_gdp else "Low")

# st.subheader("Violin Plots for Life Expectancy and Population vs Classes_gdp")

sns.set_style("whitegrid")

fig2, axs = plt.subplots(nrows=1, ncols=2, figsize=(20, 6))

sns.violinplot(x="Classes_gdp", y="lifeExp", data=data_2007, ax=axs[0], color="#F5B041")
axs[0].set_title("Life Expectancy vs Classes_gdp")

sns.violinplot(x="Classes_gdp", y="pop", data=data_2007, ax=axs[1], color="#00A6D6")
axs[1].set_title("Population vs Classes_gdp")

st.pyplot(fig)


st.write(""""
 ## Two violin graphs: One is lifeExp Vs Classes of gdpPercap, the other is: pop Vs Classes of gdpPercap
 -Classes of gdp are : High and Low, High if the gdp > the average gdpPercap, and low if otherwise""")

st.pyplot(fig2)
