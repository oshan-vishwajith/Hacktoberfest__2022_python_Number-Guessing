"""
Unit tests for Enhanced Number Guessing Game
Run with: pytest test_number_guessing.py -v
"""

import unittest
import json
import os
from unittest.mock import patch, mock_open, MagicMock
from enhanced_number_guessing import (
    GameConfig, 
    GameStatistics, 
    NumberGuessingGame
)


class TestGameConfig(unittest.TestCase):
    """Test GameConfig class"""
    
    def test_difficulties_exist(self):
        """Test that all difficulty levels are defined"""
        self.assertIn('easy', GameConfig.DIFFICULTIES)
        self.assertIn('medium', GameConfig.DIFFICULTIES)
        self.assertIn('hard', GameConfig.DIFFICULTIES)
        self.assertIn('expert', GameConfig.DIFFICULTIES)
    
    def test_difficulty_structure(self):
        """Test difficulty configuration structure"""
        for difficulty, config in GameConfig.DIFFICULTIES.items():
            self.assertIn('range', config)
            self.assertIn('hints', config)
            self.assertIn('time_limit', config)
            self.assertEqual(len(config['range']), 2)
            self.assertGreaterEqual(config['hints'], 0)
    
    def test_game_modes_exist(self):
        """Test that all game modes are defined"""
        self.assertEqual(len(GameConfig.GAME_MODES), 3)
        self.assertIn('classic', GameConfig.GAME_MODES)
        self.assertIn('timed', GameConfig.GAME_MODES)
        self.assertIn('survival', GameConfig.GAME_MODES)


class TestGameStatistics(unittest.TestCase):
    """Test GameStatistics class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.test_stats_file = 'test_game_stats.json'
        self.stats = GameStatistics(self.test_stats_file)
    
    def tearDown(self):
        """Clean up test files"""
        if os.path.exists(self.test_stats_file):
            os.remove(self.test_stats_file)
    
    def test_initialization(self):
        """Test statistics initialization"""
        self.assertEqual(self.stats.stats['games_played'], 0)
        self.assertEqual(self.stats.stats['games_won'], 0)
        self.assertEqual(self.stats.stats['total_attempts'], 0)
        self.assertIsNone(self.stats.stats['best_score'])
        self.assertEqual(len(self.stats.stats['leaderboard']), 0)
    
    def test_calculate_score(self):
        """Test score calculation"""
        # Easy difficulty, 5 attempts
        score_easy = self.stats.calculate_score(5, 'easy')
        self.assertEqual(score_easy, 750)  # (1000 - 5*50) * 1
        
        # Medium difficulty, 3 attempts
        score_medium = self.stats.calculate_score(3, 'medium')
        self.assertEqual(score_medium, 1700)  # (1000 - 3*50) * 2
        
        # Hard difficulty, 10 attempts
        score_hard = self.stats.calculate_score(10, 'hard')
        self.assertEqual(score_hard, 1500)  # (1000 - 10*50) * 3
        
        # Score should not be negative
        score_many_attempts = self.stats.calculate_score(50, 'easy')
        self.assertGreaterEqual(score_many_attempts, 0)
    
    def test_update_stats_win(self):
        """Test updating statistics after a win"""
        self.stats.update_stats(True, 5, "TestPlayer", "medium")
        
        self.assertEqual(self.stats.stats['games_played'], 1)
        self.assertEqual(self.stats.stats['games_won'], 1)
        self.assertEqual(self.stats.stats['total_attempts'], 5)
        self.assertIsNotNone(self.stats.stats['best_score'])
        self.assertEqual(len(self.stats.stats['leaderboard']), 1)
    
    def test_update_stats_loss(self):
        """Test updating statistics after a loss"""
        self.stats.update_stats(False, 10, "TestPlayer", "easy")
        
        self.assertEqual(self.stats.stats['games_played'], 1)
        self.assertEqual(self.stats.stats['games_won'], 0)
        self.assertEqual(self.stats.stats['total_attempts'], 0)
        self.assertIsNone(self.stats.stats['best_score'])
        self.assertEqual(len(self.stats.stats['leaderboard']), 0)
    
    def test_leaderboard_top_10(self):
        """Test that leaderboard keeps only top 10 scores"""
        # Add 15 entries
        for i in range(15):
            self.stats.add_to_leaderboard(f"Player{i}", i * 100, i + 1, "medium")
        
        # Should only keep top 10
        self.assertEqual(len(self.stats.stats['leaderboard']), 10)
        
        # Should be sorted by score (highest first)
        scores = [entry['score'] for entry in self.stats.stats['leaderboard']]
        self.assertEqual(scores, sorted(scores, reverse=True))
    
    def test_save_and_load_stats(self):
        """Test saving and loading statistics"""
        self.stats.update_stats(True, 3, "TestPlayer", "hard")
        self.stats.save_stats()
        
        # Create new instance and load
        new_stats = GameStatistics(self.test_stats_file)
        
        self.assertEqual(new_stats.stats['games_played'], 1)
        self.assertEqual(new_stats.stats['games_won'], 1)
        self.assertEqual(len(new_stats.stats['leaderboard']), 1)


class TestNumberGuessingGame(unittest.TestCase):
    """Test NumberGuessingGame class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.game = NumberGuessingGame()
        self.test_stats_file = 'test_game_stats.json'
        if os.path.exists(self.test_stats_file):
            os.remove(self.test_stats_file)
    
    def tearDown(self):
        """Clean up test files"""
        if os.path.exists('game_stats.json'):
            os.remove('game_stats.json')
        if os.path.exists(self.test_stats_file):
            os.remove(self.test_stats_file)
    
    def test_initialization(self):
        """Test game initialization"""
        self.assertEqual(self.game.difficulty, 'medium')
        self.assertEqual(self.game.game_mode, 'classic')
        self.assertEqual(self.game.attempts, 0)
        self.assertEqual(self.game.hints_remaining, 0)
    
    @patch('builtins.input', side_effect=['5'])
    def test_validate_input_valid(self, mock_input):
        """Test input validation with valid input"""
        result = self.game.validate_input("Enter number: ", int, 1, 10)
        self.assertEqual(result, 5)
    
    @patch('builtins.input', side_effect=['invalid', '5'])
    def test_validate_input_invalid_then_valid(self, mock_input):
        """Test input validation with invalid then valid input"""
        result = self.game.validate_input("Enter number: ", int, 1, 10)
        self.assertEqual(result, 5)
    
    @patch('builtins.input', side_effect=['0', '11', '5'])
    def test_validate_input_out_of_range(self, mock_input):
        """Test input validation with out of range values"""
        result = self.game.validate_input("Enter number: ", int, 1, 10)
        self.assertEqual(result, 5)
    
    def test_get_hint(self):
        """Test hint generation"""
        self.game.hints_remaining = 2
        self.game.target_number = 42
        self.game.lower_bound = 1
        self.game.upper_bound = 100
        
        hint = self.game.get_hint()
        self.assertIn("Hint", hint)
        self.assertEqual(self.game.hints_remaining, 1)
        
        # Test no hints remaining
        self.game.hints_remaining = 0
        hint = self.game.get_hint()
        self.assertIn("No hints", hint)
    
    @patch('builtins.input', side_effect=['TestPlayer', '2', '1'])
    @patch('random.randint', return_value=50)
    def test_setup_game(self, mock_random, mock_input):
        """Test game setup"""
        self.game.setup_game()
        
        self.assertEqual(self.game.player_name, 'TestPlayer')
        self.assertEqual(self.game.difficulty, 'medium')
        self.assertEqual(self.game.game_mode, 'classic')
        self.assertEqual(self.game.target_number, 50)
        self.assertGreater(self.game.max_attempts, 0)
    
    def test_score_calculation_consistency(self):
        """Test that score calculation is consistent"""
        stats = GameStatistics(self.test_stats_file)
        
        score1 = stats.calculate_score(5, 'medium')
        score2 = stats.calculate_score(5, 'medium')
        
        self.assertEqual(score1, score2)
    
    def test_difficulty_range_validity(self):
        """Test that difficulty ranges are valid"""
        for difficulty, config in GameConfig.DIFFICULTIES.items():
            lower, upper = config['range']
            self.assertLess(lower, upper, f"Invalid range for {difficulty}")
            self.assertGreaterEqual(lower, 1, f"Lower bound should be >= 1 for {difficulty}")


