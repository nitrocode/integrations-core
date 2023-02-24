# (C) Datadog, Inc. 2023-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

from datadog_checks.kafka_consumer.client.confluent_kafka_client import ConfluentKafkaClient
from datadog_checks.kafka_consumer.client.kafka_client import KafkaClient


def make_client(config, tls_context, log) -> KafkaClient:
    # return KafkaPythonClient(config, tls_context, log)
    return ConfluentKafkaClient(config, tls_context, log)
