def count_statuses(statuses: list[str]) -> dict[str,int]:
    counts={}

    for status in statuses:
        counts[status]=counts.get(status,0)+1

    return counts


statuses = [
    "completed",
    "pending",
    "completed",
    "cancelled",
    "pending",
    "completed"
]

print(count_statuses(statuses))


def element_count(numbers):
    count={}

    for n in numbers:
        count[n]=count.get(n,0)+1

    return count


numbers=[1,2,3,4,1,2,4]

print(element_count(numbers))

def second_largest(L):
    largest=second_largest=float('-inf')
    for num in L:
        if num> largest:
            second_largest=largest
            largest=num
        elif largest > num > second_largest:
            second_largest = num
    return second_largest


L = [10, 5, 8, 10, 7, 8]

print(second_largest(L))



## find the first non repeating character
def nrch(name):
    count={}
    for ch in name:
        count[ch]=count.get(ch,0)+1

    for ch in name:
        if count[ch]==1:
            return ch
            break
    return None

name='swwiis'
print(nrch(name))