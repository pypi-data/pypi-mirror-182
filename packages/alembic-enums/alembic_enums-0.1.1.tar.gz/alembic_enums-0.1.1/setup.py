# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['alembic_enums']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'alembic-enums',
    'version': '0.1.1',
    'description': 'Support for migrating PostgreSQL enums with Alembic',
    'long_description': '# Alembic Enums\n\n![example workflow](https://github.com/imankulov/alembic-enums/actions/workflows/tests.yml/badge.svg)\n\n**Support for migrating PostgreSQL enums with Alembic**\n\nThe package doesn\'t detect enum changes or generate migration code automatically, but it provides a helper class to run the enum migrations in Alembic migration scripts.\n\n## Problem statement\n\nWhen you define an enum column with SQLAlchemy, the initial migration defines a custom [enum type](https://www.postgresql.org/docs/current/datatype-enum.html).\n\nOnce the enum type is created, [ALTER TYPE](https://www.postgresql.org/docs/current/sql-altertype.html) allows you to add new values or rename existing ones, but not delete them.\n\nIf you need to delete a value from an enum, you must create a new enum type and migrate all the columns to use the new type.\n\n\n## Installation\n\n```bash\npip install alembic-enums\n```\n\n\n## Usage\n\nAssume you decided to rename the `state` enum values `active` and `inactive` to `enabled` and `disabled`:\n\n```diff\n class Resource(Base):\n     __tablename__ = "resources"\n     id = Column(Integer, primary_key=True)\n     name = Column(String(255), nullable=False)\n-    state = Column(Enum("enabled", "disabled", name="resource_state"), nullable=False)\n+    state = Column(Enum("active", "archived", name="resource_state"), nullable=False)\n```\n\nTo migrate the database, we create a new empty migration with `alembic revision -m "Rename enum values"` and add the following code to the generated migration script:\n\n```python\nfrom alembic import op\n\nfrom alembic_enums import EnumMigration, Column\n\n# Define a target column. As in PostgreSQL, the same enum can be used in multiple\n# column definitions, you may have more than one target column.\ncolumn = Column("resources", "state")\n\n# Define an enum migration. It defines the old and new enum values\n# for the enum, and the list of target columns.\nenum_migration = EnumMigration(\n    op=op,\n    enum_name="resource_state",\n    old_options=["enabled", "disabled"],\n    new_options=["active", "archived"],\n    columns=[column],\n)\n\n# Define upgrade and downgrade operations. Inside upgrade_ctx and downgrade_ctx\n# context managers, you can update your data.\n\ndef upgrade():\n    with enum_migration.upgrade_ctx():\n        enum_migration.update_value(column, "enabled", "active")\n        enum_migration.update_value(column, "disabled", "archived")\n\n\ndef downgrade():\n    with enum_migration.downgrade_ctx():\n        enum_migration.update_value(column, "active", "enabled")\n        enum_migration.update_value(column, "archived", "disabled")\n```\n\nUnder the hood, the `EnumMigration` class creates a new enum type, updates the target columns to use the new enum type, and deletes the old enum type.\n\n## API reference\n\n### `EnumMigration`\n\nA helper class to run enum migrations in Alembic migration scripts.\n\n**Constructor arguments:**\n\n- `op`: an instance of `alembic.operations.Operations`\n- `enum_name`: the name of the enum type\n- `old_options`: a list of old enum values\n- `new_options`: a list of new enum values\n- `columns`: a list of `Column` instances that use the enum type\n\n**Methods:**\n\n- `upgrade_ctx()`: a context manager that creates a new enum type, updates the target columns to use the new enum type, and deletes the old enum type\n- `downgrade_ctx()`: a context manager that performs the opposite operations.\n- `update_value(column, old_value, new_value)`: a helper method to update the value of the `column` to `new_value` where it was `old_value` before. It\'s useful to update the data in the upgrade and downgrade operations within the `upgrade_ctx` and `downgrade_ctx` context managers.\n- `upgrade()`: a shorthand for `with upgrade_ctx(): pass`.\n- `downgrade()`: a shorthand for `with downgrade_ctx(): pass`.\n\n### `Column`\n\nA data class to define a target column for an enum migration.\n\n**Constructor arguments:**\n\n- `table_name`: the name of the table\n- `column_name`: the name of the column\n',
    'author': 'Roman Imankulov',
    'author_email': 'roman.imankulov@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/imankulov/alembic-enums',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
