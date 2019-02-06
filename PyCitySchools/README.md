

```python
import pandas as pd
import numpy as np
```


```python
data_file= "raw_data/schools_complete.csv"
school_complete= pd.read_csv(data_file)
schools_complete= school_complete.rename(columns={"name":"school"})
schools_complete


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
      <th>School ID</th>
      <th>school</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>Wilson High School</td>
      <td>Charter</td>
      <td>2283</td>
      <td>1319574</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6</td>
      <td>Cabrera High School</td>
      <td>Charter</td>
      <td>1858</td>
      <td>1081356</td>
    </tr>
    <tr>
      <th>7</th>
      <td>7</td>
      <td>Bailey High School</td>
      <td>District</td>
      <td>4976</td>
      <td>3124928</td>
    </tr>
    <tr>
      <th>8</th>
      <td>8</td>
      <td>Holden High School</td>
      <td>Charter</td>
      <td>427</td>
      <td>248087</td>
    </tr>
    <tr>
      <th>9</th>
      <td>9</td>
      <td>Pena High School</td>
      <td>Charter</td>
      <td>962</td>
      <td>585858</td>
    </tr>
    <tr>
      <th>10</th>
      <td>10</td>
      <td>Wright High School</td>
      <td>Charter</td>
      <td>1800</td>
      <td>1049400</td>
    </tr>
    <tr>
      <th>11</th>
      <td>11</td>
      <td>Rodriguez High School</td>
      <td>District</td>
      <td>3999</td>
      <td>2547363</td>
    </tr>
    <tr>
      <th>12</th>
      <td>12</td>
      <td>Johnson High School</td>
      <td>District</td>
      <td>4761</td>
      <td>3094650</td>
    </tr>
    <tr>
      <th>13</th>
      <td>13</td>
      <td>Ford High School</td>
      <td>District</td>
      <td>2739</td>
      <td>1763916</td>
    </tr>
    <tr>
      <th>14</th>
      <td>14</td>
      <td>Thomas High School</td>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
    </tr>
  </tbody>
</table>
</div>




```python
only_district= schools_complete.loc[schools_complete["type"]== "District", :]
only_district
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
      <th>School ID</th>
      <th>school</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
    </tr>
    <tr>
      <th>7</th>
      <td>7</td>
      <td>Bailey High School</td>
      <td>District</td>
      <td>4976</td>
      <td>3124928</td>
    </tr>
    <tr>
      <th>11</th>
      <td>11</td>
      <td>Rodriguez High School</td>
      <td>District</td>
      <td>3999</td>
      <td>2547363</td>
    </tr>
    <tr>
      <th>12</th>
      <td>12</td>
      <td>Johnson High School</td>
      <td>District</td>
      <td>4761</td>
      <td>3094650</td>
    </tr>
    <tr>
      <th>13</th>
      <td>13</td>
      <td>Ford High School</td>
      <td>District</td>
      <td>2739</td>
      <td>1763916</td>
    </tr>
  </tbody>
</table>
</div>




```python
total_schools= only_district["school"].count()
print("Total Schools: ",total_schools)
total_budget= only_district["budget"].sum()
print("Total Budget: ",total_budget)
```

    Total Schools:  7
    Total Budget:  17347923
    


