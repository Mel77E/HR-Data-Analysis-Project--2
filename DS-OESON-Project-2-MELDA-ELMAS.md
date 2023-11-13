# Project Description

This project involves the exploration and analysis of HR data obtained from XYZ Technologies.
The dataset encompasses critical employee information, including identifiers, designations, performance scores, and salary details. 

As a Data Scientist, the goal is to utilize data visualization tools such as seaborn and matplotlib to create informative charts.

## Importing Modules for the Task


```python
import pandas as pd
import numpy as np
import seaborn as sns
sns.set_theme()
import matplotlib.pyplot as plt
import datetime
```

Data Extraction, Transformation, Loading and Analyses


```python
import pandas as pd
df =pd.read_csv('HRDataset_v14 .csv')
```


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Employee_Name</th>
      <th>EmpID</th>
      <th>MarriedID</th>
      <th>MaritalStatusID</th>
      <th>GenderID</th>
      <th>EmpStatusID</th>
      <th>DeptID</th>
      <th>PerfScoreID</th>
      <th>FromDiversityJobFairID</th>
      <th>Salary</th>
      <th>...</th>
      <th>ManagerName</th>
      <th>ManagerID</th>
      <th>RecruitmentSource</th>
      <th>PerformanceScore</th>
      <th>EngagementSurvey</th>
      <th>EmpSatisfaction</th>
      <th>SpecialProjectsCount</th>
      <th>LastPerformanceReview_Date</th>
      <th>DaysLateLast30</th>
      <th>Absences</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Adinolfi, Wilson  K</td>
      <td>10026</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>5</td>
      <td>4</td>
      <td>0</td>
      <td>62506</td>
      <td>...</td>
      <td>Michael Albert</td>
      <td>22.0</td>
      <td>LinkedIn</td>
      <td>Exceeds</td>
      <td>4.60</td>
      <td>5</td>
      <td>0</td>
      <td>1/17/2019</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Ait Sidi, Karthikeyan</td>
      <td>10084</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>5</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>104437</td>
      <td>...</td>
      <td>Simon Roup</td>
      <td>4.0</td>
      <td>Indeed</td>
      <td>Fully Meets</td>
      <td>4.96</td>
      <td>3</td>
      <td>6</td>
      <td>2/24/2016</td>
      <td>0</td>
      <td>17</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Akinkuolie, Sarah</td>
      <td>10196</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>5</td>
      <td>5</td>
      <td>3</td>
      <td>0</td>
      <td>64955</td>
      <td>...</td>
      <td>Kissy Sullivan</td>
      <td>20.0</td>
      <td>LinkedIn</td>
      <td>Fully Meets</td>
      <td>3.02</td>
      <td>3</td>
      <td>0</td>
      <td>5/15/2012</td>
      <td>0</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Alagbe,Trina</td>
      <td>10088</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>5</td>
      <td>3</td>
      <td>0</td>
      <td>64991</td>
      <td>...</td>
      <td>Elijiah Gray</td>
      <td>16.0</td>
      <td>Indeed</td>
      <td>Fully Meets</td>
      <td>4.84</td>
      <td>5</td>
      <td>0</td>
      <td>01/03/2019</td>
      <td>0</td>
      <td>15</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Anderson, Carol</td>
      <td>10069</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>5</td>
      <td>5</td>
      <td>3</td>
      <td>0</td>
      <td>50825</td>
      <td>...</td>
      <td>Webster Butler</td>
      <td>39.0</td>
      <td>Google Search</td>
      <td>Fully Meets</td>
      <td>5.00</td>
      <td>4</td>
      <td>0</td>
      <td>02/01/2016</td>
      <td>0</td>
      <td>2</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>306</th>
      <td>Woodson, Jason</td>
      <td>10135</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>5</td>
      <td>3</td>
      <td>0</td>
      <td>65893</td>
      <td>...</td>
      <td>Kissy Sullivan</td>
      <td>20.0</td>
      <td>LinkedIn</td>
      <td>Fully Meets</td>
      <td>4.07</td>
      <td>4</td>
      <td>0</td>
      <td>2/28/2019</td>
      <td>0</td>
      <td>13</td>
    </tr>
    <tr>
      <th>307</th>
      <td>Ybarra, Catherine</td>
      <td>10301</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>5</td>
      <td>1</td>
      <td>0</td>
      <td>48513</td>
      <td>...</td>
      <td>Brannon Miller</td>
      <td>12.0</td>
      <td>Google Search</td>
      <td>PIP</td>
      <td>3.20</td>
      <td>2</td>
      <td>0</td>
      <td>09/02/2015</td>
      <td>5</td>
      <td>4</td>
    </tr>
    <tr>
      <th>308</th>
      <td>Zamora, Jennifer</td>
      <td>10010</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
      <td>4</td>
      <td>0</td>
      <td>220450</td>
      <td>...</td>
      <td>Janet King</td>
      <td>2.0</td>
      <td>Employee Referral</td>
      <td>Exceeds</td>
      <td>4.60</td>
      <td>5</td>
      <td>6</td>
      <td>2/21/2019</td>
      <td>0</td>
      <td>16</td>
    </tr>
    <tr>
      <th>309</th>
      <td>Zhou, Julia</td>
      <td>10043</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>89292</td>
      <td>...</td>
      <td>Simon Roup</td>
      <td>4.0</td>
      <td>Employee Referral</td>
      <td>Fully Meets</td>
      <td>5.00</td>
      <td>3</td>
      <td>5</td>
      <td>02/01/2019</td>
      <td>0</td>
      <td>11</td>
    </tr>
    <tr>
      <th>310</th>
      <td>Zima, Colleen</td>
      <td>10271</td>
      <td>0</td>
      <td>4</td>
      <td>0</td>
      <td>1</td>
      <td>5</td>
      <td>3</td>
      <td>0</td>
      <td>45046</td>
      <td>...</td>
      <td>David Stanley</td>
      <td>14.0</td>
      <td>LinkedIn</td>
      <td>Fully Meets</td>
      <td>4.50</td>
      <td>5</td>
      <td>0</td>
      <td>1/30/2019</td>
      <td>0</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
