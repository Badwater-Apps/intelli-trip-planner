#!/usr/bin/env python

"""
Load answer keys for testing
"""


def load_parsed_distance_matrix_tuple() -> dict:
    """
    Load parsed distance matrix as answer key
    """
    # current_dir: str = os.path.dirname(os.path.abspath(__file__))
    # json_file: str = os.path.join(
    #     current_dir, "mock_data", "parsed_distance_matrix.json"
    # )
    # with open(json_file, "r") as read_file:
    #     distance_matrix_json: dict = json.load(read_file)
    # parsed_distance_matrix = {
    #     "distance": tuple(map(tuple, distance_matrix_json["distance"])),
    #     "duration": tuple(map(tuple, distance_matrix_json["duration"])),
    # }
    # return parsed_distance_matrix

    return {
        "distance": (
            (
                0,
                452812,
                192690,
                144369,
                311544,
                604974,
                269142,
                431026,
                438044,
                447211,
            ),
            (
                451120,
                0,
                437724,
                366440,
                229653,
                338302,
                715338,
                877222,
                884240,
                816997,
            ),
            (
                191247,
                435684,
                0,
                238990,
                405970,
                515548,
                469067,
                630950,
                637969,
                632563,
            ),
            (
                141782,
                365989,
                238765,
                0,
                167175,
                518151,
                406001,
                567884,
                574902,
                496696,
            ),
            (
                309863,
                227823,
                406651,
                168080,
                0,
                494206,
                574081,
                735965,
                742983,
                613004,
            ),
            (
                603285,
                336174,
                517201,
                518604,
                494847,
                0,
                867503,
                1029387,
                1036405,
                969162,
            ),
            (
                268459,
                714826,
                468458,
                406383,
                573558,
                866987,
                0,
                136765,
                196587,
                541398,
            ),
            (
                430493,
                876860,
                630491,
                568416,
                735592,
                1029021,
                137043,
                0,
                254873,
                599684,
            ),
            (
                437353,
                883719,
                637351,
                575276,
                742451,
                1035881,
                196616,
                254531,
                0,
                477064,
            ),
            (
                445127,
                816114,
                632335,
                496453,
                598105,
                968276,
                536307,
                594223,
                477601,
                0,
            ),
        ),
        "duration": (
            (0, 15264, 7728, 5159, 11562, 22011, 10044, 15067, 16954, 15614),
            (15059, 0, 16392, 12581, 8425, 13233, 24597, 29619, 31506, 28133),
            (7639, 16665, 0, 8987, 15333, 20726, 16839, 21862, 23748, 22951),
            (4887, 12596, 8805, 0, 6403, 19342, 14424, 19447, 21334, 17878),
            (11235, 8357, 15117, 6349, 0, 18996, 20773, 25796, 27682, 21531),
            (21761, 13096, 20604, 19283, 18997, 0, 31299, 36321, 38208, 34834),
            (9990, 24740, 16714, 14634, 21037, 31486, 0, 6617, 9845, 20924),
            (14867, 29617, 21591, 19512, 25915, 36364, 6643, 0, 11351, 22429),
            (16806, 31556, 23530, 21451, 27854, 38303, 9818, 11284, 0, 18581),
            (15202, 27941, 22645, 17695, 21465, 34688, 20836, 22301, 18618, 0),
        ),
    }


def load_parsed_distance_matrix_list() -> dict:
    """
    Load parsed distance matrix (list) as answer key
    """
    distance_matrix = load_parsed_distance_matrix_tuple()
    return {
        "distance": list(map(list, distance_matrix["distance"])),
        "duration": list(map(list, distance_matrix["duration"])),
    }
