// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Upstash
{
    public static class GetQStashScheduleV2
    {
        public static Task<GetQStashScheduleV2Result> InvokeAsync(GetQStashScheduleV2Args args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetQStashScheduleV2Result>("upstash:index/getQStashScheduleV2:getQStashScheduleV2", args ?? new GetQStashScheduleV2Args(), options.WithDefaults());

        public static Output<GetQStashScheduleV2Result> Invoke(GetQStashScheduleV2InvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetQStashScheduleV2Result>("upstash:index/getQStashScheduleV2:getQStashScheduleV2", args ?? new GetQStashScheduleV2InvokeArgs(), options.WithDefaults());
    }


    public sealed class GetQStashScheduleV2Args : Pulumi.InvokeArgs
    {
        [Input("body")]
        public string? Body { get; set; }

        [Input("callback")]
        public string? Callback { get; set; }

        [Input("delay")]
        public string? Delay { get; set; }

        [Input("header")]
        public string? Header { get; set; }

        [Input("retries")]
        public int? Retries { get; set; }

        [Input("scheduleId", required: true)]
        public string ScheduleId { get; set; } = null!;

        public GetQStashScheduleV2Args()
        {
        }
    }

    public sealed class GetQStashScheduleV2InvokeArgs : Pulumi.InvokeArgs
    {
        [Input("body")]
        public Input<string>? Body { get; set; }

        [Input("callback")]
        public Input<string>? Callback { get; set; }

        [Input("delay")]
        public Input<string>? Delay { get; set; }

        [Input("header")]
        public Input<string>? Header { get; set; }

        [Input("retries")]
        public Input<int>? Retries { get; set; }

        [Input("scheduleId", required: true)]
        public Input<string> ScheduleId { get; set; } = null!;

        public GetQStashScheduleV2InvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetQStashScheduleV2Result
    {
        public readonly string? Body;
        public readonly string? Callback;
        public readonly int CreatedAt;
        public readonly string Cron;
        public readonly string? Delay;
        public readonly string Destination;
        public readonly string? Header;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string Method;
        public readonly int? Retries;
        public readonly string ScheduleId;

        [OutputConstructor]
        private GetQStashScheduleV2Result(
            string? body,

            string? callback,

            int createdAt,

            string cron,

            string? delay,

            string destination,

            string? header,

            string id,

            string method,

            int? retries,

            string scheduleId)
        {
            Body = body;
            Callback = callback;
            CreatedAt = createdAt;
            Cron = cron;
            Delay = delay;
            Destination = destination;
            Header = header;
            Id = id;
            Method = method;
            Retries = retries;
            ScheduleId = scheduleId;
        }
    }
}
