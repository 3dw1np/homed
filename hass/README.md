# homed-hass

Alexa Smart Home skill that proxies requests to a Home Assistant instance, deployed as an AWS Lambda using the Serverless Framework.

## Prerequisites

- [Node.js](https://nodejs.org/) (for Serverless Framework)
- [Python 3.8+](https://www.python.org/)
- [Serverless Framework v3](https://www.serverless.com/)
- AWS account with credentials configured
- Home Assistant instance with a [Long-Lived Access Token](https://developers.home-assistant.io/docs/auth_api/#long-lived-access-token)
- An Alexa Smart Home skill linked to the Lambda (skill ID in `serverless.yml`)

## Setup

1. Install the Serverless plugin (packages Python deps into the Lambda):

```bash
npm install
```

Optionally, if you want to run/test locally:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Create your config file:

```bash
cp config.sample.json config.json
```

Edit `config.json` with your Home Assistant URL and access token.

| Key | Description |
|---|---|
| `url` | Home Assistant API URL (e.g. `https://ha.example.com/api`) |
| `bearer_token` | Long-lived access token from HA |
| `debug` | Enable debug logging (`true`/`false`) |
| `ssl_verify` | Verify SSL certificates (`true`/`false`) |
| `ssl_client` | Client certificate path(s), or `[]` |

3. Set your AWS profile and region:

```bash
export AWS_PROFILE="your-profile"
export AWS_DEFAULT_REGION="eu-west-1"
```

## Deploy

```bash
npx serverless deploy
```

## Remove

```bash
npx serverless remove
```
