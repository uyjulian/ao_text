from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t2510.bin",                # FileName
        "t2510",                    # MapName
        "t2510",                    # Location
        0x005A,                     # MapIndex
        "ed7126",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1B,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 90, 0, 3, 0, 4],
    )

    BuildStringList((
        "t2510",                  # 0
        "Oliver ",                # 1
        "Jack ",                  # 2
        "Temas",                  # 3
        "Alexei",                 # 4
        "Lag",                    # 5
        "Tourist",                # 6
        "Tourist",                # 7
        "Tourist",                # 8
        "Tourist",                # 9
        "Tourist",                # 10
        "Boy",                    # 11
        "Bracer Scott",           # 12
        "Bracer Wenzel",          # 13
        "Chiruru",                # 14
        "Special Support Vehicle",# 15
        "Transport",              # 16
        "イベント用",             # 17
    ))

    AddCharChip((
        "chr/ch31300.itc",                   # 00
        "chr/ch31200.itc",                   # 01
        "chr/ch25000.itc",                   # 02
        "chr/ch31302.itc",                   # 03
        "chr/ch23400.itc",                   # 04
        "chr/ch20800.itc",                   # 05
        "chr/ch20802.itc",                   # 06
        "chr/ch32200.itc",                   # 07
        "chr/ch32202.itc",                   # 08
        "chr/ch21100.itc",                   # 09
        "chr/ch21102.itc",                   # 0A
        "chr/ch32300.itc",                   # 0B
        "chr/ch32302.itc",                   # 0C
        "chr/ch44200.itc",                   # 0D
        "chr/ch44202.itc",                   # 0E
        "chr/ch21402.itc",                   # 0F
        "chr/ch21400.itc",                   # 10
        "chr/ch41500.itc",                   # 11
        "chr/ch41400.itc",                   # 12
        "chr/ch41502.itc",                   # 13
        "chr/ch27202.itc",                   # 14
        "chr/ch27302.itc",                   # 15
        "chr/ch20500.itc",                   # 16
    ))

    DeclNpc(7780,    0,       6809,    180,  261,  0x0, 0,   0,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(4294963016, 0,       5130,    180,  261,  0x0, 0,   1,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(106529,  0,       1980,    270,  261,  0x0, 0,   2,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(95629,   150,     2380,    270,  261,  0x0, 0,   3,   0,   255, 255, 0,   13,  255,  0)
    DeclNpc(163020,  0,       4294964886, 270,  261,  0x0, 0,   4,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(102949,  150,     2150,    270,  389,  0x0, 0,   5,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(102900,  150,     4030,    270,  389,  0x0, 0,   7,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(100569,  150,     2150,    90,   389,  0x0, 0,   9,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(100569,  150,     3920,    90,   389,  0x0, 0,   11,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(102900,  150,     4030,    270,  389,  0x0, 0,   13,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(100569,  150,     2150,    90,   389,  0x0, 0,   15,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(101000,  150,     4294965217, 270,  452,  0x0, 0,   20,  0,   255, 255, 0,   22,  255,  0)
    DeclNpc(98500,   150,     4294965217, 90,   452,  0x0, 0,   21,  0,   255, 255, 0,   25,  255,  0)
    DeclNpc(159949,  0,       6000,    0,    389,  0x0, 0,   22,  0,   0,   0,   0,   26,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(4294965546, 0,       4294954996, 1000,    4294965546, 1000,    4294954996, 0x007C, 0,  31, 0x0000)
    DeclActor(105420,  0,       1980,    1000,    106530,  1500,    1980,    0x007E, 0,  11, 0x0000)
    DeclActor(161990,  0,       4294964846, 1000,    163020,  1500,    4294964886, 0x007E, 0,  14, 0x0000)
    DeclActor(7580,    0,       5630,    1000,    7780,    1500,    6810,    0x007E, 0,  6,  0x0000)
    DeclActor(108250,  0,       4294961546, 1200,    108250,  1250,    4294961546, 0x007C, 0,  5,  0x0000)

    ChipFrameInfo(1024, 0)                                       # 0

    ScpFunction((
        "Function_0_400",          # 00, 0
        "Function_1_4B0",          # 01, 1
        "Function_2_503",          # 02, 2
        "Function_3_52E",          # 03, 3
        "Function_4_872",          # 04, 4
        "Function_5_B67",          # 05, 5
        "Function_6_C1E",          # 06, 6
        "Function_7_C22",          # 07, 7
        "Function_8_1A25",         # 08, 8
        "Function_9_1B62",         # 09, 9
        "Function_10_1CE5",        # 0A, 10
        "Function_11_2B78",        # 0B, 11
        "Function_12_2B7C",        # 0C, 12
        "Function_13_3847",        # 0D, 13
        "Function_14_42F2",        # 0E, 14
        "Function_15_42F6",        # 0F, 15
        "Function_16_4F7E",        # 10, 16
        "Function_17_51BE",        # 11, 17
        "Function_18_563D",        # 12, 18
        "Function_19_586E",        # 13, 19
        "Function_20_5AAE",        # 14, 20
        "Function_21_5C8E",        # 15, 21
        "Function_22_5D61",        # 16, 22
        "Function_23_5E01",        # 17, 23
        "Function_24_636E",        # 18, 24
        "Function_25_6547",        # 19, 25
        "Function_26_6647",        # 1A, 26
        "Function_27_675F",        # 1B, 27
        "Function_28_717B",        # 1C, 28
        "Function_29_733C",        # 1D, 29
        "Function_30_7393",        # 1E, 30
        "Function_31_7A34",        # 1F, 31
    ))


    def Function_0_400(): pass

    label("Function_0_400")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_438"),
        (1, "loc_444"),
        (2, "loc_450"),
        (3, "loc_45C"),
        (4, "loc_468"),
        (5, "loc_474"),
        (6, "loc_480"),
        (SWITCH_DEFAULT, "loc_48C"),
    )


    label("loc_438")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_498")

    label("loc_444")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_498")

    label("loc_450")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_498")

    label("loc_45C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_498")

    label("loc_468")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_498")

    label("loc_474")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_498")

    label("loc_480")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_498")

    label("loc_48C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_498")

    label("loc_498")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4AF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_498")

    label("loc_4AF")

    Return()

    # Function_0_400 end

    def Function_1_4B0(): pass

    label("Function_1_4B0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_502")
    OP_95(0xFE, -21200, 0, -3250, 2000, 0x0)
    Sleep(2000)
    OP_93(0xFE, 0x5A, 0x190)
    Sleep(100)
    OP_95(0xFE, 10400, 0, -3250, 2000, 0x0)
    Sleep(2000)
    OP_93(0xFE, 0x10E, 0x190)
    Sleep(100)
    Jump("Function_1_4B0")

    label("loc_502")

    Return()

    # Function_1_4B0 end

    def Function_2_503(): pass

    label("Function_2_503")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_52D")
    OP_94(0xFE, 0x24D56, 0xAC8, 0x25CA6, 0xFFFFFDA8, 0x3E8)
    Sleep(450)
    Jump("Function_2_503")

    label("loc_52D")

    Return()

    # Function_2_503 end

    def Function_3_52E(): pass

    label("Function_3_52E")

    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5BC")
    SetChrChipByIndex(0x8, 0x11)
    SetChrChipByIndex(0x9, 0x12)
    SetChrChipByIndex(0xB, 0x13)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -7600, 0, 2770, 270)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 0x10)
    SetChrPos(0x12, -8790, 0, 2770, 90)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 152840, 0, 1090, 270)
    BeginChrThread(0x11, 0, 0, 2)
    Jump("loc_848")

    label("loc_5BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_64D")
    ClearChrFlags(0x15, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_5D8")
    Jump("loc_648")

    label("loc_5D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_5E6")
    Jump("loc_648")

    label("loc_5E6")

    SetChrChipByIndex(0xB, 0x0)
    ClearChrBattleFlags(0xB, 0x4)
    SetChrPos(0xB, 10400, 0, -3250, 90)
    BeginChrThread(0xB, 0, 0, 1)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x6)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 0xA)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 3040, 0, -2160, 0)

    label("loc_648")

    Jump("loc_848")

    label("loc_64D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_687")
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x8)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -21950, 0, 4400, 270)
    Jump("loc_848")

    label("loc_687")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_714")
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x13, 0x14)
    SetChrSubChip(0x13, 0x0)
    EndChrThread(0x13, 0x0)
    SetChrBattleFlags(0x13, 0x4)
    ClearChrFlags(0x14, 0x80)
    SetChrChipByIndex(0x14, 0x15)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6D9")
    SetChrFlags(0x13, 0x10)
    SetChrFlags(0x14, 0x10)

    label("loc_6D9")

    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 7660, 0, 4900, 0)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 0xC)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    Jump("loc_848")

    label("loc_714")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_764")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -8189, 0, -2160, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -21950, 0, 4400, 270)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 0xE)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    Jump("loc_848")

    label("loc_764")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7C3")
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x6)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 0xF)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 7660, 0, 4900, 0)
    SetChrFlags(0xE, 0x10)
    SetChrFlags(0x8, 0x10)
    Jump("loc_848")

    label("loc_7C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_7FD")
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 0xA)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 1540, 0, 2160, 180)
    Jump("loc_848")

    label("loc_7FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_848")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 1540, 0, 2160, 180)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x8)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -21950, 0, 4400, 270)

    label("loc_848")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_85F")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 7)
    Event(0, 28)
    Jump("loc_871")

    label("loc_85F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_871")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x1, 0)
    Event(0, 30)

    label("loc_871")

    Return()

    # Function_3_52E end

    def Function_4_872(): pass

    label("Function_4_872")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_88E")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8A0")

    label("loc_88E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_8A0")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x236), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8A0")

    OP_70(0x4, 0x8C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8ED")
    ClearMapObjFlags(0x6, 0x4)
    SetMapObjFrame(0x6, "light", 0x0, 0x1)
    OP_78(0x6, 0x16)
    SetChrPos(0x16, -8690, 0, 220, 90)
    OP_D5(0x16, 0x0, 0x15F90, 0x0, 0x0)
    Jump("loc_A44")

    label("loc_8ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_944")
    ClearMapObjFlags(0x7, 0x4)
    SetMapObjFrame(0x7, "light", 0x0, 0x1)
    SetMapObjFrame(0x7, "chukin", 0x0, 0x1)
    OP_78(0x7, 0x16)
    SetChrPos(0x16, 2500, 0, 0, 90)
    OP_D5(0x16, 0x0, 0x15F90, 0x0, 0x0)
    Jump("loc_A44")

    label("loc_944")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_952")
    Jump("loc_A44")

    label("loc_952")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_981")
    ClearMapObjFlags(0x7, 0x4)
    SetMapObjFrame(0x7, "light", 0x0, 0x1)
    SetMapObjFrame(0x7, "chukin", 0x0, 0x1)
    Jump("loc_A44")

    label("loc_981")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_9CA")
    ClearMapObjFlags(0x6, 0x4)
    SetMapObjFrame(0x6, "light", 0x0, 0x1)
    OP_78(0x6, 0x16)
    SetChrPos(0x16, -8690, 100, 220, 90)
    OP_D5(0x16, 0x0, 0x15F90, 0x0, 0x0)
    Jump("loc_A44")

    label("loc_9CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_9F9")
    ClearMapObjFlags(0x7, 0x4)
    SetMapObjFrame(0x7, "light", 0x0, 0x1)
    SetMapObjFrame(0x7, "chukin", 0x0, 0x1)
    Jump("loc_A44")

    label("loc_9F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_A1A")
    ClearMapObjFlags(0x6, 0x4)
    SetMapObjFrame(0x6, "light", 0x0, 0x1)
    Jump("loc_A44")

    label("loc_A1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_A44")
    ClearMapObjFlags(0x7, 0x4)
    SetMapObjFrame(0x7, "light", 0x0, 0x1)
    SetMapObjFrame(0x7, "chukin", 0x0, 0x1)

    label("loc_A44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A6A")
    SetMapObjFrame(0xFF, "hikari_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_A6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_B0B")
    SetChrPos(0x16, 8500, 0, 0, 90)
    ClearMapObjFlags(0x9, 0x4)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    SetMapObjFlags(0x9, 0x1000)
    OP_78(0x9, 0x17)
    SetChrPos(0x17, -3500, 0, 0, 90)
    OP_D5(0x17, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFrame(0xA, "light", 0x0, 0x1)
    SetMapObjFlags(0xA, 0x1000)
    OP_78(0xA, 0x18)
    SetChrPos(0x18, -3500, 0, 0, 90)
    OP_D5(0x18, 0x0, 0x15F90, 0x0, 0x0)
    Jump("loc_B66")

    label("loc_B0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_B66")
    SetChrPos(0x16, 8500, 0, 0, 90)
    ClearMapObjFlags(0x9, 0x4)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    SetMapObjFlags(0x9, 0x1000)
    OP_78(0x9, 0x17)
    SetChrPos(0x17, -3500, 0, 0, 90)
    OP_D5(0x17, 0x0, 0x15F90, 0x0, 0x0)

    label("loc_B66")

    Return()

    # Function_4_872 end

    def Function_5_B67(): pass

    label("Function_5_B67")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a car magazine, "Marching Roaring Guy".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x371, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C1A")
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "You learned the\x01\x07\x02",
            ""Guard Coloring"\x07\x00",
            " paint pattern.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0x371, 1)

    label("loc_C1A")

    TalkEnd(0xFF)
    Return()

    # Function_5_B67 end

    def Function_6_C1E(): pass

    label("Function_6_C1E")

    Call(0, 7)
    Return()

    # Function_6_C1E end

    def Function_7_C22(): pass

    label("Function_7_C22")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_EA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DB3")

    NpcTalk(
        0x8,
        "Soldier Oliver",
        (
            "The Republicans who were late in escaping\x01",
            "from Crossbell are coming here.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Oliver",
        (
            "However, in the current situation where we \x01",
            "can't loosen the watchout towards the Republic,\x01",
            "we can't really help but be forced to stay here.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Oliver",
        (
            "I understand their feeling of wanting to go home\x01",
            "and so I'm a little sorry for them, however...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_EA0")

    label("loc_DB3")


    NpcTalk(
        0x8,
        "Soldier Oliver",
        (
            "In the current situation where we can't\x01",
            "loosen the watchout towards the Republic,\x01",
            "we can't really help but be forced to stay here.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Oliver",
        (
            "Maybe they can't accept it, but we\x01",
            "can only make them understand.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EA0")

    Jump("loc_1A21")

    label("loc_EA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1256")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_101D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F8B")

    ChrTalk(
        0x8,
        (
            "The black truck that forcibly passed\x01",
            "through the gate just before seems\x01",
            "it was a wanted swindler.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It was surprising in this state of tension...\x01",
            "At any rate, I'm glad he was caught.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1018")

    label("loc_F8B")


    ChrTalk(
        0x8,
        "In any case, you did a good job too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Because it was already reported\x01",
            "to Vice Commander Douglas,\x01",
            "you shouldn't be worried about it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1018")

    Jump("loc_1251")

    label("loc_101D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_10E0")

    ChrTalk(
        0x8,
        (
            "The black truck that forcibly broke away\x01",
            "through the gate just before seems it\x01",
            "was a wanted swindler.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In this state of tension...\x01",
            "Honestly, what a foolish thing to do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1251")

    label("loc_10E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11EB")

    ChrTalk(
        0x8,
        (
            "The tension at the national border\x01",
            "is truly close to the limit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Although the Republic region has\x01",
            "a buffer zone called Tangram Hill,\x01",
            "we can't really be at ease.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We have to brace our legs here.\x01",
            "We must continue to watch out diligently.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1251")

    label("loc_11EB")


    ChrTalk(
        0x8,
        (
            "For Crossbell as well,\x01",
            "we have to brace our legs here.\x01",
            "We must continue to watch out diligently.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1251")

    Jump("loc_1A21")

    label("loc_1256")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_145B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_138C")

    ChrTalk(
        0x8,
        (
            "Yesterday, Tangram Gate too was pressed\x01",
            "in dealing with the derailment accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The Republican passenger\x01",
            "buses requested support too...\x01",
            "It was quite tough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "An accident happening when this state\x01",
            "of tension is continuing... Oh man,\x01",
            "what an unfortunate thing to happen.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1456")

    label("loc_138C")


    ChrTalk(
        0x8,
        (
            "An accident happening when this state\x01",
            "of tension is continuing... Oh man,\x01",
            "what an unfortunate thing to happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I hope for no more unforeseen\x01",
            "circumstances at least until\x01",
            "the local referendum.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1456")

    Jump("loc_1A21")

    label("loc_145B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_146C")
    Call(0, 8)
    Jump("loc_1A21")

    label("loc_146C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_16E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15F6")

    ChrTalk(
        0x8,
        (
            "Recently, the pros and cons of\x01",
            "Crossbell independence are being\x01",
            "discussed in the Republic too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Furthermore, differently from Crossbell,\x01",
            "it seems that they're almost all contrary.\x01",
            "Well, I think there's nothing to be surprised...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Soon the local referendum will be hold,\x01",
            "but I wonder what could happen if the\x01",
            "independence is realized in such a situation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16DB")

    label("loc_15F6")


    ChrTalk(
        0x8,
        (
            "Soon the local referendum will be hold,\x01",
            "but I wonder what could happen if the\x01",
            "independence is realized in such a situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As a CGF, by all means I\x01",
            "wish it'll be realized, but...\x01",
            "As expected, maybe it'll be difficult.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16DB")

    Jump("loc_1A21")

    label("loc_16E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_16F1")
    Call(0, 9)
    Jump("loc_1A21")

    label("loc_16F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_17BB")

    ChrTalk(
        0x8,
        (
            "The vehicles that couldn't pass through Tangram Hill\x01",
            "due to the traffic control, are coming all at once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "*sigh*, I was expecting this to a certain\x01",
            "degree, but man, it's so busy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A21")

    label("loc_17BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1A21")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1853")

    ChrTalk(
        0x8,
        (
            "Vice Commander Douglas's trainings\x01",
            "are always like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There're many harsh things, but...\x01",
            "We have to do our best.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A21")

    label("loc_1853")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1978")

    ChrTalk(
        0x8,
        (
            "If you leave here, there's "Tangram Hill",\x01",
            "a buffer zone between the autonomous\x01",
            "state and the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "On that hill, passenger buses and orbal\x01",
            "vehicles come and go very often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Orbal vehicles can be said to be a trend\x01",
            "in the Republic where they're widespread.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A21")

    label("loc_1978")


    ChrTalk(
        0x8,
        (
            "At Tangram Hill, passenger\x01",
            "buses and orbal vehicles\x01",
            "come and go very often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Orbal vehicles can be said to be a trend\x01",
            "in the Republic where they're widespread.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A21")

    TalkEnd(0x8)
    Return()

    # Function_7_C22 end

    def Function_8_1A25(): pass

    label("Function_8_1A25")

    OP_4B(0x8, 0xFF)
    OP_4B(0xD, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AF9")

    ChrTalk(
        0x8,
        "Good morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Recently, unidentified\x01",
            "monsters have appeared\x01",
            "in the autonomous state,\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please be careful while\x01",
            "driving on the highways.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Hm, thank you.\x01",
            "I'll be careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1B59")

    label("loc_1AF9")


    ChrTalk(
        0x8,
        (
            "...Then, please sign your\x01",
            "entry certificate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Oh, you're right.\x01",
            "*scribble scribble*...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B59")

    OP_4C(0x8, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_8_1A25 end

    def Function_9_1B62(): pass

    label("Function_9_1B62")

    OP_4B(0x8, 0xFF)
    OP_4B(0xE, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C60")

    ChrTalk(
        0x8,
        (
            "When you arrive at the city, please notify\x01",
            "the parking place to City Hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you forget to do it, they will stick a no parking\x01",
            "sticker on your vehicle, so be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Oh, is that so?\x01",
            "What an unexpected bother...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_1CDC")

    label("loc_1C60")


    ChrTalk(
        0x8,
        (
            "When you arrive at the city, please notify\x01",
            "your vehicle parking registration to City Hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Yeah yeah, roger that.\x02",
    )

    CloseMessageWindow()

    label("loc_1CDC")

    OP_4C(0x8, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_9_1B62 end

    def Function_10_1CE5(): pass

    label("Function_10_1CE5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1E7E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DB2")

    NpcTalk(
        0x9,
        "Soldier Jack",
        "In the Marshlands, there's something out of the ordinary!!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Soldier Jack",
        (
            "What in the world is that mysterious tree...\x01",
            "I can't really hide my uneasiness.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E79")

    label("loc_1DB2")


    NpcTalk(
        0x9,
        "Soldier Jack",
        (
            "What in the world is that mysterious tree...\x01",
            "I can't really hide my uneasiness.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Soldier Jack",
        (
            "A-At any rate...\x01",
            "No matter the time, we must be composed!\x01",
            "Being calm is important!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E79")

    Jump("loc_2B74")

    label("loc_1E7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2134")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1F23")

    ChrTalk(
        0x9,
        (
            "I was really surprised\x01",
            "some moments ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Although I'm happy because he was caught...\x01",
            "...I'd wish for the rules to be respected.\x01\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_212F")

    label("loc_1F23")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_1F93")

    ChrTalk(
        0x9,
        (
            "I was really surprised\x01",
            "some moments ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...I'd wish for the rules \x01",
            "to be respected.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_212F")

    label("loc_1F93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_209D")

    ChrTalk(
        0x9,
        (
            "At the national border Altair City,\x01",
            "Republican Army movements\x01",
            "can be seen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Starting a large-scale practice\x01",
            "and putting pressure on Crossbell...\x01",
            "That's probably their goal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...The situation is alarming.\x01",
            "We CGF must exert ourselves...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_212F")

    label("loc_209D")


    ChrTalk(
        0x9,
        (
            "At the national border Altair City,\x01",
            "Republican Army movements\x01",
            "can be seen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...The situation is alarming.\x01",
            "We CGF must exert ourselves...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_212F")

    Jump("loc_2B74")

    label("loc_2134")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_23E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_230E")

    ChrTalk(
        0x9,
        (
            "Nothing out of the ordinary! This kind of rain has got an\x01",
            "insignificant influence[軽微 keibi] on guarding[警備 keibi]!!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)

    ChrTalk(
        0x103,
        "#00206F...0 points.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Huh...\x01",
            "I-It wasn't a pun\x01",
            "at all, you know!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I wanted to say that\x01",
            "this kind of rain hasn't\x01",
            "got a big effect on me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FAhaha, we know.\x01",
            "(...However, maybe thanks to this he relaxed a little.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_23E4")

    label("loc_230E")


    ChrTalk(
        0x9,
        (
            "I-I meant to say that\x01",
            "this kind of rain hasn't\x01",
            "got a big effect on me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Under this state of tension,\x01",
            "it's not the case to be\x01",
            "joking around, you know!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FY-You don't have to be that flustered...\x02",
    )

    CloseMessageWindow()

    label("loc_23E4")

    Jump("loc_2B74")

    label("loc_23E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_25C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2526")

    ChrTalk(
        0x9,
        (
            "It seems that "Cryptids" don't\x01",
            "appear on Tangram Hill.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "That place is a buffer zone with the Republic.\x01",
            "If they appeared, going there to exterminate\x01",
            "them would be troublesome in many ways.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It's not said they won't appear in the future, but...\x01",
            "In any case, I'll guard severely!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_25BF")

    label("loc_2526")


    ChrTalk(
        0x9,
        (
            "It seems that "Cryptids" don't\x01",
            "appear on Tangram Hill.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It's not said they won't appear in the future, but...\x01",
            "In any case, I'll guard severely!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25BF")

    Jump("loc_2B74")

    label("loc_25C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_287C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2803")

    ChrTalk(
        0x9,
        (
            "The other day the restoration of the radar \x01",
            "facility that was destroyed at the time of\x01",
            "the Trade Conference was completed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Still, those damn terrorists,\x01",
            "to think they destroyed the\x01",
            "facility unnoticed from us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Thinking about it carefully,\x01",
            "it's really a mystery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F(...Given the armored vehicle that\x01",
            "appeared underground, even for some\x01",
            "terrorists they were indeed too prepared.)\x02\x03",
            "#00003F(As we thought, they could have\x01",
            "had the "Society" cooperation.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F(Well, we have no proof, but\x01",
            "I believe it's highly likely.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2877")

    label("loc_2803")


    ChrTalk(
        0x9,
        (
            "Hm, questions regarding those\x01",
            "terrorists still remain, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "At any rate, now we'll\x01",
            "strengthen security!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2877")

    Jump("loc_2B74")

    label("loc_287C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2999")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_291E")

    ChrTalk(
        0x9,
        "At present, nothing out of the ordinary!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Damn terrorists...\x01",
            "Now that we have intel, we'll\x01",
            "intercept them with all our might.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2994")

    label("loc_291E")


    ChrTalk(
        0x9,
        (
            "We CGF will protect the\x01",
            "VIPs without fault!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...In any case, at present there's\x01",
            "nothing out of the ordinary!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2994")

    Jump("loc_2B74")

    label("loc_2999")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2A70")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A37")

    ChrTalk(
        0x9,
        (
            "There was nothing out of the ordinary\x01",
            "with President Rocksmith guarding!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We'll continue the Trade\x01",
            "Conference vigilance!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A6B")

    label("loc_2A37")


    ChrTalk(
        0x9,
        (
            "We'll continue the Trade\x01",
            "Conference vigilance!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A6B")

    Jump("loc_2B74")

    label("loc_2A70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2B74")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2B14")

    ChrTalk(
        0x9,
        (
            "The training we did some time ago\x01",
            "has been a terrific experience!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'll absolutely want to make use of it\x01",
            "in my future guarding!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B74")

    label("loc_2B14")


    ChrTalk(
        0x9,
        "Nothing out of the ordinary!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The security system for the\x01",
            "Trade Conference is perfect!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B74")

    TalkEnd(0xFE)
    Return()

    # Function_10_1CE5 end

    def Function_11_2B78(): pass

    label("Function_11_2B78")

    Call(0, 12)
    Return()

    # Function_11_2B78 end

    def Function_12_2B7C(): pass

    label("Function_12_2B7C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2BA5")
    Call(0, 27)
    Return()

    label("loc_2BA5")

    TalkBegin(0xA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2BB2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3843")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",      # 0
            "Shop\x01",      # 1
            "Quit\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C02")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2C02")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C22")
    OP_AF(0x6E)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_383E")

    label("loc_2C22")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C36")
    Jump("loc_383E")

    label("loc_2C36")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C4E")
    TalkEnd(0xA)
    Return()

    label("loc_2C4E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_383E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_2D0A")

    ChrTalk(
        0xA,
        (
            "Because the hot pot is easy and tasty,\x01",
            "we do it often at Tangram Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's really lively and fun when\x01",
            "everyone is merrily around the pot.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_383E")

    label("loc_2D0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2E82")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DF6")

    ChrTalk(
        0xA,
        (
            "Although the times are what they're...\x01",
            "Do you want to eat something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I'm sure that when you feel anxious and\x01",
            "irritated it's because you're hungry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "After you eat a lot, your\x01",
            "mind will calm down.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2E7D")

    label("loc_2DF6")


    ChrTalk(
        0xA,
        (
            "I'm sure that when you feel anxious and\x01",
            "irritated it's because you're hungry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "After you eat a lot, your\x01",
            "mind will calm down.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E7D")

    Jump("loc_383E")

    label("loc_2E82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_305B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F9B")

    ChrTalk(
        0xA,
        (
            "The damage to the CGF...\x01",
            "It was an event Mr. Lag and I,\x01",
            "who aren't members, had to endure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "They were taken out before doing anything,\x01",
            "so they must've been mortified too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "At least, I'd like the remaining\x01",
            "members to get back their spirit...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3056")

    label("loc_2F9B")


    ChrTalk(
        0xA,
        (
            "The members who became victims...\x01",
            "They were taken out before doing anything,\x01",
            "so they must've mortified too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "At least, I'd like the remaining\x01",
            "members to get back their spirit...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3056")

    Jump("loc_383E")

    label("loc_305B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3108")

    ChrTalk(
        0xA,
        (
            "Yesterday, many guests were sent here\x01",
            "with the bus transfer transports from the train.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Many of them have already gone home,\x01",
            "but it was really tough.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_383E")

    label("loc_3108")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_31F5")

    ChrTalk(
        0xA,
        (
            "In this situation where the state of \x01",
            "tension continues, there're few things\x01",
            "a humble cook like me can do, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "At least I have to prepare delicious\x01",
            "dishes so all the members can\x01",
            "display their strength at 100%.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_383E")

    label("loc_31F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_33BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3303")

    ChrTalk(
        0xA,
        (
            "An independence proposal, eh...?\x01",
            "Somehow Crossbell might've got into a big trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I can't think the Empire and Republic\x01",
            "will let it pass with no objections, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Personally, I want the mayor\x01",
            "and the others to do their best.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_33B6")

    label("loc_3303")


    ChrTalk(
        0xA,
        (
            "I can't think the Empire and Republic\x01",
            "will let pass something like independence\x01",
            "with no objections, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Personally, I want the mayor\x01",
            "and the others to do their best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33B6")

    Jump("loc_383E")

    label("loc_33BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3475")

    ChrTalk(
        0xA,
        (
            "Due to the anti-terrorists measures,\x01",
            "all the CGF guys seem to be\x01",
            "pretty fired up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Here they eat plentifully and so they\x01",
            "have to do their best for the entire day.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_383E")

    label("loc_3475")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_36BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35D6")

    ChrTalk(
        0xA,
        (
            "When you speak of Calvard, it's\x01",
            "a country that accepted many\x01",
            "different cultures since the past.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The eastern culture too is one of them,\x01",
            "and it's regarded to have given a heavy \x01",
            "influence to the cooking world too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Practically, the eastern cuisine is superb.\x01",
            "There're many things to learn for a cook like me too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_36B7")

    label("loc_35D6")


    ChrTalk(
        0xA,
        (
            "The eastern culture the Republic has received\x01",
            "is regarded to have given a heavy influence \x01",
            "to the cooking world too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Practically, the eastern cuisine is superb.\x01",
            "There're many things to learn for a cook like me too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36B7")

    Jump("loc_383E")

    label("loc_36BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_383E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37BA")

    ChrTalk(
        0xA,
        (
            "The newly arrived Vice Commander\x01",
            "is quite the funny fellow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "He's "cool" in a different way than\x01",
            "Commander Sonya and a reliable\x01",
            "man who steadily pulls everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "So there still was an excellent\x01",
            "man in the CGF, eh?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_383E")

    label("loc_37BA")


    ChrTalk(
        0xA,
        (
            "The new Vice Commander\x01",
            "is a reliable man who\x01",
            "steadily pulls everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "So there still was an excellent\x01",
            "man in the CGF, eh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_383E")

    Jump("loc_2BB2")

    label("loc_3843")

    TalkEnd(0xA)
    Return()

    # Function_12_2B7C end

    def Function_13_3847(): pass

    label("Function_13_3847")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3A32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3987")

    NpcTalk(
        0xB,
        "Soldier Alexei",
        "*sigh*...somehow I don't have an appetite.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "Soldier Alexei",
        (
            "...No, it's because we're in such a time that\x01",
            "I must eat, even if by forcing myself.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "Soldier Alexei",
        (
            "To defend Crossbell in case the\x01",
            "Empire and Republic invade...\x01",
            "...It's also to carry out that mission.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3A2D")

    label("loc_3987")


    NpcTalk(
        0xB,
        "Soldier Alexei",
        (
            "Too many things have happened...\x01",
            "It's like my head is in confusion.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "Soldier Alexei",
        (
            "Defending Crossbell.\x01",
            "...I have to carry out that mission.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A2D")

    Jump("loc_42EE")

    label("loc_3A32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3AF5")

    ChrTalk(
        0xB,
        (
            "The persons who attacked the city\x01",
            "are now hiding somewhere, eh...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "...Hmph, very good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "In order to avenge our comrades too...\x01",
            "One day, we'll smoke them out for sure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42EE")

    label("loc_3AF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3BAE")

    ChrTalk(
        0xB,
        (
            "*sigh*...a meal after manual labor\x01",
            "has truly a supreme taste.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I don't know if something will happen again...\x01",
            "I have to constantly fortify\x01",
            "myself through eating.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42EE")

    label("loc_3BAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3DAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CCD")

    ChrTalk(
        0xB,
        (
            "After Crossbell is independent,\x01",
            "if the CGF activities could become\x01",
            "recognised as those of an army...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "By all means I wouldn't want just an improvement\x01",
            "in armaments, but also in rations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "After all, I can only describe\x01",
            "the ones we have as awful...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3DA8")

    label("loc_3CCD")


    ChrTalk(
        0xB,
        (
            "...I hear that the meals served in the\x01",
            "Empire taste pretty bad too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Breaking away from the Empire and being independent,\x01",
            "I'm sure that even the rations would be improved.\x01",
            "...That's totally my imagination, eh.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DA8")

    Jump("loc_42EE")

    label("loc_3DAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3E7B")

    ChrTalk(
        0xB,
        (
            "Cryptids... According to the report I heard,\x01",
            "they're pretty tough-looking opponents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We CGF need to concentrate\x01",
            "on guarding the national border...\x01",
            "We're leaving the rest to you all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42EE")

    label("loc_3E7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3F92")

    ChrTalk(
        0xB,
        (
            "There're talks that maybe terrorists will appear, but...\x01",
            "In practice, what's important is what methods\x01",
            "would they use to try to infiltrate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It's also possible they have accomplices\x01",
            "who snuck in already. Today, I won't let\x01",
            "down my guard even for a moment.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42EE")

    label("loc_3F92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_410D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4085")

    ChrTalk(
        0xB,
        (
            "*haah*, I wanted to go to do\x01",
            "security at Michelam too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I only went there once and the\x01",
            "food they served in that\x01",
            "restaurant was good...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "...Michelam is closed so\x01",
            "they won't be running the\x01",
            "restaurant, eh?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4108")

    label("loc_4085")


    ChrTalk(
        0xB,
        (
            "...Michelam is closed so\x01",
            "they won't be running the\x01",
            "restaurant, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "...*munch munch*.\x01",
            "In any case, I'll eat\x01",
            "my meal fast.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4108")

    Jump("loc_42EE")

    label("loc_410D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_42EE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_427A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41E9")

    ChrTalk(
        0xB,
        "*chomp chomp, munch munch*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "As expected, meals after\x01",
            "training are exceptional.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I fortified myself with a meal\x01",
            "before training, but I really\x01",
            "can't stop eating this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4275")

    label("loc_41E9")


    ChrTalk(
        0xB,
        (
            "Even if it's an awful ration, after\x01",
            "training you can feel it delicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I think that meals after\x01",
            "training are really exceptional.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4275")

    Jump("loc_42EE")

    label("loc_427A")


    ChrTalk(
        0xB,
        (
            "*munch munch*...\x01",
            "Delicious, delicious...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Today they say we'll do training,\x01",
            "so I have to have a good meal.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42EE")

    TalkEnd(0xFE)
    Return()

    # Function_13_3847 end

    def Function_14_42F2(): pass

    label("Function_14_42F2")

    Call(0, 15)
    Return()

    # Function_14_42F2 end

    def Function_15_42F6(): pass

    label("Function_15_42F6")

    TalkBegin(0xC)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4303")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F7A")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",      # 0
            "Rest\x01",      # 1
            "Quit\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4353")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_4353")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4373")
    OP_AF(0x6F)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4F75")

    label("loc_4373")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4387")
    Jump("loc_4F75")

    label("loc_4387")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_439F")
    TalkEnd(0xC)
    Return()

    label("loc_439F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F75")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_453B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44A0")

    ChrTalk(
        0xC,
        (
            "I heard a rumor that Ilya\x01",
            "regained consciousness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "From now on, Crossbell will\x01",
            "gradually undergo a tough\x01",
            "situation, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "As long as we have the light called "Ilya",\x01",
            "I'm sure we'll be fine.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4536")

    label("loc_44A0")


    ChrTalk(
        0xC,
        (
            "From now on, Crossbell will\x01",
            "gradually undergo a tough\x01",
            "situation, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "As long as we have the light called "Ilya",\x01",
            "I'm sure we'll be fine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4536")

    Jump("loc_4F75")

    label("loc_453B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_46E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_463B")

    ChrTalk(
        0xC,
        (
            "To many people living in Crossbell,\x01",
            "Ilya Platiｲre is an existence\x01",
            "like the sun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "That such a woman was gravely injured...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...No, I must concentrate on my job.\x01",
            "I wonder if she'll be able to make a stage comeback...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_46DB")

    label("loc_463B")


    ChrTalk(
        0xC,
        (
            "According to rumors, Ilya Platiｲre\x01",
            "is still in a coma...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...No, I must concentrate on my job.\x01",
            "I wonder if she'll be able to make a stage comeback...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46DB")

    Jump("loc_4F75")

    label("loc_46E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_48E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_482E")

    ChrTalk(
        0xC,
        (
            "At last, tomorrow the Arc-en-ciel renewal\x01",
            "performance is going to take place...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "As expected, the highlight is going to be the hopeful \x01",
            "new face, Sully, who plays the "Star Princess" role.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "In the end, I couldn't get the tickets, but\x01",
            "Crossbell Times will probably do a feature.\x01",
            "I can't wait...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_48E0")

    label("loc_482E")


    ChrTalk(
        0xC,
        (
            "At last, tomorrow the Arc-en-ciel renewal\x01",
            "performance is going to take place...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "What kind of event will it be...?\x01",
            "I can't wait for the next feature\x01",
            "in Crossbell Times.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48E0")

    Jump("loc_4F75")

    label("loc_48E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4989")

    ChrTalk(
        0xC,
        "In a way or another, nowadays it's so boring.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Seems that tomorrow too will rain.\x01",
            "Maybe I should read an\x01",
            "Arc-en-ciel fanbook or something...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F75")

    label("loc_4989")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4B4B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AAA")

    ChrTalk(
        0xC,
        (
            "Due to the state of tension with the two major powers,\x01",
            "the CGF members look quite busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "In this situation, it appears that\x01",
            "the Support Section and the Guild\x01",
            "have undertaken CGF jobs...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "From now on, we should versatily\x01",
            "help out each other somehow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4B46")

    label("loc_4AAA")


    ChrTalk(
        0xC,
        (
            "It appears that the Support \x01",
            "Section and the Guild have\x01",
            "undertaken CGF jobs, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "From now on, we should versatily\x01",
            "help out each other somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B46")

    Jump("loc_4F75")

    label("loc_4B4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4D59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C93")

    ChrTalk(
        0xC,
        (
            "The danger of terrorisms is in the\x01",
            "fact that they firmly believe that\x01",
            "they are "right".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Willing to sacrifice themselves for their own goals...\x01",
            "They don't feel that's bad.\x01",
            "Put it bluntly, they can go to hell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "In order to not make such a thing happen,\x01",
            "the CGF guys want to do their best.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4D54")

    label("loc_4C93")


    ChrTalk(
        0xC,
        (
            "Willing to sacrifice themselves for their own goals...\x01",
            "Such a blasted idea is at\x01",
            "the basis of terrorism.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "In order to not make such a thing happen,\x01",
            "the CGF guys want to do their best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D54")

    Jump("loc_4F75")

    label("loc_4D59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4E18")

    ChrTalk(
        0xC,
        (
            "It seems that the VIPs who came\x01",
            "to Crossbell are going to see the\x01",
            "Arc-en-ciel play tonight...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The "state guest privilege" thing, I guess.\x01",
            "I'm honestly envying them...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F75")

    label("loc_4E18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4F75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EDF")

    ChrTalk(
        0xC,
        (
            "The Arc-en-ciel public performance\x01",
            "is getting close...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Even the tickets sales seem to\x01",
            "be going at a crazy speed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I guess I'll have to resign myself again...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4F75")

    label("loc_4EDF")


    ChrTalk(
        0xC,
        (
            "I'm a big fan of\x01",
            "Ilya Platiｲre...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "This time I really wanted to go see the public performance,\x01",
            "but I guess I can only resign myself again...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F75")

    Jump("loc_4303")

    label("loc_4F7A")

    TalkEnd(0xC)
    Return()

    # Function_15_42F6 end

    def Function_16_4F7E(): pass

    label("Function_16_4F7E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5059")

    ChrTalk(
        0xD,
        (
            "I can't believe a raid incident happened\x01",
            "at the destination I came for a travel...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Hmph, the heck is this CGF that can't even protect a city?\x01",
            "I don't want to stay in such a dangerous country.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51BA")

    label("loc_5059")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5067")
    Jump("loc_51BA")

    label("loc_5067")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5078")
    Call(0, 8)
    Jump("loc_51BA")

    label("loc_5078")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5086")
    Jump("loc_51BA")

    label("loc_5086")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5136")

    ChrTalk(
        0xD,
        (
            "I wonder what kind of form will take\x01",
            "today's conference...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "When I go back to the Republic,\x01",
            "I guess I'll try to order the next\x01",
            "issue of Crossbell Times.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51BA")

    label("loc_5136")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5144")
    Jump("loc_51BA")

    label("loc_5144")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_51BA")

    ChrTalk(
        0xD,
        (
            "I got tired by driving\x01",
            "at Tangram Hill.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Let's see, I guess I'll go eat\x01",
            "something at the mess hall.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51BA")

    TalkEnd(0xFE)
    Return()

    # Function_16_4F7E end

    def Function_17_51BE(): pass

    label("Function_17_51BE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_525E")

    ChrTalk(
        0xE,
        (
            "Uuh, after all that, the\x01",
            "barrier was released, and yet\x01",
            "I can't go back to the Republic...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I've got to protect\x01",
            "at least this child...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5639")

    label("loc_525E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5372")

    ChrTalk(
        0xE,
        (
            "I sympathize with the Crossbell people, but...\x01",
            "If they had had a proper army, the\x01",
            "damage would've been kept to a minimum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "As I fear, maybe they should've accepted \x01",
            "President Rocksmith and the "Iron and Blood \x01",
            "Chancellor"'s bill at theTrade Conference.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5639")

    label("loc_5372")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_544F")

    ChrTalk(
        0xE,
        (
            "It seems that a colleague of mine who went on a business \x01",
            "trip to the Republic was caught in the train accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Now I'm heading to the hospital where he's recovered...\x01",
            "Anyway, I'm glad he's safe.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5639")

    label("loc_544F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_545D")
    Jump("loc_5639")

    label("loc_545D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5544")

    ChrTalk(
        0xE,
        (
            "I feel that it can be said to be inevitable,\x01",
            "in a certain sense, for the citizens of\x01",
            "Crossbell to think about independence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Unless a bad influence comes to my business,\x01",
            "I guess I'll remain an idle onlooker.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5639")

    label("loc_5544")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5555")
    Call(0, 9)
    Jump("loc_5639")

    label("loc_5555")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5563")
    Jump("loc_5639")

    label("loc_5563")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5639")

    ChrTalk(
        0xE,
        (
            "I have a private general store.\x01",
            "I came to Crossbell to buy up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "You can really find many kinds of articles in Crossbell, \x01",
            "that is located at Zemuria's crossover point.\x01",
            "Uh uh, I can't hardly wait.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5639")

    TalkEnd(0xFE)
    Return()

    # Function_17_51BE end

    def Function_18_563D(): pass

    label("Function_18_563D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_56AE")

    ChrTalk(
        0xF,
        (
            "Oh, father...\x01",
            "Getting all excited...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Oh ho ho, I'm sorry.\x01",
            "Please, don't take offense.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_586A")

    label("loc_56AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_56BC")
    Jump("loc_586A")

    label("loc_56BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_56CA")
    Jump("loc_586A")

    label("loc_56CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5779")

    ChrTalk(
        0xF,
        (
            "They say that recently in\x01",
            "Crossbell mysterious large-\x01",
            "type monsters are appearing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "No way, how scary...\x01",
            "Maybe I got the period\x01",
            "to do a travel wrong...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_586A")

    label("loc_5779")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5787")
    Jump("loc_586A")

    label("loc_5787")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5861")

    ChrTalk(
        0xF,
        (
            "I got interested into that Orchis Tower or whatever and\x01",
            "so I came to see it against my better judgement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I already saw it at the unveiling ceremony,\x01",
            "so I think it's time for me to go back home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_586A")

    label("loc_5861")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_586A")

    label("loc_586A")

    TalkEnd(0xFE)
    Return()

    # Function_18_563D end

    def Function_19_586E(): pass

    label("Function_19_586E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_587F")
    Jump("loc_5AAA")

    label("loc_587F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_58BB")

    ChrTalk(
        0x10,
        "*sigh*, isn't the bus coming already...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5AAA")

    label("loc_58BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_59CE")

    ChrTalk(
        0x10,
        (
            "By the way, they say that an old\x01",
            "lady who was working as a fake brand\x01",
            "trader was arrested at Altair City yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Man, she was still brisk and yet to think\x01",
            "she tried a hand as an unscrupulous trader...\x01",
            "In a certain sense, she's a pitiable old lady.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AAA")

    label("loc_59CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_59DC")
    Jump("loc_5AAA")

    label("loc_59DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_59EA")
    Jump("loc_5AAA")

    label("loc_59EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5AA1")

    ChrTalk(
        0x10,
        (
            "Because of traffic regulation, this\x01",
            "morning was impossible to pass\x01",
            "through Tangram Hill.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Well, it was because the\x01",
            "President's visit, so it\x01",
            "couldn't be helped.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AAA")

    label("loc_5AA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5AAA")

    label("loc_5AAA")

    TalkEnd(0xFE)
    Return()

    # Function_19_586E end

    def Function_20_5AAE(): pass

    label("Function_20_5AAE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5B17")

    ChrTalk(
        0x11,
        (
            "Ooh, enough!\x01",
            "Why has such a\x01",
            "thing happened!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "I wonder whose fault it is, eh!?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5C8A")

    label("loc_5B17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5B25")
    Jump("loc_5C8A")

    label("loc_5B25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5B33")
    Jump("loc_5C8A")

    label("loc_5B33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5B41")
    Jump("loc_5C8A")

    label("loc_5B41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5BFE")

    ChrTalk(
        0x11,
        (
            "The members at the gate\x01",
            "are somehow scary...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "I don't care if they're in a state\x01",
            "of tension or something...\x01",
            "Would it kill them if they were\x01",
            "just a little more civil?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C8A")

    label("loc_5BFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5C0C")
    Jump("loc_5C8A")

    label("loc_5C0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5C1A")
    Jump("loc_5C8A")

    label("loc_5C1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5C8A")

    ChrTalk(
        0x11,
        (
            "Ehhm, where was the bus to\x01",
            "Crossbell City departing again...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "Transfers are really a bother.\x02",
    )

    CloseMessageWindow()

    label("loc_5C8A")

    TalkEnd(0xFE)
    Return()

    # Function_20_5AAE end

    def Function_21_5C8E(): pass

    label("Function_21_5C8E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5CC5")

    ChrTalk(
        0x12,
        (
            "Papaaa...\x01",
            "I want to go hooome...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D5D")

    label("loc_5CC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5CD3")
    Jump("loc_5D5D")

    label("loc_5CD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5CE1")
    Jump("loc_5D5D")

    label("loc_5CE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5CEF")
    Jump("loc_5D5D")

    label("loc_5CEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5CFD")
    Jump("loc_5D5D")

    label("loc_5CFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5D46")

    ChrTalk(
        0x12,
        (
            "Grampa, enough with\x01",
            "the complicated talks,\x01",
            "let's eat!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D5D")

    label("loc_5D46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5D54")
    Jump("loc_5D5D")

    label("loc_5D54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5D5D")

    label("loc_5D5D")

    TalkEnd(0xFE)
    Return()

    # Function_21_5C8E end

    def Function_22_5D61(): pass

    label("Function_22_5D61")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D76")
    Call(0, 23)
    Jump("loc_5DFD")

    label("loc_5D76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D88")
    Call(0, 24)
    Jump("loc_5DFD")

    label("loc_5D88")


    ChrTalk(
        0xFE,
        (
            "In any case...\x01",
            "We must focus on our job now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You should have yours too,\x01",
            "so leave this investigation to us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DFD")

    TalkEnd(0xFE)
    Return()

    # Function_22_5D61 end

    def Function_23_5E01(): pass

    label("Function_23_5E01")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x13, 0x10)
    TurnDirection(0x13, 0x0, 0)
    OP_52(0x13, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5E92")
    Jump("loc_5EDC")

    label("loc_5E92")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5EB2")
    OP_52(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5EDC")

    label("loc_5EB2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5ED2")
    OP_52(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5EDC")

    label("loc_5ED2")

    OP_52(0x13, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5EDC")

    OP_52(0x13, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x13, 0x10)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x14, 0x10)
    TurnDirection(0x14, 0x0, 0)
    OP_52(0x14, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5F92")
    Jump("loc_5FDC")

    label("loc_5F92")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5FB2")
    OP_52(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5FDC")

    label("loc_5FB2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5FD2")
    OP_52(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5FDC")

    label("loc_5FD2")

    OP_52(0x14, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5FDC")

    OP_52(0x14, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x14, 0x10)

    ChrTalk(
        0x13,
        "Hey, it's you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FMr. Scott and Mr. Wenzel...\x01",
            "You came all the way to the border.\x02\x03",
            "Could you be headed to the Republic?\x01",
            "Or is there a Cryptid at Tangram Hill?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "No, that's not it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Even if one did appear on\x01",
            "Tangram Hill, that would be\x01",
            "within CGF jurisdiction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FYou're certainly right about that.\x01",
            "...Umm, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "We investigated the East Crossbell Highway\x01",
            "area, where you defeated the Cryptid yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "If the "Pleroma Grass" or whatever really is connected\x01",
            "to Cryptids appearance, we wanted to see\x01",
            "if there was anymore blooming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FI see...\x01",
            "It does seem necessary to check on that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FSince you guys are Bracers, you're \x01",
            "able to go investigate places we can't\x01",
            "like back regions and so on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "Yeah, exactly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Leave this to us for now.\x01",
            "There must be things only\x01",
            "you guys can do as well.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x13, 0x10)
    SetChrFlags(0x14, 0x10)
    SetChrSubChip(0x13, 0x0)
    SetChrSubChip(0x14, 0x0)
    SetScenarioFlags(0x17C, 7)
    Return()

    # Function_23_5E01 end

    def Function_24_636E(): pass

    label("Function_24_636E")

    SetChrFlags(0x13, 0x10)
    SetChrFlags(0x14, 0x10)
    SetChrSubChip(0x13, 0x0)
    SetChrSubChip(0x14, 0x0)

    ChrTalk(
        0x13,
        (
            "Even so...\x01",
            "Following the Trade Conference\x01",
            "we can't get any less busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "I can't see Pearl,\x01",
            "my fiancｳe, at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "The girl working at the department store, eh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Well...nothing we can do about it now.\x01",
            "We're short on staff, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "When the matter in question is solved,\x01",
            "you should ask Michel for a day off.\x01",
            "I'll help adjust the daily schedule too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Ha ha, thank you, Wenzel.\x01",
            "I keep always being helped by you.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x13, 0x10)
    ClearChrFlags(0x14, 0x10)
    SetScenarioFlags(0x1, 2)
    SetScenarioFlags(0x1, 3)
    Return()

    # Function_24_636E end

    def Function_25_6547(): pass

    label("Function_25_6547")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_655C")
    Call(0, 23)
    Jump("loc_6643")

    label("loc_655C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_656E")
    Call(0, 24)
    Jump("loc_6643")

    label("loc_656E")


    ChrTalk(
        0xFE,
        (
            "I confirmed the report we received from you and\x01",
            "in the place where the other Cryptid appeared,\x01",
            ""Pleroma Grass" was blooming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...What a mysterious plant.\x01",
            "It seems it would be better to be very careful...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6643")

    TalkEnd(0xFE)
    Return()

    # Function_25_6547 end

    def Function_26_6647(): pass

    label("Function_26_6647")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6701")

    ChrTalk(
        0xFE,
        (
            "At the time of the raid incident,\x01",
            "I was at Armorica Village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I could contact Ryｹand father and know\x01",
            "they were well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...I was really relieved.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_675B")

    label("loc_6701")


    ChrTalk(
        0xFE,
        (
            "I guess I'll go back home in a little while.\x01",
            "I'm worried about Ryｹ and father, so...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_675B")

    TalkEnd(0xFE)
    Return()

    # Function_26_6647 end

    def Function_27_675F(): pass

    label("Function_27_675F")

    EventBegin(0x0)
    Fade(500)
    OP_68(106160, 1050, 2060, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(26130, 0)
    SetChrPos(0x101, 104310, 0, 2009, 90)
    SetChrPos(0x109, 104340, 0, 3150, 135)
    SetChrPos(0x102, 104290, 0, 980, 90)
    SetChrPos(0x104, 104150, 0, -190, 45)
    SetChrPos(0x103, 103100, 0, 930, 90)
    SetChrPos(0x105, 102910, 0, -220, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xA, 0xFF)
    TurnDirection(0xA, 0x109, 0)
    OP_0D()

    ChrTalk(
        0xA,
        (
            "Hi, Master Sergeant Noｱl. Are you\x01",
            "together with everyone from the SSS?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FThank you for your hard work, Mr. Temas.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FUhhm, today we\x01",
            "came for work...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 500)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Explained that you came to collect data\x01",
            "for the "gourmet recommendations".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        (
            "Ah, indeed, I think I was asked\x01",
            "that by the News Service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The "Rich Sea Hot Pot", Tangram\x01",
            "specialty, is just ready.\x01",
            "You can eat it with everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FOh, so at your mess hall the\x01",
            "main dish is a sea hot pot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F*giggle*, thank you. We'd love to try it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The, please wait.\x01",
            "I'll make the portions now.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and the others ate the Rich Sea Hot Pot.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#00200F*chomp chomp*...\x01",
            "The taste is quite good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, it seems the original taste\x01",
            "of the fish comes out nicely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Ha ha, I know, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Because the hot pot is easy and tasty,\x01",
            "we do it often at Tangram Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's really lively and fun when\x01",
            "everyone is merrily around the pot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F...Now that I think about it, I didn't\x01",
            "pick in a hot pot like this at all\x01",
            "with the Testaments' guys.\x02\x03",
            "#10302FHu hu, if I have the chance, I think\x01",
            "I'll come here with the others too.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6CBF():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6CBF)
    Sleep(50)

    def lambda_6CCF():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6CCF)
    Sleep(50)

    def lambda_6CDF():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6CDF)
    Sleep(50)

    def lambda_6CEF():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6CEF)
    Sleep(50)

    def lambda_6CFF():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6CFF)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00305FEeh...\x01",
            "Somehow you're saying an unusual thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102F*giggle*, I believe he\x01",
            "liked this dish a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FThen, it could be nice to\x01",
            "leave this presentation\x01",
            "to Mr. Wazy.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x105, 0x0, 0x1F4)

    ChrTalk(
        0x105,
        (
            "#10304FOh boy, it's a bother,\x01",
            "but I think I'll accept.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1, 1)
    SetScenarioFlags(0x173, 3)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_6E4F")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6E4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_6E6C")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6E6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_6E7F")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6E7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_6E92")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6E92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_6EAF")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6EAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_6EC2")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6EC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_6EDF")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6EDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_6EF2")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6EF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_6F0F")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6F0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_6F22")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6F22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_6F3F")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6F3F")

    OP_29(0x80, 0x1, 0xC)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7067")
    SetChrName("")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Finished to collect data from six food places!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_705E")

    AnonymousTalk(
        0x101,
        (
            "#00003FIt seems we could go report\x01",
            "to Miss Grace immediately, but...\x02\x03",
            "#00000FWe haven't found all six members'\x01",
            "favourites yet, so why don't we\x01",
            "try our best a little more?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_705E")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_7067")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_714B")
    SetChrName("")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Found the entire SSS\x01",
            "members' favourites!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00000FWith this, we found all\x01",
            "six members' favourites.\x02\x03",
            "We have plenty of data now.\x01",
            "Let's go now to the News Service to report.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x179, 0)
    OP_29(0x80, 0x1, 0xE)

    label("loc_714B")

    OP_4C(0xA, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 104640, 0, 1980, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_27_675F end

    def Function_28_717B(): pass

    label("Function_28_717B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(7990, 1000, 40, 0)
    MoveCamera(45, 32, 0, 0)
    OP_6E(470, 0)
    SetCameraDistance(24500, 0)
    SetChrFlags(0x8, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 10950, 0, 4070, 180)
    OP_4B(0x9, 0xFF)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    OP_71(0x5, 0x0, 0x8C, 0x1, 0x8)
    Sleep(300)
    Sound(143, 0, 100, 0)
    Sleep(200)
    Sound(145, 0, 100, 0)
    Sleep(1500)
    Sound(486, 0, 80, 0)
    OP_74(0x9, 0x1E)
    OP_71(0x9, 0x79, 0xB4, 0x1, 0x20)
    BeginChrThread(0x17, 1, 0, 29)
    Sleep(1500)
    Sound(487, 0, 50, 0)
    Sound(494, 0, 100, 0)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x8, 0x87, 0x0)
    OP_93(0x9, 0x87, 0x0)
    Sleep(1000)
    Sound(486, 0, 80, 0)
    OP_74(0xA, 0x1E)
    OP_71(0xA, 0x79, 0xB4, 0x1, 0x20)
    BeginChrThread(0x18, 1, 0, 29)
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1500)
    Sound(487, 0, 50, 0)
    Sound(494, 0, 100, 0)
    Sleep(1500)
    OP_64(0x8)
    OP_64(0x9)

    ChrTalk(
        0x8,
        "W-What the...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "R-Report!\x01",
            "Report to Vice Commander Douglas!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 2)
    NewScene("e4101", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_28_717B end

    def Function_29_733C(): pass

    label("Function_29_733C")

    SetChrPos(0xFE, -3500, 0, 0, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -2000, 0, 0)
    OP_9F(0x1, 3500, 0, -4000)
    OP_9F(0x1, 10500, 0, -4000)
    OP_9F(0x1, 25000, 0, -4000)
    OP_9F(0x2, 0xFE, 7000, 0x6)
    Return()

    # Function_29_733C end

    def Function_30_7393(): pass

    label("Function_30_7393")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-20630, 1000, -340, 0)
    MoveCamera(45, 32, 0, 0)
    OP_6E(470, 0)
    SetCameraDistance(20760, 0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x101, -28060, 0, 0, 270)
    SetChrPos(0x102, -28260, 0, -1200, 270)
    SetChrPos(0x104, -28260, 0, 1200, 270)
    SetChrPos(0x109, -29460, 0, 0, 270)
    SetChrPos(0x103, -29260, 0, -1200, 270)
    SetChrPos(0x105, -29260, 0, 1200, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    def lambda_7451():
        OP_95(0x101, -21060, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7451)
    Sleep(30)

    def lambda_746E():
        OP_95(0x102, -21260, 0, -1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_746E)
    Sleep(40)

    def lambda_748B():
        OP_95(0x104, -21260, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_748B)
    Sleep(800)

    def lambda_74A8():
        OP_95(0x109, -23560, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_74A8)
    Sleep(30)

    def lambda_74C5():
        OP_95(0x103, -23360, 0, -1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_74C5)
    Sleep(10)

    def lambda_74E2():
        OP_95(0x105, -23360, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_74E2)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
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

    ChrTalk(
        0x101,
        "#00000FT-That's...!\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(7990, 1000, 40, 0)
    MoveCamera(45, 32, 0, 0)
    OP_6E(470, 0)
    SetCameraDistance(24500, 0)
    SetChrFlags(0x8, 0x8000)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 10950, 0, 4070, 180)
    OP_4B(0x9, 0xFF)
    OP_0D()
    OP_71(0x5, 0x0, 0x8C, 0x1, 0x8)
    Sleep(300)
    Sound(143, 0, 100, 0)
    Sleep(200)
    Sound(145, 0, 100, 0)
    Sleep(1500)
    Sound(486, 0, 80, 0)
    OP_74(0x9, 0x1E)
    OP_71(0x9, 0x79, 0xB4, 0x1, 0x20)
    BeginChrThread(0x17, 1, 0, 29)
    Sleep(1500)
    Sound(487, 0, 50, 0)
    Sound(494, 0, 100, 0)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x8, 0x87, 0x0)
    OP_93(0x9, 0x87, 0x0)
    Sleep(1000)
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    ChrTalk(
        0x8,
        "W-What the...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "R-Report!\x01",
            "Report to Vice Commander Douglas!\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x8)
    OP_64(0x9)
    Fade(500)
    OP_68(-20630, 1000, -340, 0)
    MoveCamera(45, 32, 0, 0)
    OP_6E(470, 0)
    SetCameraDistance(20760, 0)
    OP_0D()

    ChrTalk(
        0x102,
        "#00107FAah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306FHe ran away...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FCrap, the cheated out medical\x01",
            "goods are in that truck...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FBut...\x01",
            "It seems impossible to reach him anymore.\x02\x03",
            "#00206FIt seems we were a step behind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108FIf we had used the orbal car,\x01",
            "we could've chased after him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306FOh boy, request failed, then.\x01",
            "...What do we do, Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F...For now, let's call Mr.\x01",
            "Billy and Mr. Ricardo.\x02\x03",
            "#00003FIt's regrettable, but...\x01",
            "We must properly report that\x01",
            "we couldn't catch him.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and the others told the\x01",
            "facts to Billy and Ricardo who \x01",
            "were waiting at the airport...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Afterwards, they went with\x01",
            "Billy to St. Ursula Hospital \x01",
            "to tell them the situation.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x22, 2)
    NewScene("t1530", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_30_7393 end

    def Function_31_7A34(): pass

    label("Function_31_7A34")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "CGF Only Freight Line Ahead\x01",
            "Authorized Personnel Only\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_31_7A34 end

    SaveToFile()

Try(main)
