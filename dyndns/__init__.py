import requests
from urllib_ext.parse import urlparse

API = urlparse("https://api.cloudflare.com/client/v4/")
CLOUDFLARE_HEADERS = {
    "Content-Type": "application/json",
}


def OauthAccessToken(oauth2_access_token: str) -> None:
    CLOUDFLARE_HEADERS["Authorization"] = "Bearer " + oauth2_access_token
    resp = requests.get(API / "user/tokens/verify", headers=CLOUDFLARE_HEADERS).json()
    assert resp["success"], f"Failed to authenticate to Cloudflare.\n{resp}"


def infer_ip_address():
    return requests.get("https://ipv4.icanhazip.com").text.strip()


def get_zone_id(zone: str) -> str:
    resp = requests.get(
        API / "zones", headers=CLOUDFLARE_HEADERS, params={"name": zone}
    ).json()
    assert resp["success"], f"Failed to read DNS zone from Cloudflare.\n{resp}"
    return resp["result"][0]["id"]


def get_cloudflare_state(zone: str, record: str) -> tuple[str, str, str]:
    """Fetch the ZoneID, RecordID, and current target IP address."""
    zone_id = get_zone_id(zone)
    resp = requests.get(
        API / "zones" / zone_id / "dns_records",
        headers=CLOUDFLARE_HEADERS,
        params={type: "A", "name": f"{record}.{zone}"},
    ).json()
    assert resp["success"], f"Failed to read DNS record from Cloudflare.\n{resp}"
    record = resp["result"][0]
    return zone_id, record["id"], record["content"]


def update_record(zone_id: str, record_id: str, record: str, ip: str) -> None:
    resp = requests.put(
        API / "zones" / zone_id / "dns_records" / record_id,
        headers=CLOUDFLARE_HEADERS,
        json={
            "id": zone_id,
            "type": "A",
            "name": record,
            "content": ip,
        },
    )
    assert resp["success"], f"Failed to update DNS record on Cloudflare.\n{resp}"
