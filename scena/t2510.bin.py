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
        "Function_6_C17",          # 06, 6
        "Function_7_C1B",          # 07, 7
        "Function_8_1997",         # 08, 8
        "Function_9_1AC7",         # 09, 9
        "Function_10_1C41",        # 0A, 10
        "Function_11_2A7E",        # 0B, 11
        "Function_12_2A82",        # 0C, 12
        "Function_13_36BE",        # 0D, 13
        "Function_14_4141",        # 0E, 14
        "Function_15_4145",        # 0F, 15
        "Function_16_4DCE",        # 10, 16
        "Function_17_4FF7",        # 11, 17
        "Function_18_545A",        # 12, 18
        "Function_19_5683",        # 13, 19
        "Function_20_5855",        # 14, 20
        "Function_21_5A3D",        # 15, 21
        "Function_22_5B10",        # 16, 22
        "Function_23_5BB0",        # 17, 23
        "Function_24_610E",        # 18, 24
        "Function_25_62D2",        # 19, 25
        "Function_26_63B7",        # 1A, 26
        "Function_27_64C2",        # 1B, 27
        "Function_28_6EB1",        # 1C, 28
        "Function_29_7072",        # 1D, 29
        "Function_30_70C9",        # 1E, 30
        "Function_31_775E",        # 1F, 31
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
            "It's a car magazine,\x01",
            ""Marching Roaring Guy!".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x371, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C13")
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "Learned the \x07\x02",
            ""Guard\x01",
            "Coloring"\x07\x00",
            " paint pattern.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0x371, 1)

    label("loc_C13")

    TalkEnd(0xFF)
    Return()

    # Function_5_B67 end

    def Function_6_C17(): pass

    label("Function_6_C17")

    Call(0, 7)
    Return()

    # Function_6_C17 end

    def Function_7_C1B(): pass

    label("Function_7_C1B")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_E77")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D97")

    NpcTalk(
        0x8,
        "Soldier Oliver",
        (
            "The Republicans who were\x01",
            "late in escaping from\x01",
            "Crossbell are coming here.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Oliver",
        (
            "However, in the current situation where we\x01",
            "can't let down our guard towards the Republic,\x01",
            "we have no choice but to detain them.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Oliver",
        (
            "I understand why they want to\x01",
            "go home and so I feel a little\x01",
            "sorry for them. However...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E72")

    label("loc_D97")


    NpcTalk(
        0x8,
        "Soldier Oliver",
        (
            "In the current situation where we can't\x01",
            "let down our guard towards the Republic,\x01",
            "we have no choice but to detain them.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Oliver",
        (
            "Maybe they can't accept\x01",
            "it, I have to make them\x01",
            "understand.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E72")

    Jump("loc_1993")

    label("loc_E77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_122A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_FF3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F6B")

    ChrTalk(
        0x8,
        (
            "It seems the black truck that forced\x01",
            "its way through the gate earlier was\x01",
            "operated by a man wanted for swindling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It was surprising given this\x01",
            "state of tension... Anyhow,\x01",
            "I'm glad he was caught.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FEE")

    label("loc_F6B")


    ChrTalk(
        0x8,
        (
            "In any case, you guys\x01",
            "did a good job too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We've already reported it\x01",
            "to Vice Commander Douglas.\x01",
            "There's no need to worry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FEE")

    Jump("loc_1225")

    label("loc_FF3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_10C2")

    ChrTalk(
        0x8,
        (
            "It seems the black truck that forced\x01",
            "its way through the gate earlier was\x01",
            "operated by a man wanted for swindling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In this state of\x01",
            "tension... Honestly, what\x01",
            "a foolish thing to do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1225")

    label("loc_10C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11BC")

    ChrTalk(
        0x8,
        (
            "Tensions at the state\x01",
            "border are truly close\x01",
            "to their limit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Although the Republican border\x01",
            "has a buffer zone called Tangram\x01",
            "Hill, we can't rest easy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We have to brace ourselves.\x01",
            "We must continue to guard\x01",
            "diligently.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1225")

    label("loc_11BC")


    ChrTalk(
        0x8,
        (
            "We have to brace ourselves for the\x01",
            "sake of Crossbell as well. We must\x01",
            "continue to guard diligently.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1225")

    Jump("loc_1993")

    label("loc_122A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1430")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1367")

    ChrTalk(
        0x8,
        (
            "Yesterday, Tangram Gate was\x01",
            "pressed into dealing with the\x01",
            "derailment accident as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The Republican passenger\x01",
            "buses requested support\x01",
            "also... It was quite tough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "An accident happening in this continuing\x01",
            "state of tension... Oh man, what an\x01",
            "unfortunate thing to have happen.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_142B")

    label("loc_1367")


    ChrTalk(
        0x8,
        (
            "An accident happening in this continuing\x01",
            "state of tension... Oh man, what an\x01",
            "unfortunate thing to have happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I hope for no more\x01",
            "unforeseen circumstances at\x01",
            "least until the referendum.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_142B")

    Jump("loc_1993")

    label("loc_1430")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1441")
    Call(0, 8)
    Jump("loc_1993")

    label("loc_1441")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_16A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15B8")

    ChrTalk(
        0x8,
        (
            "Recently, the question of\x01",
            "Crossbell independence is being\x01",
            "discussed in the Republic as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Differently from Crossbell, it seems almost\x01",
            "everyone is against it. Well, I think\x01",
            "that's nothing to be surprised about...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The referendum will be held soon, but I\x01",
            "wonder what will happen if independence\x01",
            "is realized in a situation like this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_169E")

    label("loc_15B8")


    ChrTalk(
        0x8,
        (
            "The referendum will be held soon, but I\x01",
            "wonder what will happen if independence\x01",
            "is realized in a situation like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As a CGF member, I'd like very much\x01",
            "for it to be realized, but... As\x01",
            "expected, it might be difficult.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_169E")

    Jump("loc_1993")

    label("loc_16A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_16B4")
    Call(0, 9)
    Jump("loc_1993")

    label("loc_16B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1778")

    ChrTalk(
        0x8,
        (
            "The cars that couldn't pass through\x01",
            "Tangram Hill due to traffic\x01",
            "restrictions are coming in all at once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "*sigh*, to a certain\x01",
            "degree I expected this,\x01",
            "but man, it's so busy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1993")

    label("loc_1778")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1993")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1815")

    ChrTalk(
        0x8,
        (
            "Vice Commander Douglas's\x01",
            "trainings are always\x01",
            "like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There're harsh in a lot\x01",
            "of ways, but... We have\x01",
            "to do our best.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1993")

    label("loc_1815")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1902")

    ChrTalk(
        0x8,
        (
            "Past here is "Tangram Hill",\x01",
            "a buffer zone between\x01",
            "Crossbell and the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There's a lot of bus and\x01",
            "vehicle traffic through\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Popularization of orbal\x01",
            "vehicles is said to be a\x01",
            "trend in the Republic.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1993")

    label("loc_1902")


    ChrTalk(
        0x8,
        (
            "There's a lot of bus and\x01",
            "vehicle traffic through\x01",
            "Tangram Hill.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Popularization of orbal\x01",
            "vehicles is said to be a\x01",
            "trend in the Republic.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1993")

    TalkEnd(0x8)
    Return()

    # Function_7_C1B end

    def Function_8_1997(): pass

    label("Function_8_1997")

    OP_4B(0x8, 0xFF)
    OP_4B(0xD, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A5E")

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
            "in the state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Please be careful while\x01",
            "driving the highways.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Yes, thank you. I'll be\x01",
            "careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1ABE")

    label("loc_1A5E")


    ChrTalk(
        0x8,
        (
            "...Then, please sign\x01",
            "your entry certificate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Oh, that's right.\x01",
            "*scribble scribble*...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ABE")

    OP_4C(0x8, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_8_1997 end

    def Function_9_1AC7(): pass

    label("Function_9_1AC7")

    OP_4B(0x8, 0xFF)
    OP_4B(0xE, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BBB")

    ChrTalk(
        0x8,
        (
            "When you arrive in the\x01",
            "city, please notify City\x01",
            "Hall of your parking space.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you forget, they'll stick\x01",
            "a no parking sticker on your\x01",
            "vehicle, so be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Oh, is that so? What an\x01",
            "unexpected bother...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_1C38")

    label("loc_1BBB")


    ChrTalk(
        0x8,
        (
            "When you arrive at the city,\x01",
            "please deliver your vehicle\x01",
            "parking registration to City Hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Yeah yeah, roger that.\x02",
    )

    CloseMessageWindow()

    label("loc_1C38")

    OP_4C(0x8, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_9_1AC7 end

    def Function_10_1C41(): pass

    label("Function_10_1C41")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1DB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CF4")

    NpcTalk(
        0x9,
        "Soldier Jack",
        (
            "There's something weird\x01",
            "in the Marshlands!!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Soldier Jack",
        (
            "What in the world is\x01",
            "that mysterious tree...\x01",
            "I can't hide my unease.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1DAF")

    label("loc_1CF4")


    NpcTalk(
        0x9,
        "Soldier Jack",
        (
            "What in the world is\x01",
            "that mysterious tree...\x01",
            "I can't hide my unease.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x9,
        "Soldier Jack",
        (
            "A-Anyway... No matter the\x01",
            "time, we must remain composed!\x01",
            "Being calm is important!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DAF")

    Jump("loc_2A7A")

    label("loc_1DB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2065")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1E4F")

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
            "Although I'm happy he was\x01",
            "caught... ...I'd wish the\x01",
            "rules would be respected.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2060")

    label("loc_1E4F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_1EBD")

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
            "...I'd wish the rules\x01",
            "would be respected.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2060")

    label("loc_1EBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FCA")

    ChrTalk(
        0x9,
        (
            "At Altair City near the\x01",
            "border, Republican Army\x01",
            "movements can be seen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Starting large-scale exercises and\x01",
            "putting pressure on Crossbell...\x01",
            "That's probably their goal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...The situation is\x01",
            "alarming. We CGF need to\x01",
            "do everything we can...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2060")

    label("loc_1FCA")


    ChrTalk(
        0x9,
        (
            "At Altair City near the\x01",
            "border, Republican Army\x01",
            "movements can be seen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...The situation is\x01",
            "alarming. We CGF need to\x01",
            "do everything we can...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2060")

    Jump("loc_2A7A")

    label("loc_2065")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2305")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_223D")

    ChrTalk(
        0x9,
        (
            "Nothing out of the ordinary! This kind of\x01",
            "rain has got an insignificant influence\x01",
            "[軽微 keibi] on guarding [警備 keibi]!!\x02",
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
            "Huh... I-It wasn't a pun\x01",
            "at all, you know!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I wanted to say that this\x01",
            "level of rain doesn't\x01",
            "affect me much...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FAhaha, we know. (...However,\x01",
            "maybe he's relaxed a little\x01",
            "thanks to this.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2300")

    label("loc_223D")


    ChrTalk(
        0x9,
        (
            "I-I meant to say that\x01",
            "this level of rain\x01",
            "doesn't affect me much...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "This state of tension is\x01",
            "no time to be joking\x01",
            "around, you know!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FY-You don't have to get\x01",
            "that flustered...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2300")

    Jump("loc_2A7A")

    label("loc_2305")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_24C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2436")

    ChrTalk(
        0x9,
        (
            "It seems Cryptids don't\x01",
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
            "They say they won't appear\x01",
            "in the future, but... In any\x01",
            "case, I'll guard strictly!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_24C3")

    label("loc_2436")


    ChrTalk(
        0x9,
        (
            "It seems Cryptids don't\x01",
            "appear on Tangram Hill.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "They say they won't appear\x01",
            "in the future, but... In any\x01",
            "case, I'll guard strictly!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24C3")

    Jump("loc_2A7A")

    label("loc_24C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2762")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26EC")

    ChrTalk(
        0x9,
        (
            "Restoration of the radar facility\x01",
            "that was destroyed during the trade\x01",
            "conference was completed yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Still, those damn terrorists...\x01",
            "To think they destroyed the\x01",
            "facility without us noticing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Thinking about it\x01",
            "carefully, it's really a\x01",
            "mystery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F(...Given the armored car that\x01",
            "appeared underground, they were too\x01",
            "prepared to be just some terrorists.)\x02\x03",
            "#00003F(As we thought, they might have had\x01",
            "Ouroboros' backing.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F(Well, we have no proof.\x01",
            "I think it's highly\x01",
            "likely, though.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_275D")

    label("loc_26EC")


    ChrTalk(
        0x9,
        (
            "Hmm. Questions still\x01",
            "remain regarding those\x01",
            "terrorists, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Anyhow, we'll tighten\x01",
            "our security now!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_275D")

    Jump("loc_2A7A")

    label("loc_2762")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2887")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2803")

    ChrTalk(
        0x9,
        (
            "Nothing out of the\x01",
            "ordinary at present!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Damn terrorists... Now that we\x01",
            "have intel, we'll intercept\x01",
            "them with all our might.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2882")

    label("loc_2803")


    ChrTalk(
        0x9,
        (
            "We CGF will protect the\x01",
            "heads of state without\x01",
            "fail!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...In any case, there's\x01",
            "nothing out of the\x01",
            "ordinary at present!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2882")

    Jump("loc_2A7A")

    label("loc_2887")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2976")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2936")

    ChrTalk(
        0x9,
        (
            "As for President Rocksmith's\x01",
            "security detail, there's\x01",
            "nothing out of the ordinary!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We'll continue our trade\x01",
            "conference security\x01",
            "posture!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2971")

    label("loc_2936")


    ChrTalk(
        0x9,
        (
            "We'll continue our trade\x01",
            "conference security\x01",
            "posture!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2971")

    Jump("loc_2A7A")

    label("loc_2976")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2A7A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2A1A")

    ChrTalk(
        0x9,
        (
            "The training we did some\x01",
            "time ago was a terrific\x01",
            "experience!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I absolutely want to\x01",
            "make use of it in future\x01",
            "security operations!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A7A")

    label("loc_2A1A")


    ChrTalk(
        0x9,
        (
            "Nothing out of the\x01",
            "ordinary!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The security system for\x01",
            "the trade conference is\x01",
            "perfect!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A7A")

    TalkEnd(0xFE)
    Return()

    # Function_10_1C41 end

    def Function_11_2A7E(): pass

    label("Function_11_2A7E")

    Call(0, 12)
    Return()

    # Function_11_2A7E end

    def Function_12_2A82(): pass

    label("Function_12_2A82")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2AAB")
    Call(0, 27)
    Return()

    label("loc_2AAB")

    TalkBegin(0xA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2AB8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36BA")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",        # 0
            "Shop\x01",        # 1
            "Cancel\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B0A")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2B0A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B2A")
    OP_AF(0x6E)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_36B5")

    label("loc_2B2A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B3E")
    Jump("loc_36B5")

    label("loc_2B3E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B56")
    TalkEnd(0xA)
    Return()

    label("loc_2B56")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36B5")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_2C18")

    ChrTalk(
        0xA,
        (
            "Because the hot pot is\x01",
            "simple and tasty, we have it\x01",
            "often here at Tangram Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's really lively and\x01",
            "fun when everyone\x01",
            "gathers around the pot.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36B5")

    label("loc_2C18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2D8A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CFE")

    ChrTalk(
        0xA,
        (
            "Although the times are\x01",
            "what they are... Want to\x01",
            "eat something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If you're feeling anxious\x01",
            "and irritated, I'm sure\x01",
            "it's because you're hungry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "After you eat a lot,\x01",
            "your mind will calm\x01",
            "down.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2D85")

    label("loc_2CFE")


    ChrTalk(
        0xA,
        (
            "If you're feeling anxious\x01",
            "and irritated, I'm sure\x01",
            "it's because you're hungry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "After you eat a lot,\x01",
            "your mind will calm\x01",
            "down.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D85")

    Jump("loc_36B5")

    label("loc_2D8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2F3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E93")

    ChrTalk(
        0xA,
        (
            "The damage to the CGF... It was\x01",
            "an event Mr. Lag and I, who\x01",
            "aren't members, had to endure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "They were taken out before\x01",
            "doing anything, so they\x01",
            "must've been mortified.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I hope the remaining\x01",
            "members get well again,\x01",
            "at least...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2F36")

    label("loc_2E93")


    ChrTalk(
        0xA,
        (
            "The sacrificed members... They were\x01",
            "taken out before doing anything, so\x01",
            "they must've mortified.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I hope the remaining\x01",
            "members get well again,\x01",
            "at least...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F36")

    Jump("loc_36B5")

    label("loc_2F3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2FDD")

    ChrTalk(
        0xA,
        (
            "Yesterday, many visitors\x01",
            "were sent here on connecting\x01",
            "buses from the train.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Most of them have\x01",
            "already gone home, but\x01",
            "it was really tough.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36B5")

    label("loc_2FDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_30AC")

    ChrTalk(
        0xA,
        (
            "With these continuing tensions,\x01",
            "there's few things a humble\x01",
            "cook like me can do, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I have to at least prepare\x01",
            "delicious dishes so all members can\x01",
            "display their strength at 100%.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36B5")

    label("loc_30AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_326D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31B6")

    ChrTalk(
        0xA,
        (
            "An independence proposal,\x01",
            "eh...? Crossbell might've\x01",
            "got itself into big trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I can't think the Empire and\x01",
            "Republic will let it pass\x01",
            "without objection, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Personally, I want the\x01",
            "mayor and the others to\x01",
            "do their best.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3268")

    label("loc_31B6")


    ChrTalk(
        0xA,
        (
            "I can't think the Empire and Republic\x01",
            "will let something like independence\x01",
            "pass without objection, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Personally, I want the\x01",
            "mayor and the others to\x01",
            "do their best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3268")

    Jump("loc_36B5")

    label("loc_326D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3316")

    ChrTalk(
        0xA,
        (
            "Due to the counter-terrorism\x01",
            "measures, all the CGF guys\x01",
            "seem pretty fired up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "They eat plenty here so\x01",
            "they can do their best\x01",
            "for the entire day.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36B5")

    label("loc_3316")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3539")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_346A")

    ChrTalk(
        0xA,
        (
            "Calvard is known for being a\x01",
            "country that has accepted many\x01",
            "different cultures for a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The Eastern culture is one of them, and\x01",
            "it's thought to have had a great influence\x01",
            "on the world of cooking as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Eastern cuisine is superb.\x01",
            "Even as a cook, there are a\x01",
            "lot of things I have to learn.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3534")

    label("loc_346A")


    ChrTalk(
        0xA,
        (
            "Eastern culture in the Republic is\x01",
            "thought to have had a heavy influence\x01",
            "on the world of cooking as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Eastern cuisine is superb.\x01",
            "Even as a cook, there are a\x01",
            "lot of things I have to learn.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3534")

    Jump("loc_36B5")

    label("loc_3539")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_36B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_362E")

    ChrTalk(
        0xA,
        (
            "The new vice commander\x01",
            "is quite the funny\x01",
            "fellow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "He's cool in a different way than\x01",
            "Commander Sonya and a reliable\x01",
            "man who steadily leads everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "So there's still an\x01",
            "excellent man left in\x01",
            "the CGF, eh?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_36B5")

    label("loc_362E")


    ChrTalk(
        0xA,
        (
            "The new vice commander\x01",
            "is a reliable man who\x01",
            "steadily leads everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "So there's still an\x01",
            "excellent man left in\x01",
            "the CGF, eh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36B5")

    Jump("loc_2AB8")

    label("loc_36BA")

    TalkEnd(0xA)
    Return()

    # Function_12_2A82 end

    def Function_13_36BE(): pass

    label("Function_13_36BE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_38AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3801")

    NpcTalk(
        0xB,
        "Soldier Alexei",
        (
            "*sigh*... I've lost my\x01",
            "appetite for some\x01",
            "reason.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "Soldier Alexei",
        (
            "...No, in a times like\x01",
            "these that I must eat, even\x01",
            "if I have to force myself.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "Soldier Alexei",
        (
            "To defend Crossbell in case of Imperial\x01",
            "or Republican invasion... ...It's also\x01",
            "to carry out that mission.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_38A7")

    label("loc_3801")


    NpcTalk(
        0xB,
        "Soldier Alexei",
        (
            "Too many things have\x01",
            "happened... It's like my\x01",
            "head is in confusion.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xB,
        "Soldier Alexei",
        (
            "Defending Crossbell.\x01",
            "...I have to carry out\x01",
            "that mission.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38A7")

    Jump("loc_413D")

    label("loc_38AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_396A")

    ChrTalk(
        0xB,
        (
            "The people who attacked\x01",
            "the city are now hiding\x01",
            "somewhere, huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "...Hmph, that's perfect.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "To avenge our comrades\x01",
            "too... One day, we'll\x01",
            "smoke them out for sure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_413D")

    label("loc_396A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3A1C")

    ChrTalk(
        0xB,
        (
            "*sigh*... A meal after\x01",
            "manual labor has a truly\x01",
            "supreme taste.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I don't what's going to happen\x01",
            "next... I have to constantly\x01",
            "fortify myself through eating.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_413D")

    label("loc_3A1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3C10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B33")

    ChrTalk(
        0xB,
        (
            "After Crossbell becomes independent,\x01",
            "if the CGF's activities become\x01",
            "recognised as those of an army...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I wouldn't want just an\x01",
            "improvement in armaments,\x01",
            "but also in rations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "After all, I can only\x01",
            "describe the ones we\x01",
            "have now as awful...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3C0B")

    label("loc_3B33")


    ChrTalk(
        0xB,
        (
            "...I hear the meals\x01",
            "served in the Empire\x01",
            "taste pretty bad too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If we break away from the Empire and become\x01",
            "independent, I'm sure that even the rations would\x01",
            "be improved. ...I guess that's my ideal fantasy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C0B")

    Jump("loc_413D")

    label("loc_3C10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3CD1")

    ChrTalk(
        0xB,
        (
            "Cryptids... According to the\x01",
            "reports I heard, they're\x01",
            "pretty tough opponents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We CGF need to concentrate on\x01",
            "guarding the border... We're\x01",
            "leaving the rest to all of you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_413D")

    label("loc_3CD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3DD9")

    ChrTalk(
        0xB,
        (
            "They say terrorists might appear, but... In\x01",
            "practice, what's important is the methods\x01",
            "they would use to try to infiltrate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It's possible they have accomplices who\x01",
            "snuck in already as well. I can't let\x01",
            "my guard down today even for a moment.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_413D")

    label("loc_3DD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3F65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3ED8")

    ChrTalk(
        0xB,
        (
            "*sigh*, I wanted to go\x01",
            "do security at Michelam\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I've only been there once and\x01",
            "the food they served in that\x01",
            "restaurant was pretty good...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "...Michelam is closed so\x01",
            "they won't be running\x01",
            "the restaurant, I guess.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3F60")

    label("loc_3ED8")


    ChrTalk(
        0xB,
        (
            "...Michelam is closed so\x01",
            "they won't be running\x01",
            "the restaurant, I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "...*munch munch*. In any\x01",
            "case, I'll eat my meal\x01",
            "fast.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F60")

    Jump("loc_413D")

    label("loc_3F65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_413D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_40C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_403E")

    ChrTalk(
        0xB,
        (
            "*chomp chomp munch\x01",
            "munch"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "As expected, meals after\x01",
            "training are\x01",
            "exceptional.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I fortified myself with a\x01",
            "meal before training, but I\x01",
            "just can't stop eating this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_40C4")

    label("loc_403E")


    ChrTalk(
        0xB,
        (
            "Even if it's an awful\x01",
            "ration, it tastes\x01",
            "delicious after training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I think that meals after\x01",
            "training are really\x01",
            "exceptional.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40C4")

    Jump("loc_413D")

    label("loc_40C9")


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
            "They say we'll be\x01",
            "training today, so I have\x01",
            "to have a good meal.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_413D")

    TalkEnd(0xFE)
    Return()

    # Function_13_36BE end

    def Function_14_4141(): pass

    label("Function_14_4141")

    Call(0, 15)
    Return()

    # Function_14_4141 end

    def Function_15_4145(): pass

    label("Function_15_4145")

    TalkBegin(0xC)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4152")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DCA")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",        # 0
            "Rest\x01",        # 1
            "Cancel\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_41A4")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_41A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41C4")
    OP_AF(0x6F)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4DC5")

    label("loc_41C4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41D8")
    Jump("loc_4DC5")

    label("loc_41D8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_41F0")
    TalkEnd(0xC)
    Return()

    label("loc_41F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DC5")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_438C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42F1")

    ChrTalk(
        0xC,
        (
            "I heard a rumor that\x01",
            "Ilya regained\x01",
            "consciousness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Things are going to get\x01",
            "gradually worse for Crossbell\x01",
            "from now on, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "As long as we have the\x01",
            "light called Ilya, I'm\x01",
            "sure we'll be fine.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4387")

    label("loc_42F1")


    ChrTalk(
        0xC,
        (
            "Things are going to get\x01",
            "gradually worse for Crossbell\x01",
            "from now on, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "As long as we have the\x01",
            "light called Ilya, I'm\x01",
            "sure we'll be fine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4387")

    Jump("loc_4DC5")

    label("loc_438C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4535")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4493")

    ChrTalk(
        0xC,
        (
            "To many people living in\x01",
            "Crossbell, Ilya Platiｲre is\x01",
            "an existence like the sun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "To think a woman like\x01",
            "her was seriously\x01",
            "injured...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...No, I've got to concentrate\x01",
            "on my job. I wonder if she'll\x01",
            "be able to make comeback...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4530")

    label("loc_4493")


    ChrTalk(
        0xC,
        (
            "According to rumors,\x01",
            "Ilya Platiｲre is still\x01",
            "in a coma...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...No, I've got to concentrate\x01",
            "on my job. I wonder if she'll\x01",
            "be able to make comeback...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4530")

    Jump("loc_4DC5")

    label("loc_4535")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4728")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4676")

    ChrTalk(
        0xC,
        (
            "At last, the Arc-en-Ciel\x01",
            "renewal performance is\x01",
            "going to open tomorrow...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "As expected, the highlight is going\x01",
            "promising newcomer Sully, who plays\x01",
            "the role of Star Princess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "In the end, I couldn't get tickets,\x01",
            "but Crossbell Times will probably\x01",
            "do a feature on it. I can't wait...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4723")

    label("loc_4676")


    ChrTalk(
        0xC,
        (
            "At last, the Arc-en-Ciel\x01",
            "renewal performance is\x01",
            "going to open tomorrow...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "What kind of event will it\x01",
            "be...? I can't wait for it to\x01",
            "be featured in Crossbell Times.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4723")

    Jump("loc_4DC5")

    label("loc_4728")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_47C6")

    ChrTalk(
        0xC,
        (
            "It's been boring lately\x01",
            "for some reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Seems it'll rain again tomorrow.\x01",
            "Maybe I should read an Arc-en-\x01",
            "Ciel fanbook or something...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DC5")

    label("loc_47C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_499F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48F5")

    ChrTalk(
        0xC,
        (
            "Due to the state of tension\x01",
            "with the major powers, the\x01",
            "CGF members look quite busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "In this situation, it appears the\x01",
            "Support Section and guild have\x01",
            "undertaken jobs for the CGF...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "We should try to complement\x01",
            "each other's strengths going\x01",
            "forward however we can.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_499A")

    label("loc_48F5")


    ChrTalk(
        0xC,
        (
            "It appears the Support\x01",
            "Section and guild have\x01",
            "undertaken CGF jobs, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "We should try to complement\x01",
            "each other's strengths going\x01",
            "forward however we can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_499A")

    Jump("loc_4DC5")

    label("loc_499F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4BC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AF8")

    ChrTalk(
        0xC,
        (
            "The danger of terrorism is in\x01",
            "the fact that they firmly\x01",
            "believe that they are "right".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Being willing to sacrifice themselves for\x01",
            "their cause... They don't see that as a bad\x01",
            "thing. To put it bluntly, they can go to hell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "To prevent something like\x01",
            "that from happening, the CGF\x01",
            "guys want to do their best.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4BBE")

    label("loc_4AF8")


    ChrTalk(
        0xC,
        (
            "Being willing to sacrifice themselves\x01",
            "for their cause... That blasted idea\x01",
            "is at the heart of terrorism.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "To prevent something like\x01",
            "that from happening, the CGF\x01",
            "guys want to do their best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BBE")

    Jump("loc_4DC5")

    label("loc_4BC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4C7E")

    ChrTalk(
        0xC,
        (
            "I heard the heads of state who\x01",
            "came to Crossbell are going to see\x01",
            "the Arc-en-Ciel play tonight...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It's a "state guest\x01",
            "privilege", I guess. I\x01",
            "honestly envy them...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DC5")

    label("loc_4C7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4DC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D34")

    ChrTalk(
        0xC,
        (
            "The Arc-en-Ciel\x01",
            "performance is drawing\x01",
            "near...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The tickets seem to be\x01",
            "selling at a crazy\x01",
            "speed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I guess I'll have to\x01",
            "resign myself again...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4DC5")

    label("loc_4D34")


    ChrTalk(
        0xC,
        (
            "I'm a big fan of Ilya\x01",
            "Platiｲre...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I really wanted to go see the\x01",
            "performance this time, but I guess\x01",
            "I'll have to give up on it again...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DC5")

    Jump("loc_4152")

    label("loc_4DCA")

    TalkEnd(0xC)
    Return()

    # Function_15_4145 end

    def Function_16_4DCE(): pass

    label("Function_16_4DCE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4E98")

    ChrTalk(
        0xD,
        (
            "I can't believe an\x01",
            "attack happened at my\x01",
            "travel destination...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Hmph, who the heck are these CGF that\x01",
            "can't even protect a city? I don't\x01",
            "want to stay in such a dangerous land.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FF3")

    label("loc_4E98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4EA6")
    Jump("loc_4FF3")

    label("loc_4EA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4EB7")
    Call(0, 8)
    Jump("loc_4FF3")

    label("loc_4EB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4EC5")
    Jump("loc_4FF3")

    label("loc_4EC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4F6A")

    ChrTalk(
        0xD,
        (
            "I wonder how today's\x01",
            "conference will turn\x01",
            "out...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "When I return to the Republic,\x01",
            "I guess I'll try to order the\x01",
            "next issue of Crossbell Times.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FF3")

    label("loc_4F6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4F78")
    Jump("loc_4FF3")

    label("loc_4F78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4FF3")

    ChrTalk(
        0xD,
        (
            "I'm tired from driving\x01",
            "through Tangram Hill.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Let's see, I think I'll\x01",
            "go eat something at the\x01",
            "mess hall.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FF3")

    TalkEnd(0xFE)
    Return()

    # Function_16_4DCE end

    def Function_17_4FF7(): pass

    label("Function_17_4FF7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5090")

    ChrTalk(
        0xE,
        (
            "Ooh. Even though the barrier's\x01",
            "down, to think I still can't\x01",
            "return to the Republic...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I've got at least\x01",
            "protect this child...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5456")

    label("loc_5090")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_51A2")

    ChrTalk(
        0xE,
        (
            "I sympathize with people of Crossbell,\x01",
            "but... If they had had a proper army,\x01",
            "damage would've been kept to a minimum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "As I feared, maybe they should've accepted\x01",
            "President Rocksmith and the Blood and Iron\x01",
            "Chancellor's proposal at the trade conference.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5456")

    label("loc_51A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_527D")

    ChrTalk(
        0xE,
        (
            "It seems a colleague of mine who went\x01",
            "on a business trip to the Republic\x01",
            "was caught up in the train accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I'm now heading to the hospital\x01",
            "where he's recovering...\x01",
            "Anyway, I'm glad he's safe.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5456")

    label("loc_527D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_528B")
    Jump("loc_5456")

    label("loc_528B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_535F")

    ChrTalk(
        0xE,
        (
            "I feel that, in a certain sense, it's\x01",
            "inevitable for the citizens of\x01",
            "Crossbell to think about independence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Unless it negatively impacts\x01",
            "my business, I guess I'll\x01",
            "remain an idle onlooker.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5456")

    label("loc_535F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5370")
    Call(0, 9)
    Jump("loc_5456")

    label("loc_5370")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_537E")
    Jump("loc_5456")

    label("loc_537E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5456")

    ChrTalk(
        0xE,
        (
            "I own a private general\x01",
            "store. I came to\x01",
            "Crossbell to stock up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "You really can find all sorts of things in\x01",
            "Crossbell. After all, it's located at the\x01",
            "crossroads of Zemuria. Haha, I can hardly wait.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5456")

    TalkEnd(0xFE)
    Return()

    # Function_17_4FF7 end

    def Function_18_545A(): pass

    label("Function_18_545A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_54C7")

    ChrTalk(
        0xF,
        (
            "Oh, father... Getting\x01",
            "all excited...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "Ohoho, I'm sorry.\x01",
            "Please, don't be\x01",
            "offended.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_567F")

    label("loc_54C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_54D5")
    Jump("loc_567F")

    label("loc_54D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_54E3")
    Jump("loc_567F")

    label("loc_54E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_558E")

    ChrTalk(
        0xF,
        (
            "They say mysterious large\x01",
            "monsters are have been appearing\x01",
            "in Crossbell recently?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "No way, how scary...\x01",
            "Maybe I chose my travel\x01",
            "timing all wrong...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_567F")

    label("loc_558E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_559C")
    Jump("loc_567F")

    label("loc_559C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5676")

    ChrTalk(
        0xF,
        (
            "I was interested in that Orchis\x01",
            "Tower or whatever and so I came to\x01",
            "see it, against my better judgment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "I already saw it at the unveiling\x01",
            "ceremony, so I think it's time\x01",
            "for me to head back home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_567F")

    label("loc_5676")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_567F")

    label("loc_567F")

    TalkEnd(0xFE)
    Return()

    # Function_18_545A end

    def Function_19_5683(): pass

    label("Function_19_5683")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5694")
    Jump("loc_5851")

    label("loc_5694")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_56C7")

    ChrTalk(
        0x10,
        (
            "*sigh*, isn't the bus\x01",
            "here yet?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5851")

    label("loc_56C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5774")

    ChrTalk(
        0x10,
        (
            "By the way, they say a fake\x01",
            "brand trader lady was arrested\x01",
            "in Altair City yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Man, she was so sharp\x01",
            "yet so underhanded. In a\x01",
            "way, I pity her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5851")

    label("loc_5774")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5782")
    Jump("loc_5851")

    label("loc_5782")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5790")
    Jump("loc_5851")

    label("loc_5790")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5848")

    ChrTalk(
        0x10,
        (
            "Because of traffic regulations,\x01",
            "it was impossible to pass through\x01",
            "Tangram Hill this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Well, the President was\x01",
            "visiting, so it couldn't\x01",
            "have been helped.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5851")

    label("loc_5848")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5851")

    label("loc_5851")

    TalkEnd(0xFE)
    Return()

    # Function_19_5683 end

    def Function_20_5855(): pass

    label("Function_20_5855")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_58C8")

    ChrTalk(
        0x11,
        (
            "Ah, enough! Why did\x01",
            "something like that have\x01",
            "to happen!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Who's to blame for this,\x01",
            "huh!?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A39")

    label("loc_58C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_58D6")
    Jump("loc_5A39")

    label("loc_58D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_58E4")
    Jump("loc_5A39")

    label("loc_58E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_58F2")
    Jump("loc_5A39")

    label("loc_58F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_59AC")

    ChrTalk(
        0x11,
        (
            "The members at the gate\x01",
            "are scary for some\x01",
            "reason...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "I don't care if there's a state of\x01",
            "tension or whatever... Would it kill\x01",
            "them to be just a little more civil?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A39")

    label("loc_59AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_59BA")
    Jump("loc_5A39")

    label("loc_59BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_59C8")
    Jump("loc_5A39")

    label("loc_59C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5A39")

    ChrTalk(
        0x11,
        (
            "Umm, where did the bus\x01",
            "to Crossbell City depart\x01",
            "from again...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "Transfers are really a\x01",
            "bother.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A39")

    TalkEnd(0xFE)
    Return()

    # Function_20_5855 end

    def Function_21_5A3D(): pass

    label("Function_21_5A3D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5A74")

    ChrTalk(
        0x12,
        (
            "Papaaa... I want to go\x01",
            "hooome...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B0C")

    label("loc_5A74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5A82")
    Jump("loc_5B0C")

    label("loc_5A82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5A90")
    Jump("loc_5B0C")

    label("loc_5A90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5A9E")
    Jump("loc_5B0C")

    label("loc_5A9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5AAC")
    Jump("loc_5B0C")

    label("loc_5AAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5AF5")

    ChrTalk(
        0x12,
        (
            "Grampa, enough with the\x01",
            "complicated stuff, let's\x01",
            "eat!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B0C")

    label("loc_5AF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5B03")
    Jump("loc_5B0C")

    label("loc_5B03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5B0C")

    label("loc_5B0C")

    TalkEnd(0xFE)
    Return()

    # Function_21_5A3D end

    def Function_22_5B10(): pass

    label("Function_22_5B10")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B25")
    Call(0, 23)
    Jump("loc_5BAC")

    label("loc_5B25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B37")
    Call(0, 24)
    Jump("loc_5BAC")

    label("loc_5B37")


    ChrTalk(
        0xFE,
        (
            "We've got to focus on\x01",
            "work for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You've got your own work\x01",
            "to do too, so leave this\x01",
            "investigation to us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BAC")

    TalkEnd(0xFE)
    Return()

    # Function_22_5B10 end

    def Function_23_5BB0(): pass

    label("Function_23_5BB0")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x13, 0x10)
    TurnDirection(0x13, 0x0, 0)
    OP_52(0x13, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5C41")
    Jump("loc_5C8B")

    label("loc_5C41")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5C61")
    OP_52(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5C8B")

    label("loc_5C61")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5C81")
    OP_52(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5C8B")

    label("loc_5C81")

    OP_52(0x13, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x13, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5C8B")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5D41")
    Jump("loc_5D8B")

    label("loc_5D41")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5D61")
    OP_52(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5D8B")

    label("loc_5D61")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5D81")
    OP_52(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5D8B")

    label("loc_5D81")

    OP_52(0x14, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5D8B")

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
            "#00000FScott and Wenzel... You're\x01",
            "here at the border.\x02\x03",
            "Could you be headed to the\x01",
            "Republic? Or maybe there's\x01",
            "a Cryptid at Tangram Hill?\x02",
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
            "Even if one did appear at\x01",
            "Tangram Hill, that would be\x01",
            "within CGF jurisdiction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FYou're certainly right\x01",
            "about that. ...Umm,\x01",
            "then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "We investigated the East\x01",
            "Crossbell Highway area, where you\x01",
            "defeated the Cryptid yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "If the "Pleroma Grass" or whatever really is\x01",
            "connected to Cryptid appearances, we wanted\x01",
            "to see if there was any more blooming there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FI see... It does seem\x01",
            "necessary to check on\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FSince you guys are bracers,\x01",
            "you're able to investigate places\x01",
            "we can't like wilderness areas.\x02",
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

    # Function_23_5BB0 end

    def Function_24_610E(): pass

    label("Function_24_610E")

    SetChrFlags(0x13, 0x10)
    SetChrFlags(0x14, 0x10)
    SetChrSubChip(0x13, 0x0)
    SetChrSubChip(0x14, 0x0)

    ChrTalk(
        0x13,
        (
            "Even so... We're busy as\x01",
            "ever following the trade\x01",
            "conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "I haven't seen my\x01",
            "fiancｳe Pearl that much\x01",
            "either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "The girl working at the\x01",
            "department store, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Well...There's nothing we\x01",
            "can do about it now. We're\x01",
            "short staffed, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "You should ask Michel for a vacation\x01",
            "once this case is over. I'll help\x01",
            "adjust our schedules, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Haha, thanks Wenzel.\x01",
            "You're always such a big\x01",
            "help.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x13, 0x10)
    ClearChrFlags(0x14, 0x10)
    SetScenarioFlags(0x1, 2)
    SetScenarioFlags(0x1, 3)
    Return()

    # Function_24_610E end

    def Function_25_62D2(): pass

    label("Function_25_62D2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62E7")
    Call(0, 23)
    Jump("loc_63B3")

    label("loc_62E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62F9")
    Call(0, 24)
    Jump("loc_63B3")

    label("loc_62F9")


    ChrTalk(
        0xFE,
        (
            "We received and confirmed your report. A\x01",
            "small amount of "Pleroma Grass" was blooming\x01",
            "at the other Cryptid sites as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What a mysterious plant.\x01",
            "We'd best be very\x01",
            "careful...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63B3")

    TalkEnd(0xFE)
    Return()

    # Function_25_62D2 end

    def Function_26_63B7(): pass

    label("Function_26_63B7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6464")

    ChrTalk(
        0xFE,
        (
            "At the time of the\x01",
            "attack, I was in\x01",
            "Armorica Village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I contacted them,\x01",
            "Ryｹ and father said they\x01",
            "were ok...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...I'm really relieved.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_64BE")

    label("loc_6464")


    ChrTalk(
        0xFE,
        (
            "I guess I'll go back home in\x01",
            "a little while. I'm worried\x01",
            "about Ryｹ and father, so...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_64BE")

    TalkEnd(0xFE)
    Return()

    # Function_26_63B7 end

    def Function_27_64C2(): pass

    label("Function_27_64C2")

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
            "Hi, Sergeant Major Noｱl.\x01",
            "Are you with everyone\x01",
            "from the SSS?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FThank you for your hard\x01",
            "work, Temas.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FUhhm, today we came for\x01",
            "work...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 500)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Explained that you came\x01",
            "for "gourmet\x01",
            "recommendations" coverage.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        (
            "Ah, indeed, I think I\x01",
            "was asked that by\x01",
            "Crossbell News.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "I just finished making my "Rich\x01",
            "Sea Hot Pot", a Tangram specialty.\x01",
            "You can eat it with everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FOh, so a sea hotpot is\x01",
            "the main dish at this\x01",
            "mess hall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FHaha, if you please.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "One moment please, then.\x01",
            "I'll serve your portions\x01",
            "now.\x02",
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
            "Lloyd and the others ate\x01",
            "the Rich Sea Hot Pot.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x103,
        (
            "#00200F*chomp, chomp*... The\x01",
            "taste is quite good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, it seems the\x01",
            "original taste of the\x01",
            "fish comes out nicely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Haha. I know, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Because the hot pot is\x01",
            "simple and tasty, we have it\x01",
            "often here at Tangram Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's really lively and\x01",
            "fun when everyone\x01",
            "gathers around the pot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F...Come to think of it, I\x01",
            "never ate a hot pot like\x01",
            "this with the Testaments.\x02\x03",
            "#10302FHehe. If I have the\x01",
            "chance, maybe I'll come\x01",
            "here for it with them.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_69EB():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_69EB)
    Sleep(50)

    def lambda_69FB():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_69FB)
    Sleep(50)

    def lambda_6A0B():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6A0B)
    Sleep(50)

    def lambda_6A1B():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6A1B)
    Sleep(50)

    def lambda_6A2B():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6A2B)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00305FWow... That's not the\x01",
            "kind of thing I hear\x01",
            "outta you very often.\x02",
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
            "#00200FThen, maybe we should\x01",
            "leave this place's\x01",
            "introduction to Wazy.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x105, 0x0, 0x1F4)

    ChrTalk(
        0x105,
        (
            "#10304FOh man. It's a pain, but\x01",
            "I think I'll take you up\x01",
            "on that.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1, 1)
    SetScenarioFlags(0x173, 3)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_6B98")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6B98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_6BB5")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6BB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_6BC8")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6BC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_6BDB")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6BDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_6BF8")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6BF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_6C0B")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6C0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_6C28")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6C28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_6C3B")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6C3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_6C58")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6C58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_6C6B")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6C6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_6C88")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6C88")

    OP_29(0x80, 0x1, 0xC)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6D93")
    SetChrName("")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Finished covering 6\x01",
            "restaurants!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6D8A")

    AnonymousTalk(
        0x101,
        (
            "#00003FIt seems we could go report to\x01",
            "Grace immediately, but...\x02\x03",
            "#00000FWe haven't found all 6\x01",
            "members' favorites yet, so why\x01",
            "don't we try a little harder?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_6D8A")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_6D93")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6E81")
    SetChrName("")
    Sound(9, 0, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Found all SSS members'\x01",
            "favorites!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00000FWith this, we found all 6\x01",
            "members' favorites.\x02\x03",
            "We've got plenty of coverage with\x01",
            "this. Let's head to the news\x01",
            "agency right away and report.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x179, 0)
    OP_29(0x80, 0x1, 0xE)

    label("loc_6E81")

    OP_4C(0xA, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 104640, 0, 1980, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_27_64C2 end

    def Function_28_6EB1(): pass

    label("Function_28_6EB1")

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
            "R-Report! Report to Vice\x01",
            "Commander Douglas!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 2)
    NewScene("e4101", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_28_6EB1 end

    def Function_29_7072(): pass

    label("Function_29_7072")

    SetChrPos(0xFE, -3500, 0, 0, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -2000, 0, 0)
    OP_9F(0x1, 3500, 0, -4000)
    OP_9F(0x1, 10500, 0, -4000)
    OP_9F(0x1, 25000, 0, -4000)
    OP_9F(0x2, 0xFE, 7000, 0x6)
    Return()

    # Function_29_7072 end

    def Function_30_70C9(): pass

    label("Function_30_70C9")

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

    def lambda_7187():
        OP_95(0x101, -21060, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7187)
    Sleep(30)

    def lambda_71A4():
        OP_95(0x102, -21260, 0, -1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_71A4)
    Sleep(40)

    def lambda_71C1():
        OP_95(0x104, -21260, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_71C1)
    Sleep(800)

    def lambda_71DE():
        OP_95(0x109, -23560, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_71DE)
    Sleep(30)

    def lambda_71FB():
        OP_95(0x103, -23360, 0, -1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_71FB)
    Sleep(10)

    def lambda_7218():
        OP_95(0x105, -23360, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7218)
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
            "R-Report! Report to Vice\x01",
            "Commander Douglas!\x02",
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
        "#00107FAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306FHe got away...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FCrap, the swindled\x01",
            "medical supplies are in\x01",
            "that truck...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FBut... We can't try to\x01",
            "chase him any further.\x02\x03",
            "#00206FIt seems we were one\x01",
            "step behind...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108FIf we had used the orbal\x01",
            "car, we could've chased\x01",
            "after him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306FOh man. Request failed,\x01",
            "then. ...What do we do,\x01",
            "Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F...For now, let's call\x01",
            "Billy and Ricardo.\x02\x03",
            "#00003FI don't like it, but...\x01",
            "we have to report that\x01",
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
            "Lloyd and the others explained the\x01",
            "facts to Billy and Ricardo who\x01",
            "were waiting at the airport...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Afterwards, they went with\x01",
            "Billy to St. Ursula Hospital\x01",
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

    # Function_30_70C9 end

    def Function_31_775E(): pass

    label("Function_31_775E")

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

    # Function_31_775E end

    SaveToFile()

Try(main)
