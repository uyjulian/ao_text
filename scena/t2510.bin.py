from ScenarioHelper import *

def main():
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
        "Oliver members",           # 1
        "Jack member",           # 2
        "Timasu",               # 3
        "Alexei members",         # 4
        "Rug",                   # 5
        "tourist",                 # 6
        "tourist",                 # 7
        "tourist",                 # 8
        "tourist",                 # 9
        "tourist",                 # 10
        "boy",                 # 11
        "Mushroute Scott",         # 12
        "Wrestler Wenzel",     # 13
        "Chiluru",                 # 14
        "Special support vehicle",             # 15
        "Truck",                 # 16
        "For events",             # 17
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
        "Function_6_C0C",          # 06, 6
        "Function_7_C10",          # 07, 7
        "Function_8_1707",         # 08, 8
        "Function_9_1844",         # 09, 9
        "Function_10_1989",        # 0A, 10
        "Function_11_261F",        # 0B, 11
        "Function_12_2623",        # 0C, 12
        "Function_13_3072",        # 0D, 13
        "Function_14_394F",        # 0E, 14
        "Function_15_3953",        # 0F, 15
        "Function_16_43CA",        # 10, 16
        "Function_17_4598",        # 11, 17
        "Function_18_4902",        # 12, 18
        "Function_19_4AEA",        # 13, 19
        "Function_20_4CB7",        # 14, 20
        "Function_21_4E91",        # 15, 21
        "Function_22_4F66",        # 16, 22
        "Function_23_4FFD",        # 17, 23
        "Function_24_550C",        # 18, 24
        "Function_25_56A6",        # 19, 25
        "Function_26_5782",        # 1A, 26
        "Function_27_5867",        # 1B, 27
        "Function_28_61A2",        # 1C, 28
        "Function_29_636A",        # 1D, 29
        "Function_30_63C1",        # 1E, 30
        "Function_31_6A25",        # 1F, 31
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
            "Car magazine \"Army · Bombing Run! There is.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('警备色彩', 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C08")
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "Paint pattern\x01\x07\x02",
            "\"Guard color\"\x07\x00",
            "I learned.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber('警备色彩', 1)

    label("loc_C08")

    TalkEnd(0xFF)
    Return()

    # Function_5_B67 end

    def Function_6_C0C(): pass

    label("Function_6_C0C")

    Call(0, 7)
    Return()

    # Function_6_C0C end

    def Function_7_C10(): pass

    label("Function_7_C10")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_DD5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D29")

    NpcTalk(
        0x8,
        "Soldier Oliver",
        (
            "He ran away from the crossbell and was late\x01",
            "Republics are visiting.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Oliver",
        (
            "But, I can not solve the warning against the Republic\x01",
            "In the present situation Well, as expected\x01",
            "I have no choice but to stop.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Oliver",
        (
            "Because I know the feelings I want to return,\x01",
            "I am a little bit hurtful ….\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_DD0")

    label("loc_D29")


    NpcTalk(
        0x8,
        "Soldier Oliver",
        (
            "I can not solve the warning against the Republic\x01",
            "In the present situation Well, as expected\x01",
            "I have no choice but to stop.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Oliver",
        (
            "It may not be convincing,\x01",
            "I have no choice but to understand.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DD0")

    Jump("loc_1703")

    label("loc_DD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_110B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_F22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E9F")

    ChrTalk(
        0x8,
        (
            "I forced a little while ago\x01",
            "黒いTruckは、指名手配中の\x01",
            "It looks like it was from a con artist.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I was surprised when I was in tension … …\x01",
            "Anyway, I'm glad I was caught.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F1D")

    label("loc_E9F")


    ChrTalk(
        0x8,
        "Anyway, you guys cheers for good work, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Douglas deputy commander\x01",
            "Since I already reported it,\x01",
            "You do not have to worry about it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F1D")

    Jump("loc_1106")

    label("loc_F22")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_FD8")

    ChrTalk(
        0x8,
        (
            "A little while ago, I forced through the gate\x01",
            "黒いTruckは、指名手配中の\x01",
            "It seems that it was from a con artist.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In this tense state ……\x01",
            "It will do stupid things at all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1106")

    label("loc_FD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10B4")

    ChrTalk(
        0x8,
        (
            "Border tension,\x01",
            "It's just like the limit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Direction towards the Republic is Tangram Hills\x01",
            "Although there is a buffer zone,\x01",
            "Still I can not rest assured.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This is a storm.\x01",
            "I have to keep vigilant firmly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1106")

    label("loc_10B4")


    ChrTalk(
        0x8,
        (
            "For Crossbell,\x01",
            "This is a storm.\x01",
            "I have to keep vigilant firmly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1106")

    Jump("loc_1703")

    label("loc_110B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_12AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1209")

    ChrTalk(
        0x8,
        (
            "Yesterday, the Tangram gate also\x01",
            "Have to keep up with the response to derailment accidents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Also in the passenger bus of the Republic\x01",
            "Or asking for support,\x01",
            "It was pretty tough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "When this tense condition continues\x01",
            "It was an accident … Well,\x01",
            "It happened when the interval was bad.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12A9")

    label("loc_1209")


    ChrTalk(
        0x8,
        (
            "When this tense condition continues\x01",
            "It was an accident … Well,\x01",
            "It happened when the interval was bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "At least for the referendum\x01",
            "Any more unforeseen circumstances\x01",
            "Please do not hold back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12A9")

    Jump("loc_1703")

    label("loc_12AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_12BF")
    Call(0, 8)
    Jump("loc_1703")

    label("loc_12BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1485")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13D2")

    ChrTalk(
        0x8,
        (
            "Recently in the Republic,\x01",
            "Cross Bell Independence Complaints\x01",
            "It seems to be discussed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Moreover, unlike in the crossbell\x01",
            "It seems that most of them are opposite.\x01",
            "Well, I guess it can not be helped … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Residents' voting will be held nearby,\x01",
            "Independence is realized in this situation\x01",
            "I wonder what it is like to be.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1480")

    label("loc_13D2")


    ChrTalk(
        0x8,
        (
            "Residents' voting will be held nearby,\x01",
            "Independence is realized in this situation\x01",
            "I wonder what it is like to be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As a guard, by all means\x01",
            "I would like you to realize … …\x01",
            "It may be difficult as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1480")

    Jump("loc_1703")

    label("loc_1485")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1496")
    Call(0, 9)
    Jump("loc_1703")

    label("loc_1496")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_151C")

    ChrTalk(
        0x8,
        (
            "By Traffic Control Tan Ram Hills\x01",
            "A car that I could not pass came all at once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, I expected it to some extent\x01",
            "This guy is busy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1703")

    label("loc_151C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1703")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_15A6")

    ChrTalk(
        0x8,
        (
            "Douglas deputy commander exercises\x01",
            "Always feel that way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There are many strict things, but …\x01",
            "I have to persevere and keep up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1703")

    label("loc_15A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1682")

    ChrTalk(
        0x8,
        (
            "Going through here, with the autonomous province\x01",
            "It is a buffer zone of the Republic\x01",
            "\"Tangram Hills\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This hill is a passenger bus or a driving car\x01",
            "I wonder if there are many things to come and go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It seems to be a republic where power guided vehicles are popular\x01",
            "It can be said that it is a trend.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1703")

    label("loc_1682")


    ChrTalk(
        0x8,
        (
            "Tangram Hills,\x01",
            "With a passenger bus or a driving car\x01",
            "There are many things to come and go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It seems to be a republic where power guided vehicles are popular\x01",
            "It can be said that it is a trend.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1703")

    TalkEnd(0x8)
    Return()

    # Function_7_C10 end

    def Function_8_1707(): pass

    label("Function_8_1707")

    OP_4B(0x8, 0xFF)
    OP_4B(0xD, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17D7")

    ChrTalk(
        0x8,
        "Good work to be done early in the morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Recently, within autonomous state\x01",
            "An unknown intelligent beast\x01",
            "It has been witnessed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Driving the highway,\x01",
            "Please take care.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Well, I'm having trouble.\x01",
            "Let's be careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_183B")

    label("loc_17D7")


    ChrTalk(
        0x8,
        (
            "…… Then, in the immigration certificate\x01",
            "please sign this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Oh, that's it.\x01",
            "Sarah Sarasara ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_183B")

    OP_4C(0x8, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_8_1707 end

    def Function_9_1844(): pass

    label("Function_9_1844")

    OP_4B(0x8, 0xFF)
    OP_4B(0xE, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1919")

    ChrTalk(
        0x8,
        (
            "When I arrived at the city, I went to the city hall\x01",
            "Please report the parking place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you forget this, put a monopolist sticker\x01",
            "Please be careful as it will be stuck.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Oops, is that so?\x01",
            "I am troublesome unexpectedly …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_1980")

    label("loc_1919")


    ChrTalk(
        0x8,
        (
            "When I arrived at the city, I went to the city hall\x01",
            "Please report car parking registration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Well, it's okay.\x02",
    )

    CloseMessageWindow()

    label("loc_1980")

    OP_4C(0x8, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_9_1844 end

    def Function_10_1989(): pass

    label("Function_10_1989")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1ACA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A22")

    NpcTalk(
        0x9,
        "Soldier Jack",
        "Anomaly in the direction of wetlands, ants! It is!\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Soldier Jack",
        (
            "That mysterious big tree is one ……\x01",
            "Anxiety can not be hidden completely.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1AC5")

    label("loc_1A22")


    NpcTalk(
        0x9,
        "Soldier Jack",
        (
            "That mysterious big tree is one ……\x01",
            "Anxiety can not be hidden completely.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Soldier Jack",
        (
            "And anyway … …\x01",
            "Calmly at any time!\x01",
            "It is important to calm down!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AC5")

    Jump("loc_261B")

    label("loc_1ACA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1D4D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1B63")

    ChrTalk(
        0x9,
        (
            "In the past, really\x01",
            "I was surprised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Although it was good because it was caught ……\x01",
            "…… I want the rules to be kept\x01",
            "There is.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D48")

    label("loc_1B63")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_1BD4")

    ChrTalk(
        0x9,
        (
            "In the past, really\x01",
            "I was surprised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "…… I want the rules to be kept\x01",
            "There is.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D48")

    label("loc_1BD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CC1")

    ChrTalk(
        0x9,
        (
            "In the Altair city of the border,\x01",
            "Movement to the Republican Army\x01",
            "It is seen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Even starting a big exercise\x01",
            "Pressure on the crossbell … …\x01",
            "There must be such a purpose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "…… It is a serious situation.\x01",
            "If we do not work hard … …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1D48")

    label("loc_1CC1")


    ChrTalk(
        0x9,
        (
            "In the Altair city of the border,\x01",
            "Movement to the Republican Army\x01",
            "It is seen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "…… It is a serious situation.\x01",
            "If we do not work hard … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D48")

    Jump("loc_261B")

    label("loc_1D4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1FB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EF7")

    ChrTalk(
        0x9,
        (
            "Abnormal · Pear! This degree of rain,\x01",
            "security#4RDisplay#Influence on minor#4RDisplay#It is! It is!\x02",
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
        "#00206F…… It is 0 point.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Happy\x01",
            "Besides, in Djare separately\x01",
            "There is not! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I am like this rain\x01",
            "Without significant impact\x01",
            "I just wanted to say … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FHaha, I know.\x01",
            "(… but, maybe I oked it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1FB2")

    label("loc_1EF7")


    ChrTalk(
        0x9,
        (
            "じ、I am like this rain\x01",
            "Without significant impact\x01",
            "That's why I wanted to say … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Under this tense condition,\x01",
            "Such a tricky thing\x01",
            "It is not because you are!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FWell, even without such a panic ……\x02",
    )

    CloseMessageWindow()

    label("loc_1FB2")

    Jump("loc_261B")

    label("loc_1FB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_213B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20AE")

    ChrTalk(
        0x9,
        (
            "\"Phantom beast\", on the Tangram Hills\x01",
            "It does not appear to be appearing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "There is a buffer zone with the Republic.\x01",
            "Even if it goes to get rid of when it appears\x01",
            "It is variously troublesome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Although it is not necessarily not to come out in the future … …\x01",
            "Anyway, we are strictly vigilant!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2136")

    label("loc_20AE")


    ChrTalk(
        0x9,
        (
            "\"Phantom beast\", on the Tangram Hills\x01",
            "It does not appear to be appearing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Although it is not necessarily not to come out in the future … …\x01",
            "Anyway, we are strictly vigilant!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2136")

    Jump("loc_261B")

    label("loc_213B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_238D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2314")

    ChrTalk(
        0x9,
        (
            "It was destroyed at the time of the trade meeting\x01",
            "Recovery of radar facilities,\x01",
            "It has been completed during this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "But for the terrorists,\x01",
            "Stolen our eyes and facilities\x01",
            "I will destroy …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Thinking carefully\x01",
            "改めて不可解ではThere is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F(… called the armored car that appeared in the basement,\x01",
            "Certainly the terrorists alone\x01",
            "I was prepared too much. )\x02\x03",
            "#00003F(After all, cooperation of \"association\"\x01",
            "It may have been there. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F(Well, there is no proof, though.\x01",
            "The possibility is high. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2388")

    label("loc_2314")


    ChrTalk(
        0x9,
        (
            "Hmm, regarding that terrorist\x01",
            "There is still a doubt … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Anyway, now we need security\x01",
            "It is making it strictly!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2388")

    Jump("loc_261B")

    label("loc_238D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2483")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2414")

    ChrTalk(
        0x9,
        "For now it is abnormal · pear!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Terrorist …\x01",
            "Since information got in,\x01",
            "I am struck with full power.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_247E")

    label("loc_2414")


    ChrTalk(
        0x9,
        (
            "Our guards absolutely have the leaders\x01",
            "I will protect you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Tentatively,\x01",
            "For now it is abnormal · pear!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_247E")

    Jump("loc_261B")

    label("loc_2483")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_254E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2512")

    ChrTalk(
        0x9,
        (
            "President Rock Smith '\x01",
            "It was abnormal · pear! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Continue to guard the trade council\x01",
            "We will continue!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2549")

    label("loc_2512")


    ChrTalk(
        0x9,
        (
            "Continue to guard the trade council\x01",
            "We will continue!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2549")

    Jump("loc_261B")

    label("loc_254E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_261B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_25D6")

    ChrTalk(
        0x9,
        (
            "In the previous exercise,\x01",
            "It was a very good experience!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "To the future security, by all means\x01",
            "I am willing to keep alive!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_261B")

    label("loc_25D6")


    ChrTalk(
        0x9,
        "Abnormal · Pear!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "For the trade meeting,\x01",
            "The security system is perfect!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_261B")

    TalkEnd(0xFE)
    Return()

    # Function_10_1989 end

    def Function_11_261F(): pass

    label("Function_11_261F")

    Call(0, 12)
    Return()

    # Function_11_261F end

    def Function_12_2623(): pass

    label("Function_12_2623")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_264C")
    Call(0, 27)
    Return()

    label("loc_264C")

    TalkBegin(0xA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2659")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_306E")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",          # 0
            "to shop\x01",      # 1
            "quit\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26B7")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_26B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26D7")
    OP_AF(0x6E)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3069")

    label("loc_26D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26EB")
    Jump("loc_3069")

    label("loc_26EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2703")
    TalkEnd(0xA)
    Return()

    label("loc_2703")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3069")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_27A8")

    ChrTalk(
        0xA,
        (
            "Because the pot is easy and delicious,\x01",
            "I do well at the Tangram gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Everyone surrounds the waiwai pot,\x01",
            "After all it's lively and fun.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3069")

    label("loc_27A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_28E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2868")

    ChrTalk(
        0xA,
        (
            "It's such a time ……\x01",
            "Would you like to eat something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I feel uneasy and irritated,\x01",
            "I am sure I am hungry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "After eating it,\x01",
            "You should settle down your mind once.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_28E0")

    label("loc_2868")


    ChrTalk(
        0xA,
        (
            "I feel uneasy and irritated,\x01",
            "I am sure I am hungry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "After eating it,\x01",
            "You should settle down your mind once.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28E0")

    Jump("loc_3069")

    label("loc_28E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2A4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29BE")

    ChrTalk(
        0xA,
        (
            "Damage to the guard …\x01",
            "隊員じゃない僕やRugさんも\x01",
            "It was pretty good event.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I fell down in the middle of my mind,\x01",
            "They also regretted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "At least, the remaining members\x01",
            "I want you to regain your energy …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2A49")

    label("loc_29BE")


    ChrTalk(
        0xA,
        (
            "Sacrifice members ……\x01",
            "I fell down in the middle of my mind,\x01",
            "They also regretted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "At least, the remaining members\x01",
            "I want you to regain your energy …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A49")

    Jump("loc_3069")

    label("loc_2A4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2ADA")

    ChrTalk(
        0xA,
        (
            "Yesterday, by train transfer with transport bus\x01",
            "A lot of customers were sent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The majority has already come back,\x01",
            "It was serious as expected.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3069")

    label("loc_2ADA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2B90")

    ChrTalk(
        0xA,
        (
            "This situation that continues in tension,\x01",
            "There is no strange chef like me\x01",
            "There is little that I can do … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Everyone in the corps\x01",
            "In order to demonstrate 100 power,\x01",
            "I have to make at least an uma dish.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3069")

    label("loc_2B90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2CE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C5E")

    ChrTalk(
        0xA,
        (
            "Independent advocacy …… Cross Bell also\x01",
            "It is becoming a serious thing somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Empire and Republic\x01",
            "I do not think he will forgive me … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Personally, the mayors\x01",
            "I wish you good luck.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2CE1")

    label("loc_2C5E")


    ChrTalk(
        0xA,
        (
            "Empire and Republic,\x01",
            "Easy to be independent\x01",
            "I do not think he will forgive me … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Personally, the mayors\x01",
            "I wish you good luck.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CE1")

    Jump("loc_3069")

    label("loc_2CE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2D7D")

    ChrTalk(
        0xA,
        (
            "With countermeasures against terrorism,\x01",
            "Everyone in the guard is pretty\x01",
            "It looks like I'm on fire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "This place is eaten with Gatsuri,\x01",
            "I have to work hard all day.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3069")

    label("loc_2D7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2F0F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E6F")

    ChrTalk(
        0xA,
        (
            "Speaking of Calvert,\x01",
            "Long ago many different cultures\x01",
            "It is a country that has accepted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Eastern culture is one of them,\x01",
            "Much impact on the world of cooking\x01",
            "It is said to have given.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Actually, Oriental cuisine is outstanding.\x01",
            "There are many places to learn as cook.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2F0A")

    label("loc_2E6F")


    ChrTalk(
        0xA,
        (
            "Eastern culture accepted by the Republic,\x01",
            "Much impact on the world of cooking\x01",
            "It is said to have given.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Actually, Oriental cuisine is outstanding.\x01",
            "There are many places to learn as cook.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F0A")

    Jump("loc_3069")

    label("loc_2F0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3069")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FF2")

    ChrTalk(
        0xA,
        (
            "New deputy commander Sun,\x01",
            "It is quite funny older brother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Cool Sogna Command\x01",
            "Also different type, with guyguy\x01",
            "It is a reliable person to pull everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "To the guard as well\x01",
            "I wish there was an excellent person.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3069")

    label("loc_2FF2")


    ChrTalk(
        0xA,
        (
            "New deputy commander Sun,\x01",
            "Guigui it will pull everyone\x01",
            "He is a reliable person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "To the guard as well\x01",
            "I wish there was an excellent person.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3069")

    Jump("loc_2659")

    label("loc_306E")

    TalkEnd(0xA)
    Return()

    # Function_12_2623 end

    def Function_13_3072(): pass

    label("Function_13_3072")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3221")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_317A")

    NpcTalk(
        0xB,
        "Soldier Alexei",
        "Fu … … I do not have much appetite.\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "Soldier Alexei",
        (
            "…… No, this is the time\x01",
            "I have to eat it even if it is impossible.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "Soldier Alexei",
        (
            "In preparation for the invasion of the Empire and the Republic,\x01",
            "I will protect this crossbell …\x01",
            "…… to fulfill its mission.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_321C")

    label("loc_317A")


    NpcTalk(
        0xB,
        "Soldier Alexei",
        (
            "Many things happened too much …\x01",
            "It seems that my head is confused.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "Soldier Alexei",
        (
            "I will protect this crossbell.\x01",
            "… … I have to fulfill that mission.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_321C")

    Jump("loc_394B")

    label("loc_3221")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_32BF")

    ChrTalk(
        0xB,
        (
            "City attackers,\x01",
            "Where are you latent now … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "…… Hung, superior.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "To defeat our enemies … …\x01",
            "I'll definitely sacrifice someday.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_394B")

    label("loc_32BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3352")

    ChrTalk(
        0xB,
        (
            "Fu … … the meal after work\x01",
            "It is exactly the best horse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I do not know what will happen in the future …\x01",
            "Just for belly\x01",
            "I have to keep it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_394B")

    label("loc_3352")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_34DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_343F")

    ChrTalk(
        0xB,
        (
            "Crossbell is independent,\x01",
            "The guard has been working as an army\x01",
            "When it seems to be recognized … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "By all means not only armed,\x01",
            "It is what I want you to improve.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "That is really tasteless\x01",
            "You can not say it …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_34D6")

    label("loc_343F")


    ChrTalk(
        0xB,
        (
            "…… Meals served in the Imperial Army,\x01",
            "I hear that it is rather unpleasant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you independently form the empire,\x01",
            "Surely the alignment will improve as well.\x01",
            "…… It is totally my imagination.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34D6")

    Jump("loc_394B")

    label("loc_34DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_357E")

    ChrTalk(
        0xB,
        (
            "Phantom beast … as far as I heard the report\x01",
            "It was a fairly strong partner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We guard the alert of the border\x01",
            "I need to focus …\x01",
            "We left it to you later.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_394B")

    label("loc_357E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_363D")

    ChrTalk(
        0xB,
        (
            "Terrorists may appear … …\x01",
            "In fact, how do you intrude\x01",
            "It is important to try.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Collaborators may already have entered.\x01",
            "Even though it is a moment today I am completely mindful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_394B")

    label("loc_363D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_37B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3729")

    ChrTalk(
        0xB,
        (
            "Oh, I'm also on Michelin\x01",
            "I wanted to go for security.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Although I have been there only once,\x01",
            "The meshes of that restaurant over there\x01",
            "Fairly …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "…… Michelam is on duty\x01",
            "Truly a restaurant\x01",
            "Are not you doing it?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_37B3")

    label("loc_3729")


    ChrTalk(
        0xB,
        (
            "…… Michelam is on duty\x01",
            "Truly a restaurant\x01",
            "Are not you doing it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "… …. munching.\x01",
            "For now, I'd like to get a mess\x01",
            "I'm going to eat it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37B3")

    Jump("loc_394B")

    label("loc_37B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_394B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_38E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3870")

    ChrTalk(
        0xB,
        "Puaku, mushrooms ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "After the exercise\x01",
            "Mesh is exceptional.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Even before exercise\x01",
            "I gave you a belly,\x01",
            "I can not stop doing nothing but college.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_38DE")

    label("loc_3870")


    ChrTalk(
        0xB,
        (
            "Even the fucking disgust,\x01",
            "After exercise I feel delicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "After the exercise\x01",
            "I think that Mesh is exceptional.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38DE")

    Jump("loc_394B")

    label("loc_38E3")


    ChrTalk(
        0xB,
        (
            "Munching …\x01",
            "Very fine …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Today is a story to do exercises,\x01",
            "I have to get on with a firm bite.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_394B")

    TalkEnd(0xFE)
    Return()

    # Function_13_3072 end

    def Function_14_394F(): pass

    label("Function_14_394F")

    Call(0, 15)
    Return()

    # Function_14_394F end

    def Function_15_3953(): pass

    label("Function_15_3953")

    TalkBegin(0xC)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3960")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43C6")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",        # 0
            "To take a break\x01",      # 1
            "quit\x01",          # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39BC")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_39BC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39DC")
    OP_AF(0x6F)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_43C1")

    label("loc_39DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39F0")
    Jump("loc_43C1")

    label("loc_39F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A08")
    TalkEnd(0xC)
    Return()

    label("loc_3A08")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43C1")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3B70")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AEC")

    ChrTalk(
        0xC,
        (
            "Rumor in the wind, Iria's consciousness\x01",
            "I heard that I returned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "From now on, crossbell\x01",
            "In a serious situation gradually\x01",
            "It will be hit by … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "As long as there is light called Iria,\x01",
            "Surely we are okay.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3B6B")

    label("loc_3AEC")


    ChrTalk(
        0xC,
        (
            "From now on, crossbell\x01",
            "In a serious situation gradually\x01",
            "It will be hit by … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "As long as there is light called Iria,\x01",
            "Surely we are okay.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B6B")

    Jump("loc_43C1")

    label("loc_3B70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3CED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C56")

    ChrTalk(
        0xC,
        (
            "Iria · Platier\x01",
            "For many people living in the crossbell\x01",
            "It is like a sun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "It seems that she was seriously injured … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "…… No, I do not get into work.\x01",
            "I wonder if she can return to the stage ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3CE8")

    label("loc_3C56")


    ChrTalk(
        0xC,
        (
            "噂では、Iria · Platier\x01",
            "It seems that consciousness has not returned yet …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "…… No, I do not get into work.\x01",
            "I wonder if she can return to the stage ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CE8")

    Jump("loc_43C1")

    label("loc_3CED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3E62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DDE")

    ChrTalk(
        0xC,
        (
            "Tomorrow will finally be the alkane shell\x01",
            "Renewal performance ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Again attention is playing \"Princess of the Star\"\x01",
            "Whether it is a newcomer of expectation or …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Eventually I could not get a ticket,\x01",
            "Crossbell Times will feature.\x01",
            "I'm looking forward to it ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3E5D")

    label("loc_3DDE")


    ChrTalk(
        0xC,
        (
            "Tomorrow will finally be the alkane shell\x01",
            "Renewal performance ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "What can we do ……\x01",
            "Crossbell Times'\x01",
            "I am looking forward to the next feature.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E5D")

    Jump("loc_43C1")

    label("loc_3E62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3EE4")

    ChrTalk(
        0xC,
        "These days, it is something special.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Talk that it will rain tomorrow, too,\x01",
            "Even in fan book of alkane shell\x01",
            "I suppose you are reading … ….\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43C1")

    label("loc_3EE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4061")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FD7")

    ChrTalk(
        0xC,
        (
            "Security guards are in a state of tension of the two major powers,\x01",
            "It seems that I am making it so busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Meanwhile, the work of the guard\x01",
            "Support Division and Guild\x01",
            "She seems to have taken over … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "From now on, somehow\x01",
            "I wish I could make up for it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_405C")

    label("loc_3FD7")


    ChrTalk(
        0xC,
        (
            "The guard's job\x01",
            "Support Division and Guild\x01",
            "She seems to have taken over … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "From now on, somehow\x01",
            "I wish I could make up for it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_405C")

    Jump("loc_43C1")

    label("loc_4061")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4219")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4175")

    ChrTalk(
        0xC,
        (
            "The danger of terrorism,\x01",
            "If they are \"justice\"\x01",
            "I am in the place to believe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "For sacrifice for purpose …\x01",
            "I do not feel it is evil,\x01",
            "Just say it shittinly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "In order not to let such a thing,\x01",
            "I'd like people in the team to work hard.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4214")

    label("loc_4175")


    ChrTalk(
        0xC,
        (
            "For sacrifice for purpose …\x01",
            "Such a fucking idea,\x01",
            "It is at the root of terrorism.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "In order not to let such a thing,\x01",
            "I'd like people in the team to work hard.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4214")

    Jump("loc_43C1")

    label("loc_4219")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_42B8")

    ChrTalk(
        0xC,
        (
            "The leaders who entered the crossbell\x01",
            "Tonight, the stage of the alkane shell\x01",
            "It seems to have a theater …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "This is the privilege of state guests.\x01",
            "I am envious of obedience … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43C1")

    label("loc_42B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_43C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4353")

    ChrTalk(
        0xC,
        (
            "The performance of the alkane shell\x01",
            "It is approaching……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The ticket sales also\x01",
            "It seems to be a tremendous speed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "There is no choice but to give up again ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_43C1")

    label("loc_4353")


    ChrTalk(
        0xC,
        (
            "I am Iria-Platier\x01",
            "He's a big fan …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I would like to go to see the performance next time,\x01",
            "There is no choice but to give up again ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43C1")

    Jump("loc_3960")

    label("loc_43C6")

    TalkEnd(0xC)
    Return()

    # Function_15_3953 end

    def Function_16_43CA(): pass

    label("Function_16_43CA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4469")

    ChrTalk(
        0xD,
        (
            "No way, I was on a trip\x01",
            "I do not believe that a raid incident will happen … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Hun, you can protect one city and what is the guard.\x01",
            "I can not stay in such a dangerous country.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4594")

    label("loc_4469")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4477")
    Jump("loc_4594")

    label("loc_4477")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4488")
    Call(0, 8)
    Jump("loc_4594")

    label("loc_4488")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4496")
    Jump("loc_4594")

    label("loc_4496")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4521")

    ChrTalk(
        0xD,
        (
            "Today's plenary session\x01",
            "What kind of aspect do you expect? …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "When I return to the Republic,\x01",
            "Next issue Crossbell Times\x01",
            "I am going to order it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4594")

    label("loc_4521")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_452F")
    Jump("loc_4594")

    label("loc_452F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4594")

    ChrTalk(
        0xD,
        (
            "With driving of Tangram Hills\x01",
            "I am tired and we are sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Which in the dining room?\x01",
            "I will eat it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4594")

    TalkEnd(0xFE)
    Return()

    # Function_16_43CA end

    def Function_17_4598(): pass

    label("Function_17_4598")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_461E")

    ChrTalk(
        0xE,
        (
            "Uh, noisy\x01",
            "Although the barrier was released\x01",
            "I can not return to the Republic … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "At least this child alone\x01",
            "If we do not protect it ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48FE")

    label("loc_461E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_46EE")

    ChrTalk(
        0xE,
        (
            "I sympathize with the crossbell people, but …\x01",
            "If there is a proper army\x01",
            "The damage should have been minimized.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "After all, it came out at the trade meeting\x01",
            "President and the idea of \"Chancellor of Iron and Blood\"\x01",
            "Should I have accepted it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48FE")

    label("loc_46EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4794")

    ChrTalk(
        0xE,
        (
            "A colleague who went on business on a business trip to the Republic,\x01",
            "I heard you were involved in a train accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I am heading to a hospital that I am hospitalized from now … …\x01",
            "I am glad that my life has been saved for the foreseeable future.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48FE")

    label("loc_4794")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_47A2")
    Jump("loc_48FE")

    label("loc_47A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_483F")

    ChrTalk(
        0xE,
        (
            "Crossbell residents\x01",
            "In thinking about independence, in a sense\x01",
            "I feel like I can not say it inevitable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "As long as my business is not adversely affected,\x01",
            "Do you sneak by this flow?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48FE")

    label("loc_483F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4850")
    Call(0, 9)
    Jump("loc_48FE")

    label("loc_4850")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_485E")
    Jump("loc_48FE")

    label("loc_485E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_48FE")

    ChrTalk(
        0xE,
        (
            "I am a personal grocer.\x01",
            "I came to buy on the crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "At the intersection of the continent Crossbell\x01",
            "Indeed, various goods can be found.\x01",
            "Hehe, I'm looking forward to it now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48FE")

    TalkEnd(0xFE)
    Return()

    # Function_17_4598 end

    def Function_18_4902(): pass

    label("Function_18_4902")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_497B")

    ChrTalk(
        0xF,
        (
            "Already, my dad\x01",
            "I got excited ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Okho, sorry.\x01",
            "Please do not feel bad.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AE6")

    label("loc_497B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4989")
    Jump("loc_4AE6")

    label("loc_4989")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4997")
    Jump("loc_4AE6")

    label("loc_4997")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4A35")

    ChrTalk(
        0xF,
        (
            "Anything, recently crossbell\x01",
            "A large unknown large monster\x01",
            "Does it appear?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Fare, scary …\x01",
            "When to come on a trip\x01",
            "I wonder if I made a mistake.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AE6")

    label("loc_4A35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4A43")
    Jump("loc_4AE6")

    label("loc_4A43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4ADD")

    ChrTalk(
        0xF,
        (
            "I was worried about the Orkis Tower and the lions\x01",
            "I came to see sightseeing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I already saw the announcement at the unveiling ceremony,\x01",
            "Let's suppose it is time to go home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AE6")

    label("loc_4ADD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4AE6")

    label("loc_4AE6")

    TalkEnd(0xFE)
    Return()

    # Function_18_4902 end

    def Function_19_4AEA(): pass

    label("Function_19_4AEA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4AFB")
    Jump("loc_4CB3")

    label("loc_4AFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4B2D")

    ChrTalk(
        0x10,
        "I guess the bus will come soon …\x02",
    )

    CloseMessageWindow()
    Jump("loc_4CB3")

    label("loc_4B2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4C03")

    ChrTalk(
        0x10,
        (
            "By the way yesterday,\x01",
            "The bar, who was doing a fake brand deal\x01",
            "He was arrested in Altair City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Well, I guess I'm shaki kaki\x01",
            "To untidy the vice business law something,\x01",
            "In a sense a poor bar.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CB3")

    label("loc_4C03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4C11")
    Jump("loc_4CB3")

    label("loc_4C11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4C1F")
    Jump("loc_4CB3")

    label("loc_4C1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4CAA")

    ChrTalk(
        0x10,
        (
            "Traffic regulation this morning,\x01",
            "Tangram ridge is also\x01",
            "I could not pass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Well, because it is the president's visit\x01",
            "I have no choice.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CB3")

    label("loc_4CAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4CB3")

    label("loc_4CB3")

    TalkEnd(0xFE)
    Return()

    # Function_19_4AEA end

    def Function_20_4CB7(): pass

    label("Function_20_4CB7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4D2A")

    ChrTalk(
        0x11,
        (
            "Oh, already!\x01",
            "Why is this\x01",
            "I wonder if it has become!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "Who the hell is it all over? Is it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_4E8D")

    label("loc_4D2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4D38")
    Jump("loc_4E8D")

    label("loc_4D38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4D46")
    Jump("loc_4E8D")

    label("loc_4D46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4D54")
    Jump("loc_4E8D")

    label("loc_4D54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4E05")

    ChrTalk(
        0x11,
        (
            "Members of the gate,\x01",
            "It's kind of crazy ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "I do not know how tense it is ….\x01",
            "It's a little bit better\x01",
            "You do not have a bee, do not you ~?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E8D")

    label("loc_4E05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4E13")
    Jump("loc_4E8D")

    label("loc_4E13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4E21")
    Jump("loc_4E8D")

    label("loc_4E21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4E8D")

    ChrTalk(
        0x11,
        (
            "Well, the bus to Crossbell City\x01",
            "Where are you getting out of it …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "It is troublesome to hand in a transit, yeah.\x02",
    )

    CloseMessageWindow()

    label("loc_4E8D")

    TalkEnd(0xFE)
    Return()

    # Function_20_4CB7 end

    def Function_21_4E91(): pass

    label("Function_21_4E91")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4ECB")

    ChrTalk(
        0x12,
        (
            "Daddy ~ ….\x01",
            "I would like to return home ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F62")

    label("loc_4ECB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4ED9")
    Jump("loc_4F62")

    label("loc_4ED9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4EE7")
    Jump("loc_4F62")

    label("loc_4EE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4EF5")
    Jump("loc_4F62")

    label("loc_4EF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4F03")
    Jump("loc_4F62")

    label("loc_4F03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4F4B")

    ChrTalk(
        0x12,
        (
            "Grandpa,\x01",
            "Muzakashi talk is good\x01",
            "Let 's eat.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F62")

    label("loc_4F4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4F59")
    Jump("loc_4F62")

    label("loc_4F59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4F62")

    label("loc_4F62")

    TalkEnd(0xFE)
    Return()

    # Function_21_4E91 end

    def Function_22_4F66(): pass

    label("Function_22_4F66")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F7B")
    Call(0, 23)
    Jump("loc_4FF9")

    label("loc_4F7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F8D")
    Call(0, 24)
    Jump("loc_4FF9")

    label("loc_4F8D")


    ChrTalk(
        0xFE,
        (
            "Tentatively …\x01",
            "I have to focus on my work now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You guys will have work as well,\x01",
            "Please leave this investigation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FF9")

    TalkEnd(0xFE)
    Return()

    # Function_22_4F66 end

    def Function_23_4FFD(): pass

    label("Function_23_4FFD")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x13, 0x10)
    TurnDirection(0x13, 0x0, 0)
    OP_52(0x13, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_508E")
    Jump("loc_50D8")

    label("loc_508E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_50AE")
    OP_52(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_50D8")

    label("loc_50AE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_50CE")
    OP_52(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_50D8")

    label("loc_50CE")

    OP_52(0x13, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_50D8")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_518E")
    Jump("loc_51D8")

    label("loc_518E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_51AE")
    OP_52(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_51D8")

    label("loc_51AE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_51CE")
    OP_52(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_51D8")

    label("loc_51CE")

    OP_52(0x14, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_51D8")

    OP_52(0x14, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x14, 0x10)

    ChrTalk(
        0x13,
        "Hi, you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FMr. Scott ……\x01",
            "You have come to the border.\x02\x03",
            "Perhaps, towards the Republic … …\x01",
            "Or a phantom in the Tangram Hills?\x02",
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
            "Near the tangram ridge\x01",
            "Even if it appears\x01",
            "I guess it is the jurisdiction of the guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FThat's certainly the case.\x01",
            "Well then, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "We guilty of you exterminating the eidolite yesterday.\x01",
            "I'm investigating the vicinity of the East Crossbell Highway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "With preliminary grass that I was reporting\x01",
            "If it really relates to a phantom beast,\x01",
            "I have to check whether there are other blooms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FI see……\x01",
            "Indeed confirmation seems necessary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FIf you are a hasteist's older brother\x01",
            "We can not get in\x01",
            "You will be able to explore the outback.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "Well, that's it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Leave it to me for the time being.\x01",
            "You guys only to you all\x01",
            "There will be things that I can not do.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x13, 0x10)
    SetChrFlags(0x14, 0x10)
    SetChrSubChip(0x13, 0x0)
    SetChrSubChip(0x14, 0x0)
    SetScenarioFlags(0x17C, 7)
    Return()

    # Function_23_4FFD end

    def Function_24_550C(): pass

    label("Function_24_550C")

    SetChrFlags(0x13, 0x10)
    SetChrFlags(0x14, 0x10)
    SetChrSubChip(0x13, 0x0)
    SetChrSubChip(0x14, 0x0)

    ChrTalk(
        0x13,
        (
            "Even so ……\x01",
            "Following the trade meeting is quite\x01",
            "I can not get rid of busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Pearl's fiance also\x01",
            "I can not meet you hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "A daughter working in a department store ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Well … there is no way to deal with now.\x01",
            "It is because there are not enough people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Once a single project is completed,\x01",
            "You may apply for a holiday to Michelle.\x01",
            "I also cooperate in adjusting the schedule.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Thank you, Wenzel.\x01",
            "You are just being saved.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x13, 0x10)
    ClearChrFlags(0x14, 0x10)
    SetScenarioFlags(0x1, 2)
    SetScenarioFlags(0x1, 3)
    Return()

    # Function_24_550C end

    def Function_25_56A6(): pass

    label("Function_25_56A6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56BB")
    Call(0, 23)
    Jump("loc_577E")

    label("loc_56BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56CD")
    Call(0, 24)
    Jump("loc_577E")

    label("loc_56CD")


    ChrTalk(
        0xFE,
        (
            "I received your report and confirmed it,\x01",
            "Also quietly at other emerging beast appearance points\x01",
            "\"Praroma grass\" was in bloom.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… It is a plant that may be acquainted with anything.\x01",
            "It seems better to be careful with heavy attention …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_577E")

    TalkEnd(0xFE)
    Return()

    # Function_25_56A6 end

    def Function_26_5782(): pass

    label("Function_26_5782")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5820")

    ChrTalk(
        0xFE,
        (
            "In the event of a street attack,\x01",
            "I was in Almorika village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Once you contact,\x01",
            "Both Ryu and Dad\x01",
            "It's safe ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…… I was really relieved.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_5863")

    label("loc_5820")


    ChrTalk(
        0xFE,
        (
            "I guess I should return home after a while.\x01",
            "Ryu and Dad are worried … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5863")

    TalkEnd(0xFE)
    Return()

    # Function_26_5782 end

    def Function_27_5867(): pass

    label("Function_27_5867")

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
            "Hi, Sergeant Noel.\x01",
            "Together with the members of the Special Affairs Support Division?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100Fお疲れ様です、Timasuさん。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWell, today I am at work\x01",
            "I came ….\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 500)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "In the interview with \"One push gourmet\"\x01",
            "I explained what came.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        (
            "Oh, certainly to a correspondent\x01",
            "I wonder if I was asked for such a thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Just like the famous Tangram main gate\x01",
            "\"Yeon Shiba pot\" has just been made.\x01",
            "You should eat together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FOh, this is a cafeteria.\x01",
            "The fish pan was the main.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FHehe, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well then, please wait.\x01",
            "We can separate now.\x02",
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
            "Lloyd 's ate rice cup.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#00200FMunching …\x01",
            "It has a nice flavor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, the original taste of the fish\x01",
            "It seems that it is frequent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Haha, is not it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Because the pot is easy and delicious,\x01",
            "I do well at the Tangram gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Everyone surrounds the waiwai pot,\x01",
            "After all it's lively and fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FBy the way, with everyone in the tester\x01",
            "What pushed the pot like this\x01",
            "I wonder if it was so much.\x02\x03",
            "#10302FIf you have the opportunity, everyone\x01",
            "You may as well come and have fun.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5D1D():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5D1D)
    Sleep(50)

    def lambda_5D2D():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5D2D)
    Sleep(50)

    def lambda_5D3D():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5D3D)
    Sleep(50)

    def lambda_5D4D():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_5D4D)
    Sleep(50)

    def lambda_5D5D():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5D5D)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00305FOh\x01",
            "Do not say something rare.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FHehe, this dish\x01",
            "I wonder if you like it quite well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FThen, the introduction here\x01",
            "Who leaves it to Waji\x01",
            "It might be nice.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x105, 0x0, 0x1F4)

    ChrTalk(
        0x105,
        (
            "#10304FWhew, it is troublesome\x01",
            "I will take care of it.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1, 1)
    SetScenarioFlags(0x173, 3)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_5EAE")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5EAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_5ECB")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5ECB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_5EDE")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5EDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_5EF1")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5EF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_5F0E")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5F0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_5F21")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5F21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_5F3E")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5F3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_5F51")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5F51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_5F6E")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5F6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_5F81")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5F81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_5F9E")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5F9E")

    OP_29(0x80, 0x1, 0xC)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_60A1")
    SetChrName("")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "I finished interviewing 6 dining places!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6098")

    AnonymousTalk(
        0x101,
        (
            "#00003FMr. Grace right away\x01",
            "It seems I can go to the report … but …\x02\x03",
            "#00000FThe favorite of all six people still\x01",
            "It was not found.\x01",
            "Maybe I'll try harder?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_6098")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_60A1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6172")
    SetChrName("")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "All members of the Special Affairs Support Division\x01",
            "I found a favorite!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00000FWith this all six people\x01",
            "I found a favorite.\x02\x03",
            "This is enough for the interview.\x01",
            "Let's go report to the airlines immediately.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x179, 0)
    OP_29(0x80, 0x1, 0xE)

    label("loc_6172")

    OP_4C(0xA, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 104640, 0, 1980, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_27_5867 end

    def Function_28_61A2(): pass

    label("Function_28_61A2")

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
        "Wh … … what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Ho, report it!\x01",
            "It is reported to deputy commander Douglas!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 2)
    NewScene("e4101", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_28_61A2 end

    def Function_29_636A(): pass

    label("Function_29_636A")

    SetChrPos(0xFE, -3500, 0, 0, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -2000, 0, 0)
    OP_9F(0x1, 3500, 0, -4000)
    OP_9F(0x1, 10500, 0, -4000)
    OP_9F(0x1, 25000, 0, -4000)
    OP_9F(0x2, 0xFE, 7000, 0x6)
    Return()

    # Function_29_636A end

    def Function_30_63C1(): pass

    label("Function_30_63C1")

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

    def lambda_647F():
        OP_95(0x101, -21060, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_647F)
    Sleep(30)

    def lambda_649C():
        OP_95(0x102, -21260, 0, -1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_649C)
    Sleep(40)

    def lambda_64B9():
        OP_95(0x104, -21260, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_64B9)
    Sleep(800)

    def lambda_64D6():
        OP_95(0x109, -23560, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_64D6)
    Sleep(30)

    def lambda_64F3():
        OP_95(0x103, -23360, 0, -1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_64F3)
    Sleep(10)

    def lambda_6510():
        OP_95(0x105, -23360, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6510)
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
        "#00000FOh, that is …!\x02",
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
        "Wh … … what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Ho, report it!\x01",
            "It is reported to deputy commander Douglas!\x02",
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
        "#00107FAhh ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306FDid you escape … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003Fくそっ、あのTruckには\x01",
            "The deceived medical supplies ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FBut …\x01",
            "I can not chase anymore.\x02\x03",
            "#00206FIt looks like I was a step slow …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108FAlso using a power guide car\x01",
            "You ought to have chased afterwards …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306FWhew, is the request a failure?\x01",
            "…… What will you do, Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F… for the moment,\x01",
            "Let's contact Billy.\x02\x03",
            "#00003FIt is regrettable ….\x01",
            "You can not catch it\x01",
            "I have to report it properly.\x02",
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
            "Lloyd's told the story of things\x01",
            "Wait at Crossbell Airport\x01",
            "Tell Billy and Ricardo …\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "After that, with Billy\x01",
            "Circumstances to Ursula Hospital\x01",
            "It was going to tell.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x22, 2)
    NewScene("t1530", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_30_63C1 end

    def Function_31_6A25(): pass

    label("Function_31_6A25")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "In the meantime, the cargo line dedicated to the guard\x01",
            "Staff only\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_31_6A25 end

    SaveToFile()

Try(main)