```python
data_file_2="raw_data/students_complete.csv"
students_complete= pd.read_csv(data_file_2)
students_complete.head(20)
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
      <th>Student ID</th>
      <th>name</th>
      <th>gender</th>
      <th>grade</th>
      <th>school</th>
      <th>reading_score</th>
      <th>math_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Paul Bradley</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>66</td>
      <td>79</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Victor Smith</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>94</td>
      <td>61</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Kevin Rodriguez</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>90</td>
      <td>60</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Dr. Richard Scott</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>67</td>
      <td>58</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Bonnie Ray</td>
      <td>F</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>97</td>
      <td>84</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>Bryan Miranda</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>94</td>
      <td>94</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6</td>
      <td>Sheena Carter</td>
      <td>F</td>
      <td>11th</td>
      <td>Huang High School</td>
      <td>82</td>
      <td>80</td>
    </tr>
    <tr>
      <th>7</th>
      <td>7</td>
      <td>Nicole Baker</td>
      <td>F</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>96</td>
      <td>69</td>
    </tr>
    <tr>
      <th>8</th>
      <td>8</td>
      <td>Michael Roth</td>
      <td>M</td>
      <td>10th</td>
      <td>Huang High School</td>
      <td>95</td>
      <td>87</td>
    </tr>
    <tr>
      <th>9</th>
      <td>9</td>
      <td>Matthew Greene</td>
      <td>M</td>
      <td>10th</td>
      <td>Huang High School</td>
      <td>96</td>
      <td>84</td>
    </tr>
    <tr>
      <th>10</th>
      <td>10</td>
      <td>Andrew Alexander</td>
      <td>M</td>
      <td>10th</td>
      <td>Huang High School</td>
      <td>90</td>
      <td>70</td>
    </tr>
    <tr>
      <th>11</th>
      <td>11</td>
      <td>Daniel Cooper</td>
      <td>M</td>
      <td>10th</td>
      <td>Huang High School</td>
      <td>78</td>
      <td>77</td>
    </tr>
    <tr>
      <th>12</th>
      <td>12</td>
      <td>Brittney Walker</td>
      <td>F</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>64</td>
      <td>79</td>
    </tr>
    <tr>
      <th>13</th>
      <td>13</td>
      <td>William Long</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>71</td>
      <td>79</td>
    </tr>
    <tr>
      <th>14</th>
      <td>14</td>
      <td>Tammy Hebert</td>
      <td>F</td>
      <td>10th</td>
      <td>Huang High School</td>
      <td>85</td>
      <td>67</td>
    </tr>
    <tr>
      <th>15</th>
      <td>15</td>
      <td>Dr. Jordan Carson</td>
      <td>M</td>
      <td>11th</td>
      <td>Huang High School</td>
      <td>94</td>
      <td>88</td>
    </tr>
    <tr>
      <th>16</th>
      <td>16</td>
      <td>Donald Zamora</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>88</td>
      <td>55</td>
    </tr>
    <tr>
      <th>17</th>
      <td>17</td>
      <td>Kimberly Santiago</td>
      <td>F</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>74</td>
      <td>75</td>
    </tr>
    <tr>
      <th>18</th>
      <td>18</td>
      <td>Kevin Stevens</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>64</td>
      <td>69</td>
    </tr>
    <tr>
      <th>19</th>
      <td>19</td>
      <td>Brandi Lyons</td>
      <td>F</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>89</td>
      <td>80</td>
    </tr>
  </tbody>
</table>
</div>




```python
students_complete.dtypes
```




    Student ID        int64
    name             object
    gender           object
    grade            object
    school           object
    reading_score     int64
    math_score        int64
    dtype: object




```python
school_counts= students_complete["school"].value_counts()
school_counts
```




    Bailey High School       4976
    Johnson High School      4761
    Hernandez High School    4635
    Rodriguez High School    3999
    Figueroa High School     2949
    Huang High School        2917
    Ford High School         2739
    Wilson High School       2283
    Cabrera High School      1858
    Wright High School       1800
    Shelton High School      1761
    Thomas High School       1635
    Griffin High School      1468
    Pena High School          962
    Holden High School        427
    Name: school, dtype: int64




```python
#grouped_students= students_complete.groupby(["school"])
#grouped_students_table= grouped_students.count()
##grouped_students_table
#merge_table_1= pd.merge(only_districts, )
```


```python
merge_table=pd.merge(only_district,students_complete , on="school")
merge_table.head()
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
      <th>School ID</th>
      <th>school</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
      <th>Student ID</th>
      <th>name</th>
      <th>gender</th>
      <th>grade</th>
      <th>reading_score</th>
      <th>math_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>0</td>
      <td>Paul Bradley</td>
      <td>M</td>
      <td>9th</td>
      <td>66</td>
      <td>79</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>1</td>
      <td>Victor Smith</td>
      <td>M</td>
      <td>12th</td>
      <td>94</td>
      <td>61</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>2</td>
      <td>Kevin Rodriguez</td>
      <td>M</td>
      <td>12th</td>
      <td>90</td>
      <td>60</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0</td>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>3</td>
      <td>Dr. Richard Scott</td>
      <td>M</td>
      <td>12th</td>
      <td>67</td>
      <td>58</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>4</td>
      <td>Bonnie Ray</td>
      <td>F</td>
      <td>9th</td>
      <td>97</td>
      <td>84</td>
    </tr>
  </tbody>
</table>
</div>




```python
total_district_students= merge_table["Student ID"].count()
print("Total Students:", total_district_students)
avg_math= round(merge_table["math_score"].mean(), 2)
avg_reading= round(merge_table["reading_score"].mean(), 2) 
print("Average Math Score: ", avg_math)
print("Average Reading Score: ", avg_reading)
```

    Total Students: 26976
    Average Math Score:  76.99
    Average Reading Score:  80.96
    


```python
passing_math= merge_table.loc[merge_table["math_score"]> 70]
passing_reading= merge_table.loc[merge_table["reading_score"]> 70]
passing_math_total=passing_math["Student ID"].count()
passing_reading_total= passing_reading["Student ID"].count()
percent_passing_math= round((passing_math_total / total_district_students) *100 , 2)
percent_passing_reading= round((passing_reading_total / total_district_students)*100, 2)
print("Math Passing Percent: ", percent_passing_math)
print("Reading Passing Percent: ", percent_passing_reading)
overall_passing_rate= round((percent_passing_math + percent_passing_reading) / 2, 2)
print("Overall Passing Rate: ", overall_passing_rate)
```

    Math Passing Percent:  64.31
    Reading Passing Percent:  78.37
    Overall Passing Rate:  71.34
    


