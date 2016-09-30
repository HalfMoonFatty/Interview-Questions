'''
Problem:

An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel. The black pixels are connected, i.e., there is only one black region. 
Pixels are connected horizontally and vertically. Given the location (x, y) of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.


For example, given the following image:

[
"0010",
"0110",
"0100"
]
and x = 0, y = 2,
Return 6.

'''

'''
Solution: find (using binary search) for the 4 boundaries

"000000111000000"
"000000101000000"
"000000101100000"
"000001100100000"

top = search row [0...x], find first row contain 1,
bottom = search row[x+1, row], find first row contian all 0
left = search col[0...y], find first col contain 1,
right = search col[y+1, col], find first col contain all 0

The area is then calculated by the boundaries.
Time complexity: O(m log n + n log m)

'''

class Solution(object):

    def minArea(self, image, x, y):

        # find the max height above x (shrink start DOWN) and below x (shrink end UP)
        def SearchRow(image, start, end, flag):
            while start < end:
                mid = start + (end - start)/2
                if ('1' in image[mid]) == flag:
                    end = mid
                else:
                    start = mid + 1
            return start


        # find the max width, to the left and to the right
        def SearchCol(image, start, end, up, down, flag):
            while start < end:
                mid = start + (end - start)/2
                for row in range(up, down):
                    if image[row][mid] == '1':   # we can shrink or extend mid
                        break                
                if (image[row][mid] == '1') == flag:
                    end = mid
                else:
                    start = mid + 1
            return start



        # up is exactly where start, but down is then end index + 1, so the row range is [up,down)
        up = SearchRow(image,0,x,True)
        down = SearchRow(image, x+1,len(image),False)

        # when search column we need to know the row range 
        left = SearchCol(image,0,y,up,down,True)
        right = SearchCol(image,y+1,len(image[0]),up,down,False)

        # as down is real down + 1, right is real right + 1;
        return (down - up)*(right - left)
