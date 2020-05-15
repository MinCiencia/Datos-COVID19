'''
MIT License

Copyright (c) 2020 Sebastian Cornejo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

"""
Los productos que salen del informe epidemiologico son:
1
2
6
15
16
18
19
25
28
"""

import utils
import pandas as pd
from shutil import copyfile
import glob
import re

def prod1(fte, producto):
    # Generando producto 1
    print('Generando producto 1')
    df = pd.read_csv(fte, dtype={'Codigo region': object, 'Codigo comuna': object})
    df.dropna(how='all', inplace=True)
    utils.regionName(df)
    # Drop filas de totales por region
    todrop = df.loc[df['Comuna'] == 'Total']
    df.drop(todrop.index, inplace=True)
    df.to_csv(producto + '.csv', index=False)
    df_t = df.T
    df_t.to_csv(producto + '_T.csv', header=False)
    identifiers = ['Region','Codigo region','Comuna','Codigo comuna','Poblacion']
    variables = [x for x in df.columns if x not in identifiers]
    variables.remove('Tasa')
    df_std = pd.melt(df, id_vars=identifiers, value_vars=variables, var_name='Fecha', value_name='Casos confirmados')
    df_std.to_csv(producto + '_std.csv', index=False)


def prod2(fte, producto):
    print('Generando producto 2')
    df = pd.read_csv(fte, dtype={'Codigo region': object, 'Codigo comuna': object})
    df.dropna(how='all', inplace=True)
    utils.regionName(df)
    # Drop filas de totales por region
    todrop = df.loc[df['Comuna'] == 'Total']
    df.drop(todrop.index, inplace=True)
    #print(df.columns)
    dates = []
    for eachColumn in df.columns:
        if '2020' in eachColumn:
            dates.append(eachColumn)
    #print('las fechas son ' + str(dates))
    for eachdate in dates:
        filename = eachdate + '-CasosConfirmados.csv'
        print('escribiendo archivo ' + filename)
        aux = df[['Region', 'Codigo region', 'Comuna', 'Codigo comuna', 'Poblacion', eachdate]]
        aux.rename(columns={eachdate: 'Casos Confirmados'}, inplace=True)
        aux.to_csv(producto + filename, index=False)


def prod15(fte, producto):
    print('Generando producto 15')
    df = pd.read_csv(fte, dtype={'Codigo region': object, 'Codigo comuna': object})
    df.dropna(how='all', inplace=True)
    utils.regionName(df)
    # Drop filas de totales por region
    todrop = df.loc[df['Comuna'] == 'Total']
    df.drop(todrop.index, inplace=True)
    df.to_csv(producto + '.csv', index=False)
    df_t = df.T
    df_t.to_csv(producto + '_T.csv', header=False)
    copyfile('../input/InformeEpidemiologico/SemanasEpidemiologicas.csv', '../output/producto15/SemanasEpidemiologicas.csv')
    identifiers = ['Region', 'Codigo region', 'Comuna', 'Codigo comuna', 'Poblacion']
    variables = [x for x in df.columns if x not in identifiers]
    df_std = pd.melt(df, id_vars=identifiers, value_vars=variables, var_name='Semana Epidemiologica', value_name='Casos confirmados')
    df_std.to_csv(producto + '_std.csv', index=False)


def prod15Nuevo(fte, prod):
    data = []
    for file in glob.glob(fte + '/*FechaInicioSintomas.csv'):
        date = re.search("\d{4}-\d{2}-\d{2}", file).group(0)
        df = pd.read_csv(file, sep=",", encoding="utf-8", dtype={'Codigo region': object, 'Codigo comuna': object})
        df.dropna(how='all', inplace=True)
        # Drop filas de totales por region
        todrop = df.loc[df['Comuna'] == 'Total']
        df.drop(todrop.index, inplace=True)
        # Hay semanas epi que se llam S en vez de SE
        for eachColumn in list(df):
            if re.search("S\d{2}", eachColumn):
                print("Bad name " + eachColumn)
                df.rename(columns={eachColumn: eachColumn.replace('S', 'SE')}, inplace=True)
        # insert publicacion as column 5
        #df['Publicacion'] = date
        df.insert(loc=5, column='Publicacion', value=date)
        data.append(df)

    #normalization
    data = pd.concat(data)
    data = data.fillna(0)
    utils.regionName(data)
    data.to_csv(prod + '.csv', index=False)
    identifiers = ['Region', 'Codigo region', 'Comuna', 'Codigo comuna', 'Poblacion', 'Publicacion']
    variables = [x for x in data.columns if x not in identifiers]
    df_std = pd.melt(data, id_vars=identifiers, value_vars=variables, var_name='Semana Epidemiologica',
                     value_name='Casos confirmados')
    df_std.to_csv(prod + '_std.csv', index=False)

    copyfile('../input/InformeEpidemiologico/SemanasEpidemiologicas.csv',
             '../output/producto15/SemanasEpidemiologicas.csv')

    #create old prod 15 from latest adition
    latest = max(data['Publicacion'])
    print(latest)
    latestdf =data.loc[data['Publicacion'] == latest]
    print(latestdf)
    latestdf.drop(['Publicacion'], axis=1, inplace=True)
    latestdf.to_csv(prod.replace('Historico', '.csv'), index=False)

    df_t = latestdf.T
    df_t.to_csv(prod.replace('Historico', '_T.csv'), header=False)

    identifiers = ['Region', 'Codigo region', 'Comuna', 'Codigo comuna', 'Poblacion']
    variables = [x for x in latestdf.columns if x not in identifiers]
    df_std = pd.melt(latestdf, id_vars=identifiers, value_vars=variables, var_name='Semana Epidemiologica',
                     value_name='Casos confirmados')
    df_std.to_csv(prod.replace('Historico', '_std.csv'), index=False)



def prod16(fte, producto):
    print('Generando producto 16')
    copyfile(fte, producto + '.csv')
    df2_t = utils.transpone_csv(producto + '.csv')
    df2_t.to_csv(producto + '_T.csv', header=False)
    df = pd.read_csv(fte)
    identifiers = ['Grupo de edad','Sexo']
    variables = [x for x in df.columns if x not in identifiers]
    df_std = pd.melt(df, id_vars=identifiers, value_vars=variables, var_name='Fecha',
                     value_name='Casos confirmados')
    df_std.to_csv(producto + '_std.csv', index=False)


def prod18(fte, producto):
    df = pd.read_csv(fte, dtype={'Codigo region': object, 'Codigo comuna': object})
    df.dropna(how='all', inplace=True)
    df.to_csv(producto + '.csv', index=False)
    df_t = df.T
    df_t.to_csv(producto + '_T.csv', header=False)
    identifiers = ['Region','Codigo region','Comuna','Codigo comuna','Poblacion']
    variables = [x for x in df.columns if x not in identifiers]
    df_std = pd.melt(df, id_vars=identifiers, value_vars=variables, var_name='Fecha',
                     value_name='Tasa de incidencia')
    df_std.to_csv(producto + '_std.csv', index=False)


def prod19_25(fte, producto):
    df = pd.read_csv(fte, dtype={'Codigo region': object, 'Codigo comuna': object})
    df.dropna(how='all', inplace=True)
    df.to_csv(producto + '.csv', index=False)
    df_t = df.T
    df_t.to_csv(producto + '_T.csv', header=False)
    identifiers = ['Region', 'Codigo region', 'Comuna', 'Codigo comuna', 'Poblacion']
    variables = [x for x in df.columns if x not in identifiers]
    if '19' in producto:
        df_std = pd.melt(df, id_vars=identifiers, value_vars=variables, var_name='Fecha',
                     value_name='Casos activos')
    elif '25' in producto:
        df_std = pd.melt(df, id_vars=identifiers, value_vars=variables, var_name='Fecha',
                             value_name='Casos actuales')
    df_std.to_csv(producto + '_std.csv', index=False)

def prod28(fte, producto):
    print('Generando producto 28')
    df = pd.read_csv(fte, dtype={'Codigo region': object})
    df.dropna(how='all', inplace=True)
    #utils.regionName(df)
    # Drop filas de totales por region
    df.to_csv(producto + '.csv', index=False)
    df_t = df.T
    df_t.to_csv(producto + '_T.csv', header=False)
    identifiers = ['SEREMI notificacion', 'Codigo region']
    variables = [x for x in df.columns if x not in identifiers]
    df_std = pd.melt(df, id_vars=identifiers, value_vars=variables,var_name='Semana Epidemiologica', value_name='Casos confirmados')
    df_std.to_csv(producto + '_std.csv', index=False)


if __name__ == '__main__':

    prod1('../input/InformeEpidemiologico/CasosAcumuladosPorComuna.csv', '../output/producto1/Covid-19')

    prod2('../input/InformeEpidemiologico/CasosAcumuladosPorComuna.csv', '../output/producto2/')

    print('Generando producto 6')
    exec(open('bulk_producto2.py').read())

    #prod15('../input/InformeEpidemiologico/FechaInicioSintomas.csv', '../output/producto15/FechaInicioSintomas')

    print('Generando producto 15')
    prod15Nuevo('../input/InformeEpidemiologico/', '../output/producto15/FechaInicioSintomasHistorico')

    prod16('../input/InformeEpidemiologico/CasosGeneroEtario.csv', '../output/producto16/CasosGeneroEtario')

    print('Generando producto 18')
    prod18('../input/InformeEpidemiologico/TasaDeIncidencia.csv', '../output/producto18/TasaDeIncidencia')

    print('Generando producto 19')
    prod19_25('../input/InformeEpidemiologico/CasosActivosPorComuna.csv', '../output/producto19/CasosActivosPorComuna')

    print('Generando producto 25')
    prod19_25('../input/InformeEpidemiologico/CasosActualesPorComuna.csv', '../output/producto25/CasosActualesPorComuna')

    prod28('../input/InformeEpidemiologico/FechaInicioSintomas_reportadosSEREMI.csv', '../output/producto28/FechaInicioSintomas_reportadosSEREMI')
