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

    Sepith("Sepith_8D30", 8,   8,   8,   8,   11,  11,  11)

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
        "BattleInfo_8C4", 0x0000, 93, 6, 60, 4, 1, 25, 0, "bc0300", "Sepith_8D30", 60, 30, 10, 0,
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
        "Function_6_182C",         # 06, 6
        "Function_7_2667",         # 07, 7
        "Function_8_3846",         # 08, 8
        "Function_9_3971",         # 09, 9
        "Function_10_3A2B",        # 0A, 10
        "Function_11_3B75",        # 0B, 11
        "Function_12_3C75",        # 0C, 12
        "Function_13_4184",        # 0D, 13
        "Function_14_42EC",        # 0E, 14
        "Function_15_4BB4",        # 0F, 15
        "Function_16_4EB8",        # 10, 16
        "Function_17_5441",        # 11, 17
        "Function_18_54A1",        # 12, 18
        "Function_19_54D1",        # 13, 19
        "Function_20_5598",        # 14, 20
        "Function_21_5724",        # 15, 21
        "Function_22_576D",        # 16, 22
        "Function_23_5799",        # 17, 23
        "Function_24_57AF",        # 18, 24
        "Function_25_68AE",        # 19, 25
        "Function_26_691F",        # 1A, 26
        "Function_27_6935",        # 1B, 27
        "Function_28_6C20",        # 1C, 28
        "Function_29_6FCB",        # 1D, 29
        "Function_30_75A3",        # 1E, 30
        "Function_31_7B4E",        # 1F, 31
        "Function_32_7F71",        # 20, 32
        "Function_33_7FBC",        # 21, 33
        "Function_34_8007",        # 22, 34
        "Function_35_8052",        # 23, 35
        "Function_36_809D",        # 24, 36
        "Function_37_80E8",        # 25, 37
        "Function_38_811F",        # 26, 38
        "Function_39_85E4",        # 27, 39
        "Function_40_8B52",        # 28, 40
        "Function_41_8C35",        # 29, 41
        "Function_42_8CD6",        # 2A, 42
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
            "Since you have too many,\x01",
            "you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xF, 0x1E, 0x0, 0x0, 0x0)

    label("loc_17D2")

    Jump("loc_1820")

    label("loc_17D7")

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

    label("loc_1820")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_16DB end

    def Function_6_182C(): pass

    label("Function_6_182C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1A4A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1979")

    ChrTalk(
        0xFE,
        (
            "There was a group of three youngsters\x01",
            "known as the Highbloods who lived in\x01",
            "that Mansion, don'tcha know?\x02",
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
            "So, what're they gonna do now?\x01",
            "Unlike back then, those kids\x01",
            "don't seem to have a car anymore.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A45")

    label("loc_1979")


    ChrTalk(
        0xFE,
        (
            "Those young'uns who lived in that\x01",
            "residence ran off to their home\x01",
            "in the Republic rather quickly...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So, what're they gonna do now?\x01",
            "Unlike back then, those kids\x01",
            "don't seem to have a car anymore.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A45")

    Jump("loc_2663")

    label("loc_1A4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1A58")
    Jump("loc_2663")

    label("loc_1A58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1C86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BB9")

    ChrTalk(
        0xFE,
        (
            "When I listened to Dieter's speech,\x01",
            "I remembered the tour bus explosion\x01",
            "accident four or five years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At the time, it was reported as an accident,\x01",
            "but if that was the result of the "fighting"\x01",
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
    Jump("loc_1C81")

    label("loc_1BB9")


    ChrTalk(
        0xFE,
        (
            "In the explosion that happened four\x01",
            "or five years ago... The victim at\x01",
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

    label("loc_1C81")

    Jump("loc_2663")

    label("loc_1C86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1D28")

    ChrTalk(
        0xFE,
        (
            "The attack the other day\x01",
            "was terribly violent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ever since, my nights have been\x01",
            "terrifying. I've even been\x01",
            "having trouble sleeping lately.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2663")

    label("loc_1D28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1D87")

    ChrTalk(
        0xFE,
        (
            "Anyhow, an occupation\x01",
            "isn't quiet either...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Who the heck is behind\x01",
            "it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2663")

    label("loc_1D87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1D95")
    Jump("loc_2663")

    label("loc_1D95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1E4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E0B")

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
            "Hah....... Huh? Did\x01",
            "something happen?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    ClearChrFlags(0x8, 0x10)
    Jump("loc_1E49")

    label("loc_1E0B")


    ChrTalk(
        0xFE,
        (
            "Oh... Looks like I dozed\x01",
            "off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        ".... What's going on?\x02",
    )

    CloseMessageWindow()

    label("loc_1E49")

    Jump("loc_2663")

    label("loc_1E4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1EC9")

    ChrTalk(
        0xFE,
        (
            "Siiighh.... Either way,\x01",
            "it's hard to sleep...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if I'll be able\x01",
            "to fall asleep as it\x01",
            "is....\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2663")

    label("loc_1EC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2052")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FB3")

    ChrTalk(
        0xFE,
        (
            "The day of the\x01",
            "referendum is drawing\x01",
            "closer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For the sake of the future of\x01",
            "the younger generation, we\x01",
            "can't tread forward lightly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I should carefully\x01",
            "organize my thoughts\x01",
            "until the day comes.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_204D")

    label("loc_1FB3")


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
            "I should gather my\x01",
            "thoughts carefully until\x01",
            "voting day.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_204D")

    Jump("loc_2663")

    label("loc_2052")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2163")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20FB")

    ChrTalk(
        0xFE,
        (
            "Some time ago, an orbal\x01",
            "car went to the\x01",
            "cathedral.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It looked like a\x01",
            "limousine used for\x01",
            "VIPs...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, that couldn't have\x01",
            "been it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_215E")

    label("loc_20FB")


    ChrTalk(
        0xFE,
        (
            "Some time ago, a\x01",
            "limousine headed towards\x01",
            "the cathedral.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, that couldn't have\x01",
            "been it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_215E")

    Jump("loc_2663")

    label("loc_2163")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_21C6")

    ChrTalk(
        0xFE,
        (
            "Ooh, it's gotten rather\x01",
            "dark.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think it's about time\x01",
            "for me to head home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2663")

    label("loc_21C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2361")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22DC")

    ChrTalk(
        0xFE,
        (
            "Come to think of it, I\x01",
            "haven't seen the pizza\x01",
            "delivery guy lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I used to see him running\x01",
            "around the neighborhood\x01",
            "all the time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(Jona's keeping him busy\x01",
            "probably...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F(He's in Lｳman State\x01",
            "right now, if I recall.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_235C")

    label("loc_22DC")


    ChrTalk(
        0xFE,
        (
            "Back in my day, the\x01",
            "pizza guy came almost\x01",
            "every single day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hoho, you could even say\x01",
            "we lived in a paradise\x01",
            "of pizza.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_235C")

    Jump("loc_2663")

    label("loc_2361")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_252D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2499")

    ChrTalk(
        0xFE,
        (
            "I offered a greeting to the youngsters\x01",
            "who recently started living at the\x01",
            "house there, but they shrugged me off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And to make matters worse,\x01",
            "they laughed at me and looked\x01",
            "down on me as if I was a dog.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmhm... The family that\x01",
            "lived there last year\x01",
            "was much more friendly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2528")

    label("loc_2499")


    ChrTalk(
        0xFE,
        (
            "Listen here now, those youngsters\x01",
            "who moved in are the sons of some\x01",
            "big-shot company executives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmmhmm... Those kids are\x01",
            "so cranky.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2528")

    Jump("loc_2663")

    label("loc_252D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_253B")
    Jump("loc_2663")

    label("loc_253B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2663")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2598")

    ChrTalk(
        0xFE,
        (
            "For pete's sake, those\x01",
            "young'uns again... So\x01",
            "darn noisy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2663")

    label("loc_2598")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25FE")

    ChrTalk(
        0xFE,
        (
            "Ah, what nice weather we\x01",
            "have today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I feel a yawn coming\x01",
            "on... *yaaaawn*\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2663")

    label("loc_25FE")


    ChrTalk(
        0xFE,
        (
            "As I thought, this\x01",
            "neighborhood is quiet as\x01",
            "always.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The sunshine feels just\x01",
            "right today...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2663")

    TalkEnd(0xFE)
    Return()

    # Function_6_182C end

    def Function_7_2667(): pass

    label("Function_7_2667")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_27FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_275A")

    ChrTalk(
        0xFE,
        (
            "I heard President Dieter\x01",
            "was arrested.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although I personally supported\x01",
            "him... his methods were heavy\x01",
            "handed in many ways.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Being shaken by evil is a\x01",
            "normal thing. I've got to\x01",
            "watch out for that too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_27F9")

    label("loc_275A")


    ChrTalk(
        0xFE,
        (
            "But even so, there's that\x01",
            "shining bluish-white tree.\x01",
            "What could be its meaning?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now that the President's\x01",
            "gone, is there anyone\x01",
            "left to deal with it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27F9")

    Jump("loc_3842")

    label("loc_27FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_280C")
    Jump("loc_3842")

    label("loc_280C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2976")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28ED")

    ChrTalk(
        0xFE,
        (
            "Crossbell State\x01",
            "independence... I'm still\x01",
            "thinking over the matter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If it were to go forward,\x01",
            "it would be a huge step\x01",
            "forward for Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think I'll believe in\x01",
            "President Dieter.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2971")

    label("loc_28ED")


    ChrTalk(
        0xFE,
        (
            "I think I'll believe in\x01",
            "President Dieter.\x02",
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

    label("loc_2971")

    Jump("loc_3842")

    label("loc_2976")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2AEC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A55")

    ChrTalk(
        0xFE,
        (
            "Ilya collapsed and Arc-\x01",
            "en-Ciel is closed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Though reconstruction is proceeding\x01",
            "smoothy, the event echoes in the\x01",
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
    Jump("loc_2AE7")

    label("loc_2A55")


    ChrTalk(
        0xFE,
        (
            "Though reconstruction is proceeding\x01",
            "smoothy, the event echoes in the\x01",
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

    label("loc_2AE7")

    Jump("loc_3842")

    label("loc_2AEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2C89")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C06")

    ChrTalk(
        0xFE,
        (
            "I heard that hostilities are occurring\x01",
            "between the CGF and that armed group\x01",
            "even now on Mainz Mountain Path.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems the CGF couldn't\x01",
            "settle the conflict even after\x01",
            "fighting all night long...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mmm. They are certainly\x01",
            "troublesome opponents.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2C84")

    label("loc_2C06")


    ChrTalk(
        0xFE,
        (
            "The CGF are combat\x01",
            "professionals. To think\x01",
            "they still haven't won...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mmm. They are certainly\x01",
            "troublesome opponents.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C84")

    Jump("loc_3842")

    label("loc_2C89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2C97")
    Jump("loc_3842")

    label("loc_2C97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2D8C")

    ChrTalk(
        0xFE,
        (
            "The Arc-en-Ciel performance... According\x01",
            "to rumor, they're trusting newcomer\x01",
            "Sully with all the additional scenes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if she'll be as popular as\x01",
            "Rixia Mao when she debuted. Anyhow,\x01",
            "I'm looking forward to seeing it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3842")

    label("loc_2D8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2E31")

    ChrTalk(
        0xFE,
        (
            "There's two days left\x01",
            "until the Arc-en-Ciel\x01",
            "performance...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Luckily, I was able to\x01",
            "reserve some A-seat tickets,\x01",
            "so I'm looking forward to it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3842")

    label("loc_2E31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3006")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F54")

    ChrTalk(
        0xFE,
        (
            "Independence as a state...\x01",
            "It'll be rather difficult to\x01",
            "pull that off, if you ask me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's no way the Empire\x01",
            "or Republic will\x01",
            "recognize a vassal state.\x02",
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
    Jump("loc_3001")

    label("loc_2F54")


    ChrTalk(
        0xFE,
        (
            "There's no way the Empire\x01",
            "or Republic will\x01",
            "recognize a vassal state.\x02",
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

    label("loc_3001")

    Jump("loc_3842")

    label("loc_3006")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_31C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_310D")

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
            "The managers plan to\x01",
            "start it up after the\x01",
            "trade conference is over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In the end, what will come\x01",
            "of it... I'm looking forward\x01",
            "to seeing the answer.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_31BE")

    label("loc_310D")


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
            "What will be the result of the\x01",
            "trade conference... I'm looking\x01",
            "forward to seeing the answer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31BE")

    Jump("loc_3842")

    label("loc_31C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_3315")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_328B")

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
            "There should be no one\x01",
            "living there, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, maybe I'm hearing\x01",
            "things.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3310")

    label("loc_328B")


    ChrTalk(
        0xFE,
        (
            "By the way, was it about ten\x01",
            "years ago that a ghost was\x01",
            "said to have appeared there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, that's mere\x01",
            "nonsensical gossip.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3310")

    Jump("loc_3842")

    label("loc_3315")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3465")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33EC")

    ChrTalk(
        0xFE,
        (
            "The veil over Orchis\x01",
            "Tower has finally been\x01",
            "removed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But I can't believe\x01",
            "they'd go to such\x01",
            "lengths to show it off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mmm. I'm looking forward\x01",
            "to seeing what will\x01",
            "happen next.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3460")

    label("loc_33EC")


    ChrTalk(
        0xFE,
        (
            "Orchis Tower... They\x01",
            "really built such a\x01",
            "thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mmm. I'm looking forward\x01",
            "to seeing what will\x01",
            "happen next.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3460")

    Jump("loc_3842")

    label("loc_3465")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_35F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3563")

    ChrTalk(
        0xFE,
        (
            "Come to think of it, Arc-en-\x01",
            "Ciel released information on\x01",
            "their next performance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They said they were doing a\x01",
            "renewal version of Golden\x01",
            "Sun, Silver Moon, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, perhaps I should\x01",
            "hurry and reserve my\x01",
            "ticket.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_35F4")

    label("loc_3563")


    ChrTalk(
        0xFE,
        (
            "In the end, I wonder how the\x01",
            "Golden Sun, Silver Moon\x01",
            "renewal version will turn out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, perhaps I should\x01",
            "hurry and reserve my\x01",
            "ticket.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35F4")

    Jump("loc_3842")

    label("loc_35F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3607")
    Jump("loc_3842")

    label("loc_3607")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3842")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_36B3")

    ChrTalk(
        0xFE,
        (
            "Recently, I've been\x01",
            "seeing a recklessly\x01",
            "driven orbal car.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Goodness... I wonder what\x01",
            "the driver plans to do if\x01",
            "there's an accident.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3842")

    label("loc_36B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37A4")

    ChrTalk(
        0xFE,
        (
            "The new City Hall\x01",
            "building was finally\x01",
            "completed the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems that a lot of time\x01",
            "has passed since its\x01",
            "construction started, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, I'm looking\x01",
            "forward to the unveiling\x01",
            "ceremony at month end.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3842")

    label("loc_37A4")


    ChrTalk(
        0xFE,
        (
            "As a businessman, I\x01",
            "participated in a part of the\x01",
            "new City Hall building project.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, I'm looking\x01",
            "forward to the unveiling\x01",
            "ceremony at month end.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3842")

    TalkEnd(0xFE)
    Return()

    # Function_7_2667 end

    def Function_8_3846(): pass

    label("Function_8_3846")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3919")
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
            "driving next time too,\x01",
            "ok?\x02",
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
    Jump("loc_396D")

    label("loc_3919")


    ChrTalk(
        0xFE,
        (
            "Hehe. If you can handle an\x01",
            "orbal car this well, you've\x01",
            "truly made it your own.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_396D")

    TalkEnd(0xFE)
    Return()

    # Function_8_3846 end

    def Function_9_3971(): pass

    label("Function_9_3971")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Looking at Reggie like this,\x01",
            "it's clear to me that he's a\x01",
            "skilled orbal car driver.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "His dad's not an employee of\x01",
            "Verne Co.'s orbal car development\x01",
            "division for nothing.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_3971 end

    def Function_10_3A2B(): pass

    label("Function_10_3A2B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B0D")
    OP_4B(0xFE, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Man. Flooring it on the\x01",
            "highway is the best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hehe. Unlike in the city,\x01",
            "there aren't to many\x01",
            "obstacles out there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Haha, I'm looking\x01",
            "forward to next time,\x01",
            "Reggie.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xFE, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0xFE, 0x10)
    SetScenarioFlags(0x0, 4)
    Jump("loc_3B71")

    label("loc_3B0D")


    ChrTalk(
        0xFE,
        (
            "Man. Flooring it on the\x01",
            "highway is the best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll try tuning it up to\x01",
            "increase the speed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B71")

    TalkEnd(0xFE)
    Return()

    # Function_10_3A2B end

    def Function_11_3B75(): pass

    label("Function_11_3B75")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3BFF")

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
        (
            "Ah, I'm tired of fixing\x01",
            "it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C71")

    label("loc_3BFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3C71")

    ChrTalk(
        0xFE,
        (
            "Now then... I've got to\x01",
            "get to work today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, but commuting on\x01",
            "rainy days is such a\x01",
            "pain.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C71")

    TalkEnd(0xFE)
    Return()

    # Function_11_3B75 end

    def Function_12_3C75(): pass

    label("Function_12_3C75")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4004")

    ChrTalk(
        0x101,
        (
            "#00005FHuh? Harold? ...Are you\x01",
            "going somewhere?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#03600FYes. I got invited to Armorica\x01",
            "Village a while back.\x02\x03",
            "#03604FLawyer Ian recommended it too, so\x01",
            "I'll be staying there with my\x01",
            "family for a while.\x02\x03",
            "#03608FI can't believe something this\x01",
            "terrible would happen in Crossbell\x01",
            "on the morning of our departure.\x02",
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
            "#00300FBut you got an invitation\x01",
            "and everything! Shouldn't\x01",
            "you go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FThat's right... It seems like\x01",
            "it's been a while since you\x01",
            "had a vacation, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#03603FNo, that won't do... I'm planning\x01",
            "to return here after taking\x01",
            "Sophia and Colin to Armorica.\x02\x03",
            "#03600FPeople I'm indebted to seem to be\x01",
            "in trouble. I can't abandon them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FIs that so...\x02\x03",
            "#00001FTo be honest, it would\x01",
            "be strange if nothing\x01",
            "happened.\x02\x03",
            "Be careful while\x01",
            "travelling on the\x01",
            "highway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#03600FSure... and thanks. You\x01",
            "guys be careful too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x192, 0)
    Jump("loc_4180")

    label("loc_4004")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4101")

    ChrTalk(
        0xF,
        (
            "#03600FI'm planning to return here after\x01",
            "taking Sophia and Colin to\x01",
            "Armorica.\x02\x03",
            "#03603FSophia and Colin have been looking\x01",
            "forward to this, but... It seems\x01",
            "the situation is quite chaotic.\x02\x03",
            "#03600F...Please, everyone. Do be\x01",
            "careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_4180")

    label("loc_4101")


    ChrTalk(
        0xF,
        (
            "#03603FI'm planning to return\x01",
            "here after taking Sophia\x01",
            "and Colin to Armorica.\x02\x03",
            "#03600F...Please, everyone. Do\x01",
            "be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4180")

    TalkEnd(0xFE)
    Return()

    # Function_12_3C75 end

    def Function_13_4184(): pass

    label("Function_13_4184")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4248")

    ChrTalk(
        0xFE,
        (
            "It's been a while since we\x01",
            "had dinner as a family. We're\x01",
            "going shopping later, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You can't avoid seeing that\x01",
            "stupidly large tree. I\x01",
            "can't help but feel uneasy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_42E8")

    label("loc_4248")


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
            "What is with that stupidly\x01",
            "large tree! If I whistle I\x01",
            "won't be scared.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42E8")

    TalkEnd(0xFE)
    Return()

    # Function_13_4184 end

    def Function_14_42EC(): pass

    label("Function_14_42EC")

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
            "#11504F#11PHmm, hmm, hmm～\x02\x03",
            "#11505FOh, I saw it! I guess it's\x01",
            "really true that there are\x01",
            "some different species lately.\x02\x03",
            "#11509FMan, I wish I had brought my\x01",
            "fishing rod.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#5PLechter... What are you\x01",
            "doing in a place like\x01",
            "this?\x02",
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
            "Oh, looks like I've caught my prey\x01",
            "even without a rod.\x02\x03",
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
        "#10105F#5PHuh?\x02",
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
            "#11509F#11PHaha, that is what I was\x01",
            "trying to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5P(...We can't let him have his way with\x01",
            "us.)\x02\x03",
            "#00001FLetcher, allow me to change the subject.\x02\x03",
            "You're a member of the intelligence\x01",
            "division that let Red Constellation enter\x01",
            "Crossbell. What are you doing here?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "#11509F#11PHaha, you finally said\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#5PHaha, well straight talk\x01",
            "is the best way of dealing\x01",
            "with people like yourself.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 500)

    ChrTalk(
        0xFE,
        (
            "#11504F#12PHaha, very well then.\x01",
            "I'll give you an answer.\x02\x03",
            "#11500FAs you can see, I came\x01",
            "here on break.\x02\x03",
            "#11506FAwesome as I am,\x01",
            "guarding that old man's\x01",
            "tiring.\x02",
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
            "#00005F#5PO-Old man? You mean\x01",
            "Chancellor Osborne?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#5PI was worried about him.\x01",
            "You're one of the\x01",
            "chancellor's aides, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#11502F#4PHehe, who knows. I don't\x01",
            "remember saying that\x01",
            "exaggerated thing even once.\x02\x03",
            "#11504FWell then. My break's almost\x01",
            "up. It's time I started\x01",
            "getting back to the old man.\x02\x03",
            "#11500FSee you guys. Good luck with\x01",
            "everything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105F#5PH-Huh!?\x02",
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x2D, 0x1F4)

    def lambda_4A90():

        label("loc_4A90")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_4A90")

    QueueWorkItem2(0x101, 2, lambda_4A90)

    def lambda_4AA2():

        label("loc_4AA2")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_4AA2")

    QueueWorkItem2(0x102, 2, lambda_4AA2)

    def lambda_4AB4():

        label("loc_4AB4")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_4AB4")

    QueueWorkItem2(0x104, 2, lambda_4AB4)

    def lambda_4AC6():

        label("loc_4AC6")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_4AC6")

    QueueWorkItem2(0x109, 2, lambda_4AC6)

    def lambda_4AD8():

        label("loc_4AD8")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_4AD8")

    QueueWorkItem2(0x105, 2, lambda_4AD8)
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
            "#00306F#5PMan, way to dodge the\x01",
            "question...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 0)), scpexpr(EXPR_END)), "loc_4B6F")
    Call(0, 15)

    label("loc_4B6F")

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

    # Function_14_42EC end

    def Function_15_4BB4(): pass

    label("Function_15_4BB4")

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
            "#00003F#6PLechter, and Kilika too...\x02\x03",
            "Both the Imperial spy and the\x01",
            "Republican one came to the\x01",
            "city with similar timing.\x02\x03",
            "#00001FWhat do you guys think?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4C9D():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4C9D)
    Sleep(50)

    def lambda_4CAD():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4CAD)
    Sleep(50)

    def lambda_4CBD():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4CBD)
    Sleep(50)

    def lambda_4CCD():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4CCD)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x109,
        (
            "#10103F#6PIt's suspicious,\x01",
            "somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#6PHaha, if that's the\x01",
            "case, shall we follow\x01",
            "them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#6PI think that would be\x01",
            "difficult.\x02\x03",
            "#00103FI got the sense that\x01",
            "both of them knew we\x01",
            "were coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PShall we report this to\x01",
            "Detective Dudley and the\x01",
            "others?\x02\x03",
            "#00000FThey might learn\x01",
            "something if they combine\x01",
            "it with their other info.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105F#6PYeah... That sounds\x01",
            "good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300F#6PIt's decided then. Let's\x01",
            "head to HQ.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0xA3, 0x1, 0xC)
    Return()

    # Function_15_4BB4 end

    def Function_16_4EB8(): pass

    label("Function_16_4EB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 6)), scpexpr(EXPR_END)), "loc_4F48")
    EventBegin(0x2)
    ClearMapFlags(0x20)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "This is the residence of Congressman\x01",
            "Campbell of the Republican Faction.\x01",
            "You've no particular business here.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Jump("loc_5440")

    label("loc_4F48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5362")
    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#00005FIf I'm remembering it\x01",
            "right, this place is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FIt's the residence of\x01",
            "Congressman Campbell, who\x01",
            "leads the Republic faction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FI heard that congressmen\x01",
            "involved with that cult\x01",
            "were overthrown...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FThat's true. In Congressman\x01",
            "Campbell's case, it seems no such\x01",
            "connection was confirmed.\x02\x03",
            "#00100FAlthough he does have a connection\x01",
            "with Heiyue, at the present time,\x01",
            "that's not illegal...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHaha. So what you're\x01",
            "saying is, it's certain\x01",
            "he's a corrupt character.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_52CE")

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
            "#00100FYou must be talking about\x01",
            "Karla. Yes, we went to\x01",
            "Sunday School together.\x02\x03",
            "#00104FTherefore, I'm relieved to\x01",
            "learn her father had no\x01",
            "connection with the cult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108FThat's right... But I wouldn't\x01",
            "want to think about my friend's\x01",
            "father being that kind of person.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52CE")


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
        "#00100FYes, I agree. Let's go.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12F, 6)
    TalkEnd(0xFF)
    Jump("loc_5440")

    label("loc_5362")

    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#00000FI think this is... The residence\x01",
            "of Congressman Campbell, leader\x01",
            "of the Republic faction.\x02\x03",
            "We don't have any business here\x01",
            "right now, so let's hold off on\x01",
            "visiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FYes, I agree. Let's go.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12F, 6)
    TalkEnd(0xFF)

    label("loc_5440")

    Return()

    # Function_16_4EB8 end

    def Function_17_5441(): pass

    label("Function_17_5441")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_546F")
    Call(0, 39)
    Return()

    label("loc_546F")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The gate is locked.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_17_5441 end

    def Function_18_54A1(): pass

    label("Function_18_54A1")

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

    # Function_18_54A1 end

    def Function_19_54D1(): pass

    label("Function_19_54D1")

    EventBegin(0x1)
    Sound(2094, 255, 100, 0)

    ChrTalk(
        0x101,
        (
            "#0000FIt seems we can fish\x01",
            "here.\x02",
        )
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
            "Fish\x01",        # 0
            "Cancel\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5593")
    OP_E2(0x2)
    MiniGame(0x6, 0x2, 0xFFFFEAA2, 0xFFFFE890, 0xFFFF5DB2, 0x10E, 0xFFFFD90E, 0xFFFFE69C, 0xFFFF5C36)

    label("loc_5593")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_19_54D1 end

    def Function_20_5598(): pass

    label("Function_20_5598")

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
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_56A3")
    SetChrFlags(0x9, 0x8000)
    EndChrThread(0x9, 0xFF)
    SetChrPos(0x9, -5000, 0, -5000, 180)

    def lambda_5693():
        OP_9B(0x0, 0xFE, 0x0, 0x7530, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5693)

    label("loc_56A3")

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

    # Function_20_5598 end

    def Function_21_5724(): pass

    label("Function_21_5724")

    SetChrPos(0xFE, 25550, 0, -4600, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -6000, 0, -4600)
    OP_9F(0x1, -15000, 0, -3100)
    OP_9F(0x1, -16000, 0, 7900)
    OP_9F(0x2, 0xFE, 5500, 0x6)
    Return()

    # Function_21_5724 end

    def Function_22_576D(): pass

    label("Function_22_576D")

    Sleep(2000)
    OP_95(0xFE, 0, 0, -5600, 2000, 0x1)
    OP_95(0xFE, -14000, 0, -5600, 2000, 0x1)
    Return()

    # Function_22_576D end

    def Function_23_5799(): pass

    label("Function_23_5799")

    Sound(468, 2, 100, 0)
    Sound(458, 0, 100, 0)
    Sleep(4500)
    Sound(494, 0, 70, 0)
    Return()

    # Function_23_5799 end

    def Function_24_57AF(): pass

    label("Function_24_57AF")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A56")
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

    def lambda_58DD():
        OP_97(0x101, 0xFFFFF830, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_58DD)
    Sleep(50)

    def lambda_58FA():
        OP_97(0x102, 0xFFFFF830, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_58FA)
    Sleep(50)

    def lambda_5917():
        OP_97(0x109, 0xFFFFF830, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5917)
    Sleep(50)

    def lambda_5934():
        OP_97(0x105, 0xFFFFF830, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5934)
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
    Jump("loc_5C39")

    label("loc_5A56")

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

    def lambda_5B09():
        OP_97(0x101, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5B09)
    Sleep(50)

    def lambda_5B26():
        OP_97(0x102, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5B26)
    Sleep(50)

    def lambda_5B43():
        OP_97(0x109, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5B43)
    Sleep(50)

    def lambda_5B60():
        OP_97(0x105, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5B60)
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

    label("loc_5C39")

    OP_68(-13920, 500, -3320, 1000)
    MoveCamera(31, 31, 0, 1000)
    OP_6E(620, 1000)
    SetCameraDistance(20000, 1000)
    BeginChrThread(0x13, 1, 0, 25)
    BeginChrThread(0x17, 1, 0, 26)

    NpcTalk(
        0x12,
        "Youth's Voice",
        "#10AHey there!\x02",
    )

    CloseMessageWindow()
    OP_68(8360, 1450, -3280, 1500)
    MoveCamera(39, 29, 0, 1500)

    NpcTalk(
        0x12,
        "Youth's Voice",
        "#5AHaha, this is the best!\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    def lambda_5CE7():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5CE7)
    Sleep(50)

    def lambda_5CF7():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5CF7)
    Sleep(50)

    def lambda_5D07():
        OP_93(0x109, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5D07)
    Sleep(50)

    def lambda_5D17():
        OP_93(0x105, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5D17)
    OP_6F(0x79)
    OP_0D()
    Sleep(1500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5DB9")
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
    Jump("loc_5EE6")

    label("loc_5DB9")

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

    def lambda_5E36():
        OP_95(0x102, 4970, 0, -5120, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5E36)
    Sleep(100)

    def lambda_5E53():
        OP_95(0x101, 3840, 0, -3970, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5E53)
    Sleep(100)

    def lambda_5E70():
        OP_95(0x109, 6070, 0, -3420, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5E70)
    Sleep(100)

    def lambda_5E8D():
        OP_95(0x105, 7190, 0, -4250, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5E8D)
    WaitChrThread(0x109, 1)

    def lambda_5EAB():
        OP_93(0x109, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5EAB)
    WaitChrThread(0x105, 1)

    def lambda_5EBC():
        OP_93(0x105, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5EBC)
    WaitChrThread(0x101, 1)

    def lambda_5ECD():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5ECD)
    WaitChrThread(0x102, 1)

    def lambda_5EDE():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5EDE)

    label("loc_5EE6")


    ChrTalk(
        0x101,
        (
            "#00005FW-What was that...? That\x01",
            "speed was reckless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FA clear speeding\x01",
            "violation...\x02\x03",
            "I feel bad for their\x01",
            "car, being driven like\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FA recklessly driven orbal\x01",
            "car... Those have been sighted\x01",
            "more often in the city, lately.\x02\x03",
            "#00103FReckless driving causes\x01",
            "problems for a lot of different\x01",
            "people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10305FOh, I see.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(50)

    ChrTalk(
        0x105,
        (
            "#10300FSo, what does that have\x01",
            "to do with the Special\x01",
            "Support Section?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_609B():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_609B)
    Sleep(50)

    def lambda_60AB():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_60AB)
    Sleep(50)

    def lambda_60BB():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_60BB)
    Sleep(50)

    ChrTalk(
        0x101,
        (
            "#00003FWe can't overlook it, of\x01",
            "course.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6185")
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
            "◆Officer Kate at\x01",
            "Waterfront Area? (debug)\x07\x00\x02",
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

    label("loc_6185")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 4)), scpexpr(EXPR_END)), "loc_624F")

    ChrTalk(
        0x101,
        (
            "#00004FIf I remember correctly,\x01",
            "Kate was patrolling\x01",
            "Entertainment District.\x02\x03",
            "#00000FI'll try contacting her\x01",
            "ENIGMA.\x02\x03",
            "The Patrol Division is\x01",
            "qualified to handle this\x01",
            "type of incident.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6303")

    label("loc_624F")


    ChrTalk(
        0x101,
        (
            "#00003F...I'll try consulting\x01",
            "Officer Kate of the\x01",
            "Patrol Division.\x02\x03",
            "#00000FShe might already have a\x01",
            "plan for dealing with\x01",
            "this sort of thing.\x02\x03",
            "I'll try contacting her\x01",
            "ENIGMA.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6303")

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
            "─Yes, this is Officer\x01",
            "Kate of the Patrol\x01",
            "Division.\x02",
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
            "#00000FOfficer Kate, thanks for\x01",
            "your hard work.\x02",
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
            "Ah, Lloyd. Did you need\x01",
            "something?\x02",
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
            "#00003FUmm, actually, there's\x01",
            "something I'd like to\x01",
            "discuss with you...\x02",
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
            "Ah, so you guys saw one\x01",
            "too.\x02\x03",
            "Well, since you're\x01",
            "here... I'd like your\x01",
            "help with something.\x02",
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
            "#00005FHelp?\x02",
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
            "If you have time, can\x01",
            "you come to my location?\x02\x03",
            "I'm waiting by the\x01",
            "Entertainment District\x01",
            "hotel.\x02",
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
            "#00000FY-Yes. Understood.\x02",
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
            "Alright then. See you\x01",
            "later.\x02",
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
        "#00100FWhat did she say?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FIt seems she wants our\x01",
            "help with something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FThe Patrol Division\x01",
            "does?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309FStop the orbal car with\x01",
            "brute force! ...Maybe\x01",
            "it's something like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FC'mon. You know that's\x01",
            "too dangerous...\x02\x03",
            "#00000FAnyway, let's head for\x01",
            "the Entertainment\x01",
            "District hotel.\x02",
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_689A")
    SetChrPos(0x0, -320, 0, -25290, 0)
    Jump("loc_68AB")

    label("loc_689A")

    SetChrPos(0x0, 3840, 0, -3970, 90)

    label("loc_68AB")

    EventEnd(0x5)
    Return()

    # Function_24_57AF end

    def Function_25_68AE(): pass

    label("Function_25_68AE")

    SetChrPos(0x13, -15860, 300, 20000, 180)
    OP_96(0xFE, 0xFFFFBD7A, 0x0, 0xFFFFF8B2, 0x4E20, 0x0)
    OP_9F(0x0, 0x13)
    OP_9F(0x1, -16800, 0, -2530)
    OP_9F(0x1, -14190, 0, -5130)
    OP_9F(0x1, -12700, 0, -5370)
    OP_9F(0x2, 0x13, 11000, 0x6)
    OP_96(0xFE, 0x767A, 0x0, 0xFFFFE85E, 0x4E20, 0x0)
    Return()

    # Function_25_68AE end

    def Function_26_691F(): pass

    label("Function_26_691F")

    Sound(486, 0, 100, 0)
    Sleep(1000)
    Sound(487, 0, 100, 0)
    Sound(494, 0, 100, 0)
    Return()

    # Function_26_691F end

    def Function_27_6935(): pass

    label("Function_27_6935")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A16")
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
            "#1K◆ About [Stopping a\x01",
            "Recklessly Driven Car],\x01",
            "you... (Debug)\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[No Change]\x01",         # 0
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A02")
    OP_29(0x69, 0x4, 0x10)
    Jump("loc_6A16")

    label("loc_6A02")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A16")
    OP_29(0x69, 0x3, 0x10)

    label("loc_6A16")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6AFE")

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
        (
            "#00105FWhy is it in a place\x01",
            "like this...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FI don't know, but... I'm\x01",
            "getting a bad feeling\x01",
            "about this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C1C")

    label("loc_6AFE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6B82")

    ChrTalk(
        0x101,
        (
            "#00006FIt's the orbal car of\x01",
            "those three, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHaha. Honestly, it's\x01",
            "better than they\x01",
            "deserve.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C1C")

    label("loc_6B82")


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
            "#10300FHmph, what an\x01",
            "affectatious design.\x02\x03",
            "#10304FHeh. It's funny how\x01",
            "poorly it matches its\x01",
            "owner.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C1C")

    TalkEnd(0xFF)
    Return()

    # Function_27_6935 end

    def Function_28_6C20(): pass

    label("Function_28_6C20")

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
            "#12P#00000FNext to the MacDowell\x01",
            "house... This must be\x01",
            "the place.\x02",
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
            "#12P#00000FExcuse us, is anyone\x01",
            "home?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#12P#00003FIt's no good, there's no\x01",
            "response.\x02",
        )
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
            "#5P#00001FOh, it... looks like\x01",
            "it's open.\x02\x03",
            "#00003FAnd I hear some voices\x01",
            "inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10105FAre they so focused on\x01",
            "their conversation that\x01",
            "they just didn't notice?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FAnyway, seeing as it's\x01",
            "open, do you think it's\x01",
            "okay for us to enter?\x02\x03",
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
            "barge in wherever we please.\x02\x03",
            "#00000FBut, we can't just walk away.\x01",
            "Let's head inside and make\x01",
            "sure they know we're here.\x02",
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

    # Function_28_6C20 end

    def Function_29_6FCB(): pass

    label("Function_29_6FCB")

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
            "#12P#10302FMan, they're a little\x01",
            "too into this aren't\x01",
            "they.\x02",
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
            "the hands of those guys.\x02\x03",
            "#00103FMr. Bond must be rather\x01",
            "agitated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10101FBut, I don't see anything\x01",
            "especially illegal in their\x01",
            "contract...\x02\x03",
            "#10106FAnd I don't recall any complaints\x01",
            "from around here either so there\x01",
            "might not be anything we can do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00003FYeah... You're right.\x02\x03",
            "#00000F...Anyway, with this, our\x01",
            "investigation of Residential\x01",
            "District is complete.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x6A, 0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_73A8")
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
            "◆Investigation Status?\x01",
            "(Debug)\x07\x00\x02",
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
        (0, "loc_7379"),
        (1, "loc_737E"),
        (2, "loc_7386"),
        (3, "loc_7397"),
        (SWITCH_DEFAULT, "loc_73A8"),
    )


    label("loc_7379")

    Jump("loc_73A8")

    label("loc_737E")

    ClearScenarioFlags(0x131, 7)
    Jump("loc_73A8")

    label("loc_7386")

    SetScenarioFlags(0x131, 7)
    ClearScenarioFlags(0x132, 0)
    ClearScenarioFlags(0x132, 1)
    ClearScenarioFlags(0x132, 2)
    Jump("loc_73A8")

    label("loc_7397")

    SetScenarioFlags(0x131, 7)
    SetScenarioFlags(0x132, 0)
    SetScenarioFlags(0x132, 1)
    SetScenarioFlags(0x132, 2)
    Jump("loc_73A8")

    label("loc_73A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7492")

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
            "#5P#00003FYeah. I'm worried about\x01",
            "him too.\x02\x03",
            "#00000FAll right, let's head to\x01",
            "Mr. Bond's new home on\x01",
            "East Street.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7573")

    label("loc_7492")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_74F4")

    ChrTalk(
        0x101,
        (
            "#5P#00000FAlright, then let's\x01",
            "continue our\x01",
            "investigation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7573")

    label("loc_74F4")


    ChrTalk(
        0x101,
        (
            "#5P#00000FAlright! We've finished\x01",
            "our investigation.\x02\x03",
            "Let's head back to the\x01",
            "City Meeting Hall and\x01",
            "make our report.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x6A, 0x1, 0x6)

    label("loc_7573")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_65(0x2, 0x1)
    SetMapObjFlags(0xB, 0x10)
    SetScenarioFlags(0x131, 6)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -17150, -6000, -18250, 180)
    EventEnd(0x5)
    Return()

    # Function_29_6FCB end

    def Function_30_75A3(): pass

    label("Function_30_75A3")

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

    def lambda_7670():
        OP_95(0xFE, -6050, -6000, -22480, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7670)
    Sleep(50)

    def lambda_768D():
        OP_95(0xFE, -4650, -6000, -22780, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_768D)
    Sleep(50)

    def lambda_76AA():
        OP_95(0xFE, -5250, -6000, -21350, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_76AA)
    Sleep(50)

    def lambda_76C7():
        OP_95(0xFE, -3850, -6000, -21480, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_76C7)
    Sleep(50)

    def lambda_76E4():
        OP_95(0xFE, -6850, -6000, -21200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_76E4)
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

    def lambda_77AE():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_77AE)
    Sleep(50)

    def lambda_77BE():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_77BE)
    Sleep(50)

    def lambda_77CE():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_77CE)
    Sleep(50)

    def lambda_77DE():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_77DE)
    Sleep(50)

    def lambda_77EE():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_77EE)
    Sleep(1000)
    Fade(500)
    OP_68(-4050, 1670, -12540, 0)
    MoveCamera(42, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14080, 0)
    OP_0D()

    def lambda_7832():

        label("loc_7832")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_7832")

    QueueWorkItem2(0x101, 1, lambda_7832)

    def lambda_7844():

        label("loc_7844")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_7844")

    QueueWorkItem2(0x104, 1, lambda_7844)

    def lambda_7856():

        label("loc_7856")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_7856")

    QueueWorkItem2(0x102, 1, lambda_7856)

    def lambda_7868():

        label("loc_7868")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_7868")

    QueueWorkItem2(0x109, 1, lambda_7868)

    def lambda_787A():

        label("loc_787A")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_787A")

    QueueWorkItem2(0x105, 1, lambda_787A)
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
            "#5P#04600FYou guys were really\x01",
            "slow, so I started\x01",
            "looking for her myself.\x02\x03",
            "#04609FAnd? Which house was it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FThis one. But...\x02\x03",
            "#00006FWe don't approve of\x01",
            "having you along.\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x1A3, 0x109, 0x3E8, 0x7D0, 0x0)
    Sleep(300)

    ChrTalk(
        0x1A3,
        (
            "#04600FHey lady. Dog person or\x01",
            "cat person. Which is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10105FM-Me?\x02\x03",
            "#10104FUmm... If I had to say,\x01",
            "then cat person, I\x01",
            "think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        "#04609FAhaha, same as me!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#6P#00303F(...Just give up. It\x01",
            "doesn't matter what we\x01",
            "say.)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#12P#00006F(*sigh*... Looks like\x01",
            "it.)\x02",
        )
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

    # Function_30_75A3 end

    def Function_31_7B4E(): pass

    label("Function_31_7B4E")

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
            "#00106FYeah... She's super\x01",
            "strong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FWith her slender arms,\x01",
            "she lifted two adult\x01",
            "men...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHaha. She's not the\x01",
            "daughter of the strongest\x01",
            "jaeger corps for nothing.\x02\x03",
            "#10302FYou understood her thirst\x01",
            "for blood back there,\x01",
            "didn't you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00303F...Don't lump me in with\x01",
            "her.\x02",
        )
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
            "#12P#04606FHey, what are you guys\x01",
            "doing?\x02\x03",
            "#04602FWe're not gonna find her\x01",
            "if we don't hurry!\x02",
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

    # Function_31_7B4E end

    def Function_32_7F71(): pass

    label("Function_32_7F71")


    def lambda_7F76():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7F76)

    def lambda_7F87():
        OP_95(0xFE, -18140, -5600, -17170, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7F87)
    WaitChrThread(0x101, 1)
    OP_95(0x101, -17710, -6000, -18270, 2000, 0x0)
    OP_93(0x101, 0x87, 0x1F4)
    Return()

    # Function_32_7F71 end

    def Function_33_7FBC(): pass

    label("Function_33_7FBC")


    def lambda_7FC1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7FC1)

    def lambda_7FD2():
        OP_95(0xFE, -18140, -5600, -17170, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7FD2)
    WaitChrThread(0x102, 1)
    OP_95(0x102, -16500, -6000, -17480, 2000, 0x0)
    OP_93(0x102, 0x87, 0x1F4)
    Return()

    # Function_33_7FBC end

    def Function_34_8007(): pass

    label("Function_34_8007")


    def lambda_800C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_800C)

    def lambda_801D():
        OP_95(0xFE, -17390, -6000, -17900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_801D)
    WaitChrThread(0x104, 1)
    OP_95(0x104, -15930, -6000, -19920, 2000, 0x0)
    OP_93(0x104, 0x87, 0x1F4)
    Return()

    # Function_34_8007 end

    def Function_35_8052(): pass

    label("Function_35_8052")


    def lambda_8057():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8057)

    def lambda_8068():
        OP_95(0xFE, -17390, -6000, -17900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8068)
    WaitChrThread(0x109, 1)
    OP_95(0x109, -16510, -6000, -18800, 2000, 0x0)
    OP_93(0x109, 0x87, 0x1F4)
    Return()

    # Function_35_8052 end

    def Function_36_809D(): pass

    label("Function_36_809D")


    def lambda_80A2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_80A2)

    def lambda_80B3():
        OP_95(0xFE, -17390, -6000, -17900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_80B3)
    WaitChrThread(0x105, 1)
    OP_95(0x105, -15400, -6000, -18710, 2000, 0x0)
    OP_93(0x105, 0x87, 0x1F4)
    Return()

    # Function_36_809D end

    def Function_37_80E8(): pass

    label("Function_37_80E8")


    def lambda_80ED():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A3, 2, lambda_80ED)

    def lambda_80FE():
        OP_95(0xFE, -14830, -6000, -20120, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_80FE)
    WaitChrThread(0x1A3, 1)
    OP_93(0x1A3, 0x13B, 0x1F4)
    Return()

    # Function_37_80E8 end

    def Function_38_811F(): pass

    label("Function_38_811F")

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

    def lambda_8454():
        OP_95(0xFE, 19310, 0, -4050, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8454)
    Sleep(50)

    def lambda_8471():
        OP_95(0xFE, 18810, 0, -2750, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_8471)
    Sleep(50)

    def lambda_848E():
        OP_95(0xFE, 18610, 0, -5350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_848E)
    Sleep(50)

    def lambda_84AB():
        OP_95(0xFE, 17110, 0, -2950, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_84AB)
    Sleep(50)

    def lambda_84C8():
        OP_95(0xFE, 16910, 0, -5250, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_84C8)
    Sleep(50)

    def lambda_84E5():
        OP_95(0xFE, 16309, 0, -4250, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_84E5)
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
        (
            "#5P#04602FAll we gotta do now is\x01",
            "catch her.\x02",
        )
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

    # Function_38_811F end

    def Function_39_85E4(): pass

    label("Function_39_85E4")

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
            "#00005FUmm... There's no\x01",
            "mistake. This the\x01",
            "address.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00103FYou're not wrong, but...\x02",
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
            "#00303FI don't sense anyone's\x01",
            "presence.\x02\x03",
            "#00301FThere must've been some\x01",
            "kinda mistake, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FMaybe the sender wrote\x01",
            "the district wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FBut this label... The delivery\x01",
            "address is written, but the\x01",
            "recipient's name isn't.\x02\x03",
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
        "#00005FHuh, what's wrong, Tio?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205FAh, no...\x02",
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x105,
        "#10305FHuh, could it be...\x02",
    )

    CloseMessageWindow()

    def lambda_895C():
        OP_95(0xFE, 17650, 0, -1500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_895C)
    Sleep(300)

    def lambda_8979():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8979)
    Sleep(100)

    def lambda_8989():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8989)
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
        "#00005FIt's open!?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)

    ChrTalk(
        0x105,
        (
            "#10304FIt was ajar, so I had a\x01",
            "feeling...\x02\x03",
            "#10300FWell, let's ask the\x01",
            "resident if this is\x01",
            "their package.\x02",
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
        "#00205F(...?)\x02",
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

    # Function_39_85E4 end

    def Function_40_8B52(): pass

    label("Function_40_8B52")

    EventBegin(0x1)

    ChrTalk(
        0x1A3,
        (
            "#04605FAww... Why are we going\x01",
            "back? Isn't the objective\x01",
            "right in front of us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, I'll be right\x01",
            "there.\x02\x03",
            "#00006F(...It's like Randy said.\x01",
            "No matter what you say to\x01",
            "her, it's pointless.)\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -5250, -1550, -11110, 180)
    EventEnd(0x4)
    Return()

    # Function_40_8B52 end

    def Function_41_8C35(): pass

    label("Function_41_8C35")

    EventBegin(0x1)

    ChrTalk(
        0x1A3,
        (
            "#04600FHey, what are you doing?\x01",
            "Hurry up and chase after\x01",
            "Mary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, you're right.\x01",
            "Let's hurry to\x01",
            "Entertainment District.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 6340, 0, -5780, 90)
    EventEnd(0x4)
    Return()

    # Function_41_8C35 end

    def Function_42_8CD6(): pass

    label("Function_42_8CD6")

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

    # Function_42_8CD6 end

    SaveToFile()

Try(main)
