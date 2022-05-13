"""Tool to update DNS records in Cloudflare."""

import logging
import sys
from argparse import ArgumentParser

from argparse_logging import add_logging_arguments

from dyndns import (
    OauthAccessToken,
    get_cloudflare_state,
    infer_ip_address,
    update_record,
)

log = logging.getLogger()


parser = ArgumentParser()
parser.add_argument("record", help="Record to update")
parser.add_argument("zone", help="DNS zone to manipulate")
parser.add_argument(
    "--token", required=True, type=OauthAccessToken, help="Oauth2 access token"
)
add_logging_arguments(parser)
args = parser.parse_args()


ip = infer_ip_address()
log.debug(f"Current IP address is {ip}")
zone_id, record_id, record_ip = get_cloudflare_state(args.zone, args.record)
log.debug(f"Cloudflare ZoneID: {zone_id}")
log.debug(f"Cloudflare RecordID: {record_id}")
log.debug(f"Currently targeted IP: {record_ip}")
if ip == record_ip:
    log.info("Record is up-to-date, nothing to do here.")
    sys.exit(0)
log.info(f"Updating {args.record}.{args.zone} from {record_ip} to {ip}")
update_record(zone_id, record_id, args.record, ip)
