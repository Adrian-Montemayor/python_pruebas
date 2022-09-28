import matplotlib.pyplot as plt
import pandas as pd

#importing the dataset
dataset = pd.read_csv('ProblemaRegresion.csv')
user_input = int(input("Seleccione la máquina a probar (1-33)>"))
X = dataset.iloc[:, user_input:user_input+1].values
y =  dataset.iloc[:, 0].values

#splitting the dataset into the training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

#Training the linear regression model on the training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title(f'Process duration by machine {user_input} (training set)')
plt.xlabel(f'machin {user_input}')
plt.ylabel('Minutes')
plt.show()

plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title(f'Process duration by machine {user_input} (Test set)')
plt.xlabel(f'machin {user_input}')
plt.ylabel('Minutes')
plt.show()

#predicted values.
print(y_pred)