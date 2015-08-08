import pandas as pd

def print_version(module_name, module):
    print(module_name + ': ', module.__version__)  
    
def get_data(filetype, path):
    if filetype == 'csv':
        return pd.read_csv(path)
    else:
        print('unsupported file type')


def partition_data(data, field, cut_point):
    testBatch = pd.DataFrame()
    trainingBatch = pd.DataFrame()
    
    trainingMask = data[field] % 10 < cut_point
    testingMask = data[field] % 10 > cut_point
    
    trainingData = data[trainingMask]
    testingData = data[testingMask]
    
    return trainingData, testingData

def make_submission_file(filename, all_ids, events, all_predictions):
    submission = pd.data_frame(index = np.concatenate(all_ids), columns = events,
                               data = np.concatenate(all_predictions))
    submission.to_csv(submission_file, index_label='id', float_format='%.3df')
    
    