<p>311 rows × 35 columns</p>
</div>




```python
df.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Employee_Name</th>
      <th>EmpID</th>
      <th>MarriedID</th>
      <th>MaritalStatusID</th>
      <th>GenderID</th>
      <th>EmpStatusID</th>
      <th>DeptID</th>
      <th>PerfScoreID</th>
      <th>FromDiversityJobFairID</th>
      <th>Salary</th>
      <th>...</th>
      <th>ManagerName</th>
      <th>ManagerID</th>
      <th>RecruitmentSource</th>
      <th>PerformanceScore</th>
      <th>EngagementSurvey</th>
      <th>EmpSatisfaction</th>
      <th>SpecialProjectsCount</th>
      <th>LastPerformanceReview_Date</th>
      <th>DaysLateLast30</th>
      <th>Absences</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Adinolfi, Wilson  K</td>
      <td>10026</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>5</td>
      <td>4</td>
      <td>0</td>
      <td>62506</td>
      <td>...</td>
      <td>Michael Albert</td>
      <td>22.0</td>
      <td>LinkedIn</td>
      <td>Exceeds</td>
      <td>4.60</td>
      <td>5</td>
      <td>0</td>
      <td>1/17/2019</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Ait Sidi, Karthikeyan</td>
      <td>10084</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>5</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>104437</td>
      <td>...</td>
      <td>Simon Roup</td>
      <td>4.0</td>
      <td>Indeed</td>
      <td>Fully Meets</td>
      <td>4.96</td>
      <td>3</td>
      <td>6</td>
      <td>2/24/2016</td>
      <td>0</td>
      <td>17</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Akinkuolie, Sarah</td>
      <td>10196</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>5</td>
      <td>5</td>
      <td>3</td>
      <td>0</td>
      <td>64955</td>
      <td>...</td>
      <td>Kissy Sullivan</td>
      <td>20.0</td>
      <td>LinkedIn</td>
      <td>Fully Meets</td>
      <td>3.02</td>
      <td>3</td>
      <td>0</td>
      <td>5/15/2012</td>
      <td>0</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Alagbe,Trina</td>
      <td>10088</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>5</td>
      <td>3</td>
      <td>0</td>
      <td>64991</td>
      <td>...</td>
      <td>Elijiah Gray</td>
      <td>16.0</td>
      <td>Indeed</td>
      <td>Fully Meets</td>
      <td>4.84</td>
      <td>5</td>
      <td>0</td>
      <td>01/03/2019</td>
      <td>0</td>
      <td>15</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Anderson, Carol</td>
      <td>10069</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>5</td>
      <td>5</td>
      <td>3</td>
      <td>0</td>
      <td>50825</td>
      <td>...</td>
      <td>Webster Butler</td>
      <td>39.0</td>
      <td>Google Search</td>
      <td>Fully Meets</td>
      <td>5.00</td>
      <td>4</td>
      <td>0</td>
      <td>02/01/2016</td>
      <td>0</td>
      <td>2</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Anderson, Linda</td>
      <td>10002</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>5</td>
      <td>4</td>
      <td>0</td>
      <td>57568</td>
      <td>...</td>
      <td>Amy Dunn</td>
      <td>11.0</td>
      <td>LinkedIn</td>
      <td>Exceeds</td>
      <td>5.00</td>
      <td>5</td>
      <td>0</td>
      <td>01/07/2019</td>
      <td>0</td>
      <td>15</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Andreola, Colby</td>
      <td>10194</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>4</td>
      <td>3</td>
      <td>0</td>
      <td>95660</td>
      <td>...</td>
      <td>Alex Sweetwater</td>
      <td>10.0</td>
      <td>LinkedIn</td>
      <td>Fully Meets</td>
      <td>3.04</td>
      <td>3</td>
      <td>4</td>
      <td>01/02/2019</td>
      <td>0</td>
      <td>19</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Athwal, Sam</td>
      <td>10062</td>
      <td>0</td>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>5</td>
      <td>3</td>
      <td>0</td>
      <td>59365</td>
      <td>...</td>
      <td>Ketsia Liebig</td>
      <td>19.0</td>
      <td>Employee Referral</td>
      <td>Fully Meets</td>
      <td>5.00</td>
      <td>4</td>
      <td>0</td>
      <td>2/25/2019</td>
      <td>0</td>
      <td>19</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Bachiochi, Linda</td>
      <td>10114</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>5</td>
      <td>3</td>
      <td>1</td>
      <td>47837</td>
      <td>...</td>
      <td>Brannon Miller</td>
      <td>12.0</td>
      <td>Diversity Job Fair</td>
      <td>Fully Meets</td>
      <td>4.46</td>
      <td>3</td>
      <td>0</td>
      <td>1/25/2019</td>
      <td>0</td>
      <td>4</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Bacong, Alejandro</td>
      <td>10250</td>
      <td>0</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>3</td>
      <td>0</td>
      <td>50178</td>
      <td>...</td>
      <td>Peter Monroe</td>
      <td>7.0</td>
      <td>Indeed</td>
      <td>Fully Meets</td>
      <td>5.00</td>
      <td>5</td>
      <td>6</td>
      <td>2/18/2019</td>
      <td>0</td>
      <td>16</td>
    </tr>
  </tbody>
</table>
<p>10 rows × 35 columns</p>
</div>




```python
#Checking the column information of the data frame
df.info()     
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 311 entries, 0 to 310
    Data columns (total 35 columns):
     #   Column                      Non-Null Count  Dtype  
    ---  ------                      --------------  -----  
     0   Employee_Name               311 non-null    object 
     1   EmpID                       311 non-null    int64  
     2   MarriedID                   311 non-null    int64  
     3   MaritalStatusID             311 non-null    int64  
     4   GenderID                    311 non-null    int64  
     5   EmpStatusID                 311 non-null    int64  
     6   DeptID                      311 non-null    int64  
     7   PerfScoreID                 311 non-null    int64  
     8   FromDiversityJobFairID      311 non-null    int64  
     9   Salary                      311 non-null    int64  
     10  Termd                       311 non-null    int64  
     11  PositionID                  311 non-null    int64  
     12  Position                    311 non-null    object 
     13  State                       311 non-null    object 
     14  Zip                         311 non-null    int64  
     15  DOB                         311 non-null    object 
     16  Sex                         311 non-null    object 
     17  MaritalDesc                 311 non-null    object 
     18  CitizenDesc                 311 non-null    object 
     19  HispanicLatino              311 non-null    object 
     20  DateofHire                  311 non-null    object 
     21  DateofHire.1                311 non-null    object 
     22  TermReason                  311 non-null    object 
     23  EmploymentStatus            311 non-null    object 
     24  Department                  311 non-null    object 
     25  ManagerName                 311 non-null    object 
     26  ManagerID                   303 non-null    float64
     27  RecruitmentSource           311 non-null    object 
     28  PerformanceScore            311 non-null    object 
     29  EngagementSurvey            311 non-null    float64
     30  EmpSatisfaction             311 non-null    int64  
     31  SpecialProjectsCount        311 non-null    int64  
     32  LastPerformanceReview_Date  311 non-null    object 
     33  DaysLateLast30              311 non-null    int64  
     34  Absences                    311 non-null    int64  
    dtypes: float64(2), int64(16), object(17)
    memory usage: 85.2+ KB
    

