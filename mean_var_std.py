import numpy as np
def calculate(list):
    print(len(list))
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    else:
        print(list)
        mat=np.array(list).reshape(3,3)
        print(mat)
        mean=[np.mean(mat,axis=0).tolist(),np.mean(mat,axis=1).tolist(),mat.flatten().mean()]

        var=[np.var(mat,axis=0).tolist(),np.var(mat,axis=1).tolist(),mat.flatten().var()]
  
        std=[np.std(mat,axis=0).tolist(),np.std(mat,axis=1).tolist(),mat.flatten().std()]

        max=[np.max(mat,axis=0).tolist(),np.max(mat,axis=1).tolist(),mat.flatten().max()]
  
        min=[np.min(mat,axis=0).tolist(),np.min(mat,axis=1).tolist(),mat.flatten().min()]
     
        sum=[np.sum(mat,axis=0).tolist(),np.sum(mat,axis=1).tolist(),mat.flatten().sum()]
      
        
        calculation = {
            'mean':mean,
            'variance':var,
            'standard deviation':std,
            'max':max,
            'min':min,
            'sum':sum
        }
        return calculation
    

