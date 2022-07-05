import * as pulumi from "@pulumi/pulumi";

import * as upstash from "@upstash/upstash"


// const provider = new upstash.Provider("p1", {
//     email: "bylmaz744@gmail.com", 
//     apiKey: "b668e945-0a23-4873-a82e-a780454d944f" 
// })


const database = upstash.getRedisDatabase({
    databaseId: "d972343a-3d6f-4810-b542-66ba34a6b501"
})


export const db = database.then(x => x) 
console.log(database)