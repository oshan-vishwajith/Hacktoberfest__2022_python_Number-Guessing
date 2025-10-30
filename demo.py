"""
Demo Script - Showcase Enhanced Number Guessing Game Features
Run this to see a quick demo of all the features
"""

from enhanced_number_guessing import GameStatistics, GameConfig
import json

def print_section(title):
    """Print a formatted section header"""
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70 + "\n")

def demo_difficulty_levels():
    """Demonstrate all difficulty levels"""
    print_section("🎲 DIFFICULTY LEVELS")
    
    print("The game offers 4 difficulty levels:\n")
    for idx, (difficulty, config) in enumerate(GameConfig.DIFFICULTIES.items(), 1):
        print(f"{idx}. {difficulty.upper()}")
        print(f"   Range: {config['range'][0]}-{config['range'][1]}")
        print(f"   Hints: {config['hints']}")
        print(f"   Multiplier: {['1x', '2x', '3x', '5x'][idx-1]}")
        print()

def demo_game_modes():
    """Demonstrate all game modes"""
    print_section("🎮 GAME MODES")
    
    modes = {
        'Classic': 'Traditional number guessing with optimal attempts',
        'Timed': 'Race against 60 seconds for bonus points',
        'Survival': 'Limited attempts with double score multiplier'
    }
    
    for idx, (mode, description) in enumerate(modes.items(), 1):
        print(f"{idx}. {mode.upper()} MODE")
        print(f"   {description}")
        print()

def demo_scoring():
    """Demonstrate scoring system"""
    print_section("🏆 SCORING SYSTEM")
    
    print("Formula: Score = (1000 - attempts × 50) × difficulty_multiplier\n")
    
    print("Examples:")
    print("-" * 70)
    
    stats = GameStatistics('demo_stats.json')
    
    examples = [
        (3, 'easy', 'Classic'),
        (5, 'medium', 'Classic'),
        (4, 'hard', 'Classic'),
        (6, 'expert', 'Classic'),
        (3, 'medium', 'Timed (with 15s bonus)'),
    ]
    
    for attempts, difficulty, mode in examples:
        score = stats.calculate_score(attempts, difficulty)
        if 'Timed' in mode:
            score += 150  # 15 seconds * 10
        if 'Survival' in mode:
            score *= 2
        
        print(f"• {attempts} attempts on {difficulty.capitalize()} mode: {score} points")
    
    print()

def demo_statistics():
    """Demonstrate statistics tracking"""
    print_section("📊 STATISTICS TRACKING")
    
    print("The game tracks comprehensive statistics:\n")
    
    tracked_items = [
        "✓ Total games played",
        "✓ Games won",
        "✓ Win rate percentage",
        "✓ Average attempts per won game",
        "✓ Personal best score",
        "✓ Complete game history"
    ]
    
    for item in tracked_items:
        print(f"  {item}")
    
    print("\n💾 All statistics are automatically saved to 'game_stats.json'")
    print()

def demo_leaderboard():
    """Demonstrate leaderboard system"""
    print_section("🏆 LEADERBOARD SYSTEM")
    
    print("Features:")
    print("  • Top 10 high scores")
    print("  • Player names and timestamps")
    print("  • Score, attempts, and difficulty level")
    print("  • Automatic sorting by score")
    print()
    
    # Create sample leaderboard
    print("Sample Leaderboard:")
    print("-" * 70)
    print(f"{'Rank':<8}{'Player':<15}{'Score':<10}{'Attempts':<10}{'Difficulty':<15}")
    print("-" * 70)
    
    sample_data = [
        (1, "SpeedRunner", 2850, 2, "Expert"),
        (2, "ProGamer", 2550, 3, "Hard"),
        (3, "QuickThinker", 1850, 3, "Medium"),
        (4, "LuckyGuess", 1700, 5, "Medium"),
        (5, "Strategist", 1500, 4, "Hard"),
    ]
    
    for rank, player, score, attempts, difficulty in sample_data:
        print(f"{rank:<8}{player:<15}{score:<10}{attempts:<10}{difficulty:<15}")
    
    print()

def demo_hints():
    """Demonstrate hint system"""
    print_section("💡 HINT SYSTEM")
    
    print("The game provides strategic hints to help you:\n")
    
    hint_types = [
        ("Parity Hint", "Reveals if the number is even or odd"),
        ("Range Hint", "Indicates if number is in lower or upper half"),
        ("Digit Sum Hint", "Shows the sum of digits in the number")
    ]
    
    for hint_type, description in hint_types:
        print(f"  • {hint_type}: {description}")
    
    print("\n💭 Example hints:")
    print('  "The number is even"')
    print('  "The number is greater than or equal to 50"')
    print('  "The sum of digits is 8"')
    print()
    
    print("Type 'hint' instead of a number to use a hint!")
    print()

