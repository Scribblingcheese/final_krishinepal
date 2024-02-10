import pickle
import math

def make_prediction(ip):
    f = open('model.pkl' , 'rb')
    Models = pickle.load(f)

    f = open('normalization.pkl' , 'rb')
    normalization = pickle.load(f)

    ip = [ip]
  
    ip = normalization.transform(ip)
    
    output = []

    for m in Models:
        output.append(m[0].predict(ip)[0])
        
    return ensemble(list(output))


def ensemble(output):
    op_string = []
    op = dict({})
    for u in list(set(output)):
        op[u] = (output.count(u) / len(output)) * 100 
        op[u] = round(op[u],2)


    op_list = sorted(op.items(),key=lambda x:x[1] ,reverse=True)

    for crop in op_list:
        op_string.append(str(crop[0]).capitalize() +" : "+ str(crop[1])+"%"+" ")

    return op_string