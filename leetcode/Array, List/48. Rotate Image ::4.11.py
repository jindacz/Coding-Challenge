48. Rotate Image
Medium

7512

440

Add to List

Share
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Example 2:


Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000


4.11 旋转图像
4.11.1 算法要求
给定nxn的二维矩阵表示一个图像。
将图像顺时针旋转90度。
in-place

例子1:
matrix=【【1，2，3】，【4，5，6】，【7，8，9】】
原地旋转变为：【【7，4，1】，【8，5，2】，【9，6，3】】

4.11.2 解题思路
这道题还是找规律，将一个二维数组旋转后和原数组比较。得到规律，然后验证这个规律是否正确。首先以3x3二维数组做测试。

以a-ij来表示二维数组的元素。基本上就是将二维数组的行转换为列。稍有不同的是，转换后的列是倒序的。那么这道题只需要简单的行列互换，然后将转换后的二维数组中的数组元素倒序一下就可以了。

4.11.3 解题代码

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
        	for j in range(i+1,len(matrix)):
        		matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(len(matrix)):
        	matrix[i].reverse()
        return

很简单的行列互换，然后倒序二维数组中的整组元素。



