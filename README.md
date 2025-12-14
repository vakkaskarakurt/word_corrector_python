# Turkish Spell Checker - Türkçe Yazım Denetleyici

> Python-based Turkish spell checking tool using multiple distance algorithms and Word2Vec embeddings

🎓 **Academic Project** | Aydın Adnan Menderes University  
📄 **Research Publication:** [The Role of Phonological Errors in Evaluation Metrics](https://dergipark.org.tr/en/pub/bbd/issue/80462/1350547)  
📊 **Achieved Accuracy:** 99.2% on benchmark dataset

---

## 🎯 Overview

This project implements a Turkish spell checker that combines multiple string distance algorithms with semantic analysis to achieve high accuracy in detecting and correcting spelling errors.

### Key Features

- ✅ **Multiple Distance Algorithms**
  - Damerau-Levenshtein (handles transpositions)
  - Jaro distance (phonetic similarity)
  - Keyboard distance (QWERTY layout-aware)
- ✅ **Semantic Analysis** using Word2Vec Turkish model
- ✅ **Combined Scoring** for best candidate selection
- ✅ **99.2% Benchmark Accuracy**

---

## 📁 Project Structure
```
word_corrector_python/
├── main.py                 # Main entry point
├── damerau_low.py         # Damerau-Levenshtein algorithm
├── jaro.py                # Jaro distance calculation
├── letter_distance.py     # Keyboard distance (QWERTY)
├── word2vec_tr.py         # Word2Vec Turkish model handler
├── combine.py             # Algorithm combination logic
├── string_correct.py      # String correction utilities
├── word2correct.py        # Word correction engine
├── file_operations.py     # File I/O operations
├── clear_words.txt        # Clean word dictionary
└── first_250k.txt         # Training dataset (250K words)
```

---

## 🚀 Installation

### Prerequisites

- Python 3.x
- Required libraries (see below)

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/vakkaskarakurt/word_corrector_python.git
cd word_corrector_python
```

2. **Download Word2Vec model**

The Word2Vec model files are hosted separately due to file size:
- Download from: https://drive.google.com/file/d/1ljwPcaBUUPARyRDxWjaxJJFWJHWNStpr/view?usp=sharing
- Extract files to project directory

3. **Install dependencies**
```bash
pip install numpy gensim
```

---

## 💻 Usage

### Basic Correction
```python
python main.py
```

The program will:
1. Load the Word2Vec model
2. Read input text
3. Detect spelling errors
4. Suggest corrections using combined algorithms
5. Return corrected text

### Example
```
Input:  "Kumanadyı kaybettm"
Output: "Kumandayı kaybettim"
```

---

## 🔬 Algorithms

### 1. Damerau-Levenshtein Distance (`damerau_low.py`)

Handles four types of single-character edits:
- **Insertion:** kitap → kitaap
- **Deletion:** kitaap → kitap
- **Substitution:** kitap → kita**b**
- **Transposition:** ktiap → ki**ta**p

**Example from our research:**
- Word: "Kitap" vs "Ktiap"
- Levenshtein Distance: 2 (delete "i", add "i")
- Damerau-Levenshtein: 1 (transpose "i" and "t")

### 2. Jaro Distance (`jaro.py`)

Measures similarity based on:
- Matching characters
- Character transpositions
- Phonetic similarity

### 3. Keyboard Distance (`letter_distance.py`)

Calculates distance based on physical QWERTY keyboard layout:
- Penalizes errors on adjacent keys less
- Considers Turkish Q keyboard layout
- Improves typo detection accuracy

### 4. Word2Vec Semantic Similarity (`word2vec_tr.py`)

- Uses pre-trained Turkish Word2Vec model
- Finds semantically similar words
- Helps with context-aware corrections

### 5. Combined Scoring (`combine.py`)

Merges all algorithms using weighted scoring:
```
final_score = w1 * damerau + w2 * jaro + 
              w3 * keyboard + w4 * semantic
```

---

## 📊 Performance

Based on testing with Turkish text corpus:

| Metric | Value |
|--------|-------|
| Accuracy | **99.2%** |
| Dataset Size | 250,000 words |
| Algorithm | Combined (4 methods) |

---

## 📚 Research

This project contributed to peer-reviewed academic research:

**Title:** "The Role of Phonological Errors in Evaluation Metrics"  
**Authors:** Ayşegül Çağlı, Vakkas Karakurt, Kürşat Edabalı Yıldırım, Fatih Soygazi, Yılmaz Kılıçaslan  
**Institution:** Computer Engineering Department, Aydın Adnan Menderes University  
**Journal:** Journal of Computer Science (BBD)  
**Volume:** IDAP-2023, pp:44-51, 2023  
**DOI:** [10.53070/bbd.1350547](https://dergipark.org.tr/en/pub/bbd/issue/80462/1350547)  
**Published:** October 18, 2023

### Research Focus

The paper investigates phonological errors in Turkish NLP and proposes enhancing evaluation metrics (ROUGE, BLEU) by integrating edit distance algorithms.

### Key Findings

From our Twitter dataset analysis (38,750 words):
- **62.51%** of errors were spelling/phonological errors
- **37.49%** were grammar errors
- Phonological errors are the most common mistake type among Turkish writers

### Main Contributions

1. **Demonstrated** that phonological errors significantly impact NLP evaluation metrics
2. **Proposed** integration of Damerau-Levenshtein algorithm with ROUGE metrics
3. **Showed** improved ROUGE-1 scores: from 57% to 80% similarity on error-containing texts
4. **Collected** real-world data from Twitter to validate findings

---

## 🛠️ Technical Details

### Data Files

- **clear_words.txt**: Dictionary of correctly spelled Turkish words
- **first_250k.txt**: Training corpus (250,000 most common Turkish words)
- **Word2Vec model**: Pre-trained embeddings (download separately)

### Word2Vec Model

Due to GitHub file size limitations, the Word2Vec model is hosted externally.  
Download link: https://drive.google.com/file/d/1ljwPcaBUUPARyRDxWjaxJJFWJHWNStpr/view?usp=sharing

---

## 🤝 Contributing

This is an academic research project. Contributions, issues, and feature requests are welcome.

---

## 📜 License

This project was developed as part of academic research at Aydın Adnan Menderes University.

---

## 👨‍💻 Authors

**Ayşegül Çağlı**  
Aydın Adnan Menderes University  

**Vakkas Karakurt**  
Aydın Adnan Menderes University  
📧  karakurtvakkas@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/vakkaskarakurt) | [GitHub](https://github.com/vakkaskarakurt)

**Kürşat Edabalı Yıldırım**  
Aydın Adnan Menderes University  

**Research Advisors:**  
- Dr. Fatih Soygazi
- Dr. Yılmaz Kılıçaslan

---

## 🙏 Acknowledgments

- Aydın Adnan Menderes University Computer Engineering Department
- Research Team: Ayşegül Çağlı, Vakkas Karakurt, Kürşat Edabalı Yıldırım
- Research Advisors: Dr. Fatih Soygazi, Dr. Yılmaz Kılıçaslan
- Turkish Language Association (TDK) for word lists
- Twitter data contributors

---

⭐ If you find this project useful, please star the repository!
