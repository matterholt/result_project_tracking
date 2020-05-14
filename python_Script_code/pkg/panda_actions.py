import pandas as pd
from .report_build.excel_format import save_excel
import os.path


def filter_keyValue(df):
    key_val = r"Templates_csv/key_values.csv"
    key_value_df = pd.read_csv(key_val, header=0)

    key_results = pd.merge(key_value_df, df, how='left',
                           on=['Loc.', 'Dir'])
    return key_results


def build_Report(report_data, model_detail):
    '''
    append the results to the master excel
    '''
    # !! better to have the the link past in from main file,
    report_loc = os.path("./Results/", model_detail.name, ".xlsx")

    row_label_df = pd.DataFrame(
        report_data['row_labels'], columns=['Loc.', 'Dir'])

    target_df = pd.DataFrame(
        report_data['target_stiff'], columns=['Target(N/mm)', ])

    baseName = model_detail.base + '(N/mm)'
    base_df = pd.DataFrame(report_data['base_stiff_vals'], columns=[
                           baseName, '%target'])

    modelName = model_detail.name + ('N/mm')
    model_df = pd.DataFrame(report_data['model_stiff_vals'], columns=[
        modelName, '%target'])

    combine_table = pd.concat(
        [row_label_df, target_df, base_df, model_df], axis=1, sort=False)

    key_value_report = filter_keyValue(combine_table)
    save_excel(key_value_report, report_loc, model_detail.name)
