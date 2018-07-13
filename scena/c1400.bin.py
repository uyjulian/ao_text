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
        "Function_7_149D",         # 07, 7
        "Function_8_1AE6",         # 08, 8
        "Function_9_21BF",         # 09, 9
        "Function_10_26E3",        # 0A, 10
        "Function_11_2AAF",        # 0B, 11
        "Function_12_354A",        # 0C, 12
        "Function_13_35C6",        # 0D, 13
        "Function_14_368B",        # 0E, 14
        "Function_15_3692",        # 0F, 15
        "Function_16_369C",        # 10, 16
        "Function_17_3BD9",        # 11, 17
        "Function_18_3CEC",        # 12, 18
        "Function_19_3E41",        # 13, 19
        "Function_20_3F2D",        # 14, 20
        "Function_21_3FF0",        # 15, 21
        "Function_22_4033",        # 16, 22
        "Function_23_407E",        # 17, 23
        "Function_24_4118",        # 18, 24
        "Function_25_4181",        # 19, 25
        "Function_26_4AE3",        # 1A, 26
        "Function_27_4BB5",        # 1B, 27
        "Function_28_4BB6",        # 1C, 28
        "Function_29_50BB",        # 1D, 29
        "Function_30_512E",        # 1E, 30
        "Function_31_51A1",        # 1F, 31
        "Function_32_5214",        # 20, 32
        "Function_33_5287",        # 21, 33
        "Function_34_66F5",        # 22, 34
        "Function_35_6DE7",        # 23, 35
        "Function_36_6E84",        # 24, 36
        "Function_37_6EC5",        # 25, 37
        "Function_38_77EB",        # 26, 38
        "Function_39_7857",        # 27, 39
        "Function_40_78C3",        # 28, 40
        "Function_41_792F",        # 29, 41
        "Function_42_796C",        # 2A, 42
        "Function_43_79A9",        # 2B, 43
        "Function_44_79E6",        # 2C, 44
        "Function_45_7F78",        # 2D, 45
        "Function_46_923B",        # 2E, 46
        "Function_47_A4FF",        # 2F, 47
        "Function_48_AC88",        # 30, 48
        "Function_49_B4C7",        # 31, 49
        "Function_50_B9CC",        # 32, 50
        "Function_51_E501",        # 33, 51
        "Function_52_E551",        # 34, 52
        "Function_53_E590",        # 35, 53
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
            "Since you have too many, you gave it up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x7, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1442")

    Jump("loc_1491")

    label("loc_1447")

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

    label("loc_1491")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_134B end

    def Function_7_149D(): pass

    label("Function_7_149D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14BD")
    Call(0, 48)
    Return()

    label("loc_14BD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1737")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16A2")

    ChrTalk(
        0xFE,
        "Ah, the Special Support Section...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FDino... Umm, the\x01",
            "other members are...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yeah... Luckily, even senior Kｷki,\x01",
            "the worst seriosuly wounded,\x01",
            "regained consciousness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As for the other seniors, some were\x01",
            "discharched and are coming back to Downtown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, as you'd expect, I think it's hard\x01",
            "to restart the group right away, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But if I wait here, I guess\x01",
            "they'll probably turn up?\x02",
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
        "#00003FI see...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18D, 2)
    Jump("loc_1732")

    label("loc_16A2")


    ChrTalk(
        0xFE,
        (
            "Even so... \x01",
            "The city is noisy this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They talk about the question of independence,\x01",
            "but I just wish they'd be a little quieter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1732")

    Jump("loc_1AE2")

    label("loc_1737")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1745")
    Jump("loc_1AE2")

    label("loc_1745")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1753")
    Jump("loc_1AE2")

    label("loc_1753")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1761")
    Jump("loc_1AE2")

    label("loc_1761")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_176F")
    Jump("loc_1AE2")

    label("loc_176F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_177D")
    Jump("loc_1AE2")

    label("loc_177D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_178B")
    Jump("loc_1AE2")

    label("loc_178B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1799")
    Jump("loc_1AE2")

    label("loc_1799")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_17A7")
    Jump("loc_1AE2")

    label("loc_17A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1A5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_197F")

    ChrTalk(
        0xFE,
        "Ah, the Special Support Section...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "H-Hey Wazy. I heard\x01",
            "you went head to head\x01",
            "against Mr. Wald...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F...If you have a question I'll answer it.\x01",
            "Do you want to hear about that from me?\x02",
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
        "N-No, nevermind...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "M-Mr. Wald's the strongest.\x01",
            "I'd never believe you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F(Wow, that jerk of Wald\x01",
            "is loved for sure.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(Yeah. To him,\x01",
            "he's like a hero.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14C, 6)
    Jump("loc_19E9")

    label("loc_197F")


    ChrTalk(
        0xFE,
        (
            "...Mr. Wald's always \x01",
            "gonna be the strongest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Y-Yeah! If I don't believe\x01",
            "in him, who ever will?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19E9")

    Jump("loc_1A58")

    label("loc_19EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19FD")
    Jump("loc_1A58")

    label("loc_19FD")


    ChrTalk(
        0xFE,
        (
            "...I gave you that\x01",
            "questionnaire\x01",
            "already, didn't I!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Take it and\x01",
            "get outta\x01",
            "here!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A58")

    Jump("loc_1AE2")

    label("loc_1A5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1A6B")
    Jump("loc_1AE2")

    label("loc_1A6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1AE2")

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
            "If Mr. Wald finds you out here,\x01",
            "don't come crying to me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AE2")

    TalkEnd(0xFE)
    Return()

    # Function_7_149D end

    def Function_8_1AE6(): pass

    label("Function_8_1AE6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1B81")

    ChrTalk(
        0xFE,
        (
            "I don't really get it, but it\x01",
            "seems to have become\x01",
            "a terrible situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Perhaps it's a good idea not\x01",
            "to leave home for awhile.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21BB")

    label("loc_1B81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1B8F")
    Jump("loc_21BB")

    label("loc_1B8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1C0D")

    ChrTalk(
        0xFE,
        (
            "I heard there's been\x01",
            "a disturbance at the\x01",
            "town of Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They say there are\x01",
            "injured... How truly sad.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21BB")

    label("loc_1C0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1C1B")
    Jump("loc_21BB")

    label("loc_1C1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1C9D")

    ChrTalk(
        0xFE,
        (
            "Come to think of it, I haven't\x01",
            "seen the usual kids today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, I wonder if they\x01",
            "went somewhere to play.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21BB")

    label("loc_1C9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1D48")

    ChrTalk(
        0xFE,
        (
            "I understand that a referendum on the pros\x01",
            "and cons of independence will be held soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't really get it, but I must\x01",
            "ponder about it properly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21BB")

    label("loc_1D48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1EA8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E30")

    ChrTalk(
        0xFE,
        (
            "There has been a lot of big news that\x01",
            "shakes the foundations of society lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There are a lot of things\x01",
            "I don't understand, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, I just don't want to\x01",
            "see everyone's smiles fade.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1EA3")

    label("loc_1E30")


    ChrTalk(
        0xFE,
        (
            "I don't understand\x01",
            "complicated subjects, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, I just don't want to\x01",
            "see everyone's smiles fade.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EA3")

    Jump("loc_21BB")

    label("loc_1EA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1F05")

    ChrTalk(
        0xFE,
        "Uh uh, good weather today too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The kids are happy.\x01",
            "How heartwarming.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21BB")

    label("loc_1F05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_205F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FA9")

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
            "Uh uh, I wonder how it\x01",
            "looks from up close.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_205A")

    label("loc_1FA9")


    ChrTalk(
        0xFE,
        (
            "The man wearing a white coat who passed\x01",
            "by just now must be a traveling musician.\x02",
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

    label("loc_205A")

    Jump("loc_21BB")

    label("loc_205F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2153")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20E9")

    ChrTalk(
        0xFE,
        (
            "That Sister is someone I don't\x01",
            "see around here often, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, she's good with\x01",
            "kids, isn't she.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_214E")

    label("loc_20E9")


    ChrTalk(
        0xFE,
        (
            "That Sister is good\x01",
            "with kids, isn't she.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, I get a warm feeling\x01",
            "just looking at her.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_214E")

    Jump("loc_21BB")

    label("loc_2153")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2161")
    Jump("loc_21BB")

    label("loc_2161")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_21BB")

    ChrTalk(
        0xFE,
        (
            "Uh uh, there's sunny and\x01",
            "warm weather today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I might just fall asleep.\x02",
    )

    CloseMessageWindow()

    label("loc_21BB")

    TalkEnd(0xFE)
    Return()

    # Function_8_1AE6 end

    def Function_9_21BF(): pass

    label("Function_9_21BF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2232")

    ChrTalk(
        0xFE,
        (
            "Hehe, somehow, the city's\x01",
            "in a huuuge uproar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They say we might go\x01",
            "to war with someone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26DF")

    label("loc_2232")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2325")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_229B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_225A")
    Call(0, 18)
    Jump("loc_2296")

    label("loc_225A")


    ChrTalk(
        0xFE,
        (
            "Kyahaha, my old man! \x01",
            "He's almost like a good citizen.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2296")

    Jump("loc_2320")

    label("loc_229B")


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
            "If we can eat stuff like that every day,\x01",
            "reconstruction 'll be done in no time!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2320")

    Jump("loc_26DF")

    label("loc_2325")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_239E")

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
            "Hehe, it's the same as usual\x01",
            "for my old man, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26DF")

    label("loc_239E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_23D1")

    ChrTalk(
        0xFE,
        "Kyahaha, it's a natural shower.\x02",
    )

    CloseMessageWindow()
    Jump("loc_26DF")

    label("loc_23D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_23DF")
    Jump("loc_26DF")

    label("loc_23DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_23ED")
    Jump("loc_26DF")

    label("loc_23ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2458")

    ChrTalk(
        0xFE,
        (
            "Woohoo! Special\x01",
            "income, get!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Nishishi... Roser, let's\x01",
            "have meat today. Yeah, meat.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26DF")

    label("loc_2458")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_24DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24A0")

    ChrTalk(
        0xFE,
        (
            "Shoo shoo!\x01",
            "Sir Vaan is passin' through!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_24D7")

    label("loc_24A0")


    ChrTalk(
        0xFE,
        (
            "Kyahaha, my old man\x01",
            "might be drinking around now!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24D7")

    Jump("loc_26DF")

    label("loc_24DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_24EA")
    Jump("loc_26DF")

    label("loc_24EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_24FB")
    Call(0, 16)
    Jump("loc_26DF")

    label("loc_24FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_END)), "loc_2560")

    ChrTalk(
        0xFE,
        (
            "Hah! It came down\x01",
            "with a lotta force!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Rain started falling before I knew it!\x02",
    )

    CloseMessageWindow()
    Jump("loc_26DF")

    label("loc_2560")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_25BC")

    ChrTalk(
        0xFE,
        "Rain's falling steadily.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If it was all juice,\x01",
            "my belly would burst.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26DF")

    label("loc_25BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_26DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_266C")

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
    Jump("loc_26DF")

    label("loc_266C")


    ChrTalk(
        0xFE,
        (
            "Those delinquent groups\x01",
            "have quieted down lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Kyahaha, are they out of\x01",
            "fighting spirit or something?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26DF")

    TalkEnd(0xFE)
    Return()

    # Function_9_21BF end

    def Function_10_26E3(): pass

    label("Function_10_26E3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_271C")

    ChrTalk(
        0xFE,
        (
            "*chuckle*...\x01",
            "Isn't that dangerous?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AAB")

    label("loc_271C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_27DD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2772")

    ChrTalk(
        0xFE,
        (
            "*chuckle*... Your\x01",
            "dad is unexpectedly\x01",
            "reliable, Vaan.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27D8")

    label("loc_2772")


    ChrTalk(
        0xFE,
        (
            "There's going to be another\x01",
            "emergency feeding come evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder what it's going to be.\x02",
    )

    CloseMessageWindow()

    label("loc_27D8")

    Jump("loc_2AAB")

    label("loc_27DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2838")

    ChrTalk(
        0xFE,
        (
            "A place called "Mainz"\x01",
            "seems to be in trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "How much, I wonder?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2AAB")

    label("loc_2838")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2889")

    ChrTalk(
        0xFE,
        (
            "*chuckle*... Should we go somewhere\x01",
            "to snatch away some soap?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AAB")

    label("loc_2889")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2897")
    Jump("loc_2AAB")

    label("loc_2897")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_28A5")
    Jump("loc_2AAB")

    label("loc_28A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_28D7")

    ChrTalk(
        0xFE,
        "Kyahaha, I can eat tons today.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2AAB")

    label("loc_28D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2960")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2923")

    ChrTalk(
        0xFE,
        "Kyahaha, Lady Roser too is passin' through!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_295B")

    label("loc_2923")


    ChrTalk(
        0xFE,
        (
            "*chuckle*...\x01",
            "Your dad might have\x01",
            "passed out, Vaan.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_295B")

    Jump("loc_2AAB")

    label("loc_2960")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_296E")
    Jump("loc_2AAB")

    label("loc_296E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_297F")
    Call(0, 16)
    Jump("loc_2AAB")

    label("loc_297F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_END)), "loc_29EC")

    ChrTalk(
        0xFE,
        (
            "Is that what\x01",
            "they call a one-\x01",
            "on-one fight?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*chuckle*... \x01",
            "It was certainly powerful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AAB")

    label("loc_29EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2A6A")

    ChrTalk(
        0xFE,
        (
            "But if you did that, your tummy\x01",
            "would rumble and rumble while moving\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*chuckle*... \x01",
            "Like your dad's...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AAB")

    label("loc_2A6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2AAB")

    ChrTalk(
        0xFE,
        (
            "*chuckle*... \x01",
            "You sure do like making\x01",
            "noise, Vaan.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AAB")

    TalkEnd(0xFE)
    Return()

    # Function_10_26E3 end

    def Function_11_2AAF(): pass

    label("Function_11_2AAF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2AF1")

    ChrTalk(
        0xFE,
        (
            "A -wwar... \x01",
            "That's no good. No good at all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3546")

    label("loc_2AF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2C44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_END)), "loc_2B6A")

    ChrTalk(
        0xFE,
        (
            "*rustle*... Umm, this is...\x01",
            "No good, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Then this one... \x01",
            "Hmm, this one's a miss too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C3F")

    label("loc_2B6A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BDE")

    ChrTalk(
        0xFE,
        "Thanks you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll take responsibility\x01",
            "and exchange for mira\x01",
            "the scraps you gave me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C3F")

    label("loc_2BDE")


    ChrTalk(
        0xFE,
        (
            "And now that my\x01",
            "stomach's full, I\x01",
            "can work hard again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanks for\x01",
            "all your\x01",
            "help, guys.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C3F")

    Jump("loc_3546")

    label("loc_2C44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2DD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D27")

    ChrTalk(
        0xFE,
        (
            "Hmm, there's mud in the cracks in the\x01",
            "pavement because of yesterday's rain, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And there's a lot of trash in those crack... Uh uh, why\x01",
            "does it always have to be my turn when this happens.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2DD3")

    label("loc_2D27")


    ChrTalk(
        0xFE,
        (
            "Ta-dah! This is where I bring out my\x01",
            "secret weapon, a "handy wooden stick".\x02",
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

    label("loc_2DD3")

    Jump("loc_3546")

    label("loc_2DD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2DE6")
    Jump("loc_3546")

    label("loc_2DE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2E87")

    ChrTalk(
        0xFE,
        (
            "*sweep, sweep*...\x01",
            "There. This area's\x01",
            "sparkling again today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, though cleaning never ends, this\x01",
            "sense of accomplishment is the best.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3546")

    label("loc_2E87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2EFC")

    ChrTalk(
        0xFE,
        (
            "I haven't seen too many people\x01",
            "fighting around here lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uh uh, that's a very good thing.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3546")

    label("loc_2EFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_304A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FC2")

    ChrTalk(
        0xFE,
        (
            "I guess it was last week. \x01",
            "A delinquent held something to his\x01",
            "ear and was muttering something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What could that thing be?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F(Could it be an ENIGMA...?)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3045")

    label("loc_2FC2")


    ChrTalk(
        0xFE,
        (
            "I guess it was last week. \x01",
            "A delinquent held something to his\x01",
            "ear and was muttering something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What could that thing be?\x02",
    )

    CloseMessageWindow()

    label("loc_3045")

    Jump("loc_3546")

    label("loc_304A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_30C4")

    ChrTalk(
        0xFE,
        (
            "Orchis Tower\x01",
            "is super tall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard it was 250 arge... I wonder\x01",
            "how many times my height that is?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3546")

    label("loc_30C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_324D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31CB")

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
            "to a place like this, they said.\x01",
            "I don't know why.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sweep, sweep*...\x01",
            "I've got to make it\x01",
            "prettier than usual.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3248")

    label("loc_31CB")


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
            "*sweep, sweep*...\x01",
            "I've got to make it\x01",
            "prettier than usual.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3248")

    Jump("loc_3546")

    label("loc_324D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_325E")
    Call(0, 16)
    Jump("loc_3546")

    label("loc_325E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_326C")
    Jump("loc_3546")

    label("loc_326C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3546")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34B6")

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
            "#10300FGood morning, Kanon.\x01",
            "How are you today?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x105, 0)

    ChrTalk(
        0xFE,
        "Ah, Mr. Wazy. Good morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, I guess there's a lot\x01",
            "of bottle trash today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I won't forgive bad manners, but it's \x01",
            "interesting looking at their various shapes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Look, the middle of\x01",
            "this one's narrow.\x01",
            "It's pretty, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHu hu, indeed. It's a nice shape.\x02\x03",
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
    Jump("loc_3546")

    label("loc_34B6")


    ChrTalk(
        0xFE,
        (
            "Bottles have different shapes and\x01",
            "looking through them is interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Look, this one's dull but shines\x01",
            "when you hold it up to light.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3546")

    TalkEnd(0xFE)
    Return()

    # Function_11_2AAF end

    def Function_12_354A(): pass

    label("Function_12_354A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35C2")

    ChrTalk(
        0xFE,
        (
            "*sigh*, this scene work\x01",
            "really takes it out of ya.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, I guess it's\x01",
            "good training, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35C2")

    label("loc_35C2")

    TalkEnd(0xFE)
    Return()

    # Function_12_354A end

    def Function_13_35C6(): pass

    label("Function_13_35C6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3687")

    ChrTalk(
        0x10,
        (
            "A-At any rate... Seeing\x01",
            "this destroyed apartment...\x01",
            "H-How intense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Thank goodness it was a-bandoned.\x01",
            "It would've been terrible if\x01",
            "there had been anyone i-inside.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3687")

    label("loc_3687")

    TalkEnd(0xFE)
    Return()

    # Function_13_35C6 end

    def Function_14_368B(): pass

    label("Function_14_368B")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_14_368B end

    def Function_15_3692(): pass

    label("Function_15_3692")

    TalkBegin(0xFE)
    Call(0, 16)
    TalkEnd(0xFE)
    Return()

    # Function_15_3692 end

    def Function_16_369C(): pass

    label("Function_16_369C")

    OP_4B(0x12, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38D7")

    ChrTalk(
        0x12,
        (
            "#04403F"I see. I'll go see Anna, then."\x02\x03",
            "The woman was a witch, so surely\x01",
            "she'd know Ron's location.\x02\x03",
            "He followed the road to Anna's hut.\x01",
            "Suddenly, Mark's ears heard the\x01",
            "piercing cry of a monster.\x02",
        )
    )

    CloseMessageWindow()
    Sound(18, 0, 100, 0)
    Sleep(300)

    ChrTalk(
        0xC,
        "*thrilled*... And then? And then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Say, let's have lunch early.\x01",
            "You brought bread for us, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "*chuckle*... Should we get it\x01",
            "in secret and then eat it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105F(Miss Ries... \x01",
            "Looks like she's here\x01",
            "for Sunday School.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(She's reading them a fairytale, huh...\x01",
            "It's a heartwarming scene, somehow.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14C, 7)
    Jump("loc_3BC8")

    label("loc_38D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AF7")

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
            "Tch, how boring. Roser, let's sleep\x01",
            "until she brings out some bread.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "*chuckle*...  Yeah, let's.\x02",
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
            "#04400FThose who don't write\x01",
            "anything will be considered\x01",
            "absent and go without lunch.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xA)

    ChrTalk(
        0xA,
        (
            "Urgh, seriously!?\x01",
            "What a tyrant!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "*chuckle*... \x01",
            "Today's Sister is really strict.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3BC8")

    label("loc_3AF7")


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
            "Wah, wait, wait, from the beginning!\x01",
            "Read it from the beginning!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "*chuckle*... \x01",
            "You're flustered now, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Uh uh, let's enjoy it together.\x02",
    )

    CloseMessageWindow()

    label("loc_3BC8")

    OP_4C(0x12, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_16_369C end

    def Function_17_3BD9(): pass

    label("Function_17_3BD9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C99")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BFB")
    Call(0, 18)
    Jump("loc_3C94")

    label("loc_3BFB")


    ChrTalk(
        0xFE,
        (
            "Man. Even though we have emergency food,\x01",
            "it's just work and work from the middle of the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wanna finish this quick\x01",
            "and get myself a drink.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C94")

    Jump("loc_3CE8")

    label("loc_3C99")


    ChrTalk(
        0xFE,
        (
            "But, the sun's\x01",
            "really bright.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It's poison to night owls like myself.\x02",
    )

    CloseMessageWindow()

    label("loc_3CE8")

    TalkEnd(0xFE)
    Return()

    # Function_17_3BD9 end

    def Function_18_3CEC(): pass

    label("Function_18_3CEC")

    OP_4B(0xA, 0xFF)
    OP_4B(0x13, 0xFF)
    TurnDirection(0xA, 0x0, 0)

    ChrTalk(
        0xA,
        (
            "Kyahaha, that old man! \x01",
            "It's rare for him to work from noon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I think the landlord will drive us\x01",
            "out of our apartment if he doesn't\x01",
            "help with the reconstruction?\x02",
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
        "Shut up and help me with this, will ya?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    SetScenarioFlags(0x0, 5)
    OP_93(0xA, 0x13B, 0x0)
    OP_93(0x13, 0x13B, 0x0)
    OP_4C(0xA, 0xFF)
    OP_4C(0x13, 0xFF)
    Return()

    # Function_18_3CEC end

    def Function_19_3E41(): pass

    label("Function_19_3E41")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EB1")

    ChrTalk(
        0xFE,
        (
            "Now then, gotta tidy\x01",
            "up quickly today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "First of all, to measure the size...done.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F29")

    label("loc_3EB1")


    ChrTalk(
        0xFE,
        (
            "*phew*, it's slightly late, but\x01",
            "I can finally take a breather.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Alright... I'll do my best this afternoon too!\x02",
    )

    CloseMessageWindow()

    label("loc_3F29")

    TalkEnd(0xFE)
    Return()

    # Function_19_3E41 end

    def Function_20_3F2D(): pass

    label("Function_20_3F2D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F78")

    ChrTalk(
        0xFE,
        "Papa's working for everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "He's so cool♪\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FEC")

    label("loc_3F78")

    SetChrName("Rimah")

    ChrTalk(
        0x14,
        "Papa, this broth's delicious.\x02",
    )

    CloseMessageWindow()
    SetChrName("Melson")

    ChrTalk(
        0x15,
        (
            "Yeah, really. Papa can feel the\x01",
            "power welling up inside him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FEC")

    TalkEnd(0xFE)
    Return()

    # Function_20_3F2D end

    def Function_21_3FF0(): pass

    label("Function_21_3FF0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4005")
    Call(0, 23)
    Jump("loc_402F")

    label("loc_4005")


    ChrTalk(
        0xFE,
        "What can I say, that's ridiculous...\x02",
    )

    CloseMessageWindow()

    label("loc_402F")

    TalkEnd(0xFE)
    Return()

    # Function_21_3FF0 end

    def Function_22_4033(): pass

    label("Function_22_4033")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4048")
    Call(0, 23)
    Jump("loc_407A")

    label("loc_4048")


    ChrTalk(
        0xFE,
        (
            "I would have liked Mr. Wald\x01",
            "to see it too...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_407A")

    TalkEnd(0xFE)
    Return()

    # Function_22_4033 end

    def Function_23_407E(): pass

    label("Function_23_407E")

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
            "Hyahah, seriously. I want to\x01",
            "bungee jump from the roof!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_23_407E end

    def Function_24_4118(): pass

    label("Function_24_4118")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Now then, it's time to\x01",
            "start my Downtown patrol.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...I wonder where I should start from.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_4118 end

    def Function_25_4181(): pass

    label("Function_25_4181")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_418E")
    Call(0, 26)
    Return()

    label("loc_418E")

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
            "#6P#00000FGood afternoon. We haven't seen\x01",
            "you since the Cult incident, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FIt's been awhile, Dino.\x02\x03",
            "Judging from what we see, it looks\x01",
            "like you've returned to your group?\x02",
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
            "#11PThey said it was because of\x01",
            "the drug that I picked fights\x01",
            "with Mr. Wald and the others...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P...To take responsibility,\x01",
            "I was spanked with a bat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10106FS-Spanked with a bat, you say...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FHu hu, well at least you\x01",
            "were able to return.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#11PWazy... So it's\x01",
            "true you joined\x01",
            "the police.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PIt's because of you that Mr. Wald...!\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00005FWald? \x01",
            "What happened to him?\x02",
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
            "#11PMr. Wald has been in \x01",
            "the worst kind of mood lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PIf you value your life,\x01",
            "don't come near this place.\x02",
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
        "#11P...Everything is the fault of Wazy there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PThe Testaments have\x01",
            "been quiet ever since\x01",
            "the incident...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PAnd now their leader, Wazy,\x01",
            "couldn't even set things properly \x01",
            "and has suddenly become a police dog.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F...I see.\x02\x03",
            "#00001FIn summary, he's become\x01",
            "irritable and violent because\x01",
            "his brawling rival is gone, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10106FI can't say I don't understand how he feels, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10308F...Oh boy.\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#11PDon't "oh boy" me! Bastard,\x01",
            "do you know what you've done!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PIt's because of you that Mr.\x01",
            "Wald is hardly ever at Ignis\x01",
            "lately, you know that!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10303F...If he wants to do that,\x01",
            "then he should.\x02\x03",
            "#10300FHu hu. I am just doing whatever\x01",
            "I want, too, you see.\x02\x03",
            "And because of that, I found it\x01",
            "unjust to be blamed by you all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PGh...\x02",
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
            "#11PIf Mr. Wald sees you here, \x01",
            "I won't be responsible for what happens\x01",
            "not only to Wazy, but to any of you too.\x02",
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

    # Function_25_4181 end

    def Function_26_4AE3(): pass

    label("Function_26_4AE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_END)), "loc_4BB4")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B6C")

    ChrTalk(
        0x101,
        (
            "#00008F...We shouldn't enter\x01",
            "this place for awhile.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FYeah... It'd be\x01",
            "helpful if you didn't.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_4B9E")

    label("loc_4B6C")


    ChrTalk(
        0x101,
        "#00003F...Let's refrain from entering Ignis.\x02",
    )

    CloseMessageWindow()

    label("loc_4B9E")

    Sleep(50)
    SetChrPos(0x0, 44540, -2500, -22490, 270)
    EventEnd(0x4)

    label("loc_4BB4")

    Return()

    # Function_26_4AE3 end

    def Function_27_4BB5(): pass

    label("Function_27_4BB5")

    Return()

    # Function_27_4BB5 end

    def Function_28_4BB6(): pass

    label("Function_28_4BB6")

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
            "#12P#10108FExchange Shop "Neinvalli"...\x02\x03",
            "#10106FIt definitely left an\x01",
            "impression on me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#5PWell, places like that have\x01",
            "their own sense of virtue.\x02\x03",
            "#00100FWe should be grateful that\x01",
            "she told us that much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00006FThat's right...\x02\x03",
            "#00008F...But a man like a\x01",
            "man-eating tiger, huh.\x02\x03",
            "#00001FAssuming he's not a terrorist,\x01",
            "it seems likely he's a jaeger...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10303FThough it's strange for\x01",
            "a jaeger to be alone.\x02\x03",
            "#10300FShould we report\x01",
            "this to the Chief?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4FC8")

    ChrTalk(
        0x101,
        (
            "#11P#00001FYeah, let's.\x02\x03",
            "#00003F(If jaegers are involved, Randy would\x01",
            "probably know something, but...)\x02\x03",
            "#00000F(Well, the support requests are finished too, so\x01",
            "shall we head back to the Support Section for now?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5085")

    label("loc_4FC8")


    ChrTalk(
        0x101,
        (
            "#11P#00001FYeah, let's.\x02\x03",
            "#00003F(If jaegers are involved, Randy would\x01",
            "probably know something, but...)\x02\x03",
            "#00000F(Well, we still have support requests left,\x01",
            "so let's take care of them.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5085")

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

    # Function_28_4BB6 end

    def Function_29_50BB(): pass

    label("Function_29_50BB")


    def lambda_50C0():
        OP_95(0xFE, -13000, 0, -10500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_50C0)

    def lambda_50DA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_50DA)
    WaitChrThread(0xFE, 1)

    def lambda_50EF():
        OP_95(0xFE, -10000, 0, -11500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_50EF)
    WaitChrThread(0xFE, 1)

    def lambda_510D():
        OP_95(0xFE, -6500, 0, -9600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_510D)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xFA, 0x1F4)
    Return()

    # Function_29_50BB end

    def Function_30_512E(): pass

    label("Function_30_512E")


    def lambda_5133():
        OP_95(0xFE, -13000, 0, -10500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5133)

    def lambda_514D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_514D)
    WaitChrThread(0xFE, 1)

    def lambda_5162():
        OP_95(0xFE, -10000, 0, -11500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5162)
    WaitChrThread(0xFE, 1)

    def lambda_5180():
        OP_95(0xFE, -7700, 0, -9000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5180)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xC8, 0x1F4)
    Return()

    # Function_30_512E end

    def Function_31_51A1(): pass

    label("Function_31_51A1")


    def lambda_51A6():
        OP_95(0xFE, -13000, 0, -10500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_51A6)

    def lambda_51C0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_51C0)
    WaitChrThread(0xFE, 1)

    def lambda_51D5():
        OP_95(0xFE, -10000, 0, -11500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_51D5)
    WaitChrThread(0xFE, 1)

    def lambda_51F3():
        OP_95(0xFE, -7500, 0, -11200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_51F3)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x14, 0x1F4)
    Return()

    # Function_31_51A1 end

    def Function_32_5214(): pass

    label("Function_32_5214")


    def lambda_5219():
        OP_95(0xFE, -13000, 0, -10500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5219)

    def lambda_5233():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5233)
    WaitChrThread(0xFE, 1)

    def lambda_5248():
        OP_95(0xFE, -10000, 0, -11500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5248)
    WaitChrThread(0xFE, 1)

    def lambda_5266():
        OP_95(0xFE, -8700, 0, -10600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5266)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x46, 0x1F4)
    Return()

    # Function_32_5214 end

    def Function_33_5287(): pass

    label("Function_33_5287")

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

    def lambda_5403():
        OP_97(0x101, 0x0, 0x0, 0xFA0, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5403)
    Sleep(100)

    def lambda_5420():
        OP_97(0x102, 0x0, 0x0, 0xFA0, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5420)
    Sleep(100)

    def lambda_543D():
        OP_97(0x109, 0x0, 0x0, 0xFA0, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_543D)
    Sleep(100)

    def lambda_545A():
        OP_97(0x105, 0x0, 0x0, 0xFA0, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_545A)
    SetCameraDistance(19000, 2000)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 0)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x17,
        "Ferocious Voice",
        "#3564V#30W──Hey, hold up.\x02",
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

    def lambda_5552():
        OP_93(0x105, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5552)
    Sleep(50)

    def lambda_5562():
        OP_93(0x109, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5562)
    Sleep(50)

    def lambda_5572():
        OP_93(0x102, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5572)
    Sleep(50)

    def lambda_5582():
        OP_93(0x101, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5582)
    Sleep(50)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    Sleep(1000)

    def lambda_55A5():
        OP_96(0xFE, 0x19DC, 0x0, 0xFFFFDEFE, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_55A5)
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
        "#10308F#2908V#40W#6P#NWald?\x02",
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

    def lambda_56B9():
        OP_96(0xFE, 0x76C, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_56B9)
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
            "#5P#00108F(He's the leader of the delinquent\x01",
            "group called Saber Viper...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FWald, what's up?\x02\x03",
            "#10300FYour members haven't seen\x01",
            "you around lately, huh?\x02",
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
            "#30WShut up. Don't concern\x01",
            "yourself with me.\x02\x03",
            "But how about you, bastard...\x01",
            "You ended up a dog of the\x01",
            "police, didn't you?\x02\x03",
            "What're you plannin', huh!?\x02",
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
            "#01601F#30W#11PYou bastard, are you fucking serious?\x02\x03",
            "#01603FDoing something like stepping away\x01",
            "from your group without settling things\x01",
            "with me, the great Wald Wales...\x02\x03",
            "#01607FThink I'll forgive you fer that? Huh!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10308F#30W............\x02",
    )

    CloseMessageWindow()

    def lambda_5A2E():
        OP_96(0xFE, 0x384, 0x0, 0x13EC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5A2E)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x101,
        "#6P#00011FWald, wait a second!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106FT-There're reasons for that...\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0x17,
        (
            "#01607F#4S#11PShut up! \x01",
            "Stay out of this!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x17,
        (
            "#01603F#11PWazy, I don't know what you're\x01",
            "after by joining the cops...\x02\x03",
            "#01608FBut you know──\x02",
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
            "#01607F#11P──You don't seriously think\x01",
            "I'm gonna let you walk out\x01",
            "of 'ere scot free, do you!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F......!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00001FKh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#00106FT-This is bad...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10303F#30W──Wald.\x02",
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(1680, 1300, 3250, 1200)

    def lambda_5C6D():
        OP_95(0xFE, 1900, 0, 4800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5C6D)
    Sleep(500)

    def lambda_5C8A():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5C8A)

    def lambda_5C97():
        OP_96(0xFE, 0x2BC, 0x0, 0x13EC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5C97)
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
            "#6P#10308F#30WIt's fine. Let me handle this.\x02\x03",
            "#10306FWald. It should be\x01",
            "painfully obvious.\x02\x03",
            "And it's true for both\x01",
            "Testaments and Saber Viper.\x02\x03",
            "#10301FYou know they're not places\x01",
            "you can stay forever, right?\x02",
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
            "#10300FBut, though my members were\x01",
            "weak at first, they've grown.\x02\x03",
            "And now, even without me, they can\x01",
            "even go toe-to-toe against you all.\x02\x03",
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
        "#5P#00108F#30WWazy......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#11P#01608F#30W............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304F#30WSame for you Saber Vipers too.\x02\x03",
            "Though many of you are thugs, you were\x01",
            "strong enough to resist the mafia's offer.\x02\x03",
            "#10300FAnd so, Wald... I think you'll\x01",
            "find your path one day too.\x02",
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
        "#11P#01604F#60W#10A...Hehe......\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x3E8)

    ChrTalk(
        0x17,
        "#11P#01609F#2809V#4S#25A#40WHA HA HA HA HA HAH!!!\x02",
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
            "#01611F#3565V#30W#11PI never thought you'd ever\x01",
            "spit out something that stupid.\x02\x03",
            "#01607F#3566VEnough, don't spout anythig anymore!\x02\x03",
            "#3561VYou defiled this "sanctuary"! \x01",
            "I'll never forgive you fer this!\x02",
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
        "#12P#00011FHey, Wazy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10303F#30WLloyd, there's no need for you to get involved.\x02\x03",
            "#10301FI have to take care\x01",
            "of this myself.\x02",
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
            "#11P#01604F#30WHehe. It looks like you still\x01",
            "got some sense in you....\x02\x03",
            "#01602FI'll give you a thorough beatin' and\x01",
            "then have you grovel before me...\x02\x03",
            "Hehe, then maybe you'll\x01",
            "snap out of it a little.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x105,
        "#6P#10303F#2909V#30W──Enough talk.\x02",
    )

    CloseMessageWindow()
    OP_24(0xB5D)
    OP_57(0x0)
    OP_5A()
    StopBGM(0xBB8)

    ChrTalk(
        0x17,
        "#11P#01601F#3567VAh...?\x02",
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

    def lambda_6522():
        OP_96(0xFE, 0x12C, 0x0, 0x13EC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6522)
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
        "#00005F(This is...!)\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7452", 0)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x105,
        (
            "#5P#10301F#2910V#30W#20AWald──\x01",
            "#40WI'm going to go all out!\x02",
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

    # Function_33_5287 end

    def Function_34_66F5(): pass

    label("Function_34_66F5")

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

    def lambda_6859():
        OP_95(0xFE, 1900, 0, 2600, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6859)
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

    def lambda_68F9():
        OP_9D(0xFE, 0x76C, 0x0, 0xFFFFFE0C, 0x898, 0x2BC)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_68F9)
    Sound(2800, 255, 100, 0)
    Sleep(500)
    CancelBlur(0)
    WaitChrThread(0x17, 1)
    Sound(862, 0, 100, 0)
    Sound(833, 0, 30, 0)
    OP_82(0x0, 0x64, 0xBB8, 0x12C)
    SetChrSubChip(0x17, 0x3)

    def lambda_6949():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x12C, 0x2BC)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_6949)
    WaitChrThread(0x17, 1)
    Sound(811, 0, 100, 0)
    OP_82(0x0, 0x64, 0xBB8, 0x64)

    ChrTalk(
        0x17,
        "#01610F#13A#11P*cough*...!\x02",
    )

    CloseMessageWindow()
    Sleep(800)

    def lambda_69A4():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_69A4)
    Sleep(1200)

    ChrTalk(
        0x17,
        (
            "#11P#01611F#40W...Ugh...bastard...\x02\x03",
            "Don't tell me... You've been\x01",
            "holding back...all this time...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10306F#30W...I'm not Randy... This was...\x01",
            "Just a little illegal technique.\x02\x03",
            "#10308FBut I didn't hold\x01",
            "anything back today.\x02\x03",
            "#10301FThis is...\x01",
            "My last show of good faith to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#11P#01611F#50WUgh... \x01",
            "...Wazy...damn you...\x02",
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
            "Have been quite fun.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_6B77():

        label("loc_6B77")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_6B77")

    QueueWorkItem2(0x101, 2, lambda_6B77)

    def lambda_6B89():

        label("loc_6B89")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_6B89")

    QueueWorkItem2(0x102, 2, lambda_6B89)

    def lambda_6B9B():

        label("loc_6B9B")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_6B9B")

    QueueWorkItem2(0x109, 2, lambda_6B9B)
    OP_68(1900, 1000, 3100, 5000)
    SetCameraDistance(17500, 5000)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)

    def lambda_6BCF():
        OP_95(0xFE, 1900, 0, 20000, 1800, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6BCF)
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

    def lambda_6C32():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_6C32)
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
            "#11P#01611F#3568V#50W#45ADon't bullshit me...\x01",
            "...I'll never accept this...!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(1000)

    ChrTalk(
        0x17,
        (
            "#11P#01610F#3569V#50W#40AYou asshole! Holdin' back against me!? \x01",
            "I'll never accept it!!\x02",
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
        "#11P#01607F#3570V#5S#50W#20AWAZYYYYYYY!!!\x02",
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

    # Function_34_66F5 end

    def Function_35_6DE7(): pass

    label("Function_35_6DE7")

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

    def lambda_6E2D():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x44C, 0x2BC)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6E2D)
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

    # Function_35_6DE7 end

    def Function_36_6E84(): pass

    label("Function_36_6E84")

    EndChrThread(0xFE, 0x2)

    def lambda_6E8D():
        OP_95(0xFE, 1900, 0, 8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6E8D)
    WaitChrThread(0xFE, 1)

    def lambda_6EAB():
        OP_95(0xFE, 1900, 0, 20000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6EAB)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_36_6E84 end

    def Function_37_6EC5(): pass

    label("Function_37_6EC5")

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

    def lambda_710F():
        OP_97(0xFE, 0xFFFFCB44, 0x0, 0x34BC, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_710F)
    Sleep(100)
    EndChrThread(0x109, 0xFF)
    SetChrPos(0x109, 18500, -2500, -23800, 315)

    def lambda_7141():
        OP_97(0xFE, 0xFFFFCB44, 0x0, 0x34BC, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7141)
    Sleep(100)
    EndChrThread(0x104, 0xFF)
    SetChrPos(0x104, 20000, -2500, -22300, 315)

    def lambda_7173():
        OP_97(0xFE, 0xFFFFCB44, 0x0, 0x34BC, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7173)
    Fade(500)
    OP_68(16200, 0, -20000, 0)
    MoveCamera(315, 27, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(23500, 0)
    OP_68(5200, 1000, -9000, 8500)
    MoveCamera(59, 27, 0, 8500)
    SetCameraDistance(19500, 8500)
    WaitChrThread(0x101, 1)

    def lambda_71E9():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_71E9)
    WaitChrThread(0x109, 1)

    def lambda_71FA():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_71FA)
    WaitChrThread(0x104, 1)

    def lambda_720B():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_720B)
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
        "#6P#10308F...How was it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11PNo good. They don't know\x01",
            "anything, it seems.\x02\x03",
            "#00013FLooks like no one's seen\x01",
            "Wald for the past few days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#11PHe must be keepin' his\x01",
            "distance from his underlings.\x02\x03",
            "#00301FOr maybe they're makin' fun of us,\x01",
            "pretendin' not to know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10106FYes... They seemed desperate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10303F...I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#6PWe tried to ask the\x01",
            "Testaments again, but...\x02\x03",
            "#00108FIt doesn't seem like anyone\x01",
            "has seen Mr. Wald recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00206FYes... Although it seems he was often\x01",
            "spotted dead drunk and worn out before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F#11PI see... It seems we don't know the\x01",
            "background behind this at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F#11PBut where the hell did\x01",
            "he get "Gnosis" from...?\x02",
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
            "#12P#10113F...Wazy, are you ok?\x02\x03",
            "Somehow, you don't look well...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FHu hu, I'm probably cold because of the rain.\x02\x03",
            "#10300FFor now, I asked Abbas and the\x01",
            "others to gather some info.\x02\x03",
            "Let's set aside the matter of Wald\x01",
            "and return to the Support Section.\x02",
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
            "#00102F#6P*giggle*, I feel like we've been\x01",
            "indebted to her more, lately.\x02",
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

    # Function_37_6EC5 end

    def Function_38_77EB(): pass

    label("Function_38_77EB")


    def lambda_77F0():
        OP_95(0xFE, 45000, -2500, -22500, 2200, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_77F0)

    def lambda_780A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_780A)
    WaitChrThread(0xFE, 1)

    def lambda_781F():
        OP_95(0xFE, 38500, -2500, -23800, 2200, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_781F)
    WaitChrThread(0xFE, 1)

    def lambda_783D():
        OP_95(0xFE, 27500, -2500, -23800, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_783D)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_38_77EB end

    def Function_39_7857(): pass

    label("Function_39_7857")


    def lambda_785C():
        OP_95(0xFE, 45000, -2500, -23300, 2200, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_785C)

    def lambda_7876():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7876)
    WaitChrThread(0xFE, 1)

    def lambda_788B():
        OP_95(0xFE, 38500, -2500, -24600, 2200, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_788B)
    WaitChrThread(0xFE, 1)

    def lambda_78A9():
        OP_95(0xFE, 27500, -2500, -24600, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_78A9)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_39_7857 end

    def Function_40_78C3(): pass

    label("Function_40_78C3")


    def lambda_78C8():
        OP_95(0xFE, 45000, -2500, -21700, 2200, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_78C8)

    def lambda_78E2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_78E2)
    WaitChrThread(0xFE, 1)

    def lambda_78F7():
        OP_95(0xFE, 38500, -2500, -23000, 2200, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_78F7)
    WaitChrThread(0xFE, 1)

    def lambda_7915():
        OP_95(0xFE, 27500, -2500, -23000, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7915)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_40_78C3 end

    def Function_41_792F(): pass

    label("Function_41_792F")


    def lambda_7934():
        OP_95(0xFE, -9500, 0, -10400, 2200, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7934)
    WaitChrThread(0xFE, 1)

    def lambda_7952():
        OP_95(0xFE, -3500, 0, -9000, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7952)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_41_792F end

    def Function_42_796C(): pass

    label("Function_42_796C")


    def lambda_7971():
        OP_95(0xFE, -9500, 0, -9800, 2200, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7971)
    WaitChrThread(0xFE, 1)

    def lambda_798F():
        OP_95(0xFE, -3500, 0, -8400, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_798F)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_42_796C end

    def Function_43_79A9(): pass

    label("Function_43_79A9")


    def lambda_79AE():
        OP_95(0xFE, -9500, 0, -11000, 2200, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_79AE)
    WaitChrThread(0xFE, 1)

    def lambda_79CC():
        OP_95(0xFE, -3500, 0, -9600, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_79CC)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_43_79A9 end

    def Function_44_79E6(): pass

    label("Function_44_79E6")

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
            "#12P#00000FSo this is the entrance to Geofront D-Division, \x01",
            "where the Wanted Monster in that extermination \x01",
            "request appeared, huh...\x02\x03",
            "#00003FThis was closed off for the\x01",
            "longest time, but it seems it's\x01",
            "been opened due to the request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203FHm, there is one small problem, though...\x02\x03",
            "#00200FWhy is there a Geofront\x01",
            "entrance in Downtown that is\x01",
            "not connected to the orbal net?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00305FYeah, now that you mention it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10105FWasn't Downtown left behind\x01",
            "by the city development?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103FYes... Before, congressmen and\x01",
            "government officials said construction\x01",
            "would occur in D-Division, but...\x02\x03",
            "#00108FIt seems the construction progressed\x01",
            "underground, and it finally reached this place.\x02\x03",
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
            "product of government waste?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FYou're telling me...\x02\x03",
            "#00000FIt seems things have improved\x01",
            "since Mr. Dieter became mayor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00300FAlright. If we're takin' down that Wanted\x01",
            "Monster, let's head inside already.\x02",
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

    # Function_44_79E6 end

    def Function_45_7F78(): pass

    label("Function_45_7F78")

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
            "#12P#00101F...We've gotten a good idea of Randy's actions\x01",
            "between yesterday evening and this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00003FYeah, let's try piecing them together.\x02",
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x1, 1)

    label("loc_8124")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8443")
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
            "#1KWhere did Randy go first?\x07\x00\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_81DF")
    ClearScenarioFlags(0x1, 1)

    label("loc_81DF")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8278")
    ClearScenarioFlags(0x1, 1)

    label("loc_8278")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_831A")
    ClearScenarioFlags(0x1, 1)

    label("loc_831A")

    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_83A9")

    ChrTalk(
        0x101,
        (
            "#5P#00003F(No... \x01",
            "This isn't the order.)\x02\x03",
            "#00001F(I'll try sorting them out again.)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_83A4")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_83A4")

    Jump("loc_843E")

    label("loc_83A9")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_83B9"),
        (SWITCH_DEFAULT, "loc_8406"),
    )


    label("loc_83B9")

    OP_2C(0xAA, 0x1)

    ChrTalk(
        0x101,
        "#5P#00000F(There's no mistake. This is definitely the order.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_843E")

    label("loc_8406")


    ChrTalk(
        0x101,
        "#5P#00003F(...This is the most likely order.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_843E")

    label("loc_843E")

    Jump("loc_8124")

    label("loc_8443")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Between 3 and 4AM "Barca", between\x01",
            "5 and 6 "Guillaume Factory",\x01",
            "and around 6 "Neinvalli".\x07\x00\x02",
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
            "#5P#00006F──He most likely first went\x01",
            "to Owner Drake to pick up\x01",
            "the trunk he left with him.\x02\x03",
            "#00008FIt's content... Randy's special\x01",
            "weapon from when he was a jaeger.\x02\x03",
            "#00001FIt's most likely a kind of\x01",
            "high-power orbal rifle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203FOrbal rifles are normally\x01",
            "transported disassembled.\x02\x03",
            "#00201FBecause it hasn't been used in\x01",
            "two years, Randy brought it to\x01",
            "the repair factory to be serviced...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#11P#10103F──Yes, no doubt about it.\x02\x03",
            "#10108FHaving a well-maintained weapon is a\x01",
            "matter of life and death on a battlefield.\x02\x03",
            "#10101FSenior Randy would definitely\x01",
            "have it checked carefully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FFinally, he stopped by the\x01",
            "exchange shop to stock up.\x02\x03",
            "#10301FHe bought gunpowder ammo too.\x01",
            "It means he has quite the special rifle, no?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00108FI've heard the Reinford Corporation have\x01",
            "models that can change between orbal\x01",
            "and gunpowder operation but...\x02\x03",
            "#00101FRegardless, it probably has a\x01",
            "number of special improvements.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00006FYeah. The Red Constellation \x01",
            "jaegers too used huge rifles\x01",
            "I had never seen before.\x02\x03",
            "#00013F──Alright, I think we've gotten a\x01",
            "handle on Randy's situation, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00206FIt was past 6AM when Mr. \x01",
            "Randy left the exchange shop...\x02\x03",
            "#00208FIt's around 10AM now, so\x01",
            "around 4 hours have passed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#11P#10106FIt seems difficult to\x01",
            "track senior now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00003F...No. Even if it's Randy,\x01",
            "his toughness has a limit.\x02\x03",
            "#00001FAnd if he's going up against the "Red\x01",
            "Constellation", he'd rest before doing so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FOn top of that, he'll use the terrain to\x01",
            "his advantage, attacking suddenly\x01",
            "and finishing it once and for all.\x02\x03",
            "#10302FWell, if he's not planning\x01",
            "on a suicide attack,\x01",
            "that's how he'd do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00101F...In any case we don't\x01",
            "have much time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00013FYeah. Without evidence, we have\x01",
            "no choice but to go towards Mainz──\x02",
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

    def lambda_8C46():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8C46)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_8C6B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8C6B)
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
        "#6P#00205FIs it from Mr. Randy?\x02",
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
            "#00007F──Special Support Section,\x01",
            "Lloyd Bannings speaking!\x02",
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
            "Hey there, Mr. Lloyd.\x02\x03",
            "...Hu hu, it seems you thought\x01",
            "I was someone else.\x02",
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
            "#00013F...Why do you have this number?\x02",
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
            "Hu hu, I told you before.\x01",
            "I am a huge fan of you guys.\x02\x03",
            "──The Times department store.\x02\x03",
            "If you are free, please\x01",
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
        (
            "#6P#00201F...Mr. Lloyd.\x01",
            "That call...\x02",
        )
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
            "#5P#00003F...Cao from the "Heiyue".\x02\x03",
            "#00013FIt seems he's waiting for us on the roof\x01",
            "of the Central Square department store.\x02",
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
            "#10301FAt a time like this...\x01",
            "What could he be planning?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00006FI don't know. \x01",
            "What I do know is, he wouldn't\x01",
            "contact us without a reason.\x02\x03",
            "#00001FLet's stop by before heading\x01",
            "to the mountain path.\x02",
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

    # Function_45_7F78 end

    def Function_46_923B(): pass

    label("Function_46_923B")

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
            "#12P#00101F...We've gotten a good idea of Randy's actions\x01",
            "between yesterday evening and this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00003FYeah, let's try piecing them together.\x02",
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x1, 1)

    label("loc_93EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_970A")
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
            "#1KWhere did Randy go first?\x07\x00\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_94A6")
    ClearScenarioFlags(0x1, 1)

    label("loc_94A6")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_953F")
    ClearScenarioFlags(0x1, 1)

    label("loc_953F")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_95E1")
    ClearScenarioFlags(0x1, 1)

    label("loc_95E1")

    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9670")

    ChrTalk(
        0x101,
        (
            "#5P#00003F(No... \x01",
            "This isn't the order.)\x02\x03",
            "#00001F(I'll try sorting them out again.)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_966B")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_966B")

    Jump("loc_9705")

    label("loc_9670")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_9680"),
        (SWITCH_DEFAULT, "loc_96CD"),
    )


    label("loc_9680")

    OP_2C(0xAA, 0x1)

    ChrTalk(
        0x101,
        "#5P#00000F(There's no mistake. This is definitely the order.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_9705")

    label("loc_96CD")


    ChrTalk(
        0x101,
        "#5P#00003F(...This is the most likely order.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_9705")

    label("loc_9705")

    Jump("loc_93EB")

    label("loc_970A")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Between 3 and 4AM "Barca", between\x01",
            "5 and 6 "Guillaume Factory",\x01",
            "and around 6 "Neinvalli".\x07\x00\x02",
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
            "#5P#00006F──He most likely first went\x01",
            "to Owner Drake to pick up\x01",
            "the trunk he left with him.\x02\x03",
            "#00008FIt's content... Randy's special\x01",
            "weapon from when he was a jaeger.\x02\x03",
            "#00001FIt's most likely a kind of\x01",
            "high-power orbal rifle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203FOrbal rifles are normally\x01",
            "transported disassembled.\x02\x03",
            "#00201FBecause it hasn't been used in\x01",
            "two years, Randy brought it to\x01",
            "the repair factory to be serviced...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103F#11P──Yes, no doubt about it.\x02\x03",
            "#10108FHaving a well-maintained weapon is a\x01",
            "matter of life and death on a battlefield.\x02\x03",
            "#10101FSenior Randy would definitely\x01",
            "have it checked carefully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10303FFinally, he stopped by the\x01",
            "exchange shop to stock up.\x02\x03",
            "#10301FHe bought gunpowder ammo too.\x01",
            "It means he has quite the special rifle, no?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00108FI've heard the Reinford Corporation have\x01",
            "models that can change between orbal\x01",
            "and gunpowder operation but...\x02\x03",
            "#00101FRegardless, it probably has a\x01",
            "number of special improvements.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00006FYeah. The Red Constellation \x01",
            "jaegers too used huge rifles\x01",
            "I had never seen before.\x02\x03",
            "#00013F──Alright, I think we've gotten a\x01",
            "handle on Randy's situation, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00206FIt was past 6AM when Mr. \x01",
            "Randy left the exchange shop...\x02\x03",
            "#00208FIt's around 10AM now, so\x01",
            "around 4 hours have passed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#11PIt seems difficult to\x01",
            "track senior now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00003F...No. Even if it's Randy,\x01",
            "his toughness has a limit.\x02\x03",
            "#00001FAnd if he's going up against the "Red\x01",
            "Constellation", he'd rest before doing so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FOn top of that, he'll use the terrain to\x01",
            "his advantage, attacking suddenly\x01",
            "and finishing it once and for all.\x02\x03",
            "#10302FWell, if he's not planning\x01",
            "on a suicide attack,\x01",
            "that's how he'd do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00101F...In any case we don't\x01",
            "have much time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00013FYeah. Without evidence, we have\x01",
            "no choice but to go towards Mainz──\x02",
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

    def lambda_9F15():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9F15)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_9F3A():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9F3A)
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
        "#6P#00205FIs it from Mr. Randy?\x02",
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
            "#00007F──Special Support Section,\x01",
            "Lloyd Bannings speaking!\x02",
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
            "Hey there, Mr. Lloyd.\x02\x03",
            "...Hu hu, it seems you thought\x01",
            "I was someone else.\x02",
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
            "#00013F...Why do you have this number?\x02",
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
            "Hu hu, I told you before.\x01",
            "I am a huge fan of you guys.\x02\x03",
            "──The Times department store.\x02\x03",
            "If you are free, please\x01",
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
        (
            "#6P#00201F...Mr. Lloyd.\x01",
            "That call...\x02",
        )
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
            "#5P#00003F...Cao from the "Heiyue".\x02\x03",
            "#00013FIt seems he's waiting for us on the roof\x01",
            "of the Central Square department store.\x02",
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
            "#12P#10301FAt a time like this...\x01",
            "What could he be planning?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00006FI don't know. \x01",
            "What I do know is, he wouldn't\x01",
            "contact us without a reason.\x02\x03",
            "#00001FLet's stop by before heading\x01",
            "to the mountain path.\x02",
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

    # Function_46_923B end

    def Function_47_A4FF(): pass

    label("Function_47_A4FF")

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

    def lambda_A5DA():
        OP_95(0x101, 8630, 0, 4260, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A5DA)

    def lambda_A5F4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A5F4)
    Sleep(500)

    def lambda_A608():
        OP_95(0x102, 9430, 0, 3460, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A608)

    def lambda_A622():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A622)
    Sleep(500)

    def lambda_A636():
        OP_95(0x109, 9830, 0, 5460, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A636)

    def lambda_A650():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_A650)
    Sleep(500)

    def lambda_A664():
        OP_95(0x105, 10630, 0, 4460, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A664)

    def lambda_A67E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_A67E)
    Sleep(50)
    WaitChrThread(0x101, 1)

    def lambda_A696():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A696)
    WaitChrThread(0x102, 1)

    def lambda_A6A7():
        OP_93(0x102, 0x168, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A6A7)
    WaitChrThread(0x109, 1)

    def lambda_A6B8():
        OP_93(0x109, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A6B8)
    WaitChrThread(0x105, 1)

    def lambda_A6C9():
        OP_93(0x105, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A6C9)
    SetMapObjFlags(0x3, 0x0)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0x102,
        (
            "#12P#00103FCongressman Geval, eh...?\x02\x03",
            "#00108FAmong the congressmen\x01",
            "who were forced to retire,\x01",
            "he may be still in a good position.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FYes, I think the congressmen\x01",
            "captured in the Cult incident\x01",
            "have it way tougher.\x02\x03",
            "#10103FLooks like we got our\x01",
            "information but I don't exactly\x01",
            "know how we'll report it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FYeah, but in the end, evil deeds\x01",
            "always come back to bite you.\x01",
            "It happens all the time.\x02\x03",
            "#00000FIf he were to work hard to better himself,\x01",
            "he would surely be rewarded someday.\x02\x03",
            "#00004FI hope Mr. Geval and\x01",
            "the other congressmen\x01",
            "choose the right path.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103FYeah...\x01",
            "(And maybe one day, Mr. Ernest too...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHu hu, that's our\x01",
            "leader for you.\x02\x03",
            "#10302FHow about it? Do you want\x01",
            "to go to Trinity for a drink\x01",
            "after that long chat?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006F*sigh*, there's no way we can do\x01",
            "something like that while on duty.\x02\x03",
            "#00000F...Anyway, that wraps up our\x01",
            "investigation of Downtown.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x6A, 0x1, 0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AB78")
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
        (0, "loc_AB4B"),
        (1, "loc_AB5F"),
        (2, "loc_AB73"),
        (SWITCH_DEFAULT, "loc_AB78"),
    )


    label("loc_AB4B")

    ClearScenarioFlags(0x131, 5)
    ClearScenarioFlags(0x131, 6)
    ClearScenarioFlags(0x131, 7)
    ClearScenarioFlags(0x132, 0)
    ClearScenarioFlags(0x132, 1)
    Jump("loc_AB78")

    label("loc_AB5F")

    SetScenarioFlags(0x131, 5)
    SetScenarioFlags(0x131, 6)
    SetScenarioFlags(0x131, 7)
    SetScenarioFlags(0x132, 0)
    SetScenarioFlags(0x132, 1)
    Jump("loc_AB78")

    label("loc_AB73")

    Jump("loc_AB78")

    label("loc_AB78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_ABD5")

    ChrTalk(
        0x101,
        (
            "#6P#00000FAlright, then let's continue\x01",
            "our investigation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AC50")

    label("loc_ABD5")

    OP_29(0x6A, 0x1, 0x6)

    ChrTalk(
        0x101,
        (
            "#6P#00000FAlright, we've finished our investigation.\x02\x03",
            "Let's head back to City Meeting Hall\x01",
            "and make our report.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AC50")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_71(0x3, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x3, 0x10)
    SetScenarioFlags(0x132, 2)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 9630, 0, 4460, 225)
    EventEnd(0x5)
    Return()

    # Function_47_A4FF end

    def Function_48_AC88(): pass

    label("Function_48_AC88")

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
            "#11POh, it's you guys... \x01",
            "What do you want?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PAnd is that...\x01",
            "W-Wazy!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PDamn...!\x01",
            "Get out, asshole!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10308FOh boy... I guess I'm\x01",
            "not welcome here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F...I understand how you feel, but please\x01",
            "just listen to what we have to say.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained the professor's request and that\x01",
            "they were here to collect the medical questionnaire.\x07\x00\x02",
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
            "#11P...Oh, that. They gave it to me\x01",
            "when I was still in treatment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00305FWhat, so you forgot about it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PHmph. I've got no drugs\x01",
            "symptoms anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PEven so, I've gotta go to the\x01",
            "hospital again? How annoying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00101FDino... You're not\x01",
            "thinking straight.\x02\x03",
            "#00103FIn the unlikely case you had\x01",
            "still symptoms, you'll cause\x01",
            "trouble for all the Vipers too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#11PUgh... I guess you're right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P...Ah, fine!\x01",
            "Wait there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PI have it here somewhere,\x01",
            "and I'll fill it out quickly.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B0CC():
        OP_95(0xFE, 44930, -2500, -22750, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_B0CC)
    WaitChrThread(0x8, 1)

    def lambda_B0EA():
        OP_95(0xFE, 47960, -2100, -22440, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_B0EA)
    Sleep(50)

    def lambda_B107():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B107)
    Sleep(50)

    def lambda_B117():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B117)
    Sleep(50)

    def lambda_B127():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B127)
    Sleep(50)

    def lambda_B137():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B137)
    Sleep(50)

    def lambda_B147():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B147)
    WaitChrThread(0x8, 1)
    Sound(116, 0, 100, 0)
    ClearMapObjFlags(0x4, 0x10)
    OP_71(0x4, 0x0, 0x10, 0x0, 0x0)
    OP_79(0x0)
    Sleep(700)

    def lambda_B176():
        OP_97(0xFE, 0x7D0, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_B176)

    def lambda_B190():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_B190)
    WaitChrThread(0x8, 2)
    SetChrFlags(0x8, 0x80)
    OP_0D()

    ChrTalk(
        0x109,
        "#6P#10106F*phew*. Looks like we'll be able to collect it.\x02",
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
        "#11P...Here. This is it, right?\x02",
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
        "#12P#00100FThank you, Dino!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P...Hmph. You've got no\x01",
            "reason to thank me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11PNow take Wazy and\x01",
            "get out of here!\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B49A")

    AnonymousTalk(
        0x101,
        (
            "#00000FNow we have finished to collect\x01",
            "all the medical questionnaires.\x02\x03",
            "Let's go deliver them to\x01",
            "Professor Seiland at once.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_29(0x70, 0x1, 0x5)

    label("loc_B49A")

    OP_93(0x8, 0xE1, 0x0)
    OP_4C(0x8, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 43610, -2500, -21900, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_48_AC88 end

    def Function_49_B4C7(): pass

    label("Function_49_B4C7")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_B541")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x1A2, 0x80)
    Jump("loc_B580")

    label("loc_B541")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_B563")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x1A2, 0x80)
    Jump("loc_B580")

    label("loc_B563")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_B580")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x1A2, 0x80)

    label("loc_B580")

    OP_68(-2990, 1930, -22180, 5000)
    MoveCamera(44, 22, 0, 5000)
    OP_6E(500, 5000)
    SetCameraDistance(49730, 5000)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_B68C")
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x104, 0x80)
    ClearChrFlags(0x1A2, 0x80)
    SetChrPos(0x1A2, 2260, 0, 22750, 180)
    SetChrPos(0x102, 1410, 0, 22750, 180)
    SetChrPos(0x101, 2900, 0, 24450, 180)
    SetChrPos(0x104, 910, 0, 24450, 180)

    def lambda_B61E():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_B61E)

    def lambda_B638():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B638)
    Sleep(100)

    def lambda_B655():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B655)
    Sleep(50)

    def lambda_B672():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B672)
    Jump("loc_B82F")

    label("loc_B68C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_B760")
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x109, 0x80)
    ClearChrFlags(0x1A2, 0x80)
    SetChrPos(0x1A2, 2260, 0, 22750, 180)
    SetChrPos(0x102, 1410, 0, 22750, 180)
    SetChrPos(0x101, 2900, 0, 24450, 180)
    SetChrPos(0x109, 910, 0, 24450, 180)

    def lambda_B6F2():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_B6F2)

    def lambda_B70C():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B70C)
    Sleep(100)

    def lambda_B729():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B729)
    Sleep(50)

    def lambda_B746():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B746)
    Jump("loc_B82F")

    label("loc_B760")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_B82F")
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x105, 0x80)
    ClearChrFlags(0x1A2, 0x80)
    SetChrPos(0x1A2, 2260, 0, 22750, 180)
    SetChrPos(0x102, 1410, 0, 22750, 180)
    SetChrPos(0x101, 2900, 0, 24450, 180)
    SetChrPos(0x105, 910, 0, 24450, 180)

    def lambda_B7C6():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_B7C6)

    def lambda_B7E0():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B7E0)
    Sleep(100)

    def lambda_B7FD():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B7FD)
    Sleep(50)

    def lambda_B81A():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B81A)

    label("loc_B82F")

    OP_6F(0x79)
    OP_68(2000, 1930, 2050, 7000)
    MoveCamera(41, 21, 0, 7000)
    OP_6E(500, 7000)
    SetCameraDistance(17730, 7000)
    OP_6F(0x79)

    ChrTalk(
        0x1A2,
        (
            "This is...\x01",
            "Another quite dreary place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F...It's the Downtown. A place that\x01",
            "was left behind from development.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x1A2)

    ChrTalk(
        0x1A2,
        (
            "Hmph...you can find such\x01",
            "places in every country too.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x1A2,
        "#12PIt's enough, let's go back to East Street.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FY-Yeah...alright.\x02",
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

    # Function_49_B4C7 end

    def Function_50_B9CC(): pass

    label("Function_50_B9CC")

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

    def lambda_BABC():
        OP_95(0xFE, 2450, 0, 8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BABC)
    Sleep(10)

    def lambda_BAD9():
        OP_95(0xFE, 1250, 0, 8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BAD9)
    Sleep(20)

    def lambda_BAF6():
        OP_95(0xFE, 2260, 0, 9650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BAF6)
    Sleep(10)

    def lambda_BB13():
        OP_95(0xFE, 3460, 0, 9650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_BB13)
    Sleep(20)

    def lambda_BB30():
        OP_95(0xFE, 1060, 0, 9650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_BB30)
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
        "#00005FThose voices...\x02",
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
            "#6PSlash, you asshole...\x01",
            "Are you serious!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#6PWhat if Mr. Wald, who's weak to liquor,\x01",
            "ruins his health at that rate? What then, huh!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "That's why I'm thinking\x01",
            "of ideas to prevent that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "And just since nothing comes to mind,\x01",
            "don't get irritated!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#6P"If he sees the view from the top of\x01",
            "the tower, he'll cheer up, won't he?". \x01",
            "Is it that your idea!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#6PIf Mr. Wald cheered up just by\x01",
            "going to a high place, no one\x01",
            "would be having a hard time!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#6P#4SI can't stand idiots\x01",
            "like you, idiot!\x01",
            "You idiot!!\x02",
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
            "#4SY-Youuu...!! You even\x01",
            "said it three times!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#4SYou're a hundred times more of an idiot!\x01",
            "You didn't come up with a single good idea!\x02",
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
        "#5P#N#4S#00007FStop it, you two!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_68(280, 2000, -1490, 3000)
    MoveCamera(36, 20, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(15650, 3000)

    def lambda_C080():
        OP_95(0xFE, 2450, 0, 500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C080)
    Sleep(10)

    def lambda_C09D():
        OP_95(0xFE, 1250, 0, 500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C09D)
    Sleep(20)

    def lambda_C0BA():
        OP_95(0xFE, 2260, 0, 2150, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C0BA)
    Sleep(10)

    def lambda_C0D7():
        OP_95(0xFE, 3460, 0, 2150, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C0D7)
    Sleep(20)

    def lambda_C0F4():
        OP_95(0xFE, 1060, 0, 2150, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C0F4)
    Sleep(200)
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_C138():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_C138)
    Sleep(10)

    def lambda_C148():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_C148)
    WaitChrThread(0x105, 1)
    WaitChrThread(0xD, 1)
    OP_6F(0x79)

    ChrTalk(
        0xE,
        "#12PYou bastards are...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00301FWhoa, you guys have your weapons out, \x01",
            "even though you're comrades.\x01",
            "That's not like you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#12PHmph... None of your\x01",
            "business, assholes!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#12PAnd what started it all was...Wazy!! \x01",
            "It's because of your half-assed\x01",
            "attitude...!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#12PYeah...! \x01",
            "It's your fault Mr. Wald's\x01",
            "became like that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#12PEverything's your fault, Wazy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#5P#10303F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#10105FW-Wait a moment!\x01",
            "Wazy didn't...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#12PAnyway, nothing'll change at this rate...\x01",
            "But first, we'll have to beat you up!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#12PHyaha, right!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#12PHuey, I'm gonna \x01",
            "steamroll you later!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#00101F(W-What do we do, Lloyd...?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#00301F(They've completely lost their cool.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00010F(Ugh. Now that it's come to this,\x01",
            "we'll have to subdue them...)\x02",
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
        (
            "Hmph...\x01",
            "How sad.\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x64, 0x7D0)
    OP_68(-7930, 6500, -5030, 6000)
    MoveCamera(41, 31, 0, 6000)
    OP_6E(500, 6000)
    SetCameraDistance(14890, 6000)
    Sleep(500)

    def lambda_C59E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C59E)
    Sleep(10)

    def lambda_C5AE():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C5AE)
    Sleep(20)

    def lambda_C5BE():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C5BE)
    Sleep(10)

    def lambda_C5CE():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C5CE)
    Sleep(20)

    def lambda_C5DE():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C5DE)
    Sleep(10)

    def lambda_C5EE():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_C5EE)
    Sleep(10)

    def lambda_C5FE():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_C5FE)
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
            "#5P#13904FConflict brings forth nothing...\x01",
            "Only the chains of foolish hatred.\x02\x03",
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
        "#70A#50WBrightly#1500W #50Wshooting stars,#1000W #50Wleaving trails in the skies...\x05\x02",
    )

    Sleep(7000)

    NpcTalk(
        0x18,
        "Blond Young Man",
        "#70A#50WLike a guiding light,#1000W #50Wthey show me the way to your eyes...\x05\x02",
    )

    Sleep(7000)

    NpcTalk(
        0x18,
        "Blond Young Man",
        "#70A#50WThis yearning#1500W #50Wpassion,#1000W #50Wtears my heart in twain...\x05\x02",
    )

    Sleep(7000)

    NpcTalk(
        0x18,
        "Blond Young Man",
        "#70A#50WAnd the cruel moon#1000W #50Wmocks my pain...\x05\x02",
    )

    Sleep(7000)

    NpcTalk(
        0x18,
        "Blond Young Man",
        "#70A#50WIf this fleeting dream#3000W #50Wshall never be...\x05\x02",
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
        "#4S...Hey, shut up, blondie!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Blond Young Man",
        "#12P#13911FUgh...!?\x02",
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
            "#11P#13909FI-Is something wrong,\x01",
            "cute little kitty?\x02\x03",
            "#13902FHmph, I'm in the middle of a performance,\x01",
            "as you can see. Sorry, but you'll need to\x01",
            "ask for my autograph later.\x02\x03",
            "#13910FI should say, if you get kicked out from\x01",
            "a place like this, it would be danger──\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x19,
        "#6PStop blabbering!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#6PQuit banging around on the roof of\x01",
            "our shop and get down from there!\x02",
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
        (
            "#13911FO-Okay,\x01",
            "all right, geez──\x02",
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
        "#12PGEEET DOOOWN!!\x02",
    )

    CloseMessageWindow()

    def lambda_CD71():
        OP_95(0xFE, -17240, 5400, -1780, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_CD71)
    Sleep(800)
    OP_95(0x19, -16880, 5400, -1950, 4000, 0x0)
    Sleep(1000)
    Sound(1013, 0, 100, 0)

    NpcTalk(
        0x18,
        "Youth's Voice",
        "#2SWhoa...!?\x02",
    )

    CloseMessageWindow()
    Sound(833, 0, 40, 0)
    Sound(992, 0, 40, 0)
    Sleep(50)
    Sound(811, 0, 100, 0)

    ChrTalk(
        0x19,
        "#2S...Ah, he fell.\x02",
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
        "#2SUgh... \x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#2S...Oh, so you're.\x02",
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

    def lambda_CF4A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CF4A)
    Sleep(10)

    def lambda_CF5A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CF5A)
    Sleep(20)

    def lambda_CF6A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_CF6A)
    Sleep(10)

    def lambda_CF7A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_CF7A)
    Sleep(20)

    def lambda_CF8A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_CF8A)

    ChrTalk(
        0xD,
        "#12PI'm bored. Later.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#12P#5AHyaha, what was with that blondie...\x02",
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
        "#6P...Don't worry about him. Let's go.\x02",
    )

    CloseMessageWindow()

    def lambda_D047():
        OP_95(0xFE, 6640, 0, -7350, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_D047)
    Sleep(800)

    def lambda_D064():
        OP_95(0xFE, 7700, 0, -7010, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_D064)

    def lambda_D07E():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D07E)
    Sleep(50)

    def lambda_D08E():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D08E)
    Sleep(50)

    def lambda_D09E():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D09E)
    Sleep(50)

    def lambda_D0AE():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D0AE)
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
            "#5P#10306F...Hmm. I guess he\x01",
            "helped us, in a way.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x18, -3400, 0, -6690, 0)

    NpcTalk(
        0x18,
        "Youth's Voice",
        (
            "H-Hmph... In the Demon City,\x01",
            "I was merely nipping a\x01",
            "blossoming quarrel in the bud.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D19F():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D19F)
    Sleep(50)

    def lambda_D1AF():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D1AF)
    Sleep(50)

    def lambda_D1BF():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D1BF)
    Sleep(50)

    def lambda_D1CF():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D1CF)
    Sleep(50)

    def lambda_D1DF():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D1DF)

    NpcTalk(
        0x18,
        "Youth's Voice",
        (
            "With love and devotion, the melody\x01",
            "of my lute brings true peace.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Youth's Voice",
        (
            "My own genius scares\x01",
            "me sometimes.\x02",
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

    def lambda_D2E7():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_D2E7)
    OP_96(0x18, 0xFFFFFD4E, 0x0, 0xFFFFECB4, 0x3E8, 0x0)

    def lambda_D308():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_D308)
    OP_96(0x18, 0xFFFFFC68, 0x0, 0xFFFFF330, 0x7D0, 0x0)

    def lambda_D329():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_D329)
    OP_96(0x18, 0x320, 0x0, 0xFFFFF416, 0x5DC, 0x0)

    def lambda_D34A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_D34A)
    OP_96(0x18, 0x654, 0x0, 0xFFFFFA10, 0x3E8, 0x0)

    def lambda_D36B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D36B)
    Sleep(50)

    def lambda_D37B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D37B)
    Sleep(50)

    def lambda_D38B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D38B)
    Sleep(50)

    def lambda_D39B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D39B)
    Sleep(50)

    def lambda_D3AB():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D3AB)
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
            "#6P#00105FU-Umm... Are you\x01",
            "all right? I heard a\x01",
            "thick sound earlier.\x02",
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
            "#11P#13903FI ended up suffering a\x01",
            "little trouble now, but...\x02\x03",
            "#13900FI've pulled myself together.\x01",
            "So, allow me to continue my performance.\x02\x03",
            "#13904FHmph, please enjoy, everyone.\x02",
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
        "#6P#00011FT-That's plenty!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106F(M-Mr. Lloyd. \x01",
            "Could this person be...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001F(Yeah, blonde with a white coat...)\x02\x03",
            "#00006F(Mr. Mueller said he was a troublesome\x01",
            "character, but... He's honestly worse \x01",
            "than I was expecting.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001F...*ahem*.\x01",
            "You are Mr. Olivier,\x01",
            "am I correct?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x18,
        "Blond Young Man",
        "#11P#13904FHmph... The very same.\x02",
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
            "The unparallaled genius wandering\x01",
            "musician and seeker of love,\x01",
            "Olivier Lenheim.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0x18,
        (
            "You all are lucky to have\x01",
            "heard one of my famous\x01",
            "guerilla recitals.\x02\x03",
            "Carve this day into your hearts.\x01",
            "It may be a once-in-a-lifetime\x01",
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
        "#6P#00006F...R-Right.\x02",
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
            "#11P#13905FAh, come to think of it...\x01",
            "Why do you know my name?\x02\x03",
            "#13902FI don't remember giving out my\x01",
            "name ever since I entered\x01",
            "Crossbell. Have we met before?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FWe're from the Crossbell Police,\x01",
            "Special Support Section.\x02\x03",
            "We're looking for you because of\x01",
            "a certain Mr. Mueller's request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FYou must know\x01",
            "him, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11P#13905FOooh, so you're the rumored...\x02\x03",
            "#13904FHmph... That Mueller's as\x01",
            "much of a worrywart as ever.\x02\x03",
            "#13912FOur love for each other\x01",
            "will not fade with only\x01",
            "this much time apart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10105FHuh!? S-So that's the kind of\x01",
            "relationship you guys have...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00306F...No, no, I doubt it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FA-Anyway... Can we\x01",
            "ask you to return\x01",
            "to Mr. Mueller?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11P#13903F...I am sorry, but I cannot\x01",
            "comply with your request.\x02\x03",
            "#13900FAfter all, I am going to be quite busy tomorrow.\x01",
            "I must enjoy Crossbell now, while I have the chance.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00105FBusy...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#11P#13904FHmph, that's how it is.\x02\x03",
            "However, if you\x01",
            "say you cannot\x01",
            "overlook this...\x02\x03",
            "#13902FI will do whatever I have to,\x01",
            "to make you overlook it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FEh? What are\x01",
            "you planning?\x02",
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
            "Julia over there!?\x02",
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

    def lambda_DF3F():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DF3F)
    Sleep(10)

    def lambda_DF4F():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DF4F)
    Sleep(20)

    def lambda_DF5F():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_DF5F)
    Sleep(10)

    def lambda_DF6F():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_DF6F)
    Sleep(20)

    def lambda_DF7F():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_DF7F)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00011FWhat...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00105FEeh...!?\x02",
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
            "#10105FHey, t-there's...\x01",
            "No one there, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F...Ah!\x02",
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

    def lambda_E11D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E11D)
    Sleep(10)

    def lambda_E12D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E12D)
    Sleep(20)

    def lambda_E13D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_E13D)
    Sleep(10)

    def lambda_E14D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_E14D)
    Sleep(20)

    def lambda_E15D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_E15D)
    Sleep(500)

    ChrTalk(
        0x18,
        (
            "#5P#13902FHmph, I'm looking forward\x01",
            "to our next meeting!\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_63(0x18, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_93(0x18, 0x0, 0x1F4)

    def lambda_E1C9():
        OP_95(0xFE, 1900, 0, 20650, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_E1C9)
    Sleep(500)

    ChrTalk(
        0x101,
        "#12P#00011FW-Wait...!\x02",
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
            "#5P#00306FMan. A troublesome guy, but in\x01",
            "a different way than Lechter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FA-Anyway, let's try\x01",
            "chasing after him.\x02\x03",
            "#00003FBut, where\x01",
            "did he go...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10303FWe should probably\x01",
            "check the places we\x01",
            "discussed earlier.\x02\x03",
            "#10300FWe found him in Downtown,\x01",
            "so let's try the others. Maybe\x01",
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

    # Function_50_B9CC end

    def Function_51_E501(): pass

    label("Function_51_E501")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E550")
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
    Jump("Function_51_E501")

    label("loc_E550")

    Return()

    # Function_51_E501 end

    def Function_52_E551(): pass

    label("Function_52_E551")

    Sleep(23000)
    OP_95(0xFE, -12870, 5400, -2670, 1000, 0x0)
    OP_93(0xFE, 0x5A, 0x0)
    Sleep(4000)
    OP_9D(0xFE, 0xFFFFD4AE, 0x1900, 0xFFFFF466, 0x4B0, 0xBB8)
    Sound(50, 0, 100, 0)
    Return()

    # Function_52_E551 end

    def Function_53_E590(): pass

    label("Function_53_E590")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Apartment "Maison Imelda"\x01\x01",
            "　    ～Unmanaged～\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x321, 0x0)"), scpexpr(EXPR_END)), "loc_E685")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E680")
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

    label("loc_E680")

    Jump("loc_E84B")

    label("loc_E685")

    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E7B3")

    ChrTalk(
        0x101,
        "#00000FLooks like it's locked.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FThere's a monster extermination\x01",
            "support request for this apartment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI think the manager is "Mrs.\x01",
            "Imelda", the shopkeeper at\x01",
            "that antique shop.\x02\x03",
            "#00000FLet's go to the antique\x01",
            "shop on Back Street\x01",
            "and borrow the key.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_E84B")

    label("loc_E7B3")


    ChrTalk(
        0x101,
        (
            "#00000FA monster extermination\x01",
            "support request for\x01",
            "this apartment came in.\x02\x03",
            "#00000FLet's go to the antique\x01",
            "shop on Back Street\x01",
            "and borrow the key.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E84B")

    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_53_E590 end

    SaveToFile()

Try(main)
