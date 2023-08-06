import os
import json
import urllib.request


def get_token(url_path):
    url = "https://auth.obp.dev.outerbounds.xyz" + url_path
    headers = json.loads(os.environ['METADATA_SERVICE_HEADERS'])
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as f:
        token_info = json.load(f)
        return token_info


def main():
    token_info = get_token("/generate/aws")

    token_file = "/tmp/obp_token"
    with open(token_file, "w") as f:
        f.write(token_info["token"])

    print("export AWS_WEB_IDENTITY_TOKEN_FILE=" + token_file)
    print("export AWS_ROLE_ARN=" + token_info["role_arn"])

if __name__ == '__main__':
    main()