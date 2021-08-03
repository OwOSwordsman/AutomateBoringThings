import openpyxl


def main():
    wb = openpyxl.Workbook()
    sheet = wb['Sheet']
    sheet["A1"] = "poop"
    sheet["A2"] = "pee"
    wb.save('test.xlsx')


if __name__ == "__main__":
    main()
