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
//
//	"github.com/pulumi/pulumi-upstash/sdk/go/upstash"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//	"github.com/upstash/pulumi-upstash/sdk/go/upstash"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := upstash.LookupKafkaConnector(ctx, &GetKafkaConnectorArgs{
//				TopicId: resource.Upstash_kafka_connector.ExampleKafkaConnector.Connector_id,
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func LookupKafkaConnector(ctx *pulumi.Context, args *LookupKafkaConnectorArgs, opts ...pulumi.InvokeOption) (*LookupKafkaConnectorResult, error) {
	opts = pkgInvokeDefaultOpts(opts)
	var rv LookupKafkaConnectorResult
	err := ctx.Invoke("upstash:index/getKafkaConnector:getKafkaConnector", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getKafkaConnector.
type LookupKafkaConnectorArgs struct {
	ConnectorId string `pulumi:"connectorId"`
}

// A collection of values returned by getKafkaConnector.
type LookupKafkaConnectorResult struct {
	ClusterId       string `pulumi:"clusterId"`
	ConnectorClass  string `pulumi:"connectorClass"`
	ConnectorId     string `pulumi:"connectorId"`
	ConnectorState  string `pulumi:"connectorState"`
	CreationTime    int    `pulumi:"creationTime"`
	EncodedUsername string `pulumi:"encodedUsername"`
	// The provider-assigned unique ID for this managed resource.
	Id                  string                   `pulumi:"id"`
	Name                string                   `pulumi:"name"`
	Properties          map[string]interface{}   `pulumi:"properties"`
	PropertiesEncrypted string                   `pulumi:"propertiesEncrypted"`
	State               string                   `pulumi:"state"`
	StateErrorMessage   string                   `pulumi:"stateErrorMessage"`
	Tasks               []map[string]interface{} `pulumi:"tasks"`
	Topics              []string                 `pulumi:"topics"`
	Ttl                 int                      `pulumi:"ttl"`
	UserPassword        string                   `pulumi:"userPassword"`
}

func LookupKafkaConnectorOutput(ctx *pulumi.Context, args LookupKafkaConnectorOutputArgs, opts ...pulumi.InvokeOption) LookupKafkaConnectorResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupKafkaConnectorResult, error) {
			args := v.(LookupKafkaConnectorArgs)
			r, err := LookupKafkaConnector(ctx, &args, opts...)
			var s LookupKafkaConnectorResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupKafkaConnectorResultOutput)
}

// A collection of arguments for invoking getKafkaConnector.
type LookupKafkaConnectorOutputArgs struct {
	ConnectorId pulumi.StringInput `pulumi:"connectorId"`
}

func (LookupKafkaConnectorOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupKafkaConnectorArgs)(nil)).Elem()
}

// A collection of values returned by getKafkaConnector.
type LookupKafkaConnectorResultOutput struct{ *pulumi.OutputState }

func (LookupKafkaConnectorResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupKafkaConnectorResult)(nil)).Elem()
}

func (o LookupKafkaConnectorResultOutput) ToLookupKafkaConnectorResultOutput() LookupKafkaConnectorResultOutput {
	return o
}

func (o LookupKafkaConnectorResultOutput) ToLookupKafkaConnectorResultOutputWithContext(ctx context.Context) LookupKafkaConnectorResultOutput {
	return o
}

func (o LookupKafkaConnectorResultOutput) ClusterId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKafkaConnectorResult) string { return v.ClusterId }).(pulumi.StringOutput)
}

func (o LookupKafkaConnectorResultOutput) ConnectorClass() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKafkaConnectorResult) string { return v.ConnectorClass }).(pulumi.StringOutput)
}

func (o LookupKafkaConnectorResultOutput) ConnectorId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKafkaConnectorResult) string { return v.ConnectorId }).(pulumi.StringOutput)
}

func (o LookupKafkaConnectorResultOutput) ConnectorState() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKafkaConnectorResult) string { return v.ConnectorState }).(pulumi.StringOutput)
}

func (o LookupKafkaConnectorResultOutput) CreationTime() pulumi.IntOutput {
	return o.ApplyT(func(v LookupKafkaConnectorResult) int { return v.CreationTime }).(pulumi.IntOutput)
}

func (o LookupKafkaConnectorResultOutput) EncodedUsername() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKafkaConnectorResult) string { return v.EncodedUsername }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o LookupKafkaConnectorResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKafkaConnectorResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o LookupKafkaConnectorResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKafkaConnectorResult) string { return v.Name }).(pulumi.StringOutput)
}

func (o LookupKafkaConnectorResultOutput) Properties() pulumi.MapOutput {
	return o.ApplyT(func(v LookupKafkaConnectorResult) map[string]interface{} { return v.Properties }).(pulumi.MapOutput)
}

func (o LookupKafkaConnectorResultOutput) PropertiesEncrypted() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKafkaConnectorResult) string { return v.PropertiesEncrypted }).(pulumi.StringOutput)
}

func (o LookupKafkaConnectorResultOutput) State() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKafkaConnectorResult) string { return v.State }).(pulumi.StringOutput)
}

func (o LookupKafkaConnectorResultOutput) StateErrorMessage() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKafkaConnectorResult) string { return v.StateErrorMessage }).(pulumi.StringOutput)
}

func (o LookupKafkaConnectorResultOutput) Tasks() pulumi.MapArrayOutput {
	return o.ApplyT(func(v LookupKafkaConnectorResult) []map[string]interface{} { return v.Tasks }).(pulumi.MapArrayOutput)
}

func (o LookupKafkaConnectorResultOutput) Topics() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupKafkaConnectorResult) []string { return v.Topics }).(pulumi.StringArrayOutput)
}

func (o LookupKafkaConnectorResultOutput) Ttl() pulumi.IntOutput {
	return o.ApplyT(func(v LookupKafkaConnectorResult) int { return v.Ttl }).(pulumi.IntOutput)
}

func (o LookupKafkaConnectorResultOutput) UserPassword() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKafkaConnectorResult) string { return v.UserPassword }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupKafkaConnectorResultOutput{})
}
