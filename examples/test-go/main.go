package main

import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/upstash/pulumi-upstash/sdk/go/upstash"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		createdDb, err := upstash.NewRedisDatabase(ctx, "exampleDB", &upstash.RedisDatabaseArgs{
			DatabaseName:  pulumi.String("pulumi-go-db"),
			Multizone:     pulumi.Bool(true),
			Region:        pulumi.String("global"),
			PrimaryRegion: pulumi.String("eu-west-1"),
			Tls:           pulumi.Bool(true),
			Eviction:      pulumi.Bool(true),
		})
		if err != nil {
			return err
		}

		dbFromGet := upstash.LookupRedisDatabaseOutput(ctx, upstash.LookupRedisDatabaseOutputArgs{
			DatabaseId: createdDb.DatabaseId,
		}, nil)

		ctx.Export("db from get request", dbFromGet)

		createdGloblaDb, err := upstash.NewRedisDatabase(ctx, "exampleGlobalDB", &upstash.RedisDatabaseArgs{
			DatabaseName:  pulumi.String("pulumi-go-db-global"),
			Region:        pulumi.String("global"),
			PrimaryRegion: pulumi.String("eu-west-1"),
		})
		if err != nil {
			return err
		}

		globaldbFromGet := upstash.LookupRedisDatabaseOutput(ctx, upstash.LookupRedisDatabaseOutputArgs{
			DatabaseId: createdGloblaDb.DatabaseId,
		}, nil)

		ctx.Export("global db from get request", globaldbFromGet)

		createdTeam, err := upstash.NewTeam(ctx, "exampleTeam", &upstash.TeamArgs{
			TeamName: pulumi.String("pulumi go team"),
			CopyCc:   pulumi.Bool(false),
			TeamMembers: pulumi.StringMap{
				"<owner_email>":  pulumi.String("owner"),
				"<second_email>": pulumi.String("dev"),
			},
		})
		if err != nil {
			return err
		}

		teamFromGet := upstash.LookupTeamOutput(ctx, upstash.LookupTeamOutputArgs{
			TeamId: createdTeam.TeamId,
		}, nil)

		ctx.Export("team from get request", teamFromGet)

		createdQStashTopicV2, err := upstash.NewQStashTopicV2(ctx, "exampleQStashTopicV2", nil)
		if err != nil {
			return err
		}

		ctx.Export("created qstash topic", createdQStashTopicV2)

		createdQStashScheduleV2, err := upstash.NewQStashScheduleV2(ctx, "exampleQStashScheduleV2", &upstash.QStashScheduleV2Args{
			Cron:        pulumi.String("* * * * *"),
			Destination: pulumi.StringOutput(createdQStashTopicV2.name),
		})
		if err != nil {
			return err
		}

		ctx.Export("created qstash schedule", createdQStashScheduleV2)

		qstashScheduleV2Get, err := upstash.LookupQStashScheduleV2(ctx, &upstash.LookupQStashScheduleV2Args{
			Id: createdQStashScheduleV2.id,
		})
		if err != nil {
			return err
		}

		ctx.Export("qstash schedule from get request", qstashScheduleV2Get)

		createdVectorIndex, err := upstash.NewVectorIndex(ctx, "exampleVectorIndex", &upstash.VectorIndexArgs{
			Name:               pulumi.String("pulumi-vector-index"),
			DimensionCount:     pulumi.Int(1536),
			Region:             pulumi.String("eu-west-1"),
			SimilarityFunction: pulumi.String("COSINE"),
			Type:               pulumi.String("payg"),
		})

		if err != nil {
			return err
		}
		pulumi.Export("created vector index", createdVectorIndex)

		vectorIndexGet, err := upstash.LookupVectorIndex(ctx, &upstash.LookupVectorIndexArgs{
			Id: createdVectorIndex.id,
		})

		if err != nil {
			return err
		}
		pulumi.Export("vector index from get request", vectorIndexGet)

		return nil
	})
}
