import * as pulumi from "@pulumi/pulumi";
import * as upstash from "@upstash/upstash";


const createdDb = new upstash.RedisDatabase("mydb", {
    databaseName: "pulumi-ts-db",
    region: "eu-west-1",
    tls: true
})



const dbFromGet = upstash.getRedisDatabaseOutput({
    databaseId: createdDb.databaseId
})

export const db = createdDb
export const dbFromGetResult = dbFromGet

