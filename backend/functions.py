"""
Author: keanteng
License: GNU GPLv3
"""

import pandas as pd
import numpy as np
import math

def get_data():
    """Load data from excel file.

    Returns:
        df : pandas dataframe.
    """
    df = pd.ExcelFile('data/kwsp_schedule.xlsx')
    return df

def get_schedule(nationality, df):
    """Specify the excel sheet to be used.

    Args:
        nationality (string): Malaysian or Non-Malaysian.
        df (Dataframe): Dataframe from get_data().

    Returns:
        Dataframe: Data frame of the contribution schedule.
    """
    if nationality == "Malaysian":
        epf_citizen = df.parse('citizen')
        return epf_citizen
    else:
        epf_foreign = df.parse('foreigner')
        return epf_foreign
    
def contribution_lookup(df, salary):
    """Find the contribution rate based on salary.

    Args:
        df (Dataframe): Dataframe from get_schedule().
        salary (Numeric): Salary.

    Returns:
        idx : Index of the contribution rate.
    """
    try:
        temp = map(lambda x: x <= salary, df['upper'])
        idx = list(temp).index(False)
    except:
        idx = 0
    return idx

def match_contribution(df, idx):
    """Find the contribution rate based on salary.

    Args:
        df (dataframe): Dataframe from get_schedule().
        idx (numeric): Index of the contribution rate.

    Returns:
        contribution : Contribution rate.
    """
    contribution = df['total'][idx]
    return contribution

def bonus_contribution_lookup(df, bonus):
    try:
        temp = map(lambda x: x <= bonus, df['upper'])
        idx = list(temp).index(False)
    except:
        idx = 0
    return idx

def match_bonus_contribution(df, idx):
    bonus_contribution = df['total'][idx]
    return bonus_contribution

def goal_seek(goal, contribution, bonus_contribution, compound_rate):
    """Find the number of years to achieve the saving goal.

    Args:
        goal (numeric): Saving goal.
        contribution (numeric): Contribution rate per month.
        compound_rate (numeric): Expected compound rate.

    Returns:
         years: Number of years to achieve the saving goal.
    """
    r = 1 + compound_rate/100
    contribution = contribution + bonus_contribution/12
    years = 1/np.log(r)*np.log((goal*(r-1))/(12*contribution*r) + 1)
    return years

def year_total(years, contribution, compound_rate):
    """Find the total contribution by year.

    Args:
        years (numeric): Number of years to achieve the saving goal.
        contribution (numeric): Contribution rate per month.
        compound_rate (numeric): Expected compound rate.

    Returns:
         total_by_year: A dataframe of the total contribution by year.
    """
    r = 1 + compound_rate/100
    total = 0
    total_by_year = []
    for i in range(1,math.ceil(years)+2):
        temp = contribution*12*(r**i)
        total = temp + total
        total_by_year.append(total)
    
    total_by_year = pd.DataFrame(total_by_year, columns=['total'])
    
    return total_by_year

def salary_contribution_summary(df, idx_salary, salary):
    if salary <= 20000:
        employee_contribution = df['employee'][idx_salary]
        employer_contribution = df['employer'][idx_salary]
        total_contribution = df['total'][idx_salary]
    else:
        employee_contribution = math.ceil(salary*0.11)
        employer_contribution = math.ceil(salary*0.12)
        total_contribution = employee_contribution + employer_contribution
    
    summary = pd.DataFrame({'Salary': salary, 
                            'Net Salary': salary - employee_contribution,
                            'Employee Contribution': employee_contribution, 
                            'Employer Contribution': employer_contribution, 
                            'Total Contribution': total_contribution}, index=[0])

    return summary

def bonus_contribution_summary(df, idx_bonus, bonus):
    if bonus <= 20000:
        employee_contribution = df['employee'][idx_bonus]
        employer_contribution = df['employer'][idx_bonus]
        total_contribution = df['total'][idx_bonus]
    else:
        employee_contribution = math.ceil(bonus*0.11)
        employer_contribution = 5
        total_contribution = employee_contribution + employer_contribution
    
    summary = pd.DataFrame({'Bonus': bonus,
                            'Net Bonus': bonus - employee_contribution,
                            'Employee Contribution': employee_contribution, 
                            'Employer Contribution': employer_contribution, 
                            'Total Contribution': total_contribution}, index=[0])
    return summary

def twenty_above_contribution(nationality, salary):
    if nationality == "Malaysian":
        contribution = math.ceil(salary*0.11) + math.ceil(salary*0.12)
    else:
        contribution = math.ceil(salary*0.11) + 5
    return contribution

def twenty_above_bonus_contribution(nationality, bonus):
    if nationality == "Malaysian":
        contribution = math.ceil(bonus*0.11) + math.ceil(bonus*0.12)
    else:
        contribution = math.ceil(bonus*0.11) + 5
    return contribution