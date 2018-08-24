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

    Sepith("Sepith_C0C7", 8,   8,   8,   8,   11,  11,  11)

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
        "BattleInfo_7A4", 0x0000, 93, 6, 60, 4, 1, 25, 0, "bc0200", "Sepith_C0C7", 60, 25, 10, 0,
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
        "Function_14_2237",        # 0E, 14
        "Function_15_2A27",        # 0F, 15
        "Function_16_2ADB",        # 10, 16
        "Function_17_2BE1",        # 11, 17
        "Function_18_2D43",        # 12, 18
        "Function_19_34FA",        # 13, 19
        "Function_20_4637",        # 14, 20
        "Function_21_515A",        # 15, 21
        "Function_22_547F",        # 16, 22
        "Function_23_5B0C",        # 17, 23
        "Function_24_62C9",        # 18, 24
        "Function_25_631F",        # 19, 25
        "Function_26_6375",        # 1A, 26
        "Function_27_6400",        # 1B, 27
        "Function_28_6545",        # 1C, 28
        "Function_29_6751",        # 1D, 29
        "Function_30_67F2",        # 1E, 30
        "Function_31_6855",        # 1F, 31
        "Function_32_6BCD",        # 20, 32
        "Function_33_7270",        # 21, 33
        "Function_34_7331",        # 22, 34
        "Function_35_73C5",        # 23, 35
        "Function_36_7470",        # 24, 36
        "Function_37_7A33",        # 25, 37
        "Function_38_912A",        # 26, 38
        "Function_39_9181",        # 27, 39
        "Function_40_9216",        # 28, 40
        "Function_41_92AF",        # 29, 41
        "Function_42_92E3",        # 2A, 42
        "Function_43_9317",        # 2B, 43
        "Function_44_934B",        # 2C, 44
        "Function_45_937F",        # 2D, 45
        "Function_46_938F",        # 2E, 46
        "Function_47_AFE8",        # 2F, 47
        "Function_48_B018",        # 30, 48
        "Function_49_B057",        # 31, 49
        "Function_50_B566",        # 32, 50
        "Function_51_BC7F",        # 33, 51
        "Function_52_BFD0",        # 34, 52
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
            "Since you have too many,\x01",
            "you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xD, 0x1E, 0x0, 0x0, 0x0)

    label("loc_21DD")

    Jump("loc_222B")

    label("loc_21E2")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the\x01",
            "chest.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_222B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_13_20E6 end

    def Function_14_2237(): pass

    label("Function_14_2237")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_228A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2255")
    Call(0, 17)
    Jump("loc_2285")

    label("loc_2255")


    ChrTalk(
        0xFE,
        "Ah, guys!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Leave Crossbell City to\x01",
            "us!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2285")

    Jump("loc_2A23")

    label("loc_228A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2298")
    Jump("loc_2A23")

    label("loc_2298")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_23B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_236C")

    ChrTalk(
        0xFE,
        (
            "Everyone seems to be seriously\x01",
            "worried about what's gonna happen\x01",
            "with the Empire and Republic...\x02",
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
    Jump("loc_23B4")

    label("loc_236C")


    ChrTalk(
        0xFE,
        (
            "Wasn't "independence" a\x01",
            "happy thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I don't really get it...\x02",
    )

    CloseMessageWindow()

    label("loc_23B4")

    Jump("loc_2A23")

    label("loc_23B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2426")

    ChrTalk(
        0xFE,
        (
            "I invited Momo to play,\x01",
            "but her mother said\x01",
            "no...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*. I'm bored for\x01",
            "some reason.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A23")

    label("loc_2426")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2449")

    ChrTalk(
        0xFE,
        "Hey, wait wait!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A23")

    label("loc_2449")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_24E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24A5")

    ChrTalk(
        0xFE,
        "Momo's laaate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope she finishes her\x01",
            "errand quickly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_24DE")

    label("loc_24A5")


    ChrTalk(
        0xFE,
        (
            "I hope Momo can at least\x01",
            "finish her errand\x01",
            "quickly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24DE")

    Jump("loc_2A23")

    label("loc_24E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_25C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_255B")

    ChrTalk(
        0xFE,
        (
            "Momo really sucks at\x01",
            "searching...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*yaaawn*... I've gotten\x01",
            "tired for some reason...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_25BC")

    label("loc_255B")


    ChrTalk(
        0xFE,
        (
            "I'm tired of staying put\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want her to find me\x01",
            "already and play a\x01",
            "different game.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25BC")

    Jump("loc_2A23")

    label("loc_25C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2769")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2701")
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x8, 0x0, 500)

    ChrTalk(
        0xFE,
        (
            "Whoops... Oh, it's you\x01",
            "guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*haah*, you scared me. I\x01",
            "thought I'd been found\x01",
            "by Momo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FHey now... Don't sneak\x01",
            "around this place as you\x01",
            "please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, come on, don't be\x01",
            "so stingy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Keep quiet about my\x01",
            "hiding place, ok?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    OP_93(0xFE, 0xE1, 0x0)
    ClearChrFlags(0x8, 0x10)
    Jump("loc_2764")

    label("loc_2701")


    ChrTalk(
        0xFE,
        (
            "I'm playing hide and\x01",
            "seek with Henri and Momo\x01",
            "now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Keep quiet about my\x01",
            "hiding place, ok?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2764")

    Jump("loc_2A23")

    label("loc_2769")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_27ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2784")
    Call(0, 15)
    Jump("loc_27E8")

    label("loc_2784")


    ChrTalk(
        0xFE,
        (
            "By the way, KeA hasn't\x01",
            "been feeling well\x01",
            "lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Guess I'll invite her to\x01",
            "play next time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27E8")

    Jump("loc_2A23")

    label("loc_27ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_27FB")
    Jump("loc_2A23")

    label("loc_27FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_296A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_290A")

    ChrTalk(
        0xFE,
        (
            "They say that there's\x01",
            "that trade stuff at\x01",
            "Orchis Tower tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't really get it, but\x01",
            "somehow I want to go have a\x01",
            "look with Henri and Momo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, I'm sure it's gonna be\x01",
            "a fun party or something. I\x01",
            "can't wait for tomorrow♪\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2965")

    label("loc_290A")


    ChrTalk(
        0xFE,
        (
            "Maybe that trade stuff\x01",
            "is a party or something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, I can't wait for\x01",
            "tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2965")

    Jump("loc_2A23")

    label("loc_296A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2978")
    Jump("loc_2A23")

    label("loc_2978")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2A0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2993")
    Call(0, 16)
    Jump("loc_2A07")

    label("loc_2993")


    ChrTalk(
        0xFE,
        (
            "By the way, KeA's\x01",
            "playing her friend\x01",
            "Shizuku today, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since she's here, I\x01",
            "guess I'll invite her\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A07")

    Jump("loc_2A23")

    label("loc_2A0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2A1A")
    Jump("loc_2A23")

    label("loc_2A1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2A23")

    label("loc_2A23")

    TalkEnd(0xFE)
    Return()

    # Function_14_2237 end

    def Function_15_2A27(): pass

    label("Function_15_2A27")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0x8,
        (
            "Momo's helping with the\x01",
            "store today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Tch. With Henri there's\x01",
            "not much choice of games\x01",
            "to play.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Ryｹ. Aren't you being\x01",
            "rude to me?\x02",
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

    # Function_15_2A27 end

    def Function_16_2ADB(): pass

    label("Function_16_2ADB")

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
            "Yeah, good idea. Let's\x01",
            "all go together.\x02",
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

    # Function_16_2ADB end

    def Function_17_2BE1(): pass

    label("Function_17_2BE1")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0x8,
        (
            "Well then, let's all\x01",
            "start patrolling the\x01",
            "city!\x02",
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
            "Crossbell Youth Special\x01",
            "Support Section, roll out!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F(Haha, "Youth Special\x01",
            "Support Section"...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F(It makes you feel\x01",
            "happy, somehow.)\x02",
        )
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

    # Function_17_2BE1 end

    def Function_18_2D43(): pass

    label("Function_18_2D43")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2E09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D61")
    Call(0, 17)
    Jump("loc_2E04")

    label("loc_2D61")


    ChrTalk(
        0xFE,
        (
            "The Youth Special Support\x01",
            "Section, eh? Even Ryｹ has good\x01",
            "ideas every now and then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since we're doing it, I\x01",
            "want to properly help\x01",
            "the people of the city.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E04")

    Jump("loc_34F6")

    label("loc_2E09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2E17")
    Jump("loc_34F6")

    label("loc_2E17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2FA9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F01")

    ChrTalk(
        0xFE,
        (
            "My father and mother got\x01",
            "back from out of state\x01",
            "yesterday too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Personally, I'm happy\x01",
            "about it, but they look\x01",
            "troubled somehow...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh", as I thought,\x01",
            "could "independence" be\x01",
            "something grave?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2FA4")

    label("loc_2F01")


    ChrTalk(
        0xFE,
        (
            "Personally, I'm happy mother\x01",
            "and father have come home, but\x01",
            "they somehow look troubled...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh", as I thought,\x01",
            "could "independence" be\x01",
            "something grave?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FA4")

    Jump("loc_34F6")

    label("loc_2FA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_301A")

    ChrTalk(
        0xFE,
        (
            "I think Momo's mother is\x01",
            "worried too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It can't be helped... To\x01",
            "think that raid\x01",
            "happened.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34F6")

    label("loc_301A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_30A0")

    ChrTalk(
        0xFE,
        (
            "H-Hey, Ryｹ!? We haven't\x01",
            "decided what to play\x01",
            "yet!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm ok with anything\x01",
            "except tiresome games\x01",
            "like this! Stop!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34F6")

    label("loc_30A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_31C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_314C")

    ChrTalk(
        0xFE,
        (
            "Ryｹ invited me this morning\x01",
            "and we went to the plaza in\x01",
            "front of the tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, Ryｹ, we shouldn't\x01",
            "have gone out on such a\x01",
            "rainy day...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_31C4")

    label("loc_314C")


    ChrTalk(
        0xFE,
        (
            "Geez, it can't be\x01",
            "helped, right? We\x01",
            "suddenly invited her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Let's wait patiently\x01",
            "until she finishes her\x01",
            "errand.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31C4")

    Jump("loc_34F6")

    label("loc_31C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_32E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3267")

    ChrTalk(
        0xFE,
        "*sigh*, I was found.\x02",
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
            "I hope he hasn't gone\x01",
            "into some strange place\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_32DB")

    label("loc_3267")


    ChrTalk(
        0xFE,
        (
            "By the way, ambulances\x01",
            "have been passing by\x01",
            "often for some time now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Did an accident happen\x01",
            "or something?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32DB")

    Jump("loc_34F6")

    label("loc_32E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3374")

    ChrTalk(
        0xFE,
        (
            "The other day, when we\x01",
            "played hide and seek, it\x01",
            "went on until evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if Momo will be\x01",
            "able to properly find\x01",
            "us...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34F6")

    label("loc_3374")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3417")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_338F")
    Call(0, 15)
    Jump("loc_3412")

    label("loc_338F")


    ChrTalk(
        0xFE,
        (
            "When Momo is here, we\x01",
            "can play more kinds of\x01",
            "games and it's fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, since she has to\x01",
            "help, there's nothing we\x01",
            "can do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3412")

    Jump("loc_34F6")

    label("loc_3417")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3425")
    Jump("loc_34F6")

    label("loc_3425")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_3433")
    Jump("loc_34F6")

    label("loc_3433")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3441")
    Jump("loc_34F6")

    label("loc_3441")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_34DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_345C")
    Call(0, 16)
    Jump("loc_34DA")

    label("loc_345C")


    ChrTalk(
        0xFE,
        (
            "According to rumors,\x01",
            "Orchis Tower is 250 arge\x01",
            "tall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder what kind of\x01",
            "building it is... I\x01",
            "can't wait to see it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34DA")

    Jump("loc_34F6")

    label("loc_34DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_34ED")
    Jump("loc_34F6")

    label("loc_34ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_34F6")

    label("loc_34F6")

    TalkEnd(0xFE)
    Return()

    # Function_18_2D43 end

    def Function_19_34FA(): pass

    label("Function_19_34FA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_35B5")

    ChrTalk(
        0xFE,
        (
            "That huge tree glowing\x01",
            "with a pale blue light...\x01",
            "What a thing to appear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't know what will happen\x01",
            "from now on but I must properly\x01",
            "record it for posterity.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4633")

    label("loc_35B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_35C3")
    Jump("loc_4633")

    label("loc_35C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_367D")

    ChrTalk(
        0xFE,
        (
            "President Dieter's words...\x01",
            "They strongly resonated in\x01",
            "the hearts of we citizens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if we were to make\x01",
            "enemies of the major powers...\x01",
            "I'd want to support him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4633")

    label("loc_367D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_37F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_377F")

    ChrTalk(
        0xFE,
        (
            "I'm taking pictures of people conducting\x01",
            "reconstruction activities, the destroyed\x01",
            "IBC building and and the like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We can't let such a\x01",
            "terrifying incident\x01",
            "happen again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I must properly record\x01",
            "it so as not to forget.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_37F0")

    label("loc_377F")


    ChrTalk(
        0xFE,
        (
            "We can't let such a\x01",
            "terrifying incident\x01",
            "happen again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I must properly record\x01",
            "it so as not to forget.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37F0")

    Jump("loc_4633")

    label("loc_37F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3965")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38D6")

    ChrTalk(
        0xFE,
        (
            "It appears that some CGF\x01",
            "armored cars headed to the\x01",
            "Mainz region last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That means\x01",
            "reinforcements are\x01",
            "heading there, right...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Is the armed group\x01",
            "really that strong an\x01",
            "enemy...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3960")

    label("loc_38D6")


    ChrTalk(
        0xFE,
        (
            "Reinforcements and even\x01",
            "vehicles from the CGF appear\x01",
            "to be heading to Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Is the armed group\x01",
            "really that strong an\x01",
            "enemy...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3960")

    Jump("loc_4633")

    label("loc_3965")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3A0C")

    ChrTalk(
        0xFE,
        (
            "I don't really get it, but... They\x01",
            "say yesterday's train accident was\x01",
            "the doing of an unknown monster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm. I'm worried it\x01",
            "could appear again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4633")

    label("loc_3A0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3A74")

    ChrTalk(
        0xFE,
        (
            "Hmm... I'm no good with the\x01",
            "ambulance sirens. They make\x01",
            "me uneasy for some reason...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4633")

    label("loc_3A74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3C55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BA7")

    ChrTalk(
        0xFE,
        (
            "I have the "Crossbell's 100\x01",
            "Famous Views" tour guide\x01",
            "published by Crossbell News.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It features a lot of spots with\x01",
            "nice scenery and it is very\x01",
            "helpful for shooting photos.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, I've already visited\x01",
            "most of the main spots. Which\x01",
            "should I shoot next, I wonder...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3C50")

    label("loc_3BA7")


    ChrTalk(
        0xFE,
        (
            "I wonder where I should\x01",
            "go take pictures\x01",
            "today...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've already visited most of the spots\x01",
            "featured "Crossbell's 100 Famous\x01",
            "Views" published by Crossbell News.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C50")

    Jump("loc_4633")

    label("loc_3C55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3DFE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D4C")

    ChrTalk(
        0xFE,
        (
            "The other day, I went to\x01",
            "St. Ursula Byroad\x01",
            "sandbank to take photos.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I saw an unfamiliar path\x01",
            "there going deeper into\x01",
            "the sandbank.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because it looked dangerous,\x01",
            "I didn't enter, but... I\x01",
            "wonder what it was.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3DF9")

    label("loc_3D4C")


    ChrTalk(
        0xFE,
        (
            "There was path I've never seen\x01",
            "before going further into the\x01",
            "St. Ursula Byroad sandbank.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because it looked dangerous,\x01",
            "I didn't enter, but... I\x01",
            "wonder what it was.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DF9")

    Jump("loc_4633")

    label("loc_3DFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3FA2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EFD")

    ChrTalk(
        0xFE,
        (
            "It looks like the Orchis\x01",
            "Tower area is authorized\x01",
            "personnel only today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since it's for security purposes\x01",
            "I think it can't be helped, but\x01",
            "I'm a little disappointed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Continuing from\x01",
            "yesterday, I took photos\x01",
            "nearby.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3F9D")

    label("loc_3EFD")


    ChrTalk(
        0xFE,
        (
            "It looks like the Orchis\x01",
            "Tower area is for\x01",
            "authorized personnel only.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I guess I'll go to take\x01",
            "pictures from the department\x01",
            "store rooftop today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F9D")

    Jump("loc_4633")

    label("loc_3FA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_40BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_406F")

    ChrTalk(
        0xFE,
        (
            "Whoops... I'm all out of\x01",
            "exposure quartz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It looks like I took too\x01",
            "many pictures at today's\x01",
            "unveiling ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I must buy new ones\x01",
            "before the orbal store\x01",
            "closes.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_40B8")

    label("loc_406F")


    ChrTalk(
        0xFE,
        (
            "I must go to buy new\x01",
            "exposure quartz before\x01",
            "the orbal store closes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40B8")

    Jump("loc_4633")

    label("loc_40BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_422A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41AA")

    ChrTalk(
        0xFE,
        (
            "After the unveiling ceremony\x01",
            "was over, I went to take a lot\x01",
            "of photos of Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Man. Anyhow it was an\x01",
            "amazingly big building. 40\x01",
            "floors above ground...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm. I can't wait to\x01",
            "develop them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4225")

    label("loc_41AA")


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
            "It appears that that\x01",
            "building will become the\x01",
            "new symbol of Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4225")

    Jump("loc_4633")

    label("loc_422A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4397")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42FE")

    ChrTalk(
        0xFE,
        (
            "The trade conference is\x01",
            "drawing near.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "VIPs from every country\x01",
            "will come and the new City\x01",
            "Hall will be unveiled...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I mustn't let good\x01",
            "chances to take pictures\x01",
            "pass me by.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4392")

    label("loc_42FE")


    ChrTalk(
        0xFE,
        (
            "The VIPs from\x01",
            "neighboring countries,\x01",
            "the unveiling...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I mustn't let good chances\x01",
            "to take pictures pass me by\x01",
            "during the trade conference.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4392")

    Jump("loc_4633")

    label("loc_4397")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_446A")

    ChrTalk(
        0xFE,
        (
            "Hmm. As I thought, even rainy\x01",
            "scenes are nice. They have a\x01",
            "different charm than usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Photographing in a rainy weather\x01",
            "requires considerable technique,\x01",
            "but... This is enjoyable as well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4633")

    label("loc_446A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4633")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4575")

    ChrTalk(
        0xFE,
        (
            "On West Crossbell\x01",
            "Highway there's a place\x01",
            "called "Knox Woodlands".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's a location that seems to\x01",
            "be nice for taking pictures,\x01",
            "with lots of dense foliage...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But because it's the\x01",
            "police academy site,\x01",
            "civilians can't go inside.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4633")

    label("loc_4575")


    ChrTalk(
        0xFE,
        (
            "Taking pictures is my hobby. I\x01",
            "visit all sorts of places in search\x01",
            "of good photographic subjects.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Civilians can't enter "Knox\x01",
            "Woodlands", but I'd like to\x01",
            "go photograph it one day.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4633")

    TalkEnd(0xFE)
    Return()

    # Function_19_34FA end

    def Function_20_4637(): pass

    label("Function_20_4637")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_47CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4733")

    ChrTalk(
        0xFE,
        (
            "It's been a while since\x01",
            "I came for coffee at\x01",
            "Morges.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How to say it... It would be\x01",
            "nice if, from now on, Crossbell\x01",
            "gradually went back to normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...But as you might\x01",
            "expect, I'm worried\x01",
            "about that huge tree.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_47C6")

    label("loc_4733")


    ChrTalk(
        0xFE,
        (
            "It would be nice if, from\x01",
            "now on, Crossbell gradually\x01",
            "went back to normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...But as you might\x01",
            "expect, I'm worried\x01",
            "about that huge tree.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47C6")

    Jump("loc_5156")

    label("loc_47CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_47D9")
    Jump("loc_5156")

    label("loc_47D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_490D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48CA")

    ChrTalk(
        0xFE,
        (
            "I was shocked too at the\x01",
            "latest Crossbell Times\x01",
            "articles, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I didn't think they spoke\x01",
            "with that much hostility\x01",
            "against the major powers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm worried about\x01",
            "Crossbell's situation\x01",
            "going forward...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4908")

    label("loc_48CA")


    ChrTalk(
        0xFE,
        (
            "I'm worried about\x01",
            "Crossbell's situation\x01",
            "going forward...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4908")

    Jump("loc_5156")

    label("loc_490D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_49C3")

    ChrTalk(
        0xFE,
        (
            "The fact that there was\x01",
            "almost no damage around\x01",
            "here is a silver lining.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Governmental District and the\x01",
            "Waterfront Area were hit\x01",
            "especially hard, after all...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5156")

    label("loc_49C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4A23")

    ChrTalk(
        0xFE,
        (
            "An occupation by an armed\x01",
            "group...? I'm worried about\x01",
            "the people of Mainz...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5156")

    label("loc_4A23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4A31")
    Jump("loc_5156")

    label("loc_4A31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4A6B")

    ChrTalk(
        0xFE,
        (
            "Today I spotted a lot of\x01",
            "ambulances...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5156")

    label("loc_4A6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4AFB")

    ChrTalk(
        0xFE,
        (
            "Hide and seek, eh...?\x01",
            "Back in the day, I did a\x01",
            "lot of that too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Looking at children\x01",
            "playing puts me in a\x01",
            "pleasant mood.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5156")

    label("loc_4AFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4C93")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C0D")

    ChrTalk(
        0xFE,
        (
            "The question of Crossbell\x01",
            "independence posed by the\x01",
            "mayor... It's a complex problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe I'll ask for Pluna\x01",
            "and Lenalee's\x01",
            "opinions...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...No, it's better if I don't.\x01",
            "Those two don't look like they're\x01",
            "thinking about it seriously...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4C8E")

    label("loc_4C0D")


    ChrTalk(
        0xFE,
        (
            "The question of Crossbell\x01",
            "independence... It's a\x01",
            "complex problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess I'll read\x01",
            "Crossbell Times and\x01",
            "think it over.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C8E")

    Jump("loc_5156")

    label("loc_4C93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4D55")

    ChrTalk(
        0xFE,
        (
            "It appears the Imperial Chronicle\x01",
            "and Remiferia's Ardent Press went\x01",
            "to cover the conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It appears I'll have\x01",
            "several articles with which\x01",
            "to compare Crossbell Times.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5156")

    label("loc_4D55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_4E06")

    ChrTalk(
        0xFE,
        (
            "Spacing out at the cafe\x01",
            "reading a book, it's\x01",
            "become this late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*brrr*... It's really chilly\x01",
            "at night. I guess I'll go back\x01",
            "home so I don't catch a cold.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5156")

    label("loc_4E06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4EEC")

    ChrTalk(
        0xFE,
        (
            "I heard Archduke Albert of\x01",
            "Remiferia is the leading investor\x01",
            "in St. Ursula Medical School.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It appears Chairman MacDowell in\x01",
            "particular has had friendly relations with\x01",
            "the Archduke for a long time, you see.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5156")

    label("loc_4EEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_50E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_501C")

    ChrTalk(
        0xFE,
        (
            "The West Zemuria Trade\x01",
            "Conference... Lately it's often\x01",
            "featured in Crossbell Times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They say it's for discussing economic\x01",
            "relationships, but I wonder what kind of\x01",
            "topics will be brought up for discussion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, I guess I'll ask\x01",
            "Miss Marble for details\x01",
            "next time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_50E0")

    label("loc_501C")


    ChrTalk(
        0xFE,
        (
            "The West Zemuria Trade Conference...\x01",
            ""Economic relationships" is a mouthful, but I\x01",
            "wonder what kind of things will be discussed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, I guess I'll ask\x01",
            "Miss Marble for details\x01",
            "next time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50E0")

    Jump("loc_5156")

    label("loc_50E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_50F3")
    Jump("loc_5156")

    label("loc_50F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5156")

    ChrTalk(
        0xFE,
        (
            "Sunday School will be\x01",
            "held this evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I mustn't forget to\x01",
            "bring my homework.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5156")

    TalkEnd(0xFE)
    Return()

    # Function_20_4637 end

    def Function_21_515A(): pass

    label("Function_21_515A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_51CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5178")
    Call(0, 17)
    Jump("loc_51C9")

    label("loc_5178")


    ChrTalk(
        0xFE,
        (
            "I'll help all the people of\x01",
            "the city who are in trouble\x01",
            "with Ryｹ and Henri!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51C9")

    Jump("loc_547B")

    label("loc_51CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_51DC")
    Jump("loc_547B")

    label("loc_51DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_51EA")
    Jump("loc_547B")

    label("loc_51EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_51F8")
    Jump("loc_547B")

    label("loc_51F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5231")

    ChrTalk(
        0xFE,
        (
            "O-Oh... I'm no good at\x01",
            "playing tag...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_547B")

    label("loc_5231")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_523F")
    Jump("loc_547B")

    label("loc_523F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_52EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52AD")

    ChrTalk(
        0xFE,
        (
            "I've finally found\x01",
            "Henri!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A-All right... Next, I\x01",
            "have to look for Ryｹ...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_52E7")

    label("loc_52AD")


    ChrTalk(
        0xFE,
        (
            "But I really don't know\x01",
            "where Ryｹ could be\x01",
            "hiding...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52E7")

    Jump("loc_547B")

    label("loc_52EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_53B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5383")

    ChrTalk(
        0xFE,
        (
            "I'm playing hide and\x01",
            "seek with Ryｹ and\x01",
            "Henri...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...But I can't find them\x01",
            "at all... Where could\x01",
            "they be hiding...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_53B0")

    label("loc_5383")


    ChrTalk(
        0xFE,
        (
            "Where could Ryｹ and\x01",
            "Henri be hiding...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53B0")

    Jump("loc_547B")

    label("loc_53B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_53C3")
    Jump("loc_547B")

    label("loc_53C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_53D1")
    Jump("loc_547B")

    label("loc_53D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_53DF")
    Jump("loc_547B")

    label("loc_53DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_53ED")
    Jump("loc_547B")

    label("loc_53ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5464")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5408")
    Call(0, 16)
    Jump("loc_545F")

    label("loc_5408")


    ChrTalk(
        0xFE,
        (
            "Tomorrow I'm going to\x01",
            "meet everyone at the\x01",
            "department store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I can't wait...\x02",
    )

    CloseMessageWindow()

    label("loc_545F")

    Jump("loc_547B")

    label("loc_5464")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5472")
    Jump("loc_547B")

    label("loc_5472")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_547B")

    label("loc_547B")

    TalkEnd(0xFE)
    Return()

    # Function_21_515A end

    def Function_22_547F(): pass

    label("Function_22_547F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5490")
    Jump("loc_5B08")

    label("loc_5490")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_549E")
    Jump("loc_5B08")

    label("loc_549E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_54AC")
    Jump("loc_5B08")

    label("loc_54AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_54BA")
    Jump("loc_5B08")

    label("loc_54BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5562")

    ChrTalk(
        0xFE,
        (
            "Who would've thought something\x01",
            "like occupation of the mining\x01",
            "town would happen...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It makes me uneasy for\x01",
            "some reason... Isn't\x01",
            "Momo home yet...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B08")

    label("loc_5562")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5570")
    Jump("loc_5B08")

    label("loc_5570")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_55DC")

    ChrTalk(
        0xFE,
        (
            "Ambulances have been\x01",
            "coming and going for\x01",
            "quite some time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Did something happen...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5B08")

    label("loc_55DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5657")

    ChrTalk(
        0xFE,
        (
            "Mr. Grimwood looks like\x01",
            "he's very busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's been going in and\x01",
            "out of his office\x01",
            "repeatedly today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B08")

    label("loc_5657")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5730")

    ChrTalk(
        0xFE,
        (
            "I've spoken seriously with my husband\x01",
            "about independence several times\x01",
            "following the trade conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's a problem that concerns\x01",
            "all of us Crossbell citizens.\x01",
            "We must consider it seriously.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B08")

    label("loc_5730")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_573E")
    Jump("loc_5B08")

    label("loc_573E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_574C")
    Jump("loc_5B08")

    label("loc_574C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5861")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57FC")

    ChrTalk(
        0xFE,
        "Welcooome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Momo and the others went\x01",
            "to the unveiling\x01",
            "ceremony today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. When she comes\x01",
            "home, I'll have to ask\x01",
            "her a lot of things.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_585C")

    label("loc_57FC")


    ChrTalk(
        0xFE,
        (
            "Momo and the others went\x01",
            "to the unveiling\x01",
            "ceremony today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, I hope they have\x01",
            "fun.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_585C")

    Jump("loc_5B08")

    label("loc_5861")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5A50")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59AD")

    ChrTalk(
        0xFE,
        (
            "The other day when it was raining,\x01",
            "I was worried about Momo who\x01",
            "hadn't returned from an errand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I asked her about it,\x01",
            "she said she was looking for\x01",
            "the umbrella she had lost.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That Momo. I can buy her\x01",
            "a replacement, and\x01",
            "yet...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's quite the cheap\x01",
            "thing to make me worry\x01",
            "about her.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5A4B")

    label("loc_59AD")


    ChrTalk(
        0xFE,
        (
            "Still, treasuring things\x01",
            "is a very good\x01",
            "mentality.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's not good that she made me\x01",
            "worry, but I'd like for Momo to\x01",
            "always have that mental attitude.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A4B")

    Jump("loc_5B08")

    label("loc_5A50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5A5E")
    Jump("loc_5B08")

    label("loc_5A5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5B08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5AB6")

    ChrTalk(
        0xFE,
        "Welcooome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We're Tallys',\x01",
            "supporters of this area!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5B08")

    label("loc_5AB6")


    ChrTalk(
        0xFE,
        (
            "Momo has gone to Sunday\x01",
            "School, so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We have to do our best\x01",
            "with work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B08")

    TalkEnd(0xFE)
    Return()

    # Function_22_547F end

    def Function_23_5B0C(): pass

    label("Function_23_5B0C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5B1D")
    Jump("loc_62C5")

    label("loc_5B1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5B2B")
    Jump("loc_62C5")

    label("loc_5B2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5BDC")

    ChrTalk(
        0xFE,
        (
            "Many orbal cars could be\x01",
            "seen heading towards the\x01",
            "border gates this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It looks like the foreign\x01",
            "residents were returning\x01",
            "to their home countries.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62C5")

    label("loc_5BDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5BEA")
    Jump("loc_62C5")

    label("loc_5BEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5BF8")
    Jump("loc_62C5")

    label("loc_5BF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5C06")
    Jump("loc_62C5")

    label("loc_5C06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5DB8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D16")

    ChrTalk(
        0xFE,
        (
            "I've just come back from\x01",
            "my drive to the\x01",
            "Bellguard Gate area...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "On the way home, I caught sight of\x01",
            "the West Crossbell Highway accident\x01",
            "scene in a great turmoil...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I never dreamed there\x01",
            "would be a derailment of\x01",
            "such grand scale...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5DB3")

    label("loc_5D16")


    ChrTalk(
        0xFE,
        (
            "On the way home, I caught sight of\x01",
            "the West Crossbell Highway accident\x01",
            "scene in a great turmoil...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It was crowded with\x01",
            "police and the CGF as\x01",
            "well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DB3")

    Jump("loc_62C5")

    label("loc_5DB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5DC6")
    Jump("loc_62C5")

    label("loc_5DC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5DD4")
    Jump("loc_62C5")

    label("loc_5DD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5DE2")
    Jump("loc_62C5")

    label("loc_5DE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_5DF0")
    Jump("loc_62C5")

    label("loc_5DF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5FD9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F22")

    ChrTalk(
        0xFE,
        (
            "My old woman is angry\x01",
            "and isn't saying a word\x01",
            "to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I suggested we see the long-\x01",
            "awaited unveiling ceremony\x01",
            "together, but she ignored me.\x02",
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
    Jump("loc_5FD4")

    label("loc_5F22")


    ChrTalk(
        0xFE,
        (
            "Hmph, come on. How long is she going\x01",
            "to remain angry with me just because\x01",
            "I made an expensive purchase...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If that's what my old\x01",
            "lady wants to do, I'll\x01",
            "just ignore her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FD4")

    Jump("loc_62C5")

    label("loc_5FD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5FE7")
    Jump("loc_62C5")

    label("loc_5FE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5FF5")
    Jump("loc_62C5")

    label("loc_5FF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_62C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_625C")

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
            "My old woman grumbled that it's\x01",
            "a useless waste, but buying it\x01",
            "was the right thing to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FA Verne Co. orbal car...\x01",
            "It has a chic design and\x01",
            "I think it's amazing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hoo, well, well... Although\x01",
            "you're still young, you\x01",
            "understand these things!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_618D")
    OP_63(0x109, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)

    label("loc_618D")

    Sleep(1000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_61B6")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_61B6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_61DC")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_61DC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6202")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_6202")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6228")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_6228")

    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00012F(They're kindred\x01",
            "spirits...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_62C5")

    label("loc_625C")


    ChrTalk(
        0xFE,
        (
            "Driving in this orbal\x01",
            "car is really the best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'd like my old lady to\x01",
            "understand that as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62C5")

    TalkEnd(0xFE)
    Return()

    # Function_23_5B0C end

    def Function_24_62C9(): pass

    label("Function_24_62C9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_62DA")
    Jump("loc_631B")

    label("loc_62DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_631B")

    ChrTalk(
        0xFE,
        (
            "I feel uneasy... I\x01",
            "wonder if an accident\x01",
            "occurred.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_631B")

    TalkEnd(0xFE)
    Return()

    # Function_24_62C9 end

    def Function_25_631F(): pass

    label("Function_25_631F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6330")
    Jump("loc_6371")

    label("loc_6330")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6371")

    ChrTalk(
        0xFE,
        (
            "I don't like the sounds\x01",
            "of ambulances very\x01",
            "much...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6371")

    TalkEnd(0xFE)
    Return()

    # Function_25_631F end

    def Function_26_6375(): pass

    label("Function_26_6375")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "When I saw the derailed\x01",
            "train, I couldn't\x01",
            "believe my eyes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems there are many\x01",
            "injured... I hope\x01",
            "they're all right...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_6375 end

    def Function_27_6400(): pass

    label("Function_27_6400")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_64AE")

    ChrTalk(
        0xFE,
        (
            "Jeez, the inside of my\x01",
            "shoes got soaked in the\x01",
            "blink of an eye!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's why I hate rain. I've\x01",
            "got to quickly finish what I\x01",
            "have to do and get home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6541")

    label("loc_64AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6541")

    ChrTalk(
        0xFE,
        (
            "Aah, jeez... Stupid rain!\x01",
            "There's nothing more\x01",
            "depressing than this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got to quickly\x01",
            "finish what I have to do\x01",
            "and get home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6541")

    TalkEnd(0xFE)
    Return()

    # Function_27_6400 end

    def Function_28_6545(): pass

    label("Function_28_6545")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_668A")

    ChrTalk(
        0xFE,
        (
            "Something like that\x01",
            "happened, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although it's not our\x01",
            "forte, we're guarding\x01",
            "the city like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although supposing it was the Empire's\x01",
            "doing, I think we'd be unlikely to be\x01",
            "attacked again immediately...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyhow, we can't let our guard\x01",
            "down until the referendum\x01",
            "three days from now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_674D")

    label("loc_668A")


    ChrTalk(
        0xFE,
        (
            "Although supposing it was the Empire's\x01",
            "doing, I think we'd be unlikely to be\x01",
            "attacked again immediately...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyhow, we can't let our guard\x01",
            "down until the referendum\x01",
            "three days from now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_674D")

    TalkEnd(0xFE)
    Return()

    # Function_28_6545 end

    def Function_29_6751(): pass

    label("Function_29_6751")

    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#00005FChief Sergei looks like\x01",
            "he's making something at\x01",
            "the Support Section...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FAnyway, it seems best if\x01",
            "we refrain from passing\x01",
            "through.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_29_6751 end

    def Function_30_67F2(): pass

    label("Function_30_67F2")

    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It looks like the door\x01",
            "is closed tightly.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x95, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6851")
    TalkEnd(0xFF)
    Call(0, 31)
    Return()

    label("loc_6851")

    TalkEnd(0xFF)
    Return()

    # Function_30_67F2 end

    def Function_31_6855(): pass

    label("Function_31_6855")

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
            "#00003F(What Pete, Quint and\x01",
            "Nielsen said before...)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_697D")
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    label("loc_697D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_69A3")
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    label("loc_69A3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_69C9")
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    label("loc_69C9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_69EF")
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    label("loc_69EF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6A15")
    OP_63(0x4, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    label("loc_6A15")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6A3B")
    OP_63(0x5, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    label("loc_6A3B")

    Sleep(1000)

    def lambda_6A43():
        TurnDirection(0x102, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6A43)
    Sleep(50)

    def lambda_6A53():
        TurnDirection(0x103, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6A53)

    def lambda_6A60():
        TurnDirection(0x104, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6A60)
    Sleep(50)

    def lambda_6A70():
        TurnDirection(0xF4, 0x101, 300)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_6A70)
    Sleep(50)

    def lambda_6A80():
        TurnDirection(0xF5, 0x101, 300)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_6A80)
    WaitChrThread(0xF5, 2)

    ChrTalk(
        0x102,
        (
            "#6P#00105FLloyd... Is something\x01",
            "wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FIs something the matter\x01",
            "with Lawyer Ian's\x01",
            "office?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00301FIt looks like no one's\x01",
            "there now...\x02",
        )
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
            "Let's go.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6BAD")

    ChrTalk(
        0x10A,
        "#12P#00605F...............\x02",
    )

    CloseMessageWindow()

    label("loc_6BAD")

    OP_5A()
    SetScenarioFlags(0x1BE, 0)
    OP_2C(0xB1, 0x3)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_31_6855 end

    def Function_32_6BCD(): pass

    label("Function_32_6BCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6BE4")
    Call(0, 49)
    Return()

    label("loc_6BE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6BF6")
    Call(0, 50)
    Return()

    label("loc_6BF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C72")

    ChrTalk(
        0x101,
        (
            "#00000FWe don't have any business outside\x01",
            "the city. It doesn't seem like we\x01",
            "need to use the car, either.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    label("loc_6C72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6D6E")
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
            "※The Support Section car\x01",
            "is now usable.\x02",
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

    label("loc_6D6E")

    SetMapFlags(0x80)
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6D89")
    Jump("loc_6DF9")

    label("loc_6D89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D98")
    Jump("loc_6DF9")

    label("loc_6D98")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6DB3")
    SetScenarioFlags(0x31, 2)

    label("loc_6DB3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6DF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_6DF3")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6DE8")
    Sound(2499, 255, 100, 0)
    Jump("loc_6DEE")

    label("loc_6DE8")

    Sound(3537, 255, 100, 0)

    label("loc_6DEE")

    Jump("loc_6DF9")

    label("loc_6DF3")

    Sound(3344, 255, 100, 0)

    label("loc_6DF9")

    SetMapObjFrame(0xA, "light", 0x0, 0x1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6E10")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_725A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_6E85")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Merkabah")
    MenuCmd(1, 0, "Cancel")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6E65"),
        (SWITCH_DEFAULT, "loc_6E76"),
    )


    label("loc_6E65")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_6E80")

    label("loc_6E76")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6E80")

    Jump("loc_7255")

    label("loc_6E85")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Use Orbal Car")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_6EDF")
    MenuCmd(1, 0, "Rest in Orbal Car")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6EDF")

    MenuCmd(1, 0, "Customize Orbal Car")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    MenuCmd(1, 0, "Cancel")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6FB6")

    ChrTalk(
        0x101,
        (
            "#00003FWith this, we've secured\x01",
            "the orbal car.\x02\x03",
            "#00001FFor now, let's head to\x01",
            "the station before the\x01",
            "operation starts.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_71BB")

    label("loc_6FB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_703F")

    ChrTalk(
        0x101,
        (
            "#00001FRight now we've got to chase after\x01",
            "Randy... Let's first perform a thorough\x01",
            "investigation inside the city.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_71BB")

    label("loc_703F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_70BC")

    ChrTalk(
        0x101,
        (
            "#00000FWe don't have any business outside\x01",
            "the city. It doesn't seem like we\x01",
            "need to use the car, either.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_71BB")

    label("loc_70BC")

    SetMapObjFrame(0xA, "light", 0x0, 0x1)
    OP_74(0xA, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_70ED")
    OP_70(0xA, 0x12C)
    OP_71(0xA, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_70FD")

    label("loc_70ED")

    OP_70(0xA, 0xF0)
    OP_71(0xA, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_70FD")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7153")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7153")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7176")
    Sound(461, 0, 100, 0)

    label("loc_7176")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7196")
    OP_70(0xA, 0x14A)
    OP_71(0xA, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_71A6")

    label("loc_7196")

    OP_70(0xA, 0x10E)
    OP_71(0xA, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_71A6")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0xA, "light", 0x1, 0x1)
    OP_70(0xA, 0x0)

    label("loc_71BB")

    Jump("loc_7255")

    label("loc_71C0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7236")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_71F9")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_7211")

    label("loc_71F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_720C")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_7211")

    label("loc_720C")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_7211")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7255")

    label("loc_7236")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_724B")
    Call(0, 33)
    Jump("loc_7255")

    label("loc_724B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7255")

    Jump("loc_6E10")

    label("loc_725A")

    SetMapObjFrame(0xA, "light", 0x1, 0x1)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_32_6BCD end

    def Function_33_7270(): pass

    label("Function_33_7270")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF000000), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x0)
    SetChrFlags(0x0, 0x8)
    SetChrFlags(0x1, 0x8)
    SetChrFlags(0x2, 0x8)
    SetChrFlags(0x3, 0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_72B6")
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    label("loc_72B6")

    SetMapObjFrame(0xFF, "main7", 0x0, 0x1)
    MiniGame(0x33, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFrame(0xFF, "main7", 0x1, 0x1)
    ClearChrFlags(0x0, 0x8)
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_731F")
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_731F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventEnd(0x5)
    SetMapFlags(0x80)
    Return()

    # Function_33_7270 end

    def Function_34_7331(): pass

    label("Function_34_7331")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_738C")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7381")
    Sound(2502, 255, 100, 0)
    Jump("loc_7387")

    label("loc_7381")

    Sound(2503, 255, 100, 0)

    label("loc_7387")

    Jump("loc_73B0")

    label("loc_738C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_73AA")
    Sound(3347, 255, 100, 0)
    Jump("loc_73B0")

    label("loc_73AA")

    Sound(3348, 255, 100, 0)

    label("loc_73B0")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_34_7331 end

    def Function_35_73C5(): pass

    label("Function_35_73C5")

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

    # Function_35_73C5 end

    def Function_36_7470(): pass

    label("Function_36_7470")

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

    def lambda_75D1():
        OP_97(0x101, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_75D1)
    Sleep(100)

    def lambda_75EE():
        OP_97(0x102, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_75EE)
    Sleep(300)

    def lambda_760B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_760B)
    Sleep(100)

    def lambda_761F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_761F)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x101, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    WaitChrThread(0x102, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_766C():
        OP_97(0x105, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_766C)
    Sleep(100)

    def lambda_7689():
        OP_97(0x109, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7689)
    Sleep(100)

    def lambda_76A6():
        OP_97(0x1A5, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A5, 0, lambda_76A6)
    Sleep(800)

    def lambda_76C3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_76C3)
    Sleep(100)

    def lambda_76D7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_76D7)
    Sleep(1000)

    def lambda_76EB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A5, 2, lambda_76EB)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00005F#5PTh-This is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00105FWh-When did this...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x109,
        (
            "#10105F#11PHuh? Was the rear\x01",
            "entrance always like\x01",
            "this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#5PWow... Looks like it's\x01",
            "under construction or\x01",
            "something.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x1A5, 0)

    ChrTalk(
        0x1A5,
        (
            "#11P#01105FOh, right. I guess you\x01",
            "guys don't know about it\x01",
            "yet.\x02\x03",
            "#01100FUmm, so after you guys\x01",
            "left, some construction\x01",
            "guys showed up.\x02\x03",
            "I think chief called\x01",
            "them.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7877():
        TurnDirection(0x101, 0x1A5, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7877)
    Sleep(50)

    def lambda_7887():
        TurnDirection(0x102, 0x1A5, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_7887)
    Sleep(50)

    def lambda_7897():
        TurnDirection(0x105, 0x1A5, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7897)
    Sleep(50)

    def lambda_78A7():
        TurnDirection(0x109, 0x1A5, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_78A7)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x101,
        (
            "#6P#00006FIs that right. I didn't\x01",
            "even notice yesterday.\x02\x03",
            "#00001FBut, what could chief be\x01",
            "planning?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103FHmm. There must be some\x01",
            "reason for this\x01",
            "construction, but...\x02\x03",
            "#00100FIn any case, it looks\x01",
            "like we shouldn't use\x01",
            "this entrance for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FYeah, let's leave via\x01",
            "the 1st floor entrance.\x02",
        )
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

    # Function_36_7470 end

    def Function_37_7A33(): pass

    label("Function_37_7A33")

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
        "#00005F#5PAh...\x02",
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
        (
            "#01002F#5PYeah, they did good\x01",
            "work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#5PChief, what's this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#5PIs this for the orbal\x01",
            "car?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#01004F#5PYeah, they constructed\x01",
            "this driveway and added\x01",
            "a parking space.\x02\x03",
            "#01004FAnd with HQ funds, no\x01",
            "less.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102F#5PIncredible!\x02\x03",
            "#10109FThere's even enough\x01",
            "space to service it\x01",
            "right here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#5PLife with an orbal car,\x01",
            "huh. There are a lot of\x01",
            "benefits to owning one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#5PHaha, I think KeA will\x01",
            "be thrilled.\x02",
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

    def lambda_8166():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8166)
    Sleep(50)

    def lambda_8176():
        OP_93(0x109, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8176)
    Sleep(50)

    def lambda_8186():
        OP_93(0x105, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8186)
    Sleep(50)

    def lambda_8196():
        OP_93(0x102, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8196)
    Sleep(50)

    def lambda_81A6():
        OP_93(0x14, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_81A6)
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

    def lambda_8217():
        OP_96(0xFE, 0x3C8C, 0x0, 0xFFFFDAE4, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8217)

    def lambda_8231():
        OP_96(0xFE, 0x3BC4, 0x0, 0xFFFFE08E, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8231)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00002F#11POh, hey there Ryｹ and\x01",
            "Henry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109F#11PHaha, we meet again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PSweet! I've never seen a\x01",
            "car like this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PWait... Did you guys buy\x01",
            "this?!\x02",
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
            "#00100F#11PIs she walking home with\x01",
            "Momo?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#6PNo clue.\x02",
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
            "#6PKeA had something to do\x01",
            "for Sister Marble and\x01",
            "stayed behind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PSo she might still be at\x01",
            "the cathedral.\x02",
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
        (
            "#00108F#11PI wonder if there's\x01",
            "something wrong...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)

    def lambda_8602():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8602)
    Sleep(50)

    def lambda_8612():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8612)
    Sleep(50)

    def lambda_8622():
        TurnDirection(0x14, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_8622)
    Sleep(50)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x14, 0)
    OP_64(0x101)
    OP_64(0x102)

    ChrTalk(
        0x105,
        (
            "#10302F#6POh brother, you guys are\x01",
            "as overprotective as\x01",
            "ever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109F#5PCan you blame them? KeA\x01",
            "is just so adorable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#11PN-No, I don't think\x01",
            "that's the only\x01",
            "reason...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00112F#11PIt's common sense for us\x01",
            "to worry. We're her\x01",
            "guardians.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#01004F#6PIf you're that worried,\x01",
            "why not head over to the\x01",
            "cathedral and pick her up?\x02\x03",
            "#01002FNow that you've got your\x01",
            "own wheels.\x02",
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
        (
            "#00102F#11PNoｱl, can we count on\x01",
            "you?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_884F():
        TurnDirection(0x101, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_884F)
    Sleep(50)

    def lambda_885F():
        TurnDirection(0x105, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_885F)
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
            "#6PNo way, you're going to\x01",
            "pick up KeA!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PMe too me too! Let me\x01",
            "ride too!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_88F4():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_88F4)
    Sleep(15)

    def lambda_8904():
        OP_93(0x102, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8904)
    Sleep(15)

    def lambda_8914():
        OP_93(0x109, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8914)
    Sleep(15)

    def lambda_8924():
        OP_93(0x105, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8924)
    Sleep(15)

    def lambda_8934():
        OP_93(0x14, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_8934)
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
        "#5PH-Hey, Ryｹ!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PGramps told us to head\x01",
            "back soon.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)

    ChrTalk(
        0x8,
        (
            "#12PAww, I forgot about\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PSis is back home today\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#11PHaha, well it sounds\x01",
            "like you two had better\x01",
            "head home right away.\x02\x03",
            "#00002FDon't worry, we'll give\x01",
            "you a ride soon.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8A89():
        OP_93(0x8, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_8A89)
    Sleep(50)

    def lambda_8A99():
        OP_93(0x9, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_8A99)
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
        "#6PWell then we're off.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F#11PRight. Take care, you\x01",
            "two.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8B11():
        OP_93(0x8, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_8B11)
    Sleep(50)

    def lambda_8B21():
        OP_93(0x9, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_8B21)
    Sleep(50)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x9, 0)
    OP_68(19000, 800, -8750, 2500)

    def lambda_8B4A():
        OP_96(0xFE, 0x2742, 0x0, 0xFFFFDF30, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8B4A)
    Sleep(50)

    def lambda_8B67():
        OP_96(0xFE, 0x2486, 0x0, 0xFFFFE796, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8B67)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    OP_6F(0x79)
    OP_93(0x14, 0x87, 0x1F4)

    ChrTalk(
        0x14,
        (
            "#01003F#5PAlright, go pick her up\x01",
            "already.\x02\x03",
            "#01000FI'll be heading back\x01",
            "now.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8BEE():
        TurnDirection(0x101, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8BEE)
    Sleep(50)

    def lambda_8BFE():
        TurnDirection(0x102, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8BFE)
    Sleep(50)

    def lambda_8C0E():
        TurnDirection(0x109, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8C0E)
    Sleep(50)

    def lambda_8C1E():
        TurnDirection(0x105, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8C1E)
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
        (
            "#00100F#11PLet's get going\x01",
            "everyone.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(19000, 800, -9350, 2500)

    def lambda_8C95():
        OP_93(0xFE, 0xB4, 0x96)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8C95)

    def lambda_8CA2():
        OP_93(0xFE, 0xB4, 0xFA)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_8CA2)

    def lambda_8CAF():
        OP_93(0xFE, 0xB4, 0x96)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8CAF)

    def lambda_8CBC():
        OP_93(0xFE, 0xB4, 0x96)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8CBC)
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
            "#10104F#5PRight, let's head to the\x01",
            "cathedral.\x02\x03",
            "#10100FFrom here, we should head to\x01",
            "Central Square and then through\x01",
            "the Entertainment District.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8DA3():
        TurnDirection(0x101, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8DA3)
    Sleep(50)

    def lambda_8DB3():
        TurnDirection(0x102, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8DB3)
    Sleep(50)

    def lambda_8DC3():
        TurnDirection(0x105, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8DC3)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        (
            "#00002F#12PSounds good. We're\x01",
            "counting on you!\x02\x03",
            "#00004FI can't wait to see the\x01",
            "look on KeA's face when\x01",
            "she sees this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F#12PHaha, she really does\x01",
            "love cars, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#6POh good grief. You guys\x01",
            "are seriously doting\x01",
            "parents.\x02",
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

    def lambda_8FB2():
        OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_8FB2)

    def lambda_8FC7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_8FC7)
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
        "#30W...Grooowl...\x02",
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

    # Function_37_7A33 end

    def Function_38_912A(): pass

    label("Function_38_912A")

    SetChrPos(0xFE, -36200, 0, 4000, 90)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -5850, 0, 4000)
    OP_9F(0x1, 800, 0, 1800)
    OP_9F(0x1, 8050, 0, -5950)
    OP_9F(0x1, 15500, 0, -6700)
    OP_9F(0x2, 0xFE, 5000, 0x6)
    Return()

    # Function_38_912A end

    def Function_39_9181(): pass

    label("Function_39_9181")

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

    # Function_39_9181 end

    def Function_40_9216(): pass

    label("Function_40_9216")

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

    # Function_40_9216 end

    def Function_41_92AF(): pass

    label("Function_41_92AF")

    OP_95(0xFE, 19000, 0, -8600, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(200)

    def lambda_92D2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_92D2)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_41_92AF end

    def Function_42_92E3(): pass

    label("Function_42_92E3")

    OP_95(0xFE, 19000, 0, -8600, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(200)

    def lambda_9306():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9306)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_42_92E3 end

    def Function_43_9317(): pass

    label("Function_43_9317")

    OP_95(0xFE, 19000, 0, -8600, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(200)

    def lambda_933A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_933A)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_43_9317 end

    def Function_44_934B(): pass

    label("Function_44_934B")

    OP_95(0xFE, 19000, 0, -8600, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(200)

    def lambda_936E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_936E)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_44_934B end

    def Function_45_937F(): pass

    label("Function_45_937F")

    Sleep(4500)
    StopSound(468, 1000, 80)
    Sound(492, 0, 80, 0)
    Return()

    # Function_45_937F end

    def Function_46_938F(): pass

    label("Function_46_938F")

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

    def lambda_9515():
        OP_97(0x101, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9515)
    Sleep(50)

    def lambda_9532():
        OP_97(0x102, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_9532)
    Sleep(50)

    def lambda_954F():
        OP_97(0x105, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_954F)
    Sleep(50)

    def lambda_956C():
        OP_97(0x109, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_956C)
    Sleep(50)

    def lambda_9589():
        OP_97(0x104, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_9589)
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

    def lambda_964E():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_964E)
    Sleep(50)

    def lambda_965E():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_965E)
    Sleep(50)

    def lambda_966E():
        OP_93(0x105, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_966E)
    Sleep(50)

    def lambda_967E():
        OP_93(0x109, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_967E)
    Sleep(50)

    def lambda_968E():
        OP_93(0x104, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_968E)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x101,
        "#5P#00005FWhat's that?\x02",
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

    def lambda_97C9():

        label("loc_97C9")

        OP_A0(0xFE, 1500, 0x0, 0x4)
        Yield()
        Jump("loc_97C9")

    QueueWorkItem2(0x18, 2, lambda_97C9)

    def lambda_97DB():
        OP_96(0xFE, 0x7FBC, 0xFFFFF8F8, 0xFFFFAD30, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_97DB)
    Sound(847, 2, 70, 0)
    WaitChrThread(0x18, 1)
    BeginChrThread(0x18, 3, 0, 47)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_981D():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_981D)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_9845():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9845)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_986D():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_986D)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_9895():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9895)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_98BD():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_98BD)
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
        "#00011F#6PW-What!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10111F#6PA-A white hawk?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305F#6PNo. It looks like a\x01",
            "falcon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#6PHey now, what're ya\x01",
            "doin' in the middle of a\x01",
            "city like this?\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x18, 0x3)
    WaitChrThread(0x18, 1)
    EndChrThread(0x18, 0x0)
    OP_68(33300, -2800, -20900, 3000)
    MoveCamera(40, 21, 0, 3000)

    def lambda_99F8():
        OP_9E(0xFE, 0x878C, 0xFFFFAD30, 0x50910, 0xED8, 0x1)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_99F8)
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

    def lambda_9B7B():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9B7B)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xBEA), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC1C), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC4E), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)

    def lambda_9BC4():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9BC4)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC80), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xCB2), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xCE4), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xD16), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)

    def lambda_9C0D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9C0D)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xD48), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xD7A), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xDAC), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xDDE), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)

    def lambda_9C56():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_9C56)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xE10), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xE42), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xE74), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xEA6), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)

    def lambda_9C9F():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9C9F)
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

    def lambda_9D43():
        OP_96(0xFE, 0x8278, 0xFFFFF1F0, 0xFFFFAA74, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_9D43)
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
            "Scree.\x02\x03",
            "Scree, scree, scree.\x02",
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
            "#00001F#5PI-It can't be... Does it\x01",
            "have business with us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00108FIt seems like it's the\x01",
            "same as when Zeit\x01",
            "speaks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00306FHmm, if PeTiote was here,\x01",
            "we could understand what\x01",
            "he's saying, but...\x02",
        )
    )

    CloseMessageWindow()
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x5, 0x10)
    OP_71(0x5, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x5)
    ClearChrFlags(0x17, 0x80)

    def lambda_9F86():
        OP_96(0xFE, 0x9A4C, 0xFFFFF060, 0xFFFFB5C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_9F86)

    def lambda_9FA0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_9FA0)
    WaitChrThread(0x17, 1)
    Sound(104, 0, 100, 0)
    OP_71(0x5, 0xA, 0x0, 0x0, 0x0)

    ChrTalk(
        0x17,
        "#01105F#12PHuh? What's the matter?\x02",
    )

    OP_79(0x5)
    SetMapObjFlags(0x5, 0x10)
    CloseMessageWindow()
    OP_63(0x17, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrChipByIndex(0x17, 0x22)
    SetChrSubChip(0x17, 0x0)

    def lambda_A01B():
        OP_95(0xFE, 37500, -4000, -19000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_A01B)
    WaitChrThread(0x17, 1)

    def lambda_A039():
        OP_95(0xFE, 34500, -4000, -21300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_A039)
    Sleep(300)

    def lambda_A056():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A056)
    Sleep(100)

    def lambda_A066():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_A066)
    Sleep(100)

    def lambda_A076():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A076)
    Sleep(100)

    def lambda_A086():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_A086)
    WaitChrThread(0x17, 1)
    SetChrChipByIndex(0x17, 0x21)
    SetChrSubChip(0x17, 0x0)
    OP_93(0x17, 0xE1, 0x1F4)
    Sound(3029, 255, 100, 0)

    ChrTalk(
        0x17,
        (
            "#01110F#11PWah! A white bird!\x02\x03",
            "#01109FHis sharp beak is so\x01",
            "cool!\x02",
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
            "#6P#08009FScree㈱\x02\x03",
            "Scree, scree, scree㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#01103F#11PHmm, hmm.\x02\x03",
            "#01102FI see, so that's what it\x01",
            "was.\x02",
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
            "#00012F#5P(KeA... I guess she\x01",
            "understands him?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10112F#5P(A-Amazing...)\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x17, 0x101, 500)

    def lambda_A247():

        label("loc_A247")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_A247")

    QueueWorkItem2(0x17, 2, lambda_A247)
    SetChrChipByIndex(0x18, 0x1F)
    SetChrSubChip(0x18, 0x2)

    ChrTalk(
        0x17,
        (
            "#01100F#11PUm, this little guy says\x01",
            "his name is "Sieg".\x02\x03",
            "He says he has a message\x01",
            "for you guys, and he\x01",
            "wants you to take it.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A2E3():
        TurnDirection(0x101, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A2E3)
    Sleep(50)

    def lambda_A2F3():
        TurnDirection(0x104, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_A2F3)
    Sleep(50)

    def lambda_A303():
        TurnDirection(0x109, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_A303)
    Sleep(50)

    def lambda_A313():
        TurnDirection(0x105, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_A313)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        "#00011F#5PO-Oh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00305FAh, he really does have\x01",
            "a note attached to his\x01",
            "leg.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A38D():
        OP_95(0xFE, 33200, -4000, -21000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A38D)
    TurnDirection(0x18, 0x101, 500)
    WaitChrThread(0x101, 1)
    EndChrThread(0x17, 0x2)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd took the memo that\x01",
            "was fastened to the\x01",
            "white falcon's leg.\x07\x00\x02",
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
            "Dear Crossbell Police,\x01",
            "Special Support Section.\x02\x03",
            "Pardon my rudeness for\x01",
            "contacting you, but your fame\x01",
            "has reached my ears.\x02\x03",
            "If you have time, would you\x01",
            "be willing to consult with me\x01",
            "privately?\x02\x03",
            "I will be waiting for you\x01",
            "this evening at the meeting\x01",
            "terrace of Crossbell Airport.\x02\x03",
            "P.S.: In case you cannot make\x01",
            "it, it is all right if you do\x01",
            "not reply.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(150)

    AnonymousTalk(
        0x101,
        "#00005F...............\x02",
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
            "#10106FWith the contents being what they\x01",
            "are and with an unknown sender...\x01",
            "This is just too suspicious!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x105,
        (
            "#10302FHowever, the handwriting\x01",
            "is beautiful and the\x01",
            "tone is so polite...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x104,
        (
            "#00301FMost importantly, the\x01",
            "white falcon crest that's\x01",
            "stamped on this memo is...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x18,
        (
            "#08000FScree.\x02\x03",
            "Scree, scree, scree.\x02",
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

    def lambda_A7A6():
        OP_96(0xFE, 0x8278, 0xFFFFF3E4, 0xFFFFAA74, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_A7A6)
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

    def lambda_A82C():

        label("loc_A82C")

        OP_A0(0xFE, 1500, 0x0, 0x4)
        Yield()
        Jump("loc_A82C")

    QueueWorkItem2(0x18, 2, lambda_A82C)
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

    def lambda_AA61():
        OP_96(0xFE, 0x8278, 0xFFFFFED4, 0xFFFF7B94, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_AA61)
    Sleep(300)

    def lambda_AA7E():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_AA7E)
    Sleep(100)

    def lambda_AA8E():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_AA8E)
    Sleep(100)

    def lambda_AA9E():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_AA9E)
    Sleep(100)

    def lambda_AAAE():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_AAAE)
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
            "#6P#00011FUmm... KeA, what did he\x01",
            "say?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x17, 0x101, 500)

    ChrTalk(
        0x17,
        (
            "#01111F#11PHmm. "Whether to come or\x01",
            "not is up to you", he\x01",
            "says.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00003FIs that so...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    def lambda_AC30():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_AC30)
    Sleep(50)

    def lambda_AC40():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_AC40)
    Sleep(50)

    def lambda_AC50():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_AC50)
    Sleep(50)

    def lambda_AC60():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_AC60)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x102,
        (
            "#6P#00108FS-So? What will you do?\x02\x03",
            "#00101FI think it's impossible,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#00306FYeah, seriously.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F#11PBut, this white falcon\x01",
            "crest... It looked like\x01",
            "that bird just now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309F#5PAhaha. Now I'm looking\x01",
            "forward to this even\x01",
            "more.\x02",
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
            "#12P#00003F─The sender took the trouble to\x01",
            "invite us. We should accept.\x02\x03",
            "#00000FThere's still time until evening,\x01",
            "so let's finish whatever else we\x01",
            "have to do before then.\x02",
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
        "#10106F#11PI-I'm kind of nervous...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00309FWell, I don't think we\x01",
            "need to go in uniform,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#5PHaha. Well, once we're through with\x01",
            "everything, let's head to Crossbell\x01",
            "Airport past the South entrance.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x17, 0x13B, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x17,
        (
            "#11P#01110FI don't really get it\x01",
            "but, good luck everyone!\x02",
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

    # Function_46_938F end

    def Function_47_AFE8(): pass

    label("Function_47_AFE8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B017")

    def lambda_AFF8():
        OP_9E(0xFE, 0x8980, 0xFFFFAD30, 0x57E40, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_AFF8)
    WaitChrThread(0x18, 1)
    Jump("Function_47_AFE8")

    label("loc_B017")

    Return()

    # Function_47_AFE8 end

    def Function_48_B018(): pass

    label("Function_48_B018")


    def lambda_B01D():
        OP_9E(0xFE, 0x846C, 0xFFFFAA74, 0x2BF20, 0xED8, 0x1)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_B01D)
    WaitChrThread(0x18, 1)

    def lambda_B03C():
        OP_9E(0xFE, 0x8084, 0xFFFFAA74, 0x57E40, 0x1194, 0x1)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_B03C)
    WaitChrThread(0x18, 1)
    Return()

    # Function_48_B018 end

    def Function_49_B057(): pass

    label("Function_49_B057")

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
            "#00206F#12PCome to think of it...\x02\x03",
            "#00200FThis is also the last\x01",
            "day Noｱl will be driving\x01",
            "for us.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B175():
        OP_93(0x109, 0xB3, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B175)
    Sleep(400)

    ChrTalk(
        0x101,
        "#12P#00006FI see... That's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112F#5PAhaha... I too think\x01",
            "it's a pity.\x02\x03",
            "This car... I quite like\x01",
            "it on a personal level.\x02\x03",
            "#10100FHowever, you all can\x01",
            "already drive it rather\x01",
            "well, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00004FYeah. You trained us on\x01",
            "our days off, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00109F*giggle*. Your drills\x01",
            "were easy to understand\x01",
            "and very helpful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10306FHmm. But, they were pretty\x01",
            "rough, weren't they?\x02\x03",
            "#10302FRather than a Sergeant\x01",
            "Major, it felt more like\x01",
            "you were a drill sergeant.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x109, 0x105, 500)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#11P#10101FT-That was because of\x01",
            "your incessant backtalk,\x01",
            "you know?\x02\x03",
            "#10106FYou can do it if you\x01",
            "try, but you don't have\x01",
            "the traffic rules down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F#11PWell for a soldier, being able\x01",
            "to give harsh instruction is a\x01",
            "necessary skill.\x02\x03",
            "#00300FAnyway, we'll enjoy the skills\x01",
            "of a pro driver for at least\x01",
            "one more day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00002FYeah. Noｱl, we're\x01",
            "counting on you.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    ChrTalk(
        0x109,
        (
            "#10109F#5PYes, please leave it to\x01",
            "me!\x02",
        )
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

    # Function_49_B057 end

    def Function_50_B566(): pass

    label("Function_50_B566")

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
            "#11P#00002FOur car... Looks like\x01",
            "it's all in one piece,\x01",
            "somehow.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BA4C")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B6B9")

    ChrTalk(
        0x109,
        (
            "#6P#10109FThank goodness... That's\x01",
            "a relief.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B6B9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B89A")

    ChrTalk(
        0x105,
        (
            "#6P#10405FStill, if I remember correctly,\x01",
            "Mayor Dieter financed this to\x01",
            "some extent...\x02\x03",
            "#10409FHehe. Using it to arrest him is\x01",
            "rather ironic, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B76B():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B76B)
    Sleep(50)

    def lambda_B77B():
        TurnDirection(0x103, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_B77B)
    Sleep(50)

    def lambda_B78B():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B78B)
    Sleep(50)

    def lambda_B79B():
        TurnDirection(0x104, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_B79B)
    Sleep(50)

    def lambda_B7AB():
        TurnDirection(0xF4, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_B7AB)
    Sleep(50)

    def lambda_B7BB():
        TurnDirection(0xF5, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_B7BB)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)

    ChrTalk(
        0x102,
        (
            "#12P#00106F...Indeed, you're quite\x01",
            "right.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B87C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B857")

    ChrTalk(
        0x109,
        "#12P#10101FNow look here Wazy...\x02",
    )

    CloseMessageWindow()
    Jump("loc_B87C")

    label("loc_B857")


    ChrTalk(
        0x109,
        "#6P#10101FNow look here Wazy...\x02",
    )

    CloseMessageWindow()

    label("loc_B87C")


    ChrTalk(
        0x103,
        "#00211FNot funny...\x02",
    )

    CloseMessageWindow()
    Jump("loc_BA47")

    label("loc_B89A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BA47")

    ChrTalk(
        0x10A,
        (
            "#6P#00603FHmm... Looks like it's in good\x01",
            "shape.\x02\x03",
            "#00600FStill, if I remember correctly,\x01",
            "I heard Mayor Dieter financed\x01",
            "this to some degree...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B941():
        TurnDirection(0x102, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B941)
    Sleep(50)

    def lambda_B951():
        TurnDirection(0x103, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_B951)
    Sleep(50)

    def lambda_B961():
        TurnDirection(0x101, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B961)
    Sleep(50)

    def lambda_B971():
        TurnDirection(0x104, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_B971)
    Sleep(50)

    def lambda_B981():
        TurnDirection(0xF4, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_B981)
    Sleep(50)

    def lambda_B991():
        TurnDirection(0xF5, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_B991)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)

    ChrTalk(
        0x102,
        (
            "#12P#00108FN-Now that you mention\x01",
            "it...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BA22")

    ChrTalk(
        0x109,
        (
            "#6P#10106FIndeed, Chief Sergei did\x01",
            "say that...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BA22")


    ChrTalk(
        0x103,
        "#00211F...It's a little ironic.\x02",
    )

    CloseMessageWindow()

    label("loc_BA47")

    Jump("loc_BB8E")

    label("loc_BA4C")


    ChrTalk(
        0x109,
        (
            "#6P#10104FThank goodness... That's\x01",
            "a relief.\x02\x03",
            "#10105F...By the way, this car\x01",
            "was financed by Mayor\x01",
            "Dieter, wasn't it.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BACC():
        TurnDirection(0x102, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_BACC)
    Sleep(50)

    def lambda_BADC():
        TurnDirection(0x103, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_BADC)
    Sleep(50)

    def lambda_BAEC():
        TurnDirection(0x101, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BAEC)
    Sleep(50)

    def lambda_BAFC():
        TurnDirection(0x104, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_BAFC)
    Sleep(50)

    def lambda_BB0C():
        TurnDirection(0xF4, 0x109, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_BB0C)
    Sleep(50)

    def lambda_BB1C():
        TurnDirection(0xF5, 0x109, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_BB1C)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)

    ChrTalk(
        0x102,
        (
            "#12P#00108FN-Now that you mention\x01",
            "it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00211F...It's a little ironic.\x02",
    )

    CloseMessageWindow()

    label("loc_BB8E")

    OP_93(0x104, 0x13B, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x104,
        (
            "#00304FWell, no matter the details,\x01",
            "this gal's a member of the\x01",
            "Support Section too.\x02\x03",
            "#00302FLet's check her out inside\x01",
            "too, to see if we can use\x01",
            "her properly or not.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)

    ChrTalk(
        0x101,
        "#11P#00000FYeah, right.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x23, 1)
    NewScene("e2010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_50_B566 end

    def Function_51_BC7F(): pass

    label("Function_51_BC7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BD25")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000FWest Crossbell highway is\x01",
            "up ahead.\x02\x03",
            "There's a Wanted Monster,\x01",
            "but... Let's finish up our\x01",
            "jobs inside the city first.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -34230, 0, 4210, 90)
    EventEnd(0x4)
    Return()

    label("loc_BD25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BE18")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BDB8")

    ChrTalk(
        0x101,
        (
            "#00000FWest Crossbell highway\x01",
            "is up ahead.\x02\x03",
            "We don't have any\x01",
            "special business this\x01",
            "way, so let's not exit.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_BE04")

    label("loc_BDB8")


    ChrTalk(
        0x101,
        (
            "#00000FWe don't have any\x01",
            "special business this\x01",
            "way, so let's not exit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BE04")

    SetChrPos(0x0, -34230, 0, 4210, 90)
    EventEnd(0x4)
    Return()

    label("loc_BE18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BE92")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001FWe've got to chase after\x01",
            "Randy... This is no time\x01",
            "to be wandering around.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -34230, 0, 4210, 90)
    EventEnd(0x4)
    Return()

    label("loc_BE92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BEFD")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001FThis is no time to be\x01",
            "leaving the city. Let's\x01",
            "turn around.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -34230, 0, 4210, 90)
    EventEnd(0x4)
    Return()

    label("loc_BEFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BFCF")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001FWe've come this far. There's no way\x01",
            "we're leaving the city now.\x02\x03",
            "The Orchis Tower infiltration\x01",
            "operation... We have to do whatever\x01",
            "it takes to make it a success.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -34230, 0, 4210, 90)
    EventEnd(0x4)
    Return()

    label("loc_BFCF")

    Return()

    # Function_51_BC7F end

    def Function_52_BFD0(): pass

    label("Function_52_BFD0")

    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C040")

    ChrTalk(
        0x101,
        (
            "#00000FLooks like it's locked\x01",
            "from the inside.\x02\x03",
            "Should we enter from the\x01",
            "front?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_C09B")

    label("loc_C040")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked. It\x01",
            "seems like it's been\x01",
            "locked from the inside.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_C09B")

    TalkEnd(0xFF)
    Return()

    # Function_52_BFD0 end

    SaveToFile()

Try(main)
