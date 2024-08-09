package main

import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/upstash/pulumi-upstash/sdk/go/upstash"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		createdDb, err := upstash.NewRedisDatabase(ctx, "exampleDB", &upstash.RedisDatabaseArgs{
			DatabaseName: pulumi.String("pulumi-go-db"),
			Multizone:    pulumi.Bool(true),
			Region:       pulumi.String("eu-west-1"),
			Tls:          pulumi.Bool(true),
			Eviction:     pulumi.Bool(true),
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

		createdCluster, err := upstash.NewKafkaCluster(ctx, "exampleCluster", &upstash.KafkaClusterArgs{
			ClusterName: pulumi.String("pulumi-go-cluster"),
			Multizone:   pulumi.Bool(false),
			Region:      pulumi.String("eu-west-1"),
		})
		if err != nil {
			return err
		}

		clusterFromGet := upstash.LookupKafkaClusterOutput(ctx, upstash.LookupKafkaClusterOutputArgs{
			ClusterId: createdCluster.ClusterId,
		}, nil)

		ctx.Export("cluster from get request", clusterFromGet)

		createdTopic, err := upstash.NewKafkaTopic(ctx, "exampleKafkaTopic", &upstash.KafkaTopicArgs{
			TopicName:      pulumi.String("pulumi-go-topic"),
			Partitions:     pulumi.Int(1),
			RetentionTime:  pulumi.Int(625135),
			RetentionSize:  pulumi.Int(725124),
			MaxMessageSize: pulumi.Int(829213),
			CleanupPolicy:  pulumi.String("delete"),
			ClusterId:      pulumi.StringOutput(createdCluster.ClusterId),
		})
		if err != nil {
			return err
		}

		topicFromGet := upstash.LookupKafkaTopicOutput(ctx, upstash.LookupKafkaTopicOutputArgs{
			TopicId: createdTopic.TopicId,
		}, nil)

		ctx.Export("topic from get request", topicFromGet)

		createdCredential, err := upstash.NewKafkaCredential(ctx, "exampleCredential", &upstash.KafkaCredentialArgs{
			ClusterId:      pulumi.StringOutput(createdCluster.ClusterId),
			CredentialName: pulumi.String("pulumi-go-credential"),
			Permissions:    pulumi.String("ALL"),
			Topic:          pulumi.StringOutput(createdTopic.TopicName),
		})
		if err != nil {
			return err
		}

		credentialFromGet := upstash.LookupKafkaCredentialOutput(ctx, upstash.LookupKafkaCredentialOutputArgs{
			CredentialId: createdCredential.CredentialId,
		}, nil)

		ctx.Export("credential from get request", credentialFromGet)

		createdConnector, err := upstash.NewKafkaConnector(ctx, "exampleConnector", &upstash.KafkaConnectorArgs{
			ClusterId: pulumi.StringOutput(createdCluster.ClusterId),
			Name:      pulumi.String("pulumi-go-connector"),
			Properties: pulumi.StringMap{
				"collection":      pulumi.String("user123"),
				"connection.uri":  pulumi.String("mongodb+srv://test:test@cluster0.fohyg7p.mongodb.net/?retryWrites=true&w=majority"),
				"connector.class": pulumi.String("com.mongodb.kafka.connect.MongoSourceConnector"),
				"database":        pulumi.String("myshinynewdb2"),
				"topics":          pulumi.String(createdTopic.TopicId),
			},
			RunningState: pulumi.String("running"),
		})
		if err != nil {
			return err
		}

		connectorFromGet := upstash.LookupKafkaConnectorOutput(ctx, upstash.LookupKafkaConnectorOutputArgs{
			ConnectorId: createdConnector.ConnectorId,
		}, nil)

		ctx.Export("connector from get request", connectorFromGet)

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
			Cron: pulumi.String("* * * * *"),
			Destination: pulumi.StringOutput(createdQStashTopicV2.name),
		})
		if err != nil {
			return err
		}

		ctx.Export("created qstash schedule", createdQStashScheduleV2)


		qstashScheduleV2Get, err := upstash.LookupQStashScheduleV2(ctx, &upstash.LookupQStashScheduleV2Args {
			Id: createdQStashScheduleV2.id,
		})
		if err!= nil {
			return err
		}

		ctx.Export("qstash schedule from get request", qstashScheduleV2Get)

		createdVectorIndex, err := upstash.NewVectorIndex(ctx, "exampleVectorIndex", &upstash.VectorIndexArgs{
			Name: pulumi.String("pulumi-vector-index"),
			DimensionCount: pulumi.Int(1536),
			Region: pulumi.String("eu-west-1"),
			SimilarityFunction: pulumi.String("COSINE"),
			Type: pulumi.String("payg"),
		})

		if err!=nil {
			return err
		}
		pulumi.Export("created vector index", createdVectorIndex)

		vectorIndexGet, err := upstash.LookupVectorIndex(ctx, &upstash.LookupVectorIndexArgs{
			Id: createdVectorIndex.id,
		})

		if err!=nil {
			return err
		}
		pulumi.Export("vector index from get request", vectorIndexGet)


		return nil
	})
}
