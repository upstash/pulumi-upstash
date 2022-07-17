// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as upstash from "@upstash/upstash";
 *
 * // Not necessary if the topic belongs to an already created cluster.
 * const exampleKafkaCluster = new upstash.KafkaCluster("exampleKafkaCluster", {
 *     clusterName: "Terraform_Upstash_Cluster",
 *     region: "eu-west-1",
 *     multizone: false,
 * });
 * const exampleKafkaTopic = new upstash.KafkaTopic("exampleKafkaTopic", {
 *     topicName: "TerraformTopic",
 *     partitions: 1,
 *     retentionTime: 625135,
 *     retentionSize: 725124,
 *     maxMessageSize: 829213,
 *     cleanupPolicy: "delete",
 *     clusterId: resource.upstash_kafka_cluster.exampleKafkaCluster.cluster_id,
 * });
 * ```
 */
export class KafkaTopic extends pulumi.CustomResource {
    /**
     * Get an existing KafkaTopic resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: KafkaTopicState, opts?: pulumi.CustomResourceOptions): KafkaTopic {
        return new KafkaTopic(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'upstash:index/kafkaTopic:KafkaTopic';

    /**
     * Returns true if the given object is an instance of KafkaTopic.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is KafkaTopic {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === KafkaTopic.__pulumiType;
    }

    /**
     * Cleanup policy will be used in the topic(compact or delete)
     */
    public readonly cleanupPolicy!: pulumi.Output<string>;
    /**
     * ID of the cluster the topic will be deployed in
     */
    public readonly clusterId!: pulumi.Output<string>;
    /**
     * Creation time of the topic
     */
    public /*out*/ readonly creationTime!: pulumi.Output<number>;
    /**
     * Max message size in the topic
     */
    public readonly maxMessageSize!: pulumi.Output<number>;
    /**
     * Whether multizone replication is enabled
     */
    public /*out*/ readonly multizone!: pulumi.Output<boolean>;
    /**
     * The number of partitions the topic will have
     */
    public readonly partitions!: pulumi.Output<number>;
    /**
     * Password to be used in authenticating to the cluster
     */
    public /*out*/ readonly password!: pulumi.Output<string>;
    /**
     * Region of the kafka topic
     */
    public /*out*/ readonly region!: pulumi.Output<string>;
    /**
     * REST Endpoint of the kafka topic
     */
    public /*out*/ readonly restEndpoint!: pulumi.Output<string>;
    /**
     * Retention size of the messages in the topic
     */
    public readonly retentionSize!: pulumi.Output<number>;
    /**
     * Retention time of messages in the topic
     */
    public readonly retentionTime!: pulumi.Output<number>;
    /**
     * State of the kafka topic (active or deleted)
     */
    public /*out*/ readonly state!: pulumi.Output<string>;
    /**
     * TCP Endpoint of the kafka topic
     */
    public /*out*/ readonly tcpEndpoint!: pulumi.Output<string>;
    /**
     * Unique Cluster ID for created topic
     */
    public /*out*/ readonly topicId!: pulumi.Output<string>;
    /**
     * Name of the topic
     */
    public readonly topicName!: pulumi.Output<string>;
    /**
     * Base64 encoded username to be used in authenticating to the cluster
     */
    public /*out*/ readonly username!: pulumi.Output<string>;

    /**
     * Create a KafkaTopic resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: KafkaTopicArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: KafkaTopicArgs | KafkaTopicState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as KafkaTopicState | undefined;
            resourceInputs["cleanupPolicy"] = state ? state.cleanupPolicy : undefined;
            resourceInputs["clusterId"] = state ? state.clusterId : undefined;
            resourceInputs["creationTime"] = state ? state.creationTime : undefined;
            resourceInputs["maxMessageSize"] = state ? state.maxMessageSize : undefined;
            resourceInputs["multizone"] = state ? state.multizone : undefined;
            resourceInputs["partitions"] = state ? state.partitions : undefined;
            resourceInputs["password"] = state ? state.password : undefined;
            resourceInputs["region"] = state ? state.region : undefined;
            resourceInputs["restEndpoint"] = state ? state.restEndpoint : undefined;
            resourceInputs["retentionSize"] = state ? state.retentionSize : undefined;
            resourceInputs["retentionTime"] = state ? state.retentionTime : undefined;
            resourceInputs["state"] = state ? state.state : undefined;
            resourceInputs["tcpEndpoint"] = state ? state.tcpEndpoint : undefined;
            resourceInputs["topicId"] = state ? state.topicId : undefined;
            resourceInputs["topicName"] = state ? state.topicName : undefined;
            resourceInputs["username"] = state ? state.username : undefined;
        } else {
            const args = argsOrState as KafkaTopicArgs | undefined;
            if ((!args || args.cleanupPolicy === undefined) && !opts.urn) {
                throw new Error("Missing required property 'cleanupPolicy'");
            }
            if ((!args || args.clusterId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'clusterId'");
            }
            if ((!args || args.maxMessageSize === undefined) && !opts.urn) {
                throw new Error("Missing required property 'maxMessageSize'");
            }
            if ((!args || args.partitions === undefined) && !opts.urn) {
                throw new Error("Missing required property 'partitions'");
            }
            if ((!args || args.retentionSize === undefined) && !opts.urn) {
                throw new Error("Missing required property 'retentionSize'");
            }
            if ((!args || args.retentionTime === undefined) && !opts.urn) {
                throw new Error("Missing required property 'retentionTime'");
            }
            if ((!args || args.topicName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'topicName'");
            }
            resourceInputs["cleanupPolicy"] = args ? args.cleanupPolicy : undefined;
            resourceInputs["clusterId"] = args ? args.clusterId : undefined;
            resourceInputs["maxMessageSize"] = args ? args.maxMessageSize : undefined;
            resourceInputs["partitions"] = args ? args.partitions : undefined;
            resourceInputs["retentionSize"] = args ? args.retentionSize : undefined;
            resourceInputs["retentionTime"] = args ? args.retentionTime : undefined;
            resourceInputs["topicName"] = args ? args.topicName : undefined;
            resourceInputs["creationTime"] = undefined /*out*/;
            resourceInputs["multizone"] = undefined /*out*/;
            resourceInputs["password"] = undefined /*out*/;
            resourceInputs["region"] = undefined /*out*/;
            resourceInputs["restEndpoint"] = undefined /*out*/;
            resourceInputs["state"] = undefined /*out*/;
            resourceInputs["tcpEndpoint"] = undefined /*out*/;
            resourceInputs["topicId"] = undefined /*out*/;
            resourceInputs["username"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(KafkaTopic.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering KafkaTopic resources.
 */
export interface KafkaTopicState {
    /**
     * Cleanup policy will be used in the topic(compact or delete)
     */
    cleanupPolicy?: pulumi.Input<string>;
    /**
     * ID of the cluster the topic will be deployed in
     */
    clusterId?: pulumi.Input<string>;
    /**
     * Creation time of the topic
     */
    creationTime?: pulumi.Input<number>;
    /**
     * Max message size in the topic
     */
    maxMessageSize?: pulumi.Input<number>;
    /**
     * Whether multizone replication is enabled
     */
    multizone?: pulumi.Input<boolean>;
    /**
     * The number of partitions the topic will have
     */
    partitions?: pulumi.Input<number>;
    /**
     * Password to be used in authenticating to the cluster
     */
    password?: pulumi.Input<string>;
    /**
     * Region of the kafka topic
     */
    region?: pulumi.Input<string>;
    /**
     * REST Endpoint of the kafka topic
     */
    restEndpoint?: pulumi.Input<string>;
    /**
     * Retention size of the messages in the topic
     */
    retentionSize?: pulumi.Input<number>;
    /**
     * Retention time of messages in the topic
     */
    retentionTime?: pulumi.Input<number>;
    /**
     * State of the kafka topic (active or deleted)
     */
    state?: pulumi.Input<string>;
    /**
     * TCP Endpoint of the kafka topic
     */
    tcpEndpoint?: pulumi.Input<string>;
    /**
     * Unique Cluster ID for created topic
     */
    topicId?: pulumi.Input<string>;
    /**
     * Name of the topic
     */
    topicName?: pulumi.Input<string>;
    /**
     * Base64 encoded username to be used in authenticating to the cluster
     */
    username?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a KafkaTopic resource.
 */
export interface KafkaTopicArgs {
    /**
     * Cleanup policy will be used in the topic(compact or delete)
     */
    cleanupPolicy: pulumi.Input<string>;
    /**
     * ID of the cluster the topic will be deployed in
     */
    clusterId: pulumi.Input<string>;
    /**
     * Max message size in the topic
     */
    maxMessageSize: pulumi.Input<number>;
    /**
     * The number of partitions the topic will have
     */
    partitions: pulumi.Input<number>;
    /**
     * Retention size of the messages in the topic
     */
    retentionSize: pulumi.Input<number>;
    /**
     * Retention time of messages in the topic
     */
    retentionTime: pulumi.Input<number>;
    /**
     * Name of the topic
     */
    topicName: pulumi.Input<string>;
}
