
def floodFill(self, image, sr, sc, color):
    colorized = [[0]*len(image[0]) for _ in range(len(image))] 
    self.colorize(image, colorized, sr, sc, image[sr][sc], color)
    return image

def colorize(self, image, colorized, sr, sc, sourceColor, color):
    if sr>=0 and sr<len(image) and sc>=0 and sc<len(image[0]):
        if image[sr][sc] == sourceColor and colorized[sr][sc] == 0:
            image[sr][sc] = color
            colorized[sr][sc] = 1
            self.colorize(image, colorized, sr-1, sc, sourceColor, color) 
            self.colorize(image, colorized, sr, sc+1, sourceColor, color) 
            self.colorize(image, colorized, sr+1, sc, sourceColor, color) 
            self.colorize(image, colorized, sr, sc-1, sourceColor, color) 
    
def printImage(image):
    # loop through all the rows
    for row in image:
        # loop through all cells of each row
        for cell in row:
            print(f"{cell}", end = ' ')
            
            # print a new line after each row
        print("\n")
    return

# - Time: O(M*N), the size of the entire 2D array (we might have to color each cell)
# - Space: O(N), size of the implicit recursive stack when using DFS. But it's O(1) for auxiliary/temp/extra space

printImage(floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))
print('\n')
printImage(floodFill([[0,0,0],[0,0,0]], 0, 0, 2))
print('\n')
printImage(floodFill([[]], 0, 0, 2))


