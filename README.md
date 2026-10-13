# clinikehr

Official Python client for the [ClinikEHR API](https://docs.clinikehr.com) —
a server-to-server REST API over a clinic's own inventory, appointments,
CRM and patient data, reached with an API key.

Base URL: `https://api.clinikehr.com/v1`

## What's generated, what's hand-written

- **Generated, never hand-edited:** `src/clinikehr/_generated/` — a typed
  [`httpx`](https://www.python-httpx.org/) + [`attrs`](https://www.attrs.org/)
  client for every operation and schema in the ClinikEHR API description,
  produced by
  [`openapi-python-client`](https://github.com/openapi-generators/openapi-python-client).
- **Hand-written, small, and tested** (`src/clinikehr/*.py`, `tests/`):
  authentication, automatic `Idempotency-Key` generation and reuse across
  retries, the retry policy, cursor pagination, typed errors, the FHIR
  `Accept` opt-in and the webhook signature verifier.

**Keep your live key on the server.** A live key (`ehr_live_…`) must never
ship in code that runs on an end user's device. Python has no browser guard
the way the TypeScript SDK does, so that discipline is yours.

## Install

```bash
pip install clinikehr
```

Requires Python 3.11 or later.

## Quickstart

```python
import os

import clinikehr
from clinikehr._generated.api.me import get_me
from clinikehr._generated.api.inventory import list_inventory_items

client = clinikehr.create_client(os.environ["CLINIKEHR_API_KEY"])  # ehr_test_… for the sandbox

me = clinikehr.raise_for_response(get_me.sync_detailed(client=client))
print(me)

items = clinikehr.raise_for_response(
    list_inventory_items.sync_detailed(client=client, clinic_id="YOUR_CLINIC_ID", limit=25)
)
print(items)
```

### Async

```python
async_response = await list_inventory_items.asyncio_detailed(client=client, clinic_id="YOUR_CLINIC_ID")
items = clinikehr.raise_for_response(async_response)
```

## Error handling

`raise_for_response()` raises `ClinikEHRApiError` — built from the API's
`application/problem+json` body — for any non-2xx response:

```python
from clinikehr import ClinikEHRApiError

try:
    clinikehr.raise_for_response(get_patient.sync_detailed(client=client, clinic_id=clinic_id, patient_id=patient_id))
except ClinikEHRApiError as err:
    print(err.status, err.code, err.request_id, err.detail)
    if err.code == "rate_limited":
        ...  # err.retry_after_seconds is set from the Retry-After header
```

A network-level failure (no response at all) raises `httpx`'s own exception
(`httpx.ConnectError`, `httpx.TimeoutException`, …) after this SDK's own
retry policy has exhausted its attempts — the retry rule is identical to the
TypeScript SDK's: a 429 always retries (honouring `Retry-After`); a 5xx or a
transport failure retries only for a GET/HEAD, or a request that carried an
`Idempotency-Key` (every POST and PATCH gets one automatically when you set
none, generated once and reused across retries — never regenerated; several
PATCH routes require one). PATCH is still never auto-retried on a 5xx: a
stale `If-Match` on a retry is a different, correct `412`.

## Pagination

```python
from clinikehr import CursorPage, paginate

def fetch_page(cursor):
    resp = clinikehr.raise_for_response(
        list_inventory_items.sync_detailed(client=client, clinic_id=clinic_id, starting_after=cursor)
    )
    return CursorPage(data=resp.data, has_more=resp.has_more, next_cursor=resp.next_cursor)

for item in paginate(fetch_page):
    print(item)
```

## FHIR

```python
client = clinikehr.create_client(api_key, fhir=True)  # every call now sends Accept: application/fhir+json
```

## Verifying a webhook notification

```python
from clinikehr import verify_webhook, WebhookVerificationError

try:
    verify_webhook(
        {"webhook-id": request.headers["webhook-id"], "webhook-timestamp": request.headers["webhook-timestamp"], "webhook-signature": request.headers["webhook-signature"]},
        raw_body,  # the RAW request body, before json.loads
        secrets=[os.environ["CLINIKEHR_WEBHOOK_SECRET"]],  # pass BOTH secrets during a rotation's overlap window
    )
except WebhookVerificationError:
    ...  # reject the delivery
```

## Development

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

## License

MIT, Copyright (c) 2026-present Bettar Platforms, Inc. See `LICENSE`.

© Bettar Platforms, Inc. ClinikEHR is a product of Bettar Platforms, Inc.

## How this repository works

This code is generated from ClinikEHR's API description and published from a
private source. Issues are welcome here. Pull requests cannot be merged
directly, because every change is made in the private source and mirrored
here: describe the change you need in an issue and we will make it there.

Questions about the API itself belong at [docs.clinikehr.com](https://docs.clinikehr.com);
to report a vulnerability, see [SECURITY.md](SECURITY.md).
