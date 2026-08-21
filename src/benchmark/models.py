## tiré de geeks for geeks https://www.geeksforgeeks.org/machine-learning/comprehensive-guide-to-classification-models-in-scikit-learn/
## modifié quand même assez fortement.
from sklearn.linear_model import LogisticRegression, LinearRegression, Ridge
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_wine, load_iris, load_breast_cancer, fetch_california_housing, load_diabetes
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.metrics import accuracy_score, classification_report, mean_squared_error
from .convert_datasets import nncr_information_compression_transformation, nncr_create_dict
import matplotlib.pyplot as plt
import numpy as np
import math

def classification_test():
    X, y = load_wine(return_X_y=True)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=47)

    
    compress_transform_dict = nncr_create_dict(X_train)
    
    X1_train = nncr_information_compression_transformation(X_train, compress_transform_dict)
    
    X1_test = nncr_information_compression_transformation(X_test, compress_transform_dict)

    # Classification par régression logistique
    model = LogisticRegression(max_iter=10000)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    print("Classical Accuracy Logistic Regression:", accuracy_score(y_test, y_pred))
    print('Shape transformation: ',X_train.shape,'->',X1_train.shape)
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
            print('Shape transformation: ',X_train.shape,'->',X1_train.shape)
            print(model_name, 'Compress MSE:', mean_squared_error(y_test,y1_pred))
            print()

def custom_regression_test():
    SEED = 1411
    np.random.seed(SEED)
    num = 1000
    max_val = 150
    noise_val = 5
    x_offset = 12
    noise = np.random.rand(num,1) * noise_val
    X = np.random.rand(num,1) * max_val + x_offset
    b = 5
    m = 10
    quadratic_func = np.array([((X[i]-30.0)**2)/-35.0 + X[i] + noise[i] for i in range(len(X))])
    linear_func = np.array([X[i]*m + b + noise[i] for i in range(len(X))])
    moe_linear_func = np.array([X[i]*m + b + noise[i] if X[i] < 50 else 105 + noise[i] for i in range(len(X))])
    sin_func = np.array([math.sin(X[i] * math.pi / 15)*m + 2*m + noise[i] for i in range(len(X))])
    log_func = np.array([math.log(X[i]) + noise[i] for i in range(len(X))])
    y = sin_func
    

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=SEED)

    plt.scatter(X_train,y_train, label='y_train', c='blue')
    plt.scatter(X_test,y_test, label='y_test', c='orange')

    model = Ridge(alpha=100)#LinearRegression()

    # Default regression prediction
    model.fit(X_train,y_train)
    # whole line prediction
    step_size = 0.5
    pred_x_plot = np.array([[i * step_size] for i in range(int(x_offset / step_size), int((max_val + x_offset) / step_size))])
    y_pred = model.predict(pred_x_plot)
    plt.plot(pred_x_plot,y_pred, color='green', label='pred_reg (train)', alpha=0.5)
    # Dataset MSE
    print('Default MSE train set:', mean_squared_error(y_train,model.predict(X_train)))
    print('Default MSE test set:', mean_squared_error(y_test,model.predict(X_test)))
    

    # Compress regression prediction
    compress_dict = nncr_create_dict(X_train)
    X1_train = nncr_information_compression_transformation(X_train,compress_dict)
    model.fit(X1_train,y_train)
    # whole line prediction
    pred_x1_plot = nncr_information_compression_transformation(pred_x_plot,compress_dict)
    y1_pred = model.predict(pred_x1_plot)
    plt.plot(pred_x_plot,y1_pred, color='red', label='pred_comp_reg (train)', alpha=0.5)

    # Dataset MSE
    X1_test = nncr_information_compression_transformation(X_test, compress_dict)
    print('Shape transformation: ',X_train.shape,'->',X1_train.shape)
    print('Compress MSE train set:', mean_squared_error(y_train,model.predict(X1_train)))
    print('Compress MSE test set:', mean_squared_error(y_test,model.predict(X1_test)))



    plt.legend(loc='best')
    plt.show()