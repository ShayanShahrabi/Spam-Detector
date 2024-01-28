## Introduction
A simple **Bayes classifier** is a group of probabilistic classifiers that usually have acceptable accuracy. This method is based on **independent events** and **Bayes theorem**. 

## Project Details
This program is an implementation of the technique mentioned above. So through analyzing SMS data with spam and non-spam labels (which is provided in the `train_data.txt` file), it will predict whether each SMS provided in the `sample_test_data.txt` file is spam or not.


# Simple Naive Bayes Classifier
The Simple Naive Bayes Classifier is a group of classifiers based on probabilities that usually have acceptable accuracy. This method is based on independent events and the Bayes theorem. In this project, we intend to write a program that receives data consisting of spam and non-spam messages, as well as a list of anonymous messages, and determines whether the anonymous messages are spam or not.


The training data consists of two columns separated by a tab character. The first column is the message label, which can have the values "spam" or "ham" (indicating whether the message is spam or not). The second column is the message text. It is guaranteed that the message text does not contain any tab characters.

The test data consists of a single column, which is the message text.

For message classification, we have two categories:

- Spam messages
- Non-spam messages (ham)

The simple Naive Bayes method calculates the probability of a message belonging to each of these categories. Finally, we choose the category with the highest probability as the final category.

If the message text contains n unique words named w1 to wn (repeated words may exist), the probability of the message belonging to the spam category is calculated as follows:

$$ 
P(spam|w_1,w_2,...,w_n) = P(spam) * \prod_{i=1}^{n} P(w_i|spam)
$$

In the above equation:

- $P_{\text{spam}}$ is the number of spam messages in the training data divided by the total number of messages in the training data.
- $P(w_i \mid \text{spam})$ is the probability of word wi appearing in spam messages.

The calculation of $P(w_i \mid \text{spam})$ is as follows:

$$
P(w_i \mid \text{spam}) = \frac{{N(w_i \mid \text{spam}) + \alpha}}{{N(\text{spam}) + (\alpha \times N(\text{vocabulary}))}}
$$

In the above equation:

- $N_{\text{vocabulary}}$ is the total number of unique words in the training data.
- $N_{\text{spam}}$ is the total number of words in spam messages in the training data.
- $N_{w_i|\text{spam}}$ is the number of occurrences of word $w_i$ in spam messages in the training data.
- $\alpha$ is a parameter to prevent the probability from being zero if a word does not exist in the data. Consider its value as $1$.

The above equations hold similarly for the ham category.

## Running the Program

Implement the program in a file named `spam_detector.py`. The program should be executed as follows:

```
python spam_detector.py train_data_filepath test_data_filepath output_filepath
```

The program should read the training and test data from the specified file paths and write the output to the specified file path.

Additionally, the output file format should be similar to the training data.

## Notes

- To clean the words, it is sufficient to remove non-alphabetic characters from the messages using the regular expression `\W+`.
- The scoring criteria are as follows:
  - If the model accuracy is at least 60%, you will receive one-third of the score.
  - If the model accuracy is at least 80%, you will receive two-thirds of the score.
  - If the model accuracy is at least 90%, you will receive the full score.

## Acknowledgemnts
I would like to express my heartfelt appreciation to my friend [Nima HeydariNasab](https://github.com/nimah79?tab=overview&from=2018-12-01&to=2018-12-31) for not only providing invaluable support and expertise but also for sharing the essential data files that were instrumental in the completion of this project.