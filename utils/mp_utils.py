def split_index(N, batch_size):
    index = []
    
    for i, j in zip(range(0, N - batch_size, batch_size), range(batch_size, N, batch_size)):
        index.append([i, j])
    
    index[-1][1] = N
    
    return index