```python
district_summary_table= pd.DataFrame([{"Total Schools":total_schools,
                                      "Total Students":total_district_students,
                                     "Total Budget($)":total_budget,
                                     "Average Math Score":avg_math,
                                     "Average Reading Score":avg_reading,
                                     "% Passing Math":percent_passing_math,
                                    "% Passing Reading":percent_passing_reading,
                                     "Overall Passing Rate":overall_passing_rate}])
district_summary_table= district_summary_table[["Total Schools","Total Students","Total Budget($)","Average Math Score","Average Reading Score","% Passing Math","% Passing Reading","Overall Passing Rate"]]
district_summary_table
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
      <th>Total Schools</th>
      <th>Total Students</th>
      <th>Total Budget($)</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>7</td>
      <td>26976</td>
      <td>17347923</td>
      <td>76.99</td>
      <td>80.96</td>
      <td>64.31</td>
      <td>78.37</td>
      <td>71.34</td>
    </tr>
  </tbody>
</table>
</div>




```python
merge_table_2=pd.merge(schools_complete,students_complete , on="school")
merge_table_2.head()
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
      <th>School ID</th>
      <th>school</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
      <th>Student ID</th>
      <th>name</th>
      <th>gender</th>
      <th>grade</th>
      <th>reading_score</th>
      <th>math_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>0</td>
      <td>Paul Bradley</td>
      <td>M</td>
      <td>9th</td>
      <td>66</td>
      <td>79</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>1</td>
      <td>Victor Smith</td>
      <td>M</td>
      <td>12th</td>
      <td>94</td>
      <td>61</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>2</td>
      <td>Kevin Rodriguez</td>
      <td>M</td>
      <td>12th</td>
      <td>90</td>
      <td>60</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0</td>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>3</td>
      <td>Dr. Richard Scott</td>
      <td>M</td>
      <td>12th</td>
      <td>67</td>
      <td>58</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>4</td>
      <td>Bonnie Ray</td>
      <td>F</td>
      <td>9th</td>
      <td>97</td>
      <td>84</td>
    </tr>
  </tbody>
</table>
</div>




```python
grouped_schools=merge_table_2.set_index("school").groupby("school")

```


```python
#schools_list=schools_complete["school"]
#schools_size=schools_complete["size"]
#schools_type= schools_complete["type"]
schools_size=schools_complete.set_index("school")["size"]
schools_type=schools_complete.set_index("school")["type"]
schools_budget=schools_complete.set_index("school")["budget"]
total_school_students= grouped_schools["name"].count().tolist()

math_score=grouped_schools["math_score"].value_counts()

avg_math_score=grouped_schools["math_score"].mean().tolist()

avg_reading_score=grouped_schools["reading_score"].mean().tolist()







```


```python
passing_math_list=[]
passing_reading_list= []
#school_list=[]

for x , group in grouped_schools:
    #school_list.append(x)
    students_total= group["Student ID"].count()
    passing_M= group.loc[group["math_score"] > 70 ]
    passing_R=group.loc[group["reading_score"] > 70 ]
    passing_M_total= passing_M["Student ID"].count()
    passing_R_total= passing_R["Student ID"].count()
    math_percentage= round((passing_M_total / students_total)*100, 2)
    reading_percentage= round((passing_R_total / students_total)*100, 2)
    
    passing_math_list.append(math_percentage)
    passing_reading_list.append(reading_percentage)
    
    


```


```python
#school_summary_table=pd.DataFrame(schools_list, columns=["school"])
#school_summary_table["type"]=schools_type
school_summary_table= pd.DataFrame(schools_size, columns=["size"])
#school_summary_table["size"]=schools_size
school_summary_table["budget($)"]=schools_budget
school_summary_table["total students"]=total_school_students
school_summary_table["Budget Per Student ($)"]= round(school_summary_table["budget($)"] / school_summary_table["total students"], 2)
school_summary_table["Average Math Score"]=avg_math_score
school_summary_table["Average Reading Score"]=avg_reading_score
school_summary_table["type"]=schools_type

school_summary_table["% Passing Math"]= passing_math_list
school_summary_table["% Passing Reading"]=passing_reading_list
school_summary_table["% Overall Passing Rate"]= round(( school_summary_table["% Passing Math"]+ school_summary_table["% Passing Reading"]) / 2, 2)
school_summary_table



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
      <th>size</th>
      <th>budget($)</th>
      <th>total students</th>
      <th>Budget Per Student ($)</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>type</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
    </tr>
    <tr>
      <th>school</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Huang High School</th>
      <td>2917</td>
      <td>1910635</td>
      <td>4976</td>
      <td>383.97</td>
      <td>77.048432</td>
      <td>81.033963</td>
      <td>District</td>
      <td>64.63</td>
      <td>79.30</td>
      <td>71.96</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>2949</td>
      <td>1884411</td>
      <td>1858</td>
      <td>1014.21</td>
      <td>83.061895</td>
      <td>83.975780</td>
      <td>District</td>
      <td>89.56</td>
      <td>93.86</td>
      <td>91.71</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>1761</td>
      <td>1056600</td>
      <td>2949</td>
      <td>358.29</td>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>Charter</td>
      <td>63.75</td>
      <td>78.43</td>
      <td>71.09</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>4635</td>
      <td>3022020</td>
      <td>2739</td>
      <td>1103.33</td>
      <td>77.102592</td>
      <td>80.746258</td>
      <td>District</td>
      <td>65.75</td>
      <td>77.51</td>
      <td>71.63</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>1468</td>
      <td>917500</td>
      <td>1468</td>
      <td>625.00</td>
      <td>83.351499</td>
      <td>83.816757</td>
      <td>Charter</td>
      <td>89.71</td>
      <td>93.39</td>
      <td>91.55</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>2283</td>
      <td>1319574</td>
      <td>4635</td>
      <td>284.70</td>
      <td>77.289752</td>
      <td>80.934412</td>
      <td>Charter</td>
      <td>64.75</td>
      <td>78.19</td>
      <td>71.47</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>1858</td>
      <td>1081356</td>
      <td>427</td>
      <td>2532.45</td>
      <td>83.803279</td>
      <td>83.814988</td>
      <td>Charter</td>
      <td>90.63</td>
      <td>92.74</td>
      <td>91.68</td>
    </tr>
    <tr>
      <th>Bailey High School</th>
      <td>4976</td>
      <td>3124928</td>
      <td>2917</td>
      <td>1071.28</td>
      <td>76.629414</td>
      <td>81.182722</td>
      <td>District</td>
      <td>63.32</td>
      <td>78.81</td>
      <td>71.06</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>427</td>
      <td>248087</td>
      <td>4761</td>
      <td>52.11</td>
      <td>77.072464</td>
      <td>80.966394</td>
      <td>Charter</td>
      <td>63.85</td>
      <td>78.28</td>
      <td>71.06</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>962</td>
      <td>585858</td>
      <td>962</td>
      <td>609.00</td>
      <td>83.839917</td>
      <td>84.044699</td>
      <td>Charter</td>
      <td>91.68</td>
      <td>92.20</td>
      <td>91.94</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>1800</td>
      <td>1049400</td>
      <td>3999</td>
      <td>262.42</td>
      <td>76.842711</td>
      <td>80.744686</td>
      <td>Charter</td>
      <td>64.07</td>
      <td>77.74</td>
      <td>70.90</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>3999</td>
      <td>2547363</td>
      <td>1761</td>
      <td>1446.54</td>
      <td>83.359455</td>
      <td>83.725724</td>
      <td>District</td>
      <td>89.89</td>
      <td>92.62</td>
      <td>91.26</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>4761</td>
      <td>3094650</td>
      <td>1635</td>
      <td>1892.75</td>
      <td>83.418349</td>
      <td>83.848930</td>
      <td>District</td>
      <td>90.21</td>
      <td>92.91</td>
      <td>91.56</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>2739</td>
      <td>1763916</td>
      <td>2283</td>
      <td>772.63</td>
      <td>83.274201</td>
      <td>83.989488</td>
      <td>District</td>
      <td>90.93</td>
      <td>93.25</td>
      <td>92.09</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>1635</td>
      <td>1043130</td>
      <td>1800</td>
      <td>579.52</td>
      <td>83.682222</td>
      <td>83.955000</td>
      <td>Charter</td>
      <td>90.28</td>
      <td>93.44</td>
      <td>91.86</td>
    </tr>
  </tbody>
</table>
</div>




```python
top_school_overall_rate = school_summary_table.sort_values(["% Overall Passing Rate"], ascending=False)

