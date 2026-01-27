import xlsxwriter
import os


def write_to_sheet(cards):

    row = 0

    workbook = xlsxwriter.Workbook('words.xlsx')
    worksheet = workbook.add_worksheet()
    
    for card in cards:

        card_front = card.front
        card_back = card.back

        worksheet.write(row, 0, card.front)
        worksheet.write(row, 1, card.back)

        row+=1
    
    workbook.close()
    
    print("Saved to:", os.path.abspath("words.xlsx"))
