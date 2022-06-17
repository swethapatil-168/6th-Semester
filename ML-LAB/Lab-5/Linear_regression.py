{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "b6e5ac70",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import pandas as pd\n",
    "from sklearn.model_selection import train_test_split \n",
    "from sklearn.linear_model import LinearRegression\n",
    "from sklearn.metrics import accuracy_score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "446c3298",
   "metadata": {},
   "outputs": [],
   "source": [
    "dataset = pd.read_csv('Salary_Data.csv')\n",
    "X = dataset.iloc[:, :-1].values\n",
    "y = dataset.iloc[:, 1].values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "7cb9a491",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Intercept: 26816.19224403119\n",
      "Coefficient: [9345.94244312]\n"
     ]
    }
   ],
   "source": [
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=0)\n",
    "regressor = LinearRegression()\n",
    "regressor.fit(X_train, y_train)\n",
    "print('Intercept:',regressor.intercept_)\n",
    "print('Coefficient:',regressor.coef_)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "19b3d77b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "y_pred = regressor.predict(X_test)\n",
    "viz_train = plt\n",
    "viz_train.scatter(X_train, y_train, color='red')\n",
    "viz_train.plot(X_train, regressor.predict(X_train), color='blue')\n",
    "viz_train.title('Salary VS Experience (Training set)')\n",
    "viz_train.xlabel('Year of Experience')\n",
    "viz_train.ylabel('Salary')\n",
    "viz_train.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "83ea9de1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "viz_test = plt\n",
    "viz_test.scatter(X_test, y_test, color='red')\n",
    "viz_test.plot(X_train, regressor.predict(X_train), color='blue')\n",
    "viz_test.title('Salary VS Experience (Test set)')\n",
    "viz_test.xlabel('Year of Experience')\n",
    "viz_test.ylabel('Salary')\n",
    "viz_test.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "f26af94a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Actual</th>\n",
       "      <th>Predicted</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>37731.0</td>\n",
       "      <td>40835.105909</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>122391.0</td>\n",
       "      <td>123079.399408</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>57081.0</td>\n",
       "      <td>65134.556261</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>63218.0</td>\n",
       "      <td>63265.367772</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>116969.0</td>\n",
       "      <td>115602.645454</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>109431.0</td>\n",
       "      <td>108125.891499</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>112635.0</td>\n",
       "      <td>116537.239698</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>55794.0</td>\n",
       "      <td>64199.962017</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>83088.0</td>\n",
       "      <td>76349.687193</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>101302.0</td>\n",
       "      <td>100649.137545</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Actual      Predicted\n",
       "0   37731.0   40835.105909\n",
       "1  122391.0  123079.399408\n",
       "2   57081.0   65134.556261\n",
       "3   63218.0   63265.367772\n",
       "4  116969.0  115602.645454\n",
       "5  109431.0  108125.891499\n",
       "6  112635.0  116537.239698\n",
       "7   55794.0   64199.962017\n",
       "8   83088.0   76349.687193\n",
       "9  101302.0  100649.137545"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df=pd.DataFrame({'Actual':y_test,'Predicted':y_pred})\n",
    "df"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
