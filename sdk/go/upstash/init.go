// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package upstash

import (
	"fmt"

	"github.com/blang/semver"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type module struct {
	version semver.Version
}

func (m *module) Version() semver.Version {
	return m.version
}

func (m *module) Construct(ctx *pulumi.Context, name, typ, urn string) (r pulumi.Resource, err error) {
	switch typ {
	case "upstash:index/kafkaCluster:KafkaCluster":
		r = &KafkaCluster{}
	case "upstash:index/kafkaConnector:KafkaConnector":
		r = &KafkaConnector{}
	case "upstash:index/kafkaCredential:KafkaCredential":
		r = &KafkaCredential{}
	case "upstash:index/kafkaTopic:KafkaTopic":
		r = &KafkaTopic{}
	case "upstash:index/qStashEndpoint:QStashEndpoint":
		r = &QStashEndpoint{}
	case "upstash:index/qStashSchedule:QStashSchedule":
		r = &QStashSchedule{}
	case "upstash:index/qStashScheduleV2:QStashScheduleV2":
		r = &QStashScheduleV2{}
	case "upstash:index/qStashTopic:QStashTopic":
		r = &QStashTopic{}
	case "upstash:index/qStashTopicV2:QStashTopicV2":
		r = &QStashTopicV2{}
	case "upstash:index/redisDatabase:RedisDatabase":
		r = &RedisDatabase{}
	case "upstash:index/team:Team":
		r = &Team{}
	case "upstash:index/vectorIndex:VectorIndex":
		r = &VectorIndex{}
	default:
		return nil, fmt.Errorf("unknown resource type: %s", typ)
	}

	err = ctx.RegisterResource(typ, name, nil, r, pulumi.URN_(urn))
	return
}

type pkg struct {
	version semver.Version
}

func (p *pkg) Version() semver.Version {
	return p.version
}

func (p *pkg) ConstructProvider(ctx *pulumi.Context, name, typ, urn string) (pulumi.ProviderResource, error) {
	if typ != "pulumi:providers:upstash" {
		return nil, fmt.Errorf("unknown provider type: %s", typ)
	}

	r := &Provider{}
	err := ctx.RegisterResource(typ, name, nil, r, pulumi.URN_(urn))
	return r, err
}

func init() {
	version, _ := PkgVersion()
	pulumi.RegisterResourceModule(
		"upstash",
		"index/kafkaCluster",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"upstash",
		"index/kafkaConnector",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"upstash",
		"index/kafkaCredential",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"upstash",
		"index/kafkaTopic",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"upstash",
		"index/qStashEndpoint",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"upstash",
		"index/qStashSchedule",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"upstash",
		"index/qStashScheduleV2",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"upstash",
		"index/qStashTopic",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"upstash",
		"index/qStashTopicV2",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"upstash",
		"index/redisDatabase",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"upstash",
		"index/team",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"upstash",
		"index/vectorIndex",
		&module{version},
	)
	pulumi.RegisterResourcePackage(
		"upstash",
		&pkg{version},
	)
}
