from prometheus_client import CollectorRegistry, Gauge, push_to_gateway

# Creamos un registro de métricas
registry = CollectorRegistry()

# Definimos una métrica
g = Gauge('metric_to_test', 'Description of gauge', registry=registry)
g.set(1) 

# Enviamos las métricas al gateway
push_to_gateway('localhost:9091', job='test', registry=registry)
