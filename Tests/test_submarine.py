import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../Application')))

import pytest
from submarine import Submarine

def test_initial_state():
    sub = Submarine()
    assert sub.depth == 0
    assert sub.horizontal == 0
    assert sub.aim == 0

def test_move_horizontal_without_aim():
    sub = Submarine()
    sub.moveHorizontal(10)
    assert sub.horizontal == 10
    assert sub.depth == 0  # Depth should not change without aim

def test_move_horizontal_with_aim():
    sub = Submarine()
    sub.moveAim(2)  # Set aim to 2
    sub.moveHorizontal(5)
    assert sub.horizontal == 5
    assert sub.depth == 10  # Depth = aim * distance = 2 * 5

def test_move_depth():
    sub = Submarine()
    sub.moveDepth(5)
    assert sub.depth == 5
    sub.moveDepth(-3)
    assert sub.depth == 2  # Depth decreases when moving up

def test_move_aim():
    sub = Submarine()
    sub.moveAim(3)
    assert sub.aim == 3
    sub.moveAim(-1)
    assert sub.aim == 2  # Aim decreases correctly

def test_get_position():
    sub = Submarine()
    sub.moveHorizontal(10)
    sub.moveDepth(5)
    assert sub.getPosition() == 50  # Position = horizontal * depth