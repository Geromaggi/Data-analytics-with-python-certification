import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')
    arreglo = np.array(list).reshape(3,3)
    calculations = {
    'mean' : [(np.mean(arreglo,axis=0)).tolist(),(np.mean(arreglo,axis=1)).tolist(),np.mean(arreglo)],
    'variance' : [(np.var(arreglo,axis=0)).tolist(),(np.var(arreglo,axis=1)).tolist(),np.var(arreglo)],
    'standard deviation' : [(np.std(arreglo,axis=0)).tolist(),(np.std(arreglo,axis=1)).tolist(),np.std(arreglo)],
    'max' : [(np.max(arreglo,axis=0)).tolist(),(np.max(arreglo,axis=1)).tolist(),np.max(arreglo)],
    'min' : [(np.min(arreglo,axis=0)).tolist(),(np.min(arreglo,axis=1)).tolist(),np.min(arreglo)],
    'sum' : [(np.sum(arreglo,axis=0)).tolist(),(np.sum(arreglo,axis=1)).tolist(),np.sum(arreglo)]}     
    return calculations