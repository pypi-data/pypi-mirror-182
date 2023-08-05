# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class Access(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Access to be allowed or denied."""

    ALLOW = "Allow"
    DENY = "Deny"


class ApplicationGatewayBackendHealthServerHealth(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Health of backend server."""

    UNKNOWN = "Unknown"
    UP = "Up"
    DOWN = "Down"
    PARTIAL = "Partial"
    DRAINING = "Draining"


class ApplicationGatewayCookieBasedAffinity(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Cookie based affinity."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class ApplicationGatewayCustomErrorStatusCode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Status code of the application gateway customer error."""

    HTTP_STATUS403 = "HttpStatus403"
    HTTP_STATUS502 = "HttpStatus502"


class ApplicationGatewayFirewallMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Web application firewall mode."""

    DETECTION = "Detection"
    PREVENTION = "Prevention"


class ApplicationGatewayOperationalState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Operational state of the application gateway resource."""

    STOPPED = "Stopped"
    STARTING = "Starting"
    RUNNING = "Running"
    STOPPING = "Stopping"


class ApplicationGatewayProtocol(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Application Gateway protocol."""

    HTTP = "Http"
    HTTPS = "Https"


class ApplicationGatewayRedirectType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Redirect type enum."""

    PERMANENT = "Permanent"
    FOUND = "Found"
    SEE_OTHER = "SeeOther"
    TEMPORARY = "Temporary"


class ApplicationGatewayRequestRoutingRuleType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Rule type."""

    BASIC = "Basic"
    PATH_BASED_ROUTING = "PathBasedRouting"


class ApplicationGatewaySkuName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Name of an application gateway SKU."""

    STANDARD_SMALL = "Standard_Small"
    STANDARD_MEDIUM = "Standard_Medium"
    STANDARD_LARGE = "Standard_Large"
    WAF_MEDIUM = "WAF_Medium"
    WAF_LARGE = "WAF_Large"
    STANDARD_V2 = "Standard_v2"
    WAF_V2 = "WAF_v2"


class ApplicationGatewaySslCipherSuite(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Ssl cipher suites enums."""

    TLS_ECDHE_RSA_WITH_AES256_CBC_SHA384 = "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384"
    TLS_ECDHE_RSA_WITH_AES128_CBC_SHA256 = "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256"
    TLS_ECDHE_RSA_WITH_AES256_CBC_SHA = "TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA"
    TLS_ECDHE_RSA_WITH_AES128_CBC_SHA = "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA"
    TLS_DHE_RSA_WITH_AES256_GCM_SHA384 = "TLS_DHE_RSA_WITH_AES_256_GCM_SHA384"
    TLS_DHE_RSA_WITH_AES128_GCM_SHA256 = "TLS_DHE_RSA_WITH_AES_128_GCM_SHA256"
    TLS_DHE_RSA_WITH_AES256_CBC_SHA = "TLS_DHE_RSA_WITH_AES_256_CBC_SHA"
    TLS_DHE_RSA_WITH_AES128_CBC_SHA = "TLS_DHE_RSA_WITH_AES_128_CBC_SHA"
    TLS_RSA_WITH_AES256_GCM_SHA384 = "TLS_RSA_WITH_AES_256_GCM_SHA384"
    TLS_RSA_WITH_AES128_GCM_SHA256 = "TLS_RSA_WITH_AES_128_GCM_SHA256"
    TLS_RSA_WITH_AES256_CBC_SHA256 = "TLS_RSA_WITH_AES_256_CBC_SHA256"
    TLS_RSA_WITH_AES128_CBC_SHA256 = "TLS_RSA_WITH_AES_128_CBC_SHA256"
    TLS_RSA_WITH_AES256_CBC_SHA = "TLS_RSA_WITH_AES_256_CBC_SHA"
    TLS_RSA_WITH_AES128_CBC_SHA = "TLS_RSA_WITH_AES_128_CBC_SHA"
    TLS_ECDHE_ECDSA_WITH_AES256_GCM_SHA384 = "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384"
    TLS_ECDHE_ECDSA_WITH_AES128_GCM_SHA256 = "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256"
    TLS_ECDHE_ECDSA_WITH_AES256_CBC_SHA384 = "TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384"
    TLS_ECDHE_ECDSA_WITH_AES128_CBC_SHA256 = "TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256"
    TLS_ECDHE_ECDSA_WITH_AES256_CBC_SHA = "TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA"
    TLS_ECDHE_ECDSA_WITH_AES128_CBC_SHA = "TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA"
    TLS_DHE_DSS_WITH_AES256_CBC_SHA256 = "TLS_DHE_DSS_WITH_AES_256_CBC_SHA256"
    TLS_DHE_DSS_WITH_AES128_CBC_SHA256 = "TLS_DHE_DSS_WITH_AES_128_CBC_SHA256"
    TLS_DHE_DSS_WITH_AES256_CBC_SHA = "TLS_DHE_DSS_WITH_AES_256_CBC_SHA"
    TLS_DHE_DSS_WITH_AES128_CBC_SHA = "TLS_DHE_DSS_WITH_AES_128_CBC_SHA"
    TLS_RSA_WITH3_DES_EDE_CBC_SHA = "TLS_RSA_WITH_3DES_EDE_CBC_SHA"
    TLS_DHE_DSS_WITH3_DES_EDE_CBC_SHA = "TLS_DHE_DSS_WITH_3DES_EDE_CBC_SHA"
    TLS_ECDHE_RSA_WITH_AES128_GCM_SHA256 = "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256"
    TLS_ECDHE_RSA_WITH_AES256_GCM_SHA384 = "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384"


class ApplicationGatewaySslPolicyName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Ssl predefined policy name enums."""

    APP_GW_SSL_POLICY20150501 = "AppGwSslPolicy20150501"
    APP_GW_SSL_POLICY20170401 = "AppGwSslPolicy20170401"
    APP_GW_SSL_POLICY20170401_S = "AppGwSslPolicy20170401S"


class ApplicationGatewaySslPolicyType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of Ssl Policy."""

    PREDEFINED = "Predefined"
    CUSTOM = "Custom"


class ApplicationGatewaySslProtocol(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Ssl protocol enums."""

    TL_SV1_0 = "TLSv1_0"
    TL_SV1_1 = "TLSv1_1"
    TL_SV1_2 = "TLSv1_2"


class ApplicationGatewayTier(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Tier of an application gateway."""

    STANDARD = "Standard"
    WAF = "WAF"
    STANDARD_V2 = "Standard_v2"
    WAF_V2 = "WAF_v2"


class AssociationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The association type of the child resource to the parent resource."""

    ASSOCIATED = "Associated"
    CONTAINS = "Contains"


class AuthenticationMethod(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """VPN client authentication method."""

    EAPTLS = "EAPTLS"
    EAPMSCHA_PV2 = "EAPMSCHAPv2"


class AuthorizationUseStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The authorization use status."""

    AVAILABLE = "Available"
    IN_USE = "InUse"


class AzureFirewallApplicationRuleProtocolType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The protocol type of a Application Rule resource."""

    HTTP = "Http"
    HTTPS = "Https"
    MSSQL = "Mssql"


class AzureFirewallNatRCActionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The action type of a NAT rule collection."""

    SNAT = "Snat"
    DNAT = "Dnat"


class AzureFirewallNetworkRuleProtocol(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The protocol of a Network Rule resource."""

    TCP = "TCP"
    UDP = "UDP"
    ANY = "Any"
    ICMP = "ICMP"


class AzureFirewallRCActionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The action type of a rule collection."""

    ALLOW = "Allow"
    DENY = "Deny"


class AzureFirewallSkuName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Name of an Azure Firewall SKU."""

    AZFW_VNET = "AZFW_VNet"
    AZFW_HUB = "AZFW_Hub"


class AzureFirewallSkuTier(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Tier of an Azure Firewall."""

    STANDARD = "Standard"


class AzureFirewallThreatIntelMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The operation mode for Threat Intel."""

    ALERT = "Alert"
    DENY = "Deny"
    OFF = "Off"


class BgpPeerState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The BGP peer state."""

    UNKNOWN = "Unknown"
    STOPPED = "Stopped"
    IDLE = "Idle"
    CONNECTING = "Connecting"
    CONNECTED = "Connected"


class CircuitConnectionStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Express Route Circuit connection state."""

    CONNECTED = "Connected"
    CONNECTING = "Connecting"
    DISCONNECTED = "Disconnected"


class ConnectionMonitorSourceStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Status of connection monitor source."""

    UNKNOWN = "Unknown"
    ACTIVE = "Active"
    INACTIVE = "Inactive"


class ConnectionState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The connection state."""

    REACHABLE = "Reachable"
    UNREACHABLE = "Unreachable"
    UNKNOWN = "Unknown"


class ConnectionStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The connection status."""

    UNKNOWN = "Unknown"
    CONNECTED = "Connected"
    DISCONNECTED = "Disconnected"
    DEGRADED = "Degraded"


class DdosCustomPolicyProtocol(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The protocol for which the DDoS protection policy is being customized."""

    TCP = "Tcp"
    UDP = "Udp"
    SYN = "Syn"


class DdosCustomPolicyTriggerSensitivityOverride(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The customized DDoS protection trigger rate sensitivity degrees. High: Trigger rate set with
    most sensitivity w.r.t. normal traffic. Default: Trigger rate set with moderate sensitivity
    w.r.t. normal traffic. Low: Trigger rate set with less sensitivity w.r.t. normal traffic.
    Relaxed: Trigger rate set with least sensitivity w.r.t. normal traffic.
    """

    RELAXED = "Relaxed"
    LOW = "Low"
    DEFAULT = "Default"
    HIGH = "High"


class DdosSettingsProtectionCoverage(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The DDoS protection policy customizability of the public IP. Only standard coverage will have
    the ability to be customized.
    """

    BASIC = "Basic"
    STANDARD = "Standard"


class DhGroup(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The DH Groups used in IKE Phase 1 for initial SA."""

    NONE = "None"
    DH_GROUP1 = "DHGroup1"
    DH_GROUP2 = "DHGroup2"
    DH_GROUP14 = "DHGroup14"
    DH_GROUP2048 = "DHGroup2048"
    ECP256 = "ECP256"
    ECP384 = "ECP384"
    DH_GROUP24 = "DHGroup24"


class Direction(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The direction of the traffic."""

    INBOUND = "Inbound"
    OUTBOUND = "Outbound"


class EffectiveRouteSource(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Who created the route."""

    UNKNOWN = "Unknown"
    USER = "User"
    VIRTUAL_NETWORK_GATEWAY = "VirtualNetworkGateway"
    DEFAULT = "Default"


class EffectiveRouteState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The value of effective route."""

    ACTIVE = "Active"
    INVALID = "Invalid"


class EffectiveSecurityRuleProtocol(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The network protocol this rule applies to."""

    TCP = "Tcp"
    UDP = "Udp"
    ALL = "All"


class EvaluationState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Connectivity analysis evaluation state."""

    NOT_STARTED = "NotStarted"
    IN_PROGRESS = "InProgress"
    COMPLETED = "Completed"


class ExpressRouteCircuitPeeringAdvertisedPublicPrefixState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The advertised public prefix state of the Peering resource."""

    NOT_CONFIGURED = "NotConfigured"
    CONFIGURING = "Configuring"
    CONFIGURED = "Configured"
    VALIDATION_NEEDED = "ValidationNeeded"


class ExpressRouteCircuitPeeringState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The state of peering."""

    DISABLED = "Disabled"
    ENABLED = "Enabled"


class ExpressRouteCircuitSkuFamily(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The family of the SKU."""

    UNLIMITED_DATA = "UnlimitedData"
    METERED_DATA = "MeteredData"


class ExpressRouteCircuitSkuTier(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The tier of the SKU."""

    STANDARD = "Standard"
    PREMIUM = "Premium"
    BASIC = "Basic"
    LOCAL = "Local"


class ExpressRouteLinkAdminState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Administrative state of the physical port."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class ExpressRouteLinkConnectorType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Physical fiber port type."""

    LC = "LC"
    SC = "SC"


class ExpressRouteLinkMacSecCipher(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Mac security cipher."""

    GCM_AES128 = "gcm-aes-128"
    GCM_AES256 = "gcm-aes-256"


class ExpressRoutePeeringState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The state of peering."""

    DISABLED = "Disabled"
    ENABLED = "Enabled"


class ExpressRoutePeeringType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The peering type."""

    AZURE_PUBLIC_PEERING = "AzurePublicPeering"
    AZURE_PRIVATE_PEERING = "AzurePrivatePeering"
    MICROSOFT_PEERING = "MicrosoftPeering"


class ExpressRoutePortsEncapsulation(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Encapsulation method on physical ports."""

    DOT1_Q = "Dot1Q"
    QIN_Q = "QinQ"


class FirewallPolicyFilterRuleActionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The action type of a rule."""

    ALLOW = "Allow"
    DENY = "Deny"


class FirewallPolicyNatRuleActionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The action type of a rule."""

    DNAT = "DNAT"


class FirewallPolicyRuleConditionApplicationProtocolType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The application protocol type of a Rule condition."""

    HTTP = "Http"
    HTTPS = "Https"


class FirewallPolicyRuleConditionNetworkProtocol(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The Network protocol of a Rule condition."""

    TCP = "TCP"
    UDP = "UDP"
    ANY = "Any"
    ICMP = "ICMP"


class FirewallPolicyRuleConditionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Rule Condition Type."""

    APPLICATION_RULE_CONDITION = "ApplicationRuleCondition"
    NETWORK_RULE_CONDITION = "NetworkRuleCondition"


class FirewallPolicyRuleType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of the rule."""

    FIREWALL_POLICY_NAT_RULE = "FirewallPolicyNatRule"
    FIREWALL_POLICY_FILTER_RULE = "FirewallPolicyFilterRule"


class FlowLogFormatType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The file type of flow log."""

    JSON = "JSON"


class HTTPMethod(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """HTTP method."""

    GET = "Get"


class HubVirtualNetworkConnectionStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The current state of the VirtualHub to vnet connection."""

    UNKNOWN = "Unknown"
    CONNECTING = "Connecting"
    CONNECTED = "Connected"
    NOT_CONNECTED = "NotConnected"


class IkeEncryption(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The IKE encryption algorithm (IKE phase 2)."""

    DES = "DES"
    DES3 = "DES3"
    AES128 = "AES128"
    AES192 = "AES192"
    AES256 = "AES256"
    GCMAES256 = "GCMAES256"
    GCMAES128 = "GCMAES128"


class IkeIntegrity(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The IKE integrity algorithm (IKE phase 2)."""

    MD5 = "MD5"
    SHA1 = "SHA1"
    SHA256 = "SHA256"
    SHA384 = "SHA384"
    GCMAES256 = "GCMAES256"
    GCMAES128 = "GCMAES128"


class IPAllocationMethod(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """IP address allocation method."""

    STATIC = "Static"
    DYNAMIC = "Dynamic"


class IpFlowProtocol(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Protocol to be verified on."""

    TCP = "TCP"
    UDP = "UDP"


class IpsecEncryption(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The IPSec encryption algorithm (IKE phase 1)."""

    NONE = "None"
    DES = "DES"
    DES3 = "DES3"
    AES128 = "AES128"
    AES192 = "AES192"
    AES256 = "AES256"
    GCMAES128 = "GCMAES128"
    GCMAES192 = "GCMAES192"
    GCMAES256 = "GCMAES256"


class IpsecIntegrity(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The IPSec integrity algorithm (IKE phase 1)."""

    MD5 = "MD5"
    SHA1 = "SHA1"
    SHA256 = "SHA256"
    GCMAES128 = "GCMAES128"
    GCMAES192 = "GCMAES192"
    GCMAES256 = "GCMAES256"


class IPVersion(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """IP address version."""

    I_PV4 = "IPv4"
    I_PV6 = "IPv6"


class IssueType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of issue."""

    UNKNOWN = "Unknown"
    AGENT_STOPPED = "AgentStopped"
    GUEST_FIREWALL = "GuestFirewall"
    DNS_RESOLUTION = "DnsResolution"
    SOCKET_BIND = "SocketBind"
    NETWORK_SECURITY_RULE = "NetworkSecurityRule"
    USER_DEFINED_ROUTE = "UserDefinedRoute"
    PORT_THROTTLED = "PortThrottled"
    PLATFORM = "Platform"


class LoadBalancerOutboundRuleProtocol(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The protocol for the outbound rule in load balancer."""

    TCP = "Tcp"
    UDP = "Udp"
    ALL = "All"


class LoadBalancerSkuName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Name of a load balancer SKU."""

    BASIC = "Basic"
    STANDARD = "Standard"


class LoadDistribution(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The load distribution policy for this rule."""

    DEFAULT = "Default"
    SOURCE_IP = "SourceIP"
    SOURCE_IP_PROTOCOL = "SourceIPProtocol"


class ManagedRuleEnabledState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Describes the state of the managed rule. Defaults to Disabled if not specified."""

    DISABLED = "Disabled"


class NatGatewaySkuName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Name of Nat Gateway SKU."""

    STANDARD = "Standard"


class NetworkOperationStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Status of the Azure async operation."""

    IN_PROGRESS = "InProgress"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"


class NextHopType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Next hop type."""

    INTERNET = "Internet"
    VIRTUAL_APPLIANCE = "VirtualAppliance"
    VIRTUAL_NETWORK_GATEWAY = "VirtualNetworkGateway"
    VNET_LOCAL = "VnetLocal"
    HYPER_NET_GATEWAY = "HyperNetGateway"
    NONE = "None"


class OfficeTrafficCategory(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The office traffic category."""

    OPTIMIZE = "Optimize"
    OPTIMIZE_AND_ALLOW = "OptimizeAndAllow"
    ALL = "All"
    NONE = "None"


class Origin(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The origin of the issue."""

    LOCAL = "Local"
    INBOUND = "Inbound"
    OUTBOUND = "Outbound"


class OwaspCrsExclusionEntryMatchVariable(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The variable to be excluded."""

    REQUEST_HEADER_NAMES = "RequestHeaderNames"
    REQUEST_COOKIE_NAMES = "RequestCookieNames"
    REQUEST_ARG_NAMES = "RequestArgNames"


class OwaspCrsExclusionEntrySelectorMatchOperator(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """When matchVariable is a collection, operate on the selector to specify which elements in the
    collection this exclusion applies to.
    """

    EQUALS = "Equals"
    CONTAINS = "Contains"
    STARTS_WITH = "StartsWith"
    ENDS_WITH = "EndsWith"
    EQUALS_ANY = "EqualsAny"


class PcError(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """PcError."""

    INTERNAL_ERROR = "InternalError"
    AGENT_STOPPED = "AgentStopped"
    CAPTURE_FAILED = "CaptureFailed"
    LOCAL_FILE_FAILED = "LocalFileFailed"
    STORAGE_FAILED = "StorageFailed"


class PcProtocol(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Protocol to be filtered on."""

    TCP = "TCP"
    UDP = "UDP"
    ANY = "Any"


class PcStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The status of the packet capture session."""

    NOT_STARTED = "NotStarted"
    RUNNING = "Running"
    STOPPED = "Stopped"
    ERROR = "Error"
    UNKNOWN = "Unknown"


class PfsGroup(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The Pfs Groups used in IKE Phase 2 for new child SA."""

    NONE = "None"
    PFS1 = "PFS1"
    PFS2 = "PFS2"
    PFS2048 = "PFS2048"
    ECP256 = "ECP256"
    ECP384 = "ECP384"
    PFS24 = "PFS24"
    PFS14 = "PFS14"
    PFSMM = "PFSMM"


class ProbeProtocol(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The protocol of the end point. If 'Tcp' is specified, a received ACK is required for the probe
    to be successful. If 'Http' or 'Https' is specified, a 200 OK response from the specifies URI
    is required for the probe to be successful.
    """

    HTTP = "Http"
    TCP = "Tcp"
    HTTPS = "Https"


class ProcessorArchitecture(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """VPN client Processor Architecture."""

    AMD64 = "Amd64"
    X86 = "X86"


class Protocol(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Network protocol."""

    TCP = "Tcp"
    HTTP = "Http"
    HTTPS = "Https"
    ICMP = "Icmp"


class ProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The current provisioning state."""

    SUCCEEDED = "Succeeded"
    UPDATING = "Updating"
    DELETING = "Deleting"
    FAILED = "Failed"


class PublicIPAddressSkuName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Name of a public IP address SKU."""

    BASIC = "Basic"
    STANDARD = "Standard"


class PublicIPPrefixSkuName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Name of a public IP prefix SKU."""

    STANDARD = "Standard"


class ResourceIdentityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity used for the resource. The type 'SystemAssigned, UserAssigned' includes
    both an implicitly created identity and a set of user assigned identities. The type 'None' will
    remove any identities from the virtual machine.
    """

    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned, UserAssigned"
    NONE = "None"


class RouteFilterRuleType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The rule type of the rule."""

    COMMUNITY = "Community"


class RouteNextHopType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of Azure hop the packet should be sent to."""

    VIRTUAL_NETWORK_GATEWAY = "VirtualNetworkGateway"
    VNET_LOCAL = "VnetLocal"
    INTERNET = "Internet"
    VIRTUAL_APPLIANCE = "VirtualAppliance"
    NONE = "None"


class SecurityRuleAccess(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Whether network traffic is allowed or denied."""

    ALLOW = "Allow"
    DENY = "Deny"


class SecurityRuleDirection(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The direction of the rule. The direction specifies if rule will be evaluated on incoming or
    outgoing traffic.
    """

    INBOUND = "Inbound"
    OUTBOUND = "Outbound"


class SecurityRuleProtocol(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Network protocol this rule applies to."""

    TCP = "Tcp"
    UDP = "Udp"
    ICMP = "Icmp"
    ESP = "Esp"
    ASTERISK = "*"
    AH = "Ah"


class ServiceProviderProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The ServiceProviderProvisioningState state of the resource."""

    NOT_PROVISIONED = "NotProvisioned"
    PROVISIONING = "Provisioning"
    PROVISIONED = "Provisioned"
    DEPROVISIONING = "Deprovisioning"


class Severity(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The severity of the issue."""

    ERROR = "Error"
    WARNING = "Warning"


class TransportProtocol(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The transport protocol for the endpoint."""

    UDP = "Udp"
    TCP = "Tcp"
    ALL = "All"


class TunnelConnectionStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The current state of the tunnel."""

    UNKNOWN = "Unknown"
    CONNECTING = "Connecting"
    CONNECTED = "Connected"
    NOT_CONNECTED = "NotConnected"


class UsageUnit(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """An enum describing the unit of measurement."""

    COUNT = "Count"


class VerbosityLevel(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Verbosity level."""

    NORMAL = "Normal"
    MINIMUM = "Minimum"
    FULL = "Full"


class VirtualNetworkGatewayConnectionProtocol(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Gateway connection protocol."""

    IK_EV2 = "IKEv2"
    IK_EV1 = "IKEv1"


class VirtualNetworkGatewayConnectionStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Virtual Network Gateway connection status."""

    UNKNOWN = "Unknown"
    CONNECTING = "Connecting"
    CONNECTED = "Connected"
    NOT_CONNECTED = "NotConnected"


class VirtualNetworkGatewayConnectionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Gateway connection type."""

    I_PSEC = "IPsec"
    VNET2_VNET = "Vnet2Vnet"
    EXPRESS_ROUTE = "ExpressRoute"
    VPN_CLIENT = "VPNClient"


class VirtualNetworkGatewaySkuName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Gateway SKU name."""

    BASIC = "Basic"
    HIGH_PERFORMANCE = "HighPerformance"
    STANDARD = "Standard"
    ULTRA_PERFORMANCE = "UltraPerformance"
    VPN_GW1 = "VpnGw1"
    VPN_GW2 = "VpnGw2"
    VPN_GW3 = "VpnGw3"
    VPN_GW4 = "VpnGw4"
    VPN_GW5 = "VpnGw5"
    VPN_GW1_AZ = "VpnGw1AZ"
    VPN_GW2_AZ = "VpnGw2AZ"
    VPN_GW3_AZ = "VpnGw3AZ"
    VPN_GW4_AZ = "VpnGw4AZ"
    VPN_GW5_AZ = "VpnGw5AZ"
    ER_GW1_AZ = "ErGw1AZ"
    ER_GW2_AZ = "ErGw2AZ"
    ER_GW3_AZ = "ErGw3AZ"


class VirtualNetworkGatewaySkuTier(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Gateway SKU tier."""

    BASIC = "Basic"
    HIGH_PERFORMANCE = "HighPerformance"
    STANDARD = "Standard"
    ULTRA_PERFORMANCE = "UltraPerformance"
    VPN_GW1 = "VpnGw1"
    VPN_GW2 = "VpnGw2"
    VPN_GW3 = "VpnGw3"
    VPN_GW4 = "VpnGw4"
    VPN_GW5 = "VpnGw5"
    VPN_GW1_AZ = "VpnGw1AZ"
    VPN_GW2_AZ = "VpnGw2AZ"
    VPN_GW3_AZ = "VpnGw3AZ"
    VPN_GW4_AZ = "VpnGw4AZ"
    VPN_GW5_AZ = "VpnGw5AZ"
    ER_GW1_AZ = "ErGw1AZ"
    ER_GW2_AZ = "ErGw2AZ"
    ER_GW3_AZ = "ErGw3AZ"


class VirtualNetworkGatewayType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of this virtual network gateway."""

    VPN = "Vpn"
    EXPRESS_ROUTE = "ExpressRoute"


class VirtualNetworkPeeringState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The status of the virtual network peering."""

    INITIATED = "Initiated"
    CONNECTED = "Connected"
    DISCONNECTED = "Disconnected"


class VirtualWanSecurityProviderType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The virtual wan security provider type."""

    EXTERNAL = "External"
    NATIVE = "Native"


class VpnAuthenticationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """VPN authentication types enabled for the VpnServerConfiguration."""

    CERTIFICATE = "Certificate"
    RADIUS = "Radius"
    AAD = "AAD"


class VpnClientProtocol(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """VPN client protocol enabled for the virtual network gateway."""

    IKE_V2 = "IkeV2"
    SSTP = "SSTP"
    OPEN_VPN = "OpenVPN"


class VpnConnectionStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The current state of the vpn connection."""

    UNKNOWN = "Unknown"
    CONNECTING = "Connecting"
    CONNECTED = "Connected"
    NOT_CONNECTED = "NotConnected"


class VpnGatewayGeneration(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The generation for this VirtualNetworkGateway. Must be None if gatewayType is not VPN."""

    NONE = "None"
    GENERATION1 = "Generation1"
    GENERATION2 = "Generation2"


class VpnGatewayTunnelingProtocol(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """VPN protocol enabled for the VpnServerConfiguration."""

    IKE_V2 = "IkeV2"
    OPEN_VPN = "OpenVPN"


class VpnType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of this virtual network gateway."""

    POLICY_BASED = "PolicyBased"
    ROUTE_BASED = "RouteBased"


class WebApplicationFirewallAction(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of Actions."""

    ALLOW = "Allow"
    BLOCK = "Block"
    LOG = "Log"


class WebApplicationFirewallEnabledState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Describes if the policy is in enabled state or disabled state."""

    DISABLED = "Disabled"
    ENABLED = "Enabled"


class WebApplicationFirewallMatchVariable(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Match Variable."""

    REMOTE_ADDR = "RemoteAddr"
    REQUEST_METHOD = "RequestMethod"
    QUERY_STRING = "QueryString"
    POST_ARGS = "PostArgs"
    REQUEST_URI = "RequestUri"
    REQUEST_HEADERS = "RequestHeaders"
    REQUEST_BODY = "RequestBody"
    REQUEST_COOKIES = "RequestCookies"


class WebApplicationFirewallMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Describes if it is in detection mode or prevention mode at policy level."""

    PREVENTION = "Prevention"
    DETECTION = "Detection"


class WebApplicationFirewallOperator(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Describes operator to be matched."""

    IP_MATCH = "IPMatch"
    EQUAL = "Equal"
    CONTAINS = "Contains"
    LESS_THAN = "LessThan"
    GREATER_THAN = "GreaterThan"
    LESS_THAN_OR_EQUAL = "LessThanOrEqual"
    GREATER_THAN_OR_EQUAL = "GreaterThanOrEqual"
    BEGINS_WITH = "BeginsWith"
    ENDS_WITH = "EndsWith"
    REGEX = "Regex"


class WebApplicationFirewallPolicyResourceState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Resource status of the policy."""

    CREATING = "Creating"
    ENABLING = "Enabling"
    ENABLED = "Enabled"
    DISABLING = "Disabling"
    DISABLED = "Disabled"
    DELETING = "Deleting"


class WebApplicationFirewallRuleType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Describes type of rule."""

    MATCH_RULE = "MatchRule"
    INVALID = "Invalid"


class WebApplicationFirewallTransform(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Describes what transforms applied before matching."""

    LOWERCASE = "Lowercase"
    TRIM = "Trim"
    URL_DECODE = "UrlDecode"
    URL_ENCODE = "UrlEncode"
    REMOVE_NULLS = "RemoveNulls"
    HTML_ENTITY_DECODE = "HtmlEntityDecode"
