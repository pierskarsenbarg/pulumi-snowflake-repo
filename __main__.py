"""A Python Pulumi program"""

import pulumi
import pulumi_snowflake as snowflake
import os

pk_test_db = snowflake.Database("pk_test",
                                comment="piers",
                                data_retention_time_in_days=1,
                                )
