import openpyxl


def main():
    workbook = openpyxl.load_workbook("excel.xlsx")
    sheet = workbook["Sheet1"]
    print(sheet["B2"].value)


    workbook.close()


if __name__ == "__main__":
    main()
