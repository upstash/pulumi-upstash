import * as pulumi from "@pulumi/pulumi";
import * as upstash from "@upstash/pulumi";


const createdDb = new upstash.RedisDatabase("mydb", {
    databaseName: "pulumi-ts-db",
    region: "global",
    primaryRegion: "eu-west-1",
    tls: true,
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

const createdQStashTopicV2 = new upstash.QStashTopicV2("myTopic", {
    name: "pulumi-qstash-topic",
    endpoints: ["https://testing1.com", "https://testing2.com"]
})

const createdScheduleV2 = new upstash.QStashScheduleV2("mySchedule", {
    body: "{\"key\": \"value\"}",
    destination: createdQStashTopicV2.name,
    cron: "* * * * */3",
})

const qstashScheduleFromGetV2 = upstash.getQStashScheduleV2Output({
    scheduleId: createdScheduleV2.scheduleId
})

const createIndex = new upstash.VectorIndex("myindex", {
    name: "pulumi-ts-index",
    region: "eu-west-1",
    dimensionCount: 1536,
    similarityFunction: "COSINE",
    type: "payg"
})

const indexFromGet = upstash.getVectorIndexOutput({
    id: createIndex.id
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

export const db = createdDb
export const dbFromGetResult = dbFromGet

export const globaldb = createdGlobalDb
export const globaldbFromGetResult = globalDbFromGet

export const QStashTopicV2 = createdQStashTopicV2
export const QStashScheduleV2 = createdScheduleV2
export const qstashScheduleFromGetV2Result = qstashScheduleFromGetV2

export const index = createIndex
export const indexFromGetResult = indexFromGet

export const team = createdTeam
export const teamFromGetResult = teamFromGet
