# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['QStashTopicArgs', 'QStashTopic']

@pulumi.input_type
class QStashTopicArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a QStashTopic resource.
        :param pulumi.Input[str] name: Name of the Qstash Topic
        """
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Qstash Topic
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _QStashTopicState:
    def __init__(__self__, *,
                 endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[str]]]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 topic_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering QStashTopic resources.
        :param pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[str]]]]] endpoints: Endpoints for the Qstash Topic
        :param pulumi.Input[str] name: Name of the Qstash Topic
        :param pulumi.Input[str] topic_id: Unique Qstash Topic ID for requested topic
        """
        if endpoints is not None:
            pulumi.set(__self__, "endpoints", endpoints)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if topic_id is not None:
            pulumi.set(__self__, "topic_id", topic_id)

    @property
    @pulumi.getter
    def endpoints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[str]]]]]]:
        """
        Endpoints for the Qstash Topic
        """
        return pulumi.get(self, "endpoints")

    @endpoints.setter
    def endpoints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[str]]]]]]):
        pulumi.set(self, "endpoints", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Qstash Topic
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="topicId")
    def topic_id(self) -> Optional[pulumi.Input[str]]:
        """
        Unique Qstash Topic ID for requested topic
        """
        return pulumi.get(self, "topic_id")

    @topic_id.setter
    def topic_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "topic_id", value)


class QStashTopic(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage

        ```python
        import pulumi
        import upstash_pulumi as upstash

        example_qstash_topic = upstash.QStashTopic("exampleQstashTopic")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: Name of the Qstash Topic
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[QStashTopicArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ```python
        import pulumi
        import upstash_pulumi as upstash

        example_qstash_topic = upstash.QStashTopic("exampleQstashTopic")
        ```

        :param str resource_name: The name of the resource.
        :param QStashTopicArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(QStashTopicArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
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
            __props__ = QStashTopicArgs.__new__(QStashTopicArgs)

            __props__.__dict__["name"] = name
            __props__.__dict__["endpoints"] = None
            __props__.__dict__["topic_id"] = None
        super(QStashTopic, __self__).__init__(
            'upstash:index/qStashTopic:QStashTopic',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            endpoints: Optional[pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[str]]]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            topic_id: Optional[pulumi.Input[str]] = None) -> 'QStashTopic':
        """
        Get an existing QStashTopic resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[Mapping[str, pulumi.Input[str]]]]] endpoints: Endpoints for the Qstash Topic
        :param pulumi.Input[str] name: Name of the Qstash Topic
        :param pulumi.Input[str] topic_id: Unique Qstash Topic ID for requested topic
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _QStashTopicState.__new__(_QStashTopicState)

        __props__.__dict__["endpoints"] = endpoints
        __props__.__dict__["name"] = name
        __props__.__dict__["topic_id"] = topic_id
        return QStashTopic(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def endpoints(self) -> pulumi.Output[Sequence[Mapping[str, str]]]:
        """
        Endpoints for the Qstash Topic
        """
        return pulumi.get(self, "endpoints")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the Qstash Topic
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="topicId")
    def topic_id(self) -> pulumi.Output[str]:
        """
        Unique Qstash Topic ID for requested topic
        """
        return pulumi.get(self, "topic_id")