303 values are missing in the ManagerID column. We can drop the column as it's not required for analysis due to many redundant values.


```python
#Having the ststaistical analysis of the given data frame.
df.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>EmpID</th>
      <th>MarriedID</th>
      <th>MaritalStatusID</th>
      <th>GenderID</th>
      <th>EmpStatusID</th>
      <th>DeptID</th>
      <th>PerfScoreID</th>
      <th>FromDiversityJobFairID</th>
      <th>Salary</th>
      <th>Termd</th>
      <th>PositionID</th>
      <th>Zip</th>
      <th>ManagerID</th>
      <th>EngagementSurvey</th>
      <th>EmpSatisfaction</th>
      <th>SpecialProjectsCount</th>
      <th>DaysLateLast30</th>
      <th>Absences</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>311.000000</td>
      <td>311.000000</td>
      <td>311.000000</td>
      <td>311.000000</td>
      <td>311.000000</td>
      <td>311.000000</td>
      <td>311.000000</td>
      <td>311.000000</td>
      <td>311.000000</td>
      <td>311.000000</td>
      <td>311.000000</td>
      <td>311.000000</td>
      <td>303.000000</td>
      <td>311.000000</td>
      <td>311.000000</td>
      <td>311.000000</td>
      <td>311.000000</td>
      <td>311.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>10156.000000</td>
      <td>0.398714</td>
      <td>0.810289</td>
      <td>0.434084</td>
      <td>2.392283</td>
      <td>4.610932</td>
      <td>2.977492</td>
      <td>0.093248</td>
      <td>69020.684887</td>
      <td>0.334405</td>
      <td>16.845659</td>
      <td>6555.482315</td>
      <td>14.570957</td>
      <td>4.110000</td>
      <td>3.890675</td>
      <td>1.218650</td>
      <td>0.414791</td>
      <td>10.237942</td>
    </tr>
    <tr>
      <th>std</th>
      <td>89.922189</td>
      <td>0.490423</td>
      <td>0.943239</td>
      <td>0.496435</td>
      <td>1.794383</td>
      <td>1.083487</td>
      <td>0.587072</td>
      <td>0.291248</td>
      <td>25156.636930</td>
      <td>0.472542</td>
      <td>6.223419</td>
      <td>16908.396884</td>
      <td>8.078306</td>
      <td>0.789938</td>
      <td>0.909241</td>
      <td>2.349421</td>
      <td>1.294519</td>
      <td>5.852596</td>
    </tr>
    <tr>
      <th>min</th>
      <td>10001.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>45046.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>1013.000000</td>
      <td>1.000000</td>
      <td>1.120000</td>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>10078.500000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>5.000000</td>
      <td>3.000000</td>
      <td>0.000000</td>
      <td>55501.500000</td>
      <td>0.000000</td>
      <td>18.000000</td>
      <td>1901.500000</td>
      <td>10.000000</td>
      <td>3.690000</td>
      <td>3.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>5.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>10156.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>5.000000</td>
      <td>3.000000</td>
      <td>0.000000</td>
      <td>62810.000000</td>
      <td>0.000000</td>
      <td>19.000000</td>
      <td>2132.000000</td>
      <td>15.000000</td>
      <td>4.280000</td>
      <td>4.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>10.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>10233.500000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>3.000000</td>
      <td>0.000000</td>
      <td>72036.000000</td>
      <td>1.000000</td>
      <td>20.000000</td>
      <td>2355.000000</td>
      <td>19.000000</td>
      <td>4.700000</td>
      <td>5.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>15.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>10311.000000</td>
      <td>1.000000</td>
      <td>4.000000</td>
      <td>1.000000</td>
      <td>5.000000</td>
      <td>6.000000</td>
      <td>4.000000</td>
      <td>1.000000</td>
      <td>250000.000000</td>
      <td>1.000000</td>
      <td>30.000000</td>
      <td>98052.000000</td>
      <td>39.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>8.000000</td>
      <td>6.000000</td>
      <td>20.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Checking the shape of the data
df.shape
     
```




    (311, 35)




