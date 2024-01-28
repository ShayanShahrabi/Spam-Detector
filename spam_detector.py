import math
import re
import sys
from collections import defaultdict
#-----------------------------------------------------------------------------
def train(train_file):
    spam_count = 0
    ham_count = 0
    word_counts_spam = defaultdict(int)
    word_counts_ham = defaultdict(int)
    vocabulary = set()

    with open(train_file, 'r', encoding='utf-8') as file:
        for line in file:
            label, text = line.strip().split('\t')
            words = re.findall(r'\w+', text)
            vocabulary.update(words)

            if label == 'spam':
                spam_count += 1
                for word in words:
                    word_counts_spam[word] += 1
            else:
                ham_count += 1
                for word in words:
                    word_counts_ham[word] += 1

    return spam_count, ham_count, word_counts_spam, word_counts_ham, vocabulary
#-----------------------------------------------------------------------------
def calculate_probability(word, word_counts, total_words, alpha, vocabulary_size):
    word_count = word_counts[word]
    return (word_count + alpha) / (total_words + alpha * vocabulary_size)
#-----------------------------------------------------------------------------
def classify_text(text, spam_count, ham_count, word_counts_spam, word_counts_ham, vocabulary, alpha=1):
    words = re.findall(r'\w+', text)
    vocabulary_size = len(vocabulary)
    spam_probability = spam_count / (spam_count + ham_count)
    ham_probability = ham_count / (spam_count + ham_count)
    spam_log_probability = 0
    ham_log_probability = 0

    for word in words:
        if word in vocabulary:
            spam_log_probability += math.log(calculate_probability(word, word_counts_spam, spam_count, alpha, vocabulary_size))
            ham_log_probability += math.log(calculate_probability(word, word_counts_ham, ham_count, alpha, vocabulary_size))

    spam_log_probability += math.log(spam_probability)
    ham_log_probability += math.log(ham_probability)

    if spam_log_probability > ham_log_probability:
        return 'spam'
    else:
        return 'ham'
#-----------------------------------------------------------------------------
def test(test_file, output_file, spam_count, ham_count, word_counts_spam, word_counts_ham, vocabulary):
    with open(test_file, 'r', encoding='utf-8') as input_file, open(output_file, 'w', encoding='utf-8') as output_file:
        for line in input_file:
            text = line.strip()
            label = classify_text(text, spam_count, ham_count, word_counts_spam, word_counts_ham, vocabulary)
            output_file.write(f'{label}\t{text}\n')

if __name__ == '__main__':
    train_file = "train_data"  # Replace with the actual train file path
    test_file = "sample_test_data"  # Replace with the actual test file path
    output_file = "output_file.txt"  # Replace with the desired output file path

    spam_count, ham_count, word_counts_spam, word_counts_ham, vocabulary = train(train_file)
    test(test_file, output_file, spam_count, ham_count, word_counts_spam, word_counts_ham, vocabulary)
#-----------------------------------------------------------------------------