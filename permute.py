arr = [1,2,3]

def permute(i, arr, current):
    if i == len(arr):
        print(current)
        return

    for each in arr:
        if each not in current:
            current.append(each)
            permute(i+1, arr, current)
            current.pop()

permute(0, arr, [])