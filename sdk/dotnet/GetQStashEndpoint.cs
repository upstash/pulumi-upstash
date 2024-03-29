// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Upstash
{
    public static class GetQStashEndpoint
    {
        /// <summary>
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Upstash = Pulumi.Upstash;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var exampleQstashEndpointData = Output.Create(Upstash.GetQStashEndpoint.InvokeAsync(new Upstash.GetQStashEndpointArgs
        ///         {
        ///             EndpointId = resource.Upstash_qstash_endpoint.ExampleQstashEndpoint.Endpoint_id,
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetQStashEndpointResult> InvokeAsync(GetQStashEndpointArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetQStashEndpointResult>("upstash:index/getQStashEndpoint:getQStashEndpoint", args ?? new GetQStashEndpointArgs(), options.WithDefaults());

        /// <summary>
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Upstash = Pulumi.Upstash;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var exampleQstashEndpointData = Output.Create(Upstash.GetQStashEndpoint.InvokeAsync(new Upstash.GetQStashEndpointArgs
        ///         {
        ///             EndpointId = resource.Upstash_qstash_endpoint.ExampleQstashEndpoint.Endpoint_id,
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetQStashEndpointResult> Invoke(GetQStashEndpointInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetQStashEndpointResult>("upstash:index/getQStashEndpoint:getQStashEndpoint", args ?? new GetQStashEndpointInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetQStashEndpointArgs : Pulumi.InvokeArgs
    {
        [Input("topicId", required: true)]
        public string TopicId { get; set; } = null!;

        public GetQStashEndpointArgs()
        {
        }
    }

    public sealed class GetQStashEndpointInvokeArgs : Pulumi.InvokeArgs
    {
        [Input("topicId", required: true)]
        public Input<string> TopicId { get; set; } = null!;

        public GetQStashEndpointInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetQStashEndpointResult
    {
        public readonly string EndpointId;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string TopicId;
        public readonly string Url;

        [OutputConstructor]
        private GetQStashEndpointResult(
            string endpointId,

            string id,

            string topicId,

            string url)
        {
            EndpointId = endpointId;
            Id = id;
            TopicId = topicId;
            Url = url;
        }
    }
}
