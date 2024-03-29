# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetKafkaConnectorResult',
    'AwaitableGetKafkaConnectorResult',
    'get_kafka_connector',
    'get_kafka_connector_output',
]

@pulumi.output_type
class GetKafkaConnectorResult:
    """
    A collection of values returned by getKafkaConnector.
    """
    def __init__(__self__, cluster_id=None, connector_class=None, connector_id=None, connector_state=None, creation_time=None, encoded_username=None, id=None, name=None, properties=None, properties_encrypted=None, state=None, state_error_message=None, tasks=None, topics=None, ttl=None, user_password=None):
        if cluster_id and not isinstance(cluster_id, str):
            raise TypeError("Expected argument 'cluster_id' to be a str")
        pulumi.set(__self__, "cluster_id", cluster_id)
        if connector_class and not isinstance(connector_class, str):
            raise TypeError("Expected argument 'connector_class' to be a str")
        pulumi.set(__self__, "connector_class", connector_class)
        if connector_id and not isinstance(connector_id, str):
            raise TypeError("Expected argument 'connector_id' to be a str")
        pulumi.set(__self__, "connector_id", connector_id)
        if connector_state and not isinstance(connector_state, str):
            raise TypeError("Expected argument 'connector_state' to be a str")
        pulumi.set(__self__, "connector_state", connector_state)
        if creation_time and not isinstance(creation_time, int):
            raise TypeError("Expected argument 'creation_time' to be a int")
        pulumi.set(__self__, "creation_time", creation_time)
        if encoded_username and not isinstance(encoded_username, str):
            raise TypeError("Expected argument 'encoded_username' to be a str")
        pulumi.set(__self__, "encoded_username", encoded_username)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
        if properties_encrypted and not isinstance(properties_encrypted, str):
            raise TypeError("Expected argument 'properties_encrypted' to be a str")
        pulumi.set(__self__, "properties_encrypted", properties_encrypted)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if state_error_message and not isinstance(state_error_message, str):
            raise TypeError("Expected argument 'state_error_message' to be a str")
        pulumi.set(__self__, "state_error_message", state_error_message)
        if tasks and not isinstance(tasks, list):
            raise TypeError("Expected argument 'tasks' to be a list")
        pulumi.set(__self__, "tasks", tasks)
        if topics and not isinstance(topics, list):
            raise TypeError("Expected argument 'topics' to be a list")
        pulumi.set(__self__, "topics", topics)
        if ttl and not isinstance(ttl, int):
            raise TypeError("Expected argument 'ttl' to be a int")
        pulumi.set(__self__, "ttl", ttl)
        if user_password and not isinstance(user_password, str):
            raise TypeError("Expected argument 'user_password' to be a str")
        pulumi.set(__self__, "user_password", user_password)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> str:
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="connectorClass")
    def connector_class(self) -> str:
        return pulumi.get(self, "connector_class")

    @property
    @pulumi.getter(name="connectorId")
    def connector_id(self) -> str:
        return pulumi.get(self, "connector_id")

    @property
    @pulumi.getter(name="connectorState")
    def connector_state(self) -> str:
        return pulumi.get(self, "connector_state")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> int:
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="encodedUsername")
    def encoded_username(self) -> str:
        return pulumi.get(self, "encoded_username")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> Mapping[str, Any]:
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter(name="propertiesEncrypted")
    def properties_encrypted(self) -> str:
        return pulumi.get(self, "properties_encrypted")

    @property
    @pulumi.getter
    def state(self) -> str:
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="stateErrorMessage")
    def state_error_message(self) -> str:
        return pulumi.get(self, "state_error_message")

    @property
    @pulumi.getter
    def tasks(self) -> Sequence[Mapping[str, Any]]:
        return pulumi.get(self, "tasks")

    @property
    @pulumi.getter
    def topics(self) -> Sequence[str]:
        return pulumi.get(self, "topics")

    @property
    @pulumi.getter
    def ttl(self) -> int:
        return pulumi.get(self, "ttl")

    @property
    @pulumi.getter(name="userPassword")
    def user_password(self) -> str:
        return pulumi.get(self, "user_password")


class AwaitableGetKafkaConnectorResult(GetKafkaConnectorResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetKafkaConnectorResult(
            cluster_id=self.cluster_id,
            connector_class=self.connector_class,
            connector_id=self.connector_id,
            connector_state=self.connector_state,
            creation_time=self.creation_time,
            encoded_username=self.encoded_username,
            id=self.id,
            name=self.name,
            properties=self.properties,
            properties_encrypted=self.properties_encrypted,
            state=self.state,
            state_error_message=self.state_error_message,
            tasks=self.tasks,
            topics=self.topics,
            ttl=self.ttl,
            user_password=self.user_password)


def get_kafka_connector(connector_id: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetKafkaConnectorResult:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_upstash as upstash

    kafka_connector_data = upstash.get_kafka_connector(topic_id=resource["upstash_kafka_connector"]["exampleKafkaConnector"]["connector_id"])
    ```
    """
    __args__ = dict()
    __args__['connectorId'] = connector_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
        if opts.plugin_download_url is None:
            opts.plugin_download_url = _utilities.get_plugin_download_url()
    __ret__ = pulumi.runtime.invoke('upstash:index/getKafkaConnector:getKafkaConnector', __args__, opts=opts, typ=GetKafkaConnectorResult).value

    return AwaitableGetKafkaConnectorResult(
        cluster_id=__ret__.cluster_id,
        connector_class=__ret__.connector_class,
        connector_id=__ret__.connector_id,
        connector_state=__ret__.connector_state,
        creation_time=__ret__.creation_time,
        encoded_username=__ret__.encoded_username,
        id=__ret__.id,
        name=__ret__.name,
        properties=__ret__.properties,
        properties_encrypted=__ret__.properties_encrypted,
        state=__ret__.state,
        state_error_message=__ret__.state_error_message,
        tasks=__ret__.tasks,
        topics=__ret__.topics,
        ttl=__ret__.ttl,
        user_password=__ret__.user_password)


@_utilities.lift_output_func(get_kafka_connector)
def get_kafka_connector_output(connector_id: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetKafkaConnectorResult]:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_upstash as upstash

    kafka_connector_data = upstash.get_kafka_connector(topic_id=resource["upstash_kafka_connector"]["exampleKafkaConnector"]["connector_id"])
    ```
    """
    ...
