import pandas as pd

def append_to_excel(df):
    pass


def model_df(label_target, stiff_pct, model_name):
    stiff_label = model_name + ' (N/mm)'
    label_with_target = pd.DataFrame(label_target, columns=[
                                     'id', 'location', 'node', 'dir', 'Target(N/mm)', 'model_id'])

    stiffness_w_percent = pd.DataFrame(
        stiff_pct, columns=[stiff_label, '%target'])
    # append to the large excel, 
    
    combine_table = pd.concat([label_with_target, stiffness_w_percent], axis=1, sort=False)
    
    drop_columns = ['id', 'node', 'model_id']
    clean_table = combine_table.drop(columns=drop_columns)

    print(clean_table)
