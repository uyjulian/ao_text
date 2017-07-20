from ScenarioHelper import *

def main():
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
        "Raise old man",             # 1
        "Pentos",               # 2
        "Yuri",                 # 3
        "Sykes",               # 4
        "Reggie",                 # 5
        "OL",                   # 6
        "Lector clerk",         # 7
        "Harold",               # 8
        "Felic",             # 9
        "lease",                 # 10
        "car",                     # 11
        "Runaway vehicle",                 # 12
        "Hostess (A)",         # 13
        "Hostess (B)",         # 14
        "Mary",                 # 15
        "SE control",                 # 16
        "bc0300",                 # 17
        "Central square",               # 18
        "Nishi dori",                 # 19
        "Administrative district",                 # 20
        "Residential area",                 # 21
        "Entertainment district",                 # 22
        "East Street",                 # 23
        "old Town",                 # 24
        "Harbor district",                 # 25
        "IBC",                 # 26
        "Beside the station",               # 27
        "Back street",                 # 28
        "Ursula interchange",           # 29
        "East Crossbell Highway",       # 30
        "West Crossbell Highway",       # 31
        "Mainz Mountain Road",           # 32
        "Orchis Tower",         # 33
    ))

    ATBonus("ATBonus_7F4", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)

    Sepith("Sepith_86A1", 8,   8,   8,   8,   11,  11,  11)

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
        "BattleInfo_8C4", 0x0000, 93, 6, 60, 4, 1, 25, 0, "bc0300", "Sepith_86A1", 60, 30, 10, 0,
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

    PlaceName(167.6699981689453, 0.0, -124.73999786376953, 0x0000, 0x0000, "Central square")
    PlaceName(61.15999984741211, 0.0, -117.44999694824219, 0x0000, 0x0000, "Nishi dori")
    PlaceName(211.41000366210938, 0.0, 19.440000534057617, 0x0000, 0x0000, "Administrative district")
    PlaceName(-37.66999816894531, 0.0, 3.240000009536743, 0x0000, 0x0000, "Residential area")
    PlaceName(80.5999984741211, 0.0, -9.720000267028809, 0x0000, 0x0000, "Entertainment district")
    PlaceName(299.29998779296875, 0.0, -162.0, 0x0000, 0x0000, "East Street")
    PlaceName(356.80999755859375, 0.0, -251.10000610351562, 0x0000, 0x0000, "old Town")
    PlaceName(344.6600036621094, 0.0, -55.08000183105469, 0x0000, 0x0000, "Harbor district")
    PlaceName(302.5400085449219, 0.0, 97.19999694824219, 0x0000, 0x0000, "IBC")
    PlaceName(185.89999389648438, 0.0, -236.52000427246094, 0x0000, 0x0000, "Beside the station")
    PlaceName(109.76000213623047, 0.0, -68.04000091552734, 0x0000, 0x0000, "Back street")
    PlaceName(181.0399932861328, 0.0, -286.739990234375, 0x0000, 0x0000, "Ursula interchange")
    PlaceName(386.7799987792969, 0.0, -139.32000732421875, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-21.469999313354492, 0.0, -119.87999725341797, 0x0000, 0x0000, "West Crossbell Highway")
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
        "Function_7_24A4",         # 07, 7
        "Function_8_34A5",         # 08, 8
        "Function_9_35B1",         # 09, 9
        "Function_10_3636",        # 0A, 10
        "Function_11_377D",        # 0B, 11
        "Function_12_387D",        # 0C, 12
        "Function_13_3D5D",        # 0D, 13
        "Function_14_3EAB",        # 0E, 14
        "Function_15_47C7",        # 0F, 15
        "Function_16_4AC2",        # 10, 16
        "Function_17_4F3F",        # 11, 17
        "Function_18_4FA4",        # 12, 18
        "Function_19_4FD9",        # 13, 19
        "Function_20_50AD",        # 14, 20
        "Function_21_5239",        # 15, 21
        "Function_22_5282",        # 16, 22
        "Function_23_52AE",        # 17, 23
        "Function_24_52C4",        # 18, 24
        "Function_25_6324",        # 19, 25
        "Function_26_6395",        # 1A, 26
        "Function_27_63AB",        # 1B, 27
        "Function_28_6663",        # 1C, 28
        "Function_29_69FF",        # 1D, 29
        "Function_30_6F74",        # 1E, 30
        "Function_31_751E",        # 1F, 31
        "Function_32_7910",        # 20, 32
        "Function_33_795B",        # 21, 33
        "Function_34_79A6",        # 22, 34
        "Function_35_79F1",        # 23, 35
        "Function_36_7A3C",        # 24, 36
        "Function_37_7A87",        # 25, 37
        "Function_38_7ABE",        # 26, 38
        "Function_39_7F83",        # 27, 39
        "Function_40_850A",        # 28, 40
        "Function_41_85CD",        # 29, 41
        "Function_42_8642",        # 2A, 42
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('初级竿', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetItemNumber('小巧射手', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('竹竿', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('钢竿侵略者', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('水中支配者', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11ED")
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17DB")
    Sound(14, 0, 100, 0)
    OP_74(0xF, 0x1E)
    OP_71(0xF, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('弹性大衣', 1)"), scpexpr(EXPR_END)), "loc_1764")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '弹性大衣'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EB, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_17D6")

    label("loc_1764")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            "In the treasure box",
            scpstr(SCPSTR_CODE_ITEM, '弹性大衣'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is contained.\x01",
            "Because my belongings are full,",
            scpstr(SCPSTR_CODE_ITEM, '弹性大衣'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I gave up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xF, 0x1E, 0x0, 0x0, 0x0)

    label("loc_17D6")

    Jump("loc_1820")

    label("loc_17DB")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is nothing in the treasure box.\x07\x00\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_19D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_192F")

    ChrTalk(
        0xFE,
        (
            "I lived in the mansion there\x01",
            "\"Hibrads\" or something\x01",
            "Three pairs of young people … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Knowing that the barrier has gone,\x01",
            "To the Republic of my home country quickly\x01",
            "You seemed to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There seems to be no car unlike before,\x01",
            "I wonder what he is going to do … …?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_19D0")

    label("loc_192F")


    ChrTalk(
        0xFE,
        (
            "The young people who lived in the mansion there,\x01",
            "To the Republic of my home country quickly\x01",
            "You seemed to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There seems to be no car unlike before,\x01",
            "I wonder what he is going to do … …?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19D0")

    Jump("loc_24A0")

    label("loc_19D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_19E3")
    Jump("loc_24A0")

    label("loc_19E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1B9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AFA")

    ChrTalk(
        0xFE,
        (
            "Listening to Dieter's speech,\x01",
            "A four-and-a-five-year-old leader\x01",
            "I remembered the explosion accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although it was reported that there was an accident at the time,\x01",
            "If that is the Empire and the Republic\x01",
            "If it was the result of \"battle\" …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Muu\x01",
            "There is considerable darkness in the crossbell\x01",
            "You can say that you were lurking.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1B98")

    label("loc_1AFA")


    ChrTalk(
        0xFE,
        (
            "Explosion accident that occurred four or five years ago ……\x01",
            "The victim at that time,\x01",
            "It sure was a little girl … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Muu\x01",
            "There is considerable darkness in the crossbell\x01",
            "You can say that you were lurking.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B98")

    Jump("loc_24A0")

    label("loc_1B9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1C19")

    ChrTalk(
        0xFE,
        (
            "In the meantime,\x01",
            "It was terrible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ever since, the night was horrible.\x01",
            "I can not sleep well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24A0")

    label("loc_1C19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1C7A")

    ChrTalk(
        0xFE,
        (
            "But what is occupation?\x01",
            "It is not calm …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Who the hell are you doing?\x02",
    )

    CloseMessageWindow()
    Jump("loc_24A0")

    label("loc_1C7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1C88")
    Jump("loc_24A0")

    label("loc_1C88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1D46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CF4")

    ChrTalk(
        0xFE,
        "…… ZZZ ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "Ha ha\x01",
            "Did something happen?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    ClearChrFlags(0x8, 0x10)
    Jump("loc_1D41")

    label("loc_1CF4")


    ChrTalk(
        0xFE,
        (
            "Oh, exactly.\x01",
            "I fell asleep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…… Did something happen?\x02",
    )

    CloseMessageWindow()

    label("loc_1D41")

    Jump("loc_24A0")

    label("loc_1D46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1DA7")

    ChrTalk(
        0xFE,
        (
            "Fufa …\x01",
            "How dreadful sleepiness ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder if I will fall asleep …\x02",
    )

    CloseMessageWindow()
    Jump("loc_24A0")

    label("loc_1DA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1EEB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E65")

    ChrTalk(
        0xFE,
        (
            "An example referendum day is\x01",
            "It is getting close.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For the future of the younger generation\x01",
            "It can not be hoped with a light feeling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Carefully until the day\x01",
            "I ought to put together my idea.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1EE6")

    label("loc_1E65")


    ChrTalk(
        0xFE,
        (
            "Compliance of independence,\x01",
            "Even for the younger generation\x01",
            "You must think seriously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Carefully until the voting day\x01",
            "I ought to put together my idea.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EE6")

    Jump("loc_24A0")

    label("loc_1EEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_200C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FA7")

    ChrTalk(
        0xFE,
        (
            "In the direction of the cathedral a while ago\x01",
            "A driving car headed for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Certainly, the leaders\x01",
            "It was used for pickup\x01",
            "It was like a limo … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, it is a mistake in seeing it.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2007")

    label("loc_1FA7")


    ChrTalk(
        0xFE,
        (
            "In the direction of the cathedral a while ago\x01",
            "A limousine headed for\x01",
            "You seemed to have gone ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, it is a mistake in seeing it.\x02",
    )

    CloseMessageWindow()

    label("loc_2007")

    Jump("loc_24A0")

    label("loc_200C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_2070")

    ChrTalk(
        0xFE,
        (
            "Oh, it's getting darker\x01",
            "Do not do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We are almost there.\x01",
            "I am going to get home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24A0")

    label("loc_2070")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_21F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_216B")

    ChrTalk(
        0xFE,
        (
            "By the way, recently\x01",
            "I do not see much pizza deliveries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Earlier it was said that every day\x01",
            "You saw it around here … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F(Perhaps Jonah was asking for it … …)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F(It is certainly in Le Mans Autonomous Region right now.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_21F4")

    label("loc_216B")


    ChrTalk(
        0xFE,
        (
            "Previously around this,\x01",
            "Every day is enough\x01",
            "A pizza deliverer was here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Coco, I like pizza much\x01",
            "You should have lived there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21F4")

    Jump("loc_24A0")

    label("loc_21F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2379")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22F7")

    ChrTalk(
        0xFE,
        (
            "Recently I came to the house there\x01",
            "I greeted the young people,\x01",
            "It was ignored.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "On the contrary, with eyes like seeing a dog\x01",
            "I looked down at me and laughed at my nose …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Wow …\x01",
            "The family who lived before\x01",
            "It was nice to have a good gratitude.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2374")

    label("loc_22F7")


    ChrTalk(
        0xFE,
        (
            "If you ask, the people who came over there\x01",
            "A company of a similar company\x01",
            "It's a story of an officer's son … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Wow …\x01",
            "They are cranky guys.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2374")

    Jump("loc_24A0")

    label("loc_2379")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2387")
    Jump("loc_24A0")

    label("loc_2387")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_24A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_23E5")

    ChrTalk(
        0xFE,
        (
            "Whew, are those young people ……\x01",
            "It's noisy and crisp.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24A0")

    label("loc_23E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2454")

    ChrTalk(
        0xFE,
        "Well, what a pleasant and cheerful mind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess I am missing out.\x01",
            "Fah ~ Ah ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_24A0")

    label("loc_2454")


    ChrTalk(
        0xFE,
        "As I thought, this neighborhood is still quiet.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Just for the sun.\x02",
    )

    CloseMessageWindow()

    label("loc_24A0")

    TalkEnd(0xFE)
    Return()

    # Function_6_182C end

    def Function_7_24A4(): pass

    label("Function_7_24A4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2621")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2595")

    ChrTalk(
        0xFE,
        "It seems that President Dieter was arrested.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was supporting him … …\x01",
            "His way of doing was also brutal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, when you worked wrong and somewhere\x01",
            "There is a shake back in the world.\x01",
            "I should also be careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_261C")

    label("loc_2595")


    ChrTalk(
        0xFE,
        (
            "Even so ……\x01",
            "That pale bright tree,\x01",
            "What is it all about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now that there is no President,\x01",
            "Who will do the deal?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_261C")

    Jump("loc_34A1")

    label("loc_2621")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_262F")
    Jump("loc_34A1")

    label("loc_262F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_279B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2705")

    ChrTalk(
        0xFE,
        (
            "\"Crossbell independent country\" … ….\x01",
            "I do not come to realize it yet … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If it is realized as it is,\x01",
            "For Crossbell it is a great step forward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am President Dieter\x01",
            "I will strongly support it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2796")

    label("loc_2705")


    ChrTalk(
        0xFE,
        (
            "I am President Dieter\x01",
            "I will strongly support it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If independence is realized as it is,\x01",
            "For Crossbell\x01",
            "It will be a big step forward.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2796")

    Jump("loc_34A1")

    label("loc_279B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_28F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_286C")

    ChrTalk(
        0xFE,
        (
            "As Iya collapsed\x01",
            "The alkane shell is also closed … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Restoration activities are progressing,\x01",
            "To the hearts of our citizens\x01",
            "Somewhere shadowed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "One bright news\x01",
            "I wish I had it … …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_28EB")

    label("loc_286C")


    ChrTalk(
        0xFE,
        (
            "Restoration activities are progressing,\x01",
            "To the hearts of our citizens\x01",
            "Somewhere shadowed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "One bright news\x01",
            "I wish I had it … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28EB")

    Jump("loc_34A1")

    label("loc_28F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2A6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29C9")

    ChrTalk(
        0xFE,
        (
            "In Mainz Road,\x01",
            "Even now the guard and armed groups\x01",
            "It seems that they are engaged.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if that guard went overnight\x01",
            "Looking at places that can not be solved yet …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mumumu, a rather troublesome partner\x01",
            "I do not think he will make a mistake.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A68")

    label("loc_29C9")


    ChrTalk(
        0xFE,
        (
            "The guard is a battle professional.\x01",
            "Even so, they still have incidents\x01",
            "Looking at the areas that can not be solved ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mumumu, a rather troublesome partner\x01",
            "I do not think he will make a mistake.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A68")

    Jump("loc_34A1")

    label("loc_2A6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2A7B")
    Jump("loc_34A1")

    label("loc_2A7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2B4B")

    ChrTalk(
        0xFE,
        (
            "The performance of the alkane shell … …\x01",
            "In rumors, to Shuri and a newcomer\x01",
            "She seems to leave an additional scene.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lisa Mao, once a newcomer\x01",
            "He is showing such an active performance ……\x01",
            "I will not be expecting anything.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34A1")

    label("loc_2B4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2BDA")

    ChrTalk(
        0xFE,
        (
            "Until the Arcane shell show\x01",
            "Two more days left … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Successfully A seat tickets too\x01",
            "It was able to be secured,\x01",
            "I ought to look forward to it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34A1")

    label("loc_2BDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2D60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CBF")

    ChrTalk(
        0xFE,
        (
            "Independence as a nation ……\x01",
            "I think it is too difficult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Empire and Republic, which is a religious country\x01",
            "I do not think I admit it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I understand the idea of the mayor … …\x01",
            "Too reckless proposition\x01",
            "I guess they have no choice.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2D5B")

    label("loc_2CBF")


    ChrTalk(
        0xFE,
        (
            "Empire and Republic, which is a religious country\x01",
            "Crossbell independence etc\x01",
            "I do not think I will admit it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I understand the idea of the mayor … …\x01",
            "Too reckless proposition\x01",
            "I guess they have no choice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D5B")

    Jump("loc_34A1")

    label("loc_2D60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2EE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E44")

    ChrTalk(
        0xFE,
        (
            "In the Orkis Tower\x01",
            "In the tenant space,\x01",
            "There are also projects that I participate in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After the meeting of the trade meeting\x01",
            "Operation is about to begin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Indeed,\x01",
            "How much achievement will be achieved ……\x01",
            "It can not be fun.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2EDC")

    label("loc_2E44")


    ChrTalk(
        0xFE,
        (
            "In the Orkis Tower\x01",
            "In the tenant space,\x01",
            "There are also projects that I participate in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After the trade meeting ended\x01",
            "How much achievement will be achieved ……\x01",
            "It can not be fun.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EDC")

    Jump("loc_34A1")

    label("loc_2EE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_301B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F91")

    ChrTalk(
        0xFE,
        (
            "From that mansion\x01",
            "Something like a girl's voice\x01",
            "I feel like I heard it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, in this mansion\x01",
            "No one should live … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmm, it is probably the sky.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3016")

    label("loc_2F91")


    ChrTalk(
        0xFE,
        (
            "By the way, about ten years ago,\x01",
            "You are going to get a gruff at this mansion\x01",
            "Was there something that was said?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I can not accept folly\x01",
            "It is just a rumor.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3016")

    Jump("loc_34A1")

    label("loc_301B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3159")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30E4")

    ChrTalk(
        0xFE,
        (
            "At last the Orkis Tower\x01",
            "You took off that veil.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However,\x01",
            "To the buildings that are over there\x01",
            "It is not supposed to be shown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, for future development\x01",
            "I will have no choice but to expect a lot.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3154")

    label("loc_30E4")


    ChrTalk(
        0xFE,
        (
            "Orchis Tower……\x01",
            "It was said that it was a building up there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, for future development\x01",
            "I will have no choice but to expect a lot.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3154")

    Jump("loc_34A1")

    label("loc_3159")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_32D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_323B")

    ChrTalk(
        0xFE,
        (
            "By the way, the alkane shell\x01",
            "Information on the next performance was out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Something 'sun of gold, moon of silver'\x01",
            "I mean to do a renewal version … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, the ticket hurried\x01",
            "It seems better to reserve it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_32CC")

    label("loc_323B")


    ChrTalk(
        0xFE,
        (
            "\"Gold Sun, the Moon of Silver\"\x01",
            "Renewal version is definitely\x01",
            "What will it be like?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, tickets hurry\x01",
            "It seems better to reserve it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32CC")

    Jump("loc_34A1")

    label("loc_32D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_32DF")
    Jump("loc_34A1")

    label("loc_32DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_34A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 5)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_337A")

    ChrTalk(
        0xFE,
        (
            "Recently, I drive hardly\x01",
            "You see a guided vehicle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Completely … if I woke up in an accident\x01",
            "I wonder what he is going to do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34A1")

    label("loc_337A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3429")

    ChrTalk(
        0xFE,
        (
            "The other day the new city hall building finally arrived\x01",
            "It seems that it was completed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A considerable period from construction starts\x01",
            "It seems that it has passed ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, the unveiling ceremony at the end of the month\x01",
            "It will be fun.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_34A1")

    label("loc_3429")


    ChrTalk(
        0xFE,
        (
            "In the new city hall building, I also as an entrepreneur\x01",
            "You have participated in some business plans.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, the unveiling ceremony at the end of the month\x01",
            "It will be fun.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34A1")

    TalkEnd(0xFE)
    Return()

    # Function_7_24A4 end

    def Function_8_34A5(): pass

    label("Function_8_34A5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3565")
    OP_4B(0xFE, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Kuku, this guided car\x01",
            "What can you get up to here\x01",
            "You are about things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Reggie, next time too\x01",
            "I will ask for a fun drive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Hello, leave it to me.\x02",
    )

    CloseMessageWindow()
    OP_4C(0xFE, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    SetScenarioFlags(0x0, 2)
    Jump("loc_35AD")

    label("loc_3565")


    ChrTalk(
        0xFE,
        (
            "Huff, this guided car\x01",
            "What can you get up to here\x01",
            "You are about things.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35AD")

    TalkEnd(0xFE)
    Return()

    # Function_8_34A5 end

    def Function_9_35B1(): pass

    label("Function_9_35B1")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Reggie looks like this,\x01",
            "Driving a car is super skill.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Indeed, my father is Vernes\x01",
            "Because it is a member of the lead vehicle development department.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_35B1 end

    def Function_10_3636(): pass

    label("Function_10_3636")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36F5")
    OP_4B(0xFE, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Well, after all\x01",
            "It's hard to get rid of the highway\x01",
            "It's awesome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "To, unlike in town\x01",
            "Do not give me extra obstacles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Huh, I will ask for the next one.\x02",
    )

    CloseMessageWindow()
    OP_4C(0xFE, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0xFE, 0x10)
    SetScenarioFlags(0x0, 4)
    Jump("loc_3779")

    label("loc_36F5")


    ChrTalk(
        0xFE,
        (
            "Well, after all\x01",
            "It's hard to get rid of the highway\x01",
            "It's awesome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "From now on\x01",
            "Tune up\x01",
            "Do not pursue speed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3779")

    TalkEnd(0xFE)
    Return()

    # Function_10_3636 end

    def Function_11_377D(): pass

    label("Function_11_377D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_380C")

    ChrTalk(
        0xFE,
        (
            "Wow, whether it is raining or not\x01",
            "I do not understand, but today is makeup\x01",
            "Nori is not very good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, I want to fix it … I can not afford it!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3879")

    label("loc_380C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3879")

    ChrTalk(
        0xFE,
        (
            "Well ……\x01",
            "I will not go to work today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Fuu, but on a rainy day\x01",
            "It is a big deal of time to go to work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3879")

    TalkEnd(0xFE)
    Return()

    # Function_11_377D end

    def Function_12_387D(): pass

    label("Function_12_387D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BF8")

    ChrTalk(
        0x101,
        (
            "#00005FThat, Mr. Harold … …\x01",
            "Maybe somewhere\x01",
            "Are you going out?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#03600FYeah, a while ago\x01",
            "I received an invitation from Almorika village.\x02\x03",
            "#03604FBecause there was also Professor Ian's recommendation,\x01",
            "All my family for a while\x01",
            "I intended to stay … …\x02\x03",
            "#03608FIn the morning of departure, the crossbell\x01",
            "It is said that becoming such a serious thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00103F…… We are also upset.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FBut, well, it's a great invitation\x01",
            "Is not it better to go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FThat's right … Mr. Harold also\x01",
            "It seems like a long vacation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#03603FHouse……\x01",
            "If you send Sofia and Collin to the village\x01",
            "I will come back to town only once.\x02\x03",
            "#03600FEven those who are indebted for by the deal\x01",
            "It seems quite confusing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FIs that so……\x02\x03",
            "#00001FHonestly, no matter what happens\x01",
            "I think that there is no state.\x02\x03",
            "Also moving to the highway\x01",
            "Please be careful enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#03600FHaha … Thank you.\x01",
            "Please take care of everyone.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x192, 0)
    Jump("loc_3D59")

    label("loc_3BF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CDE")

    ChrTalk(
        0xF,
        (
            "#03600FIf you send Sofia and Collin to the village\x01",
            "I will come back to town only once.\x02\x03",
            "#03603FI look forward to it\x01",
            "It's bad for Collins … …\x01",
            "It seems quite confusing.\x02\x03",
            "#03600F… … Please take care of everyone.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3D59")

    label("loc_3CDE")


    ChrTalk(
        0xF,
        (
            "#03603FIf you send Sofia and Collin to the village\x01",
            "I will return to town only once.\x02\x03",
            "#03600F… … Please take care of everyone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D59")

    TalkEnd(0xFE)
    Return()

    # Function_12_387D end

    def Function_13_3D5D(): pass

    label("Function_13_3D5D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E1E")

    ChrTalk(
        0xFE,
        (
            "Today is my family for the first time in a while.\x01",
            "Because I was supposed to have dinner,\x01",
            "I'm going shopping now … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That stupid big tree\x01",
            "Even getting into my eyes,\x01",
            "It makes me uneasy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3EA7")

    label("loc_3E1E")


    ChrTalk(
        0xFE,
        (
            "…… In such a case,\x01",
            "Just as old as your grandmother\x01",
            "I hope the situation is normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Such a stupid tree is there!\x01",
            "I'm afraid if you blow whistling.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EA7")

    TalkEnd(0xFE)
    Return()

    # Function_13_3D5D end

    def Function_14_3EAB(): pass

    label("Function_14_3EAB")

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
            "#11504F#11PFun Fun …\x02\x03",
            "#11505F…… Whoa, fish shot discovered!\x01",
            "Recently there are new varieties\x01",
            "It looks like it was true.\x02\x03",
            "#11509FWhew, this is\x01",
            "I should have brought a fishing rod.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#5PLecter …\x01",
            "What are you doing in such a place?\x02",
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
            "Oops, there is no pole\x01",
            "It seems that prey has taken place.\x02\x03",
            "Five prey with two arms and legs ……\x01",
            "Well, are you doing well as a fisherman?\x02",
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
        "#10105F#5PBecome\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#5PWe caught fishing and came here,\x01",
            "I said that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#11509F#11PHaha, you're saying so\x01",
            "I am planning to do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5P(… at the pace of this person\x01",
            "You can not get on. )\x02\x03",
            "#00001F…… Lecter,\x01",
            "I will change my question.\x02\x03",
            "I put the \"red constellation\" into the crossbell\x01",
            "You are a human of the Imperial Army Information Bureau,\x01",
            "What are you doing in such a place?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "#11509F#11PHaha, it came to say.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#5PHuh, well for you\x01",
            "This is about as straight\x01",
            "Not exactly right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 500)

    ChrTalk(
        0xFE,
        (
            "#11504F#12PWell, okay.\x01",
            "I will answer the question.\x02\x03",
            "#11500FI came here as you can see\x01",
            "It is where to relax.\x02\x03",
            "#11506FNo matter how much I, that osan 's\x01",
            "I'm getting tired of being just amulets.\x02",
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
            "#00005F#5PO, Osassin ……\x01",
            "Do you mean Osborne 's Excellency?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#5PI was worried … ….\x01",
            "After all you are the aides of the Prime Minister or your aides or something\x01",
            "Can we think about it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#11502F#4PKuku, I do not know.\x01",
            "At least such a great monkey\x01",
            "I do not even remember once I told you.\x02\x03",
            "#11504F…… Well,\x01",
            "The break time is over soon\x01",
            "I will return to the place of Osassu.\x02\x03",
            "#11500FSounds good,\x01",
            "At best do your best for your work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105F#5PAA no……! Is it?\x02",
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x2D, 0x1F4)

    def lambda_469F():

        label("loc_469F")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_469F")

    QueueWorkItem2(0x101, 2, lambda_469F)

    def lambda_46B1():

        label("loc_46B1")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_46B1")

    QueueWorkItem2(0x102, 2, lambda_46B1)

    def lambda_46C3():

        label("loc_46C3")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_46C3")

    QueueWorkItem2(0x104, 2, lambda_46C3)

    def lambda_46D5():

        label("loc_46D5")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_46D5")

    QueueWorkItem2(0x109, 2, lambda_46D5)

    def lambda_46E7():

        label("loc_46E7")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_46E7")

    QueueWorkItem2(0x105, 2, lambda_46E7)
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
            "#00306F#5PWhew.\x01",
            "It was torn down … …\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 0)), scpexpr(EXPR_END)), "loc_4782")
    Call(0, 15)

    label("loc_4782")

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

    # Function_14_3EAB end

    def Function_15_47C7(): pass

    label("Function_15_47C7")

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
            "#00003F#6PMr. Lecta, Ms. Kirika ……\x02\x03",
            "Empire and republican intelligence agents,\x01",
            "At similar timing\x01",
            "I was out in the city.\x02\x03",
            "#00001F…… Everyone, what do you think?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_48A3():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_48A3)
    Sleep(50)

    def lambda_48B3():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_48B3)
    Sleep(50)

    def lambda_48C3():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_48C3)
    Sleep(50)

    def lambda_48D3():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_48D3)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x109,
        "#10103F#6P…… It smells like a queen.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#6PHuh, if you were like this\x01",
            "Do you want to track them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#6PI guess it is also difficult.\x02\x03",
            "#00103FNeither of us gets to you\x01",
            "It was kind of like I knew … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6P… … For Dudley\x01",
            "Would you like to go report it?\x02\x03",
            "#00000FTogether with the information of the investigation department\x01",
            "You may understand something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105F#6POh … it looks good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300F#6POkay, if you decide so\x01",
            "Try going to the police headquarters.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0xA3, 0x1, 0xC)
    Return()

    # Function_15_47C7 end

    def Function_16_4AC2(): pass

    label("Function_16_4AC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 6)), scpexpr(EXPR_END)), "loc_4B1F")
    EventBegin(0x2)
    ClearMapFlags(0x20)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It is a mansion of Campbell Rep. Republic.\x01",
            "Especially I do not have any business to visit.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Jump("loc_4F3E")

    label("loc_4B1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E8B")
    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        "#00005FThis place is certain ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FI am summarizing republican senators\x01",
            "It is the mansion of Rep. Campbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FTo be sure, in the example cult\x01",
            "Congressmen who were involved\x01",
            "It was a story that I was down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FYeah, to Campbell Rep.\x01",
            "Such a connection\x01",
            "It seems that it was not confirmed.\x02\x03",
            "#00100FThere seems to be a relationship with \"black moon\"\x01",
            "But for now\x01",
            "It's not illegal … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FBeing a person who smells cute\x01",
            "That's correct.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4E0B")

    ChrTalk(
        0x101,
        (
            "#00000FBy the way, Erie is certain\x01",
            "With Campbell's daughter\x01",
            "You know him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FAbout Cala.\x01",
            "Well, Sunday school was the same.\x02\x03",
            "#00104FIn that sense, her father\x01",
            "To not being connected to the cult\x01",
            "I was really relieved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108FI agree……\x01",
            "I do not know that my acquaintance's father is such a person\x01",
            "I do not want to think too much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E0B")


    ChrTalk(
        0x101,
        (
            "#00000FWell, anyway … …\x01",
            "I do not have any errands right now and I will visit\x01",
            "Let's stop it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYeah, well.\x01",
            "Shall we go.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12F, 6)
    TalkEnd(0xFF)
    Jump("loc_4F3E")

    label("loc_4E8B")

    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#00000FThis place is certain ……\x01",
            "I am summarizing republican senators\x01",
            "It was a mansion of Rep. Campbell.\x02\x03",
            "I do not have any errands right now and I will visit\x01",
            "Let's stop it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYeah, well.\x01",
            "let's go.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12F, 6)
    TalkEnd(0xFF)

    label("loc_4F3E")

    Return()

    # Function_16_4AC2 end

    def Function_17_4F3F(): pass

    label("Function_17_4F3F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F6D")
    Call(0, 39)
    Return()

    label("loc_4F6D")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a lock on the door.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_17_4F3F end

    def Function_18_4FA4(): pass

    label("Function_18_4FA4")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a lock on the door.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_18_4FA4 end

    def Function_19_4FD9(): pass

    label("Function_19_4FD9")

    EventBegin(0x1)
    Sound(2094, 255, 100, 0)

    ChrTalk(
        0x101,
        "#0000FI'm going to catch you here.\x02",
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
            "Do you fish?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "To fish\x01",      # 0
            "quit\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50A8")
    OP_E2(0x2)
    MiniGame(0x6, 0x2, 0xFFFFEAA2, 0xFFFFE890, 0xFFFF5DB2, 0x10E, 0xFFFFD90E, 0xFFFFE69C, 0xFFFF5C36)

    label("loc_50A8")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_19_4FD9 end

    def Function_20_50AD(): pass

    label("Function_20_50AD")

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
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_51B8")
    SetChrFlags(0x9, 0x8000)
    EndChrThread(0x9, 0xFF)
    SetChrPos(0x9, -5000, 0, -5000, 180)

    def lambda_51A8():
        OP_9B(0x0, 0xFE, 0x0, 0x7530, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_51A8)

    label("loc_51B8")

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

    # Function_20_50AD end

    def Function_21_5239(): pass

    label("Function_21_5239")

    SetChrPos(0xFE, 25550, 0, -4600, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -6000, 0, -4600)
    OP_9F(0x1, -15000, 0, -3100)
    OP_9F(0x1, -16000, 0, 7900)
    OP_9F(0x2, 0xFE, 5500, 0x6)
    Return()

    # Function_21_5239 end

    def Function_22_5282(): pass

    label("Function_22_5282")

    Sleep(2000)
    OP_95(0xFE, 0, 0, -5600, 2000, 0x1)
    OP_95(0xFE, -14000, 0, -5600, 2000, 0x1)
    Return()

    # Function_22_5282 end

    def Function_23_52AE(): pass

    label("Function_23_52AE")

    Sound(468, 2, 100, 0)
    Sound(458, 0, 100, 0)
    Sleep(4500)
    Sound(494, 0, 70, 0)
    Return()

    # Function_23_52AE end

    def Function_24_52C4(): pass

    label("Function_24_52C4")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5568")
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

    def lambda_53F2():
        OP_97(0x101, 0xFFFFF830, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_53F2)
    Sleep(50)

    def lambda_540F():
        OP_97(0x102, 0xFFFFF830, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_540F)
    Sleep(50)

    def lambda_542C():
        OP_97(0x109, 0xFFFFF830, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_542C)
    Sleep(50)

    def lambda_5449():
        OP_97(0x105, 0xFFFFF830, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5449)
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
        "#00005FIs this sound …?\x02",
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
    Jump("loc_5748")

    label("loc_5568")

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

    def lambda_561B():
        OP_97(0x101, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_561B)
    Sleep(50)

    def lambda_5638():
        OP_97(0x102, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5638)
    Sleep(50)

    def lambda_5655():
        OP_97(0x109, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5655)
    Sleep(50)

    def lambda_5672():
        OP_97(0x105, 0x0, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5672)
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
        "#00005FIs this sound …?\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-14390, 500, 10820, 0)
    MoveCamera(70, 35, 0, 0)
    OP_6E(620, 0)
    SetCameraDistance(23150, 0)
    OP_0D()

    label("loc_5748")

    OP_68(-13920, 500, -3320, 1000)
    MoveCamera(31, 31, 0, 1000)
    OP_6E(620, 1000)
    SetCameraDistance(20000, 1000)
    BeginChrThread(0x13, 1, 0, 25)
    BeginChrThread(0x17, 1, 0, 26)

    NpcTalk(
        0x12,
        "Voice of a young man",
        "#10AIreyouhoo!\x02",
    )

    CloseMessageWindow()
    OP_68(8360, 1450, -3280, 1500)
    MoveCamera(39, 29, 0, 1500)

    NpcTalk(
        0x12,
        "Voice of a young man",
        "#5AHaha, it's great!\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    def lambda_57EF():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_57EF)
    Sleep(50)

    def lambda_57FF():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_57FF)
    Sleep(50)

    def lambda_580F():
        OP_93(0x109, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_580F)
    Sleep(50)

    def lambda_581F():
        OP_93(0x105, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_581F)
    OP_6F(0x79)
    OP_0D()
    Sleep(1500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_58C1")
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
    Jump("loc_59EE")

    label("loc_58C1")

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

    def lambda_593E():
        OP_95(0x102, 4970, 0, -5120, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_593E)
    Sleep(100)

    def lambda_595B():
        OP_95(0x101, 3840, 0, -3970, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_595B)
    Sleep(100)

    def lambda_5978():
        OP_95(0x109, 6070, 0, -3420, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5978)
    Sleep(100)

    def lambda_5995():
        OP_95(0x105, 7190, 0, -4250, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5995)
    WaitChrThread(0x109, 1)

    def lambda_59B3():
        OP_93(0x109, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_59B3)
    WaitChrThread(0x105, 1)

    def lambda_59C4():
        OP_93(0x105, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_59C4)
    WaitChrThread(0x101, 1)

    def lambda_59D5():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_59D5)
    WaitChrThread(0x102, 1)

    def lambda_59E6():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_59E6)

    label("loc_59EE")


    ChrTalk(
        0x101,
        (
            "#00005FWell, what is it …?\x01",
            "Extravagant Speed\x01",
            "I guess it was out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FObviously it is a speed breaking …\x02\x03",
            "If you do such a driving\x01",
            "The power car is poor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FDriving car that drives dangerously … …\x01",
            "Recently, in the city well\x01",
            "You seem to have been witnessed.\x02\x03",
            "#00103FIn various places\x01",
            "It seems to annoy you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10305FWell, I see.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(50)

    ChrTalk(
        0x105,
        (
            "#10300FAs the Special Affairs Support Division\x01",
            "What should I do?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5B76():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5B76)
    Sleep(50)

    def lambda_5B86():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5B86)
    Sleep(50)

    def lambda_5B96():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5B96)
    Sleep(50)

    ChrTalk(
        0x101,
        (
            "#00003Fof course,\x01",
            "To overlook\x01",
            "I will not go.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C69")
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
            "◆ Kate patrol in the port area? (for test)\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【speaking】\x01",        # 0
            "[I'm not talking]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_5C69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13E, 4)), scpexpr(EXPR_END)), "loc_5D1D")

    ChrTalk(
        0x101,
        (
            "#00004FCertainly, the car headed\x01",
            "In the entertainment area\x01",
            "There was Kate senpai.\x02\x03",
            "#00000FContact with Enigma\x01",
            "Let's consult.\x02\x03",
            "If it were such a case\x01",
            "The wide area crime prevention section is supposed to be suitable.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DB8")

    label("loc_5D1D")


    ChrTalk(
        0x101,
        (
            "#00003F…… of the wide area crime prevention division\x01",
            "To Kate Senpai\x01",
            "Let's consult.\x02\x03",
            "#00000FAs long as you are a senior\x01",
            "It may be moving to cope\x01",
            "I do not think so.\x02\x03",
            "Contact with Enigma\x01",
            "Let's consult.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DB8")

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
    SetChrName("Kate's voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "── Yes, here\x01",
            "It is Kate patrol of the wide area crime prevention division.\x02",
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
            "#00000FKate-senpai, thank you.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Kate's voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Oh, Lloyd.\x01",
            "I wonder what happened?\x02",
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
            "#00003FUh, actually to a senior\x01",
            "I have something I'd like to consult about ……\x02",
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
            "Lloyd said\x01",
            "About the case of runaway vehicles\x01",
            "I explained it all.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Kate's voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Oh, Lloyd guys as well\x01",
            "You witnessed.\x02\x03",
            "Well, it's tough …\x01",
            "Maybe you should cooperate.\x02",
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
            "#00005FCooperation ……?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Kate's voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "If you have time,\x01",
            "A bit for me\x01",
            "I wonder if you can come.\x02\x03",
            "In the vicinity of the hotel of the entertainment district\x01",
            "I'm waiting.\x02",
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
            "#00000FYes.\x01",
            "OK.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Kate's voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Well then, see you later.\x02",
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
        "#00100F…… What is Kate?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, somehow for us\x01",
            "There seems to be something that you want cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FAre you cooperating with the wide area crime prevention division?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309FStop power guide car with force!\x01",
            "… or something like being told.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FSure, that's\x01",
            "It's too dangerous …\x02\x03",
            "#00000FAnyway, at the hotel of the entertainment district\x01",
            "Let's go and try.\x02",
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6310")
    SetChrPos(0x0, -320, 0, -25290, 0)
    Jump("loc_6321")

    label("loc_6310")

    SetChrPos(0x0, 3840, 0, -3970, 90)

    label("loc_6321")

    EventEnd(0x5)
    Return()

    # Function_24_52C4 end

    def Function_25_6324(): pass

    label("Function_25_6324")

    SetChrPos(0x13, -15860, 300, 20000, 180)
    OP_96(0xFE, 0xFFFFBD7A, 0x0, 0xFFFFF8B2, 0x4E20, 0x0)
    OP_9F(0x0, 0x13)
    OP_9F(0x1, -16800, 0, -2530)
    OP_9F(0x1, -14190, 0, -5130)
    OP_9F(0x1, -12700, 0, -5370)
    OP_9F(0x2, 0x13, 11000, 0x6)
    OP_96(0xFE, 0x767A, 0x0, 0xFFFFE85E, 0x4E20, 0x0)
    Return()

    # Function_25_6324 end

    def Function_26_6395(): pass

    label("Function_26_6395")

    Sound(486, 0, 100, 0)
    Sleep(1000)
    Sound(487, 0, 100, 0)
    Sound(494, 0, 100, 0)
    Return()

    # Function_26_6395 end

    def Function_27_63AB(): pass

    label("Function_27_63AB")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6484")
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
            "#1K◆ \"Crackdown on Runaway Vehicles\"? (for test)\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【It does not change】\x01",        # 0
            "【Are doing】\x01",        # 1
            "【not doing】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6470")
    OP_29(0x69, 0x4, 0x10)
    Jump("loc_6484")

    label("loc_6470")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6484")
    OP_29(0x69, 0x3, 0x10)

    label("loc_6484")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_653E")

    ChrTalk(
        0x101,
        (
            "#00005Fthis is……\x01",
            "Yesterday's bad youth\x01",
            "Whether you are driving a driving car.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FWhy in a place like this …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FI do not know but …\x01",
            "I feel something unpleasant.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_665F")

    label("loc_653E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x69, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_65A6")

    ChrTalk(
        0x101,
        "#00006FThat guy with three people,?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHugh, really.\x01",
            "It is a disproportionate thing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_665F")

    label("loc_65A6")


    ChrTalk(
        0x101,
        (
            "#00005Fthis is……\x01",
            "Something's awesome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FOh, quite\x01",
            "It's a pretty design.\x02\x03",
            "#10304FWell, this kind of thing\x01",
            "If it is not in equilibrium with the owner\x01",
            "It's only comical.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_665F")

    TalkEnd(0xFF)
    Return()

    # Function_27_63AB end

    def Function_28_6663(): pass

    label("Function_28_6663")

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
            "#12P#00000FNext to McDowell's residence ……\x01",
            "There is no mistake here.\x02",
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
            "#12P#00000FExcuse me,\x01",
            "Is anyone coming?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        "#12P#00003FIt is useless, there is no reaction.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00105FIs the key locked up?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)

    ChrTalk(
        0x101,
        (
            "#5P#00001FNo, that is ……\x01",
            "It seems to be open.\x02\x03",
            "#00003FThings like talking from inside\x01",
            "I can hear it ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10105FCrazy about conversation\x01",
            "Did not notice?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FWell, if you are open anyway\x01",
            "Is not it okay to enter arbitrarily?\x02\x03",
            "#10302FAlright, you see, we\x01",
            "It is a fine police officer.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#5P#00006FBeing a police officer without permission\x01",
            "I do not mean I can enter … …\x02\x03",
            "#00000FWell, anyway\x01",
            "I can not leave it alone,\x01",
            "Why do not you go inside and try out a voice.\x02",
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

    # Function_28_6663 end

    def Function_29_69FF(): pass

    label("Function_29_69FF")

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
            "#12P#10302FWhew, just a little\x01",
            "You seem to be too floating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00106FYeah, it's exactly painting\x01",
            "It was feeling like a son of Dora.\x02\x03",
            "#00108FEven so,\x01",
            "This house is such a\x01",
            "I thought it was going in the hand ……\x02\x03",
            "#00103FIn this case, Mr. Bond also\x01",
            "I can not get it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10101FBut, especially in the contract\x01",
            "It seems there is no illegality either … ….\x02\x03",
            "#10106FIn that regard, even one of the complaints\x01",
            "It is a regrettable place to not say it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00003FOh … but, for now\x01",
            "I do not think we should leave it alone.\x02\x03",
            "#00000F……Anyways,\x01",
            "The residential area survey is now complete.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x6A, 0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DA6")
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
            "◆ \"What is the investigation situation? (For testing)\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【It does not change】\x01",                    # 0
            "【Not visiting New Bond House】\x01",      # 1
            "【There is still a rest】\x01",                # 2
            "【Confirmation of 6 places ended】\x01",        # 3
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
        (0, "loc_6D77"),
        (1, "loc_6D7C"),
        (2, "loc_6D84"),
        (3, "loc_6D95"),
        (SWITCH_DEFAULT, "loc_6DA6"),
    )


    label("loc_6D77")

    Jump("loc_6DA6")

    label("loc_6D7C")

    ClearScenarioFlags(0x131, 7)
    Jump("loc_6DA6")

    label("loc_6D84")

    SetScenarioFlags(0x131, 7)
    ClearScenarioFlags(0x132, 0)
    ClearScenarioFlags(0x132, 1)
    ClearScenarioFlags(0x132, 2)
    Jump("loc_6DA6")

    label("loc_6D95")

    SetScenarioFlags(0x131, 7)
    SetScenarioFlags(0x132, 0)
    SetScenarioFlags(0x132, 1)
    SetScenarioFlags(0x132, 2)
    Jump("loc_6DA6")

    label("loc_6DA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E92")

    ChrTalk(
        0x102,
        (
            "#11P#00100FHey, Lloyd.\x01",
            "Will not you go to Bond next time?\x02\x03",
            "Regarding the circumstances of moving,\x01",
            "I want to hear the detailed situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00003FOh, it is certainly worrying.\x02\x03",
            "#00000FWell then, the next street is East\x01",
            "Would you visit Bond's place?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F44")

    label("loc_6E92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6EF2")

    ChrTalk(
        0x101,
        (
            "#5P#00000FAlright, then continue\x01",
            "We will respond to the rest of the survey.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F44")

    label("loc_6EF2")


    ChrTalk(
        0x101,
        (
            "#5P#00000FOK, this is the end of the investigation.\x02\x03",
            "Let's return to the municipal hall.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x6A, 0x1, 0x6)

    label("loc_6F44")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_65(0x2, 0x1)
    SetMapObjFlags(0xB, 0x10)
    SetScenarioFlags(0x131, 6)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -17150, -6000, -18250, 180)
    EventEnd(0x5)
    Return()

    # Function_29_69FF end

    def Function_30_6F74(): pass

    label("Function_30_6F74")

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

    def lambda_7041():
        OP_95(0xFE, -6050, -6000, -22480, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7041)
    Sleep(50)

    def lambda_705E():
        OP_95(0xFE, -4650, -6000, -22780, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_705E)
    Sleep(50)

    def lambda_707B():
        OP_95(0xFE, -5250, -6000, -21350, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_707B)
    Sleep(50)

    def lambda_7098():
        OP_95(0xFE, -3850, -6000, -21480, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7098)
    Sleep(50)

    def lambda_70B5():
        OP_95(0xFE, -6850, -6000, -21200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_70B5)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x1A3,
        "#04602FOh, thank you!\x02",
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

    def lambda_717F():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_717F)
    Sleep(50)

    def lambda_718F():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_718F)
    Sleep(50)

    def lambda_719F():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_719F)
    Sleep(50)

    def lambda_71AF():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_71AF)
    Sleep(50)

    def lambda_71BF():
        TurnDirection(0xFE, 0x1A3, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_71BF)
    Sleep(1000)
    Fade(500)
    OP_68(-4050, 1670, -12540, 0)
    MoveCamera(42, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14080, 0)
    OP_0D()

    def lambda_7203():

        label("loc_7203")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_7203")

    QueueWorkItem2(0x101, 1, lambda_7203)

    def lambda_7215():

        label("loc_7215")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_7215")

    QueueWorkItem2(0x104, 1, lambda_7215)

    def lambda_7227():

        label("loc_7227")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_7227")

    QueueWorkItem2(0x102, 1, lambda_7227)

    def lambda_7239():

        label("loc_7239")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_7239")

    QueueWorkItem2(0x109, 1, lambda_7239)

    def lambda_724B():

        label("loc_724B")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_724B")

    QueueWorkItem2(0x105, 1, lambda_724B)
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
            "#5P#04600FBecause it is too late\x01",
            "I started searching for it without permission.\x02\x03",
            "#04609FSo, where is your house?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FOh, this house ……\x02\x03",
            "#00006F…… you accompany you\x01",
            "I did not admit it.\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x1A3, 0x109, 0x3E8, 0x7D0, 0x0)
    Sleep(300)

    ChrTalk(
        0x1A3,
        (
            "#04600FHey, older sister.\x01",
            "Inu and faction, which one?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10105FOh, I?\x02\x03",
            "#10104FEr …\x01",
            "Is it rather a cat school?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#04609FHaha!\x01",
            "It is the same as Charlie.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#6P#00303F(… … Give up.\x01",
            "Whatever you say is in vain. )\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        "#12P#00006F(Ha … it looks like that.\x02",
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

    # Function_30_6F74 end

    def Function_31_751E(): pass

    label("Function_31_751E")

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
        "#12P#04609FWell then let's go next!\x02",
    )

    CloseMessageWindow()
    OP_95(0x1A3, -11560, -6000, -23410, 2000, 0x0)

    ChrTalk(
        0x101,
        "#00006FSomething ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FYeah ….\x01",
            "It was amazing force.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FWith that fine arm, two large guys\x01",
            "I was hanging up … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHuh, it's truly the strongest\x01",
            "Is there a girl 's daughter?\x02\x03",
            "#10302FRandy also told the previous murder\x01",
            "There are places to communicate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00303F…… Together with Senshu.\x02",
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
            "#12P#04606FWhat are you doing?\x02\x03",
            "#04602FI have to go out early.\x01",
            "I will not find it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FOh … … I will go.\x02",
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

    # Function_31_751E end

    def Function_32_7910(): pass

    label("Function_32_7910")


    def lambda_7915():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7915)

    def lambda_7926():
        OP_95(0xFE, -18140, -5600, -17170, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7926)
    WaitChrThread(0x101, 1)
    OP_95(0x101, -17710, -6000, -18270, 2000, 0x0)
    OP_93(0x101, 0x87, 0x1F4)
    Return()

    # Function_32_7910 end

    def Function_33_795B(): pass

    label("Function_33_795B")


    def lambda_7960():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7960)

    def lambda_7971():
        OP_95(0xFE, -18140, -5600, -17170, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7971)
    WaitChrThread(0x102, 1)
    OP_95(0x102, -16500, -6000, -17480, 2000, 0x0)
    OP_93(0x102, 0x87, 0x1F4)
    Return()

    # Function_33_795B end

    def Function_34_79A6(): pass

    label("Function_34_79A6")


    def lambda_79AB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_79AB)

    def lambda_79BC():
        OP_95(0xFE, -17390, -6000, -17900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_79BC)
    WaitChrThread(0x104, 1)
    OP_95(0x104, -15930, -6000, -19920, 2000, 0x0)
    OP_93(0x104, 0x87, 0x1F4)
    Return()

    # Function_34_79A6 end

    def Function_35_79F1(): pass

    label("Function_35_79F1")


    def lambda_79F6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_79F6)

    def lambda_7A07():
        OP_95(0xFE, -17390, -6000, -17900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7A07)
    WaitChrThread(0x109, 1)
    OP_95(0x109, -16510, -6000, -18800, 2000, 0x0)
    OP_93(0x109, 0x87, 0x1F4)
    Return()

    # Function_35_79F1 end

    def Function_36_7A3C(): pass

    label("Function_36_7A3C")


    def lambda_7A41():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_7A41)

    def lambda_7A52():
        OP_95(0xFE, -17390, -6000, -17900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7A52)
    WaitChrThread(0x105, 1)
    OP_95(0x105, -15400, -6000, -18710, 2000, 0x0)
    OP_93(0x105, 0x87, 0x1F4)
    Return()

    # Function_36_7A3C end

    def Function_37_7A87(): pass

    label("Function_37_7A87")


    def lambda_7A8C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A3, 2, lambda_7A8C)

    def lambda_7A9D():
        OP_95(0xFE, -14830, -6000, -20120, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_7A9D)
    WaitChrThread(0x1A3, 1)
    OP_93(0x1A3, 0x13B, 0x1F4)
    Return()

    # Function_37_7A87 end

    def Function_38_7ABE(): pass

    label("Function_38_7ABE")

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
        "#6P#00105FHey, Lloyd … … that!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, maybe Mary.\x01",
            "#6PFinally found out.\x02",
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

    def lambda_7DF7():
        OP_95(0xFE, 19310, 0, -4050, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7DF7)
    Sleep(50)

    def lambda_7E14():
        OP_95(0xFE, 18810, 0, -2750, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_7E14)
    Sleep(50)

    def lambda_7E31():
        OP_95(0xFE, 18610, 0, -5350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7E31)
    Sleep(50)

    def lambda_7E4E():
        OP_95(0xFE, 17110, 0, -2950, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7E4E)
    Sleep(50)

    def lambda_7E6B():
        OP_95(0xFE, 16910, 0, -5250, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7E6B)
    Sleep(50)

    def lambda_7E88():
        OP_95(0xFE, 16309, 0, -4250, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7E88)
    WaitChrThread(0x1A3, 1)
    SetChrChipByIndex(0x1A3, 0xFF)
    SetChrSubChip(0x1A3, 0x0)
    WaitChrThread(0x105, 1)
    OP_6F(0x10)

    ChrTalk(
        0x104,
        "#6P#00306FDid you go?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        "#5P#04602FBut I will catch you later.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FOh, I will follow you soon!\x02",
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

    # Function_38_7ABE end

    def Function_39_7F83(): pass

    label("Function_39_7F83")

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
            "#00005FEr …\x01",
            "The address of the addressee is\x01",
            "I wonder if there is no mistake here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00103FYeah seems that way\x02",
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
            "#00303F…… The sign of people is\x01",
            "Hey maid eee.\x02\x03",
            "#00301FAfter all something\x01",
            "Is not that a mistake?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FPerhaps,\x01",
            "With your neighbor's address\x01",
            "Do you misunderstand me …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FBut this slip ……\x01",
            "I am writing an address\x01",
            "There is no name of the addressee.\x02\x03",
            "#00003FEither way I have to ask\x01",
            "I do not know.\x02",
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
        "#00005FWhat's up Tio\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205FOh, no\x02",
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x105,
        "#10305FOh could it be\x02",
    )

    CloseMessageWindow()

    def lambda_82F9():
        OP_95(0xFE, 17650, 0, -1500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_82F9)
    Sleep(300)

    def lambda_8316():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8316)
    Sleep(100)

    def lambda_8326():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8326)
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
            "#10304FBecause there was a gap between them\x01",
            "I thought it was awful, but …\x02\x03",
            "#10300FWell, for the time being\x01",
            "Let's ask.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FR-right\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F(…?)\x02",
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

    # Function_39_7F83 end

    def Function_40_850A(): pass

    label("Function_40_850A")

    EventBegin(0x1)

    ChrTalk(
        0x1A3,
        (
            "#04605FWell, why am I going to get back?\x01",
            "The target house is in front of you, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, I will head right away.\x02\x03",
            "#00006F(… … as Randy said,\x01",
            "Whatever you say, it looks useless. )\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -5250, -1550, -11110, 180)
    EventEnd(0x4)
    Return()

    # Function_40_850A end

    def Function_41_85CD(): pass

    label("Function_41_85CD")

    EventBegin(0x1)

    ChrTalk(
        0x1A3,
        (
            "#04600FWhat are you doing now?\x01",
            "I will chase Mary soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOh, let 's hurry to the red light district.\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, 6340, 0, -5780, 90)
    EventEnd(0x4)
    Return()

    # Function_41_85CD end

    def Function_42_8642(): pass

    label("Function_42_8642")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a lock on the door.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_42_8642 end

    SaveToFile()

Try(main)
