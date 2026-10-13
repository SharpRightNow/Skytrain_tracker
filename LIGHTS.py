# AI GENERATED

# Canada Line segments keyed by TransLink GTFS platform stop_ids (location_type = 0).
#
# Verified against stop_times.txt (route 13686, Canada Line): every consecutive stop pair
# in the scheduled trips has an entry here, and nothing else.
# Waterfront-bound trips (direction_id 0) use the "toward Waterfront" entries; outbound
# trips (direction_id 1, to Richmond-Brighouse / YVR-Airport) use the "away" entries.
# Each segment has one entry per direction, with the same light count.

LIGHTS = {
    # ("start_stop_id", "end_stop_id"): light_count,

    # Waterfront <-> Vancouver City Centre
    ("11273", "11303"): 3,   # toward Waterfront
    ("11302", "11272"): 3,   # away from Waterfront

    # Vancouver City Centre <-> Yaletown-Roundhouse
    ("11275", "11273"): 1,   # toward Waterfront
    ("11272", "11274"): 1,   # away from Waterfront

    # Yaletown-Roundhouse <-> Olympic Village
    ("11277", "11275"): 4,   # toward Waterfront
    ("11274", "11276"): 4,   # away from Waterfront

    # Olympic Village <-> Broadway-City Hall
    ("11279", "11277"): 0,   # toward Waterfront
    ("11276", "11278"): 0,   # away from Waterfront

    # Broadway-City Hall <-> King Edward
    ("11281", "11279"): 2,   # toward Waterfront
    ("11278", "11280"): 2,   # away from Waterfront

    # King Edward <-> Oakridge-41st Avenue
    ("11283", "11281"): 5,   # toward Waterfront
    ("11280", "11282"): 5,   # away from Waterfront

    # Oakridge-41st Avenue <-> Langara-49th Avenue
    ("11285", "11283"): 1,   # toward Waterfront
    ("11282", "11284"): 1,   # away from Waterfront

    # Langara-49th Avenue <-> Marine Drive
    ("11287", "11285"): 3,   # toward Waterfront
    ("11284", "11286"): 3,   # away from Waterfront

    # Marine Drive <-> Bridgeport
    ("11289", "11287"): 2,   # toward Waterfront
    ("11286", "11288"): 2,   # away from Waterfront

    # Bridgeport <-> Capstan
    ("12946", "11289"): 2,   # toward Waterfront
    ("11288", "12947"): 2,   # away from Waterfront

    # Capstan <-> Aberdeen
    ("11291", "12946"): 3,   # toward Waterfront
    ("12947", "11290"): 3,   # away from Waterfront

    # Aberdeen <-> Lansdowne
    ("11293", "11291"): 0,   # toward Waterfront
    ("11290", "11292"): 0,   # away from Waterfront

    # Lansdowne <-> Richmond-Brighouse
    ("11295", "11293"): 5,   # toward Waterfront
    ("11292", "11294"): 5,   # away from Waterfront

    # Bridgeport <-> Templeton
    ("11297", "11289"): 1,   # toward Waterfront
    ("11288", "11296"): 1,   # away from Waterfront

    # Templeton <-> Sea Island Centre
    ("11299", "11297"): 2,   # toward Waterfront
    ("11296", "11298"): 2,   # away from Waterfront

    # Sea Island Centre <-> YVR-Airport
    ("11301", "11299"): 3,   # toward Waterfront
    ("11298", "11300"): 3,   # away from Waterfront

}