top_school_overall_rate.reset_index(inplace=True)

top_school_overall_rate.head(5)
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
      <th>school</th>
      <th>size</th>
      <th>budget($)</th>
      <th>total students</th>
      <th>Budget Per Student ($)</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>type</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Ford High School</td>
      <td>2739</td>
      <td>1763916</td>
      <td>2283</td>
      <td>772.63</td>
      <td>83.274201</td>
      <td>83.989488</td>
      <td>District</td>
      <td>90.93</td>
      <td>93.25</td>
      <td>92.09</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Pena High School</td>
      <td>962</td>
      <td>585858</td>
      <td>962</td>
      <td>609.00</td>
      <td>83.839917</td>
      <td>84.044699</td>
      <td>Charter</td>
      <td>91.68</td>
      <td>92.20</td>
      <td>91.94</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Thomas High School</td>
      <td>1635</td>
      <td>1043130</td>
      <td>1800</td>
      <td>579.52</td>
      <td>83.682222</td>
      <td>83.955000</td>
      <td>Charter</td>
      <td>90.28</td>
      <td>93.44</td>
      <td>91.86</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Figueroa High School</td>
      <td>2949</td>
      <td>1884411</td>
      <td>1858</td>
      <td>1014.21</td>
      <td>83.061895</td>
      <td>83.975780</td>
      <td>District</td>
      <td>89.56</td>
      <td>93.86</td>
      <td>91.71</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Cabrera High School</td>
      <td>1858</td>
      <td>1081356</td>
      <td>427</td>
      <td>2532.45</td>
      <td>83.803279</td>
      <td>83.814988</td>
      <td>Charter</td>
      <td>90.63</td>
      <td>92.74</td>
      <td>91.68</td>
    </tr>
  </tbody>
</table>
</div>




