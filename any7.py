nums_seven = list(range(0,10))
nums_no_seven = list(range(0,10,2))


def any7(nums):
    for n in nums:
        if n == 7:
            print('Found a 7!')
            return n
    print('No 7s found')


