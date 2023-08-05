'''
# cdk-s3-upload-presignedurl-api

![npmjs](https://img.shields.io/npm/v/cdk-s3-upload-presignedurl-api?color=red) ![PyPI](https://img.shields.io/pypi/v/cdk-s3-upload-presignedurl-api?color=yellow) ![Maven Central](https://img.shields.io/maven-central/v/io.github.jeromevdl.awscdk/s3-upload-presignedurl-api?color=blue)

cdk-s3-upload-presignedurl-api is AWS CDK construct library that create an API to get a presigned url to upload a file in S3.

## Background

In web and mobile applications, it's common to provide the ability to upload data (documents, images, ...). Uploading files on a web server can be challenging and AWS recommends to upload files directly to S3. To do that securely, you can use [pre-signed URLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/PresignedUrlUploadObject.html). This [blog post](https://aws.amazon.com/blogs/compute/uploading-to-amazon-s3-directly-from-a-web-or-mobile-application/) provides some more details.

## Architecture

![Architecture](images/architecture.png)

1. The client makes a call to the API, specifying the "contentType" of the file to upload in request parameters (eg. `?contentType=image/png` in the URL)
2. API Gateway handles the request and execute the Lambda function.
3. The Lambda function makes a call to the [`getSignedUrl`](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/S3.html) api for a `putObject` operation.
4. The Lambda function returns the generated URL and the key of the object in S3 to API Gateway.
5. The API returns the generated URL and the key of the object in S3 to the client.
6. The client can now use this URL to upload a file, directly to S3.

## Getting Started

### TypeScript

#### Installation

```sh
$ npm install --save cdk-s3-upload-presignedurl-api
```

#### Usage

```python
import * as cdk from '@aws-cdk/core';
import { S3UploadPresignedUrlApi } from 'cdk-s3-upload-presignedurl-api';

const app = new cdk.App();
const stack = new cdk.Stack(app, '<your-stack-name>');

new S3UploadPresignedUrlApi(stack, 'S3UploadSignedUrl');
```

### Python

#### Installation

```sh
$ pip install cdk-s3-upload-presignedurl-api
```

#### Usage

```py
import aws_cdk.core as cdk
from cdk_s3_upload_presignedurl_api import S3UploadPresignedUrlApi

app = cdk.App()
stack = cdk.Stack(app, "<your-stack-name>")

S3UploadPresignedUrlApi(stack, 'S3UploadSignedUrl')
```

### Java

#### Maven configuration

```xml
<dependency>
    <groupId>io.github.jeromevdl.awscdk</groupId>
    <artifactId>s3-upload-presignedurl-api</artifactId>
    <version>...</version>
</dependency>
```

#### Usage

```java
import software.amazon.awscdk.App;
import software.amazon.awscdk.Stack;
import io.github.jeromevdl.awscdk.s3uploadpresignedurlapi.S3UploadPresignedUrlApi;

App app = new App();
Stack stack = new Stack(app, "<your-stack-name>");

new S3UploadPresignedUrlApi(stack, "S3UploadSignedUrl");
```

## Configuration

By default and without any property, the `S3UploadPresignedUrlApi` construct will create:

* The S3 Bucket, with the appropriate CORS configuration
* The Lambda function, that will genereate the pre-signed URL
* The REST API, that will expose the Lambda function to the client
* The Cognito User Pool and User Pool Client to secure the API

You can shoose to let the construct do everything or you can reuse existing resources:

* An S3 Bucket (`existingBucketObj`). Be carefull to configure CORS properly ([doc](https://docs.aws.amazon.com/AmazonS3/latest/userguide/cors.html))
* A Cognito User Pool (`existingUserPoolObj`).

You can also customize the construct:

* You can define the properties for the REST API (`apiGatewayProps`). Note that you cannot reuse an existing API.
* You can configure the allowed origins (`allowedOrigins`) when configuring CORS. Default is *.
* You can configure the expiration of the generated URLs, in seconds (`expiration`).
* You can choose to let the API open, and remove Cognito, by setting `secured` to false.
* You can choose the log retention period (`logRetention`) for Lambda and API Gateway.

See [API reference](https://github.com/jeromevdl/cdk-s3-upload-presignedurl-api/blob/main/API.md#is3uploadsignedurlapiprops-) for the details.

## Client-side usage

***Hint***: A complete example (ReactJS / Amplify) if provided in the GitHub repository ([frontend](https://github.com/jeromevdl/cdk-s3-upload-presignedurl-api/tree/main/frontend) folder).

Once the components are deployed, you will need to query the API from the client. In order to do so, you need to retrieve the outputs of the CloudFormation Stack:

* The API Endpoint (eg. `https://12345abcd.execute-api.eu-west-1.amazonaws.com/prod/`)
* The User Pool Id (eg. `eu-west-1_2b4C6E8g`)
* The User Pool Client Id (eg. `g5465n67cvfc7n6jn54768`)

### Create a user in Cognito User Pool

If you let the Construct configuration by default (`secured = true` and no reuse of pre-existing User Pool), you will have to create users in the User Pool. See the [documentation](https://docs.aws.amazon.com/cognito/latest/developerguide/how-to-create-user-accounts.html). Note that the user pool allows self-registration of users.

### Client connection to Cognito User Pool

To authenticate the users on your client, you can use the [`amazon-cognito-identity-js`](https://www.npmjs.com/package/amazon-cognito-identity-js) library or [Amplify](https://docs.amplify.aws/lib/auth/getting-started/q/platform/js/) which is much simpler to setup.

### Calling the API

* HTTP Method: `GET`
* URL: https://12345abcd.execute-api.eu-west-1.amazonaws.com/prod/ (replace with yours)
* Query Parameters: `contentType` (a valid MIME Type, eg. `image/png` or `application/pdf`)
* Headers: `Authorization` header must contain the JWT Token retrieve from Cognito

  * Ex with Amplify: `Auth.currentSession()).getIdToken().getJwtToken()`

Ex with curl:

```bash
curl "https://ab12cd34.execute-api.eu-west-1.amazonaws.com/prod/?contentType=image/png" -H "Authorization: eyJraW...AZjp4gQA"
```

The API will return a JSON containing the `uploadURL` and the `key` of the S3 object:

```json
{"uploadURL":"https://yourbucknetname.s3.eu-west-1.amazonaws.com/0454dfa5-8ca5-448a-ae30-9b734313362a.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=SADJKLJKJDF3%24NFDSFDFeu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20221218T095711Z&X-Amz-Expires=300&X-Amz-Security-Token=1234cdef&X-Amz-Signature=13579abcde&X-Amz-SignedHeaders=host&x-id=PutObject","key":"0454dfa5-8ca5-448a-ae30-9b734313362a.png"}
```

### Upload the file

You can finally use the `uploadURL` and the `PUT` HTTP method to upload your file to S3. You need to specify the exact same content type in the headers.

Ex with curl:

```bash
curl  "https://yourbucknetname.s3.eu-west-1.amazonaws.com/0454dfa5-8ca5-448a-ae30-9b734313362a.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=SADJKLJKJDF3%24NFDSFDFeu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20221218T095711Z&X-Amz-Expires=300&X-Amz-Security-Token=1234cdef&X-Amz-Signature=13579abcde&X-Amz-SignedHeaders=host&x-id=PutObject" --upload-file "path/to/my/file.png" -H "Content-Type: image/png"
```
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from ._jsii import *

import aws_cdk.aws_apigateway as _aws_cdk_aws_apigateway_ceddda9d
import aws_cdk.aws_cognito as _aws_cdk_aws_cognito_ceddda9d
import aws_cdk.aws_logs as _aws_cdk_aws_logs_ceddda9d
import aws_cdk.aws_s3 as _aws_cdk_aws_s3_ceddda9d
import constructs as _constructs_77d1e7e8


@jsii.interface(jsii_type="cdk-s3-upload-presignedurl-api.IS3UploadSignedUrlApiProps")
class IS3UploadSignedUrlApiProps(typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="allowedOrigins")
    def allowed_origins(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional CORS allowedOrigins.

        Should allow your domain(s) as allowed origin to request the API

        :default: ['*']
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="apiGatewayProps")
    def api_gateway_props(self) -> typing.Any:
        '''Optional user provided props to override the default props for the API Gateway.

        :default: - Default props are used
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="existingBucketObj")
    def existing_bucket_obj(self) -> typing.Optional[_aws_cdk_aws_s3_ceddda9d.Bucket]:
        '''Optional bucket where files should be uploaded to.

        Should contains the CORS properties

        :default: - Default Bucket is created
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="existingUserPoolObj")
    def existing_user_pool_obj(
        self,
    ) -> typing.Optional[_aws_cdk_aws_cognito_ceddda9d.UserPool]:
        '''Optional Cognito User Pool to secure the API.

        You should have created a User Pool Client too.

        :default: - Default User Pool (and User Pool Client) are created
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="expiration")
    def expiration(self) -> typing.Optional[jsii.Number]:
        '''Optional expiration time in second.

        Time before the presigned url expires.

        :default: 300
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="logRetention")
    def log_retention(
        self,
    ) -> typing.Optional[_aws_cdk_aws_logs_ceddda9d.RetentionDays]:
        '''Optional log retention time for Lambda and API Gateway.

        :default: one week
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="secured")
    def secured(self) -> typing.Optional[builtins.bool]:
        '''Optional boolean to specify if the API is secured (with Cognito) or publicly open.

        :default: true
        '''
        ...


