def seq( num):
    if( num ==1):
        return 1
    else:
        return num*num + seq(num-1)


