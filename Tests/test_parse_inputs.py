import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../Application')))

import pytest
from parse_inputs import parseLine, parseInputs

def test_parse_line():
    input_string = "forward 5"
    expected_output = [{"command": "forward", "value": 5}]
    assert parseLine(input_string) == expected_output

    input_string = "down 5"
    expected_output = [{"command": "down", "value": 5}]
    assert parseLine(input_string) == expected_output

    input_string = "up 3"
    expected_output = [{"command": "up", "value": 3}]
    assert parseLine(input_string) == expected_output

def test_parse_inputs():
    input_string = "forward 5\ndown 5\nforward 8\nup 3\ndown 8\nforward 2"
    expected_output = [
        {"command": "forward", "value": 5},
        {"command": "down", "value": 5},
        {"command": "forward", "value": 8},
        {"command": "up", "value": 3},
        {"command": "down", "value": 8},
        {"command": "forward", "value": 2}
    ]
    assert parseInputs(input_string) == expected_output

    input_string = ""
    expected_output = []
    assert parseInputs(input_string) == expected_output

    input_string = "forward 0\ndown 0\nup 0"
    expected_output = [
        {"command": "forward", "value": 0},
        {"command": "down", "value": 0},
        {"command": "up", "value": 0}
    ]
    assert parseInputs(input_string) == expected_output