class _IS3UploadSignedUrlApiPropsProxy:
    __jsii_type__: typing.ClassVar[str] = "cdk-s3-upload-presignedurl-api.IS3UploadSignedUrlApiProps"

    @builtins.property
    @jsii.member(jsii_name="allowedOrigins")
    def allowed_origins(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional CORS allowedOrigins.

        Should allow your domain(s) as allowed origin to request the API

        :default: ['*']
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedOrigins"))

    @builtins.property
    @jsii.member(jsii_name="apiGatewayProps")
    def api_gateway_props(self) -> typing.Any:
        '''Optional user provided props to override the default props for the API Gateway.

        :default: - Default props are used
        '''
        return typing.cast(typing.Any, jsii.get(self, "apiGatewayProps"))

    @builtins.property
    @jsii.member(jsii_name="existingBucketObj")
    def existing_bucket_obj(self) -> typing.Optional[_aws_cdk_aws_s3_ceddda9d.Bucket]:
        '''Optional bucket where files should be uploaded to.

        Should contains the CORS properties

        :default: - Default Bucket is created
        '''
        return typing.cast(typing.Optional[_aws_cdk_aws_s3_ceddda9d.Bucket], jsii.get(self, "existingBucketObj"))

    @builtins.property
    @jsii.member(jsii_name="existingUserPoolObj")
    def existing_user_pool_obj(
        self,
    ) -> typing.Optional[_aws_cdk_aws_cognito_ceddda9d.UserPool]:
        '''Optional Cognito User Pool to secure the API.

        You should have created a User Pool Client too.

        :default: - Default User Pool (and User Pool Client) are created
        '''
        return typing.cast(typing.Optional[_aws_cdk_aws_cognito_ceddda9d.UserPool], jsii.get(self, "existingUserPoolObj"))

    @builtins.property
    @jsii.member(jsii_name="expiration")
    def expiration(self) -> typing.Optional[jsii.Number]:
        '''Optional expiration time in second.

        Time before the presigned url expires.

        :default: 300
        '''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "expiration"))

    @builtins.property
    @jsii.member(jsii_name="logRetention")
    def log_retention(
        self,
    ) -> typing.Optional[_aws_cdk_aws_logs_ceddda9d.RetentionDays]:
        '''Optional log retention time for Lambda and API Gateway.

        :default: one week
        '''
        return typing.cast(typing.Optional[_aws_cdk_aws_logs_ceddda9d.RetentionDays], jsii.get(self, "logRetention"))

    @builtins.property
    @jsii.member(jsii_name="secured")
    def secured(self) -> typing.Optional[builtins.bool]:
        '''Optional boolean to specify if the API is secured (with Cognito) or publicly open.

        :default: true
        '''
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "secured"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IS3UploadSignedUrlApiProps).__jsii_proxy_class__ = lambda : _IS3UploadSignedUrlApiPropsProxy


