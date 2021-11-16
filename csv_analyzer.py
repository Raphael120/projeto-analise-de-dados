import pandas as pd


def read_csv(filepath):
    return pd.read_csv(filepath)


def read_as_list(filepath):
    df = read_csv(filepath)
    return df.values.tolist()


def analyse(filepath):
    df = read_csv(filepath)
    
    # Soma das Vendas
    sum_sales = df.groupby('Date').sum().reset_index()
    
    # Quantidade de Vendas
    qty_sales = df.groupby('Date').count().reset_index()
    
    # Valor minimo
    min_value = sum_sales['Sale'].min()
    row_min_value = sum_sales[sum_sales['Sale'] == min_value]
    
    # Valor máximo
    max_value = sum_sales['Sale'].max()
    row_max_value = sum_sales[sum_sales['Sale'] == max_value]
    
    # Quantidade minima
    min_qty = qty_sales['Sale'].min()
    row_min_qty = qty_sales[qty_sales['Sale'] == min_qty]
    
    # Quantidade máxima
    max_qty = qty_sales['Sale'].max()
    row_max_qty = qty_sales[qty_sales['Sale'] == max_qty]
    
    dict_result = {
        'min_value': {
            'date': row_min_value['Date'].values[0],
            'value': row_min_value['Sale'].values[0],
        },
        'max_value': {
            'date': row_max_value['Date'].values[0],
            'value': row_max_value['Sale'].values[0],
        },
        'min_qty': {
            'date': row_min_qty['Date'].values[0],
            'value': row_min_qty['Sale'].values[0],
        },
        'max_qty': {
            'date': row_max_qty['Date'].values[0],
            'value': row_max_qty['Sale'].values[0],
        },
    }
    
    return dict_result


result = analyse('planilha.csv')
