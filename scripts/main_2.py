import pandas as pd

def main():
    filePath1 = "../open-problems-multimodal/test_cite_inputs.h5"
    # for chunk in pd.read_hdf(filePath1, mode='r', key='test_cite_inputs'):
    #     print(chunk)
    with pd.HDFStore(filePath1,'r') as hdf:
        ds = hdf.get(key='test_cite_inputs')
        print(ds.iloc[2:10,1:5])
        

if __name__=="__main__":
    main()