"""
Example passive DNS Common Output Format]() parser.
It will parse the JSON file and validate it.

Author: Aaron Kaplan <aaron@lo-res.org>
Copyright 2021, all rights reserved.

License: AGPL v3. See https://www.gnu.org/licenses/agpl-3.0.en.html
"""

import sys
import json         # maybe use an ndjson library...


def is_valid(d: dict) -> bool:
    # Check MANDATORY fields according to COF
    if "rrname" not in d:
        print("Missing MANDATORY field 'rrname'", file=sys.stderr)
        return False
    if not isinstance(d['rrname'], str):
        print("Type error: 'rrname' is not a JSON string", file=sys.stderr)
        return False
    if "rrtype" not in d:
        print("Missing MANDATORY field 'rrtype'", file=sys.stderr)
        return False
    if not isinstance(d['rrtype'], str):
        print("Type error: 'rrtype' is not a JSON string", file=sys.stderr)
        return False
    if "rdata" not in d:
        print("Missing MANDATORY field 'rdata'", file=sys.stderr)
        return False
    if "rdata" not in d:
        print("Missing MANDATORY field 'rdata'", file=sys.stderr)
        return False
    if not isinstance(d['rdata'], str) and not isinstance(d['rdata'], list):
        print("'rdata' is not a list and not a string.", file=sys.stderr)
        return False
    if not ("time_first" in d and "time_last" in d) or ("zone_time_first" in d and "zone_time_last" in d):
        print("We are missing EITHER ('first_seen' and 'last_seen') OR ('zone_time_first' and zone_time_last') fields")
        return False
    # currently we don't check the OPTIONAL fields. Sorry... to be done later.
    return True


def parse_line(input: str) -> dict:
    d = None
    try:
        d = json.loads(input)
        if not is_valid(d):
            print("Warning: line %s does not conform to the COF standard." % input)
    except Exception as ex:
        print("error. Could not parse input '%s'. Reason: '%s'" %(input, str(ex)), file=sys.stderr)
    return d


def parse_lines(multilines: str):
    for line in multilines.split('\n'):
        yield parse_line(line)


if __name__ == "__main__":
    mock_input = """{"count":1909,"rdata":["cpa.circl.lu"],"rrname":"www.circl.lu","rrtype":"CNAME","time_first":"1315586409","time_last":"1449566799"}
{"count":2560,"rdata":["cpab.circl.lu"],"rrname":"www.circl.lu","rrtype":"CNAME","time_first":"1449584660","time_last":"1617676151"}"""

    for result in parse_lines(mock_input):
        print("result: %r" % result)
