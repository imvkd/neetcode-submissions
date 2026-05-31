class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        org = image[sr][sc]
        dirs = [1, 0, -1, 0, 1]

        if image[sr][sc] == color:
            return image

        def dfs(r, c, org):
            if not 0<=r<m or not 0<=c<n or image[r][c] != org:
                return
            image[r][c] = color
            for d in range(1, len(dirs)):
                dfs(r+dirs[d-1], c+dirs[d], org)

        dfs(sr, sc, org)
        return image