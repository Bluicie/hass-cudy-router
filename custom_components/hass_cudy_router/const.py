from homeassistant.components.sensor import SensorStateClass
from homeassistant.const import EntityCategory

DOMAIN = "hass_cudy_router"

PLATFORMS = {"sensor", "button", "device_tracker"}

DEFAULT_SCAN_INTERVAL = 30

MODULE_SYSTEM = "system"
MODULE_LAN = "lan"
MODULE_DEVICES = "devices"
MODULE_MESH = "mesh"
MODULE_WAN = "wan"
MODULE_WAN_SECONDARY = "wan_secondary"
MODULE_MULTI_WAN = "multi_wan"
MODULE_WIRELESS_24G = "wifi_24"
MODULE_WIRELESS_5G = "wifi_5g"
MODULE_WIRELESS_6G = "wifi_6g"
MODULE_DHCP = "dhcp"
MODULE_GSM = "gsm"
MODULE_SMS = "sms"
MODULE_VPN = "vpn"
MODULE_USB = "usb"

## System
SENSOR_SYSTEM_FIRMWARE_VERSION = "system_firmware"
SENSOR_SYSTEM_MODEL = "system_model"
SENSOR_SYSTEM_HARDWARE = "system_hardware"
SENSOR_SYSTEM_UPTIME = "system_uptime"
SENSOR_SYSTEM_LOCALTIME = "system_localtime"
## Mesh
SENSOR_MESH_NETWORK = "mesh_network"
SENSOR_MESH_UNITS = "mesh_units"
## WAN
SENSOR_WAN_PUBLIC_IP = "wan_public_ip"
SENSOR_WAN_IP = "wan_ip"
SENSOR_WAN_DNS = "wan_dns"
SENSOR_WAN_TYPE = "wan_type"
SENSOR_WAN_UPTIME = "wan_uptime"
SENSOR_WAN_GATEWAY = "wan_gateway"
SENSOR_WAN_MODE = "wan_mode"
## LAN
SENSOR_LAN_IP = "lan_ip"
SENSOR_LAN_SUBNET = "lan_subnet"
SENSOR_LAN_MAC = "lan_mac"
## WiFI 2.4G
SENSOR_24G_WIFI_SSID = "24g_wifi_ssid"
SENSOR_24G_WIFI_BSSID = "24g_wifi_bssid"
SENSOR_24G_WIFI_ENCRYPTION = "24g_wifi_encryption"
SENSOR_24G_WIFI_CHANNEL = "24g_wifi_channel"
## WiFi 5G
SENSOR_5G_WIFI_SSID = "5g_wifi_ssid"
SENSOR_5G_WIFI_BSSID = "5g_wifi_bssid"
SENSOR_5G_WIFI_ENCRYPTION = "5g_wifi_encryption"
SENSOR_5G_WIFI_CHANNEL = "5g_wifi_channel"
## WiFi 6G
SENSOR_6G_WIFI_SSID = "6g_wifi_ssid"
SENSOR_6G_WIFI_BSSID = "6g_wifi_bssid"
SENSOR_6G_WIFI_ENCRYPTION = "6g_wifi_encryption"
SENSOR_6G_WIFI_CHANNEL = "6g_wifi_channel"
## Devices
SENSOR_DEVICE_COUNT = "device_count"
SENSOR_DEVICE_WIFI_24_COUNT = "device_wifi_24_device_count"
SENSOR_DEVICE_WIFI_5_COUNT = "device_wifi_5_device_count"
SENSOR_DEVICE_WIRED_COUNT = "device_wired_device_count"
SENSOR_DEVICE_MESH_COUNT = "device_mesh_device_count"
SENSOR_DEVICE_ONLINE = "device_online"
SENSOR_DEVICE_BLOCKED = "device_blocked"
## DHCP
SENSOR_DHCP_IP_START = "dhcp_ip_start"
SENSOR_DHCP_IP_END = "dhcp_ip_end"
SENSOR_DHCP_DNS_PRIMARY = "dhcp_dns_primary"
SENSOR_DHCP_DNS_SECONDARY = "dhcp_dns_secondary"
SENSOR_DHCP_GATEWAY = "dhcp_gateway"
SENSOR_DHCP_LEASE_TIME = "dhcp_lease_time"
## GSM
SENSOR_GSM_NETWORK_TYPE = "gsm_network_type"
SENSOR_GSM_DOWNLOAD = "gsm_download"
SENSOR_GSM_UPLOAD = "gsm_upload"
SENSOR_GSM_PUBLIC_IP = "gsm_public_ip"
SENSOR_GSM_IP_ADDRESS = "gsm_ip_address"
SENSOR_GSM_CONNECTED_TIME = "gsm_connected_time"
## SMS
SENSOR_SMS_INBOX = "sms_inbox"
SENSOR_SMS_OUTBOX = "sms_outbox"
## VPN
SENSOR_VPN_ENABLED = "vpn_enabled"
SENSOR_VPN_TUNNELS = "vpn_tunnels"
## USB
SENSOR_USB_TETHERING = "usb_tethering"
SENSOR_USB_SHARING = "usb_sharing"

