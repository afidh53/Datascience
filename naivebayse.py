from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 1. Load the Iris dataset
iris = load_iris()

# 2. Separate features and target
X = iris.data
y = iris.target

# 3. Split the dataset into training and testing sets
# 80% training and 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# 4. Create the Gaussian Naive Bayes classifier
model = GaussianNB()

# 5. Train the model
model.fit(X_train, y_train)

# 6. Predict the classes of test data
y_pred = model.predict(X_test)

# 7. Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

# 8. Display confusion matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# 9. Display classification report
print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        target_names=iris.target_names
    )
)
