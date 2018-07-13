from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0200.bin",                # FileName
        "c0200",                    # MapName
        "c0200",                    # Location
        0x000A,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("c0200", "c1000_1", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 33140, -4000, -18370, 0, 0, 1, 10, 0, 11, 0, 12],
    )

    BuildStringList((
        "c0200",                  # 0
        "Ryｹ",                   # 1
        "Henri",                  # 2
        "Ponce",                  # 3
        "Burick",                 # 4
        "Momo",                   # 5
        "Elsa",                   # 6
        "Old Man Ryｹvic",        # 7
        "Katerina",               # 8
        "Chiruru",                # 9
        "Mrs. Origa",             # 10
        "Citizen",                # 11
        "CGF Member",             # 12
        "Chief Sergei",           # 13
        "Ries",                   # 14
        "Zeit",                   # 15
        "KeA",                    # 16
        "White Falcon",           # 17
        "特務支援課導力車",       # 18
        "SE制御",                 # 19
        "bc0200",                 # 20
        "Central Square",         # 21
        "West Street",            # 22
        "Governmental District",  # 23
        "Residential Street",     # 24
        "Entertainment District", # 25
        "East Street",            # 26
        "Downtown",               # 27
        "Waterfront Area",        # 28
        "IBC",                    # 29
        "Station Street",         # 30
        "Back Street",            # 31
        "St. Ursula Byroad",      # 32
        "East Crossbell Highway", # 33
        "West Crossbell HIghway", # 34
        "Mainz Mountain Road",    # 35
        "Orchis Tower",           # 36
    ))

    ATBonus("ATBonus_6D4", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)

    Sepith("Sepith_C268", 8,   8,   8,   8,   11,  11,  11)

    MonsterBattlePostion("MonsterBattlePostion_724", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_728", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_72C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_730", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_734", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_738", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_73C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_740", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_784", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_788", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_78C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_790", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_794", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_798", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_79C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_7A0", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_704", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_708", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_70C", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_710", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_714", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_718", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_71C", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_720", 2, 13, 180)

    # monster count: 2

    BattleInfo(
        "BattleInfo_7A4", 0x0000, 93, 6, 60, 4, 1, 25, 0, "bc0200", "Sepith_C268", 60, 25, 10, 0,
        (
            ("ms85100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_724", "MonsterBattlePostion_784", "ed7450", "ed7453", "ATBonus_6D4"),
            ("ms85100.dat", "ms85100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_704", "MonsterBattlePostion_784", "ed7450", "ed7453", "ATBonus_6D4"),
            ("ms85100.dat", "ms85100.dat", "ms85100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_724", "MonsterBattlePostion_784", "ed7450", "ed7453", "ATBonus_6D4"),
            (),
        )
    )

    AddCharChip((
        "chr/ch20600.itc",                   # 00
        "chr/ch22200.itc",                   # 01
        "chr/ch20200.itc",                   # 02
        "chr/ch20402.itc",                   # 03
        "chr/ch20700.itc",                   # 04
        "chr/ch10400.itc",                   # 05
        "chr/ch21600.itc",                   # 06
        "chr/ch24500.itc",                   # 07
        "chr/ch20500.itc",                   # 08
        "chr/ch20100.itc",                   # 09
        "chr/ch49000.itc",                   # 0A
        "chr/ch48500.itc",                   # 0B
        "chr/ch31300.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "monster/ch85150.itc",               # 10
        "monster/ch85151.itc",               # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(4294966296, 0,       610,     90,   261,  0x0, 0,   0,   0,   0,   1,   0,   14,  255,  0)
    DeclNpc(449,     0,       610,     90,   261,  0x0, 0,   1,   0,   0,   1,   0,   18,  255,  0)
    DeclNpc(4294952177, 0,       5829,    270,  261,  0x0, 0,   2,   0,   0,   2,   0,   19,  255,  0)
    DeclNpc(6570,    4294967146, 5119,    90,   325,  0x0, 0,   3,   0,   255, 255, 0,   20,  255,  0)
    DeclNpc(5360,    3000,    17690,   0,    261,  0x0, 0,   4,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(9159,    3000,    17489,   225,  261,  0x0, 0,   5,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(4294960606, 0,       4460,    0,    389,  0x0, 0,   6,   0,   0,   0,   0,   23,  255,  0)
    DeclNpc(10800,   0,       4294963816, 270,  389,  0x0, 0,   7,   0,   0,   0,   0,   24,  255,  0)
    DeclNpc(10729,   0,       4294962516, 270,  389,  0x0, 0,   8,   0,   0,   0,   0,   25,  255,  0)
    DeclNpc(4294962016, 0,       4489,    270,  389,  0x0, 0,   9,   0,   0,   0,   0,   26,  255,  0)
    DeclNpc(4294966446, 3000,    27399,   180,  385,  0x0, 0,   10,  0,   0,   10,  0,   27,  255,  0)
    DeclNpc(1360,    4294966996, 7380,    180,  385,  0x0, 0,   12,  0,   0,   0,   0,   28,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(250,     3470,    0,       0x10100E1,    "BattleInfo_7A4", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4800,    4294957936, 0,       0x101013B,    "BattleInfo_7A4", 0,   16,  0xFFFF, 0,  1)

    DeclActor(33490,   4294963296, 4294950556, 1500,    33490,   4294965296, 4294950556, 0x007C, 0,  32, 0x0000)
    DeclActor(33490,   4294963296, 4294950556, 1500,    33490,   4294965296, 4294950556, 0x007C, 0,  32, 0x0000)
    DeclActor(37220,   4294963296, 4294948146, 1000,    37220,   4294964296, 4294948146, 0x007C, 0,  29, 0x0000)
    DeclActor(18220,   4294967086, 4294955346, 1000,    18220,   1000,    4294955346, 0x007C, 0,  29, 0x0000)
    DeclActor(14500,   4294960796, 4294953796, 1200,    14500,   4294961796, 4294953796, 0x007C, 0,  13, 0x0000)
    DeclActor(19330,   3000,    15550,   1200,    19330,   4500,    15550,   0x007C, 0,  30, 0x0000)
    DeclActor(40950,   4294963296, 4294948076, 1200,    40950,   4294964796, 4294948076, 0x007C, 0,  52, 0x0000)

    PlaceName(70.75, 0.0, -7.0, 0x0000, 0x0000, "Central Square")
    PlaceName(5.0, 0.0, -2.5, 0x0000, 0x0000, "West Street")
    PlaceName(97.75, 0.0, 82.0, 0x0000, 0x0000, "Governmental District")
    PlaceName(-56.0, 0.0, 72.0, 0x0000, 0x0000, "Residential Street")
    PlaceName(17.0, 0.0, 64.0, 0x0000, 0x0000, "Entertainment District")
    PlaceName(152.0, 0.0, -30.0, 0x0000, 0x0000, "East Street")
    PlaceName(187.5, 0.0, -85.0, 0x0000, 0x0000, "Downtown")
    PlaceName(180.0, 0.0, 36.0, 0x0000, 0x0000, "Waterfront Area")
    PlaceName(154.0, 0.0, 130.0, 0x0000, 0x0000, "IBC")
    PlaceName(82.0, 0.0, -76.0, 0x0000, 0x0000, "Station Street")
    PlaceName(35.0, 0.0, 28.0, 0x0000, 0x0000, "Back Street")
    PlaceName(79.0, 0.0, -107.0, 0x0000, 0x0000, "St. Ursula Byroad")
    PlaceName(206.0, 0.0, -16.0, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-46.0, 0.0, -4.0, 0x0000, 0x0000, "West Crossbell HIghway")
    PlaceName(-40.0, 0.0, 96.0, 0x0000, 0x0000, "Mainz Mountain Road")
    PlaceName(91.0, 0.0, 213.0, 0x0000, 0x0000, "Orchis Tower")
    PlaceName(48.75, 0.0, -21.0, 0x0000, 0x0051, "")
    PlaceName(102.5, 0.0, 5.0, 0x0000, 0x0054, "")
    PlaceName(73.25, 0.0, -29.0, 0x0000, 0x0057, "")
    PlaceName(48.0, 0.0, 8.0, 0x0000, 0x0053, "")
    PlaceName(68.5, 0.0, 32.0, 0x0000, 0x0053, "")
    PlaceName(17.75, 0.0, 3.0, 0x0000, 0x0053, "")
    PlaceName(8.0, 0.0, 24.0, 0x0000, 0x0053, "")
    PlaceName(32.0, 0.0, 56.0, 0x0000, 0x0052, "")
    PlaceName(36.75, 0.0, 43.0, 0x0000, 0x0053, "")
    PlaceName(45.5, 0.0, 34.5, 0x0000, 0x0053, "")
    PlaceName(74.0, 0.0, 105.5, 0x0000, 0x0051, "")
    PlaceName(186.0, 0.0, -30.0, 0x0000, 0x0052, "")
    PlaceName(169.0, 0.0, -120.5, 0x0000, 0x0053, "")
    PlaceName(156.0, 0.0, -102.0, 0x0000, 0x0053, "")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4, 5])                    # 1

    ScpFunction((
        "Function_0_92C",          # 00, 0
        "Function_1_9DC",          # 01, 1
        "Function_2_A3D",          # 02, 2
        "Function_3_A9E",          # 03, 3
        "Function_4_AC9",          # 04, 4
        "Function_5_B9D",          # 05, 5
        "Function_6_C71",          # 06, 6
        "Function_7_D45",          # 07, 7
        "Function_8_E19",          # 08, 8
        "Function_9_EED",          # 09, 9
        "Function_10_F18",         # 0A, 10
        "Function_11_F79",         # 0B, 11
        "Function_12_1B16",        # 0C, 12
        "Function_13_20E6",        # 0D, 13
        "Function_14_2238",        # 0E, 14
        "Function_15_2A42",        # 0F, 15
        "Function_16_2B06",        # 10, 16
        "Function_17_2C0D",        # 11, 17
        "Function_18_2D6E",        # 12, 18
        "Function_19_3582",        # 13, 19
        "Function_20_476E",        # 14, 20
        "Function_21_52EE",        # 15, 21
        "Function_22_561F",        # 16, 22
        "Function_23_5CCC",        # 17, 23
        "Function_24_6471",        # 18, 24
        "Function_25_64CC",        # 19, 25
        "Function_26_651C",        # 1A, 26
        "Function_27_65B3",        # 1B, 27
        "Function_28_66E4",        # 1C, 28
        "Function_29_6915",        # 1D, 29
        "Function_30_69B4",        # 1E, 30
        "Function_31_6A17",        # 1F, 31
        "Function_32_6D92",        # 20, 32
        "Function_33_742B",        # 21, 33
        "Function_34_74EC",        # 22, 34
        "Function_35_7580",        # 23, 35
        "Function_36_762B",        # 24, 36
        "Function_37_7BFA",        # 25, 37
        "Function_38_9303",        # 26, 38
        "Function_39_935A",        # 27, 39
        "Function_40_93EF",        # 28, 40
        "Function_41_9488",        # 29, 41
        "Function_42_94BC",        # 2A, 42
        "Function_43_94F0",        # 2B, 43
        "Function_44_9524",        # 2C, 44
        "Function_45_9558",        # 2D, 45
        "Function_46_9568",        # 2E, 46
        "Function_47_B166",        # 2F, 47
        "Function_48_B196",        # 30, 48
        "Function_49_B1D5",        # 31, 49
        "Function_50_B6E3",        # 32, 50
        "Function_51_BE33",        # 33, 51
        "Function_52_C16C",        # 34, 52
    ))


    def Function_0_92C(): pass

    label("Function_0_92C")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_964"),
        (1, "loc_970"),
        (2, "loc_97C"),
        (3, "loc_988"),
        (4, "loc_994"),
        (5, "loc_9A0"),
        (6, "loc_9AC"),
        (SWITCH_DEFAULT, "loc_9B8"),
    )


    label("loc_964")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_9C4")

    label("loc_970")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_9C4")

    label("loc_97C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_9C4")

    label("loc_988")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_9C4")

    label("loc_994")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_9C4")

    label("loc_9A0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_9C4")

    label("loc_9AC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9C4")

    label("loc_9B8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9C4")

    label("loc_9C4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9DB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9C4")

    label("loc_9DB")

    Return()

    # Function_0_92C end

    def Function_1_9DC(): pass

    label("Function_1_9DC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A3C")
    OP_95(0xFE, 7000, -300, 610, 6000, 0x0)
    OP_95(0xFE, 7000, 0, -9140, 6000, 0x0)
    OP_95(0xFE, -1000, -10, -9140, 6000, 0x0)
    OP_95(0xFE, -1000, 0, 610, 6000, 0x0)
    Jump("Function_1_9DC")

    label("loc_A3C")

    Return()

    # Function_1_9DC end

    def Function_2_A3D(): pass

    label("Function_2_A3D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A9D")
    OP_95(0xFE, -10000, 0, 5750, 800, 0x0)
    OP_95(0xFE, -10000, 0, 2280, 800, 0x0)
    OP_95(0xFE, -27380, 0, 2280, 800, 0x0)
    OP_95(0xFE, -27380, 0, 5750, 800, 0x0)
    Jump("Function_2_A3D")

    label("loc_A9D")

    Return()

    # Function_2_A3D end

    def Function_3_A9E(): pass

    label("Function_3_A9E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AC8")
    OP_94(0xFE, 0xFFFF8F3A, 0x9EC, 0xFFFFAD9E, 0x18EC, 0x3E8)
    Sleep(300)
    Jump("Function_3_A9E")

    label("loc_AC8")

    Return()

    # Function_3_A9E end

    def Function_4_AC9(): pass

    label("Function_4_AC9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B9C")
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B08")
    OP_96(0xFE, 0x1004, 0x0, 0xFFFFF40C, 0x12C, 0x0)
    Jump("loc_B94")

    label("loc_B08")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B30")
    OP_96(0xFE, 0x1004, 0x0, 0xFFFFF3A8, 0x12C, 0x0)
    Jump("loc_B94")

    label("loc_B30")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B58")
    OP_96(0xFE, 0x1004, 0x0, 0xFFFFF344, 0x12C, 0x0)
    Jump("loc_B94")

    label("loc_B58")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B80")
    OP_96(0xFE, 0x1004, 0x0, 0xFFFFF2E0, 0x12C, 0x0)
    Jump("loc_B94")

    label("loc_B80")

    OP_96(0xFE, 0x1004, 0x0, 0xFFFFF27C, 0x12C, 0x0)

    label("loc_B94")

    Sleep(500)
    Jump("Function_4_AC9")

    label("loc_B9C")

    Return()

    # Function_4_AC9 end

    def Function_5_B9D(): pass

    label("Function_5_B9D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C70")
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_BDC")
    OP_96(0xFE, 0xA14, 0x0, 0xFFFFF40C, 0xC8, 0x0)
    Jump("loc_C68")

    label("loc_BDC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C04")
    OP_96(0xFE, 0xA14, 0x0, 0xFFFFF3A8, 0xC8, 0x0)
    Jump("loc_C68")

    label("loc_C04")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C2C")
    OP_96(0xFE, 0xA14, 0x0, 0xFFFFF344, 0xC8, 0x0)
    Jump("loc_C68")

    label("loc_C2C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C54")
    OP_96(0xFE, 0xA14, 0x0, 0xFFFFF2E0, 0xC8, 0x0)
    Jump("loc_C68")

    label("loc_C54")

    OP_96(0xFE, 0xA14, 0x0, 0xFFFFF27C, 0xC8, 0x0)

    label("loc_C68")

    Sleep(600)
    Jump("Function_5_B9D")

    label("loc_C70")

    Return()

    # Function_5_B9D end

    def Function_6_C71(): pass

    label("Function_6_C71")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D44")
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CB0")
    OP_96(0xFE, 0x11A8, 0x0, 0xFFFFF1AA, 0x12C, 0x0)
    Jump("loc_D3C")

    label("loc_CB0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CD8")
    OP_96(0xFE, 0x11DA, 0x0, 0xFFFFF1DC, 0x12C, 0x0)
    Jump("loc_D3C")

    label("loc_CD8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D00")
    OP_96(0xFE, 0x120C, 0x0, 0xFFFFF20E, 0x12C, 0x0)
    Jump("loc_D3C")

    label("loc_D00")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D28")
    OP_96(0xFE, 0x123E, 0x0, 0xFFFFF240, 0x12C, 0x0)
    Jump("loc_D3C")

    label("loc_D28")

    OP_96(0xFE, 0x1270, 0x0, 0xFFFFF272, 0x12C, 0x0)

    label("loc_D3C")

    Sleep(500)
    Jump("Function_6_C71")

    label("loc_D44")

    Return()

    # Function_6_C71 end

    def Function_7_D45(): pass

    label("Function_7_D45")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E18")
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D84")
    OP_96(0xFE, 0xE24, 0x0, 0xFFFFF92A, 0xFA, 0x0)
    Jump("loc_E10")

    label("loc_D84")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_DAC")
    OP_96(0xFE, 0xDF2, 0x0, 0xFFFFF92A, 0xFA, 0x0)
    Jump("loc_E10")

    label("loc_DAC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_DD4")
    OP_96(0xFE, 0xDC0, 0x0, 0xFFFFF92A, 0xFA, 0x0)
    Jump("loc_E10")

    label("loc_DD4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_DFC")
    OP_96(0xFE, 0xD8E, 0x0, 0xFFFFF92A, 0xFA, 0x0)
    Jump("loc_E10")

    label("loc_DFC")

    OP_96(0xFE, 0xD5C, 0x0, 0xFFFFF92A, 0xFA, 0x0)

    label("loc_E10")

    Sleep(550)
    Jump("Function_7_D45")

    label("loc_E18")

    Return()

    # Function_7_D45 end

    def Function_8_E19(): pass

    label("Function_8_E19")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EEC")
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E58")
    OP_96(0xFE, 0x910, 0x0, 0xFFFFF272, 0xC8, 0x0)
    Jump("loc_EE4")

    label("loc_E58")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E80")
    OP_96(0xFE, 0x942, 0x0, 0xFFFFF240, 0xC8, 0x0)
    Jump("loc_EE4")

    label("loc_E80")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_EA8")
    OP_96(0xFE, 0x974, 0x0, 0xFFFFF20E, 0xC8, 0x0)
    Jump("loc_EE4")

    label("loc_EA8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_ED0")
    OP_96(0xFE, 0x9A6, 0x0, 0xFFFFF1DC, 0xC8, 0x0)
    Jump("loc_EE4")

    label("loc_ED0")

    OP_96(0xFE, 0x9D8, 0x0, 0xFFFFF1AA, 0xC8, 0x0)

    label("loc_EE4")

    Sleep(600)
    Jump("Function_8_E19")

    label("loc_EEC")

    Return()

    # Function_8_E19 end

    def Function_9_EED(): pass

    label("Function_9_EED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F17")
    OP_94(0xFE, 0xFFFFFC18, 0xFFFFDCD8, 0x1B58, 0x0, 0x3E8)
    Sleep(300)
    Jump("Function_9_EED")

    label("loc_F17")

    Return()

    # Function_9_EED end

    def Function_10_F18(): pass

    label("Function_10_F18")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F78")
    OP_95(0xFE, -1630, 0, 5050, 2000, 0x0)
    OP_95(0xFE, 9840, 0, -6290, 2000, 0x0)
    OP_95(0xFE, 40380, 2060, -8580, 2000, 0x0)
    Sleep(500)
    SetChrPos(0xFE, -850, 3000, 27400, 180)
    Jump("Function_10_F18")

    label("loc_F78")

    Return()

    # Function_10_F18 end

    def Function_11_F79(): pass

    label("Function_11_F79")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10E5")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1044")
    SetChrPos(0x0, 110, 3000, 22760, 180)
    SetChrPos(0x1, 110, 3000, 22760, 180)
    SetChrPos(0x2, 110, 3000, 22760, 180)
    SetChrPos(0x3, 110, 3000, 22760, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1017")
    SetChrPos(0x4, 110, 3000, 22760, 180)
    SetChrPos(0x5, 110, 3000, 22760, 180)
    Jump("loc_1036")

    label("loc_1017")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1036")
    SetChrPos(0x4, 110, 3000, 22760, 180)

    label("loc_1036")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10E5")

    label("loc_1044")

    SetChrPos(0x0, 24460, 0, -8180, 270)
    SetChrPos(0x1, 24460, 0, -8180, 270)
    SetChrPos(0x2, 24460, 0, -8180, 270)
    SetChrPos(0x3, 24460, 0, -8180, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10BD")
    SetChrPos(0x4, 24460, 0, -8180, 270)
    SetChrPos(0x5, 24460, 0, -8180, 270)
    Jump("loc_10DC")

    label("loc_10BD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10DC")
    SetChrPos(0x4, 24460, 0, -8180, 270)

    label("loc_10DC")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10E5")

    OP_D2(0x7, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1102")
    OP_C9(0x1, 0x1000)

    label("loc_1102")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15A6")
    ClearScenarioFlags(0x38, 0)
    ClearScenarioFlags(0x38, 1)
    ClearScenarioFlags(0x38, 2)
    ClearScenarioFlags(0x38, 3)
    ClearScenarioFlags(0x38, 4)
    ClearScenarioFlags(0x38, 5)
    ClearScenarioFlags(0x38, 6)
    ClearScenarioFlags(0x38, 7)
    ClearScenarioFlags(0x39, 0)
    ClearScenarioFlags(0x39, 1)
    ClearScenarioFlags(0x39, 2)
    ClearScenarioFlags(0x39, 3)
    ClearScenarioFlags(0x39, 4)
    ClearScenarioFlags(0x39, 5)
    ClearScenarioFlags(0x39, 6)
    ClearScenarioFlags(0x39, 7)
    ClearScenarioFlags(0x3A, 0)
    ClearScenarioFlags(0x3A, 1)
    ClearScenarioFlags(0x3A, 2)
    ClearScenarioFlags(0x3A, 3)
    ClearScenarioFlags(0x3A, 4)
    ClearScenarioFlags(0x3A, 5)
    ClearScenarioFlags(0x3A, 6)
    ClearScenarioFlags(0x3A, 7)
    ClearScenarioFlags(0x3B, 0)
    ClearScenarioFlags(0x3B, 1)
    ClearScenarioFlags(0x3B, 2)
    ClearScenarioFlags(0x3B, 3)
    ClearScenarioFlags(0x3B, 4)
    ClearScenarioFlags(0x3B, 5)
    ClearScenarioFlags(0x3B, 6)
    ClearScenarioFlags(0x3B, 7)
    ClearScenarioFlags(0x3D, 5)
    ClearScenarioFlags(0x3D, 6)
    ClearScenarioFlags(0x3D, 7)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_118F")
    SetScenarioFlags(0x38, 0)

    label("loc_118F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11A5")
    SetScenarioFlags(0x38, 1)

    label("loc_11A5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11BB")
    SetScenarioFlags(0x38, 2)

    label("loc_11BB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11D1")
    SetScenarioFlags(0x38, 3)

    label("loc_11D1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11E7")
    SetScenarioFlags(0x38, 4)

    label("loc_11E7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11FD")
    SetScenarioFlags(0x38, 5)

    label("loc_11FD")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1213")
    SetScenarioFlags(0x38, 6)

    label("loc_1213")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1229")
    SetScenarioFlags(0x38, 7)

    label("loc_1229")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_123F")
    SetScenarioFlags(0x39, 0)

    label("loc_123F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1255")
    SetScenarioFlags(0x39, 1)

    label("loc_1255")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_126B")
    SetScenarioFlags(0x39, 2)

    label("loc_126B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1281")
    SetScenarioFlags(0x39, 3)

    label("loc_1281")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1297")
    SetScenarioFlags(0x39, 4)

    label("loc_1297")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12AD")
    SetScenarioFlags(0x39, 5)

    label("loc_12AD")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12C3")
    SetScenarioFlags(0x39, 6)

    label("loc_12C3")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12D9")
    SetScenarioFlags(0x39, 7)

    label("loc_12D9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12EF")
    SetScenarioFlags(0x3A, 0)

    label("loc_12EF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1305")
    SetScenarioFlags(0x3A, 1)

    label("loc_1305")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_131B")
    SetScenarioFlags(0x3A, 2)

    label("loc_131B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1331")
    SetScenarioFlags(0x3A, 3)

    label("loc_1331")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1347")
    SetScenarioFlags(0x3A, 4)

    label("loc_1347")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_135D")
    SetScenarioFlags(0x3A, 5)

    label("loc_135D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1373")
    SetScenarioFlags(0x3A, 6)

    label("loc_1373")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1389")
    SetScenarioFlags(0x3A, 7)

    label("loc_1389")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_139F")
    SetScenarioFlags(0x3B, 0)

    label("loc_139F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13B5")
    SetScenarioFlags(0x3B, 1)

    label("loc_13B5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13CB")
    SetScenarioFlags(0x3B, 2)

    label("loc_13CB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13E1")
    SetScenarioFlags(0x3B, 3)

    label("loc_13E1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13F7")
    SetScenarioFlags(0x3B, 4)

    label("loc_13F7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_140D")
    SetScenarioFlags(0x3B, 5)

    label("loc_140D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1423")
    SetScenarioFlags(0x3B, 6)

    label("loc_1423")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1439")
    SetScenarioFlags(0x3B, 7)

    label("loc_1439")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_144F")
    SetScenarioFlags(0x3D, 5)

    label("loc_144F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1465")
    SetScenarioFlags(0x3D, 6)

    label("loc_1465")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_147B")
    SetScenarioFlags(0x3D, 7)

    label("loc_147B")

    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14B6")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_15A6")

    label("loc_14B6")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14D9")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_15A6")

    label("loc_14D9")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14FC")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_15A6")

    label("loc_14FC")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_151F")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_15A6")

    label("loc_151F")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1542")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_15A6")

    label("loc_1542")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1565")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_15A6")

    label("loc_1565")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1588")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_15A6")

    label("loc_1588")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15A6")
    SetScenarioFlags(0x3C, 7)

    label("loc_15A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x35, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15BC")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_15BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15EE")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15EE")
    SetChrPos(0x0, 33260, -4000, -18040, 278)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    Event(0, 34)

    label("loc_15EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_1621")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1621")
    SetChrPos(0x0, 33490, -4000, -16740, 270)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    ClearMapFlags(0x8000000)

    label("loc_1621")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_1635")
    ClearScenarioFlags(0x22, 0)
    Event(0, 35)
    Jump("loc_1644")

    label("loc_1635")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_1644")
    ClearScenarioFlags(0x22, 1)
    Event(0, 37)

    label("loc_1644")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1655")
    Event(0, 36)

    label("loc_1655")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1680")
    SetMapFlags(0x10000000)
    Event(1, 0)

    label("loc_1680")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1691")
    Event(0, 46)

    label("loc_1691")

    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1727")
    SetChrFlags(0xD, 0x80)
    SetChrPos(0x8, 4620, 0, -3570, 315)
    BeginChrThread(0x8, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16D6")
    SetChrFlags(0x8, 0x10)

    label("loc_16D6")

    SetChrPos(0x9, 3520, 0, -1750, 180)
    BeginChrThread(0x9, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16FC")
    SetChrFlags(0x9, 0x10)

    label("loc_16FC")

    SetChrPos(0xC, 2420, 0, -3570, 45)
    BeginChrThread(0xC, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1722")
    SetChrFlags(0xC, 0x10)

    label("loc_1722")

    Jump("loc_1B15")

    label("loc_1727")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1753")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_1B15")

    label("loc_1753")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_179E")
    SetChrPos(0x8, 4100, 0, -3260, 270)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x9, 2580, 0, -3260, 90)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_1B15")

    label("loc_179E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_17E9")
    SetChrPos(0x8, 4100, 0, -3260, 270)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x9, 2580, 0, -3260, 90)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_1B15")

    label("loc_17E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_180E")
    SetChrPos(0xC, 2420, 0, -3570, 45)
    BeginChrThread(0xC, 0, 0, 8)
    Jump("loc_1B15")

    label("loc_180E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1879")
    SetChrPos(0x8, 4100, 0, -3260, 270)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x9, 2580, 0, -3260, 90)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0xA, -5710, 0, 1570, 180)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrChipByIndex(0xA, 0xB)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_1B15")

    label("loc_1879")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_18F1")
    SetChrPos(0x8, 30090, -4000, -15230, 225)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x9, 6330, -300, 1950, 270)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrPos(0xC, 4390, -40, 1630, 90)
    BeginChrThread(0xC, 0, 0, 0)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -6690, 0, 4460, 90)
    ClearChrFlags(0x11, 0x80)
    Jump("loc_1B15")

    label("loc_18F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1953")
    SetChrPos(0x8, 30090, -4000, -15230, 225)
    BeginChrThread(0x8, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1920")
    SetChrFlags(0x8, 0x10)

    label("loc_1920")

    SetChrPos(0x9, 11110, -300, 5400, 270)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrPos(0xC, 2420, 0, -3570, 45)
    BeginChrThread(0xC, 0, 0, 9)
    Jump("loc_1B15")

    label("loc_1953")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_19D5")
    SetChrPos(0x8, 4100, 0, -3260, 270)
    BeginChrThread(0x8, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1982")
    SetChrFlags(0x8, 0x10)

    label("loc_1982")

    SetChrPos(0x9, 2580, 0, -3260, 90)
    BeginChrThread(0x9, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19A8")
    SetChrFlags(0x9, 0x10)

    label("loc_19A8")

    SetChrFlags(0xC, 0x80)
    SetChrPos(0xD, 8130, 3000, 13940, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_19D0")
    SetChrFlags(0xB, 0x80)

    label("loc_19D0")

    Jump("loc_1B15")

    label("loc_19D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_19F7")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    Jump("loc_1B15")

    label("loc_19F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_1A0F")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    Jump("loc_1B15")

    label("loc_1A0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1A31")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_1B15")

    label("loc_1A31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1AB1")
    SetChrPos(0x8, 4620, 0, -3570, 315)
    BeginChrThread(0x8, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A60")
    SetChrFlags(0x8, 0x10)

    label("loc_1A60")

    SetChrPos(0x9, 3520, 0, -1750, 180)
    BeginChrThread(0x9, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A86")
    SetChrFlags(0x9, 0x10)

    label("loc_1A86")

    SetChrPos(0xC, 2420, 0, -3570, 45)
    BeginChrThread(0xC, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AAC")
    SetChrFlags(0xC, 0x10)

    label("loc_1AAC")

    Jump("loc_1B15")

    label("loc_1AB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1AF8")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0xA, -5710, 0, 1570, 180)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrChipByIndex(0xA, 0xB)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_1B15")

    label("loc_1AF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1B15")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)

    label("loc_1B15")

    Return()

    # Function_11_F79 end

    def Function_12_1B16(): pass

    label("Function_12_1B16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1BE2")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x5F, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tuika_mul", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tuika2_mul", 0x0, 0x1)
    Sound(128, 1, 100, 0)

    label("loc_1BE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C99")
    LoadEffect(0x9, "map/mpmoya.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0x78, 0x96, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xFF, 0xD, 0x5F, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tuika_mul", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tuika2_mul", 0x0, 0x1)

    label("loc_1C99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1D03")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x23, 0x96, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tuika_mul", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tuika2_mul", 0x0, 0x1)

    label("loc_1D03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D1B")
    ClearMapFlags(0x2000)
    Jump("loc_1D22")

    label("loc_1D1B")

    SetMapFlags(0x2000)
    OP_E2(0x1)

    label("loc_1D22")

    MiniGame(0x2F, 0x0, 0xFFFFFFFF, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_1DA0")
    SetMapObjFrame(0xFF, "tuika_mul", 0x1, 0x1)
    SetMapObjFrame(0xFF, "tuika", 0x1, 0x1)
    SetMapObjFrame(0xFF, "window01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "tuika2_mul", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kabuse", 0x0, 0x1)
    Jump("loc_1E2E")

    label("loc_1DA0")

    SetMapObjFrame(0xFF, "tuika_mul", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tuika", 0x0, 0x1)
    SetMapObjFrame(0xFF, "window01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tuika2_mul", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kabuse", 0x1, 0x1)
    SetMapObjFlags(0xA, 0x4)
    SetBarrier(0x0, 0x0, 0x1, 0x0, 18500, -1000, -11500, 5000, 5000, 0)
    SetBarrier(0x0, 0x1, 0x1, 0x0, 37500, -5000, -19000, 5000, 5000, 90000)

    label("loc_1E2E")

    ClearMapObjFlags(0x7, 0x10)
    OP_70(0x7, 0x1E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E4B")
    OP_1B(0x8, 0x0, 0x33)

    label("loc_1E4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E5E")
    OP_1B(0x8, 0x0, 0x33)

    label("loc_1E5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E71")
    OP_1B(0x8, 0x0, 0x33)

    label("loc_1E71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E84")
    OP_1B(0x8, 0x0, 0x33)

    label("loc_1E84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E97")
    OP_1B(0x8, 0x0, 0x33)

    label("loc_1E97")

    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EB5")
    OP_66(0x2, 0x1)
    OP_66(0x3, 0x1)

    label("loc_1EB5")

    OP_65(0x5, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1ED1")
    OP_66(0x5, 0x1)
    ClearMapObjFlags(0x3, 0x10)

    label("loc_1ED1")

    OP_65(0x6, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EED")
    OP_66(0x6, 0x1)
    ClearMapObjFlags(0x5, 0x10)

    label("loc_1EED")

    OP_52(0x1B, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_209D")
    Jump("loc_20AC")

    label("loc_209D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_20AC")
    SetMapObjFlags(0xC, 0x4)

    label("loc_20AC")

    MiniGame(0x2F, 0x0, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20E1")
    OP_70(0xD, 0x0)
    Jump("loc_20E5")

    label("loc_20E1")

    OP_70(0xD, 0x1E)

    label("loc_20E5")

    Return()

    # Function_12_1B16 end

    def Function_13_20E6(): pass

    label("Function_13_20E6")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21E2")
    Sound(14, 0, 100, 0)
    OP_74(0xD, 0x1E)
    OP_71(0xD, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x358, 1)"), scpexpr(EXPR_END)), "loc_216B")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x358),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EB, 7)
    OP_E0(0x5, 0x0)
    Jump("loc_21DD")

    label("loc_216B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x358),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xD, 0x1E, 0x0, 0x0, 0x0)

    label("loc_21DD")

    Jump("loc_222C")

    label("loc_21E2")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the chest. \x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_222C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_13_20E6 end

    def Function_14_2238(): pass

    label("Function_14_2238")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_228B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2256")
    Call(0, 17)
    Jump("loc_2286")

    label("loc_2256")


    ChrTalk(
        0xFE,
        "Ah, guys!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Leave Crossbell\x01",
            "City to us!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2286")

    Jump("loc_2A3E")

    label("loc_228B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2299")
    Jump("loc_2A3E")

    label("loc_2299")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_23BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_236D")

    ChrTalk(
        0xFE,
        (
            "Everyone seems to be seriously worried about\x01",
            "what's gonna happen with the Empire and Republic...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't really get it what\x01",
            ""independence" is, but...\x01",
            "Wasn't it a happy thing?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_23B5")

    label("loc_236D")


    ChrTalk(
        0xFE,
        (
            "Wasn't "independence"\x01",
            "a happy thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I don't really get it...\x02",
    )

    CloseMessageWindow()

    label("loc_23B5")

    Jump("loc_2A3E")

    label("loc_23BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2420")

    ChrTalk(
        0xFE,
        (
            "I invited Momo to play,\x01",
            "but her mother said no...\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*haah*, somehow I'm bored.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A3E")

    label("loc_2420")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2447")

    ChrTalk(
        0xFE,
        "Iyahhoi, wait wait!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A3E")

    label("loc_2447")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_24DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24A0")

    ChrTalk(
        0xFE,
        "Momo's laaate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope she finishes\x01",
            "her errand fast.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_24D5")

    label("loc_24A0")


    ChrTalk(
        0xFE,
        (
            "I hope Momo can at least\x01",
            "finish an errand fast.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24D5")

    Jump("loc_2A3E")

    label("loc_24DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_25B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2546")

    ChrTalk(
        0xFE,
        (
            "Momo really suck\x01",
            "at searching...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*yaaawn*...\x01",
            "Somehow I've got tired...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_25AD")

    label("loc_2546")


    ChrTalk(
        0xFE,
        (
            "I've got tired of\x01",
            "standing still too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want her to find me already\x01",
            "and do a different game.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25AD")

    Jump("loc_2A3E")

    label("loc_25B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2762")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26FA")
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x8, 0x0, 500)

    ChrTalk(
        0xFE,
        (
            "Whoops...\x01",
            "Oh, it's you guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*haah*, you scared me.\x01",
            "I thought I'd been\x01",
            "found by Momo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FHey now...\x01",
            "Don't sneak in this place\x01",
            "as you please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Eh eh, come on, don't say\x01",
            "cheeseparing things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Keep silent about me\x01",
            "hiding here, eh?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    OP_93(0xFE, 0xE1, 0x0)
    ClearChrFlags(0x8, 0x10)
    Jump("loc_275D")

    label("loc_26FA")


    ChrTalk(
        0xFE,
        (
            "I'm playing hide and seek\x01",
            "with Henri and Momo now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Keep silent about me\x01",
            "hiding here, eh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_275D")

    Jump("loc_2A3E")

    label("loc_2762")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_27E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_277D")
    Call(0, 15)
    Jump("loc_27E3")

    label("loc_277D")


    ChrTalk(
        0xFE,
        (
            "By the way, recently KeA\x01",
            "wasn't in top form.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Guess I'll invite her to play again next time.\x02",
    )

    CloseMessageWindow()

    label("loc_27E3")

    Jump("loc_2A3E")

    label("loc_27E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_27F6")
    Jump("loc_2A3E")

    label("loc_27F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_2975")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2916")

    ChrTalk(
        0xFE,
        (
            "Tomorrow, they say that\x01",
            "there's that trade stuff\x01",
            "at Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't really get somehow, but\x01",
            "with the occasion I want to go\x01",
            "have a look with Henri and Momo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Eh eh, I'm sure it's gonna\x01",
            "be a fun party or something.\x01",
            "I can't wait for tomorrow♪\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2970")

    label("loc_2916")


    ChrTalk(
        0xFE,
        (
            "Maybe that trade stuff is\x01",
            "a party or something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Eh he, can't wait for tomorrow.\x02",
    )

    CloseMessageWindow()

    label("loc_2970")

    Jump("loc_2A3E")

    label("loc_2975")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2983")
    Jump("loc_2A3E")

    label("loc_2983")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2A27")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_299E")
    Call(0, 16)
    Jump("loc_2A22")

    label("loc_299E")


    ChrTalk(
        0xFE,
        (
            "By the way, today KeA\x01",
            "is playing with a friend\x01",
            "called Shizuku, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since she's here, I guess\x01",
            "I'll invite that gal too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A22")

    Jump("loc_2A3E")

    label("loc_2A27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2A35")
    Jump("loc_2A3E")

    label("loc_2A35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2A3E")

    label("loc_2A3E")

    TalkEnd(0xFE)
    Return()

    # Function_14_2238 end

    def Function_15_2A42(): pass

    label("Function_15_2A42")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0x8,
        (
            "Today, Momo's helping\x01",
            "with the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Tch, with Henri there's not\x01",
            "much choice of games to play.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Ryｹ.\x01",
            "As you'd think, isn't that\x01",
            "rude towards me?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x10)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    Return()

    # Function_15_2A42 end

    def Function_16_2B06(): pass

    label("Function_16_2B06")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0x8,
        (
            "Then, let's all go see\x01",
            "that Orchis Tower\x01",
            "tomorrow!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Yes, that's nice.\x01",
            "Let's go all together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "M-Momo's coming too...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Okay, let's meet in front\x01",
            "of the department store\x01",
            "first thing in the morning!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x0, 4)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xC, 0x10)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_16_2B06 end

    def Function_17_2C0D(): pass

    label("Function_17_2C0D")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0x8,
        (
            "Well then, let's all start\x01",
            "patrolling the city!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "You ready, Henri, Momo?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Yes, Captain Ryｹ!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Let's gooo!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Alright, let's go then!\x01",
            "Crossbell Youth Special Support Section, roll out!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F(Ha ha, "Youth Special Support Section"...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109F(Somehow it makes you feel happy.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x0, 4)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0x8, 0x10)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_17_2C0D end

    def Function_18_2D6E(): pass

    label("Function_18_2D6E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2E47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D8C")
    Call(0, 17)
    Jump("loc_2E42")

    label("loc_2D8C")


    ChrTalk(
        0xFE,
        (
            "The Youth Special Support Section, eh...?\x01",
            "Every now and then, Ryｹ too is\x01",
            "struck with some good ideas.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since we're doing it, I want to\x01",
            "properly help the people of the city.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E42")

    Jump("loc_357E")

    label("loc_2E47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2E55")
    Jump("loc_357E")

    label("loc_2E55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2FEF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F3D")

    ChrTalk(
        0xFE,
        (
            "My father and mother came back\x01",
            "yesterday from abroad too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Personally I'm happy about it, but\x01",
            "they look troubled somehow...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh", as I thought, could the\x01",
            ""independence" be something grave?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2FEA")

    label("loc_2F3D")


    ChrTalk(
        0xFE,
        (
            "Personally, I'm happy that father \x01",
            "and mother have come home, but\x01",
            "they somehow look troubled...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh", as I thought, could the\x01",
            ""independence" be something grave?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FEA")

    Jump("loc_357E")

    label("loc_2FEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3075")

    ChrTalk(
        0xFE,
        (
            "I think that Momo's mother\x01",
            "too is worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It can't be helped...\x01",
            "Something like a raid\x01",
            "incident has happened.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_357E")

    label("loc_3075")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_30FB")

    ChrTalk(
        0xFE,
        (
            "H-Hey, Ryｹ!?\x01",
            "We haven't decided\x01",
            "what to play yet!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm ok with anything except\x01",
            "tiresome games like this! Stop!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_357E")

    label("loc_30FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3235")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31B8")

    ChrTalk(
        0xFE,
        (
            "This morning I was invited\x01",
            "by Ryｹ and we went to the\x01",
            "plaza in front of the tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, Ryｹ, we shouldn't have come\x01",
            "out on purpose on such a rainy day...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3230")

    label("loc_31B8")


    ChrTalk(
        0xFE,
        (
            "Geez, it can't be helped, right?\x01",
            "We suddenly invited her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Let's wait patiently until\x01",
            "she finishes the errand.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3230")

    Jump("loc_357E")

    label("loc_3235")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_335A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32D8")

    ChrTalk(
        0xFE,
        "*sigh*, I got found out.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the way, where could\x01",
            "Ryｹ be hiding...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope he hasn't entered in\x01",
            "some strange place again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3355")

    label("loc_32D8")


    ChrTalk(
        0xFE,
        (
            "By the way, since some time ago many\x01",
            "ambulances have been passing through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Did an accident or something happen...?\x02",
    )

    CloseMessageWindow()

    label("loc_3355")

    Jump("loc_357E")

    label("loc_335A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_33EE")

    ChrTalk(
        0xFE,
        (
            "The other day, when we played hide\x01",
            "and seek, it went on until evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if Momo will be able\x01",
            "to properly find us...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_357E")

    label("loc_33EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3498")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3409")
    Call(0, 15)
    Jump("loc_3493")

    label("loc_3409")


    ChrTalk(
        0xFE,
        (
            "When Momo is here, the number\x01",
            "of games we can do broadens\x01",
            "and it's fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, since she has to help,\x01",
            "there's nothing we can do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3493")

    Jump("loc_357E")

    label("loc_3498")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_34A6")
    Jump("loc_357E")

    label("loc_34A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_34B4")
    Jump("loc_357E")

    label("loc_34B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_34C2")
    Jump("loc_357E")

    label("loc_34C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3567")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34DD")
    Call(0, 16)
    Jump("loc_3562")

    label("loc_34DD")


    ChrTalk(
        0xFE,
        (
            "According to rumors,\x01",
            "Orchis Tower is even\x01",
            "250 arge height.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder what kind of building is it...\x01",
            "I can't wait to see it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3562")

    Jump("loc_357E")

    label("loc_3567")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3575")
    Jump("loc_357E")

    label("loc_3575")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_357E")

    label("loc_357E")

    TalkEnd(0xFE)
    Return()

    # Function_18_2D6E end

    def Function_19_3582(): pass

    label("Function_19_3582")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_364B")

    ChrTalk(
        0xFE,
        (
            "That big and pale azure\x01",
            "light emitting tree...\x01",
            "What a thing has appeared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't know what will happen from\x01",
            "now on but I must properly record\x01",
            "it and convey it to posterity.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_476A")

    label("loc_364B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3659")
    Jump("loc_476A")

    label("loc_3659")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3712")

    ChrTalk(
        0xFE,
        (
            "President Dieter's words...\x01",
            "They strongly resonated in our citizens' hearts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if we were to make enemies\x01",
            "of the two major powers...\x01",
            "I'd want to support him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_476A")

    label("loc_3712")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3882")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3803")

    ChrTalk(
        0xFE,
        (
            "I'm taking pictures of the\x01",
            "people restoration activities,\x01",
            "the destroyed IBC and so on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We can't let such a terrifying\x01",
            "incident to happen again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I must properly record it\x01",
            "so to not forget that too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_387D")

    label("loc_3803")


    ChrTalk(
        0xFE,
        (
            "We can't let such a terrifying\x01",
            "incident to happen again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I must properly record it\x01",
            "so to not forget that too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_387D")

    Jump("loc_476A")

    label("loc_3882")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3A01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_396A")

    ChrTalk(
        0xFE,
        (
            "It appears that from last night,\x01",
            "some CGF armored vehicles\x01",
            "headed to the Mainz region.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This means that they're\x01",
            "going as reinforcements...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Is that armed group that\x01",
            "much of a strong enemy...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_39FC")

    label("loc_396A")


    ChrTalk(
        0xFE,
        (
            "It appears that reinforcements\x01",
            "from the CGF and even vehicles\x01",
            "are heading to Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Is that armed group that\x01",
            "much of a strong enemy...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39FC")

    Jump("loc_476A")

    label("loc_3A01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3AB0")

    ChrTalk(
        0xFE,
        (
            "I don't know very well, but...\x01",
            "The story is that yesterday's train incident\x01",
            "was the deed of an unknown monster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hm, I'm worried it could appear again.\x02",
    )

    CloseMessageWindow()
    Jump("loc_476A")

    label("loc_3AB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3B0F")

    ChrTalk(
        0xFE,
        (
            "Hm...\x01",
            "I'm no good with the ambulance sirens.\x01",
            "Somehow they make me uneasy...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_476A")

    label("loc_3B0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3CF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C59")

    ChrTalk(
        0xFE,
        (
            "I have the Crossbell News Agency\x01",
            "published tour guide called\x01",
            ""Crossbell's 100 Famous Views".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It features a lot of spots with\x01",
            "nice scenery and it is greatly\x01",
            "useful for shooting photos.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, for the valuable spots you\x01",
            "largely end up walking around.\x01",
            "Where should I go next, I wonder...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3CF0")

    label("loc_3C59")


    ChrTalk(
        0xFE,
        (
            "Where could I go to take\x01",
            "pictures today...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For the spots featured in the\x01",
            ""Crossbell's 100 Famous Views",\x01",
            "you largely end up walking around.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CF0")

    Jump("loc_476A")

    label("loc_3CF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3EC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E07")

    ChrTalk(
        0xFE,
        (
            "The other day, I went to St. Ursula\x01",
            "Byroad sandbank to take photos.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Then, I could see an unfamiliar path\x01",
            "going further deep in the sandbank.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because it looked dangerous somehow,\x01",
            "I didn't enter it, however...\x01",
            "I wonder what was that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3EC0")

    label("loc_3E07")


    ChrTalk(
        0xFE,
        (
            "There was a never seen before path going\x01",
            "further in the St. Ursula Byroad sandbank.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because it looked dangerous somehow,\x01",
            "I didn't enter it, however...\x01",
            "I wonder what was that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EC0")

    Jump("loc_476A")

    label("loc_3EC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_407E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FCF")

    ChrTalk(
        0xFE,
        (
            "It looks like that today, the\x01",
            "Orchis Tower environs are\x01",
            "authorized personnel only.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since it's for security purposes I think it\x01",
            "can't be helped, but I'm a little disappointed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Continuing from yesterday,\x01",
            "I took photos nearby.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4079")

    label("loc_3FCF")


    ChrTalk(
        0xFE,
        (
            "It looks like that the\x01",
            "Orchis Tower environs are\x01",
            "authorized personnel only.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I guess that today\x01",
            "I'll go to take picture from the\x01",
            "department store rooftop.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4079")

    Jump("loc_476A")

    label("loc_407E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_41A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4158")

    ChrTalk(
        0xFE,
        (
            "Whoops...\x01",
            "I ended up being out\x01",
            "of exposure Quartz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It looks like I took too many pictures\x01",
            "at today's inauguration ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I must buy a new one before\x01",
            "the orbal store closes.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_41A3")

    label("loc_4158")


    ChrTalk(
        0xFE,
        (
            "I must go to buy a new\x01",
            "exposure Quartz before\x01",
            "the orbal store closes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41A3")

    Jump("loc_476A")

    label("loc_41A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_431C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_429C")

    ChrTalk(
        0xFE,
        (
            "After the inauguration ceremony\x01",
            "was over, I went to take a lot of\x01",
            "photos of Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Man, at any rate it was an\x01",
            "amazing big building.\x01",
            "40 floors above ground...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uhhm, I can't wait to develop them.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4317")

    label("loc_429C")


    ChrTalk(
        0xFE,
        (
            "I took a lot of pictures\x01",
            "of Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It appears that that building will\x01",
            "become the new symbol of Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4317")

    Jump("loc_476A")

    label("loc_431C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_44AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4416")

    ChrTalk(
        0xFE,
        "The Trade Conference is drawing close.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "VIPs from every country will come\x01",
            "and there will also be the inauguration\x01",
            "for the debut of the new City Hall...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I must not let good chances to\x01",
            "take pictures pass me by.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_44A8")

    label("loc_4416")


    ChrTalk(
        0xFE,
        "The VIPs visit from every country, the inauguration...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At the Trade Conference\x01",
            "I must not let good chances\x01",
            "to take pictures pass me by.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44A8")

    Jump("loc_476A")

    label("loc_44AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4573")

    ChrTalk(
        0xFE,
        (
            "Hm, as I thought, even a rain scenery is nice,\x01",
            "having a different charm than usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Photographing on a rainy weather\x01",
            "requires considerable technique, but...\x01",
            "This too is fun.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_476A")

    label("loc_4573")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_476A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4691")

    ChrTalk(
        0xFE,
        (
            "At the West Crossbell Highway\x01",
            "there is a place called\x01",
            ""Knox Woodlands".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's a location that appears\x01",
            "to be nice for taking pictures,\x01",
            "with lots of trees growing thickly...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But because it's the Police Academy\x01",
            "site, common people can't go inside.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_476A")

    label("loc_4691")


    ChrTalk(
        0xFE,
        (
            "Taking pictures is my hobby.\x01",
            "I search for good photographic subjects\x01",
            "and then set out to many different places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            ""Knox Woodlands" can't be\x01",
            "accessed by common people, but\x01",
            "one day I'd like to go photograph it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_476A")

    TalkEnd(0xFE)
    Return()

    # Function_19_3582 end

    def Function_20_476E(): pass

    label("Function_20_476E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_48E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_485F")

    ChrTalk(
        0xFE,
        (
            "It's been awhile since I came\x01",
            "to drink coffee at "Morges".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How to say...\x01",
            "It would be nice if, from now on, Crossbell\x01",
            "gradually went back to normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Of course I'm worried\x01",
            "about that giant tree.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_48E4")

    label("loc_485F")


    ChrTalk(
        0xFE,
        (
            "It would be nice if, from now on, Crossbell\x01",
            "gradually went back to normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Of course I'm worried\x01",
            "about that giant tree.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48E4")

    Jump("loc_52EA")

    label("loc_48E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_48F7")
    Jump("loc_52EA")

    label("loc_48F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4A18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49E0")

    ChrTalk(
        0xFE,
        (
            "I too was shocked at the lately\x01",
            "Crossbell Times articles, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I didn't think they spoke\x01",
            "that much in hostility against \x01",
            "the two major powers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Crossbell situation from\x01",
            "now on worries me...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4A13")

    label("loc_49E0")


    ChrTalk(
        0xFE,
        (
            "Crossbell situation from\x01",
            "now on worries me...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A13")

    Jump("loc_52EA")

    label("loc_4A18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4ADF")

    ChrTalk(
        0xFE,
        (
            "The fact that around here there\x01",
            "was almost no damage is a\x01",
            "blessing in disguise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, the Governmental District and the\x01",
            "Waterfront Area were especially in a bad state...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52EA")

    label("loc_4ADF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4B3F")

    ChrTalk(
        0xFE,
        (
            "An occupation by an armed group...?\x01",
            "I'm worried about the people of Mainz...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52EA")

    label("loc_4B3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4B4D")
    Jump("loc_52EA")

    label("loc_4B4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4B8A")

    ChrTalk(
        0xFE,
        (
            "Today I could spot a\x01",
            "lot of ambulances...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52EA")

    label("loc_4B8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4C16")

    ChrTalk(
        0xFE,
        (
            "Hide and seek, eh...?\x01",
            "Back in the day, I did a lot too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Looking at children playing, it\x01",
            "puts me in a pleasant mood.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52EA")

    label("loc_4C16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4DCC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D37")

    ChrTalk(
        0xFE,
        (
            "Pros and cons of the Crossbell independence\x01",
            "the Mayor proposed...\x01",
            "That's a complex problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe I'll ask for Pluna\x01",
            "and Lenalee's opinions too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...No, it's better I don't.\x01",
            "Those two don't look like to be\x01",
            "thinking too much seriously about it...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4DC7")

    label("loc_4D37")


    ChrTalk(
        0xFE,
        (
            "Pros and cons of Crossbell independence...\x01",
            "That's a complex problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess I'll read Crossbell Times\x01",
            "and try to speculate about it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DC7")

    Jump("loc_52EA")

    label("loc_4DCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4EB2")

    ChrTalk(
        0xFE,
        (
            "It appears that today the "Imperial Chronicle"\x01",
            "and Remiferia's "Ardent Press" went to get \x01",
            "materials at the conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems I might as well read\x01",
            "and compare many written\x01",
            "articles with Crossbell Times.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52EA")

    label("loc_4EB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_4F60")

    ChrTalk(
        0xFE,
        (
            "Spacing out at the cafe reading\x01",
            "a book, it's become this late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*brrr*...\x01",
            "It's really chill at night. I guess I'll go \x01",
            "back home so to not get a cold.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52EA")

    label("loc_4F60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5063")

    ChrTalk(
        0xFE,
        (
            "They say that Archduke Albert of\x01",
            "Remiferia is the number sponsor\x01",
            "who greatly invest in St. Ursula.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In particular, it appears that Chairman MacDowell \x01",
            "has been having a friendly fellowship with the \x01",
            "Archduke since in the past, you see.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52EA")

    label("loc_5063")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5264")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5197")

    ChrTalk(
        0xFE,
        (
            "The West Zemuria Trade Conference...\x01",
            "Lately it's often featured\x01",
            "in Crossbell times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They say it's for discussing economics\x01",
            "relationships, but I wonder what kind of\x01",
            "topics will be brought up for discussion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, I guess I'll ask teacher\x01",
            "Marble for details next time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_525F")

    label("loc_5197")


    ChrTalk(
        0xFE,
        (
            "The West Zemuria Trade Conference...\x01",
            ""Economics relationships" is a mouthful, but I\x01",
            "wonder what kind of things will be discussed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, I guess I'll ask teacher\x01",
            "Marble for details next time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_525F")

    Jump("loc_52EA")

    label("loc_5264")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5272")
    Jump("loc_52EA")

    label("loc_5272")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_52EA")

    ChrTalk(
        0xFE,
        (
            "Today Sunday School is going\x01",
            "to be held in the evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I must bring my homework without forgetting.\x02",
    )

    CloseMessageWindow()

    label("loc_52EA")

    TalkEnd(0xFE)
    Return()

    # Function_20_476E end

    def Function_21_52EE(): pass

    label("Function_21_52EE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5365")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_530C")
    Call(0, 17)
    Jump("loc_5360")

    label("loc_530C")


    ChrTalk(
        0xFE,
        (
            "I'll help all the people of the city who\x01",
            "are in trouble with Ryｹ and Henri...!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5360")

    Jump("loc_561B")

    label("loc_5365")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5373")
    Jump("loc_561B")

    label("loc_5373")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5381")
    Jump("loc_561B")

    label("loc_5381")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_538F")
    Jump("loc_561B")

    label("loc_538F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_53C8")

    ChrTalk(
        0xFE,
        (
            "O-Oh...\x01",
            "I'm no good at playing tag...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_561B")

    label("loc_53C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_53D6")
    Jump("loc_561B")

    label("loc_53D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5487")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5448")

    ChrTalk(
        0xFE,
        "I've finally found Henri...!\x01\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A-All right...\x01",
            "Next, I have to\x01",
            "look for Ryｹ...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5482")

    label("loc_5448")


    ChrTalk(
        0xFE,
        (
            "But I really don't know where\x01",
            "Ryｹ could be hiding...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5482")

    Jump("loc_561B")

    label("loc_5487")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5550")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_551E")

    ChrTalk(
        0xFE,
        (
            "I'm playing hide and seek\x01",
            "with Ryｹ and Henri...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...But I can't find them at all...\x01",
            "Where could they be hiding...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_554B")

    label("loc_551E")


    ChrTalk(
        0xFE,
        (
            "Where could Ryｹ and\x01",
            "Henri be hiding...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_554B")

    Jump("loc_561B")

    label("loc_5550")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_555E")
    Jump("loc_561B")

    label("loc_555E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_556C")
    Jump("loc_561B")

    label("loc_556C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_557A")
    Jump("loc_561B")

    label("loc_557A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5588")
    Jump("loc_561B")

    label("loc_5588")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5604")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55A3")
    Call(0, 16)
    Jump("loc_55FF")

    label("loc_55A3")


    ChrTalk(
        0xFE,
        (
            "Tomorrow I'm going to meet with\x01",
            "everyone at the department store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I can't wait...\x02",
    )

    CloseMessageWindow()

    label("loc_55FF")

    Jump("loc_561B")

    label("loc_5604")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5612")
    Jump("loc_561B")

    label("loc_5612")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_561B")

    label("loc_561B")

    TalkEnd(0xFE)
    Return()

    # Function_21_52EE end

    def Function_22_561F(): pass

    label("Function_22_561F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5630")
    Jump("loc_5CC8")

    label("loc_5630")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_563E")
    Jump("loc_5CC8")

    label("loc_563E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_564C")
    Jump("loc_5CC8")

    label("loc_564C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_565A")
    Jump("loc_5CC8")

    label("loc_565A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_56FA")

    ChrTalk(
        0xFE,
        (
            "Who would've thought something like the \x01",
            "mining town occupation to happen...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Somehow it makes me uneasy...\x01",
            "Isn't Momo back home yet...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CC8")

    label("loc_56FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5708")
    Jump("loc_5CC8")

    label("loc_5708")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_578A")

    ChrTalk(
        0xFE,
        (
            "It seems that ambulances have been going\x01",
            "many times back and forth since before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Did something happen...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5CC8")

    label("loc_578A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5803")

    ChrTalk(
        0xFE,
        (
            "Mr. Grimwood looks like\x01",
            "to be very busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Today too is going in and\x01",
            "out of his office repeatedly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CC8")

    label("loc_5803")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_58D2")

    ChrTalk(
        0xFE,
        (
            "After the Trade Conference I\x01",
            "talked many times seriously\x01",
            "about it with my husband.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is a problem that has to do\x01",
            "with all of us Crossbell citizens.\x01",
            "We must think about it seriously.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CC8")

    label("loc_58D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_58E0")
    Jump("loc_5CC8")

    label("loc_58E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_58EE")
    Jump("loc_5CC8")

    label("loc_58EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5A0D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59A3")

    ChrTalk(
        0xFE,
        "Welcooome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Momo and the others went to\x01",
            "the inauguration ceremony today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, when she comes home,\x01",
            "I'll have to ask her a lot of things.\x01\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5A08")

    label("loc_59A3")


    ChrTalk(
        0xFE,
        (
            "Momo and the others went to\x01",
            "the inauguration ceremony today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uh uh, I hope they have fun.\x01\x02",
    )

    CloseMessageWindow()

    label("loc_5A08")

    Jump("loc_5CC8")

    label("loc_5A0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5C0D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B6F")

    ChrTalk(
        0xFE,
        (
            "On the other day when it was raining,\x01",
            "I was worried about Momo who wasn't\x01",
            "coming back at all from an errand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I asked her about it, she said she\x01",
            "was looking for the umbrella she had lost.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That Momo, I can buy her a\x01",
            "replacement for that, and yet...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's quite the cheap thing to\x01",
            "make me worry about her.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5C08")

    label("loc_5B6F")


    ChrTalk(
        0xFE,
        (
            "Still, treasuring things is\x01",
            "a very good mentality.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's not good she made me worry,\x01",
            "but I'd like for Momo to always\x01",
            "have that mental attitude.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C08")

    Jump("loc_5CC8")

    label("loc_5C0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5C1B")
    Jump("loc_5CC8")

    label("loc_5C1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5CC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C76")

    ChrTalk(
        0xFE,
        "Welcooome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We're "Tallys'", supporters\x01",
            "of this area!\x01\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5CC8")

    label("loc_5C76")


    ChrTalk(
        0xFE,
        (
            "Momo has gone to\x01",
            "Sunday School, so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We have to do our\x01",
            "best with work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CC8")

    TalkEnd(0xFE)
    Return()

    # Function_22_561F end

    def Function_23_5CCC(): pass

    label("Function_23_5CCC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5CDD")
    Jump("loc_646D")

    label("loc_5CDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5CEB")
    Jump("loc_646D")

    label("loc_5CEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5D97")

    ChrTalk(
        0xFE,
        (
            "From the morning you could see many orbal\x01",
            "cars heading towards the borders gates.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It looks like the foreign residents\x01",
            "went back to their countries.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_646D")

    label("loc_5D97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5DA5")
    Jump("loc_646D")

    label("loc_5DA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5DB3")
    Jump("loc_646D")

    label("loc_5DB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5DC1")
    Jump("loc_646D")

    label("loc_5DC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5F74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5ECA")

    ChrTalk(
        0xFE,
        (
            "I've just come back from driving\x01",
            "to the Bellguard Gate area...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "On the way home, I caught sight\x01",
            "of the West Crossbell Highway scene\x01",
            "accident being in a great turmoil...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I never dreamed of a derailment\x01",
            "of such grand scale...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5F6F")

    label("loc_5ECA")


    ChrTalk(
        0xFE,
        (
            "On the way home, I caught sight\x01",
            "of the West Crossbell Highway scene\x01",
            "incident being in a great turmoil...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It was fully crowded with\x01",
            "police and the CGF too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F6F")

    Jump("loc_646D")

    label("loc_5F74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5F82")
    Jump("loc_646D")

    label("loc_5F82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5F90")
    Jump("loc_646D")

    label("loc_5F90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5F9E")
    Jump("loc_646D")

    label("loc_5F9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_5FAC")
    Jump("loc_646D")

    label("loc_5FAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_619C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60E9")

    ChrTalk(
        0xFE,
        (
            "My old woman is angry and\x01",
            "is not saying a word at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although I said to go see together the\x01",
            "long awaited inauguration ceremony,\x01",
            "but she ignored me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Drinking that wine with fireworks served\x01",
            "as "snacks" would've been the best, but...\x01",
            "Honestly, I can't understand her tastes.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6197")

    label("loc_60E9")


    ChrTalk(
        0xFE,
        (
            "Hmph, come on.\x01",
            "Just because I did a costly purchase, for\x01",
            "how long does she intend to be springy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If my old woman is in the mood\x01",
            "to do that, I too can ignore her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6197")

    Jump("loc_646D")

    label("loc_619C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_61AA")
    Jump("loc_646D")

    label("loc_61AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_61B8")
    Jump("loc_646D")

    label("loc_61B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_646D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6407")

    ChrTalk(
        0xFE,
        (
            "Hoh hoh ho, as expected,\x01",
            "orbal cars are nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My old woman grumbled that\x01",
            "it's a useless waste, but buying\x01",
            "it was the right thing to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FA Verne orbal car...\x01",
            "It has a chic design and\x01",
            "I think it's amazing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hoo, well, well...\x01",
            "Although still young, you're understanding...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6340")
    OP_63(0x109, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)

    label("loc_6340")

    Sleep(1000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6369")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_6369")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_638F")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_638F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_63B5")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_63B5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_63DB")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_63DB")

    Sleep(1000)

    ChrTalk(
        0x101,
        "#00012F(Kindred spirits...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_646D")

    label("loc_6407")


    ChrTalk(
        0xFE,
        (
            "Driving in this orbal car\x01",
            "is really the best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd like my old woman to\x01",
            "understand this too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_646D")

    TalkEnd(0xFE)
    Return()

    # Function_23_5CCC end

    def Function_24_6471(): pass

    label("Function_24_6471")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6482")
    Jump("loc_64C8")

    label("loc_6482")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_64C8")

    ChrTalk(
        0xFE,
        (
            "Somehow it's uneasy...\x01",
            "Could an accident have happened?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_64C8")

    TalkEnd(0xFE)
    Return()

    # Function_24_6471 end

    def Function_25_64CC(): pass

    label("Function_25_64CC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_64DD")
    Jump("loc_6518")

    label("loc_64DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6518")

    ChrTalk(
        0xFE,
        "I don't quite like the ambulances' sounds...\x02",
    )

    CloseMessageWindow()

    label("loc_6518")

    TalkEnd(0xFE)
    Return()

    # Function_25_64CC end

    def Function_26_651C(): pass

    label("Function_26_651C")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "When I saw the derailed train\x01",
            "I couldn't believe my eyes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems that there were\x01",
            "many injured people...\x01",
            "I wonder if they're fine...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_651C end

    def Function_27_65B3(): pass

    label("Function_27_65B3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6659")

    ChrTalk(
        0xFE,
        (
            "Jeez, the inside of\x01",
            "my shoes got soaked\x01",
            "in the blink of an eye!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's why I hate rain. I must finish \x01",
            "fast what I have to do and go home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_66E0")

    label("loc_6659")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_66E0")

    ChrTalk(
        0xFE,
        (
            "Aah, jeez...stupid rain!\x01",
            "There's nothing more depressing than it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I must finish fast what I have to do and go home.\x02",
    )

    CloseMessageWindow()

    label("loc_66E0")

    TalkEnd(0xFE)
    Return()

    # Function_27_65B3 end

    def Function_28_66E4(): pass

    label("Function_28_66E4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6835")

    ChrTalk(
        0xFE,
        (
            "Such an incident\x01",
            "happened, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although poorly, we're made\x01",
            "guard the city like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For instance, if the Empire were the\x01",
            "culprit, I think there would be a low\x01",
            "possibility for being attacked immediately...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At any rate, we can't let our\x01",
            "guard down until the local\x01",
            "referendum three days from now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_6911")

    label("loc_6835")


    ChrTalk(
        0xFE,
        (
            "For instance, if the Empire were the\x01",
            "culprit, I think there would be a low\x01",
            "possibility for being attacked immediately...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At any rate, we can't let our\x01",
            "guard down until the local\x01",
            "referendum three days from now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6911")

    TalkEnd(0xFE)
    Return()

    # Function_28_66E4 end

    def Function_29_6915(): pass

    label("Function_29_6915")

    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#00005FChief Sergei looks like to be making\x01",
            "something at the Support Section...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FAt any rate, it would be\x01",
            "better to not pass from here.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_29_6915 end

    def Function_30_69B4(): pass

    label("Function_30_69B4")

    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It looks like the door is closed tightly.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x95, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A13")
    TalkEnd(0xFF)
    Call(0, 31)
    Return()

    label("loc_6A13")

    TalkEnd(0xFF)
    Return()

    # Function_30_69B4 end

    def Function_31_6A17(): pass

    label("Function_31_6A17")

    EventBegin(0x0)
    Fade(1000)
    OP_68(15530, 4300, 15700, 0)
    MoveCamera(60, 14, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13270, 0)
    SetChrPos(0x101, 15530, 3000, 15700, 90)
    SetChrPos(0x102, 14820, 3000, 16800, 90)
    SetChrPos(0x103, 13710, 3000, 16700, 90)
    SetChrPos(0x104, 12510, 3000, 15490, 90)
    SetChrPos(0xF4, 13100, 3000, 14500, 90)
    SetChrPos(0xF5, 14690, 3000, 14290, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#6P#00008F............\x02\x03",
            "#00003F(What Pete, Mr. Quint and\x01",
            "Mr. Nielsen said before...)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6B47")
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    label("loc_6B47")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6B6D")
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    label("loc_6B6D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6B93")
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    label("loc_6B93")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6BB9")
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    label("loc_6BB9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6BDF")
    OP_63(0x4, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    label("loc_6BDF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6C05")
    OP_63(0x5, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    label("loc_6C05")

    Sleep(1000)

    def lambda_6C0D():
        TurnDirection(0x102, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6C0D)
    Sleep(50)

    def lambda_6C1D():
        TurnDirection(0x103, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6C1D)

    def lambda_6C2A():
        TurnDirection(0x104, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6C2A)
    Sleep(50)

    def lambda_6C3A():
        TurnDirection(0xF4, 0x101, 300)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_6C3A)
    Sleep(50)

    def lambda_6C4A():
        TurnDirection(0xF5, 0x101, 300)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_6C4A)
    WaitChrThread(0xF5, 2)

    ChrTalk(
        0x102,
        "#6P#00105FLloyd...is something wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FIs something the matter with\x01",
            "Lawyer Ian's office?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00301FIt looks like to be out now...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(300)
    OP_93(0x101, 0x111, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#11P#00006F...No, it's nothing.\x01",
            "Let's go now.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6D72")

    ChrTalk(
        0x10A,
        "#12P#00605F............\x02",
    )

    CloseMessageWindow()

    label("loc_6D72")

    OP_5A()
    SetScenarioFlags(0x1BE, 0)
    OP_2C(0xB1, 0x3)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_31_6A17 end

    def Function_32_6D92(): pass

    label("Function_32_6D92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6DA9")
    Call(0, 49)
    Return()

    label("loc_6DA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6DBB")
    Call(0, 50)
    Return()

    label("loc_6DBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E32")

    ChrTalk(
        0x101,
        (
            "#00000FWe don't have any business to go out the city.\x01",
            "Also, it doesn't seem we need to use the car.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    label("loc_6E32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F37")
    CreatePortrait(0, 67, 20, 547, 276, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis241.itp")
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※You became able to use the Support Section car.\x02",
        )
    )

    CloseMessageWindow()
    Sound(18, 0, 100, 0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_57(0x3)
    OP_CB(0x0, 0x3, 0x80FFFFFF, 0x1F4, 0x0, 0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    SetScenarioFlags(0x12B, 2)
    SetScenarioFlags(0x31, 1)
    OP_C9(0x1, 0x200000)

    label("loc_6F37")

    SetMapFlags(0x80)
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F52")
    Jump("loc_6FC2")

    label("loc_6F52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F61")
    Jump("loc_6FC2")

    label("loc_6F61")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F7C")
    SetScenarioFlags(0x31, 2)

    label("loc_6F7C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6FC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_6FBC")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6FB1")
    Sound(2499, 255, 100, 0)
    Jump("loc_6FB7")

    label("loc_6FB1")

    Sound(3537, 255, 100, 0)

    label("loc_6FB7")

    Jump("loc_6FC2")

    label("loc_6FBC")

    Sound(3344, 255, 100, 0)

    label("loc_6FC2")

    SetMapObjFrame(0xA, "light", 0x0, 0x1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6FD9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7415")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_704C")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Merkabah")
    MenuCmd(1, 0, "Quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_702C"),
        (SWITCH_DEFAULT, "loc_703D"),
    )


    label("loc_702C")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_7047")

    label("loc_703D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7047")

    Jump("loc_7410")

    label("loc_704C")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Use Orbal Car")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_70A6")
    MenuCmd(1, 0, "Rest in Orbal Car")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_70A6")

    MenuCmd(1, 0, "Customize Orbal Car")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    MenuCmd(1, 0, "Quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_737B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_717D")

    ChrTalk(
        0x101,
        (
            "#00003FWith this, we could secure the orbal car.\x02\x03",
            "#00001FFor now, let's head to the station\x01",
            "before the operation starts.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7376")

    label("loc_717D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_71FF")

    ChrTalk(
        0x101,
        (
            "#00001FAnyhow, we must chase after Randy...\x01",
            "Let's perform a thorough search\x01",
            "inside the city first of all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7376")

    label("loc_71FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7277")

    ChrTalk(
        0x101,
        (
            "#00000FWe don't have any business to go out the city.\x01",
            "Also, it doesn't seem we need to use the car.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7376")

    label("loc_7277")

    SetMapObjFrame(0xA, "light", 0x0, 0x1)
    OP_74(0xA, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_72A8")
    OP_70(0xA, 0x12C)
    OP_71(0xA, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_72B8")

    label("loc_72A8")

    OP_70(0xA, 0xF0)
    OP_71(0xA, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_72B8")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_730E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_730E")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7331")
    Sound(461, 0, 100, 0)

    label("loc_7331")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7351")
    OP_70(0xA, 0x14A)
    OP_71(0xA, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_7361")

    label("loc_7351")

    OP_70(0xA, 0x10E)
    OP_71(0xA, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_7361")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0xA, "light", 0x1, 0x1)
    OP_70(0xA, 0x0)

    label("loc_7376")

    Jump("loc_7410")

    label("loc_737B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73F1")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_73B4")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_73CC")

    label("loc_73B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_73C7")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_73CC")

    label("loc_73C7")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_73CC")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7410")

    label("loc_73F1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7406")
    Call(0, 33)
    Jump("loc_7410")

    label("loc_7406")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7410")

    Jump("loc_6FD9")

    label("loc_7415")

    SetMapObjFrame(0xA, "light", 0x1, 0x1)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_32_6D92 end

    def Function_33_742B(): pass

    label("Function_33_742B")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF000000), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x0)
    SetChrFlags(0x0, 0x8)
    SetChrFlags(0x1, 0x8)
    SetChrFlags(0x2, 0x8)
    SetChrFlags(0x3, 0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7471")
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    label("loc_7471")

    SetMapObjFrame(0xFF, "main7", 0x0, 0x1)
    MiniGame(0x33, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFrame(0xFF, "main7", 0x1, 0x1)
    ClearChrFlags(0x0, 0x8)
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_74DA")
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_74DA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventEnd(0x5)
    SetMapFlags(0x80)
    Return()

    # Function_33_742B end

    def Function_34_74EC(): pass

    label("Function_34_74EC")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_7547")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_753C")
    Sound(2502, 255, 100, 0)
    Jump("loc_7542")

    label("loc_753C")

    Sound(2503, 255, 100, 0)

    label("loc_7542")

    Jump("loc_756B")

    label("loc_7547")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7565")
    Sound(3347, 255, 100, 0)
    Jump("loc_756B")

    label("loc_7565")

    Sound(3348, 255, 100, 0)

    label("loc_756B")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_34_74EC end

    def Function_35_7580(): pass

    label("Function_35_7580")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    OP_68(40100, -2850, -19150, 0)
    MoveCamera(50, 30, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(18000, 0)
    OP_68(25400, -2250, -16450, 10000)
    MoveCamera(40, 30, 0, 10000)
    SetCameraDistance(24000, 10000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("c0180", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_35_7580 end

    def Function_36_762B(): pass

    label("Function_36_762B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x1A5, 0x4)
    SetChrPos(0x101, 43000, -4000, -18500, 270)
    SetChrPos(0x102, 43200, -4000, -19600, 270)
    SetChrPos(0x105, 44200, -4000, -18500, 270)
    SetChrPos(0x109, 44400, -4000, -19600, 270)
    SetChrPos(0x1A5, 46400, -4000, -19000, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1A5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(20000, -1500, -18000, 0)
    MoveCamera(45, 33, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(25000, 0)
    OP_68(28000, -1500, -18000, 6000)
    SetCameraDistance(23000, 6000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    ClearMapObjFlags(0x5, 0x10)
    OP_71(0x5, 0x0, 0xA, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x5)
    Fade(500)
    OP_68(39500, -3100, -19000, 0)
    MoveCamera(53, 25, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(19000, 0)
    SetCameraDistance(18000, 2500)

    def lambda_778C():
        OP_97(0x101, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_778C)
    Sleep(100)

    def lambda_77A9():
        OP_97(0x102, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_77A9)
    Sleep(300)

    def lambda_77C6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_77C6)
    Sleep(100)

    def lambda_77DA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_77DA)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x101, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    WaitChrThread(0x102, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_7827():
        OP_97(0x105, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7827)
    Sleep(100)

    def lambda_7844():
        OP_97(0x109, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7844)
    Sleep(100)

    def lambda_7861():
        OP_97(0x1A5, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A5, 0, lambda_7861)
    Sleep(800)

    def lambda_787E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_787E)
    Sleep(100)

    def lambda_7892():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7892)
    Sleep(1000)

    def lambda_78A6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A5, 2, lambda_78A6)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00005F#5PThis is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00105FW-When was it...?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x109,
        (
            "#10105F#11POh, was the Support Section\x01",
            "back entrance like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#5PYeah, it indeed seems\x01",
            "it's under construction.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x1A5, 0)

    ChrTalk(
        0x1A5,
        (
            "#11P#01105FOh, that's right.\x01",
            "You guys don't know about it.\x02\x03",
            "#01100FYou see, after you went on your business trip, \x01",
            "Lloyd, construction workers came here.\x02\x03",
            "It seems Chief called them.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7A40():
        TurnDirection(0x101, 0x1A5, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7A40)
    Sleep(50)

    def lambda_7A50():
        TurnDirection(0x102, 0x1A5, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_7A50)
    Sleep(50)

    def lambda_7A60():
        TurnDirection(0x105, 0x1A5, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7A60)
    Sleep(50)

    def lambda_7A70():
        TurnDirection(0x109, 0x1A5, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7A70)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x101,
        (
            "#6P#00006FIs that so...?\x01",
            "I didn't notice yesterday.\x02\x03",
            "#00001FStill, what does the\x01",
            "Chief intend to do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103FUhhm, I think this construction\x01",
            "has some kind of meaning...\x02\x03",
            "#00100FIn any case, it seems it would be\x01",
            "better to not pass through here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FYeah, let's go out from the 1F entranceway.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x1A5, 0x4)
    SetScenarioFlags(0x126, 3)
    EventEnd(0x5)
    NewScene("c0110", 108, 0, 0)
    IdleLoop()
    Return()

    # Function_36_762B end

    def Function_37_7BFA(): pass

    label("Function_37_7BFA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02500.itc", 0x1E)
    LoadChrToIndex("chr/ch02710.itc", 0x1F)
    LoadChrToIndex("apl/ch51107.itc", 0x20)
    SoundLoad(468)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01200.itp")
    OP_68(18000, 1660, -9000, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, 19000, 0, -8600, 180)
    SetChrPos(0x102, 19000, 0, -8600, 180)
    SetChrPos(0x109, 19000, 0, -8600, 180)
    SetChrPos(0x105, 19000, 0, -8600, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x14, 0x1E)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 19000, 0, -8600, 180)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x15, 0x20)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 12500, 0, 500, 270)
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x16, 0x1F)
    SetChrFlags(0x16, 0x20)
    SetChrFlags(0x16, 0x2)
    SetChrSubChip(0x16, 0x29)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 42450, 2400, -22230, 315)
    SetChrFlags(0x16, 0x8)
    ClearChrFlags(0x8, 0x80)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 10050, 0, -8400, 90)
    SetChrFlags(0x8, 0x8)
    ClearChrFlags(0x9, 0x80)
    OP_4B(0x9, 0xFF)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 9350, 0, -6250, 90)
    SetChrFlags(0x9, 0x8)
    ClearChrFlags(0x19, 0x80)
    OP_78(0xA, 0x19)
    OP_49()
    SetChrPos(0x19, -36200, 0, 4000, 90)
    OP_D5(0x19, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xA, 0x1000)
    SetMapObjFrame(0xA, "light", 0x0, 0x1)
    OP_74(0xA, 0x1E)
    OP_71(0xA, 0x79, 0xB4, 0x1, 0x20)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFF, 0xCF, 0xB5, 0x23, 0x96, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tuika_mul", 0x1, 0x1)
    SetMapObjFrame(0xFF, "tuika", 0x1, 0x1)
    SetMapObjFrame(0xFF, "window01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "tuika2_mul", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kabuse", 0x0, 0x1)
    SetMapObjFlags(0xC, 0x4)
    SetChrFlags(0xB, 0x8)
    FadeToBright(1000, 0)
    Sound(468, 2, 80, 0)
    Sound(457, 0, 100, 0)
    BeginChrThread(0x19, 3, 0, 38)
    OP_68(-27750, 4250, 6400, 0)
    MoveCamera(69, 0, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(16000, 0)
    OP_68(-27750, 1250, 6400, 7500)
    OP_6F(0x79)
    OP_0D()
    Sleep(1000)
    Fade(1000)
    EndChrThread(0x19, 0x3)
    Sound(459, 0, 100, 0)
    BeginChrThread(0x19, 3, 0, 39)
    BeginChrThread(0x1A, 1, 0, 45)
    OP_68(1950, 2350, -8400, 0)
    MoveCamera(22, 26, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13650, 0)
    OP_68(18950, 2350, -8400, 7500)
    MoveCamera(22, 7, 0, 7500)
    OP_6F(0x79)
    WaitChrThread(0x19, 3)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        "#00005F#5PAh...!\x02",
    )

    CloseMessageWindow()
    OP_68(23200, 450, -21750, 3500)
    MoveCamera(30, 26, 0, 3500)
    OP_6E(700, 3500)
    SetCameraDistance(19850, 3500)
    OP_6F(0x79)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(462, 0, 100, 0)
    Sleep(1000)
    OP_68(19430, 800, -10000, 0)
    MoveCamera(30, 19, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14350, 0)
    FadeToBright(1000, 0)
    OP_68(19430, 800, -8970, 2000)
    SetChrPos(0x101, 19600, 0, -10400, 180)
    SetChrPos(0x102, 20900, 0, -9500, 180)
    SetChrPos(0x109, 19600, 0, -9050, 180)
    SetChrPos(0x105, 18300, 0, -9950, 180)
    SetChrPos(0x14, 17550, 0, -8850, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_70(0xA, 0x10E)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x14,
        "#01002F#5PYeah, they did a good job.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#5PChief, what's that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#5PIs that for\x01",
            "the orbal car?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#01004F#5PYeah, they constructed this\x01",
            "driveway and added a parking space.\x02\x03",
            "#01004FAnd using HQ\x01",
            "funds, no less.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102F#5PIncredible!\x02\x03",
            "#10109FThere's even enough space\x01",
            "to service it right here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#5PLife with an orbal car, huh. There\x01",
            "are a lot of benefits to owning one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#5PHa ha, I think KeA\x01",
            "will be thrilled.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x8)
    ClearChrFlags(0x9, 0x8)

    NpcTalk(
        0x8,
        "Boy's Voice",
        "Woah! What's that!?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Boy's Voice",
        "What a nice car...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x14, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_8331():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8331)
    Sleep(50)

    def lambda_8341():
        OP_93(0x109, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8341)
    Sleep(50)

    def lambda_8351():
        OP_93(0x105, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8351)
    Sleep(50)

    def lambda_8361():
        OP_93(0x102, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8361)
    Sleep(50)

    def lambda_8371():
        OP_93(0x14, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_8371)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x14, 0)
    Fade(500)
    OP_68(13350, 800, -8750, 0)
    MoveCamera(30, 23, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(15800, 0)
    OP_68(18150, 800, -8750, 3000)
    SetCameraDistance(13800, 3000)

    def lambda_83E2():
        OP_96(0xFE, 0x3C8C, 0x0, 0xFFFFDAE4, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_83E2)

    def lambda_83FC():
        OP_96(0xFE, 0x3BC4, 0x0, 0xFFFFE08E, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_83FC)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        "#00002F#11POh, hey there Ryｹ and Henri.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109F#11PHa ha, we meet again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PSweet! I've never\x01",
            "seen a car like this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PWait...did you\x01",
            "guys buy it?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#11POf course not.\x02\x03",
            "#00002FBut it was loaned to us\x01",
            "for use on SSS business.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        "#6PS-Seriously!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PDid you guys get a\x01",
            "promotion or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#11PI wouldn't say it's a\x01",
            "promotion, exactly...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00000F#11PBut wait, is KeA not\x01",
            "with you guys today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F#11PIs she walking\x01",
            "home with Momo?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#6PNot a clue.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PWe didn't leave Sunday\x01",
            "School together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#11PHuh, really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PKeA said she had something to do with\x01",
            "Sister Marble and stayed behind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PSo she might still\x01",
            "be at the cathedral.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#11PI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#11PI wonder if there's something wrong...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)

    def lambda_87D8():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_87D8)
    Sleep(50)

    def lambda_87E8():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_87E8)
    Sleep(50)

    def lambda_87F8():
        TurnDirection(0x14, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_87F8)
    Sleep(50)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x14, 0)
    OP_64(0x101)
    OP_64(0x102)

    ChrTalk(
        0x105,
        (
            "#10302F#6POh boy, you guys are as\x01",
            "overprotective as ever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109F#5PCan you blame them?\x01",
            "KeA is just so adorable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#11PN-No, I don't think\x01",
            "that's the only reason...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00112F#11PIt's common sense for us to\x01",
            "worry; we're her guardians.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#01004F#6PIf you're that worried, why not head\x01",
            "over to the cathedral and pick her up?\x02\x03",
            "#01002FNow that you've got your own wheels.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00000F#11POh yeah, good point.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x109, 500)

    ChrTalk(
        0x102,
        "#00102F#11PNoｱl, can we count on you?\x02",
    )

    CloseMessageWindow()

    def lambda_8A21():
        TurnDirection(0x101, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8A21)
    Sleep(50)

    def lambda_8A31():
        TurnDirection(0x105, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8A31)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x109,
        "#10102F#5PYes, no problem at all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PNo way, you're going\x01",
            "to pick up KeA?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PMe too me too!\x01",
            "Let me ride too!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8AC6():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8AC6)
    Sleep(15)

    def lambda_8AD6():
        OP_93(0x102, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8AD6)
    Sleep(15)

    def lambda_8AE6():
        OP_93(0x109, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8AE6)
    Sleep(15)

    def lambda_8AF6():
        OP_93(0x105, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8AF6)
    Sleep(15)

    def lambda_8B06():
        OP_93(0x14, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_8B06)
    Sleep(15)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x14, 0)
    OP_63(0x9, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x9, 0x8, 500)

    ChrTalk(
        0x9,
        "#5PH-Hey, Ryｹ!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PYour father told you to\x01",
            "head back soon, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)

    ChrTalk(
        0x8,
        "#12PAww, I forgot about that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PSis is back home\x01",
            "today after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#11PHa ha, well it sounds like you had\x01",
            "better head home right away.\x02\x03",
            "#00002FDon't worry, we'll\x01",
            "give you a ride soon.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8C64():
        OP_93(0x8, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_8C64)
    Sleep(50)

    def lambda_8C74():
        OP_93(0x9, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_8C74)
    Sleep(50)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x9, 0)

    ChrTalk(
        0x8,
        "#6PIt's a promise!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PWell then\x01",
            "we're going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109F#11PRight. Take care, you two.\x02",
    )

    CloseMessageWindow()

    def lambda_8CEE():
        OP_93(0x8, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_8CEE)
    Sleep(50)

    def lambda_8CFE():
        OP_93(0x9, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_8CFE)
    Sleep(50)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x9, 0)
    OP_68(19000, 800, -8750, 2500)

    def lambda_8D27():
        OP_96(0xFE, 0x2742, 0x0, 0xFFFFDF30, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8D27)
    Sleep(50)

    def lambda_8D44():
        OP_96(0xFE, 0x2486, 0x0, 0xFFFFE796, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8D44)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    OP_6F(0x79)
    OP_93(0x14, 0x87, 0x1F4)

    ChrTalk(
        0x14,
        (
            "#01003F#5PAlright, go pick\x01",
            "her up already.\x02\x03",
            "#01000FI'll be heading back now.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8DCB():
        TurnDirection(0x101, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8DCB)
    Sleep(50)

    def lambda_8DDB():
        TurnDirection(0x102, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8DDB)
    Sleep(50)

    def lambda_8DEB():
        TurnDirection(0x109, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8DEB)
    Sleep(50)

    def lambda_8DFB():
        TurnDirection(0x105, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8DFB)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        "#00000F#12POk, got it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F#11PThen, let's get going.\x02",
    )

    CloseMessageWindow()
    OP_68(19000, 800, -9350, 2500)

    def lambda_8E6F():
        OP_93(0xFE, 0xB4, 0x96)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8E6F)

    def lambda_8E7C():
        OP_93(0xFE, 0xB4, 0xFA)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_8E7C)

    def lambda_8E89():
        OP_93(0xFE, 0xB4, 0x96)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8E89)

    def lambda_8E96():
        OP_93(0xFE, 0xB4, 0x96)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8E96)
    OP_93(0x14, 0xB4, 0x1F4)
    OP_96(0x14, 0x43C6, 0x0, 0xFFFFD27E, 0x9C4, 0x1)
    OP_96(0x14, 0x4A38, 0xFFFFF9C0, 0xFFFFC022, 0x9C4, 0x1)
    SetChrFlags(0x14, 0x80)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x105, 2)
    OP_6F(0x79)

    ChrTalk(
        0x109,
        (
            "#10104F#5PRight, let's head\x01",
            "to the cathedral.\x02\x03",
            "#10100FFrom here, we should head to Central Square\x01",
            "and then through the Entertainment District.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8F7D():
        TurnDirection(0x101, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8F7D)
    Sleep(50)

    def lambda_8F8D():
        TurnDirection(0x102, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8F8D)
    Sleep(50)

    def lambda_8F9D():
        TurnDirection(0x105, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8F9D)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        (
            "#00002F#12PSounds good. We're counting on you!\x02\x03",
            "#00004FI can't wait to see the look on\x01",
            "KeA's face when she sees this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F#12PHa ha, she does really\x01",
            "love cars, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#6POh boy. You guys are\x01",
            "seriously doting parents.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(19000, 800, -6740, 6000)
    MoveCamera(45, 18, 0, 6000)
    Sleep(250)
    BeginChrThread(0x109, 3, 0, 44)
    Sleep(1000)
    BeginChrThread(0x105, 3, 0, 43)
    Sleep(1000)
    BeginChrThread(0x101, 3, 0, 41)
    Sleep(1000)
    BeginChrThread(0x102, 3, 0, 42)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x105, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x109, 3)
    OP_6F(0x79)
    Sound(461, 0, 100, 0)
    OP_71(0xA, 0x10F, 0x12C, 0x1, 0x8)
    Sleep(1000)
    Sleep(500)
    OP_68(11650, 1300, 450, 9000)
    MoveCamera(60, 21, 0, 9000)
    OP_6E(700, 9000)
    SetCameraDistance(16000, 9000)
    Sound(457, 0, 100, 0)
    BeginChrThread(0x19, 3, 0, 40)
    OP_6F(0x79)
    EndChrThread(0x19, 0x3)
    SetMapObjFlags(0xA, 0x4)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x4, 0x10)
    OP_71(0x4, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x4)
    Sleep(500)
    SetCameraDistance(20000, 8000)

    def lambda_9186():
        OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_9186)

    def lambda_919B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_919B)
    Sleep(1500)
    Sound(100, 0, 100, 0)
    OP_71(0x4, 0xA, 0x0, 0x0, 0x0)
    WaitChrThread(0x15, 1)
    WaitChrThread(0x15, 2)
    SetChrFlags(0x15, 0x80)
    StopBGM(0x1770)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    Fade(1000)
    ClearChrFlags(0x16, 0x8)
    OP_68(41750, 3600, -21850, 0)
    MoveCamera(340, 30, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(16000, 3000)
    OP_6F(0x79)
    OP_0D()
    Sleep(500)
    OP_63(0x16, 0xFFFFFE70, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x16)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    Sound(3053, 255, 100, 0)

    AnonymousTalk(
        0x16,
        "#30W......Groowl......\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    FadeToDark(1000, 0, -1)
    SetCameraDistance(15500, 2000)
    OP_6F(0x79)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x1D4)
    SetScenarioFlags(0x22, 1)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_37_7BFA end

    def Function_38_9303(): pass

    label("Function_38_9303")

    SetChrPos(0xFE, -36200, 0, 4000, 90)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -5850, 0, 4000)
    OP_9F(0x1, 800, 0, 1800)
    OP_9F(0x1, 8050, 0, -5950)
    OP_9F(0x1, 15500, 0, -6700)
    OP_9F(0x2, 0xFE, 5000, 0x6)
    Return()

    # Function_38_9303 end

    def Function_39_935A(): pass

    label("Function_39_935A")

    SetChrPos(0xFE, 1250, 0, -1000, 180)
    OP_D5(0x19, 0x0, 0x2BF20, 0x0, 0x0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 5000, 0, -5500)
    OP_9F(0x1, 9000, 0, -6750)
    OP_9F(0x1, 16000, 0, -6750)
    OP_9F(0x2, 0xFE, 4000, 0x6)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0xBB8, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x3E8, 0x1)
    OP_71(0xA, 0x5B, 0x78, 0x1, 0x8)
    Return()

    # Function_39_935A end

    def Function_40_93EF(): pass

    label("Function_40_93EF")

    SetChrPos(0xFE, 19000, 0, -6740, 90)
    OP_D5(0xFE, 0x0, 0x15F90, 0x0, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x190, 0x3E8, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x190, 0x5DC, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x190, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x190, 0x9C4, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x190, 0xBB8, 0x1)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 27150, 50, -6740)
    OP_9F(0x1, 51600, 3950, -6740)
    OP_9F(0x2, 0xFE, 3500, 0x6)
    Return()

    # Function_40_93EF end

    def Function_41_9488(): pass

    label("Function_41_9488")

    OP_95(0xFE, 19000, 0, -8600, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(200)

    def lambda_94AB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_94AB)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_41_9488 end

    def Function_42_94BC(): pass

    label("Function_42_94BC")

    OP_95(0xFE, 19000, 0, -8600, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(200)

    def lambda_94DF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_94DF)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_42_94BC end

    def Function_43_94F0(): pass

    label("Function_43_94F0")

    OP_95(0xFE, 19000, 0, -8600, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(200)

    def lambda_9513():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9513)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_43_94F0 end

    def Function_44_9524(): pass

    label("Function_44_9524")

    OP_95(0xFE, 19000, 0, -8600, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(200)

    def lambda_9547():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9547)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_44_9524 end

    def Function_45_9558(): pass

    label("Function_45_9558")

    Sleep(4500)
    StopSound(468, 1000, 80)
    Sound(492, 0, 80, 0)
    Return()

    # Function_45_9558 end

    def Function_46_9568(): pass

    label("Function_46_9568")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch13800.itc", 0x1E)
    LoadChrToIndex("chr/ch13801.itc", 0x1F)
    LoadChrToIndex("chr/ch13802.itc", 0x20)
    LoadChrToIndex("chr/ch08200.itc", 0x21)
    LoadChrToIndex("chr/ch08201.itc", 0x22)
    LoadChrToIndex("apl/ch50005.itc", 0x23)
    SoundLoad(847)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis244.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu08000.itp")
    OP_68(34500, -2900, -19000, 0)
    MoveCamera(35, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    SetChrPos(0x101, 38000, -4000, -19700, 270)
    SetChrPos(0x102, 38400, -4000, -18400, 270)
    SetChrPos(0x109, 39300, -4000, -19700, 270)
    SetChrPos(0x105, 39700, -4000, -18400, 270)
    SetChrPos(0x104, 40800, -4000, -19000, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    SetChrFlags(0x18, 0x8000)
    SetChrFlags(0x18, 0x20)
    SetChrPos(0x18, 32700, 200, -36200, 0)
    OP_52(0x18, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x17, 0x21)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 42000, -4000, -19000, 270)
    OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearMapObjFlags(0x5, 0x10)
    OP_70(0x5, 0xA)
    SetCameraDistance(16500, 3000)

    def lambda_96EE():
        OP_97(0x101, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_96EE)
    Sleep(50)

    def lambda_970B():
        OP_97(0x102, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_970B)
    Sleep(50)

    def lambda_9728():
        OP_97(0x105, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_9728)
    Sleep(50)

    def lambda_9745():
        OP_97(0x109, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_9745)
    Sleep(50)

    def lambda_9762():
        OP_97(0x104, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_9762)
    FadeToBright(2000, 0)
    Sleep(1000)
    Sound(104, 0, 100, 0)
    OP_71(0x5, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x5)
    WaitChrThread(0x101, 0)
    Sound(846, 0, 100, 0)
    Sleep(300)
    StopBGM(0xBB8)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)
    OP_6F(0x79)

    def lambda_9827():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9827)
    Sleep(50)

    def lambda_9837():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_9837)
    Sleep(50)

    def lambda_9847():
        OP_93(0x105, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_9847)
    Sleep(50)

    def lambda_9857():
        OP_93(0x109, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_9857)
    Sleep(50)

    def lambda_9867():
        OP_93(0x104, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_9867)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x101,
        "#5P#00005FWhat...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#5PA bird's cry?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(10)
    WaitBGM()
    PlayBGM("ed7519", 0)
    Fade(250)
    OP_68(33700, -500, -27700, 0)
    MoveCamera(30, 27, 15, 0)
    OP_6E(700, 0)
    SetCameraDistance(12500, 0)
    OP_68(34700, -1000, -23700, 3000)
    MoveCamera(27, 27, 11, 3000)
    SetCameraDistance(15500, 3000)
    OP_52(0x18, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x101, 33200, -4000, -20000, 180)
    SetChrPos(0x102, 31800, -4000, -20300, 180)
    SetChrPos(0x109, 34600, -4000, -20000, 180)
    SetChrPos(0x104, 34700, -4000, -18700, 180)
    SetChrPos(0x105, 33300, -4000, -18700, 180)
    ClearChrFlags(0x18, 0x80)

    def lambda_999E():

        label("loc_999E")

        OP_A0(0xFE, 1500, 0x0, 0x4)
        Yield()
        Jump("loc_999E")

    QueueWorkItem2(0x18, 2, lambda_999E)

    def lambda_99B0():
        OP_96(0xFE, 0x7FBC, 0xFFFFF8F8, 0xFFFFAD30, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_99B0)
    Sound(847, 2, 70, 0)
    WaitChrThread(0x18, 1)
    BeginChrThread(0x18, 3, 0, 47)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_99F2():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_99F2)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_9A1A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9A1A)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_9A42():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9A42)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_9A6A():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9A6A)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_9A92():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_9A92)
    Sleep(2000)
    Fade(500)
    OP_68(34300, -1800, -20900, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    OP_52(0x18, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()

    ChrTalk(
        0x101,
        "#00011F#6PH-Huh!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10111F#6PA w-white hawk...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305F#6P...No, it looks\x01",
            "like a falcon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#6PHey now, what is he doin' in\x01",
            "the smack middle of the city...\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x18, 0x3)
    WaitChrThread(0x18, 1)
    EndChrThread(0x18, 0x0)
    OP_68(33300, -2800, -20900, 3000)
    MoveCamera(40, 21, 0, 3000)

    def lambda_9BD2():
        OP_9E(0xFE, 0x878C, 0xFFFFAD30, 0x50910, 0xED8, 0x1)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_9BD2)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x73A), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x76C), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x79E), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x802), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x834), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x866), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x898), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x8CA), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x92E), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x992), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x9F6), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xA28), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xA5A), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xA8C), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xABE), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xAF0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xB22), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xB54), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xB86), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)

    def lambda_9D55():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9D55)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xBEA), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC1C), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC4E), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)

    def lambda_9D9E():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9D9E)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC80), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xCB2), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xCE4), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xD16), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)

    def lambda_9DE7():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9DE7)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xD48), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xD7A), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xDAC), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xDDE), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)

    def lambda_9E30():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_9E30)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xE10), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xE42), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xE74), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xEA6), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)

    def lambda_9E79():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9E79)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xED8), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xF0A), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xF3C), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xF6E), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xFA0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xFD2), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1004), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x18, 1)
    StopSound(847, 700, 60)
    Fade(250)
    EndChrThread(0x18, 0x2)
    SetChrPos(0x18, 33400, -3100, -21900, 0)
    SetChrChipByIndex(0x18, 0x1F)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x1)

    def lambda_9F1D():
        OP_96(0xFE, 0x8278, 0xFFFFF1F0, 0xFFFFAA74, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_9F1D)
    Sleep(100)
    SetChrSubChip(0x18, 0x1)
    Sleep(100)
    SetChrSubChip(0x18, 0x0)
    Sleep(100)
    SetChrSubChip(0x18, 0x1)
    Sleep(100)
    SetChrSubChip(0x18, 0x2)
    Sleep(300)
    WaitChrThread(0x18, 1)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x18,
        (
            "Screee.\x02\x03",
            "Scree, scree, screee.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00001F#5PC-Could it be...\x01",
            "That he has business with us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00108FIt seems like when\x01",
            "Zeit speaks...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00306FUhhm, if peTiote was here with us, \x01",
            "maybe we could understand him...\x02",
        )
    )

    CloseMessageWindow()
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x5, 0x10)
    OP_71(0x5, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x5)
    ClearChrFlags(0x17, 0x80)

    def lambda_A150():
        OP_96(0xFE, 0x9A4C, 0xFFFFF060, 0xFFFFB5C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_A150)

    def lambda_A16A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_A16A)
    WaitChrThread(0x17, 1)
    Sound(104, 0, 100, 0)
    OP_71(0x5, 0xA, 0x0, 0x0, 0x0)

    ChrTalk(
        0x17,
        "#01105F#12POh, what's happened?\x02",
    )

    OP_79(0x5)
    SetMapObjFlags(0x5, 0x10)
    CloseMessageWindow()
    OP_63(0x17, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrChipByIndex(0x17, 0x22)
    SetChrSubChip(0x17, 0x0)

    def lambda_A1E2():
        OP_95(0xFE, 37500, -4000, -19000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_A1E2)
    WaitChrThread(0x17, 1)

    def lambda_A200():
        OP_95(0xFE, 34500, -4000, -21300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_A200)
    Sleep(300)

    def lambda_A21D():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A21D)
    Sleep(100)

    def lambda_A22D():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_A22D)
    Sleep(100)

    def lambda_A23D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A23D)
    Sleep(100)

    def lambda_A24D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_A24D)
    WaitChrThread(0x17, 1)
    SetChrChipByIndex(0x17, 0x21)
    SetChrSubChip(0x17, 0x0)
    OP_93(0x17, 0xE1, 0x1F4)
    Sound(3029, 255, 100, 0)

    ChrTalk(
        0x17,
        (
            "#01110F#11PWow, a white bird!\x02\x03",
            "#01109FHe's got a sharp beak,\x01",
            "he's so cool!\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x18, 0x20)
    SetChrSubChip(0x18, 0x0)
    TurnDirection(0x18, 0x17, 0)
    Sleep(300)

    ChrTalk(
        0x18,
        (
            "#6P#08009FScreee㈱\x02\x03",
            "Screee, scree, scree♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#01103F#11PHm, hm.\x02\x03",
            "#01102FI see, so that's it...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1500)

    ChrTalk(
        0x101,
        (
            "#00012F#5P(KeA...\x01",
            "Can she really understand him?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10112F#5P(A-Amazing...)\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x17, 0x101, 500)

    def lambda_A413():

        label("loc_A413")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_A413")

    QueueWorkItem2(0x17, 2, lambda_A413)
    SetChrChipByIndex(0x18, 0x1F)
    SetChrSubChip(0x18, 0x2)

    ChrTalk(
        0x17,
        (
            "#01100F#11PUhm, so, this little one\x01",
            "says he's called "Sieg".\x02\x03",
            "He's saying he's got a message\x01",
            "for you, so, will you accept it?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A4B0():
        TurnDirection(0x101, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A4B0)
    Sleep(50)

    def lambda_A4C0():
        TurnDirection(0x104, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_A4C0)
    Sleep(50)

    def lambda_A4D0():
        TurnDirection(0x109, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_A4D0)
    Sleep(50)

    def lambda_A4E0():
        TurnDirection(0x105, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_A4E0)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        "#00011F#5PI-Is that so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00305FOh, he actually has a memo\x01",
            "fastened to his leg, huh.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A563():
        OP_95(0xFE, 33200, -4000, -21000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A563)
    TurnDirection(0x18, 0x101, 500)
    WaitChrThread(0x101, 1)
    EndChrThread(0x17, 0x2)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd took the memo that was\x01",
            "fastened to the bird's leg.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x23)
    SetChrSubChip(0x101, 0x0)
    Sleep(500)
    Sound(18, 0, 100, 0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(500)
    SetMessageWindowPos(-1, 140, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Dear Crossbell Police, Special Support Section.\x02\x03",
            "Pardon my rudeness for contacting you,\x01",
            "but your fame has reached my ears.\x02\x03",
            "If you have time, would you be\x01",
            "willing to consult with me privately?\x02\x03",
            "I am going to wait for you at the meeting\x01",
            "place terrace at Crossbell Airport, this evening.\x02\x03",
            "PS: In case you cannot make it,\x01",
            "it is all right if you do not reply.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(150)

    AnonymousTalk(
        0x101,
        "#00005F............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        "#00101FT-This is...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x109,
        (
            "#10106FIt says privately, and no sender.\x01",
            "It is too suspicious, however...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x105,
        (
            "#10302FHowever, the handwriting is beautiful\x01",
            "and the sentences are polite...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x104,
        (
            "#00301FAbove all, there's a white falcon\x01",
            "crest applied on the memo...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x18,
        (
            "#08000FScreee.\x02\x03",
            "Scree, scree, screee.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    SetChrSubChip(0x18, 0x1)
    Sleep(100)
    SetChrSubChip(0x18, 0x0)
    Sleep(100)
    Sound(847, 2, 70, 0)

    def lambda_A952():
        OP_96(0xFE, 0x8278, 0xFFFFF3E4, 0xFFFFAA74, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_A952)
    SetChrSubChip(0x18, 0x1)
    Sleep(100)
    SetChrSubChip(0x18, 0x0)
    Sleep(100)
    SetChrSubChip(0x18, 0x1)
    Sleep(100)
    SetChrSubChip(0x18, 0x0)
    Sleep(100)
    SetChrSubChip(0x18, 0x1)
    WaitChrThread(0x18, 1)
    OP_68(33300, -1800, -24900, 5000)
    MoveCamera(46, 21, 0, 5000)
    SetCameraDistance(16000, 5000)
    Fade(250)
    SetChrPos(0x18, 33400, -3600, -21900, 0)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    SetChrFlags(0x18, 0x1)

    def lambda_A9D8():

        label("loc_A9D8")

        OP_A0(0xFE, 1500, 0x0, 0x4)
        Yield()
        Jump("loc_A9D8")

    QueueWorkItem2(0x18, 2, lambda_A9D8)
    BeginChrThread(0x18, 3, 0, 48)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xDDE), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xDAC), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xD7A), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xD48), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xD16), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xCE4), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xCB2), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC80), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC4E), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC1C), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xBEA), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xB86), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xB54), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xB22), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xAF0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xABE), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xA8C), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xA5A), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xA28), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x9F6), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x992), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x92E), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x8CA), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x898), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x866), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x834), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x802), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x79E), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x76C), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x73A), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x18, 3)

    def lambda_AC0D():
        OP_96(0xFE, 0x8278, 0xFFFFFED4, 0xFFFF7B94, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_AC0D)
    Sleep(300)

    def lambda_AC2A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_AC2A)
    Sleep(100)

    def lambda_AC3A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_AC3A)
    Sleep(100)

    def lambda_AC4A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_AC4A)
    Sleep(100)

    def lambda_AC5A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_AC5A)
    StopSound(847, 2000, 60)
    WaitChrThread(0x18, 1)
    EndChrThread(0x18, 0xFF)
    SetChrFlags(0x18, 0x80)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1500)
    OP_6F(0x79)
    Fade(500)
    OP_68(33300, -2800, -20900, 0)
    MoveCamera(40, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    OP_0D()
    TurnDirection(0x101, 0x17, 500)

    ChrTalk(
        0x101,
        (
            "#6P#00011FEhm...\x01",
            "KeA, what did he say?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x17, 0x101, 500)

    ChrTalk(
        0x17,
        (
            "#01111F#11PUhhm, he said that going\x01",
            "or not is up to you guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00003FI see...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    def lambda_ADD5():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_ADD5)
    Sleep(50)

    def lambda_ADE5():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_ADE5)
    Sleep(50)

    def lambda_ADF5():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_ADF5)
    Sleep(50)

    def lambda_AE05():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_AE05)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x102,
        (
            "#6P#00108FW-What do we do?\x02\x03",
            "#00101FI think that's\x01",
            "impossible, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#00306FYeah, right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F#11PHowever, a white falcon crest...\x01",
            "Even that bird looked like one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309F#5PAhaha, it makes you have\x01",
            "even more expectations.\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x101)
    Sleep(450)
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#12P#00003F──It is a welcome invitation.\x01",
            "Let's accept it.\x02\x03",
            "#00000FBecause there's still time until evening,\x01",
            "we can finish other business too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00106FU-Understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106F#11PI-I'm feeling nervous...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00309FWell, I don't think goin'\x01",
            "in full dress is needed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#5PHu hu, then, when we have finished our business, \x01",
            "let's go to the Crossbell Airport past the south exit.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x17, 0x13B, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x17,
        (
            "#11P#01110FI don't really get it, but\x01",
            "everyone, good luck!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    SetChrFlags(0x17, 0x80)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    SetChrPos(0x0, 34000, -4000, -19000, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x140, 7)
    OP_29(0xA3, 0x1, 0x11)
    OP_C9(0x1, 0x1000)
    OP_24(0x34F)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7150", 0)
    EventEnd(0x5)
    Return()

    # Function_46_9568 end

    def Function_47_B166(): pass

    label("Function_47_B166")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B195")

    def lambda_B176():
        OP_9E(0xFE, 0x8980, 0xFFFFAD30, 0x57E40, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_B176)
    WaitChrThread(0x18, 1)
    Jump("Function_47_B166")

    label("loc_B195")

    Return()

    # Function_47_B166 end

    def Function_48_B196(): pass

    label("Function_48_B196")


    def lambda_B19B():
        OP_9E(0xFE, 0x846C, 0xFFFFAA74, 0x2BF20, 0xED8, 0x1)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_B19B)
    WaitChrThread(0x18, 1)

    def lambda_B1BA():
        OP_9E(0xFE, 0x8084, 0xFFFFAA74, 0x57E40, 0x1194, 0x1)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_B1BA)
    WaitChrThread(0x18, 1)
    Return()

    # Function_48_B196 end

    def Function_49_B1D5(): pass

    label("Function_49_B1D5")

    EventBegin(0x0)
    Fade(500)
    OP_68(33500, -2700, -18100, 0)
    MoveCamera(55, 19, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, 32600, -4000, -19400, 0)
    SetChrPos(0x102, 31300, -4000, -18800, 45)
    SetChrPos(0x103, 34100, -4000, -19500, 315)
    SetChrPos(0x104, 35400, -4000, -18300, 270)
    SetChrPos(0x109, 33500, -4000, -17600, 0)
    SetChrPos(0x105, 31000, -4000, -17700, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#00206F#12PNow that I think about it...\x02\x03",
            "#00200FThis is also the last day\x01",
            "Miss Noｱl drives for us.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B2F5():
        OP_93(0x109, 0xB3, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B2F5)
    Sleep(400)

    ChrTalk(
        0x101,
        "#12P#00006FI see...that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112F#5PAhaha...\x01",
            "I think it's really a pity too.\x02\x03",
            "This car... I quite like it at\x01",
            "a personal level too.\x02\x03",
            "#10100FHowever, you all are able\x01",
            "to drive it well already, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00004FYeah, after all, we got trained\x01",
            "by you on days off, Noｱl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00109F*giggle*, you were easy to understand\x01",
            "and helped us a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10306FHmmm, still, it was\x01",
            "quite rough, hm?\x02\x03",
            "#10302FMore than a Master Sergeant, \x01",
            "to me it felt you were a drill one.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x109, 0x105, 500)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#11P#10101FT-That's because you did \x01",
            "nothing but pop off, right?\x02\x03",
            "#10106FAlthough you can do well if you get to it,\x01",
            "you don't remember the traffic rules.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F#11PWell, even to be able to teach strictly\x01",
            "is a needed disposition for a soldier.\x02\x03",
            "#00300FAt any rate, we'll fully appreciate\x01",
            "a pro's driving for all the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00002FYeah.\x01",
            "Noｱl, we're counting on you.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    ChrTalk(
        0x109,
        "#10109F#5PYes, please leave it to me!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 33500, -4000, -18000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x180, 4)
    EventEnd(0x5)
    Return()

    # Function_49_B1D5 end

    def Function_50_B6E3(): pass

    label("Function_50_B6E3")

    EventBegin(0x0)
    Fade(500)
    OP_68(33500, -2900, -17100, 0)
    MoveCamera(53, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, 33500, -4000, -17600, 0)
    SetChrPos(0x102, 32600, -4000, -19400, 0)
    SetChrPos(0x103, 34100, -4000, -19500, 315)
    SetChrPos(0x104, 35400, -4000, -18300, 315)
    SetChrPos(0xF4, 31300, -4000, -18800, 45)
    SetChrPos(0xF5, 31000, -4000, -17700, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#11P#00002FOur car...\x01",
            "Looks like it's all in piece, somehow.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BBE8")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B82E")

    ChrTalk(
        0x109,
        "#6P#10109FThank goodness...I'm relieved.\x02",
    )

    CloseMessageWindow()

    label("loc_B82E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BA1A")

    ChrTalk(
        0x105,
        (
            "#6P#10405FStill, if I remember correctly\x01",
            "you got this accommodated to a\x01",
            "certain degree by Mayor Dieter...\x02\x03",
            "#10409FHu hu, using that to\x01",
            "go to arrest him is\x01",
            "ironic, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B8F5():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B8F5)
    Sleep(50)

    def lambda_B905():
        TurnDirection(0x103, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_B905)
    Sleep(50)

    def lambda_B915():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B915)
    Sleep(50)

    def lambda_B925():
        TurnDirection(0x104, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_B925)
    Sleep(50)

    def lambda_B935():
        TurnDirection(0xF4, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_B935)
    Sleep(50)

    def lambda_B945():
        TurnDirection(0xF5, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_B945)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)

    ChrTalk(
        0x102,
        "#12P#00106F...You're right, really.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B9FC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B9D9")

    ChrTalk(
        0x109,
        "#12P#10101FWazy, listen now...\x02",
    )

    CloseMessageWindow()
    Jump("loc_B9FC")

    label("loc_B9D9")


    ChrTalk(
        0x109,
        "#6P#10101FWazy, listen now...\x02",
    )

    CloseMessageWindow()

    label("loc_B9FC")


    ChrTalk(
        0x103,
        "#00211FNot funny...\x02",
    )

    CloseMessageWindow()
    Jump("loc_BBE3")

    label("loc_BA1A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BBE3")

    ChrTalk(
        0x10A,
        (
            "#6P#00603FHm...\x01",
            "It looks like it's got no problems.\x02\x03",
            "#00600FStill, if I remember correctly, I heard\x01",
            "you got this car accommodated to a\x01",
            "certain degree by Mayor Dieter...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BADD():
        TurnDirection(0x102, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_BADD)
    Sleep(50)

    def lambda_BAED():
        TurnDirection(0x103, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_BAED)
    Sleep(50)

    def lambda_BAFD():
        TurnDirection(0x101, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BAFD)
    Sleep(50)

    def lambda_BB0D():
        TurnDirection(0x104, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_BB0D)
    Sleep(50)

    def lambda_BB1D():
        TurnDirection(0xF4, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_BB1D)
    Sleep(50)

    def lambda_BB2D():
        TurnDirection(0xF5, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_BB2D)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)

    ChrTalk(
        0x102,
        "#12P#00108FN-Now that you mention it...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BBBE")

    ChrTalk(
        0x109,
        (
            "#6P#10106FIndeed, Chief Sergei\x01",
            "did say that...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BBBE")


    ChrTalk(
        0x103,
        "#00211F...Somehow it is ironic.\x02",
    )

    CloseMessageWindow()

    label("loc_BBE3")

    Jump("loc_BD3E")

    label("loc_BBE8")


    ChrTalk(
        0x109,
        (
            "#6P#10104FThank goodness...I'm relieved.\x02\x03",
            "#10105F...By the way, you got this car\x01",
            "accommodated to a certain\x01",
            "degree by Mayor Dieter, right?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BC7C():
        TurnDirection(0x102, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_BC7C)
    Sleep(50)

    def lambda_BC8C():
        TurnDirection(0x103, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_BC8C)
    Sleep(50)

    def lambda_BC9C():
        TurnDirection(0x101, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BC9C)
    Sleep(50)

    def lambda_BCAC():
        TurnDirection(0x104, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_BCAC)
    Sleep(50)

    def lambda_BCBC():
        TurnDirection(0xF4, 0x109, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_BCBC)
    Sleep(50)

    def lambda_BCCC():
        TurnDirection(0xF5, 0x109, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_BCCC)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)

    ChrTalk(
        0x102,
        "#12P#00108FN-Now that you mention it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00211F...Somehow it is ironic.\x02",
    )

    CloseMessageWindow()

    label("loc_BD3E")

    OP_93(0x104, 0x13B, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x104,
        (
            "#00304FWell, no matter the details, this gal is\x01",
            "a member of the Support Section too.\x02\x03",
            "#00302FLet's check her inside too, to see\x01",
            "if we can use her properly or not.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)

    ChrTalk(
        0x101,
        "#11P#00000FYeah, you're right.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x23, 1)
    NewScene("e2010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_50_B6E3 end

    def Function_51_BE33(): pass

    label("Function_51_BE33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BEDC")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FThe West Crossbell highway is up ahead.\x02\x03",
            "There's a Wanted Monster, but...\x01",
            "Let's clear up the jobs inside the city first.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -34230, 0, 4210, 90)
    EventEnd(0x4)
    Return()

    label("loc_BEDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BFC6")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BF6A")

    ChrTalk(
        0x101,
        (
            "#00000FThe West Crossbell highway is up ahead.\x02\x03",
            "We don't have any special business,\x01",
            "so let's not exit.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_BFB2")

    label("loc_BF6A")


    ChrTalk(
        0x101,
        (
            "#00000FWe don't have any special business\x01",
            "here, so let's not exit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BFB2")

    SetChrPos(0x0, -34230, 0, 4210, 90)
    EventEnd(0x4)
    Return()

    label("loc_BFC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C03E")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001FNow we have to chase Randy down...\x01",
            "It's not the time to wander around.\x01\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -34230, 0, 4210, 90)
    EventEnd(0x4)
    Return()

    label("loc_C03E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C0B9")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001FNow it's not the time to go out the city.\x01",
            "Let's quietly retrace our steps.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -34230, 0, 4210, 90)
    EventEnd(0x4)
    Return()

    label("loc_C0B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C16B")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001FAfter coming here,\x01",
            "we can't leave the city.\x02\x03",
            "The operation to break into Orchis Tower...\x01",
            "We have to make it succeed at all costs.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -34230, 0, 4210, 90)
    EventEnd(0x4)
    Return()

    label("loc_C16B")

    Return()

    # Function_51_BE33 end

    def Function_52_C16C(): pass

    label("Function_52_C16C")

    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C1DF")

    ChrTalk(
        0x101,
        (
            "#00000FIt looks like it's closed\x01",
            "from the inside.\x02\x03",
            "Should we enter from the front?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_C23C")

    label("loc_C1DF")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is closed.\x01",
            "It looks like it has been\x01",
            "locked from the inside.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_C23C")

    TalkEnd(0xFF)
    Return()

    # Function_52_C16C end

    SaveToFile()

Try(main)
