from ScenarioHelper import *

def main():
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
        "Ryu",                 # 1
        "Henry",                 # 2
        "Ponce",                 # 3
        "Brick",               # 4
        "peach",                   # 5
        "Elsa",                 # 6
        "Louvic's old man",       # 7
        "Katerina",             # 8
        "Chiluru",                 # 9
        "Mrs Olga",             # 10
        "Citizen",                   # 11
        "A security guard",               # 12
        "Sergey Manager",           # 13
        "lease",                 # 14
        "Zeit",               # 15
        "Keya",                 # 16
        "White falcon",             # 17
        "Special Affairs Support Division Conducted Car",       # 18
        "SE control",                 # 19
        "bc0200",                 # 20
        "Central square",               # 21
        "Nishi dori",                 # 22
        "Administrative district",                 # 23
        "Residential area",                 # 24
        "Entertainment district",                 # 25
        "East Street",                 # 26
        "old Town",                 # 27
        "Harbor district",                 # 28
        "IBC",                 # 29
        "Beside the station",               # 30
        "Back street",                 # 31
        "Ursula interchange",           # 32
        "East Crossbell Highway",       # 33
        "West Crossbell Highway",       # 34
        "Mainz Mountain Road",           # 35
        "Orchis Tower",         # 36
    ))

    ATBonus("ATBonus_6D4", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)

    Sepith("Sepith_B5FC", 8,   8,   8,   8,   11,  11,  11)

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
        "BattleInfo_7A4", 0x0000, 93, 6, 60, 4, 1, 25, 0, "bc0200", "Sepith_B5FC", 60, 25, 10, 0,
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

    PlaceName(70.75, 0.0, -7.0, 0x0000, 0x0000, "Central square")
    PlaceName(5.0, 0.0, -2.5, 0x0000, 0x0000, "Nishi dori")
    PlaceName(97.75, 0.0, 82.0, 0x0000, 0x0000, "Administrative district")
    PlaceName(-56.0, 0.0, 72.0, 0x0000, 0x0000, "Residential area")
    PlaceName(17.0, 0.0, 64.0, 0x0000, 0x0000, "Entertainment district")
    PlaceName(152.0, 0.0, -30.0, 0x0000, 0x0000, "East Street")
    PlaceName(187.5, 0.0, -85.0, 0x0000, 0x0000, "old Town")
    PlaceName(180.0, 0.0, 36.0, 0x0000, 0x0000, "Harbor district")
    PlaceName(154.0, 0.0, 130.0, 0x0000, 0x0000, "IBC")
    PlaceName(82.0, 0.0, -76.0, 0x0000, 0x0000, "Beside the station")
    PlaceName(35.0, 0.0, 28.0, 0x0000, 0x0000, "Back street")
    PlaceName(79.0, 0.0, -107.0, 0x0000, 0x0000, "Ursula interchange")
    PlaceName(206.0, 0.0, -16.0, 0x0000, 0x0000, "East Crossbell Highway")
    PlaceName(-46.0, 0.0, -4.0, 0x0000, 0x0000, "West Crossbell Highway")
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
        "Function_15_2A49",        # 0F, 15
        "Function_16_2B08",        # 10, 16
        "Function_17_2BF6",        # 11, 17
        "Function_18_2D43",        # 12, 18
        "Function_19_3476",        # 13, 19
        "Function_20_4387",        # 14, 20
        "Function_21_4CB8",        # 15, 21
        "Function_22_4FBC",        # 16, 22
        "Function_23_5595",        # 17, 23
        "Function_24_5C47",        # 18, 24
        "Function_25_5C98",        # 19, 25
        "Function_26_5CE0",        # 1A, 26
        "Function_27_5D60",        # 1B, 27
        "Function_28_5E68",        # 1C, 28
        "Function_29_5FFB",        # 1D, 29
        "Function_30_607E",        # 1E, 30
        "Function_31_60D6",        # 1F, 31
        "Function_32_6477",        # 20, 32
        "Function_33_6A81",        # 21, 33
        "Function_34_6B42",        # 22, 34
        "Function_35_6BD6",        # 23, 35
        "Function_36_6C81",        # 24, 36
        "Function_37_71F8",        # 25, 37
        "Function_38_88C5",        # 26, 38
        "Function_39_891C",        # 27, 39
        "Function_40_89B1",        # 28, 40
        "Function_41_8A4A",        # 29, 41
        "Function_42_8A7E",        # 2A, 42
        "Function_43_8AB2",        # 2B, 43
        "Function_44_8AE6",        # 2C, 44
        "Function_45_8B1A",        # 2D, 45
        "Function_46_8B2A",        # 2E, 46
        "Function_47_A6AE",        # 2F, 47
        "Function_48_A6DE",        # 30, 48
        "Function_49_A71D",        # 31, 49
        "Function_50_AB99",        # 32, 50
        "Function_51_B252",        # 33, 51
        "Function_52_B513",        # 34, 52
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21E6")
    Sound(14, 0, 100, 0)
    OP_74(0xD, 0x1E)
    OP_71(0xD, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('ＺＷＥＩ２企鹅', 1)"), scpexpr(EXPR_END)), "loc_216F")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 'ＺＷＥＩ２企鹅'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EB, 7)
    OP_E0(0x5, 0x0)
    Jump("loc_21E1")

    label("loc_216F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            "In the treasure box",
            scpstr(SCPSTR_CODE_ITEM, 'ＺＷＥＩ２企鹅'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Is contained.\x01",
            "Because my belongings are full,",
            scpstr(SCPSTR_CODE_ITEM, 'ＺＷＥＩ２企鹅'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I gave up.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xD, 0x1E, 0x0, 0x0, 0x0)

    label("loc_21E1")

    Jump("loc_222B")

    label("loc_21E6")

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

    label("loc_222B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_13_20E6 end

    def Function_14_2237(): pass

    label("Function_14_2237")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_22A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2255")
    Call(0, 17)
    Jump("loc_229E")

    label("loc_2255")


    ChrTalk(
        0xFE,
        "Oh, older brothers!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "About Crosbell City\x01",
            "Leave it to us!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_229E")

    Jump("loc_2A45")

    label("loc_22A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_22B1")
    Jump("loc_2A45")

    label("loc_22B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_23B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2361")

    ChrTalk(
        0xFE,
        (
            "Everyone, how about the empire and the republic\x01",
            "She seems seriously suffering ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How about Dokitsu?\x01",
            "I do not understand well, but ….\x01",
            "Was not it a pleasant thing?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_23B2")

    label("loc_2361")


    ChrTalk(
        0xFE,
        (
            "Doctorate,\x01",
            "Was not it a pleasant thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I do not understand well …\x02",
    )

    CloseMessageWindow()

    label("loc_23B2")

    Jump("loc_2A45")

    label("loc_23B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2437")

    ChrTalk(
        0xFE,
        (
            "peachを遊びに誘ったんだけど、\x01",
            "I can not handle my aunt\x01",
            "I told you that ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Haa, I will somehow crash.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A45")

    label("loc_2437")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2465")

    ChrTalk(
        0xFE,
        "Well, wait a second!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A45")

    label("loc_2465")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2505")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24CB")

    ChrTalk(
        0xFE,
        "peachのやつ、おせーなー。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "About us\x01",
            "I wish I could finish it early.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2500")

    label("loc_24CB")


    ChrTalk(
        0xFE,
        (
            "peachのやつ、About us\x01",
            "Please end it soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2500")

    Jump("loc_2A45")

    label("loc_2505")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_25E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2580")

    ChrTalk(
        0xFE,
        (
            "peachのやつ、ほんと探すの\x01",
            "It is a warmth ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Faa……\x01",
            "I got sick of somehow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_25E2")

    label("loc_2580")


    ChrTalk(
        0xFE,
        (
            "Standing still\x01",
            "I got bored.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Found quickly,\x01",
            "I'd like to play another game.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25E2")

    Jump("loc_2A45")

    label("loc_25E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_27A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_273E")
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x8, 0x0, 500)

    ChrTalk(
        0xFE,
        (
            "Oops ……\x01",
            "What are you, Onii?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, I was surprised.\x01",
            "peachに見つかったかと\x01",
            "You thought that ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FWell …\x01",
            "Arbitrarily in such a place\x01",
            "Do not get in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To the other, thing is stingy\x01",
            "You have nothing to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am hiding here\x01",
            "Please be sorry!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    OP_93(0xFE, 0xE1, 0x0)
    ClearChrFlags(0x8, 0x10)
    Jump("loc_279C")

    label("loc_273E")


    ChrTalk(
        0xFE,
        (
            "今、Henryたちと\x01",
            "I'm playing hide and fuck.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am hiding here\x01",
            "Please be sorry!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_279C")

    Jump("loc_2A45")

    label("loc_27A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_281C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27BC")
    Call(0, 15)
    Jump("loc_2817")

    label("loc_27BC")


    ChrTalk(
        0xFE,
        (
            "そういや、Keyaのやつ\x01",
            "I did not feel well recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Will you invite me again next time?\x02",
    )

    CloseMessageWindow()

    label("loc_2817")

    Jump("loc_2A45")

    label("loc_281C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_282A")
    Jump("loc_2A45")

    label("loc_282A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_2989")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_292B")

    ChrTalk(
        0xFE,
        (
            "明日は、Orchis Towerで\x01",
            "Two Shawaiigi\x01",
            "There seems to be it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I do not understand it somewhat,\x01",
            "せっかくだからHenryたちと\x01",
            "I'm going to see the sights.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To, surely fun\x01",
            "It's a party or something.\x01",
            "I'm looking forward to tomorrow ~ ♪\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2984")

    label("loc_292B")


    ChrTalk(
        0xFE,
        (
            "What is Two Shawaiigi?\x01",
            "Perhaps it's a party or something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hey, look forward to tomorrow ~.\x02",
    )

    CloseMessageWindow()

    label("loc_2984")

    Jump("loc_2A45")

    label("loc_2989")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2997")
    Jump("loc_2A45")

    label("loc_2997")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2A2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29B2")
    Call(0, 16)
    Jump("loc_2A29")

    label("loc_29B2")


    ChrTalk(
        0xFE,
        (
            "そういえば、Keyaは今日\x01",
            "Being friends with Shizuku\x01",
            "Are you playing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's no problem\x01",
            "I will invite you together.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A29")

    Jump("loc_2A45")

    label("loc_2A2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2A3C")
    Jump("loc_2A45")

    label("loc_2A3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2A45")

    label("loc_2A45")

    TalkEnd(0xFE)
    Return()

    # Function_14_2237 end

    def Function_15_2A49(): pass

    label("Function_15_2A49")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0x8,
        (
            "今日はpeachのやつ、\x01",
            "I'm helping the shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "ちぇ、Henryと２人じゃ\x01",
            "I do not mind playing Haba ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Ryuってば……\x01",
            "That's truly to me\x01",
            "Is not it rude?\x02",
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

    # Function_15_2A49 end

    def Function_16_2B08(): pass

    label("Function_16_2B08")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0x8,
        (
            "Well then, tomorrow is everyone\x01",
            "Orchis Towerってやつを\x01",
            "Let's go see it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Yeah, that sounds good.\x01",
            "Let's go with everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "モ、peachもいくっ……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ok,\x01",
            "Well then in the morning\x01",
            "Collectively in front of department stores!\x02",
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

    # Function_16_2B08 end

    def Function_17_2BF6(): pass

    label("Function_17_2BF6")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0x8,
        (
            "Well then, everyone\x01",
            "I will start patrolling the streets!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "準備はいいか、Henry、peach！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "はいっ、Ryu隊長！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Iko!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ok, why do not you go!\x01",
            "Crossbell juvenile office assistance section, exercise!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F(Hello, boys assistance department …).\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109FI am getting happy.\x02",
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

    # Function_17_2BF6 end

    def Function_18_2D43(): pass

    label("Function_18_2D43")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2DF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D61")
    Call(0, 17)
    Jump("loc_2DEC")

    label("loc_2D61")


    ChrTalk(
        0xFE,
        (
            "Juvenile office assistance section ……\x01",
            "Ryuもたまにはいいアイデアを\x01",
            "You can think of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I will do it firmly\x01",
            "I would like to help everyone in the city.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DEC")

    Jump("loc_3472")

    label("loc_2DF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2DFF")
    Jump("loc_3472")

    label("loc_2DFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2F61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2ECB")

    ChrTalk(
        0xFE,
        (
            "My father and mother, too,\x01",
            "I came back from abroad yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Personally I am happy,\x01",
            "Everyone seems complicated somewhere … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ha, after all independence\x01",
            "Is it a serious thing?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2F5C")

    label("loc_2ECB")


    ChrTalk(
        0xFE,
        (
            "Dad and mom came home\x01",
            "Personally I am happy,\x01",
            "Everyone seems complicated somewhere … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ha, after all independence\x01",
            "Is it a serious thing?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F5C")

    Jump("loc_3472")

    label("loc_2F61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2FE0")

    ChrTalk(
        0xFE,
        (
            "peachのお母さんも、\x01",
            "I think that I am worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It can not be helped …\x01",
            "There are things like raids\x01",
            "Because it was.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3472")

    label("loc_2FE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3065")

    ChrTalk(
        0xFE,
        (
            "ちょ、ちょっと、Ryu！？\x01",
            "What to do still yet\x01",
            "You have not decided!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because I'm tired of all this\x01",
            "Stop it ~!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3472")

    label("loc_3065")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3178")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3107")

    ChrTalk(
        0xFE,
        (
            "今朝いきなりRyuに誘われて、\x01",
            "To go to the square in front of the tower\x01",
            "I became it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ryuったら、わざわざこんな\x01",
            "Even if it is not on a rainy day ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3173")

    label("loc_3107")


    ChrTalk(
        0xFE,
        (
            "Well, it will not work.\x01",
            "I invited you suddenly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Until your use is over\x01",
            "Let's wait slowly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3173")

    Jump("loc_3472")

    label("loc_3178")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3281")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_321D")

    ChrTalk(
        0xFE,
        "Well, I found it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "そういえばRyuは、\x01",
            "Where is it hidden ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To a funny place\x01",
            "I do not have to enter.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_327C")

    label("loc_321D")


    ChrTalk(
        0xFE,
        (
            "By the way, from a little while ago\x01",
            "It seems that ambulances often pass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Was it also an accident …?\x02",
    )

    CloseMessageWindow()

    label("loc_327C")

    Jump("loc_3472")

    label("loc_3281")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3305")

    ChrTalk(
        0xFE,
        (
            "When I played hide-and-seek,\x01",
            "It took till evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "peach、ちゃんと\x01",
            "I wonder if we can find us …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3472")

    label("loc_3305")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3396")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3320")
    Call(0, 15)
    Jump("loc_3391")

    label("loc_3320")


    ChrTalk(
        0xFE,
        (
            "peachがいたほうが、\x01",
            "The possible play will also spread\x01",
            "It's fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, if you have some help\x01",
            "It can not be helped.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3391")

    Jump("loc_3472")

    label("loc_3396")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_33A4")
    Jump("loc_3472")

    label("loc_33A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_33B2")
    Jump("loc_3472")

    label("loc_33B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_33C0")
    Jump("loc_3472")

    label("loc_33C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_345B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33DB")
    Call(0, 16)
    Jump("loc_3456")

    label("loc_33DB")


    ChrTalk(
        0xFE,
        (
            "噂じゃ、Orchis Towerは\x01",
            "As high as 250 age\x01",
            "It seems to be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What kind of building is this …?\x01",
            "I look forward to.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3456")

    Jump("loc_3472")

    label("loc_345B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3469")
    Jump("loc_3472")

    label("loc_3469")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3472")

    label("loc_3472")

    TalkEnd(0xFE)
    Return()

    # Function_18_2D43 end

    def Function_19_3476(): pass

    label("Function_19_3476")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3531")

    ChrTalk(
        0xFE,
        (
            "Such a big,\x01",
            "Moreover, a big tree that shines pale ……\x01",
            "What kind of thing appeared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I do not know what will happen in the future,\x01",
            "Take a firm record\x01",
            "I have to tell it to future generations.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4383")

    label("loc_3531")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_353F")
    Jump("loc_4383")

    label("loc_353F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_35D8")

    ChrTalk(
        0xFE,
        (
            "President Dieter's words ……\x01",
            "It resonated strongly in the hearts of our residents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To turn the two big powers into enemies\x01",
            "Even if it becomes …\x01",
            "I want to support him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4383")

    label("loc_35D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3734")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36B9")

    ChrTalk(
        0xFE,
        (
            "People who do reconstruction activities,\x01",
            "破壊されたIBCなどの建物を\x01",
            "I put it in the picture.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Never again such a terrible affair\x01",
            "Do not let him wake up …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In order not to forget it\x01",
            "I have to take a proper record.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_372F")

    label("loc_36B9")


    ChrTalk(
        0xFE,
        (
            "Never again such a terrible affair\x01",
            "Do not let him wake up …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In order not to forget it\x01",
            "I have to take a proper record.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_372F")

    Jump("loc_4383")

    label("loc_3734")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3883")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3805")

    ChrTalk(
        0xFE,
        (
            "Last night from the night, the guard armored car\x01",
            "For many in Mainz direction\x01",
            "They seem to be headed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is reinforcing\x01",
            "That's what it is ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Armed group is\x01",
            "Is that a tough opponent to that …?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_387E")

    label("loc_3805")


    ChrTalk(
        0xFE,
        (
            "Reinforcement of the guard,\x01",
            "For many in Mainz direction\x01",
            "They seem to be headed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Armed group is\x01",
            "Is that a tough opponent to that …?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_387E")

    Jump("loc_4383")

    label("loc_3883")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3907")

    ChrTalk(
        0xFE,
        (
            "I do not really know ….\x01",
            "Yesterday's train accident is incomprehensible\x01",
            "It is a story about the work of a chemistry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmm, I'm worried if it will not show up again.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4383")

    label("loc_3907")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_395F")

    ChrTalk(
        0xFE,
        (
            "HM……\x01",
            "I am not good at ambulance sirens.\x01",
            "I wonder if it makes me feel uneasy …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4383")

    label("loc_395F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3AFC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A7A")

    ChrTalk(
        0xFE,
        (
            "Crossbell Newsletter Published\x01",
            "\"Cross Bell Hundred Sceneries\"\x01",
            "I have sightseeing guides.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Many places with good landscape\x01",
            "It has been posted and taken for photography\x01",
            "It is of great help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, a wonderful spot\x01",
            "Please turn around.\x01",
            "Where should I shoot next ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3AF7")

    label("loc_3A7A")


    ChrTalk(
        0xFE,
        (
            "Where are the pictures today\x01",
            "I should go shooting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "\"Cross Bell Hundred Sceneries\"\x01",
            "The spot that was posted\x01",
            "I wish I had turned around.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AF7")

    Jump("loc_4383")

    label("loc_3AFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3C73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BE1")

    ChrTalk(
        0xFE,
        (
            "この間、Ursula interchangeの中洲へ\x01",
            "I went to take a picture.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Then in the back of Nakazu\x01",
            "You are making an unfamiliar road.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because it seemed to be somewhat dangerous\x01",
            "I did not enter, but ….\x01",
            "I wonder what was that?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3C6E")

    label("loc_3BE1")


    ChrTalk(
        0xFE,
        (
            "Ursula interchangeの中州の奥に\x01",
            "You are making an unfamiliar road.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because it seemed to be somewhat dangerous\x01",
            "I did not enter, but ….\x01",
            "I wonder what was that?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C6E")

    Jump("loc_4383")

    label("loc_3C73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3DC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D42")

    ChrTalk(
        0xFE,
        (
            "今日はOrchis Tower周辺が\x01",
            "Not for non-participants\x01",
            "You seem to be getting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think that it is not safe from the point of view,\x01",
            "It's a bit disappointing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Following yesterday,\x01",
            "I wanted to take pictures nearby.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3DBE")

    label("loc_3D42")


    ChrTalk(
        0xFE,
        (
            "Orchis Tower周辺が\x01",
            "Not for non-participants\x01",
            "You seem to be getting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, today.\x01",
            "From the rooftop of department store\x01",
            "Let's take a picture.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DBE")

    Jump("loc_4383")

    label("loc_3DC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_3ECF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E80")

    ChrTalk(
        0xFE,
        (
            "Oops ……\x01",
            "Photosensitive quartz\x01",
            "You have run out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At the unveiling ceremony in the daytime\x01",
            "It seems like I took too many photos.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Before the oval store closes\x01",
            "I have to go buy a new one.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3ECA")

    label("loc_3E80")


    ChrTalk(
        0xFE,
        (
            "Before the oval store closes\x01",
            "New sensitive quartz\x01",
            "I have to go buy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3ECA")

    Jump("loc_4383")

    label("loc_3ECF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4017")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FA6")

    ChrTalk(
        0xFE,
        (
            "Since the unveiling ceremony has ended,\x01",
            "Orchis Towerの写真を\x01",
            "I went shooting a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, even so\x01",
            "It was a really big building.\x01",
            "Was it the 40th floor above the ground …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, I'm looking forward to developing it.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4012")

    label("loc_3FA6")


    ChrTalk(
        0xFE,
        (
            "Orchis Towerの写真を\x01",
            "I got a lot of footage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That building is crossbelled\x01",
            "It is likely to be a new symbol.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4012")

    Jump("loc_4383")

    label("loc_4017")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4136")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40CB")

    ChrTalk(
        0xFE,
        "The trade meeting came close.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A great person from each country will come,\x01",
            "I will show off the new city hall building\x01",
            "There is also an unveiling ceremony ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Shutter opportunity\x01",
            "I have to make sure not to miss it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4131")

    label("loc_40CB")


    ChrTalk(
        0xFE,
        "VIP's visit to each country, unveiling ceremony …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At the trade meeting\x01",
            "Shutter opportunity\x01",
            "I have to make sure not to miss it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4131")

    Jump("loc_4383")

    label("loc_4136")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_41E7")

    ChrTalk(
        0xFE,
        (
            "Hmm, it is also the scenery of rain\x01",
            "It is good to have a different taste than usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Camera shooting at rainy weather\x01",
            "I am asked for a technique … …\x01",
            "This is fun again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4383")

    label("loc_41E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4383")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42D7")

    ChrTalk(
        0xFE,
        (
            "West Crossbell Highwayには\x01",
            "\"Knox forest area\"\x01",
            "I have a place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lots of trees grow thick,\x01",
            "It looks good to take pictures\x01",
            "It's a location though ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because it is the site of police school\x01",
            "An ordinary person can not enter.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4383")

    label("loc_42D7")


    ChrTalk(
        0xFE,
        (
            "I am interested in photography.\x01",
            "Looking for a nice subject\x01",
            "I am going out to various places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "\"Knox Forest Zone\"\x01",
            "The general public can not enter,\x01",
            "Someday I want to go shooting.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4383")

    TalkEnd(0xFE)
    Return()

    # Function_19_3476 end

    def Function_20_4387(): pass

    label("Function_20_4387")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_44CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_445B")

    ChrTalk(
        0xFE,
        (
            "After a long time in \"Morges\"\x01",
            "I came for a cup of coffee.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What I should say …\x01",
            "From now on the cross bell gradually\x01",
            "I hope to regain everyday life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Truly\x01",
            "I am worried about the huge tree.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_44C9")

    label("loc_445B")


    ChrTalk(
        0xFE,
        (
            "From now on the cross bell gradually\x01",
            "I hope to regain everyday life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Truly\x01",
            "I am worried about the huge tree.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44C9")

    Jump("loc_4CB4")

    label("loc_44CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_44DC")
    Jump("loc_4CB4")

    label("loc_44DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_45DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45AB")

    ChrTalk(
        0xFE,
        (
            "Recent Crossbell Times'\x01",
            "I was also surprised at the article ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As expected\x01",
            "To make a speech that enlarged two major powers\x01",
            "I did not think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The situation of the crossbell in the future\x01",
            "I am worried ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_45DA")

    label("loc_45AB")


    ChrTalk(
        0xFE,
        (
            "The situation of the crossbell in the future\x01",
            "I am worried ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45DA")

    Jump("loc_4CB4")

    label("loc_45DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4662")

    ChrTalk(
        0xFE,
        (
            "This neighborhood\x01",
            "It was hardly damaged\x01",
            "It is fortunate to be unhappy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Administrative districtやHarbor districtは、\x01",
            "Especially it was a terrible thing … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CB4")

    label("loc_4662")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_46AD")

    ChrTalk(
        0xFE,
        (
            "Occupation by an armed group … …\x01",
            "マインツの人たちがI am worried ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CB4")

    label("loc_46AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_46BB")
    Jump("loc_4CB4")

    label("loc_46BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_46F6")

    ChrTalk(
        0xFE,
        (
            "For quite a while today\x01",
            "Do not see an ambulance …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CB4")

    label("loc_46F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4768")

    ChrTalk(
        0xFE,
        (
            "Hide and seek\x01",
            "I used to do well a long time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When you see children playing\x01",
            "It feels smart.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CB4")

    label("loc_4768")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_48B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4844")

    ChrTalk(
        0xFE,
        (
            "Mayor's advice\x01",
            "Cross Bell Independence Come and … …\x01",
            "It's a difficult problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Also in Pruna and Linalary\x01",
            "Maybe I should ask your opinion ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… I quit after all.\x01",
            "Those two, deeply\x01",
            "I do not think he's thinking ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_48B0")

    label("loc_4844")


    ChrTalk(
        0xFE,
        (
            "Cross Bell Independence Come and … …\x01",
            "It's a difficult problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Read the Crossbell Times\x01",
            "I wonder if I can think about it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48B0")

    Jump("loc_4CB4")

    label("loc_48B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4973")

    ChrTalk(
        0xFE,
        (
            "Today \"Imperial Times\" and\x01",
            "Remiferia's \"Ardent Press\" also\x01",
            "It seems to go to the meeting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If anything, write the article\x01",
            "With the Crossbell Times\x01",
            "I would like to compare various readings.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CB4")

    label("loc_4973")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_4A0A")

    ChrTalk(
        0xFE,
        (
            "If you read books in a cafe\x01",
            "It has become such a time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Buru ……\x01",
            "It will be cold at night as well.\x01",
            "I wonder if I will return home before catching a cold.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CB4")

    label("loc_4A0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4ABE")

    ChrTalk(
        0xFE,
        (
            "Remilia's Albert Duke\x01",
            "I have invested in Ursula Medical University\x01",
            "It seems to be one of the sponsors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "McDaele, in particular,\x01",
            "From ancient times it was friendly and amiable\x01",
            "I have a relationship.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CB4")

    label("loc_4ABE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4C4A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BB6")

    ChrTalk(
        0xFE,
        (
            "Western Zemria Trade Council ……\x01",
            "Recently, often at the Crossbell Times\x01",
            "It is treated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Discuss the economic talks\x01",
            "That is to say,\x01",
            "What kind of things will be on the agenda?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, next time to Dr. Marble\x01",
            "Let's ask questions in detail.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4C45")

    label("loc_4BB6")


    ChrTalk(
        0xFE,
        (
            "Western Zemria Trade Council ……\x01",
            "I say economic relations in a bite\x01",
            "I wonder what kind of things we will discuss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, next time to Dr. Marble\x01",
            "Let's ask questions in detail.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C45")

    Jump("loc_4CB4")

    label("loc_4C4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4C58")
    Jump("loc_4CB4")

    label("loc_4C58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4CB4")

    ChrTalk(
        0xFE,
        (
            "Today in the evening\x01",
            "It was a Sunday school class.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Do not forget to bring with your homework.\x02",
    )

    CloseMessageWindow()

    label("loc_4CB4")

    TalkEnd(0xFE)
    Return()

    # Function_20_4387 end

    def Function_21_4CB8(): pass

    label("Function_21_4CB8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4D22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CD6")
    Call(0, 17)
    Jump("loc_4D1D")

    label("loc_4CD6")


    ChrTalk(
        0xFE,
        (
            "Ryuくんたちといっしょに、\x01",
            "I will help everyone in the embarrassing city … …!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D1D")

    Jump("loc_4FB8")

    label("loc_4D22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4D30")
    Jump("loc_4FB8")

    label("loc_4D30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4D3E")
    Jump("loc_4FB8")

    label("loc_4D3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4D4C")
    Jump("loc_4FB8")

    label("loc_4D4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4D89")

    ChrTalk(
        0xFE,
        (
            "Oh no!\x01",
            "My name is Nigata ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FB8")

    label("loc_4D89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4D97")
    Jump("loc_4FB8")

    label("loc_4D97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4E51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E15")

    ChrTalk(
        0xFE,
        (
            "やっとHenryちゃんを\x01",
            "You found it …?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "OK, well …\x01",
            "つぎはRyu君を\x01",
            "I have to find it … ….\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4E4C")

    label("loc_4E15")


    ChrTalk(
        0xFE,
        (
            "でも、Ryu君の隠れ場所、\x01",
            "I really do not know …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E4C")

    Jump("loc_4FB8")

    label("loc_4E51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4F0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4ED6")

    ChrTalk(
        0xFE,
        (
            "Ryu君たちと\x01",
            "Hide and seek.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But I can not find it at all …\x01",
            "Where is it hidden …?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4F07")

    label("loc_4ED6")


    ChrTalk(
        0xFE,
        (
            "Ryu君たち、\x01",
            "Where is it hidden …?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F07")

    Jump("loc_4FB8")

    label("loc_4F0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4F1A")
    Jump("loc_4FB8")

    label("loc_4F1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4F28")
    Jump("loc_4FB8")

    label("loc_4F28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_4F36")
    Jump("loc_4FB8")

    label("loc_4F36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4F44")
    Jump("loc_4FB8")

    label("loc_4F44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4FA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F5F")
    Call(0, 16)
    Jump("loc_4F9C")

    label("loc_4F5F")


    ChrTalk(
        0xFE,
        (
            "Tomorrow is everyone\x01",
            "I am in a department store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I 'm looking forward\x02",
    )

    CloseMessageWindow()

    label("loc_4F9C")

    Jump("loc_4FB8")

    label("loc_4FA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4FAF")
    Jump("loc_4FB8")

    label("loc_4FAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4FB8")

    label("loc_4FB8")

    TalkEnd(0xFE)
    Return()

    # Function_21_4CB8 end

    def Function_22_4FBC(): pass

    label("Function_22_4FBC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4FCD")
    Jump("loc_5591")

    label("loc_4FCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4FDB")
    Jump("loc_5591")

    label("loc_4FDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4FE9")
    Jump("loc_5591")

    label("loc_4FE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4FF7")
    Jump("loc_5591")

    label("loc_4FF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5068")

    ChrTalk(
        0xFE,
        "Well, it is no occupation of mining town …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is kind of uneasy …\x01",
            "peach、早く帰ってこないかしら……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5591")

    label("loc_5068")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5076")
    Jump("loc_5591")

    label("loc_5076")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_50D7")

    ChrTalk(
        0xFE,
        (
            "From a little while ago, ambulance\x01",
            "It seems like I have been back and forth many times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I wonder what happened …?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5591")

    label("loc_50D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_514D")

    ChrTalk(
        0xFE,
        (
            "Mr. Ian, I am very busy.\x01",
            "You seem to be doing it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Today, frequently\x01",
            "It seems like you are in and out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5591")

    label("loc_514D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_51F9")

    ChrTalk(
        0xFE,
        (
            "Since the trade meeting,\x01",
            "About master and master seriously\x01",
            "We talked a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Cross Bell residents\x01",
            "It is a matter related to everyone.\x01",
            "I have to think firmly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5591")

    label("loc_51F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5207")
    Jump("loc_5591")

    label("loc_5207")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_5215")
    Jump("loc_5591")

    label("loc_5215")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5318")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52B7")

    ChrTalk(
        0xFE,
        "Welcome~.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "peachたち、今日は除幕式を\x01",
            "You are going to see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, when I return home\x01",
            "Speak a lot\x01",
            "I've got to hear it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5313")

    label("loc_52B7")


    ChrTalk(
        0xFE,
        (
            "peachたち、今日は除幕式を\x01",
            "You are going to see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, have fun\x01",
            "I hope to give it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5313")

    Jump("loc_5591")

    label("loc_5318")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_54C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5438")

    ChrTalk(
        0xFE,
        (
            "On this rainy day,\x01",
            "peachがお使いからなかなか\x01",
            "I was worried not to go home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Then when you listen to the story,\x01",
            "I was looking for a lost umbrella.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "peachったら、傘なんていくらでも\x01",
            "I will buy it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As long as I worry about it,\x01",
            "It's that cheap thing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_54C1")

    label("loc_5438")


    ChrTalk(
        0xFE,
        (
            "But, to take care of things is\x01",
            "You have a very good heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is not good to worry,\x01",
            "peachにはその心をいつまでも\x01",
            "I want you to have it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54C1")

    Jump("loc_5591")

    label("loc_54C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_54D4")
    Jump("loc_5591")

    label("loc_54D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5591")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_553F")

    ChrTalk(
        0xFE,
        "Welcome~.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Support the region\x01",
            "\"Tally's shop\"\x01",
            "Here it is ~.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5591")

    label("loc_553F")


    ChrTalk(
        0xFE,
        (
            "peachも日曜学校に\x01",
            "That's what I did ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We work\x01",
            "I must do my best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5591")

    TalkEnd(0xFE)
    Return()

    # Function_22_4FBC end

    def Function_23_5595(): pass

    label("Function_23_5595")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_55A6")
    Jump("loc_5C43")

    label("loc_55A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_55B4")
    Jump("loc_5C43")

    label("loc_55B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5640")

    ChrTalk(
        0xFE,
        (
            "From this morning I will head towards the border gate\x01",
            "You can see many power guided vehicles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Apparently, the foreigner who will stay\x01",
            "You seem to be going home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C43")

    label("loc_5640")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_564E")
    Jump("loc_5C43")

    label("loc_564E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_565C")
    Jump("loc_5C43")

    label("loc_565C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_566A")
    Jump("loc_5C43")

    label("loc_566A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_57E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_575B")

    ChrTalk(
        0xFE,
        (
            "From the drive to the Belgard gate\x01",
            "It is where I came back … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I caught it on my way home.\x01",
            "West Crossbell Highwayの事故現場は\x01",
            "It was a big trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What is it that you derail dramatically up to Oh?\x01",
            "I thought it was unexpected ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_57DC")

    label("loc_575B")


    ChrTalk(
        0xFE,
        (
            "I caught it on my way home.\x01",
            "West Crossbell Highwayの事故現場は\x01",
            "It was a big trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "A lot of police and security guards crowded\x01",
            "You seem to have done it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57DC")

    Jump("loc_5C43")

    label("loc_57E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_57EF")
    Jump("loc_5C43")

    label("loc_57EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_57FD")
    Jump("loc_5C43")

    label("loc_57FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_580B")
    Jump("loc_5C43")

    label("loc_580B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_5819")
    Jump("loc_5C43")

    label("loc_5819")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_599D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5913")

    ChrTalk(
        0xFE,
        (
            "The old lady is angry,\x01",
            "I have a good tongue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Together with the unveiling ceremony\x01",
            "Although I was going to go see it,\x01",
            "I ignored it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After drinking that wine with fireworks,\x01",
            "Let's be the best … ….\x01",
            "I do not understand the atmosphere at all.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5998")

    label("loc_5913")


    ChrTalk(
        0xFE,
        (
            "Huh, whatever.\x01",
            "I bought high shopping\x01",
            "With plenty of forever ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If the grandpa is it\x01",
            "I will not know it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5998")

    Jump("loc_5C43")

    label("loc_599D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_59AB")
    Jump("loc_5C43")

    label("loc_59AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_59B9")
    Jump("loc_5C43")

    label("loc_59B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5C43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BD5")

    ChrTalk(
        0xFE,
        (
            "Hokkaido\x01",
            "I guess the guided car is good again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The old lady is wasteful\x01",
            "I left it,\x01",
            "I bought it and it was right answer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FVehicle made by Verne … …\x01",
            "With chic design\x01",
            "I think it's lovely!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ho, this is this …\x01",
            "I am still young and I can talk!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5B0C")
    OP_63(0x109, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)

    label("loc_5B0C")

    Sleep(1000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B35")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_5B35")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B5B")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_5B5B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B81")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_5B81")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5BA7")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_5BA7")

    Sleep(1000)

    ChrTalk(
        0x101,
        "#00012F(I'm in confusion … ….)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5C43")

    label("loc_5BD5")


    ChrTalk(
        0xFE,
        (
            "Drive with this driven car\x01",
            "It's really great.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even the old man, there\x01",
            "You want me to understand.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C43")

    TalkEnd(0xFE)
    Return()

    # Function_23_5595 end

    def Function_24_5C47(): pass

    label("Function_24_5C47")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5C58")
    Jump("loc_5C94")

    label("loc_5C58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5C94")

    ChrTalk(
        0xFE,
        (
            "It is kind of uneasy …\x01",
            "I wonder if it was an accident.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C94")

    TalkEnd(0xFE)
    Return()

    # Function_24_5C47 end

    def Function_25_5C98(): pass

    label("Function_25_5C98")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5CA9")
    Jump("loc_5CDC")

    label("loc_5CA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5CDC")

    ChrTalk(
        0xFE,
        "I do not like the sound of ambulances so much ….\x02",
    )

    CloseMessageWindow()

    label("loc_5CDC")

    TalkEnd(0xFE)
    Return()

    # Function_25_5C98 end

    def Function_26_5CE0(): pass

    label("Function_26_5CE0")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "The train is derailed\x01",
            "When I saw it, I suspected my eyes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "An injured person was also quite\x01",
            "It looks like it,\x01",
            "I wonder if it was OK …\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_5CE0 end

    def Function_27_5D60(): pass

    label("Function_27_5D60")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5DF8")

    ChrTalk(
        0xFE,
        (
            "Already, beforehand\x01",
            "In the shoes is Bichobicho's\x01",
            "It is not gucci gucho!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's why I do not like rain.\x01",
            "I have to finish my errands and finally come back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E64")

    label("loc_5DF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5E64")

    ChrTalk(
        0xFE,
        (
            "Oh no … raining storm!\x01",
            "I do not mind going down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I have to finish my errands and finally come back.\x02",
    )

    CloseMessageWindow()

    label("loc_5E64")

    TalkEnd(0xFE)
    Return()

    # Function_27_5D60 end

    def Function_28_5E68(): pass

    label("Function_28_5E68")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F6D")

    ChrTalk(
        0xFE,
        (
            "Such a case\x01",
            "It has happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even though it is very powerful\x01",
            "I'm being wary of the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If the empire is a criminal,\x01",
            "I will be attacking again soon\x01",
            "I do not think the possibility is low …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tentatively,\x01",
            "Until the referendum after 3 days\x01",
            "I can not mind.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_5FF7")

    label("loc_5F6D")


    ChrTalk(
        0xFE,
        (
            "If the empire is a criminal,\x01",
            "I will be attacking again soon\x01",
            "I do not think the possibility is low …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tentatively,\x01",
            "Until the referendum after 3 days\x01",
            "I can not mind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FF7")

    TalkEnd(0xFE)
    Return()

    # Function_28_5E68 end

    def Function_29_5FFB(): pass

    label("Function_29_5FFB")

    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#00005FSergey Managerが支援課に\x01",
            "It looks like I am making something ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FAnyway, here is\x01",
            "It seems better not to go through.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_29_5FFB end

    def Function_30_607E(): pass

    label("Function_30_607E")

    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door seems to be tightly closed.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x95, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_60D2")
    TalkEnd(0xFF)
    Call(0, 31)
    Return()

    label("loc_60D2")

    TalkEnd(0xFF)
    Return()

    # Function_30_607E end

    def Function_31_60D6(): pass

    label("Function_31_60D6")

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
            "#6P#00008F……………………………………………….\x02\x03",
            "#00003F(Pete, you, Mr. Quint,\x01",
            "And Nielsen's story …)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6228")
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    label("loc_6228")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_624E")
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    label("loc_624E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6274")
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    label("loc_6274")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_629A")
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    label("loc_629A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_62C0")
    OP_63(0x4, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    label("loc_62C0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_62E6")
    OP_63(0x5, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    label("loc_62E6")

    Sleep(1000)

    def lambda_62EE():
        TurnDirection(0x102, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_62EE)
    Sleep(50)

    def lambda_62FE():
        TurnDirection(0x103, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_62FE)

    def lambda_630B():
        TurnDirection(0x104, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_630B)
    Sleep(50)

    def lambda_631B():
        TurnDirection(0xF4, 0x101, 300)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_631B)
    Sleep(50)

    def lambda_632B():
        TurnDirection(0xF5, 0x101, 300)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_632B)
    WaitChrThread(0xF5, 2)

    ChrTalk(
        0x102,
        "#6P#00105FLloyd … … What's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FTo Professor Ian's office\x01",
            "Is there something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00301FNow I'm out, but … ….\x02",
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
            "#11P#00006F…… No, nothing.\x01",
            "I will go now.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6457")

    ChrTalk(
        0x10A,
        "#12P#00605F……………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_6457")

    OP_5A()
    SetScenarioFlags(0x1BE, 0)
    OP_2C(0xB1, 0x3)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_31_60D6 end

    def Function_32_6477(): pass

    label("Function_32_6477")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_648E")
    Call(0, 49)
    Return()

    label("loc_648E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_64A0")
    Call(0, 50)
    Return()

    label("loc_64A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64F2")

    ChrTalk(
        0x101,
        (
            "#00000FNow I have no business to go out to the city.\x01",
            "I do not need to use a car.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    label("loc_64F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_65EA")
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
            "* Support department vehicles are now available.\x02",
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

    label("loc_65EA")

    SetMapFlags(0x80)
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6605")
    Jump("loc_6675")

    label("loc_6605")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6614")
    Jump("loc_6675")

    label("loc_6614")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_662F")
    SetScenarioFlags(0x31, 2)

    label("loc_662F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6675")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_666F")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6664")
    Sound(2499, 255, 100, 0)
    Jump("loc_666A")

    label("loc_6664")

    Sound(3537, 255, 100, 0)

    label("loc_666A")

    Jump("loc_6675")

    label("loc_666F")

    Sound(3344, 255, 100, 0)

    label("loc_6675")

    SetMapObjFrame(0xA, "light", 0x0, 0x1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_668C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6A6B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_6705")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Mercapa")
    MenuCmd(1, 0, "quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_66E5"),
        (SWITCH_DEFAULT, "loc_66F6"),
    )


    label("loc_66E5")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_6700")

    label("loc_66F6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6700")

    Jump("loc_6A66")

    label("loc_6705")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "Travel with a driving car")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_6761")
    MenuCmd(1, 0, "Take a break with a driving car")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6761")

    MenuCmd(1, 0, "Customizing the powertrain")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    MenuCmd(1, 0, "quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_69D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6812")

    ChrTalk(
        0x101,
        (
            "#00003FThe guided car could be secured with this.\x02\x03",
            "#00001FTentatively, before the strategy\x01",
            "Let's head to the station.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_69CC")

    label("loc_6812")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_687A")

    ChrTalk(
        0x101,
        (
            "#00001FAnyway now\x01",
            "I have to chase Randy -\x01",
            "Let's thoroughly investigate the city first.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_69CC")

    label("loc_687A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68CD")

    ChrTalk(
        0x101,
        (
            "#00000FNow I have no business to go out to the city.\x01",
            "I do not need to use a car.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_69CC")

    label("loc_68CD")

    SetMapObjFrame(0xA, "light", 0x0, 0x1)
    OP_74(0xA, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_68FE")
    OP_70(0xA, 0x12C)
    OP_71(0xA, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_690E")

    label("loc_68FE")

    OP_70(0xA, 0xF0)
    OP_71(0xA, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_690E")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6964")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6964")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6987")
    Sound(461, 0, 100, 0)

    label("loc_6987")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_69A7")
    OP_70(0xA, 0x14A)
    OP_71(0xA, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_69B7")

    label("loc_69A7")

    OP_70(0xA, 0x10E)
    OP_71(0xA, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_69B7")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0xA, "light", 0x1, 0x1)
    OP_70(0xA, 0x0)

    label("loc_69CC")

    Jump("loc_6A66")

    label("loc_69D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A47")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_6A0A")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_6A22")

    label("loc_6A0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_6A1D")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_6A22")

    label("loc_6A1D")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_6A22")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6A66")

    label("loc_6A47")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A5C")
    Call(0, 33)
    Jump("loc_6A66")

    label("loc_6A5C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6A66")

    Jump("loc_668C")

    label("loc_6A6B")

    SetMapObjFrame(0xA, "light", 0x1, 0x1)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_32_6477 end

    def Function_33_6A81(): pass

    label("Function_33_6A81")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF000000), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x0)
    SetChrFlags(0x0, 0x8)
    SetChrFlags(0x1, 0x8)
    SetChrFlags(0x2, 0x8)
    SetChrFlags(0x3, 0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6AC7")
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    label("loc_6AC7")

    SetMapObjFrame(0xFF, "main7", 0x0, 0x1)
    MiniGame(0x33, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFrame(0xFF, "main7", 0x1, 0x1)
    ClearChrFlags(0x0, 0x8)
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6B30")
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_6B30")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventEnd(0x5)
    SetMapFlags(0x80)
    Return()

    # Function_33_6A81 end

    def Function_34_6B42(): pass

    label("Function_34_6B42")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_6B9D")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6B92")
    Sound(2502, 255, 100, 0)
    Jump("loc_6B98")

    label("loc_6B92")

    Sound(2503, 255, 100, 0)

    label("loc_6B98")

    Jump("loc_6BC1")

    label("loc_6B9D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6BBB")
    Sound(3347, 255, 100, 0)
    Jump("loc_6BC1")

    label("loc_6BBB")

    Sound(3348, 255, 100, 0)

    label("loc_6BC1")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_34_6B42 end

    def Function_35_6BD6(): pass

    label("Function_35_6BD6")

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

    # Function_35_6BD6 end

    def Function_36_6C81(): pass

    label("Function_36_6C81")

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

    def lambda_6DE2():
        OP_97(0x101, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6DE2)
    Sleep(100)

    def lambda_6DFF():
        OP_97(0x102, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6DFF)
    Sleep(300)

    def lambda_6E1C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6E1C)
    Sleep(100)

    def lambda_6E30():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6E30)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x101, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    WaitChrThread(0x102, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_6E7D():
        OP_97(0x105, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_6E7D)
    Sleep(100)

    def lambda_6E9A():
        OP_97(0x109, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6E9A)
    Sleep(100)

    def lambda_6EB7():
        OP_97(0x1A5, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A5, 0, lambda_6EB7)
    Sleep(800)

    def lambda_6ED4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6ED4)
    Sleep(100)

    def lambda_6EE8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6EE8)
    Sleep(1000)

    def lambda_6EFC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A5, 2, lambda_6EFC)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00005F#5Pis this……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00105FUntil when?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x109,
        (
            "#10105F#11PWell, back door of support department\x01",
            "Did you feel like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#5POh dear\x01",
            "I feel that it is under construction.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x1A5, 0)

    ChrTalk(
        0x1A5,
        (
            "#11P#01105FOh, I see.\x01",
            "Lloyd's do not know.\x02\x03",
            "#01100FWell, after Lloyd's business trip,\x01",
            "The construction people came.\x02\x03",
            "It seems the church has called.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_706B():
        TurnDirection(0x101, 0x1A5, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_706B)
    Sleep(50)

    def lambda_707B():
        TurnDirection(0x102, 0x1A5, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_707B)
    Sleep(50)

    def lambda_708B():
        TurnDirection(0x105, 0x1A5, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_708B)
    Sleep(50)

    def lambda_709B():
        TurnDirection(0x109, 0x1A5, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_709B)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x101,
        (
            "#6P#00006FIs it so……\x01",
            "I did not notice yesterday.\x02\x03",
            "#00001FHowever,\x01",
            "What on earth are you going to do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103FWell, there's something wrong.\x01",
            "I think that it is construction … ….\x02\x03",
            "#00100FAnyway, who is this\x01",
            "It seems better not to go through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FOh, let's get out from the entrance on the first floor.\x02",
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

    # Function_36_6C81 end

    def Function_37_71F8(): pass

    label("Function_37_71F8")

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
        "#00005F#5PAh……\x02",
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
        "#01002F#5PHmm, it's a nice finish.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#5PChief, this is …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F#5PBy any chance\x01",
            "For this driving car?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#01004F#5POh, with slope\x01",
            "It is construction of expansion parking space.\x02\x03",
            "#01004FOnce in budget, from the police headquarters\x01",
            "I picked it up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102F#5POh … oh good!\x02\x03",
            "#10109FIf there is only that space\x01",
            "I think that maintenance can be done!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#5PHuh, Do you have a life with a driving car?\x01",
            "It seems to be quite moist.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#5Pはは……Keyaが\x01",
            "I jumped and it seemed to be pleased.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x8)
    ClearChrFlags(0x9, 0x8)

    NpcTalk(
        0x8,
        "Boys' Voices",
        "Wow, what is this! Is it?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Boys' Voices",
        "Clean car ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x14, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_7929():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7929)
    Sleep(50)

    def lambda_7939():
        OP_93(0x109, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7939)
    Sleep(50)

    def lambda_7949():
        OP_93(0x105, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7949)
    Sleep(50)

    def lambda_7959():
        OP_93(0x102, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_7959)
    Sleep(50)

    def lambda_7969():
        OP_93(0x14, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_7969)
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

    def lambda_79DA():
        OP_96(0xFE, 0x3C8C, 0x0, 0xFFFFDAE4, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_79DA)

    def lambda_79F4():
        OP_96(0xFE, 0x3BC4, 0x0, 0xFFFFE08E, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_79F4)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x101,
        "#00002F#11Pやあ、RyuにHenry。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109F#11PHehe, I met him again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PSmooth!\x01",
            "I have never seen such a car!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PPerhaps Kore,\x01",
            "My brother bought it! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#11PHaha, that's not the case.\x02\x03",
            "#00002FBut once in the support department\x01",
            "I got used to it.\x02",
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
        "#6PIs that true, huh? Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6POnii-chan, before I knew\x01",
            "I got such a good career! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#11PNo, she got a separate career\x01",
            "I do not have it …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00000F#11PBy the way, today\x01",
            "Keyaと一緒じゃないのか？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F#11PPossibly\x01",
            "peachちゃんと一緒かしら？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#6PNo, I do not know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PFrom Sunday School together\x01",
            "I did not come back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#11PWell, is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PKeyaちゃん、マーブル先生に\x01",
            "I have something to do with it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PPossibly yet\x01",
            "Maybe he is in the cathedral …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#11PIs it so……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#11PI wonder what's wrong ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)

    def lambda_7DF4():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7DF4)
    Sleep(50)

    def lambda_7E04():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7E04)
    Sleep(50)

    def lambda_7E14():
        TurnDirection(0x14, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_7E14)
    Sleep(50)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x14, 0)
    OP_64(0x101)
    OP_64(0x102)

    ChrTalk(
        0x105,
        (
            "#10302F#6PWhew.\x01",
            "I still have overprotection as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109F#5PよっぽどKeyaちゃんが\x01",
            "It's cute and can not be helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#11PNo~……\x01",
            "I do not think there is such a thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00112F#11PWell, yeah.\x01",
            "It is a range of common sense as a guardian.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#01004F#6PKuku, if you worry so much\x01",
            "Why do not you go to pick me up in the cathedral?\x02\x03",
            "#01002FThere is a lot of legs.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00000F#11POh, that's right.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x109, 500)

    ChrTalk(
        0x102,
        "#00102F#11PNoel, can you ask?\x02",
    )

    CloseMessageWindow()

    def lambda_8004():
        TurnDirection(0x101, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8004)
    Sleep(50)

    def lambda_8014():
        TurnDirection(0x105, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8014)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x109,
        "#10102F#5PYes, it is cheap.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PWhat? Is it?\x01",
            "Keyaを迎えに行くの！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6PI and I, too!\x01",
            "Please take me with you!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_80B0():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_80B0)
    Sleep(15)

    def lambda_80C0():
        OP_93(0x102, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_80C0)
    Sleep(15)

    def lambda_80D0():
        OP_93(0x109, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_80D0)
    Sleep(15)

    def lambda_80E0():
        OP_93(0x105, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_80E0)
    Sleep(15)

    def lambda_80F0():
        OP_93(0x14, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_80F0)
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
        "#5Pちょ、ちょっとRyu！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5PCome home early to my uncle\x01",
            "Were not you being told?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)

    ChrTalk(
        0x8,
        "#12PWell, it was.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12PToday is rare, ne,\x01",
            "You are back home ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#11PHaha, if so, hurry\x01",
            "I have to go home.\x02\x03",
            "#00002Fnext time,\x01",
            "Because I can carry two people.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_824C():
        OP_93(0x8, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_824C)
    Sleep(50)

    def lambda_825C():
        OP_93(0x9, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_825C)
    Sleep(50)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x9, 0)

    ChrTalk(
        0x8,
        "#6PWhy, it's absolutely!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#6PWell then\x01",
            "Excuse me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00109F#11PHuhu, please return home.\x02",
    )

    CloseMessageWindow()

    def lambda_82E8():
        OP_93(0x8, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_82E8)
    Sleep(50)

    def lambda_82F8():
        OP_93(0x9, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_82F8)
    Sleep(50)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x9, 0)
    OP_68(19000, 800, -8750, 2500)

    def lambda_8321():
        OP_96(0xFE, 0x2742, 0x0, 0xFFFFDF30, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8321)
    Sleep(50)

    def lambda_833E():
        OP_96(0xFE, 0x2486, 0x0, 0xFFFFE796, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_833E)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    OP_6F(0x79)
    OP_93(0x14, 0x87, 0x1F4)

    ChrTalk(
        0x14,
        (
            "#01003F#5PAll right, sort of\x01",
            "Come visit me.\x02\x03",
            "#01000FI will go back ahead.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_83C9():
        TurnDirection(0x101, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_83C9)
    Sleep(50)

    def lambda_83D9():
        TurnDirection(0x102, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_83D9)
    Sleep(50)

    def lambda_83E9():
        TurnDirection(0x109, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_83E9)
    Sleep(50)

    def lambda_83F9():
        TurnDirection(0x105, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_83F9)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        "#00000F#12PYes, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F#11PWell then I'll be back.\x02",
    )

    CloseMessageWindow()
    OP_68(19000, 800, -9350, 2500)

    def lambda_8476():
        OP_93(0xFE, 0xB4, 0x96)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8476)

    def lambda_8483():
        OP_93(0xFE, 0xB4, 0xFA)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_8483)

    def lambda_8490():
        OP_93(0xFE, 0xB4, 0x96)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8490)

    def lambda_849D():
        OP_93(0xFE, 0xB4, 0x96)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_849D)
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
            "#10104F#5PHuhu, then\x01",
            "Shall we head to the cathedral?\x02\x03",
            "#10100Fここからだと、Central squareから\x01",
            "Entertainment district方面に抜けますね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8567():
        TurnDirection(0x101, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8567)
    Sleep(50)

    def lambda_8577():
        TurnDirection(0x102, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8577)
    Sleep(50)

    def lambda_8587():
        TurnDirection(0x105, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8587)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        (
            "#00002F#12PI got it, please.\x02\x03",
            "#00004F……うーん、Keyaが\x01",
            "A surprising face appears to the eyes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F#12PHuhu, that girl\x01",
            "I love driving vehicles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#6PWhew.\x01",
            "I'm really stupid.\x02",
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

    def lambda_8740():
        OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_8740)

    def lambda_8755():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_8755)
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
        "#30W………… Guru ………………\x02",
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

    # Function_37_71F8 end

    def Function_38_88C5(): pass

    label("Function_38_88C5")

    SetChrPos(0xFE, -36200, 0, 4000, 90)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -5850, 0, 4000)
    OP_9F(0x1, 800, 0, 1800)
    OP_9F(0x1, 8050, 0, -5950)
    OP_9F(0x1, 15500, 0, -6700)
    OP_9F(0x2, 0xFE, 5000, 0x6)
    Return()

    # Function_38_88C5 end

    def Function_39_891C(): pass

    label("Function_39_891C")

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

    # Function_39_891C end

    def Function_40_89B1(): pass

    label("Function_40_89B1")

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

    # Function_40_89B1 end

    def Function_41_8A4A(): pass

    label("Function_41_8A4A")

    OP_95(0xFE, 19000, 0, -8600, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(200)

    def lambda_8A6D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8A6D)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_41_8A4A end

    def Function_42_8A7E(): pass

    label("Function_42_8A7E")

    OP_95(0xFE, 19000, 0, -8600, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(200)

    def lambda_8AA1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8AA1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_42_8A7E end

    def Function_43_8AB2(): pass

    label("Function_43_8AB2")

    OP_95(0xFE, 19000, 0, -8600, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(200)

    def lambda_8AD5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8AD5)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_43_8AB2 end

    def Function_44_8AE6(): pass

    label("Function_44_8AE6")

    OP_95(0xFE, 19000, 0, -8600, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(200)

    def lambda_8B09():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8B09)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_44_8AE6 end

    def Function_45_8B1A(): pass

    label("Function_45_8B1A")

    Sleep(4500)
    StopSound(468, 1000, 80)
    Sound(492, 0, 80, 0)
    Return()

    # Function_45_8B1A end

    def Function_46_8B2A(): pass

    label("Function_46_8B2A")

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

    def lambda_8CB0():
        OP_97(0x101, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8CB0)
    Sleep(50)

    def lambda_8CCD():
        OP_97(0x102, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8CCD)
    Sleep(50)

    def lambda_8CEA():
        OP_97(0x105, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8CEA)
    Sleep(50)

    def lambda_8D07():
        OP_97(0x109, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8D07)
    Sleep(50)

    def lambda_8D24():
        OP_97(0x104, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_8D24)
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

    def lambda_8DE9():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8DE9)
    Sleep(50)

    def lambda_8DF9():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8DF9)
    Sleep(50)

    def lambda_8E09():
        OP_93(0x105, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8E09)
    Sleep(50)

    def lambda_8E19():
        OP_93(0x109, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8E19)
    Sleep(50)

    def lambda_8E29():
        OP_93(0x104, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_8E29)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x101,
        "#5P#00005Fthat……?\x02",
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

    def lambda_8F61():

        label("loc_8F61")

        OP_A0(0xFE, 1500, 0x0, 0x4)
        Yield()
        Jump("loc_8F61")

    QueueWorkItem2(0x18, 2, lambda_8F61)

    def lambda_8F73():
        OP_96(0xFE, 0x7FBC, 0xFFFFF8F8, 0xFFFFAD30, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_8F73)
    Sound(847, 2, 70, 0)
    WaitChrThread(0x18, 1)
    BeginChrThread(0x18, 3, 0, 47)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_8FB5():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8FB5)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_8FDD():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8FDD)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_9005():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9005)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_902D():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_902D)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_9055():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_9055)
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
        "#00011F#6PWhat! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10111F#6PAnd then a white hawk …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305F#6P……Disagreeable\x01",
            "It looks like falcon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#6PHey, what do you mean?\x01",
            "In the middle of such a city ……\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x18, 0x3)
    WaitChrThread(0x18, 1)
    EndChrThread(0x18, 0x0)
    OP_68(33300, -2800, -20900, 3000)
    MoveCamera(40, 21, 0, 3000)

    def lambda_918A():
        OP_9E(0xFE, 0x878C, 0xFFFFAD30, 0x50910, 0xED8, 0x1)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_918A)
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

    def lambda_930D():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_930D)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xBEA), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC1C), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC4E), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)

    def lambda_9356():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9356)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC80), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xCB2), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xCE4), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xD16), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)

    def lambda_939F():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_939F)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xD48), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xD7A), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xDAC), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xDDE), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)

    def lambda_93E8():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_93E8)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xE10), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xE42), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xE74), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xEA6), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)

    def lambda_9431():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9431)
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

    def lambda_94D5():
        OP_96(0xFE, 0x8278, 0xFFFFF1F0, 0xFFFFAA74, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_94D5)
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
            "Pewie.\x02\x03",
            "Pui, Pui, Pewie.\x02",
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
            "#00001F#5PWell, maybe ….\x01",
            "Is there something we have for us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00108FZeitが話しかける時と\x01",
            "It feels like the same thing ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00306FWell, Tio if it's fine\x01",
            "It seems I understand what you are talking about ……\x02",
        )
    )

    CloseMessageWindow()
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x5, 0x10)
    OP_71(0x5, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x5)
    ClearChrFlags(0x17, 0x80)

    def lambda_9714():
        OP_96(0xFE, 0x9A4C, 0xFFFFF060, 0xFFFFB5C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_9714)

    def lambda_972E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_972E)
    WaitChrThread(0x17, 1)
    Sound(104, 0, 100, 0)
    OP_71(0x5, 0xA, 0x0, 0x0, 0x0)

    ChrTalk(
        0x17,
        "#01105F#12POh, what's wrong?\x02",
    )

    OP_79(0x5)
    SetMapObjFlags(0x5, 0x10)
    CloseMessageWindow()
    OP_63(0x17, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrChipByIndex(0x17, 0x22)
    SetChrSubChip(0x17, 0x0)

    def lambda_97A8():
        OP_95(0xFE, 37500, -4000, -19000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_97A8)
    WaitChrThread(0x17, 1)

    def lambda_97C6():
        OP_95(0xFE, 34500, -4000, -21300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_97C6)
    Sleep(300)

    def lambda_97E3():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_97E3)
    Sleep(100)

    def lambda_97F3():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_97F3)
    Sleep(100)

    def lambda_9803():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9803)
    Sleep(100)

    def lambda_9813():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9813)
    WaitChrThread(0x17, 1)
    SetChrChipByIndex(0x17, 0x21)
    SetChrSubChip(0x17, 0x0)
    OP_93(0x17, 0xE1, 0x1F4)
    Sound(3029, 255, 100, 0)

    ChrTalk(
        0x17,
        (
            "#01110F#11PWow, it's a white trick!\x02\x03",
            "#01109FBeaked sharp pointed\x01",
            "Cool!\x02",
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
            "#6P#08009FPew eyed\x02\x03",
            "Puii, Pui, Pui ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#01103F#11PHmm, hmm.\x02\x03",
            "#01102FI see, I see.\x02",
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
            "#00012F#5P（Keya……\x01",
            "After all I wonder? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10112F#5P(That's awesome, is not it? …)\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x17, 0x101, 500)

    def lambda_99ED():

        label("loc_99ED")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_99ED")

    QueueWorkItem2(0x17, 2, lambda_99ED)
    SetChrChipByIndex(0x18, 0x1F)
    SetChrSubChip(0x18, 0x2)

    ChrTalk(
        0x17,
        (
            "#01100F#11PWell, this girl,\x01",
            "It's called \"Sieg\".\x02\x03",
            "Because there are messages in Lloyd's\x01",
            "I'm telling you to accept it?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9A82():
        TurnDirection(0x101, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9A82)
    Sleep(50)

    def lambda_9A92():
        TurnDirection(0x104, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_9A92)
    Sleep(50)

    def lambda_9AA2():
        TurnDirection(0x109, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_9AA2)
    Sleep(50)

    def lambda_9AB2():
        TurnDirection(0x105, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_9AB2)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        "#00011F#5PWell, maybe ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00305FOh, surely on the legs\x01",
            "The memo is bound up.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9B33():
        OP_95(0xFE, 33200, -4000, -21000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9B33)
    TurnDirection(0x18, 0x101, 500)
    WaitChrThread(0x101, 1)
    EndChrThread(0x17, 0x2)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはWhite falconの脚に\x01",
            "I took the memo attached.\x07\x00\x02",
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
            "Dear Sir Crossbell Police, Mission Support Division\x02\x03",
            "Hearing the reputation of everyone\x01",
            "Incomplete#4RBrute#But I contacted you.\x02\x03",
            "If you have time confidentially\x01",
            "Would you please take a look at the consultation?\x02\x03",
            "Today evening, Crossbell Airport,\x01",
            "We are waiting at the waiting terrace.\x02\x03",
            "Postscript If you can not conveniently\x01",
            "You do not have to answer.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(150)

    AnonymousTalk(
        0x101,
        "#00005F……………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        "#00101FHere, this …\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x109,
        (
            "#10106FContents and nice, sender unknown and nice\x01",
            "I am too suspicious but … ….\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x105,
        (
            "#10302FBut it's a beautiful handwriting,\x01",
            "The sentences are also polite feeling.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x104,
        (
            "#00301FMore than anything, it is pushed by memos\x01",
            "このWhite falconの紋章は……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x18,
        (
            "#08000FPewie.\x02\x03",
            "Pui, Pui, Pewie.\x02",
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

    def lambda_9ED0():
        OP_96(0xFE, 0x8278, 0xFFFFF3E4, 0xFFFFAA74, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_9ED0)
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

    def lambda_9F56():

        label("loc_9F56")

        OP_A0(0xFE, 1500, 0x0, 0x4)
        Yield()
        Jump("loc_9F56")

    QueueWorkItem2(0x18, 2, lambda_9F56)
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

    def lambda_A18B():
        OP_96(0xFE, 0x8278, 0xFFFFFED4, 0xFFFF7B94, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_A18B)
    Sleep(300)

    def lambda_A1A8():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_A1A8)
    Sleep(100)

    def lambda_A1B8():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A1B8)
    Sleep(100)

    def lambda_A1C8():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_A1C8)
    Sleep(100)

    def lambda_A1D8():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A1D8)
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
            "#6P#00011FEr …\x01",
            "Keya、彼はなんて？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x17, 0x101, 500)

    ChrTalk(
        0x17,
        (
            "#01111F#11PWell, I do not go or go\x01",
            "It depends on Lloyd's.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00003FReally……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    def lambda_A357():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_A357)
    Sleep(50)

    def lambda_A367():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_A367)
    Sleep(50)

    def lambda_A377():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_A377)
    Sleep(50)

    def lambda_A387():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_A387)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x102,
        (
            "#6P#00108FWhere are you going to do?\x02\x03",
            "#00101FNo way\x01",
            "I do not think there is nothing ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#00306FOh, indeed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108F#11Pでも、White falconの紋章って……\x01",
            "It seems that the current child was like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309F#5PHaha, no, no more\x01",
            "I will expect it.\x02",
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
            "#12P#00003F── It is a great teaser.\x01",
            "I will accept it here.\x02\x03",
            "#00000FI still have time until the evening\x01",
            "Even after I've done errands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00106FI knew.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106F#11PI was nervous …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00309FWell, as expected\x01",
            "I do not think we need to go … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#5PHuff, then then when you finish\x01",
            "Shall we go to the south exit crossbar airport?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x17, 0x13B, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x17,
        (
            "#11P#01110FI do not really know.\x01",
            "Everyone, do your best.\x02",
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

    # Function_46_8B2A end

    def Function_47_A6AE(): pass

    label("Function_47_A6AE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A6DD")

    def lambda_A6BE():
        OP_9E(0xFE, 0x8980, 0xFFFFAD30, 0x57E40, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_A6BE)
    WaitChrThread(0x18, 1)
    Jump("Function_47_A6AE")

    label("loc_A6DD")

    Return()

    # Function_47_A6AE end

    def Function_48_A6DE(): pass

    label("Function_48_A6DE")


    def lambda_A6E3():
        OP_9E(0xFE, 0x846C, 0xFFFFAA74, 0x2BF20, 0xED8, 0x1)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_A6E3)
    WaitChrThread(0x18, 1)

    def lambda_A702():
        OP_9E(0xFE, 0x8084, 0xFFFFAA74, 0x57E40, 0x1194, 0x1)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_A702)
    WaitChrThread(0x18, 1)
    Return()

    # Function_48_A6DE end

    def Function_49_A71D(): pass

    label("Function_49_A71D")

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
            "#00206F#12Pby the way……\x02\x03",
            "#00200FNoel's driving also\x01",
            "Today is the last one.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A828():
        OP_93(0x109, 0xB3, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A828)
    Sleep(400)

    ChrTalk(
        0x101,
        "#12P#00006FI see … it was.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112F#5PHaha ……\x01",
            "I am also very sorry.\x02\x03",
            "this child#2RA car#Personally\x01",
            "I liked it quite a bit.\x02\x03",
            "#10100FBut Lloyd's also\x01",
            "You can drive a lot already, do not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00004FOh, day off, something\x01",
            "Noel has trained him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00109FFluffy, easy to understand\x01",
            "It was very helpful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10306FWell,\x01",
            "But it was quite Sparta, is not it?\x02\x03",
            "#10302FRather than sergeant\x01",
            "I guess it was a demon sergeant.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x109, 0x105, 500)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#11P#10101FThat's right, you\x01",
            "Is it because you only tap down?\x02\x03",
            "#10106FIf I do it I can do it properly\x01",
            "I do not even remember the traffic rules.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F#11PWell, it is also taught strictly\x01",
            "It is necessary qualities for soldiers.\x02\x03",
            "#00300FAnyway, today's cup is\x01",
            "Let 's enjoy professional driving.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00002FAh.\x01",
            "Noel, I beg you to do my best.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    ChrTalk(
        0x109,
        "#10109F#5PYes, please leave it!\x02",
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

    # Function_49_A71D end

    def Function_50_AB99(): pass

    label("Function_50_AB99")

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
            "#11P#00002FOur car ……\x01",
            "Something seems safe.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B058")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ACD2")

    ChrTalk(
        0x109,
        "#6P#10109FIt was good … it is a sense of relief.\x02",
    )

    CloseMessageWindow()

    label("loc_ACD2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AEBF")

    ChrTalk(
        0x105,
        (
            "#6P#10405FHowever,\x01",
            "To some extent to Mayor Dieter,\x01",
            "You had the flexibility, were not you?\x02\x03",
            "#10409FHuh, using it\x01",
            "I do not want to arrest him\x01",
            "Ironic is useful, is not it?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AD90():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_AD90)
    Sleep(50)

    def lambda_ADA0():
        TurnDirection(0x103, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_ADA0)
    Sleep(50)

    def lambda_ADB0():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_ADB0)
    Sleep(50)

    def lambda_ADC0():
        TurnDirection(0x104, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_ADC0)
    Sleep(50)

    def lambda_ADD0():
        TurnDirection(0xF4, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_ADD0)
    Sleep(50)

    def lambda_ADE0():
        TurnDirection(0xF5, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_ADE0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)

    ChrTalk(
        0x102,
        "#12P#00106F… Well, really.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AE95")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AE71")

    ChrTalk(
        0x109,
        "#12P#10101FWaj, you guys ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_AE95")

    label("loc_AE71")


    ChrTalk(
        0x109,
        "#6P#10101FWaj, you guys ……\x02",
    )

    CloseMessageWindow()

    label("loc_AE95")


    ChrTalk(
        0x103,
        "#00211FIt is not stylish … ….\x02",
    )

    CloseMessageWindow()
    Jump("loc_B053")

    label("loc_AEBF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B053")

    ChrTalk(
        0x10A,
        (
            "#6P#00603FHM……\x01",
            "There seems to be no problem.\x02\x03",
            "#00600FBut for sure this car\x01",
            "To some extent former Mayor of Dieter,\x01",
            "Have you heard that you have been flexible?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AF52():
        TurnDirection(0x102, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_AF52)
    Sleep(50)

    def lambda_AF62():
        TurnDirection(0x103, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_AF62)
    Sleep(50)

    def lambda_AF72():
        TurnDirection(0x101, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AF72)
    Sleep(50)

    def lambda_AF82():
        TurnDirection(0x104, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_AF82)
    Sleep(50)

    def lambda_AF92():
        TurnDirection(0xF4, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_AF92)
    Sleep(50)

    def lambda_AFA2():
        TurnDirection(0xF5, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_AFA2)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)

    ChrTalk(
        0x102,
        "#12P#00108FThat's right. …\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B030")

    ChrTalk(
        0x109,
        (
            "#6P#10106F確かにSergey Managerが\x01",
            "I was saying that …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B030")


    ChrTalk(
        0x103,
        "#00211F… … something is ironic.\x02",
    )

    CloseMessageWindow()

    label("loc_B053")

    Jump("loc_B190")

    label("loc_B058")


    ChrTalk(
        0x109,
        (
            "#6P#10104FIt was good … it is a sense of relief.\x02\x03",
            "#10105F…… That reminds me of this car,\x01",
            "To some extent to Mayor Dieter\x01",
            "I had it interchangeable.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B0DA():
        TurnDirection(0x102, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B0DA)
    Sleep(50)

    def lambda_B0EA():
        TurnDirection(0x103, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_B0EA)
    Sleep(50)

    def lambda_B0FA():
        TurnDirection(0x101, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B0FA)
    Sleep(50)

    def lambda_B10A():
        TurnDirection(0x104, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_B10A)
    Sleep(50)

    def lambda_B11A():
        TurnDirection(0xF4, 0x109, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_B11A)
    Sleep(50)

    def lambda_B12A():
        TurnDirection(0xF5, 0x109, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_B12A)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)

    ChrTalk(
        0x102,
        "#12P#00108FThat's right. …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00211F… … something is ironic.\x02",
    )

    CloseMessageWindow()

    label("loc_B190")

    OP_93(0x104, 0x13B, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x104,
        (
            "#00304FWell, regardless of circumstances,\x01",
            "This is also a member of the support department.\x02\x03",
            "#00302FWhether it can be used properly,\x01",
            "Let's check inside.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)

    ChrTalk(
        0x101,
        "#11P#00000FOh, yes.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x23, 1)
    NewScene("e2010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_50_AB99 end

    def Function_51_B252(): pass

    label("Function_51_B252")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B2D8")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00000Fこの先はWest Crossbell Highwayだな。\x02\x03",
            "I have arrangements of devils … ….\x01",
            "Let's finish off the job in the city.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -34230, 0, 4210, 90)
    EventEnd(0x4)
    Return()

    label("loc_B2D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B3A0")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B350")

    ChrTalk(
        0x101,
        (
            "#00000Fこの先はWest Crossbell Highwayだな。\x02\x03",
            "I do not have any particular business,\x01",
            "Let's stop getting out.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_B38C")

    label("loc_B350")


    ChrTalk(
        0x101,
        (
            "#00000FThere is no business in this direction.\x01",
            "Let's stop getting out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B38C")

    SetChrPos(0x0, -34230, 0, 4210, 90)
    EventEnd(0x4)
    Return()

    label("loc_B3A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B417")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001FAnyway now\x01",
            "I have to chase Randy -\x01",
            "It is not the case that it is on a side street.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -34230, 0, 4210, 90)
    EventEnd(0x4)
    Return()

    label("loc_B417")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B47D")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001FIt is not the case that I am out of town right now.\x01",
            "Let's turn back to life.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -34230, 0, 4210, 90)
    EventEnd(0x4)
    Return()

    label("loc_B47D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B512")
    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001FCome this far to the city\x01",
            "I can not leave.\x02\x03",
            "Orchis Tower突入作戦――\x01",
            "You must make it successful at all costs.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -34230, 0, 4210, 90)
    EventEnd(0x4)
    Return()

    label("loc_B512")

    Return()

    # Function_51_B252 end

    def Function_52_B513(): pass

    label("Function_52_B513")

    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B576")

    ChrTalk(
        0x101,
        (
            "#00000FThe key from the inside\x01",
            "It looks like it's taking over.\x02\x03",
            "Do you enter from the front entrance?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_B5D0")

    label("loc_B576")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a lock on the door.\x01",
            "Apparently from the inside\x01",
            "It seems to be locked.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_B5D0")

    TalkEnd(0xFF)
    Return()

    # Function_52_B513 end

    SaveToFile()

Try(main)
