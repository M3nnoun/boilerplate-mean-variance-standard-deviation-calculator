import numpy as np

def calculate(list):
    matrix=np.array(list,)
    try:
        m=np.reshape(matrix,(3,3))
        calculations={
                'mean': [np.mean(m,axis=0).tolist(), np.mean(m,axis=1).tolist(), np.mean(m).tolist()],
                'variance': [np.var(m,axis=0).tolist(), np.var(m,axis=1).tolist(), np.var(m).tolist()],
                'standard deviation': [np.std(m,axis=0).tolist(), np.std(m,axis=1).tolist(), np.std(m).tolist()],
                'max': [np.max(m,axis=0).tolist(), np.max(m,axis=1).tolist(), np.max(m).tolist()],
                'min': [np.min(m,axis=0).tolist(), np.min(m,axis=1).tolist(), np.min(m).tolist()],
                'sum': [np.sum(m,axis=0).tolist(), np.sum(m,axis=1).tolist(), np.sum(m).tolist()]
                }
    except:
        raise ValueError('List must contain nine numbers.')
    return calculations