def demo_input_validation():
    """Demonstrate input validation"""
    print_section("✅ INPUT VALIDATION")
    
    print("Robust error handling ensures smooth gameplay:\n")
    
    features = [
        "✓ Type checking (ensures numeric input)",
        "✓ Range validation (warns if out of bounds)",
        "✓ Clear error messages",
        "✓ Automatic retry on invalid input",
        "✓ Graceful handling of edge cases"
    ]
    
    for feature in features:
        print(f"  {feature}")
    
    print()

def demo_features_summary():
    """Show comprehensive feature list"""
    print_section("✨ ALL FEATURES SUMMARY")
    
    all_features = {
        "🎯 Core Gameplay": [
            "4 difficulty levels (Easy to Expert)",
            "3 game modes (Classic, Timed, Survival)",
            "Dynamic range narrowing",
            "Strategic hint system"
        ],
        "📊 Progress Tracking": [
            "Comprehensive statistics",
            "Top 10 leaderboard",
            "Personal best tracking",
            "Persistent data storage"
        ],
        "🎨 User Experience": [
            "Interactive menu system",
            "Visual emoji feedback",
            "Clear instructions",
            "Input validation"
        ],
        "🧪 Technical": [
            "Object-oriented design",
            "100% test coverage",
            "Type hints throughout",
            "Comprehensive documentation"
        ]
    }
    
    for category, features in all_features.items():
        print(f"{category}")
        for feature in features:
            print(f"  • {feature}")
        print()

def demo_how_to_contribute():
    """Show contribution opportunities"""
    print_section("🤝 CONTRIBUTION OPPORTUNITIES")
    
    print("This project is perfect for Hacktoberfest! Here are contribution ideas:\n")
    
    contribution_levels = {
        "🌱 Beginner-Friendly": [
            "Add colorful terminal output",
            "Create ASCII art for menus",
            "Implement more hint types",
            "Add multi-language support"
        ],
        "🚀 Intermediate": [
            "Create GUI version with tkinter",
            "Implement multiplayer mode",
            "Add achievements system",
            "Create data visualizations"
        ],
        "⚡ Advanced": [
            "Build AI opponent",
            "Create web version",
            "Implement online leaderboard",
            "Add machine learning strategies"
        ]
    }
    
    for level, ideas in contribution_levels.items():
        print(f"{level}")
        for idea in ideas:
            print(f"  • {idea}")
        print()
    
    print("See CONTRIBUTING.md for detailed guidelines!")
    print()

def main():
    """Run the complete demo"""
    print("\n" + "="*70)
    print("  🎮 ENHANCED NUMBER GUESSING GAME - FEATURE SHOWCASE 🎮")
    print("="*70)
    print("\nWelcome to the feature demonstration!")
    print("This demo will showcase all the amazing features added to this repo.")
    print()
    
    input("Press Enter to begin the demo...")
    
    demo_difficulty_levels()
    input("Press Enter to continue...")
    
    demo_game_modes()
    input("Press Enter to continue...")
    
    demo_scoring()
    input("Press Enter to continue...")
    
    demo_hints()
    input("Press Enter to continue...")
    
    demo_statistics()
    input("Press Enter to continue...")
    
    demo_leaderboard()
    input("Press Enter to continue...")
    
    demo_input_validation()
    input("Press Enter to continue...")
    
    demo_features_summary()
    input("Press Enter to continue...")
    
    demo_how_to_contribute()
    
    print_section("🎉 DEMO COMPLETE!")
    
    print("Ready to play? Run:")
    print("  python enhanced_number_guessing.py")
    print()
    print("Want to contribute? Check out:")
    print("  • README_NEW.md - Project overview")
    print("  • FEATURES.md - Detailed features")
    print("  • CONTRIBUTING.md - How to contribute")
    print("  • QUICKSTART.md - Quick start guide")
    print()
    print("⭐ Star the repo if you like it!")
    print("🍴 Fork it to contribute!")
    print("🎃 Happy Hacktoberfest 2022!")
    print()
    
    # Clean up demo file
    import os
    if os.path.exists('demo_stats.json'):
        os.remove('demo_stats.json')

if __name__ == "__main__":
    main()