SENSORS_KEY_KEY = "key"
SENSORS_KEY_DESCRIPTION = "description"
SENSORS_KEY_ICON = "icon"
SENSORS_KEY_CATEGORY = "entity_category"
SENSORS_KEY_CLASS = "state_class"

BUTTON_REBOOT = "button_reboot"

DEVICE_HOSTNAME = "hostname"
DEVICE_IP = "ip"
DEVICE_MAC = "mac"
DEVICE_UPLOAD_SPEED = "upload_speed"
DEVICE_DOWNLOAD_SPEED = "download_speed"
DEVICE_SIGNAL = "signal"
DEVICE_ONLINE_TIME = "online_time"
DEVICE_CONNECTION_TYPE = "connection_type"

ICON_INFO_WORK_MODE = "mdi:router-wireless"
ICON_INFO_INTERFACE = "mdi:router-network"
ICON_SYSTEM_FIRMWARE_VERSION = "mdi:numeric"
ICON_SYSTEM_HARDWARE = "mdi:chip"
ICON_SYSTEM_MODEL = "mdi:tag-text"
ICON_SYSTEM_UPTIME = "mdi:clock-check"
ICON_SYSTEM_LOCALTIME = "mdi:clock-check"
ICON_MESH_NETWORK = "mdi:table-network"
ICON_MESH_UNITS = "mdi:server-network"
ICON_WAN_PUBLIC_IP = "mdi:web"
ICON_WAN_IP = "mdi:ip-network"
ICON_WAN_DNS = "mdi:dns"
ICON_WAN_TYPE = "mdi:transit-connection-variant"
ICON_WAN_GATEWAY = "mdi:gate-open"
ICON_WAN_UPTIME = "mdi:clock-check"
ICON_LAN_IP = "mdi:lan"
ICON_LAN_SUBNET = "mdi:network"
ICON_LAN_MAC = "mdi:network-pos"
ICON_24G_WIFI_SSID = "mdi:router-wireless"
ICON_24G_WIFI_BSSID = "mdi:router-wireless-settings"
ICON_24G_WIFI_ENCRYPTION = "mdi:key-wireless"
ICON_24G_WIFI_CHANNEL = "mdi:access-point"
ICON_5G_WIFI_SSID = "mdi:router-wireless"
ICON_5G_WIFI_BSSID = "mdi:router-wireless-settings"
ICON_5G_WIFI_ENCRYPTION = "mdi:key-wireless"
ICON_5G_WIFI_CHANNEL = "mdi:access-point"
ICON_DEVICE_COUNT = "mdi:devices"
ICON_WIFI_24_DEVICE_COUNT = "mdi:wifi"
ICON_WIFI_5_DEVICE_COUNT = "mdi:wifi-star"
ICON_WIRED_DEVICE_COUNT = "mdi:connection"
ICON_MESH_DEVICE_COUNT = "mdi:table-network"
ICON_DEVICE_ONLINE = "mdi:network"
ICON_DEVICE_BLOCKED = "mdi:network-off"
ICON_DHCP_IP_START = "mdi:ray-start-arrow"
ICON_DHCP_IP_END = "mdi:ray-end-arrow"
ICON_DHCP_DNS_PRIMARY = "mdi:dns"
ICON_DHCP_DNS_SECONDARY = "mdi:dns-outline"
ICON_DHCP_GATEWAY = "mdi:gate-open"
ICON_DHCP_LEASE_TIME = "mdi:clock-time-seven"
ICON_GSM_NETWORK_TYPE = "mdi:transit-connection-variant"
ICON_GSM_DOWNLOAD = "mdi:download"
ICON_GSM_UPLOAD = "mdi:upload"
ICON_GSM_PUBLIC_IP = "mdi:web"
ICON_GSM_IP_ADDRESS = "mdi:ip-network"
ICON_GSM_CONNECTED_TIME = "mdi:clock-check"
ICON_SMS_INBOX = "mdi:inbox-arrow-down"
ICON_SMS_OUTBOX = "mdi:inbox-arrow-up"

