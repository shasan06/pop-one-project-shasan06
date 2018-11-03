import pytest
from three_musketeers import *

left = 'left'
right = 'right'
up = 'up'
down = 'down'
M = 'M'
R = 'R'
_ = '-'

board1 =  [ [_, _, _, M, _],
            [_, _, R, M, _],
            [_, R, M, R, _],
            [_, R, _, _, _],
            [_, _, _, R, _] ]

board2 =  [ [_, _, _, M, _],
            [_, _, R, M, _],
            [_, R, M, R, _],
            [_, R, _, _, _],
            [_, _, _, R, _] ]
def test_create_board():
	create_board()
	for i in [0,1,2,3,4]:
		assert len(board[i]) == 5
		for j in range(5):
			if (i==0 and j==4) or (i==2 and j==2) or (i==4 and j==0):
				assert at((i,j)) == M
			else:
				assert at((i,j)) == R
    #eventually add at least two more test cases

def test_set_board():
    set_board(board1)
    assert at((0,0)) == _
    assert at((1,2)) == R
    assert at((1,3)) == M    
    #eventually add some board2 and at least 3 tests with it

def test_get_board():
    set_board(board1)
    assert board1 == get_board()
    #eventually add at least one more test with another board

def test_string_to_location():
    with pytest.raises(ValueError):
        string_to_location('X3')
    assert string_to_location('A0') == (0,0)
    #eventually add at least one more exception test and two more
    #test with correct inputs

def test_location_to_string():
    assert location_to_string((3,4))=='A3'


def test_at():
    assert at((0,0)) in ['M' 'R' '_']
	

def test_all_locations():
    create_board()
    assert len(all_locations())==25
	
def test_adjacent_location():
    assert adjacent_location((2,4),'left') == (4,2)
    
def test_is_legal_move_by_musketeer():
    assert is_legal_move_by_musketeer((0,0),'right')==True
	
    
def test_is_legal_move_by_enemy():
    assert is_legal_move_by_enemy((0,0),'right')==True

def test_is_legal_move():
    assert is_legal_move((0,0),'right')==True

def test_can_move_piece_at():
    assert can_move_piece_at((0,0))==True

def test_has_some_legal_move_somewhere():
    set_board(board1)
    assert has_some_legal_move_somewhere('M') == False
    assert has_some_legal_move_somewhere('R') == True
    # Eventually put at least three additional tests here
    # with at least one additional board

def test_possible_moves_from():
    assert possible_moves_from((2,4))=='up'

def test_is_legal_location():
    assert is_legal_location((0,0))==True

def test_is_within_board():
    assert is_within_board((0,0),'right')==True
	
def test_all_possible_moves_for():
    assert len(all_possible_moves_for('M'))==0
	
def test_make_move():
    make_move((0,4),'right')
    assert 1==1
	
def test_choose_computer_move():
    assert choose_computer_move('M')==((0,0),'up')
    assert choose_computer_move('R')==((0,0),'up')
	
def test_is_enemy_win():
    assert 1==1

