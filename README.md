# S4

S4 ("S3 Search") enables quick searches on static websites hosted
on [S3](https://aws.amazon.com/s3/). Users enter their search as part of the URL
path. For example, `search.example.com/code` might redirect to
`example.com/pages/how-to-write-clean-code.html`. The project exists as a Lambda
behind API Gateway. This project was bootstrapped
with [Chalice](https://github.com/aws/chalice).

Try the project at [s.penson.io](http://s.penson.io)! This page will
search [my wiki](http://wiki.penson.io).

## Deployment

First, install requirements.

    cd s4
    virtualenv -p python3 venv
    . venv/bin/activate
    pip install -r requirements.txt

Then, deploy with Chalice.

    chalice deploy.

## Development

View logs with Chalice.

    chalice logs

Run tests with `pytest`.

    python -m pytest

Note that you'll need to install dependencies from `tests/requirements.txt`.

## Custom Domain

Follow the steps below to serve the search from a custom domain name. These
steps assume that you have a domain registered with
[Route53](https://aws.amazon.com/route53/).

1. Navigate to API Gateway from the AWS console.
2. Click *Custom Domain Names* in the sidebar.
3. Select *Create Custom Domain Name* and enter your domain name.
4. Add a *Base Path Mapping* with a destination of `s4:api`.
5. Navigate to Route53 from the AWS console.
6. Click *Hosted zones* and select your domain name.
7. Select *Create Record Set* and enter a subdomain (I chose `s`).
8. Choose `A - IPv4` as the type.
9. Toggle *Yes* under *Alias* and look for the API Gateway API under *Alias
   Target*.
10. Lastly, click *Create*.
