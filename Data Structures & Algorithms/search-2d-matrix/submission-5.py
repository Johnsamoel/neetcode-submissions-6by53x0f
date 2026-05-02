class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top , bottom = 0, len(matrix) - 1

        while top <= bottom:
            mid_row = top + ((bottom - top) // 2)

            if target >= matrix[mid_row][0] and target <= matrix[mid_row][-1]:
                l , r = 0, len(matrix[mid_row]) - 1
                
                while l <= r:
                    mid = l + ((r - l) // 2)

                    if  matrix[mid_row][mid] == target:
                        return True
                    elif matrix[mid_row][mid] < target:
                        l = mid + 1
                    else:
                        r = mid - 1

                return False
            elif matrix[mid_row][0] < target:
                top = mid_row + 1 
            else:
                bottom = mid_row - 1
    
        return False
                        
