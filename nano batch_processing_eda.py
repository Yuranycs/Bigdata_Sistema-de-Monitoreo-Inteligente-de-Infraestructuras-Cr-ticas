from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg

spark = SparkSession.builder.appName("AnalisisHistorico_DataCenter").getOrCreate()

# 1. Carga de datos
df = spark.read.csv("telemetria.csv", header=True, inferSchema=True)

# 2. Limpieza y Transformación
df_limpio = df.filter(df['temperatura'].isNotNull())

# 3. EDA: Promedio de temperatura por sensor
print("--- RESULTADOS EDA: PROMEDIO POR SENSOR ---")
df_limpio.groupBy("sensor_id").agg(avg("temperatura")).show()

spark.stop()
