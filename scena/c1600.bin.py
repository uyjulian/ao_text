from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1600.bin",                # FileName
        "c1600",                    # MapName
        "c1600",                    # Location
        0x00B2,                     # MapIndex
        "ed7550",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\x01',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 178, 0, 2, 0, 3],
    )

    BuildStringList((
        "c1600",                  # 0
        "Joy",                    # 1
        "Shizuku",                # 2
        "Jona",                   # 3
        "Chief Roberts",          # 4
        "Mayor Dieter",           # 5
        "Ogre Sigmund",           # 6
        "Shirley",                # 7
        "Wald",                   # 8
        "KeA",                    # 9
        "Mariabell",              # 10
        "Arianrhod",              # 11
        "Dr. Novartis",           # 12
        "Campanella The Fool",    # 13
        "Chief Sergei",           # 14
        "Airship",                # 15
        "Airship",                # 16
        "飛空挺影",               # 17
        "飛空挺影",               # 18
        "Imperial Terrorist",     # 19
        "Imperial Terrorist",     # 20
        "Imperial Terrorist",     # 21
        "Imperial Terrorist",     # 22
        "Imperial Terrorist",     # 23
        "Imperial Terrorist",     # 24
        "Imperial Terrorist",     # 25
        "Republican Terrorist",   # 26
        "Republican Terrorist",   # 27
        "Republican Terrorist",   # 28
        "Republican Terrorist",   # 29
        "Republican Terrorist",   # 30
        "Republican Terrorist",   # 31
        "Republican Terrorist",   # 32
        "Aion",                   # 33
        "Aion",                   # 34
        "Aion",                   # 35
        "メルカバ",               # 36
        "映像",                   # 37
        "映像",                   # 38
        "映像",                   # 39
        "映像",                   # 40
        "映像",                   # 41
        "映像",                   # 42
        "SE制御",                 # 43
        "bc1600",                 # 44
    ))

    ATBonus("ATBonus_6D4", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_794", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_798", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_79C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7A0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7A4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7A8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7AC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7B0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_774", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_778", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_77C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_780", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_784", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_788", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_78C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_790", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_7B4", 0x0042, 255, 6, 45, 3, 3, 30, 0, "bc1600", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_794", "MonsterBattlePostion_774", "ed7554", "ed7554", "ATBonus_6D4"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch00000.itc",                   # 00
        "chr/ch00000.itc",                   # 01
        "chr/ch27600.itc",                   # 02
        "apl/ch51731.itc",                   # 03
        "chr/ch05410.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch00000.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "chr/ch00000.itc",                   # 10
        "chr/ch00000.itc",                   # 11
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

    DeclNpc(4294967177, 0,       22069,   0,    389,  0x0, 0,   2,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(8680,    0,       4294950817, 135,  389,  0x0, 0,   4,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(32200,   4294962896, 4294939446, 75,   453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(28399,   4294962896, 4294939546, 45,   453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
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
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
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
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 34,  22.0,                  -23.0,                 -5.400000095367432,    625.0,                 [0.14142131805419922,  0.07071070373058319,   -0.0,                  0.0,                   -0.14142140746116638,  0.07071065902709961,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -6.363961219787598,    0.07070967555046082,   1.0800000429153442,    1.0])
    DeclEvent(0x0000, 0, 62,  0.0,                   -22.0,                 -1.0,                  156.25,                [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  4.400000095367432,     0.20000000298023224,   1.0])

    DeclActor(0,       0,       0,       1500,    0,       1500,    0,       0x007C, 0,  93, 0x0000)

    ChipFrameInfo(2420, 0)                                       # 0

    ScpFunction((
        "Function_0_974",          # 00, 0
        "Function_1_A24",          # 01, 1
        "Function_2_B80",          # 02, 2
        "Function_3_D5F",          # 03, 3
        "Function_4_1334",         # 04, 4
        "Function_5_15C3",         # 05, 5
        "Function_6_16D2",         # 06, 6
        "Function_7_1923",         # 07, 7
        "Function_8_1FF5",         # 08, 8
        "Function_9_233F",         # 09, 9
        "Function_10_2FD9",        # 0A, 10
        "Function_11_302E",        # 0B, 11
        "Function_12_3083",        # 0C, 12
        "Function_13_30D8",        # 0D, 13
        "Function_14_3148",        # 0E, 14
        "Function_15_319D",        # 0F, 15
        "Function_16_31F2",        # 10, 16
        "Function_17_3222",        # 11, 17
        "Function_18_328A",        # 12, 18
        "Function_19_32C7",        # 13, 19
        "Function_20_330B",        # 14, 20
        "Function_21_334F",        # 15, 21
        "Function_22_3393",        # 16, 22
        "Function_23_33D7",        # 17, 23
        "Function_24_341B",        # 18, 24
        "Function_25_345F",        # 19, 25
        "Function_26_34A3",        # 1A, 26
        "Function_27_3A2A",        # 1B, 27
        "Function_28_3A8A",        # 1C, 28
        "Function_29_3AEA",        # 1D, 29
        "Function_30_3C0D",        # 1E, 30
        "Function_31_3D19",        # 1F, 31
        "Function_32_3DE8",        # 20, 32
        "Function_33_3EB7",        # 21, 33
        "Function_34_42B5",        # 22, 34
        "Function_35_5A02",        # 23, 35
        "Function_36_5AFA",        # 24, 36
        "Function_37_5B19",        # 25, 37
        "Function_38_5B38",        # 26, 38
        "Function_39_5B97",        # 27, 39
        "Function_40_5BB6",        # 28, 40
        "Function_41_5BFE",        # 29, 41
        "Function_42_5C4B",        # 2A, 42
        "Function_43_71BE",        # 2B, 43
        "Function_44_74DB",        # 2C, 44
        "Function_45_758F",        # 2D, 45
        "Function_46_75DF",        # 2E, 46
        "Function_47_7635",        # 2F, 47
        "Function_48_76EF",        # 30, 48
        "Function_49_7798",        # 31, 49
        "Function_50_7883",        # 32, 50
        "Function_51_78C3",        # 33, 51
        "Function_52_7946",        # 34, 52
        "Function_53_822E",        # 35, 53
        "Function_54_8A4B",        # 36, 54
        "Function_55_8B62",        # 37, 55
        "Function_56_9400",        # 38, 56
        "Function_57_9574",        # 39, 57
        "Function_58_95B3",        # 3A, 58
        "Function_59_9A4B",        # 3B, 59
        "Function_60_9A7A",        # 3C, 60
        "Function_61_9B17",        # 3D, 61
        "Function_62_9B2E",        # 3E, 62
        "Function_63_C860",        # 3F, 63
        "Function_64_C88E",        # 40, 64
        "Function_65_C8EF",        # 41, 65
        "Function_66_C950",        # 42, 66
        "Function_67_C975",        # 43, 67
        "Function_68_D48C",        # 44, 68
        "Function_69_D49F",        # 45, 69
        "Function_70_D4D4",        # 46, 70
        "Function_71_11A37",       # 47, 71
        "Function_72_11A5C",       # 48, 72
        "Function_73_11AC3",       # 49, 73
        "Function_74_11B2A",       # 4A, 74
        "Function_75_11B91",       # 4B, 75
        "Function_76_11BF8",       # 4C, 76
        "Function_77_11C5F",       # 4D, 77
        "Function_78_11CA1",       # 4E, 78
        "Function_79_11CC3",       # 4F, 79
        "Function_80_11CDF",       # 50, 80
        "Function_81_11CFB",       # 51, 81
        "Function_82_11D17",       # 52, 82
        "Function_83_11D33",       # 53, 83
        "Function_84_11D4F",       # 54, 84
        "Function_85_11D73",       # 55, 85
        "Function_86_11D7E",       # 56, 86
        "Function_87_11D89",       # 57, 87
        "Function_88_11D94",       # 58, 88
        "Function_89_11D9F",       # 59, 89
        "Function_90_11DAA",       # 5A, 90
        "Function_91_11DB5",       # 5B, 91
        "Function_92_11E30",       # 5C, 92
        "Function_93_11E48",       # 5D, 93
        "Function_94_11EA5",       # 5E, 94
    ))


    def Function_0_974(): pass

    label("Function_0_974")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_9AC"),
        (1, "loc_9B8"),
        (2, "loc_9C4"),
        (3, "loc_9D0"),
        (4, "loc_9DC"),
        (5, "loc_9E8"),
        (6, "loc_9F4"),
        (SWITCH_DEFAULT, "loc_A00"),
    )


    label("loc_9AC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_A0C")

    label("loc_9B8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_A0C")

    label("loc_9C4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_A0C")

    label("loc_9D0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_A0C")

    label("loc_9DC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_A0C")

    label("loc_9E8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_A0C")

    label("loc_9F4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A0C")

    label("loc_A00")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A0C")

    label("loc_A0C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A23")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A0C")

    label("loc_A23")

    Return()

    # Function_0_974 end

    def Function_1_A24(): pass

    label("Function_1_A24")

    SetMapObjFlags(0x5, 0x2000000)
    SetMapObjFlags(0x14, 0x2000000)
    SetMapObjFlags(0x9, 0x2000000)
    SetMapObjFlags(0xA, 0x2000000)
    SetMapObjFlags(0x13, 0x2000000)
    SetMapObjFlags(0x15, 0x2000000)
    SetMapObjFlags(0x17, 0x2000000)
    SetMapObjFlags(0x6, 0x2000000)
    SetMapObjFlags(0x7, 0x2000000)
    SetMapObjFlags(0xB, 0x2000000)
    SetMapObjFlags(0xC, 0x2000000)
    SetMapObjFlags(0x16, 0x2000000)
    SetMapObjFlags(0xD, 0x2000000)
    SetMapObjFlags(0xE, 0x2000000)
    SetMapObjFlags(0xF, 0x2000000)
    SetMapObjFlags(0x10, 0x2000000)
    SetMapObjFlags(0x11, 0x2000000)
    SetMapObjFlags(0x12, 0x2000000)
    SetMapObjFlags(0x18, 0x2000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_AB7")
    ClearMapObjFlags(0x6, 0x2000000)
    ClearMapObjFlags(0x7, 0x2000000)
    ClearMapObjFlags(0xB, 0x2000000)
    ClearMapObjFlags(0xC, 0x2000000)

    label("loc_AB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_AC6")
    ClearMapObjFlags(0x5, 0x2000000)

    label("loc_AC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_AE1")
    ClearMapObjFlags(0x5, 0x2000000)
    ClearMapObjFlags(0x9, 0x2000000)
    ClearMapObjFlags(0xA, 0x2000000)

    label("loc_AE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 0)), scpexpr(EXPR_END)), "loc_AF0")
    ClearMapObjFlags(0x5, 0x2000000)

    label("loc_AF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 1)), scpexpr(EXPR_END)), "loc_B0B")
    ClearMapObjFlags(0x5, 0x2000000)
    ClearMapObjFlags(0x9, 0x2000000)
    ClearMapObjFlags(0x13, 0x2000000)

    label("loc_B0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B2B")
    ClearMapObjFlags(0x5, 0x2000000)
    ClearMapObjFlags(0x14, 0x2000000)
    ClearMapObjFlags(0x18, 0x2000000)

    label("loc_B2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 3)), scpexpr(EXPR_END)), "loc_B70")
    ClearMapObjFlags(0xD, 0x2000000)
    ClearMapObjFlags(0xE, 0x2000000)
    ClearMapObjFlags(0xF, 0x2000000)
    ClearMapObjFlags(0x10, 0x2000000)
    ClearMapObjFlags(0x11, 0x2000000)
    ClearMapObjFlags(0x12, 0x2000000)
    ClearMapObjFlags(0x15, 0x2000000)
    ClearMapObjFlags(0x17, 0x2000000)
    ClearMapObjFlags(0x16, 0x2000000)
    SetMapObjFlags(0x18, 0x2000000)

    label("loc_B70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 4)), scpexpr(EXPR_END)), "loc_B7F")
    ClearMapObjFlags(0x16, 0x2000000)

    label("loc_B7F")

    Return()

    # Function_1_A24 end

    def Function_2_B80(): pass

    label("Function_2_B80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BC5")
    SetChrChipByIndex(0xC, 0x3)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 0, 0, 0, 180)
    OP_8E(0xC, "President Dieter")

    label("loc_BC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_BDD")
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    Jump("loc_C43")

    label("loc_BDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_BF5")
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    Jump("loc_C43")

    label("loc_BF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_C03")
    Jump("loc_C43")

    label("loc_C03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_C11")
    Jump("loc_C43")

    label("loc_C11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_C29")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    Jump("loc_C43")

    label("loc_C29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_C43")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    OP_93(0x8, 0x13B, 0x0)

    label("loc_C43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_C57")
    ClearScenarioFlags(0x22, 0)
    Event(0, 8)
    Jump("loc_D48")

    label("loc_C57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_C6B")
    ClearScenarioFlags(0x22, 1)
    Event(0, 9)
    Jump("loc_D48")

    label("loc_C6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_C7F")
    ClearScenarioFlags(0x22, 2)
    Event(0, 26)
    Jump("loc_D48")

    label("loc_C7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_C96")
    ClearScenarioFlags(0x22, 3)
    SetScenarioFlags(0x0, 5)
    Event(0, 42)
    Jump("loc_D48")

    label("loc_C96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_CAA")
    ClearScenarioFlags(0x22, 4)
    Event(0, 52)
    Jump("loc_D48")

    label("loc_CAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_CBE")
    ClearScenarioFlags(0x22, 5)
    Event(0, 53)
    Jump("loc_D48")

    label("loc_CBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_CD2")
    ClearScenarioFlags(0x22, 6)
    Event(0, 54)
    Jump("loc_D48")

    label("loc_CD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 7)), scpexpr(EXPR_END)), "loc_CE6")
    ClearScenarioFlags(0x22, 7)
    Event(0, 55)
    Jump("loc_D48")

    label("loc_CE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 0)), scpexpr(EXPR_END)), "loc_CFA")
    ClearScenarioFlags(0x23, 0)
    Event(0, 56)
    Jump("loc_D48")

    label("loc_CFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 1)), scpexpr(EXPR_END)), "loc_D0E")
    ClearScenarioFlags(0x23, 1)
    Event(0, 58)
    Jump("loc_D48")

    label("loc_D0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 2)), scpexpr(EXPR_END)), "loc_D22")
    ClearScenarioFlags(0x23, 2)
    Event(0, 67)
    Jump("loc_D48")

    label("loc_D22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 3)), scpexpr(EXPR_END)), "loc_D39")
    ClearScenarioFlags(0x23, 3)
    SetScenarioFlags(0x0, 4)
    Event(0, 70)
    Jump("loc_D48")

    label("loc_D39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 4)), scpexpr(EXPR_END)), "loc_D48")
    ClearScenarioFlags(0x23, 4)
    Event(0, 94)

    label("loc_D48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D5E")
    SetMapFlags(0x10000000)
    Event(0, 33)

    label("loc_D5E")

    Return()

    # Function_2_B80 end

    def Function_3_D5F(): pass

    label("Function_3_D5F")

    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF032877), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_F0(0x1, 0x4B0)
    OP_F3(100000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D9C")
    SetMapObjFrame(0xFF, "CS00", 0x1, 0x2)
    SetMapObjFrame(0xFF, "CS01", 0x1, 0x2)
    Jump("loc_DA8")

    label("loc_D9C")

    SetMapObjFrame(0xFF, "CS02", 0x1, 0x2)

    label("loc_DA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_DBF")
    Sound(132, 1, 50, 0)
    ClearScenarioFlags(0x0, 5)
    Jump("loc_DDE")

    label("loc_DBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DD8")
    Sound(132, 1, 50, 0)
    Jump("loc_DDE")

    label("loc_DD8")

    Sound(132, 1, 100, 0)

    label("loc_DDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_DF8")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 4)
    Jump("loc_E26")

    label("loc_DF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E14")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E26")

    label("loc_E14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_E26")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E26")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E3E")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_E3E")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E56")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_E56")

    LoadEffect(0x10, "event\\eva00_00.eff")
    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EB8")
    PlayEffect(0x10, 0x9, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x0, 0x1)

    label("loc_EB8")

    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x11, 0x4)
    SetMapObjFlags(0x12, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1012")
    SetMapObjFrame(0xFF, "sky00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kumo01a", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back00_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back01_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back02_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "a_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "b_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "c_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "d_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "02_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "03_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "futa02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "futa03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "window01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "futa00", 0x2, "close")
    SetMapObjFrame(0xFF, "futa01", 0x2, "open")
    OP_70(0x1, 0x12D)
    OP_70(0x2, 0x12D)
    OP_70(0x3, 0x12D)
    OP_70(0x4, 0x12D)
    Jump("loc_1136")

    label("loc_1012")

    SetMapObjFrame(0xFF, "sky00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kumo01a", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "back01_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "back02_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "a_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "b_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "c_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "d_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "02_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "03_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "futa02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "futa03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "window01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "futa00", 0x2, "close")
    SetMapObjFrame(0xFF, "futa01", 0x2, "close")
    OP_70(0x1, 0x0)
    OP_70(0x2, 0x0)
    OP_70(0x3, 0x0)
    OP_70(0x4, 0x0)

    label("loc_1136")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1159")
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x8, 0x20)
    OP_70(0x8, 0x2)
    Jump("loc_115F")

    label("loc_1159")

    SetMapObjFlags(0x8, 0x4)

    label("loc_115F")

    SetMapObjFrame(0xFF, "last", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1235")
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x28, 0x8000)
    OP_78(0x5, 0x28)
    SetChrPos(0x28, 0, 0, 6500, 180)
    OP_D5(0x28, 0x0, 0x2BF20, 0x0, 0x0)
    SetMapObjFlags(0x5, 0x1000)
    OP_74(0x5, 0x1E)
    OP_70(0x5, 0x42E)
    SetChrFlags(0x28, 0x1)
    OP_52(0x28, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x29, 0x80)
    SetChrFlags(0x29, 0x8000)
    OP_78(0x14, 0x29)
    SetChrPos(0x29, 0, 0, 6500, 180)
    OP_D5(0x29, 0x0, 0x2BF20, 0x0, 0x0)
    SetMapObjFlags(0x14, 0x1000)
    SetMapObjFlags(0x14, 0x4)
    OP_74(0x14, 0x1E)
    OP_70(0x14, 0x42E)
    SetChrFlags(0x29, 0x1)
    OP_52(0x29, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1235")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12CF")
    LoadEffect(0x9, "map/mprain01.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    SetMapObjFrame(0xFF, "sky00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01a", 0x0, 0x1)

    label("loc_12CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1333")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x12C, 0x384, 0x0)
    SetMapObjFrame(0xFF, "sky00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01a", 0x0, 0x1)

    label("loc_1333")

    Return()

    # Function_3_D5F end

    def Function_4_1334(): pass

    label("Function_4_1334")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1345")
    Jump("loc_15BF")

    label("loc_1345")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_150F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1471")

    ChrTalk(
        0xFE,
        (
            "*sigh*... I knew coming here\x01",
            "multiple times was a good idea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was thinking of reading a book\x01",
            "here today, but this scenery is\x01",
            "just so overwhelming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you like, you\x01",
            "guys can read this.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x2F7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x2F7, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x189, 1)
    Jump("loc_150A")

    label("loc_1471")


    ChrTalk(
        0xFE,
        (
            "*sigh*... I knew coming here\x01",
            "multiple times was a good idea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I look at this scenery,\x01",
            "even the fear I felt from\x01",
            "that raid attack subsides.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_150A")

    Jump("loc_15BF")

    label("loc_150F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_15BF")

    ChrTalk(
        0xFE,
        (
            "You can't see it from here,\x01",
            "but over in that direction,\x01",
            "the CGF is fighting, even now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even though the scenery is this\x01",
            "beautiful... It's a really sad thing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15BF")

    TalkEnd(0xFE)
    Return()

    # Function_4_1334 end

    def Function_5_15C3(): pass

    label("Function_5_15C3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_1653")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15E5")
    TalkEnd(0xFE)
    Call(0, 7)
    Return()

    label("loc_15E5")


    ChrTalk(
        0x9,
        (
            "#11223F...I'm sure you all\x01",
            "will be all right.\x02\x03",
            "#11222FSo please...\x01",
            "Save my precious\x01",
            "friend, KeA...!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16CE")

    label("loc_1653")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_16CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_166E")
    Call(0, 6)
    Jump("loc_16CE")

    label("loc_166E")


    ChrTalk(
        0x9,
        (
            "#11228FEveryone, please...\x01",
            "Take care of my\x01",
            "father and KeA.\x02\x03",
            "#11223FI will be waiting here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16CE")

    TalkEnd(0xFE)
    Return()

    # Function_5_15C3 end

    def Function_6_16D2(): pass

    label("Function_6_16D2")

    OP_93(0x9, 0x87, 0x0)

    ChrTalk(
        0x9,
        "#11221FFather, KeA...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FShizuku... So this\x01",
            "is where you were.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x0, 500)

    ChrTalk(
        0x9,
        (
            "#11220FEveryone... Yes,\x01",
            "I was looking at\x01",
            "that "huge tree".\x02\x03",
            "#11230FAre father and KeA\x01",
            "really in there...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203F...Yes. There is no mistake.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FWe still don't know where in the\x01",
            ""huge tree" they're, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11223FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...Shizuku, please wait for us.\x02\x03",
            "#00001FWe'll definitely bring back\x01",
            "Mr. Arios and KeA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00302FYeah, so don't worry, 'k?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11223F...Alright.\x02\x03",
            "#11221FEveryone, please...\x01",
            "Take care of my\x01",
            "father and KeA.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x87, 0x0)
    SetScenarioFlags(0x1AF, 2)
    Return()

    # Function_6_16D2 end

    def Function_7_1923(): pass

    label("Function_7_1923")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0x9, 0xFF)
    OP_68(7690, 1100, -15570, 0)
    MoveCamera(110, 28, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(9990, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 7530, 0, -15000, 135)
    SetChrPos(0x1, 9360, 0, -14520, 180)
    SetChrPos(0x2, 6860, 0, -16500, 90)
    SetChrPos(0x3, 8570, 0, -13930, 180)
    SetChrPos(0x4, 5900, 0, -15300, 110)
    SetChrPos(0x5, 7050, 0, -13540, 155)
    OP_93(0x9, 0x13B, 0x0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and the others\x01",
            "defeated Arios...\x02\x03",
            "And then, they explained to\x01",
            "Shizuku that Guy's murderer\x01",
            "wasn't her father.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x9,
        "#11225F...So that's what happened...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00004F...Yeah.\x02\x03",
            "#00000FMr. Arios will be back\x01",
            "with you soon, Shizuku...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11233F...Ooh... *sob*...\x02",
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
        0x9,
        (
            "#11234FOoh... Thank goodness.\x02\x03",
            "#11233FMy father didn't kill his\x01",
            "precious friend...\x01",
            "Mr. Lloyd's older brother...\x02\x03",
            "#11234FIf it's really true, my\x01",
            "father might be\x01",
            "able to turn back...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00108FShizuku...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00002FHa ha... I said it,\x01",
            "right? It's not the case\x01",
            "that he can't go back.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D04")

    ChrTalk(
        0x10A,
        (
            "#6P#00602F...Just you wait. \x01",
            "I promise you we'll bring\x01",
            "MacLaine back later.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DB4")

    label("loc_1D04")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D5B")

    ChrTalk(
        0x109,
        (
            "#6P#10102FJust wait, okay?\x01",
            "We'll bring Mr. Arios\x01",
            "back later.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DB4")

    label("loc_1D5B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1DB4")

    ChrTalk(
        0x105,
        (
            "#6P#10402FWe will bring Mr.\x01",
            "Arios back later.\x01",
            "Hu hu, I promise you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DB4")


    ChrTalk(
        0x9,
        "#11222F*cry*... Okay!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00202F...All that's left is\x01",
            "to bring back KeA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00309FYeah. To make\x01",
            "Shizuku smile, too!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E9D")

    ChrTalk(
        0x105,
        (
            "#6P#10409FHu hu. Well we have to do it now,\x01",
            "if that's how it's gonna be.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F4B")

    label("loc_1E9D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1EFA")

    ChrTalk(
        0x109,
        (
            "#6P#10109FThat's something we must\x01",
            "accomplish, no matter the cost!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F4B")

    label("loc_1EFA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F4B")

    ChrTalk(
        0x106,
        (
            "#6P#10709FIf that's how\x01",
            "it's going to be,\x01",
            "we have to do it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F4B")


    ChrTalk(
        0x9,
        (
            "#11223F...If you all won against my dad,\x01",
            "I'm sure it'll be all right.\x02\x03",
            "#11227FSo please...\x01",
            "Save my precious\x01",
            "friend KeA...!\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_93(0x9, 0x87, 0x0)
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x1AF, 1)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_7_1923 end

    def Function_8_1FF5(): pass

    label("Function_8_1FF5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05600.itc", 0x1E)
    OP_68(23800, -43600, 6100, 0)
    MoveCamera(305, 17, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(12000, 0)
    SetChrPos(0x101, 23800, -44600, 6100, 90)
    SetChrPos(0x102, 23800, -44600, 7200, 90)
    SetChrPos(0x109, 23000, -44600, 7000, 90)
    SetChrPos(0x103, 23000, -44600, 5900, 90)
    SetChrPos(0x104, 22200, -44600, 5700, 90)
    SetChrPos(0x105, 23600, -44600, 5100, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 20800, -44600, 7500, 90)
    OP_52(0x101, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x102, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x102, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x102, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x109, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x109, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x109, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x105, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x105, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x105, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1500, 0)
    MoveCamera(305, 23, 0, 6000)
    OP_6E(1100, 6000)
    SetCameraDistance(82000, 6000)
    OP_6F(0x79)
    Sleep(500)
    Fade(1000)
    OP_68(0, -53600, -25000, 0)
    MoveCamera(315, -15, 15, 0)
    OP_6E(1100, 0)
    SetCameraDistance(80000, 0)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x105, 0x8)
    SetChrFlags(0xC, 0x8)
    OP_68(0, -73600, -75000, 11000)
    MoveCamera(215, 30, 15, 11000)
    SetCameraDistance(180000, 11000)
    OP_6F(0x79)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_52(0x101, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x102, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x102, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x102, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x109, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x109, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x109, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x105, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x105, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x105, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 1)
    NewScene("c1530", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_8_1FF5 end

    def Function_9_233F(): pass

    label("Function_9_233F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05600.itc", 0x1E)
    LoadChrToIndex("apl/ch51259.itc", 0x1F)
    SoundLoad(803)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis416.itp")
    SetChrPos(0x101, -19000, -6000, 0, 270)
    SetChrPos(0x102, -19000, -6000, 0, 270)
    SetChrPos(0x103, -19000, -6000, 0, 270)
    SetChrPos(0x104, -19000, -6000, 0, 270)
    SetChrPos(0x109, -19000, -6000, 0, 270)
    SetChrPos(0x105, -19000, -6000, 0, 270)
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
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -19000, -6000, 0, 270)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-20000, -5000, 0, 0)
    MoveCamera(40, 23, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    OP_68(-23000, -5000, 0, 6000)
    SetCameraDistance(16000, 6000)
    BeginChrThread(0xC, 3, 0, 16)
    Sleep(700)
    BeginChrThread(0x101, 3, 0, 10)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 11)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 15)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 14)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 12)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 13)
    WaitChrThread(0x109, 3)

    ChrTalk(
        0x109,
        "#11P#10109FWaaah...!!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x105, 3)

    ChrTalk(
        0x105,
        (
            "#11P#10302FThis is...\x01",
            "Really incredible.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x104, 3)
    OP_6F(0x79)
    OP_68(0, 0, 0, 9000)
    MoveCamera(225, 13, 0, 9000)
    OP_6E(900, 9000)
    SetCameraDistance(130000, 9000)
    BeginChrThread(0xC, 3, 0, 17)
    Sleep(700)
    BeginChrThread(0x101, 3, 0, 17)
    Sleep(900)
    BeginChrThread(0x109, 3, 0, 17)
    Sleep(100)
    BeginChrThread(0x102, 3, 0, 17)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 17)
    OP_6F(0x79)
    EndChrThread(0xC, 0xFF)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    SetChrPos(0x101, -19700, -4400, -20300, 180)
    SetChrPos(0x102, -20300, -4400, -19700, 180)
    SetChrPos(0x103, -20000, -4400, -20000, 180)
    SetChrPos(0x104, -19700, -4400, -20300, 180)
    SetChrPos(0x109, -20300, -4400, -19700, 180)
    SetChrPos(0x105, -20000, -4400, -20000, 180)
    SetChrPos(0xC, -20000, -4400, -20000, 180)
    BeginChrThread(0x101, 0, 0, 18)
    Sleep(1000)
    Fade(1000)
    OP_68(-29000, -3900, -29000, 0)
    MoveCamera(225, 17, 0, 0)
    OP_6E(1100, 0)
    SetCameraDistance(16500, 0)
    OP_0D()
    OP_68(-24400, -3900, -38800, 6000)
    MoveCamera(205, 19, 0, 6000)
    SetCameraDistance(23500, 6000)
    OP_6F(0x79)
    WaitChrThread(0x109, 3)

    ChrTalk(
        0x101,
        (
            "#00004F#11PHa ha... \x01",
            "I'm speechless...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F#11PYes, you're right...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x103, 3)

    ChrTalk(
        0x103,
        (
            "#00202F#11P...From here, the city below\x01",
            "looks like a miniature...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F#11PI bet the view's\x01",
            "amazing at night, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-28800, -3300, -31300, 0)
    MoveCamera(205, 21, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(15500, 0)
    OP_0D()

    ChrTalk(
        0xC,
        (
            "#12P#02809FHa ha, well you can think\x01",
            "of this place as a viewing\x01",
            "platform open to the public.\x02\x03",
            "#02800FIt'd be too much of a waste if it was\x01",
            "reserved only for government officials.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_288D():
        TurnDirection(0x101, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_288D)
    Sleep(50)

    def lambda_289D():
        TurnDirection(0x102, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_289D)
    Sleep(50)

    def lambda_28AD():
        TurnDirection(0x103, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_28AD)
    Sleep(50)

    def lambda_28BD():
        TurnDirection(0x104, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_28BD)
    Sleep(50)

    def lambda_28CD():
        TurnDirection(0x105, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_28CD)
    Sleep(50)

    def lambda_28DD():
        TurnDirection(0x109, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_28DD)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    def lambda_2902():

        label("loc_2902")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_2902")

    QueueWorkItem2(0x101, 2, lambda_2902)

    def lambda_2914():

        label("loc_2914")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_2914")

    QueueWorkItem2(0x102, 2, lambda_2914)

    def lambda_2926():

        label("loc_2926")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_2926")

    QueueWorkItem2(0x103, 2, lambda_2926)

    def lambda_2938():

        label("loc_2938")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_2938")

    QueueWorkItem2(0x109, 2, lambda_2938)

    def lambda_294A():

        label("loc_294A")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_294A")

    QueueWorkItem2(0x105, 2, lambda_294A)

    def lambda_295C():

        label("loc_295C")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_295C")

    QueueWorkItem2(0x104, 2, lambda_295C)

    ChrTalk(
        0x101,
        "#00002F#5PYeah, that's a good idea.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F#5P*giggle*, I'd like to\x01",
            "take KeA here too.\x02",
        )
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(500)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xC,
        "#12P#02805FOh, excuse me.\x02",
    )

    CloseMessageWindow()
    OP_93(0xC, 0x5A, 0x1F4)
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x2)
    SetChrFlags(0xC, 0x10)
    OP_0D()
    Sound(804, 0, 100, 0)
    OP_24(0x323)
    Sleep(300)
    SetChrSubChip(0xC, 0x1)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "#11P#02801FYeah, it's me.\x02\x03",
            "#02803F...I see. Understood. \x01",
            "I'll head there right away.\x02",
        )
    )

    CloseMessageWindow()
    Sound(804, 0, 100, 0)
    SetChrSubChip(0xC, 0x0)
    Sleep(300)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x2)
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "#12P#02800FIt seems the heads of state\x01",
            "have arrived at the tower.\x02\x03",
            "I am terribly sorry, but I'll\x01",
            "have to take my leave here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#5PIs that so... \x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204F#5PThank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309F#5PMan, that was a blast.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10102F#5PYou gave us a great experience!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12P#02804FAnd I thank all of you as well.\x01",
            "That was a great change of pace.\x02\x03",
            "#02800FWell then, see you later, everyone.\x01",
            "Please, do your best with the security.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#5PYes, please leave that to us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#5PWell, you gave me that recommendation.\x01",
            "It's the least I could do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#5P──May the Goddess protect you. \x01",
            "I pray for the success of the conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#12P#02809FHa ha, I'm praying too.\x02",
    )

    CloseMessageWindow()
    OP_92(0xC, 0xFFFFADF8, 0xFFFFADF8, 0x1F4)
    OP_68(-25800, -3300, -28300, 5000)
    SetCameraDistance(17500, 5000)

    def lambda_2DB5():
        OP_95(0xFE, -21000, -4400, -21000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2DB5)
    WaitChrThread(0xC, 1)
    OP_6F(0x79)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    SetChrFlags(0xC, 0x80)
    Fade(500)
    OP_68(-28350, -3300, -32000, 0)
    MoveCamera(205, 21, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(15500, 0)
    OP_0D()
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00000F#5PWe should be getting \x01",
            "back to Mr. Dudley.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2E69():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2E69)
    Sleep(50)

    def lambda_2E79():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2E79)
    Sleep(50)

    def lambda_2E89():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2E89)
    Sleep(50)

    def lambda_2E99():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2E99)
    Sleep(50)

    def lambda_2EA9():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2EA9)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x103,
        (
            "#12P#00202FIf I remember correctly, he is in\x01",
            "the 34F security planning room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FI really hope\x01",
            "nothing happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10108FI hope so, too...\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(15000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    StopSound(132, 1000, 100)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(2000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    OP_24(0x323)
    SetScenarioFlags(0x22, 1)
    NewScene("c1540", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_9_233F end

    def Function_10_2FD9(): pass

    label("Function_10_2FD9")


    def lambda_2FDE():
        OP_95(0xFE, -20700, -6000, 0, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2FDE)

    def lambda_2FF8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2FF8)
    WaitChrThread(0xFE, 1)

    def lambda_300D():
        OP_95(0xFE, -23500, -6000, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_300D)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_10_2FD9 end

    def Function_11_302E(): pass

    label("Function_11_302E")


    def lambda_3033():
        OP_95(0xFE, -20700, -6000, 0, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3033)

    def lambda_304D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_304D)
    WaitChrThread(0xFE, 1)

    def lambda_3062():
        OP_95(0xFE, -23500, -6000, 600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3062)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_11_302E end

    def Function_12_3083(): pass

    label("Function_12_3083")


    def lambda_3088():
        OP_95(0xFE, -20700, -6000, 0, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3088)

    def lambda_30A2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_30A2)
    WaitChrThread(0xFE, 1)

    def lambda_30B7():
        OP_95(0xFE, -21500, -6000, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_30B7)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_12_3083 end

    def Function_13_30D8(): pass

    label("Function_13_30D8")


    def lambda_30DD():
        OP_95(0xFE, -20700, -6000, 0, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_30DD)

    def lambda_30F7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_30F7)
    WaitChrThread(0xFE, 1)

    def lambda_310C():
        OP_95(0xFE, -21500, -6000, 600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_310C)
    WaitChrThread(0xFE, 1)
    Sound(107, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    Return()

    # Function_13_30D8 end

    def Function_14_3148(): pass

    label("Function_14_3148")


    def lambda_314D():
        OP_95(0xFE, -20700, -6000, 0, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_314D)

    def lambda_3167():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3167)
    WaitChrThread(0xFE, 1)

    def lambda_317C():
        OP_95(0xFE, -22500, -6000, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_317C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_14_3148 end

    def Function_15_319D(): pass

    label("Function_15_319D")


    def lambda_31A2():
        OP_95(0xFE, -20700, -6000, 0, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_31A2)

    def lambda_31BC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_31BC)
    WaitChrThread(0xFE, 1)

    def lambda_31D1():
        OP_95(0xFE, -22500, -6000, -1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_31D1)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_15_319D end

    def Function_16_31F2(): pass

    label("Function_16_31F2")


    def lambda_31F7():
        OP_95(0xFE, -25000, -6000, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_31F7)

    def lambda_3211():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3211)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_16_31F2 end

    def Function_17_3222(): pass

    label("Function_17_3222")

    OP_92(0xFE, 0xFFFF9FE8, 0xFFFFD8F0, 0x1F4)

    def lambda_3234():
        OP_95(0xFE, -24600, -6000, -10000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3234)
    WaitChrThread(0xFE, 1)

    def lambda_3252():
        OP_95(0xFE, -21000, -4400, -18600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3252)
    WaitChrThread(0xFE, 1)

    def lambda_3270():
        OP_95(0xFE, -21000, -4400, -21000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3270)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_17_3222 end

    def Function_18_328A(): pass

    label("Function_18_328A")

    BeginChrThread(0xC, 3, 0, 25)
    Sleep(700)
    BeginChrThread(0x101, 3, 0, 19)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 20)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 23)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 22)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 24)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 21)
    Return()

    # Function_18_328A end

    def Function_19_32C7(): pass

    label("Function_19_32C7")


    def lambda_32CC():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0xFFFFE4A8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_32CC)
    WaitChrThread(0xFE, 1)

    def lambda_32EA():
        OP_95(0xFE, -28000, -4400, -32600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_32EA)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xA0, 0x1F4)
    Return()

    # Function_19_32C7 end

    def Function_20_330B(): pass

    label("Function_20_330B")


    def lambda_3310():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0xFFFFE4A8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3310)
    WaitChrThread(0xFE, 1)

    def lambda_332E():
        OP_95(0xFE, -29800, -4400, -32800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_332E)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xA0, 0x1F4)
    Return()

    # Function_20_330B end

    def Function_21_334F(): pass

    label("Function_21_334F")


    def lambda_3354():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0xFFFFE4A8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3354)
    WaitChrThread(0xFE, 1)

    def lambda_3372():
        OP_95(0xFE, -28700, -4400, -31400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3372)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xA0, 0x1F4)
    Return()

    # Function_21_334F end

    def Function_22_3393(): pass

    label("Function_22_3393")


    def lambda_3398():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0xFFFFE4A8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3398)
    WaitChrThread(0xFE, 1)

    def lambda_33B6():
        OP_95(0xFE, -26400, -4400, -31800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_33B6)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xA0, 0x1F4)
    Return()

    # Function_22_3393 end

    def Function_23_33D7(): pass

    label("Function_23_33D7")


    def lambda_33DC():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0xFFFFE4A8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_33DC)
    WaitChrThread(0xFE, 1)

    def lambda_33FA():
        OP_95(0xFE, -30700, -4400, -31900, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_33FA)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xBE, 0x1F4)
    Return()

    # Function_23_33D7 end

    def Function_24_341B(): pass

    label("Function_24_341B")


    def lambda_3420():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0xFFFFE4A8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3420)
    WaitChrThread(0xFE, 1)

    def lambda_343E():
        OP_95(0xFE, -27100, -4400, -30600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_343E)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xA0, 0x1F4)
    Return()

    # Function_24_341B end

    def Function_25_345F(): pass

    label("Function_25_345F")


    def lambda_3464():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0xFFFFE4A8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3464)
    WaitChrThread(0xFE, 1)

    def lambda_3482():
        OP_95(0xFE, -29400, -4400, -28800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3482)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xA0, 0x1F4)
    Return()

    # Function_25_345F end

    def Function_26_34A3(): pass

    label("Function_26_34A3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x0, 0, -33620, 0, 0)
    SetChrPos(0x1, 0, -33620, 0, 0)
    SetChrPos(0x2, 0, -33620, 0, 0)
    SetChrPos(0x3, 0, -33620, 0, 0)
    LoadChrToIndex("chr/ch42250.itc", 0x1E)
    LoadChrToIndex("chr/ch42251.itc", 0x1F)
    LoadChrToIndex("chr/ch42350.itc", 0x20)
    LoadChrToIndex("chr/ch42351.itc", 0x21)
    LoadChrToIndex("chr/ch42550.itc", 0x22)
    LoadChrToIndex("chr/ch42551.itc", 0x23)
    SoundLoad(497)
    SetChrChipByIndex(0x1A, 0x21)
    SetChrSubChip(0x1A, 0x0)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 10900, 4000, 4800, 0)
    SetChrChipByIndex(0x1B, 0x21)
    SetChrSubChip(0x1B, 0x0)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, 10900, 4000, 4800, 0)
    SetChrChipByIndex(0x1C, 0x1F)
    SetChrSubChip(0x1C, 0x0)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, 10900, 4000, 4800, 0)
    SetChrChipByIndex(0x1D, 0x1F)
    SetChrSubChip(0x1D, 0x0)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, 10900, 4000, 4800, 0)
    SetChrChipByIndex(0x1E, 0x21)
    SetChrSubChip(0x1E, 0x0)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1E, 10900, 4000, 4800, 0)
    SetChrChipByIndex(0x1F, 0x21)
    SetChrSubChip(0x1F, 0x0)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, 10900, 4000, 4800, 0)
    SetChrChipByIndex(0x20, 0x21)
    SetChrSubChip(0x20, 0x0)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, 10900, 4000, 4800, 0)
    SetChrChipByIndex(0x21, 0x23)
    SetChrSubChip(0x21, 0x0)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x21, -10600, 3300, -3000, 270)
    OP_A7(0x21, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x22, 0x23)
    SetChrSubChip(0x22, 0x0)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x22, -10600, 3300, -3000, 270)
    OP_A7(0x22, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x23, 0x23)
    SetChrSubChip(0x23, 0x0)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, -10600, 3300, -3000, 270)
    OP_A7(0x23, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x24, 0x23)
    SetChrSubChip(0x24, 0x0)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x24, -10600, 3300, -3000, 270)
    OP_A7(0x24, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x25, 0x23)
    SetChrSubChip(0x25, 0x0)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, -10600, 3300, -3000, 270)
    OP_A7(0x25, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x26, 0x23)
    SetChrSubChip(0x26, 0x0)
    SetChrFlags(0x26, 0x8000)
    SetChrPos(0x26, -10600, 3300, -3000, 270)
    OP_A7(0x26, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x27, 0x23)
    SetChrSubChip(0x27, 0x0)
    SetChrFlags(0x27, 0x8000)
    SetChrPos(0x27, -10600, 3300, -3000, 270)
    OP_A7(0x27, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x16, 0x80)
    OP_78(0x7, 0x16)
    OP_49()
    SetChrPos(0x16, 11000, 60000, 0, 170)
    OP_D5(0x16, 0x0, 0x29810, 0x0, 0x0)
    SetMapObjFlags(0x7, 0x1000)
    OP_74(0x7, 0x1E)
    OP_70(0x7, 0x3D)
    OP_71(0x7, 0x3D, 0x78, 0x0, 0x20)
    ClearChrFlags(0x17, 0x80)
    OP_78(0x6, 0x17)
    OP_49()
    SetChrPos(0x17, -11000, 62000, 0, 190)
    OP_D5(0x17, 0x0, 0x2E630, 0x0, 0x0)
    SetMapObjFlags(0x6, 0x1000)
    OP_74(0x6, 0x1E)
    OP_70(0x6, 0x3D)
    OP_71(0x6, 0x3D, 0x78, 0x0, 0x20)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x17, 0x80)
    OP_78(0xC, 0x18)
    OP_78(0xB, 0x19)
    OP_49()
    SetChrPos(0x18, 10000, 100, 0, 170)
    OP_D5(0x18, 0x0, 0x29810, 0x0, 0x0)
    SetChrPos(0x19, -10000, 100, 0, 190)
    OP_D5(0x19, 0x0, 0x2E630, 0x0, 0x0)
    SetMapObjFlags(0xC, 0x1000)
    SetMapObjFlags(0xB, 0x1000)
    OP_68(0, 28000, 0, 0)
    MoveCamera(165, -35, 0, 0)
    OP_6E(1100, 0)
    SetCameraDistance(190000, 0)

    def lambda_3835():
        OP_96(0xFE, 0x2AF8, 0x9C40, 0x0, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_3835)

    def lambda_384F():
        OP_96(0xFE, 0xFFFFD508, 0xA410, 0x0, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_384F)
    Sound(497, 2, 100, 0)
    MoveCamera(15, -35, 0, 9000)
    SetCameraDistance(110000, 9000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    EndChrThread(0x16, 0xFF)
    EndChrThread(0x17, 0xFF)
    SetChrPos(0x17, -10000, 22000, 0, 190)
    SetChrPos(0x16, 10000, 20000, 0, 170)
    BeginChrThread(0x16, 3, 0, 31)
    BeginChrThread(0x17, 3, 0, 32)
    OP_68(0, 9000, 0, 0)
    MoveCamera(45, 40, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(45000, 0)
    OP_68(0, 2000, 0, 5000)
    MoveCamera(35, 17, 0, 5000)
    SetCameraDistance(35000, 5000)
    Sleep(1500)
    Sound(942, 0, 100, 0)
    WaitChrThread(0x16, 3)
    OP_82(0xC8, 0xC8, 0xBB8, 0x12C)
    Sound(495, 0, 100, 0)
    Sound(833, 0, 50, 0)
    WaitChrThread(0x17, 3)
    OP_82(0xC8, 0xC8, 0xBB8, 0x12C)
    Sound(495, 0, 100, 0)
    Sound(833, 0, 50, 0)
    StopSound(497, 1000, 100)
    Sleep(300)
    Sound(105, 0, 100, 0)
    OP_71(0x6, 0x12D, 0x168, 0x0, 0x0)
    Sleep(500)
    BeginChrThread(0x17, 3, 0, 27)
    Sleep(1500)
    BeginChrThread(0x16, 3, 0, 28)
    Sleep(2500)
    Fade(500)
    OP_68(0, -1500, 0, 0)
    MoveCamera(0, 7, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(35000, 0)
    OP_0D()
    OP_68(0, -5000, 0, 10000)
    MoveCamera(90, 3, 0, 10000)
    SetCameraDistance(39000, 10000)
    Sleep(7000)
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    OP_6F(0x79)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_24(0x1F1)
    SetScenarioFlags(0x22, 6)
    NewScene("c1540", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_26_34A3 end

    def Function_27_3A2A(): pass

    label("Function_27_3A2A")

    ClearChrFlags(0x21, 0x80)
    BeginChrThread(0x21, 3, 0, 29)
    Sleep(500)
    ClearChrFlags(0x22, 0x80)
    BeginChrThread(0x22, 3, 0, 29)
    Sleep(500)
    ClearChrFlags(0x23, 0x80)
    BeginChrThread(0x23, 3, 0, 29)
    Sleep(500)
    ClearChrFlags(0x24, 0x80)
    BeginChrThread(0x24, 3, 0, 29)
    Sleep(500)
    ClearChrFlags(0x25, 0x80)
    BeginChrThread(0x25, 3, 0, 29)
    Sleep(4000)
    ClearChrFlags(0x26, 0x80)
    BeginChrThread(0x26, 3, 0, 29)
    Sleep(500)
    ClearChrFlags(0x27, 0x80)
    BeginChrThread(0x27, 3, 0, 29)
    Return()

    # Function_27_3A2A end

    def Function_28_3A8A(): pass

    label("Function_28_3A8A")

    ClearChrFlags(0x1A, 0x80)
    BeginChrThread(0x1A, 3, 0, 30)
    Sleep(500)
    ClearChrFlags(0x1B, 0x80)
    BeginChrThread(0x1B, 3, 0, 30)
    Sleep(500)
    ClearChrFlags(0x1C, 0x80)
    BeginChrThread(0x1C, 3, 0, 30)
    Sleep(500)
    ClearChrFlags(0x1D, 0x80)
    BeginChrThread(0x1D, 3, 0, 30)
    Sleep(500)
    ClearChrFlags(0x1E, 0x80)
    BeginChrThread(0x1E, 3, 0, 30)
    Sleep(2500)
    ClearChrFlags(0x1F, 0x80)
    BeginChrThread(0x1F, 3, 0, 30)
    Sleep(500)
    ClearChrFlags(0x20, 0x80)
    BeginChrThread(0x20, 3, 0, 30)
    Return()

    # Function_28_3A8A end

    def Function_29_3AEA(): pass

    label("Function_29_3AEA")


    def lambda_3AEF():
        OP_95(0xFE, -12600, 3300, -3000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3AEF)

    def lambda_3B09():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3B09)
    WaitChrThread(0xFE, 1)

    def lambda_3B1E():
        OP_95(0xFE, -12000, 3300, -4800, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3B1E)
    WaitChrThread(0xFE, 1)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(809, 0, 30, 0)

    def lambda_3B4D():
        OP_9D(0xFE, 0xFFFFD440, 0x0, 0xFFFFDA80, 0x320, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3B4D)
    WaitChrThread(0xFE, 1)
    Sound(326, 0, 40, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3B7F():
        OP_95(0xFE, 0, 0, -18500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3B7F)
    WaitChrThread(0xFE, 1)

    def lambda_3B9D():
        OP_95(0xFE, 0, 0, -22000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3B9D)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x4)

    def lambda_3BC0():
        OP_9E(0xFE, 0x0, 0x0, 0x15F90, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3BC0)
    WaitChrThread(0xFE, 1)

    def lambda_3BDF():
        OP_95(0xFE, -18000, -6000, 0, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3BDF)
    Sleep(500)

    def lambda_3BFC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3BFC)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_29_3AEA end

    def Function_30_3C0D(): pass

    label("Function_30_3C0D")


    def lambda_3C12():
        OP_95(0xFE, 8400, 4000, 4400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3C12)
    WaitChrThread(0xFE, 1)

    def lambda_3C30():
        OP_95(0xFE, 6800, 4000, -1300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3C30)
    WaitChrThread(0xFE, 1)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3C59():
        OP_9D(0xFE, 0x11F8, 0x0, 0xFFFFE890, 0xBE, 0x320)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3C59)
    WaitChrThread(0xFE, 1)
    Sound(326, 0, 40, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3C8B():
        OP_95(0xFE, 0, 0, -18500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3C8B)
    WaitChrThread(0xFE, 1)

    def lambda_3CA9():
        OP_95(0xFE, 0, 0, -22000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3CA9)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x4)

    def lambda_3CCC():
        OP_9E(0xFE, 0x0, 0x0, 0x15F90, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3CCC)
    WaitChrThread(0xFE, 1)

    def lambda_3CEB():
        OP_95(0xFE, -18000, -6000, 0, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3CEB)
    Sleep(500)

    def lambda_3D08():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3D08)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_30_3C0D end

    def Function_31_3D19(): pass

    label("Function_31_3D19")


    def lambda_3D1E():
        OP_D5(0xFE, 0x0, 0x2E630, 0x0, 0xED8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3D1E)

    def lambda_3D37():
        OP_D5(0xFE, 0x0, 0x2E630, 0x0, 0xED8)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_3D37)

    def lambda_3D50():
        OP_96(0xFE, 0x2710, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D50)
    Sleep(2800)

    def lambda_3D6D():
        OP_96(0xFE, 0x2710, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D6D)
    Sleep(300)

    def lambda_3D8A():
        OP_96(0xFE, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D8A)
    Sleep(300)

    def lambda_3DA7():
        OP_96(0xFE, 0x2710, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3DA7)
    Sleep(300)

    def lambda_3DC4():
        OP_96(0xFE, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3DC4)
    WaitChrThread(0xFE, 1)
    ClearMapObjFlags(0x7, 0x20)
    OP_74(0x7, 0x0)
    Return()

    # Function_31_3D19 end

    def Function_32_3DE8(): pass

    label("Function_32_3DE8")


    def lambda_3DED():
        OP_D5(0xFE, 0x0, 0x29810, 0x0, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3DED)

    def lambda_3E06():
        OP_D5(0xFE, 0x0, 0x29810, 0x0, 0xDAC)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_3E06)

    def lambda_3E1F():
        OP_96(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E1F)
    Sleep(2500)

    def lambda_3E3C():
        OP_96(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E3C)
    Sleep(300)

    def lambda_3E59():
        OP_96(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E59)
    Sleep(300)

    def lambda_3E76():
        OP_96(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E76)
    Sleep(300)

    def lambda_3E93():
        OP_96(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E93)
    WaitChrThread(0xFE, 1)
    ClearMapObjFlags(0x6, 0x20)
    OP_74(0x6, 0x0)
    Return()

    # Function_32_3DE8 end

    def Function_33_3EB7(): pass

    label("Function_33_3EB7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, -19000, -6000, 0, 270)
    SetChrPos(0x102, -19000, -6000, 0, 270)
    SetChrPos(0x103, -19000, -6000, 0, 270)
    SetChrPos(0x104, -19000, -6000, 0, 270)
    SetChrPos(0x109, -19000, -6000, 0, 270)
    SetChrPos(0x105, -19000, -6000, 0, 270)
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
    ClearMapFlags(0x10000000)
    OP_68(-20000, -5000, 0, 0)
    MoveCamera(40, 23, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    OP_68(-23000, -5000, 0, 6000)
    SetCameraDistance(16000, 6000)
    BeginChrThread(0x101, 3, 0, 10)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 11)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 15)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 14)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 12)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 13)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#11P#00105FOh...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x104, 3)
    OP_68(-25000, -4500, 0, 2500)
    MoveCamera(335, 17, 0, 2500)
    SetCameraDistance(14500, 2500)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x109,
        (
            "#12P#10102FLooks like the rain\x01",
            "let up a little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FYeah... And the view is just\x01",
            "as awesome as it ever was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00002FYeah. It'd be even better\x01",
            "on a clear day, though...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(700)
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(400)

    ChrTalk(
        0x101,
        (
            "#11P#00005FI wonder where Jona\x01",
            "and Chief Roberts are?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_41C7():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_41C7)
    Sleep(50)

    def lambda_41D7():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_41D7)
    Sleep(50)

    def lambda_41E7():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_41E7)
    Sleep(50)

    def lambda_41F7():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_41F7)
    Sleep(50)

    def lambda_4207():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4207)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)

    ChrTalk(
        0x103,
        (
            "#12P#00204FProbably on a\x01",
            "section of the roof.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FLet's look for them.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -22000, -6000, 0, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x164, 7)
    ModifyEventFlags(1, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_33_3EB7 end

    def Function_34_42B5(): pass

    label("Function_34_42B5")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch00250.itc", 0x1E)
    LoadChrToIndex("chr/ch00254.itc", 0x1F)
    LoadChrToIndex("apl/ch51405.itc", 0x20)
    LoadChrToIndex("chr/ch29300.itc", 0x21)
    SoundLoad(2280)
    SoundLoad(2683)
    SoundLoad(2281)
    SoundLoad(943)
    SoundLoad(938)
    SoundLoad(852)
    LoadEffect(0x0, "battle\\mgaria0.eff")
    LoadEffect(0x1, "event\\eva06_00.eff")
    LoadEffect(0x2, "event/ev14010.eff")
    LoadEffect(0x3, "event/ev14026.eff")
    LoadEffect(0x4, "event/ev14027.eff")
    LoadEffect(0x5, "event/ev14028.eff")
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis328.itp")
    CreatePortrait(1, 308, 154, 340, 186, 0, 0, 32, 36, 0, 0, 32, 32, 0xFFFFFF, 0x0, "c_vis329.itp")
    SetChrPos(0x101, 22400, -4400, -22300, 135)
    SetChrPos(0x103, 21700, -4400, -23000, 135)
    SetChrPos(0x102, 20700, -4400, -22300, 135)
    SetChrPos(0x104, 21700, -4400, -21300, 135)
    SetChrPos(0x109, 19700, -4400, -21900, 135)
    SetChrPos(0x105, 20700, -4400, -20900, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0xB, 0x21)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 28400, -4400, -27750, 45)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x4)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xA, 0x2)
    SetChrFlags(0xA, 0x20)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xA, 31900, -4400, -27650, 75)
    BeginChrThread(0xA, 2, 0, 36)
    ClearMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x8, 0x1000)
    OP_74(0x8, 0x1E)
    OP_70(0x8, 0x2)
    OP_68(21700, -3200, -22650, 0)
    MoveCamera(350, 19, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(15000, 1200)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_450B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_450B)

    NpcTalk(
        0xB,
        "Chief Roberts' Voice",
        "Hey, we've been waiting.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    BeginChrThread(0x32, 1, 0, 41)
    OP_68(29300, -3200, -26900, 2000)
    MoveCamera(15, 17, 0, 2000)
    SetCameraDistance(13500, 2000)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(27740, -3200, -26940, 0)
    MoveCamera(350, 19, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14500, 0)
    SetChrPos(0xA, 32200, -4400, -27850, 75)

    def lambda_4634():
        OP_97(0x101, 0x11F8, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4634)
    Sleep(100)

    def lambda_4651():
        OP_97(0x103, 0x11F8, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4651)
    Sleep(100)

    def lambda_466E():
        OP_97(0x104, 0x11F8, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_466E)
    Sleep(100)

    def lambda_468B():
        OP_97(0x102, 0x11F8, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_468B)
    Sleep(100)

    def lambda_46A8():
        OP_97(0x105, 0x11F8, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_46A8)
    Sleep(100)

    def lambda_46C5():
        OP_97(0x109, 0x11F8, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_46C5)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x101,
        (
            "#00002F#5PSo this is the equipment for\x01",
            "detecting the alert signal...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12PYeah, but as it is now,\x01",
            "it can only sense signals\x01",
            "within a 10 selge radius.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#12PThat's where Tio comes in.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#00204FNo problems here.\x02\x03",
            "#00200FBut... Will it be okay with\x01",
            "the effect of the rain?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12PIt's just light rain. I don't\x01",
            "think there will be much effect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12PHowever, I cannot bring myself to expose\x01",
            "my precious Tio to the wind and rain...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12PThat's right, how about I hold\x01",
            "my umbrella over you while\x01",
            "you startup your sensors──\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#00203FI am fine. On the contrary,\x01",
            "that will be distracting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#12P*dejected*...\x02",
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
    Sleep(1000)
    EndChrThread(0xA, 0x2)
    StopSound(938, 500, 40)

    ChrTalk(
        0xA,
        (
            "#02303F#5P──Alright. \x01",
            "I'm ready too.\x02\x03",
            "#02300FYou can startup\x01",
            "Aeon anytime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#00204FThen let's begin.\x02\x03",
            "#00200FHave you input Miss Ling and Miss Eolia's\x01",
            "ENIGMA II serial numbers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12PYeah, I got them\x01",
            "from the Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#12PI've already input them into the instrument.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5P#00202FRoger.\x02",
    )

    CloseMessageWindow()

    def lambda_4B1C():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4B1C)
    Sleep(50)

    def lambda_4B2C():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4B2C)
    Sleep(50)

    def lambda_4B3C():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4B3C)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)

    def lambda_4B58():

        label("loc_4B58")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_4B58")

    QueueWorkItem2(0x101, 2, lambda_4B58)

    def lambda_4B6A():

        label("loc_4B6A")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_4B6A")

    QueueWorkItem2(0x102, 2, lambda_4B6A)

    def lambda_4B7C():

        label("loc_4B7C")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_4B7C")

    QueueWorkItem2(0x109, 2, lambda_4B7C)

    def lambda_4B8E():

        label("loc_4B8E")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_4B8E")

    QueueWorkItem2(0x105, 2, lambda_4B8E)

    def lambda_4BA0():

        label("loc_4BA0")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_4BA0")

    QueueWorkItem2(0x104, 2, lambda_4BA0)

    def lambda_4BB2():

        label("loc_4BB2")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_4BB2")

    QueueWorkItem2(0xB, 2, lambda_4BB2)
    Sleep(150)

    ChrTalk(
        0x101,
        "#11P#00001FGood luck, Tio.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#5PPlease try to locate\x01",
            "Miss Ling and Miss Eolia.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0x15E, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x103,
        "#6P#00202FYes, here I go──\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xBB8)
    OP_92(0x103, 0x6C98, 0xFFFF8C60, 0x1F4)
    OP_68(28160, -3400, -29390, 2000)

    def lambda_4C77():
        OP_95(0xFE, 27800, -4400, -29600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4C77)
    WaitChrThread(0x103, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0xB, 0x2)
    OP_93(0x103, 0x87, 0x1F4)
    Fade(250)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    OP_0D()

    def lambda_4CC8():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_4CC8)
    Sleep(500)
    Sound(2280, 255, 100, 0)

    ChrTalk(
        0x103,
        (
            "#5P#00203F#30W──Aeon System, activate.\x02\x03",
            "#00201F#30WLinking matrix system\x01",
            "with the instrument...\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0x8E8)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7352", 0)
    MoveCamera(346, 20, 0, 18000)
    SetCameraDistance(15950, 18000)
    Sound(852, 2, 100, 0)
    Sound(943, 2, 100, 0)
    PlayEffect(0x1, 0x1, 0x103, 0x5, 0, 1450, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_71(0x8, 0xA, 0x29, 0x0, 0x0)
    OP_79(0x8)
    OP_24(0x3AF)
    Sound(143, 0, 50, 0)
    Sound(938, 2, 50, 0)
    BeginChrThread(0xA, 2, 0, 36)

    ChrTalk(
        0xA,
        (
            "#02304F#6P──Link confirmed.\x02\x03",
            "#02302FAt this rate it looks like\x01",
            "there will be no problems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5POrbal power to the instrument\x01",
            "stable at high output.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5PTio, if you please.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#00203FRoger──\x01",
            "Here I go.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x103,
        "#5P#00201F#2683V#40W#20AUnlocking sensors functions...\x02",
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#5P#00203F#2281V#20A#40WAeon System─#800W─\x01",
            "#30W#00207F#4Slimit break!\x02",
        )
    )

    Sleep(1200)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    MoveCamera(333, 19, -5, 4000)
    SetCameraDistance(22000, 4000)
    BeginChrThread(0x101, 3, 0, 38)
    BeginChrThread(0x103, 3, 0, 39)
    Sound(357, 0, 100, 0)
    PlayEffect(0x0, 0x0, 0x103, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x79)
    EndChrThread(0xA, 0x2)
    Fade(500)
    OP_68(27800, -3300, -29600, 0)
    MoveCamera(100, 20, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(12000, 0)
    BeginChrThread(0xA, 2, 0, 37)
    OP_68(34800, -2800, -36600, 7000)
    MoveCamera(100, 10, -15, 7000)
    SetCameraDistance(36000, 7000)
    BeginChrThread(0xB, 3, 0, 35)
    OP_6F(0x79)
    WaitChrThread(0xB, 3)

    ChrTalk(
        0x104,
        "#00305F#6POh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10111FT-That was...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305F#6PIt looked like some kind of\x01",
            ""wave" was sent out, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EndChrThread(0xA, 0x2)
    Fade(500)
    OP_68(28060, -3400, -29350, 0)
    MoveCamera(350, 19, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14500, 0)
    BeginChrThread(0xA, 2, 0, 36)
    OP_0D()
    OP_71(0x8, 0x5A, 0x64, 0x0, 0x0)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    StopSound(852, 500, 90)
    StopSound(943, 500, 40)
    EndChrThread(0x103, 0x3)
    Sleep(500)
    Fade(250)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    StopBGM(0x1770)
    Sleep(500)

    ChrTalk(
        0x103,
        "#6P#00206F...*phew*.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5PYes, yes, it looks like a success.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(27400, -3200, -27000, 1200)

    def lambda_520F():
        TurnDirection(0x101, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_520F)
    Sleep(50)

    def lambda_521F():
        TurnDirection(0x102, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_521F)
    Sleep(50)

    def lambda_522F():
        TurnDirection(0x104, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_522F)
    Sleep(50)

    def lambda_523F():
        TurnDirection(0x109, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_523F)
    Sleep(50)

    def lambda_524F():
        TurnDirection(0x105, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_524F)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#5P#00007FReally...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#5PDo you know\x01",
            "their location?\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7151", 0)
    TurnDirection(0xB, 0x101, 500)

    ChrTalk(
        0xB,
        (
            "#12PHmm, well to be accurate, it's actually\x01",
            "the location of their ENIGMA II units.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        (
            "#6P#00203FI sensed the two\x01",
            "alert signals too.\x02\x03",
            "#00201FThey are far to the south of here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#02302F#6PAnalyzing obtained data\x01",
            "and displaying on map...\x02\x03",
            "#02309F(*klak klak*) ──There, it's done.\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    EndChrThread(0xA, 0x2)
    StopSound(938, 500, 40)
    BeginChrThread(0x101, 3, 0, 40)
    Sleep(2000)
    SetMessageWindowPos(10, 40, -1, -1)

    AnonymousTalk(
        0x101,
        "#00005FHuh...?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(30, 80, -1, -1)

    AnonymousTalk(
        0x109,
        (
            "#10101FThat's... The south\x01",
            "side of Elm Lake...!?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 20, -1, -1)

    AnonymousTalk(
        0x104,
        (
            "#00301FWhat in the world...\x01",
            "Is there even anything there?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(20, 80, -1, -1)

    AnonymousTalk(
        0x102,
        (
            "#00108FT-Those are Marshlands\x01",
            "untouched by human hands,\x01",
            "as far as I know, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(80, 20, -1, -1)

    AnonymousTalk(
        0x105,
        (
            "#10301FSo those Bracer ladies are\x01",
            "in a place like that, eh...?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(220, 180, -1, -1)

    AnonymousTalk(
        0xA,
        (
            "#02305FI don't really get it, but\x01",
            "it's not normal, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(220, 60, -1, -1)

    AnonymousTalk(
        0xB,
        "Hmm, this is concerning...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(120, 120, -1, -1)

    AnonymousTalk(
        0x103,
        "#00208FMr. Lloyd...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(10, 40, -1, -1)

    AnonymousTalk(
        0x101,
        "#00008F............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EndChrThread(0x101, 0x3)
    OP_68(31000, -3300, -28800, 0)
    MoveCamera(13, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14500, 0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x101, 30300, -4400, -29500, 55)
    SetChrPos(0x103, 30800, -4400, -30900, 15)
    SetChrPos(0x102, 29600, -4400, -28800, 55)
    SetChrPos(0x104, 28600, -4400, -28300, 100)
    SetChrPos(0x109, 28600, -4400, -30000, 55)
    SetChrPos(0x105, 29300, -4400, -30700, 55)
    SetChrPos(0xB, 30400, -4400, -26800, 100)
    SetChrPos(0xA, 31900, -4400, -27650, 75)
    OP_70(0x8, 0x2)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)
    OP_93(0x101, 0xF0, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#11P#00003F──For now, let's go\x01",
            "back to Mr. Michel.\x02\x03",
            "#00001FAnd just in case,\x01",
            "we should ask HQ to\x01",
            "prepare a boat for us.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_57BA():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_57BA)
    Sleep(50)

    def lambda_57CA():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_57CA)
    Sleep(50)

    def lambda_57DA():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_57DA)
    Sleep(50)

    def lambda_57EA():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_57EA)
    Sleep(50)

    def lambda_57FA():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_57FA)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x102,
        "#00106F#5PRight...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10101FI agree. Considering the\x01",
            "situation, we've got to hurry!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_587D():
        TurnDirection(0x101, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_587D)
    Sleep(50)

    def lambda_588D():
        TurnDirection(0x102, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_588D)
    Sleep(50)

    def lambda_589D():
        TurnDirection(0x103, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_589D)
    Sleep(50)

    def lambda_58AD():
        TurnDirection(0x104, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_58AD)
    Sleep(50)

    def lambda_58BD():
        TurnDirection(0x109, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_58BD)
    Sleep(50)

    def lambda_58CD():
        TurnDirection(0x105, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_58CD)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        (
            "#6P#00000FThank you for your cooperation,\x01",
            "Chief Roberts and Jona.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5939():
        TurnDirection(0xB, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_5939)
    Sleep(50)

    def lambda_5949():
        TurnDirection(0xA, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_5949)
    Sleep(50)
    WaitChrThread(0xB, 0)
    WaitChrThread(0xA, 0)

    ChrTalk(
        0xB,
        (
            "#5PDon't mention it. You can\x01",
            "leave the cleanup to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#02302F#11PWell, be very careful, got it?\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(15500, 2000)
    StopSound(132, 2000, 90)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    OP_24(0x3AF)
    OP_24(0x3AA)
    OP_24(0x354)
    SetScenarioFlags(0x22, 1)
    NewScene("c1010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_34_42B5 end

    def Function_35_5A02(): pass

    label("Function_35_5A02")

    Sleep(2600)
    StopEffect(0x2, 0x2)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 29400, -2900, -26600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(1014, 0, 100, 0)
    Sleep(1000)
    Sound(895, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0x103, 0x1, 0, 1500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    Sound(998, 0, 100, 0)
    Sound(922, 0, 100, 0)
    Sound(833, 0, 40, 0)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    PlayEffect(0x2, 0xFF, 0x103, 0x1, 0, 2000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sleep(1000)
    CancelBlur(1500)
    Sleep(2000)
    Return()

    # Function_35_5A02 end

    def Function_36_5AFA(): pass

    label("Function_36_5AFA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5B18")
    SetChrSubChip(0xFE, 0x4)
    Sleep(90)
    SetChrSubChip(0xFE, 0x5)
    Sleep(90)
    Jump("Function_36_5AFA")

    label("loc_5B18")

    Return()

    # Function_36_5AFA end

    def Function_37_5B19(): pass

    label("Function_37_5B19")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5B37")
    SetChrSubChip(0xFE, 0x0)
    Sleep(90)
    SetChrSubChip(0xFE, 0x1)
    Sleep(90)
    Jump("Function_37_5B19")

    label("loc_5B37")

    Return()

    # Function_37_5B19 end

    def Function_38_5B38(): pass

    label("Function_38_5B38")

    Sound(943, 2, 50, 0)
    OP_71(0x8, 0x29, 0x32, 0x0, 0x0)
    OP_79(0x8)
    Sound(311, 0, 50, 0)
    PlayEffect(0x3, 0x2, 0xFF, 0x0, 29400, -4400, -26600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_71(0x8, 0x32, 0x59, 0x0, 0x20)
    Return()

    # Function_38_5B38 end

    def Function_39_5B97(): pass

    label("Function_39_5B97")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5BB5")
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_39_5B97")

    label("loc_5BB5")

    Return()

    # Function_39_5B97 end

    def Function_40_5BB6(): pass

    label("Function_40_5BB6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5BFD")
    Sound(1021, 0, 100, 0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x12C, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(500)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x12C, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Jump("Function_40_5BB6")

    label("loc_5BFD")

    Return()

    # Function_40_5BB6 end

    def Function_41_5BFE(): pass

    label("Function_41_5BFE")

    Sound(938, 2, 0, 0)
    Sleep(200)
    OP_25(0x3AA, 0x5)
    Sleep(200)
    OP_25(0x3AA, 0xA)
    Sleep(200)
    OP_25(0x3AA, 0xF)
    Sleep(200)
    OP_25(0x3AA, 0x14)
    Sleep(200)
    OP_25(0x3AA, 0x19)
    Sleep(200)
    OP_25(0x3AA, 0x1E)
    Sleep(200)
    OP_25(0x3AA, 0x23)
    Sleep(200)
    OP_25(0x3AA, 0x28)
    Sleep(200)
    OP_25(0x3AA, 0x2D)
    Sleep(200)
    OP_25(0x3AA, 0x32)
    Return()

    # Function_41_5BFE end

    def Function_42_5C4B(): pass

    label("Function_42_5C4B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05620.itc", 0x1E)
    LoadChrToIndex("chr/ch03700.itc", 0x1F)
    LoadChrToIndex("apl/ch51545.itc", 0x20)
    LoadChrToIndex("chr/ch03300.itc", 0x21)
    LoadChrToIndex("chr/ch03400.itc", 0x22)
    LoadChrToIndex("chr/ch02100.itc", 0x23)
    LoadChrToIndex("chr/ch13400.itc", 0x24)
    LoadChrToIndex("chr/ch03600.itc", 0x25)
    LoadChrToIndex("chr/ch03500.itc", 0x26)
    LoadChrToIndex("apl/ch51548.itc", 0x27)
    LoadChrToIndex("apl/ch51543.itc", 0x28)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12300.itp")
    LoadEffect(0x0, "event/ev500_00.eff")
    LoadEffect(0x1, "event/ev10005.eff")
    LoadEffect(0x2, "event/ev10001.eff")
    LoadEffect(0x4, "event/ev15071.eff")
    LoadEffect(0x5, "event/ev17022.eff")
    LoadEffect(0x6, "event/ev10008.eff")
    LoadEffect(0x7, "event/eva03_01.eff")
    SoundLoad(832)
    SoundLoad(852)
    SetChrPos(0x0, 0, -33620, 0, 0)
    SetChrPos(0x1, 0, -33620, 0, 0)
    SetChrPos(0x2, 0, -33620, 0, 0)
    SetChrPos(0x3, 0, -33620, 0, 0)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 0, 0, -1000, 180)
    OP_8E(0xC, "President Dieter")
    SetChrChipByIndex(0x11, 0x1F)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 1600, 0, -5000, 0)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x10, 0x20)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 0, 300, -5000, 0)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x10, 1, 0, 0)
    SetChrChipByIndex(0xD, 0x21)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, -1200, 0, 400, 180)
    SetChrChipByIndex(0xE, 0x22)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, -2400, 0, 400, 180)
    SetChrChipByIndex(0xF, 0x23)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 400, 0, 1000, 180)
    OP_52(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x13, 0x24)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, -4000, 0, -4300, 90)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x14, 0x25)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, -5000, 0, -2900, 90)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x12, 0x26)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, -5500, 0, -5000, 90)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetMapObjFrame(0xFF, "sky00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kumo01a", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back00_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back01_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back02_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "a_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "b_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "c_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "d_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "02_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "03_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "futa02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "futa03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "window01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "futa00", 0x2, "close")
    SetMapObjFrame(0xFF, "futa01", 0x2, "open")
    OP_70(0x1, 0x12D)
    OP_70(0x2, 0x12D)
    OP_70(0x3, 0x12D)
    OP_70(0x4, 0x12D)
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x28, 0x8000)
    OP_78(0x5, 0x28)
    OP_D5(0x28, 0x0, 0x2BF20, 0x0, 0x0)
    SetMapObjFlags(0x5, 0x1000)
    SetMapObjFlags(0x5, 0x4)
    OP_74(0x5, 0x1E)
    OP_70(0x5, 0x0)
    SetChrFlags(0x28, 0x1)
    OP_52(0x28, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x28, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x29, 0x80)
    SetChrFlags(0x29, 0x8000)
    OP_78(0x9, 0x29)
    OP_D5(0x29, 0x0, 0x20F58, 0x0, 0x0)
    SetMapObjFlags(0x9, 0x1000)
    SetMapObjFlags(0x9, 0x4)
    OP_74(0x9, 0x1E)
    OP_70(0x9, 0x0)
    SetChrFlags(0x29, 0x1)
    OP_52(0x29, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xDAC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x29, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x2A, 0x80)
    SetChrFlags(0x2A, 0x8000)
    OP_78(0xA, 0x2A)
    OP_D5(0x2A, 0x0, 0x36EE8, 0x0, 0x0)
    SetMapObjFlags(0xA, 0x1000)
    SetMapObjFlags(0xA, 0x4)
    OP_74(0xA, 0x1E)
    OP_70(0xA, 0x0)
    SetChrFlags(0x2A, 0x1)
    OP_52(0x2A, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1F40), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x2A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 0, 0, 0)
    MoveCamera(180, 25, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(100000, 0)
    MoveCamera(45, 15, 0, 10000)
    OP_68(0, 1000, 0, 10000)
    SetCameraDistance(12000, 10000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(0, 1300, -3000, 0)
    MoveCamera(120, 17, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(12000, 0)
    SetCameraDistance(14000, 5000)
    OP_0D()
    BeginChrThread(0x32, 1, 0, 50)
    BeginChrThread(0x10, 3, 0, 45)
    Sleep(700)
    BeginChrThread(0x11, 3, 0, 45)
    Sleep(1100)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    Sleep(1)
    CancelBlur(1500)
    WaitChrThread(0x10, 3)
    Sound(852, 2, 100, 0)
    PlayEffect(0x0, 0x0, 0x10, 0x1, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitChrThread(0x11, 3)
    OP_6F(0x79)

    ChrTalk(
        0xC,
        "#11302F#6POoh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#04500F#6POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#01605F#6PShorty, you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#04602F#6P#NWow. Aren't you\x01",
            "kind of awesome?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(190, 1300, -3970, 1500)
    OP_95(0xC, -60, 0, -2170, 1200, 0x0)
    OP_6F(0x79)

    ChrTalk(
        0xC,
        (
            "#11304F#6PKeA── No, perhaps I should\x01",
            "call you "Divine Child"\x01",
            "as the Cult once did.\x02\x03",
            "#11302FWelcome. Once again, you\x01",
            "have appeared in this world.\x02\x03",
            "As the current head of the Crois clan, \x01",
            "it is my honor to welcome you.\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    AnonymousTalk(
        0x10,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#30W...Yes.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    ChrTalk(
        0x11,
        (
            "#10804F#11PUh uh, father. I think that\x01",
            "is all for the greetings.\x02\x03",
            "#10802FIt is now the time she\x01",
            "receives a gift from them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11305F#6POh, that's right.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 170, -1, -1)
    SetChrName("Man's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Hu hu, so it seems my hard\x01",
            "work has finally paid off.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(-2000, 1300, -4300, 2000)
    MoveCamera(45, 13, 0, 2000)
    SetCameraDistance(13000, 2000)
    Sleep(1000)
    Sound(977, 0, 100, 0)
    Sound(832, 2, 100, 0)
    BeginChrThread(0x13, 3, 0, 46)
    Sleep(500)
    Sound(977, 0, 50, 0)
    BeginChrThread(0x14, 3, 0, 46)
    Sleep(500)
    Sound(977, 0, 50, 0)
    BeginChrThread(0x12, 3, 0, 46)

    def lambda_669A():
        TurnDirection(0xC, 0x14, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_669A)
    Sleep(50)

    def lambda_66AA():
        TurnDirection(0x11, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_66AA)
    Sleep(50)

    def lambda_66BA():
        TurnDirection(0x10, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_66BA)
    Sleep(50)

    def lambda_66CA():
        TurnDirection(0xD, 0x14, 500)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_66CA)
    Sleep(50)

    def lambda_66DA():
        TurnDirection(0xE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_66DA)
    Sleep(50)

    def lambda_66EA():
        TurnDirection(0xF, 0x14, 500)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_66EA)
    WaitChrThread(0xC, 0)
    WaitChrThread(0x11, 0)
    WaitChrThread(0x10, 0)
    WaitChrThread(0xD, 0)
    WaitChrThread(0xE, 0)
    WaitChrThread(0xF, 0)
    OP_6F(0x79)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    Sleep(1)
    CancelBlur(1500)
    WaitChrThread(0x13, 3)
    WaitChrThread(0x14, 3)
    WaitChrThread(0x12, 3)
    OP_68(-2500, 1300, -4300, 1700)
    Sleep(1700)
    SetChrChipByIndex(0x14, 0x28)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x14, 0x20)
    SetChrFlags(0x14, 0x10)
    SetChrFlags(0x14, 0x2)
    Sleep(120)
    Sound(812, 0, 100, 0)
    SetChrSubChip(0x14, 0x1)
    Sleep(400)
    OP_6F(0x79)
    StopSound(832, 500, 100)
    Sleep(300)

    ChrTalk(
        0x12,
        (
            "#6P#04900F#3CInheritor of the great Sept-Terrion,\x01",
            "I beg of you...\x02\x03",
            "Allow me to congratulate you on your\x01",
            "manifestation in the stead of the \x01",
            ""Ouroboros"'s Grandmaster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#04704F#6PHu hu, it may be meager, but I\x01",
            "have prepared a "gift" for you.\x02\x03",
            "#04700FPlease accept it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12302F#11P...Thank you.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10, 0x0, 0x1F4)
    Fade(500)
    OP_68(0, 1700, -5000, 0)
    MoveCamera(0, 11, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(11000, 0)
    SetChrChipByIndex(0x14, 0x25)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x20)
    ClearChrFlags(0x14, 0x10)
    ClearChrFlags(0x14, 0x2)
    Sound(812, 0, 100, 0)
    OP_4B(0x10, 0xFF)
    SetChrChipByIndex(0x10, 0x27)
    SetChrSubChip(0x10, 0x1)
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetCameraDistance(10500, 800)

    def lambda_6923():
        TurnDirection(0xC, 0x10, 0)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_6923)
    Sleep(0)

    def lambda_6933():
        TurnDirection(0xD, 0x10, 0)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_6933)
    Sleep(0)

    def lambda_6943():
        TurnDirection(0xE, 0x10, 0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_6943)
    Sleep(0)

    def lambda_6953():
        TurnDirection(0xF, 0x10, 0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_6953)
    Sleep(0)
    WaitChrThread(0xC, 0)
    WaitChrThread(0xD, 0)
    WaitChrThread(0xE, 0)
    WaitChrThread(0xF, 0)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    OP_68(0, 7000, -5000, 4000)
    MoveCamera(0, -5, 0, 4000)
    Sleep(2000)
    StopSound(132, 2000, 40)
    StopSound(852, 2000, 100)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x340)
    OP_C9(0x0, 0x10)
    FadeToBright(0, 0)
    OP_0D()
    PlayMovie(0x0, "ed72_06.pmf", 0x229, 0x1)
    Sleep(1000)
    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C9(0x1, 0x10)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    OP_A7(0x28, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x29, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x2A, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_93(0xC, 0x0, 0x1F4)
    OP_93(0xF, 0x2D, 0x1F4)
    OP_93(0xD, 0x13B, 0x1F4)
    OP_93(0xE, 0x13B, 0x1F4)
    OP_93(0x11, 0x0, 0x1F4)
    OP_93(0x13, 0x0, 0x1F4)
    OP_93(0x14, 0x0, 0x1F4)
    OP_93(0x12, 0x0, 0x1F4)
    BeginChrThread(0x28, 3, 0, 47)
    BeginChrThread(0x29, 3, 0, 48)
    BeginChrThread(0x2A, 3, 0, 49)
    OP_68(0, 19000, 1000, 0)
    MoveCamera(215, 40, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(25000, 0)
    OP_68(0, 3000, 1000, 8500)
    MoveCamera(135, 27, 0, 8500)
    SetCameraDistance(20000, 8500)
    SoundLoad(979)
    Sound(852, 2, 100, 0)
    Sound(132, 2, 100, 0)
    Sound(979, 2, 100, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x10, 3, 0, 51)
    BlurSwitch(0x0, 0x77FFFFFF, 0x0, 0x0, 0x0)
    PlayEffect(0x7, 0x3, 0xFF, 0x0, 0, 30000, 0, 0, 270, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0x4, 0xFF, 0x0, 0, 30000, 0, 0, 270, 0, 2000, 1000, 2000, 0xFF, 0, 0, 0, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(6500)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6F(0x79)
    StopEffect(0x3, 0x0)
    StopEffect(0x4, 0x0)
    CancelBlur(0)
    Fade(500)
    OP_68(0, 4500, 6500, 0)
    MoveCamera(0, -23, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(9500, 0)
    SetChrFlags(0xF, 0x8)
    OP_68(0, 3000, 6500, 1500)
    MoveCamera(0, -13, 0, 1500)
    SetCameraDistance(10500, 1500)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(0, 3000, 6500, 0)
    MoveCamera(23, 13, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(13000, 0)
    ClearChrFlags(0xF, 0x8)
    SetChrChipByIndex(0x10, 0x20)
    SetChrSubChip(0x10, 0x0)
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4C(0x10, 0xFF)
    OP_68(0, 1900, 3000, 4000)
    MoveCamera(33, 9, 0, 4000)
    OP_6E(800, 4000)
    SetCameraDistance(21000, 4000)
    OP_6F(0x79)
    WaitChrThread(0x2A, 3)
    Sleep(300)

    ChrTalk(
        0xF,
        "#01607F#6PT-These are...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#04612F#12PWoooah!\x01",
            "So cool!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#04502F#12PHehe... Nice toys\x01",
            "you've got there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#10804F#12P#NAions, the "God Machines"...\x02\x03",
            "#10800FThree interfaces for the "Sept-Terrion"\x01",
            "to create miracles...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(800)
    OP_68(0, 1000, -1000, 0)
    MoveCamera(24, 12, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(15500, 0)
    SetCameraDistance(15000, 1500)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0xC,
        "#11P#11304F#12P...They're better made than I expected.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x13, 500)

    ChrTalk(
        0xC,
        (
            "#11P#11300FLady and gentlemen of the "Society".\x01",
            "It seems I'm in your debt.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6E38():
        TurnDirection(0x13, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_6E38)
    Sleep(50)

    def lambda_6E48():
        TurnDirection(0x12, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_6E48)
    Sleep(50)

    def lambda_6E58():
        TurnDirection(0x14, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_6E58)
    Sleep(50)
    WaitChrThread(0x13, 0)
    WaitChrThread(0x12, 0)
    WaitChrThread(0x14, 0)

    def lambda_6E74():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_6E74)

    ChrTalk(
        0x13,
        (
            "#5P#04709F#6PHa ha, well on our side, we're always\x01",
            "grateful for your financial assistance.\x02\x03",
            "#04702FBeing able to use that Gordias-class\x01",
            "data especially was a great help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#04900F#3C#6P#NAnd this time, our "Grandmaster"'s\x01",
            "will too will be realized...\x02\x03",
            "There is no need to consider this a debt.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x11,
        (
            "#10809F#11PUhuhu... You are\x01",
            "quite generous.\x02\x03",
            "#10802F──Miss KeA. \x01",
            "Will you do the honors?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12301F#12PYes... Got it.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    Fade(250)
    Sound(802, 0, 50, 0)
    OP_4B(0x10, 0x1)
    SetChrChipByIndex(0x10, 0x27)
    SetChrSubChip(0x10, 0x2)
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    Sleep(500)
    OP_68(0, 1900, 3000, 2000)
    MoveCamera(33, 9, 0, 2000)
    OP_6E(800, 2000)
    SetCameraDistance(21000, 2000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(273, 0, 70, 0)
    PlayEffect(0x4, 0x1, 0xFF, 0x0, -7000, 5000, 2000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x2, 0xFF, 0x0, 9000, 5000, 2000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_710D():
        OP_93(0xC, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_710D)
    Sleep(50)

    def lambda_711D():
        OP_93(0x11, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_711D)
    Sleep(50)

    def lambda_712D():
        OP_93(0x13, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_712D)
    Sleep(50)

    def lambda_713D():
        OP_93(0x12, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_713D)
    Sleep(50)

    def lambda_714D():
        OP_93(0x14, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_714D)
    Sleep(50)
    WaitChrThread(0xC, 0)
    WaitChrThread(0x11, 0)
    WaitChrThread(0x13, 0)
    WaitChrThread(0x12, 0)
    WaitChrThread(0x14, 0)
    Sleep(2000)
    StopEffect(0x1, 0x2)
    StopEffect(0x2, 0x2)
    BeginChrThread(0x29, 3, 0, 43)
    BeginChrThread(0x2A, 3, 0, 44)
    WaitChrThread(0x29, 3)
    Sleep(2000)
    StopSound(979, 2000, 100)
    StopSound(132, 2000, 100)
    FadeToDark(2000, 0, -1)
    OP_0D()
    CancelBlur(0)
    OP_CC(0x1, 0xFF, 0x0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x229), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x24, 3)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_42_5C4B end

    def Function_43_71BE(): pass

    label("Function_43_71BE")

    OP_68(0, 2900, 3000, 1500)
    SetCameraDistance(23000, 1500)
    Sound(935, 0, 100, 0)

    def lambda_71E3():
        OP_96(0xFE, 0xFFFFE4A8, 0x7D0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_71E3)
    OP_74(0x9, 0x1E)
    OP_71(0x9, 0x14A, 0x15E, 0x0, 0x0)
    OP_79(0x9)
    OP_74(0x9, 0xA)
    OP_71(0x9, 0xA, 0x32, 0x0, 0x20)
    WaitChrThread(0x29, 1)
    OP_6F(0x79)
    Sound(905, 0, 100, 0)
    OP_71(0x9, 0x65, 0x6E, 0x15E, 0x0)
    OP_79(0x9)
    OP_71(0x9, 0x6F, 0x96, 0x0, 0x20)
    OP_68(0, 3900, -3000, 2500)
    MoveCamera(60, 7, 15, 2500)
    SetCameraDistance(40000, 6500)
    BlurSwitch(0x3E8, 0x77FFFFFF, 0x0, 0x0, 0x0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 0, 10000, -7000, 90, 0, 0, 500, 3000, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 0, 10000, -7000, 90, 0, 0, 1000, 3000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 0, 10000, -7000, 90, 0, 0, 1500, 3000, 1500, 0xFF, 0, 0, 0, 0)
    Sound(833, 0, 50, 0)
    Sound(499, 0, 100, 0)
    OP_87(0x5, 0xFF, 0x9, "Null_wing_r0 (66)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x5, 0xFF, 0x9, "Null_wing_r1(67)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x5, 0xFF, 0x9, "Null_wing_r2(68)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x5, 0xFF, 0x9, "Null_wing_l0(69)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x5, 0xFF, 0x9, "Null_wing_l1(70)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x5, 0xFF, 0x9, "Null_wing_l2(71)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_9F(0x0, 0x29)
    OP_9F(0x1, 8000, 3000, -4000)
    OP_9F(0x1, 20000, 4000, -7000)
    OP_9F(0x1, 500000, 7000, -8000)

    def lambda_74AE():
        OP_9F(0x2, 0x29, 20000, 0x6)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_74AE)
    Sleep(1000)

    def lambda_74C0():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_74C0)
    Sleep(300)

    def lambda_74D0():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_74D0)
    OP_6F(0x41)
    Return()

    # Function_43_71BE end

    def Function_44_74DB(): pass

    label("Function_44_74DB")

    Sound(978, 0, 50, 0)
    OP_25(0x3D3, 0x64)
    OP_71(0xA, 0x5A, 0x33, 0x0, 0x0)

    def lambda_74F6():
        OP_96(0xFE, 0x2328, 0x3E8, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_74F6)
    WaitChrThread(0x2A, 1)
    OP_79(0xA)
    OP_71(0xA, 0xA, 0x32, 0x0, 0x20)
    Sleep(2000)
    OP_9F(0x0, 0x2A)
    OP_9F(0x1, -5000, 3000, -3000)
    OP_9F(0x1, -20000, 4000, -6000)
    OP_9F(0x1, -200000, 7000, -7000)

    def lambda_7554():
        OP_9F(0x2, 0x2A, 10000, 0x6)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_7554)
    Sleep(1000)

    def lambda_7566():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_7566)
    Sleep(100)

    def lambda_7576():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_7576)
    Sleep(100)

    def lambda_7586():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_7586)
    Return()

    # Function_44_74DB end

    def Function_45_758F(): pass

    label("Function_45_758F")

    PlayEffect(0x1, 0xFF, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1800)

    def lambda_75CE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_75CE)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_45_758F end

    def Function_46_75DF(): pass

    label("Function_46_75DF")

    PlayEffect(0x2, 0xFF, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    Sound(936, 0, 80, 0)

    def lambda_7624():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7624)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_46_75DF end

    def Function_47_7635(): pass

    label("Function_47_7635")

    SetChrPos(0x28, 0, 20000, 7000, 180)
    OP_71(0x5, 0x5B, 0x82, 0x0, 0x20)

    def lambda_7657():
        OP_96(0xFE, 0x0, 0x1F4, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7657)
    WaitChrThread(0xFE, 1)
    OP_71(0x5, 0x83, 0x96, 0x0, 0x0)

    def lambda_7681():
        OP_96(0xFE, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7681)
    WaitChrThread(0xFE, 1)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_82(0x0, 0x1F4, 0xBB8, 0x1F4)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sound(902, 0, 100, 0)
    Sound(833, 0, 70, 0)
    OP_79(0x5)
    OP_71(0x5, 0x406, 0x42E, 0x0, 0x20)
    CancelBlur(500)
    Sleep(500)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_47_7635 end

    def Function_48_76EF(): pass

    label("Function_48_76EF")

    SetChrPos(0x29, -7000, 25000, 2000, 135)
    OP_71(0x9, 0xB, 0x32, 0x0, 0x20)

    def lambda_7711():
        OP_96(0xFE, 0xFFFFE4A8, 0x0, 0x7D0, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7711)
    Sleep(13000)
    Sound(905, 0, 70, 0)
    OP_71(0x9, 0x122, 0x136, 0x0, 0x0)
    OP_79(0x9)
    OP_74(0x9, 0xF)
    OP_71(0x9, 0x136, 0x14A, 0x0, 0x20)
    WaitChrThread(0xFE, 1)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_82(0x0, 0xFA, 0xBB8, 0x1F4)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sound(902, 0, 100, 0)
    Sound(833, 0, 70, 0)
    CancelBlur(500)
    Sleep(500)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_48_76EF end

    def Function_49_7798(): pass

    label("Function_49_7798")

    SetChrPos(0x2A, 9000, 28000, 2000, 225)
    OP_71(0xA, 0xA, 0x32, 0x0, 0x20)

    def lambda_77BA():
        OP_96(0xFE, 0x2328, 0x3E8, 0x7D0, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_77BA)
    WaitChrThread(0xFE, 1)
    OP_71(0xA, 0x33, 0x5A, 0x0, 0x0)

    def lambda_77E4():
        OP_96(0xFE, 0x2328, 0x0, 0x7D0, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_77E4)
    WaitChrThread(0xFE, 1)
    Sound(978, 0, 100, 0)
    Sound(833, 0, 100, 0)
    OP_25(0x3D3, 0x1E)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 9000, 0, 2000, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_82(0x0, 0x2BC, 0xBB8, 0x1F4)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_79(0xA)
    OP_71(0xA, 0x172, 0x19A, 0x3E8, 0x20)
    CancelBlur(500)
    Sleep(1000)
    Return()

    # Function_49_7798 end

    def Function_50_7883(): pass

    label("Function_50_7883")

    Sound(921, 0, 100, 0)
    Sound(922, 0, 50, 0)
    Sound(977, 0, 80, 0)
    Sound(832, 2, 100, 0)
    Sleep(700)
    Sound(922, 0, 40, 0)
    Sound(977, 0, 60, 0)
    Sleep(800)
    Sound(936, 0, 80, 0)
    Sleep(1000)
    Sound(936, 0, 80, 0)
    StopSound(832, 1000, 100)
    Return()

    # Function_50_7883 end

    def Function_51_78C3(): pass

    label("Function_51_78C3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7945")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_78F3")
    OP_82(0x0, 0xF, 0xBB8, 0x1F4)
    Jump("loc_793D")

    label("loc_78F3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7918")
    OP_82(0x4B, 0x96, 0x1388, 0x1F4)
    Jump("loc_793D")

    label("loc_7918")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_793D")
    OP_82(0x19, 0x32, 0x1388, 0x1F4)
    Jump("loc_793D")

    label("loc_793D")

    Sleep(500)
    Jump("Function_51_78C3")

    label("loc_7945")

    Return()

    # Function_51_78C3 end

    def Function_52_7946(): pass

    label("Function_52_7946")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05620.itc", 0x1E)
    LoadChrToIndex("chr/ch03700.itc", 0x1F)
    LoadChrToIndex("apl/ch51545.itc", 0x20)
    LoadChrToIndex("chr/ch03300.itc", 0x21)
    LoadChrToIndex("chr/ch03400.itc", 0x22)
    LoadChrToIndex("chr/ch02100.itc", 0x23)
    LoadChrToIndex("chr/ch13400.itc", 0x24)
    LoadChrToIndex("chr/ch03600.itc", 0x25)
    LoadChrToIndex("chr/ch03500.itc", 0x26)
    LoadChrToIndex("apl/ch51532.itc", 0x27)
    LoadEffect(0x0, "event/ev500_00.eff")
    SoundLoad(852)
    SoundLoad(3978)
    SetChrPos(0x0, 0, -33620, 0, 0)
    SetChrPos(0x1, 0, -33620, 0, 0)
    SetChrPos(0x2, 0, -33620, 0, 0)
    SetChrPos(0x3, 0, -33620, 0, 0)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -1500, 0, -2000, 270)
    OP_8E(0xC, "President Dieter")
    SetChrChipByIndex(0x11, 0x1F)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, -600, 0, -6300, 270)
    SetChrChipByIndex(0x10, 0x20)
    SetChrSubChip(0x10, 0x2)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 0, 300, -4900, 270)
    OP_52(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x10, 1, 0, 0)
    PlayEffect(0x0, 0x0, 0x10, 0x1, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xD, 0x21)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, -3700, 0, -700, 270)
    SetChrChipByIndex(0xE, 0x22)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, -4100, 0, 400, 270)
    SetChrChipByIndex(0xF, 0x23)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -1900, 0, -200, 270)
    OP_52(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x13, 0x24)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, -4000, 0, -4300, 270)
    SetChrChipByIndex(0x14, 0x25)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, -5000, 0, -3300, 270)
    SetChrChipByIndex(0x12, 0x26)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, -5500, 0, -5000, 270)
    SetMapObjFrame(0xFF, "sky00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kumo01a", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back00_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back01_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back02_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "a_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "b_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "c_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "d_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "02_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "03_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "futa02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "futa03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "window01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "futa00", 0x2, "close")
    SetMapObjFrame(0xFF, "futa01", 0x2, "open")
    OP_70(0x1, 0x12D)
    OP_70(0x2, 0x12D)
    OP_70(0x3, 0x12D)
    OP_70(0x4, 0x12D)
    OP_68(-7500, 2200, -4000, 0)
    MoveCamera(40, 15, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14500, 0)
    Sound(852, 2, 100, 0)
    OP_68(-2800, 1200, -3040, 3000)
    SetCameraDistance(13500, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    OP_C9(0x0, 0x80000000)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0xE,
        "#04612F#3978V#5S#11P#13AWoohoo!!\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(300)

    ChrTalk(
        0xF,
        "#11P#01611F...W-What the hell...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#12P#04809FAhaha, that was great!\x02\x03",
            "#04802FThe "Sept-Terrion of Zero"...\x01",
            "That's very well said!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#12P#04702FHehe... Operating three Gordias-class\x01",
            "final models at the same time...!\x02\x03",
            "And to think they can\x01",
            "autonomously create miracles!\x02\x03",
            "#04709FHa ha, it seems I'll be able to make\x01",
            "a good report to that person too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#12P#04900F#3C#30W............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P#04504FHmph... \x01",
            "Their power is certainly great.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#12P#10811FUh uh, I presume we should leave\x01",
            "it at this for the first time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12312F#40W............\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x320)

    ChrTalk(
        0xC,
        (
            "#11P#11309FHu hu hu...\x01",
            "#4SHA HA HA HA HA HA HA HA HA HA!!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-1650, 1200, -2100, 1500)
    MoveCamera(90, 21, 0, 1500)
    SetCameraDistance(13000, 1500)
    OP_6F(0x79)
    SetCameraDistance(12000, 10000)
    SetChrChipByIndex(0xC, 0x27)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xC, 0x2)
    SetChrFlags(0xC, 0x20)
    Sleep(110)
    Sound(812, 0, 100, 0)
    SetChrSubChip(0xC, 0x1)
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0xC,
        (
            "#11304F#30W──Now, at this very moment,\x01",
            "Crossbell has become a "holy ground"!\x02\x03",
            "#11302FStep aside, Empire and Republic.\x01",
            "It's from this very point that a new\x01",
            "continental order will spring forth!\x02\x03",
            "With the ideals of our Crois clan and spreading\x01",
            "justice throughout the world at its center...!\x02",
        )
    )

    CloseMessageWindow()
    OP_6F(0x79)
    SetCameraDistance(23000, 5000)
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0xBB8)

    ChrTalk(
        0xC,
        "#11309F#5S#40W#30AHAA HA HA HA HA HA HAH!!\x02",
    )

    Sleep(2000)
    StopSound(132, 2000, 100)
    StopSound(852, 2000, 100)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0x1770)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 3)
    NewScene("t1490", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_52_7946 end

    def Function_53_822E(): pass

    label("Function_53_822E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch11600.itc", 0x1E)
    LoadChrToIndex("chr/ch13400.itc", 0x1F)
    LoadChrToIndex("chr/ch03600.itc", 0x20)
    LoadChrToIndex("chr/ch04200.itc", 0x21)
    LoadEffect(0x0, "event\\ev500_00.eff")
    SetChrPos(0x0, 0, -33620, 0, 0)
    SetChrPos(0x1, 0, -33620, 0, 0)
    SetChrPos(0x2, 0, -33620, 0, 0)
    SetChrPos(0x3, 0, -33620, 0, 0)
    SetChrChipByIndex(0x10, 0x1E)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 12300, -33620, 23500, 0)
    OP_52(0x10, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x0, 0xFF, 0x10, 0x0, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x13, 0x1F)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 6900, 0, -14700, 135)
    SetChrChipByIndex(0x14, 0x20)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 5700, 0, -15500, 135)
    SetChrChipByIndex(0x12, 0x21)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 7500, 0, -16200, 135)
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x28, 0x8000)
    OP_78(0x5, 0x28)
    SetChrPos(0x28, 0, 0, 0, 180)
    OP_D5(0x28, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x5, 0x1000)
    OP_74(0x5, 0x1E)
    OP_70(0x5, 0x406)
    SetChrFlags(0x28, 0x1)
    OP_52(0x28, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "sky00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kumo01a", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back00_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back01_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back02_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "a_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "b_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "c_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "d_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "02_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "03_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "futa02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "futa03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "window01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "futa00", 0x2, "close")
    SetMapObjFrame(0xFF, "futa01", 0x2, "open")
    OP_70(0x1, 0x12D)
    OP_70(0x2, 0x12D)
    OP_70(0x3, 0x12D)
    OP_70(0x4, 0x12D)
    OP_68(0, 6500, 0, 0)
    MoveCamera(147, -3, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(16500, 0)
    OP_F0(0x0, 0x1)
    OP_68(0, 3500, 0, 7000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    OP_68(6800, 1200, -16300, 4000)
    MoveCamera(90, 13, 0, 4000)
    SetCameraDistance(12500, 4000)
    OP_6F(0x79)
    SetCameraDistance(11500, 30000)
    Sleep(300)

    ChrTalk(
        0x14,
        (
            "#6P#04804FNow then, the stage is set to carry out the\x01",
            ""Phantasmal Blaze Plan" in the Empire...\x02\x03",
            "#04802FFrom here, we'll wait and see\x01",
            "for awhile like we planned?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#04923FYes, correct.\x02\x03",
            "#04921FI will accompany you until the\x01",
            "appropriate stage in the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#04704F#5PHu hu. The present power of the \x01",
            ""Sept-Terrion of Zero" is comparable \x01",
            "to the vanished "Sept-Terrion of Mirage".\x02\x03",
            "Furthermore, it has shown abilities\x01",
            "the original did not have...\x02\x03",
            "#04702FHehe. Let's see how far the skills of\x01",
            "the Crois clan have made it evolve.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x13, 500)
    Sleep(100)

    ChrTalk(
        0x14,
        (
            "#12P#04809FUhuhu... You're in a\x01",
            "good mood, Doctor.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x14, 0x87, 0x1F4)

    ChrTalk(
        0x14,
        (
            "#6P#04805FThat reminds me, it looks like\x01",
            ""they" finally started moving?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#04924FIt a rather good opportunity.\x02\x03",
            "#04922FTheir position is different from ours...\x01",
            "We should find out exactly how\x01",
            "for the future's sake too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#04700F#5PHu hu, I'll leave that to you guys.\x02\x03",
            "#04704FI'll continue collecting data on\x01",
            "the "Sept-Terrion of Zero" here...\x02\x03",
            "#04702F──To see if I can obtain the ultimate\x01",
            "interface between humans and gods!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(6800, -800, -16300, 3000)
    StopSound(132, 2000, 90)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    OP_68(12300, -32820, 23400, 0)
    MoveCamera(150, 25, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(35000, 0)
    SetCameraDistance(15000, 9000)
    Sound(132, 2, 50, 0)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    StopSound(132, 1000, 40)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("e4020", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_53_822E end

    def Function_54_8A4B(): pass

    label("Function_54_8A4B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch11600.itc", 0x1E)
    LoadChrToIndex("chr/ch04200.itc", 0x1F)
    LoadEffect(0x0, "event\\ev500_00.eff")
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 0x1E)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 17450, 0, -5600, 225)
    PlayEffect(0x0, 0xFF, 0x10, 0x0, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 0x1F)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 16250, 0, -8350, 45)
    OP_68(17260, 1000, -7120, 0)
    MoveCamera(68, 17, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(12000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    label("loc_8B41")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8B54")
    Sleep(1)
    Jump("loc_8B41")

    label("loc_8B54")

    FadeToDark(1000, 0, -1)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_54_8A4B end

    def Function_55_8B62(): pass

    label("Function_55_8B62")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis416.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12300.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02900.itp")
    LoadChrToIndex("chr/ch05500.itc", 0x1E)
    LoadChrToIndex("chr/ch11600.itc", 0x1F)
    LoadEffect(0x0, "event\\ev500_00.eff")
    SoundLoad(3634)
    SoundLoad(3635)
    SetChrChipByIndex(0x11, 0x1E)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, -22000, -4400, -22000, 225)
    SetChrChipByIndex(0x10, 0x1F)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, -27500, -4400, -32600, 150)
    PlayEffect(0x0, 0xFF, 0x10, 0x0, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFF, 0xAF, 0x9B, 0x12C, 0x384, 0x0)
    SetMapObjFrame(0xFF, "sky00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kumo01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01a", 0x0, 0x1)
    OP_68(-22300, -3300, -44000, 0)
    MoveCamera(195, 15, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(28000, 0)
    OP_68(-27500, -3300, -32600, 7000)
    SetCameraDistance(14000, 7000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x10,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#30W............\x07\x00\x02",
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
    ClearChrFlags(0x11, 0x80)

    NpcTalk(
        0x11,
        "Mariabell's Voice",
        (
            "Uh uh... They have really done\x01",
            "it this time, haven't they.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-24000, -3300, -24000, 0)
    MoveCamera(180, 17, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15000, 0)
    OP_68(-27350, -3300, -31200, 5000)
    MoveCamera(150, 17, 0, 5000)
    SetCameraDistance(13500, 5000)

    def lambda_8E83():
        OP_95(0xFE, -26500, -4400, -26500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8E83)
    WaitChrThread(0x11, 1)

    def lambda_8EA1():
        OP_95(0xFE, -27000, -4400, -29500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8EA1)
    WaitChrThread(0x11, 1)
    TurnDirection(0x10, 0x11, 400)
    OP_6F(0x79)
    SetCameraDistance(11500, 50000)
    Sleep(150)

    ChrTalk(
        0x10,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#11P#12300FBell...\x02\x03",
            "#12308FDieter is looking for you...\x01",
            "Don't you have to go?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x11,
        (
            "Uhuhu. Let father\x01",
            "worry a bit more.\x02\x03",
            "I think the "barrier" will be\x01",
            "difficult to deploy without the\x01",
            "resonance of the "bells", right?\x02",
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
        0x10,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#11P#12303F#30W...Yes, as they are now.\x02\x03",
            "#12308FAlthough those Aions can operate, \x01",
            "they can't use the power of "space"...\x02\x03",
            "#12315F──Lloyd and the others. They're coming.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#6P#02913FUh uh, how troublesome.\x02\x03",
            "At this rate, it will\x01",
            "go according to plan.\x02\x03",
            "#02911FTo "his" plan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#11P#12303F#30W............\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#6P#02902FEverything is up to you, Miss KeA...\x01",
            "We only follow you.\x02\x03",
            "#02903FWill you get off here──? \x01",
            "Or will you make everything come true?\x02\x03",
            "#02912FThe time to choose will be here soon, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#11P#12304F#40W...Yes.\x02\x03",
            "#12302FAt first, KeA didn't know whether\x01",
            "there was another path...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10, 0x73, 0x1F4)
    Sleep(300)
    OP_63(0x10, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x10)
    Sleep(800)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, -1, -1, -1)

    ChrTalk(
        0x10,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#11P#12304F#3634V#40W#55AFor Lloyd, Elie, Tio, Randy, Shizuku,\x01",
            "and everyone else, too...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(11000, 2000)
    StopSound(132, 2000, 100)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x10,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#3635V#40W#45A──I'll definitely make everything come true.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    StopBGM(0x1770)
    WaitBGM()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(2000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("e302B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_55_8B62 end

    def Function_56_9400(): pass

    label("Function_56_9400")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "event/ev17031.eff")
    SoundLoad(980)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x28, 0x80)
    OP_78(0x5, 0x28)
    OP_49()
    SetChrPos(0x28, 0, 0, 0, 0)
    OP_93(0x28, 0xB4, 0x0)
    SetMapObjFlags(0x5, 0x1000)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0xB, 0x32, 0x0, 0x20)
    SetChrFlags(0x28, 0x1)
    OP_52(0x28, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1194), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(-570, 2100, -8640, 0)
    MoveCamera(144, 45, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(130610, 0)
    Sound(980, 2, 20, 0)
    FadeToBright(1000, 0)
    OP_68(3650, 11100, 4520, 10000)
    MoveCamera(133, -7, 0, 10000)
    OP_6E(800, 10000)
    SetCameraDistance(54000, 10000)
    BeginChrThread(0x29, 0, 0, 57)
    OP_0D()
    Sleep(7000)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 200000, 45500, -200000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x79)
    Sleep(1000)
    StopSound(980, 1000, 10)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopEffect(0x0, 0x2)
    SetScenarioFlags(0x23, 2)
    NewScene("e4310", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_56_9400 end

    def Function_57_9574(): pass

    label("Function_57_9574")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_95B2")
    Sleep(600)
    OP_98(0xFE, 0x0, 0xFFFFF8F8, 0x0, 0x258, 0x1)
    Sleep(600)
    OP_98(0xFE, 0x0, 0x708, 0x0, 0x258, 0x1)
    Jump("Function_57_9574")

    label("loc_95B2")

    Return()

    # Function_57_9574 end

    def Function_58_95B3(): pass

    label("Function_58_95B3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_F3(200000)
    BlurSwitch(0x0, 0x55FFFFFF, 0x0, 0x1, 0x0)
    LoadEffect(0x0, "event/ev17031.eff")
    LoadEffect(0x7, "event/ev17022.eff")
    LoadEffect(0x8, "event/eva03_01.eff")
    SoundLoad(980)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x28, 0x80)
    OP_78(0x5, 0x28)
    OP_49()
    SetChrPos(0x28, 0, 0, 0, 0)
    OP_93(0x28, 0xB4, 0x0)
    SetMapObjFlags(0x5, 0x1000)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0xB, 0x32, 0x0, 0x20)
    SetChrFlags(0x28, 0x1)
    OP_52(0x28, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1194), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x29, 0x80)
    OP_78(0x9, 0x29)
    OP_49()
    SetChrPos(0x29, -15000, 10200, 60080, 0)
    OP_93(0x29, 0xB4, 0x0)
    SetMapObjFlags(0x9, 0x1000)
    OP_74(0x9, 0x1E)
    OP_70(0x9, 0xDD)
    SetChrFlags(0x29, 0x1)
    OP_52(0x29, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_87(0x7, 0xFF, 0x9, "Null_wing_r0 (66)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x7, 0xFF, 0x9, "Null_wing_r1(67)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x7, 0xFF, 0x9, "Null_wing_r2(68)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x7, 0xFF, 0x9, "Null_wing_l0(69)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x7, 0xFF, 0x9, "Null_wing_l1(70)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x7, 0xFF, 0x9, "Null_wing_l2(71)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    ClearChrFlags(0x2B, 0x80)
    OP_78(0x13, 0x2B)
    OP_49()
    SetChrPos(0x2B, 200000, 45000, -200000, 0)
    OP_93(0x2B, 0x13B, 0x0)
    ClearMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x13, 0x1000)
    OP_74(0x13, 0x1E)
    OP_71(0x13, 0x1, 0x78, 0x0, 0x20)
    OP_FF(0x13, 0x96, 0x96, 0x96)
    OP_75(0x13, 0x1, 0x0)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 200000, 45500, -200000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(980, 2, 20, 0)
    FadeToBright(1000, 0)
    OP_68(5000, 9900, 1500, 0)
    MoveCamera(154, 2, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(42350, 0)
    OP_68(5000, 9900, 1500, 5000)
    MoveCamera(136, 3, 0, 5000)
    OP_6E(800, 5000)
    SetCameraDistance(42350, 5000)
    OP_0D()
    Sleep(1500)
    OP_75(0x13, 0x2, 0x0)
    OP_93(0x29, 0xA1, 0x28)
    EndChrThread(0x29, 0x0)
    BeginChrThread(0x29, 0, 0, 60)
    BeginChrThread(0x29, 1, 0, 61)
    Sleep(500)
    Sound(499, 0, 100, 0)
    Sound(998, 0, 100, 0)
    Sleep(4000)
    OP_6F(0x79)
    OP_FF(0x13, 0x3E8, 0x3E8, 0x3E8)
    SetMapObjFlags(0x13, 0x4)
    PlayEffect(0x8, 0xFF, 0x29, 0x5, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x8, 0xFF, 0x29, 0x5, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(999, 0, 100, 0)
    OP_68(133720, 25300, -151690, 0)
    MoveCamera(323, 6, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(107240, 0)
    Fade(500)
    OP_0D()
    BlurSwitch(0x3E8, 0x77FFFFFF, 0x0, 0x1, 0xA)
    Sleep(1500)
    EndChrThread(0x29, 0x0)
    OP_6F(0x79)
    StopSound(980, 1000, 10)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x23, 3)
    NewScene("e4310", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_58_95B3 end

    def Function_59_9A4B(): pass

    label("Function_59_9A4B")

    ClearMapObjFlags(0x9, 0x20)
    OP_79(0x9)
    Sound(982, 0, 100, 0)
    Sound(905, 0, 100, 0)
    OP_71(0x9, 0xC9, 0xDC, 0x0, 0x0)
    Sleep(300)
    Sleep(1000)
    OP_79(0x9)
    OP_70(0x9, 0xDD)
    Return()

    # Function_59_9A4B end

    def Function_60_9A7A(): pass

    label("Function_60_9A7A")

    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0xFA0, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x1F40, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x2EE0, 0x1)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 5500, 10200, 3080)
    OP_9F(0x1, 50000, 10200, -120000)
    OP_9F(0x1, 72000, 14200, -155000)
    OP_9F(0x1, 95000, 18200, -180000)
    OP_9F(0x1, 120000, 22200, -200000)
    OP_9F(0x1, 150000, 25200, -215000)
    OP_9F(0x1, 203000, 33200, -225000)
    OP_9F(0x2, 0xFE, 65000, 0x2)
    Return()

    # Function_60_9A7A end

    def Function_61_9B17(): pass

    label("Function_61_9B17")

    Sleep(2000)
    OP_74(0x9, 0x3)
    OP_71(0x9, 0x104, 0x103, 0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_61_9B17 end

    def Function_62_9B2E(): pass

    label("Function_62_9B2E")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00250.itc", 0x21)
    LoadChrToIndex("chr/ch00350.itc", 0x22)
    Call(0, 64)
    Call(0, 65)
    LoadEffect(0x0, "event/ev17050.eff")
    LoadEffect(0x1, "event/ev17051.eff")
    SoundLoad(943)
    SoundLoad(933)
    SoundLoad(927)
    SoundLoad(950)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu11300.itp")
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x28, 0x8000)
    OP_78(0x5, 0x28)
    OP_49()
    SetChrPos(0x28, 0, 0, 6500, 180)
    OP_D5(0x28, 0x0, 0x2BF20, 0x0, 0x0)
    SetMapObjFlags(0x5, 0x1000)
    OP_74(0x5, 0x1E)
    OP_70(0x5, 0x42E)
    SetChrFlags(0x28, 0x1)
    OP_52(0x28, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xC, 0x3)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 0, 0, 0, 180)
    OP_8E(0xC, "President Dieter")
    OP_52(0xC, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x101, -600, 0, -20000, 0)
    SetChrPos(0x102, 600, 0, -20000, 0)
    SetChrPos(0x103, -1100, 0, -21100, 0)
    SetChrPos(0x104, 1100, 0, -21100, 0)
    SetChrPos(0xF4, -600, 0, -22200, 0)
    SetChrPos(0xF5, 600, 0, -22200, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(0, 1100, -20000, 0)
    MoveCamera(55, 23, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13500, 0)
    FadeToBright(500, 0)
    OP_0D()

    NpcTalk(
        0xC,
        "Man's Voice",
        (
            "Well, well. To think\x01",
            "some uninvited guests\x01",
            "could make it this far.\x02",
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
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    PlayBGM("ed7356", 0)
    OP_68(0, 2500, -2000, 3000)
    MoveCamera(0, 9, 0, 3000)
    SetCameraDistance(13000, 3000)
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0x102,
        "#2P#00107F#N..."Uncle"!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#1P#00007F#NMr. Dieter...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 1300, -5000, 0)
    MoveCamera(34, 11, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, -500, 0, -15500, 0)
    SetChrPos(0x102, 500, 0, -15500, 0)
    SetChrPos(0x103, -1000, 0, -17000, 0)
    SetChrPos(0x104, 1000, 0, -17000, 0)
    SetChrPos(0xF4, 0, 0, -16700, 0)
    SetChrPos(0xF5, 0, 0, -17700, 0)
    SetCameraDistance(18000, 2000)

    def lambda_9F36():
        OP_96(0xFE, 0xFFFFFCE0, 0x0, 0xFFFFDECC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9F36)
    Sleep(50)

    def lambda_9F53():
        OP_96(0xFE, 0x320, 0x0, 0xFFFFDECC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9F53)
    Sleep(50)

    def lambda_9F70():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFDA1C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_9F70)
    Sleep(50)

    def lambda_9F8D():
        OP_96(0xFE, 0xFFFFF95C, 0x0, 0xFFFFD8F0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9F8D)

    def lambda_9FA7():
        OP_96(0xFE, 0x6A4, 0x0, 0xFFFFD8F0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9FA7)

    def lambda_9FC1():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFD5D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_9FC1)
    WaitChrThread(0xF5, 1)
    OP_6F(0x79)
    SetCameraDistance(17000, 30000)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0xC,
        (
            "Hu hu... It's been awhile,\x01",
            "ladies and gentlemen.\x02\x03",
            "However, I don't recall making a\x01",
            "lunch appointment with all of you.\x02\x03",
            "Might you have gotten the\x01",
            "date and time wrong?\x02",
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
        0x101,
        (
            "#00003F#12PSorry for visiting\x01",
            "without an appointment.\x02\x03",
            "#00001F──However, there're circumstances\x01",
            "we cannot overlook.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#N#00206FCancelling the declaration of independence, \x01",
            "the magic soldiers throughout town and other\x01",
            "things, but also...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00307F#12PFirst off, will you\x01",
            "return Keddo to us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5P#11304FOh, I don't mind at all.\x02",
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
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00011F#12PWha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5P#11300FHu hu, it seems you\x01",
            "all misunderstand.\x02\x03",
            "It isn't the case that we are forcing\x01",
            "KeA to cooperate with us, you see.\x02\x03",
            "#11303FExtraordinary difficulties\x01",
            "surround this Crossbell of ours.\x02\x03",
            "#11301FFor that reason, she is cooperating\x01",
            "with us of her own free will.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#N#00208FI wonder...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00106F#12P──You and the others must be\x01",
            "inducing her to cooperate, "uncle".\x02\x03",
            "#00108FManipulating jaegers from the shadows,\x01",
            "causing the attack on Crossbell City,\x01",
            "influencing the independence movement...\x02\x03",
            "#00101FBy freezing Imperial and Republican\x01",
            "assets, you imperiled the continued\x01",
            "existence of the autonomous state.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A60E")

    ChrTalk(
        0x10A,
        (
            "#00606F#12P#N...Regardless of whether your actions are right\x01",
            "or wrong, they can't be forgiven all the same.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A6CB")

    label("loc_A60E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A671")

    ChrTalk(
        0x105,
        (
            "#10404F#12P#NWell, people rarely go to such\x01",
            "extremes to stir up trouble.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A6CB")

    label("loc_A671")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A6CB")

    ChrTalk(
        0x109,
        (
            "#10106F#12P#N...Right or wrong, you can't\x01",
            "be forgiven just the same.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A6CB")

    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A74C")

    ChrTalk(
        0x106,
        (
            "#10708F#12P#NAnd you took that situation\x01",
            "you created, thrusted it at\x01",
            "KeA and forced her decision...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A80E")

    label("loc_A74C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A7B1")

    ChrTalk(
        0x109,
        (
            "#10108F#12P#NAnd you created such\x01",
            "a situation just to\x01",
            "get KeA's consent...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A80E")

    label("loc_A7B1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A80E")

    ChrTalk(
        0x105,
        (
            "#10408F#12P#NAnd you thrusted that\x01",
            "situation at KeA to\x01",
            "get her consent.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A80E")

    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00301F#12PIsn't that a little too dirty for a white-teeth,\x01",
            "attractive middle-aged man such as yourself?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12PPresident Dieter...\x01",
            "No, I should just\x01",
            "call you Mr. Dieter.\x02\x03",
            "#00013FIs this your "justice"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5P#11304FYes── Exactly right.\x02",
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
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    OP_68(0, 1200, 10, 0)
    MoveCamera(57, 7, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15000, 0)
    MoveCamera(37, 11, 0, 50000)
    SetCameraDistance(19000, 50000)
    OP_0D()
    Sleep(150)

    ChrTalk(
        0xC,
        (
            "#5P#11303FIt's not true that the current\x01",
            "political system is worthless.\x02\x03",
            "It just moves too slowly\x01",
            "to get anything done.\x02\x03",
            "#11301FYou all know of the tragedy that\x01",
            "was the Imperial invasion of\x01",
            "Liberl 12 years ago, correct?\x02\x03",
            "And what of those purged in the\x01",
            "democratization of the Republic?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00007F#12P#NW-What's your point!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00108F#12P#NDoes that justify what\x01",
            "all of you are doing...?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xC,
        (
            "#11304FNothing is "justified." Justice is something\x01",
            "that's "done" with power and will.\x02\x03",
            "#11300FThough I am the current head of the Crois clan,\x01",
            "I wasn't all that enthusiastic about my family's\x01",
            "mission at first.\x02\x03",
            "Incidentally, my daughter\x01",
            "knows much more about it.\x02\x03",
            "#11303F──But, once I understood that the new\x01",
            ""Sept-Terrion" my ancestors dreamed of\x01",
            "could actually be realized...\x02\x03",
            "I was ecstatic, and thankful for\x01",
            "having been born into this family.\x02\x03",
            "#11302FFor I have obtained the power to\x01",
            "govern this period of upheaval, and\x01",
            "spread "justice" throughout the land.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F#12P#N"Justice"...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00011F#12P#NThen, you're...\x02\x03",
            "#00006FSo you're doing it neither for yourself\x01",
            "nor out of a desire for control...?\x02\x03",
            "#00010FYou mean to tell me you've gone\x01",
            "this far to bring about "justice"...?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xC,
        (
            "#11309FHa ha. What other\x01",
            "reason would there be?\x02\x03",
            "#11300F10 years ago, when IBC first became\x01",
            "the entity with the most assets on the\x01",
            "continent, I had no need for wealth.\x02\x03",
            "Rule the continent? I have no interest\x01",
            "in such anachronistic fantasies.\x02\x03",
            "#11306FBut I── I could no longer stand it.\x02\x03",
            "Trapped in the framework called "nations",\x01",
            "futile struggles are unfolding in this world.\x02\x03",
            "#11303FIn tha sense, I don't care about the\x01",
            "realization of an "independent state".\x02\x03",
            "And I don't care about the invalidity\x01",
            "Chairman MacDowell declared, either.\x02\x03",
            "#11301F──As long as I widely spread to\x01",
            "the world the ideal "justice"...\x02\x03",
            "#11302FAs long as I guarantee order through that\x01",
            ""justice" and create a peaceful world!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B19D")

    ChrTalk(
        0x10A,
        "#00610F#12P#N...How foolish.\x02",
    )

    CloseMessageWindow()

    label("loc_B19D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B1D3")

    ChrTalk(
        0x105,
        "#10401F#12P#NAre you serious...?\x02",
    )

    CloseMessageWindow()

    label("loc_B1D3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B220")

    ChrTalk(
        0x109,
        (
            "#10106F#12P#NI-It's not that I can't\x01",
            "sympathize, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B220")

    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B275")

    ChrTalk(
        0x106,
        (
            "#10706F#12P#N...For me, what I heard\x01",
            "is just a mere fantasy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B275")

    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00306F#12P#NMan... Until now, I didn't\x01",
            "think you were this serious.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#00208F#12P#N...But, even that illusory "justice"\x01",
            "could be realized to a certain degree...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00106F#12P#NThat's right. If he has KeA,\x01",
            "the "Sept-Terrion of Zero"...\x02\x03",
            "#00108F...He could discard existing political rules and\x01",
            "create any he wanted. I'd have to call it cheating.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00008F#12P#N#30W............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 1100, -5000, 0)
    MoveCamera(147, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16500, 0)
    SetMapObjFlags(0x5, 0x4)
    SetChrPos(0xF4, 500, 0, -9700, 0)
    SetChrPos(0xF5, -500, 0, -10700, 0)
    MoveCamera(151, 13, 0, 30000)
    SetCameraDistance(19000, 30000)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00006F#11P──Mr. Dieter.\x02\x03",
            "I...have learned many\x01",
            "things from you.\x02\x03",
            "#00001FHowever, regarding  your "justice"... \x01",
            "It seems I overvalued it a little.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xC,
        "#6P#11301F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008FEach of us are police officers. Furthermore,\x01",
            "we're assigned to the Special Support Section.\x02\x03",
            "#00003FWe embody "justice"  by supporting the\x01",
            "citizens while following our laws and rules.\x02\x03",
            "#00001FHowever... We're not always\x01",
            "right. We've lost our way\x01",
            "many times, actually.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B6E8")

    ChrTalk(
        0x10A,
        (
            "#11P#00603F...Naturally. Maintaining\x01",
            "order and security isn't\x01",
            "always the right answer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B6E8")


    ChrTalk(
        0x102,
        (
            "#11P#00106F...That's right. Our\x01",
            "positions on how "justice"\x01",
            "should be are very different.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#00204FThough we lose our way and make mistakes\x01",
            "sometimes, pursue "justice"...\x02\x03",
            "#00202FThat is something you once\x01",
            "told us too, Mr. Dieter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00302FIsn't what you're doin' totally different\x01",
            "from the lecture you gave us back then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#11303F...That's a methodology\x01",
            "to follow when one's power\x01",
            "and will are insufficient.\x02\x03",
            "But once one has those, to\x01",
            "not bring about "justice"...\x02\x03",
            "#11301FIsn't that "laziness"?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#00013F#4S#11P──No!\x02",
    )

    CloseMessageWindow()

    def lambda_B924():
        OP_96(0xFE, 0xFFFFFCE0, 0x0, 0xFFFFE2B4, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B924)
    WaitChrThread(0x101, 1)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#00003F#11P"Justice" changes easily\x01",
            "and has no definite form...!\x02\x03",
            "And the pursuit of it\x01",
            "has value to everyone...!\x02\x03",
            "#00007FYou're trying to turn "justice"\x01",
            "into a standardized mold,\x01",
            "and force it to everyone...!\x02\x03",
            "Is that sort of thing really\x01",
            "the "justice" you seek!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#11310FUgh...\x02\x03",
            "#11307FActually, I've breathed new life\x01",
            "into the Crossbell political system\x01",
            "and implemented several reforms!\x02\x03",
            "Do you deny those results!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00106F...That's a different matter.\x02\x03",
            "#00108FWe don't intend to deny your\x01",
            "accomplishments. Actually,\x01",
            "we learned a lot from you.\x02\x03",
            "#00101FThat's why... We must point out\x01",
            "your deceit and misunderstandings.\x02\x03",
            "#00107FAs someone I respect... I want you\x01",
            "to understand your own failings!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0xC,
        "#6P#11302F#4SVery well!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 1100, 2000, 0)
    MoveCamera(0, 9, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15000, 0)
    ClearMapObjFlags(0x5, 0x4)
    SetChrPos(0xF4, -500, 0, -9700, 0)
    SetChrPos(0xF5, 500, 0, -10700, 0)
    OP_0D()
    Sleep(150)
    Sound(802, 0, 100, 0)
    SetChrSubChip(0xC, 0x1)
    Sleep(70)
    SetChrSubChip(0xC, 0x2)
    OP_68(0, 1100, -4000, 1500)
    MoveCamera(0, 21, 0, 1500)
    SetCameraDistance(27000, 1500)
    OP_6F(0x79)
    Fade(500)
    BeginChrThread(0x32, 1, 0, 66)
    SetMapObjFrame(0xFF, "futa03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "03_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "futa00", 0x2, "move")
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_BD97():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_BD97)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_BDBC():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_BDBC)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#00005F...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00307F#6P#NW-What!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(10, 1300, 0, 0)
    MoveCamera(0, 25, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16500, 0)
    OP_93(0x103, 0x0, 0x0)
    OP_93(0x104, 0x0, 0x0)
    MoveCamera(45, 13, 0, 10000)
    SetCameraDistance(13500, 10000)
    OP_0D()
    SetMessageWindowPos(250, 250, -1, -1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BEC8")

    AnonymousTalk(
        0x105,
        (
            "#10407FThis is...\x01",
            ""Orbal" energy!?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BF4E")

    label("loc_BEC8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BF05")

    AnonymousTalk(
        0x106,
        (
            "#10707FThis is...\x01",
            ""Orbal" energy!?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BF4E")

    label("loc_BF05")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BF4E")

    AnonymousTalk(
        0x109,
        (
            "#10107FAn Orbal Art... \x01",
            "──No, this is different!?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BF4E")

    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(0, 250, -1, -1)

    AnonymousTalk(
        0x103,
        (
            "#00201FPlease be careful!\x02\x03",
            "Vast spiritual energy is\x01",
            "gathering at the center\x01",
            "of Orchis Tower...!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(500)

    ChrTalk(
        0xC,
        (
            "#11304FHehe, I'm not on the level of Bell,\x01",
            "but as head of the Crois clan,\x01",
            "I can do at least this much...\x02\x03",
            "#11300FAnd, if I use the "Spiritual Conversion \x01",
            "Function" of Orchis Tower──\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0xC,
        "#11307F#4S#12AThen I can even do this!\x02",
    )

    CloseMessageWindow()
    OP_6F(0x79)
    Sound(950, 2, 40, 0)
    Sound(935, 0, 100, 0)
    PlayEffect(0x1, 0x1, 0xC, 0x5, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_C115():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_C115)
    StopEffect(0x0, 0x2)
    WaitChrThread(0xC, 2)
    OP_68(0, 4000, 5000, 3000)
    SetChrFlags(0xC, 0x20)

    def lambda_C143():
        OP_96(0xFE, 0x0, 0xFA0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_C143)
    WaitChrThread(0xC, 1)
    StopEffect(0x1, 0x2)
    Sound(930, 0, 100, 0)
    StopSound(933, 1000, 100)
    StopSound(950, 1000, 40)
    OP_6F(0x79)
    Sleep(1500)
    StopSound(927, 1000, 100)

    ChrTalk(
        0x102,
        "#00105FAh...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C1C9")

    ChrTalk(
        0x10A,
        "#00605FHe was sucked inside...!?\x02",
    )

    CloseMessageWindow()
    Jump("loc_C238")

    label("loc_C1C9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C202")

    ChrTalk(
        0x109,
        "#10111FH-He was sucked in...!?\x02",
    )

    CloseMessageWindow()
    Jump("loc_C238")

    label("loc_C202")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C238")

    ChrTalk(
        0x106,
        "#10712FHe was sucked inside...!?\x02",
    )

    CloseMessageWindow()

    label("loc_C238")

    OP_68(0, 4000, 5000, 6000)
    MoveCamera(0, -5, 0, 6000)
    SetCameraDistance(12500, 6000)
    Sound(140, 0, 100, 0)
    Sound(859, 0, 50, 0)
    OP_71(0x5, 0x406, 0x42E, 0x0, 0x20)
    Sleep(1000)
    BeginChrThread(0x28, 3, 0, 63)
    Sleep(2000)
    OP_6F(0x79)
    Sound(955, 0, 100, 0)
    SetMessageWindowPos(-1, 140, -1, -1)
    SetChrName("Man's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30WMmm... Vision and control nominal.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30WWith the power of the "Sept-Terrion",\x01",
            "it seems I'm able to control it at will.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    WaitChrThread(0x28, 3)
    StopBGM(0xBB8)
    OP_68(0, 2500, -7500, 2500)
    MoveCamera(0, 5, 0, 2500)
    SetCameraDistance(11000, 2500)
    Sleep(2000)

    def lambda_C36B():
        OP_97(0x101, 0x0, 0x0, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_C36B)
    Sleep(50)

    def lambda_C388():
        OP_97(0x102, 0x0, 0x0, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_C388)
    Sleep(50)

    def lambda_C3A5():
        OP_97(0x103, 0x0, 0x0, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_C3A5)
    Sleep(50)

    def lambda_C3C2():
        OP_97(0x104, 0x0, 0x0, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_C3C2)
    Sleep(50)

    def lambda_C3DF():
        OP_97(0xF4, 0x0, 0x0, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_C3DF)
    Sleep(50)

    def lambda_C3FC():
        OP_97(0xF5, 0x0, 0x0, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_C3FC)
    OP_6F(0x79)
    WaitChrThread(0xF5, 0)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00107F#12P#N"U-Uncle"...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    NpcTalk(
        0x101,
        "Tio",
        (
            "#00207F#6P#NHe's controlling an archaism\x01",
            "from the spiritual plane...?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        "#00310F#12P#NWhoa, is that even possible!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7554", 0)
    Fade(250)
    OP_68(0, 4000, 5000, 0)
    MoveCamera(0, 5, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x101, -800, 0, -5500, 0)
    SetChrPos(0x102, 800, 0, -5500, 0)
    SetChrPos(0x103, -1700, 0, -7000, 0)
    SetChrPos(0x104, 1700, 0, -7000, 0)
    SetChrPos(0xF4, 0, 0, -6700, 0)
    SetChrPos(0xF5, 0, 0, -7800, 0)
    SetCameraDistance(14500, 1000)
    OP_0D()
    OP_71(0x5, 0x492, 0x4BA, 0x0, 0x0)
    Sleep(200)
    Sound(905, 0, 100, 0)
    OP_79(0x5)
    OP_71(0x5, 0x4BA, 0x4CE, 0x0, 0x20)
    Sound(951, 0, 100, 0)
    Sleep(100)
    Sound(833, 0, 100, 0)
    Sound(859, 0, 100, 0)
    OP_6F(0x79)
    OP_68(0, 2000, -1000, 12000)
    MoveCamera(35, 5, 0, 12000)
    SetCameraDistance(17000, 12000)
    Sleep(1000)
    Sound(955, 0, 100, 0)
    SetMessageWindowPos(-1, 100, -1, -1)
    SetChrName("Dieter's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#18AHa ha, this is the very embodiment of "justice",\x01",
            "a white machine to make it known to the world...\x02",
        )
    )

    CloseMessageWindow()
    Sound(905, 0, 100, 0)
    OP_71(0x5, 0x4CE, 0x4E2, 0x0, 0x0)
    OP_79(0x5)
    Sound(951, 0, 100, 0)
    OP_71(0x5, 0x335, 0x348, 0x0, 0x0)
    OP_79(0x5)
    OP_71(0x5, 0x349, 0x352, 0x0, 0x20)
    Sound(833, 0, 100, 0)
    Sleep(800)
    Sound(955, 0, 100, 0)
    SetMessageWindowPos(-1, 100, -1, -1)
    SetChrName("Dieter's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#16ACome── \x01",
            "I shall "prove" it to you.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sleep(500)
    SetMessageWindowPos(-1, 100, -1, -1)
    SetChrName("Dieter's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#20AMy "justice" and your "justice"...\x01",
            "I'll show you which of them is correct!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_6F(0x79)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x21)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0x23)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0x24)
    SetChrSubChip(0xF5, 0x0)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C7C4")
    Sound(540, 0, 50, 0)

    label("loc_C7C4")

    OP_0D()
    Sleep(300)

    ChrTalk(
        0x101,
        "#00010F#12P#NUgh... Bring it on!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00107F#12P#NWe'll challenge you\x01",
            "with our full strength...!\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0x3B6)
    OP_24(0x39F)
    OP_24(0x3A5)
    OP_24(0x3AF)
    Battle("BattleInfo_7B4", 0x30200011, 0x0, 0x100, 0x11, 0xFF)
    FadeToDark(0, 0, -1)
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 67)
    Return()

    # Function_62_9B2E end

    def Function_63_C860(): pass

    label("Function_63_C860")

    OP_71(0x5, 0x442, 0x492, 0x0, 0x0)
    Sleep(200)
    Sound(905, 0, 100, 0)
    Sleep(1000)
    Sound(905, 0, 100, 0)
    OP_79(0x5)
    OP_71(0x5, 0x406, 0x42E, 0x0, 0x20)
    Return()

    # Function_63_C860 end

    def Function_64_C88E(): pass

    label("Function_64_C88E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C8A6")
    LoadChrToIndex("chr/ch03150.itc", 0x23)

    label("loc_C8A6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C8BE")
    LoadChrToIndex("chr/ch03250.itc", 0x23)

    label("loc_C8BE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C8D6")
    LoadChrToIndex("chr/ch02950.itc", 0x23)

    label("loc_C8D6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C8EE")
    LoadChrToIndex("chr/ch00950.itc", 0x23)

    label("loc_C8EE")

    Return()

    # Function_64_C88E end

    def Function_65_C8EF(): pass

    label("Function_65_C8EF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C907")
    LoadChrToIndex("chr/ch03150.itc", 0x24)

    label("loc_C907")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C91F")
    LoadChrToIndex("chr/ch03250.itc", 0x24)

    label("loc_C91F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C937")
    LoadChrToIndex("chr/ch02950.itc", 0x24)

    label("loc_C937")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C94F")
    LoadChrToIndex("chr/ch00950.itc", 0x24)

    label("loc_C94F")

    Return()

    # Function_65_C8EF end

    def Function_66_C950(): pass

    label("Function_66_C950")

    Sound(922, 0, 100, 0)
    Sound(927, 2, 100, 0)
    Sound(933, 2, 100, 0)
    Sound(943, 2, 100, 0)
    Sleep(1000)
    OP_24(0x3AF)
    Sound(143, 0, 50, 0)
    Return()

    # Function_66_C950 end

    def Function_67_C975(): pass

    label("Function_67_C975")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51769.itc", 0x1E)
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00250.itc", 0x21)
    LoadChrToIndex("chr/ch00350.itc", 0x22)
    Call(0, 64)
    Call(0, 65)
    LoadEffect(0x0, "event/ev17052.eff")
    LoadEffect(0x1, "event/ev17051.eff")
    SoundLoad(933)
    SoundLoad(927)
    SoundLoad(943)
    SoundLoad(950)
    SoundLoad(579)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xC, 0x2)
    SetChrFlags(0xC, 0x20)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x5)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 0, 2000, 5500, 180)
    OP_8E(0xC, "President Dieter")
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x21)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0x23)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0x24)
    SetChrSubChip(0xF5, 0x0)
    SetChrPos(0x101, -800, 0, -5500, 0)
    SetChrPos(0x102, 800, 0, -5500, 0)
    SetChrPos(0x103, -1700, 0, -7000, 0)
    SetChrPos(0x104, 1700, 0, -7000, 0)
    SetChrPos(0xF4, 0, 0, -6700, 0)
    SetChrPos(0xF5, 0, 0, -7800, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x28, 0x8000)
    OP_78(0x5, 0x28)
    SetChrPos(0x28, 0, 0, 6500, 180)
    OP_D5(0x28, 0x0, 0x2BF20, 0x0, 0x0)
    SetMapObjFlags(0x5, 0x1000)
    OP_74(0x5, 0x1E)
    OP_70(0x5, 0x3A2)
    SetChrFlags(0x28, 0x1)
    OP_52(0x28, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapObjFlags(0x18, 0x4)
    SetMapObjFlags(0x18, 0x1000)
    SetMapObjFrame(0xFF, "futa03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "03_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "futa00", 0x2, "open")
    OP_68(0, 3500, -1000, 0)
    MoveCamera(35, 5, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(17000, 0)
    BeginChrThread(0x32, 1, 0, 69)
    OP_68(0, 1500, -1000, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00000F#12PD-Did we do it...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300F#12PWith this, somehow...!\x02",
    )

    CloseMessageWindow()
    PlayBGM("ed7554", 0)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 0, 0, 6500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(930, 0, 80, 0)
    Sound(933, 2, 100, 0)
    Sound(927, 2, 100, 0)
    EndChrThread(0x32, 0x1)
    Sleep(1000)
    SetMapObjFlags(0x18, 0x4)
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
        0x103,
        (
            "#00207F#12PSpiritual energy is\x01",
            "rising once again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00110F#12PNo way...!\x02",
    )

    CloseMessageWindow()
    OP_68(0, 2000, -1000, 2000)
    Sound(905, 0, 100, 0)
    OP_74(0x5, 0xF)
    OP_71(0x5, 0x3A3, 0x3CA, 0x0, 0x0)
    Sleep(2000)
    Sound(902, 0, 70, 0)
    OP_79(0x5)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0xB, 0x32, 0x0, 0x20)
    Sound(951, 0, 100, 0)
    OP_6F(0x79)
    Sleep(800)
    Sound(955, 0, 100, 0)
    SetMessageWindowPos(10, 70, -1, -1)
    SetChrName("Dieter's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30WHehe, thanks to the "Sept-Terrion of Zero",\x01",
            "this machine has been granted limitless energy.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30WUnless completely destroyed,\x01",
            "defeating it is impossible.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00010F#12P#NUgh...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CECC")

    ChrTalk(
        0x10A,
        "#00610F#12P#NSo that's how it is, eh...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_CECC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CF07")

    ChrTalk(
        0x105,
        "#10410F#12P#NThis is too unfair...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_CF07")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CF4C")

    ChrTalk(
        0x109,
        "#10110F#12P#NGuh... There has to be a way...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_CF4C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CF91")

    ChrTalk(
        0x106,
        "#10708F#12P#N(...We must find its weakness!)\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_CF91")

    Sleep(500)
    Sound(955, 0, 100, 0)
    SetMessageWindowPos(10, 70, -1, -1)
    SetChrName("Dieter's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30WHehe, I don't intend\x01",
            "to take your lives.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30WIf you surrender peacefully, and\x01",
            "cooperate with my ideals──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    StopBGM(0xFA0)
    Sound(954, 0, 100, 0)
    Sound(922, 0, 100, 0)
    StopSound(933, 1000, 100)
    StopSound(927, 1000, 100)
    Fade(250)
    ClearMapObjFlags(0x5, 0x20)
    OP_70(0x5, 0xB)
    OP_0D()
    StopEffect(0x0, 0x2)
    Sleep(1500)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(10, 70, -1, -1)
    SetChrName("Dieter's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#4S!?\x02",
        )
    )

    CloseMessageWindow()
    Sound(955, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "W-What...!?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(500)
    OP_70(0x14, 0xB)
    Fade(1000)
    SetMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x14, 0x4)
    Sleep(1500)

    ChrTalk(
        0x104,
        "#00301F#12P#NW-What happened?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#00205F#12P#NThe supply of spiritual\x01",
            "energy has ceased...?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_71(0x14, 0x564, 0x58C, 0x0, 0x0)
    Sound(905, 0, 100, 0)
    Sound(954, 0, 100, 0)
    OP_79(0x14)
    Sound(902, 0, 100, 0)
    OP_68(0, 1000, -1000, 2000)
    MoveCamera(35, 19, 0, 2000)
    SetCameraDistance(35000, 2000)
    Sleep(1500)
    Fade(500)
    BeginChrThread(0x32, 1, 0, 68)
    Sound(927, 2, 100, 0)
    SetMapObjFrame(0xFF, "futa03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "03_add", 0x0, 0x1)
    OP_0D()
    SetMapObjFrame(0xFF, "futa00", 0x2, "move2")
    Sleep(1300)
    Fade(500)
    OP_68(50000, -4500, -50000, 0)
    MoveCamera(340, 21, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(50000, 0)
    OP_68(0, -4500, -10000, 9000)
    MoveCamera(0, 33, 0, 9000)
    SetCameraDistance(115000, 9000)
    OP_71(0x1, 0x12C, 0x0, 0x0, 0x0)
    OP_71(0x2, 0x12C, 0x0, 0x0, 0x0)
    OP_71(0x3, 0x12C, 0x0, 0x0, 0x0)
    OP_71(0x4, 0x12C, 0x0, 0x0, 0x0)
    Sleep(2000)
    Sound(579, 2, 30, 0)
    OP_79(0x1)
    OP_79(0x2)
    OP_79(0x3)
    OP_79(0x4)
    StopSound(927, 500, 100)
    StopSound(579, 500, 20)
    Sound(954, 0, 100, 0)
    Sound(143, 0, 30, 0)
    SetMapObjFrame(0xFF, "futa01", 0x2, "move2")
    OP_6F(0x79)
    Fade(500)
    SetMapObjFrame(0xFF, "futa02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "window01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "02_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "back00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "back01_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "back02_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "a_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "b_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "c_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "d_add", 0x0, 0x1)
    Sleep(1500)
    Fade(500)
    OP_68(0, 2000, 5500, 0)
    MoveCamera(25, 11, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    OP_0D()
    OP_68(0, 2000, 3500, 3500)
    MoveCamera(35, 11, 0, 3500)
    SetCameraDistance(17000, 3500)
    Sound(930, 0, 100, 0)
    Sound(950, 2, 40, 0)
    Sound(933, 2, 100, 0)
    PlayEffect(0x1, 0x1, 0xC, 0x5, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_D3E9():
        OP_96(0xFE, 0x0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_D3E9)
    WaitChrThread(0xC, 1)

    def lambda_D407():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_D407)
    WaitChrThread(0xC, 2)
    StopEffect(0x1, 0x2)
    StopSound(950, 1000, 30)
    StopSound(933, 1000, 100)
    Sound(935, 0, 100, 0)
    OP_6F(0x79)
    Sleep(800)

    ChrTalk(
        0xC,
        "#11310F#5PT-This cannot be...!\x02",
    )

    CloseMessageWindow()
    StopSound(132, 1000, 40)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x3A5)
    OP_24(0x39F)
    OP_24(0x3B6)
    OP_24(0x243)
    OP_24(0x3AF)
    SetScenarioFlags(0x24, 1)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_67_C975 end

    def Function_68_D48C(): pass

    label("Function_68_D48C")

    Sound(943, 2, 50, 0)
    Sleep(1500)
    OP_24(0x3AF)
    Sound(143, 0, 60, 0)
    Return()

    # Function_68_D48C end

    def Function_69_D49F(): pass

    label("Function_69_D49F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D4D3")
    Sound(203, 0, 50, 0)
    Sleep(900)
    Sound(203, 0, 60, 0)
    Sleep(1100)
    Sound(203, 0, 50, 0)
    Sleep(800)
    Sound(203, 0, 40, 0)
    Sleep(1000)
    Jump("Function_69_D49F")

    label("loc_D4D3")

    Return()

    # Function_69_D49F end

    def Function_70_D4D4(): pass

    label("Function_70_D4D4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrChipPat(0x4, 0x1, 0x1F)
    SetChrChipPat(0x5, 0x1, 0x20)
    ClearScenarioFlags(0x0, 0)
    ClearScenarioFlags(0x0, 1)
    ClearScenarioFlags(0x0, 2)
    ClearScenarioFlags(0x0, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D512")
    AddParty(0x8, 0xFF, 0xFF)
    SetScenarioFlags(0x0, 0)

    label("loc_D512")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D52A")
    AddParty(0x4, 0xFF, 0xFF)
    SetScenarioFlags(0x0, 1)

    label("loc_D52A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D542")
    AddParty(0x5, 0xFF, 0xFF)
    SetScenarioFlags(0x0, 2)

    label("loc_D542")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D55A")
    AddParty(0x9, 0xFF, 0xFF)
    SetScenarioFlags(0x0, 3)

    label("loc_D55A")

    LoadChrToIndex("chr/ch05620.itc", 0x1E)
    LoadChrToIndex("chr/ch13400.itc", 0x1F)
    LoadChrToIndex("chr/ch02500.itc", 0x20)
    LoadChrToIndex("apl/ch51732.itc", 0x21)
    LoadChrToIndex("apl/ch51113.itc", 0x22)
    LoadChrToIndex("apl/ch51734.itc", 0x23)
    LoadEffect(0x0, "event/ev10000.eff")
    LoadEffect(0x1, "event/ev10001.eff")
    LoadEffect(0x2, "event/ev17054.eff")
    SoundLoad(3787)
    SoundLoad(112)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04700.itp")
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 0, 0, 0, 0)
    OP_8E(0xC, "President Dieter")
    SetChrChipByIndex(0x13, 0x1F)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 10000, 0, 1500, 270)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x15, 0x20)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x101, -800, 0, -5500, 0)
    SetChrPos(0x102, 800, 0, -5500, 0)
    SetChrPos(0x103, -1700, 0, -7000, 0)
    SetChrPos(0x104, 1700, 0, -7000, 0)
    SetChrPos(0xF4, 100, 0, -6700, 0)
    SetChrPos(0xF5, -100, 0, -7800, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x28, 0x8000)
    OP_78(0x5, 0x28)
    SetChrPos(0x28, 0, 0, 6500, 180)
    OP_D5(0x28, 0x0, 0x2BF20, 0x0, 0x0)
    SetMapObjFlags(0x5, 0x1000)
    SetMapObjFlags(0x14, 0x4)
    OP_74(0x5, 0x1E)
    OP_70(0x5, 0x58C)
    SetChrFlags(0x28, 0x1)
    OP_52(0x28, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x29, 0x80)
    SetChrFlags(0x29, 0x8000)
    OP_78(0x14, 0x29)
    SetChrPos(0x29, 0, 0, 6500, 180)
    OP_D5(0x29, 0x0, 0x2BF20, 0x0, 0x0)
    SetMapObjFlags(0x14, 0x1000)
    ClearMapObjFlags(0x14, 0x4)
    OP_74(0x14, 0x1E)
    OP_70(0x14, 0x58C)
    SetChrFlags(0x28, 0x1)
    OP_52(0x28, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "sky00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kumo01a", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "back01_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "back02_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "a_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "b_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "c_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "d_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "02_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "03_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "futa02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "futa03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "window01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "futa00", 0x2, "close")
    SetMapObjFrame(0xFF, "futa01", 0x2, "close")
    OP_70(0x1, 0x0)
    OP_70(0x2, 0x0)
    OP_70(0x3, 0x0)
    OP_70(0x4, 0x0)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0x2E, 0x80)
    ClearChrFlags(0x2F, 0x80)
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x31, 0x80)
    OP_78(0xD, 0x2C)
    OP_78(0xE, 0x2D)
    OP_78(0xF, 0x2E)
    OP_78(0x10, 0x2F)
    OP_78(0x11, 0x30)
    OP_78(0x12, 0x31)
    OP_49()
    SetChrPos(0x2C, 15000, 6000, -3000, 0)
    SetChrPos(0x2D, 15100, 7000, -7500, 0)
    SetChrPos(0x2E, 15100, 7000, 1500, 0)
    SetChrPos(0x2F, 15200, 5000, 5000, 0)
    SetChrPos(0x30, 15200, 5000, -11000, 0)
    SetChrPos(0x31, 15000, 6000, -3000, 0)
    OP_D5(0x2C, 0x0, 0x15F90, 0x0, 0x0)
    OP_D5(0x2D, 0x0, 0x15F90, 0x0, 0x0)
    OP_D5(0x2E, 0x0, 0x15F90, 0x0, 0x0)
    OP_D5(0x2F, 0x0, 0x15F90, 0x0, 0x0)
    OP_D5(0x30, 0x0, 0x15F90, 0x0, 0x0)
    OP_D5(0x31, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0xE, 0x4)
    ClearMapObjFlags(0xF, 0x4)
    ClearMapObjFlags(0x10, 0x4)
    ClearMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0xD, 0x1000)
    SetMapObjFlags(0xE, 0x1000)
    SetMapObjFlags(0xF, 0x1000)
    SetMapObjFlags(0x10, 0x1000)
    SetMapObjFlags(0x11, 0x1000)
    SetMapObjFlags(0x12, 0x1000)
    OP_FF(0xD, 0x168, 0x168, 0x168)
    OP_FF(0xE, 0x140, 0x140, 0x140)
    OP_FF(0xF, 0x140, 0x140, 0x140)
    OP_FF(0x10, 0x140, 0x140, 0x140)
    OP_FF(0x11, 0x140, 0x140, 0x140)
    OP_FF(0x12, 0x17C, 0x17C, 0x17C)
    ClearChrFlags(0x2B, 0x80)
    OP_78(0x15, 0x2B)
    OP_49()
    SetChrPos(0x2B, 0, 15000, 6000, 180)
    OP_D5(0x2B, 0x1388, 0x2BF20, 0x0, 0x0)
    SetMapObjFlags(0x15, 0x4)
    SetMapObjFlags(0x15, 0x1000)
    OP_74(0x15, 0x1E)
    OP_71(0x15, 0x1, 0x78, 0x0, 0x20)
    ClearChrFlags(0x18, 0x80)
    OP_78(0x17, 0x18)
    OP_49()
    SetChrPos(0x18, 0, 15000, 6000, 180)
    OP_D5(0x18, 0x1388, 0x2BF20, 0x0, 0x0)
    SetMapObjFlags(0x17, 0x4)
    SetMapObjFlags(0x17, 0x1000)
    OP_68(210, 2500, 5500, 0)
    MoveCamera(35, 11, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(18050, 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(210, 1500, 5500, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0xC,
        (
            "#12P#11307FW-What is the meaning of this!?\x02\x03",
            "Why did the supply from the\x01",
            ""Sept-Terrion" suddenly stopped...!?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(240, 40, -1, -1)
    SetChrName("Ominous Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Well, my time for pointless things\x01",
            "has come to an end, I'd say.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7580", 0)
    SetChrFlags(0x102, 0x8)
    OP_68(10000, 1000, 1500, 2000)
    SetCameraDistance(14000, 2000)
    TurnDirection(0xC, 0x13, 500)
    TurnDirection(0x101, 0x13, 0)
    TurnDirection(0x102, 0x13, 0)
    TurnDirection(0x103, 0x13, 0)
    TurnDirection(0x104, 0x13, 0)
    TurnDirection(0xF4, 0x13, 0)
    TurnDirection(0xF5, 0x13, 0)
    OP_6F(0x79)
    ClearChrFlags(0x102, 0x8)
    SetCameraDistance(13000, 2000)
    Sound(223, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 10000, 0, 1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    Sound(936, 0, 100, 0)
    ClearChrFlags(0x13, 0x80)

    def lambda_DCF9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_DCF9)
    WaitChrThread(0x13, 2)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00013FFrom the "Society"...!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DD7C")

    ChrTalk(
        0x105,
        (
            "#10407FIt's F. Novartis, of the\x01",
            ""Thirteen Workshops"...!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DD99")

    label("loc_DD7C")


    ChrTalk(
        0x103,
        "#00207FDr. Novartis...!\x02",
    )

    CloseMessageWindow()

    label("loc_DD99")

    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(5960, 1000, 1210, 0)
    MoveCamera(55, 11, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(20000, 0)
    OP_0D()
    Sleep(150)

    ChrTalk(
        0xC,
        (
            "#6P#11310FDr. Novartis... \x01",
            "What ever do you mean!?\x02\x03",
            "Could the "Society" have installed\x01",
            "some sort of trap in this machine!?\x02",
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
        0x13,
        (
            "Hu hu, I said it last time. In the\x01",
            "end, we were only assisting you.\x02\x03",
            "I've gotten some good data already,\x01",
            "so I'll be taking my leave soon.\x02\x03",
            "And with that final model there,\x01",
            "as per contract.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    Sleep(200)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xC,
        (
            "#6P#11307FContract...!?\x02\x03",
            "It can't be! I bought this\x01",
            "machine from the "Society"!\x02\x03",
            "You have no right to take it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#11P#04704FNo, no. You see, the contract\x01",
            "content changed just a bit.\x02\x03",
            "Once the machine's served\x01",
            "its purpose, we'll\x01",
            "collect it. See to that.\x02\x03",
            "#04702F──It's from your daughter,\x01",
            "Miss Mariabell Crois.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#6P#11305FWha...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xFA0)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(260, 10, -1, -1)
    SetChrName("Girl's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#3787V#30W#30AUhuhu... Exactly right.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#5P#00011F#6P#NT-This voice is...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#00107FBell#6P#N...!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7572", 0)
    Fade(500)
    OP_68(15000, 5500, -3000, 0)
    MoveCamera(62, 0, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(14000, 0)
    OP_93(0xC, 0x5A, 0x0)
    OP_93(0x101, 0x5A, 0x0)
    OP_93(0x102, 0x5A, 0x0)
    OP_93(0x103, 0x5A, 0x0)
    OP_93(0x104, 0x5A, 0x0)
    OP_93(0xF4, 0x5A, 0x0)
    OP_93(0xF5, 0x5A, 0x0)
    SetCameraDistance(16000, 3000)
    Sleep(500)
    Sound(922, 0, 100, 0)
    BeginChrThread(0x2C, 3, 0, 79)
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0xC,
        (
            "#11310F#6P#NBell... What in the world...?\x02\x03",
            "#11307FAnd, just where are you!?\x02\x03",
            "You're not in Orchis Tower!?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, 160, -1, -1)

    AnonymousTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Uh uh, I haven't been\x01",
            "there in quite some time.\x02\x03",
            "I am with Miss KeA and the others.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00005F#6P#NWhat...!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00101F#6P#NI-It's true they weren't\x01",
            "on any of the floors...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    MoveCamera(57, -5, 0, 3000)
    SetCameraDistance(19500, 3000)
    Sound(922, 0, 100, 0)
    BeginChrThread(0x2D, 3, 0, 80)
    Sleep(500)
    Sound(922, 0, 100, 0)
    BeginChrThread(0x2E, 3, 0, 81)
    Sleep(500)
    Sound(922, 0, 100, 0)
    BeginChrThread(0x2F, 3, 0, 82)
    Sleep(500)
    Sound(922, 0, 100, 0)
    BeginChrThread(0x30, 3, 0, 83)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00007F#6P#NMr. Arios...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E4C0")

    ChrTalk(
        0x10A,
        "#00610F#6P#NMacLaine...!\x02",
    )

    CloseMessageWindow()

    label("loc_E4C0")


    ChrTalk(
        0x104,
        (
            "#00307F#6P#NUncle...!\x01",
            "Shirley...!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E51D")

    ChrTalk(
        0x106,
        "#10701F#6P#N"Bloody Shirley"...!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_E51D")


    ChrTalk(
        0x103,
        "#00201F#6P#NAnd even Mr. Wald...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E582")

    ChrTalk(
        0x105,
        "#10401F#6P#NSo he really was with them...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_E582")

    Sleep(150)
    SetMessageWindowPos(240, 110, -1, -1)
    SetChrName("Arios")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "............\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(120, 120, -1, -1)

    AnonymousTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Hehe...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(30, 160, -1, -1)

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Wow! \x01",
            "Now I'm excited!!!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(370, 160, -1, -1)

    AnonymousTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Tch...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0xC,
        (
            "#11310F#6P#NW-What is the meaning of this...\x02\x03",
            "#11307FDid you all... \x01",
            "betray me!?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 110, -1, -1)
    SetChrName("Arios")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "...I do apologize, President.\x02\x03",
            "However, I wasn't collaborating\x01",
            "with your plan from the very start.\x02\x03",
            "I have been collaborating with the \x01",
            ""lawyer" and Miss Mariabell's plan.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0xC,
        (
            "#11305F#30W#6P#N"Lawyer"...\x02\x03",
            "#11310FNo... It can't be...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Man's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Yes── Exactly right.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(250)
    OP_68(15000, 5500, -3000, 0)
    MoveCamera(90, 10, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(14500, 0)
    OP_FF(0xD, 0x140, 0x140, 0x140)
    SetChrPos(0x2C, 15100, 5000, -7000, 0)
    SetChrPos(0x2D, 15200, 7500, -10000, 0)
    SetChrPos(0x30, 15300, 4000, -12000, 0)
    SetChrPos(0x2E, 15100, 7500, 2000, 0)
    SetChrPos(0x2F, 15200, 4000, 4000, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_0D()
    Sound(922, 0, 100, 0)
    BeginChrThread(0x31, 3, 0, 84)
    Sleep(500)
    CancelBlur(1000)
    SetCameraDistance(17500, 1000)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E8CD")
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#00007F#4S#12P#N......!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_E8CD")


    ChrTalk(
        0x102,
        "#00105F#12P#N...Ah...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        "#00205F#12P#N...Eh...?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        "#00305F#12P#N...N-No way...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E95F")

    ChrTalk(
        0x10A,
        "#00605F#12P#NL-Lawyer Ian...!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_E95F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E98F")

    ChrTalk(
        0x109,
        "#10111F#12P#NI-It can't be...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_E98F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E9D2")

    ChrTalk(
        0x105,
        "#10410F#12P#NTo think...it would come to this...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_E9D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 0)), scpexpr(EXPR_END)), "loc_EBC1")

    ChrTalk(
        0x101,
        "#00013F#12P#N......... \x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("Lawyer Ian")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Hmm. From what I see, could\x01",
            "it be that you had realized\x01",
            "my involvement, Lloyd...?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#00006F#12P#N...Yes. I got hints\x01",
            "from Mr. Nielsen,\x01",
            "a reporter.\x02\x03",
            "#00008FAnd Pete, and the old gravekeeper...\x01",
            "From what Miss Kilika and Mr. Lechter said...\x02\x03",
            "#00013FAll of the fragments finally\x01",
            "pointed to your involvement.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("Lawyer Ian")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Uh uh. Looks like you've finally\x01",
            "caught up with Guy, eh?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_EBC1")

    Fade(500)
    OP_68(8000, 3000, -3000, 0)
    MoveCamera(50, 3, 0, 0)
    SetCameraDistance(23000, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "#6P#11310F#NMr. Grimwood... \x01",
            "What is the meaning of this...!?\x02\x03",
            "I-It's true you gave me advice\x01",
            "on various things, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(190, 100, -1, -1)
    SetChrName("Lawyer Ian")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Yes... Teaching you as a\x01",
            "student paid off big time.\x02\x03",
            "You were an elite-class manager, and as\x01",
            "a politician, you weren't too bad, either.\x02\x03",
            "If only your fatal flaw could be removed...\x01",
            "You're too much of a dreamer.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(50)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0xC,
        "#6P#11305F#N......!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(270, 110, -1, -1)

    AnonymousTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Uh uh, you thought\x01",
            "everything was going\x01",
            "according to your plan, but...\x02\x03",
            "Actually, it was all just a\x01",
            "scenario created by Mr. Grimwood.\x02\x03",
            "The manipulation of the Cult, the Trade Conference \x01",
            "agenda, the attack on Crossbell City, and even the \x01",
            "declaration of independence...\x02\x03",
            "I wonder who first put those ideas\x01",
            "into your head, father?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0xC,
        "#6P#11310F#30W#N...Ah....\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(190, 100, -1, -1)
    SetChrName("Lawyer Ian")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "If you had kept doing well, I would've\x01",
            "never revealed my true colors, but...\x02\x03",
            "It seems I must bring your days\x01",
            "as the mastermind to an end.\x02\x03",
            "I shall continue the "Azure-\x01",
            "Zero Project", of course.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0xC,
        "#6P#11310F#NAzure... Zero...?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00007F#6P#NW-What is that!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(270, 110, -1, -1)

    AnonymousTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Uh uh, the "Sept-Terrion of Zero"'s completed form...\x02\x03",
            "The "Tree of Azure", the ruler of spacetime\x01",
            "that rearranges the principle of causality...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    SetMessageWindowPos(270, 110, -1, -1)

    AnonymousTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#4SIt is its very rebirth...!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(929, 0, 40, 0)
    Sound(934, 0, 40, 0)
    Sound(112, 2, 100, 0)
    PlayEffect(0x2, 0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
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
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    StopBGM(0x1388)
    OP_68(8000, 3000, -6000, 1000)
    SetCameraDistance(24000, 1000)

    def lambda_F276():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_F276)

    def lambda_F283():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_F283)

    def lambda_F290():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F290)
    Sleep(50)

    def lambda_F2A0():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_F2A0)
    Sleep(50)

    def lambda_F2B0():
        OP_93(0x103, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_F2B0)
    Sleep(50)

    def lambda_F2C0():
        OP_93(0x104, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_F2C0)
    Sleep(50)

    def lambda_F2D0():
        OP_93(0xF4, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_F2D0)
    Sleep(50)

    def lambda_F2E0():
        OP_93(0xF5, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_F2E0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)

    ChrTalk(
        0x104,
        "#00305F#5PThis light is...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F#5PAn azure light...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00207F#5P...South-by-southwest!\x01",
            "Near the Marshlands!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00010F#5PThat's──\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7555", 0)
    OP_68(8000, 3000, -7000, 2000)
    SetCameraDistance(24500, 2000)
    StopSound(132, 1000, 40)
    StopSound(112, 1000, 90)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_C9(0x0, 0x10)
    FadeToBright(0, 0)
    OP_0D()
    PlayMovie(0x0, "ed72_07a.pmf", 0x22B, 0x1)
    Sleep(1000)
    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C9(0x1, 0x10)
    ClearMapObjFlags(0x16, 0x4)
    StopEffect(0x0, 0x0)
    OP_68(0, 2000, -20000, 0)
    MoveCamera(150, 9, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(18500, 0)
    Sound(132, 2, 50, 0)
    Sound(112, 2, 80, 0)
    OP_68(0, 2000, -13000, 4000)
    MoveCamera(145, 9, 0, 4000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0x7D0)

    ChrTalk(
        0x101,
        "#5P#00010F#6P#N............ \x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F4D7")

    ChrTalk(
        0x109,
        "#5P#10111F#6P#NWhaaaa...!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_F4D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F504")

    ChrTalk(
        0x105,
        "#5P#10410F#6P#NT-That's...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_F504")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F537")

    ChrTalk(
        0x10A,
        "#5P#00610F#6P#N...It can't be...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_F537")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F56B")

    ChrTalk(
        0x106,
        "#5P#10701F#6P#N...A huge tree...?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_F56B")

    WaitBGM()
    Sleep(10)
    PlayBGM("ed7571", 0)
    Sleep(500)

    NpcTalk(
        0x104,
        "Dr. Novartis",
        (
            "#04702F#5P#NHehe── Magnificent!\x02\x03",
            "The very fruit of a singularity... \x01",
            "I should call it an "unexpected miracle"\x01",
            "that far exceeds that "Salt Pale"!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xC,
        "#11305F#6P#N............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopSound(112, 2000, 70)
    Fade(500)
    OP_68(8000, 3000, -3000, 0)
    MoveCamera(50, 3, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(23000, 0)
    OP_0D()
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        (
            "#00007F#4S#6P#NW-Wait a minute!\x02\x03",
            "#00010F#3SIf that huge tree is the true form\x01",
            "of the "Sept-Terrion of Zero", then...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_F716():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_F716)
    Sleep(30)

    def lambda_F726():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_F726)
    Sleep(30)

    def lambda_F736():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_F736)
    Sleep(30)

    def lambda_F746():
        OP_93(0xF4, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_F746)
    Sleep(30)

    def lambda_F756():
        OP_93(0xF5, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_F756)
    Sleep(30)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)

    ChrTalk(
        0x102,
        (
            "#00107F#6P#NKeA... \x01",
            "...Just where is she!?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(270, 110, -1, -1)

    AnonymousTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Uh uh. What are you saying?\x02\x03",
            "If you are looking for Miss KeA, look,\x01",
            "you should be seeing her from there, no?\x02\x03",
            "That very "Tree of Azure"\x01",
            "is Miss KeA herself.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
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
    Sleep(300)
    SetMessageWindowPos(300, 70, -1, -1)
    SetChrName("Arios")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "...Her heart and body\x01",
            "have not been lost.\x02\x03",
            "So don't worry.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(190, 100, -1, -1)
    SetChrName("Lawyer Ian")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "But more importantly, she has\x01",
            "become the "Arbitrator" of all──\x02\x03",
            "This is not a bad result.\x01",
            "For her, and you.\x02\x03",
            "If possible, I'd like you to watch over her.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x103,
        "#00206F#6P#NW-What are you...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        "#00310F#6P#NI don't get it at all...\x02",
    )

    CloseMessageWindow()
    OP_68(15000, 5000, -5000, 1600)
    MoveCamera(69, -5, 0, 1600)
    SetCameraDistance(19500, 1600)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FB3F")
    SetMessageWindowPos(0, 170, -1, -1)

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Really, I feel you.\x02\x03",
            "But I'm having fun,\x01",
            "so that's enough, I guess.\x02\x03",
            "Right, Rixia?㈱\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x106,
        "#10701F#6P#N............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_FBA1")

    label("loc_FB3F")

    SetMessageWindowPos(0, 170, -1, -1)

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Really, I feel you.\x02\x03",
            "But I'm having fun,\x01",
            "so that's enough, I guess.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_FBA1")

    SetMessageWindowPos(10, 110, -1, -1)

    AnonymousTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Hehe. Well if you're planning to interfere,\x01",
            "feel free. I'll be your opponent.\x02\x03",
            "This too was in the contract, after all.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FCF6")
    SetMessageWindowPos(370, 160, -1, -1)

    AnonymousTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "...I don't give a damn\x01",
            "about their plan...\x02\x03",
            "But if you come, I'll crush\x01",
            "you for good this time... \x02\x03",
            "Got it, Wazy...?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x105,
        "#10401F#6P#N...Wald.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_FD77")

    label("loc_FCF6")

    SetMessageWindowPos(370, 160, -1, -1)

    AnonymousTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "...I don't give a damn\x01",
            "about their plan...\x02\x03",
            "But if you come, I'll crush\x01",
            "you for good this time....\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_FD77")

    SetMessageWindowPos(160, 150, -1, -1)

    AnonymousTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Uhuhu... Well then.\x01",
            "Have a good day, everyone.\x02\x03",
            "──And father. Thank you for\x01",
            "your support up to this point.\x02\x03",
            "Although you were but a\x01",
            "simple romantic fool...\x02\x03",
            "I never hated you, father...\x07\x00\x01\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(977, 0, 100, 0)
    BeginChrThread(0x31, 3, 0, 90)
    Sleep(200)
    BeginChrThread(0x2C, 3, 0, 85)
    Sleep(200)
    BeginChrThread(0x2D, 3, 0, 86)
    Sleep(200)
    Sound(977, 0, 50, 0)
    BeginChrThread(0x2E, 3, 0, 87)
    Sleep(200)
    BeginChrThread(0x2F, 3, 0, 88)
    Sleep(200)
    BeginChrThread(0x30, 3, 0, 89)
    WaitChrThread(0x30, 3)
    Fade(500)
    OP_68(5000, 1500, -1000, 0)
    MoveCamera(35, 11, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(19000, 0)
    OP_93(0xC, 0x5A, 0x0)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF4, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF5, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_68(2000, 1500, -1000, 3000)
    OP_0D()
    OP_6F(0x79)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0xF4)
    OP_64(0xF5)

    ChrTalk(
        0xC,
        "#5P#11311F#40W......Bell......\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0xC, 0x21)
    SetChrSubChip(0xC, 0x0)
    Sleep(1000)

    def lambda_FFA3():
        OP_A6(0xFE, 0x0, 0x1E, 0x2EE, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_FFA3)
    Sound(802, 0, 100, 0)
    SetChrSubChip(0xC, 0x1)
    Sleep(130)
    SetChrSubChip(0xC, 0x2)
    Sleep(130)
    SetChrSubChip(0xC, 0x3)
    Sleep(500)
    TurnDirection(0x13, 0xC, 500)

    ChrTalk(
        0x13,
        (
            "#04704FHu hu, well if I didn't have other plans\x01",
            "I'd love to stay to the end, but...\x02\x03",
            "#04700FWell, I'll at least hear the\x01",
            "follow up report in a distant land.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(802, 0, 100, 0)
    Sound(901, 0, 100, 0)
    SetChrChipByIndex(0x13, 0x22)
    SetChrSubChip(0x13, 0x0)
    Sleep(500)
    Fade(1000)
    SetMapObjFlags(0x14, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    OP_0D()
    OP_68(0, 2000, -1000, 2000)
    MoveCamera(31, 5, 0, 2000)
    SetCameraDistance(18000, 2000)
    Sound(980, 2, 30, 0)
    BeginChrThread(0x28, 3, 0, 77)
    Sleep(300)
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

    def lambda_1017E():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1017E)
    Sleep(50)

    def lambda_1018E():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1018E)
    Sleep(50)

    def lambda_1019E():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1019E)
    Sleep(50)

    def lambda_101AE():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_101AE)
    Sleep(50)

    def lambda_101BE():
        OP_93(0xF4, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_101BE)
    Sleep(50)

    def lambda_101CE():
        OP_93(0xF5, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_101CE)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00007F#12P#N...Ah...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x28, 3)
    BeginChrThread(0x28, 3, 0, 78)
    Sound(223, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 10000, 0, 1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    Sound(936, 0, 100, 0)

    def lambda_10260():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_10260)
    WaitChrThread(0x13, 2)
    SetChrChipByIndex(0x13, 0x1F)
    SetChrSubChip(0x13, 0x0)
    OP_D3(0x13, 0x5, "Null_hand_l(63)")
    OP_93(0x13, 0x0, 0x0)
    ClearChrFlags(0x13, 0x1)
    OP_52(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(310, 4200, 5930, 2000)
    MoveCamera(31, 7, 0, 2000)
    SetCameraDistance(15000, 2000)
    Sleep(500)
    Sound(223, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 1900, 3900, 4750, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    def lambda_10310():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_10310)
    WaitChrThread(0x13, 2)
    Sound(936, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x13,
        (
            "#5P#04709FHa ha, excuse me, then.\x02\x03",
            "#04704FI think it's pointless, but at\x01",
            "least put up a good fight.\x02\x03",
            "#04702FFor the purpose of leaving behind\x01",
            "some useful data, of course.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(955, 0, 100, 0)
    Sleep(1000)
    OP_68(0, 4900, 6000, 700)
    Sound(905, 0, 100, 0)
    OP_71(0x5, 0x51E, 0x532, 0x0, 0x0)
    OP_79(0x5)
    OP_71(0x5, 0x532, 0x55A, 0x0, 0x20)
    OP_6F(0x79)
    MoveCamera(25, 15, 0, 3000)
    SetCameraDistance(22000, 3000)
    Sound(223, 0, 100, 0)
    Sound(919, 0, 70, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 0, 0, 6500, 0, 0, 0, 5000, 5000, 5000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    Sound(936, 0, 100, 0)
    StopSound(980, 1000, 30)
    OP_75(0x5, 0x1, 0x1F4)

    def lambda_1048B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_1048B)

    def lambda_1049C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_1049C)
    WaitChrThread(0x13, 2)
    SetChrFlags(0x13, 0x80)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(0, 2000, -1000, 0)
    MoveCamera(31, 5, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(18500, 0)
    OP_0D()

    ChrTalk(
        0x103,
        "#00201F#30W#11P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00310F#30W#11PHe stirs the pot and\x01",
            "then runs away, huh...\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x6, 0, 0, -21000, 0)
    SetChrPos(0x7, 0, 0, -22000, 0)
    ClearChrFlags(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    ClearChrFlags(0x7, 0x80)
    ClearChrBattleFlags(0x7, 0x8000)
    StopBGM(0x1770)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_105C7")

    NpcTalk(
        0x105,
        "Wazy's Voice",
        "Everyone, are you all right...!?\x02",
    )

    CloseMessageWindow()
    Jump("loc_10633")

    label("loc_105C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_10606")

    NpcTalk(
        0x109,
        "Noｱl's Voice",
        "Everyone...are you all right!?\x02",
    )

    CloseMessageWindow()
    Jump("loc_10633")

    label("loc_10606")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_10633")

    NpcTalk(
        0x10A,
        "Dudley's Voice",
        "Are you ok...!?\x02",
    )

    CloseMessageWindow()

    label("loc_10633")

    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(0, 1200, -10000, 2250)
    MoveCamera(55, 13, 0, 2250)
    OP_6E(600, 2250)
    SetCameraDistance(15000, 2250)

    def lambda_106DB():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_106DB)
    Sleep(50)

    def lambda_106EB():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_106EB)
    Sleep(50)

    def lambda_106FB():
        OP_93(0x103, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_106FB)
    Sleep(50)

    def lambda_1070B():
        OP_93(0x104, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1070B)
    Sleep(50)

    def lambda_1071B():
        OP_93(0xF4, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_1071B)
    Sleep(50)

    def lambda_1072B():
        OP_93(0xF5, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_1072B)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)

    def lambda_10750():
        OP_96(0xFE, 0xFFFFFCE0, 0x0, 0xFFFFCF2C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x6, 1, lambda_10750)
    Sleep(200)

    def lambda_1076D():
        OP_96(0xFE, 0x320, 0x0, 0xFFFFCF2C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x7, 1, lambda_1076D)
    WaitChrThread(0x6, 1)
    WaitChrThread(0x7, 1)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00008FYou two...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_10809")

    ChrTalk(
        0x106,
        (
            "#10708F#12PJ-Just now... What was...\x02\x03",
            "#10707FAnd what is that\x01",
            "huge tree thing...!?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_108D0")

    label("loc_10809")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1086E")

    ChrTalk(
        0x10A,
        (
            "#00610F#12PJ-Just now... What was...\x02\x03",
            "#00607FAnd what's that huge\x01",
            "tree thing...!?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_108D0")

    label("loc_1086E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_108D0")

    ChrTalk(
        0x109,
        (
            "#10108F#12PJ-Just now... What was...\x02\x03",
            "#10107FA-And what's that\x01",
            "huge tree thing...!?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_108D0")


    ChrTalk(
        0x102,
        "#5P#00106FT-That's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5P#00206FHow should we put it...\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x15, 0x4)
    SetChrPos(0x15, -8500, -2000, -20000, 90)

    NpcTalk(
        0x15,
        "Sergei's Voice",
        (
            "...Looks like it's\x01",
            "not over yet.\x02",
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
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7567", 0)
    Fade(500)
    OP_68(0, 1000, -21800, 0)
    MoveCamera(145, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x6, -1200, 0, -12500, 0)
    SetChrPos(0x7, 1200, 0, -12500, 0)

    def lambda_10A5D():
        OP_95(0xFE, -2200, 0, -21800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_10A5D)
    Sleep(500)
    Sound(112, 2, 50, 0)
    WaitChrThread(0x15, 1)

    def lambda_10A84():
        OP_95(0xFE, 0, 0, -21800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_10A84)
    WaitChrThread(0x15, 1)
    OP_68(0, 1000, -10000, 4000)
    MoveCamera(145, 15, 0, 4000)

    def lambda_10ABE():
        OP_95(0xFE, 0, 0, -11500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_10ABE)
    WaitChrThread(0x15, 1)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#6P#00005FChief...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00301F#6PAre the people down below all right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#11P#01003FYeah, the magic soldiers disappeared\x01",
            "so we've taken the tower with no problems.\x02\x03",
            "#01001FBut...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x15, 0xB4, 0x1F4)
    Sleep(900)
    OP_68(-450, 1500, -5360, 1500)
    SetCameraDistance(18700, 1500)
    OP_93(0x15, 0x0, 0x1F4)
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0xC,
        "#11311F#40W#11P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#11P#01006F...Just what the\x01",
            "hell happened here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#6PRight...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00006F#6P...Well...\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(18200, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)
    SetChrPos(0x101, -450, 0, -9600, 180)
    SetChrPos(0x102, 450, 0, -9100, 180)
    SetChrPos(0x103, -1500, 0, -9600, 135)
    SetChrPos(0x104, 1500, 0, -9600, 225)
    SetChrPos(0xF4, -1050, 0, -8000, 180)
    SetChrPos(0xF5, 1050, 0, -8000, 180)
    SetChrPos(0x6, -1750, 0, -11400, 45)
    SetChrPos(0x7, 1750, 0, -11400, 315)
    SetChrPos(0x15, 0, 0, -12900, 0)
    OP_68(-120, 1100, -11660, 0)
    MoveCamera(143, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14000, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and others outlined what happened.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(14500, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_10DF9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10DC8")

    ChrTalk(
        0x106,
        "#11P#10712FS-Something like that has...\x02",
    )

    Jump("loc_10DF3")

    label("loc_10DC8")


    ChrTalk(
        0x106,
        "#5P#10712FS-Something like that has...\x02",
    )


    label("loc_10DF3")

    CloseMessageWindow()
    Jump("loc_10EE8")

    label("loc_10DF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_10E72")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10E43")

    ChrTalk(
        0x109,
        "#11P#10106FA-A thing like that has...\x02",
    )

    Jump("loc_10E6C")

    label("loc_10E43")


    ChrTalk(
        0x106,
        "#5P#10706FA-A thing like that has...\x02",
    )


    label("loc_10E6C")

    CloseMessageWindow()
    Jump("loc_10EE8")

    label("loc_10E72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_10EE8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10EBD")

    ChrTalk(
        0x105,
        "#11P#10406FThat's indeed surprising...\x02",
    )

    Jump("loc_10EE7")

    label("loc_10EBD")


    ChrTalk(
        0x105,
        "#5P#10406FThat's indeed surprising...\x02",
    )


    label("loc_10EE7")

    CloseMessageWindow()

    label("loc_10EE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_10F97")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10F4D")

    ChrTalk(
        0x10A,
        (
            "#11P#00608FI can't believe Lawyer Ian\x01",
            "was the sole mastermind...\x02",
        )
    )

    Jump("loc_10F91")

    label("loc_10F4D")


    ChrTalk(
        0x10A,
        (
            "#5P#00608FI can't believe Lawyer Ian\x01",
            "was the sole mastermind...\x02",
        )
    )


    label("loc_10F91")

    CloseMessageWindow()
    Jump("loc_110CC")

    label("loc_10F97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_11036")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10FF4")

    ChrTalk(
        0x105,
        (
            "#11P#10403FAnd Mr. Beardy-Bear\x01",
            "is the sole mastermind...\x02",
        )
    )

    Jump("loc_11030")

    label("loc_10FF4")


    ChrTalk(
        0x105,
        (
            "#5P#10403FAnd Mr. Beardy-Bear\x01",
            "is the sole mastermind...\x02",
        )
    )


    label("loc_11030")

    CloseMessageWindow()
    Jump("loc_110CC")

    label("loc_11036")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_110CC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11091")

    ChrTalk(
        0x109,
        (
            "#11P#10108FAnd Mr. Grimwood was\x01",
            "the sole mastermind...\x02",
        )
    )

    Jump("loc_110CB")

    label("loc_11091")


    ChrTalk(
        0x109,
        (
            "#5P#10108FAnd Mr. Grimwood was\x01",
            "the sole mastermind...\x02",
        )
    )


    label("loc_110CB")

    CloseMessageWindow()

    label("loc_110CC")


    ChrTalk(
        0x15,
        (
            "#11P#01006F...I see.\x02\x03",
            "#01001FSo a character who was known in political,\x01",
            "business, international, police and Guild circles\x01",
            "had things going on behind the scenes, huh.\x02\x03",
            "#01003FIndeed, if he felt like it, he\x01",
            "could've planned all of this.\x02\x03",
            "#01000FThe problem's the motive...\x01",
            "But now's not the time for that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#6PYes...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Sleep(200)
    SetChrName("")
    BeginChrThread(0x101, 0, 0, 74)
    WaitChrThread(0x101, 0)

    ChrTalk(
        0x101,
        (
            "#13P#00001F──Wazy. Can you\x01",
            "call the Merkabah?\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x105, 0, 0, 73)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x105,
        "#13P#10402FHu hu, I figured you'd say that.\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_93(0x105, 0x10E, 0x1F4)
    Sleep(300)
    Fade(250)
    Sound(802, 0, 80, 0)
    SetChrChipByIndex(0x105, 0x23)
    SetChrSubChip(0x105, 0x4)
    SetChrFlags(0x105, 0x10)
    SetChrFlags(0x105, 0x2)
    SetChrFlags(0x105, 0x20)
    Sleep(500)
    SetChrSubChip(0x105, 0x5)
    Sound(804, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x15,
        "#11P#01000F...Are you going?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1131D")

    def lambda_11315():
        TurnDirection(0xFE, 0x15, 500)
        ExitThread()

    QueueWorkItem(0x6, 2, lambda_11315)

    label("loc_1131D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x7, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1133C")

    def lambda_11334():
        TurnDirection(0xFE, 0x15, 500)
        ExitThread()

    QueueWorkItem(0x7, 2, lambda_11334)

    label("loc_1133C")

    OP_93(0x101, 0xB4, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00003F#6PYes, although it might not\x01",
            "be police work anymore...\x02\x03",
            "#00013FBut as long as KeA and the truth\x01",
            "of all this is waiting for us\x01",
            "there, I can't ignore it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#6P...I feel the same.\x01",
            "We have to stop Bell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#6PWell, we have come this far,\x01",
            "of course we will go all the way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F#6PLooks like my uncle and\x01",
            "Shirley are waiting for me.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x109, 0, 0, 72)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x109,
        (
            "#6P#10107FI... \x01",
            "I'll come too!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    SetChrSubChip(0x105, 0x4)
    Sound(804, 0, 100, 0)
    Sleep(300)
    Fade(250)
    Sound(802, 0, 80, 0)
    SetChrChipByIndex(0x105, 0xFF)
    ClearChrFlags(0x105, 0x10)
    ClearChrFlags(0x105, 0x2)
    ClearChrFlags(0x105, 0x20)
    SetChrSubChip(0x105, 0x0)
    OP_0D()
    Sleep(150)
    TurnDirection(0x105, 0x15, 500)
    BeginChrThread(0x105, 0, 0, 73)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x105,
        (
            "#6P#10404FWell, I'm offering you the Merkabah,\x01",
            "so I'll be coming along too.\x02\x03",
            "#10400FAnd it seems I also need to\x01",
            "settle things with Wald.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x106, 0, 0, 75)
    WaitChrThread(0x106, 0)

    ChrTalk(
        0x106,
        (
            "#6P#10703F...I need to settle things\x01",
            "with "her" as well.\x02\x03",
            "#10708FFor my own sake too...\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x10A, 0, 0, 76)
    WaitChrThread(0x10A, 0)

    ChrTalk(
        0x10A,
        (
            "#6P#00603F...I need to hear the situation\x01",
            "in detail from both MacLaine\x01",
            "and Mr. Grimwood.\x02\x03",
            "#00601FI plan to come along too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#11P#01004FHehe... It'd be useless\x01",
            "trying to stop you, huh.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x32, 1, 0, 91)
    OP_68(1020, 1900, -13060, 3000)
    MoveCamera(143, 12, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(18500, 3000)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetChrPos(0x2B, 0, 60000, -10000, 0)
    OP_D5(0x2B, 0x0, 0x0, 0x0, 0x0)
    ClearMapObjFlags(0x15, 0x4)

    def lambda_1175F():
        OP_96(0x2B, 0x0, 0x2710, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_1175F)
    BeginChrThread(0x2B, 3, 0, 71)
    OP_68(0, 45000, 0, 0)
    MoveCamera(231, -60, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(55000, 0)
    MoveCamera(211, -30, 0, 7000)
    SetCameraDistance(45000, 7000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(5000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetMapObjFlags(0x15, 0x4)
    ClearMapObjFlags(0x17, 0x4)
    SetChrPos(0x18, 11000, 0, -2000, 200)
    OP_D5(0x18, 0x0, 0x30D40, 0x0, 0x0)
    OP_75(0x17, 0x2, 0xBB8)
    OP_68(1020, 1900, -13060, 0)
    MoveCamera(143, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    OP_68(-240, 1100, -11750, 3000)
    MoveCamera(143, 17, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(14500, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x15,
        (
            "#11P#01003F──Leave the city and tower to\x01",
            "me─ the President included.\x02\x03",
            "#01001FYou guys─ Do what you need to do,\x01",
            "and keep doing it until you're satisfied...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x15,
        (
            "#01007F#11PAs the "Special Support Section"... \x01",
            "And above all else, as yourselves!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x12C, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(80, 50, -1, -1)
    SetChrName("Everyone")

    AnonymousTalk(
        0xFF,
        "#4SRight...!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(19000, 3000)
    StopSound(132, 490, 40)
    StopSound(112, 490, 40)
    FadeToDark(2000, 0, -1)
    Sleep(500)
    StopSound(497, 1500, 50)
    StopSound(496, 1500, 50)
    OP_0D()
    EndChrThread(0x2B, 0xFF)
    OP_6F(0x79)
    SetMessageWindowPos(14, 280, 60, 3)
    StopBGM(0xFA0)
    WaitBGM()
    OP_24(0x84)
    OP_24(0x70)
    Sleep(2000)
    OP_29(0xB1, 0x1, 0xF)
    OP_29(0xB1, 0x4, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 0)), scpexpr(EXPR_END)), "loc_11A28")
    OP_E0(0x33, 0x0)
    OP_E0(0x80, 0x0)
    Sleep(500)

    label("loc_11A28")

    OP_E5(0x3)
    SetScenarioFlags(0x23, 6)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_70_D4D4 end

    def Function_71_11A37(): pass

    label("Function_71_11A37")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11A5B")
    OP_82(0xA, 0xA, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_71_11A37")

    label("loc_11A5B")

    Return()

    # Function_71_11A37 end

    def Function_72_11A5C(): pass

    label("Function_72_11A5C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11A76")
    OP_FC(0x1)
    Jump("loc_11ABF")

    label("loc_11A76")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11A90")
    OP_FC(0x2)
    Jump("loc_11ABF")

    label("loc_11A90")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11AAA")
    OP_FC(0x1)
    Jump("loc_11ABF")

    label("loc_11AAA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x7, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11ABF")
    OP_FC(0x2)

    label("loc_11ABF")

    Sleep(1)
    Return()

    # Function_72_11A5C end

    def Function_73_11AC3(): pass

    label("Function_73_11AC3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11ADD")
    OP_FC(0x6)
    Jump("loc_11B26")

    label("loc_11ADD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11AF7")
    OP_FC(0x6)
    Jump("loc_11B26")

    label("loc_11AF7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11B11")
    OP_FC(0xB)
    Jump("loc_11B26")

    label("loc_11B11")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x7, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11B26")
    OP_FC(0x5)

    label("loc_11B26")

    Sleep(1)
    Return()

    # Function_73_11AC3 end

    def Function_74_11B2A(): pass

    label("Function_74_11B2A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11B44")
    OP_FC(0xB)
    Jump("loc_11B8D")

    label("loc_11B44")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11B5E")
    OP_FC(0xB)
    Jump("loc_11B8D")

    label("loc_11B5E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11B78")
    OP_FC(0x6)
    Jump("loc_11B8D")

    label("loc_11B78")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x7, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11B8D")
    OP_FC(0x6)

    label("loc_11B8D")

    Sleep(1)
    Return()

    # Function_74_11B2A end

    def Function_75_11B91(): pass

    label("Function_75_11B91")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11BAB")
    OP_FC(0x1)
    Jump("loc_11BF4")

    label("loc_11BAB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11BC5")
    OP_FC(0x2)
    Jump("loc_11BF4")

    label("loc_11BC5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11BDF")
    OP_FC(0x1)
    Jump("loc_11BF4")

    label("loc_11BDF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x7, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11BF4")
    OP_FC(0x2)

    label("loc_11BF4")

    Sleep(1)
    Return()

    # Function_75_11B91 end

    def Function_76_11BF8(): pass

    label("Function_76_11BF8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11C12")
    OP_FC(0x1)
    Jump("loc_11C5B")

    label("loc_11C12")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11C2C")
    OP_FC(0x2)
    Jump("loc_11C5B")

    label("loc_11C2C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11C46")
    OP_FC(0x1)
    Jump("loc_11C5B")

    label("loc_11C46")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x7, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11C5B")
    OP_FC(0x2)

    label("loc_11C5B")

    Sleep(1)
    Return()

    # Function_76_11BF8 end

    def Function_77_11C5F(): pass

    label("Function_77_11C5F")

    Sound(905, 0, 100, 0)
    Sound(904, 2, 100, 0)
    OP_74(0x5, 0xF)
    OP_71(0x5, 0x3A3, 0x3CA, 0x0, 0x0)
    Sleep(2000)
    Sound(902, 0, 70, 0)
    OP_79(0x5)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0xB, 0x32, 0x0, 0x0)
    Sound(951, 0, 100, 0)
    OP_24(0x388)
    Return()

    # Function_77_11C5F end

    def Function_78_11CA1(): pass

    label("Function_78_11CA1")

    Sound(905, 0, 100, 0)
    OP_71(0x5, 0x4E2, 0x4F6, 0x0, 0x0)
    OP_79(0x5)
    OP_71(0x5, 0x4F6, 0x51E, 0x0, 0x20)
    Return()

    # Function_78_11CA1 end

    def Function_79_11CC3(): pass

    label("Function_79_11CC3")

    OP_71(0xD, 0x0, 0x64, 0x0, 0x8)
    OP_79(0xD)
    OP_71(0xD, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_79_11CC3 end

    def Function_80_11CDF(): pass

    label("Function_80_11CDF")

    OP_71(0xE, 0x0, 0x64, 0x0, 0x8)
    OP_79(0xE)
    OP_71(0xE, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_80_11CDF end

    def Function_81_11CFB(): pass

    label("Function_81_11CFB")

    OP_71(0xF, 0x0, 0x64, 0x0, 0x8)
    OP_79(0xF)
    OP_71(0xF, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_81_11CFB end

    def Function_82_11D17(): pass

    label("Function_82_11D17")

    OP_71(0x10, 0x0, 0x64, 0x0, 0x8)
    OP_79(0x10)
    OP_71(0x10, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_82_11D17 end

    def Function_83_11D33(): pass

    label("Function_83_11D33")

    OP_71(0x11, 0x0, 0x64, 0x0, 0x8)
    OP_79(0x11)
    OP_71(0x11, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_83_11D33 end

    def Function_84_11D4F(): pass

    label("Function_84_11D4F")

    OP_74(0x12, 0xF)
    OP_71(0x12, 0x0, 0x64, 0x0, 0x8)
    OP_79(0x12)
    OP_74(0x12, 0x1E)
    OP_71(0x12, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_84_11D4F end

    def Function_85_11D73(): pass

    label("Function_85_11D73")

    OP_75(0xD, 0x1, 0x3E8)
    Sleep(2000)
    Return()

    # Function_85_11D73 end

    def Function_86_11D7E(): pass

    label("Function_86_11D7E")

    OP_75(0xE, 0x1, 0x3E8)
    Sleep(2000)
    Return()

    # Function_86_11D7E end

    def Function_87_11D89(): pass

    label("Function_87_11D89")

    OP_75(0xF, 0x1, 0x3E8)
    Sleep(2000)
    Return()

    # Function_87_11D89 end

    def Function_88_11D94(): pass

    label("Function_88_11D94")

    OP_75(0x10, 0x1, 0x3E8)
    Sleep(2000)
    Return()

    # Function_88_11D94 end

    def Function_89_11D9F(): pass

    label("Function_89_11D9F")

    OP_75(0x11, 0x1, 0x3E8)
    Sleep(2000)
    Return()

    # Function_89_11D9F end

    def Function_90_11DAA(): pass

    label("Function_90_11DAA")

    OP_75(0x12, 0x1, 0x3E8)
    Sleep(2000)
    Return()

    # Function_90_11DAA end

    def Function_91_11DB5(): pass

    label("Function_91_11DB5")

    Sound(497, 2, 0, 0)
    Sound(496, 2, 0, 0)
    Sleep(200)
    OP_25(0x1F1, 0x5)
    OP_25(0x1F0, 0x5)
    Sleep(200)
    OP_25(0x1F1, 0xA)
    OP_25(0x1F0, 0xA)
    Sleep(200)
    OP_25(0x1F1, 0xF)
    OP_25(0x1F0, 0xF)
    Sleep(200)
    OP_25(0x1F1, 0x14)
    OP_25(0x1F0, 0x14)
    Sleep(200)
    OP_25(0x1F1, 0x19)
    OP_25(0x1F0, 0x19)
    Sleep(200)
    OP_25(0x1F1, 0x1E)
    OP_25(0x1F0, 0x1E)
    Sleep(200)
    OP_25(0x1F1, 0x23)
    OP_25(0x1F0, 0x23)
    Sleep(200)
    OP_25(0x1F1, 0x28)
    OP_25(0x1F0, 0x28)
    Sleep(200)
    OP_25(0x1F1, 0x2D)
    OP_25(0x1F0, 0x2D)
    Sleep(200)
    OP_25(0x1F1, 0x32)
    OP_25(0x1F0, 0x32)
    Return()

    # Function_91_11DB5 end

    def Function_92_11E30(): pass

    label("Function_92_11E30")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    EventEnd(0x5)
    SetCameraDistance(13000, 0)
    Return()

    # Function_92_11E30 end

    def Function_93_11E48(): pass

    label("Function_93_11E48")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    StopEffect(0x9, 0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x394),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x394, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x18A, 0)
    OP_65(0x0, 0x1)
    EventEnd(0x3)
    Return()

    # Function_93_11E48 end

    def Function_94_11EA5(): pass

    label("Function_94_11EA5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05620.itc", 0x1E)
    LoadChrToIndex("chr/ch30000.itc", 0x1F)
    LoadChrToIndex("chr/ch02500.itc", 0x20)
    SetChrPos(0x0, 0, -33620, 0, 0)
    SetChrPos(0x1, 0, -33620, 0, 0)
    SetChrPos(0x2, 0, -33620, 0, 0)
    SetChrPos(0x3, 0, -33620, 0, 0)
    SetChrChipByIndex(0x1A, 0x1F)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1A, 0x4)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, -800, 0, -16900, 180)
    SetChrChipByIndex(0x1B, 0x1F)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1B, 0x4)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, 800, 0, -16900, 180)
    SetChrChipByIndex(0x1C, 0x1F)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1C, 0x4)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, -1800, 0, -19500, 45)
    SetChrChipByIndex(0x1D, 0x20)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1D, 0x4)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, 3700, 0, -17500, 270)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 0, 0, -17000, 180)
    ClearMapObjFlags(0x16, 0x4)
    OP_68(0, 900, -19000, 0)
    MoveCamera(140, 15, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13500, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Return()

    # Function_94_11EA5 end

    SaveToFile()

Try(main)