```python
bottom_school_overall_rate= school_summary_table.sort_values(["% Overall Passing Rate"])
bottom_school_overall_rate.reset_index(inplace=True)
bottom_school_overall_rate.head(5)
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
      <th>school</th>
      <th>size</th>
      <th>budget($)</th>
      <th>total students</th>
      <th>Budget Per Student ($)</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>type</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Wright High School</td>
      <td>1800</td>
      <td>1049400</td>
      <td>3999</td>
      <td>262.42</td>
      <td>76.842711</td>
      <td>80.744686</td>
      <td>Charter</td>
      <td>64.07</td>
      <td>77.74</td>
      <td>70.90</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bailey High School</td>
      <td>4976</td>
      <td>3124928</td>
      <td>2917</td>
      <td>1071.28</td>
      <td>76.629414</td>
      <td>81.182722</td>
      <td>District</td>
      <td>63.32</td>
      <td>78.81</td>
      <td>71.06</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Holden High School</td>
      <td>427</td>
      <td>248087</td>
      <td>4761</td>
      <td>52.11</td>
      <td>77.072464</td>
      <td>80.966394</td>
      <td>Charter</td>
      <td>63.85</td>
      <td>78.28</td>
      <td>71.06</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Shelton High School</td>
      <td>1761</td>
      <td>1056600</td>
      <td>2949</td>
      <td>358.29</td>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>Charter</td>
      <td>63.75</td>
      <td>78.43</td>
      <td>71.09</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Wilson High School</td>
      <td>2283</td>
      <td>1319574</td>
      <td>4635</td>
      <td>284.70</td>
      <td>77.289752</td>
      <td>80.934412</td>
      <td>Charter</td>
      <td>64.75</td>
      <td>78.19</td>
      <td>71.47</td>
    </tr>
  </tbody>
</table>
</div>




```python
math_by_grade= merge_table_2.groupby(["school","grade"])
average_math_scores= math_by_grade["math_score"].mean()
math_scores_summary_by_grade= pd.DataFrame(average_math_scores)
math_scores_summary_by_grade.rename(columns={"math_score":"Average Math Score"})
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
      <th></th>
      <th>Average Math Score</th>
    </tr>
    <tr>
      <th>school</th>
      <th>grade</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="4" valign="top">Bailey High School</th>
      <th>10th</th>
      <td>76.996772</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>77.515588</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>76.492218</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>77.083676</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Cabrera High School</th>
      <th>10th</th>
      <td>83.154506</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>82.765560</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>83.277487</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>83.094697</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Figueroa High School</th>
      <th>10th</th>
      <td>76.539974</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>76.884344</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>77.151369</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>76.403037</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Ford High School</th>
      <th>10th</th>
      <td>77.672316</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>76.918058</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>76.179963</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>77.361345</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Griffin High School</th>
      <th>10th</th>
      <td>84.229064</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>83.842105</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>83.356164</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>82.044010</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Hernandez High School</th>
      <th>10th</th>
      <td>77.337408</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>77.136029</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>77.186567</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>77.438495</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Holden High School</th>
      <th>10th</th>
      <td>83.429825</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>85.000000</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>82.855422</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>83.787402</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Huang High School</th>
      <th>10th</th>
      <td>75.908735</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>76.446602</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>77.225641</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>77.027251</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Johnson High School</th>
      <th>10th</th>
      <td>76.691117</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>77.491653</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>76.863248</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>77.187857</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Pena High School</th>
      <th>10th</th>
      <td>83.372000</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>84.328125</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>84.121547</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>83.625455</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Rodriguez High School</th>
      <th>10th</th>
      <td>76.612500</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>76.395626</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>77.690748</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>76.859966</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Shelton High School</th>
      <th>10th</th>
      <td>82.917411</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>83.383495</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>83.778976</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>83.420755</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Thomas High School</th>
      <th>10th</th>
      <td>83.087886</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>83.498795</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>83.497041</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>83.590022</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Wilson High School</th>
      <th>10th</th>
      <td>83.724422</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>83.195326</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>83.035794</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>83.085578</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Wright High School</th>
      <th>10th</th>
      <td>84.010288</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>83.836782</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>83.644986</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>83.264706</td>
    </tr>
  </tbody>
</table>
</div>




```python
reading_by_grade= merge_table_2.groupby(["school","grade"])
average_reading_scores= math_by_grade["reading_score"].mean()
reading_scores_summary_by_grade= pd.DataFrame(average_reading_scores)
reading_scores_summary_by_grade.rename(columns={"reading_score":"Average Reading Score"})
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
      <th></th>
      <th>Average Reading Score</th>
    </tr>
    <tr>
      <th>school</th>
      <th>grade</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="4" valign="top">Bailey High School</th>
      <th>10th</th>
      <td>80.907183</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>80.945643</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>80.912451</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>81.303155</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Cabrera High School</th>
      <th>10th</th>
      <td>84.253219</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>83.788382</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>84.287958</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>83.676136</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Figueroa High School</th>
      <th>10th</th>
      <td>81.408912</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>80.640339</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>81.384863</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>81.198598</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Ford High School</th>
      <th>10th</th>
      <td>81.262712</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>80.403642</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>80.662338</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>80.632653</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Griffin High School</th>
      <th>10th</th>
      <td>83.706897</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>84.288089</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>84.013699</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>83.369193</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Hernandez High School</th>
      <th>10th</th>
      <td>80.660147</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>81.396140</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>80.857143</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>80.866860</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Holden High School</th>
      <th>10th</th>
      <td>83.324561</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>83.815534</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>84.698795</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>83.677165</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Huang High School</th>
      <th>10th</th>
      <td>81.512386</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>81.417476</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>80.305983</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>81.290284</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Johnson High School</th>
      <th>10th</th>
      <td>80.773431</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>80.616027</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>81.227564</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>81.260714</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Pena High School</th>
      <th>10th</th>
      <td>83.612000</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>84.335938</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>84.591160</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>83.807273</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Rodriguez High School</th>
      <th>10th</th>
      <td>80.629808</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>80.864811</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>80.376426</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>80.993127</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Shelton High School</th>
      <th>10th</th>
      <td>83.441964</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>84.373786</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>82.781671</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>84.122642</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Thomas High School</th>
      <th>10th</th>
      <td>84.254157</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>83.585542</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>83.831361</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>83.728850</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Wilson High School</th>
      <th>10th</th>
      <td>84.021452</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>83.764608</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>84.317673</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>83.939778</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">Wright High School</th>
      <th>10th</th>
      <td>83.812757</td>
    </tr>
    <tr>
      <th>11th</th>
      <td>84.156322</td>
    </tr>
    <tr>
      <th>12th</th>
      <td>84.073171</td>
    </tr>
    <tr>
      <th>9th</th>
      <td>83.833333</td>
    </tr>
  </tbody>
</table>
</div>




```python
#summary_by_school_spending= school_summary_table.groupby(["school","Budget Per Student ($)"])
#summary_by_school_spending["Budget Per Student ($)","Average Math Score","Average Reading Score","% Passing Math","% Passing Reading","% Overall Passing Rate"].head()

