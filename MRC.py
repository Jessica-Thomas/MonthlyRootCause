import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame, Series


# Import csv
df = pd.read_csv('ProjectData.csv')

def Monthly_SLA(df):
    
    def charge1(self):
        sns.boxplot( x=df.filter(regex='Integrity S1'), y=df["Days Open"], palette="Blues");
        plt.show()