```python
df[['Employee_Name','GenderID']].head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Employee_Name</th>
      <th>GenderID</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Adinolfi, Wilson  K</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Ait Sidi, Karthikeyan</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Akinkuolie, Sarah</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Alagbe,Trina</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Anderson, Carol</td>
      <td>0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Anderson, Linda</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Andreola, Colby</td>
      <td>0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Athwal, Sam</td>
      <td>1</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Bachiochi, Linda</td>
      <td>0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Bacong, Alejandro</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



From the data we can conclude that the female gender is represented as 0 and the male gender as 1.


```python
df[['Employee_Name','Position','PositionID']].head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Employee_Name</th>
      <th>Position</th>
      <th>PositionID</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Adinolfi, Wilson  K</td>
      <td>Production Technician I</td>
      <td>19</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Ait Sidi, Karthikeyan</td>
      <td>Sr. DBA</td>
      <td>27</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Akinkuolie, Sarah</td>
      <td>Production Technician II</td>
      <td>20</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Alagbe,Trina</td>
      <td>Production Technician I</td>
      <td>19</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Anderson, Carol</td>
      <td>Production Technician I</td>
      <td>19</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Anderson, Linda</td>
      <td>Production Technician I</td>
      <td>19</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Andreola, Colby</td>
      <td>Software Engineer</td>
      <td>24</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Athwal, Sam</td>
      <td>Production Technician I</td>
      <td>19</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Bachiochi, Linda</td>
      <td>Production Technician I</td>
      <td>19</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Bacong, Alejandro</td>
      <td>IT Support</td>
      <td>14</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[['Employee_Name','EmploymentStatus']].head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Employee_Name</th>
      <th>EmploymentStatus</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Adinolfi, Wilson  K</td>
      <td>Active</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Ait Sidi, Karthikeyan</td>
      <td>Voluntarily Terminated</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Akinkuolie, Sarah</td>
      <td>Voluntarily Terminated</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Alagbe,Trina</td>
      <td>Active</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Anderson, Carol</td>
      <td>Voluntarily Terminated</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Anderson, Linda</td>
      <td>Active</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Andreola, Colby</td>
      <td>Active</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Athwal, Sam</td>
      <td>Active</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Bachiochi, Linda</td>
      <td>Active</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Bacong, Alejandro</td>
      <td>Active</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[['Employee_Name','Position','PositionID']].head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Employee_Name</th>
      <th>Position</th>
      <th>PositionID</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Adinolfi, Wilson  K</td>
      <td>Production Technician I</td>
      <td>19</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Ait Sidi, Karthikeyan</td>
      <td>Sr. DBA</td>
      <td>27</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Akinkuolie, Sarah</td>
      <td>Production Technician II</td>
      <td>20</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Alagbe,Trina</td>
      <td>Production Technician I</td>
      <td>19</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Anderson, Carol</td>
      <td>Production Technician I</td>
      <td>19</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Anderson, Linda</td>
      <td>Production Technician I</td>
      <td>19</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Andreola, Colby</td>
      <td>Software Engineer</td>
      <td>24</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Athwal, Sam</td>
      <td>Production Technician I</td>
      <td>19</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Bachiochi, Linda</td>
      <td>Production Technician I</td>
      <td>19</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Bacong, Alejandro</td>
      <td>IT Support</td>
      <td>14</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[['Employee_Name','Absences']].head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Employee_Name</th>
      <th>Absences</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Adinolfi, Wilson  K</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Ait Sidi, Karthikeyan</td>
      <td>17</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Akinkuolie, Sarah</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Alagbe,Trina</td>
      <td>15</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Anderson, Carol</td>
      <td>2</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Anderson, Linda</td>
      <td>15</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Andreola, Colby</td>
      <td>19</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Athwal, Sam</td>
      <td>19</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Bachiochi, Linda</td>
      <td>4</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Bacong, Alejandro</td>
      <td>16</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[['Employee_Name','TermReason']].head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Employee_Name</th>
      <th>TermReason</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Adinolfi, Wilson  K</td>
      <td>N/A-StillEmployed</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Ait Sidi, Karthikeyan</td>
      <td>career change</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Akinkuolie, Sarah</td>
      <td>hours</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Alagbe,Trina</td>
      <td>N/A-StillEmployed</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Anderson, Carol</td>
      <td>return to school</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Anderson, Linda</td>
      <td>N/A-StillEmployed</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Andreola, Colby</td>
      <td>N/A-StillEmployed</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Athwal, Sam</td>
      <td>N/A-StillEmployed</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Bachiochi, Linda</td>
      <td>N/A-StillEmployed</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Bacong, Alejandro</td>
      <td>N/A-StillEmployed</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[['Employee_Name','PerformanceScore']].head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Employee_Name</th>
      <th>PerformanceScore</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Adinolfi, Wilson  K</td>
      <td>Exceeds</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Ait Sidi, Karthikeyan</td>
      <td>Fully Meets</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Akinkuolie, Sarah</td>
      <td>Fully Meets</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Alagbe,Trina</td>
      <td>Fully Meets</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Anderson, Carol</td>
      <td>Fully Meets</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Anderson, Linda</td>
      <td>Exceeds</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Andreola, Colby</td>
      <td>Fully Meets</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Athwal, Sam</td>
      <td>Fully Meets</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Bachiochi, Linda</td>
      <td>Fully Meets</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Bacong, Alejandro</td>
      <td>Fully Meets</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[['Employee_Name','MaritalDesc']].head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Employee_Name</th>
      <th>MaritalDesc</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Adinolfi, Wilson  K</td>
      <td>Single</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Ait Sidi, Karthikeyan</td>
      <td>Married</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Akinkuolie, Sarah</td>
      <td>Married</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Alagbe,Trina</td>
      <td>Married</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Anderson, Carol</td>
      <td>Divorced</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Anderson, Linda</td>
      <td>Single</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Andreola, Colby</td>
      <td>Single</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Athwal, Sam</td>
      <td>Widowed</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Bachiochi, Linda</td>
      <td>Single</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Bacong, Alejandro</td>
      <td>Divorced</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[['Employee_Name','Sex']].head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Employee_Name</th>
      <th>Sex</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Adinolfi, Wilson  K</td>
      <td>M</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Ait Sidi, Karthikeyan</td>
      <td>M</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Akinkuolie, Sarah</td>
      <td>F</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Alagbe,Trina</td>
      <td>F</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Anderson, Carol</td>
      <td>F</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Anderson, Linda</td>
      <td>F</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Andreola, Colby</td>
      <td>F</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Athwal, Sam</td>
      <td>M</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Bachiochi, Linda</td>
      <td>F</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Bacong, Alejandro</td>
      <td>M</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[['Employee_Name','MarriedID','MaritalStatusID','MaritalDesc']].head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Employee_Name</th>
      <th>MarriedID</th>
      <th>MaritalStatusID</th>
      <th>MaritalDesc</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Adinolfi, Wilson  K</td>
      <td>0</td>
      <td>0</td>
      <td>Single</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Ait Sidi, Karthikeyan</td>
      <td>1</td>
      <td>1</td>
      <td>Married</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Akinkuolie, Sarah</td>
      <td>1</td>
      <td>1</td>
      <td>Married</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Alagbe,Trina</td>
      <td>1</td>
      <td>1</td>
      <td>Married</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Anderson, Carol</td>
      <td>0</td>
      <td>2</td>
      <td>Divorced</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Anderson, Linda</td>
      <td>0</td>
      <td>0</td>
      <td>Single</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Andreola, Colby</td>
      <td>0</td>
      <td>0</td>
      <td>Single</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Athwal, Sam</td>
      <td>0</td>
      <td>4</td>
      <td>Widowed</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Bachiochi, Linda</td>
      <td>0</td>
      <td>0</td>
      <td>Single</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Bacong, Alejandro</td>
      <td>0</td>
      <td>2</td>
      <td>Divorced</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[['Employee_Name','CitizenDesc']].head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Employee_Name</th>
      <th>CitizenDesc</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Adinolfi, Wilson  K</td>
      <td>US Citizen</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Ait Sidi, Karthikeyan</td>
      <td>US Citizen</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Akinkuolie, Sarah</td>
      <td>US Citizen</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Alagbe,Trina</td>
      <td>US Citizen</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Anderson, Carol</td>
      <td>US Citizen</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Anderson, Linda</td>
      <td>US Citizen</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Andreola, Colby</td>
      <td>US Citizen</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Athwal, Sam</td>
      <td>US Citizen</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Bachiochi, Linda</td>
      <td>US Citizen</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Bacong, Alejandro</td>
      <td>US Citizen</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[['Employee_Name','Salary','SpecialProjectsCount','Position']].head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Employee_Name</th>
      <th>Salary</th>
      <th>SpecialProjectsCount</th>
      <th>Position</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Adinolfi, Wilson  K</td>
      <td>62506</td>
      <td>0</td>
      <td>Production Technician I</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Ait Sidi, Karthikeyan</td>
      <td>104437</td>
      <td>6</td>
      <td>Sr. DBA</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Akinkuolie, Sarah</td>
      <td>64955</td>
      <td>0</td>
      <td>Production Technician II</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Alagbe,Trina</td>
      <td>64991</td>
      <td>0</td>
      <td>Production Technician I</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Anderson, Carol</td>
      <td>50825</td>
      <td>0</td>
      <td>Production Technician I</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Anderson, Linda</td>
      <td>57568</td>
      <td>0</td>
      <td>Production Technician I</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Andreola, Colby</td>
      <td>95660</td>
      <td>4</td>
      <td>Software Engineer</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Athwal, Sam</td>
      <td>59365</td>
      <td>0</td>
      <td>Production Technician I</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Bachiochi, Linda</td>
      <td>47837</td>
      <td>0</td>
      <td>Production Technician I</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Bacong, Alejandro</td>
      <td>50178</td>
      <td>6</td>
      <td>IT Support</td>
    </tr>
  </tbody>
