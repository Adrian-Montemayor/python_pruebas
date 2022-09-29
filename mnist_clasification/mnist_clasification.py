import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_openml
data = fetch_openml("mnist_784", version=1)

x, y = data["data"], data["target"]
print(x.shape)

xtrain, xtest, ytrain, ytest = train_test_split(x, y, 
                                                test_size=0.2,
                                                random_state=42)

image = np.array(xtrain[0]).reshape(28, 28)
plt.imshow(image)


from sklearn.linear_model import SGDClassifier
model = SGDClassifier()
model.fit(xtrain, ytrain)

predictions = model.predict(xtest)
print(predictions)


image = np.array(xtest[0]).reshape(28, 28)
plt.imshow(image)