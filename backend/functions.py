import pandas as pd
import numpy as np

def get_data():
    df = pd.ExcelFile('data/kwsp_schedule.xlsx')
    return df

def get_schedule(nationality, df):
    if nationality == "Malaysian":
        epf_citizen = df.parse('citizen')
        return epf_citizen
    else:
        epf_foreign = df.parse('foreigner')
        return epf_foreign
    
def match_contribution(df, salary):
    temp = map(lambda x: x <= salary, df['upper'])
    idx = list(temp).index(False)
    contribution = df['total'][idx]
    return contribution

def goal_seek(goal, contribution, compound_rate):
    r = 1 + compound_rate/100
    years = 1/np.log(r)*np.log((goal*(r-1))/(12*contribution*r) + 1)
    return years

def year_total(years, contribution, compound_rate):
    r = 1 + compound_rate/100
    total = 0
    total_by_year = []
    for i in range(1,int(years)+2):
        temp = contribution*12*(r**i)
        total = temp + total
        total_by_year.append(total)
    
    total_by_year = pd.DataFrame(total_by_year, columns=['total'])
    
    return total_by_year
    