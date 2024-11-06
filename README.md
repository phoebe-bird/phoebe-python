# Phoebe Python API library

[![PyPI version](https://img.shields.io/pypi/v/phoebe_bird.svg)](https://pypi.org/project/phoebe_bird/)

The Phoebe Python library provides convenient access to the Phoebe REST API from any Python 3.8+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by [httpx](https://github.com/encode/httpx).

It is generated with [Stainless](https://www.stainlessapi.com/).

## Documentation

The REST API documentation can be found on [science.ebird.org](https://science.ebird.org/en/use-ebird-data/download-ebird-data-products). The full API of this library can be found in [api.md](api.md).

## Installation

```sh
# install from PyPI
pip install --pre phoebe_bird
```

## Usage

The full API of this library can be found in [api.md](api.md).

```python
import os
from phoebe_bird import Phoebe

client = Phoebe(
    # This is the default and can be omitted
    api_key=os.environ.get("EBIRD_API_KEY"),
)

info = client.ref.hotspot.info.retrieve(
    "L99381",
)
print(info.country_code)
```

While you can provide an `api_key` keyword argument,
we recommend using [python-dotenv](https://pypi.org/project/python-dotenv/)
to add `EBIRD_API_KEY="My API Key"` to your `.env` file
so that your API Key is not stored in source control.

## Async usage

Simply import `AsyncPhoebe` instead of `Phoebe` and use `await` with each API call:

```python
import os
import asyncio
from phoebe_bird import AsyncPhoebe

client = AsyncPhoebe(
    # This is the default and can be omitted
    api_key=os.environ.get("EBIRD_API_KEY"),
)


async def main() -> None:
    info = await client.ref.hotspot.info.retrieve(
        "L99381",
    )
    print(info.country_code)


asyncio.run(main())
```

Functionality between the synchronous and asynchronous clients is otherwise identical.

## Using types

Nested request parameters are [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict). Responses are [Pydantic models](https://docs.pydantic.dev) which also provide helper methods for things like:

- Serializing back into JSON, `model.to_json()`
- Converting to a dictionary, `model.to_dict()`

Typed requests and responses provide autocomplete and documentation within your editor. If you would like to see type errors in VS Code to help catch bugs earlier, set `python.analysis.typeCheckingMode` to `basic`.

## Handling errors

When the library is unable to connect to the API (for example, due to network connection problems or a timeout), a subclass of `phoebe_bird.APIConnectionError` is raised.

When the API returns a non-success status code (that is, 4xx or 5xx
response), a subclass of `phoebe_bird.APIStatusError` is raised, containing `status_code` and `response` properties.

All errors inherit from `phoebe_bird.APIError`.

```python
import phoebe_bird
from phoebe_bird import Phoebe

client = Phoebe()

try:
    client.ref.hotspot.info.retrieve(
        "L99381",
    )
except phoebe_bird.APIConnectionError as e:
    print("The server could not be reached")
    print(e.__cause__)  # an underlying Exception, likely raised within httpx.
except phoebe_bird.RateLimitError as e:
    print("A 429 status code was received; we should back off a bit.")
except phoebe_bird.APIStatusError as e:
    print("Another non-200-range status code was received")
    print(e.status_code)
    print(e.response)
```

Error codes are as followed:

| Status Code | Error Type                 |
| ----------- | -------------------------- |
| 400         | `BadRequestError`          |
| 401         | `AuthenticationError`      |
| 403         | `PermissionDeniedError`    |
| 404         | `NotFoundError`            |
| 422         | `UnprocessableEntityError` |
| 429         | `RateLimitError`           |
| >=500       | `InternalServerError`      |
| N/A         | `APIConnectionError`       |

### Retries

Certain errors are automatically retried 2 times by default, with a short exponential backoff.
Connection errors (for example, due to a network connectivity problem), 408 Request Timeout, 409 Conflict,
429 Rate Limit, and >=500 Internal errors are all retried by default.

You can use the `max_retries` option to configure or disable retry settings:

```python
from phoebe_bird import Phoebe

# Configure the default for all requests:
client = Phoebe(
    # default is 2
    max_retries=0,
)

# Or, configure per-request:
client.with_options(max_retries=5).ref.hotspot.info.retrieve(
    "L99381",
)
```

### Timeouts

By default requests time out after 1 minute. You can configure this with a `timeout` option,
which accepts a float or an [`httpx.Timeout`](https://www.python-httpx.org/advanced/#fine-tuning-the-configuration) object:

```python
from phoebe_bird import Phoebe

# Configure the default for all requests:
client = Phoebe(
    # 20 seconds (default is 1 minute)
    timeout=20.0,
)

# More granular control:
client = Phoebe(
    timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0),
)

# Override per-request:
client.with_options(timeout=5.0).ref.hotspot.info.retrieve(
    "L99381",
)
```

On timeout, an `APITimeoutError` is thrown.

Note that requests that time out are [retried twice by default](#retries).

## Advanced

### Logging

We use the standard library [`logging`](https://docs.python.org/3/library/logging.html) module.

You can enable logging by setting the environment variable `PHOEBE_LOG` to `debug`.

```shell
$ export PHOEBE_LOG=debug
```

### How to tell whether `None` means `null` or missing

In an API response, a field may be explicitly `null`, or missing entirely; in either case, its value is `None` in this library. You can differentiate the two cases with `.model_fields_set`:

```py
if response.my_field is None:
  if 'my_field' not in response.model_fields_set:
    print('Got json like {}, without a "my_field" key present at all.')
  else:
    print('Got json like {"my_field": null}.')
```

### Accessing raw response data (e.g. headers)

The "raw" Response object can be accessed by prefixing `.with_raw_response.` to any HTTP method call, e.g.,

```py
from phoebe_bird import Phoebe

client = Phoebe()
response = client.ref.hotspot.info.with_raw_response.retrieve(
    "L99381",
)
print(response.headers.get('X-My-Header'))

info = response.parse()  # get the object that `ref.hotspot.info.retrieve()` would have returned
print(info.country_code)
```

These methods return an [`APIResponse`](https://github.com/phoebe-bird/phoebe-python/tree/main/src/phoebe_bird/_response.py) object.

The async client returns an [`AsyncAPIResponse`](https://github.com/phoebe-bird/phoebe-python/tree/main/src/phoebe_bird/_response.py) with the same structure, the only difference being `await`able methods for reading the response content.

#### `.with_streaming_response`

The above interface eagerly reads the full response body when you make the request, which may not always be what you want.

To stream the response body, use `.with_streaming_response` instead, which requires a context manager and only reads the response body once you call `.read()`, `.text()`, `.json()`, `.iter_bytes()`, `.iter_text()`, `.iter_lines()` or `.parse()`. In the async client, these are async methods.

```python
with client.ref.hotspot.info.with_streaming_response.retrieve(
    "L99381",
) as response:
    print(response.headers.get("X-My-Header"))

    for line in response.iter_lines():
        print(line)
```

The context manager is required so that the response will reliably be closed.

### Making custom/undocumented requests

This library is typed for convenient access to the documented API.

If you need to access undocumented endpoints, params, or response properties, the library can still be used.

#### Undocumented endpoints

To make requests to undocumented endpoints, you can make requests using `client.get`, `client.post`, and other
http verbs. Options on the client will be respected (such as retries) will be respected when making this
request.

```py
import httpx

response = client.post(
    "/foo",
    cast_to=httpx.Response,
    body={"my_param": True},
)

print(response.headers.get("x-foo"))
```

#### Undocumented request params

If you want to explicitly send an extra param, you can do so with the `extra_query`, `extra_body`, and `extra_headers` request
options.

#### Undocumented response properties

To access undocumented response properties, you can access the extra fields like `response.unknown_prop`. You
can also get all the extra fields on the Pydantic model as a dict with
[`response.model_extra`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_extra).

### Configuring the HTTP client

You can directly override the [httpx client](https://www.python-httpx.org/api/#client) to customize it for your use case, including:

- Support for proxies
- Custom transports
- Additional [advanced](https://www.python-httpx.org/advanced/clients/) functionality

```python
from phoebe_bird import Phoebe, DefaultHttpxClient

client = Phoebe(
    # Or use the `PHOEBE_BASE_URL` env var
    base_url="http://my.test.server.example.com:8083",
    http_client=DefaultHttpxClient(
        proxies="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

You can also customize the client on a per-request basis by using `with_options()`:

```python
client.with_options(http_client=DefaultHttpxClient(...))
```

### Managing HTTP resources

By default the library closes underlying HTTP connections whenever the client is [garbage collected](https://docs.python.org/3/reference/datamodel.html#object.__del__). You can manually close the client using the `.close()` method if desired, or with a context manager that closes when exiting.

## Versioning

This package generally follows [SemVer](https://semver.org/spec/v2.0.0.html) conventions, though certain backwards-incompatible changes may be released as minor versions:

1. Changes that only affect static types, without breaking runtime behavior.
2. Changes to library internals which are technically public but not intended or documented for external use. _(Please open a GitHub issue to let us know if you are relying on such internals)_.
3. Changes that we do not expect to impact the vast majority of users in practice.

We take backwards-compatibility seriously and work hard to ensure you can rely on a smooth upgrade experience.

We are keen for your feedback; please open an [issue](https://www.github.com/phoebe-bird/phoebe-python/issues) with questions, bugs, or suggestions.

### Determining the installed version

If you've upgraded to the latest version but aren't seeing any new features you were expecting then your python environment is likely still using an older version.

You can determine the version that is being used at runtime with:

```py
import phoebe_bird
print(phoebe_bird.__version__)
```

## Requirements

Python 3.8 or higher.

## Contributing

See [the contributing documentation](./CONTRIBUTING.md).