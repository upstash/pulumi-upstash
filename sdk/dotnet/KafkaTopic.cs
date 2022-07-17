// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Upstash.Upstash
{
    /// <summary>
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using Upstash = Upstash.Upstash;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         // Not necessary if the topic belongs to an already created cluster.
    ///         var exampleKafkaCluster = new Upstash.KafkaCluster("exampleKafkaCluster", new Upstash.KafkaClusterArgs
    ///         {
    ///             ClusterName = "Terraform_Upstash_Cluster",
    ///             Region = "eu-west-1",
    ///             Multizone = false,
    ///         });
    ///         var exampleKafkaTopic = new Upstash.KafkaTopic("exampleKafkaTopic", new Upstash.KafkaTopicArgs
    ///         {
    ///             TopicName = "TerraformTopic",
    ///             Partitions = 1,
    ///             RetentionTime = 625135,
    ///             RetentionSize = 725124,
    ///             MaxMessageSize = 829213,
    ///             CleanupPolicy = "delete",
    ///             ClusterId = resource.Upstash_kafka_cluster.ExampleKafkaCluster.Cluster_id,
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    [UpstashResourceType("upstash:index/kafkaTopic:KafkaTopic")]
    public partial class KafkaTopic : Pulumi.CustomResource
    {
        /// <summary>
        /// Cleanup policy will be used in the topic(compact or delete)
        /// </summary>
        [Output("cleanupPolicy")]
        public Output<string> CleanupPolicy { get; private set; } = null!;

        /// <summary>
        /// ID of the cluster the topic will be deployed in
        /// </summary>
        [Output("clusterId")]
        public Output<string> ClusterId { get; private set; } = null!;

        /// <summary>
        /// Creation time of the topic
        /// </summary>
        [Output("creationTime")]
        public Output<int> CreationTime { get; private set; } = null!;

        /// <summary>
        /// Max message size in the topic
        /// </summary>
        [Output("maxMessageSize")]
        public Output<int> MaxMessageSize { get; private set; } = null!;

        /// <summary>
        /// Whether multizone replication is enabled
        /// </summary>
        [Output("multizone")]
        public Output<bool> Multizone { get; private set; } = null!;

        /// <summary>
        /// The number of partitions the topic will have
        /// </summary>
        [Output("partitions")]
        public Output<int> Partitions { get; private set; } = null!;

        /// <summary>
        /// Password to be used in authenticating to the cluster
        /// </summary>
        [Output("password")]
        public Output<string> Password { get; private set; } = null!;

        /// <summary>
        /// Region of the kafka topic
        /// </summary>
        [Output("region")]
        public Output<string> Region { get; private set; } = null!;

        /// <summary>
        /// REST Endpoint of the kafka topic
        /// </summary>
        [Output("restEndpoint")]
        public Output<string> RestEndpoint { get; private set; } = null!;

        /// <summary>
        /// Retention size of the messages in the topic
        /// </summary>
        [Output("retentionSize")]
        public Output<int> RetentionSize { get; private set; } = null!;

        /// <summary>
        /// Retention time of messages in the topic
        /// </summary>
        [Output("retentionTime")]
        public Output<int> RetentionTime { get; private set; } = null!;

        /// <summary>
        /// State of the kafka topic (active or deleted)
        /// </summary>
        [Output("state")]
        public Output<string> State { get; private set; } = null!;

        /// <summary>
        /// TCP Endpoint of the kafka topic
        /// </summary>
        [Output("tcpEndpoint")]
        public Output<string> TcpEndpoint { get; private set; } = null!;

        /// <summary>
        /// Unique Cluster ID for created topic
        /// </summary>
        [Output("topicId")]
        public Output<string> TopicId { get; private set; } = null!;

        /// <summary>
        /// Name of the topic
        /// </summary>
        [Output("topicName")]
        public Output<string> TopicName { get; private set; } = null!;

        /// <summary>
        /// Base64 encoded username to be used in authenticating to the cluster
        /// </summary>
        [Output("username")]
        public Output<string> Username { get; private set; } = null!;


        /// <summary>
        /// Create a KafkaTopic resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public KafkaTopic(string name, KafkaTopicArgs args, CustomResourceOptions? options = null)
            : base("upstash:index/kafkaTopic:KafkaTopic", name, args ?? new KafkaTopicArgs(), MakeResourceOptions(options, ""))
        {
        }

        private KafkaTopic(string name, Input<string> id, KafkaTopicState? state = null, CustomResourceOptions? options = null)
            : base("upstash:index/kafkaTopic:KafkaTopic", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "https://github.com/upstash/upstash-pulumi-provider/releases/download/v${VERSION}",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing KafkaTopic resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static KafkaTopic Get(string name, Input<string> id, KafkaTopicState? state = null, CustomResourceOptions? options = null)
        {
            return new KafkaTopic(name, id, state, options);
        }
    }

    public sealed class KafkaTopicArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Cleanup policy will be used in the topic(compact or delete)
        /// </summary>
        [Input("cleanupPolicy", required: true)]
        public Input<string> CleanupPolicy { get; set; } = null!;

        /// <summary>
        /// ID of the cluster the topic will be deployed in
        /// </summary>
        [Input("clusterId", required: true)]
        public Input<string> ClusterId { get; set; } = null!;

        /// <summary>
        /// Max message size in the topic
        /// </summary>
        [Input("maxMessageSize", required: true)]
        public Input<int> MaxMessageSize { get; set; } = null!;

        /// <summary>
        /// The number of partitions the topic will have
        /// </summary>
        [Input("partitions", required: true)]
        public Input<int> Partitions { get; set; } = null!;

        /// <summary>
        /// Retention size of the messages in the topic
        /// </summary>
        [Input("retentionSize", required: true)]
        public Input<int> RetentionSize { get; set; } = null!;

        /// <summary>
        /// Retention time of messages in the topic
        /// </summary>
        [Input("retentionTime", required: true)]
        public Input<int> RetentionTime { get; set; } = null!;

        /// <summary>
        /// Name of the topic
        /// </summary>
        [Input("topicName", required: true)]
        public Input<string> TopicName { get; set; } = null!;

        public KafkaTopicArgs()
        {
        }
    }

    public sealed class KafkaTopicState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Cleanup policy will be used in the topic(compact or delete)
        /// </summary>
        [Input("cleanupPolicy")]
        public Input<string>? CleanupPolicy { get; set; }

        /// <summary>
        /// ID of the cluster the topic will be deployed in
        /// </summary>
        [Input("clusterId")]
        public Input<string>? ClusterId { get; set; }

        /// <summary>
        /// Creation time of the topic
        /// </summary>
        [Input("creationTime")]
        public Input<int>? CreationTime { get; set; }

        /// <summary>
        /// Max message size in the topic
        /// </summary>
        [Input("maxMessageSize")]
        public Input<int>? MaxMessageSize { get; set; }

        /// <summary>
        /// Whether multizone replication is enabled
        /// </summary>
        [Input("multizone")]
        public Input<bool>? Multizone { get; set; }

        /// <summary>
        /// The number of partitions the topic will have
        /// </summary>
        [Input("partitions")]
        public Input<int>? Partitions { get; set; }

        /// <summary>
        /// Password to be used in authenticating to the cluster
        /// </summary>
        [Input("password")]
        public Input<string>? Password { get; set; }

        /// <summary>
        /// Region of the kafka topic
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// REST Endpoint of the kafka topic
        /// </summary>
        [Input("restEndpoint")]
        public Input<string>? RestEndpoint { get; set; }

        /// <summary>
        /// Retention size of the messages in the topic
        /// </summary>
        [Input("retentionSize")]
        public Input<int>? RetentionSize { get; set; }

        /// <summary>
        /// Retention time of messages in the topic
        /// </summary>
        [Input("retentionTime")]
        public Input<int>? RetentionTime { get; set; }

        /// <summary>
        /// State of the kafka topic (active or deleted)
        /// </summary>
        [Input("state")]
        public Input<string>? State { get; set; }

        /// <summary>
        /// TCP Endpoint of the kafka topic
        /// </summary>
        [Input("tcpEndpoint")]
        public Input<string>? TcpEndpoint { get; set; }

        /// <summary>
        /// Unique Cluster ID for created topic
        /// </summary>
        [Input("topicId")]
        public Input<string>? TopicId { get; set; }

        /// <summary>
        /// Name of the topic
        /// </summary>
        [Input("topicName")]
        public Input<string>? TopicName { get; set; }

        /// <summary>
        /// Base64 encoded username to be used in authenticating to the cluster
        /// </summary>
        [Input("username")]
        public Input<string>? Username { get; set; }

        public KafkaTopicState()
        {
        }
    }
}
