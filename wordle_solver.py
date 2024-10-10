import numpy as np
from collections import Counter
import pandas as pd

# Load word list
words = pd.read_csv('valid_solutions.csv', header=None)[0].tolist()

# Convert words to numpy array for efficient computation
words_array = np.array(words)

def generate_pattern(guess, solution):
    pattern = []
    for g, s in zip(guess, solution):
        if g == s:
            pattern.append('G')  # Green
        elif g in solution:
            pattern.append('Y')  # Yellow
        else:
            pattern.append('B')  # Black/Gray
    return ''.join(pattern)

def calculate_entropy(word, words_list):
    feedback_patterns = Counter()
    n = len(words_list)
    
    for possible_word in words_list:
        pattern = generate_pattern(word, possible_word)
        feedback_patterns[pattern] += 1

    entropy = 0
    for pattern, count in feedback_patterns.items():
        p = count / n
        entropy -= p * np.log2(p)
    
    return entropy, feedback_patterns

def find_best_guess(words_list):
    max_entropy = -1
    best_guess = None
    best_feedback_patterns = None
    
    for word in words_list:
        entropy, feedback_patterns = calculate_entropy(word, words_list)
        if entropy > max_entropy:
            max_entropy = entropy
            best_guess = word
            best_feedback_patterns = feedback_patterns
    
    return best_guess, max_entropy, best_feedback_patterns

def show_entropies_and_probabilities(words_list):
    print(f"{'Word':<10} {'Entropy':<10} {'Pattern':<10} {'Count':<10} {'Probability':<10}")
    print("-" * 50)
    
    for word in words_list:
        entropy, feedback_patterns = calculate_entropy(word, words_list)
        for pattern, count in feedback_patterns.items():
            probability = count / len(words_list)
            print(f"{word:<10} {entropy:<10.4f} {pattern:<10} {count:<10} {probability:<10.4f}")

def filter_words(words_list, guess, pattern):
    return [word for word in words_list if generate_pattern(guess, word) == pattern]

def save_word_to_csv(word, filepath='my_wordlists.csv'):
    df = pd.DataFrame([word])
    df.to_csv(filepath, mode='a', header=False, index=False)

def wordle_solver_with_audio(words_list, max_attempts=6):
    attempts = 0
    remaining_words = words_list
    
    # First guess is set to "audio"
    first_guess = "audio"
    attempts += 1
    print(f"Attempt {attempts}: {first_guess}")
    
    # Simulate feedback for the first guess
    pattern = input(f"Enter feedback pattern for '{first_guess}' (G=Green, Y=Yellow, B=Black): ").strip().upper()
    
    if pattern == 'GGGGG':  # All green, word is found
        print(f"Word found: {first_guess}")
        save_word_to_csv(first_guess)  # Save to my_wordlists.csv
        return first_guess
    
    # Filter words based on feedback
    remaining_words = filter_words(remaining_words, first_guess, pattern)
    
    # Continue with the remaining attempts
    while attempts < max_attempts and len(remaining_words) > 1:
        attempts += 1
        show_entropies_and_probabilities(remaining_words)
        guess, entropy, feedback_patterns = find_best_guess(remaining_words)
        print(f"Attempt {attempts}: {guess} (Entropy: {entropy:.4f})")
        
        print("Probabilities for each feedback pattern:")
        for pattern, count in feedback_patterns.items():
            probability = count / len(remaining_words)
            print(f"Pattern: {pattern}, Count: {count}, Probability: {probability:.4f}")
        
        pattern = input(f"Enter feedback pattern for '{guess}' (G=Green, Y=Yellow, B=Black): ").strip().upper()
        
        if pattern == 'GGGGG':
            print(f"Word found: {guess}")
            save_word_to_csv(guess)  # Save to my_wordlists.csv
            return guess
        
        remaining_words = filter_words(remaining_words, guess, pattern)
    
    if len(remaining_words) == 1:
        print(f"Word found: {remaining_words[0]}")
        save_word_to_csv(remaining_words[0])  # Save to my_wordlists.csv
        return remaining_words[0]
    else:
        print("No solution found.")
        new_word = input("Please enter the correct word: ").strip().lower()
        save_word_to_csv(new_word)  # Save user input to my_wordlists.csv
        return None

# Usage
wordle_solver_with_audio(words_array)
