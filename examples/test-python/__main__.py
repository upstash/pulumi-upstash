# """A Python Pulumi program"""

from operator import truediv
import  pulumi
import upstash_pulumi as upstash

# consistent and tls fields need some modification on schema definitions
created_db = upstash.RedisDatabase(
    resource_name="myDb",
    database_name="pulumi-python-db",
    consistent=False,
    tls=True,
    region="eu-west-1",
    eviction=True,
)
get_created_db = upstash.get_redis_database_output(database_id=created_db.database_id)


created_globaldb = upstash.RedisDatabase(
    resource_name="myglobalDb",
    database_name="pulumi-python-db-global",
    region="global",
    primary_region="eu-west-1"
)
get_created_globaldb = upstash.get_redis_database_output(database_id=created_globaldb.database_id)

created_cluster = upstash.KafkaCluster(
    resource_name="myCluster",
    cluster_name="pulumi-python-cluster",
    multizone=False,
    region="eu-west-1"

)
get_created_cluster = upstash.get_kafka_cluster_output(cluster_id=created_cluster.cluster_id)


created_topic = upstash.KafkaTopic(
    resource_name="myTopic",
    topic_name="pulumi-python-topic",
    partitions=2,
    retention_time=111111,
    retention_size=111111,
    max_message_size=111111,
    cleanup_policy="delete",
    cluster_id=created_cluster.cluster_id
)

get_created_topic = upstash.get_kafka_topic_output(topic_id=created_topic.topic_id)


created_credential = upstash.KafkaCredential(
    resource_name="myCredential",
    cluster_id=created_cluster.cluster_id,
    credential_name="pulumi-python-credential",
    permissions="ALL",
    topic=created_topic.topic_name
)

get_created_credential = upstash.get_kafka_credential_output(credential_id=created_credential.credential_id)


created_connector = upstash.KafkaConnector(
    resource_name="myConnector",
    cluster_id=created_cluster.cluster_id,
    name="pulumi-python-connector",
    properties={
        "collection": "user123",
        "connection.uri": "mongodb+srv://test:test@cluster0.fohyg7p.mongodb.net/?retryWrites=true&w=majority",
        "connector.class": "com.mongodb.kafka.connect.MongoSourceConnector",
        "database": "myshinynewdb2",
        "topics": created_topic.topic_id
    },
    running_state="running"
)

get_created_connector = upstash.get_kafka_connector_output(credential_id=created_connector.credential_id)


created_team = upstash.Team(
    resource_name="myTeam",
    team_name="pulumi team",
    copy_cc=False,
    team_members={
        "<owner_email>": "owner",
        "<second_email>": "admin"
    }
)

get_created_team = upstash.get_team_output(team_id=created_team.team_id)

for i in range(0,5):
    created_db = upstash.RedisDatabase(
        resource_name="myDb" + str(i),
        database_name="pulumi-python-db2" + str(i),
        consistent=False,
        tls=True,
        region="eu-west-1"
    )

created_qstash_topic_v2 = upstash.QStashTopicV2(
    resource_name="myQStashTopicV2",
    name="pulumi-py-qstash-topic-v2",
    endpoints=["https://qstash-endpoint.com"]
)

created_qstash_schedule_v2 = upstash.QStashScheduleV2(
    resource_name="myQStashScheduleV2",
    name="pulumi-py-qstash-schedule-v2",
    schedule="0 0 * * *",
    destination=created_qstash_topic_v2.name
)

get_created_qstash_schedule_v2 = upstash.get_qstash_schedule_v2_output(schedule_id=created_qstash_schedule_v2.schedule_id)


created_vector_index = upstash.VectorIndex(
    name="pulumi-py-vector-index",
    dimension_count=1536
    region="eu-west-1"
    similarity_function="COSINE"
    type="payg"
)

get_created_vector_index = upstash.get_vector_index_output(id=created_vector_index.id)


pulumi.export("created db:", created_db)
pulumi.export("created globaldb:", created_globaldb)
pulumi.export("created cluster:", created_cluster)
pulumi.export("created topic:", created_topic)
pulumi.export("created credential:", created_credential)
pulumi.export("created connector:", created_connector)
pulumi.export("created qstash topic v2:", created_qstash_topic_v2)
pulumi.export("created qstash schedule v2:", created_qstash_schedule_v2)
pulumi.export("created vector index:", created_vector_index)
pulumi.export("created team:", created_team)


pulumi.export("get created db", get_created_db)
pulumi.export("get created globaldb", get_created_globaldb)
pulumi.export("get created cluster", get_created_cluster)
pulumi.export("get created topic:", get_created_topic)
pulumi.export("get created credential:", get_created_credential)
pulumi.export("get created connector:", get_created_connector)
pulumi.export("get created qstash schedule v2:", get_created_qstash_schedule_v2)
pulumi.export("get created vector index:", get_created_vector_index)
pulumi.export("get created team:", get_created_team)


