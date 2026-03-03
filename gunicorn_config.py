"""
Gunicorn production configuration for MedSecure-Check.
Optimized for resource-constrained environments (Free/Starter tiers).
"""

import multiprocessing
import os

# Binding
bind = f"0.0.0.0:{os.getenv('PORT', '8080')}"

# Worker Strategy
# Formula: (2 x $num_cores) + 1
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "sync"

# Timeouts & Logging
timeout = 120  # Increased for PDF generation
keepalive = 2
accesslog = "-" # Log to stdout
errorlog = "-"  # Log to stderr
loglevel = "info"

# Security
limit_request_line = 4094
limit_request_fields = 100
