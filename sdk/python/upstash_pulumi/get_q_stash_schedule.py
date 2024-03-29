# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetQStashScheduleResult',
    'AwaitableGetQStashScheduleResult',
    'get_q_stash_schedule',
    'get_q_stash_schedule_output',
]

@pulumi.output_type
class GetQStashScheduleResult:
    """
    A collection of values returned by getQStashSchedule.
    """
    def __init__(__self__, body=None, created_at=None, cron=None, destination=None, forward_headers=None, id=None, not_before=None, retries=None, schedule_id=None):
        if body and not isinstance(body, str):
            raise TypeError("Expected argument 'body' to be a str")
        pulumi.set(__self__, "body", body)
        if created_at and not isinstance(created_at, int):
            raise TypeError("Expected argument 'created_at' to be a int")
        pulumi.set(__self__, "created_at", created_at)
        if cron and not isinstance(cron, str):
            raise TypeError("Expected argument 'cron' to be a str")
        pulumi.set(__self__, "cron", cron)
        if destination and not isinstance(destination, str):
            raise TypeError("Expected argument 'destination' to be a str")
        pulumi.set(__self__, "destination", destination)
        if forward_headers and not isinstance(forward_headers, dict):
            raise TypeError("Expected argument 'forward_headers' to be a dict")
        pulumi.set(__self__, "forward_headers", forward_headers)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if not_before and not isinstance(not_before, int):
            raise TypeError("Expected argument 'not_before' to be a int")
        pulumi.set(__self__, "not_before", not_before)
        if retries and not isinstance(retries, int):
            raise TypeError("Expected argument 'retries' to be a int")
        pulumi.set(__self__, "retries", retries)
        if schedule_id and not isinstance(schedule_id, str):
            raise TypeError("Expected argument 'schedule_id' to be a str")
        pulumi.set(__self__, "schedule_id", schedule_id)

    @property
    @pulumi.getter
    def body(self) -> str:
        return pulumi.get(self, "body")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> int:
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def cron(self) -> str:
        return pulumi.get(self, "cron")

    @property
    @pulumi.getter
    def destination(self) -> str:
        return pulumi.get(self, "destination")

    @property
    @pulumi.getter(name="forwardHeaders")
    def forward_headers(self) -> Mapping[str, str]:
        return pulumi.get(self, "forward_headers")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="notBefore")
    def not_before(self) -> int:
        return pulumi.get(self, "not_before")

    @property
    @pulumi.getter
    def retries(self) -> int:
        return pulumi.get(self, "retries")

    @property
    @pulumi.getter(name="scheduleId")
    def schedule_id(self) -> str:
        return pulumi.get(self, "schedule_id")


class AwaitableGetQStashScheduleResult(GetQStashScheduleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetQStashScheduleResult(
            body=self.body,
            created_at=self.created_at,
            cron=self.cron,
            destination=self.destination,
            forward_headers=self.forward_headers,
            id=self.id,
            not_before=self.not_before,
            retries=self.retries,
            schedule_id=self.schedule_id)


def get_q_stash_schedule(schedule_id: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetQStashScheduleResult:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_upstash as upstash

    example_qstash_schedule_data = upstash.get_q_stash_schedule(schedule_id=resource["upstash_qstash_schedule"]["exampleQstashSchedule"]["schedule_id"])
    ```
    """
    __args__ = dict()
    __args__['scheduleId'] = schedule_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
        if opts.plugin_download_url is None:
            opts.plugin_download_url = _utilities.get_plugin_download_url()
    __ret__ = pulumi.runtime.invoke('upstash:index/getQStashSchedule:getQStashSchedule', __args__, opts=opts, typ=GetQStashScheduleResult).value

    return AwaitableGetQStashScheduleResult(
        body=__ret__.body,
        created_at=__ret__.created_at,
        cron=__ret__.cron,
        destination=__ret__.destination,
        forward_headers=__ret__.forward_headers,
        id=__ret__.id,
        not_before=__ret__.not_before,
        retries=__ret__.retries,
        schedule_id=__ret__.schedule_id)


@_utilities.lift_output_func(get_q_stash_schedule)
def get_q_stash_schedule_output(schedule_id: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetQStashScheduleResult]:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_upstash as upstash

    example_qstash_schedule_data = upstash.get_q_stash_schedule(schedule_id=resource["upstash_qstash_schedule"]["exampleQstashSchedule"]["schedule_id"])
    ```
    """
    ...
