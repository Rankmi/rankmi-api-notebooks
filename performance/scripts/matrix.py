from base import constants as C

def build_matrix_data(item):
    matrix, talent = item['generalAverage']['evaluationDomain'], item['talent']
    a={}
    if matrix: 
        a['Resultado Final'] = matrix['label'] if matrix['label'] else C.EMPTY_DATA
        if talent['calibrationStatus'] == 2:
            a['Resultado Final Calibrado'] = matrix['label'] if matrix['label'] else C.EMPTY_DATA
        elif(matrix['calibrationLabel'] == None and talent['calibrationStatus'] == 1):    
            a['Resultado Final Calibrado'] = matrix['label'] if matrix['label'] else C.EMPTY_DATA
        else:
            a['Resultado Final Calibrado'] = matrix['calibrationLabel'] if matrix['calibrationLabel'] else C.EMPTY_DATA 
                
    return a