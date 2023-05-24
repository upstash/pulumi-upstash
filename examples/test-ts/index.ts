import * as pulumi from "@pulumi/pulumi";
import * as upstash from "@upstash/pulumi";


const createdDb = new upstash.RedisDatabase("mydb", {
    databaseName: "pulumi-ts-db",
    region: "eu-west-1",
    tls: true,
    multizone: true,
    eviction: true,
})

const dbFromGet = upstash.getRedisDatabaseOutput({
    databaseId: createdDb.databaseId
})

const createdGlobalDb = new upstash.RedisDatabase("myglobaldb", {
    databaseName: "pulumi-ts-db-global",
    region: "global",
    primaryRegion: "eu-west-1",
    readRegions: ["us-east-1", "us-west-1"]
})

const globalDbFromGet = upstash.getRedisDatabaseOutput({
    databaseId: createdGlobalDb.databaseId
})



const createdCluster = new upstash.KafkaCluster("myCluster", {
    clusterName: "pulumi-ts-cluster",
    region: "eu-west-1",
})

const clusterFromGet = upstash.getKafkaClusterOutput({
    clusterId: createdCluster.clusterId
})


const createdTopic = new upstash.KafkaTopic("myTopic", {
    clusterId: clusterFromGet.clusterId,
    cleanupPolicy: "delete",
    maxMessageSize: 100,
    partitions: 1,
    retentionSize: 1000,
    retentionTime: 1000,
    topicName: "pulumi-ts-topic"

})

const topicFromGet = upstash.getKafkaTopicOutput({
    topicId: createdTopic.topicId
})


const createdConnector = new upstash.KafkaConnector("myConnector", {
    clusterId: clusterFromGet.clusterId,
    name: "pulumi-connector",
    properties: {
        "collection": "user123",
        "connection.uri": "mongodb+srv://test:test@cluster0.fohyg7p.mongodb.net/?retryWrites=true&w=majority",
        "connector.class": "com.mongodb.kafka.connect.MongoSourceConnector",
        "database": "myshinynewdb2",
        "topics": createdTopic.topicName
    },
    runningState: "running"
})

const connectorFromGet = upstash.getKafkaConnectorOutput({
    connectorId: createdConnector.connectorId
})



const createdTeam = new upstash.Team("myTeam", {
    teamName: "pulumi ts team",
    teamMembers: {
        "<owner_email>": "owner",
        "<second_email>": "admin"
    },
    copyCc: true
})

const teamFromGet = upstash.getTeamOutput({
    teamId: createdTeam.teamId
})



const createdQStashTopic = new upstash.QStashTopic("myTopic", {
    name: "pulumi-qstash-topic"
})
const createdEndpoint = new upstash.QStashEndpoint("myEndpoint", {
    topicId: createdQStashTopic.topicId,
    url: "https://testing1.com",

})
const createdSchedule = new upstash.QStashSchedule("mySchedule", {
    body: "{\"key\": \"value\"}",
    destination: createdQStashTopic.topicId,
    cron: "* * * * */3",
})

const qstashScheduleFromGet = upstash.getQStashScheduleOutput({
    scheduleId: createdSchedule.scheduleId
})


export const db = createdDb
export const dbFromGetResult = dbFromGet

export const globaldb = createdGlobalDb
export const globaldbFromGetResult = globalDbFromGet

export const cluster = createdCluster
export const clusterFromGetResult = clusterFromGet

export const topic = createdTopic
export const topicFromGetResult = topicFromGet

export const connector = createdConnector
export const connectorFromGetResult = connectorFromGet

export const team = createdTeam
export const teamFromGetResult = teamFromGet

export const qstashTopic = createdQStashTopic
export const qstashEndpoint = createdEndpoint
export const qstashSchedule = createdSchedule
export const qstashScheduleFromGetResult = qstashScheduleFromGet
