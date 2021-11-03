"""
A pyramid is to stack according to one simple principle: each lower at the immediate bottom
 must one block more than the above layer.

Layer	Block used 	Total Blocks
	    at #layer	Used
-----   ----------  ------------
1	    1		    1
2	    2		    3
3	    3		    6
4	    4		    10

The program reads the number of blocks, and outputs the height (total layers) of the pyramid 
that can be built following the above principle for a fully completed layers. 
If insufficient blocks to complete the next layer, report it as unused blocks.
"""

blocks = int(input("Enter the number of blocks: "))

height = int(0)
blockUsed = int(0)

while (blocks >= blockUsed):
    height += 1
    blockUsed = blockUsed + height
    if (blockUsed > blocks):
        blockUsed = blockUsed - height
        height -= 1
        break
    print("At height [", height,"], the number of blocks used for a complete pyramid is: [", blockUsed,']\n')

print("The final height of the pyramid:", height)
print("The number of blocks used for a complete pyramid:", blockUsed)
print("The number of unused blocks:", blocks - blockUsed)