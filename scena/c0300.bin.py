from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0300.bin",                # FileName
        "c0300",                    # MapName
        "c0300",                    # Location
        0x002A,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("c0300", "c1000_1", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 42, 0, 3, 0, 4],
    )

    BuildStringList((
        "c0300",                  # 0
        "Old Man Luis",           # 1
        "Pentos",                 # 2
        "Yuri",                   # 3
        "Sykes",                  # 4
        "Reggie",                 # 5
        "ＯＬ",                   # 6
        "Secretary Lechter",      # 7
        "Harold",                 # 8
        "Ferric",                 # 9
        "Ries",                   # 10
        "車",                     # 11
        "暴走車",                 # 12
        "Hostess A",              # 13
        "Hostess B",              # 14
        "Mary",                   # 15
        "SE制御",                 # 16
        "bc0300",                 # 17
        "Central Square",         # 18
        "West Street",            # 19
        "Governmental District",  # 20
        "Residential Street",     # 21
        "Entertainment District", # 22
        "East Street",            # 23
        "Downtown",               # 24
        "Waterfront Area",        # 25
        "IBC",                    # 26
        "Station Street",         # 27
        "Back Street",            # 28
        "St. Ursula Byroad",      # 29
        "East Crossbell Highway", # 30
        "West Crossbell HIghway", # 31
        "Mainz Mountain Road",    # 32
        "Orchis Tower",           # 33
    ))

    ATBonus("ATBonus_7F4", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)

    Sepith("Sepith_907A", 8,   8,   8,   8,   11,  11,  11)

    MonsterBattlePostion("MonsterBattlePostion_844", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_848", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_84C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_850", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_854", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_858", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_85C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_860", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_8A4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_8A8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_8AC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_8B0", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_8B4", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_8B8", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_8BC", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_8C0", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_824", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_828", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_82C", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_830", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_834", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_838", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_83C", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_840", 2, 13, 180)

    # monster count: 2

    BattleInfo(
        "BattleInfo_8C4", 0x0000, 93, 6, 60, 4, 1, 25, 0, "bc0300", "Sepith_907A", 60, 30, 10, 0,
        (
            ("ms85100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_844", "MonsterBattlePostion_8A4", "ed7450", "ed7453", "ATBonus_7F4"),
            ("ms85100.dat", "ms85100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_824", "MonsterBattlePostion_8A4", "ed7450", "ed7453", "ATBonus_7F4"),
            ("ms85100.dat", "ms85100.dat", "ms85100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_844", "MonsterBattlePostion_8A4", "ed7450", "ed7453", "ATBonus_7F4"),
            (),
        )
    )

    AddCharChip((
        "chr/ch21602.itc",                   # 00
        "chr/ch33000.itc",                   # 01
        "chr/ch44100.itc",                   # 02
        "chr/ch47500.itc",                   # 03
        "chr/ch23600.itc",                   # 04
        "chr/ch49300.itc",                   # 05
        "chr/ch12400.itc",                   # 06
        "chr/ch09300.itc",                   # 07
        "chr/ch22000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "monster/ch85150.itc",               # 10
        "monster/ch85151.itc",               # 11
    ))

    DeclNpc(4294954446, 4294961396, 4294935807, 315,  261,  0x0, 0,   0,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(32279,   0,       4294962927, 270,  257,  0x0, 0,   1,   0,   0,   1,   0,   7,   255,  0)
    DeclNpc(5699,    200,     4900,    180,  389,  0x0, 0,   2,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(5699,    0,       469,     360,  389,  0x0, 0,   3,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(7900,    200,     2450,    270,  389,  0x0, 0,   4,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(239,     4294966546, 4294918576, 0,    385,  0x0, 0,   5,   0,   0,   2,   0,   11,  255,  0)
    DeclNpc(4294961847, 4294961296, 4294931017, 270,  385,  0x0, 0,   6,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(9789,    0,       4294955656, 45,   389,  0x0, 0,   7,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(4294965907, 0,       4294936967, 135,  389,  0x0, 0,   8,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(4294966936, 4294961376, 0,       0x10100B4,    "BattleInfo_8C4", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4294956016, 4294941006, 4294961296, 0x10100B4,    "BattleInfo_8C4", 0,   16,  0xFFFF, 0,  1)

    DeclEvent(0x0000, 0, 30,  -7.0,                  -19.739999771118164,   -5.5,                  100.0,                 [0.09999999403953552,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   0.6999999284744263,    9.869999885559082,     1.0999999046325684,    1.0])
    DeclEvent(0x0000, 0, 40,  -7.0,                  -8.34000015258789,     -1.0,                  100.0,                 [0.09998477250337601,  0.008726206608116627,  -0.0,                  0.0,                   -0.0017452412284910679, 0.49992382526397705,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   0.6853380799293518,    4.230448246002197,     0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 38,  -7.5,                  -7.0,                  -0.0,                  100.0,                 [0.09993909299373627,  0.0174497552216053,    -0.0,                  0.0,                   -0.0034899513702839613, 0.49969542026519775,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   0.7251135110855103,    3.6287410259246826,    -0.0,                  1.0])
    DeclEvent(0x0000, 0, 41,  2.359999895095825,     -5.079999923706055,    -0.0,                  64.0,                  [0.4993147850036621,   0.006541998125612736,  -0.0,                  0.0,                   -0.026167992502450943, 0.12482869625091553,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -1.3113162517547607,   0.6186906695365906,    -0.0,                  1.0])

    DeclActor(4294961826, 4294961296, 4294925746, 1200,    4294957326, 4294960796, 4294925366, 0x007C, 0,  19, 0x0000)
    DeclActor(4294954716, 0,       4294961596, 1500,    4294954716, 2000,    4294961596, 0x007C, 0,  27, 0x0000)
    DeclActor(4294948796, 4294961696, 4294950696, 2000,    4294948796, 4294962896, 4294950696, 0x007C, 0,  28, 0x0000)
    DeclActor(17650,   0,       4294966496, 2000,    17650,   1500,    4294966496, 0x007C, 0,  17, 0x0000)
    DeclActor(0,       0,       4294966526, 2000,    0,       1500,    4294966526, 0x007C, 0,  16, 0x0000)
    DeclActor(4294931966, 4294962346, 4294925346, 1200,    4294931966, 4294963346, 4294925346, 0x007C, 0,  5,  0x0000)
    DeclActor(4294948796, 4294961696, 4294950696, 2000,    4294948796, 4294962896, 4294950696, 0x007C, 0,  18, 0x0000)
    DeclActor(4294964596, 4294960796, 4294929296, 2000,    4294964596, 4294961796, 4294929296, 0x007C, 0,  42, 0x0000)

    PlaceName(167.6699981689453, 0.0, -124.73999786376953, 0x0000, 0x0000, "Central Square")
    PlaceName(61.15999984741211, 0.0, -117.44999694824219, 0x0000, 0x0000, "West Street")
    PlaceName(211.41000366210938, 0.0, 19.440000534057617, 0x0000, 0x0000, "Governmental District")
    PlaceName(-37.66999816894531, 0.0, 3.240000009536743, 0x0000, 0x0000, "Residential Street")
    PlaceName(80.5999984741211, 0.0, -9.720000267028809, 0x0000, 0x0000, "Entertainment District")
    PlaceName(299.29998779296875, 0.0, -162.0, 0x0000, 0x0000, "East Street")
    PlaceName(356.80999755859375, 0.0, -251.10000610351562, 0x0000, 0x0000, "Downtown")
    PlaceName(344.6600036621094, 0.0, -55.08000183105469, 0x0000, 0x0000, "Waterfront Area")
    PlaceName(302.5400085449219, 0.0, 97.19999694824219, 0x0000, 0x0000, "IBC")
    PlaceName(185.89999389648438, 0.0, -236.52000427246094, 0x0000, 0x0000, "Station Street")
    PlaceName(109.76000213623047, 0.0, -68.04000091552734, 0x0000, 0x0000, "Back Street")
    PlaceName(181.0399932861328, 0.0, -286.739990234375, 0x0000, 0x0000, "St. Ursula Byroad")
    PlaceName(386.7799987792969, 0.0, -139.32000732421875, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-21.469999313354492, 0.0, -119.87999725341797, 0x0000, 0x0000, "West Crossbell HIghway")
    PlaceName(-11.75, 0.0, 42.119998931884766, 0x0000, 0x0000, "Mainz Mountain Road")
    PlaceName(200.0, 0.0, 231.5, 0x0000, 0x0000, "Orchis Tower")
    PlaceName(132.02999877929688, 0.0, -147.4199981689453, 0x0000, 0x0051, "")
    PlaceName(219.11000061035156, 0.0, -105.30000305175781, 0x0000, 0x0054, "")
    PlaceName(171.72000122070312, 0.0, -160.3800048828125, 0x0000, 0x0057, "")
    PlaceName(130.82000732421875, 0.0, -100.44000244140625, 0x0000, 0x0053, "")
    PlaceName(164.02999877929688, 0.0, -61.560001373291016, 0x0000, 0x0053, "")
    PlaceName(81.80999755859375, 0.0, -108.54000091552734, 0x0000, 0x0053, "")
    PlaceName(66.0199966430664, 0.0, -74.5199966430664, 0x0000, 0x0053, "")
    PlaceName(104.9000015258789, 0.0, -22.68000030517578, 0x0000, 0x0052, "")
    PlaceName(112.58999633789062, 0.0, -43.7400016784668, 0x0000, 0x0053, "")
    PlaceName(126.7699966430664, 0.0, -57.5099983215332, 0x0000, 0x0053, "")
    PlaceName(172.94000244140625, 0.0, 57.5099983215332, 0x0000, 0x0051, "")
    PlaceName(354.3800048828125, 0.0, -162.0, 0x0000, 0x0052, "")
    PlaceName(326.8399963378906, 0.0, -308.6099853515625, 0x0000, 0x0053, "")
    PlaceName(305.7799987792969, 0.0, -278.6400146484375, 0x0000, 0x0053, "")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4, 5])                    # 1

    ScpFunction((
        "Function_0_A24",          # 00, 0
        "Function_1_AD4",          # 01, 1
        "Function_2_B35",          # 02, 2
        "Function_3_B96",          # 03, 3
        "Function_4_F91",          # 04, 4
        "Function_5_16DB",         # 05, 5
        "Function_6_182D",         # 06, 6
        "Function_7_272C",         # 07, 7
        "Function_8_39D2",         # 08, 8
        "Function_9_3AFE",         # 09, 9
        "Function_10_3BBB",        # 0A, 10
        "Function_11_3D27",        # 0B, 11
        "Function_12_3E2E",        # 0C, 12
        "Function_13_4386",        # 0D, 13
        "Function_14_44F8",        # 0E, 14
        "Function_15_4DF8",        # 0F, 15
        "Function_16_5113",        # 10, 16
        "Function_17_56AF",        # 11, 17
        "Function_18_570F",        # 12, 18
        "Function_19_573F",        # 13, 19
        "Function_20_5804",        # 14, 20
        "Function_21_5990",        # 15, 21
        "Function_22_59D9",        # 16, 22
        "Function_23_5A05",        # 17, 23
        "Function_24_5A1B",        # 18, 24
        "Function_25_6B81",        # 19, 25
        "Function_26_6BF2",        # 1A, 26
        "Function_27_6C08",        # 1B, 27
        "Function_28_6EF3",        # 1C, 28
        "Function_29_72CF",        # 1D, 29
        "Function_30_78C8",        # 1E, 30
        "Function_31_7E83",        # 1F, 31
        "Function_32_82A7",        # 20, 32
        "Function_33_82F2",        # 21, 33
        "Function_34_833D",        # 22, 34
        "Function_35_8388",        # 23, 35
        "Function_36_83D3",        # 24, 36
        "Function_37_841E",        # 25, 37
        "Function_38_8455",        # 26, 38
        "Function_39_891A",        # 27, 39
        "Function_40_8EAD",        # 28, 40
        "Function_41_8F8D",        # 29, 41
        "Function_42_9020",        # 2A, 42
    ))


    def Function_0_A24(): pass

    label("Function_0_A24")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_A5C"),
        (1, "loc_A68"),
        (2, "loc_A74"),
        (3, "loc_A80"),
        (4, "loc_A8C"),
        (5, "loc_A98"),
        (6, "loc_AA4"),
        (SWITCH_DEFAULT, "loc_AB0"),
    )


    label("loc_A5C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_ABC")

    label("loc_A68")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_ABC")

    label("loc_A74")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_ABC")

    label("loc_A80")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_ABC")

    label("loc_A8C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_ABC")

    label("loc_A98")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_ABC")

    label("loc_AA4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_ABC")

    label("loc_AB0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_ABC")

    label("loc_ABC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AD3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_ABC")

    label("loc_AD3")

    Return()

    # Function_0_A24 end

    def Function_1_AD4(): pass

    label("Function_1_AD4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B34")
    OP_95(0xFE, 2630, 0, -4370, 1000, 0x0)
    OP_95(0xFE, 240, 0, -7350, 1000, 0x0)
    OP_95(0xFE, 240, -750, -48720, 1000, 0x0)
    Sleep(500)
    SetChrPos(0xFE, 35280, 0, -4370, 45)
    Jump("Function_1_AD4")

    label("loc_B34")

    Return()

    # Function_1_AD4 end

    def Function_2_B35(): pass

    label("Function_2_B35")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B95")
    OP_95(0xFE, 240, 0, -7350, 2000, 0x0)
    OP_95(0xFE, 2630, 0, -4370, 2000, 0x0)
    OP_95(0xFE, 35280, 0, -4370, 2000, 0x0)
    Sleep(500)
    SetChrPos(0xFE, 240, -750, -48720, 0)
    Jump("Function_2_B35")

    label("loc_B95")

    Return()

    # Function_2_B35 end

    def Function_3_B96(): pass

    label("Function_3_B96")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D27")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C58")
    SetChrPos(0x0, 230, -750, -38720, 0)
    SetChrPos(0x1, 230, -750, -38720, 0)
    SetChrPos(0x2, 230, -750, -38720, 0)
    SetChrPos(0x3, 230, -750, -38720, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C2B")
    SetChrPos(0x4, 230, -750, -38720, 0)
    SetChrPos(0x5, 230, -750, -38720, 0)
    Jump("loc_C4A")

    label("loc_C2B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C4A")
    SetChrPos(0x4, 230, -750, -38720, 0)

    label("loc_C4A")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D27")

    label("loc_C58")

    SetChrPos(0x0, 24330, 0, -4050, 270)
    SetChrPos(0x1, 24330, 0, -4050, 270)
    SetChrPos(0x2, 24330, 0, -4050, 270)
    SetChrPos(0x3, 24330, 0, -4050, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CD1")
    SetChrPos(0x4, 24330, 0, -4050, 270)
    SetChrPos(0x5, 24330, 0, -4050, 270)
    Jump("loc_CF0")

    label("loc_CD1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CF0")
    SetChrPos(0x4, 24330, 0, -4050, 270)

    label("loc_CF0")

    OP_68(24330, 2000, -4050, 0)
    MoveCamera(45, 33, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19500, 0)
    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D27")

    OP_D2(0x7, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D44")
    OP_C9(0x0, 0x1000)

    label("loc_D44")

    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_D68")
    ClearChrFlags(0x10, 0x80)
    Jump("loc_EF7")

    label("loc_D68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_D80")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_EF7")

    label("loc_D80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_D93")
    ClearChrFlags(0xF, 0x80)
    Jump("loc_EF7")

    label("loc_D93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_DA1")
    Jump("loc_EF7")

    label("loc_DA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_DAF")
    Jump("loc_EF7")

    label("loc_DAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_DCC")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_EF7")

    label("loc_DCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_DDF")
    SetChrFlags(0x8, 0x10)
    Jump("loc_EF7")

    label("loc_DDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_E43")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xA, -7580, 0, -5670, 225)
    SetChrPos(0xB, -9090, 0, -5710, 135)
    SetChrPos(0xC, -8560, 0, -7100, 0)
    SetChrFlags(0xA, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E3E")
    SetChrFlags(0xC, 0x10)

    label("loc_E3E")

    Jump("loc_EF7")

    label("loc_E43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_E51")
    Jump("loc_EF7")

    label("loc_E51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_E5F")
    Jump("loc_EF7")

    label("loc_E5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_E84")
    SetChrPos(0x9, 13450, 0, -4760, 45)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_EF7")

    label("loc_E84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_EC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EBE")
    ClearChrFlags(0xE, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 7)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EBE")
    SetChrFlags(0xE, 0x80)

    label("loc_EBE")

    Jump("loc_EF7")

    label("loc_EC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_ED1")
    Jump("loc_EF7")

    label("loc_ED1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_EEE")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_EF7")

    label("loc_EEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_EF7")

    label("loc_EF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_F0B")
    ClearScenarioFlags(0x22, 0)
    Event(0, 20)
    Jump("loc_F65")

    label("loc_F0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_F1F")
    ClearScenarioFlags(0x22, 1)
    Event(0, 29)
    Jump("loc_F65")

    label("loc_F1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_F33")
    ClearScenarioFlags(0x22, 2)
    Event(0, 31)
    Jump("loc_F65")

    label("loc_F33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F65")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F65")
    SetMapFlags(0x10000000)
    Event(0, 24)

    label("loc_F65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F90")
    SetMapFlags(0x10000000)
    Event(1, 0)

    label("loc_F90")

    Return()

    # Function_3_B96 end

    def Function_4_F91(): pass

    label("Function_4_F91")

    ClearScenarioFlags(0x0, 7)
    SetScenarioFlags(0x1, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_104C")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x64, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Sound(128, 1, 100, 0)

    label("loc_104C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10EC")
    LoadEffect(0x9, "map/mpmoya.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0x78, 0x96, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xFF, 0xD, 0x64, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)

    label("loc_10EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_113F")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x20, 0x91, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)

    label("loc_113F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1157")
    ClearMapFlags(0x2000)
    Jump("loc_115E")

    label("loc_1157")

    SetMapFlags(0x2000)
    OP_E2(0x1)

    label("loc_115E")

    LoadEffect(0xF, "eff\\mgm03_02.eff")
    PlayEffect(0xF, 0x8, 0xFF, 0x0, -9970, -6500, -41930, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x14, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x17, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x18, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11ED")
    OP_65(0x0, 0x1)

    label("loc_11ED")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1206")
    OP_10(0x1, 0x0)
    OP_10(0xC, 0x1)
    Jump("loc_120C")

    label("loc_1206")

    OP_10(0x1, 0x1)
    OP_10(0xC, 0x0)

    label("loc_120C")

    ClearMapObjFlags(0x0, 0x10)
    ClearMapObjFlags(0x1, 0x10)
    ClearMapObjFlags(0x3, 0x10)
    ClearMapObjFlags(0x4, 0x10)
    ClearMapObjFlags(0x5, 0x10)
    ClearMapObjFlags(0x6, 0x10)
    ClearMapObjFlags(0xC, 0x10)
    OP_70(0x0, 0x0)
    OP_70(0x1, 0xA)
    OP_70(0x3, 0xA)
    OP_70(0x4, 0xA)
    OP_70(0x5, 0x0)
    OP_70(0x6, 0xA)
    OP_70(0xC, 0x1E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1267")
    ClearMapObjFlags(0x2, 0x10)
    Jump("loc_126B")

    label("loc_1267")

    OP_65(0x7, 0x1)

    label("loc_126B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1288")
    ClearMapObjFlags(0xB, 0x10)
    OP_70(0xB, 0x0)

    label("loc_1288")

    OP_65(0x6, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12A3")
    OP_66(0x6, 0x1)

    label("loc_12A3")

    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12E9")
    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_END)), "loc_12E9")
    OP_66(0x1, 0x1)
    ClearMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x12, 0x1000)
    SetMapObjFrame(0x12, "light", 0x0, 0x1)
    SetScenarioFlags(0x0, 7)

    label("loc_12E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12FB")
    OP_66(0x2, 0x1)

    label("loc_12FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1318")
    OP_70(0x5, 0x10)
    OP_65(0x3, 0x1)

    label("loc_1318")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    ModifyEventFlags(0, 3, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1360")
    ModifyEventFlags(1, 0, 0x80)
    Jump("loc_13A6")

    label("loc_1360")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1378")
    ModifyEventFlags(1, 1, 0x80)
    Jump("loc_13A6")

    label("loc_1378")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1390")
    ModifyEventFlags(1, 2, 0x80)
    Jump("loc_13A6")

    label("loc_1390")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 3)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13A6")
    ModifyEventFlags(1, 3, 0x80)

    label("loc_13A6")

    OP_52(0x18, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_155B")
    OP_70(0xF, 0x0)
    Jump("loc_155F")

    label("loc_155B")

    OP_70(0xF, 0x1E)

    label("loc_155F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_156B")
    ClearScenarioFlags(0x1, 0)

    label("loc_156B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_157C")
    ClearScenarioFlags(0x1, 0)

    label("loc_157C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_158D")
    ClearScenarioFlags(0x1, 0)

    label("loc_158D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_159E")
    ClearScenarioFlags(0x1, 0)

    label("loc_159E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15C5")
    ClearMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x12, 0x1000)
    SetMapObjFrame(0x12, "light", 0x0, 0x1)

    label("loc_15C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_15D3")
    Jump("loc_16DA")

    label("loc_15D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_15E7")
    SetMapObjFlags(0xE, 0x4)
    Jump("loc_16DA")

    label("loc_15E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_15F5")
    Jump("loc_16DA")

    label("loc_15F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1609")
    SetMapObjFlags(0xE, 0x4)
    Jump("loc_16DA")

    label("loc_1609")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1617")
    Jump("loc_16DA")

    label("loc_1617")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_162B")
    SetMapObjFlags(0xE, 0x4)
    Jump("loc_16DA")

    label("loc_162B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1653")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_164E")
    SetMapObjFlags(0xE, 0x4)

    label("loc_164E")

    Jump("loc_16DA")

    label("loc_1653")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1673")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_166E")
    SetMapObjFlags(0xE, 0x4)

    label("loc_166E")

    Jump("loc_16DA")

    label("loc_1673")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1687")
    SetMapObjFlags(0xE, 0x4)
    Jump("loc_16DA")

    label("loc_1687")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_169B")
    SetMapObjFlags(0xE, 0x4)
    Jump("loc_16DA")

    label("loc_169B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_16AF")
    SetMapObjFlags(0xE, 0x4)
    Jump("loc_16DA")

    label("loc_16AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_16C3")
    SetMapObjFlags(0xE, 0x4)
    Jump("loc_16DA")

    label("loc_16C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_16D1")
    Jump("loc_16DA")

    label("loc_16D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_16DA")

    label("loc_16DA")

    Return()

    # Function_4_F91 end

    def Function_5_16DB(): pass

    label("Function_5_16DB")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17D7")
    Sound(14, 0, 100, 0)
    OP_74(0xF, 0x1E)
    OP_71(0xF, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x5DE, 1)"), scpexpr(EXPR_END)), "loc_1760")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x5DE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EB, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_17D2")

    label("loc_1760")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x5DE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " is inside the chest.\x01",
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xF, 0x1E, 0x0, 0x0, 0x0)

    label("loc_17D2")

    Jump("loc_1821")

    label("loc_17D7")

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

    label("loc_1821")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_16DB end

    def Function_6_182D(): pass

    label("Function_6_182D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1A4A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_197A")

    ChrTalk(
        0xFE,
        (
            "There was a 3-man group of youngsters\x01",
            "known as the "High  Bloods" who lived\x01",
            "in that mansion, however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now that the barrier's gone,\x01",
            "they seem to have run off to\x01",
            "their hometown in the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So, what're they gonna do now? Unlike back then,\x01",
            "those kids don't seem to have a car anymore.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A45")

    label("loc_197A")


    ChrTalk(
        0xFE,
        (
            "Those youngsters who lived in that\x01",
            "mansion ran off to their home\x01",
            "in the Republic rather quickly...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So, what're they gonna do now? Unlike back then,\x01",
            "those kids don't seem to have a car anymore.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A45")

    Jump("loc_2728")

    label("loc_1A4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1A58")
    Jump("loc_2728")

    label("loc_1A58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1C96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BC4")

    ChrTalk(
        0xFE,
        (
            "When I listened to Mr. Dieter's speech,\x01",
            "I remembered the explosion accident\x01",
            "of a tour bus four or five years ago\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At the time, it was reported as an accident,\x01",
            "but if that was the result of the "secret feud"\x01",
            "of the Empire and the Republic...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm... It can be said that\x01",
            "there's a certain darkness\x01",
            "lying dormant in Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C91")

    label("loc_1BC4")


    ChrTalk(
        0xFE,
        (
            "In the explosion that happened four\x01",
            "or five years ago... Who was injured at\x01",
            "that time was surely a small girl...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm... It can be said that\x01",
            "there's a certain darkness\x01",
            "lying dormant in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C91")

    Jump("loc_2728")

    label("loc_1C96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1D4D")

    ChrTalk(
        0xFE,
        (
            "The raid incident during this\x01",
            "time was a terribly violent one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ever since then, my nights have been terrifying.\x01",
            "I've even been having trouble sleeping lately.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2728")

    label("loc_1D4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1DC6")

    ChrTalk(
        0xFE,
        (
            "At any rate, an occupation incident\x01",
            "isn't something quiet either...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Who the heck is behind that?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2728")

    label("loc_1DC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1DD4")
    Jump("loc_2728")

    label("loc_1DD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1E98")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E45")

    ChrTalk(
        0xFE,
        "..........ZZZ...\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "Huh.......\x01",
            "Did something happen?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    ClearChrFlags(0x8, 0x10)
    Jump("loc_1E93")

    label("loc_1E45")


    ChrTalk(
        0xFE,
        (
            "Oh... Looks like I\x01",
            "completely dozed off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...Has something happened?\x02",
    )

    CloseMessageWindow()

    label("loc_1E93")

    Jump("loc_2728")

    label("loc_1E98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1F19")

    ChrTalk(
        0xFE,
        (
            "*yaaawn".... \x01",
            "Either way, it's hard to sleep...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder if I'll be able to fall asleep at this rate....\x02",
    )

    CloseMessageWindow()
    Jump("loc_2728")

    label("loc_1F19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_20A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2009")

    ChrTalk(
        0xFE,
        (
            "The day of the local\x01",
            "referendum is drawing closer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For the sake of the future of the younger\x01",
            "generation, we can't tread forward lightly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I should carefully organize my\x01",
            "thoughts until the day comes.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_20A3")

    label("loc_2009")


    ChrTalk(
        0xFE,
        (
            "The independence has to be\x01",
            "seriously considered for the\x01",
            "sake of the future generations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I should gather my thoughts\x01",
            "carefully until voting day.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20A3")

    Jump("loc_2728")

    label("loc_20A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_21F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2183")

    ChrTalk(
        0xFE,
        (
            "Some time ago, an orbal \x01",
            "car went to the cathedral.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I remember correctly, that\x01",
            "looked like a private limousine\x01",
            "which is used for VIPs, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "No, that couldn't have been it.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_21F1")

    label("loc_2183")


    ChrTalk(
        0xFE,
        (
            "Some time ago, it seems\x01",
            "a limousine headed\x01",
            "towards the cathedral...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "No, that couldn't have been it.\x02",
    )

    CloseMessageWindow()

    label("loc_21F1")

    Jump("loc_2728")

    label("loc_21F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_2266")

    ChrTalk(
        0xFE,
        (
            "Ooh, it's become\x01",
            "considerably dark.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think it's about time for\x01",
            "me to set out for home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2728")

    label("loc_2266")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_241F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2392")

    ChrTalk(
        0xFE,
        (
            "Come to think of it, I haven't seen\x01",
            "the pizza delivery man lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I used to see him running around\x01",
            "the neighborhood all the time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F(Probably the guy Jona was asking for deliveries...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F(He's in the autonomous state \x01",
            "of Leman now, right?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_241A")

    label("loc_2392")


    ChrTalk(
        0xFE,
        (
            "Before, the pizza delivering\x01",
            "man came almost every\x01",
            "single day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ho ho, there was probably someone\x01",
            "who loved pizza quite a lot.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_241A")

    Jump("loc_2728")

    label("loc_241F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_25E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_254E")

    ChrTalk(
        0xFE,
        (
            "I offered a greeting to the young men\x01",
            "who recently started living at the\x01",
            "house there, but they shrugged me off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And to add to that, they laughed at me\x01",
            "and looked down on me as if I was a dog.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmhm... The family who\x01",
            "lived there last year\x01",
            "was much more friendly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_25E4")

    label("loc_254E")


    ChrTalk(
        0xFE,
        (
            "Listen here now, those young'uns\x01",
            "who moved in are the sons of some\x01",
            "big-shot company executives...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmmhmm... \x01",
            "Those young'uns are so cranky.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25E4")

    Jump("loc_2728")

    label("loc_25E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_25F7")
    Jump("loc_2728")

    label("loc_25F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2728")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2654")

    ChrTalk(
        0xFE,
        (
            "For pete's sake, those young'uns\x01",
            "again... So darn noisy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2728")

    label("loc_2654")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26C3")

    ChrTalk(
        0xFE,
        "Well, what nice weather we have today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Looks like I got a yawn\x01",
            "coming... *yaaaawn*\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2728")

    label("loc_26C3")


    ChrTalk(
        0xFE,
        "As I thought, this neighborhood is quiet as always.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "The sunshine feels just right today...\x02",
    )

    CloseMessageWindow()

    label("loc_2728")

    TalkEnd(0xFE)
    Return()

    # Function_6_182D end

    def Function_7_272C(): pass

    label("Function_7_272C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_28DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2839")

    ChrTalk(
        0xFE,
        "I heard President Dieter was arrested.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although I personally supported him...\x01",
            "His methods were heavy handed in many ways.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Really, when you commit a crime, there's\x01",
            "always the risk it comes back at you.\x01",
            "I must be careful too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_28D6")

    label("loc_2839")


    ChrTalk(
        0xFE,
        (
            "But even so, there's that\x01",
            "shining azure pale tree.\x01",
            "What could be its meaning?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now that the President's gone, is\x01",
            "there anyone left to deal with it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28D6")

    Jump("loc_39CE")

    label("loc_28DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_28E9")
    Jump("loc_39CE")

    label("loc_28E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2A68")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29D6")

    ChrTalk(
        0xFE,
        (
            ""Crossbell State independence"...\x01",
            "I'm still thinking over the matter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If it were to become real, it would be\x01",
            "a huge step forward for Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think I'll strongly believe\x01",
            "in President Dieter.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A63")

    label("loc_29D6")


    ChrTalk(
        0xFE,
        (
            "I think I'll strongly believe\x01",
            "in President Dieter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, it'll be a huge\x01",
            "step forward for Crossbell\x01",
            "if we become independent.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A63")

    Jump("loc_39CE")

    label("loc_2A68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2BE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B4B")

    ChrTalk(
        0xFE,
        (
            "Ilya collapsed and the\x01",
            "Arc-en-ciel is closed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Though reconstruction is proceeding\x01",
            "smoothly, the event echoes in the\x01",
            "hearts of us citizens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If there was even one\x01",
            "piece of good news...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2BDE")

    label("loc_2B4B")


    ChrTalk(
        0xFE,
        (
            "Though reconstruction is proceeding\x01",
            "smoothly, the event echoes in the\x01",
            "hearts of us citizens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If there was even one\x01",
            "piece of good news...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BDE")

    Jump("loc_39CE")

    label("loc_2BE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2DC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D08")

    ChrTalk(
        0xFE,
        (
            "It seems hostilities are occurring\x01",
            "between the CGF and that armed group\x01",
            "even now on Mainz Mountain Path.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Considering that the CGF couldn't settle \x01",
            "the conflict even after fighting all night long...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mmm. It seems certain they're\x01",
            "troublesome opponents.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2DC2")

    label("loc_2D08")


    ChrTalk(
        0xFE,
        (
            "The CGF are combat professionals.\x01",
            "Considering that they couldn't settle the\x01",
            "conflict even after fighting all night long...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mmm. It seems certain they're\x01",
            "troublesome opponents.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DC2")

    Jump("loc_39CE")

    label("loc_2DC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2DD5")
    Jump("loc_39CE")

    label("loc_2DD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2ECC")

    ChrTalk(
        0xFE,
        (
            "The Arc-en-ciel public performance... \x01",
            "According to rumor, they're trusting newcomer\x01",
            "Sully with all the additional scenes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if she'll be as popular as\x01",
            "Rixia Mao when she debuted. \x01",
            "Anyhow, I'm looking forward to it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39CE")

    label("loc_2ECC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2F78")

    ChrTalk(
        0xFE,
        (
            "There's two days left until the\x01",
            "Arc-en-ciel public performance...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Luckily, I was able to\x01",
            "reserve some A seat tickets,\x01",
            "so I'm looking forward to it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39CE")

    label("loc_2F78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3163")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30A8")

    ChrTalk(
        0xFE,
        (
            "To be independent as a state... It'll be rather\x01",
            "difficult to pull that off, if you ask me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's no way the Empire or Republic,\x01",
            "suzerain states, will recognize that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I understand what the mayor's\x01",
            "thinking, but... I can't help but\x01",
            "say it's a reckless proposal.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_315E")

    label("loc_30A8")


    ChrTalk(
        0xFE,
        (
            "There's no way the Empire\x01",
            "or Republic, suzerain states,\x01",
            "will approve of this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I understand what the mayor's\x01",
            "thinking, but... I can't help but\x01",
            "say it's a reckless proposal.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_315E")

    Jump("loc_39CE")

    label("loc_3163")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_330C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_325C")

    ChrTalk(
        0xFE,
        (
            "The company I work for\x01",
            "occupies one of the tenant\x01",
            "spaces in Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The managers plan to start it up\x01",
            "after the Trade Conference is over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the end, I can't\x01",
            "wait to see how much\x01",
            "successful it will be.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3307")

    label("loc_325C")


    ChrTalk(
        0xFE,
        (
            "The company I work for\x01",
            "occupies one of the tenant\x01",
            "spaces in Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't wait to see how much\x01",
            "successful will it be after the\x01",
            "Trade Conference is over.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3307")

    Jump("loc_39CE")

    label("loc_330C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_346C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33DD")

    ChrTalk(
        0xFE,
        (
            "I feel like I heard something\x01",
            "like a little girl's voice\x01",
            "coming from that mansion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, there should be no one \x01",
            "living in there, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hm, maybe I've just misheard.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3467")

    label("loc_33DD")


    ChrTalk(
        0xFE,
        (
            "By the way, was it about ten\x01",
            "years ago that it was said that\x01",
            "a ghost was appearing there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, it's a mere\x01",
            "nonsensical gossip.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3467")

    Jump("loc_39CE")

    label("loc_346C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_35ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3553")

    ChrTalk(
        0xFE,
        (
            "The veil over Orchis Tower\x01",
            "has finally been removed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, I can't believe\x01",
            "they'd go to such\x01",
            "lengths to show it off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mmm. I can't avoid looking forward \x01",
            "very much to its future development.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_35E8")

    label("loc_3553")


    ChrTalk(
        0xFE,
        (
            "Orchis Tower... I can't believe\x01",
            "it was that much of a building...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mmm. I can't avoid looking forward \x01",
            "very much to its future development.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35E8")

    Jump("loc_39CE")

    label("loc_35ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3786")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36ED")

    ChrTalk(
        0xFE,
        (
            "Come to think of it, Arc-en-ciel released\x01",
            "information on their next performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They said they were doing a renewal version\x01",
            "of "Golden Sun, Silver Moon", but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, perhaps I should hurry\x01",
            "and reserve my tickets.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3781")

    label("loc_36ED")


    ChrTalk(
        0xFE,
        (
            "In the end, I wonder how the\x01",
            ""Golden Sun, Silver Moon"\x01",
            "renewal version will turn out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, perhaps I should hurry\x01",
            "and reserve my tickets.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3781")

    Jump("loc_39CE")

    label("loc_3786")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3794")
    Jump("loc_39CE")

    label("loc_3794")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_39CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3842")

    ChrTalk(
        0xFE,
        (
            "Recently, I've been seeing a\x01",
            "recklessly driven orbal car.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Goodness... I wonder what the driver\x01",
            "plans to do if he causes an accident.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39CE")

    label("loc_3842")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3933")

    ChrTalk(
        0xFE,
        (
            "Yesterday, the new City Hall\x01",
            "building was finally completed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems that a lot of time has passed\x01",
            "since its construction started, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Dear me, I'm looking forward to the\x01",
            "unveiling ceremony at month end.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_39CE")

    label("loc_3933")


    ChrTalk(
        0xFE,
        (
            "As a businessman, I too have joined a\x01",
            "certain company in the new city hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Dear me, I'm looking forward to the\x01",
            "unveiling ceremony at month end.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39CE")

    TalkEnd(0xFE)
    Return()

    # Function_7_272C end

    def Function_8_39D2(): pass

    label("Function_8_39D2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AA5")
    OP_4B(0xFE, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Hehe. If you can handle an\x01",
            "orbal car this well, you've\x01",
            "truly made it your own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Reggie, you handle the\x01",
            "driving next time too, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Hehe, leave it to me.\x02",
    )

    CloseMessageWindow()
    OP_4C(0xFE, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x0, 2)
    Jump("loc_3AFA")

    label("loc_3AA5")


    ChrTalk(
        0xFE,
        (
            "Uh uh. If you can handle an\x01",
            "orbal car this well, you've\x01",
            "truly made it your own.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AFA")

    TalkEnd(0xFE)
    Return()

    # Function_8_39D2 end

    def Function_9_3AFE(): pass

    label("Function_9_3AFE")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Looking at Reggie like this, it's clear to\x01",
            "me that he's a skilled orbal car driver.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "His father's not an employee of Verne Corp.\x01",
            "orbal car development division for nothing.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_3AFE end

    def Function_10_3BBB(): pass

    label("Function_10_3BBB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CB0")
    OP_4B(0xFE, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Man, as expected,\x01",
            "flooring it on the\x01",
            "highway is the best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hehe. Unlike in the city, there aren't \x01",
            "unnecessary obstacles out there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Hu hu, I'm looking forward to next time, Reggie.\x02",
    )

    CloseMessageWindow()
    OP_4C(0xFE, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0xFE, 0x10)
    SetScenarioFlags(0x0, 4)
    Jump("loc_3D23")

    label("loc_3CB0")


    ChrTalk(
        0xFE,
        (
            "Man, as expected,\x01",
            "flooring it on the\x01",
            "highway is the best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll have to tune\x01",
            "it up to increase\x01",
            "the speed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D23")

    TalkEnd(0xFE)
    Return()

    # Function_10_3BBB end

    def Function_11_3D27(): pass

    label("Function_11_3D27")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3DB4")

    ChrTalk(
        0xFE,
        (
            "Ooh. I don't know if it's\x01",
            "because of the rain, but my\x01",
            "makeup looks terrible today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ah, I'm tired of fixing it...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E2A")

    label("loc_3DB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3E2A")

    ChrTalk(
        0xFE,
        (
            "Now then... I've got to\x01",
            "get to work today too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, but commuting on\x01",
            "rainy days is such a pain.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E2A")

    TalkEnd(0xFE)
    Return()

    # Function_11_3D27 end

    def Function_12_3E2E(): pass

    label("Function_12_3E2E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41D9")

    ChrTalk(
        0x101,
        (
            "#00005FHuh? Mr. Harold...?\x01",
            "Are you going\x01",
            "somewhere?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#03600FYes. I got invited to\x01",
            "Armorica Village awhile back.\x02\x03",
            "#03604FLawyer Ian recommends it too,\x01",
            "so I'll be staying there with\x01",
            "my family for awhile...\x02\x03",
            "#03608FI can't believe something this terrible would happen\x01",
            "in Crossbell on the morning of our departure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00103F...We're shaken too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FBut you got an invitation and\x01",
            "everything! Shouldn't you go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FThat's right... It seems like it's been\x01",
            "awhile since you had a vacation, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#03603FNo, that won't do... I'm planning\x01",
            "to return here after taking Sophia\x01",
            "and Colin to Armorica Village.\x02\x03",
            "#03600FIt seems people I'm indebted to are\x01",
            "in trouble. I can't abandon them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI see...\x02\x03",
            "#00001FTo be honest, it would be\x01",
            "strange if nothing happened.\x02\x03",
            "Be careful while you're\x01",
            "travelling on the highway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#03600FHa ha...thank you very much.\x01",
            "You be careful too, everyone.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x192, 0)
    Jump("loc_4382")

    label("loc_41D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42F6")

    ChrTalk(
        0xF,
        (
            "#03600FI'm planning to return here after taking \x01",
            "Sophia and Colin to Armorica Village.\x02\x03",
            "#03603FI'm sorry for Sophia and Colin who have\x01",
            "been looking forward to this, but... \x01",
            "It seems the situation is quite chaotic.\x02\x03",
            "#03600F...Please, everyone. Do be careful too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4382")

    label("loc_42F6")


    ChrTalk(
        0xF,
        (
            "#03603FI'm planning to return here after taking \x01",
            "Sophia and Colin to Armorica Village.\x02\x03",
            "#03600F...Please, everyone. Do be careful too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4382")

    TalkEnd(0xFE)
    Return()

    # Function_12_3E2E end

    def Function_13_4386(): pass

    label("Function_13_4386")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_444A")

    ChrTalk(
        0xFE,
        (
            "It's been awhile since we had\x01",
            "dinner as a family. We're\x01",
            "going shopping later, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You can't avoid seeing\x01",
            "that stupidly large tree. \x01",
            "I can't help but feel uneasy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_44F4")

    label("loc_444A")


    ChrTalk(
        0xFE,
        (
            "...Like grandma says, it's\x01",
            "in times like these that\x01",
            "you need presence of mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To hell that stupidly large tree!\x01",
            "If I whistle away I won't be scared, you know.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44F4")

    TalkEnd(0xFE)
    Return()

    # Function_13_4386 end

    def Function_14_44F8(): pass

    label("Function_14_44F8")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x101, -5490, -6000, -34180, 180)
    SetChrPos(0x102, -4510, -6000, -33860, 180)
    SetChrPos(0x104, -5450, -6000, -33100, 180)
    SetChrPos(0x109, -4650, -6000, -31730, 180)
    SetChrPos(0x105, -5460, -6000, -31370, 180)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu11500.itp")
    SetChrFlags(0xFE, 0x8000)
    SetChrFlags(0xFE, 0x40)
    EndChrThread(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x0)
    OP_68(-7650, -4000, -36130, 0)
    MoveCamera(56, 18, 0, 0)
    OP_6E(620, 0)
    SetCameraDistance(11500, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0xFE,
        (
            "#11504F#11PHmm, hmm, hmm...\x02\x03",
            "#11505FOh, I saw it! I guess it's\x01",
            "really true that there are\x01",
            "some different species lately.\x02\x03",
            "#11509FMan, I wish I had\x01",
            "brought my fishing rod.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#5PMr. Lechter... What're you\x01",
            "doing in a place like this?\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0xFE,
        (
            "Oh, looks like I've caught\x01",
            "my prey even without a rod.\x02\x03",
            "With my own two hands, I caught\x01",
            "five of them. Not a bad haul.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    ChrTalk(
        0x109,
        "#10105F#5PHuh...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#5PI think he's trying to\x01",
            "say he lured us here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#11509F#11PHa ha, that is what\x01",
            "I was trying to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5P(...We can't let him\x01",
            "have his way with us.)\x02\x03",
            "#00001F...Mr. Lechter, allow me\x01",
            "to change the subject.\x02\x03",
            "You're a member of the intelligence\x01",
            "division that let the "Red Constellation"\x01",
            "enter Crossbell. What're you doing here?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "#11509F#11PHa ha, you finally said it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#5PHu hu, well, straight talk\x01",
            "is the best way of dealing\x01",
            "with people like yourself.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 500)

    ChrTalk(
        0xFE,
        (
            "#11504F#12PHa ha, very well then.\x01",
            "I'll give you an answer.\x02\x03",
            "#11500FAs you can see,\x01",
            "I came here on break.\x02\x03",
            "#11506FAwesome as I am, guarding\x01",
            "that old man's tiring.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005F#5PO-Old man...? You mean \x01",
            "His Grace Chancellor Osborne?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#5PI was worried about him...\x01",
            "You really are one of the\x01",
            "Chancellor's aides, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#11502F#4PHehe, who knows. \x01",
            "I don't remember saying that\x01",
            "exaggerated thing even once.\x02\x03",
            "#11504FWell then. My break's almost up.\x01",
            "It's time I started getting\x01",
            "back to the old man.\x02\x03",
            "#11500FSee you guys.\x01",
            "Good luck with everything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105F#5PH-Huh...!?\x02",
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x2D, 0x1F4)

    def lambda_4CD1():

        label("loc_4CD1")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_4CD1")

    QueueWorkItem2(0x101, 2, lambda_4CD1)

    def lambda_4CE3():

        label("loc_4CE3")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_4CE3")

    QueueWorkItem2(0x102, 2, lambda_4CE3)

    def lambda_4CF5():

        label("loc_4CF5")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_4CF5")

    QueueWorkItem2(0x104, 2, lambda_4CF5)

    def lambda_4D07():

        label("loc_4D07")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_4D07")

    QueueWorkItem2(0x109, 2, lambda_4D07)

    def lambda_4D19():

        label("loc_4D19")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_4D19")

    QueueWorkItem2(0x105, 2, lambda_4D19)
    OP_68(-7430, -4000, -32960, 6000)
    OP_95(0xFE, -4000, -6000, -34790, 3000, 0x1)
    OP_95(0xFE, -4000, -4310, -16630, 3000, 0x0)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)

    ChrTalk(
        0x104,
        (
            "#00306F#5POh man, way to dodge\x01",
            "the question...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 0)), scpexpr(EXPR_END)), "loc_4DB3")
    Call(0, 15)

    label("loc_4DB3")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x0, -5490, -6000, -34180, 180)
    ClearChrFlags(0xFE, 0x8000)
    SetChrFlags(0xFE, 0x80)
    OP_CC(0x1, 0x0, 0x0)
    SetScenarioFlags(0x1C7, 3)
    OP_29(0xA3, 0x1, 0xA)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_14_44F8 end

    def Function_15_4DF8(): pass

    label("Function_15_4DF8")

    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_68(-8100, -4000, -35460, 2000)
    MoveCamera(56, 18, 0, 2000)
    OP_6E(620, 2000)
    SetCameraDistance(11500, 2000)
    Sleep(3000)
    OP_64(0xFFFF)

    ChrTalk(
        0x101,
        (
            "#00003F#6PMr. Lechter and Miss Kilika...\x02\x03",
            "Both the Imperial spy and the\x01",
            "Republican one came to the\x01",
            "city with similar timing.\x02\x03",
            "#00001F...What do you guys think?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4EE8():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4EE8)
    Sleep(50)

    def lambda_4EF8():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4EF8)
    Sleep(50)

    def lambda_4F08():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4F08)
    Sleep(50)

    def lambda_4F18():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4F18)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x109,
        "#10103F#6P...It's suspicious, somehow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#6PHu hu, if that's the case,\x01",
            "shall we follow them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#6PI think that would be difficult.\x02\x03",
            "#00103FI got the sense that both of\x01",
            "them knew we were coming...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PShall we report this to\x01",
            "Mr. Dudley and the others?\x02\x03",
            "#00000FThey might learn something if they\x01",
            "combine it with their other info.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105F#6PYeah... That sounds good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300F#6PAlright, it's decided then.\x01",
            "Let's head to police HQ.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0xA3, 0x1, 0xC)
    Return()

    # Function_15_4DF8 end

    def Function_16_5113(): pass

    label("Function_16_5113")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 6)), scpexpr(EXPR_END)), "loc_51A4")
    EventBegin(0x2)
    ClearMapFlags(0x20)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "This is the residence of Congressman Campbell of the\x01",
            "Republican Faction. We have no particular business here.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Jump("loc_56AE")

    label("loc_51A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55CC")
    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        "#00005FIf I'm remembering it right, this place is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FIt's the residence of Congressman\x01",
            "Campbell, who leads the Republican Faction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FI heard that congressmen\x01",
            "involved with that Cult\x01",
            "were overthrown...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FThat's true. In Congressman\x01",
            "Campbell's case, it seems no\x01",
            "such connection was confirmed.\x02\x03",
            "#00100FAlthough he seems to have a connection\x01",
            "with "Heiyue", at the present time, \x01",
            "that's not illegal...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHu hu. So what you're saying is, \x01",
            "it's certain he's a corrupt character.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_5538")

    ChrTalk(
        0x101,
        (
            "#00000FCome to think of it, you're\x01",
            "friends with Mr. Campbell's\x01",
            "daughter, aren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYou must be talking about Miss Karla. \x01",
            "Yes, we went to Sunday School together.\x02\x03",
            "#00104FTherefore, I'm relieved to\x01",
            "learn her father had no\x01",
            "connection with the Cult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108FThat's right...  I wouldn't\x01",
            "want to think about my friend's\x01",
            "father being that kind of person.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5538")


    ChrTalk(
        0x101,
        (
            "#00000FWell anyway... We don't have\x01",
            "any business here right now,\x01",
            "so let's hold off on visiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes, I agree.\x01",
            "Let's go.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12F, 6)
    TalkEnd(0xFF)
    Jump("loc_56AE")

    label("loc_55CC")

    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#00000FI think this is... The residence\x01",
            "of Congressman Campbell, \x01",
            "leader of the Republican Faction.\x02\x03",
            "We don't have any business here right now, \x01",
            "so let's hold off on visiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes, I agree.\x01",
            "Let's go.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12F, 6)
    TalkEnd(0xFF)

    label("loc_56AE")

    Return()

    # Function_16_5113 end

    def Function_17_56AF(): pass

    label("Function_17_56AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_56DD")
    Call(0, 39)
    Return()

    label("loc_56DD")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_17_56AF end

    def Function_18_570F(): pass

    label("Function_18_570F")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_18_570F end

    def Function_19_573F(): pass

    label("Function_19_573F")

    EventBegin(0x1)
    Sound(2094, 255, 100, 0)

    ChrTalk(
        0x101,
        "#0000FIt seems I can fish here.\x02",
    )

    CloseMessageWindow()
    OP_68(-10220, -4000, -43550, 1500)
    MoveCamera(45, 35, 0, 1500)
    OP_6E(600, 1500)
    SetCameraDistance(15500, 1500)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Fish?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Fish \x01",      # 0
            "Quit\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57FF")
    OP_E2(0x2)
    MiniGame(0x6, 0x2, 0xFFFFEAA2, 0xFFFFE890, 0xFFFF5DB2, 0x10E, 0xFFFFD90E, 0xFFFFE69C, 0xFFFF5C36)

    label("loc_57FF")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_19_573F end

    def Function_20_5804(): pass

    label("Function_20_5804")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x105, 0x8)
    LoadChrToIndex("apl/ch51107.itc", 0x1E)
    SoundLoad(468)
    SetChrChipByIndex(0x11, 0x1E)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 0, 0, -23000, 0)
    ClearChrFlags(0x12, 0x80)
    OP_78(0x10, 0x12)
    OP_49()
    SetChrPos(0x12, 25550, 0, -4600, 0)
    OP_D5(0x12, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x10, 0x1000)
    SetMapObjFrame(0x10, "light", 0x0, 0x1)
    OP_74(0x10, 0x1E)
    OP_71(0x10, 0x79, 0xB4, 0x1, 0x20)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_590F")
    SetChrFlags(0x9, 0x8000)
    EndChrThread(0x9, 0xFF)
    SetChrPos(0x9, -5000, 0, -5000, 180)

    def lambda_58FF():
        OP_9B(0x0, 0xFE, 0x0, 0x7530, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_58FF)

    label("loc_590F")

    FadeToBright(1000, 0)
    BeginChrThread(0x12, 3, 0, 21)
    BeginChrThread(0x11, 3, 0, 22)
    BeginChrThread(0x17, 1, 0, 23)
    OP_68(-650, 2600, -7350, 0)
    MoveCamera(57, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19150, 0)
    OP_68(-6650, 2600, -7350, 7500)
    OP_6F(0x79)
    OP_0D()
    StopSound(468, 1000, 100)
    Sleep(1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_24(0x1D4)
    SetScenarioFlags(0x22, 0)
    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_20_5804 end

    def Function_21_5990(): pass

    label("Function_21_5990")

    SetChrPos(0xFE, 25550, 0, -4600, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -6000, 0, -4600)
    OP_9F(0x1, -15000, 0, -3100)
    OP_9F(0x1, -16000, 0, 7900)
    OP_9F(0x2, 0xFE, 5500, 0x6)
    Return()

    # Function_21_5990 end

    def Function_22_59D9(): pass

    label("Function_22_59D9")

    Sleep(2000)
    OP_95(0xFE, 0, 0, -5600, 2000, 0x1)
    OP_95(0xFE, -14000, 0, -5600, 2000, 0x1)
    Return()

    # Function_22_59D9 end

    def Function_23_5A05(): pass

    label("Function_23_5A05")

    Sound(468, 2, 100, 0)
    Sound(458, 0, 100, 0)
    Sleep(4500)
    Sound(494, 0, 70, 0)
    Return()

    # Function_23_5A05 end

    def Function_24_5A1B(): pass

    label("Function_24_5A1B")

    EventBegin(0x0)
    SetChrFlags(0x9, 0x80)
    EndChrThread(0x9, 0x0)
    ClearChrFlags(0x13, 0x80)
    OP_78(0x12, 0x13)
    OP_49()
    SetChrPos(0x13, -15860, 300, 25000, 180)
    OP_D5(0x13, 0x0, 0x2BF20, 0x0, 0x0)
    ClearMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x12, 0x1000)
    SetMapObjFrame(0x12, "light", 0x0, 0x1)
    OP_74(0x12, 0x1E)
    OP_71(0x12, 0xB5, 0xF0, 0x1, 0x20)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5CC2")
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    OP_68(20100, 2200, -2560, 0)
    MoveCamera(54, 26, 0, 0)
    OP_6E(620, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, 19840, 0, -3660, 270)
    SetChrPos(0x102, 20660, 0, -4830, 270)
    SetChrPos(0x109, 21080, 0, -3150, 270)
    SetChrPos(0x105, 22020, 0, -4490, 270)

    def lambda_5B49():
        OP_97(0x101, 0xFFFFF830, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5B49)
    Sleep(50)

    def lambda_5B66():
        OP_97(0x102, 0xFFFFF830, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5B66)
    Sleep(50)

    def lambda_5B83():
        OP_97(0x109, 0xFFFFF830, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5B83)
    Sleep(50)

    def lambda_5BA0():
        OP_97(0x105, 0xFFFFF830, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5BA0)
    OP_68(20100, 500, -2560, 3000)
    FadeToBright(1000, 0)
    OP_6F(0x1)
    OP_0D()
    WaitChrThread(0x101, 1)
    Sound(488, 0, 70, 0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FThis sound is...?\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-14390, 500, 10820, 0)
    MoveCamera(70, 35, 0, 0)
    OP_6E(620, 0)
    SetCameraDistance(23150, 0)
    SetChrPos(0x101, 3840, 0, -2230, 180)
    SetChrPos(0x102, 4970, 0, -2230, 180)
    SetChrPos(0x109, 6070, 0, -2280, 180)
    SetChrPos(0x105, 7190, 0, -2280, 180)
    OP_0D()
    Jump("loc_5EA5")

    label("loc_5CC2")

    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    OP_68(1780, 500, -34350, 0)
    MoveCamera(54, 26, 0, 0)
    OP_6E(620, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, -320, 0, -33220, 0)
    SetChrPos(0x102, 890, 0, -33930, 0)
    SetChrPos(0x109, -170, 0, -34990, 0)
    SetChrPos(0x105, 1100, 0, -35480, 0)

    def lambda_5D75():
        OP_97(0x101, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5D75)
    Sleep(50)

    def lambda_5D92():
        OP_97(0x102, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5D92)
    Sleep(50)

    def lambda_5DAF():
        OP_97(0x109, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5DAF)
    Sleep(50)

    def lambda_5DCC():
        OP_97(0x105, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5DCC)
    OP_68(2420, 500, -31230, 3000)
    FadeToBright(1000, 0)
    OP_6F(0x1)
    OP_0D()
    WaitChrThread(0x101, 1)
    Sound(488, 0, 70, 0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FThis sound is...?\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-14390, 500, 10820, 0)
    MoveCamera(70, 35, 0, 0)
    OP_6E(620, 0)
    SetCameraDistance(23150, 0)
    OP_0D()

    label("loc_5EA5")

    OP_68(-13920, 500, -3320, 1000)
    MoveCamera(31, 31, 0, 1000)
    OP_6E(620, 1000)
    SetCameraDistance(20000, 1000)
    BeginChrThread(0x13, 1, 0, 25)
    BeginChrThread(0x17, 1, 0, 26)

    NpcTalk(
        0x12,
        "Youth's Voice",
        "#10AYahhhhooo!\x02",
    )

    CloseMessageWindow()
    OP_68(8360, 1450, -3280, 1500)
    MoveCamera(39, 29, 0, 1500)

    NpcTalk(
        0x12,
        "Youth's Voice",
        "#5AHa ha, this is the best!\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    def lambda_5F54():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5F54)
    Sleep(50)

    def lambda_5F64():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5F64)
    Sleep(50)

    def lambda_5F74():
        OP_93(0x109, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5F74)
    Sleep(50)

    def lambda_5F84():
        OP_93(0x105, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5F84)
    OP_6F(0x79)
    OP_0D()
    Sleep(1500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6026")
    Fade(500)
    OP_68(0, 1450, -27400, 0)
    MoveCamera(46, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, -830, 0, -26340, 0)
    SetChrPos(0x102, 780, 0, -26550, 0)
    SetChrPos(0x109, -420, 0, -27750, 0)
    SetChrPos(0x105, 1070, 0, -27950, 0)
    OP_0D()
    Jump("loc_6153")

    label("loc_6026")

    Fade(500)
    OP_68(5950, 1450, -3730, 0)
    MoveCamera(49, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, 3840, 0, -2230, 90)
    SetChrPos(0x102, 4970, 0, -2230, 90)
    SetChrPos(0x109, 6070, 0, -2280, 90)
    SetChrPos(0x105, 7190, 0, -2280, 90)
    OP_0D()

    def lambda_60A3():
        OP_95(0x102, 4970, 0, -5120, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_60A3)
    Sleep(100)

    def lambda_60C0():
        OP_95(0x101, 3840, 0, -3970, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_60C0)
    Sleep(100)

    def lambda_60DD():
        OP_95(0x109, 6070, 0, -3420, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_60DD)
    Sleep(100)

    def lambda_60FA():
        OP_95(0x105, 7190, 0, -4250, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_60FA)
    WaitChrThread(0x109, 1)

    def lambda_6118():
        OP_93(0x109, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6118)
    WaitChrThread(0x105, 1)

    def lambda_6129():
        OP_93(0x105, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6129)
    WaitChrThread(0x101, 1)

    def lambda_613A():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_613A)
    WaitChrThread(0x102, 1)

    def lambda_614B():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_614B)

    label("loc_6153")


    ChrTalk(
        0x101,
        (
            "#00005FW-What was that...?\x01",
            "That speed was\x01",
            "reckless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FA clear speeding violation...\x02\x03",
            "I feel bad for their car,\x01",
            "being driven like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FA recklessly driven orbal car... \x01",
            "Those have been sighted\x01",
            "more often in the city, lately.\x02\x03",
            "#00103FReckless driving causes problems\x01",
            "for a lot of different people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10305FHmm, I see.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(50)

    ChrTalk(
        0x105,
        (
            "#10300FSo, what does that have to do\x01",
            "with the Special Support Section?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_630A():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_630A)
    Sleep(50)

    def lambda_631A():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_631A)
    Sleep(50)

    def lambda_632A():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_632A)
    Sleep(50)

    ChrTalk(
        0x101,
        (
            "#00003FWe can't\x01",
            "overlook it,\x01",
            "of course.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63F4")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "◆Officer Kate at Waterfront Area? (Debug)\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Talked to Her]\x01",      # 0
            "[Didn't]\x01",             # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_63F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 4)), scpexpr(EXPR_END)), "loc_64D3")

    ChrTalk(
        0x101,
        (
            "#00004FIf I remember correctly,\x01",
            "senior Kate was patrolling\x01",
            "Entertainment District.\x02\x03",
            "#00000FI'll try contacting\x01",
            "her ENIGMA.\x02\x03",
            "The District Crime Prevention Section\x01",
            "is qualified to handle this type of case.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6598")

    label("loc_64D3")


    ChrTalk(
        0x101,
        (
            "#00003F...I'll try consulting\x01",
            "senior Kate of the District\x01",
            "Crime Prevention Section.\x02\x03",
            "#00000FShe might already have\x01",
            "a plan for dealing with\x01",
            "this sort of thing.\x02\x03",
            "I'll try contacting\x01",
            "her ENIGMA.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6598")

    OP_93(0x101, 0x10E, 0x1F4)
    Sleep(100)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x1)
    Sound(804, 0, 100, 0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    Sound(823, 0, 100, 0)
    Sleep(2700)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Kate's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──Yes, this is Officer Kate of the\x01",
            "District Crime Prevention Section.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00000FSenior Kate, thank you for your hard work.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Kate's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ah, Lloyd. Did you\x01",
            "need something?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00003FUmm, actually, there's something\x01",
            "I'd like to discuss with you...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd outlined the reckless\x01",
            "driving incident they just\x01",
            "saw for Officer Kate.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Kate's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ah, so you guys\x01",
            "saw it too.\x02\x03",
            "Well, since you're around... I'd\x01",
            "like your help with something.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005FHelp...?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Kate's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "If you have time,\x01",
            "can you come to\x01",
            "my location?\x02\x03",
            "I'm waiting by the\x01",
            "Entertainment District hotel.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00000FY-Yes.\x01",
            "Understood.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Kate's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Alright then. See you later.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(813, 0, 40, 0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(300)
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_93(0x101, 0x10E, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()
    Sleep(150)
    TurnDirection(0x101, 0x105, 500)
    Sleep(100)

    ChrTalk(
        0x102,
        "#00100F...What did Miss Kate say?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, it seems she wants\x01",
            "our help with something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FThe District Crime Prevention Section does?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309F"Stop the orbal car with brute force!"\x01",
            "...Maybe she'll say something like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FY-You know that's\x01",
            "too dangerous...\x02\x03",
            "#00000FAnyway, let's head for the\x01",
            "Entertainment District hotel.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x130, 5)
    SetMapObjFlags(0x12, 0x4)
    OP_CC(0x1, 0xFF, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 32280, 0, -4370, 270)
    BeginChrThread(0x9, 0, 0, 1)
    OP_69(0xFF, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B6D")
    SetChrPos(0x0, -320, 0, -25290, 0)
    Jump("loc_6B7E")

    label("loc_6B6D")

    SetChrPos(0x0, 3840, 0, -3970, 90)

    label("loc_6B7E")

    EventEnd(0x5)
    Return()

    # Function_24_5A1B end

    def Function_25_6B81(): pass

    label("Function_25_6B81")

    SetChrPos(0x13, -15860, 300, 20000, 180)
    OP_96(0xFE, 0xFFFFBD7A, 0x0, 0xFFFFF8B2, 0x4E20, 0x0)
    OP_9F(0x0, 0x13)
    OP_9F(0x1, -16800, 0, -2530)
    OP_9F(0x1, -14190, 0, -5130)
    OP_9F(0x1, -12700, 0, -5370)
    OP_9F(0x2, 0x13, 11000, 0x6)
    OP_96(0xFE, 0x767A, 0x0, 0xFFFFE85E, 0x4E20, 0x0)
    Return()

    # Function_25_6B81 end

    def Function_26_6BF2(): pass

    label("Function_26_6BF2")

    Sound(486, 0, 100, 0)
    Sleep(1000)
    Sound(487, 0, 100, 0)
    Sound(494, 0, 100, 0)
    Return()

    # Function_26_6BF2 end

    def Function_27_6C08(): pass

    label("Function_27_6C08")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CE6")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K◆ About the [Runaway Vehicle Crackdown], you... (Debug)\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[No change]\x01",         # 0
            "[Did it]\x01",            # 1
            "[Didn't do it]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CD2")
    OP_29(0x69, 0x4, 0x10)
    Jump("loc_6CE6")

    label("loc_6CD2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CE6")
    OP_29(0x69, 0x3, 0x10)

    label("loc_6CE6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6DCE")

    ChrTalk(
        0x101,
        (
            "#00005FThis is... It's the car\x01",
            "those juvenile delinquents\x01",
            "were driving yesterday, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FWhy is it in a place like this...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FI don't know, but... I'm getting\x01",
            "a bad feeling about this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6EEF")

    label("loc_6DCE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6E54")

    ChrTalk(
        0x101,
        "#00006FIt's the orbal car of those three, huh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHu hu. Honestly, \x01",
            "it's better than they deserve.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6EEF")

    label("loc_6E54")


    ChrTalk(
        0x101,
        (
            "#00005FThis is... What an\x01",
            "amazing orbal car.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHmmm, what an\x01",
            "affectatious design.\x02\x03",
            "#10304FHeh. It's funny\x01",
            "how poorly it\x01",
            "matches its owners.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6EEF")

    TalkEnd(0xFF)
    Return()

    # Function_27_6C08 end

    def Function_28_6EF3(): pass

    label("Function_28_6EF3")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-17170, -3900, -20000, 0)
    MoveCamera(358, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13200, 0)
    SetChrPos(0x101, -17570, -6000, -17670, 315)
    SetChrPos(0x102, -16410, -6000, -17600, 315)
    SetChrPos(0x109, -17240, -6000, -19410, 315)
    SetChrPos(0x105, -16090, -6000, -19200, 315)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#12P#00000FNear the MacDowell's residence...\x01",
            "So this must be the place.\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x1, 0x101, 0x0, 0x2EE, 0x3E8, 0x0)
    Sleep(500)
    Sound(808, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#12P#00000FExcuse us, is\x01",
            "anyone home?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        "#12P#00003FIt's no good, there's no response.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00105FIs it locked?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)

    ChrTalk(
        0x101,
        (
            "#5P#00001FOh, look, it's\x01",
            "open actually.\x02\x03",
            "#00003FAnd I hear some\x01",
            "voices inside...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10105FAre they so focused on their conversation\x01",
            "that they just didn't notice?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FAnyway, seeing as it's open, do you\x01",
            "think it's okay for us to enter?\x02\x03",
            "#10302FWe are official police\x01",
            "officers, after all.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#5P#00006FThat doesn't mean we can just\x01",
            "barge in wherever we please...\x02\x03",
            "#00000FBut, we really need some answers so I guess\x01",
            "we don't have much choice. Let's head\x01",
            "inside and make sure they know we're here.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopSound(128, 2000, 90)
    StopBGM(0xBB8)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x206), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("c0350", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_28_6EF3 end

    def Function_29_72CF(): pass

    label("Function_29_72CF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-17170, -3900, -20000, 0)
    MoveCamera(358, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13200, 0)
    SetChrPos(0x101, -17570, -6000, -17670, 135)
    SetChrPos(0x102, -16410, -6000, -17600, 225)
    SetChrPos(0x109, -17240, -6000, -19410, 0)
    SetChrPos(0x105, -16090, -6000, -19200, 315)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x105,
        (
            "#12P#10302FMan, they're a little too\x01",
            "into this aren't they.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00106FIt seems like they're\x01",
            "quintessential lazy sons.\x02\x03",
            "#00108FBut to think this\x01",
            "beautiful house fell into\x01",
            "the hands of those guys...\x02\x03",
            "#00103FMr. Bond must be\x01",
            "rather agitated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10101FBut, I don't see anything especially\x01",
            "illegal in their contract...\x02\x03",
            "#10106FAnd I don't recall any complaints from around here\x01",
            "either so there might not be anything we can do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00003FYeah...it seems that for now\x01",
            "we can only leave them alone.\x02\x03",
            "#00000F...Anyway, with this, our investigation\x01",
            "of Residential Street is complete.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x6A, 0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_76D1")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "◆Investigation Status? (Debug)\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[No Change]\x01",                          # 0
            "[Visited Bond's New Home]\x01",            # 1
            "[Investigations Remaining]\x01",           # 2
            "[All 6 Investigations Finished]\x01",      # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_76A2"),
        (1, "loc_76A7"),
        (2, "loc_76AF"),
        (3, "loc_76C0"),
        (SWITCH_DEFAULT, "loc_76D1"),
    )


    label("loc_76A2")

    Jump("loc_76D1")

    label("loc_76A7")

    ClearScenarioFlags(0x131, 7)
    Jump("loc_76D1")

    label("loc_76AF")

    SetScenarioFlags(0x131, 7)
    ClearScenarioFlags(0x132, 0)
    ClearScenarioFlags(0x132, 1)
    ClearScenarioFlags(0x132, 2)
    Jump("loc_76D1")

    label("loc_76C0")

    SetScenarioFlags(0x131, 7)
    SetScenarioFlags(0x132, 0)
    SetScenarioFlags(0x132, 1)
    SetScenarioFlags(0x132, 2)
    Jump("loc_76D1")

    label("loc_76D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_77BB")

    ChrTalk(
        0x102,
        (
            "#11P#00100FSay Lloyd, shall we pay\x01",
            "a visit to Mr. Bond?\x02\x03",
            "I'd like to hear his\x01",
            "side of the story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00003FYeah. I'm worried about him too.\x02\x03",
            "#00000FAll right, let's head to Mr. Bond's\x01",
            "new home on East Street.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7898")

    label("loc_77BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_781D")

    ChrTalk(
        0x101,
        (
            "#5P#00000FAlright, then let's continue\x01",
            "our investigation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7898")

    label("loc_781D")


    ChrTalk(
        0x101,
        (
            "#5P#00000FAlright, we've finished our investigation.\x02\x03",
            "Let's head back to City Meeting Hall\x01",
            "and make our report.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x6A, 0x1, 0x6)

    label("loc_7898")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_65(0x2, 0x1)
    SetMapObjFlags(0xB, 0x10)
    SetScenarioFlags(0x131, 6)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -17150, -6000, -18250, 180)
    EventEnd(0x5)
    Return()

    # Function_29_72CF end

    def Function_30_78C8(): pass

    label("Function_30_78C8")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    AddParty(0xA2, 0xFF, 0xFF)
    SetChrPos(0x1A3, -1920, 0, -11670, 225)
    LoadChrToIndex("chr/ch03401.itc", 0x1E)
    OP_68(-9190, -2230, -25380, 0)
    MoveCamera(44, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(8210, 0)
    SetChrPos(0x101, -6050, -5680, -19360, 180)
    SetChrPos(0x102, -4650, -5660, -19680, 180)
    SetChrPos(0x109, -5250, -4960, -18250, 180)
    SetChrPos(0x105, -3850, -4930, -18360, 180)
    SetChrPos(0x104, -6850, -4980, -17900, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    def lambda_7995():
        OP_95(0xFE, -6050, -6000, -22480, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7995)
    Sleep(50)

    def lambda_79B2():
        OP_95(0xFE, -4650, -6000, -22780, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_79B2)
    Sleep(50)

    def lambda_79CF():
        OP_95(0xFE, -5250, -6000, -21350, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_79CF)
    Sleep(50)

    def lambda_79EC():
        OP_95(0xFE, -3850, -6000, -21480, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_79EC)
    Sleep(50)

    def lambda_7A09():
        OP_95(0xFE, -6850, -6000, -21200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7A09)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x1A3,
        "#04602FOh, there you are!\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_7AD3():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7AD3)
    Sleep(50)

    def lambda_7AE3():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7AE3)
    Sleep(50)

    def lambda_7AF3():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7AF3)
    Sleep(50)

    def lambda_7B03():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7B03)
    Sleep(50)

    def lambda_7B13():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7B13)
    Sleep(1000)
    Fade(500)
    OP_68(-4050, 1670, -12540, 0)
    MoveCamera(42, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14080, 0)
    OP_0D()

    def lambda_7B57():

        label("loc_7B57")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_7B57")

    QueueWorkItem2(0x101, 1, lambda_7B57)

    def lambda_7B69():

        label("loc_7B69")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_7B69")

    QueueWorkItem2(0x104, 1, lambda_7B69)

    def lambda_7B7B():

        label("loc_7B7B")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_7B7B")

    QueueWorkItem2(0x102, 1, lambda_7B7B)

    def lambda_7B8D():

        label("loc_7B8D")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_7B8D")

    QueueWorkItem2(0x109, 1, lambda_7B8D)

    def lambda_7B9F():

        label("loc_7B9F")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_7B9F")

    QueueWorkItem2(0x105, 1, lambda_7B9F)
    OP_95(0x1A3, -1410, 0, -6320, 5000, 0x0)
    OP_95(0x1A3, -5270, 0, -6140, 5000, 0x0)
    OP_68(-9190, -2230, -25380, 3000)
    MoveCamera(44, 23, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(8210, 3000)
    OP_95(0x1A3, -5230, -5630, -19270, 4000, 0x0)
    OP_93(0x1A3, 0xE1, 0x1F4)
    WaitChrThread(0x1A3, 1)
    OP_6F(0x79)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)

    ChrTalk(
        0x1A3,
        (
            "#5P#04600FYou guys were really slow, \x01",
            "so I started looking for her myself.\x02\x03",
            "#04609FAnd? Which house is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FWell, this one. But...\x02\x03",
            "#00006F...Wait, we didn't approve of\x01",
            "having you along.\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x1A3, 0x109, 0x3E8, 0x7D0, 0x0)
    Sleep(300)

    ChrTalk(
        0x1A3,
        (
            "#04600FHey miss. Dog person or\x01",
            "cat person. Which is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10105FM-Me?\x02\x03",
            "#10104FUmm... If I had to say,\x01",
            "then cat person, I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#04609FAhaha, same\x01",
            "as me!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#6P#00303F(...Just give up. It doesn't\x01",
            "matter what we say.)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        "#12P#00006F(*sigh*... Looks like it.)\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)
    SetScenarioFlags(0x155, 2)
    OP_C9(0x0, 0x1000)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -5940, -6000, -22110, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_30_78C8 end

    def Function_31_7E83(): pass

    label("Function_31_7E83")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-17690, -3510, -20970, 0)
    MoveCamera(7, 32, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12430, 0)
    SetChrPos(0x101, -19120, -5610, -16030, 135)
    SetChrPos(0x102, -19120, -5610, -16030, 135)
    SetChrPos(0x109, -19120, -5610, -16030, 135)
    SetChrPos(0x105, -19120, -5610, -16030, 135)
    SetChrPos(0x104, -19120, -5610, -16030, 135)
    SetChrPos(0x1A3, -19120, -5610, -16030, 135)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1A3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0xB, 0x10)
    OP_71(0xB, 0x0, 0x10, 0x0, 0x0)
    OP_79(0xB)
    Sleep(500)
    OP_68(-16690, -3510, -20970, 3000)
    BeginChrThread(0x1A3, 3, 0, 37)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 34)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 36)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 35)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 33)
    Sleep(700)
    BeginChrThread(0x101, 3, 0, 32)
    OP_6F(0x1)
    Sleep(1000)
    Sound(104, 0, 100, 0)
    OP_71(0xB, 0x10, 0x0, 0x0, 0x0)
    OP_79(0xB)
    SetMapObjFlags(0xB, 0x10)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x1A3,
        "#12P#04609FAlright, let's go!\x02",
    )

    CloseMessageWindow()
    OP_95(0x1A3, -11560, -6000, -23410, 2000, 0x0)

    ChrTalk(
        0x101,
        "#00006FHow do I put it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FYeah... She's\x01",
            "quite strong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FWith her slender arms, \x01",
            "she lifted two adult men...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHu hu. She's not a girl from the\x01",
            "strongest jaeger corps for nothing.\x02\x03",
            "#10302FThat thirst for blood before also\x01",
            "reminded me of you, Randy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00303F...Don't lump me in with her.\x02",
    )

    CloseMessageWindow()
    OP_68(-14290, -3510, -23940, 3000)
    OP_6F(0x1)
    OP_93(0x1A3, 0x13B, 0x1F4)
    OP_63(0x1A3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_9C(0x1A3, 0x0, 0x0, 0x0, 0x190, 0xBB8)
    OP_9C(0x1A3, 0x0, 0x0, 0x0, 0x190, 0xBB8)
    Sleep(300)

    ChrTalk(
        0x1A3,
        (
            "#12P#04606FHey, what're you misters doing?\x02\x03",
            "#04602FWe're not gonna find\x01",
            "her if we don't hurry!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FRight... We're coming.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(1, 2, 0x80)
    SetScenarioFlags(0x155, 3)
    OP_29(0x74, 0x1, 0x4)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -12100, -6000, -22550, 135)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_31_7E83 end

    def Function_32_82A7(): pass

    label("Function_32_82A7")


    def lambda_82AC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_82AC)

    def lambda_82BD():
        OP_95(0xFE, -18140, -5600, -17170, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_82BD)
    WaitChrThread(0x101, 1)
    OP_95(0x101, -17710, -6000, -18270, 2000, 0x0)
    OP_93(0x101, 0x87, 0x1F4)
    Return()

    # Function_32_82A7 end

    def Function_33_82F2(): pass

    label("Function_33_82F2")


    def lambda_82F7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_82F7)

    def lambda_8308():
        OP_95(0xFE, -18140, -5600, -17170, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8308)
    WaitChrThread(0x102, 1)
    OP_95(0x102, -16500, -6000, -17480, 2000, 0x0)
    OP_93(0x102, 0x87, 0x1F4)
    Return()

    # Function_33_82F2 end

    def Function_34_833D(): pass

    label("Function_34_833D")


    def lambda_8342():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8342)

    def lambda_8353():
        OP_95(0xFE, -17390, -6000, -17900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8353)
    WaitChrThread(0x104, 1)
    OP_95(0x104, -15930, -6000, -19920, 2000, 0x0)
    OP_93(0x104, 0x87, 0x1F4)
    Return()

    # Function_34_833D end

    def Function_35_8388(): pass

    label("Function_35_8388")


    def lambda_838D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_838D)

    def lambda_839E():
        OP_95(0xFE, -17390, -6000, -17900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_839E)
    WaitChrThread(0x109, 1)
    OP_95(0x109, -16510, -6000, -18800, 2000, 0x0)
    OP_93(0x109, 0x87, 0x1F4)
    Return()

    # Function_35_8388 end

    def Function_36_83D3(): pass

    label("Function_36_83D3")


    def lambda_83D8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_83D8)

    def lambda_83E9():
        OP_95(0xFE, -17390, -6000, -17900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_83E9)
    WaitChrThread(0x105, 1)
    OP_95(0x105, -15400, -6000, -18710, 2000, 0x0)
    OP_93(0x105, 0x87, 0x1F4)
    Return()

    # Function_36_83D3 end

    def Function_37_841E(): pass

    label("Function_37_841E")


    def lambda_8423():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A3, 2, lambda_8423)

    def lambda_8434():
        OP_95(0xFE, -14830, -6000, -20120, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_8434)
    WaitChrThread(0x1A3, 1)
    OP_93(0x1A3, 0x13B, 0x1F4)
    Return()

    # Function_37_841E end

    def Function_38_8455(): pass

    label("Function_38_8455")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch39000.itc", 0x1E)
    LoadChrToIndex("chr/ch03401.itc", 0x1F)
    SetChrChipByIndex(0x16, 0x1E)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 17810, 0, -4050, 90)
    OP_68(-4400, 2000, -6530, 0)
    MoveCamera(37, 29, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14500, 0)
    SetChrPos(0x101, -3430, 0, -5280, 90)
    SetChrPos(0x102, -3980, 0, -6980, 90)
    SetChrPos(0x104, -5330, 0, -4480, 90)
    SetChrPos(0x109, -5080, 0, -6480, 90)
    SetChrPos(0x105, -5830, 0, -5780, 90)
    SetChrPos(0x1A3, -3880, 0, -3980, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x9, 0x80)
    EndChrThread(0x9, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x1A3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(16720, 2000, -5140, 6000)
    MoveCamera(45, 33, 0, 6000)
    OP_6E(600, 6000)
    SetCameraDistance(14880, 6000)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(-4400, 2000, -6530, 0)
    MoveCamera(37, 29, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14500, 0)
    OP_0D()

    ChrTalk(
        0x102,
        "#6P#00105FHey Lloyd, that's...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, it must be Mary.\x01",
            "#6PWe finally found her.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(16720, 2000, -5140, 0)
    MoveCamera(45, 33, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12580, 0)
    SetChrPos(0x1A3, 7810, 0, -2750, 90)
    SetChrPos(0x101, 8310, 0, -4050, 90)
    SetChrPos(0x102, 7610, 0, -5350, 90)
    SetChrPos(0x104, 6110, 0, -2950, 90)
    SetChrPos(0x109, 5910, 0, -5250, 90)
    SetChrPos(0x105, 5310, 0, -4250, 90)
    OP_0D()
    OP_63(0x16, 0x0, 1200, 0x28, 0x2B, 0x64, 0x0)
    OP_93(0x16, 0x0, 0x1F4)
    Sleep(400)
    OP_93(0x16, 0xB4, 0x1F4)
    Sleep(200)
    OP_93(0x16, 0x5A, 0x1F4)
    OP_64(0x16)
    Sleep(1000)
    OP_95(0x16, 31570, 0, -4230, 4000, 0x0)
    SetCameraDistance(14500, 3000)
    SetChrFlags(0x16, 0x80)
    SetChrChipByIndex(0x1A3, 0x1F)
    SetChrSubChip(0x1A3, 0x0)
    SetChrFlags(0x1A3, 0x1000)

    def lambda_878A():
        OP_95(0xFE, 19310, 0, -4050, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_878A)
    Sleep(50)

    def lambda_87A7():
        OP_95(0xFE, 18810, 0, -2750, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_87A7)
    Sleep(50)

    def lambda_87C4():
        OP_95(0xFE, 18610, 0, -5350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_87C4)
    Sleep(50)

    def lambda_87E1():
        OP_95(0xFE, 17110, 0, -2950, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_87E1)
    Sleep(50)

    def lambda_87FE():
        OP_95(0xFE, 16910, 0, -5250, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_87FE)
    Sleep(50)

    def lambda_881B():
        OP_95(0xFE, 16309, 0, -4250, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_881B)
    WaitChrThread(0x1A3, 1)
    SetChrChipByIndex(0x1A3, 0xFF)
    SetChrSubChip(0x1A3, 0x0)
    WaitChrThread(0x105, 1)
    OP_6F(0x10)

    ChrTalk(
        0x104,
        "#6P#00306FAaand there she goes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        "#5P#04602FAll we gotta do now is catch her.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYeah, let's hurry!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ModifyEventFlags(0, 2, 0x80)
    SetScenarioFlags(0x155, 4)
    OP_29(0x74, 0x1, 0x5)
    OP_D7(0x1E)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 32280, 0, -4370, 270)
    BeginChrThread(0x9, 0, 0, 1)
    ModifyEventFlags(1, 3, 0x80)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 17810, 0, -4050, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_38_8455 end

    def Function_39_891A(): pass

    label("Function_39_891A")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(16970, 2000, -2590, 0)
    MoveCamera(35, 22, 0, 0)
    OP_6E(620, 0)
    SetCameraDistance(17050, 0)
    SetChrPos(0x101, 16600, 0, -3190, 0)
    SetChrPos(0x103, 16400, 0, -4390, 0)
    SetChrPos(0x104, 17590, 0, -5410, 0)
    SetChrPos(0x102, 18770, 0, -3140, 0)
    SetChrPos(0x109, 18940, 0, -4580, 0)
    SetChrPos(0x105, 17570, 0, -3990, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0x9, 0x80)
    EndChrThread(0x9, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00005FUhmm...\x01",
            "There's no mistake.\x01",
            "This is the address.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00103FYes, it seems that way, but...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)

    ChrTalk(
        0x104,
        (
            "#00303F...I don't sense\x01",
            "anyone's presence.\x02\x03",
            "#00301FIs there some\x01",
            "kind of mistake?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FDid the sender write\x01",
            "the wrong address\x01",
            "or something...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FBut this receipt... \x01",
            "The destination address is written,\x01",
            "but the addressee's name isn't.\x02\x03",
            "#00003FRegardless, we'll never know\x01",
            "whose it is if we don't ask.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x103)
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00005F...Huh, what's wrong, Tio?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205FOh, nothing...\x02",
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x105,
        "#10305FHuh, could it be...\x02",
    )

    CloseMessageWindow()

    def lambda_8CAB():
        OP_95(0xFE, 17650, 0, -1500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8CAB)
    Sleep(300)

    def lambda_8CC8():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8CC8)
    Sleep(100)

    def lambda_8CD8():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8CD8)
    OP_0D()
    WaitChrThread(0x105, 1)
    Sleep(700)
    ClearMapObjFlags(0x5, 0x10)
    OP_70(0x5, 0x0)
    OP_71(0x5, 0x0, 0xA, 0x0, 0x0)
    Sound(114, 0, 100, 0)
    OP_79(0x5)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FIt's open...!?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)

    ChrTalk(
        0x105,
        (
            "#10304FIt was ajar, so I\x01",
            "had a feeling...\x02\x03",
            "#10300FWell, let's ask the resident\x01",
            "if this is their package.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FR-Right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F(............?)\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 32280, 0, -4370, 270)
    BeginChrThread(0x9, 0, 0, 1)
    OP_65(0x3, 0x1)
    SetScenarioFlags(0x176, 1)
    OP_29(0x85, 0x1, 0x4)
    SetChrPos(0x0, 17650, 0, -2000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_39_891A end

    def Function_40_8EAD(): pass

    label("Function_40_8EAD")

    EventBegin(0x1)

    ChrTalk(
        0x1A3,
        (
            "#04605FAww... Why are we going back? \x01",
            "Isn't our target right in front of us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, let's go there now.\x02\x03",
            "#00006F(...It's like Randy said. No matter\x01",
            "what you say to her, it's pointless.)\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -5250, -1550, -11110, 180)
    EventEnd(0x4)
    Return()

    # Function_40_8EAD end

    def Function_41_8F8D(): pass

    label("Function_41_8F8D")

    EventBegin(0x1)

    ChrTalk(
        0x1A3,
        (
            "#04600FHey, what're you doing? \x01",
            "Hurry up and chase after Mary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, let's hurry to Entertainment District.\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, 6340, 0, -5780, 90)
    EventEnd(0x4)
    Return()

    # Function_41_8F8D end

    def Function_42_9020(): pass

    label("Function_42_9020")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_42_9020 end

    SaveToFile()

Try(main)
