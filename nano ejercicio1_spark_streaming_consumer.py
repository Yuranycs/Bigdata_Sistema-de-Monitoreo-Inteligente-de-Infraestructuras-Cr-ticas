nano ejercicio1_spark_streaming_consumer.py

from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, DoubleType

# Definición del esquema
schema = StructType([
    StructField("sensor_id", StringType()),
    StructField("temperatura", DoubleType()),
    StructField("humedad", DoubleType()),
    StructField("timestamp", DoubleType())
])

spark = SparkSession.builder.appName("Streaming_Anomalias_DataCenter").getOrCreate()
spark.sparkContext.setLogLevel("WARN")

# Lectura de Kafka
df_raw = spark.readStream.format("kafka").option("kafka.bootstrap.servers", "localhost:9092").option("subscribe", "sensor_data").load()

# Procesamiento: Filtrado de alertas (> 30 grados)
df_data = df_raw.selectExpr("CAST(value AS STRING)").select(from_json(col("value"), schema).alias("data")).select("data.*")
alertas = df_data.filter(col("temperatura") > 30)

# Visualización
query = alertas.writeStream.outputMode("append").format("console").start()
query.awaitTermination()
