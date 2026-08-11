## tiré de geeks for geeks https://www.geeksforgeeks.org/machine-learning/comprehensive-guide-to-classification-models-in-scikit-learn/
from sklearn.linear_model import LogisticRegression, LinearRegression, Ridge
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_wine, load_iris, load_breast_cancer, fetch_california_housing, load_diabetes
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.metrics import accuracy_score, classification_report, mean_squared_error
from .convert_datasets import nncr_information_compression_transformation, nncr_create_dict
import matplotlib.pyplot as plt
import numpy as np
def classificationTest():
    X, y = load_wine(return_X_y=True)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=47)

    print('Creating dictionnary...')
    compress_transform_dict = nncr_create_dict(X_train)
    print('Transforming training X...')
    X1_train = nncr_information_compression_transformation(X_train, compress_transform_dict)
    print('Transforming testing X...')
    X1_test = nncr_information_compression_transformation(X_test, compress_transform_dict)

    print('Running...')
    # Classification par régression logistique
    model = LogisticRegression(max_iter=10000)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    print("Classical Accuracy Logistic Regression:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))

    model.fit(X1_train, y_train)

    y_pred = model.predict(X1_test)

    print("Compressed Accuracy Logistic Regression:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))


def regression_test():
    california = 'California housing'
    diabetes = 'Diabetes'
    models = [('Linear Regression',LinearRegression()), ('Ridge regression lambda=0.5',Ridge(alpha=0.5)), ('KNN Regression',KNeighborsRegressor(n_neighbors=5))]
    for model_name,model in models:
        for name, tolerances, fetch in [(california, [1e4,1e1,1e6,1e6,1e1,1e6,1e2,1e2],fetch_california_housing), (diabetes,1e2,load_diabetes)]:
            print('Dataset:', name)
            X ,y = fetch(return_X_y=True)
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=50)
            # Default model

            model.fit(X_train,y_train)
            y_pred = model.predict(X_test)
            print(model_name, 'Default MSE:', mean_squared_error(y_test, y_pred))

            # pre-process X for california to have all values > 0
            if name == california:
                X[:,-1] *= -1
            elif name == diabetes:
                for i in range(X.shape[1]):# foreach column
                    minimum = min(X[:,i])
                    if minimum < 0:
                        X[:,i] -= minimum - 1e-2            
            tolerance=1
            if 'float' in str(type(tolerances)):
                tolerance = tolerances
                tolerances = None
            compress_dict = nncr_create_dict(X,tolerance=tolerance,tolerances=tolerances)
            X1_train = nncr_information_compression_transformation(X_train, compress_dict, tolerance=tolerance,tolerances=tolerances)
            X1_test = nncr_information_compression_transformation(X_test, compress_dict, tolerance=tolerance,tolerances=tolerances)
            # Compress Model
            model.fit(X1_train, y_train)
            y1_pred = model.predict(X1_test)
            print(model_name, 'Compress MSE:', mean_squared_error(y_test,y1_pred))

def custom_regression_test():
    np.random.seed(12)
    num = 75
    max_val = 100
    noise_val = 25
    noise = np.random.rand(num,1) * noise_val
    X = np.random.rand(num,1) * max_val #np.linspace(0,100,num=num,endpoint=True)
    b = 5
    m = 2
    y = np.array([((X[i]-30.0)**2)/-35.0 + X[i] + noise[i] for i in range(len(X))])#np.array([X[i]*m + b + noise[i] for i in range(len(X))])
    plt.scatter(X,y, label='y_true')

    model = LinearRegression()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=50)
    model.fit(X_train,y_train)

    pred_x_plot = np.array([[i] for i in range(1,max_val)])

    y_pred = model.predict(pred_x_plot)
    plt.plot(pred_x_plot,y_pred, color='orange', label='pred_reg')

    compress_dict = nncr_create_dict(X_train)
    X1_train = nncr_information_compression_transformation(X_train,compress_dict)
    pred_x1_plot = nncr_information_compression_transformation(pred_x_plot,compress_dict)
    model.fit(X1_train,y_train)
    y1_pred = model.predict(pred_x1_plot)
    plt.plot(pred_x_plot,y1_pred, color='red', label='pred_comp_reg')



    plt.legend(loc='best')
    plt.show()

#regression_test()
custom_regression_test()