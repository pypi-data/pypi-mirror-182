import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "halloumi-ami-pipelines",
    "version": "0.0.34",
    "description": "halloumi-ami-pipelines",
    "license": "Apache-2.0",
    "url": "https://github.com/sentiampc/halloumi-ami-pipelines.git",
    "long_description_content_type": "text/markdown",
    "author": "Sentia<support.mpc@sentia.com>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/sentiampc/halloumi-ami-pipelines.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "ami_pipelines",
        "ami_pipelines._jsii"
    ],
    "package_data": {
        "ami_pipelines._jsii": [
            "halloumi-ami-pipelines@0.0.34.jsii.tgz"
        ],
        "ami_pipelines": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.7",
    "install_requires": [
        "aws-cdk.aws-codebuild==1.180.0",
        "aws-cdk.aws-codecommit==1.180.0",
        "aws-cdk.aws-codepipeline-actions==1.180.0",
        "aws-cdk.aws-codepipeline==1.180.0",
        "aws-cdk.aws-ec2==1.180.0",
        "aws-cdk.aws-events-targets==1.180.0",
        "aws-cdk.aws-events==1.180.0",
        "aws-cdk.aws-iam==1.180.0",
        "aws-cdk.aws-imagebuilder==1.180.0",
        "aws-cdk.aws-kms==1.180.0",
        "aws-cdk.aws-lambda==1.180.0",
        "aws-cdk.aws-logs-destinations==1.180.0",
        "aws-cdk.aws-logs==1.180.0",
        "aws-cdk.aws-s3==1.180.0",
        "aws-cdk.aws-sns-subscriptions==1.180.0",
        "aws-cdk.aws-sns==1.180.0",
        "aws-cdk.core==1.180.0",
        "aws-cdk.custom-resources==1.180.0",
        "constructs>=3.2.27, <4.0.0",
        "jsii>=1.72.0, <2.0.0",
        "publication>=0.0.3",
        "typeguard~=2.13.3"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Typing :: Typed",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
