from re import A
import h5py

def main():
    print("Initializing...")
    filePath1 = "../open-problems-multimodal/test_cite_inputs.h5"
    with h5py.File(filePath1, 'r') as file1:
        print("Group key: %s" % list(file1.keys()))

        group_key = list(file1.keys())[0]
        print("The group key type: %s; The group key: %s" % (type(group_key), group_key))
        print(file1.keys())

        ds_key = list(file1[group_key])
        print("The dataset keys list: %s" % ds_key)

        for ds in ds_key: 
            print(file1[group_key][ds])
        # object_key_0 = ds_key[0]
        # print("The first object key: %s" % object_key_0)

        # data1 = file1[a_group_key][object_key_0]
        # print(data1)

if __name__=="__main__":
    main()