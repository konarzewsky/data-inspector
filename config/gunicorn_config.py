import os

bind = "0.0.0.0:5000"
workers = os.getenv("N_WORKERS", 1)
worker_class = "sync"
accesslog = "-"