</table>
</div>



Now we can visualize the graphs and charts


```python
df['PerformanceScore'].hist()
```




    <Axes: >




    
![png](output_26_1.png)
    


From the histogram, we can conclude that the majority of performance score in 'Fully Meets' category.


```python
df['EmpSatisfaction'].hist()
```




    <Axes: >




    
![png](output_28_1.png)
    



```python
#Histogram of the major continuous columns  salary
fig = plt.figure(figsize=(8,5))
g = sns.distplot(df.Salary)
g.set_title('Salary Distribution');
```

    C:\Users\MELDA\AppData\Local\Temp\ipykernel_3292\872885907.py:3: UserWarning: 
    
    `distplot` is a deprecated function and will be removed in seaborn v0.14.0.
    
    Please adapt your code to use either `displot` (a figure-level function with
    similar flexibility) or `histplot` (an axes-level function for histograms).
    
    For a guide to updating your code to use the new functions, please see
    https://gist.github.com/mwaskom/de44147ed2974457ad6372750bbe5751
    
      g = sns.distplot(df.Salary)
    


    
![png](output_29_1.png)
    



```python
figscale = 1
df['Salary'].plot(kind='hist', bins=30, title='Salary Distribution', figsize=(8*figscale, 4*figscale))
```




    <Axes: title={'center': 'Salary Distribution'}, ylabel='Frequency'>




    