```


```python
budget_range=[0,500, 1000, 1500, 2000]
spending_ranges= ["<500","500-1000","1000-1500","1500-2000" ]
budget_per_student= school_summary_table["Budget Per Student ($)"].tolist()
budget_per_student

```




    [383.97,
     1014.21,
     358.29,
     1103.33,
     625.0,
     284.7,
     2532.45,
     1071.28,
     52.11,
     609.0,
     262.42,
     1446.54,
     1892.75,
     772.63,
     579.52]




```python
school_summary_table["Spending Ranges (Per Student)"]= pd.cut(budget_per_student, budget_range, labels=spending_ranges)
school_summary_table
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
      <th>size</th>
      <th>budget($)</th>
      <th>total students</th>
      <th>Budget Per Student ($)</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>type</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
      <th>Spending Ranges (Per Student)</th>
    </tr>
    <tr>
      <th>school</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Huang High School</th>
      <td>2917</td>
      <td>1910635</td>
      <td>4976</td>
      <td>383.97</td>
      <td>77.048432</td>
      <td>81.033963</td>
      <td>District</td>
      <td>64.63</td>
      <td>79.30</td>
      <td>71.96</td>
      <td>&lt;500</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>2949</td>
      <td>1884411</td>
      <td>1858</td>
      <td>1014.21</td>
      <td>83.061895</td>
      <td>83.975780</td>
      <td>District</td>
      <td>89.56</td>
      <td>93.86</td>
      <td>91.71</td>
      <td>1000-1500</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>1761</td>
      <td>1056600</td>
      <td>2949</td>
      <td>358.29</td>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>Charter</td>
      <td>63.75</td>
      <td>78.43</td>
      <td>71.09</td>
      <td>&lt;500</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>4635</td>
      <td>3022020</td>
      <td>2739</td>
      <td>1103.33</td>
      <td>77.102592</td>
      <td>80.746258</td>
      <td>District</td>
      <td>65.75</td>
      <td>77.51</td>
      <td>71.63</td>
      <td>1000-1500</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>1468</td>
      <td>917500</td>
      <td>1468</td>
      <td>625.00</td>
      <td>83.351499</td>
      <td>83.816757</td>
      <td>Charter</td>
      <td>89.71</td>
      <td>93.39</td>
      <td>91.55</td>
      <td>500-1000</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>2283</td>
      <td>1319574</td>
      <td>4635</td>
      <td>284.70</td>
      <td>77.289752</td>
      <td>80.934412</td>
      <td>Charter</td>
      <td>64.75</td>
      <td>78.19</td>
      <td>71.47</td>
      <td>&lt;500</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>1858</td>
      <td>1081356</td>
      <td>427</td>
      <td>2532.45</td>
      <td>83.803279</td>
      <td>83.814988</td>
      <td>Charter</td>
      <td>90.63</td>
      <td>92.74</td>
      <td>91.68</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Bailey High School</th>
      <td>4976</td>
      <td>3124928</td>
      <td>2917</td>
      <td>1071.28</td>
      <td>76.629414</td>
      <td>81.182722</td>
      <td>District</td>
      <td>63.32</td>
      <td>78.81</td>
      <td>71.06</td>
      <td>1000-1500</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>427</td>
      <td>248087</td>
      <td>4761</td>
      <td>52.11</td>
      <td>77.072464</td>
      <td>80.966394</td>
      <td>Charter</td>
      <td>63.85</td>
      <td>78.28</td>
      <td>71.06</td>
      <td>&lt;500</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>962</td>
      <td>585858</td>
      <td>962</td>
      <td>609.00</td>
      <td>83.839917</td>
      <td>84.044699</td>
      <td>Charter</td>
      <td>91.68</td>
      <td>92.20</td>
      <td>91.94</td>
      <td>500-1000</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>1800</td>
      <td>1049400</td>
      <td>3999</td>
      <td>262.42</td>
      <td>76.842711</td>
      <td>80.744686</td>
      <td>Charter</td>
      <td>64.07</td>
      <td>77.74</td>
      <td>70.90</td>
      <td>&lt;500</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>3999</td>
      <td>2547363</td>
      <td>1761</td>
      <td>1446.54</td>
      <td>83.359455</td>
      <td>83.725724</td>
      <td>District</td>
      <td>89.89</td>
      <td>92.62</td>
      <td>91.26</td>
      <td>1000-1500</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>4761</td>
      <td>3094650</td>
      <td>1635</td>
      <td>1892.75</td>
      <td>83.418349</td>
      <td>83.848930</td>
      <td>District</td>
      <td>90.21</td>
      <td>92.91</td>
      <td>91.56</td>
      <td>1500-2000</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>2739</td>
      <td>1763916</td>
      <td>2283</td>
      <td>772.63</td>
      <td>83.274201</td>
      <td>83.989488</td>
      <td>District</td>
      <td>90.93</td>
      <td>93.25</td>
      <td>92.09</td>
      <td>500-1000</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>1635</td>
      <td>1043130</td>
      <td>1800</td>
      <td>579.52</td>
      <td>83.682222</td>
      <td>83.955000</td>
      <td>Charter</td>
      <td>90.28</td>
      <td>93.44</td>
      <td>91.86</td>
      <td>500-1000</td>
    </tr>
  </tbody>
