

# You are given two arrays of integers arrA and arrB.
# arrA contains N elements and arrB contains 2*N elements.
# However, the last N elements of arrB are all zero.
#
# Write a function that merges the N elements of arrA with the first-N elements of arrB sorted, in-place.
#
# ** elements in arrA are sorted. elements in arrB are sorted. **



def sortAB(arrA, arrB):
    N = min(len(arrA), len(arrB))
    result =[]
    queA=0
    queB=0

    while len(result) < 2*N:
        if queA >= N:
            result.append(arrB[queB])
            queB +=1
        elif queB >= N:
            result.append(arrA[queA])
            queA +=1


        elif arrA[queA] < arrB[queB]:
            result.append(arrA[queA])
            queA += 1
        else:
            result.append(arrB[queB])
            queB += 1
    return result




if __name__ == '__main__':

    # test case 1
    A = [1,3,4,7,9]
    B = [2,4,5,10,13,0,0,0,0,0]

    %timeit sortAB(A, B)

    # test case 2

    A = [1]*100
    B = [2]*100+[0]*100

    %timeit sortAB(A, B)

    # test case 3

    A = [ random.randint(0, 100000) for i in xrange(100000)]
    B = [ random.randint(0, 100000) for i in xrange(100000)]

    A.sort()

    B.sort()

    B = B + [0]*100000

    %timeit sortAB(A, B)
