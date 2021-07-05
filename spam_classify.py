import math
import pandas as pd


def probability(word, category, ham_distribution, spam_distribution, m):
    distribution = ham_distribution if category == 'ham' else spam_distribution

    V = len(distribution)

    keys = distribution.keys()

    numerator = (distribution[word] + m if word in keys else m)
    denominator = sum([distribution[key] for key in keys]) + m * V

    return numerator / float(denominator)


def words(filename):
    return filename.split()


def clean_text(k):
    spam_distribution = {}
    ham_distribution = {}
    spamreader = pd.read_excel(r"C:\Users\charv\spam_classifier\HamandSpam (2).xlsx")
    result = spamreader['Column 1'].tolist()
    text = spamreader['Column 2'].tolist()
    for i in text:
        i = i.lower()
    for i in range(len(result)):
        if result[i] == 'spam':
            list_of_words = words(text[i])

            for word in list_of_words:
                if word in spam_distribution:

                    spam_distribution[word] += 1
                else:
                    spam_distribution[word] = 1

        elif result[i] == 'ham':
            list_of_words = words(text[i])
            for word in list_of_words:
                if word in ham_distribution:
                    ham_distribution[word] += 1
                else:
                    ham_distribution[word] = 1

    hamkeys = ham_distribution.keys()
    spamkeys = spam_distribution.keys()
    spam_distribution2 = {}
    ham_distribution2 = {}

    for key in spamkeys:
        if spam_distribution[key] > k:
            spam_distribution2[key] = spam_distribution[key]

    for key in hamkeys:
        if ham_distribution[key] > k:
            ham_distribution2[key] = ham_distribution[key]

    return ham_distribution2, spam_distribution2


def classify_email(email, ham_distribution, spam_distribution, m):
    email_words = words(email)

    ham_probability = 0
    spam_probability = 0

    for word in email_words:
        ham_probability += math.log(probability(word, 'ham', ham_distribution, spam_distribution, m))
        spam_probability += math.log(probability(word, 'spam', ham_distribution, spam_distribution, m))

    return 'ham' if ham_probability > spam_probability else 'spam'


def test_filter(hamtesting, k, m):
    ham_distribution, spam_distribution = clean_text(k)

    if classify_email(hamtesting, ham_distribution, spam_distribution, m) == 'ham':
        return 'ham'
    else:
        return 'spam'


correct = 1
incorrect = 1
test = pd.read_excel(r"SMSSpamCollection.xlsx")
result = test['Column 1'].tolist()
text = test['Column 2'].tolist()
for i in range(len(text)):
    x = test_filter(text[i], 1, 1)
    if x == result[i]:
        correct += 1
    else:
        incorrect += 1
accuracy = (correct / (incorrect + correct)) * 100

test_string = input("Enter a email (string only): ")
print(test_filter(test_string, 1, 1))
print("Accuracy: ", accuracy)
