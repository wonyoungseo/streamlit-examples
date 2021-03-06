from io import BytesIO
import base64
import pandas as pd
import xlsxwriter


def column_name_2_label(df, column_name):
    column_idx = list(df.columns).index(column_name)
    column_label = xlsxwriter.utility.xl_col_to_name(column_idx)
    return column_label


def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.loc[:, 'qc_result'] = None
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    col_label = column_name_2_label(df, 'qc_result')

    workbook = writer.book
    worksheet = writer.sheets['Sheet1']

    worksheet.data_validation('{0}{1}:{0}{2}'.format(col_label, 2, len(df) + 1),
                              {'validate': 'list', 'source': ['ACCEPT', 'REJECT']})
    writer.save()
    processed_data = output.getvalue()
    return processed_data


def get_download_link(df, file_name):

    val = to_excel(df)
    b64 = base64.b64encode(val)

    href = f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{file_name}">Download excel file</a>'  # decode b'abc' => abc
    return href