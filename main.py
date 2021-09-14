
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from DataImporter import DataImporter
from MacroModel import MacroModel

if __name__ == '__main__':

    di = DataImporter()
    di.put_csv_into_df("C:/Users/user/Documents/B.A. Governance Sem.6/Heidelberg Master/macropy/testfile.csv")
    print(di.data)

    model = MacroModel()
    print(model.test_method())