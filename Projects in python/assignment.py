import string
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Function to read a text file
def read_file(filename):  # <-- Fixed parameter name
    with open(filename, 'r') as file:
        return file.read()

# Function to preprocess text (remove punctuation, convert to lowercase, and split into words)
def preprocess_text(text):
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Convert to lowercase and split into words
    words = text.lower().split()
    return words

# Function to remove stopwords
def remove_stopwords(words, stopwords):
    return [word for word in words if word not in stopwords]

# Function to count word frequencies
def count_word_frequencies(words):
    return Counter(words)

# Function to write word frequencies to an output file
def write_output(word_count, output_file, sort_by_frequency=True, top_n=None):
    if sort_by_frequency:
        sorted_word_count = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))
    else:
        sorted_word_count = dict(sorted(word_count.items()))

    if top_n:
        sorted_word_count = dict(list(sorted_word_count.items())[:top_n])

    with open(output_file, 'w') as file:
        for word, count in sorted_word_count.items():
            file.write(f"{word}: {count}\n")

# Function to generate a word cloud
def generate_word_cloud(word_count, output_image="wordcloud.png"):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_count)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.savefig(output_image)
    plt.show()

# Main function
def main():
    # Input and output file names
    input_file = "input.txt"
    output_file = "output.txt"
    stopwords = {'the', 'is', 'and', 'of', 'in', 'to', 'a', 'for', 'with', 'on', 'as', 'by', 'at', 'an', 'be', 'this', 'that', 'it', 'are', 'was', 'were', 'has', 'have', 'had', 'but', 'not', 'or', 'if', 'so', 'you', 'your', 'my', 'i', 'he', 'she', 'we', 'they', 'them', 'his', 'her', 'our', 'their'}

    # Read the input file
    text = read_file(input_file)

    # Preprocess the text
    words = preprocess_text(text)

    # Remove stopwords
    words = remove_stopwords(words, stopwords)

    # Count word frequencies
    word_count = count_word_frequencies(words)

    # Write output to file (sorted by frequency, top 10 words)
    write_output(word_count, output_file, sort_by_frequency=True, top_n=10)

    # Generate a word cloud
    generate_word_cloud(word_count, "wordcloud.png")

    print(f"Word frequencies saved to {output_file}")
    print("Word cloud generated as wordcloud.png")

# Run the program
if __name__ == "__main__":
    main()