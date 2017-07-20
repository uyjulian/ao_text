from ScenarioHelper import *

def main():
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
        "Receptionist Lanfi",         # 1
        "Receptionist Colinna",         # 2
        "Security guards",           # 3
        "Security guard wong",         # 4
        "Suzuku",                 # 5
        "Mollet chief",           # 6
        "Receptionist Reirier",         # 7
        "Pierre deputy director",         # 8
        "Researcher David",         # 9
        "Policeman",                   # 10
        "Policeman",                   # 11
        "Claudia Hime",         # 12
        "Lector clerk",         # 13
        "Republican officer",           # 14
        "Imperial army officer",             # 15
        "President Lock Smith",     # 16
        "Assistant Julia",             # 17
        "Major Muller",           # 18
        "Prince Albert",         # 19
        "Public guard",             # 20
        "Butler",                   # 21
        "Butler",                   # 22
        "A maid",                 # 23
        "A maid",                 # 24
        "A maid",                 # 25
        "A maid",                 # 26
        "A maid",                 # 27
        "A maid",                 # 28
        "A maid",                 # 29
        "City official staff",             # 30
        "City official staff",             # 31
        "Policeman",                   # 32
        "Policeman",                   # 33
        "Royal Friendly Corps Corps",         # 34
        "Sieg",                 # 35
        "Mayor of Dieter",         # 36
        "Prince Oliver",       # 37
        "McDowell",         # 38
        "Dudley investigator",         # 39
        "Prime Minister Osborne",         # 40
        "Representative",                   # 41
        "Representative",                   # 42
        "Representative",                   # 43
        "Keya",                 # 44
        "Secretary Arios",           # 45
        "dummy",                 # 46
        "Ian lawyer",           # 47
        "Chair",                   # 48
        "Chair",                   # 49
        "Tonfa",             # 50
        "Tonfa",             # 51
        "Tonfa OBJ",          # 52
        "Wrapping cloth",                 # 53
        "letter",                   # 54
        "laptop",         # 55
        "Defense Forces soldier · man",         # 56
        "Defense Forces soldier · man",         # 57
        "Defense Forces soldier · man",         # 58
        "Defense Forces soldier · man",         # 59
        "SE control",                 # 60
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
        "Function_6_18DE",         # 06, 6
        "Function_7_18FC",         # 07, 7
        "Function_8_1DB1",         # 08, 8
        "Function_9_2073",         # 09, 9
        "Function_10_2245",        # 0A, 10
        "Function_11_2A94",        # 0B, 11
        "Function_12_2B4A",        # 0C, 12
        "Function_13_2EA8",        # 0D, 13
        "Function_14_3336",        # 0E, 14
        "Function_15_34C9",        # 0F, 15
        "Function_16_3754",        # 10, 16
        "Function_17_38AA",        # 11, 17
        "Function_18_3961",        # 12, 18
        "Function_19_4647",        # 13, 19
        "Function_20_46EA",        # 14, 20
        "Function_21_4776",        # 15, 21
        "Function_22_4F4F",        # 16, 22
        "Function_23_51D1",        # 17, 23
        "Function_24_5409",        # 18, 24
        "Function_25_54B9",        # 19, 25
        "Function_26_5575",        # 1A, 26
        "Function_27_56B6",        # 1B, 27
        "Function_28_5926",        # 1C, 28
        "Function_29_5A1B",        # 1D, 29
        "Function_30_5B83",        # 1E, 30
        "Function_31_5D0B",        # 1F, 31
        "Function_32_5E2B",        # 20, 32
        "Function_33_5EB7",        # 21, 33
        "Function_34_5FA5",        # 22, 34
        "Function_35_63E0",        # 23, 35
        "Function_36_64FA",        # 24, 36
        "Function_37_6504",        # 25, 37
        "Function_38_6FD3",        # 26, 38
        "Function_39_6FDD",        # 27, 39
        "Function_40_70D5",        # 28, 40
        "Function_41_723B",        # 29, 41
        "Function_42_72D9",        # 2A, 42
        "Function_43_751D",        # 2B, 43
        "Function_44_766B",        # 2C, 44
        "Function_45_77C4",        # 2D, 45
        "Function_46_7866",        # 2E, 46
        "Function_47_799C",        # 2F, 47
        "Function_48_7ABB",        # 30, 48
        "Function_49_7C03",        # 31, 49
        "Function_50_8144",        # 32, 50
        "Function_51_91D0",        # 33, 51
        "Function_52_9D99",        # 34, 52
        "Function_53_9DA0",        # 35, 53
        "Function_54_9DC9",        # 36, 54
        "Function_55_ADA5",        # 37, 55
        "Function_56_AE24",        # 38, 56
        "Function_57_AE79",        # 39, 57
        "Function_58_AECE",        # 3A, 58
        "Function_59_AF23",        # 3B, 59
        "Function_60_AF78",        # 3C, 60
        "Function_61_AFCD",        # 3D, 61
        "Function_62_B022",        # 3E, 62
        "Function_63_B077",        # 3F, 63
        "Function_64_B11C",        # 40, 64
        "Function_65_B18E",        # 41, 65
        "Function_66_B212",        # 42, 66
        "Function_67_B282",        # 43, 67
        "Function_68_B306",        # 44, 68
        "Function_69_B376",        # 45, 69
        "Function_70_B3FA",        # 46, 70
        "Function_71_B46A",        # 47, 71
        "Function_72_B4A7",        # 48, 72
        "Function_73_B4F8",        # 49, 73
        "Function_74_B535",        # 4A, 74
        "Function_75_B590",        # 4B, 75
        "Function_76_B602",        # 4C, 76
        "Function_77_B67E",        # 4D, 77
        "Function_78_B6F0",        # 4E, 78
        "Function_79_B76C",        # 4F, 79
        "Function_80_B7E1",        # 50, 80
        "Function_81_C1D2",        # 51, 81
        "Function_82_C46A",        # 52, 82
        "Function_83_C702",        # 53, 83
        "Function_84_CA0E",        # 54, 84
        "Function_85_CA5F",        # 55, 85
        "Function_86_D1C0",        # 56, 86
        "Function_87_D215",        # 57, 87
        "Function_88_D275",        # 58, 88
        "Function_89_D2D5",        # 59, 89
        "Function_90_D335",        # 5A, 90
        "Function_91_D395",        # 5B, 91
        "Function_92_D3F5",        # 5C, 92
        "Function_93_D504",        # 5D, 93
        "Function_94_F8ED",        # 5E, 94
        "Function_95_F93E",        # 5F, 95
        "Function_96_F993",        # 60, 96
        "Function_97_F9E8",        # 61, 97
        "Function_98_FA3D",        # 62, 98
        "Function_99_FA92",        # 63, 99
        "Function_100_FAE7",       # 64, 100
        "Function_101_FB3C",       # 65, 101
        "Function_102_FB91",       # 66, 102
        "Function_103_FBF1",       # 67, 103
        "Function_104_FC51",       # 68, 104
        "Function_105_FCB1",       # 69, 105
        "Function_106_FD11",       # 6A, 106
        "Function_107_FD71",       # 6B, 107
        "Function_108_10BBD",      # 6C, 108
        "Function_109_10BDC",      # 6D, 109
        "Function_110_11528",      # 6E, 110
        "Function_111_11813",      # 6F, 111
        "Function_112_11E58",      # 70, 112
        "Function_113_11ED1",      # 71, 113
        "Function_114_11EEC",      # 72, 114
        "Function_115_11EFF",      # 73, 115
        "Function_116_124AD",      # 74, 116
        "Function_117_127D4",      # 75, 117
        "Function_118_12C2B",      # 76, 118
        "Function_119_13D21",      # 77, 119
        "Function_120_13D46",      # 78, 120
        "Function_121_13D6E",      # 79, 121
        "Function_122_13DE1",      # 7A, 122
        "Function_123_13E2F",      # 7B, 123
        "Function_124_16D89",      # 7C, 124
        "Function_125_16DFE",      # 7D, 125
        "Function_126_16E53",      # 7E, 126
        "Function_127_16EA8",      # 7F, 127
        "Function_128_16EFD",      # 80, 128
        "Function_129_16F52",      # 81, 129
        "Function_130_16FA7",      # 82, 130
        "Function_131_16FFC",      # 83, 131
        "Function_132_1702C",      # 84, 132
        "Function_133_1708C",      # 85, 133
        "Function_134_170EC",      # 86, 134
        "Function_135_17147",      # 87, 135
        "Function_136_171A7",      # 88, 136
        "Function_137_17207",      # 89, 137
        "Function_138_1746A",      # 8A, 138
        "Function_139_177A3",      # 8B, 139
        "Function_140_17A38",      # 8C, 140
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
            "Everyone, thanks for today.\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "President His Excellency also\x01",
            "I am very pleased.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_1860 end

    def Function_6_18DE(): pass

    label("Function_6_18DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18F5")
    Call(0, 93)
    Return()

    label("loc_18F5")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_6_18DE end

    def Function_7_18FC(): pass

    label("Function_7_18FC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1AAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_191E")
    TalkEnd(0xFE)
    Call(0, 49)
    Return()

    label("loc_191E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A0B")

    ChrTalk(
        0xFE,
        (
            "Croix,\x01",
            "Until the current situation is settled\x01",
            "I will be detained here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He has many sins\x01",
            "It will be imposed … …\x01",
            "I can not be blamed too strongly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Whatever the way, he will crossbell\x01",
            "It is a fact that I tried to protect … …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1AA8")

    label("loc_1A0B")


    ChrTalk(
        0xFE,
        (
            "To Croix suspect\x01",
            "Many crimes will be imposed … …\x01",
            "I can not be blamed too strongly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Whatever the way, he will crossbell\x01",
            "It is a fact that I tried to protect … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AA8")

    Jump("loc_1DAD")

    label("loc_1AAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_1B2D")

    ChrTalk(
        0xFE,
        (
            "Damn, to the terrorists\x01",
            "I do not believe that you will be so far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If the guard is moving,\x01",
            "I wish I could manage somehow ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DAD")

    label("loc_1B2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_1C67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BFE")

    ChrTalk(
        0xFE,
        (
            "Ha, Yuria Assoc.\x01",
            "If such a person is in his / her boss,\x01",
            "Every day of my life is enriching … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What is it?\x01",
            "What on earth are you thinking about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tense feeling at all\x01",
            "Proof that is not enough.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1C62")

    label("loc_1BFE")


    ChrTalk(
        0xFE,
        (
            "I can still be optimistic\x01",
            "I am not in the situation, but what ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tense feeling at all\x01",
            "Proof that is not enough.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C62")

    Jump("loc_1DAD")

    label("loc_1C67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_1DAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D31")

    ChrTalk(
        0xFE,
        (
            "Well, but in this corridor room\x01",
            "Looking is exactly spectacular.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I look at the distance, it is like\x01",
            "It seems that he is taking a walk in the air … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What is it?\x01",
            "I feel more tense.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1DAD")

    label("loc_1D31")


    ChrTalk(
        0xFE,
        (
            "When I am here,\x01",
            "I will take my eyes off the scenery, but …\x01",
            "I feel more tense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "The idea is hundreds of dollars, without a favor.\x02",
    )

    CloseMessageWindow()

    label("loc_1DAD")

    TalkEnd(0xFE)
    Return()

    # Function_7_18FC end

    def Function_8_1DB1(): pass

    label("Function_8_1DB1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1DFA")

    ChrTalk(
        0xFE,
        "There is no abnormality!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Continue to patrol!\x02",
    )

    CloseMessageWindow()
    Jump("loc_206F")

    label("loc_1DFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_1E78")

    ChrTalk(
        0xFE,
        (
            "Apparently now, the elevator also\x01",
            "You seem to be unable to use stairs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This divided situation\x01",
            "I have to manage something quickly ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_206F")

    label("loc_1E78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_2013")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F8F")

    ChrTalk(
        0xFE,
        (
            "He is an empire's army\x01",
            "Did you say Major Muller … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Then, Assistant Yulia\x01",
            "Captain of the kingdom army · royal guards … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Two people with such titles\x01",
            "It is a rare scene with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It sounds like a close friend … …\x01",
            "What on earth is it related to?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_200E")

    label("loc_1F8F")


    ChrTalk(
        0xFE,
        (
            "As I was watching the situation,\x01",
            "Like a close friends\x01",
            "Can you see it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The two were united,\x01",
            "What kind of relationship is it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_200E")

    Jump("loc_206F")

    label("loc_2013")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_206F")

    ChrTalk(
        0xFE,
        "At last the main conference started.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This tension …\x01",
            "I will tighten my body and mind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_206F")

    TalkEnd(0xFE)
    Return()

    # Function_8_1DB1 end

    def Function_9_2073(): pass

    label("Function_9_2073")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2088")
    Call(0, 10)
    Jump("loc_2241")

    label("loc_2088")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21BD")

    ChrTalk(
        0x18,
        (
            "#07108FBy the way.\x01",
            "Your Highness will return from the stairs\x01",
            "It seems that it was done … …\x02\x03",
            "#07103FHmm, but your current Prince\x01",
            "My heart is disturbed when I meet someone.\x01",
            "There is nothing like that.\x02\x03",
            "…… Unnecessary worry is useless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F(… … about Lecter\x01",
            "Are you saying that? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302F(Huh, I guess there are plenty of things.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_2241")

    label("loc_21BD")


    ChrTalk(
        0x18,
        (
            "#07103FWhat you found out in the process of vigilance\x01",
            "Please contact if you have one.\x02\x03",
            "#07100FEven here, if you know something\x01",
            "I will inform the headquarters immediately.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2241")

    TalkEnd(0xFE)
    Return()

    # Function_9_2073 end

    def Function_10_2245(): pass

    label("Function_10_2245")

    OP_4B(0x19, 0xFF)
    OP_4B(0x18, 0xFF)
    TurnDirection(0x19, 0x0, 500)

    ChrTalk(
        0x19,
        "#07300FHmm, you guys.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x18, 0x0, 500)

    ChrTalk(
        0x18,
        "#07100FIt looks like the situation will not change?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FWell, for the time being.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FFor 2 people\x01",
            "Do you have any information?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#07103FNo, unfortunately\x01",
            "It is a situation not to say this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#07303FEven in the direction of the empire\x01",
            "I am doing my best.\x02\x03",
            "#07301FAristocrats and good innovators and good,\x01",
            "Apparently it will let me grab the tail\x01",
            "I do not feel like being exposed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10108FIs that right..\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FTwo major factions of the empire …\x01",
            "Unexpectedly\x01",
            "It sounds like a nasty opponent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F….\x02\x03",
            "#00108FUm, Oliver's Prince yesterday,\x01",
            "You mentioned as \"the third way\" is not it?\x02\x03",
            "I had been worried for a long time … ….\x02\x03",
            "#00101FIf it is good, give a little story\x01",
            "Could you please tell me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FErie …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#07302FHmm, there is no reason to be in doubt.\x02\x03",
            "#07304FOriginally I am relieved\x01",
            "It's not something we can talk about ……\x01",
            "Do you mind if it is you guys.\x02\x03",
            "#07300FIn a word - he is\x01",
            "I'm trying to get rid of the \"wall\".\x02",
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
        "#00001FGet rid of the \"wall\" … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#07303FThe point is, it exists between innovation and aristocracy\x01",
            "It's like a cognitive barrier.\x02\x03",
            "#07300FTo put it even more,\x01",
            "It is a tremendous way to harmonize.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FHarmonize innovators and aristocrats … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHuh, that is it.\x01",
            "To say horribly difficult,\x01",
            "Is not it nearly idealism?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101FWa, you -\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#07302FGiggle\x01",
            "No, you are exactly as you say.\x02\x03",
            "#07304FBut he is\x01",
            "In that tremendous way \"monster\" and\x01",
            "It seems he decided to confront.\x02\x03",
            "It is a whim of the prince of ordinary\x01",
            "Hobby It is a remarkable popular person\x01",
            "On your own preparedness to whisper in the shade.\x02\x03",
            "#07302FAnd I, too\x01",
            "I have decided to go out with each other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FI see, I see … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#07104FMajor Muller ……\x01",
            "As Rosemary Claudia once again said\x01",
            "The Kingdom of Libert is the friend of the Princesses.\x02\x03",
            "#07102FDirect intervention is impossible, but …\x01",
            "When something happens, I will spare no help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        "#07304FHmm, it is a painful thing to keep up with.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FAgain,\x01",
            "Is he the man of virtue of Prince child?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#07304FHuhu, that guy\x01",
            "It is a word that matches it\x01",
            "Maybe it is such a thing.\x02\x03",
            "#07308FAnyway, now I will hold this trade meeting\x01",
            "Successful completion -\x01",
            "That is the biggest mission and purpose.\x02\x03",
            "#07300FMissions of the Special Affairs Division … …\x01",
            "I'm expecting your activity as well.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x19, 0x0, 0x0)
    OP_93(0x18, 0x0, 0x0)
    OP_4C(0x19, 0xFF)
    OP_4C(0x18, 0xFF)
    SetScenarioFlags(0x1C3, 5)
    Return()

    # Function_10_2245 end

    def Function_11_2A94(): pass

    label("Function_11_2A94")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AA9")
    Call(0, 10)
    Jump("loc_2B46")

    label("loc_2AA9")


    ChrTalk(
        0x19,
        (
            "#07303FAnyway, now I will hold this trade meeting\x01",
            "Successful completion -\x01",
            "That is the biggest mission and purpose.\x02\x03",
            "#07300FMissions of the Special Affairs Division … …\x01",
            "I'm expecting your activity as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B46")

    TalkEnd(0xFE)
    Return()

    # Function_11_2A94 end

    def Function_12_2B4A(): pass

    label("Function_12_2B4A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2BF2")

    ChrTalk(
        0xFE,
        (
            "You can go from the emergency staircase\x01",
            "The central floor below 30 F,\x01",
            "We have not secured safety yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you plan to go,\x01",
            "Please be careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EA4")

    label("loc_2BF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_2D11")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CA3")

    ChrTalk(
        0xFE,
        (
            "Mi, everyone,\x01",
            "It became a serious thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tentatively, we are the place to hold\x01",
            "I will try to defend this floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Let's tighten each other carefully!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2D0C")

    label("loc_2CA3")


    ChrTalk(
        0xFE,
        (
            "Tentatively, we are the place to hold\x01",
            "I will try to defend this floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Let's tighten each other carefully!\x02",
    )

    CloseMessageWindow()

    label("loc_2D0C")

    Jump("loc_2EA4")

    label("loc_2D11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_2DB5")

    ChrTalk(
        0xFE,
        (
            "Well, what is it after all?\x01",
            "Everyone at the VIP\x01",
            "You do not have a damper.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter how many times,\x01",
            "Every time you go through here\x01",
            "I will inadvertently shrink.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EA4")

    label("loc_2DB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_2EA4")

    ChrTalk(
        0xFE,
        (
            "Here is the right wing of the VIP floor\x01",
            "The nearest is the room of the mayor and the chairman,\x01",
            "Then Oliver's Prince ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At the end the corner room at the back\x01",
            "Osborne's Prime Minister's Office\x01",
            "It has become a room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the way, now\x01",
            "Because it is time for room make-up,\x01",
            "You can enter inside.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EA4")

    TalkEnd(0xFE)
    Return()

    # Function_12_2B4A end

    def Function_13_2EA8(): pass

    label("Function_13_2EA8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_2F54")

    ChrTalk(
        0xFE,
        (
            "Tentatively, the staff who were on the left wing\x01",
            "I gathered in this room!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now I only have to wait for headquarters instructions\x01",
            "It is regrettable that I can not do it ….\x01",
            "Anyway I do not feel guilty!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3332")

    label("loc_2F54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_3131")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3068")

    ChrTalk(
        0xFE,
        (
            "Just right now, Prince Claudia\x01",
            "I saw you ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The VIPs of each country are repeated many times a day\x01",
            "It is too close to seeing,\x01",
            "It is unlikely that there will be unusual circumstances.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well anyway, today's day\x01",
            "As if it would become a blemish of a lifetime\x01",
            "I hope that you will not feel at ease.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_312C")

    label("loc_3068")


    ChrTalk(
        0xFE,
        (
            "The VIPs of each country are repeated many times a day\x01",
            "It is also seen soon … …\x01",
            "It's a story like never again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well anyway, today's day\x01",
            "As if it would become a blemish of a lifetime\x01",
            "I hope that you will not feel at ease.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_312C")

    Jump("loc_3332")

    label("loc_3131")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_3332")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32BC")

    ChrTalk(
        0xFE,
        (
            "The left side of the VIP floor is from the front\x01",
            "Remiferia, Libert,\x01",
            "It is a room of the summit of Calvado.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the way, security at the VIP floor,\x01",
            "In consideration of each country\x01",
            "We are turning with the minimum number of people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, as long as you invite the top leaders of the country,\x01",
            "Minimal confidentiality even in this situation\x01",
            "Of course it will be necessary … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For the time being, during the break the leaders\x01",
            "Because escorts are attached to each,\x01",
            "Safety is judged to be a problem pear.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3332")

    label("loc_32BC")


    ChrTalk(
        0xFE,
        (
            "After a break time,\x01",
            "To go in and out freely around here\x01",
            "It will be difficult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "If you check the room you are inside now.\x02",
    )

    CloseMessageWindow()

    label("loc_3332")

    TalkEnd(0xFE)
    Return()

    # Function_13_2EA8 end

    def Function_14_3336(): pass

    label("Function_14_3336")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3428")

    ChrTalk(
        0xFE,
        (
            "This room is for Remyria\x01",
            "I will use it by the Grand Duke of Albert\x01",
            "We are scheduled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So, whatever the priest\x01",
            "He seems to be well versed in music.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mr. MacDael now is the best\x01",
            "Records collection\x01",
            "I am preparing for it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_34C5")

    label("loc_3428")


    ChrTalk(
        0xFE,
        (
            "McDowell and Albert Daimo\x01",
            "It seems like a good relationship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Remiferia is at Ursula Hospital\x01",
            "It is famous as a sponsor,\x01",
            "I do not know why.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34C5")

    TalkEnd(0xFE)
    Return()

    # Function_14_3336 end

    def Function_15_34C9(): pass

    label("Function_15_34C9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_34DA")
    Jump("loc_3750")

    label("loc_34DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3644")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35D5")

    ChrTalk(
        0xFE,
        (
            "Although it has been only one night since martial law,\x01",
            "The tiredness of everyone inside the tower\x01",
            "It has already peaked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I do not know what's going on ……\x01",
            "It seems that there is still quite a bit of anxiety.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As soon as this situation\x01",
            "I hope to converge … …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_363F")

    label("loc_35D5")


    ChrTalk(
        0xFE,
        (
            "The tiredness of everyone inside the tower\x01",
            "It has already peaked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As soon as this situation\x01",
            "I hope to converge … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_363F")

    Jump("loc_3750")

    label("loc_3644")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_3750")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36F5")

    ChrTalk(
        0xFE,
        (
            "Tiny chirocaro ……\x01",
            "To the extent that the whole is lightly damp.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yeah, this is perfect for potted plants.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After that, dust again\x01",
            "Make sure that it does not fall, and …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_3750")

    label("loc_36F5")


    ChrTalk(
        0xFE,
        "Potted people are perfect with this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After that, dust again\x01",
            "Make sure that it does not fall, and …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3750")

    TalkEnd(0xFE)
    Return()

    # Function_15_34C9 end

    def Function_16_3754(): pass

    label("Function_16_3754")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3824")

    ChrTalk(
        0xFE,
        (
            "This is Alcato's Excellency\x01",
            "It becomes a room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mr. MacDaely is now\x01",
            "I am on a visit, but about you\x01",
            "I've been asking you to do so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "If you want, please come in.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_38A6")

    label("loc_3824")


    ChrTalk(
        0xFE,
        (
            "Mr. MacDaely is now\x01",
            "I am on a visit, but about you\x01",
            "I have asked you to do the work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "If you want, please come in.\x02",
    )

    CloseMessageWindow()

    label("loc_38A6")

    TalkEnd(0xFE)
    Return()

    # Function_16_3754 end

    def Function_17_38AA(): pass

    label("Function_17_38AA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38BF")
    Call(0, 18)
    Jump("loc_3959")

    label("loc_38BF")


    ChrTalk(
        0xFE,
        (
            "Hmm, after all the second half of the meeting\x01",
            "More cared\x01",
            "The situation seems to be waiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Especially made from two major countries\x01",
            "As for security proposals\x01",
            "I have to be more vigilant.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3959")

    TalkEnd(0xFE)
    SetChrSubChip(0x1A, 0x2)
    Return()

    # Function_17_38AA end

    def Function_18_3961(): pass

    label("Function_18_3961")

    SetChrSubChip(0x1A, 0x2)
    SetChrSubChip(0x2D, 0x1)

    ChrTalk(
        0x1A,
        (
            "Even though discussions have been settled\x01",
            "Leading the leaders of the two major powers to falling water\x01",
            "I am tired of making it the other party.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#02509FHuhu, but also Grand Duke\x01",
            "More and more dignity has been increased.\x02\x03",
            "The predecessor will be pleased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "… … It is almost five years since I succeeded the mark.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Recently the domestic regime also\x01",
            "Although it has been prepared,\x01",
            "Actually, I have a lot more to do.\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3B39")
    Jump("loc_3B83")

    label("loc_3B39")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3B59")
    OP_52(0x1A, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3B83")

    label("loc_3B59")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3B79")
    OP_52(0x1A, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3B83")

    label("loc_3B79")

    OP_52(0x1A, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3B83")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2D, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x2D, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x2D, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x2D, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3C3C")
    Jump("loc_3C86")

    label("loc_3C3C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2D, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3C5C")
    OP_52(0x2D, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3C86")

    label("loc_3C5C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2D, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C7C")
    OP_52(0x2D, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3C86")

    label("loc_3C7C")

    OP_52(0x2D, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x2D, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3C86")

    OP_52(0x2D, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2D, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x2D, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3E03")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3CFB")

    ChrTalk(
        0x1A,
        (
            "Oh, you guys ……\x01",
            "I was taken care of yesterday.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D13")

    label("loc_3CFB")


    ChrTalk(
        0x1A,
        "Oh, you guys ……\x02",
    )

    CloseMessageWindow()

    label("loc_3D13")


    ChrTalk(
        0x2D,
        "#02505FOh, are not you of the support department?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FThank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Hmm, I heard the story but you guys\x01",
            "I am thankful to participate in security.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Before Mr. MacDaely's crisis\x01",
            "I heard that I had saved it,\x01",
            "I am truly reliable.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41E5")

    label("loc_3E03")


    ChrTalk(
        0x1A,
        "Oh, you guys ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        "#02500FOh, are not you of the support department?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FThank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Hmm, are you the Special Affairs Division?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Nice to meet you, my first success\x01",
            "I heard from Arios.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005FWith Arios\x01",
            "Do you know each other?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Oh, I have been from before\x01",
            "Please be patient with the Association.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Especially with Arios\x01",
            "Personal friendship is also deep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FI see … … is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "And Ellie, it's been a long time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Apparently you are also at the Special Affairs Support Division\x01",
            "You seem to be showing remarkable success.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FHouse……\x01",
            "But, thank you.\x02\x03",
            "#00102FYour honorable partner seems to be fine and what is more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105F(Erie-san … … with Prince Duke\x01",
            "You knew that. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F(I was planning to get used to some extent … …\x01",
            "Excuse me for being the leader of one country. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F(Okay, my girlfriend's relationship is\x01",
            "It is not easy to follow up. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "But, you guys\x01",
            "I am thankful to participate in security.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Before Mr. MacDaely's crisis\x01",
            "I heard that I had saved it,\x01",
            "I am truly reliable.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41E5")


    ChrTalk(
        0x101,
        "#00006FNo, thanks for that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#02500FHmm, I am encouraged too.\x02\x03",
            "Thanks to that, the latter part of the conference\x01",
            "It seems to be able to focus on the discussion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FThe second half of the meeting ……\x02\x03",
            "#00101FGrandfather, again\x01",
            "Do you expect a difficult situation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#02503FOh, in fact unlike the first half\x01",
            "The autonomous state has pointed out that my ear is hurting\x01",
            "It will be done one after another.\x02\x03",
            "Well, still the demands of both countries\x01",
            "Although I can also say that as usual … …\x02\x03",
            "#02501FI am another concern\x01",
            "You mean Mr. Dieter.\x02\x03",
            "Even in the autonomous state legislature he is innovative\x01",
            "Proposing ideas one after another,\x01",
            "That enthusiasm is also wonderful … …\x02\x03",
            "On the contrary, he is still young.\x01",
            "Whether that momentum does not go wrong\x01",
            "There are also worrying aspects.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101FI see……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FTo be sure, Professor Ian\x01",
            "There is something wrong with Mayor Dieter\x01",
            "I mentioned that there was … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#02503FOh, I do not even know the content\x01",
            "The measures and points will be a point\x01",
            "It will be a mistake to come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "And if that measure\x01",
            "Will it come out with good and bad things … ….\x01",
            "It all depends on the flow of the meeting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#02503FYes, that is it.\x02\x03",
            "#02500FWell, at the meeting you mayor\x01",
            "Chairperson is to support\x01",
            "It is my work and absolute proposition.\x02\x03",
            "Anyway, I am me\x01",
            "I will do my best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FGrandpa …\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C4, 0)
    ClearChrFlags(0x2D, 0x10)
    ClearChrFlags(0x1A, 0x10)
    Return()

    # Function_18_3961 end

    def Function_19_4647(): pass

    label("Function_19_4647")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_465C")
    Call(0, 18)
    Jump("loc_46E2")

    label("loc_465C")


    ChrTalk(
        0xFE,
        (
            "#02500FAt the meeting the mayor\x01",
            "Chairperson is to support\x01",
            "It is my work and absolute proposition.\x02\x03",
            "Anyway, I am me\x01",
            "I will do my best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46E2")

    TalkEnd(0xFE)
    SetChrSubChip(0x2D, 0x1)
    Return()

    # Function_19_4647 end

    def Function_20_46EA(): pass

    label("Function_20_46EA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_46FB")
    Jump("loc_4772")

    label("loc_46FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_4738")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4716")
    Call(0, 21)
    Jump("loc_4733")

    label("loc_4716")


    ChrTalk(
        0x2A,
        "#08000FPui, Pui!\x02",
    )

    CloseMessageWindow()

    label("loc_4733")

    Jump("loc_4772")

    label("loc_4738")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_4772")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4753")
    Call(0, 22)
    Jump("loc_4772")

    label("loc_4753")


    ChrTalk(
        0x2A,
        "#08000FPui, Puy!\x02",
    )

    CloseMessageWindow()

    label("loc_4772")

    TalkEnd(0xFE)
    Return()

    # Function_20_46EA end

    def Function_21_4776(): pass

    label("Function_21_4776")

    OP_4B(0x13, 0xFF)
    OP_93(0x13, 0xB4, 0x0)
    OP_93(0x2A, 0x0, 0x0)

    ChrTalk(
        0x13,
        (
            "#07008FHey, Sieg.\x01",
            "If grandmother was present\x01",
            "I wonder what he was saying?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        "#08000FPui, Pewie.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#07000FHehe, that's right.\x01",
            "…… I am, I am.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x13, 0x0, 500)

    ChrTalk(
        0x13,
        "#07002FOh, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FExcuse me……\x01",
            "Hurry up and visit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#07009FNo, do not mind.\x02\x03",
            "With one person\x01",
            "I thought of various things … ….\x01",
            "I am glad that you came rather.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FHime Highness … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F…… As I thought,\x01",
            "Is it about the second half of the meeting?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#07000FWell, there is also it … …\x01",
            "It is a bit more fundamental.\x02\x03",
            "#07003FI am also a prominent diplomat as a couple\x01",
            "Some kind of bargaining\x01",
            "I am going to have a mind … …\x02\x03",
            "Approximately required for negotiations\x01",
            "Insight, judgment, and sense of balance … …\x02\x03",
            "#07001FEven in the first half of the meeting,\x01",
            "The overwhelming difference between them\x01",
            "Because I was keenly aware of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201FIs that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FWell, that's it.\x01",
            "It is also possible to calmly analyze\x01",
            "It's amazing enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FYes, your Highness\x01",
            "Certainly with me and Lloyd's\x01",
            "Even though the age is the same … …\x02\x03",
            "I am truly excuse me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#07002FHehe, thank you.\x02\x03",
            "#07003FBut certainly, only weak\x01",
            "It can not be helped even though it is vomiting.\x02\x03",
            "Although the situation of the continent is moving,\x01",
            "Even with step by step step by step\x01",
            "I have to go forward with my experience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FOh yeah, to it\x01",
            "Is not relaxing important too?\x02\x03",
            "Even now, that's wrong\x01",
            "It's a break time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FWadi … against Princess Hime\x01",
            "That attitude, how do you manage?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#07009FHehe, it does not matter at all.\x01",
            "Being overly careful\x01",
            "Because I feel comfortable as well.\x02\x03",
            "#07002FBut … something is strange.\x02\x03",
            "While talking to you,\x01",
            "Almost like the esters\x01",
            "I feel like I am doing it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106FThat is such a word.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#07000FHuhu, that's right, everyone,\x01",
            "Shall I make you a cup of tea?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        "#00005FNo, nothing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00206FWell, and now I'm in caution.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#07004FI'm sorry, that is true.\x02\x03",
            "#07000FWell then, everyone\x01",
            "Please take care.\x02\x03",
            "I also want to fulfill my duties\x01",
            "Because I will do my best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FOk, got it.\x02",
    )

    CloseMessageWindow()
    OP_93(0x13, 0xB4, 0x0)
    OP_93(0x2A, 0x0, 0x0)
    OP_4C(0x13, 0xFF)
    SetScenarioFlags(0x1C4, 1)
    Return()

    # Function_21_4776 end

    def Function_22_4F4F(): pass

    label("Function_22_4F4F")

    OP_4B(0x20, 0xFF)
    TurnDirection(0x20, 0x0, 500)

    ChrTalk(
        0x20,
        "Oh, everyone is in charge of patrol … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FWell, I am disturbing you.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x2A, 0x0, 500)

    ChrTalk(
        0x2A,
        "#08000FPui!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FHuhu, you and your Highness Claudia\x01",
            "Sieg who you were with.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#00205FIndeed, he is Ka'a's\x01",
            "The white falcon that I was talking about ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        "#08000FPui, Pui!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301FWell, what are you saying?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FTio, do you understand?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FWell, everyone is \"Hello\".\x01",
            "To me \"Nice to meet you\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302FHuh, you remember well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        "#08009FPui, Pewie!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202F\"Naturally it is a friend of Claudia Hime\"\x01",
            "It is said that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FThank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        "#08009FPui!\x02",
    )

    CloseMessageWindow()
    OP_93(0x20, 0xB4, 0x0)
    OP_93(0x2A, 0x0, 0x0)
    OP_4C(0x20, 0xFF)
    SetScenarioFlags(0x1C3, 6)
    Return()

    # Function_22_4F4F end

    def Function_23_51D1(): pass

    label("Function_23_51D1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_51E2")
    Jump("loc_5405")

    label("loc_51E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_531A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_529B")

    ChrTalk(
        0xFE,
        (
            "We are in the tower\x01",
            "The trapped people\x01",
            "I am indebted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There are girls on the right wing ……\x01",
            "I was caught up in such a thing\x01",
            "I feel sorry for it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_5315")

    label("loc_529B")


    ChrTalk(
        0xFE,
        (
            "There are girls on the right wing ……\x01",
            "Besides, I do not feel well at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Let me take sweets later\x01",
            "I wonder if I will give it …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5315")

    Jump("loc_5405")

    label("loc_531A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_5372")

    ChrTalk(
        0xFE,
        (
            "And anyway … …\x01",
            "Our staff also calm down\x01",
            "I have to act.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5405")

    label("loc_5372")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_5380")
    Jump("loc_5405")

    label("loc_5380")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_5405")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_539B")
    Call(0, 22)
    Jump("loc_5405")

    label("loc_539B")


    ChrTalk(
        0xFE,
        (
            "Everyone, with Sieg\x01",
            "You knew that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, Sieg you,\x01",
            "It is very clever san.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5405")

    TalkEnd(0xFE)
    Return()

    # Function_23_51D1 end

    def Function_24_5409(): pass

    label("Function_24_5409")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_54AC")

    ChrTalk(
        0xFE,
        "You are a member of the Special Affairs Division.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "All about you\x01",
            "You seem to be able to stay at any time\x01",
            "I have heard from His Holiness Claudia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please, please enter freely.\x02",
    )

    CloseMessageWindow()
    Jump("loc_54B5")

    label("loc_54AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_54B5")

    label("loc_54B5")

    TalkEnd(0xFE)
    Return()

    # Function_24_5409 end

    def Function_25_54B9(): pass

    label("Function_25_54B9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_54CA")
    Jump("loc_5571")

    label("loc_54CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_5568")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54E5")
    Call(0, 21)
    Jump("loc_5563")

    label("loc_54E5")


    ChrTalk(
        0x13,
        (
            "#07000Feveryone,\x01",
            "Please go out for chat\x01",
            "Thank you very much.\x02\x03",
            "Also from here, to each other\x01",
            "Let's keep tight.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5563")

    Jump("loc_5571")

    label("loc_5568")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_5571")

    label("loc_5571")

    TalkEnd(0xFE)
    Return()

    # Function_25_54B9 end

    def Function_26_5575(): pass

    label("Function_26_5575")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_560A")

    ChrTalk(
        0xFE,
        (
            "In order not to disturb you,\x01",
            "We stay still here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In such a time the intelligent behavior\x01",
            "You have to keep in mind.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56B2")

    label("loc_560A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_5618")
    Jump("loc_56B2")

    label("loc_5618")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_56B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5633")
    Call(0, 27)
    Jump("loc_56B2")

    label("loc_5633")


    ChrTalk(
        0xFE,
        (
            "The face of Misashi\x01",
            "Is it a printed manji head?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In such a place,\x01",
            "A little fancy is too effective\x01",
            "I also feel like … ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56B2")

    TalkEnd(0xFE)
    Return()

    # Function_26_5575 end

    def Function_27_56B6(): pass

    label("Function_27_56B6")

    OP_4B(0x1C, 0xFF)
    OP_4B(0x21, 0xFF)

    ChrTalk(
        0x1C,
        (
            "Hmm, but the tea deal to give to the president is\x01",
            "Have you really been okay with this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "Haha, well, everyone of the staff\x01",
            "It is a story that I thought hard,\x01",
            "I do not think you need worry?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x21,
        (
            "Besides, here is the feeling of this place\x01",
            "Is not it nice?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "Well, then\x01",
            "I think that there were other things … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105F(? To the prepared tea cake\x01",
            "I wonder if it was also a problem? )\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#00201F(That is Mitsushi Manju ……\x01",
            "Is not it common name \"Mishiman\"? )\x02\x03",
            "(No problems or nothing,\x01",
            "With no more best choice. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106F(Well, I guess … ….?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F(Hello, but what is it?\x01",
            "It seems to be a story of the story. )\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x1C, 0xFF)
    OP_4C(0x21, 0xFF)
    SetScenarioFlags(0x1C4, 2)
    Return()

    # Function_27_56B6 end

    def Function_28_5926(): pass

    label("Function_28_5926")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_5972")

    ChrTalk(
        0xFE,
        (
            "Well, first I have to take a deep breath …\x01",
            "Wow, huh ー ー ー ー っ.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A17")

    label("loc_5972")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_5980")
    Jump("loc_5A17")

    label("loc_5980")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_5A17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_599B")
    Call(0, 27)
    Jump("loc_5A17")

    label("loc_599B")


    ChrTalk(
        0xFE,
        (
            "Well, when I say so, I\x01",
            "Somewhat anxious it came.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, now we have other things\x01",
            "I do not have time to think and prepare … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A17")

    TalkEnd(0xFE)
    Return()

    # Function_28_5926 end

    def Function_29_5A1B(): pass

    label("Function_29_5A1B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B15")

    ChrTalk(
        0x17,
        (
            "#07500FHave you guys still been?\x02\x03",
            "Hmm, if you do not mind, here we go together\x01",
            "Would you like to drink tea?\x02\x03",
            "#07509FThere are also buns,\x01",
            "Amenity#2RRelax#Please do not hesitate to ask me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FHouse……\x01",
            "That's why.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FYes, I disturbed.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_5B7F")

    label("loc_5B15")


    ChrTalk(
        0x17,
        (
            "#07503FMogmog …\x01",
            "However, this manju is superb.\x02\x03",
            "#07509FHa ha ha, some\x01",
            "Would you buy it as a gift?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B7F")

    TalkEnd(0xFE)
    Return()

    # Function_29_5A1B end

    def Function_30_5B83(): pass

    label("Function_30_5B83")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_5C1B")

    ChrTalk(
        0xFE,
        (
            "Oh, but of course … …\x01",
            "It is not a room cleaning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Teruburu ……\x01",
            "Thinking a lot about bad things\x01",
            "I can not stop trembling anyhow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D07")

    label("loc_5C1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_5C29")
    Jump("loc_5D07")

    label("loc_5C29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_5D07")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CAA")

    ChrTalk(
        0xFE,
        (
            "What is the view from here?\x01",
            "It is truly a superb view.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "While wiping the window,\x01",
            "I will take a moment to chase.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_5D07")

    label("loc_5CAA")

    OP_93(0xFE, 0x5A, 0x0)

    ChrTalk(
        0xFE,
        (
            "Hanging out … …\x01",
            "Perfume\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Kyukyuyukyu ……\x01",
            "Ruururu ~ ♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D07")

    TalkEnd(0xFE)
    Return()

    # Function_30_5B83 end

    def Function_31_5D0B(): pass

    label("Function_31_5D0B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DBD")

    ChrTalk(
        0xFE,
        (
            "Here at the break the mayor and chairman\x01",
            "It is a room to be used jointly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is being fought at the meeting right now\x01",
            "For the mayor and the chairperson, truthfully\x01",
            "I'm cleaning you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_5E27")

    label("loc_5DBD")


    ChrTalk(
        0xFE,
        (
            "Pata-beatapata …\x01",
            "Good luck, Mayor of Dieter ♪ ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Pata-beatapata …\x01",
            "I will lose, Mr. MacDaely, ♪ ♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E27")

    TalkEnd(0xFE)
    Return()

    # Function_31_5D0B end

    def Function_32_5E2B(): pass

    label("Function_32_5E2B")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Well, after this\x01",
            "It will only leave the second half of the meeting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well actually from here\x01",
            "It is hard work …… Mayor and chairman\x01",
            "I have to work hard.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_32_5E2B end

    def Function_33_5EB7(): pass

    label("Function_33_5EB7")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Oh, everyone.\x01",
            "Now, Mayor Dieter is next door\x01",
            "In the room of Prince Oliver.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And McDowell said\x01",
            "On the left wing of the Grand Duke of Albert\x01",
            "We are visiting each room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If it's okay, please direct the room\x01",
            "Why do not you visit us.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_33_5EB7 end

    def Function_34_5FA5(): pass

    label("Function_34_5FA5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5FB6")
    Jump("loc_63DC")

    label("loc_5FB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_61DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60FD")

    ChrTalk(
        0xFE,
        (
            "In addition to the Defense Forces,\x01",
            "A dubious person as a private unit\x01",
            "It seems that it operated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The hunters who struck that city,\x01",
            "A bad boy who does not suit well in this place\x01",
            "I saw you were inside the tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Despite quite a few doubts,\x01",
            "There was nothing to call out … …\x01",
            "I think there are many suspicious points when thinking now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_61D5")

    label("loc_60FD")


    ChrTalk(
        0xFE,
        (
            "The hunters who struck that city,\x01",
            "A bad boy who does not suit well in this place\x01",
            "I saw you were inside the tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Despite quite a few doubts,\x01",
            "There was nothing to call out … …\x01",
            "I think there are many suspicious points when thinking now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_61D5")

    Jump("loc_63DC")

    label("loc_61DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_625F")

    ChrTalk(
        0xFE,
        (
            "No way, to the conference hall\x01",
            "Direct terrorists\x01",
            "I can not get in … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Such a situation, what on earth\x01",
            "Who could have expected it ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63DC")

    label("loc_625F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_626D")
    Jump("loc_63DC")

    label("loc_626D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_63DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6351")

    ChrTalk(
        0xFE,
        (
            "During the break here,\x01",
            "For Prince Oliver\x01",
            "It is a room to open.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if it says anything,\x01",
            "Your success in the social circle of the empire\x01",
            "A well-known genuine florist …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Also in the setting of the room\x01",
            "I'm entering with nature.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_63DC")

    label("loc_6351")


    ChrTalk(
        0xFE,
        (
            "Speaking of Oliver's Prince,\x01",
            "Your success in the social circle of the empire\x01",
            "A well-known genuine florist …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Also in the setting of the room\x01",
            "I'm entering with nature.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63DC")

    TalkEnd(0xFE)
    Return()

    # Function_34_5FA5 end

    def Function_35_63E0(): pass

    label("Function_35_63E0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_6459")

    ChrTalk(
        0xFE,
        (
            "Really, a nightmare\x01",
            "I can only imagine seeing … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Everyone, from now on\x01",
            "What will happen?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_64F6")

    label("loc_6459")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_6467")
    Jump("loc_64F6")

    label("loc_6467")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_64F6")

    ChrTalk(
        0xFE,
        (
            "Prince Oliver is a rose flower,\x01",
            "Especially because he likes red roses\x01",
            "I'm decorating in this way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Huhu, I'm happy if you can be pleased.\x02",
    )

    CloseMessageWindow()

    label("loc_64F6")

    TalkEnd(0xFE)
    Return()

    # Function_35_63E0 end

    def Function_36_64FA(): pass

    label("Function_36_64FA")

    TalkBegin(0xFE)
    Call(0, 37)
    TalkEnd(0xFE)
    Return()

    # Function_36_64FA end

    def Function_37_6504(): pass

    label("Function_37_6504")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EBD")

    ChrTalk(
        0x2B,
        (
            "#02809FHaha, I see.\x01",
            "It can be expected in the future\x01",
            "Young people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2C,
        (
            "#07204FOh, and they are still\x01",
            "I am not dyed in any color.\x02\x03",
            "#07202FSo, increasingly -\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2C, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x2C, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x2C, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x2C, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_666A")
    Jump("loc_66B4")

    label("loc_666A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2C, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_668A")
    OP_52(0x2C, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_66B4")

    label("loc_668A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2C, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_66AA")
    OP_52(0x2C, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_66B4")

    label("loc_66AA")

    OP_52(0x2C, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x2C, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_66B4")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2B, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x2B, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x2B, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x2B, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_676D")
    Jump("loc_67B7")

    label("loc_676D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2B, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_678D")
    OP_52(0x2B, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_67B7")

    label("loc_678D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2B, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_67AD")
    OP_52(0x2B, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_67B7")

    label("loc_67AD")

    OP_52(0x2B, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x2B, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_67B7")

    OP_52(0x2B, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x2B, 0x10)
    Sleep(100)

    ChrTalk(
        0x2C,
        (
            "#07205FOh, are not you of the support department?\x02\x03",
            "#07209FIf it's okay,\x01",
            "Why do not you go out for chat?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FOh, yes.\x01",
            "I have to bother you two people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FBy the way, what kind\x01",
            "Were you talking about it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        (
            "#02804FOh, your Prince is actually\x01",
            "Military school in the empire\x01",
            "He is a director.\x02\x03",
            "#02800FI was talking about that story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205FTo say director,\x01",
            "It is one of the officials responsible for the school.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00302FOh, I'm doing such a thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2C,
        (
            "#07204FHuff, name to the last\x01",
            "It is only for lending.\x02\x03",
            "#07202FIn that sense,\x01",
            "Mayor of Dieter than I am\x01",
            "You can say that you are contributing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FMayor Dieter … …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        (
            "#02804FOh no, to the last\x01",
            "It's business meaning, though.\x02\x03",
            "#02800FThe military school from the Epstein Foundation\x01",
            "In introducing a conducting net\x01",
            "I got a little loan from IBC.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FWell, was that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205FBy the way, even in the direction of the empire\x01",
            "When the introduction of the conducting net test has begun\x01",
            "I heard it at the foundation headquarters … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHuh, you do not think\x01",
            "International bank with branches in each country.\x01",
            "The business prosperity is not huge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2C,
        (
            "#07202FHmm, you guys\x01",
            "It is also the edge of something that I did such a story.\x02\x03",
            "#07209Fif there is a chance,\x01",
            "A special lecture at my military academy\x01",
            "Do not you want to try it?\x02\x03",
            "#07212FIf you feel that\x01",
            "The forbiddance relationship between lecturers and cadets,\x01",
            "Everything will be ants.\x02",
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
        "#00006FWhat is it about ……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x2B, 0x1)

    ChrTalk(
        0x2B,
        (
            "#02809FHaha, your Highness Prince Oliver\x01",
            "I am still very happy.\x02\x03",
            "Next time while drinking alcohol,\x01",
            "I want to talk calmly.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x2C, 0x0)

    ChrTalk(
        0x2C,
        (
            "#07209FHuh, indeed.\x01",
            "This is definitely the way to join us.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2B, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x2C, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)

    ChrTalk(
        0x102,
        (
            "#00109F(His Highness and Prince …\x01",
            "You seem to be pretty enthusiastic. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F(Oh, people with big scale hobbies,\x01",
            "Is it like I get along well? )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C3, 7)
    Jump("loc_6FD2")

    label("loc_6EBD")


    ChrTalk(
        0x2B,
        (
            "#02805FBy the way your Highness\x01",
            "Is it a strong one to drink?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2C,
        (
            "#07202FOh, as it is.\x02\x03",
            "#07204F…… However, in the world\x01",
            "As much as there is a top.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F(Royal Highness Prince ……\x01",
            "It is somewhat distant eyes. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(… …. something with drinking\x01",
            "Is it also an important memory? )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6FD2")

    Return()

    # Function_37_6504 end

    def Function_38_6FD3(): pass

    label("Function_38_6FD3")

    TalkBegin(0xFE)
    Call(0, 37)
    TalkEnd(0xFE)
    Return()

    # Function_38_6FD3 end

    def Function_39_6FDD(): pass

    label("Function_39_6FDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6FF0")
    Call(0, 51)
    Return()

    label("loc_6FF0")

    TalkBegin(0xFE)

    ChrTalk(
        0x14,
        (
            "#11501FOh, is that Almorica village?\x02\x03",
            "#11509FWhy are the bees carrying honey?\x02",
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
        "#00006FNo, it can not be seen.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_39_6FDD end

    def Function_40_70D5(): pass

    label("Function_40_70D5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71B6")

    ChrTalk(
        0xFE,
        (
            "From the martial law we have been\x01",
            "It was binding on me here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the way, the president\x01",
            "A girl with a mysterious atmosphere\x01",
            "It was like I was taking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe that,\x01",
            "What is the \"Child\" of rumors …?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_7237")

    label("loc_71B6")


    ChrTalk(
        0xFE,
        (
            "What is President\x01",
            "A girl with a mysterious atmosphere\x01",
            "It was like I was taking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe that,\x01",
            "What is the \"Child\" of rumors …?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7237")

    TalkEnd(0xFE)
    Return()

    # Function_40_70D5 end

    def Function_41_723B(): pass

    label("Function_41_723B")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Since the invalid declaration of an independent country,\x01",
            "Even for us working at the tower\x01",
            "An uneasy situation continued … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, it is not meant to be such a thing.\x01",
            "I wonder what will happen in the future …\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_41_723B end

    def Function_42_72D9(): pass

    label("Function_42_72D9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_74A4")

    ChrTalk(
        0xFE,
        "Dear E, Mr. …! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FMr. Ranfi ……\x01",
            "I am glad that it was okay.\x02\x03",
            "The people of IBC here\x01",
            "It seems they are gathering?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Y-yes…\x01",
            "With orders of Mr. Maria Bell … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The city is in trouble,\x01",
            "Mr. Dieter and Mary Bell lady\x01",
            "What was it supposed to be ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F……Anyways,\x01",
            "Please stay here now.\x02\x03",
            "This situation is what we\x01",
            "I will try it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Wow, I understand …\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_7519")

    label("loc_74A4")


    ChrTalk(
        0xFE,
        (
            "Mr. Dieter and Mary Bell lady\x01",
            "What was it supposed to be ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "… and that person who was with you is certain ……\x02",
    )

    CloseMessageWindow()

    label("loc_7519")

    TalkEnd(0xFE)
    Return()

    # Function_42_72D9 end

    def Function_43_751D(): pass

    label("Function_43_751D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_75F6")

    ChrTalk(
        0xFE,
        (
            "There are no presidents on this floor … …\x01",
            "Other people may know something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Leave this place for a moment,\x01",
            "Invite yourself to investigate without heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…… However, do not make it unreasonable.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 3)
    Jump("loc_7667")

    label("loc_75F6")


    ChrTalk(
        0xFE,
        (
            "Leave this place for a moment,\x01",
            "Invite yourself to investigate without heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…… However, do not make it unreasonable.\x02",
    )

    CloseMessageWindow()

    label("loc_7667")

    TalkEnd(0xFE)
    Return()

    # Function_43_751D end

    def Function_44_766B(): pass

    label("Function_44_766B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7754")

    ChrTalk(
        0xFE,
        (
            "I believe in Mary Bell\x01",
            "I stayed in the technical department … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Clay never trusts me\x01",
            "I jumped out of the engineering department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've parted my fight but ….\x01",
            "Apparently that guy\x01",
            "It sounds like it was right.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 4)
    Jump("loc_77C0")

    label("loc_7754")


    ChrTalk(
        0xFE,
        (
            "…… Apparently Clay is better\x01",
            "It sounds like it was right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although we faced part of the fight,\x01",
            "I wonder if I can reconcile …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_77C0")

    TalkEnd(0xFE)
    Return()

    # Function_44_766B end

    def Function_45_77C4(): pass

    label("Function_45_77C4")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "After the declaration of martial law came out,\x01",
            "It was completely shut out\x01",
            "It is because it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We can not use the terminal of the power net,\x01",
            "Okay, thank you ….\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_45_77C4 end

    def Function_46_7866(): pass

    label("Function_46_7866")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_795B")

    ChrTalk(
        0xFE,
        (
            "As the security department, the structure of the tower\x01",
            "Some form of duty of officials\x01",
            "I need to figure out … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After moving to the Orkis Tower,\x01",
            "I guess the secret has increased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mary Bell Ladies\x01",
            "How the hell have you been?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 5)
    Jump("loc_7998")

    label("loc_795B")


    ChrTalk(
        0xFE,
        (
            "Mary Bell Ladies\x01",
            "How the hell have you been?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7998")

    TalkEnd(0xFE)
    Return()

    # Function_46_7866 end

    def Function_47_799C(): pass

    label("Function_47_799C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A88")

    ChrTalk(
        0xFE,
        (
            "Risk factor S, hunting army \"Red constellation\" … ….\x01",
            "President Dieter and\x01",
            "There was a suspicion that it was connected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anything, those who blew up IBC\x01",
            "Because he was shaking and hopping around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…… President …… I can not trust any longer.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 6)
    Jump("loc_7AB7")

    label("loc_7A88")


    ChrTalk(
        0xFE,
        (
            "President Dieter ……\x01",
            "I can not trust any longer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7AB7")

    TalkEnd(0xFE)
    Return()

    # Function_47_799C end

    def Function_48_7ABB(): pass

    label("Function_48_7ABB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7BB6")

    ChrTalk(
        0xC,
        (
            "#11228FFather has been … …\x01",
            "I think that I was worrying.\x02\x03",
            "About mother, about me\x02\x03",
            "While thinking about various things\x01",
            "…… I can not turn back … …\x02\x03",
            "#11227F……Everyone……\x01",
            "Please let me know about your father\x01",
            "Thank you……!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 7)
    Jump("loc_7BFF")

    label("loc_7BB6")


    ChrTalk(
        0xC,
        (
            "#11227FEveryone……\x01",
            "Please let me know about your father\x01",
            "Thank you……!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7BFF")

    TalkEnd(0xFE)
    Return()

    # Function_48_7ABB end

    def Function_49_7C03(): pass

    label("Function_49_7C03")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F6E")

    ChrTalk(
        0x11,
        (
            "#11PIs cheers for good work,\x01",
            "You are a member of the Special Affairs Division.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F#6PYeah, good tired.\x02\x03",
            "#00005FMaybe in this room … …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#11PYes, President Croise ……\x01",
            "The suspect is detained.\x02",
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
        "#6P#00108F…… What is the president like?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#11PWhen our police force was detained\x01",
            "It seemed like a strange loss … …\x01",
            "Now I am regaining calm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#11PBecause it does not appear to resist,\x01",
            "We only need a minimum number of people\x01",
            "It is a situation where it is allocated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#11PUnder instructions from Sergei police,\x01",
            "Everyone can visit, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00306FReally……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00208F… … How do you do, Mr. Lloyd.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AF, 7)
    Jump("loc_7FF7")

    label("loc_7F6E")


    ChrTalk(
        0x11,
        (
            "#11PIn this room,\x01",
            "Crois suspects\x01",
            "I have been restrained.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#11PUnder instructions from Sergei police,\x01",
            "Everyone can visit, but …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7FF7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8001")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_810D")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "To meet a dieter\x01",      # 0
            "To give up\x01",                # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_806B")
    Call(0, 50)
    Return()

    label("loc_806B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8108")

    ChrTalk(
        0x101,
        "#6P#00006F…… I will stop now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#11POK.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#11PVisit with Croix suspect\x01",
            "If you wish,\x01",
            "Please speak to me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8108")

    Jump("loc_8001")

    label("loc_810D")

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

    # Function_49_7C03 end

    def Function_50_8144(): pass

    label("Function_50_8144")


    ChrTalk(
        0x101,
        (
            "#6P#00003F……Thank you.\x02\x03",
            "#00008FWhat is he thinking right now …?\x01",
            "I feel like listening to stories.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00106F….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#11PI understand. Thank you.\x02",
    )

    CloseMessageWindow()
    OP_93(0x11, 0x0, 0x1F4)

    def lambda_820C():
        OP_95(0xFE, 111300, 0, -101000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_820C)
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
            "#11301F#5P… … you guys.\x02\x03",
            "#11304F…… Huh, what are you talking about?\x01",
            "To me who became an international criminal now … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00001F…… Mr. Dieter.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00108F…………uncle…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        (
            "#11306F#5P…… So becoming one person\x01",
            "I finally realized it.\x02\x03",
            "As Bell says,\x01",
            "I thought of Professor Grimwood\x01",
            "It was just being moved.\x02\x03",
            "#11303FHe raised the ideal of \"justice\" vocally,\x01",
            "If so, even sacrifice is disgusting#2RMost#I did not.\x02\x03",
            "#11311F…… As a result, how is it?\x01",
            "Even a single daughter abandoned,\x01",
            "I am about to lose the seat of the president now.\x02\x03",
            "#11302F…… Ha ha ha …\x01",
            "It is not that boy of that \"association\"\x01",
            "As if a pathetic clown#6RPiro#it seems like.\x02",
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
            "#12P#00006F…… We,\x01",
            "I can not completely deny you.\x02\x03",
            "#00008FFor your own \"justice\"\x01",
            "To persevere belief everywhere … …\x02\x03",
            "#00001FWhatever the way,\x01",
            "If you crossbell peace\x01",
            "It is a fact that I tried to protect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303F… they are.\x02\x03",
            "#00301FWe also used IBC before\x01",
            "In the words you said\x01",
            "There was something I felt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203F\"A living being who asks for justice\" … …\x01",
            "Maybe it is possible to say so.\x02\x03",
            "#00208FCitizens agreed with the Declaration of Independence,\x01",
            "To see your pursuit of that \"justice\"\x01",
            "It is because it felt charm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        "#11303F#5P….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00106FBut … the way you are doing is\x01",
            "After all, I think that I was wrong.\x02\x03",
            "#00108FEven if the independent nation survives,\x01",
            "The uncle's \"righteousness\" is recognized\x01",
            "As peace has come … …\x02\x03",
            "The scratches of people truncated in the process,\x01",
            "There is nothing easy to heal.\x02\x03",
            "#00101FOn the premise of sacrificing someone\x01",
            "Peace to be grabbed … …\x02\x03",
            "It is my uncle\x01",
            "I was told at the stage of that declaration of independence,\x01",
            "\"Deception\" itself is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        (
            "#11304F#5P… … Huh, that's right.\x01",
            "Ellie, you are right.\x02\x03",
            "By getting the power of Ka'aa,\x01",
            "Against my \"justice\"\x01",
            "It may have been blind.\x02\x03",
            "#11302FEven if you try Mr. Grimewood,\x01",
            "I am not aware of such deception\x01",
            "It was probably easy to handle.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8BBB")

    ChrTalk(
        0x10A,
        "#12P#00603F(…… Professor Ian … …)\x02",
    )

    CloseMessageWindow()
    Jump("loc_8C2A")

    label("loc_8BBB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8BF5")

    ChrTalk(
        0x105,
        "#12P#10403F…………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_8C2A")

    label("loc_8BF5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8C2A")

    ChrTalk(
        0x106,
        "#12P#10703F…………………………\x02",
    )

    CloseMessageWindow()

    label("loc_8C2A")


    ChrTalk(
        0x2B,
        (
            "#11303F#5PBut … what is called \"justice\"\x01",
            "It is exercised by power and will,\x01",
            "The idea itself does not change.\x02\x03",
            "#11301FYou guys are going to give your \"justice\"\x01",
            "If you are going to pursue … …\x02\x03",
            "You and your will\x01",
            "I will need to show my teachers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006F…… It's not easy, but …\x01",
            "I am planning to accomplish anything.\x02\x03",
            "#00013FTo get back Ka'aa\x01",
            "If it is necessary … …!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8DD3")

    ChrTalk(
        0x106,
        "#12P#10701F……I agree.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8E3E")

    label("loc_8DD3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8E0D")

    ChrTalk(
        0x109,
        "#12P#10101FYes, of course.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8E3E")

    label("loc_8E0D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8E3E")

    ChrTalk(
        0x105,
        "#12P#10402FHuh, that's right.\x02",
    )

    CloseMessageWindow()

    label("loc_8E3E")


    ChrTalk(
        0x2B,
        (
            "#11301F#5P…… then, if you want me\x01",
            "There is no longer any use.\x02\x03",
            "#11303FEven the teacher, … but my girls\x01",
            "Bell is honest and unfamiliar.\x02\x03",
            "#11304FYou guys regain Ka'ae,\x01",
            "Whether we can go forward ……\x02\x03",
            "#11300FLet 's try to figure out here.\x02",
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
        "#5P#00106F….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00301FLady …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00208F……Are you okay?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 500)
    Sleep(150)

    ChrTalk(
        0x102,
        (
            "#5P#00104F…… Yeah, that's fine.\x02\x03",
            "#00108FTruncated like that in the bell\x01",
            "I was a bit worried … ….\x02\x03",
            "#00102FBecause it was surprisingly solid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00004F…… Oh, I was a bit relieved.\x02\x03",
            "#00000FAs he says … …\x01",
            "Let's say we are going forward.\x02",
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

    # Function_50_8144 end

    def Function_51_91D0(): pass

    label("Function_51_91D0")

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
            "#11P#11504FNo, even so\x01",
            "It is a luxurious view.\x02\x03",
            "#11500FEveryone at the Special Affairs Division\x01",
            "Do not you think so?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00011FLecter …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00108FWhy in a place like this …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#11P#11504FHell, to the waiting room of the honorable chairperson\x01",
            "To have that attendant staff\x01",
            "Are there any wonders?\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 3)), scpexpr(EXPR_END)), "loc_945A")

    AnonymousTalk(
        0x14,
        (
            "Hey, did you see me again?\x02\x03",
            "Oh my …\x01",
            "Was it your first mistake?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_94B3")

    label("loc_945A")


    AnonymousTalk(
        0x14,
        (
            "I hope to see you all\x01",
            "It's been several weeks.\x02\x03",
            "Oh my …\x01",
            "Was it your first mistake?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_94B3")

    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    ChrTalk(
        0x102,
        (
            "#6P#00106FAh … please.\x01",
            "Please do not make jokes with serious face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00211F…… What is it,\x01",
            "It is a person who can not eat as ever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#11P#11509FHaha, that is my\x01",
            "That's a charming point.\x02\x03",
            "#11502FSo, I heard something from a little while ago\x01",
            "You seem to have a face?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FYeah, thanks.\x01",
            "Here are some situations.\x02\x03",
            "#00013FAt this trade meeting … …\x01",
            "About the movement of your imperial government.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#11P#11510FOh, I see.\x01",
            "Where are you talking about?\x01",
            "I do not know if I'm grasping … …\x02\x03",
            "#11504FThen, do you know this?\x02\x03",
            "#11501F- I'm going inside with a \"aristocrat\"\x01",
            "I'm aiming at the head of Giulious Osbourne.\x02",
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
        "#6P#10107FBecome Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10301FWow … ….?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106F… … Do not be deceived.\x01",
            "Because this is the hand of this person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00301FA hand like before\x01",
            "I will eat it twice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00211FI was worrying too much as expected.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#11P#11509FHaha, you gotta go.\x02\x03",
            "#11502FWell, to tell the truth\x01",
            "Much more reaction\x01",
            "I expected it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FHuff, unexpectedly true\x01",
            "Is not it a punch line?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006F…… Lector clerk.\x01",
            "Whatever your position and aim is OK.\x02\x03",
            "#00008FBut, as I saw ……\x01",
            "You are responsible for any work\x01",
            "I think that it is a type that you can achieve to the end.\x02\x03",
            "#00001FIn that sense, during our trade conference,\x01",
            "At least from the standpoint of security\x01",
            "We should be able to cooperate ……\x02\x03",
            "#00000F─ ─ Does it differ?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#11P#11504FKuku … I see.\x02\x03",
            "#11508FWell, as earlier as a joke -\x01",
            "If you think so, the imagination will expand a lot?\x02\x03",
            "#11501FAlways keep every pattern\x01",
            "Do not rest your hands to explore.\x02\x03",
            "#11509FWhy is it the secret to become a good writer?\x02",
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
            "#6P#00006FNobody wants to be a writer\x01",
            "I do not think so ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00301FWant to go anywhere\x01",
            "He was the one who took a person ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#11P#11504FWell, now I can do it from me\x01",
            "It's like advice.\x02\x03",
            "#11500FAt best, thinking a lot,\x01",
            "You should prepare for every case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10106F…… Thank you for your advice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006F(Ha … but …\x01",
            "I really can not read it. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00108F(Yeah, thanks in some way\x01",
            "I feel confused. )\x02",
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

    # Function_51_91D0 end

    def Function_52_9D99(): pass

    label("Function_52_9D99")

    Sound(160, 0, 100, 0)
    Return()

    # Function_52_9D99 end

    def Function_53_9DA0(): pass

    label("Function_53_9DA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9DC8")
    SetScenarioFlags(0x146, 3)

    label("loc_9DC8")

    Return()

    # Function_53_9DA0 end

    def Function_54_9DC9(): pass

    label("Function_54_9DC9")

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
            "#6P#02803FI will attend the meeting here\x01",
            "Prepared by top leaders\x01",
            "It is a floor with a waiting room.\x02\x03",
            "#02800FLet me show only roughly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#11PPlease.\x02",
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
        "#00305F#5POh, it's gorgeous as expected.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FElegantly in this room\x01",
            "I want to spend time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        (
            "#6P#02804FThis is your Highness Prince Oliver\x01",
            "It is a waiting room planned to be used.\x02\x03",
            "#02800FThere is room on left wing, too\x01",
            "It is assigned to each participant.\x02\x03",
            "#02809FWell, the head you heat up at the meeting\x01",
            "It's a place to be chilled.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A41B():
        TurnDirection(0x101, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A41B)
    Sleep(50)

    def lambda_A42B():
        TurnDirection(0x109, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_A42B)
    Sleep(50)

    def lambda_A43B():
        TurnDirection(0x102, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_A43B)
    Sleep(50)

    def lambda_A44B():
        TurnDirection(0x105, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_A44B)
    Sleep(50)

    def lambda_A45B():
        TurnDirection(0x103, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_A45B)
    Sleep(50)

    def lambda_A46B():
        TurnDirection(0x104, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_A46B)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x109,
        "#11P#10112FI see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205F#11POnce in these rooms\x01",
            "Conducting cable … …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        (
            "#6P#02805FOh, in an unobtrusive shape\x01",
            "Wiring should have been done.\x02\x03",
            "#02804FWell, for other rooms\x01",
            "As to omit it\x02\x03",
            "#02800FFinally just over there\x01",
            "Shall I introduce you?\x02",
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

    def lambda_A6FF():
        OP_98(0xFE, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x35, 1, lambda_A6FF)

    def lambda_A719():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_A719)
    Sleep(50)

    def lambda_A736():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A736)
    Sleep(50)

    def lambda_A753():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A753)
    Sleep(50)

    def lambda_A770():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A770)
    Sleep(50)

    def lambda_A78D():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A78D)
    Sleep(50)

    def lambda_A7AA():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0xFFFFFED4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A7AA)
    Sleep(50)

    def lambda_A7C7():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A7C7)
    FadeToBright(1000, 0)
    Sleep(600)

    def lambda_A7ED():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A7ED)
    Sleep(300)

    def lambda_A801():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A801)
    Sleep(600)

    def lambda_A815():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_A815)
    Sleep(300)

    def lambda_A829():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_A829)
    OP_0D()
    OP_4B(0x11, 0xFF)
    SetChrChipByIndex(0x11, 0x29)
    SetChrSubChip(0x11, 0x0)

    ChrTalk(
        0x11,
        "#12A#5PThis is Mayor of Dieter!\x02",
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
        "#12A#5PGood morning!\x02",
    )

    Sleep(1200)
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x2B, 1)

    ChrTalk(
        0x2B,
        "#02809F#11PHaha, please make it easy.\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x35, 1)
    OP_6B(0xFF)
    WaitChrThread(0x105, 1)
    OP_93(0x2B, 0x5A, 0x1F4)

    ChrTalk(
        0x2B,
        (
            "#6P#02804FThis corridor room shows the state of the meeting\x01",
            "It can be confirmed one by one.\x02\x03",
            "#02800FIn confidential meetings etc.\x01",
            "I sometimes close the curtain\x01",
            "I will keep it open this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#11PI see……\x02",
    )

    CloseMessageWindow()

    def lambda_A99E():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A99E)
    Sleep(50)

    def lambda_A9AE():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_A9AE)
    Sleep(50)

    def lambda_A9BE():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_A9BE)
    Sleep(50)

    def lambda_A9CE():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_A9CE)
    Sleep(50)

    def lambda_A9DE():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_A9DE)
    Sleep(50)

    def lambda_A9EE():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_A9EE)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    OP_68(-2000, 1500, -124000, 3000)
    MoveCamera(35, 17, 0, 3000)
    SetCameraDistance(19500, 3000)

    def lambda_AA38():
        OP_97(0x101, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AA38)
    Sleep(200)

    def lambda_AA55():
        OP_97(0x103, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_AA55)
    Sleep(200)

    def lambda_AA72():
        OP_97(0x109, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_AA72)
    Sleep(200)

    def lambda_AA8F():
        OP_97(0x102, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_AA8F)
    Sleep(200)

    def lambda_AAAC():
        OP_97(0x104, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_AAAC)
    Sleep(200)

    def lambda_AAC9():
        OP_97(0x105, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_AAC9)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)

    def lambda_AAFB():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_AAFB)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00002F#11PI can confirm the state of the meeting place\x01",
            "Thankful for a moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#11PWell, if something happens\x01",
            "I can seem to be able to rush.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F#11PIn that sense\x01",
            "I want to make it a tour route.\x02",
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
            "#6P#02803FWell, you guard with this\x01",
            "I guided three floors … …\x02\x03",
            "#02800FTo the last place you leave\x01",
            "Let me show you around.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AC86():
        TurnDirection(0x101, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AC86)
    Sleep(50)

    def lambda_AC96():
        TurnDirection(0x109, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_AC96)
    Sleep(50)

    def lambda_ACA6():
        TurnDirection(0x102, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_ACA6)
    Sleep(50)

    def lambda_ACB6():
        TurnDirection(0x105, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_ACB6)
    Sleep(50)

    def lambda_ACC6():
        TurnDirection(0x103, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_ACC6)
    Sleep(50)

    def lambda_ACD6():
        TurnDirection(0x104, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_ACD6)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x101,
        "#00005F#5PYour best place ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00302F#11PWell, where is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        (
            "#6P#02809FHuh …… most in this building\x01",
            "A place with a nice view.\x02",
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

    # Function_54_9DC9 end

    def Function_55_ADA5(): pass

    label("Function_55_ADA5")

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

    # Function_55_ADA5 end

    def Function_56_AE24(): pass

    label("Function_56_AE24")


    def lambda_AE29():
        OP_95(0xFE, 81000, 0, 1500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AE29)

    def lambda_AE43():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_AE43)
    WaitChrThread(0xFE, 1)

    def lambda_AE58():
        OP_95(0xFE, 77500, 0, -1000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AE58)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_56_AE24 end

    def Function_57_AE79(): pass

    label("Function_57_AE79")


    def lambda_AE7E():
        OP_95(0xFE, 81000, 0, 2000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AE7E)

    def lambda_AE98():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_AE98)
    WaitChrThread(0xFE, 1)

    def lambda_AEAD():
        OP_95(0xFE, 79200, 0, -400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AEAD)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_57_AE79 end

    def Function_58_AECE(): pass

    label("Function_58_AECE")


    def lambda_AED3():
        OP_95(0xFE, 81000, 0, 2000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AED3)

    def lambda_AEED():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_AEED)
    WaitChrThread(0xFE, 1)

    def lambda_AF02():
        OP_95(0xFE, 78300, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AF02)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_58_AECE end

    def Function_59_AF23(): pass

    label("Function_59_AF23")


    def lambda_AF28():
        OP_95(0xFE, 81000, 0, 2500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AF28)

    def lambda_AF42():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_AF42)
    WaitChrThread(0xFE, 1)

    def lambda_AF57():
        OP_95(0xFE, 80400, 0, -100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AF57)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_59_AF23 end

    def Function_60_AF78(): pass

    label("Function_60_AF78")


    def lambda_AF7D():
        OP_95(0xFE, 81000, 0, 2500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AF7D)

    def lambda_AF97():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_AF97)
    WaitChrThread(0xFE, 1)

    def lambda_AFAC():
        OP_95(0xFE, 79500, 0, 800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AFAC)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_60_AF78 end

    def Function_61_AFCD(): pass

    label("Function_61_AFCD")


    def lambda_AFD2():
        OP_95(0xFE, 81000, 0, 3000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AFD2)

    def lambda_AFEC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_AFEC)
    WaitChrThread(0xFE, 1)

    def lambda_B001():
        OP_95(0xFE, 80800, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B001)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_61_AFCD end

    def Function_62_B022(): pass

    label("Function_62_B022")


    def lambda_B027():
        OP_95(0xFE, 81000, 0, 3000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B027)

    def lambda_B041():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B041)
    WaitChrThread(0xFE, 1)

    def lambda_B056():
        OP_95(0xFE, 79900, 0, 2100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B056)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_62_B022 end

    def Function_63_B077(): pass

    label("Function_63_B077")


    def lambda_B07C():
        OP_95(0xFE, 109000, 0, -130500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B07C)
    WaitChrThread(0xFE, 1)

    def lambda_B09A():
        OP_95(0xFE, 109000, 0, -112500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B09A)
    WaitChrThread(0xFE, 1)

    def lambda_B0B8():
        OP_95(0xFE, 111000, 0, -110500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B0B8)
    WaitChrThread(0xFE, 1)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0x5, 0x0, 0x0)

    def lambda_B0EE():
        OP_95(0xFE, 113000, 0, -110500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B0EE)
    Sleep(500)

    def lambda_B10B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B10B)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_63_B077 end

    def Function_64_B11C(): pass

    label("Function_64_B11C")


    def lambda_B121():
        OP_95(0xFE, 109000, -600, -130500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B121)
    WaitChrThread(0xFE, 1)
    Sleep(1000)
    MoveCamera(35, 19, 0, 7000)
    SetCameraDistance(19000, 7000)

    def lambda_B156():
        OP_95(0xFE, 109000, -600, -112500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B156)
    WaitChrThread(0xFE, 1)

    def lambda_B174():
        OP_95(0xFE, 111000, -600, -110500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B174)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_64_B11C end

    def Function_65_B18E(): pass

    label("Function_65_B18E")


    def lambda_B193():
        OP_97(0xFE, 0xFFFFF254, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B193)
    Sleep(300)

    def lambda_B1B0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B1B0)
    WaitChrThread(0xFE, 1)

    def lambda_B1C5():
        OP_97(0xFE, 0xFFFFFC18, 0x0, 0x3E8, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B1C5)
    WaitChrThread(0xFE, 1)
    SetScenarioFlags(0x0, 0)

    def lambda_B1E6():
        OP_97(0xFE, 0x0, 0x0, 0x4650, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B1E6)
    WaitChrThread(0xFE, 1)

    def lambda_B204():

        label("loc_B204")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_B204")

    QueueWorkItem2(0xFE, 2, lambda_B204)
    Return()

    # Function_65_B18E end

    def Function_66_B212(): pass

    label("Function_66_B212")


    def lambda_B217():
        OP_97(0xFE, 0xFFFFF448, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B217)
    Sleep(300)

    def lambda_B234():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B234)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_AD(0x0)
    Sleep(100)

    def lambda_B256():
        OP_97(0xFE, 0x0, 0x0, 0x4268, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B256)
    WaitChrThread(0xFE, 1)

    def lambda_B274():

        label("loc_B274")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_B274")

    QueueWorkItem2(0xFE, 2, lambda_B274)
    Return()

    # Function_66_B212 end

    def Function_67_B282(): pass

    label("Function_67_B282")


    def lambda_B287():
        OP_97(0xFE, 0xFFFFEDA4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B287)
    Sleep(400)

    def lambda_B2A4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B2A4)
    WaitChrThread(0xFE, 1)

    def lambda_B2B9():
        OP_97(0xFE, 0xFFFFFC18, 0x0, 0x3E8, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B2B9)
    WaitChrThread(0xFE, 1)
    SetScenarioFlags(0x0, 1)

    def lambda_B2DA():
        OP_97(0xFE, 0x0, 0x0, 0x3F48, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B2DA)
    WaitChrThread(0xFE, 1)

    def lambda_B2F8():

        label("loc_B2F8")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_B2F8")

    QueueWorkItem2(0xFE, 2, lambda_B2F8)
    Return()

    # Function_67_B282 end

    def Function_68_B306(): pass

    label("Function_68_B306")


    def lambda_B30B():
        OP_97(0xFE, 0xFFFFEF98, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B30B)
    Sleep(400)

    def lambda_B328():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B328)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_AD(0x1)
    Sleep(100)

    def lambda_B34A():
        OP_97(0xFE, 0x0, 0x0, 0x3B60, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B34A)
    WaitChrThread(0xFE, 1)

    def lambda_B368():

        label("loc_B368")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_B368")

    QueueWorkItem2(0xFE, 2, lambda_B368)
    Return()

    # Function_68_B306 end

    def Function_69_B376(): pass

    label("Function_69_B376")


    def lambda_B37B():
        OP_97(0xFE, 0xFFFFE8F4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B37B)
    Sleep(500)

    def lambda_B398():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B398)
    WaitChrThread(0xFE, 1)

    def lambda_B3AD():
        OP_97(0xFE, 0xFFFFFC18, 0x0, 0x3E8, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B3AD)
    WaitChrThread(0xFE, 1)
    SetScenarioFlags(0x0, 2)

    def lambda_B3CE():
        OP_97(0xFE, 0x0, 0x0, 0x3B60, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B3CE)
    WaitChrThread(0xFE, 1)

    def lambda_B3EC():

        label("loc_B3EC")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_B3EC")

    QueueWorkItem2(0xFE, 2, lambda_B3EC)
    Return()

    # Function_69_B376 end

    def Function_70_B3FA(): pass

    label("Function_70_B3FA")


    def lambda_B3FF():
        OP_97(0xFE, 0xFFFFEAE8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B3FF)
    Sleep(500)

    def lambda_B41C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B41C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_AD(0x2)
    Sleep(100)

    def lambda_B43E():
        OP_97(0xFE, 0x0, 0x0, 0x3778, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B43E)
    WaitChrThread(0xFE, 1)

    def lambda_B45C():

        label("loc_B45C")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_B45C")

    QueueWorkItem2(0xFE, 2, lambda_B45C)
    Return()

    # Function_70_B3FA end

    def Function_71_B46A(): pass

    label("Function_71_B46A")


    def lambda_B46F():
        OP_95(0xFE, 111000, 0, -110500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B46F)
    WaitChrThread(0xFE, 1)

    def lambda_B48D():
        OP_95(0xFE, 113000, 0, -110500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B48D)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_71_B46A end

    def Function_72_B4A7(): pass

    label("Function_72_B4A7")


    def lambda_B4AC():
        OP_95(0xFE, 109000, 0, -130500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B4AC)
    WaitChrThread(0xFE, 1)

    def lambda_B4CA():
        OP_95(0xFE, 100000, 0, -130500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B4CA)
    Sleep(3200)

    def lambda_B4E7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B4E7)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_72_B4A7 end

    def Function_73_B4F8(): pass

    label("Function_73_B4F8")


    def lambda_B4FD():
        OP_95(0xFE, 109000, -600, -130500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B4FD)
    WaitChrThread(0xFE, 1)

    def lambda_B51B():
        OP_95(0xFE, 103000, -600, -130500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B51B)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_73_B4F8 end

    def Function_74_B535(): pass

    label("Function_74_B535")


    def lambda_B53A():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFC43C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B53A)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_AD(0x0)

    def lambda_B562():
        OP_97(0xFE, 0xFFFFDCD8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B562)
    Sleep(2700)

    def lambda_B57F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B57F)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_74_B535 end

    def Function_75_B590(): pass

    label("Function_75_B590")


    def lambda_B595():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFC43C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B595)
    WaitChrThread(0xFE, 1)

    def lambda_B5B3():
        OP_97(0xFE, 0xFFFFF8F8, 0x0, 0xFFFFF8F8, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B5B3)
    WaitChrThread(0xFE, 1)
    SetScenarioFlags(0x0, 0)

    def lambda_B5D4():
        OP_97(0xFE, 0xFFFFDCD8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B5D4)
    Sleep(2700)

    def lambda_B5F1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B5F1)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_75_B590 end

    def Function_76_B602(): pass

    label("Function_76_B602")


    def lambda_B607():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B607)
    WaitChrThread(0xFE, 1)
    Sleep(700)

    def lambda_B628():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFFA88, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B628)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_AD(0x1)

    def lambda_B650():
        OP_97(0xFE, 0xFFFFDCD8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B650)
    Sleep(2800)

    def lambda_B66D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B66D)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_76_B602 end

    def Function_77_B67E(): pass

    label("Function_77_B67E")


    def lambda_B683():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFBFF0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B683)
    WaitChrThread(0xFE, 1)

    def lambda_B6A1():
        OP_97(0xFE, 0xFFFFF8F8, 0x0, 0xFFFFF8F8, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B6A1)
    WaitChrThread(0xFE, 1)
    SetScenarioFlags(0x0, 1)

    def lambda_B6C2():
        OP_97(0xFE, 0xFFFFDCD8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B6C2)
    Sleep(2800)

    def lambda_B6DF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B6DF)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_77_B67E end

    def Function_78_B6F0(): pass

    label("Function_78_B6F0")


    def lambda_B6F5():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFC694, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B6F5)
    WaitChrThread(0xFE, 1)
    Sleep(1100)

    def lambda_B716():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF510, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B716)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_AD(0x2)

    def lambda_B73E():
        OP_97(0xFE, 0xFFFFDCD8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B73E)
    Sleep(2900)

    def lambda_B75B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B75B)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_78_B6F0 end

    def Function_79_B76C(): pass

    label("Function_79_B76C")


    def lambda_B771():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFBBA4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B771)
    WaitChrThread(0xFE, 1)
    Sleep(500)

    def lambda_B792():
        OP_97(0xFE, 0xFFFFF8F8, 0x0, 0xFFFFF8F8, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B792)
    WaitChrThread(0xFE, 1)
    SetScenarioFlags(0x0, 2)

    def lambda_B7B3():
        OP_97(0xFE, 0xFFFFDCD8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B7B3)
    Sleep(2900)

    def lambda_B7D0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B7D0)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_79_B76C end

    def Function_80_B7E1(): pass

    label("Function_80_B7E1")

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
        "#12P#10101FIt started …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00003F……Ah.\x02\x03",
            "#00000FBut, Arios\x01",
            "I have heard of being called\x01",
            "I wish I was called to Professor Ian.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202F#5PMoreover, in the name of \"Mr. bear beard\"\x01",
            "It seems to be known.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FAt the international conference, various agreements and\x01",
            "Agreement may be exchanged.\x02\x03",
            "#00100FIn that case, existing international law and\x01",
            "In accordance with international customary law etc.\x01",
            "It is necessary to judge whether it is valid or not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00005FI see……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FAn advisor for that\x01",
            "That is the beard beard teacher.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FBut it is good to start ……\x01",
            "Indeed it seems to be a little difficult story\x01",
            "You are trying it.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x2E, 0x10E, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x2E,
        (
            "#00603F#11PWell, regarding the contents of the meeting\x01",
            "It is not where we are involved.\x02\x03",
            "#00600FWhether this trade meeting finished successfully,\x01",
            "Please just concentrate on it.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-1500, 1300, -127550, 1500)

    def lambda_BCAB():
        TurnDirection(0x101, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BCAB)
    Sleep(50)

    def lambda_BCBB():
        TurnDirection(0x102, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_BCBB)
    Sleep(50)

    def lambda_BCCB():
        TurnDirection(0x109, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_BCCB)
    Sleep(50)

    def lambda_BCDB():
        TurnDirection(0x103, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_BCDB)
    Sleep(50)

    def lambda_BCEB():
        TurnDirection(0x105, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_BCEB)
    Sleep(50)

    def lambda_BCFB():
        TurnDirection(0x104, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_BCFB)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00001F#6PYes, I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00101FThen,\x01",
            "According to the meeting?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2E,
        (
            "#00604F#11POh, to you\x01",
            "34F, 35F, 36F\x01",
            "I will have patrols throughout.\x02\x03",
            "#00602FOnce, your status is\x01",
            "It is a situation that tells all officials.\x02\x03",
            "Staff of heads of state\x01",
            "Even the invited media and so on\x01",
            "You should try talking about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10100FOK!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2E,
        (
            "#00603F#11PThen I will return to 34F.\x02\x03",
            "#00600F……goddess#4REidos#Protection of.\x01",
            "Please contact me if there is something.\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x2E, 0xDAC, 0xFFFE0430, 0x1F4)
    OP_68(9000, 1300, -130000, 4000)

    def lambda_BEFD():
        OP_95(0xFE, 5500, 0, -130000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_BEFD)
    WaitChrThread(0x2E, 1)

    def lambda_BF1B():
        OP_95(0xFE, 11500, 0, -130000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_BF1B)
    Sleep(2000)

    def lambda_BF38():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_BF38)
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
            "#00008F#5P…… After all, Mr. Dudley\x01",
            "She seems to think there is something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#00103FYeah ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211F#5PThere is this dubious movement this much\x01",
            "Whether it is unnatural that there is nothing … …\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(150)

    ChrTalk(
        0x109,
        (
            "#12P#10101FApparently put your energy\x01",
            "It seems necessary to go patrol!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C080():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_C080)
    Sleep(50)

    def lambda_C090():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_C090)
    Sleep(50)

    def lambda_C0A0():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_C0A0)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x103, 0)

    ChrTalk(
        0x104,
        "#6P#00304FYou know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10300FWould you like to start patrolling now?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#5P#00001FOh, as I spinning all the way\x01",
            "Let's talk with people concerned.\x02",
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

    # Function_80_B7E1 end

    def Function_81_C1D2(): pass

    label("Function_81_C1D2")

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
            "#11P#00000FAlright ……\x01",
            "Was this one round?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FFor now\x01",
            "There seems to be no problem in particular.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00302FOh, with this condition again,\x01",
            "Let's look around and see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FI see …\x02\x03",
            "#00108F…… For the conference\x01",
            "I wonder what's going on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00006FThat's right, the mayor and the chairman\x01",
            "I think I am trying hard but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00201FThe problem is \"Chairman of Iron Blood\"\x01",
            "Is it Rock Smith President?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FWell, at break time\x01",
            "Why do not you ask someone?\x02",
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

    # Function_81_C1D2 end

    def Function_82_C46A(): pass

    label("Function_82_C46A")

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
            "#11P#00000FAlright ……\x01",
            "Was this one round?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FFor now\x01",
            "There seems to be no problem in particular.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00302FOh, with this condition again,\x01",
            "Let's look around and see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FI see …\x02\x03",
            "#00108F…… For the conference\x01",
            "I wonder what's going on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00006FThat's right, the mayor and the chairman\x01",
            "I think I am trying hard but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00201FThe problem is \"Chairman of Iron Blood\"\x01",
            "Is it Rock Smith President?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FWell, at break time\x01",
            "Why do not you ask someone?\x02",
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

    # Function_82_C46A end

    def Function_83_C702(): pass

    label("Function_83_C702")

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
        "#5P─ ─ We were waiting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#5PCrossbell Police,\x01",
            "Are you from the Special Affairs Division?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00001F……Yes.\x01",
            "Is this President 's Highness?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#5PYeah, if you come\x01",
            "I am told to go through.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x15, 0x0, 0x1F4)

    def lambda_C88A():
        OP_95(0xFE, -3200, 0, 28500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_C88A)
    WaitChrThread(0x15, 1)
    OP_93(0x15, 0xB4, 0x1F4)

    ChrTalk(
        0x15,
        "#5PPlease come inside.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#11P#00003FWell then ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00100FExcuse me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10108F(One of the largest continents,\x01",
            "Is it the leader of Calvert? …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#00306F(As expected, only a little\x01",
            "I got nervous … …)\x02",
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

    # Function_83_C702 end

    def Function_84_CA0E(): pass

    label("Function_84_CA0E")


    def lambda_CA13():
        OP_95(0xFE, -3200, 0, 27000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_CA13)
    WaitChrThread(0xFE, 1)

    def lambda_CA31():
        OP_95(0xFE, -5500, 0, 27000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_CA31)
    Sleep(600)

    def lambda_CA4E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_CA4E)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_84_CA0E end

    def Function_85_CA5F(): pass

    label("Function_85_CA5F")

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
        "#5P── Thank you for your patience.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#5PThe Osborne Chancellor's Room\x01",
            "I think that it will be on the other side.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_CC28():

        label("loc_CC28")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_CC28")

    QueueWorkItem2(0x101, 2, lambda_CC28)

    def lambda_CC3A():

        label("loc_CC3A")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_CC3A")

    QueueWorkItem2(0x102, 2, lambda_CC3A)
    Sleep(50)

    def lambda_CC4F():

        label("loc_CC4F")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_CC4F")

    QueueWorkItem2(0x103, 2, lambda_CC4F)
    Sleep(50)

    def lambda_CC64():

        label("loc_CC64")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_CC64")

    QueueWorkItem2(0x109, 2, lambda_CC64)
    Sleep(50)

    def lambda_CC79():

        label("loc_CC79")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_CC79")

    QueueWorkItem2(0x105, 2, lambda_CC79)
    Sleep(50)

    def lambda_CC8E():

        label("loc_CC8E")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_CC8E")

    QueueWorkItem2(0x104, 2, lambda_CC8E)

    ChrTalk(
        0x101,
        "#11P#00011FOh, hi.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00103FThank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        "#5PNo, thank you.\x02",
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

    def lambda_CDC7():
        TurnDirection(0x105, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_CDC7)
    Sleep(50)

    def lambda_CDD7():
        TurnDirection(0x109, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_CDD7)
    Sleep(50)

    def lambda_CDE7():
        TurnDirection(0x104, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_CDE7)
    Sleep(50)

    def lambda_CDF7():
        TurnDirection(0x102, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_CDF7)
    Sleep(50)

    def lambda_CE07():
        TurnDirection(0x101, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_CE07)
    Sleep(50)

    def lambda_CE17():
        TurnDirection(0x103, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_CE17)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)

    ChrTalk(
        0x105,
        (
            "#10309F#11PHaha, per person is good\x01",
            "As expected it is the top of a big country.\x02\x03",
            "#10302FIt is an outrageous raccoon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106FWajima ……\x01",
            "I do not say rare things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#11PBut it was quite blatant.\x02\x03",
            "#00211FTo intimidate us\x01",
            "It seems not to be the purpose … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#5PPerhaps, it is better to arrange the appearance\x01",
            "I think that was the purpose …\x02\x03",
            "#00103FPresident of the Republic,\x01",
            "To us who contributed to solving the case incident\x01",
            "The appearance of giving a medal … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FCrossbell incidents\x01",
            "Case for us ……\x02\x03",
            "#00001FThat is to say that the territorial rights as a religious country\x01",
            "Have you reinforced again …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#5PCome on … …\x01",
            "Did you call it for that?\x02\x03",
            "#00301FThe top of a big country is\x01",
            "After all it is ridiculous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#11PWell, with autonomous state council members\x01",
            "Obviously the case seems to be wrong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10108F… … If you are the prime minister\x01",
            "What kind of story is there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001F……I do not understand.\x01",
            "Anyway, let 's enclose R \\.\x02",
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

    # Function_85_CA5F end

    def Function_86_D1C0(): pass

    label("Function_86_D1C0")


    def lambda_D1C5():
        OP_95(0xFE, -3200, 0, 27000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D1C5)

    def lambda_D1DF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D1DF)
    WaitChrThread(0xFE, 1)

    def lambda_D1F4():
        OP_95(0xFE, -1500, 0, 26400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D1F4)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_86_D1C0 end

    def Function_87_D215(): pass

    label("Function_87_D215")


    def lambda_D21A():
        OP_95(0xFE, -3200, 0, 27000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D21A)

    def lambda_D234():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D234)
    WaitChrThread(0xFE, 1)

    def lambda_D249():
        OP_95(0xFE, -1200, 0, 27700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D249)
    WaitChrThread(0xFE, 1)

    def lambda_D267():

        label("loc_D267")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_D267")

    QueueWorkItem2(0xFE, 2, lambda_D267)
    Return()

    # Function_87_D215 end

    def Function_88_D275(): pass

    label("Function_88_D275")


    def lambda_D27A():
        OP_95(0xFE, -3200, 0, 27000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D27A)

    def lambda_D294():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D294)
    WaitChrThread(0xFE, 1)

    def lambda_D2A9():
        OP_95(0xFE, 100, 0, 26800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D2A9)
    WaitChrThread(0xFE, 1)

    def lambda_D2C7():

        label("loc_D2C7")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_D2C7")

    QueueWorkItem2(0xFE, 2, lambda_D2C7)
    Return()

    # Function_88_D275 end

    def Function_89_D2D5(): pass

    label("Function_89_D2D5")


    def lambda_D2DA():
        OP_95(0xFE, -3200, 0, 27000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D2DA)

    def lambda_D2F4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D2F4)
    WaitChrThread(0xFE, 1)

    def lambda_D309():
        OP_95(0xFE, 400, 0, 28100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D309)
    WaitChrThread(0xFE, 1)

    def lambda_D327():

        label("loc_D327")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_D327")

    QueueWorkItem2(0xFE, 2, lambda_D327)
    Return()

    # Function_89_D2D5 end

    def Function_90_D335(): pass

    label("Function_90_D335")


    def lambda_D33A():
        OP_95(0xFE, -3200, 0, 27000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D33A)

    def lambda_D354():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D354)
    WaitChrThread(0xFE, 1)

    def lambda_D369():
        OP_95(0xFE, -1500, 0, 25100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D369)
    WaitChrThread(0xFE, 1)

    def lambda_D387():

        label("loc_D387")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_D387")

    QueueWorkItem2(0xFE, 2, lambda_D387)
    Return()

    # Function_90_D335 end

    def Function_91_D395(): pass

    label("Function_91_D395")


    def lambda_D39A():
        OP_95(0xFE, -3200, 0, 27000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D39A)

    def lambda_D3B4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D3B4)
    WaitChrThread(0xFE, 1)

    def lambda_D3C9():
        OP_95(0xFE, 100, 0, 25500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D3C9)
    WaitChrThread(0xFE, 1)

    def lambda_D3E7():

        label("loc_D3E7")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_D3E7")

    QueueWorkItem2(0xFE, 2, lambda_D3E7)
    Return()

    # Function_91_D395 end

    def Function_92_D3F5(): pass

    label("Function_92_D3F5")

    EventBegin(0x0)

    def lambda_D3FC():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_D3FC)
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
            "#00001F(Is that the room of the Prime Minister? …)\x02\x03",
            "#00003F(Perhaps, if I visit there\x01",
            "The break time will be over. )\x02\x03",
            "#00008F(Is there anything else you have left behind?)\x02",
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

    # Function_92_D3F5 end

    def Function_93_D504(): pass

    label("Function_93_D504")

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
        "#11PCrossbell Police, Special Affairs Support Division?\x02",
    )

    CloseMessageWindow()
    OP_93(0x16, 0x0, 0x1F4)

    def lambda_D5EE():
        OP_95(0xFE, 111300, 0, -101000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_D5EE)
    WaitChrThread(0x16, 1)
    OP_93(0x16, 0xE1, 0x1F4)

    ChrTalk(
        0x16,
        (
            "#5PHis Excellency is waiting for you.\x01",
            "Stay in as it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00001FYes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00104FWell then, excuse us\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00211F(… seems like a great deal.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F(Truly an imperial soldier.\x01",
            "It is wastefully intimidating. )\x02",
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
            "#6P#00003F#6PExcuse me.\x01",
            "His Excellency Osborne.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F#6PCrossbell Police, Special Affairs Support Division,\x01",
            "We invited you by invitation.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x2F,
        "#07404F#11P#N… …. Come in.\x02",
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

    def lambda_DA7C():
        OP_96(0xFE, 0x2673C, 0x0, 0x1AA90, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DA7C)
    Sleep(300)

    def lambda_DA99():
        OP_96(0xFE, 0x266D8, 0x0, 0x1AE78, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DA99)
    Sleep(50)

    def lambda_DAB6():
        OP_96(0xFE, 0x260FC, 0x0, 0x1AA90, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_DAB6)
    Sleep(100)

    def lambda_DAD3():
        OP_96(0xFE, 0x26098, 0x0, 0x1AE78, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_DAD3)
    Sleep(100)

    def lambda_DAF0():
        OP_96(0xFE, 0x26548, 0x0, 0x1A450, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_DAF0)
    Sleep(100)

    def lambda_DB0D():
        OP_96(0xFE, 0x26098, 0x0, 0x1A450, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_DB0D)
    WaitChrThread(0x109, 1)

    def lambda_DB2B():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_DB2B)
    WaitChrThread(0x105, 1)

    def lambda_DB3C():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_DB3C)
    Sleep(500)

    ChrTalk(
        0x2F,
        (
            "#07400F#11P── This scenery is superb.\x02\x03",
            "From this height on the ground\x01",
            "Buildings that can be overlooked\x01",
            "What humans can produce … …\x02\x03",
            "#07404FHuhu, once boasted of prosperity\x01",
            "It may be a matter of business reaching ancient civilization.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000F……surely.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00200F1200 years ago\x01",
            "It is about Zemuria civilization.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F#6POh, anything like magic\x01",
            "It seems there was a useful civilization.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2F,
        (
            "#07400F#11PAs a mere utopia\x01",
            "It seems not necessarily.\x02\x03",
            "#07404FLast year, when Libert's strange change\x01",
            "A huge floating city that appeared …\x02\x03",
            "That was built in the days of Zemria,\x01",
            "And it seems that it was sealed with the hand of man.\x02\x03",
            "#07401FAs a symbol of human possibility and foolishness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00001FPossibility of people and stupidity ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#6PThat……\x01",
            "You are quite familiar?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2F,
        (
            "#07404F#11PHuh, not that much.\x02\x03",
            "#07400FEspecially for crossbells\x01",
            "Joachim as much as a priest\x01",
            "It has not reached the truth.\x02",
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
        "#6P#00013F…!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00208FSuch a thing ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2F,
        (
            "#07404F#11PHuh, and besides\x01",
            "Because there is something I do not know\x01",
            "The world is interesting.\x02\x03",
            "A game where all of the hands could be seen#4Rgame#Such\x01",
            "It is the extreme of boredom.\x02\x03",
            "#07400FDo not you think so?\x01",
            "Wadi Hemisphere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#N#10306F…… Huh.\x01",
            "Do you know my name, too?\x02\x03",
            "#10300FNo, by the name only\x01",
            "Is not it strange?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x2F,
        (
            "#07400F#11PNo, I'm curious\x01",
            "It is only that there is nothing.\x02\x03",
            "#07404FThe person who inherits the \"fighting spirit\"\x01",
            "Rather, do not intrigue me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#6P… …. you …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006F\"Imperial Army Information Bureau\" … …\x02\x03",
            "#00001FA wonderful information gathering ability\x01",
            "You seem to have it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2F,
        "#07404F#11PGiggle\x02",
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
            "Representative of Eleven Empire Government,\x01",
            "It is Gillius Osbourne.\x02\x03",
            "From you Lecter\x01",
            "I heard it variously.\x02\x03",
            "Then the remaining break time,\x01",
            "Shall we talk to you?\x02",
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
            "#12P#00003F… … So, your honorable chairperson.\x02\x03",
            "#00001FTo go out with a story is\x01",
            "What on earth are you …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00211FApparently, most things\x01",
            "I already know about it.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)

    ChrTalk(
        0x2F,
        (
            "#07404F#11PWhat a simple chat.\x02\x03",
            "#07400FOr a consciousness survey\x01",
            "It could be paraphrased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10105FConsciousness survey …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2F,
        (
            "#07403F#11POh, straightforward#4RBreakfast#Let's ask.\x02\x03",
            "#07402F…… You guys are this crossbell\x01",
            "How much do you think you have?\x02",
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
        "#12P#00013F#4SHousehold appliances\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10306FIt's also a blatant question …\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x2F, 0x1)
    Sleep(300)

    ChrTalk(
        0x2F,
        (
            "#07400F#5PHuh, there is no other choice.\x02\x03",
            "#07403FHowever, the prosperity of prosperity is always in history -\x01",
            "There are no countries that have not perished.\x02\x03",
            "Much less by the power revolution\x01",
            "Everything began to accelerate\x01",
            "In this era ……\x02\x03",
            "#07401FHow far is this relationship\x01",
            "Do you think you can stay as it is?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#6P…. That's … …\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x32, 0x0, 0xBB8, 0x96)

    ChrTalk(
        0x109,
        (
            "#6P#10107F─ ─ Yes, forever!\x02\x03",
            "The will to protect\x01",
            "If you are in the people of the autonomous province!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(150)

    ChrTalk(
        0x101,
        "#11P#00005FNoel …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2F,
        (
            "#07400F#5PYes, the will is always important.\x02\x03",
            "Sometimes#4RVigilance#Turn over,\x01",
            "You can also move history itself\x01",
            "It will not be rare.\x02\x03",
            "#07404FA person is not helpless.\x01",
            "I also believe in that possibility.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    ChrTalk(
        0x109,
        "#6P#10100FWell then, then …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2F,
        (
            "#07400F#5P─ ─ But, that intention\x01",
            "What if you collide with each other?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x32, 0x0, 0xBB8, 0x96)

    ChrTalk(
        0x109,
        "#6P#10111F…!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2F,
        (
            "#07401F#5PEasy - small intention\x01",
            "Swallowed by the greater will,\x01",
            "I will increase that fire.\x02\x03",
            "#07404FThe fire that was born so\x01",
            "When a lot of it appears on the ground …\x02\x03",
            "Every kind of justice and ethics melts in burning,\x01",
            "The world is enveloped by a flame on one side.\x02\x03",
            "#07402F── Such a sight is easy\x01",
            "Can not you see it visually?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00210F#40W……Ahh………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10110F#40W… …. Uu … …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00311F#6P#30W………………………….\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#12P#00003F#30W……surely……\x01",
            "Compared to the Empire and the Republic\x01",
            "It may be \"a small will\" …\x02\x03",
            "#00008FBut … a big flame makes a small flame\x01",
            "It will not necessarily be swallowed.\x02\x03",
            "#00007F#20WOnce dismissed the invasion of the empire\x01",
            "Like the Liber Kingdom …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F#6PAh…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10304F\"One hundred day campaign\" 12 years ago … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2F,
        (
            "#07404F#5PHuh, that's right.\x01",
            "\"Willingness\" is questioned in will.\x02\x03",
            "Libert's small but strong intention\x01",
            "To the greatly disarrayed will of the empire\x01",
            "Brilliant blow#2ROr#That means that.\x02\x03",
            "It certainly is for Crossbell\x01",
            "It can be said as a lesson.\x02\x03",
            "#07402F─ ─ to the people of Crossbell\x01",
            "The pride and strength of the people of Libert is\x01",
            "I do not know if it is equipped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00013F…!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#6P….\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x2F, 0x0)
    Sleep(300)

    ChrTalk(
        0x2F,
        (
            "#07404F#11PHuhu, break time is over.\x01",
            "Let's keep the story to this point.\x02\x03",
            "#07400F─ ─ Oh, from the Imperial Government\x01",
            "I do not mean to give a medal, in particular.\x02\x03",
            "If you give a medal to \"commoner\" poorly\x01",
            "The aristocratic power is noisy.\x02",
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
        "#5P… …. You guys were lucky.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHonorable so much\x01",
            "It is not much to be seen.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F0AB():

        label("loc_F0AB")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_F0AB")

    QueueWorkItem2(0x101, 2, lambda_F0AB)

    def lambda_F0BD():

        label("loc_F0BD")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_F0BD")

    QueueWorkItem2(0x102, 2, lambda_F0BD)
    Sleep(50)

    def lambda_F0D2():

        label("loc_F0D2")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_F0D2")

    QueueWorkItem2(0x103, 2, lambda_F0D2)

    def lambda_F0E4():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_F0E4)
    Sleep(50)

    def lambda_F0F4():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_F0F4)

    def lambda_F101():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_F101)

    ChrTalk(
        0x101,
        "#12P#00005FHuh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00301FHey … what kind of joke?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PYou guys\x01",
            "It seems to have liked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PIt may be a heavy word\x01",
            "Take it first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PFrom my point of view\x01",
            "It is not what I could say.\x02",
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

    def lambda_F2D7():
        TurnDirection(0x102, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_F2D7)
    Sleep(50)

    def lambda_F2E7():
        TurnDirection(0x104, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_F2E7)
    Sleep(50)

    def lambda_F2F7():
        TurnDirection(0x101, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F2F7)
    Sleep(50)

    def lambda_F307():
        TurnDirection(0x109, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_F307)
    Sleep(50)

    def lambda_F317():
        TurnDirection(0x105, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_F317)
    Sleep(50)

    def lambda_F327():
        TurnDirection(0x103, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_F327)
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
        "#5P#00106F… … There was nothing wrong.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00310FWell, it 's too much a thing … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00006F…… Oh, what is it?\x01",
            "I feel that the standing dimension is different.\x02\x03",
            "#00001F── Thio, are you OK?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00206FYes … somehow.\x02\x03",
            "#00208FIt came from that person\x01",
            "The image of the flame is too strong\x01",
            "I got a dizziness, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#10106FI do not mind … … even me\x01",
            "Things that I felt like I saw something ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10308F#5P\"Chancellor of Iron Blood\"? …\x01",
            "It is exactly like a monster.\x02\x03",
            "#10303FIf it is about crossbell\x01",
            "It looks like I'm drinking a bite.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#11P#00003F─ ─ But we need us#2RNone#To\x01",
            "It will not have been called.\x02\x03",
            "Even the president is … …\x01",
            "It was also said that we were interested\x01",
            "I think that it is not a lie.\x02\x03",
            "#00000FSo, if you had a good study\x01",
            "You may as well think that you should think.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F632():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_F632)
    Sleep(0)

    def lambda_F642():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_F642)
    Sleep(0)

    def lambda_F652():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_F652)
    Sleep(0)

    def lambda_F662():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_F662)
    Sleep(0)

    def lambda_F672():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_F672)
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
        "#10302F#5PHuh, it does not say that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00104F…… That's where you are\x01",
            "I can not imitate it a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00309FAh……\x01",
            "It is too positive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#10101FBut, surely …\x01",
            "It can not be helped even if it is depressed!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00202FI agree……\x01",
            "I have to make good use of the lessons learned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00003FAnyway, the break time is over.\x02\x03",
            "#00001FReturn to Mr. Dudley\x01",
            "Let me tell you the results of the interview.\x02",
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

    # Function_93_D504 end

    def Function_94_F8ED(): pass

    label("Function_94_F8ED")


    def lambda_F8F2():
        OP_95(0xFE, 111300, 0, -102500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F8F2)
    WaitChrThread(0xFE, 1)

    def lambda_F910():
        OP_95(0xFE, 113000, 0, -102500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F910)
    Sleep(600)

    def lambda_F92D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F92D)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_94_F8ED end

    def Function_95_F93E(): pass

    label("Function_95_F93E")


    def lambda_F943():
        OP_96(0xFE, 0x24540, 0x0, 0x19E10, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F943)

    def lambda_F95D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F95D)
    WaitChrThread(0xFE, 1)

    def lambda_F972():
        OP_95(0xFE, 151000, 0, 105200, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F972)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_95_F93E end

    def Function_96_F993(): pass

    label("Function_96_F993")


    def lambda_F998():
        OP_96(0xFE, 0x24540, 0x0, 0x19E10, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F998)

    def lambda_F9B2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F9B2)
    WaitChrThread(0xFE, 1)

    def lambda_F9C7():
        OP_95(0xFE, 151000, 0, 106300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F9C7)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_96_F993 end

    def Function_97_F9E8(): pass

    label("Function_97_F9E8")


    def lambda_F9ED():
        OP_96(0xFE, 0x24540, 0x0, 0x19E10, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F9ED)

    def lambda_FA07():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FA07)
    WaitChrThread(0xFE, 1)

    def lambda_FA1C():
        OP_95(0xFE, 150100, 0, 104600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FA1C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_97_F9E8 end

    def Function_98_FA3D(): pass

    label("Function_98_FA3D")


    def lambda_FA42():
        OP_96(0xFE, 0x24540, 0x0, 0x19E10, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FA42)

    def lambda_FA5C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FA5C)
    WaitChrThread(0xFE, 1)

    def lambda_FA71():
        OP_95(0xFE, 150100, 0, 106900, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FA71)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_98_FA3D end

    def Function_99_FA92(): pass

    label("Function_99_FA92")


    def lambda_FA97():
        OP_96(0xFE, 0x24540, 0x0, 0x19E10, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FA97)

    def lambda_FAB1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FAB1)
    WaitChrThread(0xFE, 1)

    def lambda_FAC6():
        OP_95(0xFE, 149200, 0, 105200, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FAC6)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_99_FA92 end

    def Function_100_FAE7(): pass

    label("Function_100_FAE7")


    def lambda_FAEC():
        OP_96(0xFE, 0x24540, 0x0, 0x19E10, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FAEC)

    def lambda_FB06():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FB06)
    WaitChrThread(0xFE, 1)

    def lambda_FB1B():
        OP_95(0xFE, 149200, 0, 106300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FB1B)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_100_FAE7 end

    def Function_101_FB3C(): pass

    label("Function_101_FB3C")


    def lambda_FB41():
        OP_95(0xFE, 110500, 0, -102500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FB41)

    def lambda_FB5B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FB5B)
    WaitChrThread(0xFE, 1)

    def lambda_FB70():
        OP_95(0xFE, 109100, 0, -103400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FB70)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_101_FB3C end

    def Function_102_FB91(): pass

    label("Function_102_FB91")


    def lambda_FB96():
        OP_95(0xFE, 110500, 0, -102500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FB96)

    def lambda_FBB0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FBB0)
    WaitChrThread(0xFE, 1)

    def lambda_FBC5():
        OP_95(0xFE, 109300, 0, -102300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FBC5)
    WaitChrThread(0xFE, 1)

    def lambda_FBE3():

        label("loc_FBE3")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_FBE3")

    QueueWorkItem2(0xFE, 2, lambda_FBE3)
    Return()

    # Function_102_FB91 end

    def Function_103_FBF1(): pass

    label("Function_103_FBF1")


    def lambda_FBF6():
        OP_95(0xFE, 110500, 0, -102500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FBF6)

    def lambda_FC10():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FC10)
    WaitChrThread(0xFE, 1)

    def lambda_FC25():
        OP_95(0xFE, 107600, 0, -103100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FC25)
    WaitChrThread(0xFE, 1)

    def lambda_FC43():

        label("loc_FC43")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_FC43")

    QueueWorkItem2(0xFE, 2, lambda_FC43)
    Return()

    # Function_103_FBF1 end

    def Function_104_FC51(): pass

    label("Function_104_FC51")


    def lambda_FC56():
        OP_95(0xFE, 110500, 0, -102500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FC56)

    def lambda_FC70():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FC70)
    WaitChrThread(0xFE, 1)

    def lambda_FC85():
        OP_95(0xFE, 107300, 0, -102000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FC85)
    WaitChrThread(0xFE, 1)

    def lambda_FCA3():

        label("loc_FCA3")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_FCA3")

    QueueWorkItem2(0xFE, 2, lambda_FCA3)
    Return()

    # Function_104_FC51 end

    def Function_105_FCB1(): pass

    label("Function_105_FCB1")


    def lambda_FCB6():
        OP_95(0xFE, 110500, 0, -102500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FCB6)

    def lambda_FCD0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FCD0)
    WaitChrThread(0xFE, 1)

    def lambda_FCE5():
        OP_95(0xFE, 109000, 0, -101000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FCE5)
    WaitChrThread(0xFE, 1)

    def lambda_FD03():

        label("loc_FD03")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_FD03")

    QueueWorkItem2(0xFE, 2, lambda_FD03)
    Return()

    # Function_105_FCB1 end

    def Function_106_FD11(): pass

    label("Function_106_FD11")


    def lambda_FD16():
        OP_95(0xFE, 110500, 0, -102500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FD16)

    def lambda_FD30():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FD30)
    WaitChrThread(0xFE, 1)

    def lambda_FD45():
        OP_95(0xFE, 108000, 0, -100300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FD45)
    WaitChrThread(0xFE, 1)

    def lambda_FD63():

        label("loc_FD63")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_FD63")

    QueueWorkItem2(0xFE, 2, lambda_FD63)
    Return()

    # Function_106_FD11 end

    def Function_107_FD71(): pass

    label("Function_107_FD71")

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
        "#12P#10107F……is this……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#11P…… Professor Ian\x01",
            "As you were worried about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10308FTo the President and the President\x01",
            "I feel like I'm being pushed.\x02\x03",
            "#10301FIs there no clue to the objection?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#11P…… Actually, various autonomous state laws\x01",
            "It is true that there are structural defects.\x02\x03",
            "#00108FTherefore, even if you take care of yourself\x01",
            "Even if you are an uncle of Dieter\x01",
            "I guess it's hard to argue … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00006F── However, its structural defects\x01",
            "When autonomous state was established 70 years ago\x01",
            "It was pressed from two major powers.\x02\x03",
            "#00013FThat brute remark on that\x01",
            "I can not accept it at all … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#5P#00301FHuh, I guess it's a conviction.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2E,
        "#00603F#11P….\x02",
    )

    CloseMessageWindow()
    OP_93(0x2E, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x2E,
        (
            "#00601F#11PIn any case, the content of the meeting\x01",
            "It is not what we perceive.\x02\x03",
            "Now the meeting itself is safe,\x01",
            "Focus on finishing.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-1500, 1300, -127550, 1300)

    def lambda_1026E():
        TurnDirection(0x101, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1026E)
    Sleep(50)

    def lambda_1027E():
        TurnDirection(0x102, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1027E)
    Sleep(50)

    def lambda_1028E():
        TurnDirection(0x109, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1028E)
    Sleep(50)

    def lambda_1029E():
        TurnDirection(0x103, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1029E)
    Sleep(50)

    def lambda_102AE():
        TurnDirection(0x105, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_102AE)
    Sleep(50)

    def lambda_102BE():
        TurnDirection(0x104, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_102BE)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00001F#6P……Yes, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#00108FWell then, let's go patrol a whole -\x02",
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
            "#00603F#5PInvestigation One Section, Dudley.\x02\x03",
            "#00605F… … Emma?\x01",
            "What on earth were you ──\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x2E,
        "#00607F#5Pwhat……! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#6P(……what?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#00108F(It seems there was something ……)\x02",
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
            "#00606F#11P─ ─ \"Red constellation\" and \"Black moon\"\x01",
            "It seems that it moved from each base.\x02\x03",
            "#00601FIt seems that he overcame the monitoring of department 1.\x02",
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
        "#00005F#6PBecome\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x104,
        "#6P#00307Fwhat! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2E,
        (
            "#00603F#11PDismay#4RUchida#No …\x01",
            "This is also within the range of assumption.\x02\x03",
            "#00601FI will let you know something happens\x01",
            "Keep watchful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#6PRyo, OK.\x02",
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

    def lambda_106BA():
        OP_95(0xFE, 5500, 0, -130000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_106BA)
    Sleep(500)

    ChrTalk(
        0x2E,
        (
            "#5P#00603F#12A── Oh, that's right.\x02\x03",
            "#14A#00601FPreliminary police force\x01",
            "You can move it … ….\x02",
        )
    )

    WaitChrThread(0x2E, 1)

    def lambda_10732():
        OP_95(0xFE, 11500, 0, -130000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_10732)
    Sleep(2000)

    def lambda_1074F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_1074F)
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
            "#6P#00308FFucking …\x01",
            "Was it really moving?\x02\x03",
            "#00310FWhat on earth are you going to do ?! Is it?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_10876():
        TurnDirection(0x103, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_10876)
    Sleep(50)

    def lambda_10886():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_10886)
    Sleep(50)

    def lambda_10896():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_10896)
    Sleep(50)

    def lambda_108A6():
        TurnDirection(0x109, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_108A6)
    Sleep(50)

    def lambda_108B6():
        TurnDirection(0x105, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_108B6)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x103,
        "#11P#00208FRandy san ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11PRandy, calm down.\x02\x03",
            "#00001FEven though \"Red constellation\"\x01",
            "I do not think I'm going to set up here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#11PWell, the front of the building\x01",
            "The police force guards it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#11P#10101FNo doubt like this\x01",
            "To start a dispute … ….?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10306FWell, that is a bit too\x01",
            "I feel unnatural.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 60, -1, -1)
    Sleep(300)
    OP_82(0x64, 0x64, 0xBB8, 0x1F4)
    SetChrName("Voice of an old man")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#4S── What is it! Is it?\x07\x00\x02",
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

    def lambda_10ADD():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_10ADD)
    Sleep(50)

    def lambda_10AED():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_10AED)
    Sleep(50)

    def lambda_10AFD():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_10AFD)
    Sleep(50)

    def lambda_10B0D():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_10B0D)
    Sleep(50)

    def lambda_10B1D():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_10B1D)
    Sleep(50)

    def lambda_10B2D():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_10B2D)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x101,
        "#11P#00011FWhat is it …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00112F#11POh my god … ….?\x02",
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

    # Function_107_FD71 end

    def Function_108_10BBD(): pass

    label("Function_108_10BBD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_10BDB")
    OP_A1(0x2E, 0x7D0, 0x8, 0x8, 0x9, 0xA, 0x9, 0x8, 0xB, 0xC, 0xB)
    Jump("Function_108_10BBD")

    label("loc_10BDB")

    Return()

    # Function_108_10BBD end

    def Function_109_10BDC(): pass

    label("Function_109_10BDC")

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
        "#11P#00010FCut …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10106FIt is terrible …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#11PIt is irresponsible ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#00301F…… Well it's over there\x01",
            "I can make the surface skin thicker.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#11P…… But, there is no basis at all\x01",
            "It is not a suggestion.\x02\x03",
            "#00108FOnly in this way\x01",
            "I did not want it to be … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10308FHm, this is Ko Goro#2RShin#Gotcha\x01",
            "I feel it ….\x02",
        )
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_10F5A():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_10F5A)
    Sleep(50)

    def lambda_10F6A():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_10F6A)
    Sleep(50)

    def lambda_10F7A():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_10F7A)
    Sleep(50)

    def lambda_10F8A():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_10F8A)
    Sleep(50)

    def lambda_10F9A():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_10F9A)
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
        "#5P#00001FAt such time …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101F#11PFrom Mr. Dudley?\x02",
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
            "#00001FYes, at Bannings ─\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice of a man")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I'm Sergei.\x02",
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
            "#00005FSergei section manager?\x01",
            "What happened? -\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Sergei's voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I do not have time, I speak briefly.\x02\x03",
            "─ ─ We heard from Sonya.\x02\x03",
            "In the vicinity of both tangrams and Bellegard gate\x01",
            "The installed radar facilities were destroyed.\x02\x03",
            "A suspicious airship invading the autonomous state airspace\x01",
            "It is an anti-aircraft radar for capturing.\x02",
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
            "#00011F#3SI mean …!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Sergei's voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Apparently it was rumored\x01",
            "It seems to be the work of terrorists.\x02\x03",
            "I also told Dudley\x01",
            "Keep it for you too.\x02",
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
            "#00007FWow, I understand!\x02",
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
        "#00101F#11PWhere are you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00307FNo way, my uncle\x01",
            "Did you do something! Is it?\x02",
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
            "#11P#00013FNo,\x01",
            "Not that one ──\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 60, -1, -1)
    SetChrName("Male voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "── Everyone.\x01",
            "A little, are you sure?\x07\x00\x02",
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

    def lambda_11486():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_11486)
    Sleep(50)

    def lambda_11496():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_11496)
    Sleep(50)

    def lambda_114A6():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_114A6)
    Sleep(50)

    def lambda_114B6():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_114B6)
    Sleep(50)

    def lambda_114C6():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_114C6)
    Sleep(50)

    def lambda_114D6():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_114D6)
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

    # Function_109_10BDC end

    def Function_110_11528(): pass

    label("Function_110_11528")

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
        "#11P#00107FAh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10310Fthis is……\x01",
            "It turned out terrible.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        (
            "#5P#00203F…… Orchise Tower\x01",
            "It seems that control was robbed.\x02\x03",
            "#00201FYesterday's hacker's\x01",
            "It may be a work.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xE1, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#11P#00010FCum, we will also go!\x02\x03",
            "#00007FAnyway get off at 35 F\x01",
            "We must ensure the safety of the leaders!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_11729():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_11729)
    Sleep(50)

    def lambda_11739():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_11739)
    Sleep(50)

    def lambda_11749():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_11749)
    Sleep(50)

    def lambda_11759():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_11759)
    Sleep(50)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x109,
        "#12P#10107F── I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00307FIf the elevator is useless\x01",
            "It looks like only an emergency staircase!\x02",
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

    # Function_110_11528 end

    def Function_111_11813(): pass

    label("Function_111_11813")

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
            "#12P#10101FSure, until a while ago\x01",
            "You ought to have passed … ….!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        "#6P#00013FTio, can you go …! Is it?\x02",
    )

    CloseMessageWindow()

    def lambda_119AA():

        label("loc_119AA")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_119AA")

    QueueWorkItem2(0x102, 2, lambda_119AA)

    def lambda_119BC():

        label("loc_119BC")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_119BC")

    QueueWorkItem2(0x104, 2, lambda_119BC)

    def lambda_119CE():

        label("loc_119CE")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_119CE")

    QueueWorkItem2(0x109, 2, lambda_119CE)

    def lambda_119E0():

        label("loc_119E0")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_119E0")

    QueueWorkItem2(0x105, 2, lambda_119E0)

    def lambda_119F2():

        label("loc_119F2")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_119F2")

    QueueWorkItem2(0x101, 2, lambda_119F2)

    ChrTalk(
        0x103,
        "#11P#00201F…… I'll do it somehow.\x02",
    )

    CloseMessageWindow()

    def lambda_11A2D():
        OP_95(0xFE, -54700, 0, 2200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_11A2D)
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
            "Tio as a connector on the side of the shutter\x01",
            "A power cable was connected.\x07\x00\x02",
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
            "#00205F#30W#11P….\x02\x03",
            "#00203F#20W…… It's a little troublesome.\x02\x03",
            "#00201FBut, if this is somehow ……\x02",
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

    def lambda_11BD9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_11BD9)
    Sleep(50)

    def lambda_11BE9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_11BE9)
    Sleep(50)

    def lambda_11BF9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_11BF9)
    Sleep(50)

    def lambda_11C09():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_11C09)
    Sleep(50)

    def lambda_11C19():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_11C19)
    Sleep(500)

    ChrTalk(
        0x102,
        "#00102FOpen……!\x02",
    )

    CloseMessageWindow()
    OP_79(0xC)

    ChrTalk(
        0x104,
        "#00309FAs expected Tio!\x02",
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
            "#00206FNo, security\x01",
            "It was just set lower.\x02\x03",
            "#00208FBut with the cancellation now\x01",
            "Security of other doors\x01",
            "It has been strengthened.\x02\x03",
            "#00201FVery completely open\x01",
            "It may not be filled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#N#10306FThat's pretty well prepared ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#12P#00010FDamn\x01",
            "Anyway you will get down!\x02",
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

    # Function_111_11813 end

    def Function_112_11E58(): pass

    label("Function_112_11E58")


    def lambda_11E5D():
        OP_95(0xFE, -55700, 0, 3300, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11E5D)
    WaitChrThread(0xFE, 1)

    def lambda_11E7B():
        OP_95(0xFE, -55700, 0, 13500, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11E7B)
    WaitChrThread(0xFE, 1)

    def lambda_11E99():
        OP_95(0xFE, -52000, 0, 13500, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11E99)
    WaitChrThread(0xFE, 1)

    def lambda_11EB7():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11EB7)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_112_11E58 end

    def Function_113_11ED1(): pass

    label("Function_113_11ED1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11EEB")
    OP_A1(0x103, 0x7D0, 0x4, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_113_11ED1")

    label("loc_11EEB")

    Return()

    # Function_113_11ED1 end

    def Function_114_11EEC(): pass

    label("Function_114_11EEC")

    Sound(145, 2, 100, 0)
    Sleep(2000)
    Sound(143, 0, 70, 0)
    OP_24(0x91)
    Return()

    # Function_114_11EEC end

    def Function_115_11EFF(): pass

    label("Function_115_11EFF")

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

    def lambda_120B6():
        OP_96(0xFE, 0xFFFFFC18, 0x0, 0x6978, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x42, 1, lambda_120B6)
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
            "─ ─ In that sense, we are equal\x01",
            "I carry a sin before the goddess … …\x02\x03",
            "deception#4RGinka#And fear#4REducation#.\x01",
            "That will be the name of that sin.\x02",
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
            "To the sacrificed soul in the past\x01",
            "To repay … !.!\x02\x03",
            "And by recent raid\x01",
            "To reward those who are injured!\x02\x03",
            "To our children, in peace\x01",
            "To deliver a proud future, too!\x02",
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
            "#4SNow is the time we fight#4RGinka#And fear#4REducation#Throwing away\x01",
            "With pride and courage\x01",
            "I have to get up!\x07\x00\x02",
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
        "Representative Campbell",
        "#5PIt is unreasonable ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x31,
        (
            "#6PHowever, … …\x01",
            "Sure it is quality#2RHowever#When it is done ……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x2D,
        "#5P#02501F(……… Dieter you …………)\x02",
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

    # Function_115_11EFF end

    def Function_116_124AD(): pass

    label("Function_116_124AD")

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
    SetChrName("President's voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Actually, Arios said\x01",
            "Once as an excellent investigator\x01",
            "I belonged to Crossbell Police.\x02\x03",
            "And in the guild, as you know\x01",
            "We have solved many international projects\x01",
            "I have a wonderful achievement.\x02\x03",
            "In that sense, never missed\x01",
            "It is not a personnel affair\x01",
            "Let me assure you again.\x07\x00\x02",
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
            "#40W……Dad……\x01",
            "……………why…………\x02",
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

    # Function_116_124AD end

    def Function_117_127D4(): pass

    label("Function_117_127D4")

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
        "#6P#11230FThe Blue Wall…\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x34, 0xC, 400)
    Sleep(150)

    ChrTalk(
        0x34,
        (
            "#10503FNo need to worry\x02\x03",
            "#10502FThere is no harm to you\x01",
            "You should be safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#6P#11221F…!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x34, 500)
    OP_68(163400, 1100, 56750, 500)
    MoveCamera(41, 19, 0, 500)
    SetCameraDistance(16000, 500)

    def lambda_12975():
        OP_96(0xFE, 0x27E48, 0x0, 0xDCB4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_12975)
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
            "#12P#11226F#30WWa, than I am\x01",
            "Dad is more ……!\x02\x03",
            "#11227F#30W……why……\x01",
            "Why is it such a thing …!\x02\x03",
            "#11232F#30WI bet he's a mother ……\x01",
            "…… It should be sorry … …!\x02",
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
            "#10504F#5PThat's true…\x02\x03",
            "Saya surely … …\x01",
            "It probably was preached on a troubled face.\x02",
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
            "#4071V#40W#25AShizuku.\x02\x03",
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

    # Function_117_127D4 end

    def Function_118_12C2B(): pass

    label("Function_118_12C2B")

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
        "#5P#00001FWe're here…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#6PAs the chief's story, quite a few people\x01",
            "It seems to be on the floor ….\x02",
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
        "Voice that looks nervous",
        "#2SY-you guys are…!?\x02",
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

    def lambda_12ED7():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_12ED7)
    Sleep(50)

    def lambda_12EE7():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_12EE7)
    Sleep(50)

    def lambda_12EF7():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_12EF7)
    Sleep(50)

    def lambda_12F07():
        OP_93(0xF4, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_12F07)
    Sleep(50)

    def lambda_12F17():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_12F17)
    Sleep(50)

    def lambda_12F27():
        OP_93(0xF5, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_12F27)
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
        "#00011FD-Deputy Chief!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00105FWhy are you here…\x02",
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0xF,
        "#5PT-that's my line!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5PI that……\x01",
            "About martial law sentence last night\x01",
            "I came to ask the Commissioner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5PThen, being restrained as it is\x01",
            "On this floor ……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13132")

    ChrTalk(
        0x10A,
        "#12P#N#00606FIs that right…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_1319A")

    label("loc_13132")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13173")

    ChrTalk(
        0x109,
        "#12P#N#10106FIs that so……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_1319A")

    label("loc_13173")


    ChrTalk(
        0x102,
        "#12P#00106FIs that so……\x02",
    )

    CloseMessageWindow()

    label("loc_1319A")


    ChrTalk(
        0x104,
        (
            "#00309FNo, somehow,\x01",
            "It is a bit surprising.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13227")

    ChrTalk(
        0x105,
        (
            "#12P#N#10402FContact Huff, above\x01",
            "You said you had a spirit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1326D")

    label("loc_13227")


    ChrTalk(
        0x103,
        (
            "#12P#N#00204FThe reason for inquiring above\x01",
            "I did not think there was.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1326D")

    OP_63(0xF, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xF,
        "#5PW-what do you mean by that!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5PFirst you guys from the Defense Army\x01",
            "Was it supposed to have been wanted?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#5PWhat are you up to!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FWell, it's a long story\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1338B")

    ChrTalk(
        0x103,
        (
            "#12P#N#00205FYou are … …\x01",
            "Were you in the technical department of IBC?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_133C5")

    label("loc_1338B")


    ChrTalk(
        0x102,
        (
            "#12P#00105FYou there …\x01",
            "Were you in the technical department of IBC?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_133C5")


    ChrTalk(
        0x10,
        "#5PYeah… I'm David from the lab\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PI also from yesterday, Marybele miss\x01",
            "I was told the dissolution of the technical department … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PI do not have a buddy, and I was stunned\x01",
            "Brought to this floor … …\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_134D7")

    ChrTalk(
        0x106,
        (
            "#12P#N#10708F…… First of all let's see each other's situation\x01",
            "It seems better to check it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13592")

    label("loc_134D7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13538")

    ChrTalk(
        0x109,
        (
            "#12P#N#10108FWell, first of all let's see each other's situation\x01",
            "It seems better to check it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13592")

    label("loc_13538")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13592")

    ChrTalk(
        0x10A,
        (
            "#12P#N#00603FHum, first of all let's see each other's situation\x01",
            "It seems better to check it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13592")

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
        "#5PS-so that's what happened…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5PSince the invalid declaration of an independent country,\x01",
            "I thought that the clouds were suspicious … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11PB-but why did it come to this\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PSomehow a bad dream\x01",
            "I feel like I'm seeing … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PThat's right … … The clay guy\x01",
            "Are you cooperating with Roberts?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PAs expected 2 or 3 days ago\x01",
            "How to hack to the tower\x01",
            "It became even clever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103FSo then Deputy Chief\x02\x03",
            "#00101FAfter all, on this floor\x01",
            "What is the official of the president side?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#5PHmm\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5PPresident and Mary Bell, of course,\x01",
            "There are no Secretary of Defense and hunters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5Pin addition……\x01",
            "I also have that girl who was at you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00006FI see…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00108FSo what floor…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203F…… from the chief for the time being\x01",
            "Should I wait for contact?\x02\x03",
            "#00201FCurrently, hurry up the upper-level area\x01",
            "I think that I have investigated.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(150)

    ChrTalk(
        0x104,
        (
            "#6P#00303FMeanwhile, I am on this floor\x01",
            "Let's check with other members too.\x02\x03",
            "#00301FPossibly something\x01",
            "Perhaps there is a guy I know.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    ChrTalk(
        0x101,
        (
            "#11P#00006FThat's true…\x01",
            "Do you want to listen to a story?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13AE0")

    ChrTalk(
        0x10A,
        (
            "#00600F#12PDeputy Director.\x01",
            "Can I ask for this place?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13B65")

    label("loc_13AE0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13B23")

    ChrTalk(
        0x109,
        (
            "#10101F#12PDeputy Director.\x01",
            "Can I ask for this place?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13B65")

    label("loc_13B23")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13B65")

    ChrTalk(
        0x105,
        (
            "#10400F#12PMr. Deputy Director.\x01",
            "Can I ask for this place?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13B65")


    def lambda_13B6A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_13B6A)
    Sleep(100)

    def lambda_13B7A():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_13B7A)

    ChrTalk(
        0xF,
        "#5PYes, leave it to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5P… … that, you guys as well.\x01",
            "Do not be too unreasonable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5PIf it collapses before grabbing the truth\x01",
            "You have neither young nor children.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000F……Yes.\x01",
            "I will keep in mind the liver.\x02",
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

    # Function_118_12C2B end

    def Function_119_13D21(): pass

    label("Function_119_13D21")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13D45")
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(1300)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1600)
    Jump("Function_119_13D21")

    label("loc_13D45")

    Return()

    # Function_119_13D21 end

    def Function_120_13D46(): pass

    label("Function_120_13D46")

    Sleep(500)

    label("loc_13D49")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13D6D")
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1600)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(1300)
    Jump("loc_13D49")

    label("loc_13D6D")

    Return()

    # Function_120_13D46 end

    def Function_121_13D6E(): pass

    label("Function_121_13D6E")


    def lambda_13D73():
        OP_95(0xFE, -2800, 0, 11100, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_13D73)

    def lambda_13D8D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_13D8D)
    WaitChrThread(0xFE, 1)
    OP_68(-2000, 1000, 2850, 3500)
    MoveCamera(37, 21, 0, 3500)
    SetCameraDistance(18000, 3500)

    def lambda_13DC7():
        OP_95(0xFE, -2500, 0, 4700, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_13DC7)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_121_13D6E end

    def Function_122_13DE1(): pass

    label("Function_122_13DE1")


    def lambda_13DE6():
        OP_95(0xFE, -2800, 0, 11000, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_13DE6)

    def lambda_13E00():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_13E00)
    WaitChrThread(0xFE, 1)

    def lambda_13E15():
        OP_95(0xFE, -1300, 0, 5300, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_13E15)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_122_13DE1 end

    def Function_123_13E2F(): pass

    label("Function_123_13E2F")

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
        "#00005F#5P(Ah…)\x02",
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
            "#11228F#30W….\x02\x03",
            "#11226F…… Kia-chan ………\x01",
            "……… Dad … … how come … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FShizuku!\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_141C9():

        label("loc_141C9")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_141C9")

    QueueWorkItem2(0xC, 2, lambda_141C9)
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
        "#11230FAh!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x103, 3)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#12P#00109FWas good……\x01",
            "You were okay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00202FMr. Shizuku also went to the Orkis Tower\x01",
            "You had been brought in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FBecause it's that osan\x01",
            "I thought it was another place … …\x02\x03",
            "#00302FBut anyway I'm glad you're OK\x02",
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
            "#30WMr. Lloyd, Mr. Randy ……\x01",
            "…… Eli and Tio also ……\x02\x03",
            "……I see……\x01",
            "I was on such a face …\x02",
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
        "#00005FShizuku… no way…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00102FYou can see now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11226F#5P……Yes.\x01",
            "Thanks to Keia-chan.\x02\x03",
            "With a mysterious force, the nerve of the eye\x01",
            "She seemed to be connected … ….\x02\x03",
            "#11231FIt's not just light anymore ……\x01",
            "I can understand the color and shape properly.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_145DF")

    ChrTalk(
        0x109,
        "#10105F#5PThat's amazing …\x02",
    )

    CloseMessageWindow()
    Jump("loc_1464A")

    label("loc_145DF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14618")

    ChrTalk(
        0x10A,
        "#00605F#5PUnbelievable power…\x02",
    )

    CloseMessageWindow()
    Jump("loc_1464A")

    label("loc_14618")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1464A")

    ChrTalk(
        0x106,
        "#10712F#5Pcan not believe……\x02",
    )

    CloseMessageWindow()

    label("loc_1464A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1469C")

    ChrTalk(
        0x105,
        (
            "#10408F#5PThe power of \"Zero's treasure\"\x01",
            "It also affects life activities …?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1470F")

    label("loc_1469C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_146D9")

    ChrTalk(
        0x106,
        "#10708F#5PIt's truly a miracle…\x02",
    )

    CloseMessageWindow()
    Jump("loc_1470F")

    label("loc_146D9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1470F")

    ChrTalk(
        0x10A,
        "#00606F#5PIt is exactly \"miracle\" …\x02",
    )

    CloseMessageWindow()

    label("loc_1470F")


    ChrTalk(
        0x104,
        (
            "#00309FNo, no matter what\x01",
            "Was not it good!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FOh … only this\x01",
            "Ka'aa was also deeply impressed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11231F#5PYes … really\x01",
            "How much do you like for Ka'a-chan?\x01",
            "It is not enough to say … …\x02\x03",
            "#11233F#30WBut ….\x01",
            "But … hey!\x02",
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
        "#12P#00101FShizuku!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011FW-what's wrong?\x02",
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
            "#11227F#5P#30WKaea, I was laughing\x01",
            "It seemed so spicy … ….!\x02\x03",
            "This is my role … …\x01",
            "… … I wish for myself\x01",
            "She seems to be forcibly telling me!\x02\x03",
            "#11232FActually to the dieter\x01",
            "I do not want to cooperate … ….!\x02\x03",
            "To Lloyd's\x01",
            "I want to go back but I can not help it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008FAh…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306FI see…\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0xB)
    Sleep(130)
    SetChrSubChip(0xC, 0xC)
    Sleep(150)

    ChrTalk(
        0xC,
        (
            "#11233F#5P#30WWhy is Ka'aa\x01",
            "Such a thing …?\x02\x03",
            "in addition……\x01",
            "…… Why is Dad …?\x02\x03",
            "#11234FI…. I….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00208FShizuku…\x02",
    )

    CloseMessageWindow()
    OP_68(163420, 900, 56850, 1200)

    def lambda_14B1B():
        OP_95(0xFE, 162800, 0, 57000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14B1B)
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
            "#6P#00104F……Thank you.\x01",
            "Thinking of Ka'a-chan.\x02\x03",
            "#00108FAlso …\x01",
            "I was totally alone and tough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11233F#5P#30WSob….\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00003F…… Shizuku-chan.\x01",
            "We need Kea\x01",
            "I came to regain it.\x02\x03",
            "#00001FThat girl and Arios are\x01",
            "Do you know where you are?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11233F#5P#30WI'm sorry……\x01",
            "I do not know anything ……\x02\x03",
            "Ka'aa from yesterday\x01",
            "I have not seen you …\x02\x03",
            "#11234FAnd … from Dad\x01",
            "I got my message to Mr. Lloyd … …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FHuh\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14DB1")

    ChrTalk(
        0x10A,
        "#00605F#5PFrom MacClain\x02",
    )

    CloseMessageWindow()
    Jump("loc_14E22")

    label("loc_14DB1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14DEC")

    ChrTalk(
        0x109,
        "#10105F#5PA, Arios! Is it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_14E22")

    label("loc_14DEC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14E22")

    ChrTalk(
        0x105,
        "#10405F#5P\"Wind sword\" is … …! Is it?\x02",
    )

    CloseMessageWindow()

    label("loc_14E22")

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
        "#00001FThis package is…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11226F#11P…… Dad to Mr. Lloyd\x01",
            "Please pass me ……\x02\x03",
            "#11221FPlease open it\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FR-right…\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_150DB")
    Sleep(50)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    label("loc_150DB")

    Sleep(1000)

    ChrTalk(
        0x101,
        "#00007F#30WThis is…\x02",
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
        "#00208F#30WThe ones Guy was using…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_151F9")

    AnonymousTalk(
        0x10A,
        (
            "#00606F#30W……no doubt.\x01",
            "The gift that the guy used#4RTonfa#It is.\x02\x03",
            "#00608FI was taken away from the scene\x01",
            "I was missing ……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_151F9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15271")

    AnonymousTalk(
        0x105,
        (
            "#10405F#30WThis is a sword … …?\x02\x03",
            "#10401FThat means …\x01",
            "Guy Bannings\x01",
            "What was on my hand ……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_1536A")

    label("loc_15271")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_152ED")

    AnonymousTalk(
        0x109,
        (
            "#10105F#30WThis is a sword … …?\x02\x03",
            "#10101FThat means …\x01",
            "Lloyd's older brother\x01",
            "What was on my hand ……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_1536A")

    label("loc_152ED")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1536A")

    AnonymousTalk(
        0x106,
        (
            "#10703F#30WThese are cut by a sword…\x02\x03",
            "#10708FThat means …\x01",
            "Lloyd's older brother\x01",
            "What was on my hand ……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_1536A")

    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    ChrTalk(
        0x102,
        "#12P#00108F#30WLloyd…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#40W….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11233F#11P#40W……I'm sorry……\x01",
            "…………really sorry……\x02\x03",
            "#40WMy dad… my father… did such a horrible thing\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F── Shizuoka-chan.\x01",
            "You do not have to feel wrong.\x02\x03",
            "#00008FReally Arios,\x01",
            "With my brother in hand\x01",
            "I did not decide … …\x02\x03",
            "#00013FApparently, I have not seen it yet,\x01",
            "There seems to be hidden truth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11227F#11P#30WHuh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301FWhat do you mean?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_156D5")

    ChrTalk(
        0x101,
        (
            "#00008FAs long as you see this sword,\x01",
            "Big brother and Arios fierce\x01",
            "The chances of having met each other will be high.\x02\x03",
            "#00003FAs far as looking at the number of swords, …\x01",
            "With that \"opponent of the Wind of the Wind\"\x01",
            "I think that my brother did a pretty good fight.\x02\x03",
            "#00013FBut…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#6P#00603F── The direct cause of death of Guy\x01",
            "Sniper from the back with a gun#22R噵 噵 噵 噵 噵 噵 噵 噵 噵 噵 噵#.\x02\x03",
            "#00601FThat's what you mean, Bannings?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FYes.\x02",
    )

    CloseMessageWindow()
    Jump("loc_157F6")

    label("loc_156D5")


    ChrTalk(
        0x101,
        (
            "#00008FAs long as you see this sword,\x01",
            "Big brother and Arios fierce\x01",
            "The chances of having met each other will be high.\x02\x03",
            "#00003FAs far as looking at the number of swords, …\x01",
            "With that \"opponent of the Wind of the Wind\"\x01",
            "I think that my brother did a pretty good fight.\x02\x03",
            "#00013F── However, the cause of direct death of the older brother is\x01",
            "It was shot by a gun from behind.#20R噵 噵 噵 噵 噵 噵 噵 噵 噵 噵#Thing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_157F6")


    ChrTalk(
        0x103,
        "#6P#00205FAh…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00105FThat is…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F── Shizuoka-chan.\x01",
            "I will also read letters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11230F#11PY-yes…\x02",
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
            "#4073V#40W── To Lloyd#1500W.\x01",
            "#40WItems that I could not give for a long time\x01",
            "I will return this to occasion.\x02\x03",
            "#4074V#40WThat product is all - ─\x01",
            "I do not intend to explain.\x02\x03",
            "#4075V#40WThe magician who appeared in the town\x01",
            "Through the Great Bell the White Sacred Machine\x01",
            "It is what we are manipulating.\x02\x03",
            "#4076V#40WHow do I manage my white god machine\x01",
            "All will be silenced.\x07\x00\x02",
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
        "#00008F#30W….\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x102,
        "#00108F#30WThis is..\x02",
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
            "#00303F…… The white god machine is,\x01",
            "I saw it in that picture.\x02\x03",
            "#00301FLook at the Galleria Fortress\x01",
            "I did a crooked ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00201FBut, the power to eliminate space is\x01",
            "It should not be usable.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15BA6")

    ChrTalk(
        0x10A,
        (
            "#6P#00608FBut McLean's guy,\x01",
            "What on earth are you ….\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15C41")

    label("loc_15BA6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15BF6")

    ChrTalk(
        0x106,
        (
            "#6P#10708FBut \"Wind Saint of the Wind\" is\x01",
            "What on earth are you ….\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15C41")

    label("loc_15BF6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15C41")

    ChrTalk(
        0x109,
        (
            "#6P#10108FBut Arios\x01",
            "What on earth are you ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15C41")

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
            scpstr(SCPSTR_CODE_ITEM, '零·破坏者'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Got Zero Breaker\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('零·破坏者', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    def lambda_15CE7():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_15CE7)

    def lambda_15CF4():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_15CF4)

    def lambda_15D01():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_15D01)
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
        "#00302FOh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00202FLloyd…\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15DD0")

    ChrTalk(
        0x105,
        (
            "#6P#10402FOh\x01",
            "As if as a tire#2RAura#It seems like you did it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15E55")

    label("loc_15DD0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15E15")

    ChrTalk(
        0x109,
        "#6P#10100FAs if as a tire#2RAura#It seems like it was …\x02",
    )

    CloseMessageWindow()
    Jump("loc_15E55")

    label("loc_15E15")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15E55")

    ChrTalk(
        0x106,
        "#6P#10702FAs if as a tire#2RAura#I was like …\x02",
    )

    CloseMessageWindow()

    label("loc_15E55")


    ChrTalk(
        0x101,
        (
            "#00004FAh……\x01",
            "Familiar and familiar with your hands.\x02",
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
            "#00004F── Shizuoka-chan.\x01",
            "Thank you for your message.\x02\x03",
            "#00000FFrom here onwards,\x01",
            "Leave it to us.\x02\x03",
            "Ka'a thing ….\x01",
            "And also Arios' s thing.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_15F61():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_15F61)
    Sleep(50)

    def lambda_15F71():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_15F71)
    Sleep(50)

    def lambda_15F81():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_15F81)

    def lambda_15F8E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_15F8E)

    ChrTalk(
        0xC,
        (
            "#11226F#11P#30WYes…\x02\x03",
            "#11228FFather has been … …\x01",
            "I think that I was worrying.\x02\x03",
            "About mother, about me\x02\x03",
            "#11233FWhile thinking about various things\x01",
            "…… I can not turn back … …\x02\x03",
            "#11227FAnd then… sob…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FAre you alright\x01",
            "I can not turn back\x01",
            "Is there such a thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00104FDad's things are\x01",
            "I'm sure I will bring it back.\x02\x03",
            "#00100FBy the name of the SSS\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FWell, this cute girl only\x01",
            "Bad mistress that makes me cry\x01",
            "I do not want to hit a single shot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00204FRight\x02\x03",
            "#00202FEven if you stretch a rope around your neck\x01",
            "Let's take home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11231F#11P#30W… …. Guru ……\x01",
            "…………Yes………!\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1644A")

    ChrTalk(
        0x10A,
        (
            "#6P#00606FBut McLein\x01",
            "Regardless of the story to take back … …\x02\x03",
            "#00601FPresidents' stakeholders\x01",
            "Where the hell did you go?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16557")

    label("loc_1644A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_164D2")

    ChrTalk(
        0x105,
        (
            "#6P#10406FBut \"wind sword Saint\"\x01",
            "Regardless of the story to take back … …\x02\x03",
            "#10401FPresidents' stakeholders\x01",
            "Where have you gone?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16557")

    label("loc_164D2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16557")

    ChrTalk(
        0x106,
        (
            "#6P#10706FBut \"wind sword Saint\"\x01",
            "Regardless of the story to take back … …\x02\x03",
            "#10708FPresidents' stakeholders\x01",
            "Where did he go?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16557")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_165A9")

    ChrTalk(
        0x109,
        (
            "#6P#10108FKa'a-chan likewise\x01",
            "It seems I do not live … ….\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1663E")

    label("loc_165A9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_165F9")

    ChrTalk(
        0x106,
        (
            "#6P#10708FAfter all, Ka'a-chan\x01",
            "It seems I do not live … ….\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1663E")

    label("loc_165F9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1663E")

    ChrTalk(
        0x105,
        (
            "#6P#10408FAfter all Ka'aa\x01",
            "It seems they do not exist.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1663E")


    ChrTalk(
        0x101,
        "#00006F#11PThat's true…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00108F…… That you left a message\x01",
            "Possibly to the tower - ─\x02",
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
            "#00005F#11POops ……\x01",
            "(Set to speaker mode)\x02",
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
    SetChrName("Voice of the boss")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Oh, Lloyd!\x02\x03",
            "Direct elevator security,\x01",
            "Finally I could cancel it ~!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        "#00002FReally?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    AnonymousTalk(
        0x102,
        "#00104FGreat, so now we can\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice of the boss")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "However, on some other floor\x01",
            "There are few people left.\x02\x03",
            "Escape from this search\x01",
            "I can not believe it is hiding.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    AnonymousTalk(
        0x103,
        "#00201FThat is…\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    AnonymousTalk(
        0x104,
        (
            "#00301FCome on, hey, sorry\x01",
            "Where the hell are you ….\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice of the boss")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "But one more thing\x02\x03",
            "On the roof of the Orchis Tower\x01",
            "It seems there is someone.\x02\x03",
            "With a white doll\x07\x00\x02",
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
        "#00013F…!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16A15")
    SetMessageWindowPos(50, 30, -1, -1)

    AnonymousTalk(
        0x109,
        (
            "#10101F…… on the roof with an elevator\x01",
            "Is it possible to go?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_16AD0")

    label("loc_16A15")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16A74")
    SetMessageWindowPos(50, 30, -1, -1)

    AnonymousTalk(
        0x105,
        (
            "#10401F…… on the roof with an elevator\x01",
            "Is it possible to go?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_16AD0")

    label("loc_16A74")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16AD0")
    SetMessageWindowPos(50, 30, -1, -1)

    AnonymousTalk(
        0x10A,
        (
            "#00601F…… on the roof with an elevator\x01",
            "Is it possible to go?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_16AD0")

    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Voice of the boss")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Oh, because I unlocked it\x01",
            "You should be able to go up.\x02\x03",
            "But if you go, be careful!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    AnonymousTalk(
        0x103,
        "#00203FRoger!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        "#00000FWell then, excuse us\x02",
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
        "#5P#00108FThe professor of the Organizaiton, or…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00301Fcan not understand……\x01",
            "I guess we only have to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203FThere is a direct elevator nearby\x01",
            "It should be usable.\x02\x03",
            "#00201FReturn to 1F if necessary\x01",
            "Let's get ready.\x02",
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
        "#11P#00007FRight!\x02",
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

    # Function_123_13E2F end

    def Function_124_16D89(): pass

    label("Function_124_16D89")

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

    # Function_124_16D89 end

    def Function_125_16DFE(): pass

    label("Function_125_16DFE")

    SetChrPos(0xFE, 156600, 0, 52000, 90)

    def lambda_16E14():
        OP_95(0xFE, 161000, 0, 52000, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_16E14)
    WaitChrThread(0xFE, 1)

    def lambda_16E32():
        OP_95(0xFE, 163300, 0, 55200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_16E32)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_125_16DFE end

    def Function_126_16E53(): pass

    label("Function_126_16E53")

    SetChrPos(0xFE, 156600, 0, 52000, 90)

    def lambda_16E69():
        OP_95(0xFE, 161000, 0, 52000, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_16E69)
    WaitChrThread(0xFE, 1)

    def lambda_16E87():
        OP_95(0xFE, 162000, 0, 54800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_16E87)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_126_16E53 end

    def Function_127_16EA8(): pass

    label("Function_127_16EA8")

    SetChrPos(0xFE, 156600, 0, 52000, 90)

    def lambda_16EBE():
        OP_95(0xFE, 161000, 0, 52000, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_16EBE)
    WaitChrThread(0xFE, 1)

    def lambda_16EDC():
        OP_95(0xFE, 162000, 0, 53600, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_16EDC)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_127_16EA8 end

    def Function_128_16EFD(): pass

    label("Function_128_16EFD")

    SetChrPos(0xFE, 156600, 0, 52000, 90)

    def lambda_16F13():
        OP_95(0xFE, 161000, 0, 52000, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_16F13)
    WaitChrThread(0xFE, 1)

    def lambda_16F31():
        OP_95(0xFE, 163300, 0, 54000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_16F31)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_128_16EFD end

    def Function_129_16F52(): pass

    label("Function_129_16F52")

    SetChrPos(0xFE, 154000, 0, 60000, 90)

    def lambda_16F68():
        OP_95(0xFE, 161300, 0, 60000, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_16F68)
    WaitChrThread(0xFE, 1)

    def lambda_16F86():
        OP_95(0xFE, 161700, 0, 58130, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_16F86)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x87, 0x1F4)
    Return()

    # Function_129_16F52 end

    def Function_130_16FA7(): pass

    label("Function_130_16FA7")

    SetChrPos(0xFE, 154000, 0, 60000, 90)

    def lambda_16FBD():
        OP_95(0xFE, 161300, 0, 60000, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_16FBD)
    WaitChrThread(0xFE, 1)

    def lambda_16FDB():
        OP_95(0xFE, 163100, 0, 58800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_16FDB)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_130_16FA7 end

    def Function_131_16FFC(): pass

    label("Function_131_16FFC")


    def lambda_17001():
        OP_95(0xFE, 110200, 0, -110500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_17001)

    def lambda_1701B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1701B)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_131_16FFC end

    def Function_132_1702C(): pass

    label("Function_132_1702C")


    def lambda_17031():
        OP_95(0xFE, 110000, 0, -110500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_17031)

    def lambda_1704B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1704B)
    WaitChrThread(0xFE, 1)

    def lambda_17060():
        OP_95(0xFE, 109600, 0, -109200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_17060)
    WaitChrThread(0xFE, 1)

    def lambda_1707E():

        label("loc_1707E")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_1707E")

    QueueWorkItem2(0xFE, 2, lambda_1707E)
    Return()

    # Function_132_1702C end

    def Function_133_1708C(): pass

    label("Function_133_1708C")


    def lambda_17091():
        OP_95(0xFE, 110000, 0, -110500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_17091)

    def lambda_170AB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_170AB)
    WaitChrThread(0xFE, 1)

    def lambda_170C0():
        OP_95(0xFE, 108600, 0, -111500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_170C0)
    WaitChrThread(0xFE, 1)

    def lambda_170DE():

        label("loc_170DE")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_170DE")

    QueueWorkItem2(0xFE, 2, lambda_170DE)
    Return()

    # Function_133_1708C end

    def Function_134_170EC(): pass

    label("Function_134_170EC")


    def lambda_170F1():
        OP_95(0xFE, 110000, 0, -110500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_170F1)

    def lambda_1710B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1710B)
    WaitChrThread(0xFE, 1)

    def lambda_17120():
        OP_95(0xFE, 109600, 0, -112200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_17120)
    WaitChrThread(0xFE, 1)

    def lambda_1713E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1713E)
    Return()

    # Function_134_170EC end

    def Function_135_17147(): pass

    label("Function_135_17147")


    def lambda_1714C():
        OP_95(0xFE, 110000, 0, -110500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1714C)

    def lambda_17166():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_17166)
    WaitChrThread(0xFE, 1)

    def lambda_1717B():
        OP_95(0xFE, 108000, 0, -109800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1717B)
    WaitChrThread(0xFE, 1)

    def lambda_17199():

        label("loc_17199")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_17199")

    QueueWorkItem2(0xFE, 2, lambda_17199)
    Return()

    # Function_135_17147 end

    def Function_136_171A7(): pass

    label("Function_136_171A7")


    def lambda_171AC():
        OP_95(0xFE, 110000, 0, -110500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_171AC)

    def lambda_171C6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_171C6)
    WaitChrThread(0xFE, 1)

    def lambda_171DB():
        OP_95(0xFE, 107500, 0, -111300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_171DB)
    WaitChrThread(0xFE, 1)

    def lambda_171F9():

        label("loc_171F9")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_171F9")

    QueueWorkItem2(0xFE, 2, lambda_171F9)
    Return()

    # Function_136_171A7 end

    def Function_137_17207(): pass

    label("Function_137_17207")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17414")
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
        "#00013FAfter all -\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FBoth devices have a shutter\x01",
            "It's closed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201FSince I was robbed of the control of the building,\x01",
            "If you can not use an elevator\x01",
            "It seems better to think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FThen, even if you shutter\x01",
            "Even if you break open with force\x01",
            "I can not help it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10107FYeah, let's hurry to the emergency stairs!\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, 109910, 0, -130740, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x1C2, 5)
    EventEnd(0x5)
    Jump("loc_17469")

    label("loc_17414")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00007FWe can not use elevator ……\x01",
            "I will head towards the emergency stairs!\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 109910, 0, -130740, 270)
    EventEnd(0x4)

    label("loc_17469")

    Return()

    # Function_137_17207 end

    def Function_138_1746A(): pass

    label("Function_138_1746A")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_174C4")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The elevator\x01",
            "It seems that it is in use on another floor,\x01",
            "There is no sign of stopping.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_1779F")

    label("loc_174C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17730")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The shutter of the elevator\x01",
            "It is tightly closed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00000FBy the way, during the meeting\x01",
            "Apart from the elevator in front\x01",
            "Did not you use it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYeah, for security reasons\x01",
            "That was supposed to be the case.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 3)), scpexpr(EXPR_END)), "loc_17656")

    ChrTalk(
        0x103,
        (
            "#00200FLike the emergency staircase,\x01",
            "Also here by the power net\x01",
            "It seems to be controlled and managed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, it seems so.\x02\x03",
            "Well, when you move\x01",
            "Let's use the front elevator.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17728")

    label("loc_17656")


    ChrTalk(
        0x103,
        (
            "#00200FBy the way, opening and closing of the lock\x01",
            "With the power net\x01",
            "It seems to be controlled and managed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, Kusufusaki is Orkistor's\x01",
            "Security is a place.\x02\x03",
            "Well, when you move\x01",
            "Let's use the front elevator.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17728")

    SetScenarioFlags(0x1C2, 2)
    Jump("loc_1779F")

    label("loc_17730")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The shutter of the elevator\x01",
            "It is tightly closed.\x02\x03",
            "During the meeting, this elevator\x01",
            "It seems that it can not be used.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_1779F")

    TalkEnd(0xFF)
    Return()

    # Function_138_1746A end

    def Function_139_177A3(): pass

    label("Function_139_177A3")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_179CB")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Emergency stairs shutter\x01",
            "It is tightly closed.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00000FAre you going to the 37th floor?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes, and completely during the meeting\x01",
            "It was a story of blockade.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 2)), scpexpr(EXPR_END)), "loc_17911")

    ChrTalk(
        0x103,
        (
            "#00200FLike an elevator,\x01",
            "This is also a power net\x01",
            "It seems to be controlled, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FPerfect security\x01",
            "It was impossible - was it?\x02\x03",
            "In the unlikely event\x01",
            "I suppose I should assume.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_179C3")

    label("loc_17911")


    ChrTalk(
        0x103,
        (
            "#00200FShutter lock\x01",
            "With the power net\x01",
            "It seems to be controlled, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FPerfect security\x01",
            "It was impossible - was it?\x02\x03",
            "In the unlikely event\x01",
            "I suppose I should assume.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_179C3")

    SetScenarioFlags(0x1C2, 3)
    Jump("loc_17A34")

    label("loc_179CB")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Emergency stairs shutter\x01",
            "It is tightly closed.\x02\x03",
            "During the meeting, to the next floor\x01",
            "I do not seem to be able to come and go.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_17A34")

    TalkEnd(0xFF)
    Return()

    # Function_139_177A3 end

    def Function_140_17A38(): pass

    label("Function_140_17A38")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001FOops, in the back room of the left wing\x01",
            "I have a president.\x02\x03",
            "Before going to the prime minister\x01",
            "Let's first visit the president.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 4370, 0, -1430, 270)
    EventEnd(0x4)
    Return()

    # Function_140_17A38 end

    SaveToFile()

Try(main)