class TestGameIntegration(unittest.TestCase):
    """Integration tests for the complete game flow"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.test_stats_file = 'test_game_stats.json'
        if os.path.exists(self.test_stats_file):
            os.remove(self.test_stats_file)
    
    def tearDown(self):
        """Clean up test files"""
        if os.path.exists('game_stats.json'):
            os.remove('game_stats.json')
        if os.path.exists(self.test_stats_file):
            os.remove(self.test_stats_file)
    
    @patch('builtins.input', side_effect=['TestPlayer', '1', '1', '25', 'hint', '30'])
    @patch('random.randint', return_value=30)
    def test_complete_game_with_hint(self, mock_random, mock_input):
        """Test a complete game flow with hint usage"""
        game = NumberGuessingGame()
        game.setup_game()
        
        # Verify setup
        self.assertEqual(game.player_name, 'TestPlayer')
        self.assertEqual(game.target_number, 30)
        
        # Game should have hints available in easy mode
        self.assertGreater(game.hints_remaining, 0)
    
    def test_multiple_games_statistics(self):
        """Test statistics tracking across multiple games"""
        stats = GameStatistics(self.test_stats_file)
        
        # Simulate 3 games
        stats.update_stats(True, 5, "Player1", "easy")
        stats.update_stats(False, 10, "Player2", "medium")
        stats.update_stats(True, 3, "Player3", "hard")
        
        self.assertEqual(stats.stats['games_played'], 3)
        self.assertEqual(stats.stats['games_won'], 2)
        
        # Check leaderboard has 2 entries (only wins)
        self.assertEqual(len(stats.stats['leaderboard']), 2)


def run_tests():
    """Run all tests"""
    unittest.main(argv=[''], verbosity=2, exit=False)


if __name__ == '__main__':
    run_tests()
