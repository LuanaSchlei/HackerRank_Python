




if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    mx = - 101
    seg_mx = - 101

    for i in arr:

        if i > mx:
            seg_mx = mx
            mx = i
        if i > seg_mx and i < mx:
            seg_mx = i
    print('Segunda pontuacao mais alto:', seg_mx)
            




