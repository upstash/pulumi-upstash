// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package upstash

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-upstash/sdk/go/upstash"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// 	"github.com/upstash/upstash-pulumi-provider/sdk/go/upstash"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := upstash.LookupRedisDatabase(ctx, &GetRedisDatabaseArgs{
// 			DatabaseId: resource.Upstash_redis_database.ExampleDB.Database_id,
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func LookupRedisDatabase(ctx *pulumi.Context, args *LookupRedisDatabaseArgs, opts ...pulumi.InvokeOption) (*LookupRedisDatabaseResult, error) {
	opts = pkgInvokeDefaultOpts(opts)
	var rv LookupRedisDatabaseResult
	err := ctx.Invoke("upstash:index/getRedisDatabase:getRedisDatabase", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getRedisDatabase.
type LookupRedisDatabaseArgs struct {
	DatabaseId string `pulumi:"databaseId"`
}

// A collection of values returned by getRedisDatabase.
type LookupRedisDatabaseResult struct {
	// Deprecated: Consistent option is deprecated.
	Consistent             bool   `pulumi:"consistent"`
	CreationTime           int    `pulumi:"creationTime"`
	DatabaseId             string `pulumi:"databaseId"`
	DatabaseName           string `pulumi:"databaseName"`
	DatabaseType           string `pulumi:"databaseType"`
	DbDailyBandwidthLimit  int    `pulumi:"dbDailyBandwidthLimit"`
	DbDiskThreshold        int    `pulumi:"dbDiskThreshold"`
	DbMaxClients           int    `pulumi:"dbMaxClients"`
	DbMaxCommandsPerSecond int    `pulumi:"dbMaxCommandsPerSecond"`
	DbMaxEntrySize         int    `pulumi:"dbMaxEntrySize"`
	DbMaxRequestSize       int    `pulumi:"dbMaxRequestSize"`
	DbMemoryThreshold      int    `pulumi:"dbMemoryThreshold"`
	Endpoint               string `pulumi:"endpoint"`
	// The provider-assigned unique ID for this managed resource.
	Id                string `pulumi:"id"`
	Multizone         bool   `pulumi:"multizone"`
	Password          string `pulumi:"password"`
	Port              int    `pulumi:"port"`
	ReadOnlyRestToken string `pulumi:"readOnlyRestToken"`
	Region            string `pulumi:"region"`
	RestToken         string `pulumi:"restToken"`
	State             string `pulumi:"state"`
	// Deprecated: TLS option is deprecated.
	Tls       bool   `pulumi:"tls"`
	UserEmail string `pulumi:"userEmail"`
}

func LookupRedisDatabaseOutput(ctx *pulumi.Context, args LookupRedisDatabaseOutputArgs, opts ...pulumi.InvokeOption) LookupRedisDatabaseResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupRedisDatabaseResult, error) {
			args := v.(LookupRedisDatabaseArgs)
			r, err := LookupRedisDatabase(ctx, &args, opts...)
			var s LookupRedisDatabaseResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupRedisDatabaseResultOutput)
}

// A collection of arguments for invoking getRedisDatabase.
type LookupRedisDatabaseOutputArgs struct {
	DatabaseId pulumi.StringInput `pulumi:"databaseId"`
}

func (LookupRedisDatabaseOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupRedisDatabaseArgs)(nil)).Elem()
}

// A collection of values returned by getRedisDatabase.
type LookupRedisDatabaseResultOutput struct{ *pulumi.OutputState }

func (LookupRedisDatabaseResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupRedisDatabaseResult)(nil)).Elem()
}

func (o LookupRedisDatabaseResultOutput) ToLookupRedisDatabaseResultOutput() LookupRedisDatabaseResultOutput {
	return o
}

func (o LookupRedisDatabaseResultOutput) ToLookupRedisDatabaseResultOutputWithContext(ctx context.Context) LookupRedisDatabaseResultOutput {
	return o
}

// Deprecated: Consistent option is deprecated.
func (o LookupRedisDatabaseResultOutput) Consistent() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupRedisDatabaseResult) bool { return v.Consistent }).(pulumi.BoolOutput)
}

func (o LookupRedisDatabaseResultOutput) CreationTime() pulumi.IntOutput {
	return o.ApplyT(func(v LookupRedisDatabaseResult) int { return v.CreationTime }).(pulumi.IntOutput)
}

func (o LookupRedisDatabaseResultOutput) DatabaseId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupRedisDatabaseResult) string { return v.DatabaseId }).(pulumi.StringOutput)
}

