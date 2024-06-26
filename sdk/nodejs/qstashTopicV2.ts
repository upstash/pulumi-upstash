// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class QStashTopicV2 extends pulumi.CustomResource {
    /**
     * Get an existing QStashTopicV2 resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: QStashTopicV2State, opts?: pulumi.CustomResourceOptions): QStashTopicV2 {
        return new QStashTopicV2(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'upstash:index/qStashTopicV2:QStashTopicV2';

    /**
     * Returns true if the given object is an instance of QStashTopicV2.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is QStashTopicV2 {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === QStashTopicV2.__pulumiType;
    }

    /**
     * Creation time for Qstash Topic.
     */
    public /*out*/ readonly createdAt!: pulumi.Output<number>;
    /**
     * Endpoints for the Qstash Topic
     */
    public readonly endpoints!: pulumi.Output<string[]>;
    /**
     * Name of the Qstash Topic
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Last Update time for Qstash Topic.
     */
    public /*out*/ readonly updatedAt!: pulumi.Output<number>;

    /**
     * Create a QStashTopicV2 resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: QStashTopicV2Args, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: QStashTopicV2Args | QStashTopicV2State, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as QStashTopicV2State | undefined;
            resourceInputs["createdAt"] = state ? state.createdAt : undefined;
            resourceInputs["endpoints"] = state ? state.endpoints : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["updatedAt"] = state ? state.updatedAt : undefined;
        } else {
            const args = argsOrState as QStashTopicV2Args | undefined;
            if ((!args || args.endpoints === undefined) && !opts.urn) {
                throw new Error("Missing required property 'endpoints'");
            }
            resourceInputs["endpoints"] = args ? args.endpoints : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["createdAt"] = undefined /*out*/;
            resourceInputs["updatedAt"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(QStashTopicV2.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering QStashTopicV2 resources.
 */
export interface QStashTopicV2State {
    /**
     * Creation time for Qstash Topic.
     */
    createdAt?: pulumi.Input<number>;
    /**
     * Endpoints for the Qstash Topic
     */
    endpoints?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Name of the Qstash Topic
     */
    name?: pulumi.Input<string>;
    /**
     * Last Update time for Qstash Topic.
     */
    updatedAt?: pulumi.Input<number>;
}

/**
 * The set of arguments for constructing a QStashTopicV2 resource.
 */
export interface QStashTopicV2Args {
    /**
     * Endpoints for the Qstash Topic
     */
    endpoints: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Name of the Qstash Topic
     */
    name?: pulumi.Input<string>;
}
