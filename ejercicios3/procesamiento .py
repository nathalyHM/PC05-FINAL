
import pandas as pd

def limpiar_columnas(df):
    
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '').str.replace('á', 'a').str.replace('é', 'e').str.replace('í', 'i').str.replace('ó', 'o').str.replace('ú', 'u')

    
    df = df.loc[:, ~df.columns.duplicated()]

    if 'DISPOSITIVO LEGAL' in df.columns:
        df['DISPOSITIVO LEGAL'] = df['DISPOSITIVO LEGAL'].str.replace(',', '')


    columnas_a_eliminar = ['ID', 'TIPO MONEDA']
    df = df.drop(columns=[col for col in columnas_a_eliminar if col in df.columns])

    return df

if __name__ == "__main__":
  
    df_reactiva = pd.read_excel('./data/reactiva.xlsx')
    df_limpiado = limpiar_columnas(df_reactiva)

   
    df_limpiado.to_excel('./data/reactiva_limpiada.xlsx', index=False)

    