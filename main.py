
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from DataImporter import DataImporter

if __name__ == '__main__':
    #print(pd.DataFrame([1, 2, 3]))
    di = DataImporter()
    di.put_csv_into_df("C:/Users/user/Documents/B.A. Governance Sem.6/Heidelberg Master/macropy/testfile.csv")
    print(di.data)

#scheun wie linearmodels hier rein!!!
