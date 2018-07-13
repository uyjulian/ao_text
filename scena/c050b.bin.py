﻿from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "中央広場",               # 1
        "西通り",                 # 2
        "行政区",                 # 3
        "住宅街",                 # 4
        "歓楽街",                 # 5
        "東通り",                 # 6
        "旧市街",                 # 7
        "港湾区",                 # 8
        "ＩＢＣ",                 # 9
        "駅前通り",               # 10
        "裏通り",                 # 11
        "ウルスラ間道",           # 12
        "東クロスベル街道",       # 13
        "西クロスベル街道",       # 14
        "マインツ山道",           # 15
        "オルキスタワー",         # 16
    ))

    PlaceName(79.5, 0.0, -9.0, 0x0000, 0x0000, "中央広場")
    PlaceName(0.0, 0.0, -76.5, 0x0000, 0x0000, "西通り")
    PlaceName(11.0, 0.0, 116.0, 0x0000, 0x0000, "行政区")
    PlaceName(-148.0, 0.0, -60.0, 0x0000, 0x0000, "住宅街")
    PlaceName(-57.25, 0.0, 10.0, 0x0000, 0x0000, "歓楽街")
    PlaceName(196.0, 0.0, 56.0, 0x0000, 0x0000, "東通り")
    PlaceName(294.0, 0.0, 31.0, 0x0000, 0x0000, "旧市街")
    PlaceName(154.0, 0.0, 158.0, 0x0000, 0x0000, "港湾区")
    PlaceName(20.0, 0.0, 233.0, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(168.0, 0.0, -73.0, 0x0000, 0x0000, "駅前通り")
    PlaceName(1.0, 0.0, -9.0, 0x0000, 0x0000, "裏通り")
    PlaceName(200.0, 0.0, -112.0, 0x0000, 0x0000, "ウルスラ間道")
    PlaceName(240.0, 0.0, 130.0, 0x0000, 0x0000, "東クロスベル街道")
    PlaceName(-52.0, 0.0, -134.0, 0x0000, 0x0000, "西クロスベル街道")
    PlaceName(-156.0, 0.0, -17.0, 0x0000, 0x0000, "マインツ山道")
    PlaceName(-140.0, 0.0, 255.0, 0x0000, 0x0000, "オルキスタワー")
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
