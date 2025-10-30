# 🚀 Quick Start Guide

## For Players

### Play the Enhanced Game

1. **Run the game:**

```bash
python enhanced_number_guessing.py
```

2. **Navigate the menu:**

   - Option 1: Play Game
   - Option 2: View Statistics
   - Option 3: View Leaderboard
   - Option 4: How to Play
   - Option 5: Exit

3. **Gameplay tips:**
   - Use binary search strategy (guess the middle value)
   - Save hints for when the range is still large
   - In timed mode, make quick decisions
   - In survival mode, think carefully before each guess

### Play the Original Simple Version

```bash
python "Number Guessing.py"
```

## For Developers

### Run Tests

```bash
# Run all tests
python test_number_guessing.py

# Or with pytest (if installed)
pytest test_number_guessing.py -v

# With coverage report
pytest --cov=enhanced_number_guessing test_number_guessing.py
```

### Code Quality Checks

```bash
# Format code
black enhanced_number_guessing.py

# Lint code
pylint enhanced_number_guessing.py

# Type checking
mypy enhanced_number_guessing.py
```

## For Contributors

### Setup Development Environment

1. **Clone the repository:**

```bash
git clone https://github.com/induwara-dissanayake/Hacktoberfest__2022_python_Number-Guessing.git
cd Hacktoberfest__2022_python_Number-Guessing
```

2. **Create virtual environment:**

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On macOS/Linux
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Create your feature branch:**

```bash
git checkout -b feature/amazing-feature
```

5. **Make changes and test:**

```bash
# Make your changes
# Run tests to ensure nothing breaks
python test_number_guessing.py

# Commit your changes
git add .
git commit -m "feat: add amazing feature"
git push origin feature/amazing-feature
```

6. **Create Pull Request on GitHub**

### Quick Feature Addition Template

```python
# In enhanced_number_guessing.py

# 1. Add configuration (if needed)
class GameConfig:
    NEW_FEATURE_CONFIG = {...}

# 2. Add method to NumberGuessingGame class
def new_feature(self):
    """
    Description of new feature
    """
    # Implementation here
    pass

# 3. Add to menu or game flow
def main_menu(self):
    # Add menu option
    print("6. 🆕 New Feature")
    # Handle selection
    elif choice == 6:
        self.new_feature()
```

### Test Template

```python
# In test_number_guessing.py

class TestNewFeature(unittest.TestCase):
    """Test new feature"""

    def setUp(self):
        """Set up test fixtures"""
        self.game = NumberGuessingGame()

    def test_new_feature(self):
        """Test that new feature works"""
        result = self.game.new_feature()
        self.assertEqual(result, expected_value)
```

## Troubleshooting

### Common Issues

**Issue: "ModuleNotFoundError"**

```bash
# Solution: Install dependencies
pip install -r requirements.txt
```

**Issue: "SyntaxError"**

- Make sure you're using Python 3.7 or higher

```bash
python --version
```

**Issue: Tests fail**

- Make sure you're in the correct directory
- Clean up any test files

```bash
Remove-Item test_game_stats.json -ErrorAction SilentlyContinue  # Windows
rm -f test_game_stats.json  # macOS/Linux
```

**Issue: Game stats not saving**

- Check file permissions in the directory
- Make sure `game_stats.json` can be created/written

### Getting Help

- 📖 Read [FEATURES.md](FEATURES.md) for detailed documentation
- 🤝 Check [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines
- 🐛 Open an issue on GitHub for bugs
- 💬 Start a discussion for questions

## Next Steps

1. ⭐ **Star the repository** if you like it
2. 🍴 **Fork the repository** to contribute
3. 🎮 **Play the game** and have fun
4. 🛠️ **Add features** and make it better
5. 📢 **Share** with friends for Hacktoberfest

---

Happy Coding! 🎃👨‍💻👩‍💻
