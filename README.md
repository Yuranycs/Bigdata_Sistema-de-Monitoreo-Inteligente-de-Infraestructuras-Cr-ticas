# Bigdata_Sistema-de-Monitoreo-Inteligente-de-Infraestructuras-Cr-ticas
Se realizará la implementación de un sistema de monitoreo inteligente para la detección temprana de anomalías térmicas y de humedad en infraestructuras críticas (Data Centers o plantas industriales). El objetivo es prevenir fallos en equipos sensibles mediante el análisis de grandes volúmenes de telemetría, transformando datos crudos en indicadores preventivos.

Conjunto de Datos Seleccionado
Datos Históricos (Batch): Un dataset de registros ambientales que incluye marcas de tiempo, identificador de sensor, temperatura y humedad
Datos en Tiempo Real (Streaming): Flujo de eventos generado sintéticamente que simula lecturas de sensores enviadas a un clúster de Kafka.
Procesamiento en Batch 
Carga y Limpieza: El script batch_processing_eda.py carga el CSV, filtra valores nulos y prepara los datos.
Análisis: Utilizamos DataFrames para calcular el promedio de temperatura por sensor, cumpliendo con la fase de análisis exploratorio.
Visualización: Los resultados se muestran en tablas directamente en la consola de Spark.
Procesamiento: Implementaste un filtro lógico (temperatura > 30) para detectar alertas, lo cual cuenta como análisis de eventos.
Visualización: Usamos el formato console para ver los "batches" de alertas y la Spark Web UI para monitorear el rendimiento.
