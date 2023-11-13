#!/usr/bin/env python
# coding: utf-8

# # Project Description

# This project involves the exploration and analysis of HR data obtained from XYZ Technologies.
# The dataset encompasses critical employee information, including identifiers, designations, performance scores, and salary details. 
# 
# As a Data Scientist, the goal is to utilize data visualization tools such as seaborn and matplotlib to create informative charts.

# ## Importing Modules for the Task

# In[15]:


import pandas as pd
import numpy as np
import seaborn as sns
sns.set_theme()
import matplotlib.pyplot as plt
import datetime


# Data Extraction, Transformation, Loading and Analyses

# In[16]:


import pandas as pd
df =pd.read_csv('HRDataset_v14 .csv')


# In[17]:


df


# In[18]:


df.head(10)


# In[19]:


#Checking the column information of the data frame
df.info()     


# 303 values are missing in the ManagerID column. We can drop the column as it's not required for analysis due to many redundant values.

# In[20]:


#Having the ststaistical analysis of the given data frame.
df.describe()


# In[21]:


#Checking the shape of the data
df.shape
     


# In[35]:


df[['Employee_Name','GenderID']].head(10)


# From the data we can conclude that the female gender is represented as 0 and the male gender as 1.

# In[22]:


df[['Employee_Name','Position','PositionID']].head(10)


# In[23]:


df[['Employee_Name','EmploymentStatus']].head(10)


# In[24]:


df[['Employee_Name','Position','PositionID']].head(10)


# In[25]:


df[['Employee_Name','Absences']].head(10)


# In[26]:


df[['Employee_Name','TermReason']].head(10)


# In[27]:


df[['Employee_Name','PerformanceScore']].head(10)


# In[28]:


df[['Employee_Name','MaritalDesc']].head(10)


# In[29]:


df[['Employee_Name','Sex']].head(10)


# In[30]:


df[['Employee_Name','MarriedID','MaritalStatusID','MaritalDesc']].head(10)


# In[31]:


df[['Employee_Name','CitizenDesc']].head(10)


# In[32]:


df[['Employee_Name','Salary','SpecialProjectsCount','Position']].head(10)


# Now we can visualize the graphs and charts

# In[33]:


df['PerformanceScore'].hist()


# From the histogram, we can conclude that the majority of performance score in 'Fully Meets' category.

# In[34]:


df['EmpSatisfaction'].hist()


# In[49]:


#Histogram of the major continuous columns  salary
fig = plt.figure(figsize=(8,5))
g = sns.distplot(df.Salary)
g.set_title('Salary Distribution');


# In[35]:


figscale = 1
df['Salary'].plot(kind='hist', bins=30, title='Salary Distribution', figsize=(8*figscale, 4*figscale))


# The salary distirbution is skewed, with the high majority of employees who is having the salary between 50,000 to 100,000.
# 

# In[36]:


sns.boxplot(data = df, x='Salary')


# In[37]:


sns.boxplot(data = df, x='EngagementSurvey')


# In[38]:


sns.boxplot(data = df, x='EmpSatisfaction')


# In[39]:


sns.boxplot(data = df, x='Absences')


# In[40]:


sns.boxplot(data = df, x='SpecialProjectsCount')


# In[41]:


sns.boxplot(data = df, x='DaysLateLast30')


# In[42]:


sns.boxplot(data = df, x='Salary', y="PerformanceScore")


# The boxplot above also shows that people with a salary of 1,00,000 and above perform their work and tasks as expected.

# In[43]:


df['MaritalDesc'].value_counts().plot(kind='bar')


# It seems like majority of employees are single or married but how many of them are still active ?

# In[53]:


plt.figure(figsize=(16, 6))
sns.countplot(x=df['EmploymentStatus'], hue=df['MaritalDesc'])


# From the figure the majority of employees are single and actively working. 
# Most people who were divorced or widowed are not active.
# Minority of married people left voluntarily, perhaps because of a change of company or region.
# 

# In[44]:


plt.figure(figsize=(8, 8))
sns.countplot(x=df['Sex'], hue=df['TermReason'])


# From the plot we can see that non-attendance is the most common factor terminating workers.The number of females who lost their position in the company is higher than when we compared with males.Moreover, the most another common reason for females to left the job becuase of education and unsatisfaction of the job they had.

# In[54]:


sns.boxplot(data=df, x="PerformanceScore", y="EngagementSurvey")
     


# Also the performance was measured by engagement survey,and the corralation is linear.

# In[46]:


sns.countplot(data=df, x='Sex')


# Based on the graph, the company shows welcoming diversity in terms of gender. However, the graph only depicts two gender identities.

# In[47]:


#pie chart

