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
        "Function_5_15BE",         # 05, 5
        "Function_6_16C3",         # 06, 6
        "Function_7_190B",         # 07, 7
        "Function_8_1FB8",         # 08, 8
        "Function_9_2302",         # 09, 9
        "Function_10_2F75",        # 0A, 10
        "Function_11_2FCA",        # 0B, 11
        "Function_12_301F",        # 0C, 12
        "Function_13_3074",        # 0D, 13
        "Function_14_30E4",        # 0E, 14
        "Function_15_3139",        # 0F, 15
        "Function_16_318E",        # 10, 16
        "Function_17_31BE",        # 11, 17
        "Function_18_3226",        # 12, 18
        "Function_19_3263",        # 13, 19
        "Function_20_32A7",        # 14, 20
        "Function_21_32EB",        # 15, 21
        "Function_22_332F",        # 16, 22
        "Function_23_3373",        # 17, 23
        "Function_24_33B7",        # 18, 24
        "Function_25_33FB",        # 19, 25
        "Function_26_343F",        # 1A, 26
        "Function_27_39C6",        # 1B, 27
        "Function_28_3A26",        # 1C, 28
        "Function_29_3A86",        # 1D, 29
        "Function_30_3BA9",        # 1E, 30
        "Function_31_3CB5",        # 1F, 31
        "Function_32_3D84",        # 20, 32
        "Function_33_3E53",        # 21, 33
        "Function_34_424C",        # 22, 34
        "Function_35_5970",        # 23, 35
        "Function_36_5A68",        # 24, 36
        "Function_37_5A87",        # 25, 37
        "Function_38_5AA6",        # 26, 38
        "Function_39_5B05",        # 27, 39
        "Function_40_5B24",        # 28, 40
        "Function_41_5B6C",        # 29, 41
        "Function_42_5BB9",        # 2A, 42
        "Function_43_7106",        # 2B, 43
        "Function_44_7423",        # 2C, 44
        "Function_45_74D7",        # 2D, 45
        "Function_46_7527",        # 2E, 46
        "Function_47_757D",        # 2F, 47
        "Function_48_7637",        # 30, 48
        "Function_49_76E0",        # 31, 49
        "Function_50_77CB",        # 32, 50
        "Function_51_780B",        # 33, 51
        "Function_52_788E",        # 34, 52
        "Function_53_8128",        # 35, 53
        "Function_54_8939",        # 36, 54
        "Function_55_8A50",        # 37, 55
        "Function_56_92FA",        # 38, 56
        "Function_57_946E",        # 39, 57
        "Function_58_94AD",        # 3A, 58
        "Function_59_9945",        # 3B, 59
        "Function_60_9974",        # 3C, 60
        "Function_61_9A11",        # 3D, 61
        "Function_62_9A28",        # 3E, 62
        "Function_63_C688",        # 3F, 63
        "Function_64_C6B6",        # 40, 64
        "Function_65_C717",        # 41, 65
        "Function_66_C778",        # 42, 66
        "Function_67_C79D",        # 43, 67
        "Function_68_D2A7",        # 44, 68
        "Function_69_D2BA",        # 45, 69
        "Function_70_D2EF",        # 46, 70
        "Function_71_116D8",       # 47, 71
        "Function_72_116FD",       # 48, 72
        "Function_73_11764",       # 49, 73
        "Function_74_117CB",       # 4A, 74
        "Function_75_11832",       # 4B, 75
        "Function_76_11899",       # 4C, 76
        "Function_77_11900",       # 4D, 77
        "Function_78_11942",       # 4E, 78
        "Function_79_11964",       # 4F, 79
        "Function_80_11980",       # 50, 80
        "Function_81_1199C",       # 51, 81
        "Function_82_119B8",       # 52, 82
        "Function_83_119D4",       # 53, 83
        "Function_84_119F0",       # 54, 84
        "Function_85_11A14",       # 55, 85
        "Function_86_11A1F",       # 56, 86
        "Function_87_11A2A",       # 57, 87
        "Function_88_11A35",       # 58, 88
        "Function_89_11A40",       # 59, 89
        "Function_90_11A4B",       # 5A, 90
        "Function_91_11A56",       # 5B, 91
        "Function_92_11AD1",       # 5C, 92
        "Function_93_11AE9",       # 5D, 93
        "Function_94_11B46",       # 5E, 94
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
    Jump("loc_15BA")

    label("loc_1345")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_150A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1471")

    ChrTalk(
        0xFE,
        (
            "*sigh*... I knew coming\x01",
            "here multiple times was\x01",
            "a good idea.\x02",
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
            "If you like, you guys\x01",
            "can read this.\x02",
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
    Jump("loc_1505")

    label("loc_1471")


    ChrTalk(
        0xFE,
        (
            "*sigh*... I knew coming\x01",
            "here multiple times was\x01",
            "a good idea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I look at this scenery,\x01",
            "even the fear I felt from\x01",
            "that attack subsides.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1505")

    Jump("loc_15BA")

    label("loc_150A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_15BA")

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
            "Even though the scenery\x01",
            "is this beautiful...\x01",
            "It's a really sad thing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15BA")

    TalkEnd(0xFE)
    Return()

    # Function_4_1334 end

    def Function_5_15BE(): pass

    label("Function_5_15BE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_1644")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15E0")
    TalkEnd(0xFE)
    Call(0, 7)
    Return()

    label("loc_15E0")


    ChrTalk(
        0x9,
        (
            "#11223F...I'm sure you'll be\x01",
            "all right.\x02\x03",
            "#11222FSo please... Save my\x01",
            "precious friend KeA!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16BF")

    label("loc_1644")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_16BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_165F")
    Call(0, 6)
    Jump("loc_16BF")

    label("loc_165F")


    ChrTalk(
        0x9,
        (
            "#11228FEveryone, please... Take\x01",
            "care of my father and\x01",
            "KeA.\x02\x03",
            "#11223FI will be waiting here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16BF")

    TalkEnd(0xFE)
    Return()

    # Function_5_15BE end

    def Function_6_16C3(): pass

    label("Function_6_16C3")

    OP_93(0x9, 0x87, 0x0)

    ChrTalk(
        0x9,
        "#11221FFather, KeA...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FShizuku... So this is\x01",
            "where you were.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x0, 500)

    ChrTalk(
        0x9,
        (
            "#11220FEveryone... Yes, I was\x01",
            "looking at that Huge\x01",
            "Tree.\x02\x03",
            "#11230FAre father and KeA\x01",
            "really in there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F...Yes. There's no\x01",
            "mistake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108FWe still don't know\x01",
            "where in the Huge Tree\x01",
            "they are, though...\x02",
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
            "#00003F...Shizuku, please wait\x01",
            "for us.\x02\x03",
            "#00001FWe'll definitely bring\x01",
            "back Arios and KeA for\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00302FYeah, so don't worry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11223F...Right.\x02\x03",
            "#11221FEveryone, please... Take\x01",
            "care of my father and\x01",
            "KeA.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x87, 0x0)
    SetScenarioFlags(0x1AF, 2)
    Return()

    # Function_6_16C3 end

    def Function_7_190B(): pass

    label("Function_7_190B")

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
            "And then, they explained\x01",
            "to Shizuku that Guy's\x01",
            "murderer wasn't Arios.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x9,
        "#11225F...I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00004F...Yeah.\x02\x03",
            "#00000FArios will be back with\x01",
            "you soon, Shizuku...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11233F...Ooh... *cry*...\x02",
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
            "#11233FMy father's precious\x01",
            "friend... So he didn't\x01",
            "look after your brother...\x02\x03",
            "#11234FIf it's really true, my\x01",
            "father might not ever be\x01",
            "able to go back...\x02",
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
            "#6P#00002FHaha... I said it,\x01",
            "right? It's not the case\x01",
            "that he can't go back.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1CCD")

    ChrTalk(
        0x10A,
        (
            "#6P#00602F...Just you wait. I\x01",
            "promise you MacLaine'll\x01",
            "be back later.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D7D")

    label("loc_1CCD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D1F")

    ChrTalk(
        0x109,
        (
            "#6P#10102FJust you wait. Arios\x01",
            "will definitely be back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D7D")

    label("loc_1D1F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D7D")

    ChrTalk(
        0x105,
        (
            "#6P#10402FArios will definitely be\x01",
            "back later. Haha, I\x01",
            "promise you that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D7D")


    ChrTalk(
        0x9,
        "#11222F*cry*... Okay!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00202F...All that's left is to\x01",
            "bring back KeA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00309FYeah. For Shizuku's\x01",
            "smile, too!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E63")

    ChrTalk(
        0x105,
        (
            "#6P#10409FHaha. Well we have to do\x01",
            "it now, if that's how\x01",
            "it's gonna be.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F11")

    label("loc_1E63")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1EC0")

    ChrTalk(
        0x109,
        (
            "#6P#10109FThat's something we must\x01",
            "accomplish, no matter\x01",
            "the cost!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F11")

    label("loc_1EC0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F11")

    ChrTalk(
        0x106,
        (
            "#6P#10709FIf that's how it's going\x01",
            "to be, we have to do it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F11")


    ChrTalk(
        0x9,
        (
            "#11223F...If you all won\x01",
            "against my dad, I'm sure\x01",
            "it'll be all right.\x02\x03",
            "#11227FSo please... Save my\x01",
            "precious friend KeA!\x02",
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

    # Function_7_190B end

    def Function_8_1FB8(): pass

    label("Function_8_1FB8")

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

    # Function_8_1FB8 end

    def Function_9_2302(): pass

    label("Function_9_2302")

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
        "#11P#10109FWoah!!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x105, 3)

    ChrTalk(
        0x105,
        "#11P#10302FThis is... incredible.\x02",
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
        "#00004F#11PHaha... I'm speechless.\x02",
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
            "#00202F#11P...From here, the city\x01",
            "below looks like\x01",
            "miniatures...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F#11PI bet the view's amazing\x01",
            "at night, too.\x02",
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
            "#12P#02809FHaha, well you can think of\x01",
            "this place as a viewing\x01",
            "platform open to the public.\x02\x03",
            "#02800FIt'd be too much of a waste\x01",
            "if it was reserved only for\x01",
            "government officials.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_283F():
        TurnDirection(0x101, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_283F)
    Sleep(50)

    def lambda_284F():
        TurnDirection(0x102, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_284F)
    Sleep(50)

    def lambda_285F():
        TurnDirection(0x103, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_285F)
    Sleep(50)

    def lambda_286F():
        TurnDirection(0x104, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_286F)
    Sleep(50)

    def lambda_287F():
        TurnDirection(0x105, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_287F)
    Sleep(50)

    def lambda_288F():
        TurnDirection(0x109, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_288F)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    def lambda_28B4():

        label("loc_28B4")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_28B4")

    QueueWorkItem2(0x101, 2, lambda_28B4)

    def lambda_28C6():

        label("loc_28C6")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_28C6")

    QueueWorkItem2(0x102, 2, lambda_28C6)

    def lambda_28D8():

        label("loc_28D8")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_28D8")

    QueueWorkItem2(0x103, 2, lambda_28D8)

    def lambda_28EA():

        label("loc_28EA")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_28EA")

    QueueWorkItem2(0x109, 2, lambda_28EA)

    def lambda_28FC():

        label("loc_28FC")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_28FC")

    QueueWorkItem2(0x105, 2, lambda_28FC)

    def lambda_290E():

        label("loc_290E")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_290E")

    QueueWorkItem2(0x104, 2, lambda_290E)

    ChrTalk(
        0x101,
        (
            "#00002F#5PYeah, that's a good\x01",
            "idea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F#5PHaha, I want to take KeA\x01",
            "here too.\x02",
        )
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(500)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xC,
        "#12P#02805FWhoops, excuse me.\x02",
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
            "#02803F...I see. Understood.\x01",
            "I'll head there right\x01",
            "away.\x02",
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
            "#12P#02800FIt seems the heads of\x01",
            "state have arrived at\x01",
            "the tower.\x02\x03",
            "I am terribly sorry, but\x01",
            "I'll have to take my\x01",
            "leave here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#5PIs that so... Thank you\x01",
            "very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204F#5PThanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309F#5PMan, that was a blast.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102F#5PYou gave us a great\x01",
            "experience!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12P#02804FAnd I thank all of you as\x01",
            "well. That was a great\x01",
            "change of pace.\x02\x03",
            "#02800FWell then, see you later,\x01",
            "everyone. Please, do your\x01",
            "best with the security.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#5PYes, leave that to us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F#5PYou gave me that\x01",
            "recommendation. It's the\x01",
            "least I could do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104F#5P─May the Goddess protect\x01",
            "you. I pray for the\x01",
            "success of the conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#12P#02809FHaha, I'm praying too.\x02",
    )

    CloseMessageWindow()
    OP_92(0xC, 0xFFFFADF8, 0xFFFFADF8, 0x1F4)
    OP_68(-25800, -3300, -28300, 5000)
    SetCameraDistance(17500, 5000)

    def lambda_2D4F():
        OP_95(0xFE, -21000, -4400, -21000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2D4F)
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
            "#00000F#5PWe should be getting\x01",
            "back to Detective\x01",
            "Dudley.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2E08():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2E08)
    Sleep(50)

    def lambda_2E18():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2E18)
    Sleep(50)

    def lambda_2E28():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2E28)
    Sleep(50)

    def lambda_2E38():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2E38)
    Sleep(50)

    def lambda_2E48():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2E48)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x103,
        (
            "#12P#00202FIf I remember correctly,\x01",
            "he's in the 34F security\x01",
            "planning room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FI really hope nothing\x01",
            "happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10108FI hope so, too.\x02",
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

    # Function_9_2302 end

    def Function_10_2F75(): pass

    label("Function_10_2F75")


    def lambda_2F7A():
        OP_95(0xFE, -20700, -6000, 0, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2F7A)

    def lambda_2F94():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2F94)
    WaitChrThread(0xFE, 1)

    def lambda_2FA9():
        OP_95(0xFE, -23500, -6000, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2FA9)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_10_2F75 end

    def Function_11_2FCA(): pass

    label("Function_11_2FCA")


    def lambda_2FCF():
        OP_95(0xFE, -20700, -6000, 0, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2FCF)

    def lambda_2FE9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2FE9)
    WaitChrThread(0xFE, 1)

    def lambda_2FFE():
        OP_95(0xFE, -23500, -6000, 600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2FFE)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_11_2FCA end

    def Function_12_301F(): pass

    label("Function_12_301F")


    def lambda_3024():
        OP_95(0xFE, -20700, -6000, 0, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3024)

    def lambda_303E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_303E)
    WaitChrThread(0xFE, 1)

    def lambda_3053():
        OP_95(0xFE, -21500, -6000, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3053)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_12_301F end

    def Function_13_3074(): pass

    label("Function_13_3074")


    def lambda_3079():
        OP_95(0xFE, -20700, -6000, 0, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3079)

    def lambda_3093():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3093)
    WaitChrThread(0xFE, 1)

    def lambda_30A8():
        OP_95(0xFE, -21500, -6000, 600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_30A8)
    WaitChrThread(0xFE, 1)
    Sound(107, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    Return()

    # Function_13_3074 end

    def Function_14_30E4(): pass

    label("Function_14_30E4")


    def lambda_30E9():
        OP_95(0xFE, -20700, -6000, 0, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_30E9)

    def lambda_3103():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3103)
    WaitChrThread(0xFE, 1)

    def lambda_3118():
        OP_95(0xFE, -22500, -6000, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3118)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_14_30E4 end

    def Function_15_3139(): pass

    label("Function_15_3139")


    def lambda_313E():
        OP_95(0xFE, -20700, -6000, 0, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_313E)

    def lambda_3158():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3158)
    WaitChrThread(0xFE, 1)

    def lambda_316D():
        OP_95(0xFE, -22500, -6000, -1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_316D)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_15_3139 end

    def Function_16_318E(): pass

    label("Function_16_318E")


    def lambda_3193():
        OP_95(0xFE, -25000, -6000, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3193)

    def lambda_31AD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_31AD)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_16_318E end

    def Function_17_31BE(): pass

    label("Function_17_31BE")

    OP_92(0xFE, 0xFFFF9FE8, 0xFFFFD8F0, 0x1F4)

    def lambda_31D0():
        OP_95(0xFE, -24600, -6000, -10000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_31D0)
    WaitChrThread(0xFE, 1)

    def lambda_31EE():
        OP_95(0xFE, -21000, -4400, -18600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_31EE)
    WaitChrThread(0xFE, 1)

    def lambda_320C():
        OP_95(0xFE, -21000, -4400, -21000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_320C)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_17_31BE end

    def Function_18_3226(): pass

    label("Function_18_3226")

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

    # Function_18_3226 end

    def Function_19_3263(): pass

    label("Function_19_3263")


    def lambda_3268():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0xFFFFE4A8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3268)
    WaitChrThread(0xFE, 1)

    def lambda_3286():
        OP_95(0xFE, -28000, -4400, -32600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3286)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xA0, 0x1F4)
    Return()

    # Function_19_3263 end

    def Function_20_32A7(): pass

    label("Function_20_32A7")


    def lambda_32AC():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0xFFFFE4A8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_32AC)
    WaitChrThread(0xFE, 1)

    def lambda_32CA():
        OP_95(0xFE, -29800, -4400, -32800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_32CA)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xA0, 0x1F4)
    Return()

    # Function_20_32A7 end

    def Function_21_32EB(): pass

    label("Function_21_32EB")


    def lambda_32F0():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0xFFFFE4A8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_32F0)
    WaitChrThread(0xFE, 1)

    def lambda_330E():
        OP_95(0xFE, -28700, -4400, -31400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_330E)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xA0, 0x1F4)
    Return()

    # Function_21_32EB end

    def Function_22_332F(): pass

    label("Function_22_332F")


    def lambda_3334():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0xFFFFE4A8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3334)
    WaitChrThread(0xFE, 1)

    def lambda_3352():
        OP_95(0xFE, -26400, -4400, -31800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3352)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xA0, 0x1F4)
    Return()

    # Function_22_332F end

    def Function_23_3373(): pass

    label("Function_23_3373")


    def lambda_3378():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0xFFFFE4A8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3378)
    WaitChrThread(0xFE, 1)

    def lambda_3396():
        OP_95(0xFE, -30700, -4400, -31900, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3396)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xBE, 0x1F4)
    Return()

    # Function_23_3373 end

    def Function_24_33B7(): pass

    label("Function_24_33B7")


    def lambda_33BC():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0xFFFFE4A8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_33BC)
    WaitChrThread(0xFE, 1)

    def lambda_33DA():
        OP_95(0xFE, -27100, -4400, -30600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_33DA)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xA0, 0x1F4)
    Return()

    # Function_24_33B7 end

    def Function_25_33FB(): pass

    label("Function_25_33FB")


    def lambda_3400():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0xFFFFE4A8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3400)
    WaitChrThread(0xFE, 1)

    def lambda_341E():
        OP_95(0xFE, -29400, -4400, -28800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_341E)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xA0, 0x1F4)
    Return()

    # Function_25_33FB end

    def Function_26_343F(): pass

    label("Function_26_343F")

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

    def lambda_37D1():
        OP_96(0xFE, 0x2AF8, 0x9C40, 0x0, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_37D1)

    def lambda_37EB():
        OP_96(0xFE, 0xFFFFD508, 0xA410, 0x0, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_37EB)
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

    # Function_26_343F end

    def Function_27_39C6(): pass

    label("Function_27_39C6")

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

    # Function_27_39C6 end

    def Function_28_3A26(): pass

    label("Function_28_3A26")

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

    # Function_28_3A26 end

    def Function_29_3A86(): pass

    label("Function_29_3A86")


    def lambda_3A8B():
        OP_95(0xFE, -12600, 3300, -3000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3A8B)

    def lambda_3AA5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3AA5)
    WaitChrThread(0xFE, 1)

    def lambda_3ABA():
        OP_95(0xFE, -12000, 3300, -4800, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3ABA)
    WaitChrThread(0xFE, 1)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(809, 0, 30, 0)

    def lambda_3AE9():
        OP_9D(0xFE, 0xFFFFD440, 0x0, 0xFFFFDA80, 0x320, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3AE9)
    WaitChrThread(0xFE, 1)
    Sound(326, 0, 40, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3B1B():
        OP_95(0xFE, 0, 0, -18500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3B1B)
    WaitChrThread(0xFE, 1)

    def lambda_3B39():
        OP_95(0xFE, 0, 0, -22000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3B39)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x4)

    def lambda_3B5C():
        OP_9E(0xFE, 0x0, 0x0, 0x15F90, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3B5C)
    WaitChrThread(0xFE, 1)

    def lambda_3B7B():
        OP_95(0xFE, -18000, -6000, 0, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3B7B)
    Sleep(500)

    def lambda_3B98():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3B98)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_29_3A86 end

    def Function_30_3BA9(): pass

    label("Function_30_3BA9")


    def lambda_3BAE():
        OP_95(0xFE, 8400, 4000, 4400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3BAE)
    WaitChrThread(0xFE, 1)

    def lambda_3BCC():
        OP_95(0xFE, 6800, 4000, -1300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3BCC)
    WaitChrThread(0xFE, 1)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3BF5():
        OP_9D(0xFE, 0x11F8, 0x0, 0xFFFFE890, 0xBE, 0x320)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3BF5)
    WaitChrThread(0xFE, 1)
    Sound(326, 0, 40, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3C27():
        OP_95(0xFE, 0, 0, -18500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3C27)
    WaitChrThread(0xFE, 1)

    def lambda_3C45():
        OP_95(0xFE, 0, 0, -22000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3C45)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x4)

    def lambda_3C68():
        OP_9E(0xFE, 0x0, 0x0, 0x15F90, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3C68)
    WaitChrThread(0xFE, 1)

    def lambda_3C87():
        OP_95(0xFE, -18000, -6000, 0, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3C87)
    Sleep(500)

    def lambda_3CA4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3CA4)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_30_3BA9 end

    def Function_31_3CB5(): pass

    label("Function_31_3CB5")


    def lambda_3CBA():
        OP_D5(0xFE, 0x0, 0x2E630, 0x0, 0xED8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3CBA)

    def lambda_3CD3():
        OP_D5(0xFE, 0x0, 0x2E630, 0x0, 0xED8)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_3CD3)

    def lambda_3CEC():
        OP_96(0xFE, 0x2710, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3CEC)
    Sleep(2800)

    def lambda_3D09():
        OP_96(0xFE, 0x2710, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D09)
    Sleep(300)

    def lambda_3D26():
        OP_96(0xFE, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D26)
    Sleep(300)

    def lambda_3D43():
        OP_96(0xFE, 0x2710, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D43)
    Sleep(300)

    def lambda_3D60():
        OP_96(0xFE, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D60)
    WaitChrThread(0xFE, 1)
    ClearMapObjFlags(0x7, 0x20)
    OP_74(0x7, 0x0)
    Return()

    # Function_31_3CB5 end

    def Function_32_3D84(): pass

    label("Function_32_3D84")


    def lambda_3D89():
        OP_D5(0xFE, 0x0, 0x29810, 0x0, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3D89)

    def lambda_3DA2():
        OP_D5(0xFE, 0x0, 0x29810, 0x0, 0xDAC)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_3DA2)

    def lambda_3DBB():
        OP_96(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3DBB)
    Sleep(2500)

    def lambda_3DD8():
        OP_96(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3DD8)
    Sleep(300)

    def lambda_3DF5():
        OP_96(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3DF5)
    Sleep(300)

    def lambda_3E12():
        OP_96(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E12)
    Sleep(300)

    def lambda_3E2F():
        OP_96(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E2F)
    WaitChrThread(0xFE, 1)
    ClearMapObjFlags(0x6, 0x20)
    OP_74(0x6, 0x0)
    Return()

    # Function_32_3D84 end

    def Function_33_3E53(): pass

    label("Function_33_3E53")

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
        "#11P#00105FMy...\x02",
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
            "#12P#10102FLooks like the rain let\x01",
            "up a little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FYeah... And the view is\x01",
            "just as awesome as it\x01",
            "ever was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00002FYeah. It'd be even\x01",
            "better on a clear day,\x01",
            "though...\x02",
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
            "#11P#00005FI wonder where Jona and\x01",
            "the Chief are?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_415F():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_415F)
    Sleep(50)

    def lambda_416F():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_416F)
    Sleep(50)

    def lambda_417F():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_417F)
    Sleep(50)

    def lambda_418F():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_418F)
    Sleep(50)

    def lambda_419F():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_419F)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)

    ChrTalk(
        0x103,
        (
            "#12P#00204FProbably on a corner of\x01",
            "the roof.\x02",
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

    # Function_33_3E53 end

    def Function_34_424C(): pass

    label("Function_34_424C")

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

    def lambda_44A2():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_44A2)

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

    def lambda_45CB():
        OP_97(0x101, 0x11F8, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_45CB)
    Sleep(100)

    def lambda_45E8():
        OP_97(0x103, 0x11F8, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_45E8)
    Sleep(100)

    def lambda_4605():
        OP_97(0x104, 0x11F8, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4605)
    Sleep(100)

    def lambda_4622():
        OP_97(0x102, 0x11F8, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4622)
    Sleep(100)

    def lambda_463F():
        OP_97(0x105, 0x11F8, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_463F)
    Sleep(100)

    def lambda_465C():
        OP_97(0x109, 0x11F8, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_465C)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x101,
        (
            "#00002F#5PSo this is the equipment\x01",
            "for detecting the alert\x01",
            "signal, huh...\x02",
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
        (
            "#12PThat's where Tio comes\x01",
            "in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#00204FNo problems here.\x02\x03",
            "#00200FBut... Will it be okay\x01",
            "with the effect of the\x01",
            "rain?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12PIt's just light rain. I\x01",
            "don't think there will\x01",
            "be much effect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12PBut I cannot bring myself\x01",
            "to expose my precious Tio\x01",
            "to the wind and rain...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12PThat's right, how about I hold\x01",
            "my umbrella over you while you\x01",
            "startup your sensors─\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#00203FI'm fine. On the\x01",
            "contrary, that will be\x01",
            "distracting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#12PUgh...\x02",
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
            "#02303F#5P─Alright. Ready on my\x01",
            "end.\x02\x03",
            "#02300FWe're ready for Aeon\x01",
            "startup anytime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#00204FThen let's begin.\x02\x03",
            "#00200FHave you input Ling and\x01",
            "Eolia's ENIGMA Ⅱ serial\x01",
            "numbers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12PYeah, I got them from\x01",
            "the Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#12PI've already input them\x01",
            "into the instrument.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5P#00202FRoger.\x02",
    )

    CloseMessageWindow()

    def lambda_4AA5():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4AA5)
    Sleep(50)

    def lambda_4AB5():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4AB5)
    Sleep(50)

    def lambda_4AC5():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4AC5)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)

    def lambda_4AE1():

        label("loc_4AE1")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_4AE1")

    QueueWorkItem2(0x101, 2, lambda_4AE1)

    def lambda_4AF3():

        label("loc_4AF3")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_4AF3")

    QueueWorkItem2(0x102, 2, lambda_4AF3)

    def lambda_4B05():

        label("loc_4B05")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_4B05")

    QueueWorkItem2(0x109, 2, lambda_4B05)

    def lambda_4B17():

        label("loc_4B17")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_4B17")

    QueueWorkItem2(0x105, 2, lambda_4B17)

    def lambda_4B29():

        label("loc_4B29")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_4B29")

    QueueWorkItem2(0x104, 2, lambda_4B29)

    def lambda_4B3B():

        label("loc_4B3B")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_4B3B")

    QueueWorkItem2(0xB, 2, lambda_4B3B)
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
            "Ling and Eolia for us.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0x15E, 0x1F4)
    Sleep(100)

    ChrTalk(
        0x103,
        "#6P#00202FI will. Here I go─\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xBB8)
    OP_92(0x103, 0x6C98, 0xFFFF8C60, 0x1F4)
    OP_68(28160, -3400, -29390, 2000)

    def lambda_4BFE():
        OP_95(0xFE, 27800, -4400, -29600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4BFE)
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

    def lambda_4C4F():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_4C4F)
    Sleep(500)
    Sound(2280, 255, 100, 0)

    ChrTalk(
        0x103,
        (
            "#5P#00203F#30W─Aeon system, activate.\x02\x03",
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
            "#02304F#6P─Link confirmed.\x02\x03",
            "#02302FAt this rate it looks\x01",
            "like there will be no\x01",
            "problems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5POrbal power to the\x01",
            "instrument stable at\x01",
            "high output.\x02",
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
        "#5P#00203FRoger─ Here I go.\x02",
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
        (
            "#5P#00201F#2683V#40W#20AUnlocking sensor\x01",
            "functions...\x02",
        )
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
        "#00305F#6POh!\x02",
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
            "#10305F#6PIt looked like some kind\x01",
            "of "wave" was sent out,\x01",
            "but...\x02",
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
        "#6P#00206F...Hmm.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PYes, yes, it looks like\x01",
            "a success.\x02",
        )
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

    def lambda_5189():
        TurnDirection(0x101, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5189)
    Sleep(50)

    def lambda_5199():
        TurnDirection(0x102, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5199)
    Sleep(50)

    def lambda_51A9():
        TurnDirection(0x104, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_51A9)
    Sleep(50)

    def lambda_51B9():
        TurnDirection(0x109, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_51B9)
    Sleep(50)

    def lambda_51C9():
        TurnDirection(0x105, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_51C9)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#5P#00007FReally!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#5PYou know the location of\x01",
            "Ling and Eolia!?\x02",
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
            "#12PHmm, well to be accurate,\x01",
            "it's actually the location\x01",
            "of their ENIGMA Ⅱ units.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    ChrTalk(
        0x103,
        (
            "#6P#00203FI sensed the two alert\x01",
            "signals too.\x02\x03",
            "#00201FFar to the south of\x01",
            "here, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#02302F#6PAnalyzing obtained data\x01",
            "and displaying on map...\x02\x03",
            "#02309F(*typing*) ─There, it's\x01",
            "done.\x02",
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
            "#10101FThis is... The south\x01",
            "side of Elm Lake!?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 20, -1, -1)

    AnonymousTalk(
        0x104,
        (
            "#00301FWhat in the world... Is\x01",
            "there even anything\x01",
            "there?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(20, 80, -1, -1)

    AnonymousTalk(
        0x102,
        (
            "#00108FIt's a marshy area\x01",
            "untouched by human hands\x01",
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
            "#10301FSo those bracer ladies\x01",
            "are in a place like\x01",
            "that, huh...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(220, 180, -1, -1)

    AnonymousTalk(
        0xA,
        (
            "#02305FI don't really get it,\x01",
            "but it's not normal,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(220, 60, -1, -1)

    AnonymousTalk(
        0xB,
        (
            "Hmm, this is\x01",
            "concerning...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(120, 120, -1, -1)

    AnonymousTalk(
        0x103,
        "#00208FLloyd...\x02",
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
            "#11P#00003F─For now, let's report\x01",
            "this to Michel.\x02\x03",
            "#00001FAnd just in case, we\x01",
            "should ask HQ to prepare\x01",
            "a boat for us.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_572B():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_572B)
    Sleep(50)

    def lambda_573B():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_573B)
    Sleep(50)

    def lambda_574B():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_574B)
    Sleep(50)

    def lambda_575B():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_575B)
    Sleep(50)

    def lambda_576B():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_576B)
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
            "situation, we've got to\x01",
            "hurry!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_57EE():
        TurnDirection(0x101, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_57EE)
    Sleep(50)

    def lambda_57FE():
        TurnDirection(0x102, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_57FE)
    Sleep(50)

    def lambda_580E():
        TurnDirection(0x103, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_580E)
    Sleep(50)

    def lambda_581E():
        TurnDirection(0x104, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_581E)
    Sleep(50)

    def lambda_582E():
        TurnDirection(0x109, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_582E)
    Sleep(50)

    def lambda_583E():
        TurnDirection(0x105, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_583E)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x101,
        (
            "#6P#00000FThank you for your\x01",
            "cooperation, Chief\x01",
            "Roberts and Jona.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_58AA():
        TurnDirection(0xB, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_58AA)
    Sleep(50)

    def lambda_58BA():
        TurnDirection(0xA, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_58BA)
    Sleep(50)
    WaitChrThread(0xB, 0)
    WaitChrThread(0xA, 0)

    ChrTalk(
        0xB,
        (
            "#5PDon't mention it. You\x01",
            "can leave the cleanup to\x01",
            "us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#02302F#11PWell, be careful at\x01",
            "least~.\x02",
        )
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

    # Function_34_424C end

    def Function_35_5970(): pass

    label("Function_35_5970")

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

    # Function_35_5970 end

    def Function_36_5A68(): pass

    label("Function_36_5A68")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5A86")
    SetChrSubChip(0xFE, 0x4)
    Sleep(90)
    SetChrSubChip(0xFE, 0x5)
    Sleep(90)
    Jump("Function_36_5A68")

    label("loc_5A86")

    Return()

    # Function_36_5A68 end

    def Function_37_5A87(): pass

    label("Function_37_5A87")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5AA5")
    SetChrSubChip(0xFE, 0x0)
    Sleep(90)
    SetChrSubChip(0xFE, 0x1)
    Sleep(90)
    Jump("Function_37_5A87")

    label("loc_5AA5")

    Return()

    # Function_37_5A87 end

    def Function_38_5AA6(): pass

    label("Function_38_5AA6")

    Sound(943, 2, 50, 0)
    OP_71(0x8, 0x29, 0x32, 0x0, 0x0)
    OP_79(0x8)
    Sound(311, 0, 50, 0)
    PlayEffect(0x3, 0x2, 0xFF, 0x0, 29400, -4400, -26600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_71(0x8, 0x32, 0x59, 0x0, 0x20)
    Return()

    # Function_38_5AA6 end

    def Function_39_5B05(): pass

    label("Function_39_5B05")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5B23")
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_39_5B05")

    label("loc_5B23")

    Return()

    # Function_39_5B05 end

    def Function_40_5B24(): pass

    label("Function_40_5B24")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5B6B")
    Sound(1021, 0, 100, 0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x12C, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(500)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x12C, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Jump("Function_40_5B24")

    label("loc_5B6B")

    Return()

    # Function_40_5B24 end

    def Function_41_5B6C(): pass

    label("Function_41_5B6C")

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

    # Function_41_5B6C end

    def Function_42_5BB9(): pass

    label("Function_42_5BB9")

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
        "#11302F#6POhh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#04500F#6POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#01605F#6PShorty, you...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#04602F#6P#NWow. Aren't we kind of\x01",
            "awesome?\x02",
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
            "#11304F#6PKeA─ No, perhaps I should\x01",
            "call you the Divine Child\x01",
            "as the Cult once did.\x02\x03",
            "#11302FWell done. Once again,\x01",
            "you have appeared in this\x01",
            "world.\x02\x03",
            "It is my honor to welcome\x01",
            "you as the current head\x01",
            "of the Crois family.\x02",
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
            "#10804F#11PHaha. I think that's all\x01",
            "for the greetings.\x02\x03",
            "#10802FI think it's about time\x01",
            "they received a little\x01",
            "gift.\x02",
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
            "Haha, so it seems my\x01",
            "hard work has finally\x01",
            "paid off.\x02",
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

    def lambda_6600():
        TurnDirection(0xC, 0x14, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_6600)
    Sleep(50)

    def lambda_6610():
        TurnDirection(0x11, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_6610)
    Sleep(50)

    def lambda_6620():
        TurnDirection(0x10, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_6620)
    Sleep(50)

    def lambda_6630():
        TurnDirection(0xD, 0x14, 500)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_6630)
    Sleep(50)

    def lambda_6640():
        TurnDirection(0xE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_6640)
    Sleep(50)

    def lambda_6650():
        TurnDirection(0xF, 0x14, 500)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_6650)
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
            "#6P#04900F#3CInheritor of the great Sept-\x01",
            "Terrion, I beg of thee...\x02\x03",
            "Allow me to congratulate you on\x01",
            "your manifestation in the stead\x01",
            "of the leader of Ouroboros.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#04704F#6PHaha, it may be meager,\x01",
            "but I have prepared a\x01",
            ""gift" for you.\x02\x03",
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

    def lambda_6883():
        TurnDirection(0xC, 0x10, 0)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_6883)
    Sleep(0)

    def lambda_6893():
        TurnDirection(0xD, 0x10, 0)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_6893)
    Sleep(0)

    def lambda_68A3():
        TurnDirection(0xE, 0x10, 0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_68A3)
    Sleep(0)

    def lambda_68B3():
        TurnDirection(0xF, 0x10, 0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_68B3)
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
        "#01607F#6PT-This is...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#04612F#12PWoah! So cool!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#04502F#12PHehe... Nice toys you've\x01",
            "got there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#10804F#12P#NAions, the "God\x01",
            "Machines"...\x02\x03",
            "#10800FThree interfaces the\x01",
            "Sept-Terrion uses to\x01",
            "create its miracles...\x02",
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
        (
            "#11P#11304F#12P...They're better made\x01",
            "than I expected.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x13, 500)

    ChrTalk(
        0xC,
        (
            "#11P#11300FLadies and gentlemen of\x01",
            "Ouroboros. It seems I am\x01",
            "in your debt.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6D96():
        TurnDirection(0x13, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_6D96)
    Sleep(50)

    def lambda_6DA6():
        TurnDirection(0x12, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_6DA6)
    Sleep(50)

    def lambda_6DB6():
        TurnDirection(0x14, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_6DB6)
    Sleep(50)
    WaitChrThread(0x13, 0)
    WaitChrThread(0x12, 0)
    WaitChrThread(0x14, 0)

    def lambda_6DD2():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_6DD2)

    ChrTalk(
        0x13,
        (
            "#5P#04709F#6PHaha, well on our side,\x01",
            "we're always grateful for\x01",
            "your financial assistance.\x02\x03",
            "#04702FBeing able to use that\x01",
            "Gordias-class data\x01",
            "especially was a great help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#04900F#3C#6P#NAnd this time, our\x01",
            "Grandmaster's will will\x01",
            "be done.\x02\x03",
            "There is no need to\x01",
            "consider this a debt.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x11,
        (
            "#10809F#11PUhuhu... You're quite\x01",
            "generous.\x02\x03",
            "#10802F─KeA. Will you do the\x01",
            "honors?\x02",
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

    def lambda_7055():
        OP_93(0xC, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_7055)
    Sleep(50)

    def lambda_7065():
        OP_93(0x11, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_7065)
    Sleep(50)

    def lambda_7075():
        OP_93(0x13, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_7075)
    Sleep(50)

    def lambda_7085():
        OP_93(0x12, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_7085)
    Sleep(50)

    def lambda_7095():
        OP_93(0x14, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_7095)
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

    # Function_42_5BB9 end

    def Function_43_7106(): pass

    label("Function_43_7106")

    OP_68(0, 2900, 3000, 1500)
    SetCameraDistance(23000, 1500)
    Sound(935, 0, 100, 0)

    def lambda_712B():
        OP_96(0xFE, 0xFFFFE4A8, 0x7D0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_712B)
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

    def lambda_73F6():
        OP_9F(0x2, 0x29, 20000, 0x6)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_73F6)
    Sleep(1000)

    def lambda_7408():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_7408)
    Sleep(300)

    def lambda_7418():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_7418)
    OP_6F(0x41)
    Return()

    # Function_43_7106 end

    def Function_44_7423(): pass

    label("Function_44_7423")

    Sound(978, 0, 50, 0)
    OP_25(0x3D3, 0x64)
    OP_71(0xA, 0x5A, 0x33, 0x0, 0x0)

    def lambda_743E():
        OP_96(0xFE, 0x2328, 0x3E8, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_743E)
    WaitChrThread(0x2A, 1)
    OP_79(0xA)
    OP_71(0xA, 0xA, 0x32, 0x0, 0x20)
    Sleep(2000)
    OP_9F(0x0, 0x2A)
    OP_9F(0x1, -5000, 3000, -3000)
    OP_9F(0x1, -20000, 4000, -6000)
    OP_9F(0x1, -200000, 7000, -7000)

    def lambda_749C():
        OP_9F(0x2, 0x2A, 10000, 0x6)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_749C)
    Sleep(1000)

    def lambda_74AE():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_74AE)
    Sleep(100)

    def lambda_74BE():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_74BE)
    Sleep(100)

    def lambda_74CE():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_74CE)
    Return()

    # Function_44_7423 end

    def Function_45_74D7(): pass

    label("Function_45_74D7")

    PlayEffect(0x1, 0xFF, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1800)

    def lambda_7516():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7516)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_45_74D7 end

    def Function_46_7527(): pass

    label("Function_46_7527")

    PlayEffect(0x2, 0xFF, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    Sound(936, 0, 80, 0)

    def lambda_756C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_756C)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_46_7527 end

    def Function_47_757D(): pass

    label("Function_47_757D")

    SetChrPos(0x28, 0, 20000, 7000, 180)
    OP_71(0x5, 0x5B, 0x82, 0x0, 0x20)

    def lambda_759F():
        OP_96(0xFE, 0x0, 0x1F4, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_759F)
    WaitChrThread(0xFE, 1)
    OP_71(0x5, 0x83, 0x96, 0x0, 0x0)

    def lambda_75C9():
        OP_96(0xFE, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_75C9)
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

    # Function_47_757D end

    def Function_48_7637(): pass

    label("Function_48_7637")

    SetChrPos(0x29, -7000, 25000, 2000, 135)
    OP_71(0x9, 0xB, 0x32, 0x0, 0x20)

    def lambda_7659():
        OP_96(0xFE, 0xFFFFE4A8, 0x0, 0x7D0, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7659)
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

    # Function_48_7637 end

    def Function_49_76E0(): pass

    label("Function_49_76E0")

    SetChrPos(0x2A, 9000, 28000, 2000, 225)
    OP_71(0xA, 0xA, 0x32, 0x0, 0x20)

    def lambda_7702():
        OP_96(0xFE, 0x2328, 0x3E8, 0x7D0, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7702)
    WaitChrThread(0xFE, 1)
    OP_71(0xA, 0x33, 0x5A, 0x0, 0x0)

    def lambda_772C():
        OP_96(0xFE, 0x2328, 0x0, 0x7D0, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_772C)
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

    # Function_49_76E0 end

    def Function_50_77CB(): pass

    label("Function_50_77CB")

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

    # Function_50_77CB end

    def Function_51_780B(): pass

    label("Function_51_780B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_788D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_783B")
    OP_82(0x0, 0xF, 0xBB8, 0x1F4)
    Jump("loc_7885")

    label("loc_783B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7860")
    OP_82(0x4B, 0x96, 0x1388, 0x1F4)
    Jump("loc_7885")

    label("loc_7860")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7885")
    OP_82(0x19, 0x32, 0x1388, 0x1F4)
    Jump("loc_7885")

    label("loc_7885")

    Sleep(500)
    Jump("Function_51_780B")

    label("loc_788D")

    Return()

    # Function_51_780B end

    def Function_52_788E(): pass

    label("Function_52_788E")

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
            "#04802FThe Sept-Terrion of\x01",
            "Zero... That's very well\x01",
            "said!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#12P#04702FHehe... Operating three\x01",
            "Gordias-class final\x01",
            "forms at the same time!\x02\x03",
            "And to think they can\x01",
            "autonomously create\x01",
            "miracles!\x02\x03",
            "#04709FHaha, that guy gave us\x01",
            "some good info!\x02",
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
            "#11P#04504FHmph... Their power is\x01",
            "certainly great.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#12P#10811FHehe. I presume this is\x01",
            "only the beginning?\x02",
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
            "#11304F#30W─Now, at this very moment, Crossbell\x01",
            "has become holy ground!\x02\x03",
            "#11302FStep aside, Empire and Republic. It\x01",
            "is from this very point that a new\x01",
            "continental order will spring forth!\x02\x03",
            "With the ideals of our Crois clan\x01",
            "and spreading justice throughout the\x01",
            "world at its center!\x02",
        )
    )

    CloseMessageWindow()
    OP_6F(0x79)
    SetCameraDistance(23000, 5000)
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0xBB8)

    ChrTalk(
        0xC,
        "#11309F#5S#40W#30AHAHAHAHAHAHA!\x02",
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

    # Function_52_788E end

    def Function_53_8128(): pass

    label("Function_53_8128")

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
            "#6P#04804FNow then, the stage is set\x01",
            "to carry out our "Phantasmal\x01",
            "Blaze Plan" in the Empire...\x02\x03",
            "#04802FFrom here, we go according\x01",
            "to plan. We'll wait and see\x01",
            "for a while?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#04923FCorrect.\x02\x03",
            "#04921FI will accompany you\x01",
            "until the appropriate\x01",
            "stage in the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#04704F#5PHaha. The present power of the Sept-\x01",
            "Terrion of Zero is comparable to the lost\x01",
            "power of the Sept-Terrion of Mirage.\x02\x03",
            "Furthermore, it has shown abilities the\x01",
            "original did not have...\x02\x03",
            "#04702FHehe. Let's see how far the skills of the\x01",
            "Crois family can carry us.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x13, 500)
    Sleep(100)

    ChrTalk(
        0x14,
        (
            "#12P#04809FUhuhu... You're in a\x01",
            "good mood, professor.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x14, 0x87, 0x1F4)

    ChrTalk(
        0x14,
        (
            "#6P#04805FThat reminds me, it\x01",
            "looks like "they"\x01",
            "finally began to act?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#04924FOn the contrary, this is a\x01",
            "good opportunity.\x02\x03",
            "#04922FTheir position is different\x01",
            "from ours... We should find\x01",
            "out exactly how.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#04700F#5PHaha, I'll leave that to\x01",
            "you guys.\x02\x03",
            "#04704FI'll continue collecting\x01",
            "data on the Sept-Terrion\x01",
            "of Zero here...\x02\x03",
            "#04702F─To see if I can obtain\x01",
            "the ultimate interface\x01",
            "between humans and gods!\x02",
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

    # Function_53_8128 end

    def Function_54_8939(): pass

    label("Function_54_8939")

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

    label("loc_8A2F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8A42")
    Sleep(1)
    Jump("loc_8A2F")

    label("loc_8A42")

    FadeToDark(1000, 0, -1)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_54_8939 end

    def Function_55_8A50(): pass

    label("Function_55_8A50")

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
            "Haha... They've really\x01",
            "done it this time,\x01",
            "haven't they.\x02",
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

    def lambda_8D6E():
        OP_95(0xFE, -26500, -4400, -26500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8D6E)
    WaitChrThread(0x11, 1)

    def lambda_8D8C():
        OP_95(0xFE, -27000, -4400, -29500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8D8C)
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
            "#12308FDieter is looking for\x01",
            "you... Don't you have to\x01",
            "go?\x07\x00\x02",
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
            "Uhuhu. Let father sweat a little\x01",
            "more.\x02\x03",
            "I think the Barrier will be\x01",
            "difficult to deploy without the\x01",
            "resonance of the Bells, right?\x02",
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
            "#11P#12303F#30W...Yes, as I am now.\x02\x03",
            "#12308FAlthough those Aions can\x01",
            "operate, they can't use\x01",
            "the power of Space...\x02\x03",
            "#12315FLloyd and the others.\x01",
            "They're coming.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#6P#02913FHaha, what ever shall I\x01",
            "do?\x02\x03",
            "With this, everything\x01",
            "will go according to\x01",
            "plan.\x02\x03",
            "#02911FAccording to "his" plan.\x02",
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
            "#6P#02902FEverything is up to you,\x01",
            "KeA... You need only\x01",
            "follow orders.\x02\x03",
            "#02903FWill you get off here?\x01",
            "Or will you make\x01",
            "everything come true?\x02\x03",
            "#02912FThe time when you must\x01",
            "choose will be here\x01",
            "soon, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#11P#12304F#40W...Yes.\x02\x03",
            "#12302FAt first, KeA didn't\x01",
            "know whether there was\x01",
            "another path...\x07\x00\x02",
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
            "#11P#12304F#3634V#40W#55AFor Lloyd, Elie, Tio,\x01",
            "Randy, Shizuku, and\x01",
            "everyone else, too...\x07\x00\x02",
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
            "#3635V#40W#45A─I'll definitely make\x01",
            "everything come true.\x07\x00\x02",
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

    # Function_55_8A50 end

    def Function_56_92FA(): pass

    label("Function_56_92FA")

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

    # Function_56_92FA end

    def Function_57_946E(): pass

    label("Function_57_946E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_94AC")
    Sleep(600)
    OP_98(0xFE, 0x0, 0xFFFFF8F8, 0x0, 0x258, 0x1)
    Sleep(600)
    OP_98(0xFE, 0x0, 0x708, 0x0, 0x258, 0x1)
    Jump("Function_57_946E")

    label("loc_94AC")

    Return()

    # Function_57_946E end

    def Function_58_94AD(): pass

    label("Function_58_94AD")

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

    # Function_58_94AD end

    def Function_59_9945(): pass

    label("Function_59_9945")

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

    # Function_59_9945 end

    def Function_60_9974(): pass

    label("Function_60_9974")

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

    # Function_60_9974 end

    def Function_61_9A11(): pass

    label("Function_61_9A11")

    Sleep(2000)
    OP_74(0x9, 0x3)
    OP_71(0x9, 0x104, 0x103, 0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_61_9A11 end

    def Function_62_9A28(): pass

    label("Function_62_9A28")

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
        "#2P#00107F#N"Uncle"!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#1P#00007F#NDieter!\x02",
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

    def lambda_9E26():
        OP_96(0xFE, 0xFFFFFCE0, 0x0, 0xFFFFDECC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9E26)
    Sleep(50)

    def lambda_9E43():
        OP_96(0xFE, 0x320, 0x0, 0xFFFFDECC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9E43)
    Sleep(50)

    def lambda_9E60():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFDA1C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_9E60)
    Sleep(50)

    def lambda_9E7D():
        OP_96(0xFE, 0xFFFFF95C, 0x0, 0xFFFFD8F0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9E7D)

    def lambda_9E97():
        OP_96(0xFE, 0x6A4, 0x0, 0xFFFFD8F0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9E97)

    def lambda_9EB1():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFD5D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_9EB1)
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
            "Haha... It's been a while, ladies\x01",
            "and gentlemen.\x02\x03",
            "However, I don't recall making a\x01",
            "lunch appointment with all of you.\x02\x03",
            "Might you have gotten the time\x01",
            "wrong?\x02",
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
            "#00001F─However, this is a\x01",
            "situation we cannot\x01",
            "overlook.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#N#00206FCancelling the declaration of\x01",
            "independence, and stationing magic\x01",
            "soldiers throughout the city...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00307F#12PFirst off, will you\x01",
            "return KeA to us?\x02",
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
            "#5P#11300FHaha, it seems you all\x01",
            "misunderstand.\x02\x03",
            "It isn't the case that\x01",
            "we're forcing KeA to\x01",
            "cooperate with us, you see.\x02\x03",
            "#11303FExtraordinary difficulties\x01",
            "surround this Crossbell of\x01",
            "ours.\x02\x03",
            "#11301FFor that reason, she is\x01",
            "cooperating with us of her\x01",
            "own free will.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#N#00208FIsn't that...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00106F#12P─You and the others must be inducing her\x01",
            "to cooperate, "uncle".\x02\x03",
            "#00108FManipulating jaegers from the shadows,\x01",
            "causing the attack on Crossbell City,\x01",
            "influencing the independence movement...\x02\x03",
            "#00101FBy freezing Imperial and Republican\x01",
            "assets, you imperiled the continued\x01",
            "existence of Crossbell State.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A4E1")

    ChrTalk(
        0x10A,
        (
            "#00606F#12P#NRegardless of whether your actions\x01",
            "are right are wrong, these actions\x01",
            "can't be forgiven all the same.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A59E")

    label("loc_A4E1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A544")

    ChrTalk(
        0x105,
        (
            "#10404F#12P#NWell, people rarely go\x01",
            "to such extremes to stir\x01",
            "up trouble.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A59E")

    label("loc_A544")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A59E")

    ChrTalk(
        0x109,
        (
            "#10106F#12P#N...Right or wrong, you\x01",
            "can't be forgiven just\x01",
            "the same.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A59E")

    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A61B")

    ChrTalk(
        0x106,
        (
            "#10708F#12P#NAnd you took that situation\x01",
            "you created, thrust it at\x01",
            "KeA and forced her decision.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A6E0")

    label("loc_A61B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A685")

    ChrTalk(
        0x109,
        (
            "#10108F#12P#NAnd you'd create a\x01",
            "situation like this just\x01",
            "to get KeA's consent!?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A6E0")

    label("loc_A685")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A6E0")

    ChrTalk(
        0x105,
        (
            "#10408F#12P#NAnd you thrust that\x01",
            "situation at KeA to get\x01",
            "her consent.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A6E0")

    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00301F#12PIsn't that a little too dirty\x01",
            "for a white-toothed, middle\x01",
            "aged salesman such as yourself?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12PPresident Dieter... No,\x01",
            "I should just call you\x01",
            "Dieter.\x02\x03",
            "#00013FIs this the "justice"\x01",
            "you spoke of?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5P#11304FYes─ Exactly right.\x02",
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
            "It just moves too slowly to get\x01",
            "anything done.\x02\x03",
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
        "#00007F#12P#NWhat is your point!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00108F#12P#NDoes that justify what\x01",
            "you all are doing?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xC,
        (
            "#11304FNothing is "justified". Justice is\x01",
            "something that's "done" with power and\x01",
            "will.\x02\x03",
            "#11300FThough I am the current head of the Crois\x01",
            "family, I wasn't all that enthusiastic\x01",
            "about our family's mission at first.\x02\x03",
            "Incidentally, my daughter knows much more\x01",
            "about it.\x02\x03",
            "#11303F─But, once I realized the new Sept-\x01",
            "Terrion my ancestors dreamed of could\x01",
            "actually be realized...\x02\x03",
            "I was ecstatic, and thankful for having\x01",
            "been born into this family.\x02\x03",
            "#11302FFor I have obtained the power to govern\x01",
            "this period of upheaval, and spread\x01",
            "justice throughout the land.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F#12P#NJustice...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        (
            "#00011F#12P#NThen, you are...\x02\x03",
            "#00006FSo you're doing it neither\x01",
            "for yourself nor out of a\x01",
            "desire for control...?\x02\x03",
            "#00010FYou mean to tell me you've\x01",
            "gone this far to bring\x01",
            "about Justice?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xC,
        (
            "#11309FHaha. What other reason would there\x01",
            "be?\x02\x03",
            "#11300F10 years ago, when IBC first became\x01",
            "the entity with the most assets on the\x01",
            "continent, I had no need for wealth.\x02\x03",
            "Rule the continent? I have no interest\x01",
            "in such anachronistic fantasies.\x02\x03",
            "#11306FBut I─ I could no longer stand it.\x02\x03",
            "Trapped in the framework called\x01",
            ""nations", futile struggles are\x01",
            "unfolding in this world.\x02\x03",
            "#11303FFor this reason I did not seek to\x01",
            "create a sovereign nation.\x02\x03",
            "And I don't care about the invalidity\x01",
            "Chairman MacDowell declared, either.\x02\x03",
            "#11301F─In order for me to spread Justice\x01",
            "throughout the world...\x02\x03",
            "#11302FIn the name of that Justice, I am\x01",
            "imposing order, to create that\x01",
            "peaceful world!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B042")

    ChrTalk(
        0x10A,
        "#00610F#12P#N...How foolish.\x02",
    )

    CloseMessageWindow()

    label("loc_B042")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B075")

    ChrTalk(
        0x105,
        "#10401F#12P#NAre you serious?\x02",
    )

    CloseMessageWindow()

    label("loc_B075")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B0C3")

    ChrTalk(
        0x109,
        (
            "#10106F#12P#NI-I don't have any\x01",
            "sympathy for you, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B0C3")

    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B10C")

    ChrTalk(
        0x106,
        (
            "#10706F#12P#N...A simple fantasy is\x01",
            "all I heard.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B10C")

    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00306F#12P#NMan... Until now, I\x01",
            "didn't think you were\x01",
            "serious.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#00208F#12P#N...But if that illusory\x01",
            "Justice could be\x01",
            "realized...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00106F#12P#NThat's right. If he has KeA, the\x01",
            "Sept-Terrion of Zero...\x02\x03",
            "#00108F...He could discard existing\x01",
            "political rules and create any he\x01",
            "wanted. I'd have to call it cheating.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00008F#12P#N#30W...............\x02",
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
            "#00006F#11PDieter.\x02\x03",
            "We've learned many things\x01",
            "from you.\x02\x03",
            "#00001FHowever, regarding\x01",
            "Justice... It seems you are\x01",
            "overvaluing it just a bit.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xC,
        "#6P#11301F...............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008FEach of us are police officers.\x01",
            "Furthermore, we're assigned to\x01",
            "the Special Support Section.\x02\x03",
            "#00003FWe embody Justice by supporting\x01",
            "the citizens while following\x01",
            "our laws and rules.\x02\x03",
            "#00001FHowever... We are not always\x01",
            "right. We've lost our way many\x01",
            "times, actually.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B558")

    ChrTalk(
        0x10A,
        (
            "#11P#00603F...Naturally. Maintaining\x01",
            "order and security isn't\x01",
            "always the right answer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B558")


    ChrTalk(
        0x102,
        (
            "#11P#00106F...That's right. Our\x01",
            "positions on how Justice\x01",
            "should be are very different.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#11P#00204FThough we lose our way and\x01",
            "make mistakes sometimes,\x01",
            "we still pursue Justice...\x02\x03",
            "#00202FThat's something you once\x01",
            "told us, isn't it, Dieter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00302FIsn't what you're doing\x01",
            "totally different from the\x01",
            "lecture you gave us back then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#11303F...That is a methodology\x01",
            "to follow when one's power\x01",
            "and will are insufficient.\x02\x03",
            "But once one has those, to\x01",
            "not bring about Justice...\x02\x03",
            "#11301FIs that not "laziness"?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#00013F#4S#11PNo!\x02",
    )

    CloseMessageWindow()

    def lambda_B796():
        OP_96(0xFE, 0xFFFFFCE0, 0x0, 0xFFFFE2B4, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B796)
    WaitChrThread(0x101, 1)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#00003F#11PJustice changes easily and has\x01",
            "no definite form.\x02\x03",
            "And the pursuit of it has\x01",
            "value to everyone!\x02\x03",
            "#00007FYou are trying to turn Justice\x01",
            "into a standardized mold, and\x01",
            "force everyone into it!\x02\x03",
            "Is that sort of thing really\x01",
            "the Justice you seek!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#11310FGh...\x02\x03",
            "#11307FActually, I've breathed new life\x01",
            "into the Crossbell political system\x01",
            "and implemented several reforms!\x02\x03",
            "Do you deny that!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00106FThat is a different matter.\x02\x03",
            "#00108FWe don't intend to deny your\x01",
            "accomplishments. Actually,\x01",
            "we learned a lot from you.\x02\x03",
            "#00101FThat's why... we must point\x01",
            "out your deceit and\x01",
            "misunderstandings.\x02\x03",
            "#00107FAs someone I respect... I\x01",
            "want you to understand your\x01",
            "own failings!\x02",
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

    def lambda_BBF1():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_BBF1)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_BC16():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_BC16)
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BD20")

    AnonymousTalk(
        0x105,
        (
            "#10407FThis is... Orbal\x01",
            "energy!?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BD9F")

    label("loc_BD20")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BD5B")

    AnonymousTalk(
        0x106,
        (
            "#10707FThis is... Orbal\x01",
            "energy!?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BD9F")

    label("loc_BD5B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BD9F")

    AnonymousTalk(
        0x109,
        (
            "#10107FOrbal arts... ─No, this\x01",
            "is different!?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BD9F")

    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(0, 250, -1, -1)

    AnonymousTalk(
        0x103,
        (
            "#00201FBe careful!\x02\x03",
            "Vast spiritual power is\x01",
            "gathering at the center\x01",
            "of Orchis Tower!\x02",
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
            "#11304FHehe. It's not on the level of Bell,\x01",
            "but as head of the Crois family, I\x01",
            "can do at least this much...\x02\x03",
            "#11300FAnd, if I use the "Soul Conversion\x01",
            "Function" of Orchis Tower─\x02",
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

    def lambda_BF56():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_BF56)
    StopEffect(0x0, 0x2)
    WaitChrThread(0xC, 2)
    OP_68(0, 4000, 5000, 3000)
    SetChrFlags(0xC, 0x20)

    def lambda_BF84():
        OP_96(0xFE, 0x0, 0xFA0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_BF84)
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C007")

    ChrTalk(
        0x10A,
        "#00605FHe was sucked inside!?\x02",
    )

    CloseMessageWindow()
    Jump("loc_C070")

    label("loc_C007")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C03D")

    ChrTalk(
        0x109,
        "#10111FH-He was sucked in!?\x02",
    )

    CloseMessageWindow()
    Jump("loc_C070")

    label("loc_C03D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C070")

    ChrTalk(
        0x106,
        "#10712FHe was sucked inside!?\x02",
    )

    CloseMessageWindow()

    label("loc_C070")

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
            "#30WMmm... Vision and\x01",
            "control nominal.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30WWith the power of the Sept-\x01",
            "Terrion, it seems I'm able\x01",
            "to control it at will.\x07\x00\x02",
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

    def lambda_C1A2():
        OP_97(0x101, 0x0, 0x0, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_C1A2)
    Sleep(50)

    def lambda_C1BF():
        OP_97(0x102, 0x0, 0x0, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_C1BF)
    Sleep(50)

    def lambda_C1DC():
        OP_97(0x103, 0x0, 0x0, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_C1DC)
    Sleep(50)

    def lambda_C1F9():
        OP_97(0x104, 0x0, 0x0, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_C1F9)
    Sleep(50)

    def lambda_C216():
        OP_97(0xF4, 0x0, 0x0, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_C216)
    Sleep(50)

    def lambda_C233():
        OP_97(0xF5, 0x0, 0x0, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_C233)
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
            "#00207F#6P#NHe's controlling the\x01",
            "doll's weapons from the\x01",
            "spiritual plane?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00310F#12P#NWhoa, is that even\x01",
            "possible!?\x02",
        )
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
            "#18AHaha, this white Aion is the\x01",
            "embodiment of the Justice I\x01",
            "will bring upon the world...\x02",
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
            "#16ACome── I shall prove it\x01",
            "to you.\x02",
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
            "#20AOf my Justice and your\x01",
            "Justice... I'll show you\x01",
            "which of them is correct!\x07\x00\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C5EF")
    Sound(540, 0, 50, 0)

    label("loc_C5EF")

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
            "#00107F#12P#NWe'll challenge you with\x01",
            "our full strength!\x02",
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

    # Function_62_9A28 end

    def Function_63_C688(): pass

    label("Function_63_C688")

    OP_71(0x5, 0x442, 0x492, 0x0, 0x0)
    Sleep(200)
    Sound(905, 0, 100, 0)
    Sleep(1000)
    Sound(905, 0, 100, 0)
    OP_79(0x5)
    OP_71(0x5, 0x406, 0x42E, 0x0, 0x20)
    Return()

    # Function_63_C688 end

    def Function_64_C6B6(): pass

    label("Function_64_C6B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C6CE")
    LoadChrToIndex("chr/ch03150.itc", 0x23)

    label("loc_C6CE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C6E6")
    LoadChrToIndex("chr/ch03250.itc", 0x23)

    label("loc_C6E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C6FE")
    LoadChrToIndex("chr/ch02950.itc", 0x23)

    label("loc_C6FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C716")
    LoadChrToIndex("chr/ch00950.itc", 0x23)

    label("loc_C716")

    Return()

    # Function_64_C6B6 end

    def Function_65_C717(): pass

    label("Function_65_C717")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C72F")
    LoadChrToIndex("chr/ch03150.itc", 0x24)

    label("loc_C72F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C747")
    LoadChrToIndex("chr/ch03250.itc", 0x24)

    label("loc_C747")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C75F")
    LoadChrToIndex("chr/ch02950.itc", 0x24)

    label("loc_C75F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C777")
    LoadChrToIndex("chr/ch00950.itc", 0x24)

    label("loc_C777")

    Return()

    # Function_65_C717 end

    def Function_66_C778(): pass

    label("Function_66_C778")

    Sound(922, 0, 100, 0)
    Sound(927, 2, 100, 0)
    Sound(933, 2, 100, 0)
    Sound(943, 2, 100, 0)
    Sleep(1000)
    OP_24(0x3AF)
    Sound(143, 0, 50, 0)
    Return()

    # Function_66_C778 end

    def Function_67_C79D(): pass

    label("Function_67_C79D")

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
        "#00000F#12PD-Did we do it!?\x02",
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
        "#00110F#12PNo way!\x02",
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
            "#30WHehe, thanks to the Sept-Terrion\x01",
            "of Zero, this machine has been\x01",
            "granted limitless energy!\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30WUnless completely\x01",
            "destroyed, defeating it\x01",
            "is impossible.\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CCEA")

    ChrTalk(
        0x10A,
        (
            "#00610F#12P#NSo that's how it is,\x01",
            "eh...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_CCEA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CD25")

    ChrTalk(
        0x105,
        "#10410F#12P#NThis is too unfair...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_CD25")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CD6A")

    ChrTalk(
        0x109,
        (
            "#10110F#12P#NGuh... There has to be a\x01",
            "way...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_CD6A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CDAF")

    ChrTalk(
        0x106,
        (
            "#10708F#12P#N(...We must find its\x01",
            "weakness!)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_CDAF")

    Sleep(500)
    Sound(955, 0, 100, 0)
    SetMessageWindowPos(10, 70, -1, -1)
    SetChrName("Dieter's Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30WHehe. I do not intend to\x01",
            "take your lives.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30WIf you'll surrender\x01",
            "peacefully, and cooperate\x01",
            "with my ideals─\x07\x00\x02",
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
            "W-What!?\x07\x00\x02",
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
            "#00205F#12P#NHas his supply of\x01",
            "spiritual energy ceased?\x02",
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

    def lambda_D203():
        OP_96(0xFE, 0x0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_D203)
    WaitChrThread(0xC, 1)

    def lambda_D221():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_D221)
    WaitChrThread(0xC, 2)
    StopEffect(0x1, 0x2)
    StopSound(950, 1000, 30)
    StopSound(933, 1000, 100)
    Sound(935, 0, 100, 0)
    OP_6F(0x79)
    Sleep(800)

    ChrTalk(
        0xC,
        "#11310F#5PThis, this cannot be!\x02",
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

    # Function_67_C79D end

    def Function_68_D2A7(): pass

    label("Function_68_D2A7")

    Sound(943, 2, 50, 0)
    Sleep(1500)
    OP_24(0x3AF)
    Sound(143, 0, 60, 0)
    Return()

    # Function_68_D2A7 end

    def Function_69_D2BA(): pass

    label("Function_69_D2BA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D2EE")
    Sound(203, 0, 50, 0)
    Sleep(900)
    Sound(203, 0, 60, 0)
    Sleep(1100)
    Sound(203, 0, 50, 0)
    Sleep(800)
    Sound(203, 0, 40, 0)
    Sleep(1000)
    Jump("Function_69_D2BA")

    label("loc_D2EE")

    Return()

    # Function_69_D2BA end

    def Function_70_D2EF(): pass

    label("Function_70_D2EF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrChipPat(0x4, 0x1, 0x1F)
    SetChrChipPat(0x5, 0x1, 0x20)
    ClearScenarioFlags(0x0, 0)
    ClearScenarioFlags(0x0, 1)
    ClearScenarioFlags(0x0, 2)
    ClearScenarioFlags(0x0, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D32D")
    AddParty(0x8, 0xFF, 0xFF)
    SetScenarioFlags(0x0, 0)

    label("loc_D32D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D345")
    AddParty(0x4, 0xFF, 0xFF)
    SetScenarioFlags(0x0, 1)

    label("loc_D345")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D35D")
    AddParty(0x5, 0xFF, 0xFF)
    SetScenarioFlags(0x0, 2)

    label("loc_D35D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D375")
    AddParty(0x9, 0xFF, 0xFF)
    SetScenarioFlags(0x0, 3)

    label("loc_D375")

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
            "#12P#11307FW-What is the meaning of\x01",
            "this!?\x02\x03",
            "Why did the supply from\x01",
            "the Sept-Terrion\x01",
            "suddenly stop!?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(240, 40, -1, -1)
    SetChrName("Ominous Voice")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Well, my time for\x01",
            "pointless things has\x01",
            "come to an end, I'd say.\x07\x00\x02",
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

    def lambda_DB0C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_DB0C)
    WaitChrThread(0x13, 2)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00013FFrom Ouroboros!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DB83")

    ChrTalk(
        0x105,
        (
            "#10407FIt's F. Novartis, of the\x01",
            "Thirteen Workshops!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DB9D")

    label("loc_DB83")


    ChrTalk(
        0x103,
        "#00207FDr. Novartis!\x02",
    )

    CloseMessageWindow()

    label("loc_DB9D")

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
            "#6P#11310FDr. Novartis... What\x01",
            "ever do you mean!?\x02\x03",
            "Could Ouroboros have\x01",
            "installed some sort of\x01",
            "trap in this machine!?\x02",
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
            "Haha, I said it last time. In the\x01",
            "end, we were only assisting you.\x02\x03",
            "I've gotten some good data already,\x01",
            "so I'll be taking my leave soon.\x02\x03",
            "And with that final model there,\x01",
            "like the contract says.\x02",
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
            "#6P#11307FContract!?\x02\x03",
            "It can't be! I bought\x01",
            "this machine from\x01",
            "Ouroboros!\x02\x03",
            "You have no right to\x01",
            "take it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#11P#04704FNo, no. You see, the\x01",
            "contract changed just a\x01",
            "bit.\x02\x03",
            "Once the machine's served\x01",
            "its purpose, we'll\x01",
            "collect it. See to that.\x02\x03",
            "#04702F─It's from your daughter,\x01",
            "Ms. Mariabell Crois.\x02",
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
        "#5P#00011F#6P#NT-this voice is...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        "#00107FBell#6P#N!?\x02",
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
            "#11310F#6P#NBell... What in the\x01",
            "world...?\x02\x03",
            "#11307FAnd, just where are\x01",
            "you!?\x02\x03",
            "You're not in Orchis\x01",
            "Tower!?\x02",
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
            "Haha, I haven't been\x01",
            "there in quite some\x01",
            "time.\x02\x03",
            "I'm with KeA and the\x01",
            "others.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00005F#6P#NWha...!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x102,
        (
            "#00101F#6P#NI-It's true they weren't\x01",
            "on any of the floors.\x02",
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
        "#00007F#6P#NArios!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E29C")

    ChrTalk(
        0x10A,
        "#00610F#6P#NMacLaine!\x02",
    )

    CloseMessageWindow()

    label("loc_E29C")


    ChrTalk(
        0x104,
        "#00307F#6P#NUncle! Shirley!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E2EE")

    ChrTalk(
        0x106,
        "#10701F#6P#NBloody Shirley!\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_E2EE")


    ChrTalk(
        0x103,
        "#00201F#6P#NAnd even Wald...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E34F")

    ChrTalk(
        0x105,
        (
            "#10401F#6P#NSo he really was with\x01",
            "them...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_E34F")

    Sleep(150)
    SetMessageWindowPos(240, 110, -1, -1)
    SetChrName("Arios")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "......\x07\x00\x02",
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
            "Wow! You guys got really\x01",
            "fired up!\x07\x00\x02",
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
            "#11310F#6P#NW-What is the meaning of\x01",
            "this...\x02\x03",
            "#11307FDo you all... mean to\x01",
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
            "...I do apologize, Mr.\x01",
            "President.\x02\x03",
            "However, I was never your\x01",
            "collaborator from the\x01",
            "very start.\x02\x03",
            "I have been collaborating\x01",
            "with the "lawyer" and Ms.\x01",
            "Mariabell.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0xC,
        (
            "#11305F#30W#6P#NLawyer...\x02\x03",
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
            "Yes─ Exactly right.\x07\x00\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E68E")
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x101,
        "#00007F#4S#12P#N...!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_E68E")


    ChrTalk(
        0x102,
        "#00105F#12P#N...Ah...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        "#00205F#12P#N...Huh...?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00305F#12P#N...No, it can't be\x01",
            "true...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E728")

    ChrTalk(
        0x10A,
        "#00605F#12P#NLawyer Ian!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_E728")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E753")

    ChrTalk(
        0x109,
        "#10111F#12P#NN-No way...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_E753")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E79C")

    ChrTalk(
        0x105,
        (
            "#10410F#12P#NIt can't be... So it's\x01",
            "come to this, huh.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_E79C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 0)), scpexpr(EXPR_END)), "loc_E983")

    ChrTalk(
        0x101,
        "#00013F#12P#N............\x02",
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
            "Hmm. From the looks of\x01",
            "things, could it be that you\x01",
            "all realized my involvement?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#00006F#12P#N...Yes. We got hints from\x01",
            "Nielsen, a reporter.\x02\x03",
            "#00008FAnd Pete, and the\x01",
            "gravekeeper... And from what\x01",
            "Kilika and Lechter told us...\x02\x03",
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
            "Haha. Looks like you've\x01",
            "finally caught up with\x01",
            "Guy, huh.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_E983")

    Fade(500)
    OP_68(8000, 3000, -3000, 0)
    MoveCamera(50, 3, 0, 0)
    SetCameraDistance(23000, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "#6P#11310F#NMr. Grimwood... What is\x01",
            "the meaning of this!?\x02\x03",
            "I-It's true you gave me\x01",
            "advice on various\x01",
            "matters, but...\x02",
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
            "You were an elite-class\x01",
            "manager, and as a politician\x01",
            "you weren't too bad, either.\x02\x03",
            "If one removed your fatal\x01",
            "flaw, that is─ You're too\x01",
            "much of a dreamer.\x07\x00\x02",
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
        "#6P#11305F#N...!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(270, 110, -1, -1)

    AnonymousTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Haha, you thought everything was going to\x01",
            "according to plan, but...\x02\x03",
            "Actually, it was all just a scenario created by\x01",
            "Lawyer Ian.\x02\x03",
            "The manipulation of the cult, the trade\x01",
            "conference agenda, the attack on Crossbell City,\x01",
            "and even the declaration of independence...\x02\x03",
            "I wonder who first put those ideas into your\x01",
            "head, father?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0xC,
        "#6P#11310F#30W#N...Oh...\x02",
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
            "If you had kept doing well,\x01",
            "I would never have revealed\x01",
            "my true colors, but...\x02\x03",
            "It seems I must bring your\x01",
            "days as the mastermind to\x01",
            "an end.\x02\x03",
            "I shall continue the\x01",
            ""Azure-Zero Plan", of\x01",
            "course.\x07\x00\x02",
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
            "Huhu. Why, it's the\x01",
            "Sept-Terrion of Zero's\x01",
            "completed form...\x02\x03",
            "The Azure Tree, ruler of\x01",
            "spacetime and\x01",
            "causality...\x07\x00\x02",
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
            "#4SIts very rebirth!\x07\x00\x02",
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

    def lambda_EFFD():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_EFFD)

    def lambda_F00A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_F00A)

    def lambda_F017():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F017)
    Sleep(50)

    def lambda_F027():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_F027)
    Sleep(50)

    def lambda_F037():
        OP_93(0x103, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_F037)
    Sleep(50)

    def lambda_F047():
        OP_93(0x104, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_F047)
    Sleep(50)

    def lambda_F057():
        OP_93(0xF4, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_F057)
    Sleep(50)

    def lambda_F067():
        OP_93(0xF5, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_F067)
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
        "#00105F#5PBlue light!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00207F#5P...South-by-southwest!\x01",
            "Near the marshlands!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00010F#5PThat's─\x02",
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
        "#5P#00010F#6P#N............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F251")

    ChrTalk(
        0x109,
        "#5P#10111F#6P#NWhaaaa!?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_F251")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F27D")

    ChrTalk(
        0x105,
        "#5P#10410F#6P#NThis is...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_F27D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F2B0")

    ChrTalk(
        0x10A,
        "#5P#00610F#6P#N...It can't be...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_F2B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F2E4")

    ChrTalk(
        0x106,
        "#5P#10701F#6P#N...A huge tree...?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_F2E4")

    WaitBGM()
    Sleep(10)
    PlayBGM("ed7571", 0)
    Sleep(500)

    NpcTalk(
        0x104,
        "Dr. Novartis",
        (
            "#04702F#5P#NHehe─ Magnificent!\x02\x03",
            "A truly singular fruit... It must be\x01",
            "called an "unexpected miracle" that\x01",
            "far exceeds even that Pillar of Salt!\x02",
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
            "#00010F#3SThat huge tree is the\x01",
            "true form of the Sept-\x01",
            "Terrion of Zero...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_F482():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_F482)
    Sleep(30)

    def lambda_F492():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_F492)
    Sleep(30)

    def lambda_F4A2():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_F4A2)
    Sleep(30)

    def lambda_F4B2():
        OP_93(0xF4, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_F4B2)
    Sleep(30)

    def lambda_F4C2():
        OP_93(0xF5, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_F4C2)
    Sleep(30)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)

    ChrTalk(
        0x102,
        (
            "#00107F#6P#NKeA... Just where is\x01",
            "she!?\x02",
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
            "Huhu. What do you think\x01",
            "you're saying?\x02\x03",
            "If you're looking for\x01",
            "KeA, can't you see her\x01",
            "from there already?\x02\x03",
            "That Azure Tree is KeA\x01",
            "herself.\x02",
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
            "But more importantly,\x01",
            "she has become the\x01",
            ""Arbitrator" of all─\x02\x03",
            "This is not a bad\x01",
            "result. For her, and for\x01",
            "you.\x02\x03",
            "If possible, I'd like\x01",
            "you to watch over her.\x07\x00\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F8A3")
    SetMessageWindowPos(0, 170, -1, -1)

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "He's right, you know.\x02\x03",
            "But if you're looking\x01",
            "for some fun, isn't that\x01",
            "good enough?\x02\x03",
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
    Jump("loc_F909")

    label("loc_F8A3")

    SetMessageWindowPos(0, 170, -1, -1)

    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "He's right, you know.\x02\x03",
            "But if it's fun, I guess\x01",
            "that's fine too, right?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_F909")

    SetMessageWindowPos(10, 110, -1, -1)

    AnonymousTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Hehe. Well if you're\x01",
            "planning to interfere, feel\x01",
            "free. I'll be your opponent.\x02\x03",
            "This was in the contract,\x01",
            "after all.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FA4D")
    SetMessageWindowPos(370, 160, -1, -1)

    AnonymousTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "...I don't know about\x01",
            "their plan...\x02\x03",
            "But if you come, I'll\x01",
            "crush you for good this\x01",
            "time.\x02\x03",
            "Got it, Wazy?\x07\x00\x02",
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
    Jump("loc_FAC4")

    label("loc_FA4D")

    SetMessageWindowPos(370, 160, -1, -1)

    AnonymousTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "...I don't know about\x01",
            "their plan...\x02\x03",
            "But if you come, I'll\x01",
            "crush you for good this\x01",
            "time.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_FAC4")

    SetMessageWindowPos(160, 150, -1, -1)

    AnonymousTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Uhuhu... Well then. Good\x01",
            "day, everyone.\x02\x03",
            "─And father. Thank you\x01",
            "for your support up to\x01",
            "this point.\x02\x03",
            "Although you were but a\x01",
            "simple romantic fool...\x02\x03",
            "I never hated you,\x01",
            "father...\x07\x00\x02",
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

    def lambda_FCE6():
        OP_A6(0xFE, 0x0, 0x1E, 0x2EE, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_FCE6)
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
            "#04704FHaha, well if I didn't have\x01",
            "other plans I would have loved\x01",
            "to stay 'til the end, but...\x02\x03",
            "#04700FWell, I'll at least hear your\x01",
            "report from afar.\x02",
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

    def lambda_FEBB():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_FEBB)
    Sleep(50)

    def lambda_FECB():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_FECB)
    Sleep(50)

    def lambda_FEDB():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_FEDB)
    Sleep(50)

    def lambda_FEEB():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_FEEB)
    Sleep(50)

    def lambda_FEFB():
        OP_93(0xF4, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_FEFB)
    Sleep(50)

    def lambda_FF0B():
        OP_93(0xF5, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_FF0B)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00007F#12P#NAh...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x28, 3)
    BeginChrThread(0x28, 3, 0, 78)
    Sound(223, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 10000, 0, 1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    Sound(936, 0, 100, 0)

    def lambda_FF9A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_FF9A)
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

    def lambda_1004A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_1004A)
    WaitChrThread(0x13, 2)
    Sound(936, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x13,
        (
            "#5P#04709FHaha. Excuse me, then.\x02\x03",
            "#04704FI think it's pointless,\x01",
            "but at least put up a\x01",
            "good fight for me.\x02\x03",
            "#04702FFor the purpose of\x01",
            "leaving behind some\x01",
            "useful data, of course.\x02",
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

    def lambda_101CB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_101CB)

    def lambda_101DC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_101DC)
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_10304")

    NpcTalk(
        0x105,
        "Wazy's Voice",
        (
            "Everyone, are you all\x01",
            "right!?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1036C")

    label("loc_10304")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_10342")

    NpcTalk(
        0x109,
        "Noｱl's Voice",
        (
            "Everyone, are you all\x01",
            "right!?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1036C")

    label("loc_10342")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1036C")

    NpcTalk(
        0x10A,
        "Dudley's Voice",
        "Are you ok!?\x02",
    )

    CloseMessageWindow()

    label("loc_1036C")

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

    def lambda_10414():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_10414)
    Sleep(50)

    def lambda_10424():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_10424)
    Sleep(50)

    def lambda_10434():
        OP_93(0x103, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_10434)
    Sleep(50)

    def lambda_10444():
        OP_93(0x104, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_10444)
    Sleep(50)

    def lambda_10454():
        OP_93(0xF4, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_10454)
    Sleep(50)

    def lambda_10464():
        OP_93(0xF5, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_10464)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)

    def lambda_10489():
        OP_96(0xFE, 0xFFFFFCE0, 0x0, 0xFFFFCF2C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x6, 1, lambda_10489)
    Sleep(200)

    def lambda_104A6():
        OP_96(0xFE, 0x320, 0x0, 0xFFFFCF2C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x7, 1, lambda_104A6)
    WaitChrThread(0x6, 1)
    WaitChrThread(0x7, 1)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00008FYou two...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_10542")

    ChrTalk(
        0x106,
        (
            "#10708F#12PJ-Just now... What\x01",
            "was...\x02\x03",
            "#10707FAnd what is that huge\x01",
            "tree thing...!?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10608")

    label("loc_10542")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_105A7")

    ChrTalk(
        0x10A,
        (
            "#00610F#12PJ-Just now... What\x01",
            "was...\x02\x03",
            "#00607FAnd what's that huge\x01",
            "tree thing...!?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10608")

    label("loc_105A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_10608")

    ChrTalk(
        0x109,
        (
            "#10108F#12PJ-Just now... What\x01",
            "was...\x02\x03",
            "#10107FAnd what is that huge\x01",
            "tree thing...!?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10608")


    ChrTalk(
        0x102,
        "#5P#00106FW-Well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5P#00206FHow to put it...\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x15, 0x4)
    SetChrPos(0x15, -8500, -2000, -20000, 90)

    NpcTalk(
        0x15,
        "Sergei's Voice",
        (
            "...Looks like it's not\x01",
            "over yet.\x02",
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

    def lambda_1078C():
        OP_95(0xFE, -2200, 0, -21800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_1078C)
    Sleep(500)
    Sound(112, 2, 50, 0)
    WaitChrThread(0x15, 1)

    def lambda_107B3():
        OP_95(0xFE, 0, 0, -21800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_107B3)
    WaitChrThread(0x15, 1)
    OP_68(0, 1000, -10000, 4000)
    MoveCamera(145, 15, 0, 4000)

    def lambda_107ED():
        OP_95(0xFE, 0, 0, -11500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_107ED)
    WaitChrThread(0x15, 1)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#6P#00005FChief!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#6PHow are things down\x01",
            "below?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#11P#01003FThe magic soldiers\x01",
            "disappeared so we've\x01",
            "taken the tower.\x02\x03",
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
            "#11P#01006F...Just what the hell\x01",
            "happened here?\x02",
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
        "#6P#00006F#6P...That's...\x02",
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
            "Lloyd and others\x01",
            "outlined what happened.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(14500, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_10AE4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10AC4")

    ChrTalk(
        0x106,
        "#11P#10712FT-That's...\x02",
    )

    Jump("loc_10ADE")

    label("loc_10AC4")


    ChrTalk(
        0x106,
        "#5P#10712FT-That's...\x02",
    )


    label("loc_10ADE")

    CloseMessageWindow()
    Jump("loc_10BB5")

    label("loc_10AE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_10B3F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10B1F")

    ChrTalk(
        0x109,
        "#11P#10106FN-No way...\x02",
    )

    Jump("loc_10B39")

    label("loc_10B1F")


    ChrTalk(
        0x106,
        "#5P#10706FN-No way...\x02",
    )


    label("loc_10B39")

    CloseMessageWindow()
    Jump("loc_10BB5")

    label("loc_10B3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_10BB5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10B8A")

    ChrTalk(
        0x105,
        (
            "#11P#10406FThat's indeed\x01",
            "surprising...\x02",
        )
    )

    Jump("loc_10BB4")

    label("loc_10B8A")


    ChrTalk(
        0x105,
        (
            "#5P#10406FThat's indeed\x01",
            "surprising...\x02",
        )
    )


    label("loc_10BB4")

    CloseMessageWindow()

    label("loc_10BB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_10C5C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10C16")

    ChrTalk(
        0x10A,
        (
            "#11P#00608FI can't believe Ian was\x01",
            "one of the\x01",
            "masterminds...\x02",
        )
    )

    Jump("loc_10C56")

    label("loc_10C16")


    ChrTalk(
        0x10A,
        (
            "#5P#00608FI can't believe Ian was\x01",
            "one of the\x01",
            "masterminds...\x02",
        )
    )


    label("loc_10C56")

    CloseMessageWindow()
    Jump("loc_10D91")

    label("loc_10C5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_10CFD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10CBA")

    ChrTalk(
        0x105,
        (
            "#11P#10403FAnd Mr. Beardy Bear is\x01",
            "one of the masterminds.\x02",
        )
    )

    Jump("loc_10CF7")

    label("loc_10CBA")


    ChrTalk(
        0x105,
        (
            "#5P#10403FAnd Mr. Beardy Bear is\x01",
            "one of the masterminds.\x02",
        )
    )


    label("loc_10CF7")

    CloseMessageWindow()
    Jump("loc_10D91")

    label("loc_10CFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_10D91")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10D57")

    ChrTalk(
        0x109,
        (
            "#11P#10108FAnd that Ian was one of\x01",
            "the masterminds...\x02",
        )
    )

    Jump("loc_10D90")

    label("loc_10D57")


    ChrTalk(
        0x109,
        (
            "#5P#10108FAnd that Ian was one of\x01",
            "the masterminds...\x02",
        )
    )


    label("loc_10D90")

    CloseMessageWindow()

    label("loc_10D91")


    ChrTalk(
        0x15,
        (
            "#11P#01006F...I see.\x02\x03",
            "#01001FSo a character who was known in\x01",
            "political, business, international,\x01",
            "police and guild circles had things\x01",
            "going on behind the scenes, huh.\x02\x03",
            "#01003FIndeed, if he felt like it, he\x01",
            "could have planned all of this.\x02\x03",
            "#01000FThe problem's the motive... But\x01",
            "now's not the time for that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#6PRight...\x02",
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
            "#13P#00001F─Wazy. Can you call the\x01",
            "Merkabah?\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x105, 0, 0, 73)
    WaitChrThread(0x105, 0)

    ChrTalk(
        0x105,
        (
            "#13P#10402FHaha, I figured you'd\x01",
            "say that.\x02",
        )
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10FE3")

    def lambda_10FDB():
        TurnDirection(0xFE, 0x15, 500)
        ExitThread()

    QueueWorkItem(0x6, 2, lambda_10FDB)

    label("loc_10FE3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x7, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11002")

    def lambda_10FFA():
        TurnDirection(0xFE, 0x15, 500)
        ExitThread()

    QueueWorkItem(0x7, 2, lambda_10FFA)

    label("loc_11002")

    OP_93(0x101, 0xB4, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00003F#6PYes. It might not be police work\x01",
            "anymore...\x02\x03",
            "#00013FBut as long as KeA and the truth\x01",
            "of all this is waiting for us\x01",
            "there, I can't ignore it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F#6P...I feel the same. We\x01",
            "have to stop Bell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#6PWell, I've come this\x01",
            "far. Might as well go\x01",
            "all the way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F#6PLooks like uncle's\x01",
            "waiting for me.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x109, 0, 0, 72)
    WaitChrThread(0x109, 0)

    ChrTalk(
        0x109,
        "#6P#10107FI'll be coming too!\x02",
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
            "#6P#10404FWe're offering you the\x01",
            "Merkabah, so I'll be\x01",
            "coming along too.\x02\x03",
            "#10400FAnd it seems I need to\x01",
            "settle things with Wald.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x106, 0, 0, 75)
    WaitChrThread(0x106, 0)

    ChrTalk(
        0x106,
        (
            "#6P#10703F...I need to settle\x01",
            "things with "her" as\x01",
            "well.\x02\x03",
            "#10708FFor my own honor...\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x10A, 0, 0, 76)
    WaitChrThread(0x10A, 0)

    ChrTalk(
        0x10A,
        (
            "#6P#00603FI need to hear the situation\x01",
            "in detail from both MacLaine\x01",
            "and Ian Grimwood.\x02\x03",
            "#00601FI plan to come along as\x01",
            "well.\x02",
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

    def lambda_113F8():
        OP_96(0x2B, 0x0, 0x2710, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_113F8)
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
            "#11P#01003F─Leave the city and tower\x01",
            "to me─ the President\x01",
            "included.\x02\x03",
            "#01001FYou guys─ Do what you need\x01",
            "to do, and keep doing it\x01",
            "until you're satisfied.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x15,
        (
            "#01007F#11PAnd as the "Special Support\x01",
            "Section"... Have confidence in\x01",
            "yourselves, above all else!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x12C, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(80, 50, -1, -1)
    SetChrName("Everyone")

    AnonymousTalk(
        0xFF,
        "#4SRight!\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 0)), scpexpr(EXPR_END)), "loc_116C9")
    OP_E0(0x33, 0x0)
    OP_E0(0x80, 0x0)
    Sleep(500)

    label("loc_116C9")

    OP_E5(0x3)
    SetScenarioFlags(0x23, 6)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_70_D2EF end

    def Function_71_116D8(): pass

    label("Function_71_116D8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_116FC")
    OP_82(0xA, 0xA, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_71_116D8")

    label("loc_116FC")

    Return()

    # Function_71_116D8 end

    def Function_72_116FD(): pass

    label("Function_72_116FD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11717")
    OP_FC(0x1)
    Jump("loc_11760")

    label("loc_11717")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11731")
    OP_FC(0x2)
    Jump("loc_11760")

    label("loc_11731")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1174B")
    OP_FC(0x1)
    Jump("loc_11760")

    label("loc_1174B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x7, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11760")
    OP_FC(0x2)

    label("loc_11760")

    Sleep(1)
    Return()

    # Function_72_116FD end

    def Function_73_11764(): pass

    label("Function_73_11764")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1177E")
    OP_FC(0x6)
    Jump("loc_117C7")

    label("loc_1177E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11798")
    OP_FC(0x6)
    Jump("loc_117C7")

    label("loc_11798")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_117B2")
    OP_FC(0xB)
    Jump("loc_117C7")

    label("loc_117B2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x7, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_117C7")
    OP_FC(0x5)

    label("loc_117C7")

    Sleep(1)
    Return()

    # Function_73_11764 end

    def Function_74_117CB(): pass

    label("Function_74_117CB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_117E5")
    OP_FC(0xB)
    Jump("loc_1182E")

    label("loc_117E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_117FF")
    OP_FC(0xB)
    Jump("loc_1182E")

    label("loc_117FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11819")
    OP_FC(0x6)
    Jump("loc_1182E")

    label("loc_11819")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x7, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1182E")
    OP_FC(0x6)

    label("loc_1182E")

    Sleep(1)
    Return()

    # Function_74_117CB end

    def Function_75_11832(): pass

    label("Function_75_11832")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1184C")
    OP_FC(0x1)
    Jump("loc_11895")

    label("loc_1184C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11866")
    OP_FC(0x2)
    Jump("loc_11895")

    label("loc_11866")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11880")
    OP_FC(0x1)
    Jump("loc_11895")

    label("loc_11880")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x7, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11895")
    OP_FC(0x2)

    label("loc_11895")

    Sleep(1)
    Return()

    # Function_75_11832 end

    def Function_76_11899(): pass

    label("Function_76_11899")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_118B3")
    OP_FC(0x1)
    Jump("loc_118FC")

    label("loc_118B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_118CD")
    OP_FC(0x2)
    Jump("loc_118FC")

    label("loc_118CD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_118E7")
    OP_FC(0x1)
    Jump("loc_118FC")

    label("loc_118E7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x7, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_118FC")
    OP_FC(0x2)

    label("loc_118FC")

    Sleep(1)
    Return()

    # Function_76_11899 end

    def Function_77_11900(): pass

    label("Function_77_11900")

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

    # Function_77_11900 end

    def Function_78_11942(): pass

    label("Function_78_11942")

    Sound(905, 0, 100, 0)
    OP_71(0x5, 0x4E2, 0x4F6, 0x0, 0x0)
    OP_79(0x5)
    OP_71(0x5, 0x4F6, 0x51E, 0x0, 0x20)
    Return()

    # Function_78_11942 end

    def Function_79_11964(): pass

    label("Function_79_11964")

    OP_71(0xD, 0x0, 0x64, 0x0, 0x8)
    OP_79(0xD)
    OP_71(0xD, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_79_11964 end

    def Function_80_11980(): pass

    label("Function_80_11980")

    OP_71(0xE, 0x0, 0x64, 0x0, 0x8)
    OP_79(0xE)
    OP_71(0xE, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_80_11980 end

    def Function_81_1199C(): pass

    label("Function_81_1199C")

    OP_71(0xF, 0x0, 0x64, 0x0, 0x8)
    OP_79(0xF)
    OP_71(0xF, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_81_1199C end

    def Function_82_119B8(): pass

    label("Function_82_119B8")

    OP_71(0x10, 0x0, 0x64, 0x0, 0x8)
    OP_79(0x10)
    OP_71(0x10, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_82_119B8 end

    def Function_83_119D4(): pass

    label("Function_83_119D4")

    OP_71(0x11, 0x0, 0x64, 0x0, 0x8)
    OP_79(0x11)
    OP_71(0x11, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_83_119D4 end

    def Function_84_119F0(): pass

    label("Function_84_119F0")

    OP_74(0x12, 0xF)
    OP_71(0x12, 0x0, 0x64, 0x0, 0x8)
    OP_79(0x12)
    OP_74(0x12, 0x1E)
    OP_71(0x12, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_84_119F0 end

    def Function_85_11A14(): pass

    label("Function_85_11A14")

    OP_75(0xD, 0x1, 0x3E8)
    Sleep(2000)
    Return()

    # Function_85_11A14 end

    def Function_86_11A1F(): pass

    label("Function_86_11A1F")

    OP_75(0xE, 0x1, 0x3E8)
    Sleep(2000)
    Return()

    # Function_86_11A1F end

    def Function_87_11A2A(): pass

    label("Function_87_11A2A")

    OP_75(0xF, 0x1, 0x3E8)
    Sleep(2000)
    Return()

    # Function_87_11A2A end

    def Function_88_11A35(): pass

    label("Function_88_11A35")

    OP_75(0x10, 0x1, 0x3E8)
    Sleep(2000)
    Return()

    # Function_88_11A35 end

    def Function_89_11A40(): pass

    label("Function_89_11A40")

    OP_75(0x11, 0x1, 0x3E8)
    Sleep(2000)
    Return()

    # Function_89_11A40 end

    def Function_90_11A4B(): pass

    label("Function_90_11A4B")

    OP_75(0x12, 0x1, 0x3E8)
    Sleep(2000)
    Return()

    # Function_90_11A4B end

    def Function_91_11A56(): pass

    label("Function_91_11A56")

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

    # Function_91_11A56 end

    def Function_92_11AD1(): pass

    label("Function_92_11AD1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    EventEnd(0x5)
    SetCameraDistance(13000, 0)
    Return()

    # Function_92_11AD1 end

    def Function_93_11AE9(): pass

    label("Function_93_11AE9")

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

    # Function_93_11AE9 end

    def Function_94_11B46(): pass

    label("Function_94_11B46")

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

    # Function_94_11B46 end

    SaveToFile()

Try(main)
