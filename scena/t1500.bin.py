from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t1500.bin",                # FileName
        "t1500",                    # MapName
        "t1500",                    # Location
        0x004D,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x03,                       # PlaceNameNumber
        0x1D,                       # PreInitFunctionIndex
        b'\x00\xff\x03',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 77, 0, 4, 0, 5],
    )

    BuildStringList((
        "t1500",                  # 0
        "Security guard Tony",           # 1
        "Nurse Ada",           # 2
        "Dyson official",         # 3
        "Professor Seyland",         # 4
        "Harold",               # 5
        "Lisha",               # 6
        "Billy",                 # 7
        "A driver",                 # 8
        "Cecil",                 # 9
        "bus",                   # 10
        "Defense Forces soldier",             # 11
        "Defense Forces soldier",             # 12
        "Defense Forces soldier",             # 13
        "Defense Forces soldier",             # 14
        "Cecil",                 # 15
        "Franc",                 # 16
        "car",                     # 17
        "Mercapa machine",         # 18
        "Nurse A",               # 19
        "Nurse B",               # 20
        "Researcher A",               # 21
        "Researcher B",               # 22
        "children",                   # 23
        "Uncle or Mister",               # 24
        "Grandfather",             # 25
        "Granny",             # 26
        "Visitor Customer A",             # 27
        "Visitor Customer B",             # 28
        "Visitor Customer C",             # 29
        "Visitor D",             # 30
        "SE control",                 # 31
        "bt1510",                 # 32
        "Ursula interchange",           # 33
    ))

    ATBonus("ATBonus_7E0", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_8C0", 5, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_8C4", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_8C8", 8, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_8CC", 11, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_8D0", 11, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_8D4", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_8D8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_8DC", 12, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_8A0", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_8A4", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_8A8", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_8AC", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_8B0", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_8B4", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_8B8", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_8BC", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_8E0", 0x0002, 255, 6, 45, 3, 3, 30, 0, "bt1510", 0x00000000, 100, 0, 0, 0,
        (
            ("ms41501.dat", "ms41401.dat", "ms41401.dat", "ms41501.dat", 0, 0, 0, 0, "MonsterBattlePostion_8C0", "MonsterBattlePostion_8A0", "ed7452", "ed7453", "ATBonus_7E0"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch28600.itc",                   # 00
        "chr/ch29800.itc",                   # 01
        "chr/ch20200.itc",                   # 02
        "chr/ch44800.itc",                   # 03
        "chr/ch09300.itc",                   # 04
        "chr/ch03200.itc",                   # 05
        "chr/ch23600.itc",                   # 06
        "chr/ch28300.itc",                   # 07
        "chr/ch05300.itc",                   # 08
    ))

    DeclNpc(4294919736, 0,       4000,    270,  261,  0x0, 0,   0,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(4294944256, 4294966296, 4294941387, 0,    257,  0x0, 0,   1,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(4294937296, 4294966296, 4294946997, 246,  389,  0x0, 0,   2,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(4294945317, 4294966296, 4294941266, 180,  389,  0x0, 0,   3,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(4294918407, 0,       4000,    90,   389,  0x0, 0,   4,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(4294917276, 0,       4294967066, 90,   389,  0x0, 0,   5,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(4294914817, 0,       13199,   180,  385,  0x0, 0,   6,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(4294913206, 0,       11979,   180,  389,  0x0, 0,   7,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(4294943096, 4294966296, 4294942587, 180,  389,  0x0, 0,   8,   0,   0,   0,   0,   95,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 21,  -47.5,                 0.0,                   -1.0,                  225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   15.833333969116211,    -0.0,                  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 27,  -42.0,                 0.0,                   -1.0,                  225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   14.0,                  -0.0,                  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 40,  -47.5,                 0.0,                   -1.0,                  225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   15.833333969116211,    -0.0,                  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 90,  -42.5,                 0.0,                   -1.0,                  225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   14.166666984558105,    -0.0,                  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 92,  -44.75,                0.0,                   -1.0,                  225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   14.916666984558105,    -0.0,                  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 93,  -47.5,                 0.0,                   -1.0,                  225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   15.833333969116211,    -0.0,                  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 94,  -43.75,                0.0,                   -1.0,                  225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   14.583333969116211,    -0.0,                  0.20000000298023224,   1.0])

    DeclActor(4294909296, 0,       4000,    1500,    4294909296, 1500,    4000,    0x007C, 0,  19, 0x0000)
    DeclActor(4294950466, 4294966296, 4294939786, 1200,    4294950116, 4294965296, 4294934526, 0x007C, 0,  20, 0x0000)
    DeclActor(4294917886, 0,       16470,   1200,    4294917886, 2000,    16470,   0x007C, 0,  18, 0x0000)
    DeclActor(4294919296, 0,       17000,   1200,    4294919296, 2000,    17000,   0x007C, 0,  18, 0x0000)
    DeclActor(4294959416, 0,       6560,    1200,    4294959416, 1500,    6560,    0x007C, 0,  98, 0x0000)
    DeclActor(4294930436, 0,       14360,   1200,    4294930436, 1500,    14360,   0x007C, 0,  99, 0x0000)

    PlaceName(-69.0, 0.0, -8.0, 0x0000, 0x0000, "Ursula interchange")
    PlaceName(-23.0, 0.0, 18.0, 0x0000, 0x0052, "")
    PlaceName(-57.900001525878906, 0.0, 4.199999809265137, 0x0000, 0x0055, "")

    ChipFrameInfo(2740, 0)                                       # 0

    ScpFunction((
        "Function_0_AB4",          # 00, 0
        "Function_1_B6C",          # 01, 1
        "Function_2_C24",          # 02, 2
        "Function_3_C85",          # 03, 3
        "Function_4_D00",          # 04, 4
        "Function_5_1432",         # 05, 5
        "Function_6_1757",         # 06, 6
        "Function_7_181B",         # 07, 7
        "Function_8_1948",         # 08, 8
        "Function_9_196F",         # 09, 9
        "Function_10_1A03",        # 0A, 10
        "Function_11_2A74",        # 0B, 11
        "Function_12_369F",        # 0C, 12
        "Function_13_3D2B",        # 0D, 13
        "Function_14_3ECF",        # 0E, 14
        "Function_15_3F88",        # 0F, 15
        "Function_16_4097",        # 10, 16
        "Function_17_431E",        # 11, 17
        "Function_18_43AB",        # 12, 18
        "Function_19_46EE",        # 13, 19
        "Function_20_473A",        # 14, 20
        "Function_21_480E",        # 15, 21
        "Function_22_5476",        # 16, 22
        "Function_23_5486",        # 17, 23
        "Function_24_5499",        # 18, 24
        "Function_25_54AC",        # 19, 25
        "Function_26_54BF",        # 1A, 26
        "Function_27_54D2",        # 1B, 27
        "Function_28_5D66",        # 1C, 28
        "Function_29_5E4A",        # 1D, 29
        "Function_30_5F01",        # 1E, 30
        "Function_31_5FC1",        # 1F, 31
        "Function_32_603D",        # 20, 32
        "Function_33_60AC",        # 21, 33
        "Function_34_60E6",        # 22, 34
        "Function_35_6135",        # 23, 35
        "Function_36_616F",        # 24, 36
        "Function_37_61A9",        # 25, 37
        "Function_38_61F8",        # 26, 38
        "Function_39_6232",        # 27, 39
        "Function_40_626C",        # 28, 40
        "Function_41_6C64",        # 29, 41
        "Function_42_6D7F",        # 2A, 42
        "Function_43_6E1D",        # 2B, 43
        "Function_44_6E49",        # 2C, 44
        "Function_45_6E54",        # 2D, 45
        "Function_46_7559",        # 2E, 46
        "Function_47_757B",        # 2F, 47
        "Function_48_75A0",        # 30, 48
        "Function_49_75C5",        # 31, 49
        "Function_50_75DD",        # 32, 50
        "Function_51_75F5",        # 33, 51
        "Function_52_760D",        # 34, 52
        "Function_53_7625",        # 35, 53
        "Function_54_8DB0",        # 36, 54
        "Function_55_8DDF",        # 37, 55
        "Function_56_8E13",        # 38, 56
        "Function_57_8EA3",        # 39, 57
        "Function_58_8EF1",        # 3A, 58
        "Function_59_8F05",        # 3B, 59
        "Function_60_8F76",        # 3C, 60
        "Function_61_8F85",        # 3D, 61
        "Function_62_900E",        # 3E, 62
        "Function_63_9013",        # 3F, 63
        "Function_64_90B9",        # 40, 64
        "Function_65_90BE",        # 41, 65
        "Function_66_9140",        # 42, 66
        "Function_67_91E7",        # 43, 67
        "Function_68_927E",        # 44, 68
        "Function_69_92A3",        # 45, 69
        "Function_70_92C8",        # 46, 70
        "Function_71_9313",        # 47, 71
        "Function_72_9370",        # 48, 72
        "Function_73_93AA",        # 49, 73
        "Function_74_93BA",        # 4A, 74
        "Function_75_93CD",        # 4B, 75
        "Function_76_93F1",        # 4C, 76
        "Function_77_9415",        # 4D, 77
        "Function_78_9439",        # 4E, 78
        "Function_79_945D",        # 4F, 79
        "Function_80_99D2",        # 50, 80
        "Function_81_9A2D",        # 51, 81
        "Function_82_9A47",        # 52, 82
        "Function_83_9A64",        # 53, 83
        "Function_84_9A81",        # 54, 84
        "Function_85_9A9B",        # 55, 85
        "Function_86_9AB8",        # 56, 86
        "Function_87_9AF5",        # 57, 87
        "Function_88_9AF6",        # 58, 88
        "Function_89_9B11",        # 59, 89
        "Function_90_9B3C",        # 5A, 90
        "Function_91_A83B",        # 5B, 91
        "Function_92_A83C",        # 5C, 92
        "Function_93_B0C1",        # 5D, 93
        "Function_94_B3A5",        # 5E, 94
        "Function_95_BCA2",        # 5F, 95
        "Function_96_C658",        # 60, 96
        "Function_97_D2A0",        # 61, 97
        "Function_98_D342",        # 62, 98
        "Function_99_D398",        # 63, 99
    ))


    def Function_0_AB4(): pass

    label("Function_0_AB4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_AF4"),
        (1, "loc_B00"),
        (2, "loc_B0C"),
        (3, "loc_B18"),
        (4, "loc_B24"),
        (5, "loc_B30"),
        (6, "loc_B3C"),
        (SWITCH_DEFAULT, "loc_B48"),
    )


    label("loc_AF4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_B54")

    label("loc_B00")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_B54")

    label("loc_B0C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_B54")

    label("loc_B18")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_B54")

    label("loc_B24")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_B54")

    label("loc_B30")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_B54")

    label("loc_B3C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_B54")

    label("loc_B48")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_B54")

    label("loc_B54")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B6B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_B54")

    label("loc_B6B")

    Return()

    # Function_0_AB4 end

    def Function_1_B6C(): pass

    label("Function_1_B6C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_BAC"),
        (1, "loc_BB8"),
        (2, "loc_BC4"),
        (3, "loc_BD0"),
        (4, "loc_BDC"),
        (5, "loc_BE8"),
        (6, "loc_BF4"),
        (SWITCH_DEFAULT, "loc_C00"),
    )


    label("loc_BAC")

    OP_A0(0xFE, 450, 0x0, 0xFB)
    Jump("loc_C0C")

    label("loc_BB8")

    OP_A0(0xFE, 550, 0x0, 0xFB)
    Jump("loc_C0C")

    label("loc_BC4")

    OP_A0(0xFE, 600, 0x0, 0xFB)
    Jump("loc_C0C")

    label("loc_BD0")

    OP_A0(0xFE, 400, 0x0, 0xFB)
    Jump("loc_C0C")

    label("loc_BDC")

    OP_A0(0xFE, 650, 0x0, 0xFB)
    Jump("loc_C0C")

    label("loc_BE8")

    OP_A0(0xFE, 350, 0x0, 0xFB)
    Jump("loc_C0C")

    label("loc_BF4")

    OP_A0(0xFE, 500, 0x0, 0xFB)
    Jump("loc_C0C")

    label("loc_C00")

    OP_A0(0xFE, 500, 0x0, 0xFB)
    Jump("loc_C0C")

    label("loc_C0C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C23")
    OP_A0(0xFE, 500, 0x0, 0xFB)
    Jump("loc_C0C")

    label("loc_C23")

    Return()

    # Function_1_B6C end

    def Function_2_C24(): pass

    label("Function_2_C24")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C84")
    OP_95(0xFE, -23040, 0, -6950, 2000, 0x0)
    OP_95(0xFE, -24930, 0, -6950, 2000, 0x0)
    OP_95(0xFE, -24930, -1000, -23250, 2000, 0x0)
    OP_95(0xFE, -23040, -1000, -23250, 2000, 0x0)
    Jump("Function_2_C24")

    label("loc_C84")

    Return()

    # Function_2_C24 end

    def Function_3_C85(): pass

    label("Function_3_C85")

    SetMapObjFlags(0xD, 0x2000000)
    SetMapObjFlags(0x11, 0x2000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_CCC")
    ClearMapObjFlags(0xD, 0x2000000)
    SetMapObjFlags(0x7, 0x2000000)
    SetMapObjFlags(0x8, 0x2000000)
    SetMapObjFlags(0xA, 0x2000000)
    SetMapObjFlags(0xB, 0x2000000)
    SetMapObjFlags(0xC, 0x2000000)
    SetMapObjFlags(0xE, 0x2000000)

    label("loc_CCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_CFF")
    ClearMapObjFlags(0x11, 0x2000000)
    SetMapObjFlags(0x7, 0x2000000)
    SetMapObjFlags(0x8, 0x2000000)
    SetMapObjFlags(0xA, 0x2000000)
    SetMapObjFlags(0xB, 0x2000000)
    SetMapObjFlags(0xC, 0x2000000)
    SetMapObjFlags(0xE, 0x2000000)

    label("loc_CFF")

    Return()

    # Function_3_C85 end

    def Function_4_D00(): pass

    label("Function_4_D00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_D24")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x9, -20070, 0, -3580, 270)
    Jump("loc_E8E")

    label("loc_D24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_D38")
    BeginChrThread(0x9, 0, 0, 2)
    Jump("loc_E8E")

    label("loc_D38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_D4C")
    BeginChrThread(0x9, 0, 0, 2)
    Jump("loc_E8E")

    label("loc_D4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_D65")
    BeginChrThread(0x9, 0, 0, 2)
    ClearChrFlags(0xA, 0x80)
    Jump("loc_E8E")

    label("loc_D65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_DC6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DA6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D9C")
    ClearChrFlags(0xE, 0x80)
    Jump("loc_DA1")

    label("loc_D9C")

    SetChrFlags(0x8, 0x80)

    label("loc_DA1")

    Jump("loc_DAB")

    label("loc_DA6")

    SetChrFlags(0x8, 0x10)

    label("loc_DAB")

    SetChrPos(0x9, -23040, -1000, -25910, 180)
    ClearChrFlags(0xA, 0x80)
    Jump("loc_E8E")

    label("loc_DC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_DD9")
    SetChrFlags(0x9, 0x80)
    Jump("loc_E8E")

    label("loc_DD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_E03")
    BeginChrThread(0x9, 0, 0, 2)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -36570, 3000, 16290, 90)
    Jump("loc_E8E")

    label("loc_E03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_E26")
    BeginChrThread(0x9, 0, 0, 2)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x10)
    Jump("loc_E8E")

    label("loc_E26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_E49")
    SetChrFlags(0x8, 0x10)
    BeginChrThread(0x9, 0, 0, 2)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x10)
    Jump("loc_E8E")

    label("loc_E49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_E74")
    BeginChrThread(0x9, 0, 0, 2)
    ClearChrFlags(0xA, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E6F")
    ClearChrFlags(0xF, 0x80)

    label("loc_E6F")

    Jump("loc_E8E")

    label("loc_E74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_E8E")
    SetChrPos(0x9, -12330, -1000, -17370, 90)

    label("loc_E8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 2)), scpexpr(EXPR_END)), "loc_E9C")
    ClearChrFlags(0xD, 0x80)

    label("loc_E9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_EB0")
    ClearScenarioFlags(0x22, 0)
    Event(0, 41)
    Jump("loc_EED")

    label("loc_EB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_EC7")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x0, 0)
    Event(0, 45)
    Jump("loc_EED")

    label("loc_EC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_EDE")
    ClearScenarioFlags(0x22, 2)
    SetScenarioFlags(0x0, 0)
    Event(0, 53)
    Jump("loc_EED")

    label("loc_EDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_EED")
    ClearScenarioFlags(0x22, 3)
    Event(0, 79)

    label("loc_EED")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1391")
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
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F7A")
    SetScenarioFlags(0x38, 0)

    label("loc_F7A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F90")
    SetScenarioFlags(0x38, 1)

    label("loc_F90")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FA6")
    SetScenarioFlags(0x38, 2)

    label("loc_FA6")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FBC")
    SetScenarioFlags(0x38, 3)

    label("loc_FBC")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FD2")
    SetScenarioFlags(0x38, 4)

    label("loc_FD2")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FE8")
    SetScenarioFlags(0x38, 5)

    label("loc_FE8")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FFE")
    SetScenarioFlags(0x38, 6)

    label("loc_FFE")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1014")
    SetScenarioFlags(0x38, 7)

    label("loc_1014")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_102A")
    SetScenarioFlags(0x39, 0)

    label("loc_102A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1040")
    SetScenarioFlags(0x39, 1)

    label("loc_1040")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1056")
    SetScenarioFlags(0x39, 2)

    label("loc_1056")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_106C")
    SetScenarioFlags(0x39, 3)

    label("loc_106C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1082")
    SetScenarioFlags(0x39, 4)

    label("loc_1082")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1098")
    SetScenarioFlags(0x39, 5)

    label("loc_1098")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10AE")
    SetScenarioFlags(0x39, 6)

    label("loc_10AE")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10C4")
    SetScenarioFlags(0x39, 7)

    label("loc_10C4")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10DA")
    SetScenarioFlags(0x3A, 0)

    label("loc_10DA")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10F0")
    SetScenarioFlags(0x3A, 1)

    label("loc_10F0")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1106")
    SetScenarioFlags(0x3A, 2)

    label("loc_1106")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_111C")
    SetScenarioFlags(0x3A, 3)

    label("loc_111C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1132")
    SetScenarioFlags(0x3A, 4)

    label("loc_1132")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1148")
    SetScenarioFlags(0x3A, 5)

    label("loc_1148")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_115E")
    SetScenarioFlags(0x3A, 6)

    label("loc_115E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1174")
    SetScenarioFlags(0x3A, 7)

    label("loc_1174")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_118A")
    SetScenarioFlags(0x3B, 0)

    label("loc_118A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11A0")
    SetScenarioFlags(0x3B, 1)

    label("loc_11A0")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11B6")
    SetScenarioFlags(0x3B, 2)

    label("loc_11B6")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11CC")
    SetScenarioFlags(0x3B, 3)

    label("loc_11CC")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11E2")
    SetScenarioFlags(0x3B, 4)

    label("loc_11E2")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11F8")
    SetScenarioFlags(0x3B, 5)

    label("loc_11F8")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_120E")
    SetScenarioFlags(0x3B, 6)

    label("loc_120E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1224")
    SetScenarioFlags(0x3B, 7)

    label("loc_1224")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_123A")
    SetScenarioFlags(0x3D, 5)

    label("loc_123A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1250")
    SetScenarioFlags(0x3D, 6)

    label("loc_1250")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1266")
    SetScenarioFlags(0x3D, 7)

    label("loc_1266")

    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12A1")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_1391")

    label("loc_12A1")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12C4")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_1391")

    label("loc_12C4")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12E7")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_1391")

    label("loc_12E7")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_130A")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_1391")

    label("loc_130A")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_132D")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_1391")

    label("loc_132D")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1350")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_1391")

    label("loc_1350")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1373")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_1391")

    label("loc_1373")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1391")
    SetScenarioFlags(0x3C, 7)

    label("loc_1391")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13A7")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13BD")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13EF")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13EF")
    SetChrPos(0x0, -50230, 0, 16410, 270)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    Event(0, 9)

    label("loc_13EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_1422")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1422")
    SetChrPos(0x0, -48000, 0, 17000, 270)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    ClearMapFlags(0x8000000)

    label("loc_1422")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E, 0)), scpexpr(EXPR_END)), "loc_1431")
    ClearScenarioFlags(0x3E, 0)
    Event(0, 8)

    label("loc_1431")

    Return()

    # Function_4_D00 end

    def Function_5_1432(): pass

    label("Function_5_1432")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_144C")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)
    Jump("loc_145E")

    label("loc_144C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_145E")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_145E")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 1)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1484")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_1484")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_149C")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_149C")

    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14B4")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_14B4")

    ModifyEventFlags(0, 3, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14DF")
    ModifyEventFlags(1, 3, 0x80)

    label("loc_14DF")

    ModifyEventFlags(0, 4, 0x80)
    ModifyEventFlags(0, 5, 0x80)
    ModifyEventFlags(0, 6, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_151B")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1516")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1516")
    ModifyEventFlags(1, 6, 0x80)

    label("loc_1516")

    Jump("loc_154C")

    label("loc_151B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_154C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 2)), scpexpr(EXPR_END)), "loc_1537")
    ModifyEventFlags(1, 5, 0x80)
    Jump("loc_154C")

    label("loc_1537")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_154C")
    ModifyEventFlags(1, 4, 0x80)

    label("loc_154C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_15D0")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x6E, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_15D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_15E7")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    Jump("loc_15E7")

    label("loc_15E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_15F5")
    Jump("loc_1697")

    label("loc_15F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_162F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_162A")
    ClearMapObjFlags(0xE, 0x4)
    SetMapObjFrame(0xE, "light", 0x0, 0x1)
    SetMapObjFlags(0xE, 0x1000)

    label("loc_162A")

    Jump("loc_1697")

    label("loc_162F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_163D")
    Jump("loc_1697")

    label("loc_163D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_164B")
    Jump("loc_1697")

    label("loc_164B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1659")
    Jump("loc_1697")

    label("loc_1659")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_166D")
    ClearMapObjFlags(0xB, 0x4)
    Jump("loc_1697")

    label("loc_166D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_168E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1689")
    ClearMapObjFlags(0xA, 0x4)

    label("loc_1689")

    Jump("loc_1697")

    label("loc_168E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1697")

    label("loc_1697")

    MiniGame(0x2F, 0x2, 0x3, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0x11, 0x80)
    SetMapObjFlags(0x7, 0x4)
    LoadEffect(0xF, "eff\\mgm03_02.eff")
    PlayEffect(0xF, 0x8, 0xFF, 0x0, -17180, -2000, -32770, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1734")
    ClearMapObjFlags(0x6, 0x10)
    OP_70(0x6, 0xA)

    label("loc_1734")

    OP_1B(0x0, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_174C")
    OP_1B(0x0, 0x0, 0x61)

    label("loc_174C")

    ClearMapObjFlags(0x6, 0x10)
    OP_70(0x6, 0xA)
    Return()

    # Function_5_1432 end

    def Function_6_1757(): pass

    label("Function_6_1757")

    EventBegin(0x2)
    SetMapFlags(0x8000000)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1Kbus停がある。\x01",
            "busで移動しますか？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Crosbell City South Exit\x01",            # 0
            "Bifurcation stop (near Naka-ku)\x01",      # 1
            "quit\x01",                      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17F3")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1813")

    label("loc_17F3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1813")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("r1530", 0, 0, 0)
    IdleLoop()

    label("loc_1813")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Return()

    # Function_6_1757 end

    def Function_7_181B(): pass

    label("Function_7_181B")

    ClearMapFlags(0x1)
    SetEventSkip(0x0, "loc_1944")
    Fade(500)
    OP_68(-59000, 1000, 2200, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(23000, 0)
    OP_E2(0x1)
    SetChrPos(0x0, -56600, 0, 3800, 180)
    SetChrPos(0x1, -56600, 0, 4900, 180)
    SetChrPos(0x2, -56600, 0, 6000, 180)
    SetChrPos(0x3, -56600, 0, 7200, 180)
    SetMapObjFlags(0x7, 0x1000)
    ClearMapObjFlags(0x7, 0x4)
    ClearChrFlags(0x11, 0x80)
    OP_78(0x7, 0x11)
    SetMapObjFrame(0x7, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x11, -71000, 0, 500, 90)
    OP_D5(0x11, 0x0, 0x15F90, 0x0, 0x0)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0x79, 0xB4, 0x0, 0x20)

    def lambda_18FB():
        OP_95(0xFE, -59000, 0, 500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_18FB)
    OP_0D()
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0x11, 1)
    OP_71(0x7, 0x5B, 0x78, 0x1, 0x0)
    OP_79(0x7)
    Sleep(300)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetEventSkip(0x1, 0x0)

    label("loc_1944")

    SetScenarioFlags(0x3E, 0)
    Return()

    # Function_7_181B end

    def Function_8_1948(): pass

    label("Function_8_1948")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetChrPos(0x0, -56560, 0, 4080, 180)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_8_1948 end

    def Function_9_196F(): pass

    label("Function_9_196F")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_19CA")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_19BF")
    Sound(2502, 255, 100, 0)
    Jump("loc_19C5")

    label("loc_19BF")

    Sound(2503, 255, 100, 0)

    label("loc_19C5")

    Jump("loc_19EE")

    label("loc_19CA")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_19E8")
    Sound(3347, 255, 100, 0)
    Jump("loc_19EE")

    label("loc_19E8")

    Sound(3348, 255, 100, 0)

    label("loc_19EE")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_196F end

    def Function_10_1A03(): pass

    label("Function_10_1A03")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1B5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AD8")

    ChrTalk(
        0x8,
        (
            "Hey … … that that glows pale\x01",
            "What is a huge tree?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Something like that suddenly appears …\x01",
            "I do not understand anything at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And, please put your fight in anyway\x01",
            "I have to guard it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1B58")

    label("loc_1AD8")


    ChrTalk(
        0x8,
        (
            "Suddenly such a huge tree appears suddenly …\x01",
            "I do not understand anything at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "And, please put your fight in anyway\x01",
            "I have to guard it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B58")

    Jump("loc_2A70")

    label("loc_1B5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1C9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C0B")

    ChrTalk(
        0x8,
        (
            "Under the influence of the invalid declaration of the independent country,\x01",
            "Defense forces seem to be confused.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "救急carやbusの護衛は\x01",
            "I am continuing for now,\x01",
            "After all I am worried about various things.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C96")

    label("loc_1C0B")


    ChrTalk(
        0x8,
        (
            "With the invalid declaration of the example,\x01",
            "Defense forces seem to be confused.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Without the escort of Defense Forces\x01",
            "救急carの行き来もできないし、\x01",
            "Do not become uneasy about various things.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C96")

    Jump("loc_2A70")

    label("loc_1C9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_1E23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D8F")

    ChrTalk(
        0x8,
        (
            "Without the escort of Defense Forces\x01",
            "救急carも行き来できないのは\x01",
            "To be honest, it's a bad situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "\"Phantom beast\" that came out on the highway,\x01",
            "Movement restriction by defense force … …\x01",
            "These two are big problems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "At least, to escort the highway\x01",
            "I want you to devote some more people.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E1E")

    label("loc_1D8F")


    ChrTalk(
        0x8,
        (
            "Without the escort of Defense Forces\x01",
            "救急carも行き来できないのは\x01",
            "To be honest, it's a bad situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "At the very least the defense army escorted the highway\x01",
            "I want you to devote some more people.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E1E")

    Jump("loc_2A70")

    label("loc_1E23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1F9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F08")

    ChrTalk(
        0x8,
        (
            "The guards from the Defense Forces, from the detention center\x01",
            "I was searching for fugitives and others … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Somehow somewhat\x01",
            "It seems I got raised.\x01",
            "What on earth did you do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, whatever.\x01",
            "I have to go back to security for the time being.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1F97")

    label("loc_1F08")


    ChrTalk(
        0x8,
        (
            "The guards from the Defense Forces, from the detention center\x01",
            "I came to search for escapists\x01",
            "I pulled it up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, whatever.\x01",
            "I have to go back to security for the time being.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F97")

    Jump("loc_2A70")

    label("loc_1F9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2324")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21D4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2130")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_209B")

    ChrTalk(
        0x8,
        (
            "Well, medical supplies\x01",
            "Let's take cheat,\x01",
            "There is a bad guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Because I could retrieve it for the time being\x01",
            "Though it was nice …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "When everyone is working hard\x01",
            "Listening to that story,\x01",
            "I will be sad.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_212B")

    label("loc_209B")


    ChrTalk(
        0x8,
        (
            "Well, medical supplies\x01",
            "Let's take cheat,\x01",
            "You have bad guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "When everyone is working hard\x01",
            "Listening to that story,\x01",
            "I will be sad.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_212B")

    Jump("loc_21CF")

    label("loc_2130")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_21CF")

    ChrTalk(
        0x8,
        (
            "Well, medical supplies\x01",
            "To take cheat,\x01",
            "There is a bad guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even though there are people in need\x01",
            "To do such a thing,\x01",
            "It is the lowest as a human being.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21CF")

    label("loc_21CF")

    Jump("loc_231F")

    label("loc_21D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22A6")

    ChrTalk(
        0x8,
        (
            "I am sorry,\x01",
            "Even if I arrived long ago\x01",
            "It is good time, but ….\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x0, 500)

    ChrTalk(
        0x8,
        (
            "Oops, excuse me,\x01",
            "Welcome to Ursula Medical University.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you are in hospital,\x01",
            "In the lobby on the 1st floor of the ward\x01",
            "I will ask the procedure.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 1)
    Jump("loc_231F")

    label("loc_22A6")


    ChrTalk(
        0x8,
        (
            "In the case of raids during this time\x01",
            "The patient has increased dramatically.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Teachers in the hospital\x01",
            "I am trying to be very busy.\x01",
            "I must do my best too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_231F")

    Jump("loc_2A70")

    label("loc_2324")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_249E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_240E")

    ChrTalk(
        0x8,
        (
            "Yeah, it's raining today.\x01",
            "Security is hard on such occasions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even so,\x01",
            "昨日はたくさん救急carが来て\x01",
            "It was serious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It seems that it was a very fancy accident,\x01",
            "The victims did not appear\x01",
            "There is no choice but to be a miracle.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2499")

    label("loc_240E")


    ChrTalk(
        0x8,
        (
            "昨日はたくさん救急carが来て\x01",
            "It was serious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It seems that it was a very fancy accident,\x01",
            "The victims did not appear\x01",
            "There is no choice but to be a miracle.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2499")

    Jump("loc_2A70")

    label("loc_249E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_252B")

    ChrTalk(
        0x8,
        (
            "Hurricane men\x01",
            "You seem to be investigating various places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I do not expect large monsters to come out\x01",
            "There seems to be rumors … ….\x01",
            "I should also be careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A70")

    label("loc_252B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2665")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25FD")

    ChrTalk(
        0x8,
        "や、Welcome to Ursula Medical University.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "さっき、Professor Seylandが\x01",
            "I walked to the rest area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Professor, often at that place recently\x01",
            "It seems to be standing.\x01",
            "…… There must be various thoughts.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2660")

    label("loc_25FD")


    ChrTalk(
        0x8,
        (
            "Professor Seyland、最近よく\x01",
            "It is appearing at the resting place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "…… There must be various thoughts.\x02",
    )

    CloseMessageWindow()

    label("loc_2660")

    Jump("loc_2A70")

    label("loc_2665")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_26F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2680")
    Call(0, 15)
    Jump("loc_26F1")

    label("loc_2680")


    ChrTalk(
        0x8,
        (
            "Oh, that time\x01",
            "Shillong's mistake in writing\x01",
            "Because it seems to be the cause … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Tentatively this time\x01",
            "I do not think there is any problem.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26F1")

    Jump("loc_2A70")

    label("loc_26F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_28F9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2791")

    ChrTalk(
        0x8,
        (
            "The limousine of the Grand Duke of Albert\x01",
            "I got home earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh yeah, I was nervous, but …\x01",
            "It is something that I can welcome properly\x01",
            "It was good to be able to do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28F4")

    label("loc_2791")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2869")

    ChrTalk(
        0x8,
        (
            "Remilia's Albert Grand Duke,\x01",
            "I'm visiting you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh yeah, I heard the story beforehand\x01",
            "When it comes to greeting\x01",
            "It is frustrating to be nervous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Until you come back,\x01",
            "I have to try not to be rude.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_28F4")

    label("loc_2869")


    ChrTalk(
        0x8,
        (
            "Oh yeah, I heard the story beforehand\x01",
            "When it comes to greeting\x01",
            "It is frustrating to be nervous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "大公がUntil you come back,\x01",
            "I have to try not to be rude.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28F4")

    Jump("loc_2A70")

    label("loc_28F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2A70")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29D3")

    ChrTalk(
        0x8,
        (
            "Hello.\x01",
            "This is St. Ursula Medical University Hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Because it is long, \"Ursula hospital\"\x01",
            "Many people abbreviate \"Ursula Medical University.\"\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oops, if it is reception of medical treatment and sympathy\x01",
            "I'm a building in the back.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A70")

    label("loc_29D3")


    ChrTalk(
        0x8,
        (
            "The wounds shot by the gun at the time of the case incident,\x01",
            "Clearly refreshing to the teacher here\x01",
            "I was cured.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ursula Medical University's proud medical technology\x01",
            "It is exactly great! … What kind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A70")

    TalkEnd(0xFE)
    Return()

    # Function_10_1A03 end

    def Function_11_2A74(): pass

    label("Function_11_2A74")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2C47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B94")

    ChrTalk(
        0x9,
        (
            "Defense forces to and from the highway\x01",
            "救急carやbusの護衛に\x01",
            "You seem to have turned our hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "People who were injured due to the disturbance in the city,\x01",
            "People who did not attend the hospital for a while\x01",
            "I got to come by Oita.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Mr. Eolia, a hawker\x01",
            "He came to help me,\x01",
            "I wonder at the hospital for a while.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2C42")

    label("loc_2B94")


    ChrTalk(
        0x9,
        (
            "Mr. Eolia, a hawker\x01",
            "He came to help me,\x01",
            "I wonder at the hospital for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "But, such a huge tree appeared,\x01",
            "Anxiety has spread to the patients.\x01",
            "I have to work hard to the utmost.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C42")

    Jump("loc_369B")

    label("loc_2C47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2DA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D1F")

    ChrTalk(
        0x9,
        (
            "The patients hospitalized,\x01",
            "My family in the city seems to be very worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "From here it can not contact Lok\x01",
            "It can not be helped because it is a situation … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Somehow the patient's anxiety\x01",
            "I have to relax.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2D9B")

    label("loc_2D1F")


    ChrTalk(
        0x9,
        (
            "The patients hospitalized,\x01",
            "My family in the city seems to be very worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Somehow the patient's anxiety\x01",
            "I have to relax.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D9B")

    Jump("loc_369B")

    label("loc_2DA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_2EC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E57")

    ChrTalk(
        0x9,
        (
            "From the Defense Forces and the president,\x01",
            "My brother respects my will.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Be sure to be safe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "それと、Cecil先輩に\x01",
            "Do not worry too much.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2EBD")

    label("loc_2E57")


    ChrTalk(
        0x9,
        (
            "My brother,\x01",
            "Be sure to be safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "それと、Cecil先輩に\x01",
            "Do not worry too much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EBD")

    Jump("loc_369B")

    label("loc_2EC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2FD7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F99")

    ChrTalk(
        0x9,
        (
            "My brother, you guys and the defense army\x01",
            "It seems I was fighting … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "……No,\x01",
            "After all not to mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "No matter what happens,\x01",
            "We are on your side with your brother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F……Thank you.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2FD2")

    label("loc_2F99")


    ChrTalk(
        0x9,
        (
            "No matter what happens,\x01",
            "We are on your side with your brother.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FD2")

    Jump("loc_369B")

    label("loc_2FD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3076")

    ChrTalk(
        0x9,
        (
            "A substantial number of cases in that incident\x01",
            "The patient was brought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I could not catch up with treatment as well ……\x01",
            "People who need surgery\x01",
            "A lot of people are waiting for your turn.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_369B")

    label("loc_3076")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3084")
    Jump("loc_369B")

    label("loc_3084")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_31A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_315D")

    ChrTalk(
        0x9,
        (
            "Shizuku, this surgery\x01",
            "She seems to be looking forward positively.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "That girl has not given up,\x01",
            "We are in the surroundings\x01",
            "You should not become pessimistic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "… Well, we also\x01",
            "I must believe and have a hard time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_319F")

    label("loc_315D")


    ChrTalk(
        0x9,
        (
            "Us too\x01",
            "Believe in the cure of Shizuoka,\x01",
            "I have to work hard.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_319F")

    Jump("loc_369B")

    label("loc_31A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_329C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_324D")

    ChrTalk(
        0x9,
        (
            "Professor Seylandだから\x01",
            "The operation until then\x01",
            "I can say that I could do it … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Shizuoka … ….\x01",
            "After all it is now medical technology\x01",
            "I wonder if it can not be cured completely.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3297")

    label("loc_324D")


    ChrTalk(
        0x9,
        (
            "Shizuoka … ….\x01",
            "After all it is now medical technology\x01",
            "I wonder if it can not be cured completely.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3297")

    Jump("loc_369B")

    label("loc_329C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_33B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3339")

    ChrTalk(
        0x9,
        (
            "Today it's time for a trade meeting\x01",
            "It seems that the plenary session will be held.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I wonder what kind of meeting it will be.\x01",
            "I have to check it properly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_33B1")

    label("loc_3339")


    ChrTalk(
        0x9,
        (
            "Philia and the orchid\x01",
            "I did not seem to be interested … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I wonder what kind of meeting it will be.\x01",
            "I have to check it properly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33B1")

    Jump("loc_369B")

    label("loc_33B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3509")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34A4")

    ChrTalk(
        0x9,
        (
            "A while ago, Albert Grand Duke\x01",
            "I bother to express my gratitude.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "He is the head of a country,\x01",
            "I wish he was a great boy, why\x01",
            "Although I thought without permission ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "To one nurse like me\x01",
            "To say honestly,\x01",
            "It seems surprisingly frank person.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3504")

    label("loc_34A4")


    ChrTalk(
        0x9,
        (
            "Albert Okoko\x01",
            "It seems surprisingly frank person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Giggle\x01",
            "I got a close affinity at once.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3504")

    Jump("loc_369B")

    label("loc_3509")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_369B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_364E")

    ChrTalk(
        0x9,
        (
            "Oh, my brother to Randy.\x01",
            "It's been a while ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(\"My younger brother\"? ….\x01",
            "I'm sure it has settled. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FHa ha, Ada-chan,\x01",
            "Have you made doing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Yes, both run and Philia\x01",
            "As usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You also have new members\x01",
            "It seems that it has increased ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If there is a chance\x01",
            "Let's play again next time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x159, 4)
    Jump("loc_369B")

    label("loc_364E")


    ChrTalk(
        0x9,
        "Hehe, I am glad to see you again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If there is a chance\x01",
            "Let's play again next time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_369B")

    TalkEnd(0xFE)
    Return()

    # Function_11_2A74 end

    def Function_12_369F(): pass

    label("Function_12_369F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_36B0")
    Jump("loc_3D27")

    label("loc_36B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_36BE")
    Jump("loc_3D27")

    label("loc_36BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_36CC")
    Jump("loc_3D27")

    label("loc_36CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_384A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37B9")

    ChrTalk(
        0xA,
        (
            "Many of the equipment used in hospitals,\x01",
            "Haroldさんという商人と\x01",
            "I mainly traded, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Now it is exclusively for the military supplies\x01",
            "In a situation that we rely on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I can not say that it is not very good quality,\x01",
            "In this situation it can not be helped.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3845")

    label("loc_37B9")


    ChrTalk(
        0xA,
        (
            "今、Many of the equipment used in hospitals,\x01",
            "国防軍の支給品にIn a situation that we rely on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I can not say that it is not very good quality,\x01",
            "In this situation it can not be helped.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3845")

    Jump("loc_3D27")

    label("loc_384A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_39D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3950")

    ChrTalk(
        0xA,
        (
            "Crossbell City 's assault is,\x01",
            "A truly ridiculous incident\x01",
            "It's what has happened ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Although it is nearly a week since that,\x01",
            "I can not wipe away the shocks yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Although reconstruction is progressing,\x01",
            "Crossbell has to recover\x01",
            "Is it possible to do …?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_39CD")

    label("loc_3950")


    ChrTalk(
        0xA,
        (
            "Although reconstruction is progressing,\x01",
            "The shock of the raid incident\x01",
            "I think that it is really big.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Crossbell has to recover\x01",
            "Is it possible to do …?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39CD")

    Jump("loc_3D27")

    label("loc_39D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_39E0")
    Jump("loc_3D27")

    label("loc_39E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3A55")

    ChrTalk(
        0xA,
        (
            "This container ……\x01",
            "An amulet doll from inside\x01",
            "Please come out well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "……why\x01",
            "Is there such a thing?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D27")

    label("loc_3A55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3B81")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B1E")

    ChrTalk(
        0xA,
        (
            "On the topic of independent advocacy in town\x01",
            "All right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "As residents of Crossbell,\x01",
            "In a way it can also be said as a desire\x01",
            "That's why.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I also want to be independent\x01",
            "I would like to agree.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3B7C")

    label("loc_3B1E")


    ChrTalk(
        0xA,
        (
            "I also want to be independent\x01",
            "I would like to agree.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "For referendums\x01",
            "Do not forget to join.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B7C")

    Jump("loc_3D27")

    label("loc_3B81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3B8F")
    Jump("loc_3D27")

    label("loc_3B8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3D1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C81")

    ChrTalk(
        0xA,
        (
            "In the Prime Minister of Remifferia,\x01",
            "Daikyo is in medical field\x01",
            "Especially it seems to put effort.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Remicheria, medical advanced country.\x01",
            "You have heard of it, have not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Hmm, if I lived in such a country\x01",
            "Even if you do not worry about sickness\x01",
            "Looks nice.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3D19")

    label("loc_3C81")


    ChrTalk(
        0xA,
        (
            "In the Prime Minister of Remifferia,\x01",
            "Daikyo is in medical field\x01",
            "Especially it seems to put effort.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Hmm, if I lived in such a country\x01",
            "Even if you do not worry about sickness\x01",
            "Looks nice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D19")

    Jump("loc_3D27")

    label("loc_3D1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3D27")

    label("loc_3D27")

    TalkEnd(0xFE)
    Return()

    # Function_12_369F end

    def Function_13_3D2B(): pass

    label("Function_13_3D2B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E71")

    ChrTalk(
        0xB,
        "……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FProfessor Seyland……？\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xB, 0x0, 500)

    ChrTalk(
        0xB,
        "…… Oh, you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I am bad but I am busy now.\x01",
            "Will you leave me alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F(After all, Shizuku-chan's\x01",
            "I wonder because of surgery … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(Oh, the surgeon\x01",
            "I told you she was … …)\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0xB4, 0x0)
    SetScenarioFlags(0x0, 4)
    Jump("loc_3ECB")

    label("loc_3E71")


    ChrTalk(
        0xB,
        "……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FIt looks like he is thinking.\x01",
            "… … Do not bother me. )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3ECB")

    TalkEnd(0xFE)
    Return()

    # Function_13_3D2B end

    def Function_14_3ECF(): pass

    label("Function_14_3ECF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EE4")
    Call(0, 15)
    Jump("loc_3F84")

    label("loc_3EE4")


    ChrTalk(
        0xC,
        (
            "#03605Fby the way……\x01",
            "The number of sheets of this time is\x01",
            "Was it 30 good?\x02\x03",
            "#03600FPreviously, 50 pieces\x01",
            "It has been ordered with 500 sheets\x01",
            "There was, and just to be sure ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F84")

    TalkEnd(0xFE)
    Return()

    # Function_14_3ECF end

    def Function_15_3F88(): pass

    label("Function_15_3F88")

    OP_4B(0x8, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0x8,
        (
            "や、Haroldさんじゃないか。\x01",
            "What are you doing today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#03600FYeah, I ordered the sheets\x01",
            "I got to the delivery.\x02\x03",
            "I'd like to deliver it immediately ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, then a bit\x01",
            "I guess I'll help bring in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#03609FHaha, Always sorry.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    OP_4C(0x8, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_15_3F88 end

    def Function_16_4097(): pass

    label("Function_16_4097")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_41D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4166")

    ChrTalk(
        0xFE,
        (
            "Thanks to medical supplies\x01",
            "I was able to deliver it safely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even so ……\x01",
            "In this crossbell emergency,\x01",
            "There was a bad guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Wait, for being caught\x01",
            "I was relieved.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_41CE")

    label("loc_4166")


    ChrTalk(
        0xFE,
        (
            "In this crossbell emergency,\x01",
            "There was a bad guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Wait, for being caught\x01",
            "I was relieved.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41CE")

    Jump("loc_431A")

    label("loc_41D3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_431A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42AA")

    ChrTalk(
        0xFE,
        (
            "Damn, in this emergency\x01",
            "I can not deliver medical supplies ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… No, that's it\x01",
            "Even if I say Ujiji?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Without worrying about you,\x01",
            "Switch your head and work.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_431A")

    label("loc_42AA")


    ChrTalk(
        0xFE,
        (
            "Things that have ended\x01",
            "It can not be helped even if you say Ujiji.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Without worrying about you,\x01",
            "Switch your head and work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_431A")

    TalkEnd(0xFE)
    Return()

    # Function_16_4097 end

    def Function_17_431E(): pass

    label("Function_17_431E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_43A7")

    ChrTalk(
        0xF,
        (
            "This is Albert Daimyo\x01",
            "It is a limousine for a shuttle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Mr. Arios was\x01",
            "I am on escorts,\x01",
            "We are safe too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43A7")

    TalkEnd(0xFE)
    Return()

    # Function_17_431E end

    def Function_18_43AB(): pass

    label("Function_18_43AB")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_43DD")
    SetScenarioFlags(0x31, 2)

    label("loc_43DD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4423")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_441D")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4412")
    Sound(2499, 255, 100, 0)
    Jump("loc_4418")

    label("loc_4412")

    Sound(3537, 255, 100, 0)

    label("loc_4418")

    Jump("loc_4423")

    label("loc_441D")

    Sound(3344, 255, 100, 0)

    label("loc_4423")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_449C")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "Board Mercapa")
    MenuCmd(1, 0, "quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_447C"),
        (SWITCH_DEFAULT, "loc_448D"),
    )


    label("loc_447C")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_4497")

    label("loc_448D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4497")

    Jump("loc_46DB")

    label("loc_449C")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "導力carで移動する")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_44D0")
    MenuCmd(1, 0, "導力carで休憩する")

    label("loc_44D0")

    MenuCmd(1, 0, "quit")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4504"),
        (1, "loc_4608"),
        (2, "loc_4699"),
        (SWITCH_DEFAULT, "loc_46D1"),
    )


    label("loc_4504")

    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    OP_74(0x8, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_4535")
    OP_70(0x8, 0x12C)
    OP_71(0x8, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_4545")

    label("loc_4535")

    OP_70(0x8, 0xF0)
    OP_71(0x8, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_4545")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_459B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_459B")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45BE")
    Sound(461, 0, 100, 0)

    label("loc_45BE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_45DE")
    OP_70(0x8, 0x14A)
    OP_71(0x8, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_45EE")

    label("loc_45DE")

    OP_70(0x8, 0x10E)
    OP_71(0x8, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_45EE")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x8, "light", 0x1, 0x1)
    OP_70(0x8, 0x0)
    Jump("loc_4423")

    label("loc_4608")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_467A")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_463D")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_4655")

    label("loc_463D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_4650")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_4655")

    label("loc_4650")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_4655")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4694")

    label("loc_467A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_468A")
    OP_AF(0xFB)
    Jump("loc_4694")

    label("loc_468A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4694")

    Jump("loc_46DB")

    label("loc_4699")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46B2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_46CC")

    label("loc_46B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_46C2")
    OP_AF(0xFB)
    Jump("loc_46CC")

    label("loc_46C2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_46CC")

    Jump("loc_46DB")

    label("loc_46D1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_46DB")

    Jump("loc_4423")

    label("loc_46E0")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_18_43AB end

    def Function_19_46EE(): pass

    label("Function_19_46EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4736")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "導力busは運行を見合わせているようだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    label("loc_4736")

    Call(0, 6)
    Return()

    # Function_19_46EE end

    def Function_20_473A(): pass

    label("Function_20_473A")

    EventBegin(0x1)
    Sound(2094, 255, 100, 0)

    ChrTalk(
        0x101,
        "#0000FI'm going to catch you here.\x02",
    )

    CloseMessageWindow()
    OP_68(-17220, 0, -31290, 1500)
    MoveCamera(60, 36, 0, 1500)
    OP_6E(500, 1500)
    SetCameraDistance(22000, 1500)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4809")
    OP_E2(0x2)
    MiniGame(0x6, 0x11, 0xFFFFBFBE, 0xFFFFFC18, 0xFFFF9A5C, 0xB4, 0xFFFFBCE4, 0xFFFFF830, 0xFFFF7FFE)

    label("loc_4809")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_20_473A end

    def Function_21_480E(): pass

    label("Function_21_480E")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(803)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    SetChrPos(0x101, -47420, 0, 290, 270)
    SetChrPos(0x102, -46710, 0, -820, 270)
    SetChrPos(0x104, -46010, 0, 1050, 270)
    SetChrPos(0x105, -44880, 0, -1000, 270)
    SetChrPos(0x109, -44460, 0, 420, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_68(-45000, 1000, 0, 0)
    MoveCamera(33, 22, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21160, 0)
    OP_68(-54310, 1000, 260, 4500)
    BeginChrThread(0x101, 0, 0, 22)
    BeginChrThread(0x102, 0, 0, 23)
    BeginChrThread(0x104, 0, 0, 24)
    BeginChrThread(0x105, 0, 0, 25)
    BeginChrThread(0x109, 0, 0, 26)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(3000)
    Sound(803, 2, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    WaitChrThread(0x101, 0)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00005F#5POops ……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 0)

    def lambda_4994():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_4994)

    ChrTalk(
        0x102,
        "#00105F#12PDo you contact other departments?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    OP_24(0x323)
    Sound(804, 0, 100, 0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    Sound(2084, 255, 100, 0)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00000F#30WYes, Special Affairs Support Division,\x01",
            "It is Lloyd · Bannings.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Sturdy voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Uhufu ….\x01",
            "You, my friend.\x02\x03",
            "I wonder who they are?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00012FMr. Michelle ……\x01",
            "Well, what is wrong?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice of Michelle")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Uhufu, I do not understand it with a single shot\x01",
            "You are quite clear.\x02\x03",
            "Or maybe you can make a love?\x02",
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
            "#00006FNo, except Mr. Michelle\x01",
            "Just because the corresponding person did not think of it.\x02\x03",
            "#00000FI'm guessing that.\x01",
            "Do you mean Kea?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice of Michelle")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Oh, that's it.\x02\x03",
            "With that child, Shizuku-chan\x01",
            "I went to play in the port area.\x02\x03",
            "I wonder if it was a zeitge?\x01",
            "Because that police dog was together\x01",
            "I think it's all right.\x02",
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
            "#00002FOh, if Zeit is with you\x01",
            "I do not need any worries.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice of Michelle")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Oh, after all?\x02\x03",
            "I was listening to the story,\x01",
            "There are tremendous dignity everywhere.\x02\x03",
            "Truly a legendary \"god of war\"\x01",
            "There is nothing left to be told.\x02",
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
            "#00004FHa ha …… Truly a legendary wolf\x01",
            "I think that it is different thing.\x02\x03",
            "#00005FOh, bother to say that\x01",
            "Did you inform me?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice of Michelle")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No, this is the main theme.\x02\x03",
            "Actually, Arios with you\x01",
            "They seem to want to exchange information.\x02\x03",
            "I will come back around the evening\x01",
            "I wonder if I can get some time?\x02",
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
            "#00000FIs it evening …?\x01",
            "Would it be ok if that was it.\x02\x03",
            "To exchange information,\x01",
            "Is it about the trade meeting again?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice of Michelle")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I have it, though …\x01",
            "About \"black moon\" and \"red constellation\".\x02",
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
            "#00003F……I understand.\x02\x03",
            "#00001FOnce you have done errands\x01",
            "I will visit there.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice of Michelle")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Well, I'll be waiting.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)

    ChrTalk(
        0x102,
        (
            "#00100F#12PAssociation of Zuidori\x01",
            "I heard from Mr. Michelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305F#11PDid something happen?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        "#00006F#5PNo, it is an offer to exchange information.\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd is concerned about the matter of Michelle\x01",
            "I explained to other members.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00303F#11P\"Black moon\" and \"red constellation\" ……\x02\x03",
            "#00301FIf Aosri is an Arios certainly\x01",
            "It seems to be detailed in the information outside autonomous province.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#11PIt may be a boat for migration.\x02\x03",
            "#10300FWell then from now\x01",
            "Will you go back to Cros Bell City?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#5PNo, Mr. Arios\x01",
            "It seems to be the evening to come back.\x02\x03",
            "Until then, I will do this errand\x01",
            "Even if it's done, it will be okay.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5370")

    ChrTalk(
        0x102,
        (
            "#00104F#12PInformation on \"Red constellation\"\x01",
            "Although it was gathered together, ….\x02\x03",
            "#00102Fせっかくcarがあるから\x01",
            "It looks nice to go around a lot yet.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53EC")

    label("loc_5370")


    ChrTalk(
        0x102,
        (
            "#00103F#12PInformation on \"Red constellation\"\x01",
            "I have not gathered so much ……\x02\x03",
            "#00100Fせっかくcarがあるから\x01",
            "It looks nice to try around.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53EC")


    ChrTalk(
        0x109,
        (
            "#10100F#11PWell then, if you do errands\x01",
            "Let's go to the east street guild.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    SetChrPos(0x0, -55000, 0, -250, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x140, 2)
    OP_29(0xA3, 0x1, 0x6)
    ModifyEventFlags(0, 0, 0x80)
    OP_24(0x323)
    EventEnd(0x5)
    Return()

    # Function_21_480E end

    def Function_22_5476(): pass

    label("Function_22_5476")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_22_5476 end

    def Function_23_5486(): pass

    label("Function_23_5486")

    Sleep(50)
    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_23_5486 end

    def Function_24_5499(): pass

    label("Function_24_5499")

    Sleep(100)
    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_24_5499 end

    def Function_25_54AC(): pass

    label("Function_25_54AC")

    Sleep(150)
    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_25_54AC end

    def Function_26_54BF(): pass

    label("Function_26_54BF")

    Sleep(200)
    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_26_54BF end

    def Function_27_54D2(): pass

    label("Function_27_54D2")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch29700.itc", 0x1E)
    LoadChrToIndex("chr/ch29900.itc", 0x20)
    LoadChrToIndex("chr/ch29400.itc", 0x21)
    LoadChrToIndex("chr/ch32800.itc", 0x22)
    LoadChrToIndex("chr/ch23000.itc", 0x23)
    LoadChrToIndex("chr/ch21000.itc", 0x24)
    LoadChrToIndex("chr/ch20000.itc", 0x25)
    LoadChrToIndex("chr/ch23300.itc", 0x26)
    LoadChrToIndex("chr/ch20400.itc", 0x27)
    LoadChrToIndex("chr/ch21200.itc", 0x28)
    LoadChrToIndex("chr/ch20900.itc", 0x29)
    LoadChrToIndex("chr/ch20500.itc", 0x2A)
    SetChrChipByIndex(0x1A, 0x1E)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x20)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1C, 0x21)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1D, 0x22)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1E, 0x23)
    SetChrSubChip(0x1E, 0x0)
    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x24)
    SetChrSubChip(0x1F, 0x0)
    ClearChrFlags(0x1F, 0x80)
    SetChrFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0x25)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0x26)
    SetChrSubChip(0x21, 0x0)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x8000)
    SetChrChipByIndex(0x22, 0x27)
    SetChrSubChip(0x22, 0x0)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8000)
    SetChrChipByIndex(0x23, 0x28)
    SetChrSubChip(0x23, 0x0)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x8000)
    SetChrChipByIndex(0x24, 0x29)
    SetChrSubChip(0x24, 0x0)
    ClearChrFlags(0x24, 0x80)
    SetChrFlags(0x24, 0x8000)
    SetChrChipByIndex(0x25, 0x2A)
    SetChrSubChip(0x25, 0x0)
    ClearChrFlags(0x25, 0x80)
    SetChrFlags(0x25, 0x8000)
    SetMapObjFlags(0x1, 0x1000)
    SetMapObjFlags(0x2, 0x1000)
    OP_68(-18000, 6000, 1300, 0)
    MoveCamera(55, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(33000, 0)
    OP_68(-18000, 1000, 1300, 10000)
    MoveCamera(45, 25, 0, 10000)
    SetCameraDistance(35000, 10000)
    SetChrPos(0x1A, -5000, 1000, -1750, 270)
    OP_A7(0x1A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x1B, 5000, 1000, 1750, 270)
    OP_A7(0x1B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x1C, -24000, 0, 14000, 180)
    OP_A7(0x1C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x1D, -24000, 0, -7000, 180)
    SetChrPos(0x1E, -16500, 0, -500, 90)
    SetChrPos(0x1F, -17000, 0, 500, 90)
    SetChrPos(0x20, -22000, 0, 0, 90)
    SetChrPos(0x21, -25500, 0, -300, 90)
    SetChrPos(0x22, -34000, 0, 700, 90)
    SetChrPos(0x23, -38000, 0, -500, 90)
    SetChrPos(0x24, -37500, 0, 500, 90)
    SetChrPos(0x25, -40000, 0, -750, 90)
    BeginChrThread(0x1A, 1, 0, 28)
    BeginChrThread(0x1C, 1, 0, 30)
    BeginChrThread(0x1E, 1, 0, 32)
    BeginChrThread(0x1F, 1, 0, 33)
    BeginChrThread(0x20, 1, 0, 34)
    BeginChrThread(0x21, 1, 0, 35)
    BeginChrThread(0x22, 1, 0, 36)
    BeginChrThread(0x23, 1, 0, 37)
    BeginChrThread(0x24, 1, 0, 38)
    BeginChrThread(0x25, 1, 0, 39)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    EndChrThread(0x1A, 0x1)
    EndChrThread(0x1B, 0x1)
    EndChrThread(0x1C, 0x1)
    EndChrThread(0x1D, 0x1)
    EndChrThread(0x1E, 0x1)
    EndChrThread(0x1F, 0x1)
    EndChrThread(0x20, 0x1)
    EndChrThread(0x21, 0x1)
    EndChrThread(0x22, 0x1)
    EndChrThread(0x23, 0x1)
    EndChrThread(0x24, 0x1)
    EndChrThread(0x25, 0x1)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    OP_64(0x1A)
    OP_64(0x1B)
    OP_64(0x1C)
    OP_64(0x1D)
    OP_71(0x1, 0x5, 0x5, 0x0, 0x8)
    OP_79(0x1)
    SetMapObjFlags(0x1, 0x10)
    OP_71(0x2, 0xA, 0xA, 0x0, 0x8)
    OP_79(0x2)
    SetMapObjFlags(0x2, 0x10)
    SetChrPos(0x101, -34900, 0, -950, 90)
    SetChrPos(0x102, -34900, 0, 450, 90)
    SetChrPos(0x103, -36500, 0, -1700, 90)
    SetChrPos(0x104, -36500, 0, 1200, 90)
    SetChrPos(0x109, -38100, 0, -1150, 90)
    SetChrPos(0x105, -38100, 0, 650, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(-35310, 1100, -350, 0)
    MoveCamera(38, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    OP_68(-36310, 1100, -350, 3000)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x103,
        (
            "#00208F#6PAfter all it is better than usual\x01",
            "There are many visiting customers …\x02",
        )
    )

    CloseMessageWindow()

    def lambda_594D():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_594D)
    Sleep(150)

    def lambda_595D():
        OP_93(0xFE, 0x10F, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_595D)
    Sleep(100)

    def lambda_596D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_596D)
    Sleep(50)

    def lambda_597D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_597D)
    Sleep(50)

    def lambda_598D():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_598D)
    Sleep(50)

    def lambda_599D():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_599D)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x105, 2)

    ChrTalk(
        0x102,
        (
            "#00106F#11PYes, a seriously injured person\x01",
            "Because there are many crowds only in the city ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#11P…… Donovan police station and\x01",
            "Iria is also in the hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F#6PYes … both of us still\x01",
            "She seems to be in coma.\x02\x03",
            "#10108FDonovan police … …\x01",
            "Francたちを庇ったらしくて。\x02\x03",
            "Francの回復が早かったのも\x01",
            "I think that it is thanks to the police.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#11PI see……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#5PIt was a splendid Osan … …\x01",
            "It's a big deal.\x02\x03",
            "#00308FIf possible, Mr. Ilya,\x01",
            "I hope I will see the situation ……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 4)), scpexpr(EXPR_END)), "loc_5BE0")

    ChrTalk(
        0x102,
        (
            "#00103F#11PI see …\x01",
            "Shuri is today\x01",
            "It seems they are coming.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5BFB")

    label("loc_5BE0")


    ChrTalk(
        0x102,
        "#00103F#11PI see …\x02",
    )

    CloseMessageWindow()

    label("loc_5BFB")


    def lambda_5C00():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 3, lambda_5C00)
    Sleep(250)

    ChrTalk(
        0x105,
        (
            "#10300F#5PSo,\x01",
            "Where is my sister's hospital room?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105F#6POh, yes …. 301.\x02\x03",
            "#10100FBefore that, a word to the receptionist,\x01",
            "You may as well tell it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#11POkay, let's go.\x02\x03",
            "#00003F（……Cecil姉も相当、\x01",
            "I guess he is busy. )\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_D7(0x24)
    OP_D7(0x25)
    OP_D7(0x26)
    OP_D7(0x27)
    OP_D7(0x28)
    OP_D7(0x29)
    OP_D7(0x2A)
    SetChrPos(0x0, -38500, 0, 0, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x180, 5)
    OP_29(0xAC, 0x1, 0x2)
    ModifyEventFlags(0, 1, 0x80)
    EventEnd(0x5)
    Return()

    # Function_27_54D2 end

    def Function_28_5D66(): pass

    label("Function_28_5D66")

    ClearChrFlags(0xFE, 0x4)
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_5D82():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_5D82)
    OP_95(0xFE, -22000, 0, -1750, 4000, 0x0)
    OP_95(0xFE, -24000, 0, -3750, 4000, 0x0)
    OP_95(0xFE, -24000, 0, -9000, 4000, 0x0)
    Sleep(500)
    BeginChrThread(0x1D, 1, 0, 31)
    OP_95(0xFE, -24000, 0, -3750, 4000, 0x0)
    OP_95(0xFE, -22000, 0, -1750, 4000, 0x0)
    OP_95(0xFE, 2000, 0, -1750, 4000, 0x0)

    def lambda_5E14():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_5E14)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0xFA0, 0x0)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x8)
    OP_79(0x2)
    SetMapObjFlags(0x2, 0x10)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_28_5D66 end

    def Function_29_5E4A(): pass

    label("Function_29_5E4A")

    ClearChrFlags(0xFE, 0x4)
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_5E66():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_5E66)
    OP_95(0xFE, -22000, 0, 1750, 4000, 0x0)
    OP_95(0xFE, -24000, 0, 3750, 4000, 0x0)
    OP_95(0xFE, -24000, 0, 11000, 4000, 0x0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0x5, 0x0, 0x8)
    OP_79(0x1)

    def lambda_5EC8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_5EC8)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0xFA0, 0x0)
    OP_64(0xFE)
    OP_71(0x1, 0x5, 0x0, 0x0, 0x8)
    OP_79(0x1)
    SetMapObjFlags(0x1, 0x10)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_29_5E4A end

    def Function_30_5F01(): pass

    label("Function_30_5F01")

    Sleep(1000)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0x5, 0x0, 0x8)
    OP_79(0x1)
    ClearChrFlags(0xFE, 0x4)
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_5F35():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_5F35)
    OP_95(0xFE, -24000, 0, 3500, 4000, 0x0)
    OP_71(0x1, 0x5, 0x0, 0x0, 0x8)
    OP_95(0xFE, -22000, 0, 1500, 4000, 0x0)
    OP_95(0xFE, 2000, 0, 1500, 4000, 0x0)

    def lambda_5F8E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_5F8E)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0xFA0, 0x0)
    OP_64(0xFE)
    OP_79(0x1)
    SetMapObjFlags(0x1, 0x10)
    SetChrFlags(0xFE, 0x4)
    BeginChrThread(0x1B, 1, 0, 29)
    Return()

    # Function_30_5F01 end

    def Function_31_5FC1(): pass

    label("Function_31_5FC1")

    ClearChrFlags(0xFE, 0x4)
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_95(0xFE, -24000, 0, -3500, 4000, 0x0)
    OP_95(0xFE, -22000, 0, -1500, 4000, 0x0)
    OP_95(0xFE, 2000, 0, -1500, 4000, 0x0)

    def lambda_6019():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_6019)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0xFA0, 0x0)
    OP_64(0xFE)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_31_5FC1 end

    def Function_32_603D(): pass

    label("Function_32_603D")

    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x960, 0x0)
    OP_93(0xFE, 0x10E, 0x3E8)
    Sleep(1000)
    OP_93(0xFE, 0x5A, 0x3E8)
    OP_9B(0x0, 0xFE, 0x0, 0x1964, 0x960, 0x0)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x8)
    OP_79(0x2)

    def lambda_608B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_608B)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x9C4, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_32_603D end

    def Function_33_60AC(): pass

    label("Function_33_60AC")

    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x4A38, 0x6D6, 0x0)

    def lambda_60C5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_60C5)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x6D6, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_33_60AC end

    def Function_34_60E6(): pass

    label("Function_34_60E6")

    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC0, 0x3E8, 0x0)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x8)
    OP_79(0x2)

    def lambda_6114():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_6114)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x3E8, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_34_60E6 end

    def Function_35_6135(): pass

    label("Function_35_6135")

    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x6F54, 0x3E8, 0x0)

    def lambda_614E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_614E)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x3E8, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_35_6135 end

    def Function_36_616F(): pass

    label("Function_36_616F")

    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x8CA0, 0x5DC, 0x0)

    def lambda_6188():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_6188)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x5DC, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_36_616F end

    def Function_37_61A9(): pass

    label("Function_37_61A9")

    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x9858, 0x578, 0x0)

    def lambda_61C2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_61C2)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x578, 0x0)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x8)
    OP_79(0x2)
    SetMapObjFlags(0x2, 0x10)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_37_61A9 end

    def Function_38_61F8(): pass

    label("Function_38_61F8")

    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x9858, 0x44C, 0x0)

    def lambda_6211():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_6211)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x44C, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_38_61F8 end

    def Function_39_6232(): pass

    label("Function_39_6232")

    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0xA028, 0x44C, 0x0)

    def lambda_624B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_624B)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x4B0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_39_6232 end

    def Function_40_626C(): pass

    label("Function_40_626C")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(803)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    OP_68(-46690, 1000, -40, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19720, 0)
    SetChrPos(0x101, -45000, 0, -700, 270)
    SetChrPos(0x102, -45000, 0, 700, 270)
    SetChrPos(0x103, -43500, 0, -700, 270)
    SetChrPos(0x104, -43500, 0, 700, 270)
    SetChrPos(0x109, -42000, 0, -700, 270)
    SetChrPos(0x105, -42000, 0, 700, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    def lambda_636E():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_636E)
    Sleep(100)

    def lambda_6386():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6386)
    Sleep(50)

    def lambda_639E():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_639E)
    Sleep(50)

    def lambda_63B6():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_63B6)
    Sleep(50)

    def lambda_63CE():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_63CE)
    Sleep(50)

    def lambda_63E6():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_63E6)
    OP_68(-48920, 1000, -570, 2700)
    SetCameraDistance(19720, 2700)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 1)
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_6440():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6440)
    Sleep(300)

    def lambda_6450():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6450)
    Sleep(300)

    def lambda_6460():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6460)
    Sleep(300)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x105, 1)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x1)
    OP_24(0x323)
    Sound(804, 0, 100, 0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005FYes, Special Affairs Support Division,\x01",
            "It is Lloyd · Bannings.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice of a boy")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Oh, thank you.\x02\x03",
            "Where are you now, now.\x02",
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
            "#00003FYou know.\x01",
            "Such times are properly\x01",
            "Is it polite to name yourself?\x02\x03",
            "#00000FUrsula hospital but ….\x01",
            "What is wrong, Jonah?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice of Jonah")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You sure, from today\x01",
            "You are returning to support work, right?\x02\x03",
            "A little request from me\x01",
            "I wonder if you will hear it.\x02",
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
            "#00006FNo, so without permission the police\x01",
            "Looking through the database ……\x02\x03",
            "#00001FBesides,\x01",
            "I am busy because I am busy ─\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice of Jonah")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Huhun, before this,\x01",
            "Search for missing destroyer\x01",
            "Who did you help?\x02\x03",
            "I told you to borrow and return.\x02",
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
            "#00013FDamn\x02\x03",
            "#00006F……it can not be helped.\x01",
            "I can not undertake anything\x01",
            "Let 's hear only the story.\x02\x03",
            "#00000FHow far should I go?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice of Jonah")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "So it's in the port area\x01",
            "Come to the front of the lighthouse.\x02\x03",
            "I will be waiting there. ♪\x02",
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
            "#00005FLighthouse\x01",
            "Whatever that place ……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice of Jonah")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Huhun, you have fun coming.\x02\x03",
            "Well then it's waiting.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(813, 0, 70, 0)
    Sleep(300)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00011F#2PAh … … exactly.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(300)

    ChrTalk(
        0x103,
        (
            "#00211F#11PAlso that Jonah is selfish\x01",
            "Did you say it?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()
    Sleep(150)
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        "#00012F#6PNo, well ….\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It is in the dock of the port area\x01",
            "I talked about what was called before the lighthouse.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00305F#5PHare?\x01",
            "Whatever that place ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F#11PWhen we say the lighthouse in the port area,\x01",
            "The bombed \"black moon\" building\x01",
            "It was rather close.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#5PCertainly, Mr. Lynn's\x01",
            "I also helped with the survey … …\x02\x03",
            "#00100FI will listen to the story\x01",
            "I wonder if it is okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F#11PAfter a section\x01",
            "Shall we go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6POh, let's do that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#11PWell, without listening to the circumstances here\x01",
            "Because it is what I have said without permission.\x02\x03",
            "#00211FI wonder if there are problems even if I let him wait a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309F#5PHaha, that is true.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    SetChrPos(0x0, -51000, 0, -700, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x181, 2)
    OP_29(0xAC, 0x1, 0x7)
    ModifyEventFlags(0, 2, 0x80)
    OP_24(0x323)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_40_626C end

    def Function_41_6C64(): pass

    label("Function_41_6C64")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    Call(0, 42)
    Call(0, 43)
    Call(0, 44)
    OP_68(-55000, 800, -300, 0)
    MoveCamera(71, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(32200, 0)
    FadeToBright(1000, 0)
    OP_68(-52000, 800, -300, 4000)
    MoveCamera(71, 19, 0, 4000)
    OP_6E(500, 4000)
    SetCameraDistance(26800, 4000)
    OP_0D()
    OP_6F(0x79)
    SetMessageWindowPos(14, 280, -1, 3)

    AnonymousTalk(
        0x101,
        "#00013F(Defense Forces unit … …)\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x105,
        (
            "#10401FIs it being guarded …?\x01",
            "The timing was bad. )\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("r1540", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_41_6C64 end

    def Function_42_6D7F(): pass

    label("Function_42_6D7F")

    LoadChrToIndex("apl/ch51616.itc", 0x1E)
    LoadChrToIndex("apl/ch51617.itc", 0x1F)
    SetChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x12, 0x1E)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x1F)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x1E)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x15, 0x1F)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x12, -50960, 0, 750, 225)
    SetChrPos(0x13, -53240, 0, 680, 135)
    SetChrPos(0x14, -53040, 0, -1550, 43)
    SetChrPos(0x15, -51030, 0, -1630, 315)
    Return()

    # Function_42_6D7F end

    def Function_43_6E1D(): pass

    label("Function_43_6E1D")

    OP_74(0xD, 0x1E)
    ClearMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xD, 0x1000)
    SetMapObjFrame(0xD, "light", 0x0, 0x1)
    SetMapObjFrame(0xD, "mark00", 0x0, 0x1)
    Return()

    # Function_43_6E1D end

    def Function_44_6E49(): pass

    label("Function_44_6E49")

    ClearMapObjFlags(0x6, 0x10)
    OP_70(0x6, 0xA)
    Return()

    # Function_44_6E49 end

    def Function_45_6E54(): pass

    label("Function_45_6E54")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x20)
    LoadChrToIndex("chr/ch00051.itc", 0x21)
    LoadChrToIndex("chr/ch03150.itc", 0x22)
    LoadChrToIndex("chr/ch03151.itc", 0x23)
    LoadChrToIndex("chr/ch02750.itc", 0x24)
    LoadChrToIndex("chr/ch02751.itc", 0x25)
    LoadChrToIndex("chr/ch41450.itc", 0x26)
    LoadChrToIndex("chr/ch41451.itc", 0x27)
    LoadChrToIndex("chr/ch41550.itc", 0x28)
    LoadChrToIndex("chr/ch41551.itc", 0x29)
    Call(0, 42)
    Call(0, 43)
    Call(0, 44)
    SetChrPos(0x101, -67340, 0, -1250, 90)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x105, -67880, 0, 500, 90)
    SetChrChipByIndex(0x105, 0x23)
    SetChrSubChip(0x105, 0x0)
    SetChrPos(0x107, -69900, 0, -550, 90)
    SetChrChipByIndex(0x107, 0x25)
    SetChrSubChip(0x107, 0x0)
    PlayBGM("ed7561", 0)
    OP_68(-52000, 2200, -300, 0)
    MoveCamera(71, 24, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(24150, 0)
    FadeToBright(1000, 0)
    OP_68(-52000, 1200, -300, 3000)
    MoveCamera(71, 24, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(23000, 3000)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x12,
        "#5PHa, I'm bored.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#5PI can not guard such a place\x01",
            "It's too tight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#6PBecome hazy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#6PBannings of the support department of the example\x01",
            "Because I'm running away.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x13, 500)
    Sleep(100)

    ChrTalk(
        0x12,
        (
            "#5PHat, for a single investigator\x01",
            "What can I do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#5PAround a foreign country long ago\x01",
            "Are not you running away?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#12PBut ridiculous things\x01",
            "It's a rumor to be taken … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#12PThe people of the fourth regiment\x01",
            "Is it true that being eaten?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x14, 500)
    Sleep(100)

    ChrTalk(
        0x12,
        "#5PHaha, it's just a hoax.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#5PBecause that's more than that\x01",
            "I want to worship Yireia's face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#5PYou sure are still in the hospital?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#11POh, that's it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#11PHave the injury cured at the end\x01",
            "I would like you to recover.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x101,
        "Voice of Lloyd",
        "#11P── I agree.\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_63(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(-59000, 800, -300, 1500)
    MoveCamera(36, 25, 0, 1500)
    OP_6E(500, 1500)
    SetCameraDistance(20500, 1500)

    def lambda_72A0():
        OP_93(0x12, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_72A0)
    Sleep(50)

    def lambda_72B0():
        OP_93(0x13, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_72B0)
    Sleep(50)

    def lambda_72C0():
        OP_93(0x14, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_72C0)
    Sleep(50)

    def lambda_72D0():
        OP_93(0x15, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_72D0)
    Sleep(50)
    WaitChrThread(0x12, 0)
    WaitChrThread(0x13, 0)
    WaitChrThread(0x14, 0)
    WaitChrThread(0x15, 0)
    Sleep(1000)
    BeginChrThread(0x101, 0, 0, 46)
    BeginChrThread(0x105, 0, 0, 47)
    BeginChrThread(0x107, 0, 0, 48)
    Sleep(1000)
    OP_68(-55500, 800, -300, 1300)
    MoveCamera(36, 25, 0, 1300)
    OP_6E(500, 1300)
    SetCameraDistance(20500, 1300)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7452", 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x107, 0)
    OP_6F(0x79)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x12,
        "#11PLloyd · Bannings! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#11PCut, it really appears!\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x14, 0x26)
    SetChrSubChip(0x14, 0x0)
    Sleep(150)
    SetChrChipByIndex(0x13, 0x28)
    SetChrSubChip(0x13, 0x0)
    Sleep(150)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x12, 0x26)
    SetChrSubChip(0x12, 0x0)
    Sleep(150)
    SetChrChipByIndex(0x15, 0x28)
    SetChrSubChip(0x15, 0x0)
    Sleep(150)

    ChrTalk(
        0x107,
        (
            "#01203F#6P#3CWhew.\x01",
            "I'm sorry to be a chemistry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10402F#6PNo, when I see that former figure\x01",
            "You can not help it indeed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PI do not mean to contend.\x02\x03",
            "#00007FBut if you stand up\x01",
            "Do not hesitate to defeat me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "#11PCheeky……!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#11PA few!\x01",
            "We will control at once!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#11Proger that#4RRaja#It is!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    SetCameraDistance(19000, 500)
    BeginChrThread(0x12, 0, 0, 49)
    BeginChrThread(0x13, 0, 0, 50)
    BeginChrThread(0x14, 0, 0, 51)
    BeginChrThread(0x15, 0, 0, 52)
    WaitChrThread(0x12, 0)
    WaitChrThread(0x13, 0)
    WaitChrThread(0x14, 0)
    WaitChrThread(0x15, 0)
    SetScenarioFlags(0x22, 2)
    Battle("BattleInfo_8E0", 0x30200011, 0x0, 0x0, 0x24, 0xFF)
    FadeToDark(0, 0, -1)
    ClearScenarioFlags(0x22, 2)
    Call(0, 53)
    Return()

    # Function_45_6E54 end

    def Function_46_7559(): pass

    label("Function_46_7559")

    SetChrFlags(0xFE, 0x1000)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1000)
    Return()

    # Function_46_7559 end

    def Function_47_757B(): pass

    label("Function_47_757B")

    Sleep(50)
    SetChrFlags(0xFE, 0x1000)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1000)
    Return()

    # Function_47_757B end

    def Function_48_75A0(): pass

    label("Function_48_75A0")

    Sleep(100)
    SetChrFlags(0xFE, 0x1000)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1000)
    Return()

    # Function_48_75A0 end

    def Function_49_75C5(): pass

    label("Function_49_75C5")

    SetChrChipByIndex(0x12, 0x27)
    SetChrSubChip(0x12, 0x0)
    OP_9B(0x1, 0xFE, 0xA, 0x5DC, 0x1388, 0x1)
    Return()

    # Function_49_75C5 end

    def Function_50_75DD(): pass

    label("Function_50_75DD")

    SetChrChipByIndex(0x13, 0x29)
    SetChrSubChip(0x13, 0x0)
    OP_9B(0x1, 0xFE, 0x15E, 0x5DC, 0x1388, 0x1)
    Return()

    # Function_50_75DD end

    def Function_51_75F5(): pass

    label("Function_51_75F5")

    SetChrChipByIndex(0x14, 0x26)
    SetChrSubChip(0x14, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x1388, 0x1)
    Return()

    # Function_51_75F5 end

    def Function_52_760D(): pass

    label("Function_52_760D")

    SetChrChipByIndex(0x15, 0x29)
    SetChrSubChip(0x15, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x1388, 0x1)
    Return()

    # Function_52_760D end

    def Function_53_7625(): pass

    label("Function_53_7625")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(2724)
    SoundLoad(2725)
    SoundLoad(2686)
    SoundLoad(2687)
    SoundLoad(2688)
    SoundLoad(2689)
    SoundLoad(2690)
    SoundLoad(2691)
    SoundLoad(2692)
    SoundLoad(2693)
    SoundLoad(2866)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00203.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu06400.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01300.itp")
    AddParty(0x2, 0xFF, 0xFF)
    OP_32(0x2, 0x0, 0x52)
    OP_32(0x2, 0x5, 0x64)
    OP_42(0x2, 0x419, 0xFF)
    OP_42(0x2, 0x5ED, 0xFF)
    OP_42(0x2, 0x651, 0xFF)
    OP_38(0x2, 0x81, 0x2)
    OP_38(0x2, 0x82, 0x2)
    OP_38(0x2, 0x83, 0x2)
    OP_38(0x2, 0x86, 0x2)
    OP_42(0x2, 0xAF, 0x1)
    OP_42(0x2, 0x66, 0x2)
    OP_42(0x2, 0x7A, 0x3)
    OP_42(0x2, 0xA2, 0x6)
    ClearScenarioFlags(0x20, 3)
    LoadChrToIndex("chr/ch41400.itc", 0x1E)
    LoadChrToIndex("chr/ch41500.itc", 0x1F)
    LoadChrToIndex("chr/ch05300.itc", 0x20)
    LoadChrToIndex("chr/ch08500.itc", 0x21)
    LoadChrToIndex("chr/ch00050.itc", 0x22)
    LoadChrToIndex("chr/ch03150.itc", 0x23)
    LoadChrToIndex("chr/ch02750.itc", 0x24)
    LoadChrToIndex("chr/ch41453.itc", 0x25)
    LoadChrToIndex("chr/ch41553.itc", 0x26)
    LoadChrToIndex("apl/ch51700.itc", 0x27)
    LoadChrToIndex("apl/ch51701.itc", 0x28)
    LoadEffect(0x0, "event/ev17027.eff")
    LoadEffect(0x3, "event/ev17004.eff")
    LoadEffect(0x4, "event/ev17005.eff")
    SetChrChipByIndex(0x101, 0x22)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x105, 0x23)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x107, 0x24)
    SetChrSubChip(0x107, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x101, -55340, 0, -1250, 90)
    SetChrPos(0x105, -55880, 0, 500, 90)
    SetChrPos(0x107, -57900, 0, -550, 90)
    SetChrPos(0x103, -44000, 0, 150, 270)
    SetChrPos(0x16, -44000, 0, -1200, 270)
    SetChrPos(0x17, -44000, 0, 0, 270)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x12, 0x25)
    SetChrSubChip(0x12, 0x2)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x26)
    SetChrSubChip(0x13, 0x2)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x25)
    SetChrSubChip(0x14, 0x2)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x15, 0x26)
    SetChrSubChip(0x15, 0x2)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x12, -50370, 0, 640, 270)
    SetChrPos(0x13, -52240, 0, 580, 270)
    SetChrPos(0x14, -52040, 0, -1450, 270)
    SetChrPos(0x15, -50440, 0, -1520, 270)
    SetChrChipByIndex(0x16, 0x20)
    SetChrSubChip(0x16, 0x0)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x17, 0x21)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    Call(0, 43)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -52000, 0, 4000, 268)
    OP_78(0xD, 0x18)
    Call(0, 44)
    OP_68(-54300, 800, -300, 0)
    MoveCamera(36, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    SetCameraDistance(20500, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x14,
        "#40W#11P… ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#40W#11POne, strong …\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sleep(100)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    Sleep(100)
    SetChrChipByIndex(0x107, 0xFF)
    SetChrSubChip(0x107, 0x0)
    Sleep(300)

    ChrTalk(
        0x105,
        "#10404F#5PWell I guess it will be my turn.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_68(-54200, 800, 860, 1200)
    MoveCamera(36, 25, 0, 1200)
    OP_6E(500, 1200)
    SetCameraDistance(20500, 1200)

    def lambda_7A08():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7A08)
    OP_9B(0x0, 0x105, 0x0, 0x190, 0x3E8, 0x0)
    Sleep(300)
    BeginChrThread(0x105, 0, 0, 54)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00005F#12P(Star cup medals …?\x02",
    )

    CloseMessageWindow()
    PlayBGM("ed7304", 0)
    SetCameraDistance(20000, 20000)
    Sleep(1000)
    Sound(2866, 255, 50, 0)

    ChrTalk(
        0x105,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#10403F#30W#5P#30ASparkle in my abyss\x01",
            "Golden Gold#4RAoi is not it.#It's engraved … …\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x105, 0, 0, 56)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x105,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#10401F#30W#5P#20AAwareness#2RMorale#In connection with Silver Yeoh,\x01",
            "Give them a memorable memory.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 59)
    Sleep(800)

    ChrTalk(
        0x13,
        "#50W#11P#2S…………Ah,\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x14,
        "#50W#11P#2S…………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x101,
        "#00011F#12P(this is……)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01203F#3C#6P(Hmm, it is transmitted to the church\x01",
            "It seems to be a suggested technique. )\x02\x03",
            "#01200F(Somehow magical powers are also\x01",
            "It seems to be using … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10403F#5P── You guys,\x01",
            "I confirmed the approach of a large eid beast.\x02\x03",
            "I managed to fight back,\x01",
            "Because everyone was injured\x01",
            "I decided to temporarily return home.\x02\x03",
            "#10401FI have not seen the appearance of Bannings,\x01",
            "I do not feel like appearing for the time being.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    BeginChrThread(0x13, 0, 0, 62)
    WaitChrThread(0x13, 0)
    Sleep(500)

    ChrTalk(
        0x13,
        "#50W#11P#2S…………………… (Kokokoku)\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    BeginChrThread(0x14, 0, 0, 64)
    WaitChrThread(0x14, 0)
    Sleep(500)

    ChrTalk(
        0x14,
        "#50W#11P#2S…… There is no sign of appearing.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_68(-53350, 800, 2710, 3000)
    OP_52(0x12, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x12, 0, 0, 61)
    BeginChrThread(0x13, 0, 0, 63)
    BeginChrThread(0x14, 0, 0, 65)
    BeginChrThread(0x15, 0, 0, 66)
    BeginChrThread(0x105, 0, 0, 55)

    def lambda_7DC2():

        label("loc_7DC2")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_7DC2")

    QueueWorkItem2(0x105, 3, lambda_7DC2)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x12, 0)
    WaitChrThread(0x13, 0)
    WaitChrThread(0x14, 0)
    WaitChrThread(0x15, 0)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    EndChrThread(0x105, 0x3)
    BeginChrThread(0x18, 0, 0, 67)
    BeginChrThread(0x101, 0, 0, 68)
    BeginChrThread(0x105, 0, 0, 69)
    BeginChrThread(0x107, 0, 0, 70)
    Sleep(1500)
    OP_68(-55360, 1500, -1970, 2000)
    MoveCamera(64, 37, 0, 2000)
    OP_6E(500, 2000)
    SetCameraDistance(19550, 2000)
    OP_6F(0x79)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x107, 0)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x107, 0x2)
    WaitChrThread(0x18, 0)
    SetMapObjFlags(0xD, 0x4)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00006F#11PThat's amazing …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01203F#12P#3CIf it is just an implicit technique\x01",
            "You can not manipulate it concretely.\x02\x03",
            "#01200FTo be aware, \"Stigmata#4RStigma#The power of\x01",
            "Was it to use it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#5PHa ha …\x01",
            "As expected it is a legendary Holy Beast.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#11P\"Stigmata#4RStigma#\"……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#5PWait a minute\x01",
            "It is old trauma.\x02\x03",
            "#10408FEither way, it's not perfect\x01",
            "The suggestion will be solved in a couple of days.\x02\x03",
            "#10401FThe army will also be wary of it\x01",
            "I want you to think that you can not use it in the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F#11PI see … OK.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xFA0)
    OP_C9(0x0, 0x80000000)

    NpcTalk(
        0x103,
        "Voice of a girl",
        "#6P#2686V#30W#20AWasy, Zeit …?\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)

    def lambda_80AE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_80AE)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x107, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-44070, 400, 120, 2000)
    MoveCamera(76, 17, 0, 2000)
    OP_6E(500, 2000)
    SetCameraDistance(19770, 2000)

    def lambda_8126():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8126)
    Sleep(50)

    def lambda_8136():
        OP_93(0x105, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8136)
    Sleep(50)

    def lambda_8146():
        OP_93(0x107, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_8146)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x107, 0)
    OP_6F(0x79)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x103,
        "#40W………………………………\x02",
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
        0x101,
        "#00005F#11P#12P#NTio …!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x107,
        "#01200F#2P#3C#6P#NHm, it seems to be safe.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x105,
        "#10404F#6P#NWhew, I am relieved.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x101, -53360, 0, -1680, 90)
    SetChrPos(0x105, -54080, 0, 130, 90)
    SetChrPos(0x107, -55410, 0, -1850, 90)
    SetChrSubChip(0x107, 0x5)
    TurnDirection(0x101, 0x103, 0)
    TurnDirection(0x103, 0x101, 0)
    OP_68(-49050, 1000, -1000, 0)
    MoveCamera(52, 11, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19080, 0)
    Fade(500)
    OP_0D()
    OP_9B(0x0, 0x101, 0x0, 0x190, 0x3E8, 0x0)

    ChrTalk(
        0x101,
        (
            "#00014F#6PWas good……!\x01",
            "Because I am in a hospital\x01",
            "What the hell am I doing ……\x02\x03",
            "#00002Fare you okay?\x01",
            "Have you not been injured?\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7523", 0)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x103,
        "#00213F#11P#2687V#50W#25A#2S…… Lloyd …… san ………\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x103,
        "#00212F#11P#2688V#20W#4S#15A#4SLloyd san ……! It is!\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    BeginChrThread(0x103, 0, 0, 71)
    OP_68(-52640, 1200, -1760, 1800)
    MoveCamera(47, 20, 0, 1800)
    OP_6E(500, 1800)
    SetCameraDistance(17000, 1800)
    WaitChrThread(0x103, 0)

    def lambda_8450():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_8450)

    def lambda_845D():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_845D)
    OP_6F(0x79)
    SetCameraDistance(15500, 40000)

    ChrTalk(
        0x101,
        (
            "#00011F#6PUg ……\x01",
            "(Kyo, the chest is … …)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x103,
        (
            "#00213F#11P#2689V#60W#25AWhere are you … …!\x02\x03",
            "#00215F#2690V#25AI heard that they are caught in a jail … …!\x02\x03",
            "#00212F#2691V#60A…… It's escaping\x01",
            "It is being chased by military people ……\x01",
            "On the guiding net, you see, …!\x02\x03",
            "#00213F#2692V#50AWow, I … … Hick …\x01",
            "……… I have been worried ………… っ!\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    Sleep(300)

    ChrTalk(
        0x101,
        "#00008F#6PTio …\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 0, 0, 78)
    BeginChrThread(0x103, 0, 0, 77)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)

    ChrTalk(
        0x101,
        (
            "#00006F#6P…… Sorry.\x01",
            "It seems I made you worry.\x02\x03",
            "#00002FBut it's okay now.\x02\x03",
            "With the help of Zeit and Wazi\x01",
            "I came back to the crossbell … …\x02\x03",
            "#00004FSo … please be relieved.\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x103,
        "#00215F#11P#2693V#40W#25A… …. Uu … … Gum … …\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)

    NpcTalk(
        0x17,
        "Daughter's voice",
        (
            "#11P#2724V#30W#N#25ASorry ….\x01",
            "It is love love.\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(300)

    NpcTalk(
        0x16,
        "Female voice",
        (
            "#11P#N#20A#30WHaha, I will not disturb you\x01",
            "I feel a little mind … …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(-52280, 1200, -1700, 2500)
    SetCameraDistance(17000, 2500)

    def lambda_87C5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_87C5)

    def lambda_87D6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_87D6)
    SetChrPos(0x16, -42500, 0, -1200, 270)
    SetChrPos(0x17, -42500, 0, 0, 270)
    BeginChrThread(0x17, 0, 0, 73)
    Sleep(100)
    BeginChrThread(0x16, 0, 0, 74)
    Sleep(1500)

    ChrTalk(
        0x101,
        (
            "#00002F#6PCecil姉！\x01",
            "それに……Franc！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x17, 0)
    WaitChrThread(0x16, 0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0x17,
        (
            "#2725V#30WErr …\x01",
            "Long time no see, Lloyd!\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xAA5)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    AnonymousTalk(
        0x16,
        (
            "#30WReally well well … …\x02\x03",
            "… … I was worried, Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)

    ChrTalk(
        0x101,
        (
            "#00006F#6PSorry ….\x01",
            "Worry everyone.\x02\x03",
            "#00002FでもFranc。\x01",
            "Does it seem to be fine?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#06409F#11PYes, already longer\x01",
            "I'm getting completely injured!\x02\x03",
            "#06406FWell Cross Bell\x01",
            "Because it became such a thing\x01",
            "I can not return to work … but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PReally……\x01",
            "But it was really good.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Sound(2277, 255, 80, 0)
    Sleep(300)
    BeginChrThread(0x103, 0, 0, 72)
    WaitChrThread(0x103, 0)
    Sleep(500)

    ChrTalk(
        0x103,
        (
            "#00215F#11P#30W……by the way.\x01",
            "What is it about that wad?\x02\x03",
            "#00216FWhere is Zeit ever ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10404F#6PHuh, well, there are various things.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01200F#6P#3CFor the time being\x01",
            "Let me explain it all together.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x16,
        "#01305F#11PHuh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        "#06411F#11PThere, now ….\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#00205F#11PIs it? What happened?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F#6PNo, what should I do ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10402F#6PHaha, perhaps\x01",
            "I always knew the language\x01",
            "Do you not notice?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x103)
    Sleep(500)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x103,
        (
            "#00205F#11P#4SZha, Zeit! Is it?\x02\x03",
            "#00207FHow come the human words\x01",
            "Are you talking ─ ─ ─! Is it?\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(18000, 2000)
    FadeToDark(1500, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(1000)
    SetScenarioFlags(0x22, 0)
    NewScene("t1510", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_53_7625 end

    def Function_54_8DB0(): pass

    label("Function_54_8DB0")

    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x1000)
    SetChrFlags(0xFE, 0x2)
    Sleep(100)
    Sound(531, 0, 50, 0)
    Sound(859, 0, 40, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    Return()

    # Function_54_8DB0 end

    def Function_55_8DDF(): pass

    label("Function_55_8DDF")

    Sleep(4000)
    BeginChrThread(0x105, 1, 0, 58)
    WaitChrThread(0x105, 1)
    Sound(802, 0, 100, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x2)
    Return()

    # Function_55_8DDF end

    def Function_56_8E13(): pass

    label("Function_56_8E13")

    Sound(895, 0, 100, 0)
    Sound(222, 0, 30, 0)
    Sound(852, 2, 100, 0)
    PlayEffect(0x3, 0x1, 0x105, 0x5, 0, 0, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    PlayEffect(0x4, 0x2, 0x105, 0x1, 0, 0, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(700)
    StopEffect(0x1, 0x2)
    BeginChrThread(0xFE, 2, 0, 57)
    Return()

    # Function_56_8E13 end

    def Function_57_8EA3(): pass

    label("Function_57_8EA3")

    Sleep(300)

    label("loc_8EA6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8EF0")
    PlayEffect(0x0, 0xFF, 0x105, 0x3, 0, 1050, 800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Jump("loc_8EA6")

    label("loc_8EF0")

    Return()

    # Function_57_8EA3 end

    def Function_58_8EF1(): pass

    label("Function_58_8EF1")

    EndChrThread(0xFE, 0x2)
    Sleep(300)
    StopEffect(0x2, 0x2)
    StopSound(852, 500, 90)
    Sleep(300)
    Return()

    # Function_58_8EF1 end

    def Function_59_8F05(): pass

    label("Function_59_8F05")


    def lambda_8F0A():
        OP_A6(0xFE, 0x1E, 0x0, 0xFA, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_8F0A)
    Sleep(200)

    def lambda_8F26():
        OP_A6(0xFE, 0x1E, 0x0, 0xFA, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_8F26)
    Sleep(200)

    def lambda_8F42():
        OP_A6(0xFE, 0x1E, 0x0, 0xFA, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_8F42)
    Sleep(200)

    def lambda_8F5E():
        OP_A6(0xFE, 0x1E, 0x0, 0xFA, 0xBB8)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_8F5E)
    Sleep(200)
    Return()

    # Function_59_8F05 end

    def Function_60_8F76(): pass

    label("Function_60_8F76")

    Sleep(250)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    Return()

    # Function_60_8F76 end

    def Function_61_8F85(): pass

    label("Function_61_8F85")

    Sleep(900)
    SetChrSubChip(0x12, 0x1)
    Sleep(700)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    BeginChrThread(0xFE, 1, 0, 1)
    OP_93(0xFE, 0x0, 0x12C)
    OP_9B(0x0, 0xFE, 0x0, 0xFA, 0x384, 0x1)
    OP_9B(0x0, 0xFE, 0x13B, 0x60E, 0x384, 0x0)
    OP_9B(0x0, 0xFE, 0x2D, 0xFA, 0x384, 0x1)
    BeginChrThread(0xFE, 3, 0, 60)
    OP_9C(0xFE, 0x0, 0x1F4, 0x3E8, 0x226, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x384, 0x1)
    Return()

    # Function_61_8F85 end

    def Function_62_900E(): pass

    label("Function_62_900E")

    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_62_900E end

    def Function_63_9013(): pass

    label("Function_63_9013")

    Sleep(200)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    BeginChrThread(0xFE, 1, 0, 1)
    OP_93(0xFE, 0x0, 0x12C)
    OP_9B(0x0, 0xFE, 0x0, 0x2EE, 0x384, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x28A, 0x384, 0x1)
    OP_9B(0x0, 0xFE, 0x13B, 0x64, 0x384, 0x0)
    Sound(464, 0, 100, 0)
    OP_71(0xD, 0x1, 0x1E, 0x1, 0x0)
    OP_79(0xD)
    OP_9B(0x0, 0xFE, 0x0, 0x96, 0x384, 0x1)
    BeginChrThread(0xFE, 3, 0, 60)
    OP_9C(0xFE, 0x0, 0x1F4, 0x3E8, 0x226, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x384, 0x1)
    Return()

    # Function_63_9013 end

    def Function_64_90B9(): pass

    label("Function_64_90B9")

    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_64_90B9 end

    def Function_65_90BE(): pass

    label("Function_65_90BE")

    Sleep(1200)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    BeginChrThread(0xFE, 1, 0, 1)
    OP_93(0xFE, 0x0, 0x12C)
    OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x384, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x2EE, 0x384, 0x1)
    OP_9B(0x0, 0xFE, 0x13B, 0x15E, 0x384, 0x0)
    BeginChrThread(0xFE, 3, 0, 60)
    OP_9C(0xFE, 0x0, 0x1F4, 0x3E8, 0x226, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x384, 0x1)
    Return()

    # Function_65_90BE end

    def Function_66_9140(): pass

    label("Function_66_9140")

    Sleep(1500)
    SetChrSubChip(0x15, 0x1)
    Sleep(700)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    BeginChrThread(0xFE, 1, 0, 1)
    OP_93(0xFE, 0x0, 0x12C)
    OP_9B(0x0, 0xFE, 0x0, 0x8CA, 0x384, 0x1)
    OP_9B(0x0, 0xFE, 0x13B, 0x60E, 0x384, 0x0)
    OP_9B(0x0, 0xFE, 0x2D, 0xFA, 0x384, 0x1)
    BeginChrThread(0xFE, 3, 0, 60)
    OP_9C(0xFE, 0x0, 0x1F4, 0x3E8, 0x226, 0x1F4)

    def lambda_91BE():
        OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x384, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_91BE)
    Sleep(300)
    Sound(463, 0, 100, 0)
    OP_71(0xD, 0x1F, 0x3C, 0x1, 0x8)
    OP_79(0xD)
    Return()

    # Function_66_9140 end

    def Function_67_91E7(): pass

    label("Function_67_91E7")

    Sound(465, 0, 100, 0)
    SetMapObjFrame(0xD, "light", 0x1, 0x1)
    Sleep(500)
    OP_9B(0x0, 0xFE, 0x0, 0xFA, 0x3E8, 0x1)
    OP_9B(0x0, 0xFE, 0x167, 0xFA, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x167, 0xFA, 0xBB8, 0x1)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -53500, 0, 3700)
    OP_9F(0x1, -55000, 0, 2900)
    OP_9F(0x1, -57000, 0, 1600)
    OP_9F(0x1, -60000, 0, 500)
    OP_9F(0x1, -69000, 0, 0)
    OP_9F(0x2, 0xFE, 4500, 0x6)
    Return()

    # Function_67_91E7 end

    def Function_68_927E(): pass

    label("Function_68_927E")


    def lambda_9283():

        label("loc_9283")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_9283")

    QueueWorkItem2(0xFE, 2, lambda_9283)
    Sleep(400)
    OP_9B(0x1, 0xFE, 0x5A, 0x6D6, 0x7D0, 0x0)
    Return()

    # Function_68_927E end

    def Function_69_92A3(): pass

    label("Function_69_92A3")


    def lambda_92A8():

        label("loc_92A8")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_92A8")

    QueueWorkItem2(0xFE, 2, lambda_92A8)
    Sleep(100)
    OP_9B(0x1, 0xFE, 0x5A, 0x4E2, 0x3E8, 0x0)
    Return()

    # Function_69_92A3 end

    def Function_70_92C8(): pass

    label("Function_70_92C8")

    Sleep(600)
    OP_9B(0x0, 0xFE, 0x5A, 0x1F4, 0x7D0, 0x1)
    OP_9D(0xFE, 0xFFFF259A, 0x0, 0xFFFFF7CC, 0x15E, 0x5DC)
    OP_9B(0x0, 0xFE, 0x0, 0xFA, 0x3E8, 0x1)

    def lambda_9305():

        label("loc_9305")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_9305")

    QueueWorkItem2(0xFE, 2, lambda_9305)
    Return()

    # Function_70_92C8 end

    def Function_71_9313(): pass

    label("Function_71_9313")

    OP_9B(0x0, 0xFE, 0x0, 0x2198, 0x1770, 0x0)
    BeginChrThread(0xFE, 3, 0, 75)
    Sound(811, 0, 50, 0)
    Sound(898, 0, 100, 0)
    BeginChrThread(0x101, 3, 0, 76)

    def lambda_933F():
        OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0x5DC)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_933F)
    Sleep(100)

    def lambda_935B():
        OP_A6(0xFE, 0x0, 0x14, 0x190, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_935B)
    Return()

    # Function_71_9313 end

    def Function_72_9370(): pass

    label("Function_72_9370")

    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x1000)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x1000)
    Sound(812, 0, 100, 0)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x3E8, 0x0)
    Return()

    # Function_72_9370 end

    def Function_73_93AA(): pass

    label("Function_73_93AA")

    OP_9B(0x0, 0xFE, 0x163, 0x1F40, 0x7D0, 0x0)
    Return()

    # Function_73_93AA end

    def Function_74_93BA(): pass

    label("Function_74_93BA")

    Sleep(100)
    OP_9B(0x0, 0xFE, 0x163, 0x1F40, 0x7D0, 0x0)
    Return()

    # Function_74_93BA end

    def Function_75_93CD(): pass

    label("Function_75_93CD")

    SetChrChipByIndex(0xFE, 0x28)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x0)
    Sleep(1005)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(300)
    Return()

    # Function_75_93CD end

    def Function_76_93F1(): pass

    label("Function_76_93F1")

    SetChrChipByIndex(0xFE, 0x28)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x8)
    Sleep(100)
    SetChrSubChip(0xFE, 0x9)
    Sleep(100)
    SetChrSubChip(0xFE, 0xA)
    Sleep(300)
    Return()

    # Function_76_93F1 end

    def Function_77_9415(): pass

    label("Function_77_9415")

    SetChrChipByIndex(0xFE, 0x28)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x2)
    Sleep(150)
    SetChrSubChip(0xFE, 0x3)
    Sleep(150)
    SetChrSubChip(0xFE, 0x4)
    Sleep(450)
    Return()

    # Function_77_9415 end

    def Function_78_9439(): pass

    label("Function_78_9439")

    SetChrChipByIndex(0xFE, 0x28)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0xA)
    Sleep(150)
    SetChrSubChip(0xFE, 0xB)
    Sleep(150)
    SetChrSubChip(0xFE, 0xC)
    Sleep(450)
    Return()

    # Function_78_9439 end

    def Function_79_945D(): pass

    label("Function_79_945D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    AddParty(0x6, 0xFF, 0xFF)
    LoadChrToIndex("chr/ch05300.itc", 0x1E)
    LoadChrToIndex("chr/ch06900.itc", 0x1F)
    LoadChrToIndex("chr/ch03154.itc", 0x20)
    LoadEffect(0x0, "battle/mgaria0.eff")
    SoundLoad(497)
    SetChrPos(0x101, -10000, 0, 750, 90)
    SetChrPos(0x103, -10200, 0, -850, 90)
    SetChrPos(0x105, -11550, 0, 1350, 90)
    SetChrPos(0x17, -11700, 0, -1450, 90)
    SetChrPos(0x107, -12050, 0, 100, 90)
    SetChrSubChip(0x107, 0x5)
    SetChrChipByIndex(0x16, 0x1E)
    SetChrSubChip(0x16, 0x0)
    SetChrFlags(0x16, 0x8000)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, -6000, 1000, 0, 270)
    SetChrChipByIndex(0x17, 0x1F)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x19, 0x80)
    OP_78(0x11, 0x19)
    OP_93(0x19, 0xB4, 0x0)
    OP_68(-10000, 3000, 0, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(25000, 0)
    FadeToBright(1000, 0)
    OP_68(-10000, 1000, 0, 3000)
    MoveCamera(45, 23, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(25000, 3000)
    OP_6F(0x79)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyds then joined the Zeit ……\x02\x03",
            "Cecilにも別れを告げてウルスラ病院を後にした。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(27000, 5000)
    BeginChrThread(0x101, 0, 0, 81)
    BeginChrThread(0x103, 0, 0, 82)
    BeginChrThread(0x105, 0, 0, 83)
    BeginChrThread(0x107, 0, 0, 84)
    BeginChrThread(0x17, 0, 0, 85)
    BeginChrThread(0x16, 0, 0, 87)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    EndChrThread(0x101, 0x0)
    EndChrThread(0x103, 0x0)
    EndChrThread(0x105, 0x0)
    EndChrThread(0x107, 0x0)
    EndChrThread(0x17, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrPos(0x105, -51000, 100, 17000, 90)
    SetChrPos(0x101, -51300, 0, 15600, 90)
    SetChrPos(0x103, -52380, 0, 17080, 90)
    SetChrPos(0x107, -51330, 0, 18780, 124)
    SetChrPos(0x17, -51810, 0, 14140, 51)
    SetChrSubChip(0x107, 0x5)
    ClearMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0xF, 0x1000)
    ClearMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x10, 0x1000)
    ClearMapObjFlags(0x11, 0x4)
    SetMapObjFlags(0x11, 0x1000)
    OP_71(0x11, 0x65, 0xA0, 0x0, 0x20)
    SetMapObjFlags(0x9, 0x4)
    OP_68(-50250, 1000, 17000, 0)
    MoveCamera(48, 32, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20150, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Fade(250)
    SetChrChipByIndex(0x105, 0x20)
    SetChrSubChip(0x105, 0x0)
    OP_0D()
    Sound(357, 0, 50, 0)
    PlayEffect(0x0, 0x0, 0x105, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_68(-49850, 1000, 17000, 18000)
    SetCameraDistance(15000, 18000)
    BeginChrThread(0x105, 3, 0, 88)
    BeginChrThread(0x19, 1, 0, 89)
    Sleep(500)
    Sound(935, 0, 100, 0)
    Sleep(1500)
    StopEffect(0x0, 0x2)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "─ ─ On the way back, Wadi goes to the hospital\x01",
            "Find the \"gap\" of the power field of the seven ioxies … …\x02\x03",
            "By fixing with the \"legal team\"\x01",
            "It is something that will be picked up by \"Mercapa\"\x01",
            "It became possible.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x26, 1, 0, 80)
    Fade(500)
    OP_68(-49730, 1500, 16190, 0)
    MoveCamera(64, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(37770, 0)
    OP_68(-43790, 1000, 18370, 6000)
    MoveCamera(68, 48, 0, 6000)
    OP_6E(500, 6000)
    SetCameraDistance(60530, 6000)
    ClearMapObjFlags(0x11, 0x4)
    SetChrPos(0x19, -48000, 18250, 17000, 180)
    OP_D5(0x19, 0x0, 0x2BF20, 0x0, 0x0)
    BeginChrThread(0x19, 0, 0, 86)
    Sleep(4000)
    StopSound(497, 1000, 60)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x19, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    SetMessageWindowPos(-1, -1, -1, -1)
    Sound(814, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ティオとFrancが参加した事により\x01",
            "At the terminal in Mercapa, request for demanding demons and so on\x01",
            "It was able to receive it.\x02\x03",
            "Since the terminal in the cabin can be used\x01",
            "Please use it.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x22, 3)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_79_945D end

    def Function_80_99D2(): pass

    label("Function_80_99D2")

    Sound(497, 2, 10, 0)
    Sleep(50)
    OP_25(0x1F1, 0xF)
    Sleep(50)
    OP_25(0x1F1, 0x14)
    Sleep(50)
    OP_25(0x1F1, 0x19)
    Sleep(50)
    OP_25(0x1F1, 0x1E)
    Sleep(50)
    OP_25(0x1F1, 0x23)
    Sleep(50)
    OP_25(0x1F1, 0x28)
    Sleep(50)
    OP_25(0x1F1, 0x2D)
    Sleep(50)
    OP_25(0x1F1, 0x32)
    Sleep(50)
    OP_25(0x1F1, 0x37)
    Sleep(50)
    OP_25(0x1F1, 0x3C)
    Sleep(50)
    OP_25(0x1F1, 0x41)
    Sleep(50)
    OP_25(0x1F1, 0x46)
    Return()

    # Function_80_99D2 end

    def Function_81_9A2D(): pass

    label("Function_81_9A2D")

    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(1000)
    OP_9B(0x0, 0xFE, 0x0, 0x2AF8, 0x7D0, 0x1)
    Return()

    # Function_81_9A2D end

    def Function_82_9A47(): pass

    label("Function_82_9A47")

    Sleep(300)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(900)
    OP_9B(0x0, 0xFE, 0x0, 0x2AF8, 0x7D0, 0x1)
    Return()

    # Function_82_9A47 end

    def Function_83_9A64(): pass

    label("Function_83_9A64")

    Sleep(300)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(800)
    OP_9B(0x0, 0xFE, 0x0, 0x2AF8, 0x7D0, 0x1)
    Return()

    # Function_83_9A64 end

    def Function_84_9A81(): pass

    label("Function_84_9A81")

    Sleep(500)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x2AF8, 0x7D0, 0x1)
    Return()

    # Function_84_9A81 end

    def Function_85_9A9B(): pass

    label("Function_85_9A9B")

    Sleep(400)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    OP_9B(0x0, 0xFE, 0x0, 0x2AF8, 0x7D0, 0x1)
    Return()

    # Function_85_9A9B end

    def Function_86_9AB8(): pass

    label("Function_86_9AB8")

    OP_96(0xFE, 0xFFFF4480, 0x251C, 0x4268, 0xBB8, 0x1)
    OP_96(0xFE, 0xFFFF4480, 0x2328, 0x4268, 0x7D0, 0x1)
    OP_96(0xFE, 0xFFFF4480, 0x2134, 0x4268, 0x3E8, 0x1)
    Return()

    # Function_86_9AB8 end

    def Function_87_9AF5(): pass

    label("Function_87_9AF5")

    Return()

    # Function_87_9AF5 end

    def Function_88_9AF6(): pass

    label("Function_88_9AF6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9B10")
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_88_9AF6")

    label("loc_9B10")

    Return()

    # Function_88_9AF6 end

    def Function_89_9B11(): pass

    label("Function_89_9B11")

    SetMapObjFrame(0xF, "Null_fream", 0x2, "start")
    Sleep(20000)
    SetMapObjFrame(0xF, "Null_fream", 0x2, "loop")
    Return()

    # Function_89_9B11 end

    def Function_90_9B3C(): pass

    label("Function_90_9B3C")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch05300.itc", 0x1E)
    ClearChrFlags(0x16, 0x80)
    SetChrChipByIndex(0x16, 0x1E)
    SetChrPos(0x16, -9000, 0, -500, 270)
    OP_68(-37710, 1000, 350, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19060, 0)
    SetChrPos(0x101, -41980, 0, 500, 90)
    SetChrPos(0x102, -42590, 0, -900, 90)
    SetChrPos(0x109, -42700, 0, 1300, 90)
    SetChrPos(0x105, -44040, 0, -1300, 90)
    SetChrPos(0x104, -43990, 0, 300, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01300.itp")
    OP_0D()
    OP_68(-34660, 1000, -430, 5000)

    def lambda_9C38():
        OP_97(0xFE, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9C38)
    Sleep(50)

    def lambda_9C55():
        OP_97(0xFE, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9C55)
    Sleep(50)

    def lambda_9C72():
        OP_97(0xFE, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9C72)
    Sleep(50)

    def lambda_9C8F():
        OP_97(0xFE, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9C8F)
    Sleep(50)

    def lambda_9CAC():
        OP_97(0xFE, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9CAC)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    OP_6F(0x1)
    Sleep(500)

    NpcTalk(
        0x16,
        "Female voice",
        "…… Lloyd ……! Is it?\x02",
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

    ChrTalk(
        0x101,
        "#00002FAh……!\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-9210, 1000, -500, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19060, 0)
    OP_0D()
    Sleep(800)
    OP_68(-23280, 1000, -240, 5000)
    MoveCamera(44, 25, 0, 5000)
    OP_6E(500, 5000)
    SetCameraDistance(17390, 5000)

    def lambda_9DDD():
        OP_95(0xFE, -21270, 0, -10, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_9DDD)
    Sleep(50)

    def lambda_9DFA():
        OP_97(0xFE, 0x2AF8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9DFA)
    Sleep(50)

    def lambda_9E17():
        OP_97(0xFE, 0x2AF8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9E17)
    Sleep(50)

    def lambda_9E34():
        OP_97(0xFE, 0x2AF8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9E34)
    Sleep(50)

    def lambda_9E51():
        OP_97(0xFE, 0x2AF8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9E51)
    Sleep(50)

    def lambda_9E6E():
        OP_97(0xFE, 0x2AF8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9E6E)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x16, 1)

    ChrTalk(
        0x101,
        (
            "#6P#00009FCecil姉……\x01",
            "Hello, I saw you suddenly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#11P#01300FHuh … … Well, Lloyd.\x02\x03",
            "#01309FEllie, Randy and you\x01",
            "Noel also ….\x01",
            "Everyone was doing well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00100FHuhu, I have not been to a long time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00309Fお久しぶりッス、Cecilさん！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#10109FHuh, it's been a long time since it's been a while.\x02\x03",
            "#10100FI was a cult incident\x01",
            "When the hospital was attacked\x01",
            "It was the first time since we met.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#11P#01309FHehe … … That was right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10302FOh, is this person your sister rumor?\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x16,
        (
            "#11P#01305FOh, it looks like there are some unfamiliar children ….\x02\x03",
            "#01300FMaybe, Noel and you\x01",
            "I wonder if it will be a new member of the rumor?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FHuh, I guess it will be like that.\x02\x03",
            "#10302FI am Wadi Hemisphere.\x01",
            "Thank you in the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#11P#01309FHehe, please.\x02\x03",
            "#01300FWell then …\x01",
            "Let me introduce myself again.\x02",
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
        0x16,
        (
            "This week\x01",
            "Working at Ursula Hospital,\x01",
            "看護師のCecil・ノイエスです。\x02\x03",
            "Hehe, my lovely little brother Lloyd,\x01",
            "Thank you.\x02",
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
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00006FCecil姉ってば……\x01",
            "Strictly it is not my sister?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#6P#00000FKohon, er … ….\x01",
            "childrenのころから何かと\x01",
            "People who are indebted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "#11P#01306FAlready it gets shy as Lloyd's.\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(500)

    ChrTalk(
        0x101,
        "#6P#00012FWell, you are not embarrassed.\x02",
    )

    CloseMessageWindow()
    OP_93(0x16, 0xE1, 0x1F4)
    Sleep(1000)
    OP_93(0x16, 0x13B, 0x1F4)
    Sleep(1000)
    OP_93(0x16, 0x10E, 0x1F4)
    Sleep(1000)

    ChrTalk(
        0x16,
        (
            "#11P#01304Fうーん、Even so ……\x01",
            "Waji also Noel\x01",
            "Very beautiful.\x02\x03",
            "#01300FLloyd, it is time to go\x01",
            "Who are you with?\x01",
            "Did anyone decide?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10105FOkay! Is it?\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00006FCecil姉……前にも言ったけど、\x01",
            "The support department is not like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#11P#01305FHa ha … that's right.\x01",
            "I did not care enough what I did.\x02\x03",
            "#01303FTio is not here at this time\x01",
            "It is unfair to talk like that.\x02\x03",
            "#01300FSince Tio came back,\x01",
            "Pick a partner slowly … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00011FThat's why … ….\x01",
            "Why is that! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00109FHehuu, what is it?\x01",
            "Cecilさんを見ると安心するわね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00309FOh, natural seems to be alive.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00006FPlease also be on the side of the tukkom side ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#11P#01304Fふふ……Even so,\x01",
            "I have not been away for so long\x01",
            "It feels nostalgic for quite some time.\x02\x03",
            "#01300FJust I am having a break, too.\x01",
            "I wonder if you can have a cup of tea together if you like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00004FWell then, I have a lot of trouble … …\x02\x03",
            "#00002FEveryone, in words\x01",
            "Would you let me downright?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10109FYes, we will be with you!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 1)
    NewScene("t1510", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_90_9B3C end

    def Function_91_A83B(): pass

    label("Function_91_A83B")

    Return()

    # Function_91_A83B end

    def Function_92_A83C(): pass

    label("Function_92_A83C")

    EventBegin(0x0)
    Fade(500)
    OP_68(-47260, 1700, -1110, 0)
    MoveCamera(44, 24, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x106, -48500, 0, -230, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_AA4E")
    SetChrPos(0x101, -46100, 0, -230, 90)
    SetChrPos(0x102, -46300, 0, -1330, 90)
    SetChrPos(0x103, -46300, 0, 870, 90)
    SetChrPos(0x104, -48400, 0, 1030, 90)

    def lambda_A8D4():
        OP_95(0xFE, -44100, 0, -230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A8D4)

    def lambda_A8EE():
        OP_95(0xFE, -44300, 0, -1330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A8EE)

    def lambda_A908():
        OP_95(0xFE, -44300, 0, 870, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A908)

    def lambda_A922():
        OP_95(0xFE, -46400, 0, 1030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A922)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A972")
    SetChrPos(0x109, -48000, 0, -1070, 90)

    def lambda_A95D():
        OP_95(0xFE, -46000, 0, -1070, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A95D)

    label("loc_A972")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A9AD")
    SetChrPos(0x105, -48000, 0, -1070, 90)

    def lambda_A998():
        OP_95(0xFE, -46000, 0, -1070, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A998)

    label("loc_A9AD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A9E8")
    SetChrPos(0x10A, -48000, 0, -1070, 90)

    def lambda_A9D3():
        OP_95(0xFE, -46000, 0, -1070, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_A9D3)

    label("loc_A9E8")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AA21")
    WaitChrThread(0x109, 1)

    label("loc_AA21")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AA35")
    WaitChrThread(0x105, 1)

    label("loc_AA35")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AA49")
    WaitChrThread(0x10A, 1)

    label("loc_AA49")

    Jump("loc_AD3A")

    label("loc_AA4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_AB5C")
    SetChrPos(0x101, -46100, 0, -230, 90)
    SetChrPos(0x103, -46300, 0, -1330, 90)
    SetChrPos(0x104, -46300, 0, 870, 90)
    SetChrPos(0x105, -48400, 0, 1030, 90)
    SetChrPos(0x109, -48000, 0, -1070, 90)

    def lambda_AAB1():
        OP_95(0xFE, -44100, 0, -230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AAB1)

    def lambda_AACB():
        OP_95(0xFE, -44300, 0, -1330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AACB)

    def lambda_AAE5():
        OP_95(0xFE, -44300, 0, 870, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AAE5)

    def lambda_AAFF():
        OP_95(0xFE, -46400, 0, 1030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_AAFF)

    def lambda_AB19():
        OP_95(0xFE, -46000, 0, -1070, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_AB19)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x109, 1)
    Jump("loc_AD3A")

    label("loc_AB5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_AC6A")
    SetChrPos(0x101, -46100, 0, -230, 90)
    SetChrPos(0x103, -46300, 0, -1330, 90)
    SetChrPos(0x104, -46300, 0, 870, 90)
    SetChrPos(0x107, -48800, 0, 1030, 90)
    SetChrPos(0x105, -48300, 0, -1070, 90)

    def lambda_ABBF():
        OP_95(0xFE, -44100, 0, -230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_ABBF)

    def lambda_ABD9():
        OP_95(0xFE, -44300, 0, -1330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_ABD9)

    def lambda_ABF3():
        OP_95(0xFE, -44300, 0, 870, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_ABF3)

    def lambda_AC0D():
        OP_95(0xFE, -46800, 0, 1030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_AC0D)

    def lambda_AC27():
        OP_95(0xFE, -46300, 0, -1070, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_AC27)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x107, 1)
    WaitChrThread(0x105, 1)
    Jump("loc_AD3A")

    label("loc_AC6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_AD3A")
    SetChrPos(0x101, -46100, 0, -230, 90)
    SetChrPos(0x103, -46300, 0, -1330, 90)
    SetChrPos(0x105, -46300, 0, 870, 90)
    SetChrPos(0x107, -48800, 0, 1030, 90)

    def lambda_ACBC():
        OP_95(0xFE, -44100, 0, -230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_ACBC)

    def lambda_ACD6():
        OP_95(0xFE, -44300, 0, -1330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_ACD6)

    def lambda_ACF0():
        OP_95(0xFE, -44300, 0, 870, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_ACF0)

    def lambda_AD0A():
        OP_95(0xFE, -46800, 0, 1030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_AD0A)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x107, 1)

    label("loc_AD3A")


    ChrTalk(
        0x106,
        (
            "#6P#10708FI am sorry, I am outside the hospital\x01",
            "I will be waiting.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_AEE5")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ADF8")

    def lambda_AD99():
        TurnDirection(0x109, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_AD99)
    Sleep(50)

    def lambda_ADA9():
        TurnDirection(0x104, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_ADA9)
    Sleep(50)

    def lambda_ADB9():
        TurnDirection(0x103, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_ADB9)
    Sleep(50)

    def lambda_ADC9():
        TurnDirection(0x102, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_ADC9)
    Sleep(50)

    def lambda_ADD9():
        TurnDirection(0x101, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_ADD9)
    Sleep(50)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)

    label("loc_ADF8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AE6C")

    def lambda_AE0D():
        TurnDirection(0x105, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_AE0D)
    Sleep(50)

    def lambda_AE1D():
        TurnDirection(0x104, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_AE1D)
    Sleep(50)

    def lambda_AE2D():
        TurnDirection(0x103, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_AE2D)
    Sleep(50)

    def lambda_AE3D():
        TurnDirection(0x102, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_AE3D)
    Sleep(50)

    def lambda_AE4D():
        TurnDirection(0x101, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AE4D)
    Sleep(50)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)

    label("loc_AE6C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AEE0")

    def lambda_AE81():
        TurnDirection(0x10A, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_AE81)
    Sleep(50)

    def lambda_AE91():
        TurnDirection(0x104, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_AE91)
    Sleep(50)

    def lambda_AEA1():
        TurnDirection(0x103, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_AEA1)
    Sleep(50)

    def lambda_AEB1():
        TurnDirection(0x102, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_AEB1)
    Sleep(50)

    def lambda_AEC1():
        TurnDirection(0x101, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AEC1)
    Sleep(50)
    WaitChrThread(0x10A, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)

    label("loc_AEE0")

    Jump("loc_B022")

    label("loc_AEE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_AF57")

    def lambda_AEF3():
        TurnDirection(0x109, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_AEF3)
    Sleep(50)

    def lambda_AF03():
        TurnDirection(0x105, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_AF03)
    Sleep(50)

    def lambda_AF13():
        TurnDirection(0x104, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_AF13)
    Sleep(50)

    def lambda_AF23():
        TurnDirection(0x103, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_AF23)
    Sleep(50)

    def lambda_AF33():
        TurnDirection(0x101, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AF33)
    Sleep(50)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x101, 0)
    Jump("loc_B022")

    label("loc_AF57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_AFC9")

    def lambda_AF65():
        TurnDirection(0x107, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_AF65)
    Sleep(50)

    def lambda_AF75():
        TurnDirection(0x105, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_AF75)
    Sleep(50)

    def lambda_AF85():
        TurnDirection(0x104, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_AF85)
    Sleep(50)

    def lambda_AF95():
        TurnDirection(0x103, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_AF95)
    Sleep(50)

    def lambda_AFA5():
        TurnDirection(0x101, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AFA5)
    Sleep(50)
    WaitChrThread(0x107, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x101, 0)
    Jump("loc_B022")

    label("loc_AFC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_B022")

    def lambda_AFD7():
        TurnDirection(0x107, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_AFD7)
    Sleep(50)

    def lambda_AFE7():
        TurnDirection(0x105, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_AFE7)
    Sleep(50)

    def lambda_AFF7():
        TurnDirection(0x103, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_AFF7)
    Sleep(50)

    def lambda_B007():
        TurnDirection(0x101, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B007)
    Sleep(50)
    WaitChrThread(0x107, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x101, 0)

    label("loc_B022")


    ChrTalk(
        0x101,
        (
            "#11P#00003FOh, I understand.\x01",
            "See you later.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_32(0xFF, 0xF9, 0x0)
    SetScenarioFlags(0x1AD, 2)
    RemoveParty(0x5, 0xFF)
    ClearChrFlags(0xD, 0x80)
    ModifyEventFlags(0, 4, 0x80)
    ModifyEventFlags(1, 5, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B08C")
    RemoveParty(0x6, 0xFF)
    AddParty(0x6, 0xFF, 0xFF)

    label("loc_B08C")

    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -44100, 0, -230, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_B0BE")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_B0BE")

    EventEnd(0x5)
    Return()

    # Function_92_A83C end

    def Function_93_B0C1(): pass

    label("Function_93_B0C1")

    EventBegin(0x0)
    Fade(500)
    OP_68(-49470, 1000, -560, 0)
    MoveCamera(46, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18720, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_B1B5")
    SetChrPos(0x101, -48020, 0, -230, 270)
    SetChrPos(0x102, -46820, 0, -830, 270)
    SetChrPos(0x103, -46820, 0, 370, 270)
    SetChrPos(0x104, -45620, 0, -1030, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B164")
    SetChrPos(0x109, -45620, 0, 570, 270)

    label("loc_B164")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B185")
    SetChrPos(0x105, -45620, 0, 570, 270)

    label("loc_B185")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B1A6")
    SetChrPos(0x10A, -45620, 0, 570, 270)

    label("loc_B1A6")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_B2DC")

    label("loc_B1B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_B222")
    SetChrPos(0x101, -48020, 0, -230, 270)
    SetChrPos(0x103, -46820, 0, -830, 270)
    SetChrPos(0x104, -46820, 0, 370, 270)
    SetChrPos(0x109, -45620, 0, -1030, 270)
    SetChrPos(0x105, -45620, 0, 570, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_B2DC")

    label("loc_B222")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_B28F")
    SetChrPos(0x101, -48020, 0, -230, 270)
    SetChrPos(0x103, -46820, 0, -830, 270)
    SetChrPos(0x104, -46820, 0, 370, 270)
    SetChrPos(0x105, -45620, 0, 570, 270)
    SetChrPos(0x107, -45320, 0, -1230, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_B2DC")

    label("loc_B28F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_B2DC")
    SetChrPos(0x101, -48020, 0, -230, 270)
    SetChrPos(0x103, -46820, 0, -830, 270)
    SetChrPos(0x105, -46820, 0, 370, 270)
    SetChrPos(0x107, -45320, 0, -1230, 270)

    label("loc_B2DC")

    OP_4B(0xD, 0xFF)
    OP_0D()

    ChrTalk(
        0xD,
        (
            "#6P#10702FWelcome back, everyone.\x01",
            "… …. Did you do business errand?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00000FOh, let's go.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearScenarioFlags(0x1AD, 2)
    ModifyEventFlags(1, 4, 0x80)
    ModifyEventFlags(0, 5, 0x80)
    SetChrFlags(0xD, 0x80)
    AddParty(0x5, 0xFF, 0xFF)
    SetChrChipPat(0x5, 0x1, 0x20)
    LoadChrChipPat()
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -48820, 0, -230, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_B3A2")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_B3A2")

    EventEnd(0x5)
    Return()

    # Function_93_B0C1 end

    def Function_94_B3A5(): pass

    label("Function_94_B3A5")

    EventBegin(0x0)
    Fade(500)
    OP_68(-46080, 1000, -230, 0)
    MoveCamera(51, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, -50520, 0, -230, 90)
    SetChrPos(0x102, -50500, 0, 1110, 90)
    SetChrPos(0x103, -50500, 0, -1420, 90)
    SetChrPos(0x104, -51500, 0, 1110, 90)
    SetChrPos(0x106, -51500, 0, -230, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B450")
    SetChrPos(0x109, -51500, 0, -1420, 90)

    label("loc_B450")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B471")
    SetChrPos(0x105, -51500, 0, -1420, 90)

    label("loc_B471")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B492")
    SetChrPos(0x10A, -51500, 0, -1420, 90)

    label("loc_B492")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    def lambda_B4AB():
        OP_95(0xFE, -44520, 0, -230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B4AB)
    Sleep(30)

    def lambda_B4C8():
        OP_95(0xFE, -44520, 0, 1110, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B4C8)
    Sleep(30)

    def lambda_B4E5():
        OP_95(0xFE, -44520, 0, -1420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B4E5)
    Sleep(30)

    def lambda_B502():
        OP_95(0xFE, -45820, 0, 1110, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B502)
    Sleep(30)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B544")

    def lambda_B52F():
        OP_95(0xFE, -45820, 0, -1420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B52F)

    label("loc_B544")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B56E")

    def lambda_B559():
        OP_95(0xFE, -45820, 0, -1420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B559)

    label("loc_B56E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B598")

    def lambda_B583():
        OP_95(0xFE, -45820, 0, -1420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_B583)

    label("loc_B598")

    Sleep(30)

    def lambda_B5A0():
        OP_95(0xFE, -48500, 0, -230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_B5A0)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 1)

    ChrTalk(
        0x106,
        (
            "#6P#10703FWell then, everyone.\x01",
            "I am here ……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    def lambda_B5F9():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B5F9)

    def lambda_B606():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B606)

    def lambda_B613():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B613)

    def lambda_B620():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B620)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B645")

    def lambda_B63D():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B63D)

    label("loc_B645")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B662")

    def lambda_B65A():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B65A)

    label("loc_B662")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B67F")

    def lambda_B677():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_B677)

    label("loc_B67F")

    WaitChrThread(0x104, 1)
    Sleep(500)

    ChrTalk(
        0x102,
        "#11P#00105FLishaさん……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#00303FFuu … … Well the way it is.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#11P#00003F……なあ、Lisha。\x02\x03",
            "#00000FAt the very least Ilia's voice\x01",
            "Will not you ask?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x106, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x106,
        "#6P#10705F…………. Eh ……………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00003FUntil you put all the keri\x01",
            "I will not see Mr. Iria ….\x02\x03",
            "I understand your feelings,\x01",
            "I also want to respect it … ….\x02\x03",
            "#00000FAt least, from outside the hospital room\x01",
            "You and Iria are talking with us\x01",
            "Is not it good to listen?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#6P#10705FAh……\x02\x03",
            "#10708F……………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)

    ChrTalk(
        0x104,
        (
            "#5P#00302FYou know, that much\x01",
            "You can have a reward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#00203FFrom here onwards, there is still difficulty\x01",
            "The likelihood of waiting is likely to be high.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00100FListening to the voice of an important person\x01",
            "I think that it will surely become a power.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BA41")

    ChrTalk(
        0x109,
        (
            "#11P#10105Fそうですよ、Lishaさん！\x02\x03",
            "#10101FLishaさんがいるって事は\x01",
            "I will be careful not to be bald!\x02\x03",
            "#10104Fその、あたしもFrancと会えて\x01",
            "I was energized much better … ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BA41")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BAFC")

    ChrTalk(
        0x105,
        (
            "#11P#10404FHuh, I guess it's okay?\x02\x03",
            "#10400FI have to meet again in the real sense\x01",
            "I will be able to defend your vows.\x02\x03",
            "#10408F…… I really can not see you\x01",
            "Sometimes it's too late?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BAFC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BBAE")

    ChrTalk(
        0x10A,
        (
            "#11P#00603F\"Silver#2RIn#\"──\x01",
            "いや、Lisha・マオ。\x02\x03",
            "#00600FI wonder what a policeman I say\x01",
            "It is emergency now.\x02\x03",
            "#00602FAt least not to have regrets\x01",
            "You should do it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BBAE")

    Sleep(1500)
    OP_64(0x106)

    ChrTalk(
        0x106,
        (
            "#6P#10704F……Everyone.\x01",
            "Thank you very much.\x02\x03",
            "#10702F… … with your words …\x01",
            "Please let me stay with you until the hospital room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00002FAh……!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00100FYes, I understood …!\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x1AD, 3)
    ModifyEventFlags(0, 6, 0x80)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -44520, 0, -230, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_94_B3A5 end

    def Function_95_BCA2(): pass

    label("Function_95_BCA2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_C3C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BCC0")
    Call(0, 96)
    Jump("loc_C3C3")

    label("loc_BCC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C1FE")

    ChrTalk(
        0x10,
        (
            "#01300FLloyd …… Arios\x01",
            "You seem to break it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, I fought quite a hard battle though ….\x01",
            "I owe it to my friends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FIt is a good prospector who increases together\x01",
            "It was also a \"wall\" to overcome\x01",
            "Mr. Arios …\x02\x03",
            "#00100FTo be honest, if anyone alone is missing\x01",
            "I think that he never made an enemy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00304F… they are.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#01309FHuhu, you guys are all\x01",
            "What is \"Support Division\"?\x01",
            "I think you can be proud enough.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x10)

    ChrTalk(
        0x10,
        (
            "#01304FWhat I talked with Arios\x01",
            "I did not find that much ….\x02\x03",
            "From that long ago,\x01",
            "Heavy things in your heart\x01",
            "I feel like I was carrying on the back.\x02\x03",
            "#01308FShizuku-chan and his wife,\x01",
            "Mr. Guy carries with himself one thing ……\x01",
            "It was almost impossible to see.\x02\x03",
            "#01300FBecause he is an endlessly strong man,\x01",
            "To depend on someone\x01",
            "I wonder if I could not do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FLoneliness due to strength ……\x01",
            "Surely it may be so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#01302FHuhu, but with you guys\x01",
            "By fighting and defeating at full power,\x01",
            "I think that it was definitely released.\x02\x03",
            "#01304FMr. Guy probably was worried,\x01",
            "As his fiancé, I will instead\x01",
            "I will thank you.\x02\x03",
            "#01309FGai's close friend, Arios\x01",
            "Thank you for rescuing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FHaha … … You are welcome.\x02\x03",
            "#00000FAll I have to do is recover Ka'aa.\x01",
            "待っていてくれ、Cecil姉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#01300FYes, I understand.\x02\x03",
            "#01303FLloyd, everyone … ….\x01",
            "Take care until the end.\x02\x03",
            "#01302FWith Kia-chan\x01",
            "To return with a smile,\x01",
            "Because I am praying here.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AC, 5)
    Jump("loc_C3C3")

    label("loc_C1FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C34F")

    ChrTalk(
        0x10,
        (
            "#01303FLloyd, everyone … ….\x01",
            "Take care until the end.\x02\x03",
            "#01302FWith Kia-chan\x01",
            "To return with a smile,\x01",
            "Because I am praying here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, please wait.\x02\x03",
            "#00003F(… the truth of the big brother incident\x01",
            "Tomorrow turned out ….\x01",
            "Now it seems not to say. )\x02\x03",
            "#00008F(Mr. Ian also revisited\x01",
            "I have to ask the circumstances … …)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_C3C3")

    label("loc_C34F")


    ChrTalk(
        0x10,
        (
            "#01303FLloyd, everyone … ….\x01",
            "Take care until the end.\x02\x03",
            "With Kia-chan\x01",
            "To return with a smile,\x01",
            "Because I am praying here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C3C3")

    Jump("loc_C654")

    label("loc_C3C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_C62F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C3E3")
    Call(0, 96)
    Jump("loc_C62A")

    label("loc_C3E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C5BA")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C50A")
    TurnDirection(0x10, 0x106, 0)

    ChrTalk(
        0x10,
        (
            "#01300FLishaさん、あなたもどうか\x01",
            "Please be careful.\x02\x03",
            "#01304FAlthough Iria is not put out directly in the mouth,\x01",
            "You always know\x01",
            "I think that I care.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C4CF")

    ChrTalk(
        0x106,
        "#10708F……I agree……\x02",
    )

    CloseMessageWindow()
    Jump("loc_C505")

    label("loc_C4CF")


    ChrTalk(
        0x106,
        (
            "#10702FYes……!\x01",
            "I promise to surely return safely.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C505")

    Jump("loc_C5B2")

    label("loc_C50A")


    ChrTalk(
        0x10,
        (
            "#01300FWith Ka'aa,\x01",
            "A promise that everyone will come home safely …\x01",
            "Please never forget it.\x02\x03",
            "#01304FAs long as there is that promise,\x01",
            "I am here for everyone's return\x01",
            "I think I can wait.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C5B2")

    SetScenarioFlags(0x0, 7)
    Jump("loc_C62A")

    label("loc_C5BA")


    ChrTalk(
        0x10,
        (
            "#01300FI am here,\x01",
            "I am waiting for everyone's return.\x02\x03",
            "#01304FGoddess' s protection will be given to Lloyd's\x01",
            "I hope to see you there ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C62A")

    Jump("loc_C654")

    label("loc_C62F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_C63D")
    Jump("loc_C654")

    label("loc_C63D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_C64B")
    Jump("loc_C654")

    label("loc_C64B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_C654")

    label("loc_C654")

    TalkEnd(0xFE)
    Return()

    # Function_95_BCA2 end

    def Function_96_C658(): pass

    label("Function_96_C658")

    EventBegin(0x0)
    Fade(500)
    OP_68(-24280, 400, -23490, 0)
    MoveCamera(32, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15570, 0)
    SetChrPos(0x101, -24090, -1000, -22920, 180)
    SetChrPos(0x102, -25290, -1000, -22000, 180)
    SetChrPos(0x103, -22850, -1000, -22000, 225)
    SetChrPos(0x104, -24260, -1000, -21430, 180)
    SetChrPos(0xF4, -22050, -1000, -22590, 225)
    SetChrPos(0xF5, -22790, -1000, -20810, 225)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrSubChip(0x10, 0x0)
    OP_93(0x10, 0xB4, 0x0)
    OP_0D()

    ChrTalk(
        0x101,
        "#5P#00000FCecil姉……ここにいたのか。\x02",
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x10, 0x101, 300)

    ChrTalk(
        0x10,
        (
            "#12P#01300FYeah, that suddenly\x01",
            "I was surprised because it appeared … …\x02\x03",
            "#01304F…… But it is a mysterious tree.\x02\x03",
            "Although it is obviously heterogeneous,\x01",
            "Somewhat lovely … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00108F(Bell said that \"Taiki\"\x01",
            "\"Ka'a-chan itself\" and\x01",
            "I was saying … …)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C8A2")

    ChrTalk(
        0x105,
        (
            "#11P#10403F(Even though she feels it\x01",
            "It may not be strange. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C969")

    label("loc_C8A2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C909")

    ChrTalk(
        0x109,
        (
            "#11P#10103F（Cecilさんならそれを感じても\x01",
            "It may not be strange. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C969")

    label("loc_C909")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C969")

    ChrTalk(
        0x106,
        (
            "#11P#10703F（Cecilさんならそれを感じても\x01",
            "It may not be strange. )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C969")

    OP_63(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x10)

    ChrTalk(
        0x10,
        (
            "#12P#01303FLloyd, and everyone ……\x02\x03",
            "#01301F… … are you going to that place?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00003F……Ah.\x02\x03",
            "#00001FThat \"Taiki\" has all the truth ……\x01",
            "Ka'aa is waiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00101FWhatever the danger in the future,\x01",
            "We have to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#12P#01308Fso……\x02",
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x10)

    ChrTalk(
        0x10,
        (
            "#12P#01303FIf true, Lloyd's\x01",
            "I do not want you to take such a risk ……\x02\x03",
            "#01308FBecause I have lost an important person once.\x01",
            "…… I do not want to taste such feelings anymore.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CB7F")

    ChrTalk(
        0x106,
        "#11P#10705FCecilさん……\x02",
    )

    CloseMessageWindow()
    Jump("loc_CBEE")

    label("loc_CB7F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CBB9")

    ChrTalk(
        0x10A,
        "#11P#00608F…………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_CBEE")

    label("loc_CBB9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CBEE")

    ChrTalk(
        0x105,
        "#11P#10408F…………………………\x02",
    )

    CloseMessageWindow()

    label("loc_CBEE")


    ChrTalk(
        0x10,
        (
            "#12P#01303F…… But if Mr. Guy was alive ……\x01",
            "Surely with Lloyd\x01",
            "I think I was trying the same thing.\x02\x03",
            "#01302FWhatever danger there,\x01",
            "To protect precious things\x01",
            "I think I jumped in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00000FCecil姉……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#12P#01304F…… So everyone,\x01",
            "Promise only one.\x02\x03",
            "#01300FIncluding Kia - chan,\x01",
            "All things come home safely.\x02\x03",
            "#01309FAs long as there is that promise,\x01",
            "I am here for everyone's return\x01",
            "I think I can wait.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00005FCecil姉……\x02\x03",
            "#00004F……I understood.\x01",
            "Please wait for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#00200FTo a considerable challenge\x01",
            "Will it be … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00102FYeah, regain Kaea-chan\x01",
            "I will definitely come back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00309FThat Arios' Osan also\x01",
            "Please do not hit me.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CED7")

    ChrTalk(
        0x10A,
        "#11P#00602FOh, of course.\x02",
    )

    CloseMessageWindow()
    Jump("loc_CF40")

    label("loc_CED7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CF0F")

    ChrTalk(
        0x109,
        "#11P#10102FYeah, you are right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_CF40")

    label("loc_CF0F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CF40")

    ChrTalk(
        0x105,
        "#11P#10402FHuh, that's right.\x02",
    )

    CloseMessageWindow()

    label("loc_CF40")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x6D), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D1D0")

    ChrTalk(
        0x10,
        (
            "#12P#01304F…, Huhu, thank you everyone.\x01",
            "I can finally be relieved with this.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x10)

    ChrTalk(
        0x10,
        (
            "#12P#01309FWell then, as a sign of promise\x01",
            "Wondering if this should be handed over.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '勇士之心'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('勇士之心', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1DE, 2)

    ChrTalk(
        0x101,
        "#5P#00005Fthis is……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#12P#01300FWhen I take the exam of a nurse\x01",
            "Mr. Guy handed in it.\x02\x03",
            "#01304FWhen it's hot, when you clench it\x01",
            "Wonder and courage came … …\x01",
            "Such an amulet.\x02\x03",
            "#01300FIt's so important,\x01",
            "Please come back safely and come back safely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00000F… Ah, I understand.\x01",
            "I will thank you for giving thanks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#12P#01309FHehe, to the Lloyd's\x01",
            "Goddess' s protection\x01",
            "I hope to see you there ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D254")

    label("loc_D1D0")


    ChrTalk(
        0x10,
        (
            "#12P#01304F…, Huhu, thank you everyone.\x01",
            "I can finally be relieved with this.\x02\x03",
            "#01309Fロイドたちに、Goddess' s protection\x01",
            "I hope to see you there ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D254")

    OP_5A()
    SetScenarioFlags(0x1AC, 4)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -24090, -1000, -22920, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D29D")
    OP_E0(0x34, 0x0)

    label("loc_D29D")

    EventEnd(0x5)
    Return()

    # Function_96_C658 end

    def Function_97_D2A0(): pass

    label("Function_97_D2A0")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D32B")

    ChrTalk(
        0x101,
        (
            "#00000FFrancが準備を済ませるまで、\x01",
            "I can not leave the hospital.\x02\x03",
            "Iria and the Donovan police\x01",
            "Let's get on well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D32B")

    Sleep(50)
    SetChrPos(0x0, -61000, 0, 0, 90)
    EventEnd(0x4)
    Return()

    # Function_97_D2A0 end

    def Function_98_D342(): pass

    label("Function_98_D342")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "St.Ursula \x01",
            "Medical College\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_98_D342 end

    def Function_99_D398(): pass

    label("Function_99_D398")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Medical College\x01",
            "~ Buffet \"Lecce\" ~\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_99_D398 end

    SaveToFile()

Try(main)
