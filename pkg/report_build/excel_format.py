import pandas as import pd
import xlsxwriter

def save_excel(df_report, result_path, model_name):
    """
    df_report is the pandas dataframe

    """
    
    #create writer object
    writer = pd.ExcelWriter(result_path, engine='xlsxwriter')

    #write data to an excel
    df_report.to_excel(writer, sheet_name="results", index=False)
    
    # get the xlsxwriter workbook and sheet object
    workbook = writer.book
    worksheet = writer.sheets['results']

    percent = workbook.add_format({'num_format': '0%'})
    center_align = workbook.add_format({'align':'center'})
    # Aligns text to center
    worksheet.set_column('B:G',50, center_align)
    ## formats percentage columns
    worksheet.set_column('E:E',50,percent )
    worksheet.set_column('G:G',50,percent )


    #Conditional format for cells
    column_range = ["E2:50", "G2:G50"]

    def conditional_formats(col):
        ## format cells colors for judgment
        ng_judgment = workbook.add_format({'bg_color': '#fa5050',
                                        'font_color': '#f50000'})
        need_better_judgment = workbook.add_format({'bg_color': '#ffd333',
                                                    'font_color': '#804800'})
        ok_judgment = workbook.add_format({'bg_color': 'c6efce',
                                        'font_color': '#006100'})


        worksheet.conditional_format(col, {'type': 'cell',
                                            'criteria': 'between',
                                            'minimum' : '.001',
                                            'maximum': '.89',
                                            'format': ng_judgment})
        worksheet.conditional_format(col, {'type': 'cell',
                                           'criteria': 'between',
                                           'minimum': '.90',
                                           'maximum': '.99',
                                           'format': need_better_judgment})
        worksheet.conditional_format(col, {'type': 'cell',
                                           'criteria': '>=',
                                           'value': '.100',
                                           'format': ok_judgment})

    for column in column_range:
        conditional_formats(column)


    small_column_size = ['E:E', 'G:G']
    med_column_size = ['C:C', 'D:D', 'F:F']
    
    worksheet.set_column('A:A', 45.71)
    worksheet.set_column('B:B', 2.86)

    def small_col(col):
        worksheet.set_column(col, 8.71)
        
    def med_col(col):
        worksheet.set_column(col, 15)

    for i in small_column_size:
        small_col(i)

    for i in med_column_size:
        med_col(i)

    writer.save()
    writer.close()