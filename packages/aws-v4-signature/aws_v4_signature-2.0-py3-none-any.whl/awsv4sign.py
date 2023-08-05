import datetime
import hashlib
import hmac
import re
import sys


def sign(key, msg) -> hmac:
    return hmac.new(key, msg.encode("utf-8"), hashlib.sha256).digest()


def get_signature_key(key, date_stamp, regionName, serviceName) -> hmac:
    k_date = sign(('AWS4' + key).encode('utf-8'), date_stamp)
    k_region = sign(k_date, regionName)
    k_service = sign(k_region, serviceName)
    k_signing = sign(k_service, 'aws4_request')
    return k_signing


def parse_url(url: str) -> tuple:
    m = re.search("(^https)\:\/\/(.*?)(/.*)", url)
    if m:
        return m.group(2), m.group(3)
    else:
        sys.exit("url isn't qualified url")


def lower_keys(map1: dict) -> dict:
    temp = {}
    for key in map1:
        temp[key.lower()]=map1[key]
    return temp


def generate_http11_header(service: str, region: str, access_key: str, secret_key: str, url: str, httpMethod: str, canonicalHeaders: dict, otherHeaders: dict, queryString: str = '', payload: str = '') -> dict:
    # https://docs.aws.amazon.com/general/latest/gr/reference-for-signature-version-4.html
    # https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html#sig-v4-examples-post

    service = service
    region = region
    t = datetime.datetime.utcnow()
    amzdate = t.strftime('%Y%m%dT%H%M%SZ')
    datestamp = t.strftime('%Y%m%d')  # Date w/o time, used in credential scope

    # ************* TASK 1: CREATE A CANONICAL REQUEST *************
    # http://docs.aws.amazon.com/general/latest/gr/sigv4-create-canonical-request.html

    # Step 1 is to define the verb (GET, POST, etc.)--already done.
    method = httpMethod.upper()

    # Step 2: Create canonical URI--the part of the URI from domain to query
    # string (use '/' if no path)
    host, canonical_uri = parse_url(url)

    # Step 3: Create the canonical query string. In this example (a GET request),
    # request parameters are in the query string. Query string values must
    # be URL-encoded (space=%20). The parameters must be sorted by name.
    # For this example, the query string is pre-formatted in the request_parameters variable.
    canonical_querystring = queryString

    # Step 4: Create the canonical headers and signed headers. Header names
    # must be trimmed and lowercase, and sorted in code point order from
    # low to high. Note that there is a trailing \n.
    mandatory_canonical_headers = {'host': host, 'x-amz-date': amzdate}
    qualified_canonical_headers = lower_keys(canonicalHeaders)
    for key in qualified_canonical_headers:
        mandatory_canonical_headers[key] = qualified_canonical_headers[key]

    canonical_headers = ''
    canonical_headers_keys = list(mandatory_canonical_headers.keys())
    canonical_headers_keys.sort()
    for key in canonical_headers_keys:
        canonical_headers = canonical_headers + f'{key}:' + mandatory_canonical_headers[key] + '\n'

    # Step 5: Create the list of signed headers. This lists the headers
    # in the canonical_headers list, delimited with ";" and in alpha order.
    # Note: The request can include any headers; canonical_headers and
    # signed_headers lists those that you want to be included in the
    # hash of the request. "Host" and "x-amz-date" are always required.
    signed_headers = ';'.join(canonical_headers_keys)

    # Step 6: Create payload hash (hash of the request body content). For GET
    # requests, the payload is an empty string ("").
    payload_hash = hashlib.sha256(payload.encode('utf-8')).hexdigest()

    # Step 7: Combine elements to create canonical request
    canonical_request = method + '\n' + canonical_uri + '\n' + canonical_querystring + '\n' + canonical_headers + '\n' + signed_headers + '\n' + payload_hash

    # ************* TASK 2: CREATE THE STRING TO SIGN*************
    # Match the algorithm to the hashing algorithm you use, either SHA-1 or
    # SHA-256 (recommended)
    algorithm = 'AWS4-HMAC-SHA256'
    credential_scope = datestamp + '/' + region + '/' + service + '/' + 'aws4_request'
    string_to_sign = algorithm + '\n' + amzdate + '\n' + credential_scope + '\n' + hashlib.sha256(canonical_request.encode('utf-8')).hexdigest()

    # ************* TASK 3: CALCULATE THE SIGNATURE *************
    # Create the signing key using the function defined above.
    signing_key = get_signature_key(secret_key, datestamp, region, service)

    # Sign the string_to_sign using the signing_key
    signature = hmac.new(signing_key, string_to_sign.encode('utf-8'), hashlib.sha256).hexdigest()

    # ************* TASK 4: ADD SIGNING INFORMATION TO THE REQUEST *************
    # The signing information can be either in a query string value or in
    # a header named Authorization. This code shows how to use a header.
    # Create authorization header and add to request headers
    authorization_header = algorithm + ' ' + 'Credential=' + access_key + '/' + credential_scope + ', ' + 'SignedHeaders=' + signed_headers + ', ' + 'Signature=' + signature

    # The request can include any headers, but MUST include "host", "x-amz-date",
    # and (for this scenario) "Authorization". "host" and "x-amz-date" must
    # be included in the canonical_headers and signed_headers, as noted
    # earlier. Order here is not significant.
    # Python note: The 'host' header is added automatically by the Python 'requests' library.
    headers = {'x-amz-date': amzdate, 'Authorization': authorization_header}
    
    # ************* TASK 5: ADD extra canonicalHeaders TO THE REQUEST *************
    for key in canonicalHeaders:
        headers[key] = canonicalHeaders[key]

    for key in otherHeaders:
        headers[key] = otherHeaders[key]

    return headers
        