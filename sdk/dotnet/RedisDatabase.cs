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
    ///         var exampleDB = new Upstash.RedisDatabase("exampleDB", new Upstash.RedisDatabaseArgs
    ///         {
    ///             DatabaseName = "Terraform DB6",
    ///             Multizone = true,
    ///             Region = "eu-west-1",
    ///             Tls = true,
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    [UpstashResourceType("upstash:index/redisDatabase:RedisDatabase")]
    public partial class RedisDatabase : Pulumi.CustomResource
    {
        /// <summary>
        /// When enabled, all writes are synchronously persisted to the disk.
        /// </summary>
        [Output("consistent")]
        public Output<bool?> Consistent { get; private set; } = null!;

        /// <summary>
        /// Creation time of the database
        /// </summary>
        [Output("creationTime")]
        public Output<int> CreationTime { get; private set; } = null!;

        /// <summary>
        /// Unique Database ID for created database
        /// </summary>
        [Output("databaseId")]
        public Output<string> DatabaseId { get; private set; } = null!;

        /// <summary>
        /// Name of the database
        /// </summary>
        [Output("databaseName")]
        public Output<string> DatabaseName { get; private set; } = null!;

        /// <summary>
        /// Type of the database
        /// </summary>
        [Output("databaseType")]
        public Output<string> DatabaseType { get; private set; } = null!;

        /// <summary>
        /// Daily bandwidth limit for the database
        /// </summary>
        [Output("dbDailyBandwidthLimit")]
        public Output<int> DbDailyBandwidthLimit { get; private set; } = null!;

        /// <summary>
        /// Disk threshold for the database
        /// </summary>
        [Output("dbDiskThreshold")]
        public Output<int> DbDiskThreshold { get; private set; } = null!;

        /// <summary>
        /// Max clients for the database
        /// </summary>
        [Output("dbMaxClients")]
        public Output<int> DbMaxClients { get; private set; } = null!;

        /// <summary>
        /// Max commands per second for the database
        /// </summary>
        [Output("dbMaxCommandsPerSecond")]
        public Output<int> DbMaxCommandsPerSecond { get; private set; } = null!;

        /// <summary>
        /// Max entry size for the database
        /// </summary>
        [Output("dbMaxEntrySize")]
        public Output<int> DbMaxEntrySize { get; private set; } = null!;

        /// <summary>
        /// Max request size for the database
        /// </summary>
        [Output("dbMaxRequestSize")]
        public Output<int> DbMaxRequestSize { get; private set; } = null!;

        /// <summary>
        /// Memory threshold for the database
        /// </summary>
        [Output("dbMemoryThreshold")]
        public Output<int> DbMemoryThreshold { get; private set; } = null!;

        /// <summary>
        /// Database URL for connection
        /// </summary>
        [Output("endpoint")]
        public Output<string> Endpoint { get; private set; } = null!;

        /// <summary>
        /// When enabled, database becomes highly available and is deployed in multiple zones. (If changed to false from true,
        /// results in deletion and recreation of the resource)
        /// </summary>
        [Output("multizone")]
        public Output<bool?> Multizone { get; private set; } = null!;

        /// <summary>
        /// Password of the database
        /// </summary>
        [Output("password")]
        public Output<string> Password { get; private set; } = null!;

        /// <summary>
        /// Port of the endpoint
        /// </summary>
        [Output("port")]
        public Output<int> Port { get; private set; } = null!;

        /// <summary>
        /// Rest Token for the database.
        /// </summary>
        [Output("readOnlyRestToken")]
        public Output<string> ReadOnlyRestToken { get; private set; } = null!;

        /// <summary>
        /// region of the database. Possible values are: "global", "eu-west-1", "us-east-1", "us-west-1", "ap-northeast-1" ,
        /// "eu-central1"
        /// </summary>
        [Output("region")]
        public Output<string> Region { get; private set; } = null!;

        /// <summary>
        /// Rest Token for the database.
        /// </summary>
        [Output("restToken")]
        public Output<string> RestToken { get; private set; } = null!;

        /// <summary>
        /// State of the database
        /// </summary>
        [Output("state")]
        public Output<string> State { get; private set; } = null!;

        /// <summary>
        /// When enabled, data is encrypted in transit. (If changed to false from true, results in deletion and recreation of the
        /// resource)
        /// </summary>
        [Output("tls")]
        public Output<bool> Tls { get; private set; } = null!;

        /// <summary>
        /// User email for the database
        /// </summary>
        [Output("userEmail")]
        public Output<string> UserEmail { get; private set; } = null!;


        /// <summary>
        /// Create a RedisDatabase resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public RedisDatabase(string name, RedisDatabaseArgs args, CustomResourceOptions? options = null)
            : base("upstash:index/redisDatabase:RedisDatabase", name, args ?? new RedisDatabaseArgs(), MakeResourceOptions(options, ""))
        {
        }

        private RedisDatabase(string name, Input<string> id, RedisDatabaseState? state = null, CustomResourceOptions? options = null)
            : base("upstash:index/redisDatabase:RedisDatabase", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "https://github.com/upstash/upstash-pulumi-provider/releases/download/v${VERSION}",
                AdditionalSecretOutputs =
                {
                    "password",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing RedisDatabase resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static RedisDatabase Get(string name, Input<string> id, RedisDatabaseState? state = null, CustomResourceOptions? options = null)
        {
            return new RedisDatabase(name, id, state, options);
        }
    }

    public sealed class RedisDatabaseArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// When enabled, all writes are synchronously persisted to the disk.
        /// </summary>
        [Input("consistent")]
        public Input<bool>? Consistent { get; set; }

        /// <summary>
        /// Name of the database
        /// </summary>
        [Input("databaseName", required: true)]
        public Input<string> DatabaseName { get; set; } = null!;

        /// <summary>
        /// When enabled, database becomes highly available and is deployed in multiple zones. (If changed to false from true,
        /// results in deletion and recreation of the resource)
        /// </summary>
        [Input("multizone")]
        public Input<bool>? Multizone { get; set; }

        /// <summary>
        /// region of the database. Possible values are: "global", "eu-west-1", "us-east-1", "us-west-1", "ap-northeast-1" ,
        /// "eu-central1"
        /// </summary>
        [Input("region", required: true)]
        public Input<string> Region { get; set; } = null!;

        /// <summary>
        /// When enabled, data is encrypted in transit. (If changed to false from true, results in deletion and recreation of the
        /// resource)
        /// </summary>
        [Input("tls")]
        public Input<bool>? Tls { get; set; }

        public RedisDatabaseArgs()
        {
        }
    }

    public sealed class RedisDatabaseState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// When enabled, all writes are synchronously persisted to the disk.
        /// </summary>
        [Input("consistent")]
        public Input<bool>? Consistent { get; set; }

        /// <summary>
        /// Creation time of the database
        /// </summary>
        [Input("creationTime")]
        public Input<int>? CreationTime { get; set; }

        /// <summary>
        /// Unique Database ID for created database
        /// </summary>
        [Input("databaseId")]
        public Input<string>? DatabaseId { get; set; }

        /// <summary>
        /// Name of the database
        /// </summary>
        [Input("databaseName")]
        public Input<string>? DatabaseName { get; set; }

        /// <summary>
        /// Type of the database
        /// </summary>
        [Input("databaseType")]
        public Input<string>? DatabaseType { get; set; }

        /// <summary>
        /// Daily bandwidth limit for the database
        /// </summary>
        [Input("dbDailyBandwidthLimit")]
        public Input<int>? DbDailyBandwidthLimit { get; set; }

        /// <summary>
        /// Disk threshold for the database
        /// </summary>
        [Input("dbDiskThreshold")]
        public Input<int>? DbDiskThreshold { get; set; }

        /// <summary>
        /// Max clients for the database
        /// </summary>
        [Input("dbMaxClients")]
        public Input<int>? DbMaxClients { get; set; }

        /// <summary>
        /// Max commands per second for the database
        /// </summary>
        [Input("dbMaxCommandsPerSecond")]
        public Input<int>? DbMaxCommandsPerSecond { get; set; }

        /// <summary>
        /// Max entry size for the database
        /// </summary>
        [Input("dbMaxEntrySize")]
        public Input<int>? DbMaxEntrySize { get; set; }

        /// <summary>
        /// Max request size for the database
        /// </summary>
        [Input("dbMaxRequestSize")]
        public Input<int>? DbMaxRequestSize { get; set; }

        /// <summary>
        /// Memory threshold for the database
        /// </summary>
        [Input("dbMemoryThreshold")]
        public Input<int>? DbMemoryThreshold { get; set; }

        /// <summary>
        /// Database URL for connection
        /// </summary>
        [Input("endpoint")]
        public Input<string>? Endpoint { get; set; }

        /// <summary>
        /// When enabled, database becomes highly available and is deployed in multiple zones. (If changed to false from true,
        /// results in deletion and recreation of the resource)
        /// </summary>
        [Input("multizone")]
        public Input<bool>? Multizone { get; set; }

        [Input("password")]
        private Input<string>? _password;

        /// <summary>
        /// Password of the database
        /// </summary>
        public Input<string>? Password
        {
            get => _password;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _password = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        /// <summary>
        /// Port of the endpoint
        /// </summary>
        [Input("port")]
        public Input<int>? Port { get; set; }

        /// <summary>
        /// Rest Token for the database.
        /// </summary>
        [Input("readOnlyRestToken")]
        public Input<string>? ReadOnlyRestToken { get; set; }

        /// <summary>
        /// region of the database. Possible values are: "global", "eu-west-1", "us-east-1", "us-west-1", "ap-northeast-1" ,
        /// "eu-central1"
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// Rest Token for the database.
        /// </summary>
        [Input("restToken")]
        public Input<string>? RestToken { get; set; }

        /// <summary>
        /// State of the database
        /// </summary>
        [Input("state")]
        public Input<string>? State { get; set; }

        /// <summary>
        /// When enabled, data is encrypted in transit. (If changed to false from true, results in deletion and recreation of the
        /// resource)
        /// </summary>
        [Input("tls")]
        public Input<bool>? Tls { get; set; }

        /// <summary>
        /// User email for the database
        /// </summary>
        [Input("userEmail")]
        public Input<string>? UserEmail { get; set; }

        public RedisDatabaseState()
        {
        }
    }
}
