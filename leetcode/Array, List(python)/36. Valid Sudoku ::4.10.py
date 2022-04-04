36. Valid Sudoku
Medium

4146

653

Add to List

Share
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:


Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.

4.10有效的数独
4.10.1 算法要求
判断一个9*9的数独是否有效，只需要根据以下规则验证填入的数字是否有效即可。
·1-9在每一行列出现一次
·1-9在每一个粗实线3*3宫内只能出现一次

这是一个部分填充的有效的数独。数独部分空格已填入了数字，空白格用"."表示。

说明：
·一个有效的数独不一定是可解的
·只需要根据规则验证填入的数字是否有效即可
·给定数独序列之包含1-9和字符"."
·给定数独9*9

4.10.2 解题思路
按照题目要求，只能遍历。首先将9x9的数独按照行列块分解开来。
然后按照行列块将数独分别存入一个二维数组中。其中存入行的数据最好办，将board换个名字就是按行分解的二维数组。以遍历的方式将board的元素存入而为行数组rows的代码如下：
for I in range(9):
	for j in range(9):
		rows[i].append(board[i][j])
存入列的数据稍微麻烦点。board本身就是一个二维数组。每遍历board的一行，而位列数组column是能促成纳入一个元素，其代码如下：

for I in range(9):
	for j in range(9):
		columns[j].append(board[i][j])

存入块是最麻烦的。因为按照块的分布，没有行列那么规律。第0块的数据需要存入到block【0】去。因此blocks【0】=【board【0】【0】，board01，board02，board10，board11，board12，board20，board21，board22】。按照这个规律，可以退出blocks【i//3*3+j//3】=boardij。因此按照块存入数据的代码如下。

for I in range(9):
	for j in range(9):
		blocks[i//3*3+j//3].append(board[i][j])
将board按照行列块存入rows，columns，blocks后，遍历行列块，用比较集合前后的长度就可以得知有没有重复的数字。

4.10.3解题代码

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows=[[] for i in range(9)] #使用列表推导创建了9个空白的子列表难，将1维列表变成了2维
        columns=[[] for i in range(9)]
        blocks=[[] for i in range(9)]

        for i in range(9):
        	for j in range(9):
        		if board[i][j]==".": #排除空白的位置
        			pass
        		else:
        			rows[i].append(board[i][j])
        			columns[j].append(board[i][j])
        			blocks[i//3*3+j//3].append(board[i][j])
        for B2L in rows,columns,blocks:
        	for subList in B2L:
        		if not len(subList)==len(set(subList)): #用集合后比较长度的方式来判断是否有重复的数组
        			return False
        return True