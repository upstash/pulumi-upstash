# """A Python Pulumi program"""

from operator import truediv
import pulumi
import upstash_pulumi as upstash

# consistent and tls fields need some modification on schema definitions
created_db = upstash.RedisDatabase(
    resource_name="myDb",
    database_name="pulumi-python-db",
    consistent=False,
    tls=True,
    region="global",
    primary_region="eu-west-1",
    eviction=True,
)
get_created_db = upstash.get_redis_database_output(database_id=created_db.database_id)


created_globaldb = upstash.RedisDatabase(
    resource_name="myglobalDb",
    database_name="pulumi-python-db-global",
    region="global",
    primary_region="eu-west-1",
)
get_created_globaldb = upstash.get_redis_database_output(
    database_id=created_globaldb.database_id
)

created_team = upstash.Team(
    resource_name="myTeam",
    team_name="pulumi team",
    copy_cc=False,
    team_members={"<owner_email>": "owner", "<second_email>": "admin"},
)

get_created_team = upstash.get_team_output(team_id=created_team.team_id)

for i in range(0, 5):
    created_db = upstash.RedisDatabase(
        resource_name="myDb" + str(i),
        database_name="pulumi-python-db2" + str(i),
        consistent=False,
        tls=True,
        region="global",
        primary_region="eu-west-1",
    )

created_qstash_topic_v2 = upstash.QStashTopicV2(
    resource_name="myQStashTopicV2",
    name="pulumi-py-qstash-topic-v2",
    endpoints=["https://qstash-endpoint.com"],
)

created_qstash_schedule_v2 = upstash.QStashScheduleV2(
    resource_name="myQStashScheduleV2",
    name="pulumi-py-qstash-schedule-v2",
    schedule="0 0 * * *",
    destination=created_qstash_topic_v2.name,
)

get_created_qstash_schedule_v2 = upstash.get_qstash_schedule_v2_output(
    schedule_id=created_qstash_schedule_v2.schedule_id
)


created_vector_index = upstash.VectorIndex(
    name="pulumi-py-vector-index",
    dimension_count=1536,
    region="eu-west-1",
    similarity_function="COSINE",
    type="payg",
)

get_created_vector_index = upstash.get_vector_index_output(id=created_vector_index.id)


pulumi.export("created db:", created_db)
pulumi.export("created globaldb:", created_globaldb)
pulumi.export("created qstash topic v2:", created_qstash_topic_v2)
pulumi.export("created qstash schedule v2:", created_qstash_schedule_v2)
pulumi.export("created vector index:", created_vector_index)
pulumi.export("created team:", created_team)


pulumi.export("get created db", get_created_db)
pulumi.export("get created globaldb", get_created_globaldb)
pulumi.export("get created qstash schedule v2:", get_created_qstash_schedule_v2)
pulumi.export("get created vector index:", get_created_vector_index)
pulumi.export("get created team:", get_created_team)
