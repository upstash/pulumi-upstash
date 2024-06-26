// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Upstash
{
    [UpstashResourceType("upstash:index/qStashTopicV2:QStashTopicV2")]
    public partial class QStashTopicV2 : Pulumi.CustomResource
    {
        /// <summary>
        /// Creation time for Qstash Topic.
        /// </summary>
        [Output("createdAt")]
        public Output<int> CreatedAt { get; private set; } = null!;

        /// <summary>
        /// Endpoints for the Qstash Topic
        /// </summary>
        [Output("endpoints")]
        public Output<ImmutableArray<string>> Endpoints { get; private set; } = null!;

        /// <summary>
        /// Name of the Qstash Topic
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Last Update time for Qstash Topic.
        /// </summary>
        [Output("updatedAt")]
        public Output<int> UpdatedAt { get; private set; } = null!;


        /// <summary>
        /// Create a QStashTopicV2 resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public QStashTopicV2(string name, QStashTopicV2Args args, CustomResourceOptions? options = null)
            : base("upstash:index/qStashTopicV2:QStashTopicV2", name, args ?? new QStashTopicV2Args(), MakeResourceOptions(options, ""))
        {
        }

        private QStashTopicV2(string name, Input<string> id, QStashTopicV2State? state = null, CustomResourceOptions? options = null)
            : base("upstash:index/qStashTopicV2:QStashTopicV2", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/upstash/pulumi-upstash",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing QStashTopicV2 resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static QStashTopicV2 Get(string name, Input<string> id, QStashTopicV2State? state = null, CustomResourceOptions? options = null)
        {
            return new QStashTopicV2(name, id, state, options);
        }
    }

    public sealed class QStashTopicV2Args : Pulumi.ResourceArgs
    {
        [Input("endpoints", required: true)]
        private InputList<string>? _endpoints;

        /// <summary>
        /// Endpoints for the Qstash Topic
        /// </summary>
        public InputList<string> Endpoints
        {
            get => _endpoints ?? (_endpoints = new InputList<string>());
            set => _endpoints = value;
        }

        /// <summary>
        /// Name of the Qstash Topic
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public QStashTopicV2Args()
        {
        }
    }

    public sealed class QStashTopicV2State : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Creation time for Qstash Topic.
        /// </summary>
        [Input("createdAt")]
        public Input<int>? CreatedAt { get; set; }

        [Input("endpoints")]
        private InputList<string>? _endpoints;

        /// <summary>
        /// Endpoints for the Qstash Topic
        /// </summary>
        public InputList<string> Endpoints
        {
            get => _endpoints ?? (_endpoints = new InputList<string>());
            set => _endpoints = value;
        }

        /// <summary>
        /// Name of the Qstash Topic
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Last Update time for Qstash Topic.
        /// </summary>
        [Input("updatedAt")]
        public Input<int>? UpdatedAt { get; set; }

        public QStashTopicV2State()
        {
        }
    }
}
