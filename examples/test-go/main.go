package main

import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// _, err := upstash.NewRedisDatabase(ctx, "exampleDB", &upstash.RedisDatabaseArgs{
		// 	DatabaseName: pulumi.String("Terraform DB6"),
		// 	Multizone:    pulumi.Bool(true),
		// 	Region:       pulumi.String("eu-west-1"),
		// 	Tls:          pulumi.Bool(true),
		// })
		// if err != nil {
		// 	return err
		// }
		return nil
	})
}
