# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetVectorIndexResult',
    'AwaitableGetVectorIndexResult',
    'get_vector_index',
    'get_vector_index_output',
]

@pulumi.output_type
class GetVectorIndexResult:
    """
    A collection of values returned by getVectorIndex.
    """
    def __init__(__self__, creation_time=None, customer_id=None, dimension_count=None, endpoint=None, id=None, max_daily_queries=None, max_daily_updates=None, max_monthly_bandwidth=None, max_query_per_second=None, max_reads_per_request=None, max_total_metadata_size=None, max_vector_count=None, max_writes_per_request=None, max_writes_per_second=None, name=None, read_only_token=None, region=None, reserved_price=None, similarity_function=None, token=None, type=None):
        if creation_time and not isinstance(creation_time, int):
            raise TypeError("Expected argument 'creation_time' to be a int")
        pulumi.set(__self__, "creation_time", creation_time)
        if customer_id and not isinstance(customer_id, str):
            raise TypeError("Expected argument 'customer_id' to be a str")
        pulumi.set(__self__, "customer_id", customer_id)
        if dimension_count and not isinstance(dimension_count, int):
            raise TypeError("Expected argument 'dimension_count' to be a int")
        pulumi.set(__self__, "dimension_count", dimension_count)
        if endpoint and not isinstance(endpoint, str):
            raise TypeError("Expected argument 'endpoint' to be a str")
        pulumi.set(__self__, "endpoint", endpoint)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if max_daily_queries and not isinstance(max_daily_queries, int):
            raise TypeError("Expected argument 'max_daily_queries' to be a int")
        pulumi.set(__self__, "max_daily_queries", max_daily_queries)
        if max_daily_updates and not isinstance(max_daily_updates, int):
            raise TypeError("Expected argument 'max_daily_updates' to be a int")
        pulumi.set(__self__, "max_daily_updates", max_daily_updates)
        if max_monthly_bandwidth and not isinstance(max_monthly_bandwidth, int):
            raise TypeError("Expected argument 'max_monthly_bandwidth' to be a int")
        pulumi.set(__self__, "max_monthly_bandwidth", max_monthly_bandwidth)
        if max_query_per_second and not isinstance(max_query_per_second, int):
            raise TypeError("Expected argument 'max_query_per_second' to be a int")
        pulumi.set(__self__, "max_query_per_second", max_query_per_second)
        if max_reads_per_request and not isinstance(max_reads_per_request, int):
            raise TypeError("Expected argument 'max_reads_per_request' to be a int")
        pulumi.set(__self__, "max_reads_per_request", max_reads_per_request)
        if max_total_metadata_size and not isinstance(max_total_metadata_size, int):
            raise TypeError("Expected argument 'max_total_metadata_size' to be a int")
        pulumi.set(__self__, "max_total_metadata_size", max_total_metadata_size)
        if max_vector_count and not isinstance(max_vector_count, int):
            raise TypeError("Expected argument 'max_vector_count' to be a int")
        pulumi.set(__self__, "max_vector_count", max_vector_count)
        if max_writes_per_request and not isinstance(max_writes_per_request, int):
            raise TypeError("Expected argument 'max_writes_per_request' to be a int")
        pulumi.set(__self__, "max_writes_per_request", max_writes_per_request)
        if max_writes_per_second and not isinstance(max_writes_per_second, int):
            raise TypeError("Expected argument 'max_writes_per_second' to be a int")
        pulumi.set(__self__, "max_writes_per_second", max_writes_per_second)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if read_only_token and not isinstance(read_only_token, str):
            raise TypeError("Expected argument 'read_only_token' to be a str")
        pulumi.set(__self__, "read_only_token", read_only_token)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if reserved_price and not isinstance(reserved_price, float):
            raise TypeError("Expected argument 'reserved_price' to be a float")
        pulumi.set(__self__, "reserved_price", reserved_price)
        if similarity_function and not isinstance(similarity_function, str):
            raise TypeError("Expected argument 'similarity_function' to be a str")
        pulumi.set(__self__, "similarity_function", similarity_function)
        if token and not isinstance(token, str):
            raise TypeError("Expected argument 'token' to be a str")
        pulumi.set(__self__, "token", token)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> int:
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="customerId")
    def customer_id(self) -> str:
        return pulumi.get(self, "customer_id")

    @property
    @pulumi.getter(name="dimensionCount")
    def dimension_count(self) -> int:
        return pulumi.get(self, "dimension_count")

    @property
    @pulumi.getter
    def endpoint(self) -> str:
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter
    def id(self) -> str:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="maxDailyQueries")
    def max_daily_queries(self) -> int:
        return pulumi.get(self, "max_daily_queries")

    @property
    @pulumi.getter(name="maxDailyUpdates")
    def max_daily_updates(self) -> int:
        return pulumi.get(self, "max_daily_updates")

    @property
    @pulumi.getter(name="maxMonthlyBandwidth")
    def max_monthly_bandwidth(self) -> int:
        return pulumi.get(self, "max_monthly_bandwidth")

    @property
    @pulumi.getter(name="maxQueryPerSecond")
    def max_query_per_second(self) -> int:
        return pulumi.get(self, "max_query_per_second")

    @property
    @pulumi.getter(name="maxReadsPerRequest")
    def max_reads_per_request(self) -> int:
        return pulumi.get(self, "max_reads_per_request")

    @property
    @pulumi.getter(name="maxTotalMetadataSize")
    def max_total_metadata_size(self) -> int:
        return pulumi.get(self, "max_total_metadata_size")

    @property
    @pulumi.getter(name="maxVectorCount")
    def max_vector_count(self) -> int:
        return pulumi.get(self, "max_vector_count")

    @property
    @pulumi.getter(name="maxWritesPerRequest")
    def max_writes_per_request(self) -> int:
        return pulumi.get(self, "max_writes_per_request")

    @property
    @pulumi.getter(name="maxWritesPerSecond")
    def max_writes_per_second(self) -> int:
        return pulumi.get(self, "max_writes_per_second")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="readOnlyToken")
    def read_only_token(self) -> str:
        return pulumi.get(self, "read_only_token")

    @property
    @pulumi.getter
    def region(self) -> str:
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="reservedPrice")
    def reserved_price(self) -> float:
        return pulumi.get(self, "reserved_price")

    @property
    @pulumi.getter(name="similarityFunction")
    def similarity_function(self) -> str:
        return pulumi.get(self, "similarity_function")

    @property
    @pulumi.getter
    def token(self) -> str:
        return pulumi.get(self, "token")

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")


