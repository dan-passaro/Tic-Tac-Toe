"""Tests for the ``ai`` module."""
import unittest

from .. import ai


class AITest(unittest.TestCase):

    def test_first_move_o_responds_center_with_corner(self):
        """If AI is O, and X took center, AI takes a corner."""
        board = [
            '   ',
            ' X ',
            '   ',
        ]

        ai_response = ai.get_ai_move(board)
        self.assertEqual((0, 0), ai_response)

    def test_first_move_o_responds_edge_with_center(self):
        """If AI is O, and X didn't take center, takes the center."""
        board = [
            'X  ',
            '   ',
            '   ',
        ]

        ai_response = ai.get_ai_move(board)
        self.assertEqual((1, 1), ai_response)

        board = [
            ' X ',
            '   ',
            '   ',
        ]

        ai_response = ai.get_ai_move(board)
        self.assertEqual((1, 1), ai_response)

    def test_o_responds_to_diagonal_trap_with_x_centered(self):
        """The AI playing O blocks a diagonal trap with X at the center."""
        board = [
            '  X',
            ' X ',
            '0  ',
        ]

        ai_response = ai.get_ai_move(board)

        took_corner = ai_response == (0, 0) or ai_response == (2, 2)
        self.assertTrue(took_corner, ai_response)

        board = [
            'X  ',
            ' X ',
            '  0',
        ]

        ai_response = ai.get_ai_move(board)

        took_corner = ai_response == (0, 2) or ai_response == (2, 0)
        self.assertTrue(took_corner, ai_response)

        board = [
            '0  ',
            ' X ',
            '  X',
        ]

        ai_response = ai.get_ai_move(board)

        took_corner = ai_response == (0, 2) or ai_response == (2, 0)
        self.assertTrue(took_corner, ai_response)

    def test_o_responds_to_diagonal_trap_with_o_centered(self):
        """The AI playing O blocks a diagonal trap with O at the center."""
        board = [
            '  X',
            ' O ',
            'X  ',
        ]

        ai_response = ai.get_ai_move(board)

        took_edge = ai_response in ((0, 1), (1, 0), (2, 1), (1, 2))
        self.assertTrue(took_edge, ai_response)

        board = [
            'X  ',
            ' O ',
            '  X',
        ]

        ai_response = ai.get_ai_move(board)

        took_edge = ai_response in ((0, 1), (1, 0), (2, 1), (1, 2))
        self.assertTrue(took_edge, ai_response)

    def test_tries_to_block_diagonal_victory(self):
        """If opponent would win next turn on a diagonal, AI blocks it."""
        board = [
            'O  ',
            ' X ',
            'X  ',
        ]

        ai_response = ai.get_ai_move(board)

        self.assertEqual((0, 2), ai_response)

        board = [
            '  O',
            ' X ',
            '  X',
        ]

        ai_response = ai.get_ai_move(board)

        self.assertEqual((0, 0), ai_response)

    def test_blocks_vertical_victory(self):
        """If opponent would win next turn on a vertical, AI blocks it."""
        board = [
            'OXO',
            ' X ',
            'X  ',
        ]

        ai_response = ai.get_ai_move(board)

        self.assertEqual((2, 1), ai_response)

        board = [
            '   ',
            ' O ',
            'XX ',
        ]

        ai_response = ai.get_ai_move(board)

        self.assertEqual((2, 2), ai_response)

    def test_blocks_horizontal_victory(self):
        """If opponent would win next turn horizontally, AI blocks it."""
        board = [
            'OXO',
            ' XX',
            'XO ',
        ]

        ai_response = ai.get_ai_move(board)

        self.assertEqual((1, 0), ai_response)

        board = [
            'OXX',
            ' O ',
            '  X',
        ]

        ai_response = ai.get_ai_move(board)

        self.assertEqual((1, 2), ai_response)

    def test_wins_diagonally(self):
        """If the AI can win this turn on a diagonal, it does so."""
        board = [
            'XXO',
            ' OX',
            '   ',
        ]

        ai_response = ai.get_ai_move(board)

        self.assertEqual((2, 0), ai_response)

    # TODO: horizontal and vertical directional victory tests

    def test_makes_diagonal_as_o_if_x_plays_strangely(self):
        """Makes a diagonal if player X gives the center to O."""
        board = [
            ' X ',
            ' OX',
            '   ',
        ]

        ai_move = ai.get_ai_move(board)

        self.assertEqual((0, 2), ai_move)

        board = [
            '   ',
            'XO ',
            ' X ',
        ]

        ai_move = ai.get_ai_move(board)

        self.assertEqual((2, 0), ai_move)

    def test_marks_empty_cell_when_no_trap_or_block_or_win(self):
        """Marks a cell when there are no traps or wins to move against,"""
        board = [
            'X  ',
            'OOX',
            'XXO',
        ]

        ai_response = ai.get_ai_move(board)

        self.assertIn(ai_response, ((0, 1), (0, 2)))

        board = [
            'XXO',
            'OOX',
            'X  ',
        ]

        ai_response = ai.get_ai_move(board)

        self.assertIn(ai_response, ((2, 1,), (2, 2)))

    def test_ai_wins_over_blocking(self):
        """If the AI could win *or* block, it wins."""
        board = [
            'XO ',
            'XOX',
            '   ',
        ]

        ai_response = ai.get_ai_move(board)

        self.assertEqual((2, 1), ai_response)