</table>
</div>




```python
spending_math_score = school_summary_table.groupby(["Spending Ranges (Per Student)"]).mean()['Average Math Score']
Spending_reading_score = school_summary_table.groupby(["Spending Ranges (Per Student)"]).mean()['Average Reading Score']
spending_passing_math =  school_summary_table.groupby(["Spending Ranges (Per Student)"]).mean()['% Passing Math']
spending_passing_reading =  school_summary_table.groupby(["Spending Ranges (Per Student)"]).mean()['% Passing Reading']
overall_passing_rate =  (spending_math_score + Spending_reading_score) / 2

spending_per_student = pd.DataFrame({"Average Math Score":spending_math_score, "Average Reading Score":Spending_reading_score,
                              "% Passing Math":spending_passing_math,"% Passing Reading":spending_passing_reading,
                                   "Overall Passing Rate":overall_passing_rate})
spending_per_student
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
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
    <tr>
      <th>Spending Ranges (Per Student)</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;500</th>
      <td>76.993025</td>
      <td>80.967495</td>
      <td>64.21</td>
      <td>78.388</td>
      <td>78.980260</td>
    </tr>
    <tr>
      <th>500-1000</th>
      <td>83.536960</td>
      <td>83.951486</td>
      <td>90.65</td>
      <td>93.070</td>
      <td>83.744223</td>
    </tr>
    <tr>
      <th>1000-1500</th>
      <td>80.038339</td>
      <td>82.407621</td>
      <td>77.13</td>
      <td>85.700</td>
      <td>81.222980</td>
    </tr>
    <tr>
      <th>1500-2000</th>
      <td>83.418349</td>
      <td>83.848930</td>
      <td>90.21</td>
      <td>92.910</td>
      <td>83.633639</td>
    </tr>
  </tbody>
</table>
</div>




```python
size_range=[0,1000, 2000, 3000, 4000, 5000]
size_ranges= ["<1000","1000-2000","2000-3000","3000-4000","4000-5000" ]
school_size= school_summary_table["size"].tolist()
school_size
```




    [2917,
     2949,
     1761,
     4635,
     1468,
     2283,
     1858,
     4976,
     427,
     962,
     1800,
     3999,
     4761,
     2739,
     1635]




```python
school_summary_table["School Size"]= pd.cut(school_size, size_range, labels=size_ranges)
school_summary_table
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
      <th>size</th>
      <th>budget($)</th>
      <th>total students</th>
      <th>Budget Per Student ($)</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>type</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
      <th>Spending Ranges (Per Student)</th>
      <th>School Size</th>
    </tr>
    <tr>
      <th>school</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Huang High School</th>
      <td>2917</td>
      <td>1910635</td>
      <td>4976</td>
      <td>383.97</td>
      <td>77.048432</td>
      <td>81.033963</td>
      <td>District</td>
      <td>64.63</td>
      <td>79.30</td>
      <td>71.96</td>
      <td>&lt;500</td>
      <td>2000-3000</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>2949</td>
      <td>1884411</td>
      <td>1858</td>
      <td>1014.21</td>
      <td>83.061895</td>
      <td>83.975780</td>
      <td>District</td>
      <td>89.56</td>
      <td>93.86</td>
      <td>91.71</td>
      <td>1000-1500</td>
      <td>2000-3000</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>1761</td>
      <td>1056600</td>
      <td>2949</td>
      <td>358.29</td>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>Charter</td>
      <td>63.75</td>
      <td>78.43</td>
      <td>71.09</td>
      <td>&lt;500</td>
      <td>1000-2000</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>4635</td>
      <td>3022020</td>
      <td>2739</td>
      <td>1103.33</td>
      <td>77.102592</td>
      <td>80.746258</td>
      <td>District</td>
      <td>65.75</td>
      <td>77.51</td>
      <td>71.63</td>
      <td>1000-1500</td>
      <td>4000-5000</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>1468</td>
      <td>917500</td>
      <td>1468</td>
      <td>625.00</td>
      <td>83.351499</td>
      <td>83.816757</td>
      <td>Charter</td>
      <td>89.71</td>
      <td>93.39</td>
      <td>91.55</td>
      <td>500-1000</td>
      <td>1000-2000</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>2283</td>
      <td>1319574</td>
      <td>4635</td>
      <td>284.70</td>
      <td>77.289752</td>
      <td>80.934412</td>
      <td>Charter</td>
      <td>64.75</td>
      <td>78.19</td>
      <td>71.47</td>
      <td>&lt;500</td>
      <td>2000-3000</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>1858</td>
      <td>1081356</td>
      <td>427</td>
      <td>2532.45</td>
      <td>83.803279</td>
      <td>83.814988</td>
      <td>Charter</td>
      <td>90.63</td>
      <td>92.74</td>
      <td>91.68</td>
      <td>NaN</td>
      <td>1000-2000</td>
    </tr>
    <tr>
      <th>Bailey High School</th>
      <td>4976</td>
      <td>3124928</td>
      <td>2917</td>
      <td>1071.28</td>
      <td>76.629414</td>
      <td>81.182722</td>
      <td>District</td>
      <td>63.32</td>
      <td>78.81</td>
      <td>71.06</td>
      <td>1000-1500</td>
      <td>4000-5000</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>427</td>
      <td>248087</td>
      <td>4761</td>
      <td>52.11</td>
      <td>77.072464</td>
      <td>80.966394</td>
      <td>Charter</td>
      <td>63.85</td>
      <td>78.28</td>
      <td>71.06</td>
      <td>&lt;500</td>
      <td>&lt;1000</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>962</td>
      <td>585858</td>
      <td>962</td>
      <td>609.00</td>
      <td>83.839917</td>
      <td>84.044699</td>
      <td>Charter</td>
      <td>91.68</td>
      <td>92.20</td>
      <td>91.94</td>
      <td>500-1000</td>
      <td>&lt;1000</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>1800</td>
      <td>1049400</td>
      <td>3999</td>
      <td>262.42</td>
      <td>76.842711</td>
      <td>80.744686</td>
      <td>Charter</td>
      <td>64.07</td>
      <td>77.74</td>
      <td>70.90</td>
      <td>&lt;500</td>
      <td>1000-2000</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>3999</td>
      <td>2547363</td>
      <td>1761</td>
      <td>1446.54</td>
      <td>83.359455</td>
      <td>83.725724</td>
      <td>District</td>
      <td>89.89</td>
      <td>92.62</td>
      <td>91.26</td>
      <td>1000-1500</td>
      <td>3000-4000</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>4761</td>
      <td>3094650</td>
      <td>1635</td>
      <td>1892.75</td>
      <td>83.418349</td>
      <td>83.848930</td>
      <td>District</td>
      <td>90.21</td>
      <td>92.91</td>
      <td>91.56</td>
      <td>1500-2000</td>
      <td>4000-5000</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>2739</td>
      <td>1763916</td>
      <td>2283</td>
      <td>772.63</td>
      <td>83.274201</td>
      <td>83.989488</td>
      <td>District</td>
      <td>90.93</td>
      <td>93.25</td>
      <td>92.09</td>
      <td>500-1000</td>
      <td>2000-3000</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>1635</td>
      <td>1043130</td>
      <td>1800</td>
      <td>579.52</td>
      <td>83.682222</td>
      <td>83.955000</td>
      <td>Charter</td>
      <td>90.28</td>
      <td>93.44</td>
      <td>91.86</td>
      <td>500-1000</td>
      <td>1000-2000</td>
    </tr>
  </tbody>
