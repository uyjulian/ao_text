from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c1400.bin",                # FileName
        "c1400",                    # MapName
        "c1400",                    # Location
        0x002E,                     # MapIndex
        "ed7101",
        0x00002000,                 # Flags
        ("c1400", "c1000_1", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 46, 0, 4, 0, 5],
    )

    BuildStringList((
        "c1400",                  # 0
        "Dino",               # 1
        "Paola Lady",           # 2
        "Van",                 # 3
        "Ruze",                   # 4
        "Canon",                 # 5
        "Huey",               # 6
        "Slash",             # 7
        "Keen",               # 8
        "Besse",                 # 9
        "Abbas",               # 10
        "Sister · Lease",       # 11
        "Bacchus",               # 12
        "Lima",                   # 13
        "Marsun",               # 14
        "Policeman",                   # 15
        "Wald",               # 16
        "Olivier",               # 17
        "Jingo",                 # 18
        "bc1400",                 # 19
        "Central square",               # 20
        "Nishi dori",                 # 21
        "Administrative district",                 # 22
        "Residential area",                 # 23
        "Entertainment district",                 # 24
        "East Street",                 # 25
        "old Town",                 # 26
        "Harbor district",                 # 27
        "IBC",                 # 28
        "Beside the station",               # 29
        "Back street",                 # 30
        "Ursula interchange",           # 31
        "East Crossbell Highway",       # 32
        "West Crossbell Highway",       # 33
        "Mainz Mountain Road",           # 34
        "Orchis Tower",         # 35
    ))

    ATBonus("ATBonus_6E8", 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_7D8", 8, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_7DC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7E0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7E4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7E8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7EC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7F0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7F4", 0, 0, 180)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_7F8", 0x008A, 0, 6, 0, 0, 255, 0, 0, "bc1400", 0x00000000, 100, 0, 0, 0,
        (
            ("ms02102.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_7D8", "MonsterBattlePostion_7D8", "ed7452", "ed7453", "ATBonus_6E8"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch06800.itc",                   # 00
        "chr/ch23302.itc",                   # 01
        "chr/ch23000.itc",                   # 02
        "chr/ch24700.itc",                   # 03
        "chr/ch23800.itc",                   # 04
        "chr/ch31700.itc",                   # 05
        "chr/ch30800.itc",                   # 06
        "chr/ch31800.itc",                   # 07
        "chr/ch14000.itc",                   # 08
        "chr/ch23400.itc",                   # 09
        "chr/ch06700.itc",                   # 0A
        "chr/ch30900.itc",                   # 0B
        "chr/ch20700.itc",                   # 0C
        "chr/ch26200.itc",                   # 0D
        "chr/ch30000.itc",                   # 0E
    ))

    DeclNpc(44880,   4294964796, 4294947206, 225,  261,  0x0, 0,   0,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(15449,   100,     4294967277, 270,  261,  0x0, 0,   1,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(9640,    0,       850,     180,  261,  0x0, 0,   2,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(10279,   0,       4294966746, 315,  261,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(34080,   4294960796, 4294929026, 45,   261,  0x0, 0,   4,   0,   0,   1,   0,   11,  255,  0)
    DeclNpc(2369,    0,       4294965086, 315,  389,  0x0, 0,   5,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(3700,    0,       4294966226, 315,  389,  0x0, 0,   6,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   7,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   0,   0,   0,   13,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   10,  0,   0,   0,   0,   14,  255,  0)
    DeclNpc(11460,   0,       4294960387, 135,  389,  0x0, 0,   8,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(32799,   4294960796, 4294930346, 315,  389,  0x0, 0,   9,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(10270,   3500,    11050,   135,  389,  0x0, 0,   12,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(9609,    3500,    13869,   135,  389,  0x0, 0,   13,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(4940,    0,       5250,    180,  389,  0x0, 0,   14,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 25,  46.5,                  -22.5,                 -3.0,                  20.25,                 [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.2222222238779068,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -23.25,                5.0,                   0.6000000238418579,    1.0])
    DeclEvent(0x0040, 0, 27,  1.6399999856948853,    0.0,                   -1.0,                  4.0,                   [0.25,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.4099999964237213,   -0.0,                  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 33,  1.899999976158142,     10.0,                  -1.0,                  100.0,                 [0.19999998807907104,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -0.37999996542930603,  -2.5,                  0.19999998807907104,   1.0])
    DeclEvent(0x0000, 0, 44,  10.039999961853027,    -37.459999084472656,   -6.409999847412109,    400.0,                 [0.19999998807907104,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -2.007999897003174,    4.682499885559082,     1.281999945640564,     1.0])

    DeclActor(47720,   4294966196, 4294934136, 1200,    47720,   100,     4294934136, 0x007C, 0,  6,  0x0000)
    DeclActor(34830,   2450,    4294947516, 1500,    34830,   3950,    4294947516, 0x007C, 0,  53, 0x0000)

    PlaceName(-110.69000244140625, 0.0, 106.94999694824219, 0x0000, 0x0000, "Central square")
    PlaceName(-186.3000030517578, 0.0, 112.12999725341797, 0x0000, 0x0000, "Nishi dori")
    PlaceName(-79.63999938964844, 0.0, 209.3000030517578, 0x0000, 0x0000, "Administrative district")
    PlaceName(-256.45001220703125, 0.0, 197.8000030517578, 0x0000, 0x0000, "Residential area")
    PlaceName(-172.5, 0.0, 188.60000610351562, 0x0000, 0x0000, "Entertainment district")
    PlaceName(-17.25, 0.0, 80.5, 0x0000, 0x0000, "East Street")
    PlaceName(23.579999923706055, 0.0, 17.25, 0x0000, 0x0000, "old Town")
    PlaceName(14.949999809265137, 0.0, 156.39999389648438, 0x0000, 0x0000, "Harbor district")
    PlaceName(-14.949999809265137, 0.0, 264.5, 0x0000, 0x0000, "IBC")
    PlaceName(-97.75, 0.0, 27.600000381469727, 0x0000, 0x0000, "Beside the station")
    PlaceName(-151.8000030517578, 0.0, 147.1999969482422, 0x0000, 0x0000, "Back street")
    PlaceName(-101.19999694824219, 0.0, -8.050000190734863, 0x0000, 0x0000, "Ursula interchange")
    PlaceName(44.849998474121094, 0.0, 96.5999984741211, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-244.9499969482422, 0.0, 110.4000015258789, 0x0000, 0x0000, "West Crossbell Highway")
    PlaceName(-238.0500030517578, 0.0, 225.39999389648438, 0x0000, 0x0000, "Mainz Mountain Road")
    PlaceName(-88.0, 0.0, 360.0, 0x0000, 0x0000, "Orchis Tower")
    PlaceName(-135.99000549316406, 0.0, 90.8499984741211, 0x0000, 0x0051, "")
    PlaceName(-74.18000030517578, 0.0, 120.75, 0x0000, 0x0054, "")
    PlaceName(-107.80999755859375, 0.0, 81.6500015258789, 0x0000, 0x0057, "")
    PlaceName(-136.85000610351562, 0.0, 124.19999694824219, 0x0000, 0x0053, "")
    PlaceName(-113.27999877929688, 0.0, 151.8000030517578, 0x0000, 0x0053, "")
    PlaceName(-171.63999938964844, 0.0, 118.44999694824219, 0x0000, 0x0053, "")
    PlaceName(-182.85000610351562, 0.0, 142.60000610351562, 0x0000, 0x0053, "")
    PlaceName(-155.25, 0.0, 179.39999389648438, 0x0000, 0x0052, "")
    PlaceName(-149.7899932861328, 0.0, 164.4499969482422, 0x0000, 0x0053, "")
    PlaceName(-139.72999572753906, 0.0, 154.67999267578125, 0x0000, 0x0053, "")
    PlaceName(-106.94999694824219, 0.0, 236.3300018310547, 0x0000, 0x0051, "")
    PlaceName(21.850000381469727, 0.0, 80.5, 0x0000, 0x0052, "")
    PlaceName(2.299999952316284, 0.0, -23.579999923706055, 0x0000, 0x0053, "")
    PlaceName(-12.649999618530273, 0.0, -2.299999952316284, 0x0000, 0x0053, "")

    ChipFrameInfo(2324, 0)                                       # 0

    ScpFunction((
        "Function_0_914",          # 00, 0
        "Function_1_9C4",          # 01, 1
        "Function_2_9EF",          # 02, 2
        "Function_3_AC8",          # 03, 3
        "Function_4_B11",          # 04, 4
        "Function_5_1105",         # 05, 5
        "Function_6_134B",         # 06, 6
        "Function_7_149C",         # 07, 7
        "Function_8_1AAD",         # 08, 8
        "Function_9_2131",         # 09, 9
        "Function_10_2654",        # 0A, 10
        "Function_11_29FE",        # 0B, 11
        "Function_12_33F7",        # 0C, 12
        "Function_13_3468",        # 0D, 13
        "Function_14_3511",        # 0E, 14
        "Function_15_3518",        # 0F, 15
        "Function_16_3522",        # 10, 16
        "Function_17_3A2E",        # 11, 17
        "Function_18_3B26",        # 12, 18
        "Function_19_3C60",        # 13, 19
        "Function_20_3D23",        # 14, 20
        "Function_21_3DE5",        # 15, 21
        "Function_22_3E22",        # 16, 22
        "Function_23_3E68",        # 17, 23
        "Function_24_3F0A",        # 18, 24
        "Function_25_3F5E",        # 19, 25
        "Function_26_4842",        # 1A, 26
        "Function_27_4913",        # 1B, 27
        "Function_28_4914",        # 1C, 28
        "Function_29_4DDA",        # 1D, 29
        "Function_30_4E4D",        # 1E, 30
        "Function_31_4EC0",        # 1F, 31
        "Function_32_4F33",        # 20, 32
        "Function_33_4FA6",        # 21, 33
        "Function_34_63F7",        # 22, 34
        "Function_35_6AD1",        # 23, 35
        "Function_36_6B6E",        # 24, 36
        "Function_37_6BAF",        # 25, 37
        "Function_38_7474",        # 26, 38
        "Function_39_74E0",        # 27, 39
        "Function_40_754C",        # 28, 40
        "Function_41_75B8",        # 29, 41
        "Function_42_75F5",        # 2A, 42
        "Function_43_7632",        # 2B, 43
        "Function_44_766F",        # 2C, 44
        "Function_45_7B82",        # 2D, 45
        "Function_46_8D16",        # 2E, 46
        "Function_47_9EB7",        # 2F, 47
        "Function_48_A5EE",        # 30, 48
        "Function_49_AE11",        # 31, 49
        "Function_50_B2F5",        # 32, 50
        "Function_51_DCEF",        # 33, 51
        "Function_52_DD3F",        # 34, 52
        "Function_53_DD7E",        # 35, 53
    ))


    def Function_0_914(): pass

    label("Function_0_914")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_94C"),
        (1, "loc_958"),
        (2, "loc_964"),
        (3, "loc_970"),
        (4, "loc_97C"),
        (5, "loc_988"),
        (6, "loc_994"),
        (SWITCH_DEFAULT, "loc_9A0"),
    )


    label("loc_94C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_9AC")

    label("loc_958")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_9AC")

    label("loc_964")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_9AC")

    label("loc_970")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_9AC")

    label("loc_97C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_9AC")

    label("loc_988")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_9AC")

    label("loc_994")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9AC")

    label("loc_9A0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9AC")

    label("loc_9AC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9C3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9AC")

    label("loc_9C3")

    Return()

    # Function_0_914 end

    def Function_1_9C4(): pass

    label("Function_1_9C4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9EE")
    OP_94(0xFE, 0x8D04, 0xFFFF6E7E, 0x7800, 0xFFFF612C, 0x3E8)
    Sleep(300)
    Jump("Function_1_9C4")

    label("loc_9EE")

    Return()

    # Function_1_9C4 end

    def Function_2_9EF(): pass

    label("Function_2_9EF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AC7")
    OP_95(0xFE, 5840, 0, -6890, 5000, 0x0)
    OP_95(0xFE, 13450, -1420, -18510, 5000, 0x0)
    OP_95(0xFE, 21750, -2500, -24790, 5000, 0x0)
    OP_95(0xFE, 21750, -6500, -38390, 5000, 0x0)
    OP_95(0xFE, 7790, -6320, -37990, 5000, 0x0)
    OP_95(0xFE, -3730, -3830, -27600, 5000, 0x0)
    OP_95(0xFE, -12250, -3030, -23600, 5000, 0x0)
    OP_95(0xFE, -12250, 0, -12120, 5000, 0x0)
    OP_95(0xFE, -10970, 0, -11360, 5000, 0x0)
    OP_95(0xFE, -5510, 0, -7900, 5000, 0x0)
    Jump("Function_2_9EF")

    label("loc_AC7")

    Return()

    # Function_2_9EF end

    def Function_3_AC8(): pass

    label("Function_3_AC8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B10")
    Sleep(4000)
    OP_95(0xFE, -6960, -3800, -27910, 1000, 0x0)
    Sleep(4000)
    OP_95(0xFE, -13650, -3010, -25240, 1000, 0x0)
    OP_93(0xFE, 0xE1, 0x12C)
    Sleep(1900)
    Jump("Function_3_AC8")

    label("loc_B10")

    Return()

    # Function_3_AC8 end

    def Function_4_B11(): pass

    label("Function_4_B11")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BEE")
    SetChrPos(0x0, 2050, 0, 14590, 180)
    SetChrPos(0x1, 2050, 0, 14590, 180)
    SetChrPos(0x2, 2050, 0, 14590, 180)
    SetChrPos(0x3, 2050, 0, 14590, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B98")
    SetChrPos(0x4, 2050, 0, 14590, 180)
    SetChrPos(0x5, 2050, 0, 14590, 180)
    Jump("loc_BB7")

    label("loc_B98")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BB7")
    SetChrPos(0x4, 2050, 0, 14590, 180)

    label("loc_BB7")

    OP_68(2050, 2000, 14590, 0)
    MoveCamera(45, 34, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(24500, 0)
    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BEE")

    OP_D2(0x7, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_C4F")
    SetChrPos(0xC, 8290, 0, -1190, 45)
    BeginChrThread(0xC, 0, 0, 0)
    SetChrPos(0xA, 9640, 0, 850, 180)
    SetChrPos(0xB, 10280, 0, -550, 315)
    Jump("loc_FE5")

    label("loc_C4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_D83")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CD4")
    SetChrPos(0xF, -200, 0, -8460, 180)
    SetChrPos(0x10, 30390, -2500, -21970, 0)
    SetChrPos(0x15, 6500, 0, 5410, 0)
    SetChrPos(0x14, 5490, 0, 5600, 0)
    Jump("loc_D2E")

    label("loc_CD4")

    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 2520, -10, -4059, 225)
    SetChrPos(0xF, 2120, -10, -6060, 315)
    SetChrPos(0x10, 310, -10, -4250, 90)
    SetChrPos(0x15, 6500, 0, 5410, 0)
    SetChrPos(0x14, 5490, 0, 5600, 0)

    label("loc_D2E")

    SetChrFlags(0x9, 0x80)
    SetChrPos(0xA, 34490, -6500, -37750, 315)
    SetChrPos(0xB, 34490, -6500, -38950, 315)
    SetChrPos(0xC, 34840, -2220, -19610, 0)
    BeginChrThread(0xC, 0, 0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D7E")
    SetChrFlags(0xC, 0x10)

    label("loc_D7E")

    Jump("loc_FE5")

    label("loc_D83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_D96")
    SetChrFlags(0x8, 0x80)
    Jump("loc_FE5")

    label("loc_D96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_DEB")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xA, 0x4)
    ClearChrFlags(0xB, 0x4)
    SetChrPos(0xA, 5840, 0, -6890, 135)
    SetChrPos(0xB, 4760, 0, -5890, 135)
    BeginChrThread(0xA, 0, 0, 2)
    BeginChrThread(0xB, 0, 0, 2)
    Jump("loc_FE5")

    label("loc_DEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_E08")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_FE5")

    label("loc_E08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_E25")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_FE5")

    label("loc_E25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_E38")
    SetChrFlags(0x8, 0x80)
    Jump("loc_FE5")

    label("loc_E38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_E83")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x4)
    ClearChrFlags(0xB, 0x4)
    SetChrPos(0xA, 5840, 0, -6890, 135)
    SetChrPos(0xB, 4760, 0, -5890, 135)
    BeginChrThread(0xA, 0, 0, 2)
    BeginChrThread(0xB, 0, 0, 2)
    Jump("loc_FE5")

    label("loc_E83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_EBE")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EB9")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xE, 0x10)

    label("loc_EB9")

    Jump("loc_FE5")

    label("loc_EBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_F34")
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 11460, 0, -6910, 270)
    SetChrPos(0xA, 9710, 0, -5240, 135)
    SetChrPos(0xB, 9190, 0, -6190, 90)
    SetChrPos(0xC, 8940, 0, -7660, 45)
    BeginChrThread(0xC, 0, 0, 0)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0x16, 0x80)
    Jump("loc_FE5")

    label("loc_F34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_END)), "loc_F7D")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0xA, 14710, 0, -5170, 180)
    SetChrPos(0xB, 14710, 0, -6450, 0)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    Jump("loc_FE5")

    label("loc_F7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_FBC")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0xA, 14710, 0, -5170, 270)
    SetChrPos(0xB, 14710, 0, -6450, 270)
    Jump("loc_FE5")

    label("loc_FBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_FE5")
    SetChrPos(0x8, 47930, -2100, -22760, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FE5")
    SetChrFlags(0xC, 0x10)

    label("loc_FE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_FF9")
    ClearScenarioFlags(0x22, 0)
    Event(0, 28)
    Jump("loc_1036")

    label("loc_FF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_1010")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x1, 2)
    Event(0, 34)
    Jump("loc_1036")

    label("loc_1010")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_1027")
    ClearScenarioFlags(0x22, 2)
    SetScenarioFlags(0x1, 3)
    Event(0, 37)
    Jump("loc_1036")

    label("loc_1027")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_1036")
    ClearScenarioFlags(0x22, 3)
    Event(0, 47)

    label("loc_1036")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1061")
    SetMapFlags(0x10000000)
    Event(1, 0)

    label("loc_1061")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_109E")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_108D")
    Event(0, 45)
    Jump("loc_109E")

    label("loc_108D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_109E")
    Event(0, 46)

    label("loc_109E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10D4")
    SetMapFlags(0x10000000)
    Event(0, 49)

    label("loc_10D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1104")
    SetMapFlags(0x10000000)
    SetScenarioFlags(0x1, 4)
    Event(0, 50)

    label("loc_1104")

    Return()

    # Function_4_B11 end

    def Function_5_1105(): pass

    label("Function_5_1105")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_111F")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x1, 2)
    Jump("loc_114E")

    label("loc_111F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_1139")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x1, 3)
    Jump("loc_114E")

    label("loc_1139")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_114E")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x96), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x1, 4)

    label("loc_114E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_11EF")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x6E, 0x0)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sentaku", 0x0, 0x1)
    Sound(128, 1, 100, 0)

    label("loc_11EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 1)), scpexpr(EXPR_END)), "loc_1207")
    SetMapObjFlags(0x1, 0x10)
    OP_65(0x1, 0x1)
    Jump("loc_120D")

    label("loc_1207")

    ClearMapObjFlags(0x1, 0x10)

    label("loc_120D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1220")
    OP_70(0x7, 0x0)
    Jump("loc_1224")

    label("loc_1220")

    OP_70(0x7, 0x1E)

    label("loc_1224")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    ModifyEventFlags(0, 3, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1246")
    Jump("loc_1298")

    label("loc_1246")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1254")
    Jump("loc_1298")

    label("loc_1254")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_END)), "loc_1267")
    ModifyEventFlags(1, 0, 0x80)
    Jump("loc_1298")

    label("loc_1267")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_127A")
    ModifyEventFlags(1, 0, 0x80)
    Jump("loc_1298")

    label("loc_127A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1298")
    ClearMapObjFlags(0x4, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x138, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1298")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_1298")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12AB")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_12AB")

    SetBarrier(0x0, 0x0, 0x1, 0x0, 11000, -6500, -34510, 4000, 2000, 7000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_131C")
    SetBarrier(0x2, 0x0, 0x1)
    SetMapObjFrame(0xFF, "kusari", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kakusi01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kakusi02", 0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1317")
    ModifyEventFlags(1, 3, 0x80)

    label("loc_1317")

    Jump("loc_134A")

    label("loc_131C")

    SetMapObjFrame(0xFF, "kusari", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kakusi01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kakusi02", 0x0, 0x1)

    label("loc_134A")

    Return()

    # Function_5_1105 end

    def Function_6_134B(): pass

    label("Function_6_134B")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_144B")
    Sound(14, 0, 100, 0)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('珊瑚戒指', 1)"), scpexpr(EXPR_END)), "loc_13D4")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '珊瑚戒指'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EB, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_1446")

    label("loc_13D4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            "In the treasure box",
            scpstr(SCPSTR_CODE_ITEM, '珊瑚戒指'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is contained.\x01",
            "Because my belongings are full,",
            scpstr(SCPSTR_CODE_ITEM, '珊瑚戒指'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I gave up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x7, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1446")

    Jump("loc_1490")

    label("loc_144B")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In the treasure box何も入っていない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_1490")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_134B end

    def Function_7_149C(): pass

    label("Function_7_149C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14BC")
    Call(0, 48)
    Return()

    label("loc_14BC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_16F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1675")

    ChrTalk(
        0xFE,
        "Oh, the Special Affairs Support Division ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FDino君……\x01",
            "Er, other members are … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, oh, thanks.\x01",
            "The most serious seniors, Koki\x01",
            "I managed to regain consciousness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Some other seniors also left the hospital\x01",
            "old Townの方に戻って来ているんだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, to the stance, immediately to the team\x01",
            "I think it is difficult to return.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But if you wait here,\x01",
            "You surely will show your face, do not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108FDino君……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FReally……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18D, 2)
    Jump("loc_16EB")

    label("loc_1675")


    ChrTalk(
        0xFE,
        (
            "Even so ……\x01",
            "From the morning the streets are noisy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard about independence,\x01",
            "I want you to do more quietly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16EB")

    Jump("loc_1AA9")

    label("loc_16F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_16FE")
    Jump("loc_1AA9")

    label("loc_16FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_170C")
    Jump("loc_1AA9")

    label("loc_170C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_171A")
    Jump("loc_1AA9")

    label("loc_171A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1728")
    Jump("loc_1AA9")

    label("loc_1728")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1736")
    Jump("loc_1AA9")

    label("loc_1736")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1744")
    Jump("loc_1AA9")

    label("loc_1744")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1752")
    Jump("loc_1AA9")

    label("loc_1752")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1760")
    Jump("loc_1AA9")

    label("loc_1760")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1A2A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1951")

    ChrTalk(
        0xFE,
        "Oh, the Special Affairs Support Division ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I mean, Wadi.\x01",
            "何でもWaldさん相手に\x01",
            "It's a story that he set a timer ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F…… I will answer if there is a question.\x01",
            "Do you want to hear it from my mouth?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    ChrTalk(
        0xFE,
        "No, no, nothing …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "ヴァ、Waldさんは最強なんだ。\x01",
            "I will never believe it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F（へっ、Waldの野郎、\x01",
            "You are being touched heartily and cancer. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(Oh, for him\x01",
            "I guess it's like a hero. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14C, 6)
    Jump("loc_19B1")

    label("loc_1951")


    ChrTalk(
        0xFE,
        (
            "……always\x01",
            "Waldさんは最強なんだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, yes, I\x01",
            "Do not believe me what to do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19B1")

    Jump("loc_1A25")

    label("loc_19B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19C5")
    Jump("loc_1A25")

    label("loc_19C5")


    ChrTalk(
        0xFE,
        (
            "……Already,\x01",
            "The monkechoro is\x01",
            "You gave it! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Bring it\x01",
            "Slowly quickly\x01",
            "I will go!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A25")

    Jump("loc_1AA9")

    label("loc_1A2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1A38")
    Jump("loc_1AA9")

    label("loc_1A38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1AA9")

    ChrTalk(
        0xFE,
        (
            "…. Once you understand\x01",
            "Go ahead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Waldさんに見つかったら、\x01",
            "I do not know anything about it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AA9")

    TalkEnd(0xFE)
    Return()

    # Function_7_149C end

    def Function_8_1AAD(): pass

    label("Function_8_1AAD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1B3B")

    ChrTalk(
        0xFE,
        (
            "I do not really understand it,\x01",
            "It is in a serious situation\x01",
            "Looks like it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "People who have not left home for a while\x01",
            "Perhaps it might be good.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_212D")

    label("loc_1B3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1B49")
    Jump("loc_212D")

    label("loc_1B49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1BD6")

    ChrTalk(
        0xFE,
        (
            "In the town of Mainz,\x01",
            "A terrible trouble is occurring\x01",
            "That's right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although it says that injured people are out, ……\x01",
            "It is truly sad.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_212D")

    label("loc_1BD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1BE4")
    Jump("loc_212D")

    label("loc_1BE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1C62")

    ChrTalk(
        0xFE,
        (
            "By the way, today is my usual\x01",
            "I do not see the appearance of children.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, to somewhere\x01",
            "I wonder if you went to play.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_212D")

    label("loc_1C62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1CFE")

    ChrTalk(
        0xFE,
        (
            "Anything soon, about independence\x01",
            "It seems that the referendum will be held.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "わたしにはI do not really understand it,\x01",
            "I have to think properly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_212D")

    label("loc_1CFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1E2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DBC")

    ChrTalk(
        0xFE,
        (
            "Recently, I am making noise\x01",
            "There are lots of big news.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I also do not understand\x01",
            "There are many … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway everyone's smile\x01",
            "I do not want to stop it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E2A")

    label("loc_1DBC")


    ChrTalk(
        0xFE,
        (
            "The difficult story to me\x01",
            "I do not know well … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway everyone's smile\x01",
            "I do not want to stop it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E2A")

    Jump("loc_212D")

    label("loc_1E2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1E94")

    ChrTalk(
        0xFE,
        "Hehe, it is a good weather today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The children are doing fine,\x01",
            "It is happy with heart and warmth.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_212D")

    label("loc_1E94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1FC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F29")

    ChrTalk(
        0xFE,
        (
            "The new city hall building\x01",
            "From anywhere in Crossbell City\x01",
            "見えるLooks like it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, if you look closely\x01",
            "I wonder how good you are.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FC0")

    label("loc_1F29")


    ChrTalk(
        0xFE,
        (
            "People who wore a white coat that was the earlier\x01",
            "I wonder if you are a traveling musician.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am far from ears.\x01",
            "I did not hear well,\x01",
            "Hehe, it was a pleasant investigation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FC0")

    Jump("loc_212D")

    label("loc_1FC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_20C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2046")

    ChrTalk(
        0xFE,
        (
            "That sister,\x01",
            "I do not see much of it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, with children\x01",
            "You are good at making friends.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_20BE")

    label("loc_2046")


    ChrTalk(
        0xFE,
        (
            "That sister, with the children\x01",
            "You are good at making friends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, just looking\x01",
            "Something makes my feelings warm.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20BE")

    Jump("loc_212D")

    label("loc_20C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_20D1")
    Jump("loc_212D")

    label("loc_20D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_212D")

    ChrTalk(
        0xFE,
        (
            "Huhu, I will be shy today.\x01",
            "It's nice weather, is not it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I will be doing it.\x02",
    )

    CloseMessageWindow()

    label("loc_212D")

    TalkEnd(0xFE)
    Return()

    # Function_8_1AAD end

    def Function_9_2131(): pass

    label("Function_9_2131")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_21AA")

    ChrTalk(
        0xFE,
        (
            "Hello, something about the street\x01",
            "I'm becoming a big trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Someone may become a war\x01",
            "I told you I do not know.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2650")

    label("loc_21AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_227B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_220A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21D2")
    Call(0, 18)
    Jump("loc_2205")

    label("loc_21D2")


    ChrTalk(
        0xFE,
        (
            "Caja Ha, O yasie's gossip,\x01",
            "It is as thoughtful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2205")

    Jump("loc_2276")

    label("loc_220A")


    ChrTalk(
        0xFE,
        (
            "Hello, today's cooked also\x01",
            "It was delicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If such things are eating out every day,\x01",
            "You can do it all the time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2276")

    Jump("loc_2650")

    label("loc_227B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_22F1")

    ChrTalk(
        0xFE,
        (
            "Something today, the adults\x01",
            "Sawasawa wardrobe cancer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Baboon, my father's father\x01",
            "It is as usual.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2650")

    label("loc_22F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2329")

    ChrTalk(
        0xFE,
        "Caja Ha, a natural showers shower.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2650")

    label("loc_2329")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2337")
    Jump("loc_2650")

    label("loc_2337")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2345")
    Jump("loc_2650")

    label("loc_2345")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_23B5")

    ChrTalk(
        0xFE,
        (
            "Pika!\x01",
            "Rinkja, you gotta get it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "ニシシ……Ruze、\x01",
            "I will eat Niku today, Niku.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2650")

    label("loc_23B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2441")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23FD")

    ChrTalk(
        0xFE,
        (
            "Slack ah ~,\x01",
            "Van様のお通りで〜い！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_243C")

    label("loc_23FD")


    ChrTalk(
        0xFE,
        (
            "Caja Ha, O yasie's gossip,\x01",
            "It is a toko maybe you drank that!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_243C")

    Jump("loc_2650")

    label("loc_2441")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_244F")
    Jump("loc_2650")

    label("loc_244F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2460")
    Call(0, 16)
    Jump("loc_2650")

    label("loc_2460")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_END)), "loc_24BF")

    ChrTalk(
        0xFE,
        (
            "Well ~! even if\x01",
            "It was powerful force!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I did not think I was wronged!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2650")

    label("loc_24BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_252C")

    ChrTalk(
        0xFE,
        "Rain, Shitoshito descending.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If it were all this juice\x01",
            "I have a cold sprinkle in the end.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2650")

    label("loc_252C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2650")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25D8")

    ChrTalk(
        0xFE,
        (
            "Oh, sure\x01",
            "You guys are scared.\x01",
            "Besides, to the bad older brother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even in an incident ……\x01",
            "What? Is it different?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hey, that's a pinch.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2650")

    label("loc_25D8")


    ChrTalk(
        0xFE,
        (
            "Recently, brothers on the defective team,\x01",
            "The trouble came out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Kahaha, fighting spirit\x01",
            "Do not you enter?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2650")

    TalkEnd(0xFE)
    Return()

    # Function_9_2131 end

    def Function_10_2654(): pass

    label("Function_10_2654")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2694")

    ChrTalk(
        0xFE,
        (
            "Couscous……\x01",
            "Is not that a bad idea?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29FA")

    label("loc_2694")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_273B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26EF")

    ChrTalk(
        0xFE,
        (
            "Couscous……\x01",
            "Vanのお父さんって\x01",
            "It is reliable on surprise.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2736")

    label("loc_26EF")


    ChrTalk(
        0xFE,
        (
            "For cooking,\x01",
            "There is one more evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What next will you have to eat?\x02",
    )

    CloseMessageWindow()

    label("loc_2736")

    Jump("loc_29FA")

    label("loc_273B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_278E")

    ChrTalk(
        0xFE,
        (
            "Mainz is the place\x01",
            "It seems to be something Jave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "How do you say ya?\x02",
    )

    CloseMessageWindow()
    Jump("loc_29FA")

    label("loc_278E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_27D5")

    ChrTalk(
        0xFE,
        (
            "Couscous …… somewhere\x01",
            "Do not forget to have a soap.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29FA")

    label("loc_27D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_27E3")
    Jump("loc_29FA")

    label("loc_27E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_27F1")
    Jump("loc_29FA")

    label("loc_27F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2829")

    ChrTalk(
        0xFE,
        "I can eat belly everyday tonight.\x02",
    )

    CloseMessageWindow()
    Jump("loc_29FA")

    label("loc_2829")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_28AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_286C")

    ChrTalk(
        0xFE,
        "キャハハッ、Ruze様もお通りで〜い！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_28A8")

    label("loc_286C")


    ChrTalk(
        0xFE,
        (
            "Couscous……\x01",
            "Vanのお父さん、\x01",
            "I guess you are wearing a monza.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28A8")

    Jump("loc_29FA")

    label("loc_28AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_28BB")
    Jump("loc_29FA")

    label("loc_28BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_28CC")
    Call(0, 16)
    Jump("loc_29FA")

    label("loc_28CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_END)), "loc_293F")

    ChrTalk(
        0xFE,
        (
            "Oh,\x01",
            "Timane shooter\x01",
            "Are you saying that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Couscous……\x01",
            "It sure was powerful force.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29FA")

    label("loc_293F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_29B5")

    ChrTalk(
        0xFE,
        (
            "But that's it. Stomach\x01",
            "It looks like you're getting premature.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Couscous……\x01",
            "Vanのお父さんみたいに。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29FA")

    label("loc_29B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_29FA")

    ChrTalk(
        0xFE,
        (
            "Couscous……\x01",
            "Vanったら本当に\x01",
            "Because I like the noise.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29FA")

    TalkEnd(0xFE)
    Return()

    # Function_10_2654 end

    def Function_11_29FE(): pass

    label("Function_11_29FE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2A46")

    ChrTalk(
        0xFE,
        (
            "Well, it's a war … …\x01",
            "I can not do such a thing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33F3")

    label("loc_2A46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2BAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_END)), "loc_2ABF")

    ChrTalk(
        0xFE,
        (
            "Gasagoso …\x01",
            "Well, this is … no good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well then …\x01",
            "Well, this is too lazy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BA5")

    label("loc_2ABF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B31")

    ChrTalk(
        0xFE,
        "Thank you, Onii-chan.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The waste materials received\x01",
            "I am responsible\x01",
            "I will exchange money.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BA5")

    label("loc_2B31")


    ChrTalk(
        0xFE,
        (
            "Well, stomach too\x01",
            "It's going to be full,\x01",
            "I will do my best again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Onii-chan\x01",
            "You helped me a lot\x01",
            "Thanks.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BA5")

    Jump("loc_33F3")

    label("loc_2BAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2CDD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C49")

    ChrTalk(
        0xFE,
        (
            "Well, due to yesterday's rain\x01",
            "The cobblestone gap is a bit muddy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And a lot of garbage in the gap ……\x01",
            "Huhu, this is when it's time for you to go.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2CD8")

    label("loc_2C49")


    ChrTalk(
        0xFE,
        (
            "Well, this is my secret weapon\x01",
            "\"Affordable wooden stick\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Young man … … so doing this\x01",
            "It scrapes out garbage collected in the gap.\x01",
            "It's pretty fun.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CD8")

    Jump("loc_33F3")

    label("loc_2CDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2CEB")
    Jump("loc_33F3")

    label("loc_2CEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2D7A")

    ChrTalk(
        0xFE,
        (
            "Come quick, oh ….\x01",
            "How about today, this neighborhood\x01",
            "It's shiny.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, there is no end to cleaning,\x01",
            "This sense of accomplishment is great.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33F3")

    label("loc_2D7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2DEF")

    ChrTalk(
        0xFE,
        (
            "Recently, people who are fighting around here\x01",
            "I did not see it much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Huh, it is a very good thing.\x02",
    )

    CloseMessageWindow()
    Jump("loc_33F3")

    label("loc_2DEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2F30")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EB3")

    ChrTalk(
        0xFE,
        (
            "Was it last week, bad\x01",
            "Your older brother hit something on his ear\x01",
            "I was talking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder what he was, what was it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F(Maybe things about Enigma …?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2F2B")

    label("loc_2EB3")


    ChrTalk(
        0xFE,
        (
            "Was it last week, bad\x01",
            "Your older brother hit something on his ear\x01",
            "I was talking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder what he was, what was it?\x02",
    )

    CloseMessageWindow()

    label("loc_2F2B")

    Jump("loc_33F3")

    label("loc_2F30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2FB6")

    ChrTalk(
        0xFE,
        (
            "Orchis Towerって、\x01",
            "You seem to be very tall, are not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard 250 ages ….\x01",
            "How many times is my height?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33F3")

    label("loc_2FB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3144")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30B1")

    ChrTalk(
        0xFE,
        (
            "Anything today from foreign countries\x01",
            "Reporters and elder people\x01",
            "You seem to have come a long way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Someone in this place\x01",
            "I told you not to come,\x01",
            "I do not know such a thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Come quick, oh ….\x01",
            "More than usual\x01",
            "I have to keep it clean.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_313F")

    label("loc_30B1")


    ChrTalk(
        0xFE,
        (
            "Anything today from foreign countries\x01",
            "Eli really people\x01",
            "You seem to have come a long way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Come quick, oh ….\x01",
            "More than usual\x01",
            "I have to keep it clean.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_313F")

    Jump("loc_33F3")

    label("loc_3144")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3155")
    Call(0, 16)
    Jump("loc_33F3")

    label("loc_3155")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3163")
    Jump("loc_33F3")

    label("loc_3163")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_33F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3375")

    ChrTalk(
        0xFE,
        "Please let me know …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As usual\x01",
            "No matter how much you clean\x01",
            "The trash will not go away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300Fおはよう、Canon。\x01",
            "How are you today?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x105, 0)

    ChrTalk(
        0xFE,
        "Oh, Mr. Wasy, good morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, today is\x01",
            "I wonder if there are a lot of trash in the bottle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can not forgive manners,\x01",
            "There are various shapes and it's interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hey, this is something\x01",
            "The middle is kinky and waist\x01",
            "Beautiful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHehe, it sure is a beautiful shape.\x02\x03",
            "#10300FとりあえずCanon、\x01",
            "Be careful with the debris.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yes, thank you.\x02",
    )

    CloseMessageWindow()
    OP_93(0xFE, 0xB4, 0x0)
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x137, 3)
    Jump("loc_33F3")

    label("loc_3375")


    ChrTalk(
        0xFE,
        (
            "Bottles, there are various shapes\x01",
            "It's fun to watch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Look, I'm sorry to bother you\x01",
            "It shines brightly when hit by light.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33F3")

    TalkEnd(0xFE)
    Return()

    # Function_11_29FE end

    def Function_12_33F7(): pass

    label("Function_12_33F7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3464")

    ChrTalk(
        0xFE,
        (
            "Well, after all\x01",
            "Do not use physical strength on site work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But well, well this\x01",
            "It's a good training.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3464")

    label("loc_3464")

    TalkEnd(0xFE)
    Return()

    # Function_12_33F7 end

    def Function_13_3468(): pass

    label("Function_13_3468")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_350D")

    ChrTalk(
        0x10,
        (
            "そ、Even so ……\x01",
            "In this apartment\x01",
            "The destruction is fantastic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Although it was good in a waste apartment,\x01",
            "I thought that there were people inside,\x01",
            "I'm horrified.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_350D")

    label("loc_350D")

    TalkEnd(0xFE)
    Return()

    # Function_13_3468 end

    def Function_14_3511(): pass

    label("Function_14_3511")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_14_3511 end

    def Function_15_3518(): pass

    label("Function_15_3518")

    TalkBegin(0xFE)
    Call(0, 16)
    TalkEnd(0xFE)
    Return()

    # Function_15_3518 end

    def Function_16_3522(): pass

    label("Function_16_3522")

    OP_4B(0x12, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_375E")

    ChrTalk(
        0x12,
        (
            "#04403F\"Yes, let's go to Anna's place. \"\x02\x03",
            "If she is a witch, surely there is Ron\x01",
            "It should be looking for places.\x02\x03",
            "Following the road I came, I headed to Ana's hut.\x01",
            "Suddenly in the ears of the running Mark,\x01",
            "I heard the voice of a shameless beast.\x02",
        )
    )

    CloseMessageWindow()
    Sound(18, 0, 100, 0)
    Sleep(300)

    ChrTalk(
        0xC,
        "It's exciting … so … with that …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Let 's make a daytime early.\x01",
            "You brought me some bread, do not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Couscous……\x01",
            "Let 's eat secretly and eat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105F(Mr. Lease … ….\x01",
            "Today is a business trip to Sunday school\x01",
            "You seem to be coming. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(Are you reading the fairy tale ……\x01",
            "What a warm sight. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14C, 7)
    Jump("loc_3A1D")

    label("loc_375E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3961")

    ChrTalk(
        0x12,
        (
            "#04403FWhen approaching those who fearfully heard a voice,\x01",
            "There …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well, I guess.\x01",
            "Ruze、パンがもらえるまで寝ちまうか。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Couscous … … That's right.\x02",
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x12)

    ChrTalk(
        0x12,
        (
            "#04400FAlthough I forgot to mention it,\x01",
            "At the end of today's lesson\x01",
            "Write down the impression of the book.\x02\x03",
            "#04400FIf you can not write anything\x01",
            "We regard it as non-participation,\x01",
            "I will withdraw lunch, so I will do it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xA)

    ChrTalk(
        0xA,
        (
            "You gotta get serious! Is it?\x01",
            "Such a domineering!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Couscous……\x01",
            "Today's sister is pretty millet.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3A1D")

    label("loc_3961")


    ChrTalk(
        0x12,
        (
            "#04403FWhen approaching those who fearfully heard a voice,\x01",
            "There …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Wait, wait, from the beginning!\x01",
            "Please read from the beginning!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Couscous……\x01",
            "I came to assemble now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Huhu, everyone is a good friend and I enjoy.\x02",
    )

    CloseMessageWindow()

    label("loc_3A1D")

    OP_4C(0x12, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_16_3522 end

    def Function_17_3A2E(): pass

    label("Function_17_3A2E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3ACD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A50")
    Call(0, 18)
    Jump("loc_3AC8")

    label("loc_3A50")


    ChrTalk(
        0xFE,
        (
            "It seems that there are cooks,\x01",
            "It is not unusual work from daytime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Let me finish quickly,\x01",
            "I'm going to have a drink quickly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AC8")

    Jump("loc_3B22")

    label("loc_3ACD")


    ChrTalk(
        0xFE,
        (
            "Trust me, the sun is\x01",
            "It's dazzling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It is poisonous for a night type man.\x02",
    )

    CloseMessageWindow()

    label("loc_3B22")

    TalkEnd(0xFE)
    Return()

    # Function_17_3A2E end

    def Function_18_3B26(): pass

    label("Function_18_3B26")

    OP_4B(0xA, 0xFF)
    OP_4B(0x13, 0xFF)
    TurnDirection(0xA, 0x0, 0)

    ChrTalk(
        0xA,
        (
            "Caja Ha, O yasie's gossip,\x01",
            "I am unusually working from daytime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Whatever you do with Hooko,\x01",
            "You kick out from the apartment.\x01",
            "She seems to have told the landlord.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x13, 0xA, 0)

    ChrTalk(
        0x13,
        (
            "おらぁ、Van。\x01",
            "You are not talking about extra things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "Shut up and help your work.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    SetScenarioFlags(0x0, 5)
    OP_93(0xA, 0x13B, 0x0)
    OP_93(0x13, 0x13B, 0x0)
    OP_4C(0xA, 0xFF)
    OP_4C(0x13, 0xFF)
    Return()

    # Function_18_3B26 end

    def Function_19_3C60(): pass

    label("Function_19_3C60")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CC2")

    ChrTalk(
        0xFE,
        (
            "Well, today as well.\x01",
            "Would you like me to pick it up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "First, measure the dimensions, and …\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D1F")

    label("loc_3CC2")


    ChrTalk(
        0xFE,
        (
            "Well, I got a bit late but\x01",
            "I finally breathed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yoshito … I will try my best from the afternoon too!\x02",
    )

    CloseMessageWindow()

    label("loc_3D1F")

    TalkEnd(0xFE)
    Return()

    # Function_19_3C60 end

    def Function_20_3D23(): pass

    label("Function_20_3D23")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D80")

    ChrTalk(
        0xFE,
        "Dad, I work for everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Very cool, ♪\x02",
    )

    CloseMessageWindow()
    Jump("loc_3DE1")

    label("loc_3D80")

    SetChrName("Lima")

    ChrTalk(
        0x14,
        "Dad, this juice delicious ー ー ー ー ー ー ー.\x02",
    )

    CloseMessageWindow()
    SetChrName("Marsun")

    ChrTalk(
        0x15,
        (
            "Oh, it is true.\x01",
            "Daddy also gains power.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DE1")

    TalkEnd(0xFE)
    Return()

    # Function_20_3D23 end

    def Function_21_3DE5(): pass

    label("Function_21_3DE5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DFA")
    Call(0, 23)
    Jump("loc_3E1E")

    label("loc_3DFA")


    ChrTalk(
        0xFE,
        "I wonder what kind of thing it looks like ….\x02",
    )

    CloseMessageWindow()

    label("loc_3E1E")

    TalkEnd(0xFE)
    Return()

    # Function_21_3DE5 end

    def Function_22_3E22(): pass

    label("Function_22_3E22")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E37")
    Call(0, 23)
    Jump("loc_3E64")

    label("loc_3E37")


    ChrTalk(
        0xFE,
        (
            "Waldさんも\x01",
            "You should not miss seeing … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E64")

    TalkEnd(0xFE)
    Return()

    # Function_22_3E22 end

    def Function_23_3E68(): pass

    label("Function_23_3E68")

    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)

    ChrTalk(
        0xD,
        "Orchis Towerっつったっけ？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Indeed,\x01",
            "I will make a monstrous hey mon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Hiha, certainly.\x01",
            "Try bungee from the rooftop!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_23_3E68 end

    def Function_24_3F0A(): pass

    label("Function_24_3F0A")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "さてと、これからold Townを\x01",
            "It's a patrolling place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…… Where do you turn from?\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_3F0A end

    def Function_25_3F5E(): pass

    label("Function_25_3F5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3F6B")
    Call(0, 26)
    Return()

    label("loc_3F6B")

    EventBegin(0x0)
    Fade(500)
    OP_68(44710, -500, -23880, 0)
    MoveCamera(49, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    OP_4B(0x8, 0xFF)
    SetChrPos(0x101, 45140, -2500, -22290, 90)
    SetChrPos(0x102, 45040, -2500, -24290, 90)
    SetChrPos(0x109, 43640, -2500, -22090, 90)
    SetChrPos(0x105, 43950, -2500, -23790, 90)
    TurnDirection(0x101, 0x8, 0)
    TurnDirection(0x102, 0x8, 0)
    TurnDirection(0x109, 0x8, 0)
    TurnDirection(0x105, 0x8, 0)
    OP_0D()
    Sleep(300)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#11PYou guys……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FHello.\x01",
            "Ever since we met at the time of a cult incident?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100F久しぶりね、Dino君。\x02\x03",
            "Looking at that situation,\x01",
            "You seem to have returned to the team, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11POh, ah … well … well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PWaldさんたちに\x01",
            "The matter that I sold a fight\x01",
            "He acknowledged that it was caused by medicine … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P…… Put a bat in a bowl\x01",
            "I got it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10106FWhat is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FHuh, I can return soon.\x01",
            "It was good.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#11PWadi\x01",
            "Having entered the police station\x01",
            "It was true.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11Pお前のせいでWaldさんは……！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00005FWald……？\x01",
            "What's wrong with him?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    ChrTalk(
        0x8,
        (
            "#11P…… to you\x01",
            "Because I became caring at the time of the incident\x01",
            "I will advise only one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PWaldさんは近頃、\x01",
            "I am in a bad mood at the worst.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PIf life is regrettable\x01",
            "Do not come near here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00105FYou are in a bad mood … ….\x01",
            "What happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11P…… All, it's because of Wazi there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PAfter a while from that incident\x01",
            "Testers' guys\x01",
            "Becoming an adult …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PThis time the head of the head,\x01",
            "Do not put on the locke\x01",
            "It suddenly became a police dog.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F……got it.\x02\x03",
            "#00001FThe point is, there is a competition\x01",
            "There is no fighting opponent,\x01",
            "Is it irritated?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10106FI do not know the feeling, but …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10308F… …. Good luck.\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#11PWhat are you grieving! It is!\x01",
            "Oh, what did I do ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PおかげでWaldさん、\x01",
            "Recently IGNIS\x01",
            "You did not show my face! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10303F…… If he wants to do so\x01",
            "That way.\x02\x03",
            "#10300FHuh, I also want to do it myself\x01",
            "It's just that I'm doing it.\x02\x03",
            "In that respect, to you guys\x01",
            "I do not intend to be accused.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PDamn\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    ChrTalk(
        0x8,
        (
            "#11PWhen it is delicious\x01",
            "Go ahead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PWaldさんに見つかったら\x01",
            "Not just Wadi, you also\x01",
            "I do not know anything about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F…… Today's place is quiet\x01",
            "It seems better to break away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00108F… That's right.\x02\x03",
            "#00100Fそれじゃあね、Dino君。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PFunk\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10308F………………………………\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x138, 0)
    OP_93(0x8, 0x10E, 0x0)
    OP_4C(0x8, 0xFF)
    ModifyEventFlags(0, 0, 0x80)
    SetChrPos(0x0, 44540, -2500, -22490, 270)
    EventEnd(0x5)
    Return()

    # Function_25_3F5E end

    def Function_26_4842(): pass

    label("Function_26_4842")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_END)), "loc_4912")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48CB")

    ChrTalk(
        0x101,
        (
            "#00008F…… For a while here\x01",
            "It seems better not to enter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FAh……\x01",
            "I will be saved if you do so.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_48FC")

    label("loc_48CB")


    ChrTalk(
        0x101,
        "#00003F… … I will stop entering Ignis.\x02",
    )

    CloseMessageWindow()

    label("loc_48FC")

    Sleep(50)
    SetChrPos(0x0, 44540, -2500, -22490, 270)
    EventEnd(0x4)

    label("loc_4912")

    Return()

    # Function_26_4842 end

    def Function_27_4913(): pass

    label("Function_27_4913")

    Return()

    # Function_27_4913 end

    def Function_28_4914(): pass

    label("Function_28_4914")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, -13000, 0, -7000, 0)
    SetChrPos(0x102, -13000, 0, -7000, 0)
    SetChrPos(0x109, -13000, 0, -7000, 0)
    SetChrPos(0x105, -13000, 0, -7000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-13000, 1200, -8000, 0)
    MoveCamera(39, 27, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(20000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x2)
    OP_68(-7600, 1200, -10100, 6500)
    MoveCamera(53, 29, 0, 6500)
    SetCameraDistance(19000, 6500)
    BeginChrThread(0x101, 3, 0, 29)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 30)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 31)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 32)
    Sleep(1100)
    Sound(104, 0, 100, 0)
    OP_71(0x2, 0x5, 0x0, 0x0, 0x0)
    OP_79(0x2)
    SetMapObjFlags(0x2, 0x10)
    WaitChrThread(0x105, 3)
    OP_6F(0x79)

    ChrTalk(
        0x109,
        (
            "#12P#10108FExchange shop Ninevali ……\x02\x03",
            "#10106FIt was truly powerful though\x01",
            "It has been torn down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#5PWell, in the industry\x01",
            "You should have your own honorific.\x02\x03",
            "#00100FEven if you just taught me over there\x01",
            "Let's thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00006FThat's right.\x02\x03",
            "#00008FEven so\x01",
            "Is it like a man eating a tiger?\x02\x03",
            "#00001FIf you are not a terrorist\x01",
            "It seems that the possibility of a hunter is high, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10303FWell, if you are a hunter, you are one\x01",
            "It is slightly unnatural though.\x02\x03",
            "#10300FIncluding those around\x01",
            "Can I report it to the section chief?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D01")

    ChrTalk(
        0x101,
        (
            "#11P#00001FOh, let's do that.\x02\x03",
            "#00003F(If it is a hunter relationship, Randy\x01",
            "I heard something … …)\x02\x03",
            "#00000F(Okay, I just cleared up the support request\x01",
            "Once I return to the support department ……? )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DA4")

    label("loc_4D01")


    ChrTalk(
        0x101,
        (
            "#11P#00001FOh, let's do that.\x02\x03",
            "#00003F(If it is a hunter relationship, Randy\x01",
            "I heard something … …)\x02\x03",
            "#00000F(Oh well, now it is still there\x01",
            "Let me clear up the support request. )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DA4")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -9830, 0, -10560, 90)
    SetScenarioFlags(0x128, 5)
    OP_29(0xA1, 0x1, 0xE)
    ModifyEventFlags(1, 2, 0x80)
    OP_C9(0x0, 0x1000)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_28_4914 end

    def Function_29_4DDA(): pass

    label("Function_29_4DDA")


    def lambda_4DDF():
        OP_95(0xFE, -13000, 0, -10500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4DDF)

    def lambda_4DF9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4DF9)
    WaitChrThread(0xFE, 1)

    def lambda_4E0E():
        OP_95(0xFE, -10000, 0, -11500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4E0E)
    WaitChrThread(0xFE, 1)

    def lambda_4E2C():
        OP_95(0xFE, -6500, 0, -9600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4E2C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xFA, 0x1F4)
    Return()

    # Function_29_4DDA end

    def Function_30_4E4D(): pass

    label("Function_30_4E4D")


    def lambda_4E52():
        OP_95(0xFE, -13000, 0, -10500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4E52)

    def lambda_4E6C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4E6C)
    WaitChrThread(0xFE, 1)

    def lambda_4E81():
        OP_95(0xFE, -10000, 0, -11500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4E81)
    WaitChrThread(0xFE, 1)

    def lambda_4E9F():
        OP_95(0xFE, -7700, 0, -9000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4E9F)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xC8, 0x1F4)
    Return()

    # Function_30_4E4D end

    def Function_31_4EC0(): pass

    label("Function_31_4EC0")


    def lambda_4EC5():
        OP_95(0xFE, -13000, 0, -10500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4EC5)

    def lambda_4EDF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4EDF)
    WaitChrThread(0xFE, 1)

    def lambda_4EF4():
        OP_95(0xFE, -10000, 0, -11500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4EF4)
    WaitChrThread(0xFE, 1)

    def lambda_4F12():
        OP_95(0xFE, -7500, 0, -11200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4F12)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x14, 0x1F4)
    Return()

    # Function_31_4EC0 end

    def Function_32_4F33(): pass

    label("Function_32_4F33")


    def lambda_4F38():
        OP_95(0xFE, -13000, 0, -10500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4F38)

    def lambda_4F52():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4F52)
    WaitChrThread(0xFE, 1)

    def lambda_4F67():
        OP_95(0xFE, -10000, 0, -11500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4F67)
    WaitChrThread(0xFE, 1)

    def lambda_4F85():
        OP_95(0xFE, -8700, 0, -10600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4F85)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x46, 0x1F4)
    Return()

    # Function_32_4F33 end

    def Function_33_4FA6(): pass

    label("Function_33_4FA6")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01600.itp")
    LoadChrToIndex("chr/ch02100.itc", 0x1E)
    LoadChrToIndex("chr/ch02150.itc", 0x1F)
    LoadChrToIndex("apl/ch50019.itc", 0x20)
    LoadChrToIndex("apl/ch50030.itc", 0x21)
    LoadChrToIndex("chr/ch03050.itc", 0x22)
    LoadEffect(0x0, "event\\ev17004.eff")
    LoadEffect(0x1, "event\\ev17005.eff")
    SoundLoad(832)
    SoundLoad(2908)
    SoundLoad(2909)
    SoundLoad(2910)
    SoundLoad(3564)
    SoundLoad(3565)
    SoundLoad(3566)
    SoundLoad(3561)
    SoundLoad(3567)
    SoundLoad(2807)
    SoundLoad(2809)
    OP_68(1900, 1100, 9700, 0)
    MoveCamera(53, 29, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x101, 1900, 0, 6800, 0)
    SetChrPos(0x102, 1100, 0, 5700, 0)
    SetChrPos(0x109, 2700, 0, 5700, 0)
    SetChrPos(0x105, 1900, 0, 4600, 0)
    SetChrChipByIndex(0x17, 0x1E)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    ClearChrFlags(0x17, 0x4)
    SetChrPos(0x17, 9470, -60, -13170, 327)
    OP_52(0x17, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)

    def lambda_5122():
        OP_97(0x101, 0x0, 0x0, 0xFA0, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5122)
    Sleep(100)

    def lambda_513F():
        OP_97(0x102, 0x0, 0x0, 0xFA0, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_513F)
    Sleep(100)

    def lambda_515C():
        OP_97(0x109, 0x0, 0x0, 0xFA0, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_515C)
    Sleep(100)

    def lambda_5179():
        OP_97(0x105, 0x0, 0x0, 0xFA0, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5179)
    SetCameraDistance(19000, 2000)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 0)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x17,
        "Ferocious voice",
        "#3564V#30W─ ─ Wait, or Kora.\x02",
    )

    CloseMessageWindow()
    OP_24(0xDEC)
    OP_C9(0x1, 0x80000000)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(4430, 2000, -7760, 3500)
    MoveCamera(96, 23, 0, 3500)
    OP_6E(500, 3500)
    SetCameraDistance(16990, 3500)

    def lambda_526B():
        OP_93(0x105, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_526B)
    Sleep(50)

    def lambda_527B():
        OP_93(0x109, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_527B)
    Sleep(50)

    def lambda_528B():
        OP_93(0x102, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_528B)
    Sleep(50)

    def lambda_529B():
        OP_93(0x101, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_529B)
    Sleep(50)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    Sleep(1000)

    def lambda_52BE():
        OP_96(0xFE, 0x19DC, 0x0, 0xFFFFDEFE, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_52BE)
    WaitChrThread(0x17, 1)
    OP_6F(0x79)
    Sleep(500)
    OP_C9(0x0, 0x80000000)
    Sound(3306, 255, 80, 0)

    ChrTalk(
        0x101,
        "#00005F#30W#6P#NAh……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        "#10308F#2908V#40W#6P#NWaldか。\x02",
    )

    CloseMessageWindow()
    OP_24(0xB5C)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(1770, 1300, 3460, 0)
    MoveCamera(137, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15700, 0)
    SetMapObjFrame(0xFF, "light2", 0x0, 0x1)
    EndChrThread(0x17, 0x1)
    SetChrPos(0x17, 3800, 0, -2200, 315)
    SetChrPos(0x101, 500, 0, 6200, 180)
    SetChrPos(0x102, 3900, 0, 5200, 225)
    SetChrPos(0x109, 4200, 0, 6000, 225)
    SetChrPos(0x105, 1900, 0, 6200, 180)

    def lambda_53DA():
        OP_96(0xFE, 0x76C, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_53DA)
    OP_0D()
    WaitChrThread(0x17, 1)
    OP_93(0x17, 0x0, 0x1F4)

    ChrTalk(
        0x109,
        "#10105F(Er, is this person … …?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00108F(The team called Saber Viper\x01",
            "It's a person who summarizes … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FWald、どうしたんだい？\x02\x03",
            "#10300FTo the team as well\x01",
            "I heard that he is not making a face.\x02",
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
        0x17,
        (
            "#30W… …. Rie.\x01",
            "You do not care about me.\x02\x03",
            "Better than that … …\x01",
            "You seem to have become a Satsu dog?\x02\x03",
            "What do you mean … … Ah?\x02",
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
        0x105,
        (
            "#6P#10306F#30WWhatever you plan to do … …\x02\x03",
            "#10302FEveryone in the tests\x01",
            "It was convinced, and to anyone else\x01",
            "I do not bother you, though?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#01601F#30W#11PTame … … Are you seriously saying that?\x02\x03",
            "#01603FWith this one … …\x01",
            "Wald・ヴァレスと決着付けずに\x01",
            "Let's get through the team …\x02\x03",
            "#01607FDo you think that you will be forgiven, Ah! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10308F#30W…………………….\x02",
    )

    CloseMessageWindow()

    def lambda_573A():
        OP_96(0xFE, 0x384, 0x0, 0x13EC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_573A)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        "#6P#00011FWald、待ってくれ！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106FThat, there are circumstances … …\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0x17,
        (
            "#01607F#4S#11PRie!\x01",
            "The outfield is sunk!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x17,
        (
            "#01603F#11PWazi, what aim is your aim\x01",
            "I do not know if I got into Satsu … …\x02\x03",
            "#01608FHowever,\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    Fade(500)
    SetCameraDistance(15200, 300)
    SetChrChipByIndex(0x17, 0x1F)
    SetChrSubChip(0x17, 0x0)
    Sound(805, 0, 100, 0)
    Sleep(800)
    OP_82(0x64, 0x0, 0xBB8, 0x3E8)

    ChrTalk(
        0x17,
        (
            "#01607F#11P─ ─ ___ ___ 0\x01",
            "old Town#6Rこ　こ#から抜けられるとは\x01",
            "I do not think so! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F……!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00001FDamn\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#00106FI was troubled …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10303F#30W──Wald。\x02",
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(1680, 1300, 3250, 1200)

    def lambda_5974():
        OP_95(0xFE, 1900, 0, 4800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5974)
    Sleep(500)

    def lambda_5991():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5991)

    def lambda_599E():
        OP_96(0xFE, 0x2BC, 0x0, 0x13EC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_599E)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x101, 1)
    EndChrThread(0x101, 0x2)
    OP_93(0x101, 0x5A, 0x0)
    OP_6F(0x79)
    SetCameraDistance(14700, 30000)
    MoveCamera(138, 22, 0, 30000)

    ChrTalk(
        0x101,
        "#12P#00011FHey, Wadi! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10308F#30WLeave it to me so.\x02\x03",
            "#10306F……ねえ、Wald。\x01",
            "It is terribly common.\x02\x03",
            "Take the tests\x01",
            "Do it for Saber Viper ……\x02\x03",
            "#10301FIt is not a place where I can live forever\x01",
            "You know that, too?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x17,
        "#11P#01605F#11PWhat? Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10303F#30WI was formed the testament\x01",
            "old Town#6Rこ　こ#で好き勝手をしていた\x01",
            "It is to become a deterrent to you.\x02\x03",
            "#10300FHowever, it was weak at the beginning\x01",
            "Everyone in the tester also grew up.\x02\x03",
            "I personally got out,\x01",
            "To the extent that you can compete with you.\x02\x03",
            "My role is already over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#11P#01607F#30W…… Well, …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304F#30WAnd …\x01",
            "Someday surely other members\x01",
            "It should nest from the team.\x02\x03",
            "Graduating the moratorium season\x01",
            "I will find my own way ……\x02\x03",
            "#10302FI believe so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005F#30WWadi\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#00108F#30WWajima ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#11P#01608F#30W……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304F#30WYou guys are the same for you.\x02\x03",
            "There are a lot of casualties, but at the invitation of the Mafia\x01",
            "It has a spirit and gut feeling not to ride.\x02\x03",
            "#10300FだからWald……\x01",
            "I am sure that you will find a way.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)
    Sleep(300)
    Sound(2807, 255, 100, 0)

    ChrTalk(
        0x17,
        "#11P#01604F#60W#10A…………………\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x3E8)

    ChrTalk(
        0x17,
        "#11P#01609F#2809V#4S#25A#40WHa ha ha ha ha ha ha! It is! It is!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrFlags(0x17, 0x10)
    SetChrFlags(0x17, 0x2)
    SetChrChipByIndex(0x17, 0x21)
    SetChrSubChip(0x17, 0x1)
    Sound(805, 0, 100, 0)
    Sleep(500)
    Fade(500)
    OP_68(1470, 1300, 3040, 700)
    MoveCamera(144, 22, 0, 700)
    OP_6E(600, 700)
    SetCameraDistance(13720, 700)
    Sound(533, 0, 60, 0)
    Sound(532, 0, 70, 0)
    SetChrSubChip(0x17, 0x2)
    Sleep(60)
    SetChrSubChip(0x17, 0x3)
    Sleep(500)
    OP_6F(0x79)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x17,
        (
            "#01611F#3565V#30W#11PNo way No way\x01",
            "Hana is to get rid of the sweet little thing!\x02\x03",
            "#01607F#3566VAlright, do not speak any more!\x02\x03",
            "#3561VTemple dirty this \"sanctuary\"!\x01",
            "You can not absolutely forgive me! It is!\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xDE9)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    Sleep(300)

    ChrTalk(
        0x105,
        "#6P#10303F#40WThat's right.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x101,
        "#12P#00011FHey, Wadi!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10303F#30WLloyd, handed is useless.\x02\x03",
            "#10301FThis Timan is for me alone\x01",
            "I have to put a kelly.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    Fade(250)
    ClearChrFlags(0x17, 0x10)
    ClearChrFlags(0x17, 0x2)
    SetChrChipByIndex(0x17, 0x1F)
    SetChrSubChip(0x17, 0x0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x17,
        (
            "#11P#01604F#30WKuku, that much\x01",
            "You seem to know … …\x02\x03",
            "#01602FStrike down thoroughly\x01",
            "I will crawl on the ground …\x02\x03",
            "Well, that's right.\x01",
            "You know I'll wake up for a while.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x105,
        "#6P#10303F#2909V#30W── The talk is over.\x02",
    )

    CloseMessageWindow()
    OP_24(0xB5D)
    OP_57(0x0)
    OP_5A()
    StopBGM(0xBB8)

    ChrTalk(
        0x17,
        "#11P#01601F#3567VAh……?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xDEF)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    Fade(500)
    MoveCamera(153, 25, 0, 2500)
    SetCameraDistance(15500, 2500)

    def lambda_6205():
        OP_96(0xFE, 0x12C, 0x0, 0x13EC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6205)
    PlayEffect(0x1, 0x2, 0x105, 0x1, 0, 0, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sound(832, 2, 50, 0)
    Sleep(1000)
    OP_6F(0x79)
    Fade(500)
    OP_68(1900, 1100, 4100, 0)
    MoveCamera(38, 20, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(14790, 0)
    SetMapObjFrame(0xFF, "light2", 0x1, 0x1)
    OP_68(1900, 1100, 3100, 1500)
    SetCameraDistance(15790, 1500)
    SetChrPos(0x109, 4000, 0, 6000, 225)
    OP_93(0x101, 0x87, 0x0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x17,
        "#12P#01605FIt is! Is it?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        "#00005F(this is……!)\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7452", 0)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x105,
        (
            "#5P#10301F#2910V#30W#20AWald─#800W─\x01",
            "#40WI am going seriously.#12R噵 噵 噵 噵 噵 噵#.\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    SetScenarioFlags(0x1, 2)
    SetChrBattleFlags(0x101, 0x8)
    SetChrBattleFlags(0x102, 0x8)
    SetChrBattleFlags(0x109, 0x8)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_32(0x4, 0x0, 0x46)
    OP_32(0x4, 0xFB, 0x0)
    OP_32(0x4, 0xD, 0x32)
    Battle("BattleInfo_7F8", 0x30200011, 0x0, 0x0, 0x12, 0xFF)
    FadeToDark(0, 0, -1)
    MiniGame(0x32, 0x4, 0x3, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_32(0x4, 0xFE, 0x0)
    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 34)
    Return()

    # Function_33_4FA6 end

    def Function_34_63F7(): pass

    label("Function_34_63F7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02153.itc", 0x1E)
    LoadChrToIndex("chr/ch02150.itc", 0x1F)
    LoadChrToIndex("chr/ch03050.itc", 0x20)
    LoadChrToIndex("chr/ch03051.itc", 0x21)
    LoadChrToIndex("apl/ch51111.itc", 0x22)
    LoadEffect(0x0, "battle\\ms00000.eff")
    SoundLoad(3568)
    SoundLoad(3569)
    SoundLoad(3570)
    OP_68(1900, 1000, 4100, 0)
    MoveCamera(135, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x101, 300, 0, 5100, 135)
    SetChrPos(0x102, 3900, 0, 5200, 225)
    SetChrPos(0x109, 4000, 0, 6000, 225)
    SetChrChipByIndex(0x17, 0x1E)
    SetChrSubChip(0x17, 0x2)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    ClearChrFlags(0x17, 0x4)
    SetChrPos(0x17, 1900, 0, 1500, 0)
    OP_52(0x17, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrChipByIndex(0x105, 0x20)
    SetChrSubChip(0x105, 0x0)
    SetChrPos(0x105, 1900, 0, 5800, 180)
    SetMapObjFrame(0xFF, "light2", 0x0, 0x1)
    StopBGM(0xFA0)
    WaitBGM()
    FadeToBright(250, 0)
    OP_68(1900, 1000, 2150, 700)
    SetCameraDistance(15500, 700)
    SetChrChip(0x0, 0x105, 0x32, 0xC8)

    def lambda_655B():
        OP_95(0xFE, 1900, 0, 2600, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_655B)
    WaitChrThread(0x105, 1)
    BeginChrThread(0x105, 3, 0, 35)
    Sleep(400)
    OP_68(1900, 1000, 1100, 1500)
    MoveCamera(130, 21, 0, 1500)
    OP_6E(550, 1500)
    SetCameraDistance(16500, 1500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    PlayEffect(0x0, 0x1, 0x105, 0x5, 0, 1100, 1000, 0, 0, 0, 200, 200, 200, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x17, 0x1E)
    SetChrSubChip(0x17, 0x0)

    def lambda_65FB():
        OP_9D(0xFE, 0x76C, 0x0, 0xFFFFFE0C, 0x898, 0x2BC)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_65FB)
    Sound(2800, 255, 100, 0)
    Sleep(500)
    CancelBlur(0)
    WaitChrThread(0x17, 1)
    Sound(862, 0, 100, 0)
    Sound(833, 0, 30, 0)
    OP_82(0x0, 0x64, 0xBB8, 0x12C)
    SetChrSubChip(0x17, 0x3)

    def lambda_664B():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x12C, 0x2BC)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_664B)
    WaitChrThread(0x17, 1)
    Sound(811, 0, 100, 0)
    OP_82(0x0, 0x64, 0xBB8, 0x64)

    ChrTalk(
        0x17,
        "#01610F#13A#11PGreat!\x02",
    )

    CloseMessageWindow()
    Sleep(800)

    def lambda_66A7():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_66A7)
    Sleep(1200)

    ChrTalk(
        0x17,
        (
            "#11P#01611F#40W… …. Gug …… Tame …\x02\x03",
            "No way … until now …\x01",
            "Always … … pulling out my hand … ….?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10306F#30W…… Not Randy, but\x01",
            "It's a bit of a bad technique now.\x02\x03",
            "#10308FBut to you today\x01",
            "I had you go out without taking refuge.\x02\x03",
            "#10301FThis is……\x01",
            "The last sincerity that I can show.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#11P#01611F#50WGeez …\x01",
            "…… Wadi …… Troops ……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x105, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#11P#10303F#30Wさよなら、Wald。\x02\x03",
            "#10300FFor the past 2 years …\x01",
            "It was pretty fun.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_6868():

        label("loc_6868")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_6868")

    QueueWorkItem2(0x101, 2, lambda_6868)

    def lambda_687A():

        label("loc_687A")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_687A")

    QueueWorkItem2(0x102, 2, lambda_687A)

    def lambda_688C():

        label("loc_688C")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_688C")

    QueueWorkItem2(0x109, 2, lambda_688C)
    OP_68(1900, 1000, 3100, 5000)
    SetCameraDistance(17500, 5000)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)

    def lambda_68C0():
        OP_95(0xFE, 1900, 0, 20000, 1800, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_68C0)
    Sleep(3000)
    BeginChrThread(0x101, 3, 0, 36)
    Sleep(1000)
    BeginChrThread(0x109, 3, 0, 36)
    Sleep(800)
    BeginChrThread(0x102, 3, 0, 36)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)
    OP_68(1900, 1000, -500, 2000)
    MoveCamera(140, 23, 0, 2000)
    SetCameraDistance(16500, 2000)
    Sleep(500)

    def lambda_6923():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_6923)
    Sleep(1200)
    OP_6F(0x79)
    OP_68(1900, 1000, -500, 50000)
    MoveCamera(136, 34, 0, 50000)
    OP_6E(550, 50000)
    SetCameraDistance(39710, 50000)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x17,
        (
            "#11P#01611F#3568V#50W#45AFunny Pictures ……\x01",
            "… … Absolutely not admitted …!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(1000)

    ChrTalk(
        0x17,
        (
            "#11P#01610F#3569V#50W#40AI do not want to go through alone ……\x01",
            "I admit I admit it or not! It is!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(1900, 1000, -500, 6000)
    MoveCamera(136, 34, 0, 6000)
    OP_6E(550, 6000)
    SetCameraDistance(39710, 6000)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    EndChrThread(0x17, 0x2)
    Sleep(1500)
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)

    ChrTalk(
        0x17,
        "#11P#01607F#3570V#5S#50W#20AWell, I do not mind. It is! It is!\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    Sleep(500)
    SetScenarioFlags(0x22, 0)
    NewScene("c1000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_34_63F7 end

    def Function_35_6AD1(): pass

    label("Function_35_6AD1")

    SetChrFlags(0x105, 0x10)
    SetChrFlags(0x105, 0x2)
    SetChrFlags(0x105, 0x20)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x0)
    Sleep(60)
    Sound(802, 0, 100, 0)
    Sound(3093, 255, 100, 0)
    SetChrSubChip(0x105, 0x0)
    Sleep(240)
    Sound(534, 0, 40, 0)
    Sound(809, 0, 80, 0)
    SetChrChip(0x1, 0x105, 0x0, 0x0)

    def lambda_6B17():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x44C, 0x2BC)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6B17)
    SetChrSubChip(0x105, 0x1)
    Sound(815, 0, 100, 0)
    Sound(195, 0, 100, 0)
    Sound(501, 0, 100, 0)
    Sleep(300)
    Sound(833, 0, 40, 0)
    SetChrSubChip(0x105, 0x1)
    WaitChrThread(0x105, 1)
    ClearChrFlags(0x105, 0x10)
    ClearChrFlags(0x105, 0x2)
    ClearChrFlags(0x105, 0x20)
    SetChrChipByIndex(0x105, 0x20)
    SetChrSubChip(0x105, 0x0)
    Return()

    # Function_35_6AD1 end

    def Function_36_6B6E(): pass

    label("Function_36_6B6E")

    EndChrThread(0xFE, 0x2)

    def lambda_6B77():
        OP_95(0xFE, 1900, 0, 8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6B77)
    WaitChrThread(0xFE, 1)

    def lambda_6B95():
        OP_95(0xFE, 1900, 0, 20000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6B95)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_36_6B6E end

    def Function_37_6BAF(): pass

    label("Function_37_6BAF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, 50000, -2100, -22500, 270)
    SetChrPos(0x104, 50000, -2100, -21700, 270)
    SetChrPos(0x109, 50000, -2100, -23300, 270)
    SetChrPos(0x105, -17300, 0, -10400, 90)
    SetChrPos(0x102, -18500, 0, -9800, 90)
    SetChrPos(0x103, -19700, 0, -11000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x8C, 0x0)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sentaku", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    ClearMapObjFlags(0x8, 0x4)
    SoundLoad(128)
    Sound(128, 2, 100, 0)
    PlayBGM("ed7560", 0)
    OP_68(18500, 500, -25000, 0)
    MoveCamera(32, 4, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(40500, 0)
    MoveCamera(27, 4, 0, 6000)
    SetCameraDistance(45500, 6000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x6E, 0x0)
    OP_68(47000, -600, -22500, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(21500, 0)
    OP_0D()
    Sound(116, 0, 100, 0)
    ClearMapObjFlags(0x4, 0x10)
    OP_71(0x4, 0x0, 0xF, 0x0, 0x0)
    OP_79(0x4)
    OP_68(38500, -600, -23800, 5500)
    BeginChrThread(0x101, 3, 0, 38)
    Sleep(600)
    BeginChrThread(0x109, 3, 0, 39)
    Sleep(600)
    BeginChrThread(0x104, 3, 0, 40)
    Sleep(1300)
    Sound(117, 0, 100, 0)
    OP_71(0x4, 0xF, 0x0, 0x0, 0x0)
    WaitChrThread(0x101, 3)
    SetChrPos(0x101, 18500, -2500, -22300, 315)

    def lambda_6DF9():
        OP_97(0xFE, 0xFFFFCB44, 0x0, 0x34BC, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6DF9)
    Sleep(100)
    EndChrThread(0x109, 0xFF)
    SetChrPos(0x109, 18500, -2500, -23800, 315)

    def lambda_6E2B():
        OP_97(0xFE, 0xFFFFCB44, 0x0, 0x34BC, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6E2B)
    Sleep(100)
    EndChrThread(0x104, 0xFF)
    SetChrPos(0x104, 20000, -2500, -22300, 315)

    def lambda_6E5D():
        OP_97(0xFE, 0xFFFFCB44, 0x0, 0x34BC, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6E5D)
    Fade(500)
    OP_68(16200, 0, -20000, 0)
    MoveCamera(315, 27, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(23500, 0)
    OP_68(5200, 1000, -9000, 8500)
    MoveCamera(59, 27, 0, 8500)
    SetCameraDistance(19500, 8500)
    WaitChrThread(0x101, 1)

    def lambda_6ED3():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6ED3)
    WaitChrThread(0x109, 1)

    def lambda_6EE4():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6EE4)
    WaitChrThread(0x104, 1)

    def lambda_6EF5():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6EF5)
    OP_6F(0x79)
    Sleep(300)
    OP_68(-11500, 1000, -10400, 3000)
    MoveCamera(55, 31, 0, 3000)
    Sleep(1000)
    BeginChrThread(0x105, 3, 0, 41)
    Sleep(100)
    BeginChrThread(0x102, 3, 0, 42)
    Sleep(100)
    BeginChrThread(0x103, 3, 0, 43)
    Sleep(2500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x105, 0xFF)
    OP_68(1200, 1100, -8000, 0)
    MoveCamera(37, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, 2900, 0, -7750, 270)
    SetChrPos(0x104, 2250, 0, -6700, 270)
    SetChrPos(0x109, 2250, 0, -9350, 270)
    SetChrPos(0x105, -500, 0, -8250, 90)
    SetChrPos(0x102, 200, 0, -6700, 90)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x103, -100, 0, -9350, 90)
    SetChrSubChip(0x103, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    SetCameraDistance(16500, 1500)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x105,
        "#6P#10308F……How was it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11PIt is useless……\x01",
            "It seems I do not know at all.\x02\x03",
            "#00013Fここ数日、Waldの姿は\x01",
            "It seems that nobody is looking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#11PApparently thoroughly\x01",
            "I guess you kept away from me ……\x02\x03",
            "#00301FConversely do not know where to go\x01",
            "I got stuck and got stuck.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10106FYeah … That seemed desperate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10303F……Really.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#6PAgain to the children of Testaments\x01",
            "I tried asking it again ….\x02\x03",
            "#00108F誰も最近、Waldさんの姿を\x01",
            "There seems to be no one to see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00206FYes … … Destroyed and crushed figure\x01",
            "I heard that I often saw it for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#11PI see.\x01",
            "I can not see the relationship behind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#11PThat asshole, Where from where?\x01",
            "\"Gnostic\" you … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10308F…………………………………….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10113F… … Wadi, are you all right?\x02\x03",
            "Something does not look good on you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FHuh, it may have been cold due to rain.\x02\x03",
            "#10300Fとりあえず、Abbasたちに\x01",
            "I asked for information collection.\x02\x03",
            "Waldのことは置いておいて\x01",
            "We will return to the support department once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11P… … That's right.\x01",
            "Ka'a prepared breakfast\x01",
            "He seems to be giving away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#6PHuhu, somewhat recently,\x01",
            "I have been taking care of me.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(17000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    ReplaceBGM("ed7150", "ed7560")
    StopSound(128, 1000, 100)
    Sleep(1000)
    Sleep(1000)
    SetScenarioFlags(0x23, 1)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_37_6BAF end

    def Function_38_7474(): pass

    label("Function_38_7474")


    def lambda_7479():
        OP_95(0xFE, 45000, -2500, -22500, 2200, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7479)

    def lambda_7493():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7493)
    WaitChrThread(0xFE, 1)

    def lambda_74A8():
        OP_95(0xFE, 38500, -2500, -23800, 2200, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_74A8)
    WaitChrThread(0xFE, 1)

    def lambda_74C6():
        OP_95(0xFE, 27500, -2500, -23800, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_74C6)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_38_7474 end

    def Function_39_74E0(): pass

    label("Function_39_74E0")


    def lambda_74E5():
        OP_95(0xFE, 45000, -2500, -23300, 2200, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_74E5)

    def lambda_74FF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_74FF)
    WaitChrThread(0xFE, 1)

    def lambda_7514():
        OP_95(0xFE, 38500, -2500, -24600, 2200, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7514)
    WaitChrThread(0xFE, 1)

    def lambda_7532():
        OP_95(0xFE, 27500, -2500, -24600, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7532)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_39_74E0 end

    def Function_40_754C(): pass

    label("Function_40_754C")


    def lambda_7551():
        OP_95(0xFE, 45000, -2500, -21700, 2200, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7551)

    def lambda_756B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_756B)
    WaitChrThread(0xFE, 1)

    def lambda_7580():
        OP_95(0xFE, 38500, -2500, -23000, 2200, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7580)
    WaitChrThread(0xFE, 1)

    def lambda_759E():
        OP_95(0xFE, 27500, -2500, -23000, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_759E)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_40_754C end

    def Function_41_75B8(): pass

    label("Function_41_75B8")


    def lambda_75BD():
        OP_95(0xFE, -9500, 0, -10400, 2200, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_75BD)
    WaitChrThread(0xFE, 1)

    def lambda_75DB():
        OP_95(0xFE, -3500, 0, -9000, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_75DB)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_41_75B8 end

    def Function_42_75F5(): pass

    label("Function_42_75F5")


    def lambda_75FA():
        OP_95(0xFE, -9500, 0, -9800, 2200, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_75FA)
    WaitChrThread(0xFE, 1)

    def lambda_7618():
        OP_95(0xFE, -3500, 0, -8400, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7618)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_42_75F5 end

    def Function_43_7632(): pass

    label("Function_43_7632")


    def lambda_7637():
        OP_95(0xFE, -9500, 0, -11000, 2200, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7637)
    WaitChrThread(0xFE, 1)

    def lambda_7655():
        OP_95(0xFE, -3500, 0, -9600, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7655)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_43_7632 end

    def Function_44_766F(): pass

    label("Function_44_766F")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(8090, -4470, -37870, 0)
    MoveCamera(39, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16540, 0)
    SetChrFlags(0xA, 0x80)
    EndChrThread(0xA, 0x0)
    SetChrFlags(0xB, 0x80)
    EndChrThread(0xB, 0x0)
    SetChrPos(0x101, 9720, -6420, -37340, 0)
    SetChrPos(0x102, 8270, -6390, -37670, 0)
    SetChrPos(0x103, 10420, -6420, -38430, 0)
    SetChrPos(0x104, 9060, -6390, -39050, 0)
    SetChrPos(0x109, 11890, -6440, -37730, 310)
    SetChrPos(0x105, 11080, -6420, -39330, 310)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#12P#00000FHere is the arrangement requested by the demon demonic order to be arranged,\x01",
            "Is it the entrance of Geo Front D … ….\x02\x03",
            "#00003FPreviously materials\x01",
            "It should have been left,\x01",
            "It seems that it was removed for the request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203FHmm, I have a little doubt … …\x02\x03",
            "#00200FWhy is the power net\x01",
            "引かれていないold Townに、\x01",
            "The entrance to the Geo Front?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00305FOh, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10105F確かold Townは、都市開発から\x01",
            "You should be left behind, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103FYeah ….\x01",
            "In the past, the D section was the speculation of lawmakers and officials\x01",
            "I told you that it was built … ….\x02\x03",
            "#00108FWhile underground construction is going on endlessly\x01",
            "You seem to have expanded to such a place.\x02\x03",
            "#00106FUnexpected demand was built up,\x01",
            "Construction seems to have begun unplanned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FWell, I see.\x02\x03",
            "#10304FIn short, by the corrupt government\x01",
            "Is it a product of interest?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FOh, certainly … …\x02\x03",
            "#00000FSince Dieter became mayor\x01",
            "It seems that improvements have been made.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00300FWell, if you go to the extermination of arranged majestic animals\x01",
            "Let's try entering quickly.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x16B, 2)
    ModifyEventFlags(0, 3, 0x80)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x4)
    SetChrPos(0xA, 5840, 0, -6890, 135)
    BeginChrThread(0xA, 0, 0, 2)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x4)
    SetChrPos(0xB, 4760, 0, -5890, 135)
    BeginChrThread(0xB, 0, 0, 2)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 10220, -6440, -36310, 0)
    EventEnd(0x5)
    Return()

    # Function_44_766F end

    def Function_45_7B82(): pass

    label("Function_45_7B82")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(803)
    SoundLoad(894)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    OP_68(-13300, 1100, -10600, 0)
    MoveCamera(60, 35, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, -13300, 0, -9400, 200)
    SetChrPos(0x102, -14000, 0, -11600, 20)
    SetChrPos(0x103, -14600, 0, -10500, 110)
    SetChrPos(0x109, -12000, 0, -10500, 290)
    SetChrPos(0x105, -12600, 0, -11600, 340)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    MoveCamera(70, 30, 0, 3000)
    SetCameraDistance(17500, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x102,
        (
            "#12P#00101F… from last night to this morning\x01",
            "Randy 's movements came into view.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00003FOh, let's lightly organize.\x02",
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x1, 1)

    label("loc_7D03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FF2")
    SetScenarioFlags(0x1, 1)
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
            "#1KWas Randy first visited?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Exchange shop \"Ninevali\"\x01",      # 0
            "Repair shop \"Guillaume Studio\"\x01",      # 1
            "Casino Bar \"Barca\"\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7DB7")
    ClearScenarioFlags(0x1, 1)

    label("loc_7DB7")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KThen Randy visited?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Exchange shop \"Ninevali\"\x01",      # 0
            "Repair shop \"Guillaume Studio\"\x01",      # 1
            "Casino Bar \"Barca\"\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7E48")
    ClearScenarioFlags(0x1, 1)

    label("loc_7E48")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KLast time Randy visited?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Exchange shop \"Ninevali\"\x01",      # 0
            "Repair shop \"Guillaume Studio\"\x01",      # 1
            "Casino Bar \"Barca\"\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7EE4")
    ClearScenarioFlags(0x1, 1)

    label("loc_7EE4")

    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F76")

    ChrTalk(
        0x101,
        (
            "#5P#00003F(Disagreeable……\x01",
            "It should not be in this order. )\x02\x03",
            "#00001F(Let's organize it again.)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F71")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7F71")

    Jump("loc_7FED")

    label("loc_7F76")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_7F86"),
        (SWITCH_DEFAULT, "loc_7FBC"),
    )


    label("loc_7F86")

    OP_2C(0xAA, 0x1)

    ChrTalk(
        0x101,
        "#5P#00000F(No doubt, this is the order.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_7FED")

    label("loc_7FBC")


    ChrTalk(
        0x101,
        "#5P#00003F(… … maybe, this is the turn.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_7FED")

    label("loc_7FED")

    Jump("loc_7D03")

    label("loc_7FF2")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "３時〜４時　Casino Bar \"Barca\"\x01",
            "５時〜６時　Repair shop \"Guillaume Studio\"\x01",
            "6 o'clock - change shop \"Ninevali\"\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#5P#00006F─ ─ probably first\x01",
            "I had it with Drake owner\x01",
            "I guess I got a trunk.\x02\x03",
            "#00008FIt was in the trunk\x01",
            "Randy's hunting gifts … …\x02\x03",
            "#00001FProbably, boasts considerable offensive power\x01",
            "I guess it's a driving rifle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203FUsually, such a rifle\x01",
            "You should carry it in a disassembled state.\x02\x03",
            "#00201FBecause I have not used it for about 2 years,\x01",
            "Randy declined the unit\x01",
            "I had them repair workshops ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#11P#10103F─ ─ Yes, I think there is no mistake.\x02\x03",
            "#10108FMaintenance of arms, life and death on the battlefield\x01",
            "It is a thing to change … ….\x02\x03",
            "#10101FIf Randy-senpai, absolutely\x01",
            "It should have been carefully checked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FFinally, drop by the exchange shop\x01",
            "It seems that they purchased various things … ….\x02\x03",
            "#10301FI mean you bought gunpowder ammo\x01",
            "Is it a rather special rifle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00108FSome of Rheinfault\x01",
            "Switch between the power formula and the pyrotechnic formula\x01",
            "I heard there is also a lineup ……\x02\x03",
            "#00101FEither way, it's quite special\x01",
            "It will be an enhanced rifle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00006FOh, red constellation hunters also\x01",
            "A huge rifle that I have not seen\x01",
            "You used it.\x02\x03",
            "#00013F── Ok, by this,\x01",
            "I could grasp the situation of Randy ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00206FAt the end Randy says a replacement shop\x01",
            "It was 6 o'clock this morning that I visited … …\x02\x03",
            "#00208FIt's about 10 o'clock now\x01",
            "It's almost four hours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#11P#10106FFrom now on catching up to my legs is\x01",
            "It seems to be pretty difficult, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00003F…… No, Randy said\x01",
            "There should be a limit no matter how much it is tough.\x02\x03",
            "#00001FIf you're on a \"red constellation\"\x01",
            "As expected it will take as much as a nap.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FIn addition, utilizing the benefits of the topography\x01",
            "Tackle it at a stretch …\x02\x03",
            "#10302FWell, at the time of honorable resolution\x01",
            "I have to plan to do some special things\x01",
            "I think the area is reasonable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00101F…… Anyway\x01",
            "I can not afford that much already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00013FOh, it will not work if this happens\x01",
            "Only going to Mainz direction ─\x02",
        )
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)

    def lambda_8767():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8767)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_878C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_878C)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x6)
    Sound(802, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x101,
        "#5P#00011FNo way ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00205FFrom Randy's … ….?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x7)
    OP_24(0x323)
    Sound(804, 0, 100, 0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00007F── Yes, the Special Affairs Support Division,\x01",
            "It is Lloyd · Bannings!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice of a young man")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Hi, Mr. Lloyd.\x02\x03",
            "…… Huh, apparently someone else\x01",
            "You seem to have made me wrong.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005FWell, that voice ……\x02\x03",
            "#00013F…… Why is this number?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice of a young man")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Huh, I told you.\x01",
            "It is a fan of Lloyd's.\x02\x03",
            "── Times department store.\x02\x03",
            "If you are free,\x01",
            "Please come to the rooftop.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(813, 0, 70, 0)
    Sleep(400)
    Sound(894, 2, 100, 0)
    Sleep(1200)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x6)
    Sound(804, 0, 100, 0)
    OP_24(0x37E)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#6P#00201F…… Lloyd.\x01",
            "The current communication ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00108FWell, who the hell were you?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_64(0x101)
    Sleep(300)
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#5P#00003F…… It is Tsao of \"Black moon\".\x02\x03",
            "#00013FCentral squareのデパートの\x01",
            "She seems to be waiting at the rooftop.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#11P#10111FWell ……! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10301FAt such time …\x01",
            "What on earth are you going to do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00006F……I do not understand.\x01",
            "However, that man was meaningless\x01",
            "I do not think that I will contact him.\x02\x03",
            "#00001FBefore going out to the mountain path\x01",
            "Let's get close to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00101FI knew.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00201FLet's hurry anyway.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    SetChrPos(0x0, -13220, 0, -9320, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x166, 1)
    OP_29(0xAA, 0x1, 0x4)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7151", 0)
    OP_24(0x323)
    OP_24(0x37E)
    EventEnd(0x5)
    Return()

    # Function_45_7B82 end

    def Function_46_8D16(): pass

    label("Function_46_8D16")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(803)
    SoundLoad(894)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    OP_68(-6100, -2500, -25800, 0)
    MoveCamera(65, 30, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(21000, 0)
    OP_F0(0x0, 0x1)
    SetChrPos(0x101, -5500, -3800, -24600, 215)
    SetChrPos(0x102, -6900, -3800, -26100, 35)
    SetChrPos(0x103, -7200, -3650, -25050, 125)
    SetChrPos(0x109, -4900, -3800, -26300, 305)
    SetChrPos(0x105, -6100, -3800, -26800, 35)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    MoveCamera(75, 25, 0, 3000)
    SetCameraDistance(17000, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x102,
        (
            "#12P#00101F… from last night to this morning\x01",
            "Randy 's movements came into view.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00003FOh, let's lightly organize.\x02",
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x1, 1)

    label("loc_8E9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_918A")
    SetScenarioFlags(0x1, 1)
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
            "#1KWas Randy first visited?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Exchange shop \"Ninevali\"\x01",      # 0
            "Repair shop \"Guillaume Studio\"\x01",      # 1
            "Casino Bar \"Barca\"\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8F4F")
    ClearScenarioFlags(0x1, 1)

    label("loc_8F4F")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KThen Randy visited?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Exchange shop \"Ninevali\"\x01",      # 0
            "Repair shop \"Guillaume Studio\"\x01",      # 1
            "Casino Bar \"Barca\"\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8FE0")
    ClearScenarioFlags(0x1, 1)

    label("loc_8FE0")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KLast time Randy visited?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Exchange shop \"Ninevali\"\x01",      # 0
            "Repair shop \"Guillaume Studio\"\x01",      # 1
            "Casino Bar \"Barca\"\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_907C")
    ClearScenarioFlags(0x1, 1)

    label("loc_907C")

    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_910E")

    ChrTalk(
        0x101,
        (
            "#5P#00003F(Disagreeable……\x01",
            "It should not be in this order. )\x02\x03",
            "#00001F(Let's organize it again.)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9109")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9109")

    Jump("loc_9185")

    label("loc_910E")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_911E"),
        (SWITCH_DEFAULT, "loc_9154"),
    )


    label("loc_911E")

    OP_2C(0xAA, 0x1)

    ChrTalk(
        0x101,
        "#5P#00000F(No doubt, this is the order.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_9185")

    label("loc_9154")


    ChrTalk(
        0x101,
        "#5P#00003F(… … maybe, this is the turn.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_9185")

    label("loc_9185")

    Jump("loc_8E9B")

    label("loc_918A")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "３時〜４時　Casino Bar \"Barca\"\x01",
            "５時〜６時　Repair shop \"Guillaume Studio\"\x01",
            "6 o'clock - change shop \"Ninevali\"\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#5P#00006F─ ─ probably first\x01",
            "I had it with Drake owner\x01",
            "I guess I got a trunk.\x02\x03",
            "#00008FIt was in the trunk\x01",
            "Randy's hunting gifts … …\x02\x03",
            "#00001FProbably, boasts considerable offensive power\x01",
            "I guess it's a driving rifle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203FUsually, such a rifle\x01",
            "You should carry it in a disassembled state.\x02\x03",
            "#00201FBecause I have not used it for about 2 years,\x01",
            "Randy declined the unit\x01",
            "I had them repair workshops ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103F#11P─ ─ Yes, I think there is no mistake.\x02\x03",
            "#10108FMaintenance of arms, life and death on the battlefield\x01",
            "It is a thing to change … ….\x02\x03",
            "#10101FIf Randy-senpai, absolutely\x01",
            "It should have been carefully checked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10303FFinally, drop by the exchange shop\x01",
            "It seems that they purchased various things … ….\x02\x03",
            "#10301FI mean you bought gunpowder ammo\x01",
            "Is it a rather special rifle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00108FSome of Rheinfault\x01",
            "Switch between the power formula and the pyrotechnic formula\x01",
            "I heard there is also a lineup ……\x02\x03",
            "#00101FEither way, it's quite special\x01",
            "It will be an enhanced rifle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00006FOh, red constellation hunters also\x01",
            "A huge rifle that I have not seen\x01",
            "You used it.\x02\x03",
            "#00013F── Ok, by this,\x01",
            "I could grasp the situation of Randy ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00206FAt the end Randy says a replacement shop\x01",
            "It was 6 o'clock this morning that I visited … …\x02\x03",
            "#00208FIt's about 10 o'clock now\x01",
            "It's almost four hours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#11PFrom now on catching up to my legs is\x01",
            "It seems to be pretty difficult, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00003F…… No, Randy said\x01",
            "There should be a limit no matter how much it is tough.\x02\x03",
            "#00001FIf you're on a \"red constellation\"\x01",
            "As expected it will take as much as a nap.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FIn addition, utilizing the benefits of the topography\x01",
            "Tackle it at a stretch …\x02\x03",
            "#10302FWell, at the time of honorable resolution\x01",
            "I have to plan to do some special things\x01",
            "I think the area is reasonable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00101F…… Anyway\x01",
            "I can not afford that much already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00013FOh, it will not work if this happens\x01",
            "Only going to Mainz direction ─\x02",
        )
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)

    def lambda_9907():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9907)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_992C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_992C)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x6)
    Sound(802, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x101,
        "#5P#00011FNo way ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00205FFrom Randy's … ….?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x7)
    OP_24(0x323)
    Sound(804, 0, 100, 0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00007F── Yes, the Special Affairs Support Division,\x01",
            "It is Lloyd · Bannings!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Male voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Hi, Mr. Lloyd.\x02\x03",
            "…… Huh, apparently someone else\x01",
            "You seem to have made me wrong.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005FWell, that voice ……\x02\x03",
            "#00013F…… Why is this number?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Male voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Huh, I told you.\x01",
            "It is a fan of Lloyd's.\x02\x03",
            "── Times department store.\x02\x03",
            "If you are free,\x01",
            "Please come to the rooftop.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(813, 0, 70, 0)
    Sleep(400)
    Sound(894, 2, 100, 0)
    Sleep(1200)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x6)
    Sound(804, 0, 100, 0)
    OP_24(0x37E)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#6P#00201F…… Lloyd.\x01",
            "The current communication ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00108FWell, who the hell were you?\x02",
    )

    CloseMessageWindow()
    OP_64(0x101)
    Sleep(300)
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#5P#00003F…… It is Tsao of \"Black moon\".\x02\x03",
            "#00013FCentral squareのデパートの\x01",
            "She seems to be waiting at the rooftop.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#10111F#11PWell ……! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10301FAt such time …\x01",
            "What on earth are you going to do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00006F……I do not understand.\x01",
            "However, that man was meaningless\x01",
            "I do not think that I will contact him.\x02\x03",
            "#00001FBefore going out to the mountain path\x01",
            "Let's get close to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00101FI knew.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00201FLet's hurry anyway.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    SetChrPos(0x0, -5500, -3800, -24330, 207)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x166, 1)
    OP_29(0xAA, 0x1, 0x4)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7151", 0)
    OP_24(0x323)
    OP_24(0x37E)
    EventEnd(0x5)
    Return()

    # Function_46_8D16 end

    def Function_47_9EB7(): pass

    label("Function_47_9EB7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(9630, 1300, 4460, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16210, 0)
    SetChrPos(0x101, 13000, 0, 7800, 225)
    SetChrPos(0x102, 13000, 0, 7800, 225)
    SetChrPos(0x109, 13000, 0, 7800, 225)
    SetChrPos(0x105, 13000, 0, 7800, 225)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x3, 0x10)
    OP_71(0x3, 0x0, 0x10, 0x0, 0x0)
    OP_79(0x0)
    OP_0D()
    Sleep(500)

    def lambda_9F92():
        OP_95(0x101, 8630, 0, 4260, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9F92)

    def lambda_9FAC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9FAC)
    Sleep(500)

    def lambda_9FC0():
        OP_95(0x102, 9430, 0, 3460, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9FC0)

    def lambda_9FDA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9FDA)
    Sleep(500)

    def lambda_9FEE():
        OP_95(0x109, 9830, 0, 5460, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9FEE)

    def lambda_A008():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_A008)
    Sleep(500)

    def lambda_A01C():
        OP_95(0x105, 10630, 0, 4460, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A01C)

    def lambda_A036():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_A036)
    Sleep(50)
    WaitChrThread(0x101, 1)

    def lambda_A04E():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A04E)
    WaitChrThread(0x102, 1)

    def lambda_A05F():
        OP_93(0x102, 0x168, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A05F)
    WaitChrThread(0x109, 1)

    def lambda_A070():
        OP_93(0x109, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A070)
    WaitChrThread(0x105, 1)

    def lambda_A081():
        OP_93(0x105, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A081)
    SetMapObjFlags(0x3, 0x0)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x102,
        (
            "#12P#00103FBut, Congressman Gebal … …\x02\x03",
            "#00108FI was supposed to be chased from work\x01",
            "Among the lawmakers,\x01",
            "It may be still better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FYes, after a cult incident\x01",
            "The arrested parliamentarians\x01",
            "I think there are more severe situations.\x02\x03",
            "#10103FI think that it is obviously a reward,\x01",
            "Human beings who were danced, somewhere\x01",
            "I do not think I'm satisfied.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FOh, but after all,\x01",
            "Someday the bad things bounce back to me …\x01",
            "That would be worldwide.\x02\x03",
            "#00000FOn the other hand, if you are trying to get over it,\x01",
            "The day will always come to be rewarded.\x02\x03",
            "#00004FEven if that ghebal san\x01",
            "Even for the campaign members,\x01",
            "I hope someday that will happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103FI see …\x01",
            "(Ernest also someday … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHe is the leader.\x01",
            "Something to say is ok.\x02\x03",
            "#10302FHow about now, talk to the story\x01",
            "In this way Trinity\x01",
            "Why do you take a cup as you go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FHuh, during work\x01",
            "I could not do that.\x02\x03",
            "#00000F……Anyways.\x01",
            "これでold Townの調査は終了だ。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x6A, 0x1, 0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A50F")
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
            "【There is still a rest】\x01",              # 0
            "【Confirmation of 6 places ended】\x01",      # 1
            "【It does not change】\x01",                  # 2
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
        (0, "loc_A4E2"),
        (1, "loc_A4F6"),
        (2, "loc_A50A"),
        (SWITCH_DEFAULT, "loc_A50F"),
    )


    label("loc_A4E2")

    ClearScenarioFlags(0x131, 5)
    ClearScenarioFlags(0x131, 6)
    ClearScenarioFlags(0x131, 7)
    ClearScenarioFlags(0x132, 0)
    ClearScenarioFlags(0x132, 1)
    Jump("loc_A50F")

    label("loc_A4F6")

    SetScenarioFlags(0x131, 5)
    SetScenarioFlags(0x131, 6)
    SetScenarioFlags(0x131, 7)
    SetScenarioFlags(0x132, 0)
    SetScenarioFlags(0x132, 1)
    Jump("loc_A50F")

    label("loc_A50A")

    Jump("loc_A50F")

    label("loc_A50F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A564")

    ChrTalk(
        0x101,
        (
            "#6P#00000FAll right, then\x01",
            "We will continue to investigate.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A5B6")

    label("loc_A564")

    OP_29(0x6A, 0x1, 0x6)

    ChrTalk(
        0x101,
        (
            "#6P#00000FOK, this is the end of the investigation.\x02\x03",
            "Let's return to the municipal hall.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A5B6")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_71(0x3, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x3, 0x10)
    SetScenarioFlags(0x132, 2)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 9630, 0, 4460, 225)
    EventEnd(0x5)
    Return()

    # Function_47_9EB7 end

    def Function_48_A5EE(): pass

    label("Function_48_A5EE")

    EventBegin(0x0)
    Fade(500)
    OP_68(43660, -1700, -21280, 0)
    MoveCamera(37, 21, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(21420, 0)
    SetChrPos(0x101, 42460, -2500, -21980, 45)
    SetChrPos(0x102, 43410, -2500, -23070, 45)
    SetChrPos(0x104, 43290, -2500, -24550, 45)
    SetChrPos(0x109, 41320, -2500, -22550, 45)
    SetChrPos(0x105, 41680, -2500, -23920, 45)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#11POh, you guys …\x01",
            "What is it for?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PAnd there are those …\x01",
            "Wow, Wadi! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PCut …!\x01",
            "Ahh, this bastard!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10308FWhew ……\x01",
            "It is hated very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F…… I understand your feelings\x01",
            "Let me tell you a bit.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "At the request of Professor Lloyd\x01",
            "I explained the circumstances of collecting the questionnaire table.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        "#11PMonth leopard ……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P…… Oh, at Ursula hospital\x01",
            "I was handed over when I was passing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00305FWhat, you forgot it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHmm, the impact of medicines\x01",
            "I have not left at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PNo need to bother\x01",
            "It is too bad to go to the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00101FDinoくん……\x01",
            "Self-judgment is not good.\x02\x03",
            "#00103FIf the symptoms remain in the unlikely event,\x01",
            "Everyone in Viper also inconveniences\x01",
            "I might get it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PWell … it certainly is, but …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P…… Oh, I already understood!\x01",
            "Please wait there for a moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PBecause I got it somewhere,\x01",
            "I write it in a hurry and bring it.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AA0C():
        OP_95(0xFE, 44930, -2500, -22750, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_AA0C)
    WaitChrThread(0x8, 1)

    def lambda_AA2A():
        OP_95(0xFE, 47960, -2100, -22440, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_AA2A)
    Sleep(50)

    def lambda_AA47():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AA47)
    Sleep(50)

    def lambda_AA57():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AA57)
    Sleep(50)

    def lambda_AA67():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AA67)
    Sleep(50)

    def lambda_AA77():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_AA77)
    Sleep(50)

    def lambda_AA87():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_AA87)
    WaitChrThread(0x8, 1)
    Sound(116, 0, 100, 0)
    ClearMapObjFlags(0x4, 0x10)
    OP_71(0x4, 0x0, 0x10, 0x0, 0x0)
    OP_79(0x0)
    Sleep(700)

    def lambda_AAB6():
        OP_97(0xFE, 0x7D0, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_AAB6)

    def lambda_AAD0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_AAD0)
    WaitChrThread(0x8, 2)
    SetChrFlags(0x8, 0x80)
    OP_0D()

    ChrTalk(
        0x109,
        "#6P#10106FYou seem to be able to recover somehow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FOh, are you waiting for a while?\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x8, 0x80)
    OP_71(0x4, 0x10, 0x0, 0x0, 0x0)
    OP_79(0x0)
    SetMapObjFlags(0x4, 0x10)
    SetChrPos(0x8, 44880, -2500, -20090, 225)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_93(0x101, 0x2D, 0x0)
    OP_93(0x102, 0x2D, 0x0)
    OP_93(0x104, 0x2D, 0x0)
    OP_93(0x109, 0x2D, 0x0)
    OP_93(0x105, 0x2D, 0x0)
    Sleep(1000)
    Sound(117, 0, 100, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        "#11P…… Hora, is this OK?\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '迪诺的问诊表'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('迪诺的问诊表', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#6P#00000FOh, it certainly got it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00100Fありがとう、Dinoくん。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P…… Hmm, I will thank you\x01",
            "You do not have squeaks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PCome on, take me quickly\x01",
            "Say somewhere! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00006FBecause, I knew.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10303F… … You got in the way.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x152, 3)
    OP_29(0x70, 0x1, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ADE4")

    AnonymousTalk(
        0x101,
        (
            "#00000FWith this, all the questionnaire charts\x01",
            "I finished collecting it.\x02\x03",
            "Immediately to Professor Seyland\x01",
            "Let's suppose that we will go reporting.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_29(0x70, 0x1, 0x5)

    label("loc_ADE4")

    OP_93(0x8, 0xE1, 0x0)
    OP_4C(0x8, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 43610, -2500, -21900, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_48_A5EE end

    def Function_49_AE11(): pass

    label("Function_49_AE11")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-2990, 1930, -22180, 0)
    MoveCamera(44, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(40910, 0)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x16, 0x8000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_AE8B")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x1A2, 0x80)
    Jump("loc_AECA")

    label("loc_AE8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_AEAD")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x1A2, 0x80)
    Jump("loc_AECA")

    label("loc_AEAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_AECA")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x1A2, 0x80)

    label("loc_AECA")

    OP_68(-2990, 1930, -22180, 5000)
    MoveCamera(44, 22, 0, 5000)
    OP_6E(500, 5000)
    SetCameraDistance(49730, 5000)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_AFD6")
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x104, 0x80)
    ClearChrFlags(0x1A2, 0x80)
    SetChrPos(0x1A2, 2260, 0, 22750, 180)
    SetChrPos(0x102, 1410, 0, 22750, 180)
    SetChrPos(0x101, 2900, 0, 24450, 180)
    SetChrPos(0x104, 910, 0, 24450, 180)

    def lambda_AF68():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_AF68)

    def lambda_AF82():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AF82)
    Sleep(100)

    def lambda_AF9F():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AF9F)
    Sleep(50)

    def lambda_AFBC():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AFBC)
    Jump("loc_B179")

    label("loc_AFD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_B0AA")
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x109, 0x80)
    ClearChrFlags(0x1A2, 0x80)
    SetChrPos(0x1A2, 2260, 0, 22750, 180)
    SetChrPos(0x102, 1410, 0, 22750, 180)
    SetChrPos(0x101, 2900, 0, 24450, 180)
    SetChrPos(0x109, 910, 0, 24450, 180)

    def lambda_B03C():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_B03C)

    def lambda_B056():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B056)
    Sleep(100)

    def lambda_B073():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B073)
    Sleep(50)

    def lambda_B090():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B090)
    Jump("loc_B179")

    label("loc_B0AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_B179")
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x105, 0x80)
    ClearChrFlags(0x1A2, 0x80)
    SetChrPos(0x1A2, 2260, 0, 22750, 180)
    SetChrPos(0x102, 1410, 0, 22750, 180)
    SetChrPos(0x101, 2900, 0, 24450, 180)
    SetChrPos(0x105, 910, 0, 24450, 180)

    def lambda_B110():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_B110)

    def lambda_B12A():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B12A)
    Sleep(100)

    def lambda_B147():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B147)
    Sleep(50)

    def lambda_B164():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B164)

    label("loc_B179")

    OP_6F(0x79)
    OP_68(2000, 1930, 2050, 7000)
    MoveCamera(41, 21, 0, 7000)
    OP_6E(500, 7000)
    SetCameraDistance(17730, 7000)
    OP_6F(0x79)

    ChrTalk(
        0x1A2,
        (
            "here……\x01",
            "It is a deserted place for a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F……old Townよ。\x01",
            "It is a place left behind development.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x1A2)

    ChrTalk(
        0x1A2,
        (
            "Hun … like this\x01",
            "Really there are also in every country.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        "#12Pもう十分だ、East Streetに戻るぞ。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FOh, oh … I got it.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0x12, 0x8000)
    ClearChrFlags(0x16, 0x8000)
    SetScenarioFlags(0x1C5, 4)
    OP_29(0x73, 0x1, 0x8)
    SetScenarioFlags(0x23, 0)
    NewScene("c1000", 111, 0, 0)
    IdleLoop()
    Return()

    # Function_49_AE11 end

    def Function_50_B2F5(): pass

    label("Function_50_B2F5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch46500.itc", 0x1E)
    LoadChrToIndex("apl/ch51270.itc", 0x1F)
    LoadChrToIndex("apl/ch51271.itc", 0x20)
    LoadChrToIndex("chr/ch30850.itc", 0x21)
    LoadChrToIndex("chr/ch31750.itc", 0x22)
    LoadChrToIndex("chr/ch23900.itc", 0x23)
    SoundLoad(849)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13900.itp")
    OP_68(960, 2000, 7700, 0)
    MoveCamera(37, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16940, 0)
    SetChrPos(0x101, 2450, 0, 12000, 180)
    SetChrPos(0x102, 1250, 0, 12000, 180)
    SetChrPos(0x104, 2260, 0, 13650, 180)
    SetChrPos(0x109, 3460, 0, 13650, 180)
    SetChrPos(0x105, 1060, 0, 13650, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    def lambda_B3E5():
        OP_95(0xFE, 2450, 0, 8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B3E5)
    Sleep(10)

    def lambda_B402():
        OP_95(0xFE, 1250, 0, 8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B402)
    Sleep(20)

    def lambda_B41F():
        OP_95(0xFE, 2260, 0, 9650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B41F)
    Sleep(10)

    def lambda_B43C():
        OP_95(0xFE, 3460, 0, 9650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B43C)
    Sleep(20)

    def lambda_B459():
        OP_95(0xFE, 1060, 0, 9650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B459)
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    SetChrChipByIndex(0x18, 0x1F)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0x18, -9420, 6230, -3210, 90)
    SetChrPos(0xD, 380, 0, -2000, 90)
    SetChrPos(0xE, 3610, 0, -2000, 270)
    StopBGM(0xBB8)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x105, 1)

    NpcTalk(
        0xD,
        "Voice of a man",
        "#4S… …., Kora!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xE,
        "Voice of a man",
        (
            "#4SAh! Is it? Complain\x01",
            "I do not mean to say that!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7517", 0)

    ChrTalk(
        0x101,
        "#00005FThis voice ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FLloyd, that!\x02",
    )

    CloseMessageWindow()
    OP_68(850, 2000, -2600, 3000)
    MoveCamera(39, 25, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(16810, 3000)
    OP_6F(0x79)

    ChrTalk(
        0xD,
        (
            "#6Pてめえ、Slash……\x01",
            "Are you thinking about it! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#6PあのままWaldさんが酒に溺れて\x01",
            "What do you do if you break your body, A! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "So, I do not think so\x01",
            "I will be thinking about various ideas! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I can not think of anything.\x01",
            "Crisp and cool!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#6PLater, \"If you look at the scenery above the tower,\x01",
            "Do not hesitate to fix Kisuga \"\x01",
            "That thing that I lightly pulled out! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#6PWaldさんの機嫌が\x01",
            "If it gets fixed at about a high place\x01",
            "Nobody is having trouble! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#6P#4SWith an idiot like you\x01",
            "Do not stay with me, you idiot!\x01",
            "This idiot! It is!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xE, 0x21)
    SetChrSubChip(0xE, 0x0)
    OP_0D()

    ChrTalk(
        0xE,
        (
            "#4SWell, Tzeze ~! It is!\x01",
            "I told you three times, Kora! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#4SI will not have any good ideas\x01",
            "I am one hundred times what you are!\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    Sound(540, 0, 50, 0)
    SetChrChipByIndex(0xD, 0x22)
    SetChrSubChip(0xD, 0x0)
    OP_0D()

    ChrTalk(
        0xD,
        "#6P… …! It is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#6P#4SLet's do it, Ah! Is it?\x02",
    )

    CloseMessageWindow()
    Sleep(100)

    ChrTalk(
        0x101,
        "#5P#N#4S#00007FStop it, you guys!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_68(280, 2000, -1490, 3000)
    MoveCamera(36, 20, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(15650, 3000)

    def lambda_B986():
        OP_95(0xFE, 2450, 0, 500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B986)
    Sleep(10)

    def lambda_B9A3():
        OP_95(0xFE, 1250, 0, 500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B9A3)
    Sleep(20)

    def lambda_B9C0():
        OP_95(0xFE, 2260, 0, 2150, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B9C0)
    Sleep(10)

    def lambda_B9DD():
        OP_95(0xFE, 3460, 0, 2150, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B9DD)
    Sleep(20)

    def lambda_B9FA():
        OP_95(0xFE, 1060, 0, 2150, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B9FA)
    Sleep(200)
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_BA3E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_BA3E)
    Sleep(10)

    def lambda_BA4E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_BA4E)
    WaitChrThread(0x105, 1)
    WaitChrThread(0xD, 1)
    OP_6F(0x79)

    ChrTalk(
        0xE,
        "#12PTogether …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00301FCome on, brothers\x01",
            "To bring out weapons,\x01",
            "Is not he like me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#12PHappy\x01",
            "It does not matter to Tame!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#12PSpeaking of origin … Wadi! It is!\x01",
            "Temple is a huge man\x01",
            "Because of letting go …! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#12PThat's it……!\x01",
            "Waldさんがあんなことに\x01",
            "It is because of Wadi that I came down!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#12PEverything is bad, Wasi!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#5P#10303F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#10105FWait a moment, please!\x01",
            "Waji you …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#12PAnyway, it will not fit as it is … …\x01",
            "First of all I will try to craze the temples! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#12PHiakha, I see!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#12PHuey、てめえを\x01",
            "It's after that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#00101F(What do you do, Lloyd …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#00301F(Why does my blood come up to my head completely?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00010F(Come on, become like this\x01",
            "Only to control by us … …)\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x3C, 0x1F4)
    Sound(849, 0, 100, 0)
    Sleep(1000)
    OP_63(0xE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(10)
    OP_63(0xD, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(20)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(10)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    NpcTalk(
        0x18,
        "Voice of a young man",
        (
            "Hydrofluoric acid\x01",
            "It is sad.\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x64, 0x7D0)
    OP_68(-7930, 6500, -5030, 6000)
    MoveCamera(41, 31, 0, 6000)
    OP_6E(500, 6000)
    SetCameraDistance(14890, 6000)
    Sleep(500)

    def lambda_BEA8():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BEA8)
    Sleep(10)

    def lambda_BEB8():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BEB8)
    Sleep(20)

    def lambda_BEC8():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BEC8)
    Sleep(10)

    def lambda_BED8():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_BED8)
    Sleep(20)

    def lambda_BEE8():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_BEE8)
    Sleep(10)

    def lambda_BEF8():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_BEF8)
    Sleep(10)

    def lambda_BF08():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_BF08)
    OP_6F(0x79)
    Sleep(1000)
    Fade(1000)
    OP_68(-9650, 6900, -3210, 0)
    MoveCamera(305, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(13930, 0)
    OP_0D()
    StopBGM(0xFA0)

    NpcTalk(
        0x18,
        "Blond hair youth",
        (
            "#5P#13904FNo conflict will produce anything ……\x01",
            "I just spin a chain of silly hatred.\x02\x03",
            "#13902FLet's give such songs to you.\x02\x03",
            "Unraveling chaotic heart\x01",
            "As long as you tie people together,\x01",
            "Such kindly sad song ……\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Fade(500)
    SetChrFlags(0x18, 0x2)
    SetChrFlags(0x18, 0x10)
    SetChrFlags(0x18, 0x20)
    SetChrChipByIndex(0x18, 0x20)
    SetChrSubChip(0x18, 0x0)
    BeginChrThread(0x18, 0, 0, 51)
    OP_52(0x18, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x19, 0x23)
    SetChrPos(0x19, -17200, 5400, -6800, 45)
    BeginChrThread(0x19, 0, 0, 52)
    OP_52(0x19, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    Sleep(10)
    PlayBGM("ed7578", 1)
    Sleep(1000)

    NpcTalk(
        0x18,
        "Blond hair youth",
        "#70A#50WTo go flow#1500WIn the case of#50WStar#1000WIn the case of#50WThe trajectory ……\x05\x02",
    )

    Sleep(7000)

    NpcTalk(
        0x18,
        "Blond hair youth",
        "#70A#50WA guide#1000WIn the case of#50WContinue to you …\x05\x02",
    )

    Sleep(7000)

    NpcTalk(
        0x18,
        "Blond hair youth",
        "#70A#50WIf you get burned#1500WIn the case of#50Wthought#1000WIn the case of#50WTearing my chest ……\x05\x02",
    )

    Sleep(7000)

    NpcTalk(
        0x18,
        "Blond hair youth",
        "#70A#50WPainfulness#1000WIn the case of#50WThe moon laughs ……\x05\x02",
    )

    Sleep(7000)

    NpcTalk(
        0x18,
        "Blond hair youth",
        "#70A#50WThere is nothing to come true#3000WIn the case of#50WIf it is ephemeral … …\x05\x02",
    )

    WaitChrThread(0x19, 1)
    Sleep(1000)
    OP_57(0x0)
    OP_5A()
    OP_99(0x19, 0x18, 0xFA, 0x2710, 0x0)
    Sound(809, 0, 30, 0)
    OP_9B(0x1, 0x19, 0xB4, 0x3E8, 0x2710, 0x0)
    Sound(811, 0, 100, 0)
    StopBGM(0x3E8)
    Sleep(500)
    Fade(500)
    EndChrThread(0x18, 0x0)
    ClearChrFlags(0x18, 0x2)
    ClearChrFlags(0x18, 0x10)
    ClearChrFlags(0x18, 0x20)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x6)
    SetChrSubChip(0xE, 0x0)
    SetChrPos(0xD, 1000, 0, -2000, 270)
    SetChrPos(0xE, 2400, 0, -2000, 270)
    OP_0D()
    WaitBGM()
    PlayBGM("ed7518", 0)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x19,
        "#4S…… Hey, I'm lucky! It is!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Blond hair youth",
        "#12P#13911FMumbo ……! Is it?\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(1000)
    OP_68(-9170, 6600, -2680, 0)
    MoveCamera(42, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16370, 0)
    OP_0D()
    OP_63(0x18, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)
    OP_93(0x18, 0x10E, 0x1F4)
    Sleep(1000)
    OP_64(0x18)

    NpcTalk(
        0x18,
        "Blond hair youth",
        (
            "#11P#13909FWell, what's up?\x01",
            "Cute kitten.\x02\x03",
            "#13902FHurry, as you can see while playing.\x01",
            "If it is bad, but please sign up later.\x02\x03",
            "#13910FOr, if you are kicked in such a place\x01",
            "Indeed dangerous ----\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x19,
        "#6PDo not mess up!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#6PBecause it is me-wak at the store,\x01",
            "Hurry up!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_99(0x19, 0x18, 0xFA, 0x2710, 0x0)
    Sound(809, 0, 30, 0)
    OP_63(0x18, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_9B(0x1, 0x19, 0xB4, 0x3E8, 0x2710, 0x0)
    Sound(811, 0, 100, 0)
    Sleep(500)
    OP_93(0x18, 0x13B, 0x0)
    OP_9D(0x18, 0xFFFFD814, 0x1900, 0xFFFFF8B2, 0x15E, 0x7D0)
    Sound(50, 0, 100, 0)
    Sleep(500)
    OP_93(0x18, 0x10E, 0x0)
    OP_9D(0x18, 0xFFFFCFB8, 0x1518, 0xFFFFFCA4, 0xFA, 0xBB8)
    Sound(30, 0, 100, 0)
    Sleep(500)
    OP_93(0x18, 0xB4, 0x1F4)

    NpcTalk(
        0x18,
        "Blond hair youth",
        (
            "#13911FI know,\x01",
            "Because I understood it already - ─ ─\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x19, 0x10E, 0x1F4)
    OP_9D(0x19, 0xFFFFCFB8, 0x1518, 0xFFFFF4A2, 0xFA, 0xBB8)
    Sound(30, 0, 100, 0)
    OP_93(0x19, 0x0, 0x1F4)
    OP_99(0x19, 0x18, 0xFA, 0x2710, 0x0)
    Sound(809, 0, 30, 0)
    OP_9B(0x1, 0x19, 0xB4, 0x3E8, 0x2710, 0x0)
    Sound(811, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x19,
        "#12POoooo!\x02",
    )

    CloseMessageWindow()

    def lambda_C5A9():
        OP_95(0xFE, -17240, 5400, -1780, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_C5A9)
    Sleep(800)
    OP_95(0x19, -16880, 5400, -1950, 4000, 0x0)
    Sleep(1000)
    Sound(1013, 0, 100, 0)

    NpcTalk(
        0x18,
        "Voice of a young man",
        "#2SOh……! Is it?\x02",
    )

    CloseMessageWindow()
    Sound(833, 0, 40, 0)
    Sound(992, 0, 40, 0)
    Sleep(50)
    Sound(811, 0, 100, 0)

    ChrTalk(
        0x19,
        "#2S… … Oh, it fell.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#2SAre you alive, Kimpa?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Voice of a young man",
        "#2SMother's Day\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#2S…… I'm alive.\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x19, 0x80)
    OP_64(0x18)
    Sleep(500)
    Fade(1000)
    OP_68(280, 2000, -1490, 0)
    MoveCamera(36, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15650, 0)
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    SetChrFlags(0x9, 0x8000)
    OP_0D()
    Sleep(1000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)
    OP_64(0xD)
    OP_64(0xE)
    OP_93(0xD, 0x0, 0x1F4)

    ChrTalk(
        0xD,
        "#12POh … what the hell.\x02",
    )

    CloseMessageWindow()

    def lambda_C78C():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C78C)
    Sleep(10)

    def lambda_C79C():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C79C)
    Sleep(20)

    def lambda_C7AC():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C7AC)
    Sleep(10)

    def lambda_C7BC():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C7BC)
    Sleep(20)

    def lambda_C7CC():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C7CC)

    ChrTalk(
        0xD,
        "#12PSomething has turned white, I will go home.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#12P#5AHiha, what is that blond hair ……\x02",
    )

    CloseMessageWindow()
    OP_93(0xD, 0x5A, 0x1F4)
    OP_99(0xD, 0xE, 0x1F4, 0x1388, 0x0)
    Sound(811, 0, 60, 0)
    OP_9B(0x1, 0xD, 0xB4, 0xC8, 0x1388, 0x0)

    ChrTalk(
        0xE,
        "#12PTo struggle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#6P… … Good, so I will go home.\x02",
    )

    CloseMessageWindow()

    def lambda_C889():
        OP_95(0xFE, 6640, 0, -7350, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_C889)
    Sleep(800)

    def lambda_C8A6():
        OP_95(0xFE, 7700, 0, -7010, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_C8A6)

    def lambda_C8C0():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C8C0)
    Sleep(50)

    def lambda_C8D0():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C8D0)
    Sleep(50)

    def lambda_C8E0():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C8E0)
    Sleep(50)

    def lambda_C8F0():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C8F0)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xE, 1)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)

    ChrTalk(
        0x101,
        "#5P#00012FHe ran away … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#5P#10306F… …. In a way\x01",
            "Have I been rescued?\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x18, -3400, 0, -6690, 0)

    NpcTalk(
        0x18,
        "Voice of a young man",
        (
            "フ、Hydrofluoric acid\x01",
            "It is supposed to bloom in the demonic city\x01",
            "I picked up the bud of conflict.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C9C0():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C9C0)
    Sleep(50)

    def lambda_C9D0():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C9D0)
    Sleep(50)

    def lambda_C9E0():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C9E0)
    Sleep(50)

    def lambda_C9F0():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C9F0)
    Sleep(50)

    def lambda_CA00():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_CA00)

    NpcTalk(
        0x18,
        "Voice of a young man",
        (
            "Bring peace with love and sincerity\x01",
            "Examination of my lute … ….\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Voice of a young man",
        (
            "My talent is\x01",
            "Sometimes it will be horrible.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(980, 2000, 1730, 0)
    MoveCamera(142, 31, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16810, 0)
    OP_0D()
    OP_96(0x18, 0xFFFFF132, 0x0, 0xFFFFE624, 0x7D0, 0x0)
    OP_96(0x18, 0xFFFFF772, 0x0, 0xFFFFE570, 0x7D0, 0x0)
    OP_96(0x18, 0xFFFFF646, 0x0, 0xFFFFEC96, 0x7D0, 0x0)

    def lambda_CAF0():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_CAF0)
    OP_96(0x18, 0xFFFFFD4E, 0x0, 0xFFFFECB4, 0x3E8, 0x0)

    def lambda_CB11():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_CB11)
    OP_96(0x18, 0xFFFFFC68, 0x0, 0xFFFFF330, 0x7D0, 0x0)

    def lambda_CB32():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_CB32)
    OP_96(0x18, 0x320, 0x0, 0xFFFFF416, 0x5DC, 0x0)

    def lambda_CB53():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_CB53)
    OP_96(0x18, 0x654, 0x0, 0xFFFFFA10, 0x3E8, 0x0)

    def lambda_CB74():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CB74)
    Sleep(50)

    def lambda_CB84():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CB84)
    Sleep(50)

    def lambda_CB94():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_CB94)
    Sleep(50)

    def lambda_CBA4():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_CBA4)
    Sleep(50)

    def lambda_CBB4():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_CBB4)
    OP_93(0x18, 0x0, 0x1F4)
    EndChrThread(0x18, 0x1)
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
        0x102,
        (
            "#6P#00105FOh, that … … Is it okay?\x01",
            "What was that about a while ago?\x01",
            "I heard a dull sound, though.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Blond hair youth",
        (
            "#11P#13904FHood, do not worry,\x01",
            "Mademoiselle.\x02\x03",
            "#13902FSuch as the height etc,\x01",
            "Try to run through the sky of the continent right now\x01",
            "It is not a terrible thing to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00306FI do not understand the meaning …\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Blond hair youth",
        (
            "#11P#13903FA little trouble\x01",
            "I have been hit by … …\x02\x03",
            "#13900FRewrite your mind and continue\x01",
            "I will show off.\x02\x03",
            "#13904FHurry, enjoy yourself.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x18, 0x1F)
    SetChrSubChip(0x18, 0x0)
    OP_0D()

    ChrTalk(
        0x101,
        "#6P#00011FOf course it is fine!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106F(B, Lloyd.\x01",
            "Perhaps this person … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001F(Oh, white coat on blond … …)\x02\x03",
            "#00006F(Mr. Muller\x01",
            "I was told that he was a troublesome person … …\x01",
            "To be honest, it is more than expected. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001F…… Kohon.\x01",
            "あなたは、Olivierさんで\x01",
            "There is no mistake, is it?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Blond hair youth",
        "#11P#13904FHydrofluoric …… very much.\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("Blond hair youth")

    AnonymousTalk(
        0xFF,
        (
            "Journey in search of love\x01",
            "A musical performer who made a genius of unprecedented,\x01",
            "Olivier・レンハイムだ。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x18,
        (
            "Huh, you guys are in luck.\x01",
            "To this genius guerrilla recital\x01",
            "I was able to encounter it.\x02\x03",
            "Please engrave the day of today to its heart,\x01",
            "Please make it a lifetime memory.\x02",
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
        "#6P#00006F… … Haha.\x02",
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x18)
    OP_63(0x18, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    OP_0D()

    ChrTalk(
        0x18,
        (
            "#11P#13905FAle, by the way ….\x01",
            "Why do you know that name?\x02\x03",
            "#13902FAfter entering the crossbell\x01",
            "I did not intend to memorize it.\x01",
            "… … Have you met anywhere?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FWe are Crossbell Police,\x01",
            "It is a person of the affairs support department.\x02\x03",
            "At the request of Mr. Muller\x01",
            "I was looking for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FTo your acquaintance\x01",
            "Is it correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11P#13905FRumors, you guys are …\x02\x03",
            "#13904FHydrofluoric acid\x01",
            "Muller's worry as ever.\x02\x03",
            "#13912FTo this extent\x01",
            "Where I spent separately,\x01",
            "Our love will not fade away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10105FWhat!\x01",
            "Well, is that such a relationship …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00306F… … No, probably not.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FAnd anyway … …\x01",
            "To Mr. Muller\x01",
            "Could you please come back?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11P#13903F… … It's bad, but that request\x01",
            "I can not afford to hear it.\x02\x03",
            "#13900FAnyway, I will be busy tomorrow.\x01",
            "Now I will cross this bell\x01",
            "I want to fully enjoy it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00105FBecome busy …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11P#13904FHuh, this story.\x02\x03",
            "If you\x01",
            "I have to miss that\x01",
            "In other words …\x02\x03",
            "#13902FWhatever hands you use\x01",
            "Shall I miss it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FOh ….?\x01",
            "What am I supposed to do?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0x87, 0x1F4)
    OP_63(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x18,
        (
            "#12P#13907F#4SHappy …!\x01",
            "That's over there Yuria Assoc! Is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)

    def lambda_D6F5():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D6F5)
    Sleep(10)

    def lambda_D705():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D705)
    Sleep(20)

    def lambda_D715():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D715)
    Sleep(10)

    def lambda_D725():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D725)
    Sleep(20)

    def lambda_D735():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D735)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00011FBecome Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00105FWell ……! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10107F#4SWhere are you! Is it?\x02",
    )

    CloseMessageWindow()
    OP_68(8520, 2000, -12850, 3000)
    MoveCamera(45, 27, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(24500, 3000)
    OP_6F(0x79)

    ChrTalk(
        0x109,
        (
            "#10105FOh, oh, that … ….\x01",
            "There is no one but ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F…… Ha ha!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(1000)
    OP_68(1810, 1560, 4120, 0)
    MoveCamera(49, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21950, 0)
    SetChrPos(0x18, 1900, 0, 8440, 180)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)

    def lambda_D8EC():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D8EC)
    Sleep(10)

    def lambda_D8FC():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D8FC)
    Sleep(20)

    def lambda_D90C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D90C)
    Sleep(10)

    def lambda_D91C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D91C)
    Sleep(20)

    def lambda_D92C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D92C)
    Sleep(500)

    ChrTalk(
        0x18,
        (
            "#5P#13902FHuh, I can see you again\x01",
            "I am looking forward to it!\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_63(0x18, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_93(0x18, 0x0, 0x1F4)

    def lambda_D993():
        OP_95(0xFE, 1900, 0, 20650, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_D993)
    Sleep(500)

    ChrTalk(
        0x101,
        "#12P#00011FWait a minute … …!\x02",
    )

    CloseMessageWindow()
    OP_68(1070, 1560, 2280, 3000)
    SetCameraDistance(17880, 3000)
    WaitChrThread(0x18, 1)
    OP_64(0x18)
    SetChrFlags(0x18, 0x80)
    OP_6F(0x1)
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
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7101", 0)

    ChrTalk(
        0x102,
        "#12P#00106FI ran away … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#11P#10101FIn such a classic hand\x01",
            "I was caught … …\x02\x03",
            "#10106FAssociate Professor Julia Julia\x01",
            "In such a place\x01",
            "I do not think so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00306FWhew, what is Lecta\x01",
            "In another sense it seems to be a nasty older brother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FAnyway\x01",
            "Do you want to chase after that?\x02\x03",
            "#00003FEven so,\x01",
            "Where have you gone ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10303FAfter all, the place I was talking about\x01",
            "It is a thing to try as one\x01",
            "It might be nice.\x02\x03",
            "#10300Fold Townで見つけたから、\x01",
            "If there are other candidates … …\x01",
            "Back streetかHarbor district、かな？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#11P#10100FAnyway, let's look for it!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 2029, 0, 250, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    ClearChrFlags(0x9, 0x8000)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x156, 2)
    OP_29(0x76, 0x1, 0x2)
    EventEnd(0x5)
    Return()

    # Function_50_B2F5 end

    def Function_51_DCEF(): pass

    label("Function_51_DCEF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DD3E")
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x4)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    Jump("Function_51_DCEF")

    label("loc_DD3E")

    Return()

    # Function_51_DCEF end

    def Function_52_DD3F(): pass

    label("Function_52_DD3F")

    Sleep(23000)
    OP_95(0xFE, -12870, 5400, -2670, 1000, 0x0)
    OP_93(0xFE, 0x5A, 0x0)
    Sleep(4000)
    OP_9D(0xFE, 0xFFFFD4AE, 0x1900, 0xFFFFF466, 0x4B0, 0xBB8)
    Sound(50, 0, 100, 0)
    Return()

    # Function_52_DD3F end

    def Function_53_DD7E(): pass

    label("Function_53_DD7E")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Apartment \"Maison Imerda\"\x01\x01",
            "~ Currently out of operation ~\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('伊梅尔达馆的钥匙', 0x0)"), scpexpr(EXPR_END)), "loc_DE93")
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Do you use the key of Maison Imelda?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DE8E")
    OP_5A()
    Sleep(500)
    Sound(806, 0, 100, 0)
    Sleep(1000)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I opened the key of \"Maison Imerda\".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_29(0x67, 0x1, 0x1)
    SetScenarioFlags(0x133, 1)
    SetMapObjFlags(0x1, 0x10)
    OP_65(0x1, 0x1)

    label("loc_DE8E")

    Jump("loc_E02B")

    label("loc_DE93")

    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DFA7")

    ChrTalk(
        0x101,
        "#00000F… It seems locked.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FMysteriously exterminated in this apartment\x01",
            "There was a request for assistance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FSurely, the manager\x01",
            "Shop owner of antique shop\x01",
            "It was \"Madame Imeda\".\x02\x03",
            "#00000FBack streetにある\x01",
            "To the antique shop\x01",
            "Let's borrow the key.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_E02B")

    label("loc_DFA7")


    ChrTalk(
        0x101,
        (
            "#00000FIn this apartment\x01",
            "Request for support of devil elimination\x01",
            "It should have been included.\x02\x03",
            "#00000FBack streetにある\x01",
            "To the antique shop\x01",
            "Let's borrow the key.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E02B")

    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_53_DD7E end

    SaveToFile()

Try(main)
