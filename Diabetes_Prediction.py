import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../Diabetes Prediction/diabetes.csv")

df2 = df[(df['Glucose']>0) & (df['BloodPressure']>0) & (df['SkinThickness']>0) & (df['Insulin']>0) & (df['BMI']>0)]

class_0 = df2[df2['Outcome'] == 0]
class_1 = df2[df2['Outcome'] == 1]

class_count_0, class_count_1 = df2['Outcome'].value_counts()
class_1_over = class_1.sample(class_count_0, replace=True)
test_over = pd.concat([class_1_over, class_0], axis=0)

X = test_over.iloc[:,0:8].values
y = test_over.iloc[:, -1].values

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)


#Decision Tree
from sklearn.tree import DecisionTreeClassifier

classifier = DecisionTreeClassifier(criterion = 'gini',max_depth=7, random_state = 0)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)
print(cm)

plt.matshow(cm)
plt.title('Confusion matrix of the classifier\n')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.colorbar()
plt.show()

from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))

import graphviz
from sklearn import tree
dot_data = tree.export_graphviz(classifier, out_file=None)  
graph = graphviz.Source(dot_data)
graph.render("diabetes")

#Random Forest
X_train1, X_test1, y_train1, y_test1 = train_test_split(X, y, test_size = 0.25, random_state = 0)

from sklearn.ensemble import RandomForestClassifier

classifier1 = RandomForestClassifier(n_estimators = 10, criterion = 'gini',max_depth = 20 ,random_state = 0)
classifier1.fit(X_train1, y_train1)

y_pred1 = classifier1.predict(X_test1)

cm1 = confusion_matrix(y_test1, y_pred1)
print(cm1)

plt.matshow(cm1)
plt.title('Confusion matrix of the classifier\n')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.colorbar()
plt.show()

print(classification_report(y_test1,y_pred1))

import pickle

pickle.dump(classifier1,open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))

result=model.predict(([[1,114,66,36,200,38.1,0.289,21]]))
print(result)

if result[0][0] < 0.5 :
  prediction="Good News! You do not have diabetes!"
else :
  prediction="There is a high chance you might have diabetes."
print(prediction)