SENSORS = {
    MODULE_SYSTEM: [
        {
            SENSORS_KEY_KEY: SENSOR_SYSTEM_MODEL,
            SENSORS_KEY_DESCRIPTION: [ "Model", "Model Name" ],
            SENSORS_KEY_ICON: "mdi:tag-text",
            SENSORS_KEY_CATEGORY: EntityCategory.DIAGNOSTIC,
            SENSORS_KEY_CLASS: None
        },
        {
            SENSORS_KEY_KEY: SENSOR_SYSTEM_FIRMWARE_VERSION,
            SENSORS_KEY_DESCRIPTION: ["Firmware Version", "Firmware"],
            SENSORS_KEY_ICON: "mdi:numeric",
            SENSORS_KEY_CATEGORY: EntityCategory.DIAGNOSTIC,
            SENSORS_KEY_CLASS: None
        },
        {
            SENSORS_KEY_KEY: SENSOR_SYSTEM_HARDWARE,
            SENSORS_KEY_DESCRIPTION: ["Hardware"],
            SENSORS_KEY_ICON: "mdi:chip",
            SENSORS_KEY_CATEGORY: EntityCategory.DIAGNOSTIC,
            SENSORS_KEY_CLASS: None
        },
        {
            SENSORS_KEY_KEY: SENSOR_SYSTEM_UPTIME,
            SENSORS_KEY_DESCRIPTION: ["Uptime", "Connected Time", "System Uptime"],
            SENSORS_KEY_ICON: "mdi:clock-check",
            SENSORS_KEY_CATEGORY: EntityCategory.DIAGNOSTIC,
            SENSORS_KEY_CLASS: None
        },
        {
            SENSORS_KEY_KEY: SENSOR_SYSTEM_LOCALTIME,
            SENSORS_KEY_DESCRIPTION: ["Local Time", "Localtime", "Time"],
            SENSORS_KEY_ICON: "mdi:clock-check",
            SENSORS_KEY_CATEGORY: EntityCategory.DIAGNOSTIC,
            SENSORS_KEY_CLASS: None
        },
    ],
    MODULE_LAN: [
        {
            SENSORS_KEY_KEY: SENSOR_LAN_IP,
            SENSORS_KEY_DESCRIPTION: ["IP Address", "LAN IP Address", "LAN IP"],
            SENSORS_KEY_ICON: "mdi:lan",
            SENSORS_KEY_CATEGORY: EntityCategory.DIAGNOSTIC,
            SENSORS_KEY_CLASS: None
        },
        {
            SENSORS_KEY_KEY: SENSOR_LAN_SUBNET,
            SENSORS_KEY_DESCRIPTION: ["Subnet Mask", "Subnet"],
            SENSORS_KEY_ICON: "mdi:network",
            SENSORS_KEY_CATEGORY: EntityCategory.DIAGNOSTIC,
            SENSORS_KEY_CLASS: None
        },
        {
            SENSORS_KEY_KEY: SENSOR_LAN_MAC,
            SENSORS_KEY_DESCRIPTION: ["MAC-Address", "MAC Address", "MAC"],
            SENSORS_KEY_ICON: "mdi:network-pos",
            SENSORS_KEY_CATEGORY: EntityCategory.DIAGNOSTIC,
            SENSORS_KEY_CLASS: None
        },
    ],
    MODULE_MESH: [
        {
            SENSORS_KEY_KEY: SENSOR_MESH_NETWORK,
            SENSORS_KEY_DESCRIPTION: ["Mesh Network", "Mesh", "Device Name"],
            SENSORS_KEY_ICON: "mdi:table-network",
            SENSORS_KEY_CATEGORY: EntityCategory.DIAGNOSTIC,
            SENSORS_KEY_CLASS: None
        },
        {
            SENSORS_KEY_KEY: SENSOR_MESH_UNITS,
            SENSORS_KEY_DESCRIPTION: ["Mesh Units", "Units"],
            SENSORS_KEY_ICON: "mdi:server-network",
            SENSORS_KEY_CATEGORY: EntityCategory.DIAGNOSTIC,
            SENSORS_KEY_CLASS: None
        },
        {
            SENSORS_KEY_KEY: SENSOR_DEVICE_MESH_COUNT,
            SENSORS_KEY_DESCRIPTION: ["Mesh Devices", "Mesh Devices Connected", "Mesh Node Count"],
            SENSORS_KEY_ICON: "mdi:server-plus",
            SENSORS_KEY_CATEGORY: None,
            SENSORS_KEY_CLASS: SensorStateClass.MEASUREMENT
        },
    ],
    MODULE_WAN: [
        {
            SENSORS_KEY_KEY: SENSOR_WAN_TYPE,
            SENSORS_KEY_DESCRIPTION: ["Protocol", "Connection Type", "Type"],
            SENSORS_KEY_ICON: "mdi:transit-connection-variant",
            SENSORS_KEY_CATEGORY: EntityCategory.DIAGNOSTIC,
            SENSORS_KEY_CLASS: None
        },
        {
            SENSORS_KEY_KEY: SENSOR_WAN_IP,
            SENSORS_KEY_DESCRIPTION: ["IP Address", "WAN IP", "Public IP"],
            SENSORS_KEY_ICON: "mdi:network",
            SENSORS_KEY_CATEGORY: EntityCategory.DIAGNOSTIC,
            SENSORS_KEY_CLASS: None
        },
        {
            SENSORS_KEY_KEY: SENSOR_WAN_GATEWAY,
            SENSORS_KEY_DESCRIPTION: ["Gateway", "Default Gateway"],
            SENSORS_KEY_ICON: "mdi:gate-open",
            SENSORS_KEY_CATEGORY: EntityCategory.DIAGNOSTIC,
            SENSORS_KEY_CLASS: None
        },
        {
            SENSORS_KEY_KEY: SENSOR_WAN_UPTIME,
            SENSORS_KEY_DESCRIPTION: ["Connected Time", "Uptime"],
            SENSORS_KEY_ICON: "mdi:clock-check",
            SENSORS_KEY_CATEGORY: EntityCategory.DIAGNOSTIC,
            SENSORS_KEY_CLASS: None
        },
        {
            SENSORS_KEY_KEY: SENSOR_WAN_DNS,
            SENSORS_KEY_DESCRIPTION: ["DNS", "DNS Server", "DNS Address", "DNS Addresses"],
            SENSORS_KEY_ICON: "mdi:dns",
            SENSORS_KEY_CATEGORY: EntityCategory.DIAGNOSTIC,
            SENSORS_KEY_CLASS: None
        },
    ],
    MODULE_WAN_SECONDARY: [
        {
            SENSORS_KEY_KEY: SENSOR_WAN_TYPE,
            SENSORS_KEY_DESCRIPTION: ["Protocol", "Connection Type", "Type"],
            SENSORS_KEY_ICON: "mdi:transit-connection-variant",
            SENSORS_KEY_CATEGORY: EntityCategory.DIAGNOSTIC,
            SENSORS_KEY_CLASS: None
        },
        {
            SENSORS_KEY_KEY: SENSOR_WAN_IP,
            SENSORS_KEY_DESCRIPTION: ["IP Address", "WAN IP", "Public IP"],
            SENSORS_KEY_ICON: "mdi:network",
            SENSORS_KEY_CATEGORY: EntityCategory.DIAGNOSTIC,
            SENSORS_KEY_CLASS: None
        },
        {
            SENSORS_KEY_KEY: SENSOR_WAN_GATEWAY,
            SENSORS_KEY_DESCRIPTION: ["Gateway", "Default Gateway"],
            SENSORS_KEY_ICON: "mdi:gate-open",
            SENSORS_KEY_CATEGORY: EntityCategory.DIAGNOSTIC,
            SENSORS_KEY_CLASS: None
        },
        {
            SENSORS_KEY_KEY: SENSOR_WAN_UPTIME,
            SENSORS_KEY_DESCRIPTION: ["Connected Time", "Uptime"],
            SENSORS_KEY_ICON: "mdi:clock-check",
            SENSORS_KEY_CATEGORY: EntityCategory.DIAGNOSTIC,
            SENSORS_KEY_CLASS: None
        },
        {
            SENSORS_KEY_KEY: SENSOR_WAN_DNS,
            SENSORS_KEY_DESCRIPTION: ["DNS", "DNS Server", "DNS Address", "DNS Addresses"],
            SENSORS_KEY_ICON: "mdi:dns",
            SENSORS_KEY_CATEGORY: EntityCategory.DIAGNOSTIC,
            SENSORS_KEY_CLASS: None
        },
    ],
    MODULE_MULTI_WAN: [
        {
            SENSORS_KEY_KEY: SENSOR_WAN_MODE,
            SENSORS_KEY_DESCRIPTION: ["Mode", "Load Balancing"],
            SENSORS_KEY_ICON: "mdi:multicast",
            SENSORS_KEY_CATEGORY: EntityCategory.DIAGNOSTIC,
            SENSORS_KEY_CLASS: None
        },
    ],
    MODULE_DHCP: [
        {
            SENSORS_KEY_KEY: SENSOR_DHCP_IP_START,
            SENSORS_KEY_DESCRIPTION: ["IP Start", "Start IP", "Start"],
            SENSORS_KEY_ICON: "mdi:ray-start-arrow",
            SENSORS_KEY_CATEGORY: EntityCategory.DIAGNOSTIC,
            SENSORS_KEY_CLASS: None
        },
        {
            SENSORS_KEY_KEY: SENSOR_DHCP_IP_END,
            SENSORS_KEY_DESCRIPTION: ["IP End", "End IP", "End"],
            SENSORS_KEY_ICON: "mdi:ray-end-arrow",
            SENSORS_KEY_CATEGORY: EntityCategory.DIAGNOSTIC,
            SENSORS_KEY_CLASS: None
        },
        {
            SENSORS_KEY_KEY: SENSOR_DHCP_DNS_PRIMARY,
            SENSORS_KEY_DESCRIPTION: ["Preferred DNS", "Primary DNS", "DNS Server"],
            SENSORS_KEY_ICON: "mdi:dns",
            SENSORS_KEY_CATEGORY: EntityCategory.DIAGNOSTIC,
            SENSORS_KEY_CLASS: None
        },
        {
            SENSORS_KEY_KEY: SENSOR_DHCP_DNS_SECONDARY,
            SENSORS_KEY_DESCRIPTION: ["Alternate DNS", "Secondary DNS", "Alternate DNS"],
            SENSORS_KEY_ICON: "mdi:dns-outline",
            SENSORS_KEY_CATEGORY: EntityCategory.DIAGNOSTIC,
            SENSORS_KEY_CLASS: None
        },
        {
            SENSORS_KEY_KEY: SENSOR_DHCP_GATEWAY,
            SENSORS_KEY_DESCRIPTION: ["Default Gateway", "Gateway"],
            SENSORS_KEY_ICON: "mdi:gate-open",
            SENSORS_KEY_CATEGORY: EntityCategory.DIAGNOSTIC,
            SENSORS_KEY_CLASS: None
        },
        {
            SENSORS_KEY_KEY: SENSOR_DHCP_LEASE_TIME,
            SENSORS_KEY_DESCRIPTION: ["Leasetime", "Lease Time", "Lease"],
            SENSORS_KEY_ICON: "mdi:clock-time-seven",
            SENSORS_KEY_CATEGORY: EntityCategory.DIAGNOSTIC,
            SENSORS_KEY_CLASS: None
        },
    ],
    MODULE_WIRELESS_24G: [
        {
            SENSORS_KEY_KEY: SENSOR_24G_WIFI_SSID,
            SENSORS_KEY_DESCRIPTION: ["SSID"],
            SENSORS_KEY_ICON: "mdi:router-wireless",
            SENSORS_KEY_CATEGORY: EntityCategory.DIAGNOSTIC,
            SENSORS_KEY_CLASS: None
        },
        {
            SENSORS_KEY_KEY: SENSOR_24G_WIFI_BSSID,
            SENSORS_KEY_DESCRIPTION: ["BSSID"],
            SENSORS_KEY_ICON: "mdi:router-wireless-settings",
            SENSORS_KEY_CATEGORY: EntityCategory.DIAGNOSTIC,
            SENSORS_KEY_CLASS: None
        },
        {
            SENSORS_KEY_KEY: SENSOR_24G_WIFI_ENCRYPTION,
            SENSORS_KEY_DESCRIPTION: ["Encryption"],
            SENSORS_KEY_ICON: "mdi:key-wireless",
            SENSORS_KEY_CATEGORY: EntityCategory.DIAGNOSTIC,
            SENSORS_KEY_CLASS: None
        },
        {
            SENSORS_KEY_KEY: SENSOR_24G_WIFI_CHANNEL,
            SENSORS_KEY_DESCRIPTION: ["Channel"],
            SENSORS_KEY_ICON: "mdi:access-point",
            SENSORS_KEY_CATEGORY: None,
            SENSORS_KEY_CLASS: SensorStateClass.MEASUREMENT
        }
    ],
    MODULE_WIRELESS_5G: [
        {
            SENSORS_KEY_KEY: SENSOR_5G_WIFI_SSID,
            SENSORS_KEY_DESCRIPTION: ["SSID"],
            SENSORS_KEY_ICON: "mdi:router-wireless",
            SENSORS_KEY_CATEGORY: EntityCategory.DIAGNOSTIC,
            SENSORS_KEY_CLASS: None
        },
        {
            SENSORS_KEY_KEY: SENSOR_5G_WIFI_BSSID,
            SENSORS_KEY_DESCRIPTION: ["BSSID"],
            SENSORS_KEY_ICON: "mdi:router-wireless-settings",
            SENSORS_KEY_CATEGORY: EntityCategory.DIAGNOSTIC,
            SENSORS_KEY_CLASS: None
        },
        {
            SENSORS_KEY_KEY: SENSOR_5G_WIFI_ENCRYPTION,
            SENSORS_KEY_DESCRIPTION: ["Encryption"],
            SENSORS_KEY_ICON: "mdi:key-wireless",
            SENSORS_KEY_CATEGORY: EntityCategory.DIAGNOSTIC,
            SENSORS_KEY_CLASS: None
        },
        {
            SENSORS_KEY_KEY: SENSOR_5G_WIFI_CHANNEL,
            SENSORS_KEY_DESCRIPTION: ["Channel"],
            SENSORS_KEY_ICON: "mdi:access-point",
            SENSORS_KEY_CATEGORY: None,
            SENSORS_KEY_CLASS: SensorStateClass.MEASUREMENT
        }
    ],
    MODULE_WIRELESS_6G: [
        {
            SENSORS_KEY_KEY: SENSOR_6G_WIFI_SSID,
            SENSORS_KEY_DESCRIPTION: ["SSID"],
            SENSORS_KEY_ICON: "mdi:router-wireless",
            SENSORS_KEY_CATEGORY: EntityCategory.DIAGNOSTIC,
            SENSORS_KEY_CLASS: None
        },
        {
            SENSORS_KEY_KEY: SENSOR_6G_WIFI_BSSID,
            SENSORS_KEY_DESCRIPTION: ["BSSID"],
            SENSORS_KEY_ICON: "mdi:router-wireless-settings",
            SENSORS_KEY_CATEGORY: EntityCategory.DIAGNOSTIC,
            SENSORS_KEY_CLASS: None
        },
        {
            SENSORS_KEY_KEY: SENSOR_6G_WIFI_ENCRYPTION,
            SENSORS_KEY_DESCRIPTION: ["Encryption"],
            SENSORS_KEY_ICON: "mdi:key-wireless",
            SENSORS_KEY_CATEGORY: EntityCategory.DIAGNOSTIC,
            SENSORS_KEY_CLASS: None
        },
        {
            SENSORS_KEY_KEY: SENSOR_6G_WIFI_CHANNEL,
            SENSORS_KEY_DESCRIPTION: ["Channel"],
            SENSORS_KEY_ICON: "mdi:access-point",
            SENSORS_KEY_CATEGORY: None,
            SENSORS_KEY_CLASS: SensorStateClass.MEASUREMENT
        }
    ],
    MODULE_GSM: [
        {
            SENSORS_KEY_KEY: SENSOR_GSM_NETWORK_TYPE,
            SENSORS_KEY_DESCRIPTION: ["Network Type"],
            SENSORS_KEY_ICON: "mdi:transit-connection-variant",
            SENSORS_KEY_CATEGORY: EntityCategory.DIAGNOSTIC,
            SENSORS_KEY_CLASS: None
        },
        {
            SENSORS_KEY_KEY: SENSOR_GSM_DOWNLOAD,
            SENSORS_KEY_DESCRIPTION: ["Download"],
            SENSORS_KEY_ICON: "mdi:download",
            SENSORS_KEY_CATEGORY: EntityCategory.DIAGNOSTIC,
            SENSORS_KEY_CLASS: None
        },
        {
            SENSORS_KEY_KEY: SENSOR_GSM_UPLOAD,
            SENSORS_KEY_DESCRIPTION: ["Upload"],
            SENSORS_KEY_ICON: "mdi:upload",
            SENSORS_KEY_CATEGORY: EntityCategory.DIAGNOSTIC,
            SENSORS_KEY_CLASS: None
        },
        {
            SENSORS_KEY_KEY: SENSOR_GSM_PUBLIC_IP,
            SENSORS_KEY_DESCRIPTION: ["Public IP Address"],
            SENSORS_KEY_ICON: "mdi:web",
            SENSORS_KEY_CATEGORY: EntityCategory.DIAGNOSTIC,
            SENSORS_KEY_CLASS: None
        },
        {
            SENSORS_KEY_KEY: SENSOR_GSM_IP_ADDRESS,
            SENSORS_KEY_DESCRIPTION: ["IP Address", "IPv4 Address"],
            SENSORS_KEY_ICON: "mdi:checkbox-marked",
            SENSORS_KEY_CATEGORY: EntityCategory.DIAGNOSTIC,
            SENSORS_KEY_CLASS: None
        },
        {
            SENSORS_KEY_KEY: SENSOR_GSM_CONNECTED_TIME,
            SENSORS_KEY_DESCRIPTION: ["Connected Time"],
            SENSORS_KEY_ICON: "mdi:clock-check",
            SENSORS_KEY_CATEGORY: EntityCategory.DIAGNOSTIC,
            SENSORS_KEY_CLASS: None
        },
    ],
    MODULE_SMS: [
        {
            SENSORS_KEY_KEY: SENSOR_SMS_INBOX,
            SENSORS_KEY_DESCRIPTION: ["Inbox"],
            SENSORS_KEY_ICON: "mdi:inbox-arrow-down",
            SENSORS_KEY_CATEGORY: None,
            SENSORS_KEY_CLASS: SensorStateClass.MEASUREMENT
        },
        {
            SENSORS_KEY_KEY: SENSOR_SMS_OUTBOX,
            SENSORS_KEY_DESCRIPTION: ["Outbox"],
            SENSORS_KEY_ICON: "mdi:inbox-arrow-up",
            SENSORS_KEY_CATEGORY: None,
            SENSORS_KEY_CLASS: SensorStateClass.MEASUREMENT
        },
    ],
    MODULE_VPN: [
        {
            SENSORS_KEY_KEY: SENSOR_VPN_ENABLED,
            SENSORS_KEY_DESCRIPTION: ["Status", "Enabled", "VPN Status"],
            SENSORS_KEY_ICON: "mdi:checkbox-marked",
            SENSORS_KEY_CATEGORY: EntityCategory.DIAGNOSTIC,
            SENSORS_KEY_CLASS: None
        },
        {
            SENSORS_KEY_KEY: SENSOR_VPN_TUNNELS,
            SENSORS_KEY_DESCRIPTION: ["Tunnels", "Tunnel", "VPN Tunnels"],
            SENSORS_KEY_ICON: "mdi:tunnel",
            SENSORS_KEY_CATEGORY: EntityCategory.DIAGNOSTIC,
            SENSORS_KEY_CLASS: None
        },
    ],
    MODULE_USB: [
        {
            SENSORS_KEY_KEY: SENSOR_USB_TETHERING,
            SENSORS_KEY_DESCRIPTION: ["Connected", "Not connected"],
            SENSORS_KEY_ICON: "mdi:usb",
            SENSORS_KEY_CATEGORY: EntityCategory.DIAGNOSTIC,
            SENSORS_KEY_CLASS: None
        },
        {
            SENSORS_KEY_KEY: SENSOR_USB_SHARING,
            SENSORS_KEY_DESCRIPTION: ["Connected", "Not connected"],
            SENSORS_KEY_ICON: "mdi:usb-port",
            SENSORS_KEY_CATEGORY: EntityCategory.DIAGNOSTIC,
            SENSORS_KEY_CLASS: None
        },
    ],
    MODULE_DEVICES: [
        {
            SENSORS_KEY_KEY: SENSOR_DEVICE_COUNT,
            SENSORS_KEY_DESCRIPTION: ["Devices"],
            SENSORS_KEY_ICON: "mdi:devices",
            SENSORS_KEY_CATEGORY: None,
            SENSORS_KEY_CLASS: SensorStateClass.MEASUREMENT
        },
        {
            SENSORS_KEY_KEY: SENSOR_DEVICE_ONLINE,
            SENSORS_KEY_DESCRIPTION: ["Online", "Online Devices", "Connected"],
            SENSORS_KEY_ICON: "mdi:network",
            SENSORS_KEY_CATEGORY: None,
            SENSORS_KEY_CLASS: SensorStateClass.MEASUREMENT
        },
        {
            SENSORS_KEY_KEY: SENSOR_DEVICE_BLOCKED,
            SENSORS_KEY_DESCRIPTION: ["Blocked", "Blocked Devices"],
            SENSORS_KEY_ICON: "mdi:network-off",
            SENSORS_KEY_CATEGORY: None,
            SENSORS_KEY_CLASS: SensorStateClass.MEASUREMENT
        },
        {
            SENSORS_KEY_KEY: SENSOR_DEVICE_WIFI_24_COUNT,
            SENSORS_KEY_DESCRIPTION: ["2.4G WiFi"],
            SENSORS_KEY_ICON: "mdi:wifi",
            SENSORS_KEY_CATEGORY: None,
            SENSORS_KEY_CLASS: SensorStateClass.MEASUREMENT
        },
        {
            SENSORS_KEY_KEY: SENSOR_DEVICE_WIFI_5_COUNT,
            SENSORS_KEY_DESCRIPTION: ["5G WiFi"],
            SENSORS_KEY_ICON: "mdi:wifi-star",
            SENSORS_KEY_CATEGORY: None,
            SENSORS_KEY_CLASS: SensorStateClass.MEASUREMENT
        },
        {
            SENSORS_KEY_KEY: SENSOR_DEVICE_WIRED_COUNT,
            SENSORS_KEY_DESCRIPTION: ["Wired"],
            SENSORS_KEY_ICON: "mdi:connection",
            SENSORS_KEY_CATEGORY: None,
            SENSORS_KEY_CLASS: SensorStateClass.MEASUREMENT
        },
        {
            SENSORS_KEY_KEY: SENSOR_DEVICE_MESH_COUNT,
            SENSORS_KEY_DESCRIPTION: ["Mesh"],
            SENSORS_KEY_ICON: "mdi:table-network",
            SENSORS_KEY_CATEGORY: None,
            SENSORS_KEY_CLASS: SensorStateClass.MEASUREMENT
        },
    ],
}



