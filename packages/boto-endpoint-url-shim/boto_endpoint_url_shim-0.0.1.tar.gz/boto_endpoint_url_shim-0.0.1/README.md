# Boto Endpoint URL shim

Configure `boto3` and `botocore` endpoint URL via environment variables or
shared configuration file.

This project is motivated by the yet-to-be-merged [`boto3` PR#2746][1], and
follows the [`aws-sdk` proposal #230][2].

## Quick start

To use the main interface described in [proposal #230][2], set up either
service-specific environment variables or `endpoint_url` in a service-specific
sub-section of the shared configuration file and set up the proposed endpoint
URL resolution.

```py
import boto_endpoint_url_shim
import boto3

boto_endpoint_url_shim.proposed_endpoint_url_resolution()

s3 = boto3.resource("s3")  # uses custom endpoint URL
```

## Endpoint URL resolution order

The endpoint URL will be determined by the following steps:

1. `endpoint_url` keyword argument
    ```py
    import boto3
    boto3.resource("s3", endpoint_url="http://localhost:8088")
    ```
1. first function set up by `boto_endpoint_url_shim`
1. second function set up by `boto_endpoint_url_shim`
1. ...
1. fallback to default endpoint determination of `botocore`

The first truthy value provided by one of the steps will be used as endpoint URL
for the clients and resources, otherwise the resolution continues to the next step.

Two convenience functions are exposed by `boto_endpoint_url_shim` to set up
common endpoint URL resolution orders:

* `proposed_endpoint_url_resolution`, the proposed interface of [proposal
  #230][2]
    1. configuration via service-specific environment variable
    1. configuration via service sub-sections of the shared configuration file
* `global_endpoint_url_resolution`, an extension of the proposed interface
    1. configuration via service-specific environment variable
    1. configuration via service sub-sections of the shared configuration file
    1. configuration via global environment variable
    1. configuration via global parameter in shared configuration file

Any other endpoint URL resolution order, can be set up using the
`custom_endpoint_url_resolution` function, with passing the configuration
functions as variadic arguments in the order they should be used.

```py
boto_endpoint_url_shim.custom_endpoint_url_resolution(step1, step2, ..., stepN)
```

## Endpoint URL configuration options

### Proposed interface

The [proposal #230][2] includes two main methods for service-specific endpoint
configuration.

This main interface can be set up using `proposed_endpoint_url_resolution()`.

#### Configuration via service-specific environment variable

Implementation: `read_service_env_var`.

Read the configuration from environment variables
`AWS_<SERVICE_ID>_ENDPOINT_URL` in which `<SERVICE_ID>` is the `ServiceId` of
the of a specific service as defined in its `ServiceModel`, transformed with
spaces replaced with underscores and letters upper-cased.

```sh
AWS_DYNAMODB_ENDPOINT_URL=http://localhost:8024
AWS_ELASTIC_BEANSTALK_ENDPOINT_URL=http://localhost:8053
```

#### Configuration via service sub-sections of the shared configuration file

Implementation: `read_service_config_file`.

Read the configuration from the shared configuration file, as the
`endpoint_url` parameter under the `service_id` sub-section. As above,
`service_id` is a transform for the `ServiceId` with spaces replaced with
underscores and letters lower-cased.

```ini
[profile local-services]
dynamodb =
    endpoint_url = http://localhost:8024
elastic_beanstalk =
    endpoint_url = http://localhost:8053
```

### Alternative interfaces

Several more interfaces are included in the [proposal #230][1], they have been
implemented as functions in this package.

As a convenience, the proposed interface above followed by the global
environment variable and global configuration file methods can be set up using
`global_endpoint_url_resolution`.

#### Configuration via mapping in global environment variable

Implementation: `read_mapping_env_var`.

Read the configuration from the global environment variable `AWS_ENDPOINT_URL`,
containing a mapping of lower-case `service_id`s to endpoint URLs.

```sh
AWS_ENDPOINT_URL="dynamodb=http://localhost:8024,elastic_beanstalk=http://localhost:8053"
```

**NB.** The mapping is loaded once on the first use of the function and cached
for later uses.

#### Configuration via global environment variable

Implementation: `read_global_env_var`.

Read the configuration from the global environment variable `AWS_ENDPOINT_URL`
and use this endpoint URL for all services.

```sh
AWS_ENDPOINT_URL=http://localhost:8099
```

#### Configuration via global parameter in shared configuration file

Implementation: `read_global_config_file`.

Read the configuration from the `endpoint_url` parameter at the top level of a
profile and use this endpoint URL for all services.

```ini
[profile local-services]
endpoint_url = http://localhost:8099
```

#### Configuration via named top level parameters in shared configuration file

Implementation: `read_named_top_level_config_file`.

Read the configuration from the `<service_id>_endpoint_url` parameter at the top
level of a profile, with `<service_id>` the lower-case `service_id`.

```ini
[profile local-services]
dynamodb_endpoint_url = http://localhost:8024
elastic_beanstalk_endpoint_url = http://localhost:8053
```

### Custom interface

Users are free to define and use functions to obtain the endpoint URL of a
service.

The custom functions must adhere to the following signature:

```py
def func(session: botocore.session.Session, service_id: str) -> str | None: ...
```

with:
* `session` a `botocore.session.Session`
* `service_id` the `ServiceId` of a specific service as defined in its
  `ServiceModel`, transformed with spaces replaced with underscores and letters
  lower-cased
* `returns` a `str | None` either the endpoint URL or None to continue to the
  next step in the resolution chain

[1]: https://github.com/boto/boto3/pull/2746
[2]: https://github.com/aws/aws-sdk/pull/230
