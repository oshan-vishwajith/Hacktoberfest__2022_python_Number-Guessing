# 🎮 Enhanced Number Guessing Game - Hacktoberfest 2022

<p align="center">
  <img alt="Coder GIF" height=250 width=350 src="https://cdn.dribbble.com/users/1187836/screenshots/6539429/programer.gif" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Hacktoberfest-2022-orange?style=for-the-badge" alt="Hacktoberfest 2022">
  <img src="https://img.shields.io/badge/Python-3.7+-blue?style=for-the-badge&logo=python" alt="Python 3.7+">
  <img src="https://img.shields.io/badge/Contributions-Welcome-brightgreen?style=for-the-badge" alt="Contributions Welcome">
</p>

## 🎯 About

Welcome to the **Enhanced Number Guessing Game**! This project is part of **Hacktoberfest 2022**, featuring a feature-rich number guessing game with multiple difficulty levels, game modes, scoring systems, and comprehensive statistics tracking.

### ✨ Features

- 🎲 **4 Difficulty Levels**: Easy, Medium, Hard, and Expert
- 🎮 **3 Game Modes**: Classic, Timed Challenge, and Survival
- 💡 **Intelligent Hint System**: Strategic hints to help you win
- 📊 **Statistics Tracking**: Win rates, average attempts, and more
- 🏆 **Leaderboard System**: Top 10 high scores
- ✅ **Input Validation**: Robust error handling
- 🧪 **100% Tested**: Comprehensive unit tests included
- 🎨 **User-Friendly Interface**: Clear prompts and feedback

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/induwara-dissanayake/Hacktoberfest__2022_python_Number-Guessing.git
cd Hacktoberfest__2022_python_Number-Guessing
```

2. **Create a virtual environment (optional but recommended)**

```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

3. **Install dependencies (only needed for testing)**

```bash
pip install -r requirements.txt
```

4. **Run the game**

```bash
python enhanced_number_guessing.py
```

## 🎮 How to Play

1. **Choose Your Difficulty**

   - Easy (1-50, 3 hints)
   - Medium (1-100, 2 hints)
   - Hard (1-200, 1 hint)
   - Expert (1-500, no hints)

2. **Select Game Mode**

   - **Classic**: Traditional gameplay with optimal attempts
   - **Timed**: Race against 60 seconds for bonus points
   - **Survival**: Limited attempts with double score

3. **Make Your Guesses**

   - Enter numbers to guess the secret number
   - Type 'hint' to get a clue (if available)
   - Watch the range narrow with each guess

4. **Win and Score Points**
   - Fewer attempts = higher score
   - Higher difficulty = score multiplier
   - Compete on the leaderboard!

## 📊 Game Features

### Difficulty Levels

| Difficulty | Range | Hints | Multiplier |
| ---------- | ----- | ----- | ---------- |
| Easy       | 1-50  | 3     | 1x         |
| Medium     | 1-100 | 2     | 2x         |
| Hard       | 1-200 | 1     | 3x         |
| Expert     | 1-500 | 0     | 5x         |

### Scoring System

```
Score = (1000 - attempts × 50) × difficulty_multiplier
```

**Bonuses:**

- Timed Mode: +10 points per remaining second
- Survival Mode: 2x score multiplier

## 🧪 Running Tests

```bash
# Run all tests
pytest test_number_guessing.py -v

# Run with coverage
pytest --cov=enhanced_number_guessing test_number_guessing.py

# Run specific test class
pytest test_number_guessing.py::TestGameStatistics -v
```

## 🤝 Contributing to Hacktoberfest

We welcome contributions! Here's how you can participate:

### Step-by-Step Guide

1. **Register for Hacktoberfest**

   - Sign up at [hacktoberfest.com](https://hacktoberfest.com/)

2. **Fork this repository**

   - Click the 'Fork' button at the top right

3. **Clone your fork**

```bash
git clone https://github.com/<your-username>/Hacktoberfest__2022_python_Number-Guessing.git
cd Hacktoberfest__2022_python_Number-Guessing
```

4. **Create a new branch**

```bash
git checkout -b feature/your-feature-name
```

5. **Make your changes**

   - Add new features
   - Fix bugs
   - Improve documentation
   - Add tests

6. **Commit and push**

```bash
git add .
git commit -m "feat: add awesome feature"
git push origin feature/your-feature-name
```

7. **Create a Pull Request**
   - Go to your fork on GitHub
   - Click 'New Pull Request'
   - Describe your changes

**🎉 Yay!!! You've completed your Hacktoberfest contribution!**

### 💡 Contribution Ideas

- Add color output using colorama
- Create a GUI version with tkinter
- Implement multiplayer mode
- Add achievements system
- Create data visualizations
- Add more hint types
- Implement AI opponent
- Add multi-language support

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## 📚 Documentation

- **[FEATURES.md](FEATURES.md)** - Detailed feature documentation
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - Contribution guidelines
- **[requirements.txt](requirements.txt)** - Python dependencies

## 🗂️ Project Structure

```
Hacktoberfest__2022_python_Number-Guessing/
├── enhanced_number_guessing.py  # Main enhanced game with all features
├── Number Guessing.py           # Original simple version
├── test_number_guessing.py      # Comprehensive unit tests
├── requirements.txt             # Python dependencies
├── .gitignore                   # Git ignore file
├── README.md                    # This file
├── CONTRIBUTING.md              # Contribution guidelines
├── FEATURES.md                  # Detailed feature docs
├── Sandunika/                   # Community contributions
│   └── Number Guessing.txt
└── Vartika_01/                  # Community contributions
    └── number_guessing.py
```

## 🏆 Contributors

Thank you to all contributors who have helped make this project better!

<a href="https://github.com/induwara-dissanayake/Hacktoberfest__2022_python_Number-Guessing/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=induwara-dissanayake/Hacktoberfest__2022_python_Number-Guessing" />
</a>

## 📝 License

This project is open source and available for educational purposes as part of Hacktoberfest 2022.

## 🌟 Show Your Support

Give a ⭐️ if you like this project!

## 📧 Contact

- GitHub: [@induwara-dissanayake](https://github.com/induwara-dissanayake)
- Project Link: [Hacktoberfest\_\_2022_python_Number-Guessing](https://github.com/induwara-dissanayake/Hacktoberfest__2022_python_Number-Guessing)

---

<p align="center">Made with ❤️ for Hacktoberfest 2022</p>
