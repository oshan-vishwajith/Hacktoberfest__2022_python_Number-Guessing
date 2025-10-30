# Contributing to Enhanced Number Guessing Game

Thank you for your interest in contributing to this Hacktoberfest project! 🎉

## How to Contribute

### 1. Fork and Clone

```bash
# Fork this repository using the GitHub UI
# Then clone your fork
git clone https://github.com/YOUR-USERNAME/Hacktoberfest__2022_python_Number-Guessing.git
cd Hacktoberfest__2022_python_Number-Guessing
```

### 2. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-fix-name
```

### 3. Set Up Development Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 4. Make Your Changes

#### Code Style Guidelines

- Follow PEP 8 style guide
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and concise
- Add type hints where appropriate

#### Example:

```python
def calculate_score(attempts: int, difficulty: str) -> int:
    """
    Calculate player score based on attempts and difficulty.

    Args:
        attempts: Number of attempts taken
        difficulty: Difficulty level ('easy', 'medium', 'hard', 'expert')

    Returns:
        Calculated score as integer
    """
    # Implementation here
    pass
```

### 5. Add Tests

- Write unit tests for new features
- Ensure all tests pass: `pytest test_number_guessing.py -v`
- Aim for high test coverage: `pytest --cov=enhanced_number_guessing`

### 6. Run Code Quality Checks

```bash
# Format code
black enhanced_number_guessing.py

# Lint code
pylint enhanced_number_guessing.py

# Type checking
mypy enhanced_number_guessing.py
```

### 7. Commit Your Changes

```bash
git add .
git commit -m "feat: add awesome new feature"
```

#### Commit Message Convention

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `test:` Adding or updating tests
- `refactor:` Code refactoring
- `style:` Code style changes (formatting, etc.)
- `perf:` Performance improvements

### 8. Push and Create Pull Request

```bash
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub with:

- Clear title describing the change
- Detailed description of what was added/fixed
- Screenshots (if applicable)
- Reference to any related issues

## Feature Ideas

Here are some features you could contribute:

### Beginner-Friendly

- [ ] Add color output using colorama library
- [ ] Create ASCII art for game screens
- [ ] Add sound effects (optional dependency)
- [ ] Implement multi-language support
- [ ] Add more hint types

### Intermediate

- [ ] Create a GUI version using tkinter
- [ ] Add multiplayer mode
- [ ] Implement achievements system
- [ ] Add game replay functionality
- [ ] Create difficulty auto-adjustment based on performance

### Advanced

- [ ] Add AI opponent that learns from player strategies
- [ ] Implement online leaderboard with database
- [ ] Create web version using Flask/Django
- [ ] Add data visualization for game statistics
- [ ] Implement machine learning for optimal guessing strategy

## Bug Reports

Found a bug? Please create an issue with:

- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Python version and OS
- Error messages (if any)

## Questions?

Feel free to open an issue with the `question` label if you need help!

## Code Review Process

1. Maintainers will review your PR within 2-3 days
2. Address any requested changes
3. Once approved, your PR will be merged
4. Congratulations! You're now a contributor! 🎉

## Recognition

All contributors will be acknowledged in the README.md file.

Thank you for making this project better! 🚀