MODULE_DEVICE_LIST = "device_list"

CUDY_DEVICES = [
    "AP11000",
    "AP1200",
    "AP1200-Outdoor",
    "AP1300",
    "AP1300-Outdoor",
    "AP1300D",
    "AP1300Wall",
    "AP3000",
    "AP3000-Outdoor",
    "AP3000D",
    "AP3000Wall",
    "AP3600",
    "C200P",
    "IR02",
    "IR04",
    "LT15E",
    "LT18",
    "LT300",
    "LT300V3",
    "LT400",
    "LT400-Outdoor",
    "LT400E",
    "LT400V",
    "LT500",
    "LT500-Outdoor",
    "LT500E",
    "LT700-Outdoor",
    "LT700E",
    "LT700V",
    "M11000",
    "M1200",
    "M1300",
    "M1500",
    "M1800",
    "M3000",
    "M3600",
    "P2",
    "P4",
    "P5",
    "R700",
    "RE1200",
    "RE1200-Outdoor",
    "RE1500",
    "RE1800",
    "RE3000",
    "RE3600",
    "TR1200",
    "TR3000",
    "WR11000",
    "WR1200",
    "WR1200E",
    "WR1300",
    "WR1300E",
    "WR1300EV2",
    "WR1300S",
    "WR1300V4.0",
    "WR1500",
    "WR300",
    "WR3000",
    "WR3000E",
    "WR3000P",
    "WR3000S",
    "WR300S",
    "WR3600",
    "WR3600E",
    "WR3600H",
    "WR6500",
    "WR6500H",
    "X6",
]

