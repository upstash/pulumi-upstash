# Upstash Resource Provider

The Upstash Pulumi Provider lets you manage [Upstash](http://upstash.com) resources programatically.

## Installing

This package is available for several languages/platforms:

### Node.js (JavaScript/TypeScript)

To use from JavaScript or TypeScript in Node.js, install using either `npm`:

```bash
npm install @upstash/pulumi
```

or `yarn`:

```bash
yarn add @upstash/pulumi
```

### Python

To use from Python, install using `pip`:

```bash
pip install upstash_pulumi
```

### Go

To use from Go, use `go get` to grab the latest version of the library:

```bash
go get github.com/upstash/upstash-pulumi-provider/sdk/go/...
```

## Configuration

The following configuration points are available for the `upstash` provider:

- `upstash:apiKey` (environment: `UPSTASH_API_KEY`) - the API key for `upstash`. Can be obtained from the [console](https://console.upstash.com).
- `upstash:email` (environment: `UPSTASH_EMAIL`) - owner email of the resources

## Some Examples

### TypeScript:
```
import * as pulumi from "@pulumi/pulumi";
import * as upstash from "@upstash/pulumi";

// multiple redis databases in a single for loop

for (let i = 0; i < 5; i++) {
    new upstash.RedisDatabase("mydb" + i, {
        databaseName: "pulumi-ts-db" + i,
        region: "eu-west-1",
        tls: true
    })
}

```

### Go:
```
package main

import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/upstash/upstash-pulumi-provider/sdk/go/upstash"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {

		createdTeam, err := upstash.NewTeam(ctx, "exampleTeam", &upstash.TeamArgs{
			TeamName: pulumi.String("pulumi go team"),
			CopyCc:   pulumi.Bool(false),
			TeamMembers: pulumi.StringMap{
				"<owner-email>": pulumi.String("owner"),
				"<some-other-user-email>":   pulumi.String("dev"),
			},

		})
		if err != nil {
			return err
		}
		return nil
	})
}

```


### Python: 
```
import  pulumi
import upstash_pulumi as upstash

created_cluster = upstash.KafkaCluster(
    resource_name="myCluster",
    cluster_name="pulumi-python-cluster",
    multizone=False,
    region="eu-west-1"
)
```

## Reference

For reference, please look into `/examples` directory for resource management using different languages. You can also visit [developer api docs](https://developer.upstash.com/) to see parameters and their behaviors.