class S3UploadPresignedUrlApi(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="cdk-s3-upload-presignedurl-api.S3UploadPresignedUrlApi",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        props: typing.Optional[IS3UploadSignedUrlApiProps] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eacb99d5edf59176efece7d66cf3d220b3205f1ae22c487c18c831126c402698)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="bucket")
    def bucket(self) -> _aws_cdk_aws_s3_ceddda9d.Bucket:
        return typing.cast(_aws_cdk_aws_s3_ceddda9d.Bucket, jsii.get(self, "bucket"))

    @builtins.property
    @jsii.member(jsii_name="restApi")
    def rest_api(self) -> _aws_cdk_aws_apigateway_ceddda9d.RestApi:
        return typing.cast(_aws_cdk_aws_apigateway_ceddda9d.RestApi, jsii.get(self, "restApi"))

    @builtins.property
    @jsii.member(jsii_name="userPool")
    def user_pool(self) -> typing.Any:
        return typing.cast(typing.Any, jsii.get(self, "userPool"))

    @builtins.property
    @jsii.member(jsii_name="userPoolClient")
    def user_pool_client(self) -> typing.Any:
        return typing.cast(typing.Any, jsii.get(self, "userPoolClient"))


__all__ = [
    "IS3UploadSignedUrlApiProps",
    "S3UploadPresignedUrlApi",
]

publication.publish()

def _typecheckingstub__eacb99d5edf59176efece7d66cf3d220b3205f1ae22c487c18c831126c402698(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    props: typing.Optional[IS3UploadSignedUrlApiProps] = None,
) -> None:
    """Type checking stubs"""
    pass
