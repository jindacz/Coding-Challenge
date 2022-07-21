package week8_session1;
​
class Problem1_Solution {
​
    /*
​
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    UNDERSTAND:
​
    - if source cell already has newColor, return image as it is
    - output: the image (2-D array) after flooding the correct cells
    - constraints:
        * 1 <= numCols, numRows <= 50
        * 0 <= image[i][j], color < 2^16
        * 0 <= sr < numRows
        * 0 <= sc < numCols
     - no specific time/space constraints
​
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    MATCH:
​
    - Perform a BFS/DFS Search through the 2D Array.
​
    (Why is this essentially a graph problem? Because it involves a 2-D array)
    (Is there a relationship between the cells? Yes; if a cell neighbor is not the newColor, then we color it)
    (Can this be solved with recursion? Yes, you can recursively call on the 4-directionally neighbouring cells of the
    current cell.)
​
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    PLAN:
​
    - Store color of the starting cell at coordinates r, c in a variable: sourceColor
    - Check if current cell color at coordinates r, c is not equal to sourceColor; return.
    - If current cell color at coordinates r, c is equal to newColor, return.
      Else, update the current cell color as newColor: image[r][c] = newColor
    - Attempt to flood-fill the neighboring cells by making 4 recursive calls to the function with co-ordinates:
      (r+1, c), (r-1, c), (r, c+1), (r, c-1)
        - Check valid boundaries before flood-filling
    - Print the updated 2D array
​
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    IMPLEMENT:
​
    < see code below >
​
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    REVIEW:
​
    < run through test cases below >
​
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    EVALUATE:
​
    - Time: O(M*N), the size of the entire 2D array (we might have to color each cell)
    - Space: O(N), size of the implicit recursive stack when using DFS. But it's O(1) for auxiliary/temp/extra space
​
    */
    public static void main(String[] args) {
​
        System.out.println("\n+++++ Test Case #1 ++++");
        int[][] result = floodFill(TEST_IMAGE_1, 1, 1, 2);
        printImage(result);
​
        System.out.println("\n+++++ Test Case #2 ++++");
        result = floodFill(TEST_IMAGE_2, 0, 0, 2);
        printImage(result);
​
        System.out.println("\n+++++ Test Case #3 ++++");
        result = floodFill(TEST_IMAGE_3, 1, 1, 2);
        printImage(result);
​
        System.out.println("\n+++++ Test Case #4 ++++");
        result = floodFill(TEST_IMAGE_4, 1, 1, 2);
        printImage(result);
​
        System.out.println("\n+++++ Test Case #5 ++++");
        result = floodFill(TEST_IMAGE_5, 0, 0, 2);
        printImage(result);
​
        System.out.println("\n+++++ Test Case #6 ++++");
        result = floodFill(TEST_IMAGE_6, 0, 0, 2);
        printImage(result);
    }
​
    public static final int[][] TEST_IMAGE_1 = {
            {1, 1, 1},
            {1, 1, 0},
            {1, 0, 1}
    };
​
    public static final int[][] TEST_IMAGE_2 = {
            {0, 0, 0},
            {0, 0, 0}
    };
​
    public static final int[][] TEST_IMAGE_3 = {
            {1, 1, 1, 1},
            {1, 1, 0, 1},
            {1, 0, 1, 0},
            {1, 1, 1, 1}
    };
​
    public static final int[][] TEST_IMAGE_4 = {
            {1, 1, 1, 1},
            {1, 1, 0, 1},
            {1, 0, 1, 0},
            {1, 0, 1, 1}
    };
​
    public static final int[][] TEST_IMAGE_5 = {
            {1},
            {1},
            {1},
            {1},
            {1}
    };
​
    public static final int[][] TEST_IMAGE_6 = {
            {1},
            {1},
            {-99},
            {1},
            {1}
    };
​
    public static void printImage(int[][] image) {
        // Loop through all rows
        for (int[] row : image) {
​
            // Loop through all cells of each row
            for (int cell : row) System.out.print(cell + " ");
​
            // Print a new line after each row
            System.out.print("\n");
        }
    }
​
    public static int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        // save the color at our original starting cell (source) so that we only flood cells that match our starting color
        int sourceColor = image[sr][sc];
​
        // if the source cell already has the new color, just return the image
        if (sourceColor == newColor) {
            return image;
        }
​
        // otherwise if the source cell doesn't have the new color, we flood the source cell
        floodHelper(image, sourceColor, newColor, sr, sc);
​
        return image;
    }
​
    public static void floodHelper(int[][] image, int sourceColor, int newColor, int r, int c) {
        if (image[r][c] == sourceColor) {
            image[r][c] = newColor;
​
            // explore neighbors
            int topRowNeighbor = r - 1;
            int bottomRowNeighbor = r + 1;
            int leftColumnNeighbor = c - 1;
            int rightColumnNeighbor = c + 1;
​
            if (r >= 1) {
                floodHelper(image, sourceColor, newColor, topRowNeighbor, c);
            }
​
            int numRows = image.length;
            if (bottomRowNeighbor < numRows) {
                floodHelper(image, sourceColor, newColor, bottomRowNeighbor, c);
            }
​
            if (c >= 1) {
                floodHelper(image, sourceColor, newColor, r, leftColumnNeighbor);
            }
​
            int numColumns = image[0].length;
            if (rightColumnNeighbor < numColumns) {
                floodHelper(image, sourceColor, newColor, r, rightColumnNeighbor);
            }
        }
    }
​
}