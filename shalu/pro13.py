class NaiveBayesClassifier:

    def __init__(self, X, y):
        self.X, self.y = X, y
        self.N = len(self.X)

        self.dim = len(self.X[0])
        self.attrs = [[] for _ in range(self.dim)]
        self.output_dom = {}

        self.data = []  # To store every row [Xi, yi]

        for i in range(len(self.X)):
            for j in range(self.dim):
                if not self.X[i][j] in self.attrs[j]:
                    self.attrs[j].append(self.X[i][j])

            if not self.y[i] in self.output_dom.keys():
                self.output_dom[self.y[i]] = 1
            else:
                self.output_dom[self.y[i]] += 1
            self.data.append([self.X[i], self.y[i]])

    def classify(self, entry):

        solve = None
        max_arg = -1

        for y in self.output_dom.keys():

            prob = self.output_dom[y] / self.N  # P(y)

            for i in range(self.dim):
                cases = [x for x in self.data if x[0][i] == entry[i] and x[1] == y]
                n = len(cases)
                prob *= n / self.N  # P *= P(Xi = xi)
            if prob > max_arg:
                max_arg = prob
                solve = y

        return solve


import pandas as pd

data = pd.read_csv('titanic.csv')

print(data.head())

y = list(map(lambda v: 'yes' if v == 1 else 'no', data['Survived'].values))  # target values as string

# We won't use the 'Name' nor the 'Fare' field

X = data[['Pclass', 'Sex', 'Age', 'Siblings/Spouses Aboard', 'Parents/Children Aboard']].values

print(len(y))

y_train = y[:600]
y_val = y[600:]

X_train = X[:600]
X_val = X[600:]

# Creating the Naive Bayes Classifier instance with the training data

nbc = NaiveBayesClassifier(X_train, y_train)

total_cases = len(y_val)  # size of validation set

# Well classified examples and bad classified examples
good = 0
bad = 0

for i in range(total_cases):
    predict = nbc.classify(X_val[i])
    if y_val[i] == predict:
        good += 1
    else:
        bad += 1

print('TOTAL EXAMPLES:', total_cases)
print('RIGHT:', good)
print('WRONG:', bad)
print('ACCURACY:', good / total_cases)



