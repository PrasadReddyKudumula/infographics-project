import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

elepro = pd.read_excel("electricpro.xlsx")
eletri = pd.read_excel("electrification.xlsx")
elcon = pd.read_excel("cons.xlsx")

def cleansing(data):
    Name = data['Name']
    data = data.set_index(Name)
    data = data.drop("Name",axis = 1)
    return data

elepro = cleansing(elepro)
eletri = cleansing(eletri)
elcon = cleansing(elcon)


def graph1(ax, data):

    ax.plot(data.loc["Brazil", 1995:2020], '#1f77b4', label='Brazil')
    ax.plot(data.loc["Russia", 1995:2020], '#ff7f0e', label='Russia')
    ax.plot(data.loc["India", 1995:2020], '#2ca02c', label='India')
    ax.plot(data.loc["China", 1995:2020], '#9467bd', label='China')
    ax.plot(data.loc["South Africa", 1995:2020], '#d62728', label='S. Africa')

    ax.set_title('Electricity consumption (1995-2020)')
    ax.set_xlabel('Year[1995 - 2020]')
    ax.set_ylabel('Electricity(TWh)')
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.7)

# Creating years list , which we use in dataExctraction function
year = [1990, 1995, 2000, 2005, 2010, 2015, 2020]

# Creating dataExtraction function
def extract(data, col):

    emptyList = []  # empty list

    for j in year:
        line = data.loc[col,j]
        emptyList = np.append(emptyList, line)
    return emptyList

pro = extract(elepro, "G7")
con = extract(elcon,"G7")


def graph2(ax, data1, data2):
    ax.bar([x- 1 for x in years], data1,width = 1, label='production' )
    ax.bar([x for x in years], data2,width = 1,label ='consumption')
    ax.set_ylim(3000,)
    ax.set_xlabel("Years")
    ax.set_ylabel("'Electricity(TWh)'")
    ax.set_title("Production vs Consumption")
    ax.legend()

def graph3(ax, data):
    ax.plot(data.loc["Canada", 1995:2020], '#1f77b4', label='Brazil')
    ax.plot(data.loc["France", 1995:2020], '#ff7f0e', label='Russia')
    ax.plot(data.loc["Germany", 1995:2020], '#2ca02c', label='India')
    ax.plot(data.loc["Italy", 1995:2020], '#9467bd', label='China')
    ax.plot(data.loc["Japan", 1995:2020], '#d62728', label='S. Africa')

    ax.set_title('Electrification (1995-2020)')
    ax.set_xlabel('Year[1995 -2020]')
    ax.set_ylabel('Electricity(TWh)')
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.7)

def graph4(ax,data):
    blocks = ['Europe', 'CIS',
              'North America',
              'Latin America',
              'Asia','Africa',
              'Middle-East']

    empty = []
    for i in blocks:
        # Extract the energy consumption for each block for the year 2020
        loca = data.loc[i, 2020]
        empty = np.append(empty, loca)  # Append the consumption value to the list

    empty = empty.round(2)  # Round the consumption values to two decimal places
    # Create a Pandas Series from the list with the blocks as the index
    data = pd.Series(data=empty, index=blocks)

    # Define a range of blue shades for visual distinction in the pie chart
    shades  = [
    "#6495ED",  # Cornflower Blue
    "#FF69B4",  # Hot Pink
    "#B0C4DE",  # Light Steel Blue
    "#006400",  # Dark Green
    "#FFD700",  # Gold
    "#DC143C",  # Crimson
    "#00CED1"   # Dark Turquoise
                ]

    # Create a pie chart with the data
    ax.pie(data, labels=None, colors=shades,  startangle=90,
         )  # The pie chart is formatted with percentages, a start angle, and wedge properties

    ax.set_title("Electricity Production year [2020]")  # Set the title of the pie chart

    # Place a legend on the side of the plot
    ax.legend(blocks, loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

    # Add text in the middle of the pie chart, displaying total energy consumption
    ax.text(0, 0, '26597.0 TWH', horizontalalignment='center', verticalalignment='center')

def plotting(k = True):
        # Create a single figure with subplots
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))

        # Plot each chart on its corresponding subplot
        graph1(axes[0,0],elepro)
        graph2(axes[0,1],pro,con)
        graph3(axes[1,0],eletri)
        graph4(axes[1,1],elepro)
        # Add "Hello World" text at the bottom of the entire figure
        story = "\nThis dashboard analyzes Energy.\n" \
            "  1.China electricity consumption jumped from 1000 to near 8000.\n " \
            "  2. BRICS producing more electrcity than required  .\n" \
            "  3.  world's year 2020 total energy usage 13356.23 Twh\n" \
            "  4. world's year 2020 total electricity  consumption 26597.23 Twh\n  "
        student_details="Name:prasad \nID:22083068"
        Title="BRICS electrification"
        fig.text(0.01, 0.01, story, ha='left', fontsize=10)
        fig.text(0.95, 0.01, student_details, ha='right', fontsize=10)

        # Add a title at the top-center of the entire figure
        fig.suptitle(Title, fontsize=16, y=0.99,weight='bold')

        # Adjust layout for better spacing
        plt.tight_layout(rect=[0, 0.15, 1, 1]) # Adjust the rect parameter to leave space at the bottom

        # Save the entire figure as a single PNG file with 300dpi resolution
        plt.savefig('22083068.png', dpi=300)
        #Uncomment line 138 if you want to see output while running this code and comment line 136 if you do not want to generate png.
        #plt.show()

plotting()