![png](output_30_1.png)
    


The salary distirbution is skewed, with the high majority of employees who is having the salary between 50,000 to 100,000.



```python
sns.boxplot(data = df, x='Salary')
```




    <Axes: xlabel='Salary'>




    
![png](output_32_1.png)
    



```python
sns.boxplot(data = df, x='EngagementSurvey')
```




    <Axes: xlabel='EngagementSurvey'>




    
![png](output_33_1.png)
    



```python
sns.boxplot(data = df, x='EmpSatisfaction')
```




    <Axes: xlabel='EmpSatisfaction'>




    
![png](output_34_1.png)
    



```python
sns.boxplot(data = df, x='Absences')
```




    <Axes: xlabel='Absences'>




    
![png](output_35_1.png)
    



```python
sns.boxplot(data = df, x='SpecialProjectsCount')
```




    <Axes: xlabel='SpecialProjectsCount'>




    
![png](output_36_1.png)
    



```python
sns.boxplot(data = df, x='DaysLateLast30')
```




    <Axes: xlabel='DaysLateLast30'>




    
![png](output_37_1.png)
    



```python
sns.boxplot(data = df, x='Salary', y="PerformanceScore")
```




    <Axes: xlabel='Salary', ylabel='PerformanceScore'>




    
![png](output_38_1.png)
    


