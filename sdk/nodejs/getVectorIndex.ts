// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export function getVectorIndex(args: GetVectorIndexArgs, opts?: pulumi.InvokeOptions): Promise<GetVectorIndexResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("upstash:index/getVectorIndex:getVectorIndex", {
        "id": args.id,
    }, opts);
}

/**
 * A collection of arguments for invoking getVectorIndex.
 */
export interface GetVectorIndexArgs {
    id: string;
}

/**
 * A collection of values returned by getVectorIndex.
 */
export interface GetVectorIndexResult {
    readonly creationTime: number;
    readonly customerId: string;
    readonly dimensionCount: number;
    readonly endpoint: string;
    readonly id: string;
    readonly maxDailyQueries: number;
    readonly maxDailyUpdates: number;
    readonly maxMonthlyBandwidth: number;
    readonly maxQueryPerSecond: number;
    readonly maxReadsPerRequest: number;
    readonly maxTotalMetadataSize: number;
    readonly maxVectorCount: number;
    readonly maxWritesPerRequest: number;
    readonly maxWritesPerSecond: number;
    readonly name: string;
    readonly readOnlyToken: string;
    readonly region: string;
    readonly reservedPrice: number;
    readonly similarityFunction: string;
    readonly token: string;
    readonly type: string;
}

export function getVectorIndexOutput(args: GetVectorIndexOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetVectorIndexResult> {
    return pulumi.output(args).apply(a => getVectorIndex(a, opts))
}

/**
 * A collection of arguments for invoking getVectorIndex.
 */
export interface GetVectorIndexOutputArgs {
    id: pulumi.Input<string>;
}
