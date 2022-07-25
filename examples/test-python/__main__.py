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
    region="eu-west-1"
)
get_created_db = upstash.get_redis_database_output(database_id=created_db.database_id)


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


created_team = upstash.Team(
    resource_name="myTeam",
    team_name="pulumi team",
    copy_cc=False,
    team_members={
        "bylmaz744@gmail.com": "owner",
        "burak@upstash.com": "admin"
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

pulumi.export("created db:", created_db)
pulumi.export("created cluster:", created_cluster)
pulumi.export("created topic:", created_topic)
pulumi.export("created credential:", created_credential)
pulumi.export("created team:", created_team)


pulumi.export("get_created_db", get_created_db)
pulumi.export("get_created_cluster", get_created_cluster)
pulumi.export("get_created topic:", get_created_topic)
pulumi.export("get_created credential:", get_created_credential)
pulumi.export("get_created team:", get_created_team)


