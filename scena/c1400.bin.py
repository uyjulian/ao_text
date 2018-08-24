from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Dino",                   # 1
        "Grandma Paola",          # 2
        "Vaan",                   # 3
        "Roser",                  # 4
        "Kanon",                  # 5
        "Huey",                   # 6
        "Slash",                  # 7
        "Kientz",                 # 8
        "Veysset",                # 9
        "Abbas",                  # 10
        "Sister Ries",            # 11
        "Bacchus",                # 12
        "Rimah",                  # 13
        "Melson",                 # 14
        "Policeman",              # 15
        "Wald",                   # 16
        "Olivier",                # 17
        "Jingo",                  # 18
        "bc1400",                 # 19
        "Central Square",         # 20
        "West Street",            # 21
        "Governmental District",  # 22
        "Residential Street",     # 23
        "Entertainment District", # 24
        "East Street",            # 25
        "Downtown",               # 26
        "Waterfront Area",        # 27
        "IBC",                    # 28
        "Station Street",         # 29
        "Back Street",            # 30
        "St. Ursula Byroad",      # 31
        "East Crossbell Highway", # 32
        "West Crossbell HIghway", # 33
        "Mainz Mountain Road",    # 34
        "Orchis Tower",           # 35
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

    PlaceName(-110.69000244140625, 0.0, 106.94999694824219, 0x0000, 0x0000, "Central Square")
    PlaceName(-186.3000030517578, 0.0, 112.12999725341797, 0x0000, 0x0000, "West Street")
    PlaceName(-79.63999938964844, 0.0, 209.3000030517578, 0x0000, 0x0000, "Governmental District")
    PlaceName(-256.45001220703125, 0.0, 197.8000030517578, 0x0000, 0x0000, "Residential Street")
    PlaceName(-172.5, 0.0, 188.60000610351562, 0x0000, 0x0000, "Entertainment District")
    PlaceName(-17.25, 0.0, 80.5, 0x0000, 0x0000, "East Street")
    PlaceName(23.579999923706055, 0.0, 17.25, 0x0000, 0x0000, "Downtown")
    PlaceName(14.949999809265137, 0.0, 156.39999389648438, 0x0000, 0x0000, "Waterfront Area")
    PlaceName(-14.949999809265137, 0.0, 264.5, 0x0000, 0x0000, "IBC")
    PlaceName(-97.75, 0.0, 27.600000381469727, 0x0000, 0x0000, "Station Street")
    PlaceName(-151.8000030517578, 0.0, 147.1999969482422, 0x0000, 0x0000, "Back Street")
    PlaceName(-101.19999694824219, 0.0, -8.050000190734863, 0x0000, 0x0000, "St. Ursula Byroad")
    PlaceName(44.849998474121094, 0.0, 96.5999984741211, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-244.9499969482422, 0.0, 110.4000015258789, 0x0000, 0x0000, "West Crossbell HIghway")
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
        "Function_8_1AAE",         # 08, 8
        "Function_9_2183",         # 09, 9
        "Function_10_26C0",        # 0A, 10
        "Function_11_2A71",        # 0B, 11
        "Function_12_34E6",        # 0C, 12
        "Function_13_3562",        # 0D, 13
        "Function_14_3621",        # 0E, 14
        "Function_15_3628",        # 0F, 15
        "Function_16_3632",        # 10, 16
        "Function_17_3B53",        # 11, 17
        "Function_18_3C4F",        # 12, 18
        "Function_19_3DA3",        # 13, 19
        "Function_20_3E70",        # 14, 20
        "Function_21_3F33",        # 15, 21
        "Function_22_3F7B",        # 16, 22
        "Function_23_3FC4",        # 17, 23
        "Function_24_405D",        # 18, 24
        "Function_25_40C6",        # 19, 25
        "Function_26_49E7",        # 1A, 26
        "Function_27_4ABA",        # 1B, 27
        "Function_28_4ABB",        # 1C, 28
        "Function_29_4FBF",        # 1D, 29
        "Function_30_5032",        # 1E, 30
        "Function_31_50A5",        # 1F, 31
        "Function_32_5118",        # 20, 32
        "Function_33_518B",        # 21, 33
        "Function_34_65D7",        # 22, 34
        "Function_35_6CB3",        # 23, 35
        "Function_36_6D50",        # 24, 36
        "Function_37_6D91",        # 25, 37
        "Function_38_7693",        # 26, 38
        "Function_39_76FF",        # 27, 39
        "Function_40_776B",        # 28, 40
        "Function_41_77D7",        # 29, 41
        "Function_42_7814",        # 2A, 42
        "Function_43_7851",        # 2B, 43
        "Function_44_788E",        # 2C, 44
        "Function_45_7E1D",        # 2D, 45
        "Function_46_90A5",        # 2E, 46
        "Function_47_A32E",        # 2F, 47
        "Function_48_AA82",        # 30, 48
        "Function_49_B2AE",        # 31, 49
        "Function_50_B7C2",        # 32, 50
        "Function_51_E1E0",        # 33, 51
        "Function_52_E230",        # 34, 52
        "Function_53_E26F",        # 35, 53
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1447")
    Sound(14, 0, 100, 0)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x3D, 1)"), scpexpr(EXPR_END)), "loc_13D0")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x3D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EB, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_1442")

    label("loc_13D0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x3D),
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
    OP_71(0x7, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1442")

    Jump("loc_1490")

    label("loc_1447")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1727")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1699")

    ChrTalk(
        0xFE,
        (
            "Ah, the Special Support\x01",
            "Section...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FDino... Umm, those other\x01",
            "members are...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yeah... Thanks to you guys,\x01",
            "even Kouki, the sickest one,\x01",
            "regained consciousness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A lot of us were\x01",
            "hospitalized but we've\x01",
            "all returned to Downtown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well as you might expect, I\x01",
            "think it's hard to return to\x01",
            "the group right away, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But if you wait here, I\x01",
            "guess they'll probably\x01",
            "turn up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108FDino...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FIs that so...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18D, 2)
    Jump("loc_1722")

    label("loc_1699")


    ChrTalk(
        0xFE,
        (
            "Even so... The city is\x01",
            "noisy this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard about the question\x01",
            "of independence, I just wish\x01",
            "they'd be a little quieter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1722")

    Jump("loc_1AAA")

    label("loc_1727")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1735")
    Jump("loc_1AAA")

    label("loc_1735")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1743")
    Jump("loc_1AAA")

    label("loc_1743")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1751")
    Jump("loc_1AAA")

    label("loc_1751")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_175F")
    Jump("loc_1AAA")

    label("loc_175F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_176D")
    Jump("loc_1AAA")

    label("loc_176D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_177B")
    Jump("loc_1AAA")

    label("loc_177B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1789")
    Jump("loc_1AAA")

    label("loc_1789")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1797")
    Jump("loc_1AAA")

    label("loc_1797")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1A2A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1964")

    ChrTalk(
        0xFE,
        (
            "Ah, the Special Support\x01",
            "Section...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "H-Hey Wazy. I heard you\x01",
            "went head to head\x01",
            "against Wald, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F...If you have a question I'll\x01",
            "answer it. Are you trying to\x01",
            "get me to say something?\x02",
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
        "N-No, nevermind!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "W-Wald's the strongest.\x01",
            "I'll never believe that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F(Wow, Wald sure is\x01",
            "loved.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(Yeah. To these guys,\x01",
            "he's like a hero.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14C, 6)
    Jump("loc_19B6")

    label("loc_1964")


    ChrTalk(
        0xFE,
        (
            "...Wald's always gonna\x01",
            "be the strongest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Y-Yeah! I'll never\x01",
            "believe it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19B6")

    Jump("loc_1A25")

    label("loc_19BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19CA")
    Jump("loc_1A25")

    label("loc_19CA")


    ChrTalk(
        0xFE,
        (
            "...I gave you that\x01",
            "questionnaire already,\x01",
            "didn't I!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Take it and get outta\x01",
            "here!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A25")

    Jump("loc_1AAA")

    label("loc_1A2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1A38")
    Jump("loc_1AAA")

    label("loc_1A38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1AAA")

    ChrTalk(
        0xFE,
        (
            "...If you understand,\x01",
            "then get outta here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Don't come cryin' to me\x01",
            "if Wald finds you out\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AAA")

    TalkEnd(0xFE)
    Return()

    # Function_7_149C end

    def Function_8_1AAE(): pass

    label("Function_8_1AAE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1B4A")

    ChrTalk(
        0xFE,
        (
            "I don't really get it, but\x01",
            "it seems to have become a\x01",
            "terrible situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Perhaps it's a good idea\x01",
            "not to leave home for a\x01",
            "while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_217F")

    label("loc_1B4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1B58")
    Jump("loc_217F")

    label("loc_1B58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1BD6")

    ChrTalk(
        0xFE,
        (
            "I heard there's been a\x01",
            "disturbance at the town\x01",
            "of Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They say there are\x01",
            "injured... How truly\x01",
            "sad.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_217F")

    label("loc_1BD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1BE4")
    Jump("loc_217F")

    label("loc_1BE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1C65")

    ChrTalk(
        0xFE,
        (
            "Come to think of it, I\x01",
            "haven't seen the usual\x01",
            "kids today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, I wonder if they\x01",
            "went somewhere to play.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_217F")

    label("loc_1C65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1D11")

    ChrTalk(
        0xFE,
        (
            "I understand that a referendum\x01",
            "on the question of independence\x01",
            "will be held soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't really get it,\x01",
            "but I must consider the\x01",
            "question properly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_217F")

    label("loc_1D11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1E6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DF5")

    ChrTalk(
        0xFE,
        (
            "There has been a lot of big\x01",
            "news shaking the foundations\x01",
            "of society lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There are a lot of\x01",
            "things I don't\x01",
            "understand, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, I just don't\x01",
            "want to see everyone's\x01",
            "smiles fade.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E68")

    label("loc_1DF5")


    ChrTalk(
        0xFE,
        (
            "I don't understand\x01",
            "complicated subjects,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, I just don't\x01",
            "want to see everyone's\x01",
            "smiles fade.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E68")

    Jump("loc_217F")

    label("loc_1E6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1ECD")

    ChrTalk(
        0xFE,
        (
            "Haha, there's good\x01",
            "weather today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The kids are happy. How\x01",
            "heartwarming.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_217F")

    label("loc_1ECD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2026")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F70")

    ChrTalk(
        0xFE,
        (
            "It looks like you can see the\x01",
            "new City Hall building from\x01",
            "anywhere in Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, I wonder how it\x01",
            "looks from up close.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2021")

    label("loc_1F70")


    ChrTalk(
        0xFE,
        (
            "The man wearing a white coat\x01",
            "who passed by just now must\x01",
            "be a traveling musician.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I couldn't hear it well with\x01",
            "my poor hearing, but that was\x01",
            "a pleasant melody, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2021")

    Jump("loc_217F")

    label("loc_2026")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2118")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20AF")

    ChrTalk(
        0xFE,
        (
            "That sister is someone I\x01",
            "don't see around here\x01",
            "often, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, she's good with\x01",
            "kids, isn't she.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2113")

    label("loc_20AF")


    ChrTalk(
        0xFE,
        (
            "That sister is good with\x01",
            "kids, isn't she.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, I get a warm\x01",
            "feeling just looking at\x01",
            "her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2113")

    Jump("loc_217F")

    label("loc_2118")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2126")
    Jump("loc_217F")

    label("loc_2126")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_217F")

    ChrTalk(
        0xFE,
        (
            "Haha, there's sunny and\x01",
            "warm weather today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I might just fall\x01",
            "asleep.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_217F")

    TalkEnd(0xFE)
    Return()

    # Function_8_1AAE end

    def Function_9_2183(): pass

    label("Function_9_2183")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_21F6")

    ChrTalk(
        0xFE,
        (
            "Hehe, somehow, the\x01",
            "city's in a huuuge\x01",
            "uproar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They say we might go to\x01",
            "war with someone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26BC")

    label("loc_21F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_22EB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2260")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_221E")
    Call(0, 18)
    Jump("loc_225B")

    label("loc_221E")


    ChrTalk(
        0xFE,
        (
            "Kyahaha, that old man!\x01",
            "He's almost like a good\x01",
            "citizen.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_225B")

    Jump("loc_22E6")

    label("loc_2260")


    ChrTalk(
        0xFE,
        (
            "Hehe, today's emergency\x01",
            "food was good too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If we can each stuff like that\x01",
            "every day, reconstruction 'll\x01",
            "be done in no time!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22E6")

    Jump("loc_26BC")

    label("loc_22EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2364")

    ChrTalk(
        0xFE,
        (
            "The adults are noisy\x01",
            "today for some reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, it's the same as\x01",
            "usual for my old man,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26BC")

    label("loc_2364")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2397")

    ChrTalk(
        0xFE,
        (
            "Kyahaha, it's a natural\x01",
            "shower.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26BC")

    label("loc_2397")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_23A5")
    Jump("loc_26BC")

    label("loc_23A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_23B3")
    Jump("loc_26BC")

    label("loc_23B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_241F")

    ChrTalk(
        0xFE,
        (
            "Woohoo! Extra allowance,\x01",
            "get!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Nishishi... Roser, let's\x01",
            "have meat today. Yeah,\x01",
            "meat.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26BC")

    label("loc_241F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_24B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2472")

    ChrTalk(
        0xFE,
        (
            "Yeah, yeah! Everything\x01",
            "goes like Master Vaan\x01",
            "says!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_24AF")

    label("loc_2472")


    ChrTalk(
        0xFE,
        (
            "Kyahaha, that old man!\x01",
            "He might be drinking\x01",
            "around now!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24AF")

    Jump("loc_26BC")

    label("loc_24B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_24C2")
    Jump("loc_26BC")

    label("loc_24C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_24D3")
    Call(0, 16)
    Jump("loc_26BC")

    label("loc_24D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_END)), "loc_253D")

    ChrTalk(
        0xFE,
        (
            "Hah! He does have a\x01",
            "lotta stamina, though!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Rain started falling\x01",
            "before I knew it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26BC")

    label("loc_253D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2599")

    ChrTalk(
        0xFE,
        "Rain's falling steadily.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If it was all juice, my\x01",
            "belly would burst.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26BC")

    label("loc_2599")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_26BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2649")

    ChrTalk(
        0xFE,
        (
            "Oh, you guys are those\x01",
            "police, right? You even have\x01",
            "that delinquent with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Did something happen?\x01",
            "Huh? Am I wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Tch, how boring.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_26BC")

    label("loc_2649")


    ChrTalk(
        0xFE,
        (
            "Those delinquent groups\x01",
            "have quieted down\x01",
            "lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Kyahaha, are they out of\x01",
            "fighting spirit or\x01",
            "something?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26BC")

    TalkEnd(0xFE)
    Return()

    # Function_9_2183 end

    def Function_10_26C0(): pass

    label("Function_10_26C0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_26FF")

    ChrTalk(
        0xFE,
        (
            "*chuckle*... Wouldn't\x01",
            "that be dangerous?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A6D")

    label("loc_26FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_27C0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2755")

    ChrTalk(
        0xFE,
        (
            "*chuckle*... Your dad is\x01",
            "unexpectedly reliable,\x01",
            "Vaan.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27BB")

    label("loc_2755")


    ChrTalk(
        0xFE,
        (
            "There's going to be\x01",
            "another emergency\x01",
            "feeding come evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder what it's going\x01",
            "to be.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27BB")

    Jump("loc_2A6D")

    label("loc_27C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2817")

    ChrTalk(
        0xFE,
        (
            "Mainz seems dangerous\x01",
            "for some reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder how dangerous.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A6D")

    label("loc_2817")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2862")

    ChrTalk(
        0xFE,
        (
            "*chuckle*... Should we\x01",
            "go somewhere to swipe\x01",
            "some soap?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A6D")

    label("loc_2862")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2870")
    Jump("loc_2A6D")

    label("loc_2870")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_287E")
    Jump("loc_2A6D")

    label("loc_287E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_28B3")

    ChrTalk(
        0xFE,
        (
            "Kyahaha, I get to eat\x01",
            "tons today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A6D")

    label("loc_28B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_292F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28FC")

    ChrTalk(
        0xFE,
        (
            "Kyahaha, it's just like\x01",
            "you said, Roser!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_292A")

    label("loc_28FC")


    ChrTalk(
        0xFE,
        (
            "*chuckle*... Your dad\x01",
            "might faint, Vaan.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_292A")

    Jump("loc_2A6D")

    label("loc_292F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_293D")
    Jump("loc_2A6D")

    label("loc_293D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_294E")
    Call(0, 16)
    Jump("loc_2A6D")

    label("loc_294E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_END)), "loc_29B8")

    ChrTalk(
        0xFE,
        (
            "Is that what they call a\x01",
            "one-on-one fight?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*chuckle*... It was\x01",
            "certainly intense.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A6D")

    label("loc_29B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2A2D")

    ChrTalk(
        0xFE,
        (
            "But I think my tummy's\x01",
            "rumbling because of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*chuckle*... You're just\x01",
            "like your dad, Vaan.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A6D")

    label("loc_2A2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2A6D")

    ChrTalk(
        0xFE,
        (
            "*chuckle*... You sure do\x01",
            "like making noise, Vaan.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A6D")

    TalkEnd(0xFE)
    Return()

    # Function_10_26C0 end

    def Function_11_2A71(): pass

    label("Function_11_2A71")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2ABB")

    ChrTalk(
        0xFE,
        (
            "T-To think a war...\x01",
            "That's no good. No good\x01",
            "at all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34E2")

    label("loc_2ABB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2BF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_END)), "loc_2B33")

    ChrTalk(
        0xFE,
        (
            "*rustle*... Umm, this\x01",
            "is... No good, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Then this one... Hmm,\x01",
            "this one's a miss too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BF1")

    label("loc_2B33")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B90")

    ChrTalk(
        0xFE,
        "Thanks you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm gonna sell this\x01",
            "scrap you gave us\x01",
            "properly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BF1")

    label("loc_2B90")


    ChrTalk(
        0xFE,
        (
            "And now that my\x01",
            "stomach's full, I can\x01",
            "work hard again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanks for all your\x01",
            "help, guys.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BF1")

    Jump("loc_34E2")

    label("loc_2BF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2D8A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CD9")

    ChrTalk(
        0xFE,
        (
            "Hmm, there's mud in the cracks\x01",
            "in the pavement because of\x01",
            "yesterday's rain, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And there's a lot of trash in those\x01",
            "cracks... Haha, why does it always\x01",
            "have to be my turn when this happens.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2D85")

    label("loc_2CD9")


    ChrTalk(
        0xFE,
        (
            "Ta-dah! This is where I\x01",
            "bring out my secret weapon,\x01",
            "a "handy wooden stick".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There we go... This is how you\x01",
            "scrape the trash out of those\x01",
            "cracks. It's pretty fun.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D85")

    Jump("loc_34E2")

    label("loc_2D8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2D98")
    Jump("loc_34E2")

    label("loc_2D98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2E38")

    ChrTalk(
        0xFE,
        (
            "*sweep, sweep*... There.\x01",
            "This area's sparkling\x01",
            "again today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, though cleaning never\x01",
            "ends, this sense of\x01",
            "accomplishment is the best.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34E2")

    label("loc_2E38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2EAC")

    ChrTalk(
        0xFE,
        (
            "I haven't seen too many\x01",
            "people fighting around\x01",
            "here lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, that's a very good\x01",
            "thing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34E2")

    label("loc_2EAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2FF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F6E")

    ChrTalk(
        0xFE,
        (
            "I guess it was last week. A\x01",
            "delinquent held something to his\x01",
            "ear and was muttering something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What could that thing\x01",
            "be?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F(Could it be an ENIGMA?)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2FF0")

    label("loc_2F6E")


    ChrTalk(
        0xFE,
        (
            "I guess it was last week. A\x01",
            "delinquent held something to his\x01",
            "ear and was muttering something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What could that thing\x01",
            "be?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FF0")

    Jump("loc_34E2")

    label("loc_2FF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_306F")

    ChrTalk(
        0xFE,
        (
            "Orchis Tower is super\x01",
            "tall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard it was 250\x01",
            "arge... I wonder how many\x01",
            "times my height that is?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34E2")

    label("loc_306F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_31F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3176")

    ChrTalk(
        0xFE,
        (
            "I heard a lot of reporters\x01",
            "and important people from\x01",
            "foreign countries came today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But none of them would come\x01",
            "to a place like this, they\x01",
            "said. I don't know why.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sweep, sweep*... I've\x01",
            "got to make it prettier\x01",
            "than usual.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_31F3")

    label("loc_3176")


    ChrTalk(
        0xFE,
        (
            "I heard a lot of super\x01",
            "important foreigners\x01",
            "came today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sweep, sweep*... I've\x01",
            "got to make it prettier\x01",
            "than usual.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31F3")

    Jump("loc_34E2")

    label("loc_31F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3209")
    Call(0, 16)
    Jump("loc_34E2")

    label("loc_3209")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3217")
    Jump("loc_34E2")

    label("loc_3217")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_34E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3452")

    ChrTalk(
        0xFE,
        "*sweep, sweep*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*. As usual, no matter\x01",
            "how much I clean, the\x01",
            "garbage just won't go away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FGood morning, Kanon. How\x01",
            "are you today?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x105, 0)

    ChrTalk(
        0xFE,
        "Ah, Wazy. Good morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, I guess there's a\x01",
            "lot of bottle trash\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I won't forgive it, but\x01",
            "it's interesting looking\x01",
            "at their various shapes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Look, the middle of this\x01",
            "one's narrow. It's\x01",
            "pretty, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHaha, indeed. It's a\x01",
            "nice shape.\x02\x03",
            "#10300FFor now, Kanon, watch\x01",
            "out for shards and such.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yeah, thanks.\x02",
    )

    CloseMessageWindow()
    OP_93(0xFE, 0xB4, 0x0)
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x137, 3)
    Jump("loc_34E2")

    label("loc_3452")


    ChrTalk(
        0xFE,
        (
            "Bottles have different\x01",
            "shapes and looking through\x01",
            "them is interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Look, this one's dull\x01",
            "but shines when you hold\x01",
            "it up to light.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34E2")

    TalkEnd(0xFE)
    Return()

    # Function_11_2A71 end

    def Function_12_34E6(): pass

    label("Function_12_34E6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_355E")

    ChrTalk(
        0xFE,
        (
            "*sigh*, this scene work\x01",
            "really takes it out of\x01",
            "ya.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, I guess it's good\x01",
            "training, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_355E")

    label("loc_355E")

    TalkEnd(0xFE)
    Return()

    # Function_12_34E6 end

    def Function_13_3562(): pass

    label("Function_13_3562")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_361D")

    ChrTalk(
        0x10,
        (
            "B-But even so... Seeing\x01",
            "this destroyed apartment...\x01",
            "H-How intense!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Thank goodness it was abandoned.\x01",
            "It would have been terrible if\x01",
            "there was anyone inside.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_361D")

    label("loc_361D")

    TalkEnd(0xFE)
    Return()

    # Function_13_3562 end

    def Function_14_3621(): pass

    label("Function_14_3621")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_14_3621 end

    def Function_15_3628(): pass

    label("Function_15_3628")

    TalkBegin(0xFE)
    Call(0, 16)
    TalkEnd(0xFE)
    Return()

    # Function_15_3628 end

    def Function_16_3632(): pass

    label("Function_16_3632")

    OP_4B(0x12, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_384D")

    ChrTalk(
        0x12,
        (
            "#04403F"I see. I'll go see Anna, then."\x02\x03",
            "The woman was a witch, so surely\x01",
            "she'd know Ron's location.\x02\x03",
            "He followed the road to Anna's\x01",
            "hut. Suddenly, Mark's ears heard\x01",
            "the piercing cry of a monster.\x02",
        )
    )

    CloseMessageWindow()
    Sound(18, 0, 100, 0)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "So exciting... And then?\x01",
            "And then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Huh? Let's have lunch\x01",
            "early. You brought\x01",
            "bread, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "*chuckle*... Let's eat\x01",
            "it secretly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105F(Ries... Looks like\x01",
            "she's here for Sunday\x01",
            "School.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(She's reading them a fairy\x01",
            "tale, huh... It's a\x01",
            "heartwarming scene, somehow.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14C, 7)
    Jump("loc_3B42")

    label("loc_384D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A68")

    ChrTalk(
        0x12,
        (
            "#04403FThe terrifying cry grew\x01",
            "closer, and then...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Yeah, yeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Tch, how boring. Roser,\x01",
            "I'm sleeping until you\x01",
            "bring me some bread.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "*chuckle*... Is that so.\x02",
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x12)

    ChrTalk(
        0x12,
        (
            "#04400FI forgot to say it earlier, but I'll\x01",
            "have you write your thoughts on this\x01",
            "book at the end of today's class.\x02\x03",
            "#04400FThose who don't write anything will\x01",
            "be considered absent and go without\x01",
            "lunch.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xA)

    ChrTalk(
        0xA,
        (
            "Wha, seriously!? What a\x01",
            "tyrant!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "*chuckle*... Today's\x01",
            "sister is really strict.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3B42")

    label("loc_3A68")


    ChrTalk(
        0x12,
        (
            "#04403FThe terrifying cry grew\x01",
            "closer, and then...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Wah, wait, wait, from\x01",
            "the beginning! Read it\x01",
            "from the beginning!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "*chuckle*... You always\x01",
            "get flustered around\x01",
            "now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Haha, let's enjoy it\x01",
            "together.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B42")

    OP_4C(0x12, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_16_3632 end

    def Function_17_3B53(): pass

    label("Function_17_3B53")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BFC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B75")
    Call(0, 18)
    Jump("loc_3BF7")

    label("loc_3B75")


    ChrTalk(
        0xFE,
        (
            "Man. Even though they're\x01",
            "feeding us, I can't work\x01",
            "for free in broad daylight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm gonna have a drink\x01",
            "when this is over.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BF7")

    Jump("loc_3C4B")

    label("loc_3BFC")


    ChrTalk(
        0xFE,
        (
            "But, the sun's really\x01",
            "bright.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's poison to night\x01",
            "owls like myself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C4B")

    TalkEnd(0xFE)
    Return()

    # Function_17_3B53 end

    def Function_18_3C4F(): pass

    label("Function_18_3C4F")

    OP_4B(0xA, 0xFF)
    OP_4B(0x13, 0xFF)
    TurnDirection(0xA, 0x0, 0)

    ChrTalk(
        0xA,
        (
            "Kyahaha, that old man!\x01",
            "It's rare for him to\x01",
            "work before noon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I think the landlord drove him\x01",
            "out of his apartment and told him\x01",
            "to help with the reconstruction?\x02",
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
            "Ah, Vaan. Don't say\x01",
            "anything unnecessary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Shut up and help me with\x01",
            "this, will ya?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    SetScenarioFlags(0x0, 5)
    OP_93(0xA, 0x13B, 0x0)
    OP_93(0x13, 0x13B, 0x0)
    OP_4C(0xA, 0xFF)
    OP_4C(0x13, 0xFF)
    Return()

    # Function_18_3C4F end

    def Function_19_3DA3(): pass

    label("Function_19_3DA3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DFD")

    ChrTalk(
        0xFE,
        (
            "Now then, gotta tidy up\x01",
            "quickly today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "First to measure...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E6C")

    label("loc_3DFD")


    ChrTalk(
        0xFE,
        (
            "Phew. It's a bit late,\x01",
            "but I can finally take a\x01",
            "breather.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Alright... I'll do my\x01",
            "best this afternoon!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E6C")

    TalkEnd(0xFE)
    Return()

    # Function_19_3DA3 end

    def Function_20_3E70(): pass

    label("Function_20_3E70")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EBB")

    ChrTalk(
        0xFE,
        (
            "Papa's working for\x01",
            "everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "He's so cool♪\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F2F")

    label("loc_3EBB")

    SetChrName("Rimah")

    ChrTalk(
        0x14,
        (
            "Papa, this broth's\x01",
            "delicious.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("Melson")

    ChrTalk(
        0x15,
        (
            "Yeah, really. Papa can\x01",
            "feel the power welling\x01",
            "up inside him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F2F")

    TalkEnd(0xFE)
    Return()

    # Function_20_3E70 end

    def Function_21_3F33(): pass

    label("Function_21_3F33")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F48")
    Call(0, 23)
    Jump("loc_3F77")

    label("loc_3F48")


    ChrTalk(
        0xFE,
        (
            "What can I say, that's\x01",
            "ridiculous, huh...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F77")

    TalkEnd(0xFE)
    Return()

    # Function_21_3F33 end

    def Function_22_3F7B(): pass

    label("Function_22_3F7B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F90")
    Call(0, 23)
    Jump("loc_3FC0")

    label("loc_3F90")


    ChrTalk(
        0xFE,
        (
            "I would have liked Wald\x01",
            "to show himself...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FC0")

    TalkEnd(0xFE)
    Return()

    # Function_22_3F7B end

    def Function_23_3FC4(): pass

    label("Function_23_3FC4")

    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)

    ChrTalk(
        0xD,
        "Orchis Tower, was it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Man, they've built\x01",
            "something ridiculous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Heheh, seriously. I want\x01",
            "to bungee jump from the\x01",
            "roof!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_23_3FC4 end

    def Function_24_405D(): pass

    label("Function_24_405D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Now then, it's time to\x01",
            "start my Downtown\x01",
            "patrol.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I wonder where I\x01",
            "should start from.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_405D end

    def Function_25_40C6(): pass

    label("Function_25_40C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_40D3")
    Call(0, 26)
    Return()

    label("loc_40D3")

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
        "#11PYou guys...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FGood afternoon. We\x01",
            "haven't seen you since\x01",
            "the cult incident, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FIt's been a while, Dino.\x02\x03",
            "If we're seeing you like\x01",
            "this, it looks like you've\x01",
            "returned to your group?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PY-Yeah, I guess.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PThey said it was because of the\x01",
            "medicine that I picked fights\x01",
            "with Wald and the others...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P...It was like getting\x01",
            "hit with a bat, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106FG-Getting hit with a\x01",
            "bat, you say...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FHaha, well at least you\x01",
            "were able to return.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#11PWazy... So it's true you\x01",
            "joined the police.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PIt's because of you that\x01",
            "Wald...!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00005FWald? What happened to\x01",
            "him?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    ChrTalk(
        0x8,
        (
            "#11P...Because you guys helped\x01",
            "us in the incident, I'll\x01",
            "give you a warning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PWald has been in the\x01",
            "worst kind of mood\x01",
            "lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PIf you value your life,\x01",
            "don't come near this\x01",
            "place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00105FA bad mood, you say...\x01",
            "Did something happen?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P...Everything is the\x01",
            "fault of Wazy there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PThe Testaments have been\x01",
            "quiet ever since the\x01",
            "incident...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PAnd now their leader Wazy became\x01",
            "one of those police dogs without\x01",
            "even settling things properly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F...I see.\x02\x03",
            "#00001FIn summary, he's become irritable\x01",
            "and violent because his brawling\x01",
            "rival is gone, is that it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106FI understand how you\x01",
            "feel, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10308F...Now, now.\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#11PD-Don't patronize me!!\x01",
            "You! Do you know what\x01",
            "you've done!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PIt's because of you that\x01",
            "Wald is hardly ever at Ignis\x01",
            "lately, you know that!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10303F...If that's what he\x01",
            "wants to do, then he\x01",
            "should.\x02\x03",
            "#10300FHehe. I'm just doing\x01",
            "whatever I want, too,\x01",
            "you see.\x02\x03",
            "I'm not trying to blame\x01",
            "you guys for any of\x01",
            "this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PGuh...\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    ChrTalk(
        0x8,
        (
            "#11P...Hmph. In that case,\x01",
            "get out of here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PIf Wald sees you here, I\x01",
            "won't be responsible for\x01",
            "what happens to any of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F...I think it's best if\x01",
            "we withdraw for today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00108F...I agree.\x02\x03",
            "#00100FSee you, Dino.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PHmph...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10308F............\x02",
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

    # Function_25_40C6 end

    def Function_26_49E7(): pass

    label("Function_26_49E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_END)), "loc_4AB9")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A71")

    ChrTalk(
        0x101,
        (
            "#00008F...We shouldn't enter\x01",
            "this place for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FYeah... It'd be helpful\x01",
            "if you didn't.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_4AA3")

    label("loc_4A71")


    ChrTalk(
        0x101,
        (
            "#00003F...Let's refrain from\x01",
            "entering Ignis.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AA3")

    Sleep(50)
    SetChrPos(0x0, 44540, -2500, -22490, 270)
    EventEnd(0x4)

    label("loc_4AB9")

    Return()

    # Function_26_49E7 end

    def Function_27_4ABA(): pass

    label("Function_27_4ABA")

    Return()

    # Function_27_4ABA end

    def Function_28_4ABB(): pass

    label("Function_28_4ABB")

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
            "#12P#10108FExchange Shop\x01",
            ""Neinvalli"...\x02\x03",
            "#10106FIt definitely left an\x01",
            "impression on me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#5PWell, places like that\x01",
            "have their own moral\x01",
            "code.\x02\x03",
            "#00100FWe should be grateful\x01",
            "that she even told us\x01",
            "that much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00006FRight...\x02\x03",
            "#00008F...But a man like a man-\x01",
            "eating tiger, huh.\x02\x03",
            "#00001FAssuming he's not a\x01",
            "terrorist, it seems\x01",
            "likely he's a jaeger...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10303FThough it is strange for\x01",
            "a jaeger to be alone.\x02\x03",
            "#10300FShould we report this to\x01",
            "the chief?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4ECC")

    ChrTalk(
        0x101,
        (
            "#11P#00001FYeah, let's.\x02\x03",
            "#00003F(If jaegers are involved, Randy\x01",
            "would probably know something,\x01",
            "but...)\x02\x03",
            "#00000F(Well whatever. This matter's been\x01",
            "taken care of for now, so shall we\x01",
            "head back to the Support Section?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F89")

    label("loc_4ECC")


    ChrTalk(
        0x101,
        (
            "#11P#00001FYeah, let's.\x02\x03",
            "#00003F(If jaegers are involved,\x01",
            "Randy would probably know\x01",
            "something, but...)\x02\x03",
            "#00000F(Well, we still have\x01",
            "support requests left, so\x01",
            "let's take care of them.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F89")

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

    # Function_28_4ABB end

    def Function_29_4FBF(): pass

    label("Function_29_4FBF")


    def lambda_4FC4():
        OP_95(0xFE, -13000, 0, -10500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4FC4)

    def lambda_4FDE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4FDE)
    WaitChrThread(0xFE, 1)

    def lambda_4FF3():
        OP_95(0xFE, -10000, 0, -11500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4FF3)
    WaitChrThread(0xFE, 1)

    def lambda_5011():
        OP_95(0xFE, -6500, 0, -9600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5011)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xFA, 0x1F4)
    Return()

    # Function_29_4FBF end

    def Function_30_5032(): pass

    label("Function_30_5032")


    def lambda_5037():
        OP_95(0xFE, -13000, 0, -10500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5037)

    def lambda_5051():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5051)
    WaitChrThread(0xFE, 1)

    def lambda_5066():
        OP_95(0xFE, -10000, 0, -11500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5066)
    WaitChrThread(0xFE, 1)

    def lambda_5084():
        OP_95(0xFE, -7700, 0, -9000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5084)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xC8, 0x1F4)
    Return()

    # Function_30_5032 end

    def Function_31_50A5(): pass

    label("Function_31_50A5")


    def lambda_50AA():
        OP_95(0xFE, -13000, 0, -10500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_50AA)

    def lambda_50C4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_50C4)
    WaitChrThread(0xFE, 1)

    def lambda_50D9():
        OP_95(0xFE, -10000, 0, -11500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_50D9)
    WaitChrThread(0xFE, 1)

    def lambda_50F7():
        OP_95(0xFE, -7500, 0, -11200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_50F7)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x14, 0x1F4)
    Return()

    # Function_31_50A5 end

    def Function_32_5118(): pass

    label("Function_32_5118")


    def lambda_511D():
        OP_95(0xFE, -13000, 0, -10500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_511D)

    def lambda_5137():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5137)
    WaitChrThread(0xFE, 1)

    def lambda_514C():
        OP_95(0xFE, -10000, 0, -11500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_514C)
    WaitChrThread(0xFE, 1)

    def lambda_516A():
        OP_95(0xFE, -8700, 0, -10600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_516A)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x46, 0x1F4)
    Return()

    # Function_32_5118 end

    def Function_33_518B(): pass

    label("Function_33_518B")

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

    def lambda_5307():
        OP_97(0x101, 0x0, 0x0, 0xFA0, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5307)
    Sleep(100)

    def lambda_5324():
        OP_97(0x102, 0x0, 0x0, 0xFA0, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5324)
    Sleep(100)

    def lambda_5341():
        OP_97(0x109, 0x0, 0x0, 0xFA0, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5341)
    Sleep(100)

    def lambda_535E():
        OP_97(0x105, 0x0, 0x0, 0xFA0, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_535E)
    SetCameraDistance(19000, 2000)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 0)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x17,
        "Ferocious Voice",
        "#3564V#30W─Hold up, assholes.\x02",
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

    def lambda_5459():
        OP_93(0x105, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5459)
    Sleep(50)

    def lambda_5469():
        OP_93(0x109, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5469)
    Sleep(50)

    def lambda_5479():
        OP_93(0x102, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5479)
    Sleep(50)

    def lambda_5489():
        OP_93(0x101, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5489)
    Sleep(50)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    Sleep(1000)

    def lambda_54AC():
        OP_96(0xFE, 0x19DC, 0x0, 0xFFFFDEFE, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_54AC)
    WaitChrThread(0x17, 1)
    OP_6F(0x79)
    Sleep(500)
    OP_C9(0x0, 0x80000000)
    Sound(3306, 255, 80, 0)

    ChrTalk(
        0x101,
        "#00005F#30W#6P#NAh...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        "#10308F#2908V#40W#6P#NSo it's you.\x02",
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

    def lambda_55C7():
        OP_96(0xFE, 0x76C, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_55C7)
    OP_0D()
    WaitChrThread(0x17, 1)
    OP_93(0x17, 0x0, 0x1F4)

    ChrTalk(
        0x109,
        "#10105F(Uh, this guy is...?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00108F(He's the leader of the\x01",
            "Saber Vipers gang...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FWald, what's up?\x02\x03",
            "#10300FYour members haven't\x01",
            "seen you around lately,\x01",
            "huh.\x02",
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
            "#30WShut up. Don't concern yourself\x01",
            "with me.\x02\x03",
            "But how about you, ya bastard...\x01",
            "You ended up a dog of the police,\x01",
            "didn't you?\x02\x03",
            "What're ya plannin', huh!?\x02",
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
            "#6P#10306F#30WOh, nothing much...\x02\x03",
            "#10302FThe Testaments are all\x01",
            "fine with it and I'm not\x01",
            "bothering anyone, am I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#01601F#30W#11PYou bastard, are you fucking\x01",
            "serious?\x02\x03",
            "#01603FDoing something like stepping away\x01",
            "from your group without the consent\x01",
            "of I, the great Wald Wales...\x02\x03",
            "#01607FThink I'll forgive ya fer that?\x01",
            "Huh!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10308F#30W......\x02",
    )

    CloseMessageWindow()

    def lambda_591E():
        OP_96(0xFE, 0x384, 0x0, 0x13EC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_591E)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        "#6P#00011FWald, wait a second!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106FW-We have our reasons...\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0x17,
        (
            "#01607F#4S#11PShut up! Stay out of\x01",
            "this!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x17,
        (
            "#01603F#11PWazy, I don't know what\x01",
            "you are after by joining\x01",
            "the cops...\x02\x03",
            "#01608FBut you know─\x02",
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
            "#01607F#11PYou don't seriously think\x01",
            "I'm gonna let you walk out\x01",
            "of here scot free, do ya!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00001FUgh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#00106FT-This is bad...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10303F#30W─Wald.\x02",
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(1680, 1300, 3250, 1200)

    def lambda_5B4C():
        OP_95(0xFE, 1900, 0, 4800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5B4C)
    Sleep(500)

    def lambda_5B69():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5B69)

    def lambda_5B76():
        OP_96(0xFE, 0x2BC, 0x0, 0x13EC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5B76)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x101, 1)
    EndChrThread(0x101, 0x2)
    OP_93(0x101, 0x5A, 0x0)
    OP_6F(0x79)
    SetCameraDistance(14700, 30000)
    MoveCamera(138, 22, 0, 30000)

    ChrTalk(
        0x101,
        "#12P#00011FH-Hey, Wazy!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10308F#30WIt's fine. Let me handle\x01",
            "this.\x02\x03",
            "#10306FWald. It should be\x01",
            "painfully obvious.\x02\x03",
            "And it's true of both\x01",
            "the Testaments and the\x01",
            "Saber Vipers.\x02\x03",
            "#10301FYou know they're not\x01",
            "places you can stay\x01",
            "forever, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x17,
        "#11P#01605F#11PHuh...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10303F#30WI formed the Testaments to keep\x01",
            "you guys from just doing whatever\x01",
            "you liked here in Downtown.\x02\x03",
            "#10300FBut, though my members were weak\x01",
            "at first, they've grown.\x02\x03",
            "And now, even without me, they\x01",
            "can even go toe-to-toe against\x01",
            "you.\x02\x03",
            "My job here is done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#11P#01607F#30W...Y-You bastard...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304F#30WAnd one day.... I know\x01",
            "the other members will\x01",
            "outgrow the team as well.\x02\x03",
            "To move beyond this life\x01",
            "and find their own paths.\x02\x03",
            "#10302FThat's what I believe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005F#30WWazy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#00108F#30WWazy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#11P#01608F#30W...............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304F#30WThe same goes for you Saber\x01",
            "Vipers.\x02\x03",
            "Though many of you are thugs,\x01",
            "you were strong enough to\x01",
            "resist the mafia's offer.\x02\x03",
            "#10300FAnd so, Wald... I think\x01",
            "you'll find your path one day\x01",
            "too.\x02",
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
        "#11P#01604F#60W#10AHah...\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x3E8)

    ChrTalk(
        0x17,
        "#11P#01609F#2809V#4S#25A#40WHAHAHAHAHAHA!\x02",
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
            "#01611F#3565V#30W#11PI never thought you'd\x01",
            "ever spit out something\x01",
            "that stupid.\x02\x03",
            "#01607F#3566VI've heard enough. Don't\x01",
            "spout any of your\x01",
            "bullshit anymore!\x02\x03",
            "#3561VYou defiled our\x01",
            "Sanctuary! I'll never\x01",
            "forgive you for this!\x02",
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
        "#6P#10303F#40WI see...\x02",
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
        "#12P#00011FHey Wazy....\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10303F#30WLloyd, there's no need\x01",
            "for you to get involved.\x02\x03",
            "#10301FI have to take care of\x01",
            "this myself.\x02",
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
            "#11P#01604F#30WHehe. It looks like\x01",
            "you've still got some\x01",
            "sense in you....\x02\x03",
            "#01602FI'll give you a thorough\x01",
            "beating and then have\x01",
            "you grovel before me...\x02\x03",
            "Hehe, then maybe you'll\x01",
            "come to your senses...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x105,
        "#6P#10303F#2909V#30W─Enough talk.\x02",
    )

    CloseMessageWindow()
    OP_24(0xB5D)
    OP_57(0x0)
    OP_5A()
    StopBGM(0xBB8)

    ChrTalk(
        0x17,
        "#11P#01601F#3567VAh?\x02",
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

    def lambda_640D():
        OP_96(0xFE, 0x12C, 0x0, 0x13EC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_640D)
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
        "#12P#01605F!?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        "#00005F(This is...)\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7452", 0)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x105,
        (
            "#5P#10301F#2910V#30W#20AWald─\x01",
            "#40WI'm going all out!\x02",
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

    # Function_33_518B end

    def Function_34_65D7(): pass

    label("Function_34_65D7")

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

    def lambda_673B():
        OP_95(0xFE, 1900, 0, 2600, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_673B)
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

    def lambda_67DB():
        OP_9D(0xFE, 0x76C, 0x0, 0xFFFFFE0C, 0x898, 0x2BC)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_67DB)
    Sound(2800, 255, 100, 0)
    Sleep(500)
    CancelBlur(0)
    WaitChrThread(0x17, 1)
    Sound(862, 0, 100, 0)
    Sound(833, 0, 30, 0)
    OP_82(0x0, 0x64, 0xBB8, 0x12C)
    SetChrSubChip(0x17, 0x3)

    def lambda_682B():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x12C, 0x2BC)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_682B)
    WaitChrThread(0x17, 1)
    Sound(811, 0, 100, 0)
    OP_82(0x0, 0x64, 0xBB8, 0x64)

    ChrTalk(
        0x17,
        "#01610F#13A#11P*cough*!\x02",
    )

    CloseMessageWindow()
    Sleep(800)

    def lambda_6883():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_6883)
    Sleep(1200)

    ChrTalk(
        0x17,
        (
            "#11P#01611F#40W...Ugh... You bastard...\x02\x03",
            "Don't tell me... You've\x01",
            "been holding back... all\x01",
            "this time...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10306F#30W...I'm not Randy, that\x01",
            "was just my little\x01",
            "special technique.\x02\x03",
            "#10308FBut I didn't hold\x01",
            "anything back today.\x02\x03",
            "#10301FThat's the last favor I\x01",
            "ever give you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#11P#01611F#50WUgh... Wazy... You...\x01",
            "bastard...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x105, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x105,
        (
            "#11P#10303F#30WGoodbye, Wald.\x02\x03",
            "#10300FThese past two years...\x01",
            "It's been fun.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_6A4E():

        label("loc_6A4E")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_6A4E")

    QueueWorkItem2(0x101, 2, lambda_6A4E)

    def lambda_6A60():

        label("loc_6A60")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_6A60")

    QueueWorkItem2(0x102, 2, lambda_6A60)

    def lambda_6A72():

        label("loc_6A72")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_6A72")

    QueueWorkItem2(0x109, 2, lambda_6A72)
    OP_68(1900, 1000, 3100, 5000)
    SetCameraDistance(17500, 5000)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)

    def lambda_6AA6():
        OP_95(0xFE, 1900, 0, 20000, 1800, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6AA6)
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

    def lambda_6B09():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_6B09)
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
            "#11P#01611F#3568V#50W#45ADon't bullshit me! I'll\x01",
            "never accept this!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(1000)

    ChrTalk(
        0x17,
        (
            "#11P#01610F#3569V#50W#40AYou asshole! Holding\x01",
            "back against me!? I'll\x01",
            "never accept it!!\x02",
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
        "#11P#01607F#3570V#5S#50W#20AWAZYYYYYYY!\x02",
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

    # Function_34_65D7 end

    def Function_35_6CB3(): pass

    label("Function_35_6CB3")

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

    def lambda_6CF9():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x44C, 0x2BC)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6CF9)
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

    # Function_35_6CB3 end

    def Function_36_6D50(): pass

    label("Function_36_6D50")

    EndChrThread(0xFE, 0x2)

    def lambda_6D59():
        OP_95(0xFE, 1900, 0, 8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6D59)
    WaitChrThread(0xFE, 1)

    def lambda_6D77():
        OP_95(0xFE, 1900, 0, 20000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6D77)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_36_6D50 end

    def Function_37_6D91(): pass

    label("Function_37_6D91")

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

    def lambda_6FDB():
        OP_97(0xFE, 0xFFFFCB44, 0x0, 0x34BC, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6FDB)
    Sleep(100)
    EndChrThread(0x109, 0xFF)
    SetChrPos(0x109, 18500, -2500, -23800, 315)

    def lambda_700D():
        OP_97(0xFE, 0xFFFFCB44, 0x0, 0x34BC, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_700D)
    Sleep(100)
    EndChrThread(0x104, 0xFF)
    SetChrPos(0x104, 20000, -2500, -22300, 315)

    def lambda_703F():
        OP_97(0xFE, 0xFFFFCB44, 0x0, 0x34BC, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_703F)
    Fade(500)
    OP_68(16200, 0, -20000, 0)
    MoveCamera(315, 27, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(23500, 0)
    OP_68(5200, 1000, -9000, 8500)
    MoveCamera(59, 27, 0, 8500)
    SetCameraDistance(19500, 8500)
    WaitChrThread(0x101, 1)

    def lambda_70B5():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_70B5)
    WaitChrThread(0x109, 1)

    def lambda_70C6():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_70C6)
    WaitChrThread(0x104, 1)

    def lambda_70D7():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_70D7)
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
        "#6P#10308FHow was it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11PNo good. They don't know\x01",
            "anything, it seems.\x02\x03",
            "#00013FLooks like no one's seen\x01",
            "Wald for the past few\x01",
            "days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#11PHe must be keeping his\x01",
            "distance from his\x01",
            "underlings.\x02\x03",
            "#00301FMaybe they're making fun\x01",
            "of us, pretending not to\x01",
            "know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106FUmm... They seemed\x01",
            "desperate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10303FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#6PWe could ask the\x01",
            "Testaments again, but...\x02\x03",
            "#00108FIt doesn't seem like\x01",
            "anyone has seen Wald\x01",
            "recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00206FYes... Even if he was\x01",
            "dead drunk, you'd see him\x01",
            "again before too long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#11PI see... It seems we\x01",
            "don't know the background\x01",
            "behind this at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#11PBut where the hell did\x01",
            "that guy get his hands\x01",
            "on Gnosis?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10308F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10113FWazy, you ok?\x02\x03",
            "You look really pale.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FHaha, I'm probably cold\x01",
            "because of the rain.\x02\x03",
            "#10300FFor now, I'll ask Abbas\x01",
            "and the others to gather\x01",
            "some info.\x02\x03",
            "Let's set aside the\x01",
            "matter of Wald and return\x01",
            "to the Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11P...I agree. It looked\x01",
            "like KeA was preparing\x01",
            "breakfast for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#6PHaha, I feel like she's\x01",
            "been helping us out more\x01",
            "lately.\x02",
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

    # Function_37_6D91 end

    def Function_38_7693(): pass

    label("Function_38_7693")


    def lambda_7698():
        OP_95(0xFE, 45000, -2500, -22500, 2200, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7698)

    def lambda_76B2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_76B2)
    WaitChrThread(0xFE, 1)

    def lambda_76C7():
        OP_95(0xFE, 38500, -2500, -23800, 2200, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_76C7)
    WaitChrThread(0xFE, 1)

    def lambda_76E5():
        OP_95(0xFE, 27500, -2500, -23800, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_76E5)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_38_7693 end

    def Function_39_76FF(): pass

    label("Function_39_76FF")


    def lambda_7704():
        OP_95(0xFE, 45000, -2500, -23300, 2200, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7704)

    def lambda_771E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_771E)
    WaitChrThread(0xFE, 1)

    def lambda_7733():
        OP_95(0xFE, 38500, -2500, -24600, 2200, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7733)
    WaitChrThread(0xFE, 1)

    def lambda_7751():
        OP_95(0xFE, 27500, -2500, -24600, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7751)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_39_76FF end

    def Function_40_776B(): pass

    label("Function_40_776B")


    def lambda_7770():
        OP_95(0xFE, 45000, -2500, -21700, 2200, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7770)

    def lambda_778A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_778A)
    WaitChrThread(0xFE, 1)

    def lambda_779F():
        OP_95(0xFE, 38500, -2500, -23000, 2200, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_779F)
    WaitChrThread(0xFE, 1)

    def lambda_77BD():
        OP_95(0xFE, 27500, -2500, -23000, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_77BD)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_40_776B end

    def Function_41_77D7(): pass

    label("Function_41_77D7")


    def lambda_77DC():
        OP_95(0xFE, -9500, 0, -10400, 2200, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_77DC)
    WaitChrThread(0xFE, 1)

    def lambda_77FA():
        OP_95(0xFE, -3500, 0, -9000, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_77FA)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_41_77D7 end

    def Function_42_7814(): pass

    label("Function_42_7814")


    def lambda_7819():
        OP_95(0xFE, -9500, 0, -9800, 2200, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7819)
    WaitChrThread(0xFE, 1)

    def lambda_7837():
        OP_95(0xFE, -3500, 0, -8400, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7837)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_42_7814 end

    def Function_43_7851(): pass

    label("Function_43_7851")


    def lambda_7856():
        OP_95(0xFE, -9500, 0, -11000, 2200, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7856)
    WaitChrThread(0xFE, 1)

    def lambda_7874():
        OP_95(0xFE, -3500, 0, -9600, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7874)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_43_7851 end

    def Function_44_788E(): pass

    label("Function_44_788E")

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
            "#12P#00000FSo this is the entrance to Geofront\x01",
            "D-Division, where the wanted monster in\x01",
            "that extermination request appeared, huh...\x02\x03",
            "#00003FThis was closed off for the longest time,\x01",
            "but it seems it's been opened due to the\x01",
            "request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203FHmm, there's one small problem,\x01",
            "though...\x02\x03",
            "#00200FWhy is there a Geofront\x01",
            "entrance in Downtown, that's\x01",
            "not connected to the orbal net?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00305FYeah, now that you\x01",
            "mention it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10105FWasn't Downtown left\x01",
            "behind by the city\x01",
            "development?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103FYes... Before, congresspeople and\x01",
            "government officials said construction\x01",
            "would occur in D-Division, but...\x02\x03",
            "#00108FIt seems the construction progressed\x01",
            "underground, and it finally reached\x01",
            "this place.\x02\x03",
            "#00106FNonexistent demand was fabricated, and\x01",
            "construction proceeded haphazardly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FOh, I see.\x02\x03",
            "#10304FIn other words, it's a\x01",
            "product of government\x01",
            "waste?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FYou're telling me...\x02\x03",
            "#00000FIt seems things have\x01",
            "improved since Dieter\x01",
            "became mayor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00300FAlright. If we're taking\x01",
            "down that wanted monster,\x01",
            "let's head inside already.\x02",
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

    # Function_44_788E end

    def Function_45_7E1D(): pass

    label("Function_45_7E1D")

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
            "#12P#00101F...We've gotten a good idea of\x01",
            "Randy's actions between yesterday\x01",
            "evening and this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00003FYeah, let's try piecing\x01",
            "it together.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x1, 1)

    label("loc_7FC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_82E8")
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
            "#1KWhere did Randy go\x01",
            "first?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Exchange Shop "Neinvalli"\x01",            # 0
            "Repair Shop "Guillaume Factory"\x01",      # 1
            "Casino/Bar "Barca"\x01",                   # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8082")
    ClearScenarioFlags(0x1, 1)

    label("loc_8082")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhere did Randy go next?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Exchange Shop "Neinvalli"\x01",            # 0
            "Repair Shop "Guillaume Factory"\x01",      # 1
            "Casino/Bar "Barca"\x01",                   # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_811B")
    ClearScenarioFlags(0x1, 1)

    label("loc_811B")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhere did Randy go last?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Exchange Shop "Neinvalli"\x01",            # 0
            "Repair Shop "Guillaume Factory"\x01",      # 1
            "Casino/Bar "Barca"\x01",                   # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_81BD")
    ClearScenarioFlags(0x1, 1)

    label("loc_81BD")

    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_824E")

    ChrTalk(
        0x101,
        (
            "#5P#00003F(No... This can't be the\x01",
            "order.)\x02\x03",
            "#00001F(I'll try sorting them\x01",
            "out again.)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8249")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8249")

    Jump("loc_82E3")

    label("loc_824E")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_825E"),
        (SWITCH_DEFAULT, "loc_82AB"),
    )


    label("loc_825E")

    OP_2C(0xAA, 0x1)

    ChrTalk(
        0x101,
        (
            "#5P#00000F(There's no mistake.\x01",
            "This is definitely the\x01",
            "order.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_82E3")

    label("loc_82AB")


    ChrTalk(
        0x101,
        (
            "#5P#00003F(...This is the most\x01",
            "likely order.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_82E3")

    label("loc_82E3")

    Jump("loc_7FC7")

    label("loc_82E8")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Between 3 and 4AM Barca, between\x01",
            "5 and 6 Guillaume Factory, and\x01",
            "around 6 Neinvalli.\x07\x00\x02",
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
            "#5P#00006F─He most likely first went\x01",
            "to Owner Drake to pick up\x01",
            "the trunk he left with him.\x02\x03",
            "#00008FIt's contents... Randy's\x01",
            "special weapon from when he\x01",
            "was a jaeger.\x02\x03",
            "#00001FIt's most likely a kind of\x01",
            "high-power orbal rifle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203FOrbal rifles are normally transported\x01",
            "disassembled.\x02\x03",
            "#00201FBecause it hasn't been used in two\x01",
            "years, Randy brought it to the\x01",
            "maintenance workshop to be serviced...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#11P#10103F─Yeah. No doubt about it.\x02\x03",
            "#10108FHaving a well-maintained\x01",
            "weapon is a matter of life\x01",
            "and death on a battlefield.\x02\x03",
            "#10101FRandy would definitely have\x01",
            "it checked carefully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FFinally, he stopped by the\x01",
            "Exchange Shop to stock up.\x02\x03",
            "#10301FHe bought gunpowder ammo\x01",
            "too. That means he has quite\x01",
            "the special rifle, no?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00108FI've heard the Reinford Company has\x01",
            "models that can change between orbal\x01",
            "and gunpowder operation but...\x02\x03",
            "#00101FRegardless, it probably has a number\x01",
            "of special improvements.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00006FYeah. The Red Constellation\x01",
            "jaegers were using huge rifles\x01",
            "I'd never seen before as well.\x02\x03",
            "#00013F─Alright, I think we've gotten\x01",
            "a handle on Randy's situation,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00206FIt was past 6AM when\x01",
            "Randy left the exchange\x01",
            "shop...\x02\x03",
            "#00208FIt's around 10 AM now,\x01",
            "so around 4 hours have\x01",
            "passed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#11P#10106FIt seems difficult to\x01",
            "track him now, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00003F...No. Even if it's Randy,\x01",
            "his toughness has a limit.\x02\x03",
            "#00001FAnd if he's going up\x01",
            "against Red Constellation,\x01",
            "he'd rest before doing so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FOn top of that, he's planning on using the\x01",
            "terrain to his advantage, attacking\x01",
            "suddenly and finishing it once and for all.\x02\x03",
            "#10302FWell, if he's not planning on a suicide\x01",
            "attack, that's how he'd do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00101FIn any case, we don't\x01",
            "have much time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00013FYeah. Without evidence,\x01",
            "we have no choice but to\x01",
            "go towards Mainz─\x02",
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

    def lambda_8AE5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8AE5)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_8B0A():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8B0A)
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
        "#5P#00011FNo way...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00205FIs it from Randy?\x02",
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
            "#00007F─Lloyd Bannings, Special\x01",
            "Support Section!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Young Man's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Hey there, Lloyd.\x02\x03",
            "Haha, it seems you\x01",
            "thought I was someone\x01",
            "else.\x02",
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
            "#00005FT-This voice is...\x02\x03",
            "#00013FWhy do you have this\x01",
            "number?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Young Man's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Haha, I told you before.\x01",
            "I'm a huge fan of you\x01",
            "guys.\x02\x03",
            "─The Times Department\x01",
            "Store.\x02\x03",
            "If you have time, please\x01",
            "come to the roof.\x07\x00\x02",
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
        "#6P#00201FLloyd. That was...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00108FW-Who was it?\x02",
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
            "#5P#00003F...Cao of Heiyue.\x02\x03",
            "#00013FHe says he's waiting for us\x01",
            "on the roof of the Central\x01",
            "Square department store.\x02",
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
        "#11P#10111FHuh!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10301FAt a time like this?\x01",
            "What could he be\x01",
            "planning?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00006FI don't know. What I do know\x01",
            "is, he wouldn't contact us\x01",
            "without a reason.\x02\x03",
            "#00001FLet's stop by before heading\x01",
            "to the mountains.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00101FU-Understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00201FAnyway, let's hurry.\x02",
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

    # Function_45_7E1D end

    def Function_46_90A5(): pass

    label("Function_46_90A5")

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
            "#12P#00101F...We've gotten a good idea of\x01",
            "Randy's actions between yesterday\x01",
            "evening and this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00003FYeah, let's try piecing\x01",
            "it together.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x1, 1)

    label("loc_9253")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9574")
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
            "#1KWhere did Randy go\x01",
            "first?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Exchange Shop "Neinvalli"\x01",            # 0
            "Repair Shop "Guillaume Factory"\x01",      # 1
            "Casino/Bar "Barca"\x01",                   # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_930E")
    ClearScenarioFlags(0x1, 1)

    label("loc_930E")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhere did Randy go next?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Exchange Shop "Neinvalli"\x01",            # 0
            "Repair Shop "Guillaume Factory"\x01",      # 1
            "Casino/Bar "Barca"\x01",                   # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_93A7")
    ClearScenarioFlags(0x1, 1)

    label("loc_93A7")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KWhere did Randy go last?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Exchange Shop "Neinvalli"\x01",            # 0
            "Repair Shop "Guillaume Factory"\x01",      # 1
            "Casino/Bar "Barca"\x01",                   # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9449")
    ClearScenarioFlags(0x1, 1)

    label("loc_9449")

    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_94DA")

    ChrTalk(
        0x101,
        (
            "#5P#00003F(No... This can't be the\x01",
            "order.)\x02\x03",
            "#00001F(I'll try sorting them\x01",
            "out again.)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_94D5")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_94D5")

    Jump("loc_956F")

    label("loc_94DA")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_94EA"),
        (SWITCH_DEFAULT, "loc_9537"),
    )


    label("loc_94EA")

    OP_2C(0xAA, 0x1)

    ChrTalk(
        0x101,
        (
            "#5P#00000F(There's no mistake.\x01",
            "This is definitely the\x01",
            "order.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_956F")

    label("loc_9537")


    ChrTalk(
        0x101,
        (
            "#5P#00003F(...This is the most\x01",
            "likely order.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_956F")

    label("loc_956F")

    Jump("loc_9253")

    label("loc_9574")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Between 3 and 4AM Barca, between\x01",
            "5 and 6 Guillaume Factory, and\x01",
            "around 6 Neinvalli.\x07\x00\x02",
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
            "#5P#00006F─He most likely first went\x01",
            "to Owner Drake to pick up\x01",
            "the trunk he left with him.\x02\x03",
            "#00008FIt's contents... Randy's\x01",
            "special weapon from when he\x01",
            "was a jaeger.\x02\x03",
            "#00001FIt's most likely a kind of\x01",
            "high-power orbal rifle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203FOrbal rifles are normally transported\x01",
            "disassembled.\x02\x03",
            "#00201FBecause it hasn't been used in two\x01",
            "years, Randy brought it to the\x01",
            "maintenance workshop to be serviced...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103F#11P─Yeah. No doubt about it.\x02\x03",
            "#10108FHaving a well-maintained\x01",
            "weapon is a matter of life\x01",
            "and death on a battlefield.\x02\x03",
            "#10101FRandy would definitely have\x01",
            "it checked carefully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10303FFinally, he stopped by the\x01",
            "Exchange Shop to stock up.\x02\x03",
            "#10301FHe bought gunpowder ammo\x01",
            "too. That means he has quite\x01",
            "the special rifle, no?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00108FI've heard the Reinford Company has\x01",
            "models that can change between orbal\x01",
            "and gunpowder operation but...\x02\x03",
            "#00101FRegardless, it probably has a number\x01",
            "of special improvements.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00006FYeah. The Red Constellation\x01",
            "jaegers were using huge rifles\x01",
            "I'd never seen before as well.\x02\x03",
            "#00013F─Alright, I think we've gotten\x01",
            "a handle on Randy's situation,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00206FIt was past 6AM when\x01",
            "Randy left the exchange\x01",
            "shop...\x02\x03",
            "#00208FIt's around 10 AM now,\x01",
            "so around 4 hours have\x01",
            "passed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#11PIt seems difficult to\x01",
            "track him now, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00003F...No. Even if it's Randy,\x01",
            "his toughness has a limit.\x02\x03",
            "#00001FAnd if he's going up\x01",
            "against Red Constellation,\x01",
            "he'd rest before doing so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FOn top of that, he's planning on using the\x01",
            "terrain to his advantage, attacking\x01",
            "suddenly and finishing it once and for all.\x02\x03",
            "#10302FWell, if he's not planning on a suicide\x01",
            "attack, that's how he'd do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00101FIn any case, we don't\x01",
            "have much time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00013FYeah. Without evidence,\x01",
            "we have no choice but to\x01",
            "go towards Mainz─\x02",
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

    def lambda_9D79():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9D79)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_9D9E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9D9E)
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
        "#5P#00011FNo way...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00205FIs it from Randy?\x02",
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
            "#00007F─Lloyd Bannings, Special\x01",
            "Support Section!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Man's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Hey there, Lloyd.\x02\x03",
            "Haha, it seems you\x01",
            "thought I was someone\x01",
            "else.\x02",
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
            "#00005FT-This voice is...\x02\x03",
            "#00013FWhy do you have this\x01",
            "number?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Man's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Haha, I told you before.\x01",
            "I'm a huge fan of you\x01",
            "guys.\x02\x03",
            "─The Times Department\x01",
            "Store.\x02\x03",
            "If you have time, please\x01",
            "come to the roof.\x07\x00\x02",
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
        "#6P#00201FLloyd. That was...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00108FW-Who was it?\x02",
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
            "#5P#00003F...Cao of Heiyue.\x02\x03",
            "#00013FHe says he's waiting for us\x01",
            "on the roof of the Central\x01",
            "Square department store.\x02",
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
        "#10111F#11PHuh!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10301FAt a time like this?\x01",
            "What could he be\x01",
            "planning?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00006FI don't know. What I do know\x01",
            "is, he wouldn't contact us\x01",
            "without a reason.\x02\x03",
            "#00001FLet's stop by before heading\x01",
            "to the mountains.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00101FU-Understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00201FAnyway, let's hurry.\x02",
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

    # Function_46_90A5 end

    def Function_47_A32E(): pass

    label("Function_47_A32E")

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

    def lambda_A409():
        OP_95(0x101, 8630, 0, 4260, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A409)

    def lambda_A423():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A423)
    Sleep(500)

    def lambda_A437():
        OP_95(0x102, 9430, 0, 3460, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A437)

    def lambda_A451():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A451)
    Sleep(500)

    def lambda_A465():
        OP_95(0x109, 9830, 0, 5460, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A465)

    def lambda_A47F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_A47F)
    Sleep(500)

    def lambda_A493():
        OP_95(0x105, 10630, 0, 4460, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A493)

    def lambda_A4AD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_A4AD)
    Sleep(50)
    WaitChrThread(0x101, 1)

    def lambda_A4C5():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A4C5)
    WaitChrThread(0x102, 1)

    def lambda_A4D6():
        OP_93(0x102, 0x168, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A4D6)
    WaitChrThread(0x109, 1)

    def lambda_A4E7():
        OP_93(0x109, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A4E7)
    WaitChrThread(0x105, 1)

    def lambda_A4F8():
        OP_93(0x105, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A4F8)
    SetMapObjFlags(0x3, 0x0)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x102,
        (
            "#12P#00103FBut Congressman Geval...\x02\x03",
            "#00108FIt might be better if he\x01",
            "was still in the\x01",
            "hospital, honestly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FYes, I think the congressmen\x01",
            "captured in the cult incident\x01",
            "have it even tougher.\x02\x03",
            "#10103FLooks like we got our\x01",
            "information but I don't exactly\x01",
            "know how we'll report it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FYeah, but in the end, evil\x01",
            "deeds always come back to bite\x01",
            "you. It happens all the time.\x02\x03",
            "#00000FIf he were to work hard to\x01",
            "better himself, he would\x01",
            "surely be rewarded someday.\x02\x03",
            "#00004FI hope Geval and the other\x01",
            "congresspeople choose the\x01",
            "right path.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103FYeah... (And Ernest\x01",
            "too...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FThat's our leader for\x01",
            "you.\x02\x03",
            "#10302FHow 'bout it? Wanna head\x01",
            "to Trinity for a drink\x01",
            "after that long chat?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006F*sigh*, there's no way\x01",
            "we can do something like\x01",
            "that while on duty.\x02\x03",
            "#00000F...Anyway, that wraps up\x01",
            "our investigation of\x01",
            "Downtown.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x6A, 0x1, 0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A96E")
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
            "[Investigations Remaining]\x01",           # 0
            "[All 6 Investigations Finished]\x01",      # 1
            "[No Change]\x01",                          # 2
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
        (0, "loc_A941"),
        (1, "loc_A955"),
        (2, "loc_A969"),
        (SWITCH_DEFAULT, "loc_A96E"),
    )


    label("loc_A941")

    ClearScenarioFlags(0x131, 5)
    ClearScenarioFlags(0x131, 6)
    ClearScenarioFlags(0x131, 7)
    ClearScenarioFlags(0x132, 0)
    ClearScenarioFlags(0x132, 1)
    Jump("loc_A96E")

    label("loc_A955")

    SetScenarioFlags(0x131, 5)
    SetScenarioFlags(0x131, 6)
    SetScenarioFlags(0x131, 7)
    SetScenarioFlags(0x132, 0)
    SetScenarioFlags(0x132, 1)
    Jump("loc_A96E")

    label("loc_A969")

    Jump("loc_A96E")

    label("loc_A96E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A9CB")

    ChrTalk(
        0x101,
        (
            "#6P#00000FAlright then, let's\x01",
            "continue our\x01",
            "investigation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AA4A")

    label("loc_A9CB")

    OP_29(0x6A, 0x1, 0x6)

    ChrTalk(
        0x101,
        (
            "#6P#00000FAlright! We've finished\x01",
            "our investigation.\x02\x03",
            "Let's head back to the\x01",
            "City Meeting Hall and\x01",
            "make our report.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AA4A")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_71(0x3, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x3, 0x10)
    SetScenarioFlags(0x132, 2)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 9630, 0, 4460, 225)
    EventEnd(0x5)
    Return()

    # Function_47_A32E end

    def Function_48_AA82(): pass

    label("Function_48_AA82")

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
            "#11POh, it's you guys...\x01",
            "What the hell do you\x01",
            "want?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PAnd is that... Wazy!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PDamn! Get the fuck out,\x01",
            "asshole!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10308FOh man... I guess I'm\x01",
            "not welcome here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F...I understand how you\x01",
            "feel, but please just listen\x01",
            "to what we have to say.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained the professor's\x01",
            "request and that they were here to\x01",
            "collect the medical questionnaire.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        "#11PQuestionnaire?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P...Oh, that. They gave\x01",
            "it to me when I was\x01",
            "still in treatment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00305FOh, so you forgot about\x01",
            "it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHmph. I've no Gnosis\x01",
            "symptoms anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PEven so, I've gotta go\x01",
            "to the hospital again?\x01",
            "How annoying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00101FDino... You're not thinking\x01",
            "straight.\x02\x03",
            "#00103FIn the unlikely event you still\x01",
            "had symptoms, you'd cause\x01",
            "trouble for all the Vipers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PUgh... I guess you're\x01",
            "right...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11P...Ah, fine! Wait there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PI have it here\x01",
            "somewhere, and I'll fill\x01",
            "it out quickly.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AEC7():
        OP_95(0xFE, 44930, -2500, -22750, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_AEC7)
    WaitChrThread(0x8, 1)

    def lambda_AEE5():
        OP_95(0xFE, 47960, -2100, -22440, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_AEE5)
    Sleep(50)

    def lambda_AF02():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AF02)
    Sleep(50)

    def lambda_AF12():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AF12)
    Sleep(50)

    def lambda_AF22():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AF22)
    Sleep(50)

    def lambda_AF32():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_AF32)
    Sleep(50)

    def lambda_AF42():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_AF42)
    WaitChrThread(0x8, 1)
    Sound(116, 0, 100, 0)
    ClearMapObjFlags(0x4, 0x10)
    OP_71(0x4, 0x0, 0x10, 0x0, 0x0)
    OP_79(0x0)
    Sleep(700)

    def lambda_AF71():
        OP_97(0xFE, 0x7D0, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_AF71)

    def lambda_AF8B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_AF8B)
    WaitChrThread(0x8, 2)
    SetChrFlags(0x8, 0x80)
    OP_0D()

    ChrTalk(
        0x109,
        (
            "#6P#10106F*sigh*. Looks like we'll\x01",
            "be able to collect it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FYeah, let's wait a bit.\x02",
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
        (
            "#11P...Here. This is it,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x32E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x32E, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#6P#00000FYeah, it is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00100FThanks Dino!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P...Hmph. You've no\x01",
            "reason to thank me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PNow take Wazy and get\x01",
            "out of here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00006FA-All right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10303F...Sorry to bother you.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x152, 3)
    OP_29(0x70, 0x1, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B281")

    AnonymousTalk(
        0x101,
        (
            "#00000FWith this, we've\x01",
            "collected all the\x01",
            "questionnaires.\x02\x03",
            "Let's deliver them to\x01",
            "Professor Seiland\x01",
            "immediately.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_29(0x70, 0x1, 0x5)

    label("loc_B281")

    OP_93(0x8, 0xE1, 0x0)
    OP_4C(0x8, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 43610, -2500, -21900, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_48_AA82 end

    def Function_49_B2AE(): pass

    label("Function_49_B2AE")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_B328")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x1A2, 0x80)
    Jump("loc_B367")

    label("loc_B328")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_B34A")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x1A2, 0x80)
    Jump("loc_B367")

    label("loc_B34A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_B367")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x1A2, 0x80)

    label("loc_B367")

    OP_68(-2990, 1930, -22180, 5000)
    MoveCamera(44, 22, 0, 5000)
    OP_6E(500, 5000)
    SetCameraDistance(49730, 5000)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_B473")
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x104, 0x80)
    ClearChrFlags(0x1A2, 0x80)
    SetChrPos(0x1A2, 2260, 0, 22750, 180)
    SetChrPos(0x102, 1410, 0, 22750, 180)
    SetChrPos(0x101, 2900, 0, 24450, 180)
    SetChrPos(0x104, 910, 0, 24450, 180)

    def lambda_B405():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_B405)

    def lambda_B41F():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B41F)
    Sleep(100)

    def lambda_B43C():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B43C)
    Sleep(50)

    def lambda_B459():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B459)
    Jump("loc_B616")

    label("loc_B473")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_B547")
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x109, 0x80)
    ClearChrFlags(0x1A2, 0x80)
    SetChrPos(0x1A2, 2260, 0, 22750, 180)
    SetChrPos(0x102, 1410, 0, 22750, 180)
    SetChrPos(0x101, 2900, 0, 24450, 180)
    SetChrPos(0x109, 910, 0, 24450, 180)

    def lambda_B4D9():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_B4D9)

    def lambda_B4F3():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B4F3)
    Sleep(100)

    def lambda_B510():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B510)
    Sleep(50)

    def lambda_B52D():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B52D)
    Jump("loc_B616")

    label("loc_B547")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_B616")
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x105, 0x80)
    ClearChrFlags(0x1A2, 0x80)
    SetChrPos(0x1A2, 2260, 0, 22750, 180)
    SetChrPos(0x102, 1410, 0, 22750, 180)
    SetChrPos(0x101, 2900, 0, 24450, 180)
    SetChrPos(0x105, 910, 0, 24450, 180)

    def lambda_B5AD():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_B5AD)

    def lambda_B5C7():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B5C7)
    Sleep(100)

    def lambda_B5E4():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B5E4)
    Sleep(50)

    def lambda_B601():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B601)

    label("loc_B616")

    OP_6F(0x79)
    OP_68(2000, 1930, 2050, 7000)
    MoveCamera(41, 21, 0, 7000)
    OP_6E(500, 7000)
    SetCameraDistance(17730, 7000)
    OP_6F(0x79)

    ChrTalk(
        0x1A2,
        (
            "This is... Another\x01",
            "desolate place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F...This is Downtown. It was\x01",
            "passed over during development\x01",
            "of the rest of the city.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x1A2)

    ChrTalk(
        0x1A2,
        (
            "Hmph... There are places\x01",
            "like this in every\x01",
            "nation.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        (
            "#12PI've had enough. We're\x01",
            "going back to East\x01",
            "Street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FS-Sure, alright.\x02",
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

    # Function_49_B2AE end

    def Function_50_B7C2(): pass

    label("Function_50_B7C2")

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

    def lambda_B8B2():
        OP_95(0xFE, 2450, 0, 8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B8B2)
    Sleep(10)

    def lambda_B8CF():
        OP_95(0xFE, 1250, 0, 8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B8CF)
    Sleep(20)

    def lambda_B8EC():
        OP_95(0xFE, 2260, 0, 9650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B8EC)
    Sleep(10)

    def lambda_B909():
        OP_95(0xFE, 3460, 0, 9650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B909)
    Sleep(20)

    def lambda_B926():
        OP_95(0xFE, 1060, 0, 9650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B926)
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
        "Man's Voice",
        "#4SWhat did you say!? Hey!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xE,
        "Man's Voice",
        (
            "#4SHah!? You're nothing but\x01",
            "a big pile of excuses!\x02",
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
        "#00005FThat voice...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FLloyd, look there!\x02",
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
            "#6PYou asshole... Are you\x01",
            "serious!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#6PWhat if Wald got drunk\x01",
            "and beat your face in?\x01",
            "What then, huh!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "That's why I'm thinking\x01",
            "of ideas to prevent\x01",
            "that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "You're not gonna think\x01",
            "of anything. Get out of\x01",
            "here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#6PEarlier you said, "If he sees the\x01",
            "view from the top of the tower, he'll\x01",
            "cheer up, won't he?", didn't you!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#6PIf Wald could be cheered up just by\x01",
            "going to a high place, we wouldn't\x01",
            "be talking about this right now!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#6P#4SI can't stand idiots\x01",
            "like you! You idiot!!\x02",
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
            "#4SY-Youuu...!! Don't make\x01",
            "me say it again!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#4SYou're a hundred times more\x01",
            "of an idiot! You didn't come\x01",
            "up with a single good idea!\x02",
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
        "#6PWhat did you say!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#6P#4SYou wanna go? Huh!?\x02",
    )

    CloseMessageWindow()
    Sleep(100)

    ChrTalk(
        0x101,
        "#5P#N#4S#00007FStop it you two!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_68(280, 2000, -1490, 3000)
    MoveCamera(36, 20, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(15650, 3000)

    def lambda_BE58():
        OP_95(0xFE, 2450, 0, 500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BE58)
    Sleep(10)

    def lambda_BE75():
        OP_95(0xFE, 1250, 0, 500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BE75)
    Sleep(20)

    def lambda_BE92():
        OP_95(0xFE, 2260, 0, 2150, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BE92)
    Sleep(10)

    def lambda_BEAF():
        OP_95(0xFE, 3460, 0, 2150, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_BEAF)
    Sleep(20)

    def lambda_BECC():
        OP_95(0xFE, 1060, 0, 2150, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_BECC)
    Sleep(200)
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_BF10():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_BF10)
    Sleep(10)

    def lambda_BF20():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_BF20)
    WaitChrThread(0x105, 1)
    WaitChrThread(0xD, 1)
    OP_6F(0x79)

    ChrTalk(
        0xE,
        "#12PYou assholes...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00301FWhoa, you guys have your weapons\x01",
            "out, even though you're on the\x01",
            "same side. That's not like you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#12PHmph... None of your\x01",
            "business, asshole!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#12PI told you before,\x01",
            "Wazy!! It's because you\x01",
            "made fun of us before!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#12PYeah! It's your fault\x01",
            "Wald's like that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#12PEverything's your fault,\x01",
            "Wazy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#5P#10303F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10105FH-Hey! Wazy's not...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#12PAnyway, nothing'll change\x01",
            "at this rate... We've\x01",
            "gotta beat you up first!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#12PYeah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#12PHuey, you can steamroll\x01",
            "'em after that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#00101F(W-What do we do?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00301FThey've completely lost\x01",
            "their cool.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00010F(Ugh. If it's like this,\x01",
            "then we'll have to\x01",
            "subdue them...)\x02",
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
        "Youth's Voice",
        "Hmph... How sad.\x02",
    )

    CloseMessageWindow()
    VolumeBGM(0x64, 0x7D0)
    OP_68(-7930, 6500, -5030, 6000)
    MoveCamera(41, 31, 0, 6000)
    OP_6E(500, 6000)
    SetCameraDistance(14890, 6000)
    Sleep(500)

    def lambda_C32F():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C32F)
    Sleep(10)

    def lambda_C33F():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C33F)
    Sleep(20)

    def lambda_C34F():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C34F)
    Sleep(10)

    def lambda_C35F():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C35F)
    Sleep(20)

    def lambda_C36F():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C36F)
    Sleep(10)

    def lambda_C37F():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_C37F)
    Sleep(10)

    def lambda_C38F():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_C38F)
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
        "Blond Young Man",
        (
            "#5P#13904FConflict brings forth\x01",
            "nothing... Only the chains\x01",
            "of foolish hatred.\x02\x03",
            "#13902FTo you, I give a song.\x02\x03",
            "A gentle yet painful song,\x01",
            "to bind the confused\x01",
            "hearts of the people...\x02",
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
        "Blond Young Man",
        (
            "#70A#50WBrightly#1500W #50Wshooting\x01",
            "stars,#1000W #50Wleaving\x01",
            "trails in the skies...\x05\x02",
        )
    )

    Sleep(7000)

    NpcTalk(
        0x18,
        "Blond Young Man",
        (
            "#70A#50WLike a guiding\x01",
            "light,#1000W #50Wthey show\x01",
            "me the way to your eyes...\x05\x02",
        )
    )

    Sleep(7000)

    NpcTalk(
        0x18,
        "Blond Young Man",
        (
            "#70A#50WThis yearning#1500W\x01",
            "#50Wpassion,#1000W #50Wtears\x01",
            "my heart in twain...\x05\x02",
        )
    )

    Sleep(7000)

    NpcTalk(
        0x18,
        "Blond Young Man",
        (
            "#70A#50WAnd the cruel moon#1000W\x01",
            "#50Wmocks my pain...\x05\x02",
        )
    )

    Sleep(7000)

    NpcTalk(
        0x18,
        "Blond Young Man",
        (
            "#70A#50WIf this fleeting\x01",
            "dream#3000W #50Wshall\x01",
            "never be...\x05\x02",
        )
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
        "#4SHey, shut up, blondie!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Blond Young Man",
        "#12P#13911FUgh!?\x02",
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
        "Blond Young Man",
        (
            "#11P#13909FI-Is something wrong, cute little kitty?\x02\x03",
            "#13902FYes, I'm in the middle of a performance,\x01",
            "as you can see. Sorry, but you'll need\x01",
            "to ask for my autograph later.\x02\x03",
            "#13910FI should say, if you get kicked in a\x01",
            "place like this it's danger─\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x19,
        "#6PWho cares about that!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#6PQuit banging around on\x01",
            "the roof of my shop and\x01",
            "get down from there!\x02",
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
        "Blond Young Man",
        "#13911FO-Okay, all right─\x02",
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
        "#12PGET DOWN!!\x02",
    )

    CloseMessageWindow()

    def lambda_CAE3():
        OP_95(0xFE, -17240, 5400, -1780, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_CAE3)
    Sleep(800)
    OP_95(0x19, -16880, 5400, -1950, 4000, 0x0)
    Sleep(1000)
    Sound(1013, 0, 100, 0)

    NpcTalk(
        0x18,
        "Youth's Voice",
        "#2SAh!?\x02",
    )

    CloseMessageWindow()
    Sound(833, 0, 40, 0)
    Sound(992, 0, 40, 0)
    Sleep(50)
    Sound(811, 0, 100, 0)

    ChrTalk(
        0x19,
        "#2SAh, he fell.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#2SYou alive, blondie?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Youth's Voice",
        "#2SUgh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#2SOh, so you are.\x02",
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
        "#12PAh... About that.\x02",
    )

    CloseMessageWindow()

    def lambda_CCB1():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CCB1)
    Sleep(10)

    def lambda_CCC1():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CCC1)
    Sleep(20)

    def lambda_CCD1():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_CCD1)
    Sleep(10)

    def lambda_CCE1():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_CCE1)
    Sleep(20)

    def lambda_CCF1():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_CCF1)

    ChrTalk(
        0xD,
        "#12PI'm bored. Later.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#12P#5AHah, what was with that\x01",
            "blond guy...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xD, 0x5A, 0x1F4)
    OP_99(0xD, 0xE, 0x1F4, 0x1388, 0x0)
    Sound(811, 0, 60, 0)
    OP_9B(0x1, 0xD, 0xB4, 0xC8, 0x1388, 0x0)

    ChrTalk(
        0xE,
        "#12PUgh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#6PDon't worry about him.\x01",
            "Let's go.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_CDAB():
        OP_95(0xFE, 6640, 0, -7350, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_CDAB)
    Sleep(800)

    def lambda_CDC8():
        OP_95(0xFE, 7700, 0, -7010, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_CDC8)

    def lambda_CDE2():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CDE2)
    Sleep(50)

    def lambda_CDF2():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CDF2)
    Sleep(50)

    def lambda_CE02():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_CE02)
    Sleep(50)

    def lambda_CE12():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_CE12)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xE, 1)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)

    ChrTalk(
        0x101,
        "#5P#00012FT-There they went...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#5P#10306FHmm. I guess he helped\x01",
            "us, in a way.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x18, -3400, 0, -6690, 0)

    NpcTalk(
        0x18,
        "Youth's Voice",
        (
            "Hmph... In the Demon City, I\x01",
            "was merely nipping a\x01",
            "blossoming quarrel in the bud.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_CEFE():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CEFE)
    Sleep(50)

    def lambda_CF0E():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CF0E)
    Sleep(50)

    def lambda_CF1E():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_CF1E)
    Sleep(50)

    def lambda_CF2E():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_CF2E)
    Sleep(50)

    def lambda_CF3E():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_CF3E)

    NpcTalk(
        0x18,
        "Youth's Voice",
        (
            "With love and devotion,\x01",
            "the melody of my lute\x01",
            "brings true peace.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Youth's Voice",
        (
            "My own genius scares me\x01",
            "sometimes.\x02",
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

    def lambda_D046():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_D046)
    OP_96(0x18, 0xFFFFFD4E, 0x0, 0xFFFFECB4, 0x3E8, 0x0)

    def lambda_D067():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_D067)
    OP_96(0x18, 0xFFFFFC68, 0x0, 0xFFFFF330, 0x7D0, 0x0)

    def lambda_D088():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_D088)
    OP_96(0x18, 0x320, 0x0, 0xFFFFF416, 0x5DC, 0x0)

    def lambda_D0A9():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_D0A9)
    OP_96(0x18, 0x654, 0x0, 0xFFFFFA10, 0x3E8, 0x0)

    def lambda_D0CA():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D0CA)
    Sleep(50)

    def lambda_D0DA():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D0DA)
    Sleep(50)

    def lambda_D0EA():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D0EA)
    Sleep(50)

    def lambda_D0FA():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D0FA)
    Sleep(50)

    def lambda_D10A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D10A)
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
            "#6P#00105FU-Umm... Are you all\x01",
            "right? I heard a thud\x01",
            "earlier.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Blond Young Man",
        (
            "#11P#13904FHmph, worry not,\x01",
            "mademoiselle.\x02\x03",
            "#13902FSuch a height is nothing to\x01",
            "fear for I, who flies through\x01",
            "the skies of this continent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00306FI don't get it...\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Blond Young Man",
        (
            "#11P#13903FI sensed trouble not too\x01",
            "long ago, but...\x02\x03",
            "#13900FI've pulled myself\x01",
            "together. All me to\x01",
            "continue my performance.\x02\x03",
            "#13904FPlease enjoy, everyone.\x02",
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
        "#6P#00011FT-that's plenty!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106F(L-Lloyd. Could he\x01",
            "be...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001F(Yeah, blonde with a white\x01",
            "coat...)\x02\x03",
            "#00006F(Mueller said he was a troublesome\x01",
            "character, but... He's honestly\x01",
            "worse than I was expecting.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001F...Ahem. You are\x01",
            "Olivier, correct?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Blond Young Man",
        "#11P#13904FYes... The very same.\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("Blond Young Man")

    AnonymousTalk(
        0xFF,
        (
            "Wandering musician and seeker of\x01",
            "love, Olivier Lenheim.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x18,
        (
            "You all are lucky to have heard one\x01",
            "of my famous guerilla recitals.\x02\x03",
            "Carve this day into your hearts. It\x01",
            "may be a once-in-a-lifetime\x01",
            "experience for you all.\x02",
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
        "#6P#00006FR-Right.\x02",
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
            "#11P#13905FAh, come to think of it... Why\x01",
            "do you know my name?\x02\x03",
            "#13902FI don't remember giving out my\x01",
            "name ever since I came to\x01",
            "Crossbell. Have we met before?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FWe're from the Crossbell\x01",
            "Police, Special Support\x01",
            "Section.\x02\x03",
            "We're looking for you\x01",
            "because of a certain Mr.\x01",
            "Mueller's request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FYou must know him,\x01",
            "correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11P#13905FOhhh, so you're the...\x02\x03",
            "#13904FHmph... That Mueller's\x01",
            "as much of a worrywart\x01",
            "as ever.\x02\x03",
            "#13912FOur love for each other\x01",
            "will not fade with only\x01",
            "this much time apart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10105FHuh!? So that's the kind\x01",
            "of relationship you guys\x01",
            "have...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00306FI doubt it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FAnyway... Can we ask you\x01",
            "to return to Mueller?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11P#13903FI am sorry, but I cannot comply\x01",
            "with your request.\x02\x03",
            "#13900FIn any case, I am quite busy\x01",
            "tomorrow. I must enjoy Crossbell\x01",
            "now, while I have the chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00105FBusy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11P#13904FHmph, just talking to\x01",
            "myself.\x02\x03",
            "However, if you say you\x01",
            "cannot overlook this...\x02\x03",
            "#13902FI will do whatever I\x01",
            "have to to make you\x01",
            "overlook it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FHuh? What are you\x01",
            "planning?\x02",
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
            "#12P#13907F#4SHuh!? Is that Captain\x01",
            "Julia up there!?\x02",
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

    def lambda_DC21():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DC21)
    Sleep(10)

    def lambda_DC31():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DC31)
    Sleep(20)

    def lambda_DC41():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_DC41)
    Sleep(10)

    def lambda_DC51():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_DC51)
    Sleep(20)

    def lambda_DC61():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_DC61)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00011FWhat...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00105FReally!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10107F#4SW-Where!?\x02",
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
            "#10105FHey, t-there's... no one\x01",
            "there, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FWhat!?\x02",
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

    def lambda_DDFF():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DDFF)
    Sleep(10)

    def lambda_DE0F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DE0F)
    Sleep(20)

    def lambda_DE1F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_DE1F)
    Sleep(10)

    def lambda_DE2F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_DE2F)
    Sleep(20)

    def lambda_DE3F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_DE3F)
    Sleep(500)

    ChrTalk(
        0x18,
        (
            "#5P#13902FHmph, I'm looking\x01",
            "forward to our next\x01",
            "meeting!\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_63(0x18, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_93(0x18, 0x0, 0x1F4)

    def lambda_DEAB():
        OP_95(0xFE, 1900, 0, 20650, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_DEAB)
    Sleep(500)

    ChrTalk(
        0x101,
        "#12P#00011FW-Wait!\x02",
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
        "#12P#00106FH-He got away...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#11P#10101FWe fell for the oldest\x01",
            "trick in the book...\x02\x03",
            "#10106FThere's no way Captain\x01",
            "Julia would be in a\x01",
            "place like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00306FMan. A troublesome guy,\x01",
            "but in a different way\x01",
            "than Lechter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FA-Anyway, let's try\x01",
            "chasing after him.\x02\x03",
            "#00003FBut, where did he go...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10303FWe should probably check the\x01",
            "places we discussed earlier.\x02\x03",
            "#10300FWe found him in Downtown, so\x01",
            "let's try the others. Maybe\x01",
            "Back Street or Waterfront Area?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#11P#10100FAnyway, let's go!\x02",
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

    # Function_50_B7C2 end

    def Function_51_E1E0(): pass

    label("Function_51_E1E0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E22F")
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
    Jump("Function_51_E1E0")

    label("loc_E22F")

    Return()

    # Function_51_E1E0 end

    def Function_52_E230(): pass

    label("Function_52_E230")

    Sleep(23000)
    OP_95(0xFE, -12870, 5400, -2670, 1000, 0x0)
    OP_93(0xFE, 0x5A, 0x0)
    Sleep(4000)
    OP_9D(0xFE, 0xFFFFD4AE, 0x1900, 0xFFFFF466, 0x4B0, 0xBB8)
    Sound(50, 0, 100, 0)
    Return()

    # Function_52_E230 end

    def Function_53_E26F(): pass

    label("Function_53_E26F")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Apartment "Maison Imelda"\x01",
            " \x01",
            "～Unmanaged～\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x321, 0x0)"), scpexpr(EXPR_END)), "loc_E35F")
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Use the Maison Imelda key?\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E35A")
    OP_5A()
    Sleep(500)
    Sound(806, 0, 100, 0)
    Sleep(1000)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Unlocked "Maison Imelda".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_29(0x67, 0x1, 0x1)
    SetScenarioFlags(0x133, 1)
    SetMapObjFlags(0x1, 0x10)
    OP_65(0x1, 0x1)

    label("loc_E35A")

    Jump("loc_E526")

    label("loc_E35F")

    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E48E")

    ChrTalk(
        0x101,
        "#00000F...Looks like it's locked.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FThere's a monster\x01",
            "extermination support\x01",
            "request for this apartment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI think the manager is Mrs.\x01",
            "Imelda, the shopkeeper at\x01",
            "that antique shop.\x02\x03",
            "#00000FLet's go to the antique\x01",
            "shop on Back Street and\x01",
            "borrow the key.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_E526")

    label("loc_E48E")


    ChrTalk(
        0x101,
        (
            "#00000FA monster extermination\x01",
            "support request for this\x01",
            "apartment came in.\x02\x03",
            "#00000FLet's go to the antique\x01",
            "shop on Back Street and\x01",
            "borrow the key.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E526")

    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_53_E26F end

    SaveToFile()

Try(main)