h = pd.DataFrame(df["Sex"].value_counts()).reset_index()
palette_color = sns.color_palette('bright')
plt.pie(h["Sex"], labels=h["index"], colors=sns.color_palette('Set1'),autopct='%.0f%%')
plt.tight_layout()


# In[48]:


sns.swarmplot(x='Sex', y='Salary', data=df)
plt.xlabel("Gender")
plt.ylabel("Salary")


# Again for gender based analysis from above there  are few number of female with Salary higher than 2,00,000, which is also a good sign for equal pay and diversity.

# In[49]:


# Checking marital status of the employees
fig = plt.figure(figsize=(8,5))
g = sns.catplot(x="MaritalDesc",kind='count',order=['Single', 'Married', 'Divorced', 'Widowed', 'Separated'], aspect=1.3, data=df);
g.fig.suptitle("Count of Marital status",y=1.05)


# In[50]:


plt.figure(figsize=(16, 6))
sns.countplot(x=df['EmploymentStatus'], hue=df['Department'])


# In all types of employment relationships, the production department has the most employees.

# In[51]:


plt.figure(figsize=(16, 6))
sns.countplot(x=df['EmploymentStatus'], hue=df['EmpSatisfaction'])


# In[52]:


plt.figure(figsize=(16, 6))
sns.countplot(x=df['Department'], hue=df['PerformanceScore'])


# In[53]:


plt.figure(figsize=(16, 6))
sns.countplot(x=df['Sex'], hue=df['EmpSatisfaction'])


# In[65]:


# The number of the staff regarding the department
fig = plt.figure(figsize=(10,4))
g = sns.catplot(x="Department",kind='count',order=['Production       ', 'IT/IS', 'Software Engineering',
       'Admin Offices', 'Sales', 'Executive Office'], aspect=2.0, data=df);
g.fig.suptitle("Number of employee per department",y=1.05);


# In[54]:


# Mean Salary per department
plt.figure(figsize=(12, 6))
sns.barplot(x='Department', y='Salary', width = 1.0, data=df)
plt.title('Salary of the employees based on department')
plt.xlabel('Department')
plt.ylabel('Mean Salary per Department')
plt.show()


# In[55]:


#Hiring platforms preffered
plt.figure(figsize = (19, 8))

sns.countplot( x ="RecruitmentSource", data=df)


# Indeed,LinkedIn and Goodle Search is the top three recruitment source among all.

# In[56]:


plt.figure(figsize=(16, 6))
sns.countplot(x=df['RecruitmentSource'], hue=df['PerformanceScore'])


# Employee performance is correlated with the recruitment source's popularity. This illustrates that the right places to find passionate and enthusiastic individuals are the sources.

# In[57]:


#heat map
fig = plt.figure(figsize=(8,5))
g = sns.heatmap(df.corr());
g.set_title('correlation between continuous variables [Heat Map]')


# In[61]:


r = df.loc[:,["PerfScoreID","Salary","EngagementSurvey","EmpSatisfaction","SpecialProjectsCount","Absences","DaysLateLast30"]]
     

sns.heatmap(r.corr(),vmin = -1,vmax = 1,annot = True);


# In[58]:


r = df.loc[:,["PerfScoreID","Salary","EngagementSurvey","EmpSatisfaction","Department","Absences","GenderID"]]
     
sns.heatmap(r.corr(),vmin = -1,vmax = 1,annot = True);


# In[71]:


sns.barplot(df,y ="Department",x ="Salary",hue = "Sex")


# In[76]:


plt.scatter(df['Salary'], df['Absences'])
plt.xlabel('Salary')
plt.ylabel('Absences')
plt.title('Effect of Salary because of Absences')
plt.show()


# In[79]:


plt.scatter(df['Salary'], df['MaritalStatusID'])
plt.xlabel('Salary')
plt.ylabel('MaritalStatusID')
plt.title('Effect of Salary because of Marital Status')
plt.show()


# In[82]:


sns.barplot(df,y ="Department",x ="Salary",hue = "MaritalStatusID")


# In[83]:


sns.violinplot(data = df,y = "Department", x = "PerfScoreID")
plt.ylabel('Department')

plt.xlabel('Performance Score')
     


# In[107]:


#Recruting diversity analysis based on citizenship

plt.hist(df['CitizenDesc'])
plt.title('Citizenship of Employees')
plt.xlabel('Type of Citizens')
plt.ylabel('Number of Employees')
     


# The US Citizens aregot hired more in the company, this is not diversity freindly.

# # Conclusion
# 
# 1. Most of the employees in the company earn between 50000 and 7000 p.a. 
# 2. The production department is the largest one, followed by IT and finally Sales.
# 3. Around 80% of the employees fully meet their performance requirements.
# 4. The company needs to be more open to international employees. The reputation of the company must be considered.
# 5. The IT department has the highest rate of employee turnover. Therefore, recruitment teams should evaluate the hiring process for the IT department.
