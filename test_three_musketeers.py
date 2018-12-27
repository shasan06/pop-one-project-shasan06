Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import pytest
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

board2 =  [ [_, M, _, R, _],
            [_, _, R, M, _],
            [M, R, _, R, _],
            [_, R, _, R, _],
            [_, _, R, R, _] ]
			
board3 =  [ [r, r, r, r, m],
            [r, r, r, r, r],
            [r, r, m, r, r],
            [r, r, r, r, r],
            [m, r, r, r, r] ]
			
board4 =  [ [_, R_, _,M,_],
            [_, R, _, _, _],
            [R, _, M, _, _],
            [_, R, _, _, _],
            [R, _, _, M, _] ]	
			
board5 =  [ [_, R, _, M, _],
            [_, R, _, _, _],
            [R, _, _, M, _],
            [_, R, _, _, _],
            [R, _, _, M, _] ]
			
board6 =  [ [_, R, _, R, _],
            [_, R, _, _, _],
            [R, _, M, M, M],
            [_, R, _, _, _],
            [R, _, _, R, _] ]			

			
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
    assert at((0,2)) == _
    assert at((1,3)) == M
    assert at((3,1)) == R     
	set_board(board2)
    assert at((0,0)) == _
    assert at((1,3)) == M
    assert at((3,1)) == R    
    #eventually add some board2 and at least 3 tests with it

def test_get_board():
    set_board(board1)
    board0 == get_board()
    assert board0[0][2] == _
    assert board0[1][3] == M
    assert board0[3][1] == R  
    #eventually add at least one more test with another board

def test_string_to_location():
    with pytest.raises(ValueError):
        string_to_location('X3')
		#???
    assert string_to_location('A4') == (0,3)
	assert string_to_location('E1') == (4,0)
	assert string_to_location('C3') == (2,2)
	
    #eventually add at least one more exception test and two more
    #test with correct inputs

def test_location_to_string():
    with pytest.raises(ValueError):
        location_to_string((6,9))
		#???

    assert location_to_string((3,4)) == 'A3'
	assert location_to_string((0,3)) == 'A4'
	assert location_to_string((4,0)) == 'E1'
	assert location_to_string((2,2)) == 'C3'


def test_at():
    for i in range(0,5):
	    for j in range(0,5):
            assert at((i,j)) in ['M' 'R' '_']
    set_board(board1)
    assert at((0,2)) == _
    assert at((1,3)) == M
    assert at((3,1)) == R 	

def test_all_locations():
    create_board()
    assert len(all_locations())==5
	for i in [0,1,2,3,4]:
		assert len(board[i]) == 5
		for j in range(5):
			if (i==0 and j==4) or (i==2 and j==2) or (i==4 and j==0):
				assert at((i,j)) == M
			else:
				assert at((i,j)) == R
	
def test_adjacent_location():

    assert adjacent_location((2,4),'left') == (2,3)
    assert adjacent_location((0,3),'down') == (1,3)
    assert adjacent_location((1,4),'up') == (0,4)
    assert adjacent_location((4,1),'right') == (4,2)
 
	
def test_is_legal_move_by_musketeer():
    set_board(board1)
    assert is_legal_move_by_musketeer((1,3),'left')==True
    assert is_legal_move_by_musketeer((2,2),'right')==True	
    assert is_legal_move_by_musketeer((2,2),'up')==True
    assert is_legal_move_by_musketeer((1,3),'right')==False
    assert is_legal_move_by_musketeer((1,3),'down')==True
	#???exception
def test_is_legal_move_by_enemy():
    set_board(board1)
    assert is_legal_move_by_enemy((0,0),'right')==False
	assert is_legal_move_by_enemy((1,2),'left')==True
	assert is_legal_move_by_enemy((0,3),'down')==False
	assert is_legal_move_by_enemy((2,1),'up')==True
	assert is_legal_move_by_enemy((1,3),'down')==False
	

def test_is_legal_move():
    set_board(board1)
    assert is_legal_move((0,0),'right')==True
	assert is_legal_move((1,2),'left')==True
	assert is_legal_move((0,3),'down')==False
	assert is_legal_move((2,3),'right')==True
	assert is_legal_move((1,3),'down')==False

def test_can_move_piece_at():
    set_board(board1)
    assert can_move_piece_at((0,0))==True
	assert can_move_piece_at((1,2))==True
	assert can_move_piece_at((0,3))==False
	assert can_move_piece_at((2,3))==True
	assert can_move_piece_at((1,3))==False

def test_has_some_legal_move_somewhere():
    set_board(board1)
    assert has_some_legal_move_somewhere('M') == True
    assert has_some_legal_move_somewhere('R') == True
	set_board(board4)
	assert has_some_legal_move_somewhere('M') == False
	assert has_some_legal_move_somewhere('R') == True
    # Eventually put at least three additional tests here
    # with at least one additional board

def test_possible_moves_from():
    set_board(board1)
    assert possible_moves_from((2,4))=='up'
    assert possible_moves_from((3,2))=='down'
    assert possible_moves_from((2,3))=='right'	
	assert possible_moves_from((0,4))=='left'
    

def test_is_legal_location():
    set_board(board1)
    assert is_legal_location((1,3))==True
	assert is_legal_location((0,3))==True
	assert is_legal_location((2,2))==True
	assert is_legal_location((3,0))==True

def test_is_within_board():
    set_board(board1)
    assert is_within_board((2,2),'right')==True
	assert is_within_board((3,1),'left')==True
	assert is_within_board((1,2),'up')==True
	assert is_within_board((3,2),'down')==False
	
def test_all_possible_moves_for():
    set_board(board1)
    assert len(all_possible_moves_for('M'))==((1,2),left)
	assert len(all_possible_moves_for('M'))==((2,3),down)
	assert len(all_possible_moves_for('M'))==((2,1),left)
	assert len(all_possible_moves_for('M'))==((2,3),right)
	assert len(all_possible_moves_for('R'))==((1,1),left)
	assert len(all_possible_moves_for('R'))==((1,2),up)
	assert len(all_possible_moves_for('R'))==((2,0),left)
	assert len(all_possible_moves_for('R'))==((3,0),left)
	assert len(all_possible_moves_for('R'))==((4,1),down)
	assert len(all_possible_moves_for('R'))==((4,2),left)
	assert len(all_possible_moves_for('R'))==((4,4),right)
	
def test_make_move():
    set_board(board1)
    make_move((1,2),'left')
    assert at((1,2)) == _
    assert at((1,1)) == R
    make_move((2,2),'right')
    assert at((2,2)) == _
    assert at((2,3)) == M
    make_move((3,1),down)
    assert at((3,1)) == _
    assert at((4,1)) == R

    
	
def test_choose_computer_move():
    assert choose_computer_move('M')==((0,0),'up')
    assert choose_computer_move('R')==((0,0),'up')
	
def test_is_enemy_win():
    set_board(board1)
	assert is_enemy_win() == False
	
	set_board(board2)
	assert is_enemy_win() == False
	
	set_board(board3)
	assert is_enemy_win() == False
	
	set_board(board4)
	assert is_enemy_win() == False
	
	set_board(board5)
	assert is_enemy_win() == True
	
	set_board(board6)
	assert is_enemy_win() == True
© 2018 GitHub, Inc.
