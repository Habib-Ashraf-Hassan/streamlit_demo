import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("gapminder_with_codes.csv")
data_2007 = data[data['year'] == 2007]
# Create the figure and axes objects for the subplots
fig, ax = plt.subplots(1, 3, figsize=(15, 5))

# Plot the violin plot for population
sns.violinplot(y="pop", data=data_2007, ax=ax[0])
ax[0].set_title("Population Distribution")

# Plot the violin plot for life expectancy
sns.violinplot(y="lifeExp", data=data_2007, ax=ax[1])
ax[1].set_title("Life Expectancy Distribution")

# Plot the violin plot for GDP per capita
sns.violinplot(y="gdpPercap", data=data_2007, ax=ax[2])
ax[2].set_title("GDP per capita")

# Show the plot
plt.show()

# Two other separate violin plots of lifeExp Vs gdpPercap and pop Vs gdpPercap
# Calculate the average of gdpPercap in the year 2007
gdp_mean = data_2007["gdpPercap"].mean()

# Create a new list called "classes_gdp" tp store the high and low values
classes_gdp = ["high" if x > gdp_mean else "low" for x in data_2007["gdpPercap"]]

# Create the figure and axes objects for the subplots
fig2, axes = plt.subplots(1, 2, figsize=(10, 5))

# Plot the violin plot for life expectancy and Classes_gdp
sns.violinplot(x=classes_gdp, y=data_2007["lifeExp"], ax=axes[0], color="blue")
axes[0].set_title("Life Expectancy Distribution by the gdp")
axes[0].set_xlabel("Classes of GDP per cap(High and Low)")
axes[0].set_ylabel("Life expectancy")

# Plot the violin plot for population and Classes_gdp
sns.violinplot(x=classes_gdp, y=data_2007["pop"], ax=axes[1], color="red")
axes[1].set_title("Population Distribution by the gdp")
axes[1].set_xlabel("Classes of GDP per cap(High and Low)")
axes[1].set_ylabel("Population")
plt.show()
