import numpy as np

def split(array, nrows, ncols):
    """Split a matrix into sub-matrices."""

    r, h = array.shape
    return (array.reshape(h//nrows, nrows, -1, ncols)
                 .swapaxes(1, 2)
                 .reshape(-1, nrows, ncols))


def count_occurrences(matrix, value):
    count = 0
    for row in matrix:
        for element in row:
            if element == value:
                count += 1
    return count

def entropy(prob,box_quant):
    h = np.zeros((len(prob),box_quant)) 
    for i in range(len(prob)):
        for j in range(box_quant):            
            if prob[i,j] != 0:
                h[i,j] = -prob[i,j] * np.log(prob[i,j])
    return h.sum(axis=0)

def Basin_Entropy(basin, n):
    values = np.int16(np.unique(basin)) #attractors codes
    Boxes = split(basin, n, n) #boxes
    box_size = n*n
    p = np.ones((len(values),len(Boxes))) #probabilites
    Si = np.ones(len(Boxes))
    Nb = 0
    box_quant = len(Boxes)

    for i in values:
        for j in range(len(Boxes)):
            p[i,j] = count_occurrences(Boxes[j],i)/box_size

    '''
    print(p.shape)
    plt.matshow(p, cmap='nipy_spectral')
    plt.show()
    '''
    Si = entropy(p,box_quant)
    
    for j in range(len(Boxes)):
        Nb = Nb + (1 if len(np.unique(Boxes[j])) > 1 else 0)

    Sb = Si.sum()/len(Boxes)
    Sbb = Si.sum()/Nb
 
    return Sb, Sbb
