from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c050b.bin",                # FileName
        "c050b",                    # MapName
        "c050b",                    # Location
        0x0026,                     # MapIndex
        "ed7117",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 38, 0, 0, 0, 1],
    )

    BuildStringList((
        "c050b",                  # 0
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

    PlaceName(79.5, 0.0, -9.0, 0x0000, 0x0000, "Central square")
    PlaceName(0.0, 0.0, -76.5, 0x0000, 0x0000, "Nishi dori")
    PlaceName(11.0, 0.0, 116.0, 0x0000, 0x0000, "Administrative district")
    PlaceName(-148.0, 0.0, -60.0, 0x0000, 0x0000, "Residential area")
    PlaceName(-57.25, 0.0, 10.0, 0x0000, 0x0000, "Entertainment district")
    PlaceName(196.0, 0.0, 56.0, 0x0000, 0x0000, "East Street")
    PlaceName(294.0, 0.0, 31.0, 0x0000, 0x0000, "old Town")
    PlaceName(154.0, 0.0, 158.0, 0x0000, 0x0000, "Harbor district")
    PlaceName(20.0, 0.0, 233.0, 0x0000, 0x0000, "IBC")
    PlaceName(168.0, 0.0, -73.0, 0x0000, 0x0000, "Beside the station")
    PlaceName(1.0, 0.0, -9.0, 0x0000, 0x0000, "Back street")
    PlaceName(200.0, 0.0, -112.0, 0x0000, 0x0000, "Ursula interchange")
    PlaceName(240.0, 0.0, 130.0, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-52.0, 0.0, -134.0, 0x0000, 0x0000, "West Crossbell Highway")
    PlaceName(-156.0, 0.0, -17.0, 0x0000, 0x0000, "Mainz Mountain Road")
    PlaceName(-140.0, 0.0, 255.0, 0x0000, 0x0000, "Orchis Tower")
    PlaceName(71.0, 0.0, -49.0, 0x0000, 0x0051, "")
    PlaceName(100.5, 0.0, 38.5, 0x0000, 0x0054, "")
    PlaceName(106.0, 0.0, -31.0, 0x0000, 0x0057, "")
    PlaceName(38.0, 0.0, -18.5, 0x0000, 0x0053, "")
    PlaceName(35.5, 0.0, 32.0, 0x0000, 0x0053, "")
    PlaceName(9.0, 0.0, -57.0, 0x0000, 0x0053, "")
    PlaceName(-23.5, 0.0, -45.0, 0x0000, 0x0053, "")
    PlaceName(-33.0, 0.0, 16.0, 0x0000, 0x0052, "")
    PlaceName(-15.0, 0.0, 8.0, 0x0000, 0x0053, "")
    PlaceName(6.0, 0.0, 8.0, 0x0000, 0x0053, "")
    PlaceName(-41.0, 0.0, 118.0, 0x0000, 0x0051, "")
    PlaceName(233.0, 0.0, 91.0, 0x0000, 0x0052, "")
    PlaceName(313.0, 0.0, -26.0, 0x0000, 0x0053, "")
    PlaceName(278.0, 0.0, -19.5, 0x0000, 0x0053, "")

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
