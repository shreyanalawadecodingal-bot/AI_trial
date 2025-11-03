from sklearn.datasets import fetch_openml
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt

mnist = fetch_openml('mnist_784', version=1)
X = mnist['data'] / 255.0
y = mnist['target'].astype(int)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=10000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = metrics.accuracy_score(y_test, y_pred)
print(f"Test accuracy: {accuracy}")

for i in range(5):
    plt.imshow(X_test.iloc[i].values.reshape(28, 28), cmap=plt.cm.binary)
    plt.title(f"Predicted: {y_pred[i]}, Actual: {y_test.iloc[i]}")
    plt.show()


import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns

def introduction_to_ml():
    print("=== Step 1: Loading Digit Dataset ===")
    digits = load_digits()
    X, y = digits.data, digits.target
    print(f"Total number of samples: {len(X)}")
    print(f"Image shape: {digits.images[0].shape}")
    print(f"Number of classes: {len(np.unique(y))}")
    print("\n=== Step 2: Visualizing Sample Digits ===")
    plt.figure(figsize=(10, 5))
    for i in range(10):
        plt.subplot(2, 5, i+1)
        plt.imshow(digits.images[i], cmap='gray')
        plt.title(f'Digit: {digits.target[i]}')
        plt.axis('off')
    plt.tight_layout()
    plt.savefig('sample_digits.png')
    plt.close()
    print("\n=== Step 3: Preparing Data ===")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    print("\n=== Step 4: Training Neural Network ===")
    mlp = MLPClassifier(hidden_layer_sizes=(100, 50), max_iter=500, activation='relu', solver='adam', random_state=42)
    mlp.fit(X_train_scaled, y_train)
    print("\n=== Step 5: Model Evaluation ===")
    y_pred = mlp.predict(X_test_scaled)
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    plt.figure(figsize=(10, 8))
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title('Confusion Matrix')
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.tight_layout()
    plt.savefig('confusion_matrix.png')
    plt.close()
    print("\n=== Step 6: Visualizing Predictions ===")
    plt.figure(figsize=(12, 6))
    for i in range(10):
        plt.subplot(2, 5, i+1)
        plt.imshow(X_test.reshape(-1, 8, 8)[i], cmap='gray')
        plt.title(f'True: {y_test[i]}, Pred: {y_pred[i]}')
        plt.axis('off')
    plt.tight_layout()
    plt.savefig('predictions.png')
    plt.close()
    accuracy = mlp.score(X_test_scaled, y_test)
    print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

def main():
    print("Machine Learning Project: Digit Recognition")
    introduction_to_ml()

if __name__ == "__main__":
    main()
