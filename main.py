import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Reading data from the file
data = pd.read_csv('kelber_lab.csv')

# Getting planet Name
plan_Name = data["pl_name"]

# Orbital Period (make it unit in days)
# may need to change format to unit in days don't know yet
# use log
plan_Orbital_period = data["pl_orbper"]
plan_Orbital_period = np.log(plan_Orbital_period)
plan_Orbital_period = plan_Orbital_period.dropna()

# Exoplanet Radius
plan_radius = data["pl_rade"]
plan_radius = plan_radius.dropna()
plan_radius = np.log(plan_radius)

# Create X & Y format
df = pd.DataFrame({'Orbital Period': plan_Orbital_period, 'Exoplanet Radius': plan_radius, 'Name': plan_Name})

# Drop missing values
df = df.dropna()

# Select 8 solar Planets
selected_planets = ['Earth', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# Plot the graph
plt.figure(figsize=(10, 6))
plt.scatter(df['Orbital Period'], df['Exoplanet Radius'], color='Red', label='Exoplanets')

for planet in selected_planets:
    selected_index = df[df['Name'] == planet].index
    plt.scatter(df.loc[selected_index, 'Orbital Period'], df.loc[selected_index, 'Exoplanet Radius'],
                label=planet, s=100)  # Increase size to make it brighter

plt.xlabel('Orbital Period (log days)')
plt.ylabel('Radius (log Earth radii)')
plt.title('Exoplanet Radius vs. Orbital Period')
plt.legend()
plt.grid(True)
plt.show()

# Plot Number 2
plan_Mass = data["pl_bmassj"]
plan_Mass = plan_Mass.dropna()
plan_Mass = np.log(plan_Mass)

# OE is comparing orbital period and exoplanet Mass
# dropping NAN values
OE = pd.DataFrame({'Orbital Period': plan_Orbital_period, 'Exoplanet Mass': plan_Mass, 'Name': plan_Name})
OE.dropna()

# Plot the OE Graph
plt.figure(figsize=(10, 6))
plt.scatter(OE['Orbital Period'], OE['Exoplanet Mass'], color='Red', label='Exoplanets')

for planet in selected_planets:
    selected_index = OE[OE['Name'] == planet].index
    plt.scatter(OE.loc[selected_index, 'Orbital Period'], OE.loc[selected_index, 'Exoplanet Mass'],
                label=planet, s=100)  # Increase size to make it brighter

plt.xlabel('Orbital Period (log days)')
plt.ylabel('Exoplanet Mass (log Jupiter Mass)')
plt.title('Exoplanet Mass vs. Orbital Period')
plt.legend()
plt.grid(True)
plt.show()

# Plot Number 3
# ER is comparing exoplanet mass and exoplanet radius
ER = pd.DataFrame({'Exoplanet Mass': plan_Mass, 'Exoplanet Radius': plan_radius, 'Name': plan_Name})
ER.dropna()

# Plot the ER graph
plt.figure(figsize=(10, 6))
plt.scatter(ER['Exoplanet Mass'], ER['Exoplanet Radius'], color='Red', label='Exoplanets')

for planet in selected_planets:
    selected_index = ER[ER['Name'] == planet].index
    plt.scatter(ER.loc[selected_index, 'Exoplanet Mass'], ER.loc[selected_index, 'Exoplanet Radius'],
                label=planet, s=100)  # Increase size to make it brighter

plt.xlabel('Exoplanet Mass (log Jupiter Mass)')
plt.ylabel('Exoplanet Radius (log Earth radii)')
plt.title('Exoplanet Radius vs. Exoplanet Mass')
plt.legend()
plt.grid(True)
plt.show()