The boxplot above also shows that people with a salary of 1,00,000 and above perform their work and tasks as expected.


```python
df['MaritalDesc'].value_counts().plot(kind='bar')
```




    <Axes: >




    
![png](output_40_1.png)
    


It seems like majority of employees are single or married but how many of them are still active ?


```python

plt.figure(figsize=(16, 6))
sns.countplot(x=df['EmploymentStatus'], hue=df['MaritalDesc'])
```




    <Axes: xlabel='EmploymentStatus', ylabel='count'>




    
![png](output_42_1.png)
    


From the figure the majority of employees are single and actively working. 
Most people who were divorced or widowed are not active.
Minority of married people left voluntarily, perhaps because of a change of company or region.



```python

plt.figure(figsize=(8, 8))
sns.countplot(x=df['Sex'], hue=df['TermReason'])
```




    <Axes: xlabel='Sex', ylabel='count'>




    
![png](output_44_1.png)
    


From the plot we can see that non-attendance is the most common factor terminating workers.The number of females who lost their position in the company is higher than when we compared with males.Moreover, the most another common reason for females to left the job becuase of education and unsatisfaction of the job they had.


```python
sns.boxplot(data=df, x="PerformanceScore", y="EngagementSurvey")
     
```




    <Axes: xlabel='PerformanceScore', ylabel='EngagementSurvey'>




    
![png](output_46_1.png)
    


Also the performance was measured by engagement survey,and the corralation is linear.


```python
sns.countplot(data=df, x='Sex')
```




    <Axes: xlabel='Sex', ylabel='count'>




    
![png](output_48_1.png)
    


Based on the graph, the company shows welcoming diversity in terms of gender. However, the graph only depicts two gender identities.


```python
#pie chart

h = pd.DataFrame(df["Sex"].value_counts()).reset_index()
palette_color = sns.color_palette('bright')
plt.pie(h["Sex"], labels=h["index"], colors=sns.color_palette('Set1'),autopct='%.0f%%')
plt.tight_layout()
```


    
![png](output_50_0.png)
    



```python
sns.swarmplot(x='Sex', y='Salary', data=df)
plt.xlabel("Gender")
plt.ylabel("Salary")
```




    Text(10.250000000000002, 0.5, 'Salary')



    C:\Users\MELDA\anaconda3\lib\site-packages\seaborn\categorical.py:3544: UserWarning: 6.8% of the points cannot be placed; you may want to decrease the size of the markers or use stripplot.
      warnings.warn(msg, UserWarning)
    


    
![png](output_51_2.png)
    


Again for gender based analysis from above there  are few number of female with Salary higher than 2,00,000, which is also a good sign for equal pay and diversity.


```python
# Checking marital status of the employees
fig = plt.figure(figsize=(8,5))
g = sns.catplot(x="MaritalDesc",kind='count',order=['Single', 'Married', 'Divorced', 'Widowed', 'Separated'], aspect=1.3, data=df);
g.fig.suptitle("Count of Marital status",y=1.05)
```




    Text(0.5, 1.05, 'Count of Marital status')




    <Figure size 800x500 with 0 Axes>



    
![png](output_53_2.png)
    



```python

plt.figure(figsize=(16, 6))
sns.countplot(x=df['EmploymentStatus'], hue=df['Department'])
```




    <Axes: xlabel='EmploymentStatus', ylabel='count'>




    
![png](output_54_1.png)
    


In all types of employment relationships, the production department has the most employees.


```python

plt.figure(figsize=(16, 6))
sns.countplot(x=df['EmploymentStatus'], hue=df['EmpSatisfaction'])
```




    <Axes: xlabel='EmploymentStatus', ylabel='count'>




    
![png](output_56_1.png)
    



```python
plt.figure(figsize=(16, 6))
sns.countplot(x=df['Department'], hue=df['PerformanceScore'])
```




    <Axes: xlabel='Department', ylabel='count'>




    
![png](output_57_1.png)
    



```python
plt.figure(figsize=(16, 6))
sns.countplot(x=df['Sex'], hue=df['EmpSatisfaction'])
```




    <Axes: xlabel='Sex', ylabel='count'>




    
![png](output_58_1.png)
    



