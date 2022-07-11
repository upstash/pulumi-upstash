# """A Python Pulumi program"""

import  pulumi
import upstash_upstash as upstash

# consistent and tls fields need some modification on schema definitions
created_db = upstash.RedisDatabase(
    resource_name="myDb",
    database_name="pulumi-python-db",
    consistent=False,
    tls=True,
    region="eu-west-1",
    multizone=True
)

test = upstash.get_redis_database_output(database_id=created_db.database_id)
# dbFromGet = created_db.database_id.apply(lambda x: upstash.get_redis_database(database_id=x))

# pulumi.export("db from get:", dbFromGet)
pulumi.export("test:", test)

