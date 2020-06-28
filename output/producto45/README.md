# DP1 - Casos Probables, No Notificados y Confirmados por FIS por comuna: Descripción
Archivo que da cuenta de los casos probables, no notificados y confirmados notificados en cada una de las comunas de Chile, según residencia.

Se entiende por caso probables la persona que cumple los criterios de definición de caso sospechoso con una muestra "indeterminada" a SARS-CoV-2 o bien personas en contacto estrecho con un caso confirmado que desarrollan al menos un síntoma compatible con COVID-19. Para efectos epidemiológicos, los casos probables se considerarán casos confirmados y por ende serán contabilizados dentro de los casos totales. 

Se entiende por caso no notificado la persona que cumple los criterios de de definición de casos sospechoso, probable o confirmado y no está registrada en la plataforma EPIVIGILA.

Se entiende por caso confirmado la persona notificada que cumple con los criterios de definición de caso sospechoso o probable con una muestra positiva de SARS-CoV-2, o bien persona no notificada con un registro de resultado de laboratorio positiva a SARS-CoV-2.

Se entiende por comuna de residencia la comuna que la persona declara como su vivienda habitual. 

# Columnas y valores
El archivo CasosProbablePorComuna.csv contiene las columnas 'Región', ‘Código Región’, 'Comuna', ‘Código comuna’, 'Población', múltiples columnas correspondientes a '[fecha]'. Estas últimas columnas, ‘[fecha]’, contienen los 'Casos Confirmados' reportados por el Ministerio de Salud de Chile en cada una de las fechas que se indican en las respectivas columnas. La columna 'Tasa' contiene el número de casos confirmados por cada 100 mil habitantes de una población. El archivo Covid-19_T.csv es la versión traspuesta (serie de tiempo) del primer archivo. Todos estos valores están separados entre sí por comas (csv).

# Fuente
Informes epidemiológicos publicados periódicamente por el Ministerio de Salud de Chile. Ver en:
https://www.minsal.cl/nuevo-coronavirus-2019-ncov/informe-epidemiologico-covid-19/

A su vez, el Ministerio de Salud utiliza como fuente para la elaboración de estos informes el Sistema de notificación EPIVIGILA, del Departamento de Epidemiología, DIPLAS. 

# Frecuencia de actualización

Cada 2 a 3 días.

# Notas aclaratorias

**Nota aclaratoria 1:** El archivo no contempla los casos con región o comuna desconocida, es decir, aquellos casos en que no se registró la región de vivienda habitual en la notificación o bien son casos con domicilio en el extranjero. 

**Nota aclaratoria 2:** Los informes epidemiológicos del Ministerio de Salud informan del último día contabilizado para efectos de la elaboración de cada uno de ellos, habitualmente con corte a las 21 hrs. 

**Nota aclaratoria 3:** Previo al 15 de abril de 2020 los informes epidemiológicos del Ministerio de Salud no entregaban datos de confirmados notificados en comunas con bajo número de casos, para proteger la identidad de las personas contagiadas. 

**Nota aclaratoria 4:** Acorde a lo informado por Epidemiología MINSAL, los datos de residencia son provisorios a la fecha del último reporte, pues se van actualizando retroactivamente a medida que se confirman casos y evoluciona la investigación epidemiológica.

**Nota aclaratoria 5:** Los datos de población provienen de las proyecciones estadísticas del INE, con base en el CENSO 2017 (para más detalles revisar https://www.ine.cl/estadisticas/sociales/demografia-y-vitales/proyecciones-de-poblacion).
