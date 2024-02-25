# database_config.py

import os

# Retrieve database connection URL from environment variable
DATABASE_URL = os.getenv('mysql://doadmin:show-password@db-mysql-nyc3-35936-do-user-15450315-0.c.db.ondigitalocean.com:25060/defaultdb?ssl-mode=REQUIRED')

# Database connection details
DB_CONFIG = {
    'url': DATABASE_URL
}