</table>
</div>




```python
size_math_score = school_summary_table.groupby(["School Size"]).mean()['Average Math Score']
size_reading_score = school_summary_table.groupby(["School Size"]).mean()['Average Reading Score']
size_passing_math =  school_summary_table.groupby(["School Size"]).mean()['% Passing Math']
size_passing_reading =  school_summary_table.groupby(["School Size"]).mean()['% Passing Reading']
size_overall_passing_rate =  (size_math_score + size_reading_score) / 2

size_per_school = pd.DataFrame({"Average Math Score":size_math_score, "Average Reading Score":size_reading_score,
                              "% Passing Math":size_passing_math,"% Passing Reading":size_passing_reading,
                                   "Overall Passing Rate":size_overall_passing_rate})
size_per_school
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
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
    <tr>
      <th>School Size</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;1000</th>
      <td>80.456190</td>
      <td>82.505546</td>
      <td>77.765000</td>
      <td>85.240000</td>
      <td>81.480868</td>
    </tr>
    <tr>
      <th>1000-2000</th>
      <td>80.878295</td>
      <td>82.697890</td>
      <td>79.688000</td>
      <td>87.148000</td>
      <td>81.788093</td>
    </tr>
    <tr>
      <th>2000-3000</th>
      <td>80.168570</td>
      <td>82.483411</td>
      <td>77.467500</td>
      <td>86.150000</td>
      <td>81.325990</td>
    </tr>
    <tr>
      <th>3000-4000</th>
      <td>83.359455</td>
      <td>83.725724</td>
      <td>89.890000</td>
      <td>92.620000</td>
      <td>83.542589</td>
    </tr>
    <tr>
      <th>4000-5000</th>
      <td>79.050118</td>
      <td>81.925970</td>
      <td>73.093333</td>
      <td>83.076667</td>
      <td>80.488044</td>
    </tr>
  </tbody>
</table>
</div>




```python
type_math_score = school_summary_table.groupby(["type"]).mean()['Average Math Score']
type_reading_score = school_summary_table.groupby(["type"]).mean()['Average Reading Score']
type_passing_math =  school_summary_table.groupby(["type"]).mean()['% Passing Math']
type_passing_reading =  school_summary_table.groupby(["type"]).mean()['% Passing Reading']
type_overall_passing_rate =  (type_math_score + type_reading_score) / 2

type_per_school = pd.DataFrame({"Average Math Score":type_math_score, "Average Reading Score":type_reading_score,
                              "% Passing Math":type_passing_math,"% Passing Reading":type_passing_reading,
                                   "Overall Passing Rate":type_overall_passing_rate})
type_per_school
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
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>Overall Passing Rate</th>
    </tr>
    <tr>
      <th>type</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Charter</th>
      <td>80.324201</td>
      <td>82.429369</td>
      <td>77.340000</td>
      <td>85.551250</td>
      <td>81.376785</td>
    </tr>
    <tr>
      <th>District</th>
      <td>80.556334</td>
      <td>82.643266</td>
      <td>79.184286</td>
      <td>86.894286</td>
      <td>81.599800</td>
    </tr>
  </tbody>
</table>
</div>


