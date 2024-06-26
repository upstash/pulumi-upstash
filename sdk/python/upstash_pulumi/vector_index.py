# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['VectorIndexArgs', 'VectorIndex']

@pulumi.input_type
class VectorIndexArgs:
    def __init__(__self__, *,
                 dimension_count: pulumi.Input[int],
                 region: pulumi.Input[str],
                 similarity_function: pulumi.Input[str],
                 type: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None,
                 reserved_price: Optional[pulumi.Input[float]] = None):
        """
        The set of arguments for constructing a VectorIndex resource.
        :param pulumi.Input[int] dimension_count: Size of the vector array.
        :param pulumi.Input[str] region: The region where your index is deployed.
        :param pulumi.Input[str] similarity_function: Associated distance metric to calculate the similarity.
        :param pulumi.Input[str] type: Associated plan of the index. Either `free`, `paid`, `fixed` or `pro`.
        :param pulumi.Input[str] name: Name of the index.
        :param pulumi.Input[float] reserved_price: Monthly pricing of your index. Only available for fixed and pro plans.
        """
        pulumi.set(__self__, "dimension_count", dimension_count)
        pulumi.set(__self__, "region", region)
        pulumi.set(__self__, "similarity_function", similarity_function)
        pulumi.set(__self__, "type", type)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if reserved_price is not None:
            pulumi.set(__self__, "reserved_price", reserved_price)

    @property
    @pulumi.getter(name="dimensionCount")
    def dimension_count(self) -> pulumi.Input[int]:
        """
        Size of the vector array.
        """
        return pulumi.get(self, "dimension_count")

    @dimension_count.setter
    def dimension_count(self, value: pulumi.Input[int]):
        pulumi.set(self, "dimension_count", value)

    @property
    @pulumi.getter
    def region(self) -> pulumi.Input[str]:
        """
        The region where your index is deployed.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: pulumi.Input[str]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="similarityFunction")
    def similarity_function(self) -> pulumi.Input[str]:
        """
        Associated distance metric to calculate the similarity.
        """
        return pulumi.get(self, "similarity_function")

    @similarity_function.setter
    def similarity_function(self, value: pulumi.Input[str]):
        pulumi.set(self, "similarity_function", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        Associated plan of the index. Either `free`, `paid`, `fixed` or `pro`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the index.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="reservedPrice")
    def reserved_price(self) -> Optional[pulumi.Input[float]]:
        """
        Monthly pricing of your index. Only available for fixed and pro plans.
        """
        return pulumi.get(self, "reserved_price")

    @reserved_price.setter
    def reserved_price(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "reserved_price", value)


@pulumi.input_type
class _VectorIndexState:
    def __init__(__self__, *,
                 creation_time: Optional[pulumi.Input[int]] = None,
                 customer_id: Optional[pulumi.Input[str]] = None,
                 dimension_count: Optional[pulumi.Input[int]] = None,
                 endpoint: Optional[pulumi.Input[str]] = None,
                 max_daily_queries: Optional[pulumi.Input[int]] = None,
                 max_daily_updates: Optional[pulumi.Input[int]] = None,
                 max_monthly_bandwidth: Optional[pulumi.Input[int]] = None,
                 max_query_per_second: Optional[pulumi.Input[int]] = None,
                 max_reads_per_request: Optional[pulumi.Input[int]] = None,
                 max_total_metadata_size: Optional[pulumi.Input[int]] = None,
                 max_vector_count: Optional[pulumi.Input[int]] = None,
                 max_writes_per_request: Optional[pulumi.Input[int]] = None,
                 max_writes_per_second: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 read_only_token: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 reserved_price: Optional[pulumi.Input[float]] = None,
                 similarity_function: Optional[pulumi.Input[str]] = None,
                 token: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering VectorIndex resources.
        :param pulumi.Input[int] creation_time: The creation time of the vector index in UTC as unix timestamp.
        :param pulumi.Input[str] customer_id: The unique ID associated to the owner of this index.
        :param pulumi.Input[int] dimension_count: Size of the vector array.
        :param pulumi.Input[str] endpoint: Associated endpoint of your index.
        :param pulumi.Input[int] max_daily_queries: The number of maximum query operations you can perform in a day. Only query operations are included in query count.
        :param pulumi.Input[int] max_daily_updates: The number of maximum update operations you can perform in a day. Only upsert operations are included in update count.
        :param pulumi.Input[int] max_monthly_bandwidth: The maximum amount of monthly bandwidth for the index. Unit is bytes. `-1` if the limit is unlimited.
        :param pulumi.Input[int] max_query_per_second: The number of maximum query operations you can perform per second. Only query operations are included in query count.
        :param pulumi.Input[int] max_reads_per_request: The number of maximum vectors in a read operation. Query and fetch operations are included in read operations.
        :param pulumi.Input[int] max_total_metadata_size: The amount of maximum size for the total metadata sizes in your index.
        :param pulumi.Input[int] max_vector_count: The number of maximum that your index can contain.
        :param pulumi.Input[int] max_writes_per_request: The number of maximum vectors in a write operation. Only upsert operations are included in write operations.
        :param pulumi.Input[int] max_writes_per_second: The number of maximum write operations you can perform per second. Only upsert operations are included in write count.
        :param pulumi.Input[str] name: Name of the index.
        :param pulumi.Input[str] read_only_token: Readonly REST token to send request to the related index. You can't perform update operation with this token.
        :param pulumi.Input[str] region: The region where your index is deployed.
        :param pulumi.Input[float] reserved_price: Monthly pricing of your index. Only available for fixed and pro plans.
        :param pulumi.Input[str] similarity_function: Associated distance metric to calculate the similarity.
        :param pulumi.Input[str] token: REST token to send request to the related index.
        :param pulumi.Input[str] type: Associated plan of the index. Either `free`, `paid`, `fixed` or `pro`.
        """
        if creation_time is not None:
            pulumi.set(__self__, "creation_time", creation_time)
        if customer_id is not None:
            pulumi.set(__self__, "customer_id", customer_id)
        if dimension_count is not None:
            pulumi.set(__self__, "dimension_count", dimension_count)
        if endpoint is not None:
            pulumi.set(__self__, "endpoint", endpoint)
        if max_daily_queries is not None:
            pulumi.set(__self__, "max_daily_queries", max_daily_queries)
        if max_daily_updates is not None:
            pulumi.set(__self__, "max_daily_updates", max_daily_updates)
        if max_monthly_bandwidth is not None:
            pulumi.set(__self__, "max_monthly_bandwidth", max_monthly_bandwidth)
        if max_query_per_second is not None:
            pulumi.set(__self__, "max_query_per_second", max_query_per_second)
        if max_reads_per_request is not None:
            pulumi.set(__self__, "max_reads_per_request", max_reads_per_request)
        if max_total_metadata_size is not None:
            pulumi.set(__self__, "max_total_metadata_size", max_total_metadata_size)
        if max_vector_count is not None:
            pulumi.set(__self__, "max_vector_count", max_vector_count)
        if max_writes_per_request is not None:
            pulumi.set(__self__, "max_writes_per_request", max_writes_per_request)
        if max_writes_per_second is not None:
            pulumi.set(__self__, "max_writes_per_second", max_writes_per_second)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if read_only_token is not None:
            pulumi.set(__self__, "read_only_token", read_only_token)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if reserved_price is not None:
            pulumi.set(__self__, "reserved_price", reserved_price)
        if similarity_function is not None:
            pulumi.set(__self__, "similarity_function", similarity_function)
        if token is not None:
            pulumi.set(__self__, "token", token)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[pulumi.Input[int]]:
        """
        The creation time of the vector index in UTC as unix timestamp.
        """
        return pulumi.get(self, "creation_time")

    @creation_time.setter
    def creation_time(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "creation_time", value)

    @property
    @pulumi.getter(name="customerId")
    def customer_id(self) -> Optional[pulumi.Input[str]]:
        """
        The unique ID associated to the owner of this index.
        """
        return pulumi.get(self, "customer_id")

    @customer_id.setter
    def customer_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "customer_id", value)

    @property
    @pulumi.getter(name="dimensionCount")
    def dimension_count(self) -> Optional[pulumi.Input[int]]:
        """
        Size of the vector array.
        """
        return pulumi.get(self, "dimension_count")

    @dimension_count.setter
    def dimension_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "dimension_count", value)

    @property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[str]]:
        """
        Associated endpoint of your index.
        """
        return pulumi.get(self, "endpoint")

    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "endpoint", value)

    @property
    @pulumi.getter(name="maxDailyQueries")
    def max_daily_queries(self) -> Optional[pulumi.Input[int]]:
        """
        The number of maximum query operations you can perform in a day. Only query operations are included in query count.
        """
        return pulumi.get(self, "max_daily_queries")

    @max_daily_queries.setter
    def max_daily_queries(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_daily_queries", value)

    @property
    @pulumi.getter(name="maxDailyUpdates")
    def max_daily_updates(self) -> Optional[pulumi.Input[int]]:
        """
        The number of maximum update operations you can perform in a day. Only upsert operations are included in update count.
        """
        return pulumi.get(self, "max_daily_updates")

    @max_daily_updates.setter
    def max_daily_updates(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_daily_updates", value)

    @property
    @pulumi.getter(name="maxMonthlyBandwidth")
    def max_monthly_bandwidth(self) -> Optional[pulumi.Input[int]]:
        """
        The maximum amount of monthly bandwidth for the index. Unit is bytes. `-1` if the limit is unlimited.
        """
        return pulumi.get(self, "max_monthly_bandwidth")

    @max_monthly_bandwidth.setter
    def max_monthly_bandwidth(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_monthly_bandwidth", value)

    @property
    @pulumi.getter(name="maxQueryPerSecond")
    def max_query_per_second(self) -> Optional[pulumi.Input[int]]:
        """
        The number of maximum query operations you can perform per second. Only query operations are included in query count.
        """
        return pulumi.get(self, "max_query_per_second")

    @max_query_per_second.setter
    def max_query_per_second(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_query_per_second", value)

    @property
    @pulumi.getter(name="maxReadsPerRequest")
    def max_reads_per_request(self) -> Optional[pulumi.Input[int]]:
        """
        The number of maximum vectors in a read operation. Query and fetch operations are included in read operations.
        """
        return pulumi.get(self, "max_reads_per_request")

    @max_reads_per_request.setter
    def max_reads_per_request(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_reads_per_request", value)

    @property
    @pulumi.getter(name="maxTotalMetadataSize")
    def max_total_metadata_size(self) -> Optional[pulumi.Input[int]]:
        """
        The amount of maximum size for the total metadata sizes in your index.
        """
        return pulumi.get(self, "max_total_metadata_size")

    @max_total_metadata_size.setter
    def max_total_metadata_size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_total_metadata_size", value)

    @property
    @pulumi.getter(name="maxVectorCount")
    def max_vector_count(self) -> Optional[pulumi.Input[int]]:
        """
        The number of maximum that your index can contain.
        """
        return pulumi.get(self, "max_vector_count")

    @max_vector_count.setter
    def max_vector_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_vector_count", value)

    @property
    @pulumi.getter(name="maxWritesPerRequest")
    def max_writes_per_request(self) -> Optional[pulumi.Input[int]]:
        """
        The number of maximum vectors in a write operation. Only upsert operations are included in write operations.
        """
        return pulumi.get(self, "max_writes_per_request")

    @max_writes_per_request.setter
    def max_writes_per_request(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_writes_per_request", value)

    @property
    @pulumi.getter(name="maxWritesPerSecond")
    def max_writes_per_second(self) -> Optional[pulumi.Input[int]]:
        """
        The number of maximum write operations you can perform per second. Only upsert operations are included in write count.
        """
        return pulumi.get(self, "max_writes_per_second")

    @max_writes_per_second.setter
    def max_writes_per_second(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_writes_per_second", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the index.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="readOnlyToken")
    def read_only_token(self) -> Optional[pulumi.Input[str]]:
        """
        Readonly REST token to send request to the related index. You can't perform update operation with this token.
        """
        return pulumi.get(self, "read_only_token")

    @read_only_token.setter
    def read_only_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "read_only_token", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region where your index is deployed.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="reservedPrice")
    def reserved_price(self) -> Optional[pulumi.Input[float]]:
        """
        Monthly pricing of your index. Only available for fixed and pro plans.
        """
        return pulumi.get(self, "reserved_price")

    @reserved_price.setter
    def reserved_price(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "reserved_price", value)

    @property
    @pulumi.getter(name="similarityFunction")
    def similarity_function(self) -> Optional[pulumi.Input[str]]:
        """
        Associated distance metric to calculate the similarity.
        """
        return pulumi.get(self, "similarity_function")

    @similarity_function.setter
    def similarity_function(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "similarity_function", value)

    @property
    @pulumi.getter
    def token(self) -> Optional[pulumi.Input[str]]:
        """
        REST token to send request to the related index.
        """
        return pulumi.get(self, "token")

    @token.setter
    def token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "token", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        Associated plan of the index. Either `free`, `paid`, `fixed` or `pro`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


class VectorIndex(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dimension_count: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 reserved_price: Optional[pulumi.Input[float]] = None,
                 similarity_function: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage

        ```python
        import pulumi
        import upstash_pulumi as upstash

        vector_resource = upstash.VectorIndex("vectorResource",
            dimension_count=1536,
            region="us-east-1",
            similarity_function="COSINE",
            type="fixed")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] dimension_count: Size of the vector array.
        :param pulumi.Input[str] name: Name of the index.
        :param pulumi.Input[str] region: The region where your index is deployed.
        :param pulumi.Input[float] reserved_price: Monthly pricing of your index. Only available for fixed and pro plans.
        :param pulumi.Input[str] similarity_function: Associated distance metric to calculate the similarity.
        :param pulumi.Input[str] type: Associated plan of the index. Either `free`, `paid`, `fixed` or `pro`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VectorIndexArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ```python
        import pulumi
        import upstash_pulumi as upstash

        vector_resource = upstash.VectorIndex("vectorResource",
            dimension_count=1536,
            region="us-east-1",
            similarity_function="COSINE",
            type="fixed")
        ```

        :param str resource_name: The name of the resource.
        :param VectorIndexArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VectorIndexArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dimension_count: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 reserved_price: Optional[pulumi.Input[float]] = None,
                 similarity_function: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.plugin_download_url is None:
            opts.plugin_download_url = _utilities.get_plugin_download_url()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VectorIndexArgs.__new__(VectorIndexArgs)

            if dimension_count is None and not opts.urn:
                raise TypeError("Missing required property 'dimension_count'")
            __props__.__dict__["dimension_count"] = dimension_count
            __props__.__dict__["name"] = name
            if region is None and not opts.urn:
                raise TypeError("Missing required property 'region'")
            __props__.__dict__["region"] = region
            __props__.__dict__["reserved_price"] = reserved_price
            if similarity_function is None and not opts.urn:
                raise TypeError("Missing required property 'similarity_function'")
            __props__.__dict__["similarity_function"] = similarity_function
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
            __props__.__dict__["creation_time"] = None
            __props__.__dict__["customer_id"] = None
            __props__.__dict__["endpoint"] = None
            __props__.__dict__["max_daily_queries"] = None
            __props__.__dict__["max_daily_updates"] = None
            __props__.__dict__["max_monthly_bandwidth"] = None
            __props__.__dict__["max_query_per_second"] = None
            __props__.__dict__["max_reads_per_request"] = None
            __props__.__dict__["max_total_metadata_size"] = None
            __props__.__dict__["max_vector_count"] = None
            __props__.__dict__["max_writes_per_request"] = None
            __props__.__dict__["max_writes_per_second"] = None
            __props__.__dict__["read_only_token"] = None
            __props__.__dict__["token"] = None
        super(VectorIndex, __self__).__init__(
            'upstash:index/vectorIndex:VectorIndex',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            creation_time: Optional[pulumi.Input[int]] = None,
            customer_id: Optional[pulumi.Input[str]] = None,
            dimension_count: Optional[pulumi.Input[int]] = None,
            endpoint: Optional[pulumi.Input[str]] = None,
            max_daily_queries: Optional[pulumi.Input[int]] = None,
            max_daily_updates: Optional[pulumi.Input[int]] = None,
            max_monthly_bandwidth: Optional[pulumi.Input[int]] = None,
            max_query_per_second: Optional[pulumi.Input[int]] = None,
            max_reads_per_request: Optional[pulumi.Input[int]] = None,
            max_total_metadata_size: Optional[pulumi.Input[int]] = None,
            max_vector_count: Optional[pulumi.Input[int]] = None,
            max_writes_per_request: Optional[pulumi.Input[int]] = None,
            max_writes_per_second: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            read_only_token: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            reserved_price: Optional[pulumi.Input[float]] = None,
            similarity_function: Optional[pulumi.Input[str]] = None,
            token: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'VectorIndex':
        """
        Get an existing VectorIndex resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] creation_time: The creation time of the vector index in UTC as unix timestamp.
        :param pulumi.Input[str] customer_id: The unique ID associated to the owner of this index.
        :param pulumi.Input[int] dimension_count: Size of the vector array.
        :param pulumi.Input[str] endpoint: Associated endpoint of your index.
        :param pulumi.Input[int] max_daily_queries: The number of maximum query operations you can perform in a day. Only query operations are included in query count.
        :param pulumi.Input[int] max_daily_updates: The number of maximum update operations you can perform in a day. Only upsert operations are included in update count.
        :param pulumi.Input[int] max_monthly_bandwidth: The maximum amount of monthly bandwidth for the index. Unit is bytes. `-1` if the limit is unlimited.
        :param pulumi.Input[int] max_query_per_second: The number of maximum query operations you can perform per second. Only query operations are included in query count.
        :param pulumi.Input[int] max_reads_per_request: The number of maximum vectors in a read operation. Query and fetch operations are included in read operations.
        :param pulumi.Input[int] max_total_metadata_size: The amount of maximum size for the total metadata sizes in your index.
        :param pulumi.Input[int] max_vector_count: The number of maximum that your index can contain.
        :param pulumi.Input[int] max_writes_per_request: The number of maximum vectors in a write operation. Only upsert operations are included in write operations.
        :param pulumi.Input[int] max_writes_per_second: The number of maximum write operations you can perform per second. Only upsert operations are included in write count.
        :param pulumi.Input[str] name: Name of the index.
        :param pulumi.Input[str] read_only_token: Readonly REST token to send request to the related index. You can't perform update operation with this token.
        :param pulumi.Input[str] region: The region where your index is deployed.
        :param pulumi.Input[float] reserved_price: Monthly pricing of your index. Only available for fixed and pro plans.
        :param pulumi.Input[str] similarity_function: Associated distance metric to calculate the similarity.
        :param pulumi.Input[str] token: REST token to send request to the related index.
        :param pulumi.Input[str] type: Associated plan of the index. Either `free`, `paid`, `fixed` or `pro`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _VectorIndexState.__new__(_VectorIndexState)

        __props__.__dict__["creation_time"] = creation_time
        __props__.__dict__["customer_id"] = customer_id
        __props__.__dict__["dimension_count"] = dimension_count
        __props__.__dict__["endpoint"] = endpoint
        __props__.__dict__["max_daily_queries"] = max_daily_queries
        __props__.__dict__["max_daily_updates"] = max_daily_updates
        __props__.__dict__["max_monthly_bandwidth"] = max_monthly_bandwidth
        __props__.__dict__["max_query_per_second"] = max_query_per_second
        __props__.__dict__["max_reads_per_request"] = max_reads_per_request
        __props__.__dict__["max_total_metadata_size"] = max_total_metadata_size
        __props__.__dict__["max_vector_count"] = max_vector_count
        __props__.__dict__["max_writes_per_request"] = max_writes_per_request
        __props__.__dict__["max_writes_per_second"] = max_writes_per_second
        __props__.__dict__["name"] = name
        __props__.__dict__["read_only_token"] = read_only_token
        __props__.__dict__["region"] = region
        __props__.__dict__["reserved_price"] = reserved_price
        __props__.__dict__["similarity_function"] = similarity_function
        __props__.__dict__["token"] = token
        __props__.__dict__["type"] = type
        return VectorIndex(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[int]:
        """
        The creation time of the vector index in UTC as unix timestamp.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="customerId")
    def customer_id(self) -> pulumi.Output[str]:
        """
        The unique ID associated to the owner of this index.
        """
        return pulumi.get(self, "customer_id")

    @property
    @pulumi.getter(name="dimensionCount")
    def dimension_count(self) -> pulumi.Output[int]:
        """
        Size of the vector array.
        """
        return pulumi.get(self, "dimension_count")

    @property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[str]:
        """
        Associated endpoint of your index.
        """
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter(name="maxDailyQueries")
    def max_daily_queries(self) -> pulumi.Output[int]:
        """
        The number of maximum query operations you can perform in a day. Only query operations are included in query count.
        """
        return pulumi.get(self, "max_daily_queries")

    @property
    @pulumi.getter(name="maxDailyUpdates")
    def max_daily_updates(self) -> pulumi.Output[int]:
        """
        The number of maximum update operations you can perform in a day. Only upsert operations are included in update count.
        """
        return pulumi.get(self, "max_daily_updates")

    @property
    @pulumi.getter(name="maxMonthlyBandwidth")
    def max_monthly_bandwidth(self) -> pulumi.Output[int]:
        """
        The maximum amount of monthly bandwidth for the index. Unit is bytes. `-1` if the limit is unlimited.
        """
        return pulumi.get(self, "max_monthly_bandwidth")

    @property
    @pulumi.getter(name="maxQueryPerSecond")
    def max_query_per_second(self) -> pulumi.Output[int]:
        """
        The number of maximum query operations you can perform per second. Only query operations are included in query count.
        """
        return pulumi.get(self, "max_query_per_second")

    @property
    @pulumi.getter(name="maxReadsPerRequest")
    def max_reads_per_request(self) -> pulumi.Output[int]:
        """
        The number of maximum vectors in a read operation. Query and fetch operations are included in read operations.
        """
        return pulumi.get(self, "max_reads_per_request")

    @property
    @pulumi.getter(name="maxTotalMetadataSize")
    def max_total_metadata_size(self) -> pulumi.Output[int]:
        """
        The amount of maximum size for the total metadata sizes in your index.
        """
        return pulumi.get(self, "max_total_metadata_size")

    @property
    @pulumi.getter(name="maxVectorCount")
    def max_vector_count(self) -> pulumi.Output[int]:
        """
        The number of maximum that your index can contain.
        """
        return pulumi.get(self, "max_vector_count")

    @property
    @pulumi.getter(name="maxWritesPerRequest")
    def max_writes_per_request(self) -> pulumi.Output[int]:
        """
        The number of maximum vectors in a write operation. Only upsert operations are included in write operations.
        """
        return pulumi.get(self, "max_writes_per_request")

    @property
    @pulumi.getter(name="maxWritesPerSecond")
    def max_writes_per_second(self) -> pulumi.Output[int]:
        """
        The number of maximum write operations you can perform per second. Only upsert operations are included in write count.
        """
        return pulumi.get(self, "max_writes_per_second")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the index.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="readOnlyToken")
    def read_only_token(self) -> pulumi.Output[str]:
        """
        Readonly REST token to send request to the related index. You can't perform update operation with this token.
        """
        return pulumi.get(self, "read_only_token")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The region where your index is deployed.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="reservedPrice")
    def reserved_price(self) -> pulumi.Output[float]:
        """
        Monthly pricing of your index. Only available for fixed and pro plans.
        """
        return pulumi.get(self, "reserved_price")

    @property
    @pulumi.getter(name="similarityFunction")
    def similarity_function(self) -> pulumi.Output[str]:
        """
        Associated distance metric to calculate the similarity.
        """
        return pulumi.get(self, "similarity_function")

    @property
    @pulumi.getter
    def token(self) -> pulumi.Output[str]:
        """
        REST token to send request to the related index.
        """
        return pulumi.get(self, "token")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Associated plan of the index. Either `free`, `paid`, `fixed` or `pro`.
        """
        return pulumi.get(self, "type")

