import re
from collections import Counter


# Define a list of common words to ignore
common_words = {"A", "AND", "AN", "OF", "IN", "THE"}

def clean_text(text):
    # Convert to uppercase and remove non-alphanumeric characters
    text = text.upper()
    text = re.sub(r'[^A-Z0-9\s]', '', text)
    return text

def get_top_words(file_path):
    # Read and clean the text file
    with open(file_path, 'r') as file:
        text = file.read()
    cleaned_text = clean_text(text)
    
    # Split text into words and filter out common words
    words = [word for word in cleaned_text.split() if word not in common_words]
    
    # Count the frequency of each word
    word_counts = Counter(words)
    
    # Get the 15 most common words
    top_words = [word for word, count in word_counts.most_common(15)]
    return top_words

def calculate_similarity(words1, words2):
    # Calculate the number of common words between two lists
    return len(set(words1) & set(words2))

# List of text files
file_paths = [
    "c:\\Users\\manas\\OneDrive\\Desktop\\5th Sem\\Softwarelab 6 assignment\\book1.txt",
    "c:\\Users\\manas\\OneDrive\\Desktop\\5th Sem\\Softwarelab 6 assignment\\book2.txt",
    "c:\\Users\\manas\\OneDrive\\Desktop\\5th Sem\\Softwarelab 6 assignment\\book3.txt",
    "c:\\Users\\manas\\OneDrive\\Desktop\\5th Sem\\Softwarelab 6 assignment\\book4.txt",
    "c:\\Users\\manas\\OneDrive\\Desktop\\5th Sem\\Softwarelab 6 assignment\\book5.txt"
]


# Get the top words for each file
top_words_per_file = {file: get_top_words(file) for file in file_paths}

# Compare each pair of files
most_similar_pair = None
max_common_words = 0

for i in range(len(file_paths)):
    for j in range(i + 1, len(file_paths)):
        file1, file2 = file_paths[i], file_paths[j]
        common_word_count = calculate_similarity(top_words_per_file[file1], top_words_per_file[file2])
        
        if common_word_count > max_common_words:
            max_common_words = common_word_count
            most_similar_pair = (file1, file2)

# Output the result
print("Most similar pair:", most_similar_pair)
print("Number of common top words:", max_common_words)
