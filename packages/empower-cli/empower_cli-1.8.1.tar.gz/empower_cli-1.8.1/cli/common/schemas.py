from pydantic import BaseModel, Field


class AuthResponse1(BaseModel):
    server_url: str = Field(alias="authServerUrl")
    redirect_url: str = Field(alias="authServerUrl")
    realm: str = Field(alias="authRealm")
    client_id: str = Field(alias="authClientId")
    auth_enabled: str = Field(alias="authEnabled")


class OauthDomain(BaseModel):
    server_url: str = Field(alias="authServerUrl")
    realm: str = Field(alias="authRealm")
    user_service_url: str = Field(alias="userServiceUrl")
    client_id: str = Field(alias="clientId")