```python
# The number of the staff regarding the department
fig = plt.figure(figsize=(10,4))
g = sns.catplot(x="Department",kind='count',order=['Production       ', 'IT/IS', 'Software Engineering',
       'Admin Offices', 'Sales', 'Executive Office'], aspect=2.0, data=df);
g.fig.suptitle("Number of employee per department",y=1.05);
```


    <Figure size 1000x400 with 0 Axes>



    
![png](output_59_1.png)
    



```python
# Mean Salary per department
plt.figure(figsize=(12, 6))
sns.barplot(x='Department', y='Salary', width = 1.0, data=df)
plt.title('Salary of the employees based on department')
plt.xlabel('Department')
plt.ylabel('Mean Salary per Department')
plt.show()
```


    
![png](output_60_0.png)
    



```python
#Hiring platforms preffered
plt.figure(figsize = (19, 8))

sns.countplot( x ="RecruitmentSource", data=df)
```




    <Axes: xlabel='RecruitmentSource', ylabel='count'>




    
![png](output_61_1.png)
    


Indeed,LinkedIn and Goodle Search is the top three recruitment source among all.


```python
plt.figure(figsize=(16, 6))
sns.countplot(x=df['RecruitmentSource'], hue=df['PerformanceScore'])
```




    <Axes: xlabel='RecruitmentSource', ylabel='count'>




    
![png](output_63_1.png)
    


Employee performance is correlated with the recruitment source's popularity. This illustrates that the right places to find passionate and enthusiastic individuals are the sources.


```python

#heat map
fig = plt.figure(figsize=(8,5))
g = sns.heatmap(df.corr());
g.set_title('correlation between continuous variables [Heat Map]')
```

    C:\Users\MELDA\AppData\Local\Temp\ipykernel_10348\1550317639.py:3: FutureWarning: The default value of numeric_only in DataFrame.corr is deprecated. In a future version, it will default to False. Select only valid columns or specify the value of numeric_only to silence this warning.
      g = sns.heatmap(df.corr());
    




    Text(0.5, 1.0, 'correlation between continuous variables [Heat Map]')




    
![png](output_65_2.png)
    



```python
r = df.loc[:,["PerfScoreID","Salary","EngagementSurvey","EmpSatisfaction","SpecialProjectsCount","Absences","DaysLateLast30"]]
     

sns.heatmap(r.corr(),vmin = -1,vmax = 1,annot = True);

```


    
![png](output_66_0.png)
    



```python
r = df.loc[:,["PerfScoreID","Salary","EngagementSurvey","EmpSatisfaction","Department","Absences","GenderID"]]
     
sns.heatmap(r.corr(),vmin = -1,vmax = 1,annot = True);
```

    C:\Users\MELDA\AppData\Local\Temp\ipykernel_10348\286419917.py:3: FutureWarning: The default value of numeric_only in DataFrame.corr is deprecated. In a future version, it will default to False. Select only valid columns or specify the value of numeric_only to silence this warning.
      sns.heatmap(r.corr(),vmin = -1,vmax = 1,annot = True);
    


    
![png](output_67_1.png)
    



```python

sns.barplot(df,y ="Department",x ="Salary",hue = "Sex")

```




    <Axes: xlabel='Salary', ylabel='Department'>




    
![png](output_68_1.png)
    



```python
plt.scatter(df['Salary'], df['Absences'])
plt.xlabel('Salary')
plt.ylabel('Absences')
plt.title('Effect of Salary because of Absences')
plt.show()
```


    
![png](output_69_0.png)
    



```python
plt.scatter(df['Salary'], df['MaritalStatusID'])
plt.xlabel('Salary')
plt.ylabel('MaritalStatusID')
plt.title('Effect of Salary because of Marital Status')
plt.show()
```


    
![png](output_70_0.png)
    



```python

sns.barplot(df,y ="Department",x ="Salary",hue = "MaritalStatusID")
```




    <Axes: xlabel='Salary', ylabel='Department'>




    
![png](output_71_1.png)
    



```python

sns.violinplot(data = df,y = "Department", x = "PerfScoreID")
plt.ylabel('Department')

plt.xlabel('Performance Score')
     
```




    Text(0.5, 0, 'Performance Score')




    
![png](output_72_1.png)
    



```python
#Recruting diversity analysis based on citizenship

plt.hist(df['CitizenDesc'])
plt.title('Citizenship of Employees')
plt.xlabel('Type of Citizens')
plt.ylabel('Number of Employees')
     
```




    Text(0, 0.5, 'Number of Employees')




    
![png](output_73_1.png)
    


The US Citizens aregot hired more in the company, this is not diversity freindly.

# Conclusion

1. Most of the employees in the company earn between 50000 and 7000 p.a. 
2. The production department is the largest one, followed by IT and finally Sales.
3. Around 80% of the employees fully meet their performance requirements.
4. The company needs to be more open to international employees. The reputation of the company must be considered.
5. The IT department has the highest rate of employee turnover. Therefore, recruitment teams should evaluate the hiring process for the IT department.
