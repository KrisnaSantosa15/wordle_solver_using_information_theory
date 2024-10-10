# 🧩 Wordle Solver Using Information Theory

![Source: https://word.tips](https://word.tips/api/v1/prismic-images/f2952532-27dc-425f-b0aa-df226f5a5bb5_wordle-answers-main.jpg)

## 🎯 Problem Statement

Wordle is a word puzzle game where players guess a five-letter word within six attempts. After each guess, feedback is given in colored tiles:
- 🟩 Green: Letter is in the word and in the correct position
- 🟨 Yellow: Letter is in the word but in the wrong position
- ⬛ Gray: Letter is not in the word

This project aims to develop a Wordle solver using information theory, generating the next guess based on player feedback.

Inspired by 3Blue1Brown's video on [Solve Wordle using Information Theory](https://www.youtube.com/watch?v=v68zYyaEmEA).

[![Solve Wordle using Information Theory](https://img.youtube.com/vi/v68zYyaEmEA/0.jpg)](https://www.youtube.com/watch?v=v68zYyaEmEA)

## 🧠 Approach

![Wordle Solver Using Information Theory, source: analyticsvidhya.com](https://cdn.analyticsvidhya.com/wp-content/uploads/2024/09/InformationEntropyForaBernoullitrialX01thegraphofentropyvs.-1.webp)

Our Wordle solver uses a probabilistic approach:
1. Maintain a list of possible words based on feedback
2. Calculate the probability of each letter appearing in each position
3. Generate the next guess by selecting the word with the highest probability of being correct

## 💻 Implementation

The solver is implemented in Python with these steps:
1. Load a list of five-letter words from a dictionary file
2. Initialize possible words based on player feedback
3. Calculate letter probabilities for each position
4. Generate the next guess using highest probability word

![Implementation](image.png)

Tile colors are represented as:
- Green: G
- Yellow: Y
- Gray: B (Black)

## ⚠️ Limitation

The solver is limited by:
- Dictionary file size
- Word puzzle complexity
- Ambiguous or inconsistent feedback

Currently, the opening word is static ("AUDIO"). Future improvements include:
- Dynamic opening word based on highest probability
- Using suggestions like "CRANE" or "SLOTH" (frequently used letters)

## 🚀 Usage

To use the Wordle solver:

1. Clone the repository:
```bash
git clone https://github.com/KrisnaSantosa15/wordle_solver_using_information_theory.git
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the solver:
```bash
python wordle_solver.py
```

4. Enter feedback as `GGYGB` (Green, Green, Yellow, Green, Black)

5. The solver will generate the next guess

## 🎓 Conclusion

This Wordle solver demonstrates the application of information theory in word puzzles, highlighting the importance of probability in decision-making. It provides an efficient and effective way to solve Wordle puzzles using a probabilistic approach.

## 📚 References

1. [Wordle](https://wordly.org/)
2. [Information Theory](https://en.wikipedia.org/wiki/Information_theory)
3. [Probabilistic Methods](https://en.wikipedia.org/wiki/Probabilistic_method)
4. [Python Programming Language](https://www.python.org/)
5. [Dictionary File](https://www.kaggle.com/datasets/bcruise/wordle-valid-words)

---

If you find this project interesting, don't forget to give it a star! ⭐