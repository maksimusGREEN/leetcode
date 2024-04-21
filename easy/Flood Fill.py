# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

# You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

# Return the modified image after performing the flood fill.


from typing import List

def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

    current_color = image[sr][sc]
    
    def dfs(sr, sc, color):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] != current_color:
            return
        image[sr][sc] = color
        dfs(sr-1, sc, color)
        dfs(sr+1, sc, color)
        dfs(sr, sc-1, color)
        dfs(sr, sc+1, color)
    
    if image[sr][sc]==color:
        return image
    dfs(sr, sc, color)
    return image
    