"""
Clone of 2048 game.
"""

#import poc_2048_gui
import random        

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.    
OFFSETS = {UP: (1, 0), 
           DOWN: (-1, 0), 
           LEFT: (0, 1), 
           RIGHT: (0, -1)} 


def add_tup(tuple1, tuple2):
    """
    adds two tuples
    """
    return (tuple1[0] + tuple2[0], tuple1[1] + tuple2[1])

def mult_tup(tuple1, coef):
    """
    multiplies a tuple by a constant
    """
    return (tuple1[0] * coef, tuple1[1] * coef)
   
def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    # replace with your code
    result_list = [0] * len(line)
    available = 0
    for dummy_n in range(0, len(line)):
        if line[dummy_n] != 0:
            result_list[available] = line[dummy_n]
            available += 1
    check_loc = 0
    end_loc = len(result_list) - 1
    length = len(result_list)

    while (check_loc <= (length - 2)):
        if result_list[check_loc] == 0:
            break
        if result_list[check_loc] == result_list[check_loc + 1]:
            result_list[check_loc] += result_list[check_loc + 1]
            for dummy_n in range(check_loc + 1, length - 1):
                result_list[dummy_n] = result_list[dummy_n + 1]
            result_list[end_loc] = 0
            end_loc -= 1
            check_loc += 1
        else:
            check_loc += 1
    return result_list

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self.rows = grid_height
        self.cols = grid_width
        self.reset()
        self.up_list =[(0, n) for n in range(0, self.cols)]
        self.down_list = [(self.rows - 1, n) for n in range(0, self.cols)]
        self.left_list = [(n, 0) for n in range(0, self.rows)]
        self.right_list = [(n, self.cols - 1) for n in range(0, self.rows)]

        self.dir_dict = {UP: self.up_list,
                        DOWN: self.down_list,
                        LEFT: self.left_list,
                        RIGHT: self.right_list}
    
    def reset(self):
        """
        Reset the game so the grid is empty.
        """
        # replace with your code
        self.cells = [ [ 0 for dummy_row in range(self.cols)] for dummy_col in range(self.rows)]
    
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        return self.cells

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self.rows
    
    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self.cols
                            
    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        changed = False
        #current = 0
        if (direction == 'UP' or direction == 'DOWN'):
            length = self.cols  
        else:
            length = self.rows
            
            
        for initial_tile in self.dir_dict[direction]:
            
            temp_list = []
            merge_list = []
            for dummy_n in range(0, length):                
                temp_list.append(add_tup(initial_tile, mult_tup(OFFSETS[direction],dummy_n)))
            
            
            for element in temp_list:
                    
                    merge_list.append(self.cells[element[0]][element[1]])
                    
            add_list = merge(merge_list)

            #print add_list
            #print temp_list
            dummy_n = 0
            for element in temp_list:
                
                #print add_list[n]
                if self.cells[element[0]][element[1]] == add_list[dummy_n] or changed:
                    changed = True
                self.cells[element[0]][element[1]] = add_list[dummy_n]
                dummy_n += 1
        
        #check to see if there are any empty tiles
        empty = False
        
        for dummy_row in range(0, self.rows):
            for dummy_col in range(0, self.cols):
                if self.cells[dummy_row][dummy_col] == 0:
                    empty = True
                    break
            if empty == True:
                break
                
        if changed and empty:
            self.new_tile()
        
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty 
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        rand_row = random.randrange(0, self.rows)
        rand_col = random.randrange(0, self.cols)
        
        rand_num = random.randrange(0, 10)
        #max_count = 16
        #count = 0
        if self.cells[rand_row][rand_col] != 0:
                self.new_tile()  
        else:
            if rand_num < 9:
                self.cells[rand_row][rand_col] = 2
            else:
                self.cells[rand_row][rand_col] = 4
        
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """        
        # replace with your code
        self.cells[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """        
        # replace with your code
        return self.cells[row][col]
 
import poc_2048_gui    
poc_2048_gui.run_gui(TwentyFortyEight(4, 4))


#import poc_simpletest

#def run_test(game_class):
#    
#    suite = poc_simpletest.TestSuite()
#    
#    game = game_class(4, 4)
#    #print "cells: " + str(game.cells)
#    #print "cells: "
#    #print game.cells
#    suite.run_test(merge([2, 0, 2, 4]), [4, 4, 0, 0], "Test #1:")
#    suite.run_test(merge([0, 0, 2, 2]), [4, 0, 0, 0], "Test #2:")
#    suite.run_test(merge([2, 2, 0, 0]), [4, 0, 0, 0], "Test #3:")
#    suite.run_test(merge([2, 2, 2, 2]), [4, 4, 0, 0], "Test #4:")
#    suite.run_test(merge([8, 16, 16, 8]), [8, 32, 8, 0], "Test #5:")
#    suite.run_test(merge([0, 4, 4, 2]), [8, 2, 0, 0], "Test #6:")
#    suite.run_test(game.get_grid_height(), 4, "Test #7:")
#    suite.run_test(game.get_grid_width(), 4, "Test #8:")
#    #game.set_tile(0, 3, 4)
#    #print game.get_tile(0, 3)
#    #for n in range(0, 4):
#    #    game.new_tile()
##        print game.cells
#    #print game.dir_dict['DOWN']
#    game.cells = [[4, 2, 2, 2],
#                  [0, 0, 2, 8],
#                  [4, 2, 2, 8],
#                  [0, 2, 0, 4]]
#    game.move(UP)
#    print game.cells
#    suite.report_results()
#    
#
#run_test(TwentyFortyEight)

#game = TwentyFortyEight(3, 5)
#print game.get_grid_height()
#print game.get_grid_width()
#print game.get_tile(0,0)
##print game.get_tile(2,4)
#print game.cells
