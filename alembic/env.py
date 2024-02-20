# alembic.env.py

from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
import os
from alembic import context
from tenant_mangement.models import Base

config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)



target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = os.environ.get('DATABASE_URL')
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True, dialect_opts={"paramstyle": "named"})
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    configuration = context.config
    configuration.set_main_option('sqlalchemy.url', os.environ['DATABASE_URL'])

    connectable = engine_from_config(configuration.get_section(configuration.config_ini_section), prefix="sqlalchemy.", poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()