class AwaitableGetVectorIndexResult(GetVectorIndexResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVectorIndexResult(
            creation_time=self.creation_time,
            customer_id=self.customer_id,
            dimension_count=self.dimension_count,
            endpoint=self.endpoint,
            id=self.id,
            max_daily_queries=self.max_daily_queries,
            max_daily_updates=self.max_daily_updates,
            max_monthly_bandwidth=self.max_monthly_bandwidth,
            max_query_per_second=self.max_query_per_second,
            max_reads_per_request=self.max_reads_per_request,
            max_total_metadata_size=self.max_total_metadata_size,
            max_vector_count=self.max_vector_count,
            max_writes_per_request=self.max_writes_per_request,
            max_writes_per_second=self.max_writes_per_second,
            name=self.name,
            read_only_token=self.read_only_token,
            region=self.region,
            reserved_price=self.reserved_price,
            similarity_function=self.similarity_function,
            token=self.token,
            type=self.type)


def get_vector_index(id: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVectorIndexResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['id'] = id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
        if opts.plugin_download_url is None:
            opts.plugin_download_url = _utilities.get_plugin_download_url()
    __ret__ = pulumi.runtime.invoke('upstash:index/getVectorIndex:getVectorIndex', __args__, opts=opts, typ=GetVectorIndexResult).value

    return AwaitableGetVectorIndexResult(
        creation_time=__ret__.creation_time,
        customer_id=__ret__.customer_id,
        dimension_count=__ret__.dimension_count,
        endpoint=__ret__.endpoint,
        id=__ret__.id,
        max_daily_queries=__ret__.max_daily_queries,
        max_daily_updates=__ret__.max_daily_updates,
        max_monthly_bandwidth=__ret__.max_monthly_bandwidth,
        max_query_per_second=__ret__.max_query_per_second,
        max_reads_per_request=__ret__.max_reads_per_request,
        max_total_metadata_size=__ret__.max_total_metadata_size,
        max_vector_count=__ret__.max_vector_count,
        max_writes_per_request=__ret__.max_writes_per_request,
        max_writes_per_second=__ret__.max_writes_per_second,
        name=__ret__.name,
        read_only_token=__ret__.read_only_token,
        region=__ret__.region,
        reserved_price=__ret__.reserved_price,
        similarity_function=__ret__.similarity_function,
        token=__ret__.token,
        type=__ret__.type)


@_utilities.lift_output_func(get_vector_index)
def get_vector_index_output(id: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVectorIndexResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...
