'''
# replace this
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

import aws_cdk.aws_certificatemanager as _aws_cdk_aws_certificatemanager_ceddda9d
import aws_cdk.aws_cognito as _aws_cdk_aws_cognito_ceddda9d
import aws_cdk.aws_lambda as _aws_cdk_aws_lambda_ceddda9d
import constructs as _constructs_77d1e7e8


class RemixApp(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@rogerchi/cdk-remix-app.RemixApp",
):
    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        remix_path: builtins.str,
        cognito_auth: typing.Optional[typing.Union["RemixCognitoAuthProps", typing.Dict[builtins.str, typing.Any]]] = None,
        custom_domain: typing.Optional[typing.Union["RemixCustomDomainProps", typing.Dict[builtins.str, typing.Any]]] = None,
        ddb_sessions: typing.Optional[builtins.bool] = None,
        is_dev: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param remix_path: 
        :param cognito_auth: 
        :param custom_domain: 
        :param ddb_sessions: 
        :param is_dev: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80d96be4bb6c1aeaf00fe044b8e2d965e18669bd9a2ce3daba01d40f9c479dbb)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        __2 = RemixAppProps(
            remix_path=remix_path,
            cognito_auth=cognito_auth,
            custom_domain=custom_domain,
            ddb_sessions=ddb_sessions,
            is_dev=is_dev,
        )

        jsii.create(self.__class__, self, [scope, id, __2])

    @builtins.property
    @jsii.member(jsii_name="cdnDistributionId")
    def cdn_distribution_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cdnDistributionId"))

    @builtins.property
    @jsii.member(jsii_name="cdnDomainName")
    def cdn_domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cdnDomainName"))

    @builtins.property
    @jsii.member(jsii_name="handler")
    def handler(self) -> _aws_cdk_aws_lambda_ceddda9d.Function:
        return typing.cast(_aws_cdk_aws_lambda_ceddda9d.Function, jsii.get(self, "handler"))


@jsii.data_type(
    jsii_type="@rogerchi/cdk-remix-app.RemixAppProps",
    jsii_struct_bases=[],
    name_mapping={
        "remix_path": "remixPath",
        "cognito_auth": "cognitoAuth",
        "custom_domain": "customDomain",
        "ddb_sessions": "ddbSessions",
        "is_dev": "isDev",
    },
)
class RemixAppProps:
    def __init__(
        self,
        *,
        remix_path: builtins.str,
        cognito_auth: typing.Optional[typing.Union["RemixCognitoAuthProps", typing.Dict[builtins.str, typing.Any]]] = None,
        custom_domain: typing.Optional[typing.Union["RemixCustomDomainProps", typing.Dict[builtins.str, typing.Any]]] = None,
        ddb_sessions: typing.Optional[builtins.bool] = None,
        is_dev: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param remix_path: 
        :param cognito_auth: 
        :param custom_domain: 
        :param ddb_sessions: 
        :param is_dev: 
        '''
        if isinstance(cognito_auth, dict):
            cognito_auth = RemixCognitoAuthProps(**cognito_auth)
        if isinstance(custom_domain, dict):
            custom_domain = RemixCustomDomainProps(**custom_domain)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b30273385cd0d64f1ccab10a02f0adc300eee6a81631444fd1484ad836b8f95)
            check_type(argname="argument remix_path", value=remix_path, expected_type=type_hints["remix_path"])
            check_type(argname="argument cognito_auth", value=cognito_auth, expected_type=type_hints["cognito_auth"])
            check_type(argname="argument custom_domain", value=custom_domain, expected_type=type_hints["custom_domain"])
            check_type(argname="argument ddb_sessions", value=ddb_sessions, expected_type=type_hints["ddb_sessions"])
            check_type(argname="argument is_dev", value=is_dev, expected_type=type_hints["is_dev"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "remix_path": remix_path,
        }
        if cognito_auth is not None:
            self._values["cognito_auth"] = cognito_auth
        if custom_domain is not None:
            self._values["custom_domain"] = custom_domain
        if ddb_sessions is not None:
            self._values["ddb_sessions"] = ddb_sessions
        if is_dev is not None:
            self._values["is_dev"] = is_dev

    @builtins.property
    def remix_path(self) -> builtins.str:
        result = self._values.get("remix_path")
        assert result is not None, "Required property 'remix_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cognito_auth(self) -> typing.Optional["RemixCognitoAuthProps"]:
        result = self._values.get("cognito_auth")
        return typing.cast(typing.Optional["RemixCognitoAuthProps"], result)

    @builtins.property
    def custom_domain(self) -> typing.Optional["RemixCustomDomainProps"]:
        result = self._values.get("custom_domain")
        return typing.cast(typing.Optional["RemixCustomDomainProps"], result)

    @builtins.property
    def ddb_sessions(self) -> typing.Optional[builtins.bool]:
        result = self._values.get("ddb_sessions")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def is_dev(self) -> typing.Optional[builtins.bool]:
        result = self._values.get("is_dev")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RemixAppProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@rogerchi/cdk-remix-app.RemixCognitoAuthProps",
    jsii_struct_bases=[],
    name_mapping={"auth_domain": "authDomain", "user_pool": "userPool"},
)
class RemixCognitoAuthProps:
    def __init__(
        self,
        *,
        auth_domain: builtins.str,
        user_pool: _aws_cdk_aws_cognito_ceddda9d.IUserPool,
    ) -> None:
        '''
        :param auth_domain: 
        :param user_pool: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee4060c73d12add46dff49d03edc562f3a39b9f2f10606dc2b94c298e557c44d)
            check_type(argname="argument auth_domain", value=auth_domain, expected_type=type_hints["auth_domain"])
            check_type(argname="argument user_pool", value=user_pool, expected_type=type_hints["user_pool"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "auth_domain": auth_domain,
            "user_pool": user_pool,
        }

    @builtins.property
    def auth_domain(self) -> builtins.str:
        result = self._values.get("auth_domain")
        assert result is not None, "Required property 'auth_domain' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_pool(self) -> _aws_cdk_aws_cognito_ceddda9d.IUserPool:
        result = self._values.get("user_pool")
        assert result is not None, "Required property 'user_pool' is missing"
        return typing.cast(_aws_cdk_aws_cognito_ceddda9d.IUserPool, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RemixCognitoAuthProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@rogerchi/cdk-remix-app.RemixCustomDomainProps",
    jsii_struct_bases=[],
    name_mapping={"certificate": "certificate", "domain_name": "domainName"},
)
class RemixCustomDomainProps:
    def __init__(
        self,
        *,
        certificate: _aws_cdk_aws_certificatemanager_ceddda9d.ICertificate,
        domain_name: builtins.str,
    ) -> None:
        '''
        :param certificate: 
        :param domain_name: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5b3fdd44084252709ecf959805125c6e61168f8ee1c59ffd05681c45383e8ec)
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "certificate": certificate,
            "domain_name": domain_name,
        }

    @builtins.property
    def certificate(self) -> _aws_cdk_aws_certificatemanager_ceddda9d.ICertificate:
        result = self._values.get("certificate")
        assert result is not None, "Required property 'certificate' is missing"
        return typing.cast(_aws_cdk_aws_certificatemanager_ceddda9d.ICertificate, result)

    @builtins.property
    def domain_name(self) -> builtins.str:
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RemixCustomDomainProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "RemixApp",
    "RemixAppProps",
    "RemixCognitoAuthProps",
    "RemixCustomDomainProps",
]

