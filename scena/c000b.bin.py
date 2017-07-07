from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c000b.bin",                # FileName
        "c000b",                    # MapName
        "c000b",                    # Location
        0x0002,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0, 1],
    )

    BuildStringList((
        "c000b",                  # 0
        "Central square",               # 1
        "Nishi dori",                 # 2
        "Administrative district",                 # 3
        "Residential area",                 # 4
        "Entertainment district",                 # 5
        "East Street",                 # 6
        "old Town",                 # 7
        "Harbor district",                 # 8
        "IBC",                 # 9
        "Beside the station",               # 10
        "Back street",                 # 11
        "Ursula interchange",           # 12
        "East Crossbell Highway",       # 13
        "West Crossbell Highway",       # 14
        "Mainz Mountain Road",           # 15
        "Orchis Tower",         # 16
    ))

    PlaceName(-9.25, 0.0, 67.0, 0x0000, 0x0000, "Central square")
    PlaceName(-75.0, 0.0, 71.5, 0x0000, 0x0000, "Nishi dori")
    PlaceName(17.75, 0.0, 156.0, 0x0000, 0x0000, "Administrative district")
    PlaceName(-136.0, 0.0, 146.0, 0x0000, 0x0000, "Residential area")
    PlaceName(-63.0, 0.0, 138.0, 0x0000, 0x0000, "Entertainment district")
    PlaceName(72.0, 0.0, 44.0, 0x0000, 0x0000, "East Street")
    PlaceName(107.5, 0.0, -11.0, 0x0000, 0x0000, "old Town")
    PlaceName(100.0, 0.0, 110.0, 0x0000, 0x0000, "Harbor district")
    PlaceName(74.0, 0.0, 204.0, 0x0000, 0x0000, "IBC")
    PlaceName(2.0, 0.0, -2.0, 0x0000, 0x0000, "Beside the station")
    PlaceName(-45.0, 0.0, 102.0, 0x0000, 0x0000, "Back street")
    PlaceName(-1.0, 0.0, -33.0, 0x0000, 0x0000, "Ursula interchange")
    PlaceName(126.0, 0.0, 58.0, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-126.0, 0.0, 70.0, 0x0000, 0x0000, "West Crossbell Highway")
    PlaceName(-120.0, 0.0, 170.0, 0x0000, 0x0000, "Mainz Mountain Road")
    PlaceName(11.0, 0.0, 286.0, 0x0000, 0x0000, "Orchis Tower")
    PlaceName(-31.25, 0.0, 53.0, 0x0000, 0x0051, "")
    PlaceName(22.5, 0.0, 79.0, 0x0000, 0x0054, "")
    PlaceName(-6.75, 0.0, 45.0, 0x0000, 0x0057, "")
    PlaceName(-32.0, 0.0, 82.0, 0x0000, 0x0053, "")
    PlaceName(-11.5, 0.0, 106.0, 0x0000, 0x0053, "")
    PlaceName(-62.25, 0.0, 77.0, 0x0000, 0x0053, "")
    PlaceName(-72.0, 0.0, 98.0, 0x0000, 0x0053, "")
    PlaceName(-48.0, 0.0, 130.0, 0x0000, 0x0052, "")
    PlaceName(-43.25, 0.0, 117.0, 0x0000, 0x0053, "")
    PlaceName(-34.5, 0.0, 108.5, 0x0000, 0x0053, "")
    PlaceName(-6.0, 0.0, 179.5, 0x0000, 0x0051, "")
    PlaceName(106.0, 0.0, 44.0, 0x0000, 0x0052, "")
    PlaceName(89.0, 0.0, -46.5, 0x0000, 0x0053, "")
    PlaceName(76.0, 0.0, -28.0, 0x0000, 0x0053, "")

    ChipFrameInfo(756, 0)                                        # 0

    ScpFunction((
        "Function_0_2F4",          # 00, 0
        "Function_1_2F5",          # 01, 1
    ))


    def Function_0_2F4(): pass

    label("Function_0_2F4")

    Return()

    # Function_0_2F4 end

    def Function_1_2F5(): pass

    label("Function_1_2F5")

    Return()

    # Function_1_2F5 end

    SaveToFile()

Try(main)
