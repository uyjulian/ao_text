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
        "Function_6_18E1",         # 06, 6
        "Function_7_18FF",         # 07, 7
        "Function_8_1E70",         # 08, 8
        "Function_9_21AA",         # 09, 9
        "Function_10_23DE",        # 0A, 10
        "Function_11_2D02",        # 0B, 11
        "Function_12_2DF6",        # 0C, 12
        "Function_13_3182",        # 0D, 13
        "Function_14_367F",        # 0E, 14
        "Function_15_37F0",        # 0F, 15
        "Function_16_3ABF",        # 10, 16
        "Function_17_3BF6",        # 11, 17
        "Function_18_3CBD",        # 12, 18
        "Function_19_4AF1",        # 13, 19
        "Function_20_4B8D",        # 14, 20
        "Function_21_4C13",        # 15, 21
        "Function_22_540D",        # 16, 22
        "Function_23_56AF",        # 17, 23
        "Function_24_58A3",        # 18, 24
        "Function_25_5955",        # 19, 25
        "Function_26_59EE",        # 1A, 26
        "Function_27_5B26",        # 1B, 27
        "Function_28_5D74",        # 1C, 28
        "Function_29_5E78",        # 1D, 29
        "Function_30_5FF3",        # 1E, 30
        "Function_31_6197",        # 1F, 31
        "Function_32_62CC",        # 20, 32
        "Function_33_638D",        # 21, 33
        "Function_34_649C",        # 22, 34
        "Function_35_694B",        # 23, 35
        "Function_36_6A7C",        # 24, 36
        "Function_37_6A86",        # 25, 37
        "Function_38_75E4",        # 26, 38
        "Function_39_75EE",        # 27, 39
        "Function_40_76F9",        # 28, 40
        "Function_41_783F",        # 29, 41
        "Function_42_78FC",        # 2A, 42
        "Function_43_7B35",        # 2B, 43
        "Function_44_7CAC",        # 2C, 44
        "Function_45_7DEB",        # 2D, 45
        "Function_46_7E88",        # 2E, 46
        "Function_47_7FE6",        # 2F, 47
        "Function_48_813C",        # 30, 48
        "Function_49_8281",        # 31, 49
        "Function_50_87A5",        # 32, 50
        "Function_51_9866",        # 33, 51
        "Function_52_A501",        # 34, 52
        "Function_53_A508",        # 35, 53
        "Function_54_A531",        # 36, 54
        "Function_55_B5B6",        # 37, 55
        "Function_56_B635",        # 38, 56
        "Function_57_B68A",        # 39, 57
        "Function_58_B6DF",        # 3A, 58
        "Function_59_B734",        # 3B, 59
        "Function_60_B789",        # 3C, 60
        "Function_61_B7DE",        # 3D, 61
        "Function_62_B833",        # 3E, 62
        "Function_63_B888",        # 3F, 63
        "Function_64_B92D",        # 40, 64
        "Function_65_B99F",        # 41, 65
        "Function_66_BA23",        # 42, 66
        "Function_67_BA93",        # 43, 67
        "Function_68_BB17",        # 44, 68
        "Function_69_BB87",        # 45, 69
        "Function_70_BC0B",        # 46, 70
        "Function_71_BC7B",        # 47, 71
        "Function_72_BCB8",        # 48, 72
        "Function_73_BD09",        # 49, 73
        "Function_74_BD46",        # 4A, 74
        "Function_75_BDA1",        # 4B, 75
        "Function_76_BE13",        # 4C, 76
        "Function_77_BE8F",        # 4D, 77
        "Function_78_BF01",        # 4E, 78
        "Function_79_BF7D",        # 4F, 79
        "Function_80_BFF2",        # 50, 80
        "Function_81_CA66",        # 51, 81
        "Function_82_CD3F",        # 52, 82
        "Function_83_D018",        # 53, 83
        "Function_84_D323",        # 54, 84
        "Function_85_D374",        # 55, 85
        "Function_86_DBC9",        # 56, 86
        "Function_87_DC1E",        # 57, 87
        "Function_88_DC7E",        # 58, 88
        "Function_89_DCDE",        # 59, 89
        "Function_90_DD3E",        # 5A, 90
        "Function_91_DD9E",        # 5B, 91
        "Function_92_DDFE",        # 5C, 92
        "Function_93_DF31",        # 5D, 93
        "Function_94_10534",       # 5E, 94
        "Function_95_10585",       # 5F, 95
        "Function_96_105DA",       # 60, 96
        "Function_97_1062F",       # 61, 97
        "Function_98_10684",       # 62, 98
        "Function_99_106D9",       # 63, 99
        "Function_100_1072E",      # 64, 100
        "Function_101_10783",      # 65, 101
        "Function_102_107D8",      # 66, 102
        "Function_103_10838",      # 67, 103
        "Function_104_10898",      # 68, 104
        "Function_105_108F8",      # 69, 105
        "Function_106_10958",      # 6A, 106
        "Function_107_109B8",      # 6B, 107
        "Function_108_118CD",      # 6C, 108
        "Function_109_118EC",      # 6D, 109
        "Function_110_121E6",      # 6E, 110
        "Function_111_124FF",      # 6F, 111
        "Function_112_12B4C",      # 70, 112
        "Function_113_12BC5",      # 71, 113
        "Function_114_12BE0",      # 72, 114
        "Function_115_12BF3",      # 73, 115
        "Function_116_1318E",      # 74, 116
        "Function_117_134AD",      # 75, 117
        "Function_118_13918",      # 76, 118
        "Function_119_14BB2",      # 77, 119
        "Function_120_14BD7",      # 78, 120
        "Function_121_14BFF",      # 79, 121
        "Function_122_14C72",      # 7A, 122
        "Function_123_14CC0",      # 7B, 123
        "Function_124_17D48",      # 7C, 124
        "Function_125_17DBD",      # 7D, 125
        "Function_126_17E12",      # 7E, 126
        "Function_127_17E67",      # 7F, 127
        "Function_128_17EBC",      # 80, 128
        "Function_129_17F11",      # 81, 129
        "Function_130_17F66",      # 82, 130
        "Function_131_17FBB",      # 83, 131
        "Function_132_17FEB",      # 84, 132
        "Function_133_1804B",      # 85, 133
        "Function_134_180AB",      # 86, 134
        "Function_135_18106",      # 87, 135
        "Function_136_18166",      # 88, 136
        "Function_137_181C6",      # 89, 137
        "Function_138_18437",      # 8A, 138
        "Function_139_187B5",      # 8B, 139
        "Function_140_18ABF",      # 8C, 140
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
            "Everyone, thank you for\x01",
            "your help today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The President was\x01",
            "delighted to see you as\x01",
            "well.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_1860 end

    def Function_6_18E1(): pass

    label("Function_6_18E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18F8")
    Call(0, 93)
    Return()

    label("loc_18F8")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_6_18E1 end

    def Function_7_18FF(): pass

    label("Function_7_18FF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1AF0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1921")
    TalkEnd(0xFE)
    Call(0, 49)
    Return()

    label("loc_1921")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A33")

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
            "many crimes... But I don't\x01",
            "want to punish him harshly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Regardless of his methods, the\x01",
            "truth is that he was trying to\x01",
            "protect Crossbell...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1AEB")

    label("loc_1A33")


    ChrTalk(
        0xFE,
        (
            "Suspect Crois has been charged\x01",
            "with many crimes... But I don't\x01",
            "want to punish him harshly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Regardless of his methods, the\x01",
            "truth is that he was trying to\x01",
            "protect Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AEB")

    Jump("loc_1E6C")

    label("loc_1AF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_1B7D")

    ChrTalk(
        0xFE,
        (
            "Damn. To think the\x01",
            "terrorists would go this\x01",
            "far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If the CGF had acted,\x01",
            "they should have been\x01",
            "able to do something...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E6C")

    label("loc_1B7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_1CD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C57")

    ChrTalk(
        0xFE,
        (
            "*sigh*, Captain Julia... If\x01",
            "she were my boss, each of my\x01",
            "days would be complete...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, I mustn't. What the\x01",
            "hell am I thinking?\x02",
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
    Jump("loc_1CD3")

    label("loc_1C57")


    ChrTalk(
        0xFE,
        (
            "We still can't be\x01",
            "optimistic about the\x01",
            "situation, so why am I...\x02",
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

    label("loc_1CD3")

    Jump("loc_1E6C")

    label("loc_1CD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_1E6C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DD4")

    ChrTalk(
        0xFE,
        (
            "*sigh*, but this viewing\x01",
            "corridor really does\x01",
            "have a nice view.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you set your gaze in the\x01",
            "distance, it feels as if you're\x01",
            "taking a walk through the sky...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, I mustn't. I've got\x01",
            "to be a little more\x01",
            "nervous.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1E6C")

    label("loc_1DD4")


    ChrTalk(
        0xFE,
        (
            "Now that I'm here, I'm getting\x01",
            "distracted by the view... I've\x01",
            "to to be more nervous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's nothing\x01",
            "redeeming about idle\x01",
            "thoughts, they say.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E6C")

    TalkEnd(0xFE)
    Return()

    # Function_7_18FF end

    def Function_8_1E70(): pass

    label("Function_8_1E70")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1EC6")

    ChrTalk(
        0xFE,
        (
            "Nothing out of the\x01",
            "ordinary!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We're continuing our\x01",
            "patrols!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21A6")

    label("loc_1EC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_1F63")

    ChrTalk(
        0xFE,
        (
            "It seems we can't use\x01",
            "the elevator or the\x01",
            "stairs right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Divided like this, we'll\x01",
            "need to do something on\x01",
            "our own at this rate...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21A6")

    label("loc_1F63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_212F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20A4")

    ChrTalk(
        0xFE,
        (
            "They called him Lt.\x01",
            "Mueller of the Imperial\x01",
            "Army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And Captain Julia is supreme\x01",
            "commander of the Royal Guard\x01",
            "and the Royal Elite Guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's rare to see two\x01",
            "people with those titles\x01",
            "together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's almost like they're good\x01",
            "friends... I wonder just what\x01",
            "their relationship is.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_212A")

    label("loc_20A4")


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
            "Just what is the\x01",
            "relationship between\x01",
            "those two, I wonder.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_212A")

    Jump("loc_21A6")

    label("loc_212F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_21A6")

    ChrTalk(
        0xFE,
        (
            "The main session has\x01",
            "finally started.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This feeling of\x01",
            "tension... It's affecting\x01",
            "both body and soul.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21A6")

    TalkEnd(0xFE)
    Return()

    # Function_8_1E70 end

    def Function_9_21AA(): pass

    label("Function_9_21AA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21BF")
    Call(0, 10)
    Jump("loc_23DA")

    label("loc_21BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2326")

    ChrTalk(
        0x18,
        (
            "#07108FCome to think of it, it seems Her\x01",
            "Highness returned via the stairs\x01",
            "earlier...\x02\x03",
            "#07103FHmm. Considering how Her Highness\x01",
            "is now, her heart won't be thrown\x01",
            "in disarray by meeting him.\x02\x03",
            "...Needless worrying is useless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F(...Is she talking about\x01",
            "Lechter?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F(Haha. It seems there's\x01",
            "various things between\x01",
            "them.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_23DA")

    label("loc_2326")


    ChrTalk(
        0x18,
        (
            "#07103FPlease contact me if you learn\x01",
            "anything through your security\x01",
            "procedures.\x02\x03",
            "#07100FOn my end, I'll report to the\x01",
            "security planning room\x01",
            "immediately if I learn anything.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23DA")

    TalkEnd(0xFE)
    Return()

    # Function_9_21AA end

    def Function_10_23DE(): pass

    label("Function_10_23DE")

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
        (
            "#07100FHas the situation\x01",
            "changed?\x02",
        )
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
            "received any info?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        "#07103FNo, unfortunately.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#07303F...The Empire is going all out,\x01",
            "but.\x02\x03",
            "#07301FWhether it's the noble faction or\x01",
            "the reformist faction, we haven't\x01",
            "got a lead on either of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10108FIs that so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FThe two major imperial factions...\x01",
            "They seem like unthinkably\x01",
            "troublesome opponents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F............\x02\x03",
            "#00108FUm, Prince Olivert spoke\x01",
            "to you about the "third\x01",
            "option" yesterday, right?\x02\x03",
            "I've been interested in\x01",
            "that this whole time...\x02\x03",
            "#00101FIf it's all right with\x01",
            "you, could we hear a\x01",
            "little more about it?\x02",
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
            "#07300FIn a word― They are Barriers\x01",
            "he's trying to clear away.\x02",
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
        (
            "#00001FClearing away\x01",
            "Barriers...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#07303FIn short, there are\x01",
            "recognizable walls between the\x01",
            "reformist and noble factions.\x02\x03",
            "#07300FFurthermore, they both see\x01",
            "reconciliation as out of the\x01",
            "question.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FReconciliation between\x01",
            "the reformist and noble\x01",
            "factions...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHehe. And the difficulty\x01",
            "there is they both think\x01",
            "idealistically, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101FW-Wazy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#07302FHaha... It's just as you say.\x02\x03",
            "#07304FIt's like that guy decided to confront that\x01",
            ""monster" through some absurd methods.\x02\x03",
            "I don't know if it's the act of a bastard\x01",
            "prince, if it's one of his hobbies or if he's\x01",
            "just showing off. But his mind is made up.\x02\x03",
            "#07302FAnd I've decided to stick with him.\x02",
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
            "#07104FLt. Mueller... As Princess\x01",
            "Klaudia has said, Liberl is\x01",
            "an ally of the prince.\x02\x03",
            "#07102FWe cannot directly intervene,\x01",
            "but please don't hesitate to\x01",
            "ask if you need something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#07304FHmm. I'm deeply\x01",
            "grateful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FThis is why the prince\x01",
            "is who he is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "#07304FHaha. He would never admit to it,\x01",
            "but I'm sure you're right.\x02\x03",
            "#07308FAnyway, right now I need this trade\x01",
            "conference to end without incident―\x01",
            "I will focus on that objective.\x02\x03",
            "#07300FLadies and gentlemen of the Special\x01",
            "Support Section... I look forward\x01",
            "to seeing your results.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x19, 0x0, 0x0)
    OP_93(0x18, 0x0, 0x0)
    OP_4C(0x19, 0xFF)
    OP_4C(0x18, 0xFF)
    SetScenarioFlags(0x1C3, 5)
    Return()

    # Function_10_23DE end

    def Function_11_2D02(): pass

    label("Function_11_2D02")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D17")
    Call(0, 10)
    Jump("loc_2DF2")

    label("loc_2D17")


    ChrTalk(
        0x19,
        (
            "#07303FAnyway, right now I need this trade\x01",
            "conference to end without incident―\x01",
            "I will focus on that objective.\x02\x03",
            "#07300FLadies and gentlemen of the Special\x01",
            "Support Section... I look forward\x01",
            "to seeing your results.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DF2")

    TalkEnd(0xFE)
    Return()

    # Function_11_2D02 end

    def Function_12_2DF6(): pass

    label("Function_12_2DF6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2EA6")

    ChrTalk(
        0xFE,
        (
            "The core floors below 30F you can\x01",
            "get to from the emergency stairs\x01",
            "aren't completely safe yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you're planning on\x01",
            "going there, please be\x01",
            "careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_317E")

    label("loc_2EA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_2FD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F66")

    ChrTalk(
        0xFE,
        (
            "E-Everyone, the\x01",
            "situation has gotten\x01",
            "serious, yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For now, let's work to\x01",
            "protect the floors we're\x01",
            "stationed on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Let's brace ourselves as\x01",
            "we proceed!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2FD3")

    label("loc_2F66")


    ChrTalk(
        0xFE,
        (
            "For now, let's work to\x01",
            "protect the floors we're\x01",
            "stationed on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Let's brace ourselves as\x01",
            "we proceed!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FD3")

    Jump("loc_317E")

    label("loc_2FD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_307E")

    ChrTalk(
        0xFE,
        (
            "*sigh*. The auras of the\x01",
            "VIPs sure are\x01",
            "impressive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter how prepared I am,\x01",
            "every time they pass through\x01",
            "here I unconsciously shrivel up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_317E")

    label("loc_307E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_317E")

    ChrTalk(
        0xFE,
        (
            "The mayor and chairman are using the first\x01",
            "room in this right wing of the VIP floor,\x01",
            "and then there's Prince Olivert ...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Chancellor Osborne is\x01",
            "using the deepest room\x01",
            "in.\x02",
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

    label("loc_317E")

    TalkEnd(0xFE)
    Return()

    # Function_12_2DF6 end

    def Function_13_3182(): pass

    label("Function_13_3182")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_3249")

    ChrTalk(
        0xFE,
        (
            "For now, we've got to\x01",
            "gather the left wing\x01",
            "staff in this room!\x02",
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
    Jump("loc_367B")

    label("loc_3249")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_3408")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3341")

    ChrTalk(
        0xFE,
        (
            "I saw Princess Klaudia\x01",
            "just now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Seeing the VIPs so many times in\x01",
            "one day and being so close to\x01",
            "them... I can hardly believe it.\x02",
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
    Jump("loc_3403")

    label("loc_3341")


    ChrTalk(
        0xFE,
        (
            "Seeing the VIPs so many times in one\x01",
            "day and being so close to them... I\x01",
            "don't think this will happen again.\x02",
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

    label("loc_3403")

    Jump("loc_367B")

    label("loc_3408")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_367B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35FD")

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
            "By the way, out of consideration\x01",
            "for the VIPs, a minimum number of\x01",
            "personnel on patrol on this floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, even though you've been\x01",
            "invited by the heads of state, you\x01",
            "need to maintain confidentiality...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For now, because the heads of state are\x01",
            "accompanied by their escorts during breaks,\x01",
            "there are no problems in the security area.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_367B")

    label("loc_35FD")


    ChrTalk(
        0xFE,
        (
            "Later, during break\x01",
            "time, it'll be harder to\x01",
            "move about this area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you want to check the\x01",
            "rooms, now is the time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_367B")

    TalkEnd(0xFE)
    Return()

    # Function_13_3182 end

    def Function_14_367F(): pass

    label("Function_14_367F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3758")

    ChrTalk(
        0xFE,
        (
            "Archduke Albert of\x01",
            "Remiferia will be using\x01",
            "this room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And, I understand the\x01",
            "Archduke has a deep\x01",
            "knowledge of music.\x02",
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
    Jump("loc_37EC")

    label("loc_3758")


    ChrTalk(
        0xFE,
        (
            "It seems Chairman MacDowell\x01",
            "and Archduke Albert have a\x01",
            "very good relationship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Remiferia is famous as\x01",
            "the sponsor of St.\x01",
            "Ursula Hospital.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37EC")

    TalkEnd(0xFE)
    Return()

    # Function_14_367F end

    def Function_15_37F0(): pass

    label("Function_15_37F0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3801")
    Jump("loc_3ABB")

    label("loc_3801")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_39AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3928")

    ChrTalk(
        0xFE,
        (
            "It's only been one night since martial law\x01",
            "was declared, but the fatigue of everyone\x01",
            "is the tower has already reached a peak.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We don't know what will\x01",
            "happen... As expected, it\x01",
            "seems everyone is worried.\x02",
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
    Jump("loc_39A6")

    label("loc_3928")


    ChrTalk(
        0xFE,
        (
            "The fatigue of everyone\x01",
            "in this tower has\x01",
            "already reached a peak.\x02",
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

    label("loc_39A6")

    Jump("loc_3ABB")

    label("loc_39AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_3ABB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A61")

    ChrTalk(
        0xFE,
        (
            "*work, work, work*...\x01",
            "I've worked up a nice\x01",
            "sweat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Alright. With this, the\x01",
            "potted plant's perfect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now, to once again check\x01",
            "for any dust...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_3ABB")

    label("loc_3A61")


    ChrTalk(
        0xFE,
        (
            "With this, the potted\x01",
            "plant's perfect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now, to once again check\x01",
            "for any dust...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3ABB")

    TalkEnd(0xFE)
    Return()

    # Function_15_37F0 end

    def Function_16_3ABF(): pass

    label("Function_16_3ABF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B80")

    ChrTalk(
        0xFE,
        (
            "This is the room of His\x01",
            "Excellency, Archduke\x01",
            "Albert.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Right now he is visiting\x01",
            "with Chairman MacDowell.\x01",
            "He may have passed you by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you like, please\x01",
            "enter.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_3BF2")

    label("loc_3B80")


    ChrTalk(
        0xFE,
        (
            "Right now he is visiting\x01",
            "with Chairman MacDowell.\x01",
            "He may have passed you by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you like, please\x01",
            "enter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BF2")

    TalkEnd(0xFE)
    Return()

    # Function_16_3ABF end

    def Function_17_3BF6(): pass

    label("Function_17_3BF6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C0B")
    Call(0, 18)
    Jump("loc_3CB5")

    label("loc_3C0B")


    ChrTalk(
        0xFE,
        (
            "Yes. We can't lose focus\x01",
            "in the conference's\x01",
            "second half.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We'll need to especially watch out\x01",
            "for proposals regarding security\x01",
            "guarantees from the major powers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CB5")

    TalkEnd(0xFE)
    SetChrSubChip(0x1A, 0x2)
    Return()

    # Function_17_3BF6 end

    def Function_18_3CBD(): pass

    label("Function_18_3CBD")

    SetChrSubChip(0x1A, 0x2)
    SetChrSubChip(0x2D, 0x1)

    ChrTalk(
        0x1A,
        (
            "*sigh*. Though the arguments are settled,\x01",
            "it's tiring when your opponents are the\x01",
            "heads of state of the major powers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#02509FHaha. But Archduke, your\x01",
            "presence is growing as\x01",
            "well.\x02\x03",
            "Your predecessors would\x01",
            "be proud.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "...It's been five years\x01",
            "since I became head of\x01",
            "my family.\x02",
        )
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3EEA")
    Jump("loc_3F34")

    label("loc_3EEA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3F0A")
    OP_52(0x1A, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3F34")

    label("loc_3F0A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F2A")
    OP_52(0x1A, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3F34")

    label("loc_3F2A")

    OP_52(0x1A, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3F34")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2D, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x2D, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x2D, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x2D, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3FED")
    Jump("loc_4037")

    label("loc_3FED")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2D, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_400D")
    OP_52(0x2D, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4037")

    label("loc_400D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2D, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_402D")
    OP_52(0x2D, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4037")

    label("loc_402D")

    OP_52(0x2D, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x2D, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4037")

    OP_52(0x2D, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2D, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x2D, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_41FF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_40B4")

    ChrTalk(
        0x1A,
        (
            "Ah, you all... Thank you\x01",
            "for your help yesterday.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40CD")

    label("loc_40B4")


    ChrTalk(
        0x1A,
        "Oh, it's you all...\x02",
    )

    CloseMessageWindow()

    label("loc_40CD")


    ChrTalk(
        0x2D,
        (
            "#02505FOh, if it isn't the\x01",
            "Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHello. Sorry for\x01",
            "interrupting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Hmm. I've heard about you. I'd like\x01",
            "to thank you for participating in\x01",
            "the security detail.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "I heard you saved Chairman MacDowell's\x01",
            "life before. From the bottom of my\x01",
            "heart, I know you can be trusted.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4614")

    label("loc_41FF")


    ChrTalk(
        0x1A,
        "Oh, it's you all...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#02500FOh, if it isn't the\x01",
            "Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHello. Sorry for\x01",
            "interrupting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Hmm, so you're the\x01",
            "Special Support Section,\x01",
            "huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "How do you do. I heard\x01",
            "about your exploits from\x01",
            "Arios.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FDo you know Arios?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "Yes. We've been friendly\x01",
            "with the Bracer Guild\x01",
            "for quite a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "My relationship with\x01",
            "Arios is especially\x01",
            "deep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FI see... So that's how\x01",
            "it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "And Elie. It's been a\x01",
            "while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "It seems your remarkable\x01",
            "achievements with the Special\x01",
            "Support Section stand out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FNo... But, thank you.\x02\x03",
            "#00102FI'm just glad Your\x01",
            "Excellency is well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105F(Elie... So she knows\x01",
            "the Archduke.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F(Their speech is\x01",
            "familiar... Even though\x01",
            "he's a head of state.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F(Man. Milady\x01",
            "relationships can't be\x01",
            "called ordinary.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "But, I'm glad famous people like\x01",
            "yourselves are participating in\x01",
            "the security detail.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        (
            "I heard you saved Chairman MacDowell's\x01",
            "life before. From the bottom of my\x01",
            "heart, I know you can be trusted.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4614")


    ChrTalk(
        0x101,
        (
            "#00006FNo, you don't need to\x01",
            "thank us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#02500FHmm. I too think that's\x01",
            "reassuring.\x02\x03",
            "Thanks to you, we'll be able to\x01",
            "concentrate on arguments for\x01",
            "the conference's second half.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FThe conference's second\x01",
            "half...\x02\x03",
            "#00101FGrandfather, do you\x01",
            "expect to be in a\x01",
            "difficult position?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#02503FYes. In contrast to the first half,\x01",
            "painfully true faults of our state will be\x01",
            "pointed out one after the next, you see.\x02\x03",
            "Even so, if the two countries are able to\x01",
            "state their usual demands...\x02\x03",
            "#02501FMy other fear is Dieter.\x02\x03",
            "Even in State Congress, he introduced one\x01",
            "radical idea after the next with great\x01",
            "enthusiasm, but...\x02\x03",
            "It can't be helped that he's young. I'm\x01",
            "worried that vigor will turn in a bad\x01",
            "direction.\x02",
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
            "good or bad fortune... is all up\x01",
            "to how the conference goes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2D,
        (
            "#02503FYes, precisely.\x02\x03",
            "#02500FWell, as chairman, it's\x01",
            "my job to support Dieter\x01",
            "at this conference.\x02\x03",
            "Anyway, I must do what I\x01",
            "can, in my own way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FGrandfather... Thank you\x01",
            "for speaking with us.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C4, 0)
    ClearChrFlags(0x2D, 0x10)
    ClearChrFlags(0x1A, 0x10)
    Return()

    # Function_18_3CBD end

    def Function_19_4AF1(): pass

    label("Function_19_4AF1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B06")
    Call(0, 18)
    Jump("loc_4B85")

    label("loc_4B06")


    ChrTalk(
        0xFE,
        (
            "#02500FWell, as chairman, it's\x01",
            "my job to support Dieter\x01",
            "at this conference.\x02\x03",
            "Anyway, I must do what I\x01",
            "can, in my own way.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B85")

    TalkEnd(0xFE)
    SetChrSubChip(0x2D, 0x1)
    Return()

    # Function_19_4AF1 end

    def Function_20_4B8D(): pass

    label("Function_20_4B8D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_4B9E")
    Jump("loc_4C0F")

    label("loc_4B9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_4BD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BB9")
    Call(0, 21)
    Jump("loc_4BD3")

    label("loc_4BB9")


    ChrTalk(
        0x2A,
        "#08000FScree, scree!\x02",
    )

    CloseMessageWindow()

    label("loc_4BD3")

    Jump("loc_4C0F")

    label("loc_4BD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_4C0F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BF3")
    Call(0, 22)
    Jump("loc_4C0F")

    label("loc_4BF3")


    ChrTalk(
        0x2A,
        "#08000FScree, screeee!\x02",
    )

    CloseMessageWindow()

    label("loc_4C0F")

    TalkEnd(0xFE)
    Return()

    # Function_20_4B8D end

    def Function_21_4C13(): pass

    label("Function_21_4C13")

    OP_4B(0x13, 0xFF)
    OP_93(0x13, 0xB4, 0x0)
    OP_93(0x2A, 0x0, 0x0)

    ChrTalk(
        0x13,
        (
            "#07008FHello Sieg. Could this be a\x01",
            "statement from my grandmother,\x01",
            "who is unable to attend?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        "#08000FScree, scree.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#07000FHaha, I see. ...I am who\x01",
            "I am, I suppose.\x02",
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
            "#00000FSorry for visiting so\x01",
            "suddenly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#07009FNo, please don't worry\x01",
            "about it.\x02\x03",
            "I was thinking things\x01",
            "out by myself... I'm\x01",
            "glad you've come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FPrincess...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F...Could you have been\x01",
            "thinking about the second\x01",
            "half of the conference?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#07000FYes, that too... But it was\x01",
            "something more fundamental.\x02\x03",
            "#07003FAs crown princess, I have a certain\x01",
            "amount of knowledge regarding\x01",
            "diplomatic negotiations, but...\x02\x03",
            "For negotiations, you need insight,\x01",
            "judgment and a sense of balance...\x02\x03",
            "#07001FThe first half of the conference\x01",
            "made me aware that I am lacking in\x01",
            "those areas.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201FThat, huh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FBut, your composure and\x01",
            "logic were plenty\x01",
            "amazing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FYes. And on top of that,\x01",
            "you're the same age as\x01",
            "Lloyd and I...\x02\x03",
            "That's truly awe-\x01",
            "inspiring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#07002FThank you very much.\x02\x03",
            "#07003FBut certainly, the fact that my\x01",
            "voice is small can't be helped.\x02\x03",
            "Though the continent moves, I\x01",
            "will gain experience step-by-step\x01",
            "without rushing, and proceed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FThat's right. And\x01",
            "relaxation is important,\x01",
            "you know.\x02\x03",
            "I mean, it's your break\x01",
            "time right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FWazy... What's with that\x01",
            "attitude in front of the\x01",
            "princess?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#07009FHaha, I don't mind. His lack\x01",
            "of excessive formality makes\x01",
            "me feel a little better.\x02\x03",
            "#07002FBut... It's strange.\x02\x03",
            "Speaking with all of you makes\x01",
            "me feel like I'm speaking with\x01",
            "Estelle and Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106FThose words are more\x01",
            "than we deserve.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#07000FHaha. Well everyone,\x01",
            "would you like some tea?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00005FOh no, please don't\x01",
            "worry about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206FYes. And we have to\x01",
            "finish our patrol.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#07004FI'm sorry. There is that\x01",
            "too.\x02\x03",
            "#07000FBut everyone, please do\x01",
            "be careful.\x02\x03",
            "And I as well will do my\x01",
            "best to carry out my\x01",
            "duty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FYes, roger that.\x02",
    )

    CloseMessageWindow()
    OP_93(0x13, 0xB4, 0x0)
    OP_93(0x2A, 0x0, 0x0)
    OP_4C(0x13, 0xFF)
    SetScenarioFlags(0x1C4, 1)
    Return()

    # Function_21_4C13 end

    def Function_22_540D(): pass

    label("Function_22_540D")

    OP_4B(0x20, 0xFF)
    TurnDirection(0x20, 0x0, 500)

    ChrTalk(
        0x20,
        (
            "My, you're those patrol\x01",
            "officers...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes. Sorry for\x01",
            "interrupting.\x02",
        )
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
            "#00102FHaha. You're Sieg that's\x01",
            "with Her Highness,\x01",
            "Princess Klaudia.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#00205FI see. So you're the\x01",
            "white falcon KeA was\x01",
            "speaking with.\x02",
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
        (
            "#10100FTio, can you understand\x01",
            "him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202FYes, he's saying "Hello"\x01",
            "to everyone. And "How do\x01",
            "you do" to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHaha, he's got a good\x01",
            "memory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2A,
        "#08009FScree, scree!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202F"A matter of course for\x01",
            "Princess Klaudia's\x01",
            "friends", he says.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FHaha, thank you.\x02",
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

    # Function_22_540D end

    def Function_23_56AF(): pass

    label("Function_23_56AF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_56C0")
    Jump("loc_589F")

    label("loc_56C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_57E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5764")

    ChrTalk(
        0xFE,
        (
            "We're looking after the\x01",
            "people trapped in the\x01",
            "tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's a girl in the\x01",
            "right wing... Poor thing,\x01",
            "caught up in all of this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_57DE")

    label("loc_5764")


    ChrTalk(
        0xFE,
        (
            "There's a girl in the\x01",
            "right wing... And she\x01",
            "looks rather depressed.\x02",
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

    label("loc_57DE")

    Jump("loc_589F")

    label("loc_57E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_5836")

    ChrTalk(
        0xFE,
        (
            "A-Anyway... Us staffers\x01",
            "have to remain calm and\x01",
            "do what we can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_589F")

    label("loc_5836")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_5844")
    Jump("loc_589F")

    label("loc_5844")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_589F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_585F")
    Call(0, 22)
    Jump("loc_589F")

    label("loc_585F")


    ChrTalk(
        0xFE,
        (
            "Oh, you know Sieg, do\x01",
            "you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. Sieg is very\x01",
            "clever.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_589F")

    TalkEnd(0xFE)
    Return()

    # Function_23_56AF end

    def Function_24_58A3(): pass

    label("Function_24_58A3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_5948")

    ChrTalk(
        0xFE,
        (
            "You're the Special\x01",
            "Support Section,\x01",
            "correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please everyone, speak\x01",
            "with Her Highness as you\x01",
            "usually do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please, feel free to\x01",
            "enter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5951")

    label("loc_5948")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_5951")

    label("loc_5951")

    TalkEnd(0xFE)
    Return()

    # Function_24_58A3 end

    def Function_25_5955(): pass

    label("Function_25_5955")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_5966")
    Jump("loc_59EA")

    label("loc_5966")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_59E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5981")
    Call(0, 21)
    Jump("loc_59DC")

    label("loc_5981")


    ChrTalk(
        0x13,
        (
            "#07000FEveryone, thank you for\x01",
            "chatting with me.\x02\x03",
            "Let's both focus on\x01",
            "what's to come.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59DC")

    Jump("loc_59EA")

    label("loc_59E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_59EA")

    label("loc_59EA")

    TalkEnd(0xFE)
    Return()

    # Function_25_5955 end

    def Function_26_59EE(): pass

    label("Function_26_59EE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_5A78")

    ChrTalk(
        0xFE,
        (
            "We are waiting here so\x01",
            "as not to interrupt all\x01",
            "of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's in times like these\x01",
            "that we must think\x01",
            "rationally.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B22")

    label("loc_5A78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_5A86")
    Jump("loc_5B22")

    label("loc_5A86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_5B22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5AA1")
    Call(0, 27)
    Jump("loc_5B22")

    label("loc_5AA1")


    ChrTalk(
        0xFE,
        (
            "A steamed bun with a\x01",
            "Mishy print on it, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I feel a little open-\x01",
            "heartedness goes a long way\x01",
            "in a place like this...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B22")

    TalkEnd(0xFE)
    Return()

    # Function_26_59EE end

    def Function_27_5B26(): pass

    label("Function_27_5B26")

    OP_4B(0x1C, 0xFF)
    OP_4B(0x21, 0xFF)

    ChrTalk(
        0x1C,
        (
            "Hmm, but will this do\x01",
            "for tea cakes for the\x01",
            "President?\x02",
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
            "place amazing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "Hmm. Even so, there must\x01",
            "be others, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105F(? Might there be some\x01",
            "problem with the tea\x01",
            "cakes?)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#00201F(I think those are none\x01",
            "other than Mishy steamed\x01",
            "buns... Alias "Michybuns".)\x02\x03",
            "(There's no problem. No\x01",
            "choice could be better.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106F(R-Really?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F(Haha. But I feel like\x01",
            "they could be good\x01",
            "conversation material.)\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x1C, 0xFF)
    OP_4C(0x21, 0xFF)
    SetScenarioFlags(0x1C4, 2)
    Return()

    # Function_27_5B26 end

    def Function_28_5D74(): pass

    label("Function_28_5D74")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_5DBE")

    ChrTalk(
        0xFE,
        (
            "F-First, a deep\x01",
            "breath... *inhaaale*,\x01",
            "*exhaaale*...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E74")

    label("loc_5DBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_5DCC")
    Jump("loc_5E74")

    label("loc_5DCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_5E74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DE7")
    Call(0, 27)
    Jump("loc_5E74")

    label("loc_5DE7")


    ChrTalk(
        0xFE,
        (
            "Hmm. Now that I think\x01",
            "about it, I'm getting\x01",
            "anxious somethow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But at this late hour, I\x01",
            "don't have time to\x01",
            "prepare anything else...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E74")

    TalkEnd(0xFE)
    Return()

    # Function_28_5D74 end

    def Function_29_5E78(): pass

    label("Function_29_5E78")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F67")

    ChrTalk(
        0x17,
        (
            "#07500FYou guys are still here.\x02\x03",
            "Hmm. Would you like to\x01",
            "have tea with me?\x02\x03",
            "#07509FThere's steamed buns\x01",
            "too, so why not make\x01",
            "yourselves at home?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FNo... We can't.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes. Sorry for\x01",
            "interrupting.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_5FEF")

    label("loc_5F67")


    ChrTalk(
        0x17,
        (
            "#07503F*crunch, munch*... But\x01",
            "these steamed buns are\x01",
            "exquisite.\x02\x03",
            "#07509FHahaha. I think I'll\x01",
            "take a few home with me\x01",
            "as souvenirs.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FEF")

    TalkEnd(0xFE)
    Return()

    # Function_29_5E78 end

    def Function_30_5FF3(): pass

    label("Function_30_5FF3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_608F")

    ChrTalk(
        0xFE,
        (
            "Ah, it's only natural,\x01",
            "but... This is no time\x01",
            "to be cleaning rooms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*shiver*... When I think\x01",
            "bad thoughts, I can't\x01",
            "stop shaking.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6193")

    label("loc_608F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_609D")
    Jump("loc_6193")

    label("loc_609D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_6193")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6139")

    ChrTalk(
        0xFE,
        (
            "Looking out over Crossbell\x01",
            "from here really does give\x01",
            "a great view.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I unintentionally stare\x01",
            "out when cleaning\x01",
            "windows.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_6193")

    label("loc_6139")

    OP_93(0xFE, 0x5A, 0x0)

    ChrTalk(
        0xFE,
        (
            "*wipe wipe wipe*... *hum\x01",
            "huhu～m♪*\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*wipe wipe wipe*... *lah\x01",
            "la la～h♪*\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6193")

    TalkEnd(0xFE)
    Return()

    # Function_30_5FF3 end

    def Function_31_6197(): pass

    label("Function_31_6197")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6265")

    ChrTalk(
        0xFE,
        (
            "The mayor and chairman\x01",
            "will share this room\x01",
            "during breaks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For the mayor and chairman battling it out\x01",
            "in the conference, I will put everything I\x01",
            "have into cleaning this room.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_62C8")

    label("loc_6265")


    ChrTalk(
        0xFE,
        (
            "*pat, pat, pat*... Go\x01",
            "for it, Mr. Mayor!♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*pat, pat, pat*... Go\x01",
            "for it, Mr. Chairman!♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62C8")

    TalkEnd(0xFE)
    Return()

    # Function_31_6197 end

    def Function_32_62CC(): pass

    label("Function_32_62CC")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "*sigh*. With this, just\x01",
            "the conference's second\x01",
            "half is left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Honestly though, it'll be more difficult\x01",
            "from here on out... The mayor and\x01",
            "chairman have to do their best for us.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_32_62CC end

    def Function_33_638D(): pass

    label("Function_33_638D")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Ah, everyone. Mayor\x01",
            "Dieter is in Prince\x01",
            "Olivert's room right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "And Chairman MacDowell is in Archduke\x01",
            "Albert's room in the left wing. Both of\x01",
            "them are visiting with their colleagues.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you like, why not try\x01",
            "visiting each of those\x01",
            "rooms directly.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_33_638D end

    def Function_34_649C(): pass

    label("Function_34_649C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_64AD")
    Jump("loc_6947")

    label("loc_64AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6721")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6625")

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
            "I remember having many doubts, but I didn't\x01",
            "question things... Thinking back on it now,\x01",
            "there were a lot of suspicious points.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_671C")

    label("loc_6625")


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
            "I remember having many doubts, but I didn't\x01",
            "question things... Thinking back on it now,\x01",
            "there were a lot of suspicious points.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_671C")

    Jump("loc_6947")

    label("loc_6721")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_67AE")

    ChrTalk(
        0xFE,
        (
            "To think the terrorists\x01",
            "entered the conference\x01",
            "room directly...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just who could have\x01",
            "predicted a situation\x01",
            "like this?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6947")

    label("loc_67AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_67BC")
    Jump("loc_6947")

    label("loc_67BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_6947")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68A9")

    ChrTalk(
        0xFE,
        (
            "This room is for Prince\x01",
            "Olivert during breaks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, the prince is known\x01",
            "in the Empire's high society as\x01",
            "a famous authentic idealist...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I put a lot of energy\x01",
            "even into setting up\x01",
            "this room.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_6947")

    label("loc_68A9")


    ChrTalk(
        0xFE,
        (
            "After all, the prince is known\x01",
            "in the Empire's high society as\x01",
            "a famous authentic idyllist...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I put a lot of energy\x01",
            "even into setting up\x01",
            "this room.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6947")

    TalkEnd(0xFE)
    Return()

    # Function_34_649C end

    def Function_35_694B(): pass

    label("Function_35_694B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_69CF")

    ChrTalk(
        0xFE,
        (
            "Honestly, I can only\x01",
            "think I'm seeing a bad\x01",
            "dream...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I wonder what's going\x01",
            "to happen to everyone\x01",
            "now?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A78")

    label("loc_69CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_69DD")
    Jump("loc_6A78")

    label("loc_69DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_6A78")

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
        (
            "Haha, I'll be happy if\x01",
            "he likes them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A78")

    TalkEnd(0xFE)
    Return()

    # Function_35_694B end

    def Function_36_6A7C(): pass

    label("Function_36_6A7C")

    TalkBegin(0xFE)
    Call(0, 37)
    TalkEnd(0xFE)
    Return()

    # Function_36_6A7C end

    def Function_37_6A86(): pass

    label("Function_37_6A86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_74AC")

    ChrTalk(
        0x2B,
        (
            "#02809FHaha, I see. I have high\x01",
            "hopes for those men and\x01",
            "women in the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2C,
        (
            "#07204FYes. And those people\x01",
            "are not dyed any color.\x02\x03",
            "#07202FThat's why, more and\x01",
            "more―\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2C, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x2C, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x2C, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x2C, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6BF8")
    Jump("loc_6C42")

    label("loc_6BF8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2C, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6C18")
    OP_52(0x2C, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6C42")

    label("loc_6C18")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2C, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6C38")
    OP_52(0x2C, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6C42")

    label("loc_6C38")

    OP_52(0x2C, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x2C, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6C42")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2B, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x2B, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x2B, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x2B, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6CFB")
    Jump("loc_6D45")

    label("loc_6CFB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2B, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6D1B")
    OP_52(0x2B, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6D45")

    label("loc_6D1B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2B, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6D3B")
    OP_52(0x2B, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6D45")

    label("loc_6D3B")

    OP_52(0x2B, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x2B, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6D45")

    OP_52(0x2B, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x2B, 0x10)
    Sleep(100)

    ChrTalk(
        0x2C,
        (
            "#07205FOh, if it isn't the\x01",
            "Support Section.\x02\x03",
            "#07209FCare to join us for a\x01",
            "little chat?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FAh, yes. Sorry to\x01",
            "interrupt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FBy the way, what are you\x01",
            "talking about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        (
            "#02804FOur prince here is actually a\x01",
            "member of the board of directors\x01",
            "of an Imperial military academy.\x02\x03",
            "#02800FI was speaking with him about\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205FDirector. That's one of\x01",
            "the people responsible\x01",
            "for a school, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FHeh, so you know even\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2C,
        (
            "#07204FHaha. It's nothing more\x01",
            "than a name I'm\x01",
            "borrowing.\x02\x03",
            "#07202FAnd, they say Mayor\x01",
            "Dieter's contribution is\x01",
            "even greater than my own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FMayor Dieter?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        (
            "#02804FAh, well, in the end, it's just\x01",
            "business.\x02\x03",
            "#02800FThat military academy received a small\x01",
            "amount of funding from IBC for the\x01",
            "Epstein Foundation's orbal network test.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FI-I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205FNow that you mention it, I\x01",
            "heard orbal network tests had\x01",
            "started in the Empire, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHehe. As expected from an international bank\x01",
            "with branch offices in each nation. Their\x01",
            "business is nothing if not widespread.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2C,
        (
            "#07202FHmm. I feel a connection with\x01",
            "you all, talking like this.\x02\x03",
            "#07209FIf there's an opportunity, would\x01",
            "you feel like giving a special\x01",
            "lecture at my military academy?\x02\x03",
            "#07212FIf you are interested, be aware\x01",
            "that relations between lecturers\x01",
            "and students is prohibited.\x02",
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
        (
            "#00006FW-What are you talking\x01",
            "about?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x2B, 0x1)

    ChrTalk(
        0x2B,
        (
            "#02809FHaha. You must be quite\x01",
            "pleased, Prince Olivert.\x02\x03",
            "After this, I'd like to\x01",
            "have a relaxed chat over\x01",
            "drinks.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x2C, 0x0)

    ChrTalk(
        0x2C,
        (
            "#07209FHaha, indeed. I would\x01",
            "love to join you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2B, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x2C, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)

    ChrTalk(
        0x102,
        (
            "#00109F(The prince and\x01",
            ""uncle"... They've\x01",
            "really hit it off.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F(Yeah. Maybe they get along\x01",
            "because their hobbies have\x01",
            "the same scale?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C3, 7)
    Jump("loc_75E3")

    label("loc_74AC")


    ChrTalk(
        0x2B,
        (
            "#02805FBy the way, can you hold\x01",
            "your liquor?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2C,
        (
            "#07202FYeah, to a certain\x01",
            "extent.\x02\x03",
            "#07204F...There's many in this\x01",
            "world who are better\x01",
            "than me, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F(His Highness... He has\x01",
            "a distant look,\x01",
            "somehow.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(...? I wonder if he has some\x01",
            "kind of important memories\x01",
            "related to alcohol?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_75E3")

    Return()

    # Function_37_6A86 end

    def Function_38_75E4(): pass

    label("Function_38_75E4")

    TalkBegin(0xFE)
    Call(0, 37)
    TalkEnd(0xFE)
    Return()

    # Function_38_75E4 end

    def Function_39_75EE(): pass

    label("Function_39_75EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7601")
    Call(0, 51)
    Return()

    label("loc_7601")

    TalkBegin(0xFE)

    ChrTalk(
        0x14,
        (
            "#11501FOh, is that Armorica\x01",
            "Village?\x02\x03",
            "#11509FThe bees are diligently\x01",
            "carrying honey.\x02",
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
        (
            "#00006FC'mon. There's no way\x01",
            "you can see that.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_39_75EE end

    def Function_40_76F9(): pass

    label("Function_40_76F9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_77C9")

    ChrTalk(
        0xFE,
        (
            "We've been held here\x01",
            "ever since martial law\x01",
            "was declared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Come to think of it, he\x01",
            "had a girl with a\x01",
            "mysterious aura with him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Could she have been the\x01",
            "rumored Divine Child?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_783B")

    label("loc_77C9")


    ChrTalk(
        0xFE,
        (
            "The President had a girl\x01",
            "with a mysterious aura\x01",
            "with him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Could she have been the\x01",
            "rumored Divine Child?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_783B")

    TalkEnd(0xFE)
    Return()

    # Function_40_76F9 end

    def Function_41_783F(): pass

    label("Function_41_783F")

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
            "W-Who could have thought\x01",
            "this would happen. And\x01",
            "what will happen now...?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_41_783F end

    def Function_42_78FC(): pass

    label("Function_42_78FC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7AC0")

    ChrTalk(
        0xFE,
        "L-Lady Elie!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FLanfei... Thank goodness\x01",
            "you're safe.\x02\x03",
            "It looks like all the\x01",
            "IBC personnel are\x01",
            "assembled here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Y-Yes... Just as Miss\x01",
            "Mariabell ordered...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The situation in the city has\x01",
            "become troublesome... What are Mr.\x01",
            "Dieter and Lady Mariabell up to...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F...Anyway, please stay\x01",
            "here for the time being.\x02\x03",
            "We'll do something about\x01",
            "this situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "U-Understood... I'll\x01",
            "leave it to you, then.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_7B31")

    label("loc_7AC0")


    ChrTalk(
        0xFE,
        (
            "I wonder what are Mr.\x01",
            "Dieter and Lady\x01",
            "Mariabell up to...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...And, I'm sure that\x01",
            "person with him was...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B31")

    TalkEnd(0xFE)
    Return()

    # Function_42_78FC end

    def Function_43_7B35(): pass

    label("Function_43_7B35")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C2D")

    ChrTalk(
        0xFE,
        (
            "The President and the others aren't\x01",
            "on this floor... but the other\x01",
            "people here may know something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Leave this place to me for\x01",
            "now. Feel free to conduct\x01",
            "your investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...However, don't do\x01",
            "anything reckless.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 3)
    Jump("loc_7CA8")

    label("loc_7C2D")


    ChrTalk(
        0xFE,
        (
            "Leave this place to me for\x01",
            "now. Feel free to conduct\x01",
            "your investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...However, don't do\x01",
            "anything reckless.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7CA8")

    TalkEnd(0xFE)
    Return()

    # Function_43_7B35 end

    def Function_44_7CAC(): pass

    label("Function_44_7CAC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D80")

    ChrTalk(
        0xFE,
        (
            "I believed in Miss Mariabell\x01",
            "and remained in the\x01",
            "Technology Division, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Clay said he couldn't\x01",
            "trust her and left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We fought and split\x01",
            "up... But it appears\x01",
            "Clay was right.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 4)
    Jump("loc_7DE7")

    label("loc_7D80")


    ChrTalk(
        0xFE,
        (
            "...It appears Clay was\x01",
            "right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Though we fought and\x01",
            "split up, I wonder if we\x01",
            "can reconcile...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7DE7")

    TalkEnd(0xFE)
    Return()

    # Function_44_7CAC end

    def Function_45_7DEB(): pass

    label("Function_45_7DEB")

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
            "terminals either.\x01",
            "Goodness...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_45_7DEB end

    def Function_46_7E88(): pass

    label("Function_46_7E88")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FA4")

    ChrTalk(
        0xFE,
        (
            "The Security Department needs a\x01",
            "certain understanding of the tower\x01",
            "layout and personnel duties.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But ever since we moved into\x01",
            "Orchis Tower, I got the feeling\x01",
            "there was more hidden than usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What in the world are\x01",
            "Mariabell and the others\x01",
            "doing...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 5)
    Jump("loc_7FE2")

    label("loc_7FA4")


    ChrTalk(
        0xFE,
        (
            "What in the world are\x01",
            "Mariabell and the others\x01",
            "doing...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7FE2")

    TalkEnd(0xFE)
    Return()

    # Function_46_7E88 end

    def Function_47_7FE6(): pass

    label("Function_47_7FE6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8102")

    ChrTalk(
        0xFE,
        (
            "The jaeger group Red Constellation, with a\x01",
            "threat rating of S... I suspected President\x01",
            "Dieter of being connected to them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't believe the guys who\x01",
            "destroyed IBC are wandering\x01",
            "around so brazenly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...The President... He\x01",
            "can no longer be\x01",
            "trusted.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 6)
    Jump("loc_8138")

    label("loc_8102")


    ChrTalk(
        0xFE,
        (
            "President Dieter... He\x01",
            "can no longer be\x01",
            "trusted.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8138")

    TalkEnd(0xFE)
    Return()

    # Function_47_7FE6 end

    def Function_48_813C(): pass

    label("Function_48_813C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8245")

    ChrTalk(
        0xC,
        (
            "#11228FI think father has been\x01",
            "worried about this for a\x01",
            "very long time.\x02\x03",
            "And about mother... And me\x01",
            "too.\x02\x03",
            "He's overthought various\x01",
            "things... About how he can't\x01",
            "go back to how he was...\x02\x03",
            "#11227F...Everyone... Please take\x01",
            "care of my father!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 7)
    Jump("loc_827D")

    label("loc_8245")


    ChrTalk(
        0xC,
        (
            "#11227FEveryone, please... Take\x01",
            "care of my father!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_827D")

    TalkEnd(0xFE)
    Return()

    # Function_48_813C end

    def Function_49_8281(): pass

    label("Function_49_8281")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_85DE")

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
            "#6P#00003F#6PYes, thanks for your\x01",
            "hard work.\x02\x03",
            "#00005FCould this room be...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#11PYes, it's President\x01",
            "Crois'... No, Suspect\x01",
            "Crois.\x02",
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
        (
            "#6P#00108F...How is the President\x01",
            "doing?\x02",
        )
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
            "#11PPer direction of\x01",
            "Inspector Sergei, you all\x01",
            "are allowed to see him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00306FIs that so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00208F...Lloyd, what should we\x01",
            "do?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AF, 7)
    Jump("loc_865D")

    label("loc_85DE")


    ChrTalk(
        0x11,
        (
            "#11PSuspect Crois is\x01",
            "detained in this room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#11PPer direction of\x01",
            "Inspector Sergei, you all\x01",
            "are allowed to see him...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_865D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8667")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_876E")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Meet with Dieter\x01",      # 0
            "Refuse\x01",                # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_86C9")
    Call(0, 50)
    Return()

    label("loc_86C9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8769")

    ChrTalk(
        0x101,
        "#6P#00006F...Not right now.\x02",
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
            "to meet with Suspect Crois,\x01",
            "please speak with me again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8769")

    Jump("loc_8667")

    label("loc_876E")

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

    # Function_49_8281 end

    def Function_50_87A5(): pass

    label("Function_50_87A5")


    ChrTalk(
        0x101,
        (
            "#6P#00003F...If you please.\x02\x03",
            "#00008FWhat is he thinking about\x01",
            "right now? ...I feel I\x01",
            "want to ask him that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00106F...............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#11PUnderstood... Go ahead,\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x11, 0x0, 0x1F4)

    def lambda_8867():
        OP_95(0xFE, 111300, 0, -101000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8867)
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
            "#11301F#5P......You guys, huh.\x02\x03",
            "#11304F...Heh, what do you want?\x01",
            "I'm an international\x01",
            "criminal now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00001F...Dieter.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00108F..."Uncle"...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        (
            "#11306F#5P...Being alone like this, I finally\x01",
            "realized.\x02\x03",
            "It's as Bell said. I did nothing\x01",
            "more than act as Mr. Grimwood\x01",
            "wanted me to.\x02\x03",
            "#11303FWith a loud voice, I held the ideal\x01",
            "of "justice", and for that reason,\x01",
            "sacrifices were acceptable.\x02\x03",
            "#11311F...And what was the result? I've\x01",
            "been abandoned by my only daughter,\x01",
            "and now I've lost the presidency.\x02\x03",
            "#11302F...Hahaha... I'm not that boy from\x01",
            "Ouroboros, but I'm just as pitiful\x01",
            "a "Fool".\x02",
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
            "#12P#00006F...We can't deny any of that.\x02\x03",
            "#00008FFor our own "justice", we will break\x01",
            "through anything, anywhere...\x02\x03",
            "#00001FRegardless of your methods, the fact\x01",
            "that you were trying to protect\x01",
            "Crossbell is the absolute truth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303F...You're telling me.\x02\x03",
            "#00301FWe felt it back when you\x01",
            "said those words to us\x01",
            "at IBC too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203F"Humans are creatures that desire\x01",
            "justice"... You can certainly say that.\x02\x03",
            "#00208FAnd through the declaration of\x01",
            "independence that the citizens approved,\x01",
            "you felt you were pursuing "justice".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        "#11303F#5P...............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00106FBut in the end, I think your\x01",
            "methods were wrong.\x02\x03",
            "#00108FIf the independent state continued,\x01",
            "your "justice" recognized and peace\x01",
            "obtained, "uncle"...\x02\x03",
            "The wounds of the people discarded\x01",
            "in the process wouldn't have been\x01",
            "so easily healed.\x02\x03",
            "#00101FA peace based on the premise of\x01",
            "sacrificing people...\x02\x03",
            "Doesn't that make the declaration\x01",
            "of independence you uttered on the\x01",
            "platform that day deception itself?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        (
            "#11304F#5P...Hehe. You're right Elie. It is as\x01",
            "you say.\x02\x03",
            "By obtaining the power called KeA, I\x01",
            "might have been blinded by my own\x01",
            ""justice".\x02\x03",
            "#11302FMr. Grimwood saw that I had deceived\x01",
            "myself without realizing it, and I\x01",
            "became easy to manipulate.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_922D")

    ChrTalk(
        0x10A,
        "#12P#00603F(...Lawyer Ian...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_928C")

    label("loc_922D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_925F")

    ChrTalk(
        0x105,
        "#12P#10403F............\x02",
    )

    CloseMessageWindow()
    Jump("loc_928C")

    label("loc_925F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_928C")

    ChrTalk(
        0x106,
        "#12P#10703F............\x02",
    )

    CloseMessageWindow()

    label("loc_928C")


    ChrTalk(
        0x2B,
        (
            "#11303F#5PHowever... "Justice" is something\x01",
            "exercised through power and will.\x01",
            "That idea itself will never change.\x02\x03",
            "#11301FIf you all would continue your own\x01",
            "pursuit of "justice"...\x02\x03",
            "You need to show Mr. Grimwood and\x01",
            "the others your own power and will.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006F...It won't be easy...\x01",
            "But we will do it, no\x01",
            "matter what it takes.\x02\x03",
            "#00013FWe'll have to, if we're\x01",
            "going to take back KeA!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9447")

    ChrTalk(
        0x106,
        "#12P#10701F...Right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_94B2")

    label("loc_9447")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_947E")

    ChrTalk(
        0x109,
        "#12P#10101FAlright, we will.\x02",
    )

    CloseMessageWindow()
    Jump("loc_94B2")

    label("loc_947E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_94B2")

    ChrTalk(
        0x105,
        "#12P#10402FHehe, that's right.\x02",
    )

    CloseMessageWindow()

    label("loc_94B2")


    ChrTalk(
        0x2B,
        (
            "#11301F#5P...In that case, you have no further\x01",
            "use for me.\x02\x03",
            "#11303FGrimwood said it himself... Even though\x01",
            "Bell is my daughter, I honestly have no\x01",
            "idea how far she is willing to go.\x02\x03",
            "#11304FWhether you can proceed and take back\x01",
            "KeA...\x02\x03",
            "#11300FI can see the answer right here.\x02",
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
            "#00108FI'm worried because Bell\x01",
            "discarded him like that,\x01",
            "but...\x02\x03",
            "#00102FHe's surprisingly\x01",
            "composed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00004F...Yeah. I'm a little\x01",
            "worried too.\x02\x03",
            "#00000FIt's like he said... We\x01",
            "need to move forward.\x02",
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

    # Function_50_87A5 end

    def Function_51_9866(): pass

    label("Function_51_9866")

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
            "#11P#11504FBut what a view, really.\x02\x03",
            "#11500FDon't you agree, Special\x01",
            "Support Section?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00011FLechter...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00108FWhat are you doing in a\x01",
            "place like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#11P#11504FHaha. If the staff of His Excellency, the\x01",
            "Chancellor, is in the waiting room of the same,\x01",
            "surely there's nothing strange about that.\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 3)), scpexpr(EXPR_END)), "loc_9B26")

    AnonymousTalk(
        0x14,
        (
            "Ah, we meet again.\x02\x03",
            "But no... I guess the first time\x01",
            "was by mistake.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_9B8B")

    label("loc_9B26")


    AnonymousTalk(
        0x14,
        (
            "It's been several weeks\x01",
            "since we last met.\x02\x03",
            "But no... I guess the\x01",
            "first time was by\x01",
            "mistake.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_9B8B")

    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    ChrTalk(
        0x102,
        (
            "#6P#00106FUmm... I'm asking you, so please\x01",
            "don't joke around with such a\x01",
            "serious look on your face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00211F...How should I say it.\x01",
            "He's cunning, as always.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#11P#11509FHaha, that's my charm\x01",
            "point, you see!\x02\x03",
            "#11502FBut, it looks like you\x01",
            "wanted to say something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FYes. Thanks to you we got\x01",
            "word of several situations.\x02\x03",
            "#00013FAbout this trade\x01",
            "conference... And the actions\x01",
            "of your Imperial government.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#11P#11510FHmm, I see. I don't know how\x01",
            "much you've learned, but...\x02\x03",
            "#11504FDid you know this?\x02\x03",
            "#11501F―I'm actually collaborating\x01",
            "with the Noble Faction, and I'm\x01",
            "after Giliath Osborne's life.\x02",
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
        "#6P#10107FWhat!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10301FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106F...Don't be deceived.\x01",
            "Just look at who's\x01",
            "saying it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00301FWe won't fall for that\x01",
            "one again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00211FHe's making fun of us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#11P#11509FHah, oh well then.\x02\x03",
            "#11502FI was hoping for a\x01",
            "better reaction, to tell\x01",
            "you the truth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FHaha, so the punchline\x01",
            "isn't that it's actually\x01",
            "true?\x02",
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
            "#00001FBecause of that, you should at least be\x01",
            "able to help us with security during the\x01",
            "conference...\x02\x03",
            "#00000F─Am I wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#11P#11504FHaha... I see.\x02\x03",
            "#11508FWell, that remark before was a\x01",
            "joke... but you could imagine\x01",
            "something like that happening, right?\x02\x03",
            "#11501FWe must always be searching for those\x01",
            "patterns.\x02\x03",
            "#11509FThat's the secret to being a good\x01",
            "writer, right?\x02",
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
            "#6P#00006FI don't think there are\x01",
            "any authors here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00301FMan, just how much is\x01",
            "this guy going to tease\x01",
            "us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#11P#11504FWell, that's all the\x01",
            "advice I can give for the\x01",
            "moment.\x02\x03",
            "#11500FYou should think about\x01",
            "the various cases, and be\x01",
            "ready for any of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106F...Thanks for the\x01",
            "warning.\x02",
        )
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
            "#6P#00108F(Right. I feel it's\x01",
            "because he threw us off\x01",
            "guard.)\x02",
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

    # Function_51_9866 end

    def Function_52_A501(): pass

    label("Function_52_A501")

    Sound(160, 0, 100, 0)
    Return()

    # Function_52_A501 end

    def Function_53_A508(): pass

    label("Function_53_A508")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A530")
    SetScenarioFlags(0x146, 3)

    label("loc_A530")

    Return()

    # Function_53_A508 end

    def Function_54_A531(): pass

    label("Function_54_A531")

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
            "#6P#10302FHaha, I could spend\x01",
            "plenty of "me" time in a\x01",
            "room like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        (
            "#6P#02804FThis is Prince Olivert's waiting\x01",
            "room.\x02\x03",
            "#02800FThere are rooms in the left wing\x01",
            "as well, and each participant has\x01",
            "been assigned a room.\x02\x03",
            "#02809FIt's a place to cool heads if they\x01",
            "get too hot in the conference, if\x01",
            "you get my meaning.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_ABE8():
        TurnDirection(0x101, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_ABE8)
    Sleep(50)

    def lambda_ABF8():
        TurnDirection(0x109, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_ABF8)
    Sleep(50)

    def lambda_AC08():
        TurnDirection(0x102, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_AC08)
    Sleep(50)

    def lambda_AC18():
        TurnDirection(0x105, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_AC18)
    Sleep(50)

    def lambda_AC28():
        TurnDirection(0x103, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_AC28)
    Sleep(50)

    def lambda_AC38():
        TurnDirection(0x104, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_AC38)
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
            "rooms aside...\x02\x03",
            "#02800FI've one final place to\x01",
            "show you.\x02",
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

    def lambda_AEB0():
        OP_98(0xFE, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x35, 1, lambda_AEB0)

    def lambda_AECA():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_AECA)
    Sleep(50)

    def lambda_AEE7():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AEE7)
    Sleep(50)

    def lambda_AF04():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AF04)
    Sleep(50)

    def lambda_AF21():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_AF21)
    Sleep(50)

    def lambda_AF3E():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AF3E)
    Sleep(50)

    def lambda_AF5B():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0xFFFFFED4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AF5B)
    Sleep(50)

    def lambda_AF78():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_AF78)
    FadeToBright(1000, 0)
    Sleep(600)

    def lambda_AF9E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_AF9E)
    Sleep(300)

    def lambda_AFB2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_AFB2)
    Sleep(600)

    def lambda_AFC6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_AFC6)
    Sleep(300)

    def lambda_AFDA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_AFDA)
    OP_0D()
    OP_4B(0x11, 0xFF)
    SetChrChipByIndex(0x11, 0x29)
    SetChrSubChip(0x11, 0x0)

    ChrTalk(
        0x11,
        "#12A#5PIt's Mayor Dieter!\x02",
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
        (
            "#12A#5PThanks for your hard\x01",
            "work!\x02",
        )
    )

    Sleep(1200)
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x2B, 1)

    ChrTalk(
        0x2B,
        "#02809F#11PHaha, at ease, please.\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x35, 1)
    OP_6B(0xFF)
    WaitChrThread(0x105, 1)
    OP_93(0x2B, 0x5A, 0x1F4)

    ChrTalk(
        0x2B,
        (
            "#6P#02804FFrom these corridor windows,\x01",
            "you can get a full view of\x01",
            "the conference.\x02\x03",
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

    def lambda_B163():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B163)
    Sleep(50)

    def lambda_B173():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_B173)
    Sleep(50)

    def lambda_B183():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B183)
    Sleep(50)

    def lambda_B193():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B193)
    Sleep(50)

    def lambda_B1A3():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_B1A3)
    Sleep(50)

    def lambda_B1B3():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_B1B3)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    OP_68(-2000, 1500, -124000, 3000)
    MoveCamera(35, 17, 0, 3000)
    SetCameraDistance(19500, 3000)

    def lambda_B1FD():
        OP_97(0x101, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B1FD)
    Sleep(200)

    def lambda_B21A():
        OP_97(0x103, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_B21A)
    Sleep(200)

    def lambda_B237():
        OP_97(0x109, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B237)
    Sleep(200)

    def lambda_B254():
        OP_97(0x102, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B254)
    Sleep(200)

    def lambda_B271():
        OP_97(0x104, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_B271)
    Sleep(200)

    def lambda_B28E():
        OP_97(0x105, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_B28E)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)

    def lambda_B2C0():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_B2C0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00002F#11PIt's great to be able to\x01",
            "check on the conference\x01",
            "room like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#11PThat's right. If anything\x01",
            "happens, we could be\x01",
            "there right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F#11PIn that case, I want to\x01",
            "make this part of our\x01",
            "patrol route.\x02",
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
            "#6P#02803FNow then. With this,\x01",
            "I've showed you the\x01",
            "three secure floors...\x02\x03",
            "#02800FBut, if you'll allow me\x01",
            "to show this last place\x01",
            "I've been saving...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B48F():
        TurnDirection(0x101, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B48F)
    Sleep(50)

    def lambda_B49F():
        TurnDirection(0x109, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B49F)
    Sleep(50)

    def lambda_B4AF():
        TurnDirection(0x102, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B4AF)
    Sleep(50)

    def lambda_B4BF():
        TurnDirection(0x105, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_B4BF)
    Sleep(50)

    def lambda_B4CF():
        TurnDirection(0x103, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_B4CF)
    Sleep(50)

    def lambda_B4DF():
        TurnDirection(0x104, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_B4DF)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)

    ChrTalk(
        0x101,
        "#00005F#5PA place you were saving?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00302F#11PHuh? Where is that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2B,
        (
            "#6P#02809FHaha, the place with the\x01",
            "best view in this\x01",
            "building.\x02",
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

    # Function_54_A531 end

    def Function_55_B5B6(): pass

    label("Function_55_B5B6")

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

    # Function_55_B5B6 end

    def Function_56_B635(): pass

    label("Function_56_B635")


    def lambda_B63A():
        OP_95(0xFE, 81000, 0, 1500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B63A)

    def lambda_B654():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B654)
    WaitChrThread(0xFE, 1)

    def lambda_B669():
        OP_95(0xFE, 77500, 0, -1000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B669)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_56_B635 end

    def Function_57_B68A(): pass

    label("Function_57_B68A")


    def lambda_B68F():
        OP_95(0xFE, 81000, 0, 2000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B68F)

    def lambda_B6A9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B6A9)
    WaitChrThread(0xFE, 1)

    def lambda_B6BE():
        OP_95(0xFE, 79200, 0, -400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B6BE)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_57_B68A end

    def Function_58_B6DF(): pass

    label("Function_58_B6DF")


    def lambda_B6E4():
        OP_95(0xFE, 81000, 0, 2000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B6E4)

    def lambda_B6FE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B6FE)
    WaitChrThread(0xFE, 1)

    def lambda_B713():
        OP_95(0xFE, 78300, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B713)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_58_B6DF end

    def Function_59_B734(): pass

    label("Function_59_B734")


    def lambda_B739():
        OP_95(0xFE, 81000, 0, 2500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B739)

    def lambda_B753():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B753)
    WaitChrThread(0xFE, 1)

    def lambda_B768():
        OP_95(0xFE, 80400, 0, -100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B768)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_59_B734 end

    def Function_60_B789(): pass

    label("Function_60_B789")


    def lambda_B78E():
        OP_95(0xFE, 81000, 0, 2500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B78E)

    def lambda_B7A8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B7A8)
    WaitChrThread(0xFE, 1)

    def lambda_B7BD():
        OP_95(0xFE, 79500, 0, 800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B7BD)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_60_B789 end

    def Function_61_B7DE(): pass

    label("Function_61_B7DE")


    def lambda_B7E3():
        OP_95(0xFE, 81000, 0, 3000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B7E3)

    def lambda_B7FD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B7FD)
    WaitChrThread(0xFE, 1)

    def lambda_B812():
        OP_95(0xFE, 80800, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B812)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_61_B7DE end

    def Function_62_B833(): pass

    label("Function_62_B833")


    def lambda_B838():
        OP_95(0xFE, 81000, 0, 3000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B838)

    def lambda_B852():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B852)
    WaitChrThread(0xFE, 1)

    def lambda_B867():
        OP_95(0xFE, 79900, 0, 2100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B867)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_62_B833 end

    def Function_63_B888(): pass

    label("Function_63_B888")


    def lambda_B88D():
        OP_95(0xFE, 109000, 0, -130500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B88D)
    WaitChrThread(0xFE, 1)

    def lambda_B8AB():
        OP_95(0xFE, 109000, 0, -112500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B8AB)
    WaitChrThread(0xFE, 1)

    def lambda_B8C9():
        OP_95(0xFE, 111000, 0, -110500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B8C9)
    WaitChrThread(0xFE, 1)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0x5, 0x0, 0x0)

    def lambda_B8FF():
        OP_95(0xFE, 113000, 0, -110500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B8FF)
    Sleep(500)

    def lambda_B91C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B91C)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_63_B888 end

    def Function_64_B92D(): pass

    label("Function_64_B92D")


    def lambda_B932():
        OP_95(0xFE, 109000, -600, -130500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B932)
    WaitChrThread(0xFE, 1)
    Sleep(1000)
    MoveCamera(35, 19, 0, 7000)
    SetCameraDistance(19000, 7000)

    def lambda_B967():
        OP_95(0xFE, 109000, -600, -112500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B967)
    WaitChrThread(0xFE, 1)

    def lambda_B985():
        OP_95(0xFE, 111000, -600, -110500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B985)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_64_B92D end

    def Function_65_B99F(): pass

    label("Function_65_B99F")


    def lambda_B9A4():
        OP_97(0xFE, 0xFFFFF254, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B9A4)
    Sleep(300)

    def lambda_B9C1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B9C1)
    WaitChrThread(0xFE, 1)

    def lambda_B9D6():
        OP_97(0xFE, 0xFFFFFC18, 0x0, 0x3E8, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B9D6)
    WaitChrThread(0xFE, 1)
    SetScenarioFlags(0x0, 0)

    def lambda_B9F7():
        OP_97(0xFE, 0x0, 0x0, 0x4650, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B9F7)
    WaitChrThread(0xFE, 1)

    def lambda_BA15():

        label("loc_BA15")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_BA15")

    QueueWorkItem2(0xFE, 2, lambda_BA15)
    Return()

    # Function_65_B99F end

    def Function_66_BA23(): pass

    label("Function_66_BA23")


    def lambda_BA28():
        OP_97(0xFE, 0xFFFFF448, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BA28)
    Sleep(300)

    def lambda_BA45():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BA45)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_AD(0x0)
    Sleep(100)

    def lambda_BA67():
        OP_97(0xFE, 0x0, 0x0, 0x4268, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BA67)
    WaitChrThread(0xFE, 1)

    def lambda_BA85():

        label("loc_BA85")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_BA85")

    QueueWorkItem2(0xFE, 2, lambda_BA85)
    Return()

    # Function_66_BA23 end

    def Function_67_BA93(): pass

    label("Function_67_BA93")


    def lambda_BA98():
        OP_97(0xFE, 0xFFFFEDA4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BA98)
    Sleep(400)

    def lambda_BAB5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BAB5)
    WaitChrThread(0xFE, 1)

    def lambda_BACA():
        OP_97(0xFE, 0xFFFFFC18, 0x0, 0x3E8, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BACA)
    WaitChrThread(0xFE, 1)
    SetScenarioFlags(0x0, 1)

    def lambda_BAEB():
        OP_97(0xFE, 0x0, 0x0, 0x3F48, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BAEB)
    WaitChrThread(0xFE, 1)

    def lambda_BB09():

        label("loc_BB09")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_BB09")

    QueueWorkItem2(0xFE, 2, lambda_BB09)
    Return()

    # Function_67_BA93 end

    def Function_68_BB17(): pass

    label("Function_68_BB17")


    def lambda_BB1C():
        OP_97(0xFE, 0xFFFFEF98, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BB1C)
    Sleep(400)

    def lambda_BB39():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BB39)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_AD(0x1)
    Sleep(100)

    def lambda_BB5B():
        OP_97(0xFE, 0x0, 0x0, 0x3B60, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BB5B)
    WaitChrThread(0xFE, 1)

    def lambda_BB79():

        label("loc_BB79")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_BB79")

    QueueWorkItem2(0xFE, 2, lambda_BB79)
    Return()

    # Function_68_BB17 end

    def Function_69_BB87(): pass

    label("Function_69_BB87")


    def lambda_BB8C():
        OP_97(0xFE, 0xFFFFE8F4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BB8C)
    Sleep(500)

    def lambda_BBA9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BBA9)
    WaitChrThread(0xFE, 1)

    def lambda_BBBE():
        OP_97(0xFE, 0xFFFFFC18, 0x0, 0x3E8, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BBBE)
    WaitChrThread(0xFE, 1)
    SetScenarioFlags(0x0, 2)

    def lambda_BBDF():
        OP_97(0xFE, 0x0, 0x0, 0x3B60, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BBDF)
    WaitChrThread(0xFE, 1)

    def lambda_BBFD():

        label("loc_BBFD")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_BBFD")

    QueueWorkItem2(0xFE, 2, lambda_BBFD)
    Return()

    # Function_69_BB87 end

    def Function_70_BC0B(): pass

    label("Function_70_BC0B")


    def lambda_BC10():
        OP_97(0xFE, 0xFFFFEAE8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BC10)
    Sleep(500)

    def lambda_BC2D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BC2D)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_AD(0x2)
    Sleep(100)

    def lambda_BC4F():
        OP_97(0xFE, 0x0, 0x0, 0x3778, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BC4F)
    WaitChrThread(0xFE, 1)

    def lambda_BC6D():

        label("loc_BC6D")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_BC6D")

    QueueWorkItem2(0xFE, 2, lambda_BC6D)
    Return()

    # Function_70_BC0B end

    def Function_71_BC7B(): pass

    label("Function_71_BC7B")


    def lambda_BC80():
        OP_95(0xFE, 111000, 0, -110500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BC80)
    WaitChrThread(0xFE, 1)

    def lambda_BC9E():
        OP_95(0xFE, 113000, 0, -110500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BC9E)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_71_BC7B end

    def Function_72_BCB8(): pass

    label("Function_72_BCB8")


    def lambda_BCBD():
        OP_95(0xFE, 109000, 0, -130500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BCBD)
    WaitChrThread(0xFE, 1)

    def lambda_BCDB():
        OP_95(0xFE, 100000, 0, -130500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BCDB)
    Sleep(3200)

    def lambda_BCF8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BCF8)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_72_BCB8 end

    def Function_73_BD09(): pass

    label("Function_73_BD09")


    def lambda_BD0E():
        OP_95(0xFE, 109000, -600, -130500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BD0E)
    WaitChrThread(0xFE, 1)

    def lambda_BD2C():
        OP_95(0xFE, 103000, -600, -130500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BD2C)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_73_BD09 end

    def Function_74_BD46(): pass

    label("Function_74_BD46")


    def lambda_BD4B():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFC43C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BD4B)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_AD(0x0)

    def lambda_BD73():
        OP_97(0xFE, 0xFFFFDCD8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BD73)
    Sleep(2700)

    def lambda_BD90():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BD90)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_74_BD46 end

    def Function_75_BDA1(): pass

    label("Function_75_BDA1")


    def lambda_BDA6():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFC43C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BDA6)
    WaitChrThread(0xFE, 1)

    def lambda_BDC4():
        OP_97(0xFE, 0xFFFFF8F8, 0x0, 0xFFFFF8F8, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BDC4)
    WaitChrThread(0xFE, 1)
    SetScenarioFlags(0x0, 0)

    def lambda_BDE5():
        OP_97(0xFE, 0xFFFFDCD8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BDE5)
    Sleep(2700)

    def lambda_BE02():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BE02)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_75_BDA1 end

    def Function_76_BE13(): pass

    label("Function_76_BE13")


    def lambda_BE18():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BE18)
    WaitChrThread(0xFE, 1)
    Sleep(700)

    def lambda_BE39():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFFA88, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BE39)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_AD(0x1)

    def lambda_BE61():
        OP_97(0xFE, 0xFFFFDCD8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BE61)
    Sleep(2800)

    def lambda_BE7E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BE7E)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_76_BE13 end

    def Function_77_BE8F(): pass

    label("Function_77_BE8F")


    def lambda_BE94():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFBFF0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BE94)
    WaitChrThread(0xFE, 1)

    def lambda_BEB2():
        OP_97(0xFE, 0xFFFFF8F8, 0x0, 0xFFFFF8F8, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BEB2)
    WaitChrThread(0xFE, 1)
    SetScenarioFlags(0x0, 1)

    def lambda_BED3():
        OP_97(0xFE, 0xFFFFDCD8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BED3)
    Sleep(2800)

    def lambda_BEF0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BEF0)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_77_BE8F end

    def Function_78_BF01(): pass

    label("Function_78_BF01")


    def lambda_BF06():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFC694, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BF06)
    WaitChrThread(0xFE, 1)
    Sleep(1100)

    def lambda_BF27():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF510, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BF27)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_AD(0x2)

    def lambda_BF4F():
        OP_97(0xFE, 0xFFFFDCD8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BF4F)
    Sleep(2900)

    def lambda_BF6C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BF6C)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_78_BF01 end

    def Function_79_BF7D(): pass

    label("Function_79_BF7D")


    def lambda_BF82():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFBBA4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BF82)
    WaitChrThread(0xFE, 1)
    Sleep(500)

    def lambda_BFA3():
        OP_97(0xFE, 0xFFFFF8F8, 0x0, 0xFFFFF8F8, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BFA3)
    WaitChrThread(0xFE, 1)
    SetScenarioFlags(0x0, 2)

    def lambda_BFC4():
        OP_97(0xFE, 0xFFFFDCD8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BFC4)
    Sleep(2900)

    def lambda_BFE1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BFE1)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_79_BF7D end

    def Function_80_BFF2(): pass

    label("Function_80_BFF2")

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
            "#00000FI heard Arios was\x01",
            "coming, but to think\x01",
            "Lawyer Ian's here too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202F#5PAnd what's more, it\x01",
            "seems he's known by the\x01",
            "name Mr. Beardy Bear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FAt international conferences, various\x01",
            "agreements are made.\x02\x03",
            "#00100FWhen that happens, it's necessary to judge\x01",
            "whether such agreements are valid based on\x01",
            "existing international and common law.\x02",
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
            "#12P#10302FSo that Mr. Beardy Bear\x01",
            "is here to advise on\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FIt's great that the conference has\x01",
            "started... But it looks they're\x01",
            "discussing some difficult things.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x2E, 0x10E, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x2E,
        (
            "#00603F#11PWell, it's not our place to be\x01",
            "concerned with the details of\x01",
            "the conference discussions.\x02\x03",
            "#00600FWill this conference end\x01",
            "without issue? Focus only on\x01",
            "making sure it does.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-1500, 1300, -127550, 1500)

    def lambda_C516():
        TurnDirection(0x101, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_C516)
    Sleep(50)

    def lambda_C526():
        TurnDirection(0x102, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_C526)
    Sleep(50)

    def lambda_C536():
        TurnDirection(0x109, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_C536)
    Sleep(50)

    def lambda_C546():
        TurnDirection(0x103, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_C546)
    Sleep(50)

    def lambda_C556():
        TurnDirection(0x105, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_C556)
    Sleep(50)

    def lambda_C566():
        TurnDirection(0x104, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_C566)
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
            "#5P#00101FThen, do we do as\x01",
            "planned?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2E,
        (
            "#00604F#11PYes. You all will patrol 34,\x01",
            "35 and 36F for me.\x02\x03",
            "#00602FFor now, given your social\x01",
            "standing, you're to speak\x01",
            "only with staff.\x02\x03",
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
            "#00603F#11PI'm heading back to 34F,\x01",
            "then.\x02\x03",
            "#00600F...May the Goddess\x01",
            "protect you. Call me if\x01",
            "anything happens.\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x2E, 0xDAC, 0xFFFE0430, 0x1F4)
    OP_68(9000, 1300, -130000, 4000)

    def lambda_C766():
        OP_95(0xFE, 5500, 0, -130000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_C766)
    WaitChrThread(0x2E, 1)

    def lambda_C784():
        OP_95(0xFE, 11500, 0, -130000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_C784)
    Sleep(2000)

    def lambda_C7A1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_C7A1)
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
            "#00008F#5P...It seems Dudley also\x01",
            "thinks something will\x01",
            "happen.\x02",
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
            "#00211F#5PWith so many suspicious\x01",
            "actions lately, it'd be\x01",
            "strange if nothing happened.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(150)

    ChrTalk(
        0x109,
        (
            "#12P#10101FLooks like we'll need to\x01",
            "be extra careful on our\x01",
            "patrols.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C8FC():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_C8FC)
    Sleep(50)

    def lambda_C90C():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_C90C)
    Sleep(50)

    def lambda_C91C():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_C91C)
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
        (
            "#6P#10300FShall we start our\x01",
            "patrol, then?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#5P#00001FYeah. Let's speak with\x01",
            "the various staff members\x01",
            "during our patrol.\x02",
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

    # Function_80_BFF2 end

    def Function_81_CA66(): pass

    label("Function_81_CA66")

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
            "#11P#00000FAlright... This\x01",
            "completes our patrol.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FIt seems there's nothing\x01",
            "particularly wrong at\x01",
            "present.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00302FWe should make another\x01",
            "loop around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FRight...\x02\x03",
            "#00108FI wonder how the\x01",
            "conference is going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00006FYeah... I'm sure the Mayor\x01",
            "and the Chairman are doing\x01",
            "their best, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00201FThe problem is the Blood\x01",
            "and Iron Chancellor and\x01",
            "President Rocksmith, yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FWell, maybe we should\x01",
            "ask someone about it\x01",
            "during the break.\x02",
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

    # Function_81_CA66 end

    def Function_82_CD3F(): pass

    label("Function_82_CD3F")

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
            "#11P#00000FAlright... This\x01",
            "completes our patrol.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FIt seems there's nothing\x01",
            "particularly wrong at\x01",
            "present.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00302FWe should make another\x01",
            "loop around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FRight...\x02\x03",
            "#00108FI wonder how the\x01",
            "conference is going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00006FYeah... I'm sure the Mayor\x01",
            "and the Chairman are doing\x01",
            "their best, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00201FThe problem is the Blood\x01",
            "and Iron Chancellor and\x01",
            "President Rocksmith, yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FWell, maybe we should\x01",
            "ask someone about it\x01",
            "during the break.\x02",
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

    # Function_82_CD3F end

    def Function_83_D018(): pass

    label("Function_83_D018")

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
        "#5P─We've been waiting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#5PYou are the people of\x01",
            "Crossbell Police's Special\x01",
            "Support Section, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00001F...Yes. And this is the\x01",
            "President's room?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#5PYes. I've been told to\x01",
            "let you through.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x15, 0x0, 0x1F4)

    def lambda_D1BC():
        OP_95(0xFE, -3200, 0, 28500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_D1BC)
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
            "#12P#10108F(He's leader of Calvard,\x01",
            "one of the continent's\x01",
            "largest countries...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#11P#00306F(I'm a bit nervous...)\x02",
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

    # Function_83_D018 end

    def Function_84_D323(): pass

    label("Function_84_D323")


    def lambda_D328():
        OP_95(0xFE, -3200, 0, 27000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D328)
    WaitChrThread(0xFE, 1)

    def lambda_D346():
        OP_95(0xFE, -5500, 0, 27000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D346)
    Sleep(600)

    def lambda_D363():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D363)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_84_D323 end

    def Function_85_D374(): pass

    label("Function_85_D374")

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
        "#5P─Thank you for coming.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#5PI think Chancellor\x01",
            "Osborne's room is on the\x01",
            "other side.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D544():

        label("loc_D544")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_D544")

    QueueWorkItem2(0x101, 2, lambda_D544)

    def lambda_D556():

        label("loc_D556")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_D556")

    QueueWorkItem2(0x102, 2, lambda_D556)
    Sleep(50)

    def lambda_D56B():

        label("loc_D56B")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_D56B")

    QueueWorkItem2(0x103, 2, lambda_D56B)
    Sleep(50)

    def lambda_D580():

        label("loc_D580")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_D580")

    QueueWorkItem2(0x109, 2, lambda_D580)
    Sleep(50)

    def lambda_D595():

        label("loc_D595")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_D595")

    QueueWorkItem2(0x105, 2, lambda_D595)
    Sleep(50)

    def lambda_D5AA():

        label("loc_D5AA")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_D5AA")

    QueueWorkItem2(0x104, 2, lambda_D5AA)

    ChrTalk(
        0x101,
        "#11P#00011F...Ah, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#11P#00103FThanks for helping us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#5PDon't mention it. Well\x01",
            "then.\x02",
        )
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

    def lambda_D6E9():
        TurnDirection(0x105, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_D6E9)
    Sleep(50)

    def lambda_D6F9():
        TurnDirection(0x109, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_D6F9)
    Sleep(50)

    def lambda_D709():
        TurnDirection(0x104, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_D709)
    Sleep(50)

    def lambda_D719():
        TurnDirection(0x102, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_D719)
    Sleep(50)

    def lambda_D729():
        TurnDirection(0x101, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D729)
    Sleep(50)

    def lambda_D739():
        TurnDirection(0x103, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_D739)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)

    ChrTalk(
        0x105,
        (
            "#10309F#11PHaha, he has a great attitude.\x01",
            "It's just what you'd expect from\x01",
            "the leader of a large country.\x02\x03",
            "#10302FHe's quite the sly fox, isn't\x01",
            "he?\x02",
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
            "#00211FI don't think he was\x01",
            "trying to pressure us,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#5PHe was probably just trying to put on a\x01",
            "good show.\x02\x03",
            "#00103FThe Republican President, putting on a\x01",
            "show where he decorates we who contributed\x01",
            "to the cult incident's resolution...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FHe said Crossbell's\x01",
            "incidents are their\x01",
            "incidents...\x02\x03",
            "#00001FThat restates the Republic's\x01",
            "dominion over Crossbell as a\x01",
            "subject state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#5PMan... I wonder if that's the\x01",
            "real reason he wanted to meet\x01",
            "with us.\x02\x03",
            "#00301FThe leader of a large\x01",
            "country... I guess you never\x01",
            "know what to expect from them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F#11PYeah. The difference from\x01",
            "state congresspeople is\x01",
            "night and day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10108F...I wonder what the\x01",
            "chancellor wants to\x01",
            "speak with us about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001F...No idea. Anyway,\x01",
            "let's think about his\x01",
            "possible motives.\x02",
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

    # Function_85_D374 end

    def Function_86_DBC9(): pass

    label("Function_86_DBC9")


    def lambda_DBCE():
        OP_95(0xFE, -3200, 0, 27000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DBCE)

    def lambda_DBE8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DBE8)
    WaitChrThread(0xFE, 1)

    def lambda_DBFD():
        OP_95(0xFE, -1500, 0, 26400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DBFD)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_86_DBC9 end

    def Function_87_DC1E(): pass

    label("Function_87_DC1E")


    def lambda_DC23():
        OP_95(0xFE, -3200, 0, 27000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DC23)

    def lambda_DC3D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DC3D)
    WaitChrThread(0xFE, 1)

    def lambda_DC52():
        OP_95(0xFE, -1200, 0, 27700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DC52)
    WaitChrThread(0xFE, 1)

    def lambda_DC70():

        label("loc_DC70")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_DC70")

    QueueWorkItem2(0xFE, 2, lambda_DC70)
    Return()

    # Function_87_DC1E end

    def Function_88_DC7E(): pass

    label("Function_88_DC7E")


    def lambda_DC83():
        OP_95(0xFE, -3200, 0, 27000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DC83)

    def lambda_DC9D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DC9D)
    WaitChrThread(0xFE, 1)

    def lambda_DCB2():
        OP_95(0xFE, 100, 0, 26800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DCB2)
    WaitChrThread(0xFE, 1)

    def lambda_DCD0():

        label("loc_DCD0")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_DCD0")

    QueueWorkItem2(0xFE, 2, lambda_DCD0)
    Return()

    # Function_88_DC7E end

    def Function_89_DCDE(): pass

    label("Function_89_DCDE")


    def lambda_DCE3():
        OP_95(0xFE, -3200, 0, 27000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DCE3)

    def lambda_DCFD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DCFD)
    WaitChrThread(0xFE, 1)

    def lambda_DD12():
        OP_95(0xFE, 400, 0, 28100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DD12)
    WaitChrThread(0xFE, 1)

    def lambda_DD30():

        label("loc_DD30")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_DD30")

    QueueWorkItem2(0xFE, 2, lambda_DD30)
    Return()

    # Function_89_DCDE end

    def Function_90_DD3E(): pass

    label("Function_90_DD3E")


    def lambda_DD43():
        OP_95(0xFE, -3200, 0, 27000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DD43)

    def lambda_DD5D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DD5D)
    WaitChrThread(0xFE, 1)

    def lambda_DD72():
        OP_95(0xFE, -1500, 0, 25100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DD72)
    WaitChrThread(0xFE, 1)

    def lambda_DD90():

        label("loc_DD90")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_DD90")

    QueueWorkItem2(0xFE, 2, lambda_DD90)
    Return()

    # Function_90_DD3E end

    def Function_91_DD9E(): pass

    label("Function_91_DD9E")


    def lambda_DDA3():
        OP_95(0xFE, -3200, 0, 27000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DDA3)

    def lambda_DDBD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DDBD)
    WaitChrThread(0xFE, 1)

    def lambda_DDD2():
        OP_95(0xFE, 100, 0, 25500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DDD2)
    WaitChrThread(0xFE, 1)

    def lambda_DDF0():

        label("loc_DDF0")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_DDF0")

    QueueWorkItem2(0xFE, 2, lambda_DDF0)
    Return()

    # Function_91_DD9E end

    def Function_92_DDFE(): pass

    label("Function_92_DDFE")

    EventBegin(0x0)

    def lambda_DE05():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_DE05)
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
            "#00001F(So that's the\x01",
            "chancellor's room,\x01",
            "huh...)\x02\x03",
            "#00003F(Break time will probably\x01",
            "be over once we finish\x01",
            "visiting with him.)\x02\x03",
            "#00008F(Is there anything else\x01",
            "we need to do?)\x02",
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

    # Function_92_DDFE end

    def Function_93_DF31(): pass

    label("Function_93_DF31")

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
        (
            "#11PCrossbell Police,\x01",
            "Special Support Section,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x16, 0x0, 0x1F4)

    def lambda_E02C():
        OP_95(0xFE, 111300, 0, -101000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_E02C)
    WaitChrThread(0x16, 1)
    OP_93(0x16, 0xE1, 0x1F4)

    ChrTalk(
        0x16,
        (
            "#5PHis Excellency is\x01",
            "waiting. You can enter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00001FY-Yes, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00104FThen, if you'll excuse\x01",
            "me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00211F(He seems kind of\x01",
            "arrogant.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F(That's how the Imperial\x01",
            "military is. Pointlessly\x01",
            "overbearing.)\x02",
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
            "#6P#00003F#6PExcuse us, Chancellor\x01",
            "Osborne.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F#6PThank you for inviting\x01",
            "the Support Section.\x02",
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

    def lambda_E4BE():
        OP_96(0xFE, 0x2673C, 0x0, 0x1AA90, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E4BE)
    Sleep(300)

    def lambda_E4DB():
        OP_96(0xFE, 0x266D8, 0x0, 0x1AE78, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E4DB)
    Sleep(50)

    def lambda_E4F8():
        OP_96(0xFE, 0x260FC, 0x0, 0x1AA90, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_E4F8)
    Sleep(100)

    def lambda_E515():
        OP_96(0xFE, 0x26098, 0x0, 0x1AE78, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_E515)
    Sleep(100)

    def lambda_E532():
        OP_96(0xFE, 0x26548, 0x0, 0x1A450, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_E532)
    Sleep(100)

    def lambda_E54F():
        OP_96(0xFE, 0x26098, 0x0, 0x1A450, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_E54F)
    WaitChrThread(0x109, 1)

    def lambda_E56D():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_E56D)
    WaitChrThread(0x105, 1)

    def lambda_E57E():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_E57E)
    Sleep(500)

    ChrTalk(
        0x2F,
        (
            "#07400F#11P─It's truly a magnificent view.\x02\x03",
            "To think humans could build this\x01",
            "structure to look down at the\x01",
            "ground from such a height...\x02\x03",
            "#07404FHaha, it's proof that we've\x01",
            "finally reached the glory that\x01",
            "ancient civilization once had.\x02",
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
            "#6P#00200FYou're talking about the\x01",
            "ancient Zemurian civilization\x01",
            "of 1200 years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305F#6PYeah. They say their\x01",
            "civilization was almost\x01",
            "magical in its convenience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2F,
        (
            "#07400F#11PIt wasn't necessarily a simple\x01",
            "utopia.\x02\x03",
            "#07404FLast year, the giant city that\x01",
            "floated above Liberl during\x01",
            "that phenomenon last year...\x02\x03",
            "That too was constructed in the\x01",
            "ancient Zemurian period, and it\x01",
            "was sealed away by human hands.\x02\x03",
            "#07401FIt is a true symbol of both the\x01",
            "foolishness and the\x01",
            "possibilities of mankind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001FFoolishness and\x01",
            "possibilities, you\x01",
            "say...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#6PBut... You sure know a\x01",
            "lot about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2F,
        (
            "#07404F#11PHaha, not that much.\x02\x03",
            "#07400FIn relation to Crossbell, I\x01",
            "failed to learn the truth that\x01",
            "Joachim was a cult priest.\x02",
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
        "#6P#00208FSo you even do that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2F,
        (
            "#07404F#11PHaha, it's precisely because\x01",
            "of the unknown that this\x01",
            "world is so interesting.\x02\x03",
            "If we had everything in the\x01",
            "palm of our hand, it would\x01",
            "be the height of boredom.\x02\x03",
            "#07400FDon't you agree, Wazy\x01",
            "Hemisphere?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#N#10306F...Hmph. So you know my\x01",
            "name as well.\x02\x03",
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
            "#07400F#11PThere's not much I'm not\x01",
            "interested in.\x02\x03",
            "#07404FThe successor of the War\x01",
            "God is very interesting\x01",
            "indeed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#6PYou...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FThe Imperial\x01",
            "Intelligence Division...\x02\x03",
            "#00001FIt seems you have\x01",
            "impressive intelligence\x01",
            "gathering capabilities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2F,
        "#07404F#11PHehe...\x02",
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
            "representative of the Imperial\x01",
            "government.\x02\x03",
            "I have heard all about you from\x01",
            "Lechter.\x02\x03",
            "Won't you join me for a chat during\x01",
            "the remainder of our break?\x02",
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
            "#12P#00003FSo then, Chancellor.\x02\x03",
            "#00001FWhat exactly would you\x01",
            "like to discuss with us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00211FIt seems you're already\x01",
            "aware of the current\x01",
            "situation.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)

    ChrTalk(
        0x2F,
        (
            "#07404F#11POh, this is just a\x01",
            "simple chat.\x02\x03",
            "#07400FIf possible, I would\x01",
            "like your opinion on\x01",
            "something.\x02",
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
            "#07403F#11PI'll ask you directly:\x02\x03",
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
        "#12P#00013F#4S...!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10306FAnother blunt\x01",
            "question...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x2F, 0x1)
    Sleep(300)

    ChrTalk(
        0x2F,
        (
            "#07400F#5PHaha, it's not out of malice.\x02\x03",
            "#07403FIt's just that there's one constant\x01",
            "throughout history─ There are no\x01",
            "nations that haven't been destroyed.\x02\x03",
            "To say nothing of the orbal\x01",
            "revolution, which accelerated\x01",
            "everything in the current era.\x02\x03",
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
            "#6P#10107FF-Forever!\x02\x03",
            "As long as the citizens\x01",
            "of this state have the\x01",
            "will to protect it!\x02",
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
            "#07400F#5PYes. Strong will is\x01",
            "critical.\x02\x03",
            "In rare cases, trends\x01",
            "reverse and history\x01",
            "itself changes.\x02\x03",
            "#07404FThe people are not\x01",
            "powerless. I believe in\x01",
            "their potential.\x02",
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
            "#07400F#5P─But, what happens in a\x01",
            "clash of wills?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x32, 0x0, 0xBB8, 0x96)

    ChrTalk(
        0x109,
        "#6P#10111F...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x2F,
        (
            "#07401F#5PIt's simple─ When a small will is\x01",
            "engulfed by a large one, its\x01",
            "flames intensify.\x02\x03",
            "#07404FAnd when the hellfire that is born\x01",
            "appears above ground...\x02\x03",
            "All justice and morality dissolves\x01",
            "in the heat, and the whole world\x01",
            "is engulfed in its flames.\x02\x03",
            "#07402F─Such a scene is easy to imagine,\x01",
            "no?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00210F#40WAhhh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10110F#40WUgh...!\x02",
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
            "#12P#00003F#30WIndeed, our will might be\x01",
            "small compared to the\x01",
            "Empire or Republic...\x02\x03",
            "#00008FBut it's not definite that\x01",
            "a smaller flame will be\x01",
            "engulfed by a bigger one.\x02\x03",
            "#00007F#20WJust like the Imperial\x01",
            "invasion Liberl once\x01",
            "repelled!\x02",
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
        (
            "#6P#10304FThe "Hundred Days' War"\x01",
            "12 years ago, huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x2F,
        (
            "#07404F#5PHaha, exactly. Will is a question of\x01",
            ""Strength".\x02\x03",
            "Liberl's small yet strong will overcame\x01",
            "the large but disorganized will of the\x01",
            "Empire.\x02\x03",
            "Crossbell could learn something from\x01",
            "that example.\x02\x03",
            "#07402FIn the end, I don't know if the citizens\x01",
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
            "#07404F#11PHaha, break time's over.\x01",
            "Let's end our discussion\x01",
            "here.\x02\x03",
            "#07400F─Oh yes, and I don't intend\x01",
            "to give you an award from\x01",
            "the Imperial government.\x02\x03",
            "When awards are given to\x01",
            ""commoners", the nobles\x01",
            "become quite noisy, you see.\x02",
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
            "#5PIt's rare to see His\x01",
            "Excellency in such a\x01",
            "good mood.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FCAA():

        label("loc_FCAA")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_FCAA")

    QueueWorkItem2(0x101, 2, lambda_FCAA)

    def lambda_FCBC():

        label("loc_FCBC")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_FCBC")

    QueueWorkItem2(0x102, 2, lambda_FCBC)
    Sleep(50)

    def lambda_FCD1():

        label("loc_FCD1")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_FCD1")

    QueueWorkItem2(0x103, 2, lambda_FCD1)

    def lambda_FCE3():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_FCE3)
    Sleep(50)

    def lambda_FCF3():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_FCF3)

    def lambda_FD00():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_FD00)

    ChrTalk(
        0x101,
        "#12P#00005FHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00301FHey, is that some kind\x01",
            "of joke?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHe must have taken an\x01",
            "interest in you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PHis words may have been\x01",
            "weighty, but you should\x01",
            "accept them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5P─Though I shouldn't be\x01",
            "saying such things in my\x01",
            "position.\x02",
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

    def lambda_FEF0():
        TurnDirection(0x102, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_FEF0)
    Sleep(50)

    def lambda_FF00():
        TurnDirection(0x104, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_FF00)
    Sleep(50)

    def lambda_FF10():
        TurnDirection(0x101, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_FF10)
    Sleep(50)

    def lambda_FF20():
        TurnDirection(0x109, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_FF20)
    Sleep(50)

    def lambda_FF30():
        TurnDirection(0x105, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_FF30)
    Sleep(50)

    def lambda_FF40():
        TurnDirection(0x103, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_FF40)
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
        (
            "#5P#00106F...I suppose it was\x01",
            "reasonable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00310FYeah, but he's a real\x01",
            "monster...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00006FHow to say it... I feel\x01",
            "like he has a different\x01",
            "perspective.\x02\x03",
            "#00001F─Tio, are you okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00206FYes, somehow.\x02\x03",
            "#00208FThe images of flames he told\x01",
            "us about was too intense.\x01",
            "I'm a little dizzy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#10106FI don't blame you...\x01",
            "Even I felt I could see\x01",
            "them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10308F#5PThe Blood and Iron\x01",
            "Chancellor, huh. What a\x01",
            "monster.\x02\x03",
            "#10303FIt seems he's thinking\x01",
            "of swallowing Crossbell\x01",
            "in one gulp.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#11P#00003FBut he didn't call us\x01",
            "here to torment us.\x02\x03",
            "The President too... I\x01",
            "think their interest in\x01",
            "us is no lie.\x02\x03",
            "#00000FIn that case, maybe it's\x01",
            "best to think of it as a\x01",
            "good learning experience.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_10255():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_10255)
    Sleep(0)

    def lambda_10265():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_10265)
    Sleep(0)

    def lambda_10275():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_10275)
    Sleep(0)

    def lambda_10285():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_10285)
    Sleep(0)

    def lambda_10295():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_10295)
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
        "#10302F#5PHehe, I suppose.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00104FI think that's the part\x01",
            "of your personality I\x01",
            "can't imitate well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00309FYeah... You're too\x01",
            "positive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#5P#10101FB-But... I can't help\x01",
            "feeling a bit depressed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00202FThat's true... But we\x01",
            "should take this as a\x01",
            "lesson.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00003FAnyway, break time's over.\x02\x03",
            "#00001FLet's head back to Dudley\x01",
            "and let him know the\x01",
            "results of our interviews.\x02",
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

    # Function_93_DF31 end

    def Function_94_10534(): pass

    label("Function_94_10534")


    def lambda_10539():
        OP_95(0xFE, 111300, 0, -102500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10539)
    WaitChrThread(0xFE, 1)

    def lambda_10557():
        OP_95(0xFE, 113000, 0, -102500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10557)
    Sleep(600)

    def lambda_10574():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10574)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_94_10534 end

    def Function_95_10585(): pass

    label("Function_95_10585")


    def lambda_1058A():
        OP_96(0xFE, 0x24540, 0x0, 0x19E10, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1058A)

    def lambda_105A4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_105A4)
    WaitChrThread(0xFE, 1)

    def lambda_105B9():
        OP_95(0xFE, 151000, 0, 105200, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_105B9)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_95_10585 end

    def Function_96_105DA(): pass

    label("Function_96_105DA")


    def lambda_105DF():
        OP_96(0xFE, 0x24540, 0x0, 0x19E10, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_105DF)

    def lambda_105F9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_105F9)
    WaitChrThread(0xFE, 1)

    def lambda_1060E():
        OP_95(0xFE, 151000, 0, 106300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1060E)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_96_105DA end

    def Function_97_1062F(): pass

    label("Function_97_1062F")


    def lambda_10634():
        OP_96(0xFE, 0x24540, 0x0, 0x19E10, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10634)

    def lambda_1064E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1064E)
    WaitChrThread(0xFE, 1)

    def lambda_10663():
        OP_95(0xFE, 150100, 0, 104600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10663)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_97_1062F end

    def Function_98_10684(): pass

    label("Function_98_10684")


    def lambda_10689():
        OP_96(0xFE, 0x24540, 0x0, 0x19E10, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10689)

    def lambda_106A3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_106A3)
    WaitChrThread(0xFE, 1)

    def lambda_106B8():
        OP_95(0xFE, 150100, 0, 106900, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_106B8)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_98_10684 end

    def Function_99_106D9(): pass

    label("Function_99_106D9")


    def lambda_106DE():
        OP_96(0xFE, 0x24540, 0x0, 0x19E10, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_106DE)

    def lambda_106F8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_106F8)
    WaitChrThread(0xFE, 1)

    def lambda_1070D():
        OP_95(0xFE, 149200, 0, 105200, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1070D)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_99_106D9 end

    def Function_100_1072E(): pass

    label("Function_100_1072E")


    def lambda_10733():
        OP_96(0xFE, 0x24540, 0x0, 0x19E10, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10733)

    def lambda_1074D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1074D)
    WaitChrThread(0xFE, 1)

    def lambda_10762():
        OP_95(0xFE, 149200, 0, 106300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10762)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_100_1072E end

    def Function_101_10783(): pass

    label("Function_101_10783")


    def lambda_10788():
        OP_95(0xFE, 110500, 0, -102500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10788)

    def lambda_107A2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_107A2)
    WaitChrThread(0xFE, 1)

    def lambda_107B7():
        OP_95(0xFE, 109100, 0, -103400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_107B7)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_101_10783 end

    def Function_102_107D8(): pass

    label("Function_102_107D8")


    def lambda_107DD():
        OP_95(0xFE, 110500, 0, -102500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_107DD)

    def lambda_107F7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_107F7)
    WaitChrThread(0xFE, 1)

    def lambda_1080C():
        OP_95(0xFE, 109300, 0, -102300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1080C)
    WaitChrThread(0xFE, 1)

    def lambda_1082A():

        label("loc_1082A")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_1082A")

    QueueWorkItem2(0xFE, 2, lambda_1082A)
    Return()

    # Function_102_107D8 end

    def Function_103_10838(): pass

    label("Function_103_10838")


    def lambda_1083D():
        OP_95(0xFE, 110500, 0, -102500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1083D)

    def lambda_10857():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10857)
    WaitChrThread(0xFE, 1)

    def lambda_1086C():
        OP_95(0xFE, 107600, 0, -103100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1086C)
    WaitChrThread(0xFE, 1)

    def lambda_1088A():

        label("loc_1088A")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_1088A")

    QueueWorkItem2(0xFE, 2, lambda_1088A)
    Return()

    # Function_103_10838 end

    def Function_104_10898(): pass

    label("Function_104_10898")


    def lambda_1089D():
        OP_95(0xFE, 110500, 0, -102500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1089D)

    def lambda_108B7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_108B7)
    WaitChrThread(0xFE, 1)

    def lambda_108CC():
        OP_95(0xFE, 107300, 0, -102000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_108CC)
    WaitChrThread(0xFE, 1)

    def lambda_108EA():

        label("loc_108EA")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_108EA")

    QueueWorkItem2(0xFE, 2, lambda_108EA)
    Return()

    # Function_104_10898 end

    def Function_105_108F8(): pass

    label("Function_105_108F8")


    def lambda_108FD():
        OP_95(0xFE, 110500, 0, -102500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_108FD)

    def lambda_10917():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10917)
    WaitChrThread(0xFE, 1)

    def lambda_1092C():
        OP_95(0xFE, 109000, 0, -101000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1092C)
    WaitChrThread(0xFE, 1)

    def lambda_1094A():

        label("loc_1094A")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_1094A")

    QueueWorkItem2(0xFE, 2, lambda_1094A)
    Return()

    # Function_105_108F8 end

    def Function_106_10958(): pass

    label("Function_106_10958")


    def lambda_1095D():
        OP_95(0xFE, 110500, 0, -102500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1095D)

    def lambda_10977():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_10977)
    WaitChrThread(0xFE, 1)

    def lambda_1098C():
        OP_95(0xFE, 108000, 0, -100300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1098C)
    WaitChrThread(0xFE, 1)

    def lambda_109AA():

        label("loc_109AA")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_109AA")

    QueueWorkItem2(0xFE, 2, lambda_109AA)
    Return()

    # Function_106_10958 end

    def Function_107_109B8(): pass

    label("Function_107_109B8")

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
        "#12P#10107FThis is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F#11PIt's just as Lawyer Ian\x01",
            "feared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10308FIt seems like the Blood and Iron\x01",
            "Chancellor and the President are\x01",
            "shoving this down Crossbell's throat.\x02\x03",
            "#10301FIs there no basis for an objection?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#11PIt's true that's there's\x01",
            "various structural flaws\x01",
            "in Crossbell's laws.\x02\x03",
            "#00108FThat's why it's difficult\x01",
            "for Mayor Dieter and my\x01",
            "grandfather to object.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00006F─But, those defects were\x01",
            "forced on Crossbell during\x01",
            "its founding 70 years ago.\x02\x03",
            "#00013FOn top of that, no one\x01",
            "could agree with their\x01",
            "overbearing statements.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00301FHmph. So this crime was\x01",
            "premeditated.\x02",
        )
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
            "discussions are none of our\x01",
            "business.\x02\x03",
            "Right now, we need to focus on\x01",
            "making sure the meeting comes\x01",
            "to an end without incident.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-1500, 1300, -127550, 1300)

    def lambda_10F18():
        TurnDirection(0x101, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_10F18)
    Sleep(50)

    def lambda_10F28():
        TurnDirection(0x102, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_10F28)
    Sleep(50)

    def lambda_10F38():
        TurnDirection(0x109, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_10F38)
    Sleep(50)

    def lambda_10F48():
        TurnDirection(0x103, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_10F48)
    Sleep(50)

    def lambda_10F58():
        TurnDirection(0x105, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_10F58)
    Sleep(50)

    def lambda_10F68():
        TurnDirection(0x104, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_10F68)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00001F#6PYes, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00108FIn that case, perhaps\x01",
            "another patrol─\x02",
        )
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
            "#00603F#5PSection One, it's\x01",
            "Dudley.\x02\x03",
            "#00605FEma. What in the world─\x02",
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
        (
            "#5P#00108F(It looks like something\x01",
            "happened...)\x02",
        )
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
            "#00606F#11P─Red Constellation and\x01",
            "Heiyue have each left\x01",
            "their respective bases.\x02\x03",
            "#00601FIt seems they've shaken\x01",
            "off our surveillance.\x02",
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
            "#00601FI'll let you know if\x01",
            "anything else happens.\x01",
            "Stay on your guard.\x02",
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

    def lambda_1137B():
        OP_95(0xFE, 5500, 0, -130000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_1137B)
    Sleep(500)

    ChrTalk(
        0x2E,
        (
            "#5P#00603F#12A─Oh, that's right.\x02\x03",
            "#14A#00601FMaybe I should mobilize\x01",
            "our reserve police\x01",
            "force...\x02",
        )
    )

    WaitChrThread(0x2E, 1)

    def lambda_11402():
        OP_95(0xFE, 11500, 0, -130000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_11402)
    Sleep(2000)

    def lambda_1141F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_1141F)
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
            "really coming, huh...\x02\x03",
            "#00310FWhat could they be\x01",
            "planning!?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_11552():
        TurnDirection(0x103, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_11552)
    Sleep(50)

    def lambda_11562():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_11562)
    Sleep(50)

    def lambda_11572():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_11572)
    Sleep(50)

    def lambda_11582():
        TurnDirection(0x109, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_11582)
    Sleep(50)

    def lambda_11592():
        TurnDirection(0x105, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_11592)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x103,
        "#11P#00208FRandy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11PRandy, calm down.\x02\x03",
            "#00001FIf if they're Red\x01",
            "Constellation, I don't think\x01",
            "they'd pick a fight here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#11PRight. There's a police\x01",
            "squad protecting the\x01",
            "entrance of this building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#11P#10101FCould they be starting a\x01",
            "conflict at a time like\x01",
            "this?\x02",
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
            "#4S─What was that!?\x07\x00\x02",
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

    def lambda_117E8():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_117E8)
    Sleep(50)

    def lambda_117F8():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_117F8)
    Sleep(50)

    def lambda_11808():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_11808)
    Sleep(50)

    def lambda_11818():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_11818)
    Sleep(50)

    def lambda_11828():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_11828)
    Sleep(50)

    def lambda_11838():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_11838)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x101,
        "#11P#00011FWhat was that just now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00112F#11PG-Grandfather?\x02",
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

    # Function_107_109B8 end

    def Function_108_118CD(): pass

    label("Function_108_118CD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_118EB")
    OP_A1(0x2E, 0x7D0, 0x8, 0x8, 0x9, 0xA, 0x9, 0x8, 0xB, 0xC, 0xB)
    Jump("Function_108_118CD")

    label("loc_118EB")

    Return()

    # Function_108_118CD end

    def Function_109_118EC(): pass

    label("Function_109_118EC")

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
        "#11P#00010FUgh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10106FHow terrible...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#11PThat's absurd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#11P#00301FHow dare they be so\x01",
            "brazen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#11PBut, it's not the case\x01",
            "that their proposals\x01",
            "completely lack any basis.\x02\x03",
            "#00108FI hoped it wouldn't go\x01",
            "like this, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10308FThey just have to hold\x01",
            "out a little longer...\x02",
        )
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_11C58():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_11C58)
    Sleep(50)

    def lambda_11C68():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_11C68)
    Sleep(50)

    def lambda_11C78():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_11C78)
    Sleep(50)

    def lambda_11C88():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_11C88)
    Sleep(50)

    def lambda_11C98():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_11C98)
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
        "#5P#00001FAt a time like this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101F#11PIs that Dudley?\x02",
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
            "#00001FYes, it's Bannings─\x02",
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
            "#00005FChief? What's wro─\x02",
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
            "─I got a call from Sonya.\x02\x03",
            "The radar facilities near\x01",
            "Tangram and Bellguard\x01",
            "were destroyed.\x02\x03",
            "It's anti-air radar to\x01",
            "detect airships invading\x01",
            "the state.\x02",
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
            "#00011F#3SWha!?\x02",
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
            "It's a rumor but it\x01",
            "seems to be the work of\x01",
            "terrorists.\x02\x03",
            "I told Dudley, but I'll\x01",
            "tell you guys too. Be\x01",
            "ready for anything.\x02",
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
        "#6P#00307FIs it my uncle?\x02",
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
        "#11P#00013FN-No, that's not it!\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 60, -1, -1)
    SetChrName("Man's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "Listen up, everyone.\x07\x00\x02",
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

    def lambda_12144():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_12144)
    Sleep(50)

    def lambda_12154():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_12154)
    Sleep(50)

    def lambda_12164():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_12164)
    Sleep(50)

    def lambda_12174():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_12174)
    Sleep(50)

    def lambda_12184():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_12184)
    Sleep(50)

    def lambda_12194():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_12194)
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

    # Function_109_118EC end

    def Function_110_121E6(): pass

    label("Function_110_121E6")

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
        "#11P#00107FAh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10310FThis is... a troublesome\x01",
            "situation.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        (
            "#5P#00203FIt seems we've lost\x01",
            "control of Orchis Tower.\x02\x03",
            "#00201FIt's possibly the doing\x01",
            "of yesterday's hacker.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xE1, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#11P#00010FUgh, we have to go, too.\x02\x03",
            "#00007FAnyway, we've got to go to\x01",
            "35F and ensure the safety\x01",
            "of the dignitaries!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_123FF():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_123FF)
    Sleep(50)

    def lambda_1240F():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1240F)
    Sleep(50)

    def lambda_1241F():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1241F)
    Sleep(50)

    def lambda_1242F():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1242F)
    Sleep(50)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x109,
        "#12P#10107FRoger!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00307FIf the elevator isn't\x01",
            "working, we've no choice but\x01",
            "to use the emergency stairs!\x02",
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

    # Function_110_121E6 end

    def Function_111_124FF(): pass

    label("Function_111_124FF")

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
            "#12P#10101FT-This was open just a\x01",
            "moment ago!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(
        0x101,
        "#6P#00013FTio, can you do it!?\x02",
    )

    CloseMessageWindow()

    def lambda_1268F():

        label("loc_1268F")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_1268F")

    QueueWorkItem2(0x102, 2, lambda_1268F)

    def lambda_126A1():

        label("loc_126A1")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_126A1")

    QueueWorkItem2(0x104, 2, lambda_126A1)

    def lambda_126B3():

        label("loc_126B3")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_126B3")

    QueueWorkItem2(0x109, 2, lambda_126B3)

    def lambda_126C5():

        label("loc_126C5")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_126C5")

    QueueWorkItem2(0x105, 2, lambda_126C5)

    def lambda_126D7():

        label("loc_126D7")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_126D7")

    QueueWorkItem2(0x101, 2, lambda_126D7)

    ChrTalk(
        0x103,
        "#11P#00201F...I'll try.\x02",
    )

    CloseMessageWindow()

    def lambda_12706():
        OP_95(0xFE, -54700, 0, 2200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_12706)
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
            "Tio connected an orbal\x01",
            "cable to the shutter\x01",
            "control panel.\x02",
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
            "#00203F#20W...It's a bit difficult.\x02\x03",
            "#00201FBut I'll do it\x01",
            "somehow...\x02",
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

    def lambda_128A6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_128A6)
    Sleep(50)

    def lambda_128B6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_128B6)
    Sleep(50)

    def lambda_128C6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_128C6)
    Sleep(50)

    def lambda_128D6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_128D6)
    Sleep(50)

    def lambda_128E6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_128E6)
    Sleep(500)

    ChrTalk(
        0x102,
        "#00102FIt opened!\x02",
    )

    CloseMessageWindow()
    OP_79(0xC)

    ChrTalk(
        0x104,
        "#00309FThat's our PeTiote!\x02",
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
            "#00206FNo, it's just that the security\x01",
            "setting's been lowered.\x02\x03",
            "#00208FBut now that this one has been\x01",
            "unlocked, it's possible that the other\x01",
            "doors' security has been reinforced.\x02\x03",
            "#00201FI might not be able to open all of\x01",
            "them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#N#10306FThen we'll need to be\x01",
            "careful.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#12P#00010FUgh... Anyway, let's go!\x02",
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

    # Function_111_124FF end

    def Function_112_12B4C(): pass

    label("Function_112_12B4C")


    def lambda_12B51():
        OP_95(0xFE, -55700, 0, 3300, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_12B51)
    WaitChrThread(0xFE, 1)

    def lambda_12B6F():
        OP_95(0xFE, -55700, 0, 13500, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_12B6F)
    WaitChrThread(0xFE, 1)

    def lambda_12B8D():
        OP_95(0xFE, -52000, 0, 13500, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_12B8D)
    WaitChrThread(0xFE, 1)

    def lambda_12BAB():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_12BAB)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_112_12B4C end

    def Function_113_12BC5(): pass

    label("Function_113_12BC5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12BDF")
    OP_A1(0x103, 0x7D0, 0x4, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_113_12BC5")

    label("loc_12BDF")

    Return()

    # Function_113_12BC5 end

    def Function_114_12BE0(): pass

    label("Function_114_12BE0")

    Sound(145, 2, 100, 0)
    Sleep(2000)
    Sound(143, 0, 70, 0)
    OP_24(0x91)
    Return()

    # Function_114_12BE0 end

    def Function_115_12BF3(): pass

    label("Function_115_12BF3")

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

    def lambda_12DAA():
        OP_96(0xFE, 0xFFFFFC18, 0x0, 0x6978, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x42, 1, lambda_12DAA)
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
            "─For this reason, we all\x01",
            "stand before the Goddess as\x01",
            "equals, burdened with sin.\x02\x03",
            "Deception and cowardice.\x01",
            "These are the names of our\x01",
            "sins.\x02",
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
            "For revenge for the\x01",
            "souls which have already\x01",
            "been sacrificed as well!\x02\x03",
            "For those wounded in the\x01",
            "recent attack as well!\x02\x03",
            "And for a peaceful,\x01",
            "proud future for our\x01",
            "children as well!\x02",
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
        "#5PW-What a load of...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x31,
        "#6PB-But... He's right...\x02",
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

    # Function_115_12BF3 end

    def Function_116_1318E(): pass

    label("Function_116_1318E")

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
            "By the way, Secretary Arios once\x01",
            "also served Crossbell in the role\x01",
            "of police detective.\x02\x03",
            "And in the guild, as you know, he\x01",
            "is known for having resolved a\x01",
            "number of international incidents.\x02\x03",
            "For these reasons, I assure you\x01",
            "that he is the right choice for\x01",
            "this position.\x02",
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
        "#40W...Father... ...Why...\x02",
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

    # Function_116_1318E end

    def Function_117_134AD(): pass

    label("Function_117_134AD")

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
        "#6P#11230FA blue Barrier...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x34, 0xC, 400)
    Sleep(150)

    ChrTalk(
        0x34,
        (
            "#10503F...No need to worry.\x02\x03",
            "#10502FNo harm will come to\x01",
            "you, so relax.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#6P#11221F...!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x34, 500)
    OP_68(163400, 1100, 56750, 500)
    MoveCamera(41, 19, 0, 500)
    SetCameraDistance(16000, 500)

    def lambda_13645():
        OP_96(0xFE, 0x27E48, 0x0, 0xDCB4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_13645)
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
            "#12P#11226F#30WDon't think about me,\x01",
            "think about yourself!\x02\x03",
            "#11227F#30W...Why... ...Why are you\x01",
            "doing this!?\x02\x03",
            "#11232F#30WIf mom saw you like\x01",
            "this... I'm sure she'd\x01",
            "be very sad!\x02",
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
            "#10504F#5P...You're right.\x02\x03",
            "If Saya were here... I'm sure\x01",
            "she would lecture me with a\x01",
            "stern look on her face.\x02",
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
            "#4071V#40W#25A─Shizuku.\x02\x03",
            "#4072V#40W#30AI have a favor to ask of you.\x02",
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

    # Function_117_134AD end

    def Function_118_13918(): pass

    label("Function_118_13918")

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
            "#00108F#6PAccording to chief, there\x01",
            "should be a lot of people\x01",
            "on this floor, but...\x02",
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

    def lambda_13BD3():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_13BD3)
    Sleep(50)

    def lambda_13BE3():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_13BE3)
    Sleep(50)

    def lambda_13BF3():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_13BF3)
    Sleep(50)

    def lambda_13C03():
        OP_93(0xF4, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_13C03)
    Sleep(50)

    def lambda_13C13():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_13C13)
    Sleep(50)

    def lambda_13C23():
        OP_93(0xF5, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_13C23)
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
        "#00011FV-Vice Chief!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00105FWhy are you here?\x02",
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
            "#5PI... Uh... came to ask the secretary\x01",
            "about the declaration of martial law\x01",
            "that was handed down last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5PI was in the middle of doing that\x01",
            "when the restrictions went into\x01",
            "effect, and got stuck on this floor.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13E7E")

    ChrTalk(
        0x10A,
        "#12P#N#00606F...Really, now.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_13ECA")

    label("loc_13E7E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13EB1")

    ChrTalk(
        0x109,
        "#12P#N#10106FI see...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_13ECA")

    label("loc_13EB1")


    ChrTalk(
        0x102,
        "#12P#00106FI see...\x02",
    )

    CloseMessageWindow()

    label("loc_13ECA")


    ChrTalk(
        0x104,
        (
            "#00309FHow should I say it. I\x01",
            "didn't expect this from\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13F6F")

    ChrTalk(
        0x105,
        (
            "#12P#N#10402FHehe, to think you had\x01",
            "the guts to question\x01",
            "your superiors...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13FC7")

    label("loc_13F6F")


    ChrTalk(
        0x103,
        (
            "#12P#N#00204FI wonder if you really\x01",
            "were intending to consult\x01",
            "with your superiors.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13FC7")

    OP_63(0xF, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xF,
        (
            "#5PW-What ever do you\x01",
            "mean!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5PYou guys know that you're\x01",
            "wanted by the State Guard\x01",
            "in the first place, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5PWhat the hell do you\x01",
            "think you're doing!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FWell... It's a long\x01",
            "story.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14114")

    ChrTalk(
        0x103,
        (
            "#12P#N#00205FYou there... Were you in\x01",
            "the IBC Technology\x01",
            "Division?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_1415A")

    label("loc_14114")


    ChrTalk(
        0x102,
        (
            "#12P#00105FYou there... Were you in\x01",
            "the IBC Technology\x01",
            "Division?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1415A")


    ChrTalk(
        0x10,
        (
            "#5PYeah... I'm Researcher\x01",
            "David.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PYesterday, Ms. Mariabell\x01",
            "announced the dissolution of\x01",
            "the Technology Division...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5PMy partner wasn't with me. While\x01",
            "I was still dumbfounded by it, I\x01",
            "was brought to this floor.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14291")

    ChrTalk(
        0x106,
        (
            "#12P#N#10708F...First, I think we\x01",
            "should exchange notes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14358")

    label("loc_14291")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_142F9")

    ChrTalk(
        0x109,
        (
            "#12P#N#10108FUmm, I think it's best\x01",
            "to first confirm each\x01",
            "other's situations.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14358")

    label("loc_142F9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14358")

    ChrTalk(
        0x10A,
        (
            "#12P#N#00603FHmm. It seems best to\x01",
            "first confirm each\x01",
            "other's situations.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14358")

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
        (
            "#5PS-So that's what\x01",
            "happened...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5PEver since the independence\x01",
            "invalidity declaration, things\x01",
            "haven't looked so good, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PW-Why did this have to\x01",
            "happen...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PI feel like I'm having a\x01",
            "bad dream...\x02",
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
            "#5PIt's no wonder their tower\x01",
            "hacking methods have been getting\x01",
            "better for the past couple days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103FSo then... Vice Chief.\x02\x03",
            "#00101FWhere on this floor are\x01",
            "the people on the\x01",
            "President's side?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#5PY-Yes...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5POf course the President and Mariabell,\x01",
            "but also the Secretary of Defense and\x01",
            "the jaegers... None of them are here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#5PAnd... That little girl\x01",
            "that was with all of you\x01",
            "neither.\x02",
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
        (
            "#6P#00108FJust what floor are they\x01",
            "on...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00203F...I think we need to\x01",
            "wait to hear from Chief\x01",
            "Roberts.\x02\x03",
            "#00201FI think he's hurriedly\x01",
            "searching the upper\x01",
            "floors as we speak.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(150)

    ChrTalk(
        0x104,
        (
            "#6P#00303FWhile he's doing that,\x01",
            "let's check the area.\x02\x03",
            "#00301FIt's possible there's\x01",
            "someone around who might\x01",
            "know something.\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14946")

    ChrTalk(
        0x10A,
        (
            "#00600F#12PVice Chief. Can you take\x01",
            "care of this area?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_149E3")

    label("loc_14946")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14997")

    ChrTalk(
        0x109,
        (
            "#10101F#12PVice Chief. Can you take\x01",
            "care of this area?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_149E3")

    label("loc_14997")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_149E3")

    ChrTalk(
        0x105,
        (
            "#10400F#12PVice Chief. Can you take\x01",
            "care of this area?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_149E3")


    def lambda_149E8():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_149E8)
    Sleep(100)

    def lambda_149F8():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_149F8)

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
            "#5PIf you collapse before\x01",
            "learning the truth, you'll\x01",
            "have gained nothing, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000F...Roger. We'll keep\x01",
            "that in mind.\x02",
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

    # Function_118_13918 end

    def Function_119_14BB2(): pass

    label("Function_119_14BB2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_14BD6")
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(1300)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1600)
    Jump("Function_119_14BB2")

    label("loc_14BD6")

    Return()

    # Function_119_14BB2 end

    def Function_120_14BD7(): pass

    label("Function_120_14BD7")

    Sleep(500)

    label("loc_14BDA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_14BFE")
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1600)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(1300)
    Jump("loc_14BDA")

    label("loc_14BFE")

    Return()

    # Function_120_14BD7 end

    def Function_121_14BFF(): pass

    label("Function_121_14BFF")


    def lambda_14C04():
        OP_95(0xFE, -2800, 0, 11100, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14C04)

    def lambda_14C1E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_14C1E)
    WaitChrThread(0xFE, 1)
    OP_68(-2000, 1000, 2850, 3500)
    MoveCamera(37, 21, 0, 3500)
    SetCameraDistance(18000, 3500)

    def lambda_14C58():
        OP_95(0xFE, -2500, 0, 4700, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14C58)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_121_14BFF end

    def Function_122_14C72(): pass

    label("Function_122_14C72")


    def lambda_14C77():
        OP_95(0xFE, -2800, 0, 11000, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14C77)

    def lambda_14C91():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_14C91)
    WaitChrThread(0xFE, 1)

    def lambda_14CA6():
        OP_95(0xFE, -1300, 0, 5300, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14CA6)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_122_14C72 end

    def Function_123_14CC0(): pass

    label("Function_123_14CC0")

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
            "#11226F...KeA... ...Dad...\x01",
            "Why...?\x02",
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

    def lambda_15027():

        label("loc_15027")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_15027")

    QueueWorkItem2(0xC, 2, lambda_15027)
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
            "#12P#00109FThank goodness you're\x01",
            "okay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00202FYou were brought to\x01",
            "Orchis Tower too,\x01",
            "weren't you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FSince you're the daughter of\x01",
            "that old man, I thought you\x01",
            "might be somewhere else.\x02\x03",
            "#00302FAnyway, I'm glad you're\x01",
            "safe.\x02",
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
            "#30WLloyd, Randy, Elie and Tio...\x02\x03",
            "...I see... So that's what you all\x01",
            "look like.\x02",
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
        "#00005FShizuku, it can't be.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00102FYou can... see?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11226F#5PYes. Thanks to KeA.\x02\x03",
            "I think she reconnected\x01",
            "my optic nerve using some\x01",
            "strange power.\x02\x03",
            "#11231FIt's not just light I can\x01",
            "see anymore... I can see\x01",
            "colors and shapes too.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1542F")

    ChrTalk(
        0x109,
        "#10105F#5PA-Amazing...\x02",
    )

    CloseMessageWindow()
    Jump("loc_154A1")

    label("loc_1542F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1546C")

    ChrTalk(
        0x10A,
        "#00605F#5PWhat unbelievable power.\x02",
    )

    CloseMessageWindow()
    Jump("loc_154A1")

    label("loc_1546C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_154A1")

    ChrTalk(
        0x106,
        "#10712F#5PI don't believe it...\x02",
    )

    CloseMessageWindow()

    label("loc_154A1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15508")

    ChrTalk(
        0x105,
        (
            "#10408F#5PCan the power of the\x01",
            "Sept-Terrion of Zero\x01",
            "influence living things?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1558C")

    label("loc_15508")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15554")

    ChrTalk(
        0x106,
        (
            "#10708F#5PThis must be one of\x01",
            "those "miracles"...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1558C")

    label("loc_15554")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1558C")

    ChrTalk(
        0x10A,
        "#00606F#5PA true "miracle", huh...\x02",
    )

    CloseMessageWindow()

    label("loc_1558C")


    ChrTalk(
        0x104,
        (
            "#00309FAh, well isn't that\x01",
            "great!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYeah... Even if she could\x01",
            "only do this, it would be\x01",
            "a remarkable feat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11231F#5PYes... I know that no\x01",
            "matter how much I thank\x01",
            "her, it won't be enough.\x02\x03",
            "#11233F#30W...But... But... Waaah!\x02",
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
            "#11227F#5P#30WThough she smiled, KeA\x01",
            "looked like she was in\x01",
            "great pain!\x02\x03",
            "I know it's my role to do\x01",
            "it... But I couldn't get\x01",
            "through to her!\x02\x03",
            "#11232FEven though she really\x01",
            "doesn't want to cooperate\x01",
            "with Dieter and the others!\x02\x03",
            "Even though she really\x01",
            "wants to go home with you\x01",
            "guys!\x02",
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
            "#11233F#5P#30WWhy is KeA doing all of\x01",
            "this?\x02\x03",
            "And... Why is my dad...\x02\x03",
            "#11234FI.... I...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00208FShizuku...\x02",
    )

    CloseMessageWindow()
    OP_68(163420, 900, 56850, 1200)

    def lambda_1595A():
        OP_95(0xFE, 162800, 0, 57000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1595A)
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
            "#6P#00104FThanks for worrying\x01",
            "about KeA.\x02\x03",
            "#00108FAnd... It must have been\x01",
            "hard on your own.\x02",
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
            "#00003FWe came to get KeA,\x01",
            "Shizuku.\x02\x03",
            "#00001FDo you know where she,\x01",
            "Arios and the others\x01",
            "went?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11233F#5P#30WSorry... I don't know\x01",
            "anything...\x02\x03",
            "I haven't seen KeA since\x01",
            "yesterday...\x02\x03",
            "#11234FUmm... My dad told me to\x01",
            "tell you guys\x01",
            "something...\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15BA3")

    ChrTalk(
        0x10A,
        "#00605F#5PThis is from MacLaine!?\x02",
    )

    CloseMessageWindow()
    Jump("loc_15C13")

    label("loc_15BA3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15BD6")

    ChrTalk(
        0x109,
        "#10105F#5PF-From Arios!?\x02",
    )

    CloseMessageWindow()
    Jump("loc_15C13")

    label("loc_15BD6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15C13")

    ChrTalk(
        0x105,
        (
            "#10405F#5PThe Divine Blade of\x01",
            "Wind...!?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15C13")

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
            "#11226F#11P...It's from father to\x01",
            "Lloyd...\x02\x03",
            "#11221FPlease, open it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FR-Right...\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15EB4")
    Sleep(50)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    label("loc_15EB4")

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
        "#00208F#30WThe ones Guy used...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15FDF")

    AnonymousTalk(
        0x10A,
        (
            "#00606F#30W...There's no mistake.\x01",
            "Those are his tonfas.\x02\x03",
            "#00608FThey disappeared from the\x01",
            "scene of the crime and have\x01",
            "been missing ever since.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_15FDF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16057")

    AnonymousTalk(
        0x105,
        (
            "#10405F#30WThese sword cuts...?\x02\x03",
            "#10401F...This means he killed\x01",
            "Guy Bannings\x01",
            "personally...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_16147")

    label("loc_16057")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_160D0")

    AnonymousTalk(
        0x109,
        (
            "#10105F#30WThese sword cuts...?\x02\x03",
            "#10101FThen that means the one\x01",
            "who offed you brother\x01",
            "is...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_16147")

    label("loc_160D0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16147")

    AnonymousTalk(
        0x106,
        (
            "#10703F#30WThis is... A sword cut.\x02\x03",
            "#10708FThen that means the one\x01",
            "who offed you brother\x01",
            "is...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_16147")

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
            "#11233F#11P#40W...Sorry... I'm really\x01",
            "sorry.\x02\x03",
            "#40WMy father... He did such\x01",
            "a terrible thing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F─Shizuku. You're not\x01",
            "responsible for this.\x02\x03",
            "#00008FIt's not for certain\x01",
            "that Arios killed my\x01",
            "brother.\x02\x03",
            "#00013FIt seems that there's\x01",
            "some unseen, hidden\x01",
            "truth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11227F#11P#30WHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301FWhat do you mean?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1648A")

    ChrTalk(
        0x101,
        (
            "#00008FBased on these sword cuts, it's likely\x01",
            "Arios and my brother engaged in a\x01",
            "violent battle.\x02\x03",
            "#00003FBased on the number of cuts... it would\x01",
            "seem my brother and that Divine Blade\x01",
            "of Wind were rather evenly matched.\x02\x03",
            "#00013F...But...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#6P#00603F─Guy's direct cause of\x01",
            "death was a gunshot in\x01",
            "the back.\x02\x03",
            "#00601FThat's what you're\x01",
            "referring to, Bannings?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FYes.\x02",
    )

    CloseMessageWindow()
    Jump("loc_165BA")

    label("loc_1648A")


    ChrTalk(
        0x101,
        (
            "#00008FBased on these sword cuts, it's likely\x01",
            "Arios and my brother engaged in a\x01",
            "violent battle.\x02\x03",
            "#00003FBased on the number of cuts... it would\x01",
            "seem my brother and that Divine Blade\x01",
            "of Wind were rather evenly matched.\x02\x03",
            "#00013F─But, the direct cause of my brother's\x01",
            "death was a gunshot from behind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_165BA")


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
            "#00000F─Shizuku. I'll read the\x01",
            "letter too.\x02",
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
            "#4073V#40W─To Lloyd. \x01",
            "#40WAllow me to take this opportunity to return\x01",
            "what I should have given you long ago.\x02\x03",
            "#4074V#40W─I have no intention of explaining the contents.\x02\x03",
            "#4075V#40WFurthermore, the magic soldiers that have been\x01",
            "appearing the city are controlled by the white\x01",
            "Aion through that great bell.\x02\x03",
            "#4076V#40WIf you can do something about that white\x01",
            "machine, they will all be silenced.\x07\x00\x02",
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
        "#00008F#30W...............\x02",
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
            "#00303F...The white Aion...\x01",
            "That's the one we saw on\x01",
            "the monitor, right?\x02\x03",
            "#00301FIt wiped Garrelia\x01",
            "Fortress clean off the\x01",
            "face of the map.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00201FHowever, it should no\x01",
            "longer be able to use its\x01",
            "spatial annihilation power.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16A01")

    ChrTalk(
        0x10A,
        (
            "#6P#00608FBut that MacLaine...\x01",
            "What on earth could he\x01",
            "be planning...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16ABB")

    label("loc_16A01")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16A6D")

    ChrTalk(
        0x106,
        (
            "#6P#10708FBut, the Divine Blade of\x01",
            "Wind... What on earth\x01",
            "could he be planning...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16ABB")

    label("loc_16A6D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16ABB")

    ChrTalk(
        0x109,
        (
            "#6P#10108FBut, what on earth could\x01",
            "Arios be planning...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16ABB")

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

    def lambda_16B5D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_16B5D)

    def lambda_16B6A():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_16B6A)

    def lambda_16B77():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_16B77)
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
        "#6P#00202FLloyd...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16C3D")

    ChrTalk(
        0x105,
        (
            "#6P#10402FWow... It's like they\x01",
            "were made just for you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16CCD")

    label("loc_16C3D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16C88")

    ChrTalk(
        0x109,
        (
            "#6P#10100FIt's like they were made\x01",
            "just for you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16CCD")

    label("loc_16C88")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16CCD")

    ChrTalk(
        0x106,
        (
            "#6P#10702FIt seems they were made\x01",
            "just for you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16CCD")


    ChrTalk(
        0x101,
        (
            "#00004FYeah... It's strange how\x01",
            "familiar they feel in my\x01",
            "hands.\x02",
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
            "#00004F─Shizuku. Thank you for\x01",
            "telling us.\x02\x03",
            "#00000FPlease, leave the rest\x01",
            "to us.\x02\x03",
            "Both KeA... and Arios as\x01",
            "well.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_16DD8():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_16DD8)
    Sleep(50)

    def lambda_16DE8():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_16DE8)
    Sleep(50)

    def lambda_16DF8():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_16DF8)

    def lambda_16E05():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_16E05)

    ChrTalk(
        0xC,
        (
            "#11226F#11P#30WOkay...\x02\x03",
            "#11228FI think father has been\x01",
            "worried about this for a\x01",
            "very long time.\x02\x03",
            "And about mother... And me\x01",
            "too.\x02\x03",
            "#11233FHe's overthought various\x01",
            "things... About how he can't\x01",
            "go back to how he was...\x02\x03",
            "#11227F...And now... *sob*...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FIt's all right─ There's\x01",
            "still a chance he could\x01",
            "be a detective again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00104FWe'll definitely bring\x01",
            "your father back to you.\x02\x03",
            "#00100FI swear it on the name\x01",
            "of the Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FWell, if he would make his cute only\x01",
            "daughter cry like this, we'll have to\x01",
            "give him a spanking first, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00204F...Indeed.\x02\x03",
            "#00202FWe'll tie a rope around\x01",
            "his neck and drag him\x01",
            "back here if we have to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11231F#11P#30W...*sob*... Please do!\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_17345")

    ChrTalk(
        0x10A,
        (
            "#6P#00606FSetting aside the talk\x01",
            "about bringing MacLaine\x01",
            "back...\x02\x03",
            "#00601FWhere could the\x01",
            "President's collaborators\x01",
            "have gone off to?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17498")

    label("loc_17345")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_173F1")

    ChrTalk(
        0x105,
        (
            "#6P#10406FSetting aside what we said\x01",
            "about bringing the Divine\x01",
            "Blade of Wind back...\x02\x03",
            "#10401FWhere could the\x01",
            "President's collaborators\x01",
            "have gone?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17498")

    label("loc_173F1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_17498")

    ChrTalk(
        0x106,
        (
            "#6P#10706FSetting aside what we said\x01",
            "about bringing the Divine\x01",
            "Blade of Wind back...\x02\x03",
            "#10708FWhere could the\x01",
            "President's collaborators\x01",
            "have gone?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17498")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_174D5")

    ChrTalk(
        0x109,
        "#6P#10108FKeA's not here either...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1754A")

    label("loc_174D5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_17512")

    ChrTalk(
        0x106,
        "#6P#10708FKeA's not here either...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1754A")

    label("loc_17512")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1754A")

    ChrTalk(
        0x105,
        "#6P#10408FKeA's not here either...\x02",
    )

    CloseMessageWindow()

    label("loc_1754A")


    ChrTalk(
        0x101,
        "#00006F#11PRight...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00108F─He left that message for us.\x01",
            "It's possible that something else\x01",
            "has been left for us in this t──\x02",
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
    SetChrName("Chief's Roberts' Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ah, it's you guys!\x02\x03",
            "I finally got through\x01",
            "the express elevator's\x01",
            "security!\x07\x00\x02",
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
        (
            "#00104FThat's great. In that\x01",
            "case...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Chief's Roberts' Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "But, there's hardly\x01",
            "anyone left on the other\x01",
            "floors.\x02\x03",
            "I'm not getting the\x01",
            "impression that they're\x01",
            "evading my search...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    AnonymousTalk(
        0x103,
        "#00201FIsn't that...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    AnonymousTalk(
        0x104,
        (
            "#00301FWhoa, then where the\x01",
            "heck could KeA and the\x01",
            "others have gone?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Chief's Roberts' Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Just one more thing...\x02\x03",
            "It seems there is\x01",
            ""someone" on the Orchis\x01",
            "Tower roof.\x02\x03",
            "Together with a white\x01",
            "doll.\x07\x00\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1799E")
    SetMessageWindowPos(50, 30, -1, -1)

    AnonymousTalk(
        0x109,
        (
            "#10101F...Can we use the\x01",
            "elevator to get to the\x01",
            "roof?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_17A51")

    label("loc_1799E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_179FA")
    SetMessageWindowPos(50, 30, -1, -1)

    AnonymousTalk(
        0x105,
        (
            "#10401F...Can we use the\x01",
            "elevator to get to the\x01",
            "roof?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_17A51")

    label("loc_179FA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_17A51")
    SetMessageWindowPos(50, 30, -1, -1)

    AnonymousTalk(
        0x10A,
        (
            "#00601F...Can we use the\x01",
            "elevator to get to the\x01",
            "roof?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_17A51")

    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("Chief's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Yeah. I've released the\x01",
            "lock for you, so you can\x01",
            "use it right away.\x02\x03",
            "If you're going, please!\x01",
            "Be careful!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    AnonymousTalk(
        0x103,
        "#00203FRoger that.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00000FThen, if you'll excuse\x01",
            "me.\x02",
        )
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
        (
            "#5P#00108FOuroboros' doctor, or\x01",
            "possibly...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00301FWe don't know... We'll\x01",
            "have to go there to find\x01",
            "out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203FWe should be able to get\x01",
            "there using the nearby\x01",
            "express elevator.\x02\x03",
            "#00201FIf necessary, let's go\x01",
            "to 1F to get ready for\x01",
            "this.\x02",
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

    # Function_123_14CC0 end

    def Function_124_17D48(): pass

    label("Function_124_17D48")

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

    # Function_124_17D48 end

    def Function_125_17DBD(): pass

    label("Function_125_17DBD")

    SetChrPos(0xFE, 156600, 0, 52000, 90)

    def lambda_17DD3():
        OP_95(0xFE, 161000, 0, 52000, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_17DD3)
    WaitChrThread(0xFE, 1)

    def lambda_17DF1():
        OP_95(0xFE, 163300, 0, 55200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_17DF1)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_125_17DBD end

    def Function_126_17E12(): pass

    label("Function_126_17E12")

    SetChrPos(0xFE, 156600, 0, 52000, 90)

    def lambda_17E28():
        OP_95(0xFE, 161000, 0, 52000, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_17E28)
    WaitChrThread(0xFE, 1)

    def lambda_17E46():
        OP_95(0xFE, 162000, 0, 54800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_17E46)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_126_17E12 end

    def Function_127_17E67(): pass

    label("Function_127_17E67")

    SetChrPos(0xFE, 156600, 0, 52000, 90)

    def lambda_17E7D():
        OP_95(0xFE, 161000, 0, 52000, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_17E7D)
    WaitChrThread(0xFE, 1)

    def lambda_17E9B():
        OP_95(0xFE, 162000, 0, 53600, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_17E9B)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_127_17E67 end

    def Function_128_17EBC(): pass

    label("Function_128_17EBC")

    SetChrPos(0xFE, 156600, 0, 52000, 90)

    def lambda_17ED2():
        OP_95(0xFE, 161000, 0, 52000, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_17ED2)
    WaitChrThread(0xFE, 1)

    def lambda_17EF0():
        OP_95(0xFE, 163300, 0, 54000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_17EF0)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_128_17EBC end

    def Function_129_17F11(): pass

    label("Function_129_17F11")

    SetChrPos(0xFE, 154000, 0, 60000, 90)

    def lambda_17F27():
        OP_95(0xFE, 161300, 0, 60000, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_17F27)
    WaitChrThread(0xFE, 1)

    def lambda_17F45():
        OP_95(0xFE, 161700, 0, 58130, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_17F45)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x87, 0x1F4)
    Return()

    # Function_129_17F11 end

    def Function_130_17F66(): pass

    label("Function_130_17F66")

    SetChrPos(0xFE, 154000, 0, 60000, 90)

    def lambda_17F7C():
        OP_95(0xFE, 161300, 0, 60000, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_17F7C)
    WaitChrThread(0xFE, 1)

    def lambda_17F9A():
        OP_95(0xFE, 163100, 0, 58800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_17F9A)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_130_17F66 end

    def Function_131_17FBB(): pass

    label("Function_131_17FBB")


    def lambda_17FC0():
        OP_95(0xFE, 110200, 0, -110500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_17FC0)

    def lambda_17FDA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_17FDA)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_131_17FBB end

    def Function_132_17FEB(): pass

    label("Function_132_17FEB")


    def lambda_17FF0():
        OP_95(0xFE, 110000, 0, -110500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_17FF0)

    def lambda_1800A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1800A)
    WaitChrThread(0xFE, 1)

    def lambda_1801F():
        OP_95(0xFE, 109600, 0, -109200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1801F)
    WaitChrThread(0xFE, 1)

    def lambda_1803D():

        label("loc_1803D")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_1803D")

    QueueWorkItem2(0xFE, 2, lambda_1803D)
    Return()

    # Function_132_17FEB end

    def Function_133_1804B(): pass

    label("Function_133_1804B")


    def lambda_18050():
        OP_95(0xFE, 110000, 0, -110500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_18050)

    def lambda_1806A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1806A)
    WaitChrThread(0xFE, 1)

    def lambda_1807F():
        OP_95(0xFE, 108600, 0, -111500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1807F)
    WaitChrThread(0xFE, 1)

    def lambda_1809D():

        label("loc_1809D")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_1809D")

    QueueWorkItem2(0xFE, 2, lambda_1809D)
    Return()

    # Function_133_1804B end

    def Function_134_180AB(): pass

    label("Function_134_180AB")


    def lambda_180B0():
        OP_95(0xFE, 110000, 0, -110500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_180B0)

    def lambda_180CA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_180CA)
    WaitChrThread(0xFE, 1)

    def lambda_180DF():
        OP_95(0xFE, 109600, 0, -112200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_180DF)
    WaitChrThread(0xFE, 1)

    def lambda_180FD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_180FD)
    Return()

    # Function_134_180AB end

    def Function_135_18106(): pass

    label("Function_135_18106")


    def lambda_1810B():
        OP_95(0xFE, 110000, 0, -110500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1810B)

    def lambda_18125():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_18125)
    WaitChrThread(0xFE, 1)

    def lambda_1813A():
        OP_95(0xFE, 108000, 0, -109800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1813A)
    WaitChrThread(0xFE, 1)

    def lambda_18158():

        label("loc_18158")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_18158")

    QueueWorkItem2(0xFE, 2, lambda_18158)
    Return()

    # Function_135_18106 end

    def Function_136_18166(): pass

    label("Function_136_18166")


    def lambda_1816B():
        OP_95(0xFE, 110000, 0, -110500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1816B)

    def lambda_18185():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_18185)
    WaitChrThread(0xFE, 1)

    def lambda_1819A():
        OP_95(0xFE, 107500, 0, -111300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1819A)
    WaitChrThread(0xFE, 1)

    def lambda_181B8():

        label("loc_181B8")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_181B8")

    QueueWorkItem2(0xFE, 2, lambda_181B8)
    Return()

    # Function_136_18166 end

    def Function_137_181C6(): pass

    label("Function_137_181C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_183D2")
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
        "#00101FAll three are shut down.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201FBecause control of the building\x01",
            "has been stolen, I don't think\x01",
            "we can use the elevators.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FThen, if we can't get\x01",
            "the shutters open, we\x01",
            "can't do anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10107FYes. Let's hurry to the\x01",
            "emergency stairs!\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 109910, 0, -130740, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x1C2, 5)
    EventEnd(0x5)
    Jump("loc_18436")

    label("loc_183D2")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00007FWe can't use the\x01",
            "elevators... Let's hurry\x01",
            "to the emergency stairs!\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 109910, 0, -130740, 270)
    EventEnd(0x4)

    label("loc_18436")

    Return()

    # Function_137_181C6 end

    def Function_138_18437(): pass

    label("Function_138_18437")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1849C")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "This elevator is heading\x01",
            "to other floors and shows\x01",
            "no sign of stopping.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_187B1")

    label("loc_1849C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1873F")
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
            "that first one, huh.\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 3)), scpexpr(EXPR_END)), "loc_1864F")

    ChrTalk(
        0x103,
        (
            "#00200FThe same as the emergency\x01",
            "stairs, it seems this too is\x01",
            "controlled via the orbal net.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, looks that way.\x02\x03",
            "Whatever. When we need\x01",
            "to move, let's use that\x01",
            "first elevator.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18737")

    label("loc_1864F")


    ChrTalk(
        0x103,
        (
            "#00200FBy the way, it seems the\x01",
            "lock mechanism is controlled\x01",
            "via the orbal net.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, I should expect\x01",
            "that much from the Orchis\x01",
            "Tower security system.\x02\x03",
            "Whatever. When we need to\x01",
            "move, let's use that\x01",
            "first elevator.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18737")

    SetScenarioFlags(0x1C2, 2)
    Jump("loc_187B1")

    label("loc_1873F")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The elevator's shutter\x01",
            "is firmly shut.\x02\x03",
            "It seems you can't use\x01",
            "this elevator during the\x01",
            "conference.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_187B1")

    TalkEnd(0xFF)
    Return()

    # Function_138_18437 end

    def Function_139_187B5(): pass

    label("Function_139_187B5")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18A3A")
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The emergency stairs'\x01",
            "shutter is firmly shut.\x07\x00\x02",
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
            "#00100FYes. They said it would be\x01",
            "sealed for the duration of\x01",
            "the conference.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 2)), scpexpr(EXPR_END)), "loc_18963")

    ChrTalk(
        0x103,
        (
            "#00200FThe same as the elevator, it\x01",
            "seems this these too are\x01",
            "controlled via the orbal net...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FPerfect security is\x01",
            "impossible― I remember\x01",
            "hearing that.\x02\x03",
            "We've got to keep that\x01",
            "in the back of our\x01",
            "minds, just in case.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18A32")

    label("loc_18963")


    ChrTalk(
        0x103,
        (
            "#00200FIt seems the shutter\x01",
            "lock is controlled via\x01",
            "the orbal net...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FPerfect security is\x01",
            "impossible― I remember\x01",
            "hearing that.\x02\x03",
            "We've got to keep that\x01",
            "in the back of our\x01",
            "minds, just in case.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18A32")

    SetScenarioFlags(0x1C2, 3)
    Jump("loc_18ABB")

    label("loc_18A3A")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The emergency stairs'\x01",
            "shutter is firmly shut.\x02\x03",
            "It seems you can't\x01",
            "proceed to the next floor\x01",
            "during the conference.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_18ABB")

    TalkEnd(0xFF)
    Return()

    # Function_139_187B5 end

    def Function_140_18ABF(): pass

    label("Function_140_18ABF")

    EventBegin(0x1)

    ChrTalk(
        0x101,
        (
            "#00001FWhoops, the President's in\x01",
            "the innermost room in the\x01",
            "left wing.\x02\x03",
            "Before visiting the\x01",
            "chancellor, let's first pay\x01",
            "a visit to the President.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 4370, 0, -1430, 270)
    EventEnd(0x4)
    Return()

    # Function_140_18ABF end

    SaveToFile()

Try(main)
