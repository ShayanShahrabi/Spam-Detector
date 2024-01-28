# Simple Naive Bayes Classifier
The Simple Naive Bayes Classifier is a group of classifiers based on probabilities that usually have acceptable accuracy. This method is based on independent events and the Bayes theorem. In this project, we intend to write a program that receives data consisting of spam and non-spam messages, as well as a list of anonymous messages, and determines whether the anonymous messages are spam or not.


The training data consists of two columns separated by a tab character. The first column is the message label, which can have the values "spam" or "ham" (indicating whether the message is spam or not). The second column is the message text. It is guaranteed that the message text does not contain any tab characters.

The test data consists of a single column, which is the message text.

For message classification, we have two categories:

- Spam messages
- Non-spam messages (ham)

The simple Naive Bayes method calculates the probability of a message belonging to each of these categories. Finally, we choose the category with the highest probability as the final category.

If the message text contains n unique words named $w_1$ to $w_n$ (repeated words may exist), the probability of the message belonging to the spam category is calculated as follows:

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

## How the Program Works

The program reads the training and test data from the specified file paths and writes the output to the specified file path.

Additionally, the output file format should be similar to the training data.

## Notes
- The scoring criteria were as following:
  - If the model accuracy is at least 60%, the code receives one-third of the score.
  - If the model accuracy is at least 80%, the code receives two-thirds of the score.
  - If the model accuracy is at least 90%, the code receives the full score.

(The implementation in the `main-notebook.ipynb` file avhieved a sacore of 100 / 100)

## How to run the code?
There are 2 files in the repo:
- `main-notebook.ipynb` which contains explanatoins and the code itself
- `spam_detectos.py` which only contains the code (the exact code is used in the jupyter notebook)

So you can run which ever you like, the results are totally the same.

## Acknowledgemnts
I would like to express my heartfelt appreciation to my friend [Nima HeydariNasab](https://github.com/nimah79?tab=overview&from=2018-12-01&to=2018-12-31) for not only providing invaluable support and expertise but also for sharing the essential data files that were instrumental in the completion of this project.