publication.publish()

def _typecheckingstub__80d96be4bb6c1aeaf00fe044b8e2d965e18669bd9a2ce3daba01d40f9c479dbb(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    remix_path: builtins.str,
    cognito_auth: typing.Optional[typing.Union[RemixCognitoAuthProps, typing.Dict[builtins.str, typing.Any]]] = None,
    custom_domain: typing.Optional[typing.Union[RemixCustomDomainProps, typing.Dict[builtins.str, typing.Any]]] = None,
    ddb_sessions: typing.Optional[builtins.bool] = None,
    is_dev: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b30273385cd0d64f1ccab10a02f0adc300eee6a81631444fd1484ad836b8f95(
    *,
    remix_path: builtins.str,
    cognito_auth: typing.Optional[typing.Union[RemixCognitoAuthProps, typing.Dict[builtins.str, typing.Any]]] = None,
    custom_domain: typing.Optional[typing.Union[RemixCustomDomainProps, typing.Dict[builtins.str, typing.Any]]] = None,
    ddb_sessions: typing.Optional[builtins.bool] = None,
    is_dev: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee4060c73d12add46dff49d03edc562f3a39b9f2f10606dc2b94c298e557c44d(
    *,
    auth_domain: builtins.str,
    user_pool: _aws_cdk_aws_cognito_ceddda9d.IUserPool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5b3fdd44084252709ecf959805125c6e61168f8ee1c59ffd05681c45383e8ec(
    *,
    certificate: _aws_cdk_aws_certificatemanager_ceddda9d.ICertificate,
    domain_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass
