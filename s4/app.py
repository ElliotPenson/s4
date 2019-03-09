import os

import boto3
from chalice import Chalice, Response
from fuzzywuzzy import fuzz

app = Chalice(app_name="s4")


@app.route("/")
def index():
    """Provide s4 usage information."""
    domain_name = app.current_request.context.get("domainName", "example.com")
    return f"Enter a search in the URL path. For example, {domain_name}/text"


@app.route("/{query}")
def search(query):
    """Perform a fuzzy search of HTML files in an S3 bucket."""
    bucket = os.environ["BUCKET"]
    best_key = match(query, get_html_keys(bucket))
    url = os.path.join("http://", bucket, best_key)
    return redirect(url)


def redirect(url):
    return Response(body=None, status_code=301, headers={"Location": url})


def match(query, collection):
    """Find the string in the collection most similar to the given query."""
    return max(collection, key=lambda item: fuzz.token_set_ratio(query, item))


def get_html_keys(bucket_name):
    """Return a list of HTML filenames found in the given bucket."""
    s3 = boto3.resource("s3")
    bucket = s3.Bucket(bucket_name)
    return [s3_object.key for s3_object in bucket.objects.all()
            if is_html(s3_object.key)]


def is_html(filename):
    return filename.lower().endswith(".html")
