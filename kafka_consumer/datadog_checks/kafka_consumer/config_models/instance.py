# (C) Datadog, Inc. 2021-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

# This file is autogenerated.
# To change this file you should edit assets/configuration/spec.yaml and then run the following commands:
#     ddev -x validate config -s <INTEGRATION_NAME>
#     ddev -x validate models -s <INTEGRATION_NAME>

from __future__ import annotations

from typing import Any, Mapping, Optional, Sequence, Union

from pydantic import BaseModel, root_validator, validator

from datadog_checks.base.utils.functions import identity
from datadog_checks.base.utils.models import validation

from . import defaults, validators


class MetricPatterns(BaseModel):
    class Config:
        allow_mutation = False

    exclude: Optional[Sequence[str]]
    include: Optional[Sequence[str]]


class SaslOauthTokenProvider(BaseModel):
    class Config:
        allow_mutation = False

    client_id: Optional[str]
    client_secret: Optional[str]
    url: Optional[str]


class InstanceConfig(BaseModel):
    class Config:
        allow_mutation = False

    consumer_groups: Optional[Mapping[str, Any]]
    disable_generic_tags: Optional[bool]
    empty_default_hostname: Optional[bool]
    kafka_client_api_version: Optional[str]
    kafka_connect_str: Union[str, Sequence[str]]
    metric_patterns: Optional[MetricPatterns]
    min_collection_interval: Optional[float]
    monitor_all_broker_highwatermarks: Optional[bool]
    monitor_unlisted_consumer_groups: Optional[bool]
    sasl_kerberos_domain_name: Optional[str]
    sasl_kerberos_keytab: Optional[str]
    sasl_kerberos_principal: Optional[str]
    sasl_kerberos_service_name: Optional[str]
    sasl_mechanism: Optional[str]
    sasl_oauth_token_provider: Optional[SaslOauthTokenProvider]
    sasl_plain_password: Optional[str]
    sasl_plain_username: Optional[str]
    security_protocol: Optional[str]
    service: Optional[str]
    tags: Optional[Sequence[str]]
    tls_ca_cert: Optional[str]
    tls_cert: Optional[str]
    tls_crlfile: Optional[str]
    tls_private_key: Optional[str]
    tls_private_key_password: Optional[str]
    tls_validate_hostname: Optional[bool]
    tls_verify: Optional[bool]

    @root_validator(pre=True)
    def _initial_validation(cls, values):
        return validation.core.initialize_config(getattr(validators, 'initialize_instance', identity)(values))

    @validator('*', pre=True, always=True)
    def _ensure_defaults(cls, v, field):
        if v is not None or field.required:
            return v

        return getattr(defaults, f'instance_{field.name}')(field, v)

    @validator('*')
    def _run_validations(cls, v, field):
        if not v:
            return v

        return getattr(validators, f'instance_{field.name}', identity)(v, field=field)

    @root_validator(pre=False)
    def _final_validation(cls, values):
        return validation.core.finalize_config(getattr(validators, 'finalize_instance', identity)(values))
