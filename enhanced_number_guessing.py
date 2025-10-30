"""
Enhanced Number Guessing Game
Features:
- Multiple difficulty levels
- Score tracking and leaderboard
- Game statistics
- Hint system
- Input validation
- Game modes (Classic, Timed, Survival)
"""

import random
import math
import json
import time
from datetime import datetime
from typing import Dict, List, Tuple, Optional


class GameConfig:
    """Configuration for different difficulty levels"""
    DIFFICULTIES = {
        'easy': {'range': (1, 50), 'hints': 3, 'time_limit': None},
        'medium': {'range': (1, 100), 'hints': 2, 'time_limit': None},
        'hard': {'range': (1, 200), 'hints': 1, 'time_limit': None},
        'expert': {'range': (1, 500), 'hints': 0, 'time_limit': None}
    }
    
    GAME_MODES = ['classic', 'timed', 'survival']


class GameStatistics:
    """Track and manage game statistics"""
    
    def __init__(self, stats_file: str = 'game_stats.json'):
        self.stats_file = stats_file
        self.stats = self.load_stats()
    
    def load_stats(self) -> Dict:
        """Load statistics from file"""
        try:
            with open(self.stats_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {
                'games_played': 0,
                'games_won': 0,
                'total_attempts': 0,
                'best_score': None,
                'leaderboard': []
            }
    
    def save_stats(self):
        """Save statistics to file"""
        with open(self.stats_file, 'w') as f:
            json.dump(self.stats, f, indent=4)
    
    def update_stats(self, won: bool, attempts: int, player_name: str, difficulty: str):
        """Update game statistics"""
        self.stats['games_played'] += 1
        if won:
            self.stats['games_won'] += 1
            self.stats['total_attempts'] += attempts
            
            score = self.calculate_score(attempts, difficulty)
            
            # Update best score
            if self.stats['best_score'] is None or score > self.stats['best_score']:
                self.stats['best_score'] = score
            
            # Add to leaderboard
            self.add_to_leaderboard(player_name, score, attempts, difficulty)
        
        self.save_stats()
    
    def calculate_score(self, attempts: int, difficulty: str) -> int:
        """Calculate score based on attempts and difficulty"""
        difficulty_multiplier = {'easy': 1, 'medium': 2, 'hard': 3, 'expert': 5}
        base_score = 1000
        penalty = attempts * 50
        return max(0, (base_score - penalty) * difficulty_multiplier.get(difficulty, 1))
    
    def add_to_leaderboard(self, player_name: str, score: int, attempts: int, difficulty: str):
        """Add player to leaderboard"""
        entry = {
            'name': player_name,
            'score': score,
            'attempts': attempts,
            'difficulty': difficulty,
            'timestamp': datetime.now().isoformat()
        }
        
        self.stats['leaderboard'].append(entry)
        # Keep top 10 scores
        self.stats['leaderboard'] = sorted(
            self.stats['leaderboard'], 
            key=lambda x: x['score'], 
            reverse=True
        )[:10]
    
    def display_stats(self):
        """Display game statistics"""
        print("\n" + "="*50)
        print("GAME STATISTICS".center(50))
        print("="*50)
        print(f"Total Games Played: {self.stats['games_played']}")
        print(f"Games Won: {self.stats['games_won']}")
        if self.stats['games_played'] > 0:
            win_rate = (self.stats['games_won'] / self.stats['games_played']) * 100
            print(f"Win Rate: {win_rate:.2f}%")
        if self.stats['games_won'] > 0:
            avg_attempts = self.stats['total_attempts'] / self.stats['games_won']
            print(f"Average Attempts (Won Games): {avg_attempts:.2f}")
        if self.stats['best_score']:
            print(f"Best Score: {self.stats['best_score']}")
        print("="*50 + "\n")
    
    def display_leaderboard(self):
        """Display top 10 leaderboard"""
        print("\n" + "="*60)
        print("LEADERBOARD - TOP 10".center(60))
        print("="*60)
        
        if not self.stats['leaderboard']:
            print("No entries yet. Be the first to play!".center(60))
        else:
            print(f"{'Rank':<6}{'Name':<15}{'Score':<10}{'Attempts':<10}{'Difficulty':<15}")
            print("-"*60)
            for idx, entry in enumerate(self.stats['leaderboard'], 1):
                print(f"{idx:<6}{entry['name']:<15}{entry['score']:<10}{entry['attempts']:<10}{entry['difficulty']:<15}")
        
        print("="*60 + "\n")


class NumberGuessingGame:
    """Main game class with enhanced features"""
    
    def __init__(self):
        self.stats = GameStatistics()
        self.difficulty = 'medium'
        self.game_mode = 'classic'
        self.hints_remaining = 0
        self.target_number = 0
        self.lower_bound = 0
        self.upper_bound = 0
        self.max_attempts = 0
        self.attempts = 0
        self.start_time = 0
        self.player_name = ""
    
    def validate_input(self, prompt: str, input_type: type, min_val: Optional[int] = None, 
                      max_val: Optional[int] = None) -> any:
        """Validate user input with type checking and range validation"""
        while True:
            try:
                user_input = input_type(input(prompt))
                if min_val is not None and user_input < min_val:
                    print(f"⚠️  Please enter a value >= {min_val}")
                    continue
                if max_val is not None and user_input > max_val:
                    print(f"⚠️  Please enter a value <= {max_val}")
                    continue
                return user_input
            except ValueError:
                print(f"⚠️  Invalid input! Please enter a valid {input_type.__name__}.")
            except KeyboardInterrupt:
                print("\n\n👋 Game interrupted. Goodbye!")
                exit(0)
    
    def get_hint(self) -> str:
        """Generate a hint for the player"""
        if self.hints_remaining <= 0:
            return "❌ No hints remaining!"
        
        self.hints_remaining -= 1
        
        # Different types of hints
        hint_types = [
            f"The number is {'even' if self.target_number % 2 == 0 else 'odd'}",
            f"The number is {'less than' if self.target_number < (self.lower_bound + self.upper_bound) / 2 else 'greater than or equal to'} {(self.lower_bound + self.upper_bound) // 2}",
            f"The sum of digits is {sum(int(d) for d in str(self.target_number))}"
        ]
        
        hint = random.choice(hint_types)
        return f"💡 Hint ({self.hints_remaining} remaining): {hint}"
    
    def setup_game(self):
        """Setup game configuration"""
        print("\n" + "="*60)
        print("🎮 ENHANCED NUMBER GUESSING GAME 🎮".center(60))
        print("="*60)
        
        self.player_name = input("\nEnter your name: ").strip() or "Player"
        
        # Select difficulty
        print("\n📊 Select Difficulty:")
        for idx, (diff, config) in enumerate(GameConfig.DIFFICULTIES.items(), 1):
            print(f"  {idx}. {diff.capitalize()} (Range: {config['range'][0]}-{config['range'][1]}, Hints: {config['hints']})")
        
        diff_choice = self.validate_input("Choose difficulty (1-4): ", int, 1, 4)
        self.difficulty = list(GameConfig.DIFFICULTIES.keys())[diff_choice - 1]
        
        # Select game mode
        print("\n🎯 Select Game Mode:")
        print("  1. Classic - Standard number guessing")
        print("  2. Timed - Guess within 60 seconds")
        print("  3. Survival - Limited attempts, increasing difficulty")
        
        mode_choice = self.validate_input("Choose mode (1-3): ", int, 1, 3)
        self.game_mode = GameConfig.GAME_MODES[mode_choice - 1]
        
        # Setup based on difficulty
        config = GameConfig.DIFFICULTIES[self.difficulty]
        self.lower_bound, self.upper_bound = config['range']
        self.hints_remaining = config['hints']
        self.target_number = random.randint(self.lower_bound, self.upper_bound)
        self.max_attempts = round(math.log(self.upper_bound - self.lower_bound + 1, 2))
        self.attempts = 0
        self.start_time = time.time()
        
        print(f"\n✨ Game Setup Complete!")
        print(f"   Player: {self.player_name}")
        print(f"   Difficulty: {self.difficulty.capitalize()}")
        print(f"   Mode: {self.game_mode.capitalize()}")
        print(f"   Range: {self.lower_bound} - {self.upper_bound}")
        print(f"   Max Attempts: {self.max_attempts}")
        print(f"   Hints Available: {self.hints_remaining}")
        if self.game_mode == 'timed':
            print(f"   Time Limit: 60 seconds")
        print()
    
    def play_classic_mode(self) -> bool:
        """Play classic mode"""
        print("🎲 Starting Classic Mode...\n")
        
        while self.attempts < self.max_attempts:
            print(f"Attempt {self.attempts + 1}/{self.max_attempts}")
            print(f"Current Range: {self.lower_bound} - {self.upper_bound}")
            
            # Check for hint request
            action = input("Enter your guess (or 'hint' for a hint): ").strip().lower()
            
            if action == 'hint':
                print(self.get_hint())
                continue
            
            try:
                guess = int(action)
            except ValueError:
                print("⚠️  Invalid input! Please enter a number or 'hint'.")
                continue
            
            if guess < self.lower_bound or guess > self.upper_bound:
                print(f"⚠️  Please guess between {self.lower_bound} and {self.upper_bound}!")
                continue
            
            self.attempts += 1
            
            if guess == self.target_number:
                elapsed_time = time.time() - self.start_time
                print(f"\n🎉 Congratulations {self.player_name}! You guessed it!")
                print(f"   Number: {self.target_number}")
                print(f"   Attempts: {self.attempts}/{self.max_attempts}")
                print(f"   Time: {elapsed_time:.2f} seconds")
                score = self.stats.calculate_score(self.attempts, self.difficulty)
                print(f"   Score: {score}")
                return True
            elif guess < self.target_number:
                print("📈 Too low! Try a higher number.")
                self.lower_bound = max(self.lower_bound, guess + 1)
            else:
                print("📉 Too high! Try a lower number.")
                self.upper_bound = min(self.upper_bound, guess - 1)
            
            print()
        
        return False
    
    def play_timed_mode(self) -> bool:
        """Play timed mode with 60 second limit"""
        print("⏱️  Starting Timed Mode... You have 60 seconds!\n")
        time_limit = 60
        
        while self.attempts < self.max_attempts:
            elapsed = time.time() - self.start_time
            remaining = time_limit - elapsed
            
            if remaining <= 0:
                print("\n⏰ Time's up!")
                return False
            
            print(f"⏱️  Time Remaining: {remaining:.1f}s | Attempt {self.attempts + 1}/{self.max_attempts}")
            print(f"Current Range: {self.lower_bound} - {self.upper_bound}")
            
            action = input("Enter your guess (or 'hint'): ").strip().lower()
            
            if action == 'hint':
                print(self.get_hint())
                continue
            
            try:
                guess = int(action)
            except ValueError:
                print("⚠️  Invalid input!")
                continue
            
            if guess < self.lower_bound or guess > self.upper_bound:
                print(f"⚠️  Guess between {self.lower_bound} and {self.upper_bound}!")
                continue
            
            self.attempts += 1
            
            if guess == self.target_number:
                elapsed_time = time.time() - self.start_time
                print(f"\n🎉 Amazing! You beat the clock!")
                print(f"   Number: {self.target_number}")
                print(f"   Attempts: {self.attempts}/{self.max_attempts}")
                print(f"   Time: {elapsed_time:.2f} seconds")
                score = self.stats.calculate_score(self.attempts, self.difficulty) + int((time_limit - elapsed_time) * 10)
                print(f"   Score (with time bonus): {score}")
                return True
            elif guess < self.target_number:
                print("📈 Too low!")
                self.lower_bound = max(self.lower_bound, guess + 1)
            else:
                print("📉 Too high!")
                self.upper_bound = min(self.upper_bound, guess - 1)
            
            print()
        
        return False
    
    def play_survival_mode(self) -> bool:
        """Play survival mode - stricter attempt limit"""
        print("💀 Starting Survival Mode... Every guess counts!\n")
        
        # Survival mode has fewer attempts
        survival_attempts = max(3, self.max_attempts - 2)
        
        while self.attempts < survival_attempts:
            print(f"❤️  Lives: {survival_attempts - self.attempts} | Attempt {self.attempts + 1}/{survival_attempts}")
            print(f"Current Range: {self.lower_bound} - {self.upper_bound}")
            
            action = input("Enter your guess (or 'hint'): ").strip().lower()
            
            if action == 'hint':
                print(self.get_hint())
                continue
            
            try:
                guess = int(action)
            except ValueError:
                print("⚠️  Invalid input!")
                continue
            
            if guess < self.lower_bound or guess > self.upper_bound:
                print(f"⚠️  Guess between {self.lower_bound} and {self.upper_bound}!")
                continue
            
            self.attempts += 1
            
            if guess == self.target_number:
                elapsed_time = time.time() - self.start_time
                print(f"\n🏆 Incredible! You survived!")
                print(f"   Number: {self.target_number}")
                print(f"   Attempts: {self.attempts}/{survival_attempts}")
                print(f"   Time: {elapsed_time:.2f} seconds")
                score = self.stats.calculate_score(self.attempts, self.difficulty) * 2  # Double score for survival
                print(f"   Score (survival bonus): {score}")
                return True
            elif guess < self.target_number:
                print("📈 Too low!")
                self.lower_bound = max(self.lower_bound, guess + 1)
            else:
                print("📉 Too high!")
                self.upper_bound = min(self.upper_bound, guess - 1)
            
            print()
        
        return False
    
    def play(self):
        """Main game loop"""
        self.setup_game()
        
        # Play based on selected mode
        if self.game_mode == 'classic':
            won = self.play_classic_mode()
        elif self.game_mode == 'timed':
            won = self.play_timed_mode()
        else:  # survival
            won = self.play_survival_mode()
        
        # Game over
        if not won:
            print(f"\n😔 Game Over!")
            print(f"   The number was: {self.target_number}")
            print(f"   Attempts used: {self.attempts}")
            print(f"   Better luck next time, {self.player_name}!")
        
        # Update statistics
        self.stats.update_stats(won, self.attempts, self.player_name, self.difficulty)
    
    def main_menu(self):
        """Display main menu"""
        while True:
            print("\n" + "="*60)
            print("MAIN MENU".center(60))
            print("="*60)
            print("1. 🎮 Play Game")
            print("2. 📊 View Statistics")
            print("3. 🏆 View Leaderboard")
            print("4. ❓ How to Play")
            print("5. 🚪 Exit")
            print("="*60)
            
            choice = self.validate_input("Select an option (1-5): ", int, 1, 5)
            
            if choice == 1:
                self.play()
            elif choice == 2:
                self.stats.display_stats()
            elif choice == 3:
                self.stats.display_leaderboard()
            elif choice == 4:
                self.show_instructions()
            else:
                print("\n👋 Thanks for playing! Goodbye!")
                break
    
    def show_instructions(self):
        """Display game instructions"""
        print("\n" + "="*60)
        print("HOW TO PLAY".center(60))
        print("="*60)
        print("""
📝 OBJECTIVE:
   Guess the secret number within the given attempts!

🎯 GAME MODES:
   • Classic: Traditional number guessing
   • Timed: Race against 60 seconds
   • Survival: Limited attempts with higher stakes

📊 DIFFICULTY LEVELS:
   • Easy: 1-50, 3 hints
   • Medium: 1-100, 2 hints
   • Hard: 1-200, 1 hint
   • Expert: 1-500, no hints

💡 HINTS:
   Type 'hint' instead of a number to get a clue!
   Hints reveal information about the number.

🏆 SCORING:
   Higher scores for fewer attempts and harder difficulties.
   Timed mode gives bonus points for speed.
   Survival mode doubles your score!

✨ TIPS:
   • Use binary search strategy for optimal guessing
   • Save hints for when you really need them
   • Pay attention to the narrowing range
   • Practice makes perfect!
        """)
        print("="*60)


def main():
    """Entry point for the enhanced game"""
    game = NumberGuessingGame()
    game.main_menu()


if __name__ == "__main__":
    main()
