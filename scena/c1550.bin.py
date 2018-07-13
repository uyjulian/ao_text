from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1550.bin",                # FileName
        "c1550",                    # MapName
        "c1550",                    # Location
        0x00B0,                     # MapIndex
        "ed7151",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 176, 0, 3, 0, 4],
    )

    BuildStringList((
        "c1550",                  # 0
        "Receptionist Lanfei",    # 1
        "Receptionist Korinna",   # 2
        "Guard Bills",            # 3
        "Guard Wong",             # 4
        "Shizuku",                # 5
        "Chief Morett",           # 6
        "Receptionist Lilie",     # 7
        "Vice Chief Pierre",      # 8
        "Researcher David",       # 9
        "Policeman",              # 10
        "Policeman",              # 11
        "Princess Klaudia",       # 12
        "Secretary Lechter",      # 13
        "Republican Army Officer",# 14
        "Imperial Army Officer",  # 15
        "President Rocksmith",    # 16
        "Captain Julia",          # 17
        "Major Mueller",          # 18
        "Archduke Albert",        # 19
        "Archduke House Guard",   # 20
        "Butler",                 # 21
        "Butler",                 # 22
        "Maid",                   # 23
        "Maid",                   # 24
        "Maid",                   # 25
        "Maid",                   # 26
        "Maid",                   # 27
        "Maid",                   # 28
        "Maid",                   # 29
        "City Hall Staffer",      # 30
        "City Hall Staffer",      # 31
        "Policeman",              # 32
        "Policeman",              # 33
        "Royal Guard Soldier",    # 34
        "Sieg",                   # 35
        "Mayor Dieter",           # 36
        "Prince Olivert",         # 37
        "Chairman MacDowell",     # 38
        "Detective Dudley",       # 39
        "Chancellor Osborne",     # 40
        "Congressman",            # 41
        "Congressman",            # 42
        "Congressman",            # 43
        "KeA",                    # 44
        "Secretary Arios",        # 45
        "Dummy",                  # 46
        "Lawyer Ian",             # 47
        "椅子",                   # 48
        "椅子",                   # 49
        "トンファー",             # 50
        "トンファー",             # 51
        "トンファーOBJ",          # 52
        "風呂敷",                 # 53
        "手紙",                   # 54
        "Laptop",                 # 55
        "State Guard Soldier - Man",# 56
        "State Guard Soldier - Man",# 57
        "State Guard Soldier - Man",# 58
        "State Guard Soldier - Man",# 59
        "SE制御",                 # 60
    ))

    AddCharChip((
        "chr/ch30000.itc",                   # 00
        "chr/ch11000.itc",                   # 01
        "chr/ch12400.itc",                   # 02
        "chr/ch41200.itc",                   # 03
        "chr/ch41000.itc",                   # 04
        "chr/ch11700.itc",                   # 05
        "chr/ch05410.itc",                   # 06
        "apl/ch51233.itc",                   # 07
        "chr/ch29400.itc",                   # 08
        "chr/ch27400.itc",                   # 09
        "chr/ch30500.itc",                   # 0A
        "chr/ch10902.itc",                   # 0B
        "chr/ch11002.itc",                   # 0C
        "chr/ch11102.itc",                   # 0D
        "chr/ch05802.itc",                   # 0E
        "chr/ch05902.itc",                   # 0F
        "chr/ch25600.itc",                   # 10
        "chr/ch25700.itc",                   # 11
        "chr/ch34500.itc",                   # 12
        "chr/ch25800.itc",                   # 13
        "chr/ch25900.itc",                   # 14
        "chr/ch11200.itc",                   # 15
        "chr/ch11300.itc",                   # 16
        "chr/ch11802.itc",                   # 17
        "chr/ch28600.itc",                   # 18
        "chr/ch28000.itc",                   # 19
        "chr/ch27900.itc",                   # 1A
        "chr/ch05602.itc",                   # 1B
        "chr/ch13802.itc",                   # 1C
        "chr/ch41600.itc",                   # 1D
        "chr/ch27902.itc",                   # 1E
        "chr/ch06402.itc",                   # 1F
        "chr/ch11712.itc",                   # 20
    ))

    DeclNpc(0,       300,     31700,   180,  389,  0x0, 0,   30,  0,   255, 255, 0,   42,  255,  0)
    DeclNpc(7110,    300,     32759,   90,   385,  0x0, 0,   10,  0,   0,   0,   0,   45,  255,  0)
    DeclNpc(3910,    0,       5050,    180,  385,  0x0, 0,   24,  0,   0,   0,   0,   46,  255,  0)
    DeclNpc(1700,    0,       4294945167, 180,  385,  0x0, 0,   24,  0,   0,   0,   0,   47,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   6,   0,   255, 255, 0,   48,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   9,   0,   255, 255, 0,   41,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   10,  0,   255, 255, 0,   40,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   31,  0,   255, 255, 0,   43,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   8,   0,   255, 255, 0,   44,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   1,   0,   255, 255, 0,   25,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   2,   0,   0,   0,   0,   39,  255,  0)
    DeclNpc(4294847157, 0,       103459,  270,  389,  0x0, 0,   3,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   4,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   5,   0,   0,   0,   0,   29,  255,  0)
    DeclNpc(2180,    0,       4294840386, 45,   389,  0x0, 0,   21,  0,   0,   0,   0,   9,   255,  0)
    DeclNpc(3180,    0,       4294840386, 45,   389,  0x0, 0,   22,  0,   0,   0,   0,   11,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   23,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   24,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   19,  0,   0,   0,   0,   26,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   20,  0,   0,   0,   0,   34,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   16,  0,   0,   0,   0,   14,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   17,  0,   0,   0,   0,   15,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   18,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   17,  0,   0,   0,   0,   28,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   18,  0,   0,   0,   0,   30,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   17,  0,   0,   0,   0,   31,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   16,  0,   0,   0,   0,   35,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   25,  0,   0,   0,   0,   32,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   26,  0,   0,   0,   0,   33,  255,  0)
    DeclNpc(103339,  0,       4294838407, 180,  389,  0x0, 0,   0,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(3849,    0,       899,     180,  389,  0x0, 0,   0,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   29,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   28,  0,   255, 255, 0,   20,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   27,  0,   255, 255, 0,   38,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   13,  0,   255, 255, 0,   36,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   14,  0,   255, 255, 0,   19,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    236,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 92,  109.0,                 -122.5,                -1.0,                  81.0,                  [0.1666666716337204,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -18.166667938232422,   40.833335876464844,    0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 137, 112.3499984741211,     -130.72999572753906,   -1.0,                  36.0,                  [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -37.45000076293945,    32.682498931884766,    0.20000001788139343,   1.0])

    DeclActor(80610,   0,       2930,    1000,    80610,   1500,    2930,    0x007C, 0,  138, 0x0000)
    DeclActor(86730,   0,       3250,    1000,    86730,   1500,    3250,    0x007C, 0,  138, 0x0000)
    DeclActor(4294915726, 0,       3070,    1000,    4294915726, 1500,    3070,    0x007C, 0,  139, 0x0000)

    ChipFrameInfo(2824, 0)                                       # 0

    ScpFunction((
        "Function_0_B08",          # 00, 0
        "Function_1_BB8",          # 01, 1
        "Function_2_C0B",          # 02, 2
        "Function_3_C5E",          # 03, 3
        "Function_4_1570",         # 04, 4
        "Function_5_1860",         # 05, 5
        "Function_6_18E6",         # 06, 6
        "Function_7_1904",         # 07, 7
        "Function_8_1E8A",         # 08, 8
        "Function_9_21C5",         # 09, 9
        "Function_10_242E",        # 0A, 10
        "Function_11_2DFE",        # 0B, 11
        "Function_12_2EF2",        # 0C, 12
        "Function_13_327B",        # 0D, 13
        "Function_14_377F",        # 0E, 14
        "Function_15_390F",        # 0F, 15
        "Function_16_3BDF",        # 10, 16
        "Function_17_3D14",        # 11, 17
        "Function_18_3DFE",        # 12, 18
        "Function_19_4C5D",        # 13, 19
        "Function_20_4D09",        # 14, 20
        "Function_21_4D8F",        # 15, 21
        "Function_22_5605",        # 16, 22
        "Function_23_58B5",        # 17, 23
        "Function_24_5AB1",        # 18, 24
        "Function_25_5B60",        # 19, 25
        "Function_26_5C04",        # 1A, 26
        "Function_27_5D3D",        # 1B, 27
        "Function_28_5F91",        # 1C, 28
        "Function_29_6095",        # 1D, 29
        "Function_30_6215",        # 1E, 30
        "Function_31_63C3",        # 1F, 31
        "Function_32_6501",        # 20, 32
        "Function_33_65BB",        # 21, 33
        "Function_34_66B3",        # 22, 34
        "Function_35_6B88",        # 23, 35
        "Function_36_6CBA",        # 24, 36
        "Function_37_6CC4",        # 25, 37
        "Function_38_7884",        # 26, 38
        "Function_39_788E",        # 27, 39
        "Function_40_7999",        # 28, 40
        "Function_41_7AF0",        # 29, 41
        "Function_42_7BAD",        # 2A, 42
        "Function_43_7DF8",        # 2B, 43
        "Function_44_7F73",        # 2C, 44
        "Function_45_80B9",        # 2D, 45
        "Function_46_8156",        # 2E, 46
        "Function_47_82CF",        # 2F, 47
        "Function_48_842A",        # 30, 48
        "Function_49_855C",        # 31, 49
        "Function_50_8A7B",        # 32, 50
        "Function_51_9BB0",        # 33, 51
        "Function_52_A868",        # 34, 52
        "Function_53_A86F",        # 35, 53
        "Function_54_A898",        # 36, 54
        "Function_55_B92D",        # 37, 55
        "Function_56_B9AC",        # 38, 56
        "Function_57_BA01",        # 39, 57
        "Function_58_BA56",        # 3A, 58
        "Function_59_BAAB",        # 3B, 59
        "Function_60_BB00",        # 3C, 60
        "Function_61_BB55",        # 3D, 61
        "Function_62_BBAA",        # 3E, 62
        "Function_63_BBFF",        # 3F, 63
        "Function_64_BCA4",        # 40, 64
        "Function_65_BD16",        # 41, 65
        "Function_66_BD9A",        # 42, 66
        "Function_67_BE0A",        # 43, 67
        "Function_68_BE8E",        # 44, 68
        "Function_69_BEFE",        # 45, 69
        "Function_70_BF82",        # 46, 70
        "Function_71_BFF2",        # 47, 71
        "Function_72_C02F",        # 48, 72
        "Function_73_C080",        # 49, 73
        "Function_74_C0BD",        # 4A, 74
        "Function_75_C118",        # 4B, 75
        "Function_76_C18A",        # 4C, 76
        "Function_77_C206",        # 4D, 77
        "Function_78_C278",        # 4E, 78
        "Function_79_C2F4",        # 4F, 79
        "Function_80_C369",        # 50, 80
        "Function_81_CDF0",        # 51, 81
        "Function_82_D0CB",        # 52, 82
        "Function_83_D3A6",        # 53, 83
        "Function_84_D6C5",        # 54, 84
        "Function_85_D716",        # 55, 85
        "Function_86_DF61",        # 56, 86
        "Function_87_DFB6",        # 57, 87
        "Function_88_E016",        # 58, 88
        "Function_89_E076",        # 59, 89
        "Function_90_E0D6",        # 5A, 90
        "Function_91_E136",        # 5B, 91
        "Function_92_E196",        # 5C, 92
        "Function_93_E2C9",        # 5D, 93
        "Function_94_10953",       # 5E, 94
        "Function_95_109A4",       # 5F, 95
        "Function_96_109F9",       # 60, 96
        "Function_97_10A4E",       # 61, 97
        "Function_98_10AA3",       # 62, 98
        "Function_99_10AF8",       # 63, 99
        "Function_100_10B4D",      # 64, 100
        "Function_101_10BA2",      # 65, 101
        "Function_102_10BF7",      # 66, 102
        "Function_103_10C57",      # 67, 103
        "Function_104_10CB7",      # 68, 104
        "Function_105_10D17",      # 69, 105
        "Function_106_10D77",      # 6A, 106
        "Function_107_10DD7",      # 6B, 107
        "Function_108_11D28",      # 6C, 108
        "Function_109_11D47",      # 6D, 109
        "Function_110_126B1",      # 6E, 110
        "Function_111_129DF",      # 6F, 111
        "Function_112_1304D",      # 70, 112
        "Function_113_130C6",      # 71, 113
        "Function_114_130E1",      # 72, 114
        "Function_115_130F4",      # 73, 115
        "Function_116_136A1",      # 74, 116
        "Function_117_139CB",      # 75, 117
        "Function_118_13E50",      # 76, 118
        "Function_119_1513A",      # 77, 119
        "Function_120_1515F",      # 78, 120
        "Function_121_15187",      # 79, 121
        "Function_122_151FA",      # 7A, 122
        "Function_123_15248",      # 7B, 123
        "Function_124_183F6",      # 7C, 124
        "Function_125_1846B",      # 7D, 125
        "Function_126_184C0",      # 7E, 126
        "Function_127_18515",      # 7F, 127
        "Function_128_1856A",      # 80, 128
        "Function_129_185BF",      # 81, 129
        "Function_130_18614",      # 82, 130
        "Function_131_18669",      # 83, 131
        "Function_132_18699",      # 84, 132
        "Function_133_186F9",      # 85, 133
        "Function_134_18759",      # 86, 134
        "Function_135_187B4",      # 87, 135
        "Function_136_18814",      # 88, 136
        "Function_137_18874",      # 89, 137
        "Function_138_18AE9",      # 8A, 138
        "Function_139_18E73",      # 8B, 139
        "Function_140_1917B",      # 8C, 140
    ))


    def Function_0_B08(): pass

    label("Function_0_B08")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_B40"),
        (1, "loc_B4C"),
        (2, "loc_B58"),
        (3, "loc_B64"),
        (4, "loc_B70"),
        (5, "loc_B7C"),
        (6, "loc_B88"),
        (SWITCH_DEFAULT, "loc_B94"),
    )


    label("loc_B40")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_BA0")

    label("loc_B4C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_BA0")

    label("loc_B58")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_BA0")

    label("loc_B64")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_BA0")

    label("loc_B70")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_BA0")

    label("loc_B7C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_BA0")

    label("loc_B88")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_BA0")

    label("loc_B94")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_BA0")

    label("loc_BA0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BB7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_BA0")

    label("loc_BB7")

    Return()

    # Function_0_B08 end

    def Function_1_BB8(): pass

    label("Function_1_BB8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C0A")
    OP_95(0xFE, 110000, 0, -107310, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(300)
    OP_95(0xFE, 110000, 0, -126470, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(300)
    Jump("Function_1_BB8")

    label("loc_C0A")

    Return()

    # Function_1_BB8 end

    def Function_2_C0B(): pass

    label("Function_2_C0B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C5D")
    OP_95(0xFE, -132100, 0, 100800, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(300)
    OP_95(0xFE, -122620, 0, 100800, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    Jump("Function_2_C0B")

    label("loc_C5D")

    Return()

    # Function_2_C0B end

    def Function_3_C5E(): pass

    label("Function_3_C5E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C88")
    ClearScenarioFlags(0x25, 1)
    Call(0, 52)

    label("loc_C88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D68")
    SetChrChipByIndex(0x2F, 0xB)
    SetChrSubChip(0x2F, 0x0)
    ClearChrFlags(0x2F, 0x80)
    SetChrFlags(0x2F, 0x8000)
    SetChrPos(0x2F, 5650, -5850, -106000, 270)
    SetChrChipByIndex(0x2C, 0xD)
    SetChrSubChip(0x2C, 0x0)
    ClearChrFlags(0x2C, 0x80)
    SetChrFlags(0x2C, 0x8000)
    SetChrPos(0x2C, 5650, -5850, -108800, 270)
    SetChrChipByIndex(0x13, 0xC)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 5650, -5850, -111700, 270)
    SetChrChipByIndex(0x2D, 0xE)
    SetChrSubChip(0x2D, 0x0)
    ClearChrFlags(0x2D, 0x80)
    SetChrFlags(0x2D, 0x8000)
    SetChrPos(0x2D, 1800, -5850, -102100, 180)
    SetChrChipByIndex(0x36, 0xF)
    SetChrSubChip(0x36, 0x0)
    ClearChrFlags(0x36, 0x80)
    SetChrFlags(0x36, 0x8000)
    SetChrPos(0x36, 11800, -5850, -104800, 270)
    SetChrChipByIndex(0x34, 0x7)
    SetChrSubChip(0x34, 0x0)
    ClearChrFlags(0x34, 0x80)
    SetChrFlags(0x34, 0x8000)
    SetChrPos(0x34, 5000, -5800, -99450, 180)

    label("loc_D68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DD7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D96")
    SetChrPos(0x15, -3200, 0, 27000, 90)
    ClearChrFlags(0x15, 0x80)

    label("loc_D96")

    SetChrPos(0x17, -130150, 150, 105800, 90)
    ClearChrFlags(0x17, 0x80)
    SetChrChipByIndex(0x17, 0x20)
    SetChrChipByIndex(0x17, 0x20)
    SetChrSubChip(0x17, 0x0)
    EndChrThread(0x17, 0x0)
    SetChrBattleFlags(0x17, 0x4)
    SetChrPos(0x16, 111300, 0, -102500, 270)
    ClearChrFlags(0x16, 0x80)

    label("loc_DD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_E54")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 111300, 0, -102500, 270)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 110390, 0, -126470, 0)
    BeginChrThread(0x12, 0, 0, 1)
    ClearChrFlags(0x27, 0x80)
    SetChrPos(0x27, -3110, 0, 1600, 90)
    ClearChrFlags(0x2B, 0x80)
    SetChrPos(0x2B, 156990, 0, 110700, 180)
    SetChrChipByIndex(0x2B, 0x1B)
    SetChrSubChip(0x2B, 0x0)
    EndChrThread(0x2B, 0x0)
    SetChrBattleFlags(0x2B, 0x4)
    Jump("loc_141C")

    label("loc_E54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_FAA")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -121320, 0, 5490, 270)
    BeginChrThread(0xD, 0, 0, 0)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -123130, 0, 5700, 90)
    BeginChrThread(0xE, 0, 0, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -128710, 150, 3860, 180)
    SetChrChipByIndex(0xF, 0x1F)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -134450, 0, 3390, 270)
    BeginChrThread(0x10, 0, 0, 0)
    ClearChrFlags(0x20, 0x80)
    SetChrPos(0x20, -122470, 0, 50530, 0)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x1F, -122470, 0, 51740, 180)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, -122350, 0, 57760, 225)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -126560, 150, 110790, 180)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -121670, 0, 111190, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -122620, 0, 100800, 270)
    BeginChrThread(0xA, 0, 0, 2)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -132640, 0, 109740, 135)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 163500, 0, 57920, 90)
    BeginChrThread(0xC, 0, 0, 0)
    Jump("loc_141C")

    label("loc_FAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 6)), scpexpr(EXPR_END)), "loc_FB8")
    Jump("loc_141C")

    label("loc_FB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_10A2")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 149450, 0, 58300, 180)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x27, 110360, 0, -114690, 180)
    SetChrPos(0x1D, 110360, 0, -115990, 0)
    ClearChrFlags(0x28, 0x80)
    SetChrPos(0x28, -2480, 0, 25200, 180)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x20, -127400, 0, 108660, 270)
    SetChrPos(0x21, -128400, 0, 108660, 90)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x12, -122940, 0, 102860, 90)
    SetChrPos(0x1C, -121540, 0, 102860, 270)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x22, 153210, 0, 51920, 0)
    SetChrPos(0x24, 153210, 0, 52920, 180)
    Jump("loc_141C")

    label("loc_10A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 4)), scpexpr(EXPR_END)), "loc_10B0")
    Jump("loc_141C")

    label("loc_10B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_12AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_10D8")
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, -120140, 0, 103460, 270)

    label("loc_10D8")

    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 8690, 0, -132450, 270)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -9280, 0, -132230, 90)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x18, 2180, 0, -126910, 0)
    SetChrPos(0x19, 3180, 0, -126910, 0)
    ClearChrFlags(0x28, 0x80)
    SetChrPos(0x28, 3850, 0, 900, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_1165")
    ClearChrFlags(0x27, 0x80)
    SetChrPos(0x27, 103340, 0, -128889, 180)

    label("loc_1165")

    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, -3280, 0, 13320, 90)
    ClearChrFlags(0x29, 0x80)
    SetChrPos(0x29, -3280, 0, 21260, 90)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x2D, 0x80)
    SetChrPos(0x1A, -128710, 150, 3860, 180)
    SetChrPos(0x2D, -130100, 150, 3080, 90)
    SetChrChipByIndex(0x1A, 0x17)
    SetChrSubChip(0x1A, 0x0)
    EndChrThread(0x1A, 0x0)
    SetChrBattleFlags(0x1A, 0x4)
    SetChrChipByIndex(0x2D, 0xE)
    SetChrSubChip(0x2D, 0x0)
    EndChrThread(0x2D, 0x0)
    SetChrBattleFlags(0x2D, 0x4)
    SetChrSubChip(0x1A, 0x2)
    SetChrSubChip(0x2D, 0x1)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x2A, -134080, 0, 52160, 0)
    SetChrPos(0x13, -134280, 0, 53360, 180)
    BeginChrThread(0x13, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_12AA")
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    SetChrPos(0x25, 153850, 0, 3760, 90)
    SetChrPos(0x26, 155060, 0, 3760, 270)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x2B, 0x80)
    SetChrPos(0x2C, 159940, 150, 57060, 270)
    SetChrPos(0x2B, 158000, 150, 57950, 180)
    SetChrChipByIndex(0x2C, 0xD)
    SetChrSubChip(0x2C, 0x0)
    EndChrThread(0x2C, 0x0)
    SetChrBattleFlags(0x2C, 0x4)
    SetChrChipByIndex(0x2B, 0x1B)
    SetChrSubChip(0x2B, 0x0)
    EndChrThread(0x2B, 0x0)
    SetChrBattleFlags(0x2B, 0x4)
    SetChrSubChip(0x2B, 0x1)
    SetChrFlags(0x2C, 0x10)
    SetChrFlags(0x2B, 0x10)

    label("loc_12AA")

    Jump("loc_141C")

    label("loc_12AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_141C")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 8690, 0, -132450, 270)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -9280, 0, -132230, 90)
    ClearChrFlags(0x27, 0x80)
    SetChrPos(0x27, 103340, 0, -128889, 180)
    ClearChrFlags(0x28, 0x80)
    SetChrPos(0x28, 3850, 0, 900, 180)
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x1E, -122130, 0, -3260, 90)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x1F, -134000, 0, 5590, 315)
    ClearChrFlags(0x2A, 0x80)
    OP_52(0x2A, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x20, 0x80)
    SetChrPos(0x2A, -134080, 0, 52160, 0)
    SetChrPos(0x20, -134280, 0, 53360, 180)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x1C, -125880, 0, 107290, 180)
    SetChrPos(0x21, -124670, 0, 106100, 270)
    SetChrFlags(0x1C, 0x10)
    SetChrFlags(0x21, 0x10)
    ClearChrFlags(0x22, 0x80)
    SetChrPos(0x22, 163430, 0, -1430, 90)
    ClearChrFlags(0x23, 0x80)
    SetChrPos(0x23, 153670, 0, 6380, 0)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 160670, 0, 60390, 0)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, 150610, 0, 51190, 270)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 161310, 0, 111420, 0)
    SetChrFlags(0x14, 0x10)

    label("loc_141C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_1430")
    ClearScenarioFlags(0x22, 0)
    Event(0, 54)
    Jump("loc_14DC")

    label("loc_1430")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_1444")
    ClearScenarioFlags(0x22, 1)
    Event(0, 80)
    Jump("loc_14DC")

    label("loc_1444")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_1458")
    ClearScenarioFlags(0x22, 2)
    Event(0, 107)
    Jump("loc_14DC")

    label("loc_1458")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_146C")
    ClearScenarioFlags(0x22, 3)
    Event(0, 109)
    Jump("loc_14DC")

    label("loc_146C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_1480")
    ClearScenarioFlags(0x22, 4)
    Event(0, 110)
    Jump("loc_14DC")

    label("loc_1480")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_1494")
    ClearScenarioFlags(0x22, 5)
    Event(0, 115)
    Jump("loc_14DC")

    label("loc_1494")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_14A8")
    ClearScenarioFlags(0x22, 6)
    Event(0, 116)
    Jump("loc_14DC")

    label("loc_14A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 7)), scpexpr(EXPR_END)), "loc_14B9")
    ClearScenarioFlags(0x22, 7)
    Jump("loc_14DC")

    label("loc_14B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 0)), scpexpr(EXPR_END)), "loc_14CD")
    ClearScenarioFlags(0x23, 0)
    Event(0, 117)
    Jump("loc_14DC")

    label("loc_14CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 1)), scpexpr(EXPR_END)), "loc_14DC")
    ClearScenarioFlags(0x23, 1)
    Event(0, 85)

    label("loc_14DC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14FA")
    Event(0, 81)

    label("loc_14FA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1521")
    Event(0, 82)

    label("loc_1521")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_153B")
    Event(0, 111)

    label("loc_153B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1555")
    Event(0, 118)

    label("loc_1555")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_156F")
    Event(0, 123)

    label("loc_156F")

    Return()

    # Function_3_C5E end

    def Function_4_1570(): pass

    label("Function_4_1570")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1589")
    VolumeBGM(0x46, 0xC8)
    Jump("loc_15A0")

    label("loc_1589")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15A0")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x12E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_15A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15CB")
    SetBarrier(0x0, 0x0, 0x1, 0x0, -4000, -1000, 27000, 5000, 5000, 90000)

    label("loc_15CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15DF")
    ClearMapObjFlags(0x2, 0x10)

    label("loc_15DF")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15F7")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_15F7")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1613")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_1613")

    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1642")
    SetMapObjFrame(0xFF, "bs", 0x1, 0x1)
    Jump("loc_164C")

    label("loc_1642")

    SetMapObjFrame(0xFF, "bs", 0x0, 0x1)

    label("loc_164C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_166E")
    ClearMapObjFlags(0x16, 0x4)
    OP_70(0x16, 0x46)
    ClearMapObjFlags(0x17, 0x4)
    OP_70(0x17, 0x46)

    label("loc_166E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_16B3")
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_16B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16EE")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)

    label("loc_16EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_170E")
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)

    label("loc_170E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_171D")
    ClearMapObjFlags(0x2, 0x10)

    label("loc_171D")

    ClearMapObjFlags(0x9, 0x10)
    ClearMapObjFlags(0xA, 0x10)
    ClearMapObjFlags(0xB, 0x10)
    ClearMapObjFlags(0xD, 0x10)
    ClearMapObjFlags(0x7, 0x10)
    ClearMapObjFlags(0x8, 0x10)
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1771")
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    OP_66(0x0, 0x1)
    OP_66(0x1, 0x1)
    Jump("loc_1811")

    label("loc_1771")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17B6")
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 7)), scpexpr(EXPR_END)), "loc_17A5")
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0x6, 0x10)
    Jump("loc_17B1")

    label("loc_17A5")

    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0x6, 0x10)

    label("loc_17B1")

    Jump("loc_1811")

    label("loc_17B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17E3")
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    OP_66(0x0, 0x1)
    OP_66(0x1, 0x1)
    Jump("loc_1811")

    label("loc_17E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_1809")
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    Jump("loc_1811")

    label("loc_1809")

    OP_66(0x0, 0x1)
    OP_66(0x1, 0x1)

    label("loc_1811")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_END)), "loc_1824")
    OP_65(0x2, 0x1)
    SetMapObjFlags(0xC, 0x4)

    label("loc_1824")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 7)), scpexpr(EXPR_END)), "loc_1833")
    SetMapObjFlags(0x9, 0x4)

    label("loc_1833")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_184C")
    OP_52(0x2A, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_184C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_185F")
    OP_1B(0x15, 0x0, 0x8C)

    label("loc_185F")

    Return()

    # Function_4_1570 end

    def Function_5_1860(): pass

    label("Function_5_1860")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1877")
    Call(0, 83)
    Return()

    label("loc_1877")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Everyone, thank you\x01",
            "for your help today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The President was very delighted\x01",
            "to see you as well.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_1860 end

    def Function_6_18E6(): pass

    label("Function_6_18E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18FD")
    Call(0, 93)
    Return()

    label("loc_18FD")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_6_18E6 end

    def Function_7_1904(): pass

    label("Function_7_1904")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1B07")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1926")
    TalkEnd(0xFE)
    Call(0, 49)
    Return()

    label("loc_1926")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A41")

    ChrTalk(
        0xFE,
        (
            "We will hold suspect Crois\x01",
            "here until the current\x01",
            "situation is under control.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He has been charged with\x01",
            "many crimes... But I don't want\x01",
            "him to be punished harshly too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Regardless of his methods, the truth is\x01",
            "that he was trying to protect Crossbell...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1B02")

    label("loc_1A41")


    ChrTalk(
        0xFE,
        (
            "Suspect Crois has been charged\x01",
            "with many crimes... But I don't want\x01",
            "him to be punished harshly too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Regardless of his methods, the truth is\x01",
            "that he was trying to protect Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B02")

    Jump("loc_1E86")

    label("loc_1B07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_1B94")

    ChrTalk(
        0xFE,
        (
            "Damn. To think the terrorists\x01",
            "would go this far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If the CGF had acted, they should\x01",
            "have been able to do something...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E86")

    label("loc_1B94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_1CF0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C6F")

    ChrTalk(
        0xFE,
        (
            "*sigh*, Captain Julia...\x01",
            "If she were my boss, each of\x01",
            "my days would be complete...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, I mustn't. \x01",
            "What the hell am I thinking?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Damn. This is proof that\x01",
            "I'm not nervous enough.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1CEB")

    label("loc_1C6F")


    ChrTalk(
        0xFE,
        (
            "We still can't be optimistic about\x01",
            "the situation, so why am I...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Damn. This is proof that\x01",
            "I'm not nervous enough.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CEB")

    Jump("loc_1E86")

    label("loc_1CF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_1E86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DEC")

    ChrTalk(
        0xFE,
        (
            "*sigh*, but this viewing corridor\x01",
            "really does have a nice view.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you set your gaze in the distance, it feels\x01",
            "as if you're taking a walk through the sky...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, I mustn't. I've got to\x01",
            "be a little more nervous.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1E86")

    label("loc_1DEC")


    ChrTalk(
        0xFE,
        (
            "Now that I'm here, I'm getting\x01",
            "distracted by the view... \x01",
            "I've got to be more nervous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's nothing redeeming\x01",
            "about idle thoughts, they say.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E86")

    TalkEnd(0xFE)
    Return()

    # Function_7_1904 end

    def Function_8_1E8A(): pass

    label("Function_8_1E8A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1EE0")

    ChrTalk(
        0xFE,
        "Nothing out of the ordinary!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "We're continuing our patrols!\x02",
    )

    CloseMessageWindow()
    Jump("loc_21C1")

    label("loc_1EE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_1F82")

    ChrTalk(
        0xFE,
        (
            "It seems that we can't use the\x01",
            "elevator or the stairs right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Divided like this, we'll need to do\x01",
            "something on our own at this rate...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21C1")

    label("loc_1F82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_214F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20C4")

    ChrTalk(
        0xFE,
        (
            "They called him Major Mueller\x01",
            "of the Imperial Army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And Captain Julia is supreme commander of\x01",
            "the Royal Army and the Royal Elite Guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's rare to see two people\x01",
            "with those titles together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's almost like they're good friends...\x01",
            "I wonder just what their relationship is.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_214A")

    label("loc_20C4")


    ChrTalk(
        0xFE,
        (
            "Seeing them like this,\x01",
            "it's almost as if\x01",
            "they're good friends...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just what is the relationship\x01",
            "between those two, I wonder.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_214A")

    Jump("loc_21C1")

    label("loc_214F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_21C1")

    ChrTalk(
        0xFE,
        "The main session has finally started.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This nervousness... \x01",
            "I feel tense both in body and mind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21C1")

    TalkEnd(0xFE)
    Return()

    # Function_8_1E8A end

    def Function_9_21C5(): pass

    label("Function_9_21C5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21DA")
    Call(0, 10)
    Jump("loc_242A")

    label("loc_21DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2375")

    ChrTalk(
        0x18,
        (
            "#07108FCome to think of it, it seems\x01",
            "Her Highness returned from\x01",
            "the stairs direction earlier...\x02\x03",
            "#07103FHmm. Considering how Her Highness is now,\x01",
            "it won't happen that her heart would be thrown\x01",
            "in disarray by meeting that person.\x02\x03",
            "...It's useless worrying unnecessarily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F(...Is she talking\x01",
            "about Mr. Lechter?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F(Hu hu. It seems there's\x01",
            "various things between them.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_242A")

    label("loc_2375")


    ChrTalk(
        0x18,
        (
            "#07103FPlease contact me if you learn anything\x01",
            "through your security procedures.\x02\x03",
            "#07100FOn my end, I'll report to the security planning \x01",
            "room immediately if I learn anything.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_242A")

    TalkEnd(0xFE)
    Return()

    # Function_9_21C5 end

    def Function_10_242E(): pass

    label("Function_10_242E")

    OP_4B(0x19, 0xFF)
    OP_4B(0x18, 0xFF)
    TurnDirection(0x19, 0x0, 500)

    ChrTalk(
        0x19,
        "#07300FHmm. You guys, huh.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x18, 0x0, 500)

    ChrTalk(
        0x18,
        "#07100FHas the situation changed?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FNo, for the time being.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FHave either of you\x01",
            "received any intel?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#07103FNo, unfortunately there's\x01",
            "nothing special to mention.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#07303F...The Empire too is doing\x01",
            "its very best, however...\x02\x03",
            "#07301FWhether it's the Noble Faction or\x01",
            "the Reformist Faction, we haven't\x01",
            "got a lead on either of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10108FSo that's how it is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FThe two major Imperial factions...\x01",
            "They seem like unthinkably\x01",
            "troublesome opponents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F............\x02\x03",
            "#00108FUm, Prince Olivert spoke about\x01",
            "a "third option" yesterday, right?\x02\x03",
            "I've been interested in that this whole time...\x02\x03",
            "#00101FIf it's all right with you, could\x01",
            "we hear a little more about it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FElie...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#07302FHmm. Thinking about the\x01",
            "problem is perfectly natural.\x02\x03",
            "#07304FIt's not something I can\x01",
            "normally discuss casually, but\x01",
            "if it's you guys I don't mind.\x02\x03",
            "#07300FIn a word― He's trying to\x01",
            "clear away some "barriers".\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00001FClearing away "barriers"...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#07303FIn short, there're recognizable barriers\x01",
            "between the Reformist and Noble factions.\x02\x03",
            "#07300FFurthermore, it's an absurd option:\x01",
            "To make both parties reconcile.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FReconciliation between the\x01",
            "Reformist and Noble factions...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHu hu. Well, should I say there will\x01",
            "be difficulties in doing that, or rather,\x01",
            "isn't it just some idealistic thought?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101FW-Wazy―\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#07302FHu hu... \x01",
            "It's just as you say.\x02\x03",
            "#07304FIt's like that guy has decided\x01",
            "a confrontation with a "monster"\x01",
            "through some absurd methods.\x02\x03",
            "I'm fully aware they're talking behind his back\x01",
            "saying he's a whimsical bastard prince and\x01",
            "a show-off of a snob who lives for his hobbies.\x02\x03",
            "#07302FAnd I've decided to\x01",
            "stick with him too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FI-I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#07104FMajor Mueller... As Princess\x01",
            "Klaudia has said, Liberl\x01",
            "is an ally of the prince.\x02\x03",
            "#07102FWe cannot directly intervene, but please\x01",
            "don't hesitate to ask if you need something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#07304FHmm. I'm deeply grateful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FCould this too be one of the\x01",
            "prince's natural virtues?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#07304FHu hu, those are words really\x01",
            "not suited for that guy, but\x01",
            "maybe it's indeed as you say.\x02\x03",
            "#07308FAnyway, right now I need this Trade\x01",
            "Conference to end without incident―\x01",
            "I will focus on that objective.\x02\x03",
            "#07300FLadies and gentlemen of the Special Support\x01",
            "Section... I look forward to seeing your results.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x19, 0x0, 0x0)
    OP_93(0x18, 0x0, 0x0)
    OP_4C(0x19, 0xFF)
    OP_4C(0x18, 0xFF)
    SetScenarioFlags(0x1C3, 5)
    Return()

    # Function_10_242E end

    def Function_11_2DFE(): pass

    label("Function_11_2DFE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E13")
    Call(0, 10)
    Jump("loc_2EEE")

    label("loc_2E13")


    ChrTalk(
        0x19,
        (
            "#07303FAnyway, right now I need this Trade\x01",
            "Conference to end without incident―\x01",
            "I will focus on that objective.\x02\x03",
            "#07300FLadies and gentlemen of the Special Support\x01",
            "Section... I look forward to seeing your results.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EEE")

    TalkEnd(0xFE)
    Return()

    # Function_11_2DFE end

    def Function_12_2EF2(): pass

    label("Function_12_2EF2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2F9F")

    ChrTalk(
        0xFE,
        (
            "The core floors below from 30F\x01",
            "you can go to from the emergency\x01",
            "stairs are not completely safe yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you intend to go there,\x01",
            "please be careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3277")

    label("loc_2F9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_30C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3057")

    ChrTalk(
        0xFE,
        (
            "E-Everyone. A terrible\x01",
            "thing has happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For now, let's work to protect\x01",
            "this floor we're stationed on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Let's brace ourselves as we proceed!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_30C4")

    label("loc_3057")


    ChrTalk(
        0xFE,
        (
            "For now, let's work to protect\x01",
            "this floor we're stationed on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Let's brace ourselves as we proceed!\x02",
    )

    CloseMessageWindow()

    label("loc_30C4")

    Jump("loc_3277")

    label("loc_30C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_3171")

    ChrTalk(
        0xFE,
        (
            "*sigh*. The auras\x01",
            "of the VIPs sure\x01",
            "are impressive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter how much I'm prepared,\x01",
            "every time they pass through here\x01",
            "I unconsciously contract.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3277")

    label("loc_3171")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_3277")

    ChrTalk(
        0xFE,
        (
            "The very first room to the right on\x01",
            "this VIP floor is used by the Mayor\x01",
            "and Chairman, then there's the Prince...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And finally, Chancellor \x01",
            "Osborne is using the\x01",
            "deepest room in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They're cleaning the\x01",
            "rooms now, so please\x01",
            "feel free to enter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3277")

    TalkEnd(0xFE)
    Return()

    # Function_12_2EF2 end

    def Function_13_327B(): pass

    label("Function_13_327B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_333D")

    ChrTalk(
        0xFE,
        (
            "For now, we've gathered the\x01",
            "left wing staff in this room!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm worried because we can't do\x01",
            "anything but wait for direction from\x01",
            "HQ... Anyway, we've got to do our best!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_377B")

    label("loc_333D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_34EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3432")

    ChrTalk(
        0xFE,
        (
            "I saw Princess\x01",
            "Klaudia just now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Seeing the VIPs so many times in\x01",
            "one day and being close to them...\x01",
            "I can hardly believe it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyhow, I've got to do my\x01",
            "best today to avoid a\x01",
            "lifetime of embarrassment.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_34E9")

    label("loc_3432")


    ChrTalk(
        0xFE,
        (
            "Seeing the VIPs so many times in\x01",
            "one day and being close to them...\x01",
            "This will never happen again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyhow, I've got to do my\x01",
            "best today to avoid a\x01",
            "lifetime of embarrassment.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34E9")

    Jump("loc_377B")

    label("loc_34EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_377B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36FA")

    ChrTalk(
        0xFE,
        (
            "From the front, the rooms in the left wing\x01",
            "of the VIP floor are for the heads of\x01",
            "state from Remiferia, Liberl and Calvard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the way, out of consideration for\x01",
            "the VIPs, there's a minimum number\x01",
            "of personnel on patrol on this floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, even though you've been invited \x01",
            "by the heads of state, a minimum \x01",
            "level of confidentiality is needed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For now, because the heads of state are\x01",
            "accompanied by their escorts even during breaks,\x01",
            "there are no problems in the security area.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_377B")

    label("loc_36FA")


    ChrTalk(
        0xFE,
        (
            "Later, during break\x01",
            "time, it'll be harder to\x01",
            "move about in this area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "If you want to check the rooms, now is the time.\x02",
    )

    CloseMessageWindow()

    label("loc_377B")

    TalkEnd(0xFE)
    Return()

    # Function_13_327B end

    def Function_14_377F(): pass

    label("Function_14_377F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3858")

    ChrTalk(
        0xFE,
        (
            "Archduke Albert of\x01",
            "Remiferia will be\x01",
            "using this room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And, I understand the Archduke\x01",
            "has a deep knowledge of music.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Right now, I'm preparing\x01",
            "Chairman MacDowell's\x01",
            "record collection.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_390B")

    label("loc_3858")


    ChrTalk(
        0xFE,
        (
            "It seems Chairman MacDowell and Archduke\x01",
            "Albert have a very good relationship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Remiferia is also famous as the\x01",
            "sponsor of St. Ursula Hospital...\x01",
            "Somehow it makes sense.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_390B")

    TalkEnd(0xFE)
    Return()

    # Function_14_377F end

    def Function_15_390F(): pass

    label("Function_15_390F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3920")
    Jump("loc_3BDB")

    label("loc_3920")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3ACA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A47")

    ChrTalk(
        0xFE,
        (
            "It's only been one night since martial law\x01",
            "was declared, but the fatigue of everyone\x01",
            "in the tower has already reached a peak.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We don't know what will happen...\x01",
            "As expected, it seems everyone is worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope this situation is\x01",
            "resolved quickly, but...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_3AC5")

    label("loc_3A47")


    ChrTalk(
        0xFE,
        (
            "The fatigue of everyone in this\x01",
            "tower has already reached a peak.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope this situation is\x01",
            "resolved quickly, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AC5")

    Jump("loc_3BDB")

    label("loc_3ACA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_3BDB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B81")

    ChrTalk(
        0xFE,
        (
            "*work, work, work*... \x01",
            "I've worked up a nice sweat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Alright. With this, the potted plant's perfect.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now, to once again\x01",
            "check for any dust...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_3BDB")

    label("loc_3B81")


    ChrTalk(
        0xFE,
        "With this, the potted plant's perfect.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now, to once again\x01",
            "check for any dust...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BDB")

    TalkEnd(0xFE)
    Return()

    # Function_15_390F end

    def Function_16_3BDF(): pass

    label("Function_16_3BDF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C9D")

    ChrTalk(
        0xFE,
        (
            "This is the room of his\x01",
            "grace, Archduke Albert.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Right now, Chairman MacDowell\x01",
            "is visiting, however I was\x01",
            "told to let you pass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "If you like, please enter.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_3D10")

    label("loc_3C9D")


    ChrTalk(
        0xFE,
        (
            "Right now he is visiting\x01",
            "with Chairman MacDowell.\x01",
            "I was told to let you pass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "If you like, please enter.\x02",
    )

    CloseMessageWindow()

    label("loc_3D10")

    TalkEnd(0xFE)
    Return()

    # Function_16_3BDF end

    def Function_17_3D14(): pass

    label("Function_17_3D14")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D29")
    Call(0, 18)
    Jump("loc_3DF6")

    label("loc_3D29")


    ChrTalk(
        0xFE,
        (
            "Hm, as expected, the second\x01",
            "half of the conference requires\x01",
            "our guard to be even higher.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We'll need to especially watch out\x01",
            "for proposals regarding security\x01",
            "guarantees from the two major powers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DF6")

    TalkEnd(0xFE)
    SetChrSubChip(0x1A, 0x2)
    Return()

    # Function_17_3D14 end

    def Function_18_3DFE(): pass

    label("Function_18_3DFE")

    SetChrSubChip(0x1A, 0x2)
    SetChrSubChip(0x2D, 0x1)

    ChrTalk(
        0x1A,
        (
            "*sigh*. Though the arguments are settled,\x01",
            "it's tiring when your opponents are the\x01",
            "heads of state of the two major powers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#02509FUh uh. But Archduke, your\x01",
            "presence is growing as well.\x02\x03",
            "Your predecessors would be proud.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "...It's been five years since I became head of my family.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Although domestic order was\x01",
            "finally secured recently, I have\x01",
            "a long way to go as a leader.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x1A, 0x10)
    TurnDirection(0x1A, 0x0, 0)
    OP_52(0x1A, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4030")
    Jump("loc_407A")

    label("loc_4030")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4050")
    OP_52(0x1A, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_407A")

    label("loc_4050")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4070")
    OP_52(0x1A, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_407A")

    label("loc_4070")

    OP_52(0x1A, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_407A")

    OP_52(0x1A, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x1A, 0x10)
    Sleep(500)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x2D, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2D, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x2D, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x2D, 0x10)
    TurnDirection(0x2D, 0x0, 0)
    OP_52(0x2D, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x2D, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2D, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x2D, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x2D, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2D, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x2D, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2D, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x2D, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x2D, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x2D, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4133")
    Jump("loc_417D")

    label("loc_4133")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2D, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4153")
    OP_52(0x2D, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_417D")

    label("loc_4153")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2D, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4173")
    OP_52(0x2D, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_417D")

    label("loc_4173")

    OP_52(0x2D, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x2D, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_417D")

    OP_52(0x2D, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2D, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x2D, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_432B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_41FA")

    ChrTalk(
        0x1A,
        (
            "Ah, you all... Thank you\x01",
            "for your help yesterday.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4212")

    label("loc_41FA")


    ChrTalk(
        0x1A,
        "Oh, you all are...\x02",
    )

    CloseMessageWindow()

    label("loc_4212")


    ChrTalk(
        0x2D,
        "#02505FOh, if it isn't the Support Section.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FPardon the interruption.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Hmm. I've heard about it, so I'd like to thank\x01",
            "you for participating in the security detail.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "I heard you saved Chairman \x01",
            "MacDowell's life before. \x01",
            "I know you can be very reliable.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4766")

    label("loc_432B")


    ChrTalk(
        0x1A,
        "Oh, it's you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        "#02500FOoh, if it isn't the Support Section.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FSorry to intrude.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Hmm, so you're the Special Support Section?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "How do you do. I heard about\x01",
            "your exploits from Arios.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005FDo you know\x01",
            "Mr. Arios?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Yes. We've been friendly with the\x01",
            "Bracer Guild for quite a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "My personal relationship with\x01",
            "Arios is especially deep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FI see... So that's how it is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "And Elie. It's been awhile.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "It seems your remarkable achievements with\x01",
            "the Special Support Section stand out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FNot at all...\x01",
            "But thank you very much.\x02\x03",
            "#00102FI'm just glad Your Grace too is well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105F(Miss Elie... So she\x01",
            "knows the Archduke.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F(I am used to this to a certain degree, but...\x01",
            "The other party is a head of state...Impressive.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F(Man. Milady's relationships\x01",
            "can't be called ordinary.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Anyway, I'm glad highly reputed people like \x01",
            "yourselves are participating in the security detail.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "I heard you saved Chairman \x01",
            "MacDowell's life before. \x01",
            "I know you can be very reliable.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4766")


    ChrTalk(
        0x101,
        "#00006FNo, you don't need to thank us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#02500FHmm. I too think that's reassuring.\x02\x03",
            "Because of you, we'll be able to concentrate on\x01",
            "arguments for the conference's second half.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FThe conference's second half...\x02\x03",
            "#00101FGrandfather, do you expect to\x01",
            "be in a difficult position?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#02503FYes. In contrast to the first half,\x01",
            "painfully true faults of our autonomous state \x01",
            "will be pointed out one after the next, you see.\x02\x03",
            "Even so, it could end with their\x01",
            "demands being the same as always...\x02\x03",
            "#02501FMy other fear is Dieter.\x01\x02\x03",
            "Even during the congress, he introduced\x01",
            "one radical idea after the next with\x01",
            "great enthusiasm, but...\x02\x03",
            "It can't be helped that he's\x01",
            "young. I'm worried that vigor\x01",
            "will turn in a bad direction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FI think Lawyer Ian said\x01",
            "Mayor Dieter has some\x01",
            "kind of plan, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#02503FYes. I myself don't know what\x01",
            "it is, but it will become a\x01",
            "point of discussion for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "And whether this plan will bring\x01",
            "good or bad fortune, is all up\x01",
            "to how the conference goes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#02503FYes, that's exactly it.\x02\x03",
            "#02500FWell, as the Chairman, it's\x01",
            "my categoric job to support\x01",
            "the Mayor at the conference.\x02\x03",
            "Anyway, I must do what\x01",
            "I can, in my own way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FGrandfather... \x01",
            "I wish you the best.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C4, 0)
    ClearChrFlags(0x2D, 0x10)
    ClearChrFlags(0x1A, 0x10)
    Return()

    # Function_18_3DFE end

    def Function_19_4C5D(): pass

    label("Function_19_4C5D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C72")
    Call(0, 18)
    Jump("loc_4D01")

    label("loc_4C72")


    ChrTalk(
        0xFE,
        (
            "#02500FWell, as the Chairman, it's\x01",
            "my categoric job to support\x01",
            "the Mayor at the conference.\x02\x03",
            "Anyway, I must do what\x01",
            "I can, in my own way.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D01")

    TalkEnd(0xFE)
    SetChrSubChip(0x2D, 0x1)
    Return()

    # Function_19_4C5D end

    def Function_20_4D09(): pass

    label("Function_20_4D09")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_4D1A")
    Jump("loc_4D8B")

    label("loc_4D1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_4D54")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D35")
    Call(0, 21)
    Jump("loc_4D4F")

    label("loc_4D35")


    ChrTalk(
        0x2A,
        "#08000FScree, scree!\x02",
    )

    CloseMessageWindow()

    label("loc_4D4F")

    Jump("loc_4D8B")

    label("loc_4D54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_4D8B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D6F")
    Call(0, 22)
    Jump("loc_4D8B")

    label("loc_4D6F")


    ChrTalk(
        0x2A,
        "#08000FScree, screeee!\x02",
    )

    CloseMessageWindow()

    label("loc_4D8B")

    TalkEnd(0xFE)
    Return()

    # Function_20_4D09 end

    def Function_21_4D8F(): pass

    label("Function_21_4D8F")

    OP_4B(0x13, 0xFF)
    OP_93(0x13, 0xB4, 0x0)
    OP_93(0x2A, 0x0, 0x0)

    ChrTalk(
        0x13,
        (
            "#07008FSay, Sieg. \x01",
            "What would have my grandmother\x01",
            "said if she could have attended?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        "#08000FScree, screee.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#07000F*giggle*, I see. ...I am\x01",
            "who I am, I suppose.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x13, 0x0, 500)

    ChrTalk(
        0x13,
        "#07002FAh, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FSorry for visiting\x01",
            "so suddenly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#07009FNo, please don't worry about it.\x02\x03",
            "I was thinking things\x01",
            "out by myself... I am\x01",
            "glad you have come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FYour Highness...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F...Could you have been thinking about\x01",
            "the second half of the conference?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#07000FYes, that too... But it was\x01",
            "something more fundamental.\x02\x03",
            "#07003FAs Crown Princess, I have a certain\x01",
            "amount of knowledge regarding\x01",
            "diplomatic negotiations, but...\x02\x03",
            "For negotiations, you need insight,\x01",
            "judgment and a sense of balance...\x02\x03",
            "#07001FThe first half of the conference \x01",
            "made me aware that I am\x01",
            "lacking in those areas.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201FIs that so...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FWell, even bein' able to\x01",
            "analyse that much with\x01",
            "composure is plenty amazin'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FYes. And on top of that,\x01",
            "you're about the same age as Mr. Lloyd,\x01",
            "I and the others, Your Highness...\x02\x03",
            "That's truly awe-inspiring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#07002F*giggle*, thank you very much.\x02\x03",
            "#07003FBut certainly, the fact that my\x01",
            "voice is small can't be helped.\x02\x03",
            "The state of things in the continent may move,\x01",
            "but I will have to gain experience one step at\x01",
            "a time without being impatient.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FThat's right. And relax is\x01",
            "important too, you know?\x02\x03",
            "I mean, it's your\x01",
            "break time right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FWazy... What's with that attitude\x01",
            "in front of Her Highness?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#07009F*giggle*, I don't mind. His lack\x01",
            "of excessive formality makes me\x01",
            "feel at ease too.\x02\x03",
            "#07002FHowever... It's strange.\x02\x03",
            "Speaking with all of you makes\x01",
            "me feel like I am speaking with\x01",
            "Miss Estelle and the others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106FThose words are more than we deserve.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#07000F*giggle*. Well everyone,\x01",
            "would you like some tea?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        "#00005FNo, it's out of the question.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206FYes. And we have to finish our patrol.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#07004FI am sorry. You're right too.\x02\x03",
            "#07000FThen everyone, please\x01",
            "do be careful.\x02\x03",
            "And I as well will do my\x01",
            "best to carry out my duty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FYes, understood.\x02",
    )

    CloseMessageWindow()
    OP_93(0x13, 0xB4, 0x0)
    OP_93(0x2A, 0x0, 0x0)
    OP_4C(0x13, 0xFF)
    SetScenarioFlags(0x1C4, 1)
    Return()

    # Function_21_4D8F end

    def Function_22_5605(): pass

    label("Function_22_5605")

    OP_4B(0x20, 0xFF)
    TurnDirection(0x20, 0x0, 500)

    ChrTalk(
        0x20,
        "My, you're those patrol officers...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes. Sorry for interrupting.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x2A, 0x0, 500)

    ChrTalk(
        0x2A,
        "#08000FScree!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F*giggle*, you're Sieg. You were with\x01",
            "her highness, Princess Klaudia, eh?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#00205FI see. So he's the white\x01",
            "falcon KeA was speaking of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        "#08000FScree, scree!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301FHmm, what's he saying?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FTio, can you understand him?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FYes, he's saying [Hello] to everyone. \x01",
            "And [Nice to meet you] to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302FHu hu, he's got a good memory.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        "#08009FScree, screee!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202F[A matter of course for Princess\x01",
            "Klaudia's friends], he says.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FHa ha, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        "#08009FScree!\x02",
    )

    CloseMessageWindow()
    OP_93(0x20, 0xB4, 0x0)
    OP_93(0x2A, 0x0, 0x0)
    OP_4C(0x20, 0xFF)
    SetScenarioFlags(0x1C3, 6)
    Return()

    # Function_22_5605 end

    def Function_23_58B5(): pass

    label("Function_23_58B5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_58C6")
    Jump("loc_5AAD")

    label("loc_58C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_59F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_596B")

    ChrTalk(
        0xFE,
        (
            "We're looking after\x01",
            "the people trapped\x01",
            "in the tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's a girl in the\x01",
            "right wing... Poor thing,\x01",
            "wrapped up in all of this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_59EC")

    label("loc_596B")


    ChrTalk(
        0xFE,
        (
            "There's a little girl in the right wing...\x01",
            "And she looks rather depressed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think I'll bring her\x01",
            "some sweets later...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59EC")

    Jump("loc_5AAD")

    label("loc_59F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_5A44")

    ChrTalk(
        0xFE,
        (
            "A-Anyway... Us staffers\x01",
            "have to remain calm and\x01",
            "do what we can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AAD")

    label("loc_5A44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_5A52")
    Jump("loc_5AAD")

    label("loc_5A52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_5AAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A6D")
    Call(0, 22)
    Jump("loc_5AAD")

    label("loc_5A6D")


    ChrTalk(
        0xFE,
        (
            "Oh, you know\x01",
            "Sieg, do you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh. Sieg is\x01",
            "very smart.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5AAD")

    TalkEnd(0xFE)
    Return()

    # Function_23_58B5 end

    def Function_24_5AB1(): pass

    label("Function_24_5AB1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_5B53")

    ChrTalk(
        0xFE,
        "You're the Special Support Section, correct?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was told by princess \x01",
            "Klaudia to always \x01",
            "let you pass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please, feel free to enter.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5B5C")

    label("loc_5B53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_5B5C")

    label("loc_5B5C")

    TalkEnd(0xFE)
    Return()

    # Function_24_5AB1 end

    def Function_25_5B60(): pass

    label("Function_25_5B60")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_5B71")
    Jump("loc_5C00")

    label("loc_5B71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_5BF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B8C")
    Call(0, 21)
    Jump("loc_5BF2")

    label("loc_5B8C")


    ChrTalk(
        0x13,
        (
            "#07000FEveryone, thank\x01",
            "you very much \x01",
            "for chatting with me.\x02\x03",
            "Let's both focus\x01",
            "on what's to come.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BF2")

    Jump("loc_5C00")

    label("loc_5BF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_5C00")

    label("loc_5C00")

    TalkEnd(0xFE)
    Return()

    # Function_25_5B60 end

    def Function_26_5C04(): pass

    label("Function_26_5C04")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_5C8E")

    ChrTalk(
        0xFE,
        (
            "We are waiting here so as\x01",
            "not to interrupt all of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's in times like these that\x01",
            "we must think rationally.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D39")

    label("loc_5C8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_5C9C")
    Jump("loc_5D39")

    label("loc_5C9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_5D39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CB7")
    Call(0, 27)
    Jump("loc_5D39")

    label("loc_5CB7")


    ChrTalk(
        0xFE,
        (
            "A steamed bun with a\x01",
            "Michey print on it, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I feel a little open-\x01",
            "heartedness goes a long\x01",
            "way in a place like this...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D39")

    TalkEnd(0xFE)
    Return()

    # Function_26_5C04 end

    def Function_27_5D3D(): pass

    label("Function_27_5D3D")

    OP_4B(0x1C, 0xFF)
    OP_4B(0x21, 0xFF)

    ChrTalk(
        0x1C,
        (
            "Hmm, but will this do for\x01",
            "tea cakes for the President?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "Ahaha, well the staff did their\x01",
            "very best on them, so I suppose\x01",
            "there's no need to worry?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "And look, isn't this\x01",
            ""local feeling" good?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "Hmm. Even so, I think\x01",
            "there were others too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105F(? Was there a problem about\x01",
            "the cakes made for the tea?)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#00201F(Those are Michey steamed buns...\x01",
            "Alias "Michbuns"...?)\x02\x03",
            "(There's no problem. \x01",
            "No choice could be better.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106F(R-Really...?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F(Ha ha. I feel like this conversation\x01",
            "could be nice coverage material.)\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x1C, 0xFF)
    OP_4C(0x21, 0xFF)
    SetScenarioFlags(0x1C4, 2)
    Return()

    # Function_27_5D3D end

    def Function_28_5F91(): pass

    label("Function_28_5F91")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_5FDC")

    ChrTalk(
        0xFE,
        (
            "F-First, a deep breath... \x01",
            "*inhaaale*, *exhaaale*...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6091")

    label("loc_5FDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_5FEA")
    Jump("loc_6091")

    label("loc_5FEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_6091")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6005")
    Call(0, 27)
    Jump("loc_6091")

    label("loc_6005")


    ChrTalk(
        0xFE,
        (
            "Hmm. Now that I think about it,\x01",
            "I'm getting anxious somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But at this late hour, I don't have\x01",
            "time to prepare anything else...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6091")

    TalkEnd(0xFE)
    Return()

    # Function_28_5F91 end

    def Function_29_6095(): pass

    label("Function_29_6095")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6187")

    ChrTalk(
        0x17,
        (
            "#07500FYou guys are still here.\x02\x03",
            "Hmm. Would you like\x01",
            "to have tea with me?\x02\x03",
            "#07509FThere's steamed buns too, so why\x01",
            "not making yourselves at home?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FNo... \x01",
            "We can't.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FYes. Sorry for interrupting.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_6211")

    label("loc_6187")


    ChrTalk(
        0x17,
        (
            "#07503F*crunch, munch*... But these\x01",
            "steamed buns are exquisite.\x02\x03",
            "#07509FHa ha ha. I think I'll take a\x01",
            "few home with me as souvenirs.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6211")

    TalkEnd(0xFE)
    Return()

    # Function_29_6095 end

    def Function_30_6215(): pass

    label("Function_30_6215")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_62BB")

    ChrTalk(
        0xFE,
        (
            "Ah, it's only natural, but... \x01",
            "This is no time to be cleaning rooms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*shiver*... When I think\x01",
            "about many bad things,\x01",
            "I can't stop shaking.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63BF")

    label("loc_62BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_62C9")
    Jump("loc_63BF")

    label("loc_62C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_63BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6365")

    ChrTalk(
        0xFE,
        (
            "Looking out over Crossbell from\x01",
            "here really does give a great view.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I unintentionally stare\x01",
            "out when cleaning windows.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_63BF")

    label("loc_6365")

    OP_93(0xFE, 0x5A, 0x0)

    ChrTalk(
        0xFE,
        (
            "*wipe wipe wipe*...\x01",
            "*hum huhu～m♪*\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*wipe wipe wipe*...\x01",
            "*lah la la～h♪*\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63BF")

    TalkEnd(0xFE)
    Return()

    # Function_30_6215 end

    def Function_31_63C3(): pass

    label("Function_31_63C3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6492")

    ChrTalk(
        0xFE,
        (
            "The Mayor and Chairman will\x01",
            "share this room during breaks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For the Mayor and Chairman battling it out\x01",
            "in the conference, I will put everything \x01",
            "I have into cleaning this room.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_64FD")

    label("loc_6492")


    ChrTalk(
        0xFE,
        (
            "*flap, flap, flap*... \x01",
            "Go for it, Mr. Mayor!♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*flap, flap, flap*... \x01",
            "Go for it, Mr. Chairman!♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_64FD")

    TalkEnd(0xFE)
    Return()

    # Function_31_63C3 end

    def Function_32_6501(): pass

    label("Function_32_6501")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "*sigh*. With this, just the\x01",
            "conference's second half is left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Honestly though, it'll be more difficult\x01",
            "from here on out... The Mayor and\x01",
            "Chairman have to do their best.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_32_6501 end

    def Function_33_65BB(): pass

    label("Function_33_65BB")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Ah, everyone. \x01",
            "Mayor Dieter is in Prince\x01",
            "Olivert's room right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And Chairman MacDowell is in \x01",
            "Archduke Albert's room in the left wing.\x01",
            "They are both visiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you like, why not try visiting\x01",
            "each of those rooms directly.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_33_65BB end

    def Function_34_66B3(): pass

    label("Function_34_66B3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_66C4")
    Jump("loc_6B84")

    label("loc_66C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6938")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_683C")

    ChrTalk(
        0xFE,
        (
            "It seems the President made use\x01",
            "of a private force of suspicious\x01",
            "people outside the State Guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I saw the jaegers that attacked the\x01",
            "city and a juvenile delinquent who\x01",
            "looked out of place here in the tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I remember having many doubts, but I\x01",
            "didn't question things... Thinking back on it\x01",
            "now, there were a lot of suspicious points.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_6933")

    label("loc_683C")


    ChrTalk(
        0xFE,
        (
            "I saw the jaegers that attacked the\x01",
            "city and a juvenile delinquent who\x01",
            "looked out of place here in the tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I remember having many doubts, but I\x01",
            "didn't question things... Thinking back on it\x01",
            "now, there were a lot of suspicious points.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6933")

    Jump("loc_6B84")

    label("loc_6938")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_69D1")

    ChrTalk(
        0xFE,
        (
            "To think the terrorists would\x01",
            "have entered the conference\x01",
            "venue directly...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just who could have predicted\x01",
            "a situation like this?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B84")

    label("loc_69D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_69DF")
    Jump("loc_6B84")

    label("loc_69DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_6B84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6AD5")

    ChrTalk(
        0xFE,
        (
            "This room is for\x01",
            "Prince Olivert\x01",
            "during breaks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, the Prince is known\x01",
            "in the Empire's high society\x01",
            "as a famous authentic idyllist...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I spontaneously put a lot of energy\x01",
            "into setting up this room.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_6B84")

    label("loc_6AD5")


    ChrTalk(
        0xFE,
        (
            "Speaking of Prince Olivert, he's\x01",
            "known in the Empire's high society\x01",
            "as a famous authentic idyllist...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I spontaneously put a lot of energy\x01",
            "into setting up this room.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B84")

    TalkEnd(0xFE)
    Return()

    # Function_34_66B3 end

    def Function_35_6B88(): pass

    label("Function_35_6B88")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_6C0C")

    ChrTalk(
        0xFE,
        (
            "Honestly, I can only think\x01",
            "I'm having a bad dream...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I wonder what's going\x01",
            "to happen to everyone now?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6CB6")

    label("loc_6C0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_6C1A")
    Jump("loc_6CB6")

    label("loc_6C1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_6CB6")

    ChrTalk(
        0xFE,
        (
            "Prince Olivert loves roses, especially\x01",
            "red roses, so I've decorated his room\x01",
            "with them like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uh uh, I'll be happy if he likes them.\x02",
    )

    CloseMessageWindow()

    label("loc_6CB6")

    TalkEnd(0xFE)
    Return()

    # Function_35_6B88 end

    def Function_36_6CBA(): pass

    label("Function_36_6CBA")

    TalkBegin(0xFE)
    Call(0, 37)
    TalkEnd(0xFE)
    Return()

    # Function_36_6CBA end

    def Function_37_6CC4(): pass

    label("Function_37_6CC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7742")

    ChrTalk(
        0x2B,
        (
            "#02809FHa ha, I see. I have high\x01",
            "hopes for those young men\x01",
            "and women in the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2C,
        (
            "#07204FYes. And those people\x01",
            "are not dyed any color.\x02\x03",
            "#07202FThat's why, more and more―\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2C, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2B, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x2C, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x2C, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x2C, 0x10)
    TurnDirection(0x2C, 0x0, 0)
    OP_52(0x2C, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x2C, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x2C, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x2C, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x2C, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2C, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x2C, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x2C, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x2C, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6E3D")
    Jump("loc_6E87")

    label("loc_6E3D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2C, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6E5D")
    OP_52(0x2C, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6E87")

    label("loc_6E5D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2C, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6E7D")
    OP_52(0x2C, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6E87")

    label("loc_6E7D")

    OP_52(0x2C, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x2C, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6E87")

    OP_52(0x2C, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x2C, 0x10)
    Sleep(50)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x2B, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x2B, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x2B, 0x10)
    TurnDirection(0x2B, 0x0, 0)
    OP_52(0x2B, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x2B, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x2B, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x2B, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x2B, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2B, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x2B, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x2B, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x2B, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6F40")
    Jump("loc_6F8A")

    label("loc_6F40")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2B, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6F60")
    OP_52(0x2B, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6F8A")

    label("loc_6F60")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2B, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6F80")
    OP_52(0x2B, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6F8A")

    label("loc_6F80")

    OP_52(0x2B, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x2B, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6F8A")

    OP_52(0x2B, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x2B, 0x10)
    Sleep(100)

    ChrTalk(
        0x2C,
        (
            "#07205FOh, if it isn't the Support Section?\x02\x03",
            "#07209FWhy don't you join us for\x01",
            "a little chat, if you please?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FAh, yes. \x01",
            "If we're not interrupting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FBy the way, what were\x01",
            "you talking about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        (
            "#02804FOur prince here is actually a\x01",
            "member of the board of directors\x01",
            "of an Imperial military academy.\x02\x03",
            "#02800FI was speaking with him about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205FDirector... That is one of the people\x01",
            "responsible for a school, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00302FWhoa, you're doin' that too?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2C,
        (
            "#07204FHu hu. It's nothing more than\x01",
            "me having my name put there.\x02\x03",
            "#07202FIn that sense, I can say that\x01",
            "Mayor Dieter is contributing\x01",
            "way more than myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FMayor Dieter...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        (
            "#02804FAh, no, he just means\x01",
            "in a business level sense.\x02\x03",
            "#02800FThat military academy received a small\x01",
            "amount of funding from IBC for the\x01",
            "Epstein Foundation's orbal net test.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FS-So that's what happened.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205FNow that you mention it, I\x01",
            "heard orbal net tests had\x01",
            "started in the Empire...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHu hu. As expected from an international\x01",
            "bank with branch offices in each nation. \x01",
            "Your business scope is enormous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2C,
        (
            "#07202FHmm. I feel having had this\x01",
            "conversation with you was fate too.\x02\x03",
            "#07209FIf there's an opportunity, would\x01",
            "you feel like giving a special\x01",
            "lecture at my military academy?\x02\x03",
            "#07212FIf you're interested, be aware\x01",
            "that relations between lecturers\x01",
            "and students are prohibited.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00006FW-What're you talking about?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x2B, 0x1)

    ChrTalk(
        0x2B,
        (
            "#02809FHa ha. You must be quite\x01",
            "pleased, Prince Olivert.\x02\x03",
            "After this, I'd like to have\x01",
            "a relaxed chat over drinks.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x2C, 0x0)

    ChrTalk(
        0x2C,
        (
            "#07209FUh uh, indeed. \x01",
            "I would love to join you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2B, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x2C, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)

    ChrTalk(
        0x102,
        (
            "#00109F(His Highness and "uncle"...\x01",
            "It looks like they've really hit it off.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F(Yeah. Maybe they get along because\x01",
            "their hobbies have the same scale?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C3, 7)
    Jump("loc_7883")

    label("loc_7742")


    ChrTalk(
        0x2B,
        (
            "#02805FBy the way, can you\x01",
            "hold your liquor?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2C,
        (
            "#07202FYeah, to a certain extent.\x02\x03",
            "#07204F...Although in this world, there's\x01",
            "someone who is a lot better than me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F(His Highness... He has a\x01",
            "distant look, somehow.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(...? I wonder if he has some kind of\x01",
            "important memories related to alcohol?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7883")

    Return()

    # Function_37_6CC4 end

    def Function_38_7884(): pass

    label("Function_38_7884")

    TalkBegin(0xFE)
    Call(0, 37)
    TalkEnd(0xFE)
    Return()

    # Function_38_7884 end

    def Function_39_788E(): pass

    label("Function_39_788E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_78A1")
    Call(0, 51)
    Return()

    label("loc_78A1")

    TalkBegin(0xFE)

    ChrTalk(
        0x14,
        (
            "#11501FOh, is that Armorica Village?\x02\x03",
            "#11509FThe bees are diligently carrying honey.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00006FC'mon. There's no way you can see that.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_39_788E end

    def Function_40_7999(): pass

    label("Function_40_7999")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A78")

    ChrTalk(
        0xFE,
        (
            "We have been held here ever since\x01",
            "martial law was declared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Come to think of it, the\x01",
            "President had a girl with a\x01",
            "mysterious aura with him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Could she have been the\x01",
            "rumored "Divine Child"?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_7AEC")

    label("loc_7A78")


    ChrTalk(
        0xFE,
        (
            "The President had a\x01",
            "girl with a mysterious\x01",
            "aura with him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Could she have been the\x01",
            "rumored "Divine Child"?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7AEC")

    TalkEnd(0xFE)
    Return()

    # Function_40_7999 end

    def Function_41_7AF0(): pass

    label("Function_41_7AF0")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Ever since the independence\x01",
            "invalidity declaration, we who work\x01",
            "in the tower have remained uneasy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "W-Who could have thought this would\x01",
            "happen. And what will happen now...?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_41_7AF0 end

    def Function_42_7BAD(): pass

    label("Function_42_7BAD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D80")

    ChrTalk(
        0xFE,
        "L-Lady Elie...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FMiss Lanfei... Thank\x01",
            "goodness you're safe.\x02\x03",
            "It looks like all the IBC\x01",
            "personnel are assembled here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Y-Yes... Just as Milady\x01",
            "Mariabell ordered...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The situation in the city has become\x01",
            "troublesome... What are Mr. Dieter\x01",
            "and Milady Mariabell up to...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F...Anyway, please stay\x01",
            "here for the time being.\x02\x03",
            "We'll do something\x01",
            "about this situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "U-Understood... \x01",
            "I will leave it to you, then.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_7DF4")

    label("loc_7D80")


    ChrTalk(
        0xFE,
        (
            "I wonder what are Mr. Dieter\x01",
            "and Milady Mariabell up to...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...And, I am sure that person with him was...\x02",
    )

    CloseMessageWindow()

    label("loc_7DF4")

    TalkEnd(0xFE)
    Return()

    # Function_42_7BAD end

    def Function_43_7DF8(): pass

    label("Function_43_7DF8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7EF3")

    ChrTalk(
        0xFE,
        (
            "The President and the others aren't on this floor...\x01",
            "But maybe the others know something about them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Leave this place to me for now. \x01",
            "Feel free to conduct your investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...However, don't do anything reckless.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 3)
    Jump("loc_7F6F")

    label("loc_7EF3")


    ChrTalk(
        0xFE,
        (
            "Leave this place to me for now. \x01",
            "Feel free to conduct your investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...However, don't do anything reckless.\x02",
    )

    CloseMessageWindow()

    label("loc_7F6F")

    TalkEnd(0xFE)
    Return()

    # Function_43_7DF8 end

    def Function_44_7F73(): pass

    label("Function_44_7F73")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8049")

    ChrTalk(
        0xFE,
        (
            "I believed in Miss Mariabell and remained\x01",
            "in the technology division, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Clay said he couldn't\x01",
            "believe her and left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We fought and split up...\x01",
            "But it appears\x01",
            "Clay was right.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 4)
    Jump("loc_80B5")

    label("loc_8049")


    ChrTalk(
        0xFE,
        (
            "...It appears that\x01",
            "Clay was right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Though we fought and split up,\x01",
            "I wonder if we can reconcile...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_80B5")

    TalkEnd(0xFE)
    Return()

    # Function_44_7F73 end

    def Function_45_80B9(): pass

    label("Function_45_80B9")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "When martial law was handed\x01",
            "down, information within the\x01",
            "city was completely shut off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We can't use the orbal\x01",
            "terminals either. Goodness...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_45_80B9 end

    def Function_46_8156(): pass

    label("Function_46_8156")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8283")

    ChrTalk(
        0xFE,
        (
            "The security department needs a\x01",
            "certain understanding of tower\x01",
            "structure and personnel duties.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But ever since we moved into Orchis Tower, I got\x01",
            "the feeling there were more things hidden than usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What in the world are Milady Mariabell\x01",
            "and the President doing...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 5)
    Jump("loc_82CB")

    label("loc_8283")


    ChrTalk(
        0xFE,
        (
            "What in the world are Milady Mariabell\x01",
            "and the President doing...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_82CB")

    TalkEnd(0xFE)
    Return()

    # Function_46_8156 end

    def Function_47_82CF(): pass

    label("Function_47_82CF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_83EF")

    ChrTalk(
        0xFE,
        (
            "The jaeger corps "Red Constellation", with a\x01",
            "threat rating of S... I suspected President\x01",
            "Dieter of being connected to them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't believe those guys who destroyed\x01",
            "IBC are wandering around so brazenly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...The President... He can no longer be trusted.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 6)
    Jump("loc_8426")

    label("loc_83EF")


    ChrTalk(
        0xFE,
        (
            "President Dieter... \x01",
            "He can no longer be trusted.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8426")

    TalkEnd(0xFE)
    Return()

    # Function_47_82CF end

    def Function_48_842A(): pass

    label("Function_48_842A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8520")

    ChrTalk(
        0xC,
        (
            "#11228FI think... My father has been\x01",
            "worried this whole time.\x02\x03",
            "About mother... And me...\x02\x03",
            "While overthinking about many things...\x01",
            "He became unable to turn back...\x02\x03",
            "#11227F...Everyone...\x01",
            "Please take care\x01",
            "of my father...!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 7)
    Jump("loc_8558")

    label("loc_8520")


    ChrTalk(
        0xC,
        (
            "#11227FEveryone...\x01",
            "Please, take\x01",
            "care of my father!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8558")

    TalkEnd(0xFE)
    Return()

    # Function_48_842A end

    def Function_49_855C(): pass

    label("Function_49_855C")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x11, 0xFF)
    SetChrFlags(0x12, 0x80)
    OP_68(110010, 1100, -102270, 0)
    MoveCamera(30, 30, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16290, 0)
    SetChrPos(0x101, 109100, 0, -103400, 90)
    SetChrPos(0x102, 108800, 0, -102500, 90)
    SetChrPos(0x103, 107600, 0, -103100, 90)
    SetChrPos(0x104, 107300, 0, -102200, 90)
    SetChrPos(0xF4, 109000, 0, -100900, 135)
    SetChrPos(0xF5, 108000, 0, -100300, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_88A8")

    ChrTalk(
        0x11,
        (
            "#11PGood work, Special\x01",
            "Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F#6PYes, likewise.\x02\x03",
            "#00005FCould this room be...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#11PYes, it's President Crois'... \x01",
            "No, suspect Crois'.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#6P#00108F...How is the President doing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#11PWhen he was arrested he\x01",
            "looked dumbfounded...\x01",
            "But now he looks calm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#11PHe shows no signs of\x01",
            "resisting, so we have only a\x01",
            "minimum number of personnel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#11PPer direction of Inspector Sergei,\x01",
            "you all are allowed to see him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00306FI see..\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00208F...Mr. Lloyd, what should we do?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AF, 7)
    Jump("loc_8927")

    label("loc_88A8")


    ChrTalk(
        0x11,
        (
            "#11PSuspect Crois\x01",
            "is detained\x01",
            "in this room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#11PPer direction of Inspector Sergei,\x01",
            "you all are allowed to see him...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8927")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8931")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A44")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Meet with Dieter\x01",      # 0
            "Not Right Now\x01",         # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_899A")
    Call(0, 50)
    Return()

    label("loc_899A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8A3F")

    ChrTalk(
        0x101,
        "#6P#00006F...We won't right now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#11PUnderstood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#11PIf you decide you do want\x01",
            "to meet with suspect Crois,\x01",
            "please speak with me again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A3F")

    Jump("loc_8931")

    label("loc_8A44")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0x11, 0xFF)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 110390, 0, -126470, 0)
    BeginChrThread(0x12, 0, 0, 1)
    EventEnd(0x5)
    Return()

    # Function_49_855C end

    def Function_50_8A7B(): pass

    label("Function_50_8A7B")


    ChrTalk(
        0x101,
        (
            "#6P#00003F...If you please.\x02\x03",
            "#00008FWhat is he thinking about right now?\x01",
            "...I feel I want to ask him that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00106F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#11PUnderstood... Go ahead, then.\x02",
    )

    CloseMessageWindow()
    OP_93(0x11, 0x0, 0x1F4)

    def lambda_8B3A():
        OP_95(0xFE, 111300, 0, -101000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8B3A)
    WaitChrThread(0x11, 1)
    OP_93(0x11, 0xE1, 0x1F4)
    ClearMapObjFlags(0x2, 0x10)
    BeginChrThread(0x101, 3, 0, 94)
    Sleep(700)
    Sound(103, 0, 100, 0)
    OP_71(0x2, 0x0, 0x5, 0x0, 0x0)
    BeginChrThread(0x102, 3, 0, 94)
    Sleep(300)
    FadeToDark(1000, 0, -1)
    BeginChrThread(0x103, 3, 0, 94)
    Sleep(600)
    BeginChrThread(0x104, 3, 0, 94)
    OP_0D()
    LoadChrToIndex("apl/ch51716.itc", 0x28)
    SetChrChipByIndex(0x2B, 0x28)
    SetChrSubChip(0x2B, 0x0)
    SetChrPos(0x2B, 156990, 0, 110700, 45)
    OP_8E(0x2B, "President Dieter")
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)
    OP_68(156330, 1500, 108970, 0)
    MoveCamera(39, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16050, 0)
    SetChrPos(0x11, 162130, 0, 110210, 225)
    SetChrPos(0x27, 161880, 0, 102310, 315)
    OP_4B(0x27, 0xFF)
    SetChrPos(0x101, 156570, 0, 108170, 356)
    SetChrPos(0x102, 158130, 0, 108480, 322)
    SetChrPos(0x103, 158750, 0, 107480, 315)
    SetChrPos(0x104, 159040, 0, 108660, 322)
    SetChrPos(0xF4, 155360, 0, 107640, 45)
    SetChrPos(0xF5, 157370, 0, 107370, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0xF4, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0xF5, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetCameraDistance(14610, 2000)
    FadeToBright(500, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x2B,
        (
            "#11301F#5P......You guys?\x02\x03",
            "#11304F...Hu hu, what do you want from me,\x01",
            "an international criminal now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00001F...Mr. Dieter.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00108F......"Uncle"......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        (
            "#11306F#5P...Being alone like this,\x01",
            "I finally realized.\x02\x03",
            "It's as Bell said. I did\x01",
            "nothing more than act as\x01",
            "Mr. Grimwood wanted me to.\x02\x03",
            "#11303FWith a loud voice, I held the ideal of "justice",\x01",
            "and for that reason, sacrifices were acceptable.\x02\x03",
            "#11311F...And what was the result? I've even\x01",
            "been abandoned by my only daughter,\x01",
            "and now I've lost the presidency.\x02\x03",
            "#11302F...Ha ha ha ha... I'm not that boy\x01",
            "from the "Society", but I'm just\x01",
            "as pitiful as a "fool".\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x4, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x5, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)
    OP_64(0x4)
    OP_64(0x5)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#12P#00006F...We can't deny all of that.\x01\x02\x03",
            "#00008FFor your own "justice", you stubbornly\x01",
            "sticked to your beliefs...\x02\x03",
            "#00001FRegardless of your methods, the fact\x01",
            "that you were trying to protect\x01",
            "Crossbell is the absolute truth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303F...Right.\x02\x03",
            "#00301FWe too really felt it\x01",
            "in the words you said\x01",
            "back then at IBC.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203F"Humans are creatures that desire justice"... \x01",
            "It could certainly be said that.\x02\x03",
            "#00208FAnd through the declaration of independence,\x01",
            "that the citizens approved, you really felt\x01",
            "the charm of that "justice" you were pursuing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        "#11303F#5P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00106FBut in the end, I think your\x01",
            "methods were wrong.\x02\x03",
            "#00108FIf the independent state would have continued\x01",
            "to exist like that, your "justice" recognized\x01",
            "and peace obtained, "uncle"...\x02\x03",
            "The wounds of the people discarded in the \x01",
            "process wouldn't have easily healed.\x02\x03",
            "#00101FA peace obtained on the premise\x01",
            "of sacrificing people...\x02\x03",
            "Doesn't that make the declaration\x01",
            "of independence you uttered on the\x01",
            "platform that day "deception" itself?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        (
            "#11304F#5P...Hu hu. You're right, Elie.\x01",
            "It's as you say.\x02\x03",
            "By obtaining the power called "KeA",\x01",
            "maybe I became blinded\x01",
            "by my own "justice".\x02\x03",
            "#11302FMr. Grimwood saw I had deceived\x01",
            "myself without realizing it, and\x01",
            "I became easy to manipulate.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9546")

    ChrTalk(
        0x10A,
        "#12P#00603F(...Lawyer Ian...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_95A5")

    label("loc_9546")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9578")

    ChrTalk(
        0x105,
        "#12P#10403F............\x02",
    )

    CloseMessageWindow()
    Jump("loc_95A5")

    label("loc_9578")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_95A5")

    ChrTalk(
        0x106,
        "#12P#10703F............\x02",
    )

    CloseMessageWindow()

    label("loc_95A5")


    ChrTalk(
        0x2B,
        (
            "#11303F#5PHowever... "Justice" is something\x01",
            "exercised through power and will. \x01",
            "That idea itself doesn't change.\x02\x03",
            "#11301FIf you all would continue your\x01",
            "own pursuit of "justice"...\x02\x03",
            "You need to show Mr. Grimwood and\x01",
            "the others your own power and will.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006F...It won't be easy... But we'll\x01",
            "do it, no matter what it takes.\x02\x03",
            "#00013FWe'll have to, if we're\x01",
            "going to take back KeA...!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9766")

    ChrTalk(
        0x106,
        "#12P#10701F...That's right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_97D0")

    label("loc_9766")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_979B")

    ChrTalk(
        0x109,
        "#12P#10101FYes, of course.\x02",
    )

    CloseMessageWindow()
    Jump("loc_97D0")

    label("loc_979B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_97D0")

    ChrTalk(
        0x105,
        "#12P#10402FHu hu, that's right.\x02",
    )

    CloseMessageWindow()

    label("loc_97D0")


    ChrTalk(
        0x2B,
        (
            "#11301F#5P...In that case, you have\x01",
            "no further use for me.\x02\x03",
            "#11303FMr. Grimwood said it himself... Even though\x01",
            "she's my daughter, I honestly have no idea\x01",
            "how far Bell is willing to go.\x02\x03",
            "#11304FTaking back KeA...\x01",
            "Will you be able to move forward or not...?\x02\x03",
            "#11300FI will ascertain that from this place.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_70(0x2, 0x0)
    SetChrPos(0x11, 111300, 0, -102500, 270)
    SetChrPos(0x27, -3110, 0, 1600, 90)
    SetChrPos(0x101, 109100, 0, -103400, 90)
    SetChrPos(0x102, 109600, 0, -101800, 90)
    SetChrPos(0x103, 107600, 0, -103600, 90)
    SetChrPos(0x104, 107000, 0, -102400, 90)
    SetChrPos(0xF4, 108500, 0, -100900, 135)
    SetChrPos(0xF5, 107500, 0, -100800, 135)
    OP_68(109860, 400, -101510, 0)
    MoveCamera(44, 29, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17830, 0)
    TurnDirection(0x101, 0x102, 0)
    TurnDirection(0x103, 0x102, 0)
    TurnDirection(0x104, 0x102, 0)
    TurnDirection(0xF4, 0x102, 0)
    TurnDirection(0xF5, 0x102, 0)
    FadeToBright(500, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x102,
        "#5P#00106F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00301FMilady...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00208F...Are you all right?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 500)
    Sleep(150)

    ChrTalk(
        0x102,
        (
            "#5P#00104F...Yes, I'm fine.\x02\x03",
            "#00108FI was worried a little because Bell\x01",
            "discarded him like that, but...\x02\x03",
            "#00102FHe was surprisingly composed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00004F...Yeah. I was a little relieved too.\x02\x03",
            "#00000FIt's like he said... \x01",
            "We need to move forward.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 110390, 0, -126470, 0)
    BeginChrThread(0x12, 0, 0, 1)
    OP_4C(0x11, 0xFF)
    OP_4C(0x27, 0xFF)
    SetChrPos(0x0, 109100, 0, -103400, 180)
    SetScenarioFlags(0x1AF, 6)
    EventEnd(0x5)
    Return()

    # Function_50_8A7B end

    def Function_51_9BB0(): pass

    label("Function_51_9BB0")

    EventBegin(0x0)
    OP_4B(0x14, 0xFF)
    Fade(500)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu11500.itp")
    OP_68(158620, 1300, 109080, 0)
    MoveCamera(36, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16290, 0)
    SetChrPos(0x101, 158620, 0, 109080, 45)
    SetChrPos(0x102, 157420, 0, 109080, 45)
    SetChrPos(0x103, 159110, 0, 107900, 45)
    SetChrPos(0x104, 157120, 0, 107350, 45)
    SetChrPos(0x109, 156000, 0, 107350, 45)
    SetChrPos(0x105, 155330, 0, 107970, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    ChrTalk(
        0x14,
        (
            "#11P#11504FMan, what a\x01",
            "first class view.\x02\x03",
            "#11500FDon't you agree too,\x01",
            "Special Support Section?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00011FMr. Lechter...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00108FWhat're you doing here...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#11P#11504FHa ha, surely there's nothing strange about \x01",
            "the staff of His Excellency the Chancellor,\x01",
            "being in the same waiting room, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x14, 0xE1, 0x1F4)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 3)), scpexpr(EXPR_END)), "loc_9E6C")

    AnonymousTalk(
        0x14,
        (
            "Hey, we meet again.\x02\x03",
            "Umm, no... I guess the\x01",
            "first time was by mistake.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_9ED4")

    label("loc_9E6C")


    AnonymousTalk(
        0x14,
        (
            "It's been several weeks\x01",
            "since we last met.\x02\x03",
            "Umm, no... The first time\x01",
            "was a mistake, wasn't it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_9ED4")

    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    ChrTalk(
        0x102,
        (
            "#6P#00106FUmm... Please, don't joke around\x01",
            "with such a serious look on your face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00211F...How should I say it.\x01",
            "Cunning, as always.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#11P#11509FHa ha, that's my charm\x01",
            "point, you see!\x02\x03",
            "#11502FBut, it looks like you wanted\x01",
            "to say something since before?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FYes. Thankfully, we got\x01",
            "word of several situations.\x02\x03",
            "#00013FAbout the actions of your Imperial government...\x01",
            "Regarding this Trade Conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#11P#11510FHmm, I see. \x01",
            "I don't know how much \x01",
            "you've learned, but...\x02\x03",
            "#11504FThen, do you know this?\x02\x03",
            "#11501F――I'm actually collaborating with the "Noble\x01",
            "Faction", and I'm after Giliath Osborne's life.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#6P#10107FWhat...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10301FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106F...Don't be deceived. \x01",
            "Just look at who's saying it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00301FWe won't fall for\x01",
            "that one again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00211FHe is making fun of us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#11P#11509FHah ha, oh well then.\x02\x03",
            "#11502FI was hoping for a\x01",
            "better reaction, to\x01",
            "tell you the truth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FHu hu, so the punchline isn't\x01",
            "that it's actually true?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006F...Secretary Lechter. Given your position,\x01",
            "I don't care at all what you're after.\x02\x03",
            "#00008FBut from my point of view... You're the\x01",
            "type that takes responsibility and follows\x01",
            "through, no matter what kind of job it is.\x02\x03",
            "#00001FBecause of that, you should at\x01",
            "least be able to help us with\x01",
            "security during the conference...\x02\x03",
            "#00000F──Am I wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#11P#11504FHehe... I see.\x02\x03",
            "#11508FWell, that remark before was a joke... but you\x01",
            "could imagine something like that happening, right?\x02\x03",
            "#11501FWe must always search\x01",
            "for all the patterns.\x02\x03",
            "#11509FThat's the key to being a good writer, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x4, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x5, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00006FI think no one here wants\x01",
            "to become an author...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00301FMan, just how much is this\x01",
            "guy goin' to tease us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#11P#11504FWell, that's all the advice\x01",
            "I can give for the moment.\x02\x03",
            "#11500FYou should think about the various\x01",
            "cases, and be ready for any of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10106F...Thank you very much for the advice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006F(*sigh*... I really\x01",
            "can't read him at all.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00108F(Right. I feel it's because\x01",
            "he threw us off guard.)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x14, 0x0, 0x0)
    OP_4C(0x14, 0xFF)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x1C4, 3)
    Call(0, 53)
    EventEnd(0x5)
    Return()

    # Function_51_9BB0 end

    def Function_52_A868(): pass

    label("Function_52_A868")

    Sound(160, 0, 100, 0)
    Return()

    # Function_52_A868 end

    def Function_53_A86F(): pass

    label("Function_53_A86F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A897")
    SetScenarioFlags(0x146, 3)

    label("loc_A897")

    Return()

    # Function_53_A86F end

    def Function_54_A898(): pass

    label("Function_54_A898")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05600.itc", 0x28)
    LoadChrToIndex("apl/ch51231.itc", 0x29)
    CreatePortrait(0, 16, 192, 528, 256, 0, 20, 512, 64, 0, 0, 512, 64, 0xFFFFFF, 0x0, "c_vis506.itp")
    OP_68(81000, 1000, 4000, 0)
    MoveCamera(50, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, 81000, 0, 5500, 180)
    SetChrPos(0x102, 81000, 0, 5500, 180)
    SetChrPos(0x103, 81000, 0, 5500, 180)
    SetChrPos(0x104, 81000, 0, 5500, 180)
    SetChrPos(0x109, 81000, 0, 5500, 180)
    SetChrPos(0x105, 81000, 0, 5500, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x2B, 0x28)
    SetChrSubChip(0x2B, 0x0)
    ClearChrFlags(0x2B, 0x80)
    SetChrFlags(0x2B, 0x8000)
    SetChrPos(0x2B, 81000, 0, 5500, 180)
    OP_A7(0x2B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(79000, 1000, 300, 5000)
    SetCameraDistance(18500, 5000)
    BeginChrThread(0x101, 0, 0, 55)
    FadeToBright(1000, 0)
    OP_0D()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(3500)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 3)
    OP_6F(0x79)

    ChrTalk(
        0x2B,
        (
            "#6P#02803FThis is a floor of rooms I've prepared\x01",
            "for the heads of state who will be\x01",
            "participating in the conference.\x02\x03",
            "#02800FLet me show you around a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#11PPlease do.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x2B, 0xFF)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    SetChrPos(0x101, 112700, 0, -131500, 270)
    SetChrPos(0x102, 112700, 0, -130000, 270)
    SetChrPos(0x103, 113900, 0, -131100, 270)
    SetChrPos(0x104, 113900, 0, -129600, 270)
    SetChrPos(0x109, 115100, 0, -131300, 270)
    SetChrPos(0x105, 115100, 0, -129800, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x2B, 111000, 0, -130500, 270)
    SetChrPos(0x35, 111000, -600, -130500, 270)
    OP_68(109220, 1500, -130990, 0)
    MoveCamera(34, 22, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(21500, 0)
    SetChrFlags(0x35, 0x20)
    SetChrFlags(0x35, 0x40)
    SetChrFlags(0x35, 0x8)
    SetChrFlags(0x35, 0x4)
    ClearScenarioFlags(0x0, 0)
    ClearScenarioFlags(0x0, 1)
    ClearScenarioFlags(0x0, 2)
    OP_68(108910, 1500, -111640, 13000)
    FadeToBright(1000, 0)
    BeginChrThread(0x2B, 3, 0, 63)
    BeginChrThread(0x35, 3, 0, 64)
    Sleep(50)
    BeginChrThread(0x101, 3, 0, 65)
    Sleep(400)
    BeginChrThread(0x103, 3, 0, 67)
    Sleep(100)
    BeginChrThread(0x102, 3, 0, 66)
    BeginChrThread(0x109, 3, 0, 69)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 68)
    Sleep(100)
    BeginChrThread(0x105, 3, 0, 70)
    OP_0D()
    WaitChrThread(0x2B, 3)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    FadeToDark(1000, 0, -1)
    BeginChrThread(0x101, 3, 0, 71)
    Sleep(900)
    BeginChrThread(0x102, 3, 0, 71)
    OP_0D()
    EndChrThread(0x2B, 0xFF)
    EndChrThread(0x35, 0xFF)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    SetChrPos(0x101, 153000, 0, 55500, 90)
    SetChrPos(0x102, 152600, 0, 56800, 90)
    SetChrPos(0x103, 152600, 0, 53900, 135)
    SetChrPos(0x104, 151900, 0, 57900, 45)
    SetChrPos(0x109, 151700, 0, 55500, 90)
    SetChrPos(0x105, 150800, 0, 53700, 135)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x2B, 149300, 0, 56000, 90)
    OP_A7(0x2B, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_68(163300, 1500, 56000, 0)
    MoveCamera(53, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21000, 0)
    OP_68(153300, 900, 56000, 5000)
    SetCameraDistance(18000, 5000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x104,
        "#00305F#5POh, it's so extravagant!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FHu hu, I'd like to gracefully\x01",
            "spend time in a room like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        (
            "#6P#02804FThis is Prince Olivert's\x01",
            "waiting room.\x02\x03",
            "#02800FThere're rooms in the left wing as well, and\x01",
            "each participant has been assigned a room.\x02\x03",
            "#02809FIt's a place to cool heads if they get too\x01",
            "hot in the conference, if you get my meaning.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AF4F():
        TurnDirection(0x101, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AF4F)
    Sleep(50)

    def lambda_AF5F():
        TurnDirection(0x109, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_AF5F)
    Sleep(50)

    def lambda_AF6F():
        TurnDirection(0x102, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_AF6F)
    Sleep(50)

    def lambda_AF7F():
        TurnDirection(0x105, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_AF7F)
    Sleep(50)

    def lambda_AF8F():
        TurnDirection(0x103, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_AF8F)
    Sleep(50)

    def lambda_AF9F():
        TurnDirection(0x104, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_AF9F)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x109,
        "#11P#10112FI-I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205F#11PAre there orbal cables\x01",
            "in these rooms, too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        (
            "#6P#02805FYes, I had them wired\x01",
            "inconspicuously.\x02\x03",
            "#02804FSetting those other\x01",
            "rooms aside──\x02\x03",
            "#02800FI've one final\x01",
            "place to show you.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6B(0x35)
    EndChrThread(0x2B, 0xFF)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    OP_A7(0x2B, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(12000, 900, -130000, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, 12200, 0, -129300, 270)
    SetChrPos(0x102, 11600, 0, -130699, 270)
    SetChrPos(0x103, 13300, 0, -129800, 270)
    SetChrPos(0x104, 13000, 0, -131000, 270)
    SetChrPos(0x109, 14400, 0, -129300, 270)
    SetChrPos(0x105, 14700, 0, -130699, 270)
    SetChrPos(0x2B, 10000, 0, -130000, 270)
    SetChrPos(0x35, 12000, -600, -130000, 270)
    SetChrChipByIndex(0x11, 0x0)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 7400, 0, -127600, 225)
    SetChrChipByIndex(0x12, 0x0)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, -7400, 0, -127600, 135)

    def lambda_B218():
        OP_98(0xFE, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x35, 1, lambda_B218)

    def lambda_B232():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_B232)
    Sleep(50)

    def lambda_B24F():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B24F)
    Sleep(50)

    def lambda_B26C():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B26C)
    Sleep(50)

    def lambda_B289():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B289)
    Sleep(50)

    def lambda_B2A6():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B2A6)
    Sleep(50)

    def lambda_B2C3():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0xFFFFFED4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B2C3)
    Sleep(50)

    def lambda_B2E0():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B2E0)
    FadeToBright(1000, 0)
    Sleep(600)

    def lambda_B306():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B306)
    Sleep(300)

    def lambda_B31A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B31A)
    Sleep(600)

    def lambda_B32E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_B32E)
    Sleep(300)

    def lambda_B342():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_B342)
    OP_0D()
    OP_4B(0x11, 0xFF)
    SetChrChipByIndex(0x11, 0x29)
    SetChrSubChip(0x11, 0x0)

    ChrTalk(
        0x11,
        "#12A#5PGood morning, Mayor Dieter!\x02",
    )

    Sleep(1200)
    OP_57(0x0)
    OP_5A()
    Sleep(2500)
    OP_4B(0x12, 0xFF)
    SetChrChipByIndex(0x12, 0x29)
    SetChrSubChip(0x12, 0x0)

    ChrTalk(
        0x12,
        "#12A#5PThank you for your hard work!\x02",
    )

    Sleep(1200)
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x2B, 1)

    ChrTalk(
        0x2B,
        "#02809F#11PHa ha, at ease, please.\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x35, 1)
    OP_6B(0xFF)
    WaitChrThread(0x105, 1)
    OP_93(0x2B, 0x5A, 0x1F4)

    ChrTalk(
        0x2B,
        (
            "#6P#02804FFrom these corridor windows, you can\x01",
            "get a full view of the conference.\x02\x03",
            "#02800FDuring confidential meetings\x01",
            "the curtains are closed, but\x01",
            "they will be open this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#11PI see...\x02",
    )

    CloseMessageWindow()

    def lambda_B4D8():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B4D8)
    Sleep(50)

    def lambda_B4E8():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_B4E8)
    Sleep(50)

    def lambda_B4F8():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B4F8)
    Sleep(50)

    def lambda_B508():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B508)
    Sleep(50)

    def lambda_B518():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_B518)
    Sleep(50)

    def lambda_B528():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_B528)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    OP_68(-2000, 1500, -124000, 3000)
    MoveCamera(35, 17, 0, 3000)
    SetCameraDistance(19500, 3000)

    def lambda_B572():
        OP_97(0x101, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B572)
    Sleep(200)

    def lambda_B58F():
        OP_97(0x103, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_B58F)
    Sleep(200)

    def lambda_B5AC():
        OP_97(0x109, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B5AC)
    Sleep(200)

    def lambda_B5C9():
        OP_97(0x102, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B5C9)
    Sleep(200)

    def lambda_B5E6():
        OP_97(0x104, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_B5E6)
    Sleep(200)

    def lambda_B603():
        OP_97(0x105, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_B603)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)

    def lambda_B635():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_B635)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00002F#11PIt's great to be able to check on\x01",
            "the conference room like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#11PThat's right. If anything happens,\x01",
            "we could be there right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F#11PIn that case, I want to make\x01",
            "this part of our patrol route.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-3000, 900, -128000, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    OP_0D()

    ChrTalk(
        0x2B,
        (
            "#6P#02803FNow then. With this, I've showed\x01",
            "you the three secure floors...\x02\x03",
            "#02800FBut, if you'll allow me to show\x01",
            "this last place I've been saving...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B804():
        TurnDirection(0x101, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B804)
    Sleep(50)

    def lambda_B814():
        TurnDirection(0x109, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B814)
    Sleep(50)

    def lambda_B824():
        TurnDirection(0x102, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B824)
    Sleep(50)

    def lambda_B834():
        TurnDirection(0x105, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_B834)
    Sleep(50)

    def lambda_B844():
        TurnDirection(0x103, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_B844)
    Sleep(50)

    def lambda_B854():
        TurnDirection(0x104, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_B854)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x101,
        "#00005F#5PA place you've been saving?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00302F#11PHuh? Where's that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        (
            "#6P#02809FHu hu, the place with the\x01",
            "best view in this building\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(19500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 1)
    NewScene("c1600", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_54_A898 end

    def Function_55_B92D(): pass

    label("Function_55_B92D")

    Sound(160, 0, 100, 0)
    Sleep(500)
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x7, 0x10)
    OP_71(0x7, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x7)
    BeginChrThread(0x2B, 3, 0, 56)
    Sleep(900)
    BeginChrThread(0x101, 3, 0, 57)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 58)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 59)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 60)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 61)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 62)
    Sleep(1300)
    Sound(107, 0, 100, 0)
    OP_71(0x7, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x7)
    SetMapObjFlags(0x7, 0x10)
    Return()

    # Function_55_B92D end

    def Function_56_B9AC(): pass

    label("Function_56_B9AC")


    def lambda_B9B1():
        OP_95(0xFE, 81000, 0, 1500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B9B1)

    def lambda_B9CB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B9CB)
    WaitChrThread(0xFE, 1)

    def lambda_B9E0():
        OP_95(0xFE, 77500, 0, -1000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B9E0)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_56_B9AC end

    def Function_57_BA01(): pass

    label("Function_57_BA01")


    def lambda_BA06():
        OP_95(0xFE, 81000, 0, 2000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BA06)

    def lambda_BA20():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BA20)
    WaitChrThread(0xFE, 1)

    def lambda_BA35():
        OP_95(0xFE, 79200, 0, -400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BA35)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_57_BA01 end

    def Function_58_BA56(): pass

    label("Function_58_BA56")


    def lambda_BA5B():
        OP_95(0xFE, 81000, 0, 2000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BA5B)

    def lambda_BA75():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BA75)
    WaitChrThread(0xFE, 1)

    def lambda_BA8A():
        OP_95(0xFE, 78300, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BA8A)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_58_BA56 end

    def Function_59_BAAB(): pass

    label("Function_59_BAAB")


    def lambda_BAB0():
        OP_95(0xFE, 81000, 0, 2500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BAB0)

    def lambda_BACA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BACA)
    WaitChrThread(0xFE, 1)

    def lambda_BADF():
        OP_95(0xFE, 80400, 0, -100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BADF)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_59_BAAB end

    def Function_60_BB00(): pass

    label("Function_60_BB00")


    def lambda_BB05():
        OP_95(0xFE, 81000, 0, 2500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BB05)

    def lambda_BB1F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BB1F)
    WaitChrThread(0xFE, 1)

    def lambda_BB34():
        OP_95(0xFE, 79500, 0, 800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BB34)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_60_BB00 end

    def Function_61_BB55(): pass

    label("Function_61_BB55")


    def lambda_BB5A():
        OP_95(0xFE, 81000, 0, 3000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BB5A)

    def lambda_BB74():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BB74)
    WaitChrThread(0xFE, 1)

    def lambda_BB89():
        OP_95(0xFE, 80800, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BB89)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_61_BB55 end

    def Function_62_BBAA(): pass

    label("Function_62_BBAA")


    def lambda_BBAF():
        OP_95(0xFE, 81000, 0, 3000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BBAF)

    def lambda_BBC9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BBC9)
    WaitChrThread(0xFE, 1)

    def lambda_BBDE():
        OP_95(0xFE, 79900, 0, 2100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BBDE)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_62_BBAA end

    def Function_63_BBFF(): pass

    label("Function_63_BBFF")


    def lambda_BC04():
        OP_95(0xFE, 109000, 0, -130500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BC04)
    WaitChrThread(0xFE, 1)

    def lambda_BC22():
        OP_95(0xFE, 109000, 0, -112500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BC22)
    WaitChrThread(0xFE, 1)

    def lambda_BC40():
        OP_95(0xFE, 111000, 0, -110500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BC40)
    WaitChrThread(0xFE, 1)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0x5, 0x0, 0x0)

    def lambda_BC76():
        OP_95(0xFE, 113000, 0, -110500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BC76)
    Sleep(500)

    def lambda_BC93():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BC93)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_63_BBFF end

    def Function_64_BCA4(): pass

    label("Function_64_BCA4")


    def lambda_BCA9():
        OP_95(0xFE, 109000, -600, -130500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BCA9)
    WaitChrThread(0xFE, 1)
    Sleep(1000)
    MoveCamera(35, 19, 0, 7000)
    SetCameraDistance(19000, 7000)

    def lambda_BCDE():
        OP_95(0xFE, 109000, -600, -112500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BCDE)
    WaitChrThread(0xFE, 1)

    def lambda_BCFC():
        OP_95(0xFE, 111000, -600, -110500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BCFC)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_64_BCA4 end

    def Function_65_BD16(): pass

    label("Function_65_BD16")


    def lambda_BD1B():
        OP_97(0xFE, 0xFFFFF254, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BD1B)
    Sleep(300)

    def lambda_BD38():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BD38)
    WaitChrThread(0xFE, 1)

    def lambda_BD4D():
        OP_97(0xFE, 0xFFFFFC18, 0x0, 0x3E8, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BD4D)
    WaitChrThread(0xFE, 1)
    SetScenarioFlags(0x0, 0)

    def lambda_BD6E():
        OP_97(0xFE, 0x0, 0x0, 0x4650, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BD6E)
    WaitChrThread(0xFE, 1)

    def lambda_BD8C():

        label("loc_BD8C")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_BD8C")

    QueueWorkItem2(0xFE, 2, lambda_BD8C)
    Return()

    # Function_65_BD16 end

    def Function_66_BD9A(): pass

    label("Function_66_BD9A")


    def lambda_BD9F():
        OP_97(0xFE, 0xFFFFF448, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BD9F)
    Sleep(300)

    def lambda_BDBC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BDBC)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_AD(0x0)
    Sleep(100)

    def lambda_BDDE():
        OP_97(0xFE, 0x0, 0x0, 0x4268, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BDDE)
    WaitChrThread(0xFE, 1)

    def lambda_BDFC():

        label("loc_BDFC")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_BDFC")

    QueueWorkItem2(0xFE, 2, lambda_BDFC)
    Return()

    # Function_66_BD9A end

    def Function_67_BE0A(): pass

    label("Function_67_BE0A")


    def lambda_BE0F():
        OP_97(0xFE, 0xFFFFEDA4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BE0F)
    Sleep(400)

    def lambda_BE2C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BE2C)
    WaitChrThread(0xFE, 1)

    def lambda_BE41():
        OP_97(0xFE, 0xFFFFFC18, 0x0, 0x3E8, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BE41)
    WaitChrThread(0xFE, 1)
    SetScenarioFlags(0x0, 1)

    def lambda_BE62():
        OP_97(0xFE, 0x0, 0x0, 0x3F48, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BE62)
    WaitChrThread(0xFE, 1)

    def lambda_BE80():

        label("loc_BE80")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_BE80")

    QueueWorkItem2(0xFE, 2, lambda_BE80)
    Return()

    # Function_67_BE0A end

    def Function_68_BE8E(): pass

    label("Function_68_BE8E")


    def lambda_BE93():
        OP_97(0xFE, 0xFFFFEF98, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BE93)
    Sleep(400)

    def lambda_BEB0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BEB0)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_AD(0x1)
    Sleep(100)

    def lambda_BED2():
        OP_97(0xFE, 0x0, 0x0, 0x3B60, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BED2)
    WaitChrThread(0xFE, 1)

    def lambda_BEF0():

        label("loc_BEF0")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_BEF0")

    QueueWorkItem2(0xFE, 2, lambda_BEF0)
    Return()

    # Function_68_BE8E end

    def Function_69_BEFE(): pass

    label("Function_69_BEFE")


    def lambda_BF03():
        OP_97(0xFE, 0xFFFFE8F4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BF03)
    Sleep(500)

    def lambda_BF20():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BF20)
    WaitChrThread(0xFE, 1)

    def lambda_BF35():
        OP_97(0xFE, 0xFFFFFC18, 0x0, 0x3E8, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BF35)
    WaitChrThread(0xFE, 1)
    SetScenarioFlags(0x0, 2)

    def lambda_BF56():
        OP_97(0xFE, 0x0, 0x0, 0x3B60, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BF56)
    WaitChrThread(0xFE, 1)

    def lambda_BF74():

        label("loc_BF74")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_BF74")

    QueueWorkItem2(0xFE, 2, lambda_BF74)
    Return()

    # Function_69_BEFE end

    def Function_70_BF82(): pass

    label("Function_70_BF82")


    def lambda_BF87():
        OP_97(0xFE, 0xFFFFEAE8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BF87)
    Sleep(500)

    def lambda_BFA4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BFA4)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_AD(0x2)
    Sleep(100)

    def lambda_BFC6():
        OP_97(0xFE, 0x0, 0x0, 0x3778, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BFC6)
    WaitChrThread(0xFE, 1)

    def lambda_BFE4():

        label("loc_BFE4")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_BFE4")

    QueueWorkItem2(0xFE, 2, lambda_BFE4)
    Return()

    # Function_70_BF82 end

    def Function_71_BFF2(): pass

    label("Function_71_BFF2")


    def lambda_BFF7():
        OP_95(0xFE, 111000, 0, -110500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BFF7)
    WaitChrThread(0xFE, 1)

    def lambda_C015():
        OP_95(0xFE, 113000, 0, -110500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C015)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_71_BFF2 end

    def Function_72_C02F(): pass

    label("Function_72_C02F")


    def lambda_C034():
        OP_95(0xFE, 109000, 0, -130500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C034)
    WaitChrThread(0xFE, 1)

    def lambda_C052():
        OP_95(0xFE, 100000, 0, -130500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C052)
    Sleep(3200)

    def lambda_C06F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C06F)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_72_C02F end

    def Function_73_C080(): pass

    label("Function_73_C080")


    def lambda_C085():
        OP_95(0xFE, 109000, -600, -130500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C085)
    WaitChrThread(0xFE, 1)

    def lambda_C0A3():
        OP_95(0xFE, 103000, -600, -130500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C0A3)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_73_C080 end

    def Function_74_C0BD(): pass

    label("Function_74_C0BD")


    def lambda_C0C2():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFC43C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C0C2)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_AD(0x0)

    def lambda_C0EA():
        OP_97(0xFE, 0xFFFFDCD8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C0EA)
    Sleep(2700)

    def lambda_C107():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C107)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_74_C0BD end

    def Function_75_C118(): pass

    label("Function_75_C118")


    def lambda_C11D():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFC43C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C11D)
    WaitChrThread(0xFE, 1)

    def lambda_C13B():
        OP_97(0xFE, 0xFFFFF8F8, 0x0, 0xFFFFF8F8, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C13B)
    WaitChrThread(0xFE, 1)
    SetScenarioFlags(0x0, 0)

    def lambda_C15C():
        OP_97(0xFE, 0xFFFFDCD8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C15C)
    Sleep(2700)

    def lambda_C179():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C179)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_75_C118 end

    def Function_76_C18A(): pass

    label("Function_76_C18A")


    def lambda_C18F():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C18F)
    WaitChrThread(0xFE, 1)
    Sleep(700)

    def lambda_C1B0():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFFA88, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C1B0)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_AD(0x1)

    def lambda_C1D8():
        OP_97(0xFE, 0xFFFFDCD8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C1D8)
    Sleep(2800)

    def lambda_C1F5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C1F5)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_76_C18A end

    def Function_77_C206(): pass

    label("Function_77_C206")


    def lambda_C20B():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFBFF0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C20B)
    WaitChrThread(0xFE, 1)

    def lambda_C229():
        OP_97(0xFE, 0xFFFFF8F8, 0x0, 0xFFFFF8F8, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C229)
    WaitChrThread(0xFE, 1)
    SetScenarioFlags(0x0, 1)

    def lambda_C24A():
        OP_97(0xFE, 0xFFFFDCD8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C24A)
    Sleep(2800)

    def lambda_C267():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C267)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_77_C206 end

    def Function_78_C278(): pass

    label("Function_78_C278")


    def lambda_C27D():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFC694, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C27D)
    WaitChrThread(0xFE, 1)
    Sleep(1100)

    def lambda_C29E():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF510, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C29E)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_AD(0x2)

    def lambda_C2C6():
        OP_97(0xFE, 0xFFFFDCD8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C2C6)
    Sleep(2900)

    def lambda_C2E3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C2E3)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_78_C278 end

    def Function_79_C2F4(): pass

    label("Function_79_C2F4")


    def lambda_C2F9():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFBBA4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C2F9)
    WaitChrThread(0xFE, 1)
    Sleep(500)

    def lambda_C31A():
        OP_97(0xFE, 0xFFFFF8F8, 0x0, 0xFFFFF8F8, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C31A)
    WaitChrThread(0xFE, 1)
    SetScenarioFlags(0x0, 2)

    def lambda_C33B():
        OP_97(0xFE, 0xFFFFDCD8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C33B)
    Sleep(2900)

    def lambda_C358():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C358)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_79_C2F4 end

    def Function_80_C369(): pass

    label("Function_80_C369")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00900.itc", 0x28)
    SetChrPos(0x101, -3000, 0, -127400, 0)
    SetChrPos(0x102, -1700, 0, -126900, 0)
    SetChrPos(0x103, -4100, 0, -126900, 0)
    SetChrPos(0x104, -5400, 0, -127400, 0)
    SetChrPos(0x109, -2500, 0, -128300, 0)
    SetChrPos(0x105, -4500, 0, -128300, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x2E, 0x28)
    SetChrSubChip(0x2E, 0x0)
    ClearChrFlags(0x2E, 0x80)
    SetChrFlags(0x2E, 0x8000)
    SetChrPos(0x2E, 0, 0, -127700, 0)
    SetChrChipByIndex(0x2F, 0xB)
    SetChrSubChip(0x2F, 0x0)
    ClearChrFlags(0x2F, 0x80)
    SetChrFlags(0x2F, 0x8000)
    SetChrPos(0x2F, 5650, -5850, -106000, 270)
    SetChrChipByIndex(0x2C, 0xD)
    SetChrSubChip(0x2C, 0x0)
    ClearChrFlags(0x2C, 0x80)
    SetChrFlags(0x2C, 0x8000)
    SetChrPos(0x2C, 5650, -5850, -108800, 270)
    SetChrChipByIndex(0x13, 0xC)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 5650, -5850, -111700, 270)
    SetChrChipByIndex(0x2D, 0xE)
    SetChrSubChip(0x2D, 0x0)
    ClearChrFlags(0x2D, 0x80)
    SetChrFlags(0x2D, 0x8000)
    SetChrPos(0x2D, 1800, -5850, -102100, 180)
    SetChrChipByIndex(0x36, 0xF)
    SetChrSubChip(0x36, 0x0)
    ClearChrFlags(0x36, 0x80)
    SetChrFlags(0x36, 0x8000)
    SetChrPos(0x36, 11800, -5850, -104800, 270)
    SetChrChipByIndex(0x34, 0x7)
    SetChrSubChip(0x34, 0x0)
    ClearChrFlags(0x34, 0x80)
    SetChrFlags(0x34, 0x8000)
    SetChrPos(0x34, 5000, -5800, -99450, 180)
    SetMapObjFrame(0xFF, "bs", 0x1, 0x1)
    OP_68(-3000, 300, -126900, 0)
    MoveCamera(47, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    VolumeBGM(0x46, 0x3E8)
    OP_68(-3000, 1300, -126900, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x109,
        "#12P#10101FIt started...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00003F...Yeah.\x02\x03",
            "#00000FI heard Mr. Arios was\x01",
            "coming, but to think\x01",
            "Lawyer Ian's here too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202F#5PFurthermore, it seems he is known\x01",
            "by the name "Mr. Beardy-Bear".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FAt international conferences,\x01",
            "various agreements are made.\x02\x03",
            "#00100FWhen that happens, it's necessary to judge\x01",
            "whether such agreements are valid based on\x01",
            "existing international law and common law.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00005FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FSo that Mr. Beardy-Bear is\x01",
            "here to advise on that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FIt's great that the conference has\x01",
            "started... But it looks like they're\x01",
            "discussin' some difficult things.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x2E, 0x10E, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x2E,
        (
            "#00603F#11PWell, it's not our place to be concerned with\x01",
            "the details of the conference discussions.\x02\x03",
            "#00600FWill this conference end without issue?\x01",
            "Focus only on making sure it does.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-1500, 1300, -127550, 1500)

    def lambda_C89B():
        TurnDirection(0x101, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_C89B)
    Sleep(50)

    def lambda_C8AB():
        TurnDirection(0x102, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_C8AB)
    Sleep(50)

    def lambda_C8BB():
        TurnDirection(0x109, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_C8BB)
    Sleep(50)

    def lambda_C8CB():
        TurnDirection(0x103, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_C8CB)
    Sleep(50)

    def lambda_C8DB():
        TurnDirection(0x105, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_C8DB)
    Sleep(50)

    def lambda_C8EB():
        TurnDirection(0x104, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_C8EB)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00001F#6PYes, understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00101FThen, do we do\x01",
            "as planned?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2E,
        (
            "#00604F#11PYes. You all will\x01",
            "patrol 34F, 35F and\x01",
            "36F for me.\x02\x03",
            "#00602FFor now, given your social standing,\x01",
            "you're to speak only with staff.\x02\x03",
            "You should speak with the\x01",
            "news media and the staffs of\x01",
            "the heads of state as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10100FUnderstood!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2E,
        (
            "#00603F#11PI'm heading back to 34F, then.\x02\x03",
            "#00600F...May Aidios protect you.\x01",
            "Call me if anything happens.\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x2E, 0xDAC, 0xFFFE0430, 0x1F4)
    OP_68(9000, 1300, -130000, 4000)

    def lambda_CAE8():
        OP_95(0xFE, 5500, 0, -130000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_CAE8)
    WaitChrThread(0x2E, 1)

    def lambda_CB06():
        OP_95(0xFE, 11500, 0, -130000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_CB06)
    Sleep(2000)

    def lambda_CB23():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_CB23)
    WaitChrThread(0x2E, 1)
    SetChrFlags(0x2E, 0x80)
    OP_6F(0x79)
    Fade(500)
    OP_68(-3000, 1300, -126900, 0)
    MoveCamera(47, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00008F#5P...It seems Mr. Dudley also\x01",
            "thinks something will happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#00103FYes...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211F#5PWith so many suspicious actions lately,\x01",
            "it would be strange if nothing happened.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(150)

    ChrTalk(
        0x109,
        (
            "#12P#10101FLooks like we'll need to be\x01",
            "extra careful on our patrols.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_CC86():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_CC86)
    Sleep(50)

    def lambda_CC96():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_CC96)
    Sleep(50)

    def lambda_CCA6():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_CCA6)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x103, 0)

    ChrTalk(
        0x104,
        "#6P#00304FRight.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10300FShall we start our patrol, then?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#5P#00001FYeah. Let's speak with the various\x01",
            "staff members during our rounds.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x28)
    SetChrPos(0x0, -3000, 0, -128000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 8690, 0, -132450, 270)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -9280, 0, -132230, 90)
    SetScenarioFlags(0x142, 0)
    OP_29(0xA4, 0x1, 0x1)
    OP_32(0xFF, 0xFE, 0x0)
    Sleep(500)
    EventEnd(0x5)
    SetChrFlags(0x2F, 0x8000)
    SetChrFlags(0x2C, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x2D, 0x8000)
    SetChrFlags(0x36, 0x8000)
    SetChrFlags(0x34, 0x8000)
    Return()

    # Function_80_C369 end

    def Function_81_CDF0(): pass

    label("Function_81_CDF0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(73000, 1200, -1000, 0)
    MoveCamera(50, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 74500, 0, -1000, 270)
    SetChrPos(0x102, 73800, 0, 200, 225)
    SetChrPos(0x103, 73800, 0, -2200, 315)
    SetChrPos(0x104, 72200, 0, 200, 135)
    SetChrPos(0x109, 71500, 0, -1000, 90)
    SetChrPos(0x105, 72200, 0, -2200, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#11P#00000FAlright... \x01",
            "This completes our patrol.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FIt seems there's nothing\x01",
            "particularly wrong at present.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00302FWe should make\x01",
            "another loop around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FTrue...\x02\x03",
            "#00108FI wonder how the\x01",
            "conference is going?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00006FYeah... I'm sure the Mayor and the\x01",
            "Chairman are doing their best, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00201FThe problem is the "Blood and Iron\x01",
            "Chancellor" and President Rocksmith, yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FWell, maybe we should ask someone\x01",
            "about it during the break.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 2)
    NewScene("c1540", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_81_CDF0 end

    def Function_82_D0CB(): pass

    label("Function_82_D0CB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-55500, 1200, -1500, 0)
    MoveCamera(50, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, -54000, 0, -1500, 270)
    SetChrPos(0x102, -54700, 0, -300, 225)
    SetChrPos(0x103, -54700, 0, -2700, 315)
    SetChrPos(0x104, -56300, 0, -300, 135)
    SetChrPos(0x109, -57000, 0, -1500, 90)
    SetChrPos(0x105, -56300, 0, -2700, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#11P#00000FAlright... \x01",
            "This completes our patrol.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FIt seems there's nothing\x01",
            "particularly wrong at present.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00302FWe should make\x01",
            "another loop around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FTrue...\x02\x03",
            "#00108FI wonder how the\x01",
            "conference is going?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00006FYeah... I'm sure the Mayor and the\x01",
            "Chairman are doing their best, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00201FThe problem is the "Blood and Iron\x01",
            "Chancellor" and President Rocksmith, yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FWell, maybe we should ask someone\x01",
            "about it during the break.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 2)
    NewScene("c1540", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_82_D0CB end

    def Function_83_D3A6(): pass

    label("Function_83_D3A6")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x15, 0xFF)
    OP_68(-1790, 1200, 27440, 0)
    MoveCamera(40, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)
    SetChrFlags(0x29, 0x80)
    SetChrPos(0x101, -1500, 0, 26400, 270)
    SetChrPos(0x102, -1200, 0, 27700, 270)
    SetChrPos(0x103, 100, 0, 26800, 270)
    SetChrPos(0x104, 400, 0, 28100, 270)
    SetChrPos(0x109, -1500, 0, 25100, 315)
    SetChrPos(0x105, 100, 0, 25500, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetBarrier(0x2, 0x0, 0x1)
    OP_0D()

    ChrTalk(
        0x15,
        "#5P──We've been waiting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#5PYou're the people of Crossbell Police's\x01",
            "Special Support Section, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00001F...Yes. And this is\x01",
            "the President's room?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#5PYes. I've been told\x01",
            "to let you through.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x15, 0x0, 0x1F4)

    def lambda_D54B():
        OP_95(0xFE, -3200, 0, 28500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_D54B)
    WaitChrThread(0x15, 1)
    OP_93(0x15, 0xB4, 0x1F4)

    ChrTalk(
        0x15,
        "#5PPlease, enter.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00003FWell then...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00100FExcuse us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10108F(He's the leader of Calvard, one of\x01",
            "the continent's largest countries...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#00306F(Now I'm just a \x01",
            "tiny bit nervous...)\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 84)
    Sleep(700)
    Sound(103, 0, 100, 0)
    BeginChrThread(0x102, 3, 0, 84)
    Sleep(300)
    FadeToDark(1000, 0, -1)
    BeginChrThread(0x103, 3, 0, 84)
    Sleep(600)
    BeginChrThread(0x104, 3, 0, 84)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetScenarioFlags(0x22, 0)
    NewScene("e4020", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_83_D3A6 end

    def Function_84_D6C5(): pass

    label("Function_84_D6C5")


    def lambda_D6CA():
        OP_95(0xFE, -3200, 0, 27000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D6CA)
    WaitChrThread(0xFE, 1)

    def lambda_D6E8():
        OP_95(0xFE, -5500, 0, 27000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D6E8)
    Sleep(600)

    def lambda_D705():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D705)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_84_D6C5 end

    def Function_85_D716(): pass

    label("Function_85_D716")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-2350, 1200, 27000, 0)
    MoveCamera(40, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17200, 0)
    SetChrPos(0x101, -5500, 0, 27000, 90)
    SetChrPos(0x102, -5500, 0, 27000, 90)
    SetChrPos(0x103, -5500, 0, 27000, 90)
    SetChrPos(0x104, -5500, 0, 27000, 90)
    SetChrPos(0x109, -5500, 0, 27000, 90)
    SetChrPos(0x105, -5500, 0, 27000, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x35, -800, 0, 26600, 0)
    SetChrFlags(0x29, 0x80)
    OP_4B(0x15, 0xFF)
    SetChrPos(0x15, -3200, 0, 28500, 180)
    SetBarrier(0x2, 0x0, 0x1)
    Sound(103, 0, 100, 0)
    FadeToBright(1000, 0)
    BeginChrThread(0x104, 3, 0, 89)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 91)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 88)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 90)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 87)
    Sleep(700)
    BeginChrThread(0x101, 3, 0, 86)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x15,
        "#5P──Thank you for your hard work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#5PI think Chancellor Osborne's\x01",
            "room is on the opposite side.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D8F3():

        label("loc_D8F3")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_D8F3")

    QueueWorkItem2(0x101, 2, lambda_D8F3)

    def lambda_D905():

        label("loc_D905")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_D905")

    QueueWorkItem2(0x102, 2, lambda_D905)
    Sleep(50)

    def lambda_D91A():

        label("loc_D91A")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_D91A")

    QueueWorkItem2(0x103, 2, lambda_D91A)
    Sleep(50)

    def lambda_D92F():

        label("loc_D92F")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_D92F")

    QueueWorkItem2(0x109, 2, lambda_D92F)
    Sleep(50)

    def lambda_D944():

        label("loc_D944")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_D944")

    QueueWorkItem2(0x105, 2, lambda_D944)
    Sleep(50)

    def lambda_D959():

        label("loc_D959")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_D959")

    QueueWorkItem2(0x104, 2, lambda_D959)

    ChrTalk(
        0x101,
        "#11P#00011F...Ah, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00103FThank you for helping us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#5PDon't mention it. Well then.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 84)
    Sleep(1500)
    OP_68(-800, 1200, 26600, 2000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    Sound(104, 0, 100, 0)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)
    OP_6F(0x79)
    WaitChrThread(0x15, 3)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)

    def lambda_DA9B():
        TurnDirection(0x105, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_DA9B)
    Sleep(50)

    def lambda_DAAB():
        TurnDirection(0x109, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_DAAB)
    Sleep(50)

    def lambda_DABB():
        TurnDirection(0x104, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_DABB)
    Sleep(50)

    def lambda_DACB():
        TurnDirection(0x102, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_DACB)
    Sleep(50)

    def lambda_DADB():
        TurnDirection(0x101, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_DADB)
    Sleep(50)

    def lambda_DAEB():
        TurnDirection(0x103, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_DAEB)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)

    ChrTalk(
        0x105,
        (
            "#10309F#11PHa ha, he has a great attitude. It's just what\x01",
            "you'd expect from the leader of a large country.\x02\x03",
            "#10302FHe's quite the sly fox, isn't he?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106FWazy... I think you're\x01",
            "overstating it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#11PBut he was rather blunt.\x02\x03",
            "#00211FI don't think he was trying\x01",
            "to pressure us, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#5PHe was probably just trying\x01",
            "to put on a good show.\x02\x03",
            "#00103FThe Republic's President, putting on a\x01",
            "show where he decorates we who contributed\x01",
            "to the Cult incident's resolution...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FCrossbell's incidents\x01",
            "are their incidents..\x02\x03",
            "#00001FThat restates the Republic's dominion\x01",
            "over Crossbell as a subject state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#5PMan... I wonder if that's the real\x01",
            "reason he wanted to meet with us.\x02\x03",
            "#00301FThe leader of a large country... \x01",
            "They really are amazin' people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#11PYeah. The difference from the autonomous\x01",
            "state congressmen is night and day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10108F...I wonder what the Chancellor\x01",
            "wants to speak with us about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001F...No idea. Anyway, \x01",
            "let's prepare ourselves.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4C(0x15, 0xFF)
    SetChrPos(0x0, -1500, 0, 27000, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x142, 3)
    OP_29(0xA4, 0x1, 0x3)
    ModifyEventFlags(1, 0, 0x80)
    OP_1B(0x15, 0xFF, 0xFFFF)
    ClearChrFlags(0x29, 0x80)
    EventEnd(0x5)
    Return()

    # Function_85_D716 end

    def Function_86_DF61(): pass

    label("Function_86_DF61")


    def lambda_DF66():
        OP_95(0xFE, -3200, 0, 27000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DF66)

    def lambda_DF80():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DF80)
    WaitChrThread(0xFE, 1)

    def lambda_DF95():
        OP_95(0xFE, -1500, 0, 26400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DF95)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_86_DF61 end

    def Function_87_DFB6(): pass

    label("Function_87_DFB6")


    def lambda_DFBB():
        OP_95(0xFE, -3200, 0, 27000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DFBB)

    def lambda_DFD5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DFD5)
    WaitChrThread(0xFE, 1)

    def lambda_DFEA():
        OP_95(0xFE, -1200, 0, 27700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DFEA)
    WaitChrThread(0xFE, 1)

    def lambda_E008():

        label("loc_E008")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_E008")

    QueueWorkItem2(0xFE, 2, lambda_E008)
    Return()

    # Function_87_DFB6 end

    def Function_88_E016(): pass

    label("Function_88_E016")


    def lambda_E01B():
        OP_95(0xFE, -3200, 0, 27000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E01B)

    def lambda_E035():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E035)
    WaitChrThread(0xFE, 1)

    def lambda_E04A():
        OP_95(0xFE, 100, 0, 26800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E04A)
    WaitChrThread(0xFE, 1)

    def lambda_E068():

        label("loc_E068")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_E068")

    QueueWorkItem2(0xFE, 2, lambda_E068)
    Return()

    # Function_88_E016 end

    def Function_89_E076(): pass

    label("Function_89_E076")


    def lambda_E07B():
        OP_95(0xFE, -3200, 0, 27000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E07B)

    def lambda_E095():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E095)
    WaitChrThread(0xFE, 1)

    def lambda_E0AA():
        OP_95(0xFE, 400, 0, 28100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E0AA)
    WaitChrThread(0xFE, 1)

    def lambda_E0C8():

        label("loc_E0C8")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_E0C8")

    QueueWorkItem2(0xFE, 2, lambda_E0C8)
    Return()

    # Function_89_E076 end

    def Function_90_E0D6(): pass

    label("Function_90_E0D6")


    def lambda_E0DB():
        OP_95(0xFE, -3200, 0, 27000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E0DB)

    def lambda_E0F5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E0F5)
    WaitChrThread(0xFE, 1)

    def lambda_E10A():
        OP_95(0xFE, -1500, 0, 25100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E10A)
    WaitChrThread(0xFE, 1)

    def lambda_E128():

        label("loc_E128")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_E128")

    QueueWorkItem2(0xFE, 2, lambda_E128)
    Return()

    # Function_90_E0D6 end

    def Function_91_E136(): pass

    label("Function_91_E136")


    def lambda_E13B():
        OP_95(0xFE, -3200, 0, 27000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E13B)

    def lambda_E155():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E155)
    WaitChrThread(0xFE, 1)

    def lambda_E16A():
        OP_95(0xFE, 100, 0, 25500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E16A)
    WaitChrThread(0xFE, 1)

    def lambda_E188():

        label("loc_E188")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_E188")

    QueueWorkItem2(0xFE, 2, lambda_E188)
    Return()

    # Function_91_E136 end

    def Function_92_E196(): pass

    label("Function_92_E196")

    EventBegin(0x0)

    def lambda_E19D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_E19D)
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(111800, 1100, -102500, 2000)
    MoveCamera(45, 15, 0, 2000)
    SetCameraDistance(19500, 2000)
    OP_6F(0x79)
    SetChrName("Lloyd")

    AnonymousTalk(
        0xFF,
        (
            "#00001F(So that's the Chancellor's room, huh...)\x02\x03",
            "#00003F(Break time will probably be over\x01",
            "once we finish visiting with him.)\x02\x03",
            "#00008F(Is there anything else we need to do?)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 109000, 0, -122500, 0)
    SetScenarioFlags(0x142, 4)
    ModifyEventFlags(0, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_92_E196 end

    def Function_93_E2C9(): pass

    label("Function_93_E2C9")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x16, 0xFF)
    OP_68(110500, 1100, -102500, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, 109100, 0, -103400, 90)
    SetChrPos(0x102, 108800, 0, -102500, 90)
    SetChrPos(0x103, 107600, 0, -103100, 90)
    SetChrPos(0x104, 107300, 0, -102200, 90)
    SetChrPos(0x109, 109000, 0, -100900, 135)
    SetChrPos(0x105, 108000, 0, -100300, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    ChrTalk(
        0x16,
        "#11PCrossbell Police, Special Support Section, right?\x02",
    )

    CloseMessageWindow()
    OP_93(0x16, 0x0, 0x1F4)

    def lambda_E3C4():
        OP_95(0xFE, 111300, 0, -101000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_E3C4)
    WaitChrThread(0x16, 1)
    OP_93(0x16, 0xE1, 0x1F4)

    ChrTalk(
        0x16,
        (
            "#5PHis Excellency the Chancellor\x01",
            "is waiting. Enter inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00001FA-Alright.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00104FExcuse us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00211F(...He seems kind of arrogant.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F(That's an Imperial soldier for you.\x01",
            "Pointlessly overbearing.)\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 94)
    Sleep(700)
    Sound(103, 0, 100, 0)
    OP_71(0x2, 0x0, 0x5, 0x0, 0x0)
    BeginChrThread(0x102, 3, 0, 94)
    Sleep(300)
    FadeToDark(1000, 0, -1)
    BeginChrThread(0x103, 3, 0, 94)
    Sleep(600)
    BeginChrThread(0x104, 3, 0, 94)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    StopBGM(0xFA0)
    LoadChrToIndex("chr/ch00002.itc", 0x28)
    LoadChrToIndex("chr/ch00102.itc", 0x29)
    LoadChrToIndex("chr/ch00202.itc", 0x2A)
    LoadChrToIndex("chr/ch00302.itc", 0x2B)
    LoadChrToIndex("chr/ch02902.itc", 0x2C)
    LoadChrToIndex("chr/ch03002.itc", 0x2D)
    LoadChrToIndex("chr/ch10900.itc", 0x2E)
    LoadChrToIndex("chr/ch10902.itc", 0x2F)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07400.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis416.itp")
    OP_68(148000, 1100, 106000, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    SetChrPos(0x101, 146500, 0, 106000, 90)
    SetChrPos(0x102, 146500, 0, 106000, 90)
    SetChrPos(0x103, 146500, 0, 106000, 90)
    SetChrPos(0x104, 146500, 0, 106000, 90)
    SetChrPos(0x109, 146500, 0, 106000, 90)
    SetChrPos(0x105, 146500, 0, 106000, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x2F, 0x2E)
    SetChrSubChip(0x2F, 0x0)
    ClearChrFlags(0x2F, 0x80)
    SetChrFlags(0x2F, 0x8000)
    SetChrPos(0x2F, 160900, 0, 110700, 0)
    OP_52(0x2F, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2F, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2F, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(153000, 1100, 106000, 5000)
    SetCameraDistance(17500, 5000)
    FadeToBright(1000, 0)
    BeginChrThread(0x101, 3, 0, 95)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 96)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 97)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 98)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 99)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 100)
    WaitChrThread(0x105, 3)
    Sound(104, 0, 100, 0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#6P#00003F#6P──Excuse us,\x01",
            "Chancellor Osborne.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F#6PThank you for inviting the police,\x01",
            "Special Support Section.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x2F,
        "#07404F#11P#N...Do come in.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7583", 0)
    OP_68(159600, 1000, 110400, 2000)
    MoveCamera(43, 17, 0, 2000)
    OP_6F(0x79)
    SetCameraDistance(17000, 40000)
    SetChrPos(0x101, 150500, 0, 107200, 90)
    SetChrPos(0x102, 150400, 0, 108200, 90)
    SetChrPos(0x103, 148900, 0, 107200, 90)
    SetChrPos(0x104, 148800, 0, 108200, 90)
    SetChrPos(0x109, 150000, 0, 106600, 90)
    SetChrPos(0x105, 148800, 0, 106600, 90)

    def lambda_E869():
        OP_96(0xFE, 0x2673C, 0x0, 0x1AA90, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E869)
    Sleep(300)

    def lambda_E886():
        OP_96(0xFE, 0x266D8, 0x0, 0x1AE78, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E886)
    Sleep(50)

    def lambda_E8A3():
        OP_96(0xFE, 0x260FC, 0x0, 0x1AA90, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_E8A3)
    Sleep(100)

    def lambda_E8C0():
        OP_96(0xFE, 0x26098, 0x0, 0x1AE78, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_E8C0)
    Sleep(100)

    def lambda_E8DD():
        OP_96(0xFE, 0x26548, 0x0, 0x1A450, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_E8DD)
    Sleep(100)

    def lambda_E8FA():
        OP_96(0xFE, 0x26098, 0x0, 0x1A450, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_E8FA)
    WaitChrThread(0x109, 1)

    def lambda_E918():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_E918)
    WaitChrThread(0x105, 1)

    def lambda_E929():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_E929)
    Sleep(500)

    ChrTalk(
        0x2F,
        (
            "#07400F#11P──It's truly a magnificent view.\x02\x03",
            "To think humans could build this\x01",
            "structure to look down at the\x01",
            "ground from such a height...\x02\x03",
            "#07404FHu hu, it's proof that we've finally reached\x01",
            "the glory that ancient civilization once had.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000F...Indeed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200FYou are talking about the ancient\x01",
            "Zemurian civilization of 1200 years ago?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F#6PYeah. They say their civilization was\x01",
            "almost magical in its convenience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2F,
        (
            "#07400F#11PIt wasn't necessarily a simple utopia.\x01\x02\x03",
            "#07404FLast year, the giant city that floated \x01",
            "above Liberl during that phenomenon...\x02\x03",
            "That too was constructed in the ancient Zemurian\x01",
            "period, and it was sealed away by human hands...\x02\x03",
            "#07401FAs the symbol of both the foolishness\x01",
            "and the possibilities of mankind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00001FFoolishness and possibilities, you say...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#6PBut... You sure know\x01",
            "a lot about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2F,
        (
            "#07404F#11PHu hu, not that much.\x02\x03",
            "#07400FIn relation to Crossbell, \x01",
            "I failed to learn the truth that\x01",
            "Joachim was a Cult's high priest.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x32, 0x0, 0xBB8, 0xC8)

    ChrTalk(
        0x101,
        "#6P#00013F...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00208FYou know even that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2F,
        (
            "#07404F#11PHu hu, it's precisely because\x01",
            "of the unknown that this\x01",
            "world is so interesting.\x02\x03",
            "If we had everything in the palm of our\x01",
            "hand, it would be the height of boredom.\x02\x03",
            "#07400FDon't you agree,\x01",
            "Wazy Hemisphere?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#N#10306F...Hmph. So you know\x01",
            "my name as well.\x02\x03",
            "#10300FWell, perhaps you know\x01",
            "more than just my name.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x2F,
        (
            "#07400F#11PNo, nothing of special interest.\x01\x02\x03",
            "#07404FThe successor of the "War God",\x01",
            "instead, intrigues me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#6P...You...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FThe "Imperial Army Intelligence Division"...\x02\x03",
            "#00001FIt seems it has impressive\x01",
            "intelligence gathering capabilities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2F,
        "#07404F#11PHu hu...\x02",
    )

    CloseMessageWindow()
    OP_93(0x2F, 0x10E, 0x1F4)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x2F,
        (
            "I am Giliath Osborne,\x01",
            "representative of the\x01",
            "Erebonian Imperial government.\x02\x03",
            "I have heard all about\x01",
            "you from Lechter.\x02\x03",
            "Won't you join me for a chat\x01",
            "during the remainder of our break?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    SetCameraDistance(16500, 1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrChipByIndex(0x101, 0x28)
    SetChrSubChip(0x101, 0x2)
    SetChrChipByIndex(0x102, 0x29)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x2A)
    SetChrSubChip(0x103, 0x2)
    SetChrChipByIndex(0x104, 0x2B)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x2C)
    SetChrSubChip(0x109, 0x2)
    SetChrChipByIndex(0x105, 0x2D)
    SetChrSubChip(0x105, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x2F, 0x2F)
    SetChrSubChip(0x2F, 0x0)
    SetChrPos(0x102, 157600, 50, 107600, 160)
    SetChrPos(0x104, 156200, 50, 107600, 160)
    SetChrPos(0x101, 158600, 50, 104000, 0)
    SetChrPos(0x103, 157650, 50, 104000, 0)
    SetChrPos(0x109, 156700, 50, 104000, 0)
    SetChrPos(0x105, 155750, 50, 104000, 0)
    SetChrPos(0x2F, 159900, 50, 105900, 270)
    ClearChrFlags(0x37, 0x80)
    OP_78(0xF, 0x37)
    ClearChrFlags(0x38, 0x80)
    OP_78(0x10, 0x38)
    OP_49()
    SetChrPos(0x37, 157500, 0, 107700, 0)
    OP_D5(0x37, 0x0, 0x53020, 0x0, 0x0)
    SetChrPos(0x38, 156100, 0, 107700, 0)
    OP_D5(0x38, 0x0, 0x53020, 0x0, 0x0)
    OP_68(158600, 2600, 106100, 0)
    MoveCamera(59, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    OP_68(158600, 800, 106100, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#12P#00003F...So then, Chancellor.\x02\x03",
            "#00001FWhat exactly would you\x01",
            "like to discuss with us...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00211FIt seems you are already aware\x01",
            "of the current situation.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)

    ChrTalk(
        0x2F,
        (
            "#07404F#11POh, this is just a simple chat.\x02\x03",
            "#07400FIf possible, I would like\x01",
            "your opinion on something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10105FOpinion...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2F,
        (
            "#07403F#11PYes. I'll ask you directly:\x02\x03",
            "#07402F...How long do you think\x01",
            "Crossbell can hold out?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7571", 0)
    SetCameraDistance(15500, 80000)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#12P#00013F#4S...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10306FQuite the blunt question...\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x2F, 0x1)
    Sleep(300)

    ChrTalk(
        0x2F,
        (
            "#07400F#5PHu hu, it's not out of malice.\x02\x03",
            "#07403FIt's just that there's one constant\x01",
            "throughout history── There are no\x01",
            "nations that haven't been destroyed.\x02\x03",
            "To say nothing of the orbal\x01",
            "revolution, which accelerated\x01",
            "everything in the current era...\x02\x03",
            "#07401FHow much longer do you think this\x01",
            "land can avoid that destiny?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#6P...T-That's...\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x32, 0x0, 0xBB8, 0x96)

    ChrTalk(
        0x109,
        (
            "#6P#10107F──F-Forever!\x02\x03",
            "As long as the citizens of this autonomous\x01",
            "state have the will to protect it!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(150)

    ChrTalk(
        0x101,
        "#11P#00005FNoｱl...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2F,
        (
            "#07400F#5PYes. Strong will is critical.\x02\x03",
            "In rare cases, trends\x01",
            "reverse and history\x01",
            "itself changes.\x02\x03",
            "#07404FThe people are not powerless.\x01",
            "I believe in their potential.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x109,
        "#6P#10100FT-Then...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2F,
        (
            "#07400F#5P──But, what happens\x01",
            "if those wills clash?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x32, 0x0, 0xBB8, 0x96)

    ChrTalk(
        0x109,
        "#6P#10111F......!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2F,
        (
            "#07401F#5PIt's simple── When a small\x01",
            "will is engulfed by a large\x01",
            "one, its flames intensify.\x02\x03",
            "#07404FAnd when the hellfire that is\x01",
            "born appears above ground...\x02\x03",
            "All justice and morality dissolves in the heat,\x01",
            "and the whole world is engulfed in its flames.\x02\x03",
            "#07402F──Such a scene is\x01",
            "easy to imagine, no?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00210F#40W...Ahhh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10110F#40W...Ugh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00311F#6P#30W............\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#12P#00003F#30WIndeed, our will might\x01",
            "be small compared to the\x01",
            "Empire or Republic...\x02\x03",
            "#00008FBut it's not definite that a smaller\x01",
            "flame will be engulfed by a bigger one.\x02\x03",
            "#00007F#20WJust like the Imperial invasion\x01",
            "Liberl once repelled...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F#6PAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10304FThe "Hundred Days War" 12 year ago, huh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2F,
        (
            "#07404F#5PHu hu, exactly. Will is a\x01",
            "question of "strength".\x02\x03",
            "Liberl's small yet strong will\x01",
            "overcame the large but\x01",
            "disorganized will of the Empire.\x02\x03",
            "Crossbell could learn\x01",
            "something from that example.\x02\x03",
            "#07402F──In the end, I don't know if the citizens\x01",
            "of Crossbell have the same pride and\x01",
            "strength as the Liberlians, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00013F...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#6P............\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x2F, 0x0)
    Sleep(300)

    ChrTalk(
        0x2F,
        (
            "#07404F#11PHu hu, break time's over.\x01",
            "Let's end our discussion here.\x02\x03",
            "#07400F──Oh yes, and I don't intend to give you any\x01",
            "special medals from the Imperial government.\x02\x03",
            "When awards are given to "commoners",\x01",
            "the nobles become quite noisy, you see.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(17000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_68(110500, 1100, -102500, 0)
    MoveCamera(48, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    SetChrPos(0x101, 113000, 0, -102500, 270)
    SetChrPos(0x102, 113000, 0, -102500, 270)
    SetChrPos(0x103, 113000, 0, -102500, 270)
    SetChrPos(0x104, 113000, 0, -102500, 270)
    SetChrPos(0x109, 113000, 0, -102500, 270)
    SetChrPos(0x105, 113000, 0, -102500, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x35, 108200, 0, -102800, 0)
    OP_70(0x2, 0x0)
    Sleep(2000)
    FadeToBright(1000, 0)
    Sound(103, 0, 100, 0)
    OP_71(0x2, 0x0, 0x5, 0x0, 0x0)
    BeginChrThread(0x105, 3, 0, 106)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 105)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 104)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 103)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 102)
    Sleep(700)
    BeginChrThread(0x101, 3, 0, 101)
    Sleep(1200)
    Sound(104, 0, 100, 0)
    OP_71(0x2, 0x5, 0x0, 0x0, 0x0)
    WaitChrThread(0x101, 3)
    StopBGM(0x1B58)

    ChrTalk(
        0x16,
        "#5PYou guys were lucky.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIt's rare to see His Excellency,\x01",
            "in such a good mood.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_100A6():

        label("loc_100A6")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_100A6")

    QueueWorkItem2(0x101, 2, lambda_100A6)

    def lambda_100B8():

        label("loc_100B8")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_100B8")

    QueueWorkItem2(0x102, 2, lambda_100B8)
    Sleep(50)

    def lambda_100CD():

        label("loc_100CD")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_100CD")

    QueueWorkItem2(0x103, 2, lambda_100CD)

    def lambda_100DF():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_100DF)
    Sleep(50)

    def lambda_100EF():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_100EF)

    def lambda_100FC():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_100FC)

    ChrTalk(
        0x101,
        "#12P#00005FHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00301FHey...is that some kind of joke?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHe must have taken\x01",
            "an interest in you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHis words may have been weighty,\x01",
            "but you should accept them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5P──Though I shouldn't be saying\x01",
            "such things in my position.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x16, 3, 0, 94)
    Sleep(800)
    Sound(103, 0, 100, 0)
    OP_71(0x2, 0x0, 0x5, 0x0, 0x0)
    Sleep(1000)
    Sound(104, 0, 100, 0)
    OP_71(0x2, 0x5, 0x0, 0x0, 0x0)
    OP_68(108800, 1100, -102180, 2000)
    MoveCamera(56, 25, 0, 2000)
    SetCameraDistance(16650, 2000)
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
    WaitChrThread(0x16, 3)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)

    def lambda_102EF():
        TurnDirection(0x102, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_102EF)
    Sleep(50)

    def lambda_102FF():
        TurnDirection(0x104, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_102FF)
    Sleep(50)

    def lambda_1030F():
        TurnDirection(0x101, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1030F)
    Sleep(50)

    def lambda_1031F():
        TurnDirection(0x109, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1031F)
    Sleep(50)

    def lambda_1032F():
        TurnDirection(0x105, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1032F)
    Sleep(50)

    def lambda_1033F():
        TurnDirection(0x103, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1033F)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x103, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7583", 0)

    ChrTalk(
        0x102,
        "#5P#00106F...How unreasonable.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00310FYeah, he's a real monster...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00006FHow to say it... I feel like he\x01",
            "has a different perspective.\x02\x03",
            "#00001F──Tio, are you okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00206FYes...somehow.\x02\x03",
            "#00208FThe images of flames he told\x01",
            "us about were too intense.\x01",
            "I am a little dizzy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#10106FI don't blame you...\x01",
            "Even I felt I somehow could see them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10308F#5PThe "Blood and Iron Chancellor"...\x01",
            "Truly a monster.\x02\x03",
            "#10303FIt seems he's thinking of\x01",
            "swallowing Crossbell in one gulp.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#11P#00003F──But he didn't call us\x01",
            "here to torment us.\x02\x03",
            "The President too... \x01",
            "I think their interest\x01",
            "in us is no lie.\x02\x03",
            "#00000FIn that case, maybe it's best to think\x01",
            "of it as a good learning experience.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_10657():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_10657)
    Sleep(0)

    def lambda_10667():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_10667)
    Sleep(0)

    def lambda_10677():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_10677)
    Sleep(0)

    def lambda_10687():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_10687)
    Sleep(0)

    def lambda_10697():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_10697)
    Sleep(0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x103, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x105,
        "#10302F#5PHu hu, I suppose.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00104F...I think that's the part of your\x01",
            "personality I can't imitate well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00309FYeah...\x01",
            "You're too positive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#10101FB-But... I can't help\x01",
            "feeling a bit depressed!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00202FThat is true... We have to make the\x01",
            "most of this lesson we have learned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00003FAnyway, break time's over.\x02\x03",
            "#00001FLet's head back to Mr. Dudley and\x01",
            "let him know the results of our interviews.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(18000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(2000)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x1C4, 4)
    SetScenarioFlags(0x22, 3)
    NewScene("c1540", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_93_E2C9 end

    def Function_94_10953(): pass

    label("Function_94_10953")


    def lambda_10958():
        OP_95(0xFE, 111300, 0, -102500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10958)
    WaitChrThread(0xFE, 1)

    def lambda_10976():
        OP_95(0xFE, 113000, 0, -102500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10976)
    Sleep(600)

    def lambda_10993():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10993)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_94_10953 end

    def Function_95_109A4(): pass

    label("Function_95_109A4")


    def lambda_109A9():
        OP_96(0xFE, 0x24540, 0x0, 0x19E10, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_109A9)

    def lambda_109C3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_109C3)
    WaitChrThread(0xFE, 1)

    def lambda_109D8():
        OP_95(0xFE, 151000, 0, 105200, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_109D8)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_95_109A4 end

    def Function_96_109F9(): pass

    label("Function_96_109F9")


    def lambda_109FE():
        OP_96(0xFE, 0x24540, 0x0, 0x19E10, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_109FE)

    def lambda_10A18():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10A18)
    WaitChrThread(0xFE, 1)

    def lambda_10A2D():
        OP_95(0xFE, 151000, 0, 106300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10A2D)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_96_109F9 end

    def Function_97_10A4E(): pass

    label("Function_97_10A4E")


    def lambda_10A53():
        OP_96(0xFE, 0x24540, 0x0, 0x19E10, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10A53)

    def lambda_10A6D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10A6D)
    WaitChrThread(0xFE, 1)

    def lambda_10A82():
        OP_95(0xFE, 150100, 0, 104600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10A82)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_97_10A4E end

    def Function_98_10AA3(): pass

    label("Function_98_10AA3")


    def lambda_10AA8():
        OP_96(0xFE, 0x24540, 0x0, 0x19E10, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10AA8)

    def lambda_10AC2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10AC2)
    WaitChrThread(0xFE, 1)

    def lambda_10AD7():
        OP_95(0xFE, 150100, 0, 106900, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10AD7)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_98_10AA3 end

    def Function_99_10AF8(): pass

    label("Function_99_10AF8")


    def lambda_10AFD():
        OP_96(0xFE, 0x24540, 0x0, 0x19E10, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10AFD)

    def lambda_10B17():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10B17)
    WaitChrThread(0xFE, 1)

    def lambda_10B2C():
        OP_95(0xFE, 149200, 0, 105200, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10B2C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_99_10AF8 end

    def Function_100_10B4D(): pass

    label("Function_100_10B4D")


    def lambda_10B52():
        OP_96(0xFE, 0x24540, 0x0, 0x19E10, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10B52)

    def lambda_10B6C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10B6C)
    WaitChrThread(0xFE, 1)

    def lambda_10B81():
        OP_95(0xFE, 149200, 0, 106300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10B81)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_100_10B4D end

    def Function_101_10BA2(): pass

    label("Function_101_10BA2")


    def lambda_10BA7():
        OP_95(0xFE, 110500, 0, -102500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10BA7)

    def lambda_10BC1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10BC1)
    WaitChrThread(0xFE, 1)

    def lambda_10BD6():
        OP_95(0xFE, 109100, 0, -103400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10BD6)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_101_10BA2 end

    def Function_102_10BF7(): pass

    label("Function_102_10BF7")


    def lambda_10BFC():
        OP_95(0xFE, 110500, 0, -102500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10BFC)

    def lambda_10C16():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10C16)
    WaitChrThread(0xFE, 1)

    def lambda_10C2B():
        OP_95(0xFE, 109300, 0, -102300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10C2B)
    WaitChrThread(0xFE, 1)

    def lambda_10C49():

        label("loc_10C49")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_10C49")

    QueueWorkItem2(0xFE, 2, lambda_10C49)
    Return()

    # Function_102_10BF7 end

    def Function_103_10C57(): pass

    label("Function_103_10C57")


    def lambda_10C5C():
        OP_95(0xFE, 110500, 0, -102500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10C5C)

    def lambda_10C76():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10C76)
    WaitChrThread(0xFE, 1)

    def lambda_10C8B():
        OP_95(0xFE, 107600, 0, -103100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10C8B)
    WaitChrThread(0xFE, 1)

    def lambda_10CA9():

        label("loc_10CA9")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_10CA9")

    QueueWorkItem2(0xFE, 2, lambda_10CA9)
    Return()

    # Function_103_10C57 end

    def Function_104_10CB7(): pass

    label("Function_104_10CB7")


    def lambda_10CBC():
        OP_95(0xFE, 110500, 0, -102500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10CBC)

    def lambda_10CD6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10CD6)
    WaitChrThread(0xFE, 1)

    def lambda_10CEB():
        OP_95(0xFE, 107300, 0, -102000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10CEB)
    WaitChrThread(0xFE, 1)

    def lambda_10D09():

        label("loc_10D09")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_10D09")

    QueueWorkItem2(0xFE, 2, lambda_10D09)
    Return()

    # Function_104_10CB7 end

    def Function_105_10D17(): pass

    label("Function_105_10D17")


    def lambda_10D1C():
        OP_95(0xFE, 110500, 0, -102500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10D1C)

    def lambda_10D36():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10D36)
    WaitChrThread(0xFE, 1)

    def lambda_10D4B():
        OP_95(0xFE, 109000, 0, -101000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10D4B)
    WaitChrThread(0xFE, 1)

    def lambda_10D69():

        label("loc_10D69")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_10D69")

    QueueWorkItem2(0xFE, 2, lambda_10D69)
    Return()

    # Function_105_10D17 end

    def Function_106_10D77(): pass

    label("Function_106_10D77")


    def lambda_10D7C():
        OP_95(0xFE, 110500, 0, -102500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10D7C)

    def lambda_10D96():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10D96)
    WaitChrThread(0xFE, 1)

    def lambda_10DAB():
        OP_95(0xFE, 108000, 0, -100300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10DAB)
    WaitChrThread(0xFE, 1)

    def lambda_10DC9():

        label("loc_10DC9")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_10DC9")

    QueueWorkItem2(0xFE, 2, lambda_10DC9)
    Return()

    # Function_106_10D77 end

    def Function_107_10DD7(): pass

    label("Function_107_10DD7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00900.itc", 0x28)
    LoadChrToIndex("apl/ch51258.itc", 0x29)
    SoundLoad(803)
    SetChrPos(0x101, -3000, 0, -127400, 0)
    SetChrPos(0x102, -1700, 0, -126900, 0)
    SetChrPos(0x103, -4100, 0, -126900, 0)
    SetChrPos(0x104, -5400, 0, -127400, 0)
    SetChrPos(0x109, -2500, 0, -128300, 0)
    SetChrPos(0x105, -4500, 0, -128300, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x2E, 0x28)
    SetChrSubChip(0x2E, 0x0)
    ClearChrFlags(0x2E, 0x80)
    SetChrFlags(0x2E, 0x8000)
    SetChrPos(0x2E, 0, 0, -127700, 0)
    SetChrChipByIndex(0x2F, 0xB)
    SetChrSubChip(0x2F, 0x0)
    ClearChrFlags(0x2F, 0x80)
    SetChrFlags(0x2F, 0x8000)
    SetChrPos(0x2F, 5650, -5850, -106000, 270)
    SetChrChipByIndex(0x2C, 0xD)
    SetChrSubChip(0x2C, 0x0)
    ClearChrFlags(0x2C, 0x80)
    SetChrFlags(0x2C, 0x8000)
    SetChrPos(0x2C, 5650, -5850, -108800, 270)
    SetChrChipByIndex(0x13, 0xC)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 5650, -5850, -111700, 270)
    EndChrThread(0x13, 0xFF)
    SetChrChipByIndex(0x2D, 0xE)
    SetChrSubChip(0x2D, 0x0)
    ClearChrFlags(0x2D, 0x80)
    SetChrFlags(0x2D, 0x8000)
    SetChrPos(0x2D, 1800, -5850, -102100, 180)
    SetChrChipByIndex(0x36, 0xF)
    SetChrSubChip(0x36, 0x0)
    ClearChrFlags(0x36, 0x80)
    SetChrFlags(0x36, 0x8000)
    SetChrPos(0x36, 11800, -5850, -104800, 270)
    SetChrChipByIndex(0x34, 0x7)
    SetChrSubChip(0x34, 0x0)
    ClearChrFlags(0x34, 0x80)
    SetChrFlags(0x34, 0x8000)
    SetChrPos(0x34, 5000, -5800, -99450, 180)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetMapObjFrame(0xFF, "bs", 0x1, 0x1)
    OP_68(-3000, 300, -126900, 0)
    MoveCamera(47, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    VolumeBGM(0x50, 0x3E8)
    OP_68(-3000, 1300, -126900, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x109,
        "#12P#10107F...That's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#11P...It is just as\x01",
            "Lawyer Ian feared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10308FIt seems like the Blood and Iron Chancellor and the\x01",
            "President are shoving this down Crossbell's throat.\x02\x03",
            "#10301FIs there no basis for an objection?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#11PIt's true that there're various structural \x01",
            "flaws in the autonomous state law.\x02\x03",
            "#00108FThat's why it is difficult\x01",
            "for Mayor Dieter and my\x01",
            "grandfather to object.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00006F──But, those defects were\x01",
            "forced on Crossbell during\x01",
            "its founding 70 years ago.\x02\x03",
            "#00013FOn top of that, no one could agree\x01",
            "with their overbearing statements.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#00301FHmph. So this crime was premeditated.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2E,
        "#00603F#11P............\x02",
    )

    CloseMessageWindow()
    OP_93(0x2E, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x2E,
        (
            "#00601F#11PIn any case, the conference\x01",
            "discussions are none of our business.\x02\x03",
            "Right now, we need to focus on making sure\x01",
            "the meeting comes to an end without incident.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-1500, 1300, -127550, 1300)

    def lambda_11348():
        TurnDirection(0x101, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_11348)
    Sleep(50)

    def lambda_11358():
        TurnDirection(0x102, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_11358)
    Sleep(50)

    def lambda_11368():
        TurnDirection(0x109, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_11368)
    Sleep(50)

    def lambda_11378():
        TurnDirection(0x103, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_11378)
    Sleep(50)

    def lambda_11388():
        TurnDirection(0x105, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_11388)
    Sleep(50)

    def lambda_11398():
        TurnDirection(0x104, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_11398)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00001F#6P...Yes, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#00108FIn that case, perhaps another patrol──\x02",
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x2E, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Sound(804, 0, 100, 0)
    OP_24(0x323)
    OP_93(0x2E, 0xB4, 0x1F4)
    SetChrFlags(0x2E, 0x20)
    SetChrFlags(0x2E, 0x10)
    SetChrFlags(0x2E, 0x2)
    SetChrChipByIndex(0x2E, 0x29)
    SetChrSubChip(0x2E, 0x6)
    Sleep(300)
    SetChrSubChip(0x2E, 0x7)

    ChrTalk(
        0x2E,
        (
            "#00603F#5PSection One, this is Dudley.\x02\x03",
            "#00605F...Emma?\x01",
            "Has something──\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x2E,
        "#00607F#5PWhat...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#6P(...What is it?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#00108F(It looks like something happened...)\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x2E, 0x20)
    ClearChrFlags(0x2E, 0x10)
    ClearChrFlags(0x2E, 0x2)
    SetChrChipByIndex(0x2E, 0x28)
    SetChrSubChip(0x2E, 0x0)
    OP_93(0x2E, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x2E,
        (
            "#00606F#11P──"Red Constellation" and "Heiyue"\x01",
            "have each left their respective bases.\x02\x03",
            "#00601FIt seems they've shaken off our surveillance.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#6PWha...\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x104,
        "#6P#00307FWhat!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2E,
        (
            "#00603F#11PDon't panic. This is\x01",
            "within our expectations.\x02\x03",
            "#00601FI'll let you know if anything\x01",
            "else happens. Stay on your guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#6PU-Understood.\x02",
    )

    CloseMessageWindow()
    OP_92(0x2E, 0xDAC, 0xFFFE0430, 0x1F4)
    SetChrFlags(0x2E, 0x20)
    SetChrFlags(0x2E, 0x10)
    SetChrFlags(0x2E, 0x2)
    SetChrChipByIndex(0x2E, 0x29)
    SetChrSubChip(0x2E, 0x8)
    OP_68(9000, 1300, -130000, 4000)
    BeginChrThread(0x2E, 3, 0, 108)

    def lambda_117BB():
        OP_95(0xFE, 5500, 0, -130000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_117BB)
    Sleep(500)

    ChrTalk(
        0x2E,
        (
            "#5P#00603F#12A──Oh, that's right.\x02\x03",
            "#14A#00601FMaybe I should mobilize our\x01",
            "reserve police force...\x02",
        )
    )

    WaitChrThread(0x2E, 1)

    def lambda_11844():
        OP_95(0xFE, 11500, 0, -130000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_11844)
    Sleep(2000)

    def lambda_11861():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_11861)
    WaitChrThread(0x2E, 1)
    EndChrThread(0x2E, 0xFF)
    SetChrFlags(0x2E, 0x80)
    OP_6F(0x79)
    Fade(500)
    OP_68(-3000, 1300, -126900, 0)
    MoveCamera(47, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    OP_0D()
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
            "#6P#00308FDamn... So they're\x01",
            "really comin', huh...\x02\x03",
            "#00310FWhat could they be plannin'!?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_11994():
        TurnDirection(0x103, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_11994)
    Sleep(50)

    def lambda_119A4():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_119A4)
    Sleep(50)

    def lambda_119B4():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_119B4)
    Sleep(50)

    def lambda_119C4():
        TurnDirection(0x109, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_119C4)
    Sleep(50)

    def lambda_119D4():
        TurnDirection(0x105, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_119D4)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x103,
        "#11P#00208FMr. Randy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11PRandy, calm down.\x02\x03",
            "#00001FEven if it's the "Red Constellation",\x01",
            "I don't think they'd pick a fight here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#11PRight. There's a police squad protecting\x01",
            "the entrance of this building...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#11P#10101FCould they be starting a\x01",
            "conflict at a time like this...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10306FHmm. I feel like that's\x01",
            "a little unnatural.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 60, -1, -1)
    Sleep(300)
    OP_82(0x64, 0x64, 0xBB8, 0x1F4)
    SetChrName("Elderly Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#4S──What did you say!?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_11C3D():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_11C3D)
    Sleep(50)

    def lambda_11C4D():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_11C4D)
    Sleep(50)

    def lambda_11C5D():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_11C5D)
    Sleep(50)

    def lambda_11C6D():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_11C6D)
    Sleep(50)

    def lambda_11C7D():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_11C7D)
    Sleep(50)

    def lambda_11C8D():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_11C8D)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x101,
        "#11P#00011FWhat was that just now...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00112F#11PG-Grandfather...?\x02",
    )

    CloseMessageWindow()
    OP_68(-3000, 300, -126900, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_24(0x323)
    SetScenarioFlags(0x22, 4)
    NewScene("c1540", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_107_10DD7 end

    def Function_108_11D28(): pass

    label("Function_108_11D28")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11D46")
    OP_A1(0x2E, 0x7D0, 0x8, 0x8, 0x9, 0xA, 0x9, 0x8, 0xB, 0xC, 0xB)
    Jump("Function_108_11D28")

    label("loc_11D46")

    Return()

    # Function_108_11D28 end

    def Function_109_11D47(): pass

    label("Function_109_11D47")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x28)
    SoundLoad(803)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    SetChrPos(0x101, -3000, 0, -127400, 0)
    SetChrPos(0x102, -1700, 0, -126900, 0)
    SetChrPos(0x103, -4100, 0, -126900, 0)
    SetChrPos(0x104, -5400, 0, -127400, 0)
    SetChrPos(0x109, -2500, 0, -128300, 0)
    SetChrPos(0x105, -4500, 0, -128300, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x2F, 0xB)
    SetChrSubChip(0x2F, 0x0)
    ClearChrFlags(0x2F, 0x80)
    SetChrFlags(0x2F, 0x8000)
    SetChrPos(0x2F, 5650, -5850, -106000, 270)
    SetChrChipByIndex(0x2C, 0xD)
    SetChrSubChip(0x2C, 0x0)
    ClearChrFlags(0x2C, 0x80)
    SetChrFlags(0x2C, 0x8000)
    SetChrPos(0x2C, 5650, -5850, -108800, 270)
    SetChrChipByIndex(0x13, 0xC)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 5650, -5850, -111700, 270)
    EndChrThread(0x13, 0xFF)
    SetChrChipByIndex(0x2D, 0xE)
    SetChrSubChip(0x2D, 0x0)
    ClearChrFlags(0x2D, 0x80)
    SetChrFlags(0x2D, 0x8000)
    SetChrPos(0x2D, 1800, -5850, -102100, 180)
    SetChrChipByIndex(0x36, 0xF)
    SetChrSubChip(0x36, 0x0)
    ClearChrFlags(0x36, 0x80)
    SetChrFlags(0x36, 0x8000)
    SetChrPos(0x36, 11800, -5850, -104800, 270)
    SetChrChipByIndex(0x34, 0x7)
    SetChrSubChip(0x34, 0x0)
    ClearChrFlags(0x34, 0x80)
    SetChrFlags(0x34, 0x8000)
    SetChrPos(0x34, 5000, -5800, -99450, 180)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetMapObjFrame(0xFF, "bs", 0x1, 0x1)
    OP_68(-3560, 300, -126600, 0)
    MoveCamera(47, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16110, 0)
    VolumeBGM(0x50, 0x3E8)
    OP_68(-3560, 1300, -126600, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#11P#00010FUgh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10106FH-How terrible...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#11PAbsurd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#00301F...How dare they\x01",
            "be so brazen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#11P...However, it's not the case that their\x01",
            "proposals completely lack any basis.\x02\x03",
            "#00108FI hoped it wouldn't\x01",
            "go like this, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10308FHm, they just have to hold\x01",
            "out a little longer...\x02",
        )
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_120C1():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_120C1)
    Sleep(50)

    def lambda_120D1():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_120D1)
    Sleep(50)

    def lambda_120E1():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_120E1)
    Sleep(50)

    def lambda_120F1():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_120F1)
    Sleep(50)

    def lambda_12101():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_12101)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x28)
    SetChrSubChip(0x101, 0x2)
    Sleep(500)

    ChrTalk(
        0x101,
        "#5P#00001FAt a time like this...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101F#11PIs that from Mr. Dudley?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x3)
    Sleep(300)
    Sound(804, 0, 100, 0)
    OP_24(0x323)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00001FYes, it's Bannings──\x02",
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
            "It's me, Sergei.\x02",
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
            "#00005FChief Sergei?\x01",
            "What's wro──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Sergei's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "No time. I'll be brief.\x02\x03",
            "──I got a call from Sonya.\x02\x03",
            "The radar facilities near the Tangram\x01",
            "and Bellguard gates were destroyed.\x02\x03",
            "They're anti-air radars to detect\x01",
            "airships invading the state.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00011F#3SWha...!?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Sergei's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It appears it was the work of\x01",
            "those rumored terrorists.\x02\x03",
            "I told Dudley, but I'll tell you\x01",
            "guys too. Be ready for anything.\x02",
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
            "#00007FU-Understood!\x02",
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
    SetChrSubChip(0x101, 0x2)
    Sound(804, 0, 100, 0)

    ChrTalk(
        0x102,
        "#00101F#11PW-What's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00307FDon't tell me my uncle and\x01",
            "the others did something!?\x02",
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
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        (
            "#11P#00013FN-No, that's\x01",
            "not them──\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 60, -1, -1)
    SetChrName("Man's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "──Everyone.\x01",
            "Can I say something?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1260F():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1260F)
    Sleep(50)

    def lambda_1261F():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1261F)
    Sleep(50)

    def lambda_1262F():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1262F)
    Sleep(50)

    def lambda_1263F():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1263F)
    Sleep(50)

    def lambda_1264F():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1264F)
    Sleep(50)

    def lambda_1265F():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1265F)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    OP_68(-3560, 300, -126600, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    OP_24(0x323)
    SetScenarioFlags(0x22, 5)
    NewScene("c1540", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_109_11D47 end

    def Function_110_126B1(): pass

    label("Function_110_126B1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, -3000, 0, -127400, 0)
    SetChrPos(0x102, -1700, 0, -126900, 0)
    SetChrPos(0x103, -4100, 0, -126900, 0)
    SetChrPos(0x104, -5400, 0, -127400, 0)
    SetChrPos(0x109, -2500, 0, -128300, 0)
    SetChrPos(0x105, -4500, 0, -128300, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(-3560, 300, -126600, 0)
    MoveCamera(47, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16110, 0)
    OP_68(-3560, 1300, -126600, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x102,
        "#11P#00107FAh──\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10310FThis is... \x01",
            "A very troublesome situation.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        (
            "#5P#00203F...It seems we have lost\x01",
            "control of Orchis Tower.\x02\x03",
            "#00201FPossibly the doing\x01",
            "of yesterday's hacker.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xE1, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#11P#00010FUgh, we have to go, too!\x02\x03",
            "#00007FAnyway, we've got to go to 35F and\x01",
            "ensure the safety of the heads of state!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_128D6():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_128D6)
    Sleep(50)

    def lambda_128E6():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_128E6)
    Sleep(50)

    def lambda_128F6():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_128F6)
    Sleep(50)

    def lambda_12906():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_12906)
    Sleep(50)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x109,
        "#12P#10107F──Roger!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00307FIf the elevator isn't working, we'll have\x01",
            "no choice but to use the emergency stairs!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -3000, 0, -128000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_29(0xA4, 0x1, 0x4)
    OP_29(0xA4, 0x1, 0x5)
    EventEnd(0x5)
    Return()

    # Function_110_126B1 end

    def Function_111_129DF(): pass

    label("Function_111_129DF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51235.itc", 0x28)
    SoundLoad(938)
    SoundLoad(145)
    SoundLoad(143)
    OP_68(-55500, 1700, 3700, 0)
    MoveCamera(37, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x101, -55700, 0, 700, 0)
    SetChrPos(0x102, -56700, 0, -300, 0)
    SetChrPos(0x103, -54700, 0, 300, 0)
    SetChrPos(0x104, -54700, 0, -1200, 0)
    SetChrPos(0x109, -55700, 0, -800, 0)
    SetChrPos(0x105, -56700, 0, -1800, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x3E, 0x80)
    OP_78(0x13, 0x3E)
    OP_49()
    SetChrPos(0x3E, -55100, 100, 2200, 0)
    OP_D5(0x3E, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x13, 0x1000)
    SetMapObjFlags(0x13, 0x4)
    FadeToBright(1000, 0)
    OP_68(-55700, 1300, 1700, 2000)
    MoveCamera(53, 19, 0, 2000)
    SetCameraDistance(17500, 2000)
    OP_6F(0x79)

    ChrTalk(
        0x109,
        (
            "#12P#10101FT-This was open\x01",
            "just a moment ago...!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        "#6P#00013FTio, can you do it...!?\x02",
    )

    CloseMessageWindow()

    def lambda_12B75():

        label("loc_12B75")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_12B75")

    QueueWorkItem2(0x102, 2, lambda_12B75)

    def lambda_12B87():

        label("loc_12B87")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_12B87")

    QueueWorkItem2(0x104, 2, lambda_12B87)

    def lambda_12B99():

        label("loc_12B99")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_12B99")

    QueueWorkItem2(0x109, 2, lambda_12B99)

    def lambda_12BAB():

        label("loc_12BAB")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_12BAB")

    QueueWorkItem2(0x105, 2, lambda_12BAB)

    def lambda_12BBD():

        label("loc_12BBD")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_12BBD")

    QueueWorkItem2(0x101, 2, lambda_12BBD)

    ChrTalk(
        0x103,
        "#11P#00201F...I will try something.\x02",
    )

    CloseMessageWindow()

    def lambda_12BF8():
        OP_95(0xFE, -54700, 0, 2200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_12BF8)
    WaitChrThread(0x103, 1)
    Sound(853, 0, 100, 0)
    Sound(318, 0, 100, 0)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Tio connected an orbal cable\x01",
            "to the shutter control panel.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0x103, 0x10E, 0x1F4)
    Sleep(150)
    Fade(250)
    Sound(802, 0, 100, 0)
    ClearMapObjFlags(0x13, 0x4)
    SetChrChipByIndex(0x103, 0x28)
    SetChrSubChip(0x103, 0x0)
    BeginChrThread(0x103, 3, 0, 113)
    Sound(938, 2, 100, 0)
    SetCameraDistance(17200, 0)
    OP_0D()
    Sleep(1300)

    ChrTalk(
        0x103,
        (
            "#00205F#30W#11P............\x02\x03",
            "#00203F#20W...It is a bit difficult.\x02\x03",
            "#00201FBut, if I do this, maybe...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-55000, 1500, 3700, 0)
    MoveCamera(39, 29, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15500, 0)
    OP_0D()
    SetCameraDistance(17500, 2000)
    Sound(140, 0, 100, 0)
    Sleep(500)
    EndChrThread(0x103, 0x3)
    StopSound(938, 300, 100)
    BeginChrThread(0x43, 1, 0, 114)
    ClearMapObjFlags(0xC, 0x10)
    OP_71(0xC, 0x0, 0x3C, 0x0, 0x0)
    Sleep(500)

    def lambda_12D9D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_12D9D)
    Sleep(50)

    def lambda_12DAD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_12DAD)
    Sleep(50)

    def lambda_12DBD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_12DBD)
    Sleep(50)

    def lambda_12DCD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_12DCD)
    Sleep(50)

    def lambda_12DDD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_12DDD)
    Sleep(500)

    ChrTalk(
        0x102,
        "#00102FIt opened...!\x02",
    )

    CloseMessageWindow()
    OP_79(0xC)

    ChrTalk(
        0x104,
        "#00309FThat's our peTiote!\x02",
    )

    CloseMessageWindow()
    OP_68(-55700, 1300, 1700, 1500)
    MoveCamera(53, 19, 0, 1500)
    SetCameraDistance(17500, 1500)
    Sleep(1250)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetMapObjFlags(0x13, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    OP_6F(0x79)
    TurnDirection(0x103, 0x104, 500)

    ChrTalk(
        0x103,
        (
            "#00206FNo, it is just that the security\x01",
            "settings have been lowered.\x02\x03",
            "#00208FBut now that this one has been\x01",
            "unlocked, it is possible that the other\x01",
            "doors' security has been reinforced.\x02\x03",
            "#00201FI might not be able\x01",
            "to open all of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#N#10306FThen we'll need to be careful.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#12P#00010FUgh... \x01",
            "Anyway, let's go!\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 112)
    Sleep(650)
    BeginChrThread(0x103, 3, 0, 112)
    Sleep(50)
    BeginChrThread(0x102, 3, 0, 112)
    Sleep(400)
    BeginChrThread(0x109, 3, 0, 112)
    Sleep(400)
    BeginChrThread(0x104, 3, 0, 112)
    Sleep(400)
    BeginChrThread(0x105, 3, 0, 112)
    OP_68(-55700, 300, 1700, 3000)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    OP_C9(0x1, 0x10000)
    OP_50(0x52, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x21, 5)
    OP_24(0x3AA)
    OP_24(0x91)
    SetScenarioFlags(0x22, 7)
    NewScene("c1540", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_111_129DF end

    def Function_112_1304D(): pass

    label("Function_112_1304D")


    def lambda_13052():
        OP_95(0xFE, -55700, 0, 3300, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_13052)
    WaitChrThread(0xFE, 1)

    def lambda_13070():
        OP_95(0xFE, -55700, 0, 13500, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_13070)
    WaitChrThread(0xFE, 1)

    def lambda_1308E():
        OP_95(0xFE, -52000, 0, 13500, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1308E)
    WaitChrThread(0xFE, 1)

    def lambda_130AC():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_130AC)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_112_1304D end

    def Function_113_130C6(): pass

    label("Function_113_130C6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_130E0")
    OP_A1(0x103, 0x7D0, 0x4, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_113_130C6")

    label("loc_130E0")

    Return()

    # Function_113_130C6 end

    def Function_114_130E1(): pass

    label("Function_114_130E1")

    Sound(145, 2, 100, 0)
    Sleep(2000)
    Sound(143, 0, 70, 0)
    OP_24(0x91)
    Return()

    # Function_114_130E1 end

    def Function_115_130F4(): pass

    label("Function_115_130F4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51616.itc", 0x28)
    LoadChrToIndex("chr/ch27702.itc", 0x29)
    LoadChrToIndex("chr/ch27802.itc", 0x2A)
    SetChrPos(0x0, 3000, 0, 2500, 0)
    SetChrPos(0x1, 3000, 0, 2500, 0)
    SetChrPos(0x2, 3000, 0, 2500, 0)
    SetChrPos(0x3, 3000, 0, 2500, 0)
    SetChrChipByIndex(0x2D, 0xE)
    SetChrSubChip(0x2D, 0x1)
    ClearChrFlags(0x2D, 0x80)
    SetChrFlags(0x2D, 0x8000)
    SetChrPos(0x2D, -128000, 0, 58100, 180)
    SetChrChipByIndex(0x30, 0x29)
    SetChrSubChip(0x30, 0x1)
    ClearChrFlags(0x30, 0x80)
    SetChrFlags(0x30, 0x8000)
    SetChrPos(0x30, -126300, 0, 58100, 180)
    SetChrChipByIndex(0x31, 0x2A)
    SetChrSubChip(0x31, 0x2)
    ClearChrFlags(0x31, 0x80)
    SetChrFlags(0x31, 0x8000)
    SetChrPos(0x31, -128000, 0, 53800, 0)
    SetChrChipByIndex(0x32, 0x1E)
    SetChrSubChip(0x32, 0x2)
    ClearChrFlags(0x32, 0x80)
    SetChrFlags(0x32, 0x8000)
    SetChrPos(0x32, -126300, 0, 53800, 0)
    ClearMapObjFlags(0x15, 0x4)
    SetMapObjFlags(0x15, 0x1000)
    OP_FF(0x15, 0x320, 0x320, 0x320)
    SetMapObjFrame(0x15, "01", 0x0, 0x1)
    SetMapObjFrame(0x15, "02", 0x1, 0x1)
    SetMapObjFrame(0x15, "03", 0x0, 0x1)
    SetChrChipByIndex(0x3F, 0x28)
    SetChrSubChip(0x3F, 0x0)
    ClearChrFlags(0x3F, 0x80)
    SetChrFlags(0x3F, 0x8000)
    SetChrPos(0x3F, -3500, 0, 19000, 90)
    SetChrChipByIndex(0x40, 0x28)
    SetChrSubChip(0x40, 0x0)
    ClearChrFlags(0x40, 0x80)
    SetChrFlags(0x40, 0x8000)
    SetChrPos(0x40, -3500, 0, 10900, 90)
    SetChrChipByIndex(0x41, 0x28)
    SetChrSubChip(0x41, 0x0)
    ClearChrFlags(0x41, 0x80)
    SetChrFlags(0x41, 0x8000)
    SetChrPos(0x41, -3500, 0, 27000, 90)
    SetChrChipByIndex(0x42, 0x28)
    SetChrSubChip(0x42, 0x0)
    ClearChrFlags(0x42, 0x80)
    SetChrFlags(0x42, 0x8000)
    SetChrPos(0x42, -1000, 0, 0, 0)

    def lambda_132AB():
        OP_96(0xFE, 0xFFFFFC18, 0x0, 0x6978, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x42, 1, lambda_132AB)
    OP_68(-1000, 1300, 2000, 0)
    MoveCamera(30, 19, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(20000, 0)
    OP_68(-1000, 700, 17000, 7000)
    MoveCamera(39, 21, 0, 7000)
    SetCameraDistance(25500, 7000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-120000, 1500, 56000, 0)
    MoveCamera(40, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    OP_68(-125000, 1500, 56000, 4000)
    SetCameraDistance(15000, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    SetMessageWindowPos(210, 90, -1, -1)
    SetChrName("President Dieter")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──For this reason, we all stand before the\x01",
            "Goddess as equals, burdened with sin...\x02\x03",
            "Deception and cowardice. \x01",
            "These are the names of our sins.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetMapObjFrame(0x15, "01", 0x1, 0x1)
    SetMapObjFrame(0x15, "02", 0x0, 0x1)
    SetMapObjFrame(0x15, "03", 0x0, 0x1)
    Sleep(300)
    SetMessageWindowPos(210, 90, -1, -1)
    SetChrName("President Dieter")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "For revenge for the souls which have\x01",
            "already been sacrificed as well...!\x02\x03",
            "For those wounded in the\x01",
            "recent attack as well!\x02\x03",
            "And for a peaceful, proud future\x01",
            "for our children as well!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetMapObjFrame(0x15, "01", 0x0, 0x1)
    SetMapObjFrame(0x15, "02", 0x0, 0x1)
    SetMapObjFrame(0x15, "03", 0x1, 0x1)
    Sleep(300)
    SetMessageWindowPos(210, 90, -1, -1)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)
    SetChrName("President Dieter")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#4SNow, we must discard deception\x01",
            "and cowardice, and stand with\x01",
            "pride, and courage!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(-127000, 1200, 56000, 1500)
    OP_6F(0x79)

    NpcTalk(
        0x30,
        "Congressman Campbell",
        "#5PHm, ridiculous...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x31,
        (
            "#6PB-But...\x01",
            "I do wonder about that...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x2D,
        "#5P#02501F(...Dieter...)\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(15500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetScenarioFlags(0x22, 5)
    NewScene("c1500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_115_130F4 end

    def Function_116_136A1(): pass

    label("Function_116_136A1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch08702.itc", 0x28)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu11201.itp")
    SetChrChipByIndex(0xC, 0x28)
    SetChrSubChip(0xC, 0x1)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 157800, 0, 58000, 180)
    ClearMapObjFlags(0x14, 0x4)
    SetMapObjFlags(0x14, 0x1000)
    OP_FF(0x14, 0x320, 0x320, 0x320)
    ClearChrFlags(0x3E, 0x80)
    OP_78(0x14, 0x3E)
    OP_49()
    SetChrPos(0x3E, 162000, 500, 56000, 0)
    OP_D5(0x3E, 0x0, 0x15F90, 0x0, 0x0)
    OP_68(161000, 2500, 56000, 0)
    MoveCamera(55, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(12000, 0)
    OP_68(159000, 2100, 56000, 4000)
    MoveCamera(45, 15, 0, 4000)
    SetCameraDistance(14000, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    SetMessageWindowPos(200, 120, -1, -1)
    SetChrName("President's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Actually, Secretary Arios once\x01",
            "also served Crossbell in the role\x01",
            "of an excellent police detective.\x02\x03",
            "And in the Guild, as you know,\x01",
            "he's known for having resolved\x01",
            "a number of international incidents.\x02\x03",
            "For these reasons, I assure you\x01",
            "that he's the right choice for\x01",
            "this position.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(158490, 900, 58440, 2000)
    MoveCamera(20, 15, 0, 2000)
    OP_6F(0x79)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0xC,
        (
            "#40W...Father...\x01",
            "...Why...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    SetCameraDistance(13500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x23, 5)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_116_136A1 end

    def Function_117_139CB(): pass

    label("Function_117_139CB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch03800.itc", 0x28)
    LoadChrToIndex("apl/ch51717.itc", 0x29)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10500.itp")
    SoundLoad(4071)
    SoundLoad(4072)
    SetChrChipByIndex(0x34, 0x28)
    SetChrSubChip(0x34, 0x0)
    ClearChrFlags(0x34, 0x80)
    SetChrFlags(0x34, 0x8000)
    SetChrPos(0x34, 163400, 0, 57000, 90)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 163400, 0, 56000, 90)
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    OP_68(163400, -800, 56500, 0)
    MoveCamera(41, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    OP_68(163400, 1200, 56500, 4000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0xC,
        "#6P#11230FThe blue "barrier" has...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x34, 0xC, 400)
    Sleep(150)

    ChrTalk(
        0x34,
        (
            "#10503F...No need to worry.\x02\x03",
            "#10502FNo harm will come\x01",
            "to you, so relax.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#6P#11221F...!!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x34, 500)
    OP_68(163400, 1100, 56750, 500)
    MoveCamera(41, 19, 0, 500)
    SetCameraDistance(16000, 500)

    def lambda_13B6C():
        OP_96(0xFE, 0x27E48, 0x0, 0xDCB4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_13B6C)
    WaitChrThread(0xC, 1)
    Fade(250)
    Sound(812, 0, 100, 0)
    Sound(811, 0, 20, 0)
    SetChrChipByIndex(0x34, 0x29)
    SetChrSubChip(0x34, 0x0)
    SetChrFlags(0x34, 0x10)
    SetChrFlags(0x34, 0x2)
    SetChrFlags(0x34, 0x20)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_0D()
    Sleep(110)
    Sound(898, 0, 100, 0)
    SetChrSubChip(0x34, 0x1)
    Sleep(110)
    SetChrSubChip(0x34, 0x2)
    OP_6F(0x79)
    SetCameraDistance(15500, 20000)

    ChrTalk(
        0xC,
        (
            "#12P#11226F#30WD-Don't think about me,\x01",
            "think about yourself...!\x02\x03",
            "#11227F#30W...Why... ...Why are\x01",
            "you doing this!?\x02\x03",
            "#11232F#30WIf mother saw you like this...\x01",
            "...I'm sure she'd be very sad...!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(898, 0, 100, 0)
    SetChrSubChip(0x34, 0x3)
    Sleep(130)
    SetChrSubChip(0x34, 0x4)
    Sleep(130)
    SetChrSubChip(0x34, 0x5)
    Sleep(500)

    ChrTalk(
        0x34,
        (
            "#10504F#5P...That's true.\x02\x03",
            "If Saya were here... I'm sure she would\x01",
            "lecture me with a stern look on her face.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x34, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x34)
    Sleep(300)
    Sound(812, 0, 100, 0)
    SetChrSubChip(0x34, 0x6)
    Sleep(130)
    SetChrSubChip(0x34, 0x7)
    Sleep(130)
    SetChrSubChip(0x34, 0x8)
    Sleep(500)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0x34,
        (
            "#4071V#40W#25A──Shizuku.\x02\x03",
            "#4072V#40W#30AI have one favor to ask of you.\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    SetCameraDistance(15000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 7)
    NewScene("c1600", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_117_139CB end

    def Function_118_13E50(): pass

    label("Function_118_13E50")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch06400.itc", 0x28)
    OP_68(-1500, 1100, 0, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18250, 0)
    SetChrPos(0x101, -1000, 0, -100, 90)
    SetChrPos(0x102, -2100, 0, 0, 90)
    SetChrPos(0x103, -2100, 0, -1300, 90)
    SetChrPos(0x104, -2100, 0, 1200, 90)
    SetChrPos(0xF4, -3200, 0, 600, 90)
    SetChrPos(0xF5, -3200, 0, -800, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetCameraDistance(17500, 1500)
    FadeToBright(1000, 0)
    Sleep(500)
    BeginChrThread(0x101, 2, 0, 119)
    Sleep(100)
    BeginChrThread(0x102, 2, 0, 120)
    Sleep(300)
    BeginChrThread(0xF4, 2, 0, 119)
    BeginChrThread(0xF5, 2, 0, 120)
    Sleep(400)
    BeginChrThread(0x103, 2, 0, 120)
    Sleep(200)
    BeginChrThread(0x104, 2, 0, 119)
    OP_0D()
    Sleep(500)
    EndChrThread(0x101, 0x2)
    OP_93(0x101, 0x5A, 0x0)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0xF4, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0xF5, 0x2)
    Sleep(300)

    ChrTalk(
        0x101,
        "#5P#00001FWe're here...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#6PAccording to Chief Roberts, there should \x01",
            "be a lot of people on this floor, but...\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xF, 0x28)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x40)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -5500, 0, 11000, 90)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, -5500, 0, 11000, 90)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    EndChrThread(0x10, 0xFF)
    SetChrSubChip(0x10, 0x0)

    NpcTalk(
        0xF,
        "Nervous Voice",
        "#2SY-You guys are...!?\x02",
    )

    CloseMessageWindow()
    StopBGM(0x1770)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-2500, 1100, 11000, 2000)

    def lambda_14114():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_14114)
    Sleep(50)

    def lambda_14124():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_14124)
    Sleep(50)

    def lambda_14134():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_14134)
    Sleep(50)

    def lambda_14144():
        OP_93(0xF4, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_14144)
    Sleep(50)

    def lambda_14154():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_14154)
    Sleep(50)

    def lambda_14164():
        OP_93(0xF5, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_14164)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)
    Sound(103, 0, 100, 0)
    BeginChrThread(0xF, 3, 0, 121)
    Sleep(800)
    BeginChrThread(0x10, 3, 0, 122)
    Sleep(2500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00011FT-The Vice Chief!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00105FWhy are you here...?\x02",
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0xF,
        "#5PT-That's my line!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5PI... Uh... Came to ask the Secretary\x01",
            "about the declaration of martial law\x01",
            "that was handed down last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5PI was in the middle of doing that when the restrictions\x01",
            "went into effect, and got stuck on this floor.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_143C7")

    ChrTalk(
        0x10A,
        "#12P#N#00606F...I understand.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_14420")

    label("loc_143C7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_143FF")

    ChrTalk(
        0x109,
        "#12P#N#10106FIs that so...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_14420")

    label("loc_143FF")


    ChrTalk(
        0x102,
        "#12P#00106FIs that right...\x02",
    )

    CloseMessageWindow()

    label("loc_14420")


    ChrTalk(
        0x104,
        (
            "#00309FHow should I say it. \x01",
            "I didn't expect this from you.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_144D4")

    ChrTalk(
        0x105,
        (
            "#12P#N#10402FHu hu, to think you had the strong spirit\x01",
            "to enquire with your superiors...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1452F")

    label("loc_144D4")


    ChrTalk(
        0x103,
        (
            "#12P#N#00204FI didn't think you had the strong spirit\x01",
            "to enquire with your superiors.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1452F")

    OP_63(0xF, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xF,
        "#5PW-What ever do you mean!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5PYou guys know that you're wanted by the\x01",
            "State Guard in the first place, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#5PWhat the hell do you think you're doing!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FWell... It's a long story.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1467C")

    ChrTalk(
        0x103,
        (
            "#12P#N#00205FYou there... Were you in the\x01",
            "IBC technology division?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_146C2")

    label("loc_1467C")


    ChrTalk(
        0x102,
        (
            "#12P#00105FYou there... Were you in the\x01",
            "IBC technology division?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_146C2")


    ChrTalk(
        0x10,
        "#5PYeah... I'm Researcher David.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PYesterday, Milady Mariabell announced the\x01",
            "dissolution of the technology division...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PMy partner wasn't with me, and I was\x01",
            "dumbfounded when I was brought to this floor.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14805")

    ChrTalk(
        0x106,
        (
            "#12P#N#10708F...I think it's best to first\x01",
            "confirm each other's situations.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_148CB")

    label("loc_14805")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1486D")

    ChrTalk(
        0x109,
        (
            "#12P#N#10108FUmm, I think it's best to first\x01",
            "confirm each other's situations.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_148CB")

    label("loc_1486D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_148CB")

    ChrTalk(
        0x10A,
        (
            "#12P#N#00603FHm, it seems best to first\x01",
            "confirm each other's situations.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_148CB")

    SetCameraDistance(17000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_68(-122300, 1100, 2650, 0)
    MoveCamera(42, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16000, 0)
    SetChrPos(0x101, -122500, 0, 1500, 0)
    SetChrPos(0x102, -123800, 0, 1200, 45)
    SetChrPos(0x103, -122900, 0, 300, 0)
    SetChrPos(0x104, -124900, 0, 1400, 45)
    SetChrPos(0xF4, -121200, 0, 800, 315)
    SetChrPos(0xF5, -120900, 0, 2000, 315)
    SetChrPos(0xF, -122100, 0, 3800, 180)
    SetChrPos(0x10, -123200, 0, 4000, 180)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -120700, 0, 4200, 225)
    EndChrThread(0xD, 0xFF)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -124000, 0, 4800, 180)
    EndChrThread(0xE, 0xFF)
    SetChrSubChip(0xE, 0x0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7302", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x12E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM(-1, -1)
    ReplaceBGM("ed7151", "ed7302")
    ReplaceBGM("ed7550", "ed7302")
    SetCameraDistance(17000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0xF,
        "#5PS-So that's what happened...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5PEver since the independence declaration of\x01",
            "invalidity, things haven't looked so good, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11PW-Why did this have to happen...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PI feel like I'm\x01",
            "having a bad dream...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PI see... So Clay is\x01",
            "assisting Chief Roberts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PIt's no wonder their tower hacking \x01",
            "methods have been getting better\x01",
            "for the past couple days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103FSo then... Vice Chief.\x02\x03",
            "#00101FWho're the people on the\x01",
            "President's faction on this floor?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#5PH-Hmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5POf course the President and Miss Mariabell, the Secretary\x01",
            "of Defense and the jaegers...none of them are here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5PAnd... That little girl that\x01",
            "was with all of you neither.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00006F...I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00108FJust what floor are they on...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203F...I think we need to wait\x01",
            "to hear from Chief Roberts.\x02\x03",
            "#00201FI think he is hurriedly searching\x01",
            "the upper floors as we speak.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(150)

    ChrTalk(
        0x104,
        (
            "#6P#00303FWhile he's doin' that, let's\x01",
            "check who else is on this floor.\x02\x03",
            "#00301FIt's possible there's someone\x01",
            "around who might know something.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        (
            "#11P#00006F...I agree. Let's try\x01",
            "speaking with everyone.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14ECA")

    ChrTalk(
        0x10A,
        (
            "#00600F#12PVice Chief. Can you\x01",
            "take care of this area?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14F67")

    label("loc_14ECA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14F1B")

    ChrTalk(
        0x109,
        (
            "#10101F#12PVice Chief. Can you\x01",
            "take care of this area?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14F67")

    label("loc_14F1B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14F67")

    ChrTalk(
        0x105,
        (
            "#10400F#12PVice Chief. Can you\x01",
            "take care of this area?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14F67")


    def lambda_14F6C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_14F6C)
    Sleep(100)

    def lambda_14F7C():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_14F7C)

    ChrTalk(
        0xF,
        "#5PSure. Leave it to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5P...Um, guys. Don't do\x01",
            "anything too reckless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5PIf you were done in before learning the\x01",
            "truth, you'll have gained nothing, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000F...Roger. We'll\x01",
            "keep that in mind.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    ClearChrFlags(0xF, 0x40)
    ClearChrFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x40)
    ClearChrFlags(0x10, 0x8000)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -121320, 0, 5490, 270)
    BeginChrThread(0xD, 0, 0, 0)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -123130, 0, 5700, 90)
    BeginChrThread(0xE, 0, 0, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -128710, 150, 3860, 180)
    SetChrChipByIndex(0xF, 0x1F)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -134450, 0, 3390, 270)
    BeginChrThread(0x10, 0, 0, 0)
    OP_49()
    OP_D7(0x28)
    SetChrPos(0x0, -121800, 0, 1620, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A6, 6)
    OP_29(0xB1, 0x1, 0xD)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_118_13E50 end

    def Function_119_1513A(): pass

    label("Function_119_1513A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1515E")
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(1300)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1600)
    Jump("Function_119_1513A")

    label("loc_1515E")

    Return()

    # Function_119_1513A end

    def Function_120_1515F(): pass

    label("Function_120_1515F")

    Sleep(500)

    label("loc_15162")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_15186")
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1600)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(1300)
    Jump("loc_15162")

    label("loc_15186")

    Return()

    # Function_120_1515F end

    def Function_121_15187(): pass

    label("Function_121_15187")


    def lambda_1518C():
        OP_95(0xFE, -2800, 0, 11100, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1518C)

    def lambda_151A6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_151A6)
    WaitChrThread(0xFE, 1)
    OP_68(-2000, 1000, 2850, 3500)
    MoveCamera(37, 21, 0, 3500)
    SetCameraDistance(18000, 3500)

    def lambda_151E0():
        OP_95(0xFE, -2500, 0, 4700, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_151E0)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_121_15187 end

    def Function_122_151FA(): pass

    label("Function_122_151FA")


    def lambda_151FF():
        OP_95(0xFE, -2800, 0, 11000, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_151FF)

    def lambda_15219():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_15219)
    WaitChrThread(0xFE, 1)

    def lambda_1522E():
        OP_95(0xFE, -1300, 0, 5300, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1522E)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_122_151FA end

    def Function_123_15248(): pass

    label("Function_123_15248")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x28)
    LoadChrToIndex("apl/ch51727.itc", 0x29)
    LoadChrToIndex("apl/ch50091.itc", 0x2A)
    LoadChrToIndex("apl/ch50005.itc", 0x2B)
    LoadChrToIndex("apl/ch51726.itc", 0x2C)
    SoundLoad(803)
    SoundLoad(4073)
    SoundLoad(4074)
    SoundLoad(4075)
    SoundLoad(4076)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis336.itp")
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis030.itp")
    CreatePortrait(2, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    CreatePortrait(4, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu11202.itp")
    OP_68(151770, 1100, 57250, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18550, 0)
    SetChrPos(0x101, 150700, 0, 55450, 90)
    SetChrPos(0x102, 150700, 0, 56550, 90)
    SetChrPos(0x103, 149800, 0, 54900, 90)
    SetChrPos(0x104, 149800, 0, 57100, 90)
    SetChrPos(0xF4, 148900, 0, 55450, 90)
    SetChrPos(0xF5, 148900, 0, 56550, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 163400, 0, 57000, 90)
    OP_4B(0xC, 0xFF)
    ClearChrFlags(0x3B, 0x80)
    OP_78(0x11, 0x3B)
    OP_49()
    SetChrPos(0x3B, 158000, 500, 56000, 0)
    OP_D5(0x3B, 0x0, 0x53020, 0x0, 0x0)
    SetMapObjFlags(0x11, 0x1000)
    ClearChrFlags(0x3C, 0x80)
    OP_78(0x12, 0x3C)
    OP_49()
    SetChrPos(0x3C, 158000, 500, 56000, 0)
    OP_D5(0x3C, 0x0, 0x4E20, 0x0, 0x0)
    SetMapObjFlags(0x12, 0x1000)
    StopBGM(0xFA0)
    SetCameraDistance(17800, 1500)
    FadeToBright(1000, 0)
    Sleep(800)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#5P(Ah...)\x02",
    )

    CloseMessageWindow()
    OP_68(163680, 1100, 57070, 3000)
    MoveCamera(45, 19, 0, 3000)
    SetCameraDistance(17800, 3000)
    OP_6F(0x79)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7523", 0)

    ChrTalk(
        0xC,
        (
            "#11228F#30W............\x02\x03",
            "#11226F...KeA...\x01",
            "...Father... Why...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FShizuku...!\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_155B5():

        label("loc_155B5")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_155B5")

    QueueWorkItem2(0xC, 2, lambda_155B5)
    OP_68(163400, 900, 56500, 4000)
    MoveCamera(49, 25, 0, 4000)
    SetCameraDistance(16500, 4000)
    BeginChrThread(0x101, 3, 0, 125)
    Sleep(500)
    BeginChrThread(0x102, 3, 0, 126)
    Sleep(500)
    BeginChrThread(0x104, 3, 0, 128)
    Sleep(500)
    BeginChrThread(0x103, 3, 0, 127)
    BeginChrThread(0xF4, 3, 0, 129)
    Sleep(1000)
    BeginChrThread(0xF5, 3, 0, 130)

    ChrTalk(
        0xC,
        "#11230FOh...!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x103, 3)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#12P#00109FThank goodness...\x01",
            "You're okay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00202FYou were brought to Orchis\x01",
            "Tower too, weren't you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FSince you're the daughter of that ol' man,\x01",
            "I thought you might be somewhere else...\x02\x03",
            "#00302FAnyway, I'm glad you're safe.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xC, 0x20)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xC, 0x2)
    SetChrChipByIndex(0xC, 0x2C)
    SetChrSubChip(0xC, 0x2)
    Sleep(130)
    SetChrSubChip(0xC, 0x1)
    Sleep(130)
    SetChrSubChip(0xC, 0x0)
    Sleep(130)
    SetChrSubChip(0xC, 0x1)
    Sleep(130)
    SetChrSubChip(0xC, 0x2)
    OP_CB(0x4, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x4, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    OP_CC(0x0, 0x4, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0xC,
        (
            "#30WMr. Lloyd, Mr. Randy...\x01",
            "Miss Elie and Miss Tio too...\x02\x03",
            "...I see... So that's\x01",
            "what you all look like...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x4, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x4, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    OP_CC(0x0, 0x4, 0x0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FShizuku, could it be...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00102FYou can...see?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11226F#5P...Yes.\x01",
            "Thanks to KeA.\x02\x03",
            "I think she reconnected my optic\x01",
            "nerves using some strange power...\x02\x03",
            "#11231FIt's not just light I can see...\x01",
            "I can see colors and shapes too.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_159DE")

    ChrTalk(
        0x109,
        "#10105F#5PA-Amazing...\x02",
    )

    CloseMessageWindow()
    Jump("loc_15A53")

    label("loc_159DE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15A1E")

    ChrTalk(
        0x10A,
        "#00605F#5P...What unbelievable power.\x02",
    )

    CloseMessageWindow()
    Jump("loc_15A53")

    label("loc_15A1E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15A53")

    ChrTalk(
        0x106,
        "#10712F#5PI can't believe it...\x02",
    )

    CloseMessageWindow()

    label("loc_15A53")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15AC2")

    ChrTalk(
        0x105,
        (
            "#10408F#5PCan the power of the "Sep-Terrion\x01",
            "of Zero" influence living things too...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15B46")

    label("loc_15AC2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15B0E")

    ChrTalk(
        0x106,
        "#10708F#5PThis must be one of those "miracles"...\x02",
    )

    CloseMessageWindow()
    Jump("loc_15B46")

    label("loc_15B0E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15B46")

    ChrTalk(
        0x10A,
        "#00606F#5PA true "miracle", huh...\x02",
    )

    CloseMessageWindow()

    label("loc_15B46")


    ChrTalk(
        0x104,
        (
            "#00309FWell, isn't\x01",
            "that great!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYeah...\x01",
            "Just this would be a remarkable feat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11231F#5PYes... I know that no\x01",
            "matter how much I thank\x01",
            "her, it won't be enough...\x02\x03",
            "#11233F#30W...But...\x01",
            "But... Waaah!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    SetChrSubChip(0xC, 0x3)
    Sleep(130)
    SetChrSubChip(0xC, 0x4)
    BeginChrThread(0xC, 2, 0, 124)
    Sleep(800)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#12P#00101FShizuku...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011FW-What's wrong?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xC, 2)
    SetChrSubChip(0xC, 0x9)
    Sleep(130)
    SetChrSubChip(0xC, 0xA)
    Sleep(150)

    ChrTalk(
        0xC,
        (
            "#11227F#5P#30WThough she smiled, KeA looked\x01",
            "like she was in great pain...!\x02\x03",
            "She said that was her role...\x01",
            "...That that was what she wished for, but to me \x01",
            "she looked like she was forcing herself to say that!\x02\x03",
            "#11232FEven though she really doesn't want to\x01",
            "cooperate with Mr. Dieter and the others...!\x02\x03",
            "Even though she really wants to go\x01",
            "home with Mr. Lloyd and you all...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008FAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306FI see...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0xB)
    Sleep(130)
    SetChrSubChip(0xC, 0xC)
    Sleep(150)

    ChrTalk(
        0xC,
        (
            "#11233F#5P#30WWhy is KeA doing\x01",
            "all of this...?\x02\x03",
            "And... \x01",
            "...Why is my father...\x02\x03",
            "#11234FI... I...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00208F...Shizuku...\x02",
    )

    CloseMessageWindow()
    OP_68(163420, 900, 56850, 1200)

    def lambda_15F64():
        OP_95(0xFE, 162800, 0, 57000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_15F64)
    WaitChrThread(0x102, 1)
    TurnDirection(0x102, 0xC, 500)
    Sound(812, 0, 100, 0)
    SetChrFlags(0x102, 0x20)
    SetChrFlags(0x102, 0x10)
    SetChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 0x2C)
    SetChrSubChip(0x102, 0x11)
    Sleep(100)
    SetChrSubChip(0x102, 0x12)
    Sleep(500)

    ChrTalk(
        0x102,
        (
            "#6P#00104FThank you for worrying\x01",
            "about KeA.\x02\x03",
            "#00108FAnd... It must have\x01",
            "been hard on your own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11233F#5P#30WAaah... *sob*...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00003FWe came to\x01",
            "get KeA back,\x01",
            "Shizuku.\x02\x03",
            "#00001FSo you know where she, \x01",
            "Mr. Arios and the others went?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11233F#5P#30WSorry... I don't\x01",
            "know anything...\x02\x03",
            "I haven't seen KeA\x01",
            "since yesterday...\x02\x03",
            "#11234FUmm... My father told me to\x01",
            "give you something, Mr. Lloyd...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FHuh...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_161BD")

    ChrTalk(
        0x10A,
        "#00605F#5PMacLaine has...!?\x02",
    )

    CloseMessageWindow()
    Jump("loc_16237")

    label("loc_161BD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_161F4")

    ChrTalk(
        0x109,
        "#10105F#5PF-From Mr. Arios!?\x02",
    )

    CloseMessageWindow()
    Jump("loc_16237")

    label("loc_161F4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16237")

    ChrTalk(
        0x105,
        "#10405F#5PThe "Divine Blade of Wind" has...!?\x02",
    )

    CloseMessageWindow()

    label("loc_16237")

    SetCameraDistance(16000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrPos(0x101, 158200, 0, 57400, 180)
    ClearChrFlags(0x102, 0x20)
    ClearChrFlags(0x102, 0x10)
    ClearChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x102, 158200, 0, 54600, 350)
    SetChrPos(0x103, 155800, 0, 54600, 45)
    SetChrPos(0x104, 156800, 0, 57400, 135)
    SetChrPos(0xF4, 155600, 0, 57400, 135)
    SetChrPos(0xF5, 154700, 0, 55400, 90)
    ClearChrFlags(0xC, 0x20)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xC, 0x2)
    SetChrChipByIndex(0xC, 0x6)
    SetChrSubChip(0xC, 0x0)
    SetChrPos(0xC, 159300, 0, 56400, 270)
    SetChrChipByIndex(0x3D, 0x2A)
    SetChrSubChip(0x3D, 0x1E)
    SetChrFlags(0x3D, 0x8000)
    SetChrPos(0x3D, 158350, 250, 56000, 0)
    SetChrChipByIndex(0x3A, 0x29)
    SetChrSubChip(0x3A, 0x1B)
    SetChrFlags(0x3A, 0x8000)
    SetChrFlags(0x3A, 0x2)
    SetChrFlags(0x3A, 0x10)
    SetChrFlags(0x3A, 0x20)
    SetChrPos(0x3A, 157600, 250, 55800, 0)
    SetChrChipByIndex(0x39, 0x29)
    SetChrSubChip(0x39, 0x1B)
    SetChrFlags(0x39, 0x8000)
    SetChrFlags(0x39, 0x2)
    SetChrFlags(0x39, 0x10)
    SetChrFlags(0x39, 0x20)
    SetChrPos(0x39, 157800, 300, 55800, 0)
    ClearMapObjFlags(0x11, 0x4)
    OP_68(157500, 1100, 56000, 0)
    MoveCamera(39, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(16500, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00001FThis package is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11226F#11P...My father told me to\x01",
            "give it to you, Mr. Lloyd...\x02\x03",
            "#11221FPlease, open it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FA-Alright...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xBB8)
    Fade(500)
    SetCameraDistance(16000, 300)
    Sound(898, 0, 100, 0)
    SetMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x12, 0x4)
    ClearChrFlags(0x3D, 0x80)
    ClearChrBattleFlags(0x3D, 0x8000)
    ClearChrFlags(0x39, 0x80)
    ClearChrBattleFlags(0x39, 0x8000)
    ClearChrFlags(0x3A, 0x80)
    ClearChrBattleFlags(0x3A, 0x8000)
    OP_0D()
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_164EF")
    Sleep(50)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    label("loc_164EF")

    Sleep(1000)

    ChrTalk(
        0x101,
        "#00007F#30W...These are...\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7534", 0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(800)

    AnonymousTalk(
        0x103,
        "#00208F#30WThe ones Mr. Guy used...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1661E")

    AnonymousTalk(
        0x10A,
        (
            "#00606F#30W...There's no mistake.\x01",
            "Those are his tonfas.\x02\x03",
            "#00608FThey disappeared from the scene of the\x01",
            "crime and have been missing ever since.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_1661E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16699")

    AnonymousTalk(
        0x105,
        (
            "#10405F#30WAnd these sword cuts...?\x02\x03",
            "#10401F...This means that\x01",
            "who killed Guy\x01",
            "Bannings was...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_167A2")

    label("loc_16699")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1671B")

    AnonymousTalk(
        0x109,
        (
            "#10105F#30WThese sword cuts...?\x02\x03",
            "#10101FThen it means...\x01",
            "Who killed Mr. Lloyd's\x01",
            "older brother was...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_167A2")

    label("loc_1671B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_167A2")

    AnonymousTalk(
        0x106,
        (
            "#10703F#30WThese are...sword cuts.\x02\x03",
            "#10708FThen that means\x01",
            "the one who killed Mr.\x01",
            "Lloyd's older brother was...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_167A2")

    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    ChrTalk(
        0x102,
        "#12P#00108F#30WLloyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#40W............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11233F#11P#40W...I'm sorry...\x01",
            "...I'm really sorry...\x02\x03",
            "#40WMy father... He did such a terrible thing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F──Shizuku. \x01",
            "You're not responsible for this.\x02\x03",
            "#00008FIt's not for certain \x01",
            "that Mr. Arios killed\x01",
            "my big brother...\x02\x03",
            "#00013FIt seems that there's some\x01",
            "unseen, hidden truth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11227F#11P#30WEh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301FWhat do you mean?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16B1F")

    ChrTalk(
        0x101,
        (
            "#00008FBased on these sword cuts, \x01",
            "it's likely Mr. Arios and my big \x01",
            "brother engaged in a violent battle.\x02\x03",
            "#00003FBased on the number of cuts... It would\x01",
            "seem my brother and that "Divine Blade\x01",
            "of Wind" were rather evenly matched.\x02\x03",
            "#00013F...But...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#6P#00603F──What directly caused Guy's death \x01",
            "was him being shot with a gun from behind.\x02\x03",
            "#00601FThat's what you're referring to, Bannings?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FYes.\x02",
    )

    CloseMessageWindow()
    Jump("loc_16C6C")

    label("loc_16B1F")


    ChrTalk(
        0x101,
        (
            "#00008FFrom the look of these cuts,\x01",
            "it's likely my big brother and\x01",
            "Mr. Arios had a fierce battle.\x02\x03",
            "#00003FFrom the appearance and number of cuts...\x01",
            "I think my brother put up a good fight\x01",
            "against the "Divine Blade of Wind".\x02\x03",
            "#00013F──But, what directly caused my big brother's death \x01",
            "was him being shot with a gun from behind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16C6C")


    ChrTalk(
        0x103,
        "#6P#00205FAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00105FThen...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F──Shizuku. \x01",
            "I'll read the letter too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11230F#11PA-Alright...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrFlags(0x3D, 0x80)
    SetChrBattleFlags(0x3D, 0x8000)
    SetChrChipByIndex(0x101, 0x2B)
    SetChrSubChip(0x101, 0x0)
    Sleep(500)
    Sound(18, 0, 100, 0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    Sleep(500)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, 140, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#4073V#40W──To Lloyd. Allow me to take\x01",
            "#40Wthis opportunity to return what I\x01",
            "should have given you long ago.\x02\x03",
            "#4074V#40WI have no intention of\x01",
            "explaining about the content.\x02\x03",
            "#4075V#40WFurthermore, the magic soldiers that have\x01",
            "appeared in the city are controlled by\x01",
            "the white Aion through that big bell.\x02\x03",
            "#4076V#40WIf you can do something about that white\x01",
            "Aion, they will all be silenced.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xFEC)
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(500)

    AnonymousTalk(
        0x101,
        "#00008F#30W............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        "#00108F#30W...This is...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    ChrTalk(
        0x104,
        (
            "#00303F...The white Aion... That's the\x01",
            "one we saw on the monitor, right?\x02\x03",
            "#00301FIt wiped out Garrelia Fortress\x01",
            "right off the face of the map...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00201FHowever, it should no longer be able\x01",
            "to use its spatial annihilation power.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_170B5")

    ChrTalk(
        0x10A,
        (
            "#6P#00608FBut that MacLaine... What on\x01",
            "earth could he be planning...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17175")

    label("loc_170B5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_17123")

    ChrTalk(
        0x106,
        (
            "#6P#10708FBut, the "Divine Blade of Wind"...\x01",
            "What on earth could he be planning...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17175")

    label("loc_17123")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_17175")

    ChrTalk(
        0x109,
        (
            "#6P#10108FBut, what on earth could\x01",
            "Mr. Arios be planning...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17175")

    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sleep(300)
    Fade(250)
    SetChrFlags(0x39, 0x80)
    SetChrBattleFlags(0x39, 0x8000)
    SetChrFlags(0x3A, 0x80)
    SetChrBattleFlags(0x3A, 0x8000)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x29)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sleep(300)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x3F2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x3F2, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    def lambda_17217():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_17217)

    def lambda_17224():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_17224)

    def lambda_17231():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_17231)
    OP_68(157850, 1100, 56700, 1000)
    MoveCamera(21, 21, 0, 1000)
    SetCameraDistance(16000, 1000)
    OP_6F(0x79)
    Sleep(150)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x10)
    Sound(263, 0, 70, 0)
    OP_A0(0x101, 2000, 0x8, 0x17)
    Sleep(300)

    ChrTalk(
        0x104,
        "#00302FOh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00202FMr. Lloyd...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_172FD")

    ChrTalk(
        0x105,
        (
            "#6P#10402FWow... It's like they\x01",
            "were made just for you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1738D")

    label("loc_172FD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_17348")

    ChrTalk(
        0x109,
        "#6P#10100FIt's like they were made just for you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1738D")

    label("loc_17348")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1738D")

    ChrTalk(
        0x106,
        "#6P#10702FIt seems they were made just for you.\x02",
    )

    CloseMessageWindow()

    label("loc_1738D")


    ChrTalk(
        0x101,
        (
            "#00004FYeah... It's strange how\x01",
            "familiar they feel in my hands.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x10)
    SetChrChipByIndex(0x101, 0x29)
    SetChrSubChip(0x101, 0x0)
    OP_68(157500, 1100, 56000, 1300)
    MoveCamera(39, 21, 0, 1300)
    SetCameraDistance(17500, 1300)
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sleep(150)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00004F──Shizuku. \x01",
            "Thank you for telling us.\x02\x03",
            "#00000FPlease, leave\x01",
            "the rest to us.\x02\x03",
            "Both KeA... And\x01",
            "Mr. Arios as well.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1749F():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1749F)
    Sleep(50)

    def lambda_174AF():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_174AF)
    Sleep(50)

    def lambda_174BF():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_174BF)

    def lambda_174CC():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_174CC)

    ChrTalk(
        0xC,
        (
            "#11226F#11P#30W...Okay...\x02\x03",
            "#11228FI think father has been worried\x01",
            "for a very long time...\x02\x03",
            "About mother... And me too.\x02\x03",
            "#11233FWhile overthinking various things... \x01",
            "...He's become unable to turn back...\x02\x03",
            "#11227F...And now... *sob*...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FIt's all right──\x01",
            "No way he can't\x01",
            "turn back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00104FWe'll definitely bring\x01",
            "your father back to you.\x02\x03",
            "#00100FI swear it on the name of the Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FWell, if that bad ol' man would make his cute\x01",
            "only daughter cry like this, we'll have to\x01",
            "give him a good spankin' first, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00204F...Right.\x02\x03",
            "#00202FWe will tie a rope around his neck and\x01",
            "drag him back here if we have to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11231F#11P#30W...*sob*...\x01",
            "...Please do!\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(17000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    SetChrFlags(0x3D, 0x80)
    SetChrBattleFlags(0x3D, 0x8000)
    SetChrFlags(0x39, 0x80)
    SetChrBattleFlags(0x39, 0x8000)
    OP_68(112000, 1200, -110500, 0)
    MoveCamera(40, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, 112500, 0, -110500, 270)
    SetChrPos(0x102, 112500, 0, -110500, 270)
    SetChrPos(0x103, 112500, 0, -110500, 270)
    SetChrPos(0x104, 112500, 0, -110500, 270)
    SetChrPos(0xF4, 112500, 0, -110500, 270)
    SetChrPos(0xF5, 112500, 0, -110500, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF4, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetMapObjFlags(0x12, 0x4)
    SetChrPos(0xC, 163500, 0, 57920, 90)
    OP_4C(0xC, 0xFF)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7302", 0)
    FadeToBright(1000, 0)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x1)
    OP_68(109500, 1200, -110500, 5000)
    BeginChrThread(0xF5, 3, 0, 136)
    Sleep(700)
    BeginChrThread(0xF4, 3, 0, 135)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 133)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 134)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 132)
    Sleep(700)
    BeginChrThread(0x101, 3, 0, 131)
    WaitChrThread(0x101, 3)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0xF4, 0x2)
    EndChrThread(0xF5, 0x2)
    Sound(104, 0, 100, 0)
    OP_71(0x1, 0x5, 0x0, 0x0, 0x0)
    OP_79(0x1)
    SetMapObjFlags(0x1, 0x10)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_179FD")

    ChrTalk(
        0x10A,
        (
            "#6P#00606FSetting aside the talk about\x01",
            "bringing MacLaine back...\x02\x03",
            "#00601FWhere could the President's\x01",
            "collaborators have gone off to?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17B4C")

    label("loc_179FD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_17AA7")

    ChrTalk(
        0x105,
        (
            "#6P#10406FSetting aside the talk about bringing\x01",
            "the "Divine Blade of Wind" back...\x02\x03",
            "#10401FWhere could the President's\x01",
            "collaborators have gone?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17B4C")

    label("loc_17AA7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_17B4C")

    ChrTalk(
        0x106,
        (
            "#6P#10706FSetting aside the talk about bringing\x01",
            "the "Divine Blade of Wind" back...\x02\x03",
            "#10708FWhere could the President's\x01",
            "collaborators have gone?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17B4C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_17B89")

    ChrTalk(
        0x109,
        (
            "#6P#10108FKeA's not here\x01",
            "either...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17BFC")

    label("loc_17B89")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_17BC6")

    ChrTalk(
        0x106,
        (
            "#6P#10708FKeA's not here\x01",
            "either...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17BFC")

    label("loc_17BC6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_17BFC")

    ChrTalk(
        0x105,
        (
            "#6P#10408FKeA's not here\x01",
            "either.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17BFC")


    ChrTalk(
        0x101,
        "#00006F#11PThat's true...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00108F...He left that message for us. It's possible that\x01",
            "something else has been left for us in this tow──\x02",
        )
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x28)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00005F#11POh... (I should put it\x01",
            "on speaker mode, huh.)\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    OP_24(0x323)
    Sound(804, 0, 100, 0)
    Sleep(300)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x2, 0x3)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Chief Roberts' Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ah, Lloyd, guys!\x02\x03",
            "I finally got through the express\x01",
            "elevator's security!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        "#00002FReally!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    AnonymousTalk(
        0x102,
        "#00104FThat's great. In that case...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Chief Roberts' Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "But, there's hardly anyone\x01",
            "left on the other floors.\x02\x03",
            "I'm not getting the impression\x01",
            "that they're evading my search.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    AnonymousTalk(
        0x103,
        "#00201FThen...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    AnonymousTalk(
        0x104,
        (
            "#00301FWhoa, then where the heck could\x01",
            "KeA and the others have gone?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Chief Roberts' Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Just one more thing...\x02\x03",
            "It seems there is "someone"\x01",
            "on the Orchis Tower roof.\x02\x03",
            "Together with that white doll.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(100)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        "#00013F...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1804C")
    SetMessageWindowPos(50, 30, -1, -1)

    AnonymousTalk(
        0x109,
        (
            "#10101F...Can we use the elevator\x01",
            "to get to the roof?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_180FF")

    label("loc_1804C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_180A8")
    SetMessageWindowPos(50, 30, -1, -1)

    AnonymousTalk(
        0x105,
        (
            "#10401F...Can we use the elevator\x01",
            "to get to the roof?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_180FF")

    label("loc_180A8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_180FF")
    SetMessageWindowPos(50, 30, -1, -1)

    AnonymousTalk(
        0x10A,
        (
            "#00601F...Can we use the elevator\x01",
            "to get to the roof?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_180FF")

    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Chief Roberts' Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Yeah. I've released the lock for you,\x01",
            "so you can use it right away.\x02\x03",
            "If you're going, please! Be careful!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    AnonymousTalk(
        0x103,
        "#00203FRoger.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        "#00000FExcuse us, then.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x2, 0x3)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x102,
        "#5P#00108FThat "Society"'s Doctor, or possibly...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00301FI don't know... We'll have\x01",
            "to go there to find out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203FWe should be able to get there\x01",
            "using the nearby express elevator.\x02\x03",
            "#00201FIf necessary, let's go to\x01",
            "1F to get ready for this.\x02",
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
    Sleep(300)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x101,
        "#11P#00007FRight...!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(18750, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0xC, 0x40)
    ClearChrFlags(0xC, 0x8000)
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x28)
    OP_D7(0x29)
    OP_D7(0x2A)
    OP_D7(0x2B)
    OP_D7(0x2C)
    SetChrPos(0x0, 109120, 0, -111930, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A6, 7)
    OP_29(0xB1, 0x1, 0xE)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7352", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x160), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM(-1, -1)
    ReplaceBGM("ed7151", "ed7352")
    ReplaceBGM("ed7550", "ed7352")
    OP_24(0x323)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_123_15248 end

    def Function_124_183F6(): pass

    label("Function_124_183F6")

    SetChrSubChip(0xC, 0x4)
    Sleep(130)
    SetChrSubChip(0xC, 0x5)
    Sleep(130)
    SetChrSubChip(0xC, 0x6)
    Sleep(130)
    SetChrSubChip(0xC, 0x7)
    Sleep(130)
    SetChrSubChip(0xC, 0x4)
    Sleep(300)
    SetChrSubChip(0xC, 0x5)
    Sleep(130)
    SetChrSubChip(0xC, 0x6)
    Sleep(130)
    SetChrSubChip(0xC, 0x7)
    Sleep(130)
    SetChrSubChip(0xC, 0x4)
    Sleep(500)
    SetChrSubChip(0xC, 0x5)
    Sleep(130)
    SetChrSubChip(0xC, 0x6)
    Sleep(130)
    SetChrSubChip(0xC, 0x7)
    Sleep(130)
    SetChrSubChip(0xC, 0x4)
    Sleep(300)
    SetChrSubChip(0xC, 0x5)
    Sleep(130)
    SetChrSubChip(0xC, 0x6)
    Sleep(130)
    SetChrSubChip(0xC, 0x7)
    Sleep(130)
    SetChrSubChip(0xC, 0x4)
    Return()

    # Function_124_183F6 end

    def Function_125_1846B(): pass

    label("Function_125_1846B")

    SetChrPos(0xFE, 156600, 0, 52000, 90)

    def lambda_18481():
        OP_95(0xFE, 161000, 0, 52000, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_18481)
    WaitChrThread(0xFE, 1)

    def lambda_1849F():
        OP_95(0xFE, 163300, 0, 55200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1849F)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_125_1846B end

    def Function_126_184C0(): pass

    label("Function_126_184C0")

    SetChrPos(0xFE, 156600, 0, 52000, 90)

    def lambda_184D6():
        OP_95(0xFE, 161000, 0, 52000, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_184D6)
    WaitChrThread(0xFE, 1)

    def lambda_184F4():
        OP_95(0xFE, 162000, 0, 54800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_184F4)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_126_184C0 end

    def Function_127_18515(): pass

    label("Function_127_18515")

    SetChrPos(0xFE, 156600, 0, 52000, 90)

    def lambda_1852B():
        OP_95(0xFE, 161000, 0, 52000, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1852B)
    WaitChrThread(0xFE, 1)

    def lambda_18549():
        OP_95(0xFE, 162000, 0, 53600, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_18549)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_127_18515 end

    def Function_128_1856A(): pass

    label("Function_128_1856A")

    SetChrPos(0xFE, 156600, 0, 52000, 90)

    def lambda_18580():
        OP_95(0xFE, 161000, 0, 52000, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_18580)
    WaitChrThread(0xFE, 1)

    def lambda_1859E():
        OP_95(0xFE, 163300, 0, 54000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1859E)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_128_1856A end

    def Function_129_185BF(): pass

    label("Function_129_185BF")

    SetChrPos(0xFE, 154000, 0, 60000, 90)

    def lambda_185D5():
        OP_95(0xFE, 161300, 0, 60000, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_185D5)
    WaitChrThread(0xFE, 1)

    def lambda_185F3():
        OP_95(0xFE, 161700, 0, 58130, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_185F3)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x87, 0x1F4)
    Return()

    # Function_129_185BF end

    def Function_130_18614(): pass

    label("Function_130_18614")

    SetChrPos(0xFE, 154000, 0, 60000, 90)

    def lambda_1862A():
        OP_95(0xFE, 161300, 0, 60000, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1862A)
    WaitChrThread(0xFE, 1)

    def lambda_18648():
        OP_95(0xFE, 163100, 0, 58800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_18648)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_130_18614 end

    def Function_131_18669(): pass

    label("Function_131_18669")


    def lambda_1866E():
        OP_95(0xFE, 110200, 0, -110500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1866E)

    def lambda_18688():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_18688)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_131_18669 end

    def Function_132_18699(): pass

    label("Function_132_18699")


    def lambda_1869E():
        OP_95(0xFE, 110000, 0, -110500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1869E)

    def lambda_186B8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_186B8)
    WaitChrThread(0xFE, 1)

    def lambda_186CD():
        OP_95(0xFE, 109600, 0, -109200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_186CD)
    WaitChrThread(0xFE, 1)

    def lambda_186EB():

        label("loc_186EB")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_186EB")

    QueueWorkItem2(0xFE, 2, lambda_186EB)
    Return()

    # Function_132_18699 end

    def Function_133_186F9(): pass

    label("Function_133_186F9")


    def lambda_186FE():
        OP_95(0xFE, 110000, 0, -110500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_186FE)

    def lambda_18718():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_18718)
    WaitChrThread(0xFE, 1)

    def lambda_1872D():
        OP_95(0xFE, 108600, 0, -111500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1872D)
    WaitChrThread(0xFE, 1)

    def lambda_1874B():

        label("loc_1874B")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_1874B")

    QueueWorkItem2(0xFE, 2, lambda_1874B)
    Return()

    # Function_133_186F9 end

    def Function_134_18759(): pass

    label("Function_134_18759")


    def lambda_1875E():
        OP_95(0xFE, 110000, 0, -110500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1875E)

    def lambda_18778():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_18778)
    WaitChrThread(0xFE, 1)

    def lambda_1878D():
        OP_95(0xFE, 109600, 0, -112200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1878D)
    WaitChrThread(0xFE, 1)

    def lambda_187AB():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_187AB)
    Return()

    # Function_134_18759 end

    def Function_135_187B4(): pass

    label("Function_135_187B4")


    def lambda_187B9():
        OP_95(0xFE, 110000, 0, -110500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_187B9)

    def lambda_187D3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_187D3)
    WaitChrThread(0xFE, 1)

    def lambda_187E8():
        OP_95(0xFE, 108000, 0, -109800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_187E8)
    WaitChrThread(0xFE, 1)

    def lambda_18806():

        label("loc_18806")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_18806")

    QueueWorkItem2(0xFE, 2, lambda_18806)
    Return()

    # Function_135_187B4 end

    def Function_136_18814(): pass

    label("Function_136_18814")


    def lambda_18819():
        OP_95(0xFE, 110000, 0, -110500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_18819)

    def lambda_18833():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_18833)
    WaitChrThread(0xFE, 1)

    def lambda_18848():
        OP_95(0xFE, 107500, 0, -111300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_18848)
    WaitChrThread(0xFE, 1)

    def lambda_18866():

        label("loc_18866")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_18866")

    QueueWorkItem2(0xFE, 2, lambda_18866)
    Return()

    # Function_136_18814 end

    def Function_137_18874(): pass

    label("Function_137_18874")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18A84")
    EventBegin(0x0)
    Fade(500)
    OP_68(74590, 1500, -850, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 70580, 0, -490, 90)
    SetChrPos(0x102, 70580, 0, -1690, 90)
    SetChrPos(0x103, 70600, 0, 720, 90)
    SetChrPos(0x104, 69600, 0, -500, 90)
    SetChrPos(0x109, 69570, 0, -2070, 90)
    SetChrPos(0x105, 69670, 0, 740, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    ChrTalk(
        0x101,
        "#00013FI knew it―\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FAll three are\x01",
            "shut down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201FBecause control of the building\x01",
            "has been taken over, I don't think\x01",
            "we can use the elevators.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FThen, if we can't get\x01",
            "the shutters open,\x01",
            "we can't do anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10107FYes. Let's hurry to the emergency stairs!\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, 109910, 0, -130740, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x1C2, 5)
    EventEnd(0x5)
    Jump("loc_18AE8")

    label("loc_18A84")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00007FWe can't use the elevators...\x01",
            "Let's hurry to the emergency stairs!\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 109910, 0, -130740, 270)
    EventEnd(0x4)

    label("loc_18AE8")

    Return()

    # Function_137_18874 end

    def Function_138_18AE9(): pass

    label("Function_138_18AE9")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_18B4E")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The elevator is heading to\x01",
            "another floor and shows\x01",
            "no sign of stopping.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_18E6F")

    label("loc_18B4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18DFD")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The elevator's shutter\x01",
            "is firmly shut.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00000FThat's right. During the conference,\x01",
            "we can't use any elevators except\x01",
            "the ones in the front, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes. It must be that way\x01",
            "for security reasons.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 3)), scpexpr(EXPR_END)), "loc_18D17")

    ChrTalk(
        0x103,
        (
            "#00200FThe same as the emergency\x01",
            "stairs, it seems these too are\x01",
            "controlled via the orbal net.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, seems that way.\x02\x03",
            "Well, whatever. When we need to move,\x01",
            "let's use the elevators in the front.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18DF5")

    label("loc_18D17")


    ChrTalk(
        0x103,
        (
            "#00200FBy the way, it seems the\x01",
            "lock mechanism is controlled\x01",
            "via the orbal network.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, that's Orchis\x01",
            "Tower security for you.\x02\x03",
            "Well, whatever. When we need to move,\x01",
            "let's use the elevators in the front.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18DF5")

    SetScenarioFlags(0x1C2, 2)
    Jump("loc_18E6F")

    label("loc_18DFD")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The elevator's shutter\x01",
            "is firmly shut.\x02\x03",
            "It seems you can't use this elevator\x01",
            "during the conference.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_18E6F")

    TalkEnd(0xFF)
    Return()

    # Function_138_18AE9 end

    def Function_139_18E73(): pass

    label("Function_139_18E73")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_190F6")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The emergency stairs' shutter\x01",
            "is firmly shut.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00000F37F is this way.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes. They said it would be sealed\x01",
            "for the duration of the conference.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 2)), scpexpr(EXPR_END)), "loc_1901E")

    ChrTalk(
        0x103,
        (
            "#00200FThe same as the elevator, \x01",
            "it seems these too are\x01",
            "controlled via the orbal net...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThere's no such thing as perfect\x01",
            "security― I remember hearing that.\x02\x03",
            "Let's think about possible\x01",
            "situations, just in case.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_190EE")

    label("loc_1901E")


    ChrTalk(
        0x103,
        (
            "#00200FIt seems the shutter\x01",
            "lock is controlled\x01",
            "via the orbal net...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThere's no such thing as perfect\x01",
            "security― I remember hearing that.\x02\x03",
            "Let's think about possible\x01",
            "situations, just in case.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_190EE")

    SetScenarioFlags(0x1C2, 3)
    Jump("loc_19177")

    label("loc_190F6")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The emergency stairs'\x01",
            "shutter is firmly shut.\x02\x03",
            "It seems you can't proceed to the next\x01",
            "floor during the conference.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_19177")

    TalkEnd(0xFF)
    Return()

    # Function_139_18E73 end

    def Function_140_1917B(): pass

    label("Function_140_1917B")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001FWhoops, the President's in the\x01",
            "innermost room in the left wing.\x02\x03",
            "Before visiting the Chancellor,\x01",
            "let's first pay a visit to the President.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 4370, 0, -1430, 270)
    EventEnd(0x4)
    Return()

    # Function_140_1917B end

    SaveToFile()

Try(main)
