import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt

# Reads the csv file containing the data
data= pd.read_csv("exams.csv")
data.head()
data.tail()
data.info()
data.isnull().sum()
data.columns
#Name columns that are in the csv file
data=data.rename(columns={"race/ethnicity":"race_ethnicity","parental level of education":"Parent Level Education"
,"test preparation course":"test_preparation_course","math score":"math_score","reading score":"reading_score","writing score":"writing_score"})

# Function to create bar graphs
def bar_graph_plot(variable):
    var = data[variable]
    varCount = var.value_counts()

    plt.figure(figsize =(8,6))
    plt.bar(varCount.index, varCount)
    plt.xticks(varCount.index, varCount.index.values,rotation=45)
    plt.ylabel("Number of Students")
    plt.title(variable)
    plt.show()
    print("{}: \n {}".format(variable,varCount))

# Shows graphs containing basic info on education of student's parents and whether they completed the prep for exam
category = ["Parent Level Education","test_preparation_course"]
for i in category: 
    bar_graph_plot(i)

# Graph to show if completing the test prep helped student score higher
sns.catplot(data=data,x="test_preparation_course",y="math_score",kind="bar")
plt.show()

#Compares education of parents with math score of students to see if having degree seeking parents had an effect on their grades
y=data[["Parent Level Education","math_score","reading_score","writing_score"]].groupby(["Parent Level Education"]).mean().sort_values(by="math_score",ascending = False)
sns.catplot(x="Parent Level Education",y="math_score",data=data, kind="bar")
plt.xticks(rotation=90)
plt.show()