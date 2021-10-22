# simple algorithm to find starting point of a linked list
def tortise_and_hare(nums):
    tortise = nums[nums[0]]
    hare = nums[nums[nums[0]]]
    while tortise != hare:
        tortise = nums[tortise]
        hare = nums[nums[hare]]
    pntr1 = tortise
    pntr2 = nums[0]
    while pntr1 != pntr2:
        pntr1 = nums[pntr1]
        pntr2 = nums[pntr2]
    print(pntr1)