CAPABILITY_URLS = {
    MODULE_SYSTEM: [
        "/admin/system/status?detail=1",
        "/admin/system/status/detail/1",
    ],
    MODULE_LAN: [
        "/admin/network/lan/status?detail=1",
    ],
    MODULE_DHCP: [
        "/admin/services/dhcp/status?detail=1",
    ],
    MODULE_DEVICES: [
        "/admin/network/devices/status?detail=1",
    ],
    MODULE_WAN: [
        "/admin/network/wan/iface/wan/status?detail=1",
        "/admin/network/wan/status?detail=1",
    ],
    MODULE_WAN_SECONDARY: [
        "/admin/network/wan/iface/wand/status?detail=1",
    ],
    MODULE_MULTI_WAN: [
        "/admin/network/mwan3/status?detail=1",
    ],
    MODULE_MESH: [
        "/admin/network/mesh/status?detail=1",
    ],
    MODULE_VPN: [
        "/admin/network/vpn/status?detail=1",
    ],
    MODULE_WIRELESS_5G: [
        "/admin/network/wireless/status?detail=1&iface=wlan10",
    ],
    MODULE_WIRELESS_24G: [
        "/admin/network/wireless/status?detail=1&iface=wlan00",
    ],
    MODULE_WIRELESS_6G: [
        "/admin/network/wireless/status?detail=1&iface=wlan20",
    ],
    MODULE_GSM: [
        "/admin/network/gcom/iface/4g/status?detail=1",
    ],
    MODULE_SMS: [
        "/admin/network/gcom/sms/iface/4g/status?detail=1",
    ],
    MODULE_USB: [
        "/admin/services/usb/status?detail=1",
    ],
    MODULE_DEVICE_LIST: [
        "/admin/network/devices/devlist?detail=1",
    ],
}
