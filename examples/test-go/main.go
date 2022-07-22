package main

import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/upstash/upstash-pulumi-provider/sdk/go/upstash"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		createdDb, err := upstash.NewRedisDatabase(ctx, "exampleDB", &upstash.RedisDatabaseArgs{
			DatabaseName: pulumi.String("pulumi-go-db"),
			Multizone:    pulumi.Bool(true),
			Region:       pulumi.String("eu-west-1"),
			Tls:          pulumi.Bool(true),
		})
		if err != nil {
			return err
		}

		dbFromGet := upstash.LookupRedisDatabaseOutput(ctx, upstash.LookupRedisDatabaseOutputArgs{
			DatabaseId: createdDb.DatabaseId,
		}, nil)
		if err != nil {
			return err
		}

		ctx.Export("db from get request", dbFromGet)

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
		if err != nil {
			return err
		}

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
		if err != nil {
			return err
		}

		ctx.Export("topic from get request", topicFromGet)

		createdCredential, err := upstash.NewKafkaCredential(ctx, "exampleCredential", &upstash.KafkaCredentialArgs{
			ClusterId:      pulumi.StringOutput(createdCluster.ClusterId),
			CredentialName: pulumi.String("pulumi-go-credential"),
			Permissions:    pulumi.String("ALL"),
			Topic:          pulumi.StringOutput(createdTopic.TopicName),
		})

		credentialFromGet := upstash.LookupKafkaCredentialOutput(ctx, upstash.LookupKafkaCredentialOutputArgs{
			CredentialId: createdCredential.CredentialId,
		}, nil)
		if err != nil {
			return err
		}

		ctx.Export("credential from get request", credentialFromGet)

		createdTeam, err := upstash.NewTeam(ctx, "exampleTeam", &upstash.TeamArgs{
			TeamName: pulumi.String("pulumi go team"),
			CopyCc:   pulumi.Bool(false),
			TeamMembers: pulumi.StringMap{
				"bylmaz744@gmail.com": pulumi.String("owner"),
				"burak@upstash.com":   pulumi.String("dev"),
			},
		})
		if err != nil {
			return err
		}

		teamFromGet := upstash.LookupTeamOutput(ctx, upstash.LookupTeamOutputArgs{
			TeamId: createdTeam.TeamId,
		}, nil)
		if err != nil {
			return err
		}

		ctx.Export("team from get request", teamFromGet)

		return nil
	})
}