func (o LookupRedisDatabaseResultOutput) DatabaseName() pulumi.StringOutput {
	return o.ApplyT(func(v LookupRedisDatabaseResult) string { return v.DatabaseName }).(pulumi.StringOutput)
}

func (o LookupRedisDatabaseResultOutput) DatabaseType() pulumi.StringOutput {
	return o.ApplyT(func(v LookupRedisDatabaseResult) string { return v.DatabaseType }).(pulumi.StringOutput)
}

func (o LookupRedisDatabaseResultOutput) DbDailyBandwidthLimit() pulumi.IntOutput {
	return o.ApplyT(func(v LookupRedisDatabaseResult) int { return v.DbDailyBandwidthLimit }).(pulumi.IntOutput)
}

func (o LookupRedisDatabaseResultOutput) DbDiskThreshold() pulumi.IntOutput {
	return o.ApplyT(func(v LookupRedisDatabaseResult) int { return v.DbDiskThreshold }).(pulumi.IntOutput)
}

func (o LookupRedisDatabaseResultOutput) DbMaxClients() pulumi.IntOutput {
	return o.ApplyT(func(v LookupRedisDatabaseResult) int { return v.DbMaxClients }).(pulumi.IntOutput)
}

func (o LookupRedisDatabaseResultOutput) DbMaxCommandsPerSecond() pulumi.IntOutput {
	return o.ApplyT(func(v LookupRedisDatabaseResult) int { return v.DbMaxCommandsPerSecond }).(pulumi.IntOutput)
}

func (o LookupRedisDatabaseResultOutput) DbMaxEntrySize() pulumi.IntOutput {
	return o.ApplyT(func(v LookupRedisDatabaseResult) int { return v.DbMaxEntrySize }).(pulumi.IntOutput)
}

func (o LookupRedisDatabaseResultOutput) DbMaxRequestSize() pulumi.IntOutput {
	return o.ApplyT(func(v LookupRedisDatabaseResult) int { return v.DbMaxRequestSize }).(pulumi.IntOutput)
}

func (o LookupRedisDatabaseResultOutput) DbMemoryThreshold() pulumi.IntOutput {
	return o.ApplyT(func(v LookupRedisDatabaseResult) int { return v.DbMemoryThreshold }).(pulumi.IntOutput)
}

func (o LookupRedisDatabaseResultOutput) Endpoint() pulumi.StringOutput {
	return o.ApplyT(func(v LookupRedisDatabaseResult) string { return v.Endpoint }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o LookupRedisDatabaseResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupRedisDatabaseResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o LookupRedisDatabaseResultOutput) Multizone() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupRedisDatabaseResult) bool { return v.Multizone }).(pulumi.BoolOutput)
}

func (o LookupRedisDatabaseResultOutput) Password() pulumi.StringOutput {
	return o.ApplyT(func(v LookupRedisDatabaseResult) string { return v.Password }).(pulumi.StringOutput)
}

func (o LookupRedisDatabaseResultOutput) Port() pulumi.IntOutput {
	return o.ApplyT(func(v LookupRedisDatabaseResult) int { return v.Port }).(pulumi.IntOutput)
}

func (o LookupRedisDatabaseResultOutput) ReadOnlyRestToken() pulumi.StringOutput {
	return o.ApplyT(func(v LookupRedisDatabaseResult) string { return v.ReadOnlyRestToken }).(pulumi.StringOutput)
}

func (o LookupRedisDatabaseResultOutput) Region() pulumi.StringOutput {
	return o.ApplyT(func(v LookupRedisDatabaseResult) string { return v.Region }).(pulumi.StringOutput)
}

func (o LookupRedisDatabaseResultOutput) RestToken() pulumi.StringOutput {
	return o.ApplyT(func(v LookupRedisDatabaseResult) string { return v.RestToken }).(pulumi.StringOutput)
}

func (o LookupRedisDatabaseResultOutput) State() pulumi.StringOutput {
	return o.ApplyT(func(v LookupRedisDatabaseResult) string { return v.State }).(pulumi.StringOutput)
}

// Deprecated: TLS option is deprecated.
func (o LookupRedisDatabaseResultOutput) Tls() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupRedisDatabaseResult) bool { return v.Tls }).(pulumi.BoolOutput)
}

func (o LookupRedisDatabaseResultOutput) UserEmail() pulumi.StringOutput {
	return o.ApplyT(func(v LookupRedisDatabaseResult) string { return v.UserEmail }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupRedisDatabaseResultOutput{})
}
