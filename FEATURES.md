# Enhanced Number Guessing Game - Features Documentation

## 🎮 Core Features

### 1. Multiple Difficulty Levels

The game offers four difficulty levels to challenge players of all skill levels:

#### Easy Mode

- **Range**: 1-50
- **Hints**: 3 available
- **Score Multiplier**: 1x
- **Perfect for**: Beginners and casual players

#### Medium Mode

- **Range**: 1-100
- **Hints**: 2 available
- **Score Multiplier**: 2x
- **Perfect for**: Players familiar with the game

#### Hard Mode

- **Range**: 1-200
- **Hints**: 1 available
- **Score Multiplier**: 3x
- **Perfect for**: Experienced players

#### Expert Mode

- **Range**: 1-500
- **Hints**: 0 available
- **Score Multiplier**: 5x
- **Perfect for**: Masters of the game

### 2. Game Modes

#### Classic Mode

- Traditional number guessing gameplay
- Calculated optimal attempts based on range
- Strategic narrowing of the search range
- Hint system available

#### Timed Mode

- 60-second time limit
- All features of classic mode
- Time bonus points for faster completion
- Adds urgency and excitement

#### Survival Mode

- Reduced attempt limit (3 attempts minimum)
- Double score multiplier
- Higher stakes gameplay
- Tests efficiency and strategy

### 3. Intelligent Hint System

The game provides contextual hints to help players:

**Hint Types:**

1. **Parity Hint**: Reveals if the number is even or odd
2. **Range Hint**: Indicates if the number is in the lower or upper half
3. **Digit Sum Hint**: Shows the sum of digits in the number

**Strategic Usage:**

- Limited hints based on difficulty
- Consume hints strategically when stuck
- Type 'hint' instead of a number to get a clue

### 4. Comprehensive Scoring System

**Base Score Formula:**

```
Score = (1000 - attempts × 50) × difficulty_multiplier
```

**Multipliers:**

- Easy: 1x
- Medium: 2x
- Hard: 3x
- Expert: 5x

**Bonuses:**

- **Timed Mode**: +10 points per remaining second
- **Survival Mode**: 2x score multiplier

**Example:**

- 3 attempts on Hard mode: (1000 - 150) × 3 = 2,550 points
- 5 attempts on Easy mode: (1000 - 250) × 1 = 750 points

### 5. Statistics Tracking

**Tracked Metrics:**

- Total games played
- Games won
- Overall win rate percentage
- Average attempts per won game
- Personal best score
- Complete game history

**Persistent Storage:**

- Statistics saved to JSON file
- Survives between game sessions
- Easy to backup and transfer

### 6. Leaderboard System

**Features:**

- Top 10 high scores
- Player name
- Score achieved
- Number of attempts
- Difficulty level
- Timestamp of achievement

**Sorting:**

- Automatically sorted by score (highest first)
- Only keeps top 10 performances
- Fair competition across all difficulty levels

### 7. Input Validation

**Robust Error Handling:**

- Type checking (ensures numeric input)
- Range validation (warns if out of bounds)
- Graceful error messages
- Prevents game crashes

**User-Friendly:**

- Clear error messages
- Helpful prompts
- Retry mechanism
- Input sanitization

### 8. Dynamic Range Narrowing

**Smart Range Updates:**

- Automatically narrows search range after each guess
- Shows current valid range
- Helps players make informed decisions
- Prevents duplicate guessing

**Visual Feedback:**

```
Current Range: 1 - 100
Guess: 50
Too high!
Current Range: 1 - 49  ← Automatically updated
```

## 🎯 User Experience Features

### Interactive Menu System

- Clean, organized main menu
- Easy navigation
- Multiple viewing options
- Instructions readily available

### Visual Feedback

- Emoji indicators for different states
- Clear success/failure messages
- Progress tracking
- Time remaining display (timed mode)

### Game Instructions

- Comprehensive how-to-play guide
- Strategy tips
- Scoring explanation
- Feature overview

## 📊 Technical Features

### Object-Oriented Design

- Modular class structure
- Clear separation of concerns
- Easy to extend and maintain
- Reusable components

### Data Persistence

- JSON-based statistics storage
- Automatic save after each game
- Load on startup
- Error-resistant file handling

### Performance

- Efficient algorithms
- Minimal resource usage
- Fast response times
- No external dependencies (main game)

## 🔧 Developer Features

### Testability

- Comprehensive unit tests
- High code coverage
- Mock-friendly design
- Integration tests

### Code Quality

- PEP 8 compliant
- Type hints
- Docstrings
- Clear naming conventions

### Extensibility

- Easy to add new difficulty levels
- Simple game mode additions
- Pluggable hint system
- Customizable scoring

## 🚀 Future Feature Ideas

### Planned Enhancements

1. **Multiplayer Mode**: Compete against friends
2. **Achievements System**: Unlock badges and rewards
3. **Daily Challenges**: New puzzle each day
4. **Custom Ranges**: Player-defined number ranges
5. **Themes**: Different visual styles
6. **Sound Effects**: Audio feedback (optional)
7. **Online Leaderboard**: Global competition
8. **AI Opponent**: Play against computer
9. **Tutorial Mode**: Interactive learning
10. **Statistics Graphs**: Visual data representation

### Community Contributions Welcome!

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to add features.

## 📈 Version History

### v2.0.0 (Current)

- ✨ Multiple difficulty levels
- 🎮 Three game modes
- 💡 Hint system
- 📊 Statistics and leaderboard
- ✅ Input validation
- 🧪 Comprehensive tests

### v1.0.0 (Original)

- Basic number guessing
- Single difficulty
- Binary search attempts calculation
- Simple win/loss feedback

---

**Note**: This is a Hacktoberfest 2022 project. Contributions are welcome! 🎃
