# Simple python script to benchmark your cpu
# original project can be found at https://github.com/realKarthikNair/pybmark

import timeit,platform # timeit measures execution time of given code snippet(s)
                       # platform.python_implementation() scraps which python implementation is being used

"""
so basically our benchmarking script tries to
do 0|1|2|3|4|5|6|7|8..... upto 99998 
"""
flag=False
print("<<<Welcome to PyBMark 1.0>>>")
if platform.python_implementation()!="CPython":
    if platform.python_implementation()=="PyPy":
        flag=True
        print("Detected PyPy implementation, to ensure fare results, time taken by your computer would be multipled by 6")
    else:
        print("Detected Jython or ipython, \nProgram is currently optimized only for Cpython and Pypy\n Results shoudn't be used for comparison ! ")
    
bmark_script='"|".join(str(i) for i in range(99999))'


print("Running CPU Benchmark.... ")
print("Please wait until the test ends...")
print("Test 1...")

"""
The raw_score of the cpu is the time taken by it (in seconds)
to iterate the benchmarking script 1000 times in a row
"""

raw_score0=round(timeit.timeit(bmark_script, number=1000), 0)

print("Test 2...")
prime_script='''
def prime_gen(start,end):
    for i in range(start, end):
        for j in range(2,int(i/2)):
            if i%j==0:
                break
        else:
            pass
prime_gen(2,1001)
'''

raw_score1=round(timeit.timeit(prime_script, number=50000 ), 0)
raw_score=raw_score0+raw_score1


"""
Kept expected base+end points to make the code less complicated
This way , the slowest pc would take 300 seconds and
the fastest pc would take one second 
"""
if raw_score>400:raw_score=400
elif raw_score<1:raw_score=1

"""
The criteria is self-explanatory
"""
scoring_criteria={}
scores=[i for i in range (1,401)];c=0
for i in range(400,0,-1):
    scoring_criteria[scores[c]]=i; c+=1
    
    
print("<<<BENCHMARK REPORT>>>\n")

if flag!=True:
    print("Your computer took ",raw_score," seconds to do the operations. \nThe slowest relevant computer is expected to take 400 seconds\nand the fastest computer is expected to take 1 second ! ")
else:
    print("Your computer took ",raw_score," seconds to do the operations.\nThe slowest relevant computer is expected to take 400 seconds\nand the fastest computer is expected to take 1 second ! ")
    print("\nBut since PyPy was used, time taken would be converted to 6 times of the actual taken time ")
    raw_score=int(raw_score*6)
    print("\nNet time is ",raw_score)
    
   


pc_score=scoring_criteria[raw_score]
print(f"\nYour pc scored {round(pc_score/4,2)} points out of 100 ! ")
