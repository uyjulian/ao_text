from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c1410.bin",                # FileName
        "c1410",                    # MapName
        "c1410",                    # Location
        0x0030,                     # MapIndex
        "ed7117",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 48, 0, 4, 0, 5],
    )

    BuildStringList((
        "c1410",                  # 0
        "Abbas",               # 1
        "Liang",                 # 2
        "Keen",               # 3
        "Besse",                 # 4
        "Azel",                 # 5
        "Ashley",             # 6
        "Salina",                 # 7
        "Yuggott",               # 8
        "Citizen",                   # 9
        "Citizen",                   # 10
        "Blond hair youth",             # 11
        "Citizen",                   # 12
        "Citizen",                   # 13
        "Luganoff",               # 14
        "Koki",                 # 15
        "Dino",               # 16
    ))

    AddCharChip((
        "apl/ch50375.itc",                   # 00
        "chr/ch06700.itc",                   # 01
        "chr/ch30900.itc",                   # 02
        "chr/ch31800.itc",                   # 03
        "chr/ch20502.itc",                   # 04
        "chr/ch34200.itc",                   # 05
        "chr/ch46500.itc",                   # 06
        "chr/ch20400.itc",                   # 07
        "chr/ch34300.itc",                   # 08
        "chr/ch21300.itc",                   # 09
        "chr/ch22100.itc",                   # 0A
        "chr/ch09202.itc",                   # 0B
        "chr/ch06700.itc",                   # 0C
        "chr/ch20402.itc",                   # 0D
        "chr/ch34302.itc",                   # 0E
        "chr/ch21302.itc",                   # 0F
        "chr/ch22102.itc",                   # 10
        "chr/ch06800.itc",                   # 11
        "chr/ch30800.itc",                   # 12
    ))

    DeclNpc(4294962577, 0,       11880,   180,  261,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(2980,    0,       14779,   180,  261,  0x0, 0,   2,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(3200,    0,       7579,    270,  261,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(16149,   0,       12020,   270,  261,  0x0, 0,   2,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(4294966206, 0,       14909,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(4294966696, 150,     12619,   0,    389,  0x0, 0,   11,  0,   255, 255, 0,   27,  255,  0)
    DeclNpc(3789,    0,       55279,   90,   389,  0x0, 0,   4,   0,   255, 255, 0,   28,  255,  0)
    DeclNpc(4294964886, 29,      52169,   225,  389,  0x0, 0,   5,   0,   0,   0,   0,   29,  255,  0)
    DeclNpc(4294966056, 0,       4139,    0,    389,  0x0, 0,   7,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(4294967126, 0,       4019,    315,  389,  0x0, 0,   8,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   6,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(15479,   0,       12319,   270,  389,  0x0, 0,   9,   0,   0,   0,   0,   25,  255,  0)
    DeclNpc(15300,   0,       10909,   270,  389,  0x0, 0,   10,  0,   0,   0,   0,   26,  255,  0)
    DeclNpc(17079,   1000,    4294964717, 225,  389,  0x0, 0,   18,  0,   0,   0,   0,   30,  255,  0)
    DeclNpc(11420,   0,       7809,    0,    389,  0x0, 0,   18,  0,   0,   0,   0,   31,  255,  0)
    DeclNpc(2920,    0,       6769,    89,   389,  0x0, 0,   17,  0,   0,   0,   0,   32,  255,  0)

    DeclActor(2980,    0,       13420,   1500,    2980,    1500,    14780,   0x007E, 0,  14, 0x0000)
    DeclActor(4294966206, 0,       13420,   1500,    4294966206, 1500,    14780,   0x007E, 0,  17, 0x0000)

    ChipFrameInfo(884, 0)                                        # 0

    ScpFunction((
        "Function_0_374",          # 00, 0
        "Function_1_424",          # 01, 1
        "Function_2_499",          # 02, 2
        "Function_3_572",          # 03, 3
        "Function_4_661",          # 04, 4
        "Function_5_B47",          # 05, 5
        "Function_6_BF9",          # 06, 6
        "Function_7_1BA4",         # 07, 7
        "Function_8_20BA",         # 08, 8
        "Function_9_21FF",         # 09, 9
        "Function_10_23A4",        # 0A, 10
        "Function_11_33FD",        # 0B, 11
        "Function_12_3513",        # 0C, 12
        "Function_13_35F4",        # 0D, 13
        "Function_14_4553",        # 0E, 14
        "Function_15_4572",        # 0F, 15
        "Function_16_4735",        # 10, 16
        "Function_17_5425",        # 11, 17
        "Function_18_5429",        # 12, 18
        "Function_19_6089",        # 13, 19
        "Function_20_61C5",        # 14, 20
        "Function_21_62BF",        # 15, 21
        "Function_22_62C9",        # 16, 22
        "Function_23_641A",        # 17, 23
        "Function_24_6552",        # 18, 24
        "Function_25_66AD",        # 19, 25
        "Function_26_677C",        # 1A, 26
        "Function_27_6863",        # 1B, 27
        "Function_28_68CD",        # 1C, 28
        "Function_29_69E5",        # 1D, 29
        "Function_30_6ABC",        # 1E, 30
        "Function_31_6B8E",        # 1F, 31
        "Function_32_6CB1",        # 20, 32
        "Function_33_6D82",        # 21, 33
        "Function_34_7CD7",        # 22, 34
    ))


    def Function_0_374(): pass

    label("Function_0_374")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_3AC"),
        (1, "loc_3B8"),
        (2, "loc_3C4"),
        (3, "loc_3D0"),
        (4, "loc_3DC"),
        (5, "loc_3E8"),
        (6, "loc_3F4"),
        (SWITCH_DEFAULT, "loc_400"),
    )


    label("loc_3AC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_3B8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_3C4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_3D0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_3DC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_3E8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_3F4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_400")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_40C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_423")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_40C")

    label("loc_423")

    Return()

    # Function_0_374 end

    def Function_1_424(): pass

    label("Function_1_424")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_498")
    OP_95(0xFE, 2970, 30, 4200, 1000, 0x0)
    OP_93(0xFE, 0x5A, 0x12C)
    Sleep(5500)
    OP_95(0xFE, 2950, 30, 6580, 1000, 0x0)
    OP_95(0xFE, 6630, 30, 6580, 1000, 0x0)
    OP_93(0xFE, 0xB4, 0x12C)
    Sleep(8500)
    OP_95(0xFE, 2950, 30, 6580, 1000, 0x0)
    Jump("Function_1_424")

    label("loc_498")

    Return()

    # Function_1_424 end

    def Function_2_499(): pass

    label("Function_2_499")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_571")
    OP_95(0xFE, 8850, 20, 2630, 1000, 0x0)
    OP_95(0xFE, 6340, 20, 2420, 1000, 0x0)
    OP_93(0xFE, 0x0, 0x12C)
    Sleep(5000)
    OP_95(0xFE, 8850, 20, 2630, 1000, 0x0)
    OP_95(0xFE, 10230, 0, 4410, 1000, 0x0)
    OP_93(0xFE, 0x5A, 0x12C)
    Sleep(3200)
    OP_95(0xFE, 8850, 20, 2630, 1000, 0x0)
    OP_95(0xFE, 5070, 20, 2420, 1000, 0x0)
    OP_93(0xFE, 0x13B, 0x12C)
    Sleep(5000)
    OP_95(0xFE, 8850, 20, 2630, 1000, 0x0)
    OP_95(0xFE, 10230, 0, 4410, 1000, 0x0)
    OP_93(0xFE, 0x5A, 0x12C)
    Sleep(3200)
    Jump("Function_2_499")

    label("loc_571")

    Return()

    # Function_2_499 end

    def Function_3_572(): pass

    label("Function_3_572")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_660")
    OP_93(0xFE, 0x0, 0x0)
    OP_95(0xFE, 9900, 30, 10300, 1000, 0x0)
    OP_93(0xFE, 0x5A, 0x12C)
    Sleep(2000)
    OP_93(0xFE, 0x0, 0x0)
    OP_95(0xFE, 9900, 30, 12000, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x12C)
    Sleep(2000)
    OP_93(0xFE, 0x0, 0x0)
    OP_95(0xFE, 9900, 30, 13490, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x12C)
    Sleep(2000)
    OP_93(0xFE, 0xB4, 0x0)
    OP_95(0xFE, 9900, 30, 12000, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x12C)
    Sleep(2000)
    OP_93(0xFE, 0xB4, 0x0)
    OP_95(0xFE, 9900, 30, 10300, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x12C)
    Sleep(2000)
    OP_93(0xFE, 0xB4, 0x0)
    OP_95(0xFE, 9900, 30, 9810, 1000, 0x0)
    OP_93(0xFE, 0x5A, 0x12C)
    Sleep(2000)
    Jump("Function_3_572")

    label("loc_660")

    Return()

    # Function_3_572 end

    def Function_4_661(): pass

    label("Function_4_661")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_679")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_B46")

    label("loc_679")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_729")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x15, -200, 0, 8580, 90)
    SetChrPos(0x17, -1650, 0, 7350, 90)
    SetChrPos(0x16, -1380, 0, 9380, 90)
    SetChrPos(0x9, 2090, 0, 8400, 270)
    SetChrPos(0xB, 3220, 0, 7570, 270)
    SetChrPos(0xA, 4280, 0, 9490, 270)
    BeginChrThread(0xB, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_724")
    SetMapFlags(0x10000000)
    Event(0, 34)

    label("loc_724")

    Jump("loc_B46")

    label("loc_729")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_775")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0xA, 600, 0, 12440, 45)
    SetChrPos(0xB, 4650, 0, 12470, 315)
    SetChrPos(0xC, 2830, 0, 10890, 0)
    BeginChrThread(0xB, 0, 0, 0)
    Jump("loc_B46")

    label("loc_775")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_797")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_B46")

    label("loc_797")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_7F7")
    SetChrPos(0xA, 0, 0, 7400, 90)
    SetChrPos(0xB, 1470, 0, 5650, 0)
    SetChrPos(0x8, 2000, 0, 7720, 225)
    BeginChrThread(0xB, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F2")
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0x8, 0x10)

    label("loc_7F2")

    Jump("loc_B46")

    label("loc_7F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_857")
    SetChrPos(0xA, 0, 0, 7400, 90)
    SetChrPos(0xB, 1470, 0, 5650, 0)
    SetChrPos(0x8, 2000, 0, 7720, 225)
    BeginChrThread(0xB, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_852")
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0x8, 0x10)

    label("loc_852")

    Jump("loc_B46")

    label("loc_857")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_8B3")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x10, -3060, 150, 3640, 0)
    SetChrPos(0x11, -3140, 150, 6740, 180)
    SetChrChipByIndex(0x10, 0xD)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    SetChrChipByIndex(0x11, 0xE)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    Jump("loc_B46")

    label("loc_8B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_90F")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x10, -3060, 150, 3640, 0)
    SetChrPos(0x11, -3140, 150, 6740, 180)
    SetChrChipByIndex(0x10, 0xD)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    SetChrChipByIndex(0x11, 0xE)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    Jump("loc_B46")

    label("loc_90F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_973")
    SetChrPos(0x8, -4080, 0, 12480, 45)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -2730, 150, 12430, 0)
    SetChrChipByIndex(0xD, 0xB)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_95F")
    SetChrFlags(0x8, 0x10)

    label("loc_95F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_96E")
    SetChrFlags(0xD, 0x10)

    label("loc_96E")

    Jump("loc_B46")

    label("loc_973")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_981")
    Jump("loc_B46")

    label("loc_981")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_A67")
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F1")
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 14020, 30, 11650, 270)
    SetChrFlags(0x12, 0x10)
    SetChrPos(0x9, 9900, 30, 9810, 90)
    SetChrFlags(0x9, 0x10)
    BeginChrThread(0x9, 0, 0, 3)
    SetChrPos(0xB, 2980, 0, 14780, 180)
    BeginChrThread(0xB, 0, 0, 0)
    Jump("loc_A44")

    label("loc_9F1")

    SetChrPos(0x13, -3060, 150, 3640, 0)
    SetChrPos(0x14, -3140, 150, 6740, 180)
    SetChrChipByIndex(0x13, 0xF)
    SetChrSubChip(0x13, 0x0)
    EndChrThread(0x13, 0x0)
    SetChrBattleFlags(0x13, 0x4)
    SetChrChipByIndex(0x14, 0x10)
    SetChrSubChip(0x14, 0x0)
    EndChrThread(0x14, 0x0)
    SetChrBattleFlags(0x14, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A44")
    SetChrFlags(0x8, 0x10)

    label("loc_A44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A53")
    SetChrFlags(0x13, 0x10)

    label("loc_A53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A62")
    SetChrFlags(0x14, 0x10)

    label("loc_A62")

    Jump("loc_B46")

    label("loc_A67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_AFD")
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x4)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    SetChrPos(0xE, -2630, 150, 12430, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 15210, 0, 8880, 180)
    SetChrPos(0xB, 15290, 0, 7520, 0)
    BeginChrThread(0xB, 0, 0, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0xA, 0, 0, 7400, 180)
    SetChrFlags(0xA, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AF8")
    SetChrFlags(0x10, 0x10)
    SetChrFlags(0x11, 0x10)

    label("loc_AF8")

    Jump("loc_B46")

    label("loc_AFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_END)), "loc_B0B")
    Jump("loc_B46")

    label("loc_B0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_B2B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x138, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B26")
    SetMapFlags(0x10000000)
    Event(0, 33)

    label("loc_B26")

    Jump("loc_B46")

    label("loc_B2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_B46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x138, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B46")
    SetMapFlags(0x10000000)
    Event(0, 33)

    label("loc_B46")

    Return()

    # Function_4_661 end

    def Function_5_B47(): pass

    label("Function_5_B47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B63")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x232), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B82")

    label("loc_B63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B82")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_B8F")
    OP_65(0x0, 0x1)

    label("loc_B8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BA1")
    OP_65(0x1, 0x1)

    label("loc_BA1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BBA")
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x1)
    Jump("loc_BC0")

    label("loc_BBA")

    OP_10(0x0, 0x1)
    OP_10(0x1, 0x0)

    label("loc_BC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BE1")
    Sound(128, 1, 50, 0)

    label("loc_BE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BF8")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)

    label("loc_BF8")

    Return()

    # Function_5_B47 end

    def Function_6_BF9(): pass

    label("Function_6_BF9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_C0A")
    Jump("loc_1BA0")

    label("loc_C0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_C3C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C25")
    Jump("loc_C37")

    label("loc_C25")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C37")
    Jump("loc_C37")

    label("loc_C37")

    Jump("loc_1BA0")

    label("loc_C3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_CCF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C57")
    Call(0, 7)
    Jump("loc_CCA")

    label("loc_C57")


    ChrTalk(
        0x8,
        (
            "#04100FRegarding Wald's\x01",
            "I will continue to investigate.\x02\x03",
            "As soon as I know something\x01",
            "Please wait as we contact you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CCA")

    Jump("loc_1BA0")

    label("loc_CCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_D25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CEA")
    Call(0, 8)
    Jump("loc_D20")

    label("loc_CEA")


    ChrTalk(
        0x8,
        (
            "#04100FInformation collection on Waldo\x01",
            "Leave it to us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D20")

    Jump("loc_1BA0")

    label("loc_D25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_D85")

    ChrTalk(
        0x8,
        (
            "#04100FApparently,\x01",
            "It seems like a job in a hurry.\x02\x03",
            "If you have something, say it anytime.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BA0")

    label("loc_D85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_105A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FDB")

    ChrTalk(
        0x8,
        (
            "#04100FThe viper guys\x01",
            "It seems that he started looking for Wald.\x02\x03",
            "Apparently for the last couple of days,\x01",
            "She seems to have disappeared, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301FAnything ……\x01",
            "Where and what am I doing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10301F……Abbasたちも\x01",
            "You do not see it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x105, 0)

    ChrTalk(
        0x8,
        (
            "#04100FOh, this week is fresh.\x02\x03",
            "Before that, occasionally\x01",
            "There was something to see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10308FReally……\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x8)

    ChrTalk(
        0x8,
        (
            "#04100F…… Wadi, do not suffer too much.\x02\x03",
            "Despite saying that it disappeared\x01",
            "It's at most a few days.\x02\x03",
            "Besides that, now\x01",
            "The work you have to do is\x01",
            "Is it there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FOh … That's right.\x02\x03",
            "#10302Fありがとう、Abbas。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16E, 6)
    Jump("loc_1055")

    label("loc_FDB")

    TurnDirection(0x8, 0x105, 0)

    ChrTalk(
        0x8,
        (
            "#04100FThings about Waldo\x01",
            "We also care about ourselves.\x02\x03",
            "So, Wadi, I do not worry unnecessarily\x01",
            "You should concentrate on your current job.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1055")

    Jump("loc_1BA0")

    label("loc_105A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1181")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1075")
    Call(0, 9)
    Jump("loc_117C")

    label("loc_1075")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_112C")
    TurnDirection(0x8, 0x105, 0)

    ChrTalk(
        0x8,
        (
            "#04100FWaddai … were you coming.\x02\x03",
            "Hiroshi at the store#2RRelax#Whenever you want it, say it.\x01",
            "I'll prepare my seat right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FGiggle\x01",
            "ありがとう、Abbas。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x2D, 0x0)
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 1)
    Jump("loc_117C")

    label("loc_112C")


    ChrTalk(
        0x8,
        (
            "#04100FHiroshi at the store#2RRelax#Whenever you want it, say it.\x01",
            "I'll prepare my seat right away.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_117C")

    Jump("loc_1BA0")

    label("loc_1181")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_12B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_123C")

    ChrTalk(
        0x8,
        (
            "#04100F…… The recent old city is relatively quiet.\x02\x03",
            "So Wadi,\x01",
            "I do not care about this direction\x01",
            "You should concentrate on the work of the support department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300Fああ……ありがとう、Abbas。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12B1")

    label("loc_123C")


    ChrTalk(
        0x8,
        (
            "#04100F…… The recent old city is relatively quiet.\x02\x03",
            "So Wadi,\x01",
            "I do not care about this direction\x01",
            "You should concentrate on the work of the support department.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12B1")

    Jump("loc_1BA0")

    label("loc_12B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_15D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13AA")

    ChrTalk(
        0x8,
        (
            "#04105FThat guest, well … …\x02\x03",
            "#04102F…… Huh, surely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F(Wow, I laughed … …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305F(Oh, it's surprising … …)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F(Well ……\x01",
            "  フフ、君たちAbbasを\x01",
            "What do you think? )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_13DE")

    label("loc_13AA")


    ChrTalk(
        0x8,
        (
            "#04102FThat guest, well … …\x01",
            "…… Huh, surely.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13DE")

    Jump("loc_15CC")

    label("loc_13E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1586")

    ChrTalk(
        0x8,
        "#04100F…………………….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FAbbas、考え事かい？\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x105, 0)

    ChrTalk(
        0x8,
        (
            "#04100FWas it …?\x02\x03",
            "…… Oh, in the world\x01",
            "I thought that there were various people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309FHaha, indeed.\x02\x03",
            "#10304FBut if you say that\x01",
            "We are also there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#04102FHur …… There is no difference.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(this person……\x01",
            "You talk quite well with Waji. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F(Hehe, that's it.\x01",
            "I guess we are on good terms. )\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 0)
    Jump("loc_15CC")

    label("loc_1586")


    ChrTalk(
        0x8,
        (
            "#04100F…………………….\x02\x03",
            "…… In the world\x01",
            "There are various people.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15CC")

    Jump("loc_1BA0")

    label("loc_15D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_16F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16A1")

    ChrTalk(
        0x8,
        (
            "#04100FHow many cops are also in this old city\x01",
            "It seems they are coming to a circuit.\x02\x03",
            "Was the job of Wadi, support department delayed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FOh, for now\x01",
            "Is there a problem in particular?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#04100FIf so, then.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16F1")

    label("loc_16A1")


    ChrTalk(
        0x8,
        (
            "#04100FPolicemen also in this old city\x01",
            "It seems they are coming to a circuit.\x02\x03",
            "…… It is a hard work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16F1")

    Jump("loc_1BA0")

    label("loc_16F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_END)), "loc_1870")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_182C")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x105, 0)

    ChrTalk(
        0x8,
        (
            "#04100FWadi, are you all right?\x01",
            "It looks a little pale.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FOh, it's okay.\x01",
            "Do not worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#04100FI see, I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F(These two people … ….\x01",
            "You are strangely assassinating. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F(Yes, but it's strange\x01",
            "They are communicating. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_186B")

    label("loc_182C")

    TurnDirection(0x8, 0x105, 0)

    ChrTalk(
        0x8,
        (
            "#04100FWadi, our help is\x01",
            "Whenever you need it, say it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_186B")

    Jump("loc_1BA0")

    label("loc_1870")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_196C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_191B")

    ChrTalk(
        0x8,
        (
            "#04100FEven here if ordered\x01",
            "Accepting.\x02\x03",
            "Please do not hesitate to ask at any time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(Feel free to contact with this person, … ….\x01",
            "What a casual thing it is difficult. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1967")

    label("loc_191B")


    ChrTalk(
        0x8,
        (
            "#04100FEven here if ordered\x01",
            "Accepting.\x02\x03",
            "Please do not hesitate to ask at any time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1967")

    Jump("loc_1BA0")

    label("loc_196C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1BA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B37")

    ChrTalk(
        0x8,
        (
            "#04100FWaji, what about testing\x01",
            "Leave it all here.\x02\x03",
            "You are\x01",
            "Do as you want to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FOh, I will let you.\x02\x03",
            "#10304FFrom now on Trinity\x01",
            "Sometimes I think I will have a face,\x01",
            "I hope you do your best to manage the store.\x02\x03",
            "#10302FHuff, if you get crushed\x01",
            "Cozy places will decrease.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#04102FWell, I knew.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F(These two people have a strange relationship … …)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FWhat kind of past is there?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BA0")

    label("loc_1B37")


    ChrTalk(
        0x8,
        (
            "#04100FWaji, what about testing\x01",
            "Leave it all here.\x02\x03",
            "You are\x01",
            "Do as you want to do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BA0")

    TalkEnd(0xFE)
    Return()

    # Function_6_BF9 end

    def Function_7_1BA4(): pass

    label("Function_7_1BA4")

    OP_4B(0x8, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EBD")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x105, 0)
    Sleep(1000)
    TurnDirection(0xB, 0x105, 0)
    TurnDirection(0xA, 0x105, 0)

    ChrTalk(
        0x8,
        (
            "#04100FWadi\x01",
            "Apparently to various things tough\x01",
            "It seems to be getting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "実は今朝、俺とBesseの２人で\x01",
            "I saw him with that redhead … …\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CF9")
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#10108FAs expected after all …\x01",
            "I was in the old city.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CF9")


    ChrTalk(
        0xB,
        (
            "Something ……\x01",
            "It looked like I thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I saw it near the exchange shop\x01",
            "If I do think soon\x01",
            "I went away to the city, but … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Is there something happening …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FOh, hey.\x02\x03",
            "#10300FBut this is\x01",
            "It is story within the support section to the last.\x01",
            "I do not need to worry about everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04100F……Really.\x02\x03",
            "But when we need our hands\x01",
            "You can say anytime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FOh, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F(Randy … Wait a minute.\x01",
            "I will definitely catch it … …)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16E, 2)
    Jump("loc_2098")

    label("loc_1EBD")


    ChrTalk(
        0x105,
        (
            "#10300FそういえばAbbas……\x01",
            "Did you gather information on Wald?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x105, 0)
    Sleep(1000)
    TurnDirection(0xB, 0x105, 0)
    TurnDirection(0xA, 0x105, 0)

    ChrTalk(
        0x8,
        (
            "#04100FDisagreeable……\x01",
            "For now, the strong information is\x01",
            "Almost not obtained.\x02\x03",
            "Probably to avoid eye view\x01",
            "Because he was acting,\x01",
            "There was almost no sighting information.\x02\x03",
            "It is not easy to grasp the route of obtaining medicine\x01",
            "To be honest, it will be quite difficult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10303F……Really.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04100FWell, even so\x01",
            "I will continue the survey.\x02\x03",
            "As soon as I know something\x01",
            "Please wait as we contact you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FOh, I got it.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x16E, 1)

    label("loc_2098")

    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0x8, 0xFF)
    OP_93(0xA, 0x5A, 0x0)
    OP_93(0xB, 0x0, 0x0)
    OP_93(0x8, 0xE1, 0x0)
    Return()

    # Function_7_1BA4 end

    def Function_8_20BA(): pass

    label("Function_8_20BA")

    OP_4B(0x8, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x105, 0)
    Sleep(1000)
    TurnDirection(0xB, 0x105, 0)
    TurnDirection(0xA, 0x105, 0)

    ChrTalk(
        0x8,
        (
            "#04100FWas it …?\x01",
            "Information collection on Waldo\x01",
            "Leave it to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "However, once the setup is in place\x01",
            "I will go listening immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "So, Wadi, you\x01",
            "Focus on the work of the support department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FThank you, I have asked for your kindness.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16E, 0)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0x8, 0x10)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0x8, 0xFF)
    OP_93(0xA, 0x5A, 0x0)
    OP_93(0xB, 0x0, 0x0)
    OP_93(0x8, 0xE1, 0x0)
    Return()

    # Function_8_20BA end

    def Function_9_21FF(): pass

    label("Function_9_21FF")

    OP_4B(0x8, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xD,
        (
            "This store, quite recently\x01",
            "It seems that it is prosperous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Enviously … Hey!\x01",
            "I want to have the economy divided.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04102FHuu, neither there never\x01",
            "It is not that the economy is bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Well, I do not deny well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F(Both of you seem to be enjoying something.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F(Huff, geezers,\x01",
            "I think that the wavelength matches. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211F(… if you say that\x01",
            "I think that Mr. Wasy too. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 6)
    OP_4C(0xD, 0xFF)
    OP_4C(0x8, 0xFF)
    ClearChrFlags(0xD, 0x10)
    Return()

    # Function_9_21FF end

    def Function_10_23A4(): pass

    label("Function_10_23A4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_24D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2470")

    ChrTalk(
        0xFE,
        (
            "Ursula hospital,\x01",
            "A considerable number of patients\x01",
            "She seems to be floating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I informed my father about it,\x01",
            "I am busy but managed somehow\x01",
            "It seemed to be turning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…… I have to work hard as well.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_24CF")

    label("loc_2470")


    ChrTalk(
        0xFE,
        (
            "Still, in the future I like my father\x01",
            "I do not know whether it will be on the road ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…… I have to work hard as well.\x02",
    )

    CloseMessageWindow()

    label("loc_24CF")

    Jump("loc_33F9")

    label("loc_24D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_25C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2567")

    ChrTalk(
        0xFE,
        (
            "What I have to think first is\x01",
            "It is safe for neighboring residents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For the sake of emergency,\x01",
            "The state of east street\x01",
            "I think that it is better to watch over you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25BF")

    label("loc_2567")


    ChrTalk(
        0xFE,
        (
            "This is us\x01",
            "I will try it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You managed to manage it safely\x01",
            "Please come back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25BF")

    Jump("loc_33F9")

    label("loc_25C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_28A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2809")

    ChrTalk(
        0xFE,
        (
            "今朝、Abbasがみんなを集めて\x01",
            "\"For the time being, I left Trinity ahead\"\x01",
            "Just saying I just went somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I did not even mention the destination,\x01",
            "I wonder what happened ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FAbbasが……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FPerhaps,\x01",
            "Are you with Wasi?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… I do not know.\x01",
            "They also have defense forces\x01",
            "It looks like you are wandering around in the city … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Was it possibly arrested …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201FWaji-san like that ha men\x01",
            "I do not think so … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FHM……\x01",
            "Well, it is better to settle anyway.\x01",
            "Is not it good?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "… … That's right.\x01",
            "Anyway we need to protect the shop ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_28A0")

    label("loc_2809")


    ChrTalk(
        0xFE,
        (
            "ワジやAbbasも心配だけど……\x01",
            "…… Father in Ursula hospital\x01",
            "Is it alright.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because of my father, even in this situation\x01",
            "It seems to be patient's response … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28A0")

    Jump("loc_33F9")

    label("loc_28A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_28B3")
    Jump("loc_33F9")

    label("loc_28B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_296A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28CE")
    Call(0, 7)
    Jump("loc_2965")

    label("loc_28CE")


    ChrTalk(
        0xFE,
        (
            "Even so ……\x01",
            "He is that redhead, even though it is raining\x01",
            "I had a tremendous amount of baggage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if I saw it, it would be considerable weight,\x01",
            "I was surprised because it was agile.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2965")

    Jump("loc_33F9")

    label("loc_296A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2A66")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2985")
    Call(0, 8)
    Jump("loc_2A61")

    label("loc_2985")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A24")

    ChrTalk(
        0xFE,
        (
            "By the way yesterday\x01",
            "A derailment accident on the West Crossbell Highway\x01",
            "It happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Seemingly a few people were seriously injured … …\x01",
            "My father seems to be considerably busy as well.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2A61")

    label("loc_2A24")


    ChrTalk(
        0xFE,
        (
            "My father is amazing ……\x01",
            "In such a situation, everyone is counted on … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A61")

    Jump("loc_33F9")

    label("loc_2A66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2B61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AE6")

    ChrTalk(
        0xFE,
        "I … … What do you want to be?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "… … Damn, how much again\x01",
            "There is no answer even if you think about it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2B5C")

    label("loc_2AE6")


    ChrTalk(
        0xFE,
        (
            "Right now, studying itself is there\x01",
            "I did not dislike it …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Also heading to the desk\x01",
            "I wonder if I can see something ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B5C")

    Jump("loc_33F9")

    label("loc_2B61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2D03")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C84")

    ChrTalk(
        0xFE,
        (
            "When I was little I was like my father\x01",
            "I want to become a doctor,\x01",
            "I thought so … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But since when, as much as my dad\x01",
            "Noticing that it is not excellent … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "……\x01",
            "What am I talking about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ha … forever\x01",
            "Because I'm blown away like this\x01",
            "I am incomplete.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2CFE")

    label("loc_2C84")


    ChrTalk(
        0xFE,
        (
            "Or, the waiter\x01",
            "Do not be wrong, Masui.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even my salary is out,\x01",
            "I have to do my job seriously.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CFE")

    Jump("loc_33F9")

    label("loc_2D03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2F38")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EBB")

    ChrTalk(
        0xFE,
        (
            "What I should say …\x01",
            "Recently, everyone is lively.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With half-hearted feelings\x01",
            "I guess only I am working ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ha\x01",
            "I wonder what I am doing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F(Wadi … ….\x01",
            "Are not you calling out a voice? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F(Oh, from testosterins testiments\x01",
            "I leave it to the autonomy of everyone. )\x02\x03",
            "#10300F(Purposely from me it is unnecessary\x01",
            "I try not to speak out. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211F(……somehow,\x01",
            "It looks like Sergei manager. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2F33")

    label("loc_2EBB")


    ChrTalk(
        0xFE,
        (
            "Recently, everyone is lively.\x01",
            "I am the only half-way … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ha\x01",
            "I wonder what I am doing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F33")

    Jump("loc_33F9")

    label("loc_2F38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_308A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_303D")

    ChrTalk(
        0xFE,
        (
            "Men of Vipers this morning\x01",
            "Bump over your shoulders\x01",
            "I have been sending a fellowship … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you apologize obediently from here\x01",
            "Inspirational\x01",
            "I started pulling myself up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Abbasから聞いていた\x01",
            "It was a workaround,\x01",
            "It is really effective.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3085")

    label("loc_303D")


    ChrTalk(
        0xFE,
        (
            "Is this a peaceful coping method …?\x01",
            "Abbasから学ぶべきことは\x01",
            "There are so many.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3085")

    Jump("loc_33F9")

    label("loc_308A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_31FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3118")

    ChrTalk(
        0xFE,
        "Sounds awesome, that blonde guest ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you thought that you did a sudden flirting talk\x01",
            "Next time we are playing billiards\x01",
            "What is rarely slashing … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31F6")

    label("loc_3118")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31AE")

    ChrTalk(
        0xFE,
        (
            "Some, someone outside\x01",
            "It sounds a bit noisy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Perhaps the customers of the time ago ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "… Well, good,\x01",
            "It seems better not to mind.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_31F6")

    label("loc_31AE")


    ChrTalk(
        0xFE,
        "Perhaps the customers of the time ago ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "… Well, okay, I do not care.\x02",
    )

    CloseMessageWindow()

    label("loc_31F6")

    Jump("loc_33F9")

    label("loc_31FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_323D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3216")
    Call(0, 11)
    Jump("loc_3238")

    label("loc_3216")


    ChrTalk(
        0xFE,
        "Then customers, please visit here.\x02",
    )

    CloseMessageWindow()

    label("loc_3238")

    Jump("loc_33F9")

    label("loc_323D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_32BF")

    ChrTalk(
        0xFE,
        (
            "Well, on rainy days\x01",
            "I feel like I'm feeling down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Jimajima, hair bounces … ….\x01",
            "I want you to stop it soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33F9")

    label("loc_32BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_33F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3392")

    ChrTalk(
        0xFE,
        "I am not specially catered for serving ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because there was nothing else to do,\x01",
            "I inevitably accepted the waiter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, even though I took over\x01",
            "I will work with responsibility.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_33F9")

    label("loc_3392")


    ChrTalk(
        0xFE,
        (
            "Welcome, if you want to get a seat\x01",
            "Please tell me it will guide you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "This is a waiter for me, though.\x02",
    )

    CloseMessageWindow()

    label("loc_33F9")

    TalkEnd(0xFE)
    Return()

    # Function_10_23A4 end

    def Function_11_33FD(): pass

    label("Function_11_33FD")

    OP_4B(0xA, 0xFF)
    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)

    ChrTalk(
        0xA,
        "Well, the customer is two people.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Counter seats and table seats\x01",
            "There is, but which do you do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "That's right.\x01",
            "That's it,\x01",
            "Shall I make it a counter seat?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "Yes, let's do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Certainly.\x01",
            "Then I will show you.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0x10, 0xFF)
    OP_4C(0x11, 0xFF)
    ClearChrFlags(0x10, 0x10)
    ClearChrFlags(0x11, 0x10)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_11_33FD end

    def Function_12_3513(): pass

    label("Function_12_3513")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_35EA")
    TalkBegin(0xB)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3533")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35E6")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3591")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3591")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35B1")
    OP_AF(0xB3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_35E1")

    label("loc_35B1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35C5")
    Jump("loc_35E1")

    label("loc_35C5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35E1")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 13)

    label("loc_35E1")

    Jump("loc_3533")

    label("loc_35E6")

    TalkEnd(0xB)
    Return()

    label("loc_35EA")

    TalkBegin(0xB)
    Call(0, 13)
    TalkEnd(0xB)
    Return()

    # Function_12_3513 end

    def Function_13_35F4(): pass

    label("Function_13_35F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3854")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37D7")

    ChrTalk(
        0xB,
        (
            "Even so … I was surprised.\x01",
            "ワジとAbbasが教会の関係者だとは。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3788")

    ChrTalk(
        0xB,
        (
            "Something like a distant thing suddenly somewhat\x01",
            "Do not get distracted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10402FHuh, well, the essence does not change\x01",
            "I will be glad if you touch us as usual.\x02\x03",
            "#10404FI've been with \"Testers\" with you guys\x01",
            "Wadi Hemisphere is the only one,\x01",
            "It is enough to say that it is true me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "That's right.\x01",
            "I am glad if you say so.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37CF")

    label("loc_3788")


    ChrTalk(
        0xB,
        (
            "I had never done that before,\x01",
            "Sho, honestly I can not believe it now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37CF")

    SetScenarioFlags(0x0, 3)
    Jump("loc_384F")

    label("loc_37D7")


    ChrTalk(
        0xB,
        (
            "ワ、ワジとAbbasが\x01",
            "You are a stakeholder in the church.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I had never done that before,\x01",
            "Sho, honestly I can not believe it now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_384F")

    Jump("loc_4552")

    label("loc_3854")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3949")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38E7")

    ChrTalk(
        0xB,
        (
            "Well, as expected, that monster\x01",
            "What you want to do\x01",
            "You had better stop it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well, I have not attacked it now,\x01",
            "There is no fear of God who does not touch.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3944")

    label("loc_38E7")


    ChrTalk(
        0xB,
        (
            "Azelは、ひ、東通りにいる\x01",
            "I went back to my family once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Oh, I hope your happiness is safe.\x02",
    )

    CloseMessageWindow()

    label("loc_3944")

    Jump("loc_4552")

    label("loc_3949")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_39C5")

    ChrTalk(
        0xB,
        (
            "Abbasにも……\x01",
            "There must be something wrong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Now as I say,\x01",
            "And I have to protect the store firmly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4552")

    label("loc_39C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_39D3")
    Jump("loc_4552")

    label("loc_39D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3A7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39EE")
    Call(0, 7)
    Jump("loc_3A77")

    label("loc_39EE")


    ChrTalk(
        0xB,
        (
            "Oh, his face … …\x01",
            "What a big impression it was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I mean, I'm thinking about it\x01",
            "I mean the imminent obsessive ……\x01",
            "To be honest, it fell apart quite a bit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A77")

    Jump("loc_4552")

    label("loc_3A7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3B1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A97")
    Call(0, 8)
    Jump("loc_3B15")

    label("loc_3A97")


    ChrTalk(
        0xB,
        (
            "Here, from now on\x01",
            "I'm planning to listen and try various things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Gugnosis and the source of\x01",
            "I hope to find out where ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B15")

    Jump("loc_4552")

    label("loc_3B1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3CE2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C93")

    ChrTalk(
        0xB,
        "Ka, the cocktail is an explosion.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "O, daring ideas\x01",
            "It creates innovative inventions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "But … a bit\x01",
            "It may have been overwhelming.\x01",
            "… … It seems I had no talent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "so……\x01",
            "Ka, I'm stopping making cocktails.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "My last work ……\x01",
            "Well, please dispose somewhere.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '粉红液体'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('粉红液体', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x17C, 5)
    Jump("loc_3CDD")

    label("loc_3C93")


    ChrTalk(
        0xB,
        "Ka, I'm stopping making cocktails.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "…… I do not want to be a murderer.\x02",
    )

    CloseMessageWindow()

    label("loc_3CDD")

    Jump("loc_4552")

    label("loc_3CE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3ED6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E53")

    ChrTalk(
        0xB,
        (
            "My cocktail,\x01",
            "ア、Ashleyさんに大量に\x01",
            "I bought it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Ah, regardless of taste and appearance,\x01",
            "You were praised that you can use it on the battlefield.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Hmm……? Have you been praised?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "And anyway … …\x01",
            "My cocktail is\x01",
            "Ashleyさんのお墨付きだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Okay, you should go get it.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '褐色液体'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('褐色液体', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x17C, 4)
    Jump("loc_3ED1")

    label("loc_3E53")


    ChrTalk(
        0xB,
        (
            "My cocktail can be used on the battlefield ……\x01",
            "That is, it means that it is nutritious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The smell is alright ……\x01",
            "Please say go and go.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3ED1")

    Jump("loc_4552")

    label("loc_3ED6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_40F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4068")

    ChrTalk(
        0xB,
        (
            "ア、AzelとLiang、\x01",
            "Always going to have fun with two people\x01",
            "I am studying cocktails.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "So, I also\x01",
            "I decided to make it as a trial.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Because it looks bad from two people\x01",
            "I was told that I can not put it in the shop … …\x01",
            "There is no doubt that the ingredients are good for the body.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Take it, OK, if you do not mind.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '紫色液体'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('紫色液体', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00005FOh, oh …… Thank you.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16E, 3)
    Jump("loc_40ED")

    label("loc_4068")


    ChrTalk(
        0xB,
        (
            "My cocktail is\x01",
            "The material has absolute confidence.\x01",
            "There is no doubt that it is good for your body.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It looks like it is ……\x01",
            "Go, go ahead.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40ED")

    Jump("loc_4552")

    label("loc_40F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4286")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4213")

    ChrTalk(
        0xB,
        (
            "け、今朝はKeenと一緒に\x01",
            "I went to stock,\x01",
            "I came across with Viper.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "In spite of himself\x01",
            "Although it became it,\x01",
            "Keenに止められたんだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "No way, that way Viper\x01",
            "I did not expect to withdraw, but …\x01",
            "Here, this may be discovered.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4281")

    label("loc_4213")


    ChrTalk(
        0xB,
        (
            "We are already,\x01",
            "I do not do a useless fight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "A, if you want to make aza\x01",
            "I can not even see the shop.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4281")

    Jump("loc_4552")

    label("loc_4286")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4331")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42F3")

    ChrTalk(
        0xB,
        "くそっ、ついにLiangまで……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "That blonde white coat ……\x01",
            "Well, it is considerable Tsumono.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_432C")

    label("loc_42F3")


    ChrTalk(
        0xB,
        (
            "Oh, that blonde white coat,\x01",
            "It was like a stormy customer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_432C")

    Jump("loc_4552")

    label("loc_4331")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_43B3")

    ChrTalk(
        0xB,
        (
            "Thanks.\x01",
            "Recently the number of customers coming from the city has increased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "But I wonder if I feel uneasy about security\x01",
            "I do not think so much at night.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4552")

    label("loc_43B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_44B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_445E")

    ChrTalk(
        0xB,
        (
            "Oh, if it's not after that,\x01",
            "The basic billiards are all you can play.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "However, at least 1 drink or more\x01",
            "It is a condition to get ordered.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_44B3")

    label("loc_445E")


    ChrTalk(
        0xB,
        (
            "Billiards are\x01",
            "Basically it's all you can play.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "However, it is limited to the customers of the bar.\x02",
    )

    CloseMessageWindow()

    label("loc_44B3")

    Jump("loc_4552")

    label("loc_44B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4552")

    ChrTalk(
        0xB,
        (
            "I am a billiard\x01",
            "A, instructor / scorer\x01",
            "It was decided to be in charge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "However, how to hit the ball and rules\x01",
            "If you do not understand, ask me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4552")

    Return()

    # Function_13_35F4 end

    def Function_14_4553(): pass

    label("Function_14_4553")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_456E")
    Call(0, 12)
    Jump("loc_4571")

    label("loc_456E")

    Call(0, 15)

    label("loc_4571")

    Return()

    # Function_14_4553 end

    def Function_15_4572(): pass

    label("Function_15_4572")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4654")
    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45CB")

    ChrTalk(
        0x9,
        (
            "Oh, at times like this\x01",
            "Abbasがいてくれたらな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4650")

    label("loc_45CB")


    ChrTalk(
        0x9,
        (
            "Thus again with Viper\x01",
            "It is a day to cooperate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, their ability\x01",
            "We are the most familiar,\x01",
            "I do not have any more friends as a friend.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4650")

    TalkEnd(0x9)
    Return()

    label("loc_4654")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4671")
    TalkBegin(0x9)
    Call(0, 22)
    TalkEnd(0x9)
    Return()

    label("loc_4671")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_467E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4731")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46DC")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_46DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46FC")
    OP_AF(0xB3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_472C")

    label("loc_46FC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4710")
    Jump("loc_472C")

    label("loc_4710")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_472C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 16)

    label("loc_472C")

    Jump("loc_467E")

    label("loc_4731")

    TalkEnd(0x9)
    Return()

    # Function_15_4572 end

    def Function_16_4735(): pass

    label("Function_16_4735")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_486E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4809")

    ChrTalk(
        0x9,
        (
            "Abbasがしばらく\x01",
            "To live is\x01",
            "Sometimes there are … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "This time more than ever\x01",
            "Seriously or serious look\x01",
            "I feel like I was doing it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "… … as soon as you come back\x01",
            "I do not mind.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4869")

    label("loc_4809")


    ChrTalk(
        0x9,
        (
            "For the time being,\x01",
            "I wonder how long it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "… … as soon as you come back\x01",
            "I do not mind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4869")

    Jump("loc_5424")

    label("loc_486E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4B44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4911")

    ChrTalk(
        0x9,
        (
            "I am doing my best at work\x01",
            "For people, here\x01",
            "I make special drinks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Everyone drinks well.\x01",
            "The mixer is also fully operational.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B3F")

    label("loc_4911")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4ADB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A83")

    ChrTalk(
        0x9,
        (
            "The support department will do the reconstruction work\x01",
            "They are helping me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Take this.\x01",
            "He behaves to everyone\x01",
            "It's a special drink.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '甘露『紫绀』'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got six pieces.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('甘露『紫绀』', 6)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00005FCan I have this so much?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHuh, that's it for the number of people.\x01",
            "ありがとう、Liang。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Haha, you are welcome.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18D, 4)
    Jump("loc_4AD6")

    label("loc_4A83")


    ChrTalk(
        0x9,
        (
            "Help me with reconstruction work\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Huhu, you are a special support department.\x02",
    )

    CloseMessageWindow()

    label("loc_4AD6")

    Jump("loc_4B3F")

    label("loc_4ADB")


    ChrTalk(
        0x9,
        (
            "Azelたちの作った豚汁、\x01",
            "It sounds like it was popular.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "What to do, cook it out\x01",
            "My heart will warm up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B3F")

    Jump("loc_5424")

    label("loc_4B44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4CDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C49")

    ChrTalk(
        0x9,
        (
            "In this occupation case,\x01",
            "It is a conspiracy of the Imperial government\x01",
            "There seems to be a story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Anything, excuse this incident\x01",
            "Imperial troops stationing Crossbell\x01",
            "I am thinking about … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If it were true\x01",
            "It is not very,\x01",
            "It is an unforgivable story.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4CDA")

    label("loc_4C49")


    ChrTalk(
        0x9,
        (
            "If really, the Imperial government\x01",
            "For political purposes, this occupation case\x01",
            "If it caused it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It is not very,\x01",
            "It is an unforgivable story.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CDA")

    Jump("loc_5424")

    label("loc_4CDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4D44")

    ChrTalk(
        0x9,
        (
            "Wald ……\x01",
            "I wonder what you are really doing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Even if it is sake … drug …\x02",
    )

    CloseMessageWindow()
    Jump("loc_5424")

    label("loc_4D44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4E76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DE6")

    ChrTalk(
        0x9,
        (
            "Those customers,\x01",
            "I'm pretty sorry for my soup pasta\x01",
            "You seem to like it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "ふふ、流石はAbbas秘伝の\x01",
            "Is it a special recipe?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4E71")

    label("loc_4DE6")


    ChrTalk(
        0x9,
        (
            "With what I made\x01",
            "I can make people smile\x01",
            "It is very wonderful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Cooking is quite painful, though,\x01",
            "I feel that everything will be rewarded.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E71")

    Jump("loc_5424")

    label("loc_4E76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5026")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FAE")

    ChrTalk(
        0x9,
        (
            "Yesterday, Vipers members\x01",
            "Two people came aboard in my house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "What was that, because it was a terrific sword curtain\x01",
            "I wonder if he came to fight even in a fight\x01",
            "I thought that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "They went downstairs with a feeling of being upset\x01",
            "I heard about Wald and went.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Let me worry about my brothers and sisters.\x01",
            "Wald … I wonder what you are doing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5021")

    label("loc_4FAE")


    ChrTalk(
        0x9,
        (
            "While I was an enemy\x01",
            "Somewhat respectable places\x01",
            "I thought that it was … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Wald, now,\x01",
            "Clearly saying it is disqualified from the head.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5021")

    Jump("loc_5424")

    label("loc_5026")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_50BB")

    ChrTalk(
        0x9,
        (
            "Besse、シェイカーに\x01",
            "I was putting something suspicious though\x01",
            "Are you OK……?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you consult us,\x01",
            "I can do advice, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5424")

    label("loc_50BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_51F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_516E")

    ChrTalk(
        0x9,
        "Hi, welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Today we have good seasonal ingredients\x01",
            "I recommend daily small bowls.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "There is also a lunch menu,\x01",
            "If you are interested, please feel free to ask.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_51EC")

    label("loc_516E")


    ChrTalk(
        0x9,
        (
            "Today we have good seasonal ingredients\x01",
            "I recommend daily small bowls.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "There is also a lunch menu,\x01",
            "If you are interested, please feel free to ask.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51EC")

    Jump("loc_5424")

    label("loc_51F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_528C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5209")
    Jump("loc_5287")

    label("loc_5209")


    ChrTalk(
        0x9,
        (
            "After all, the game with that customer is\x01",
            "The settlement did not arrive, but …\x01",
            "Clearly, it was my complete defeat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "There is something above in the world.\x02",
    )

    CloseMessageWindow()

    label("loc_5287")

    Jump("loc_5424")

    label("loc_528C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5308")

    ChrTalk(
        0x9,
        (
            "はは、Azelのお姉さんも\x01",
            "As usual I am anxious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "While watching the exchange of two people\x01",
            "Something will be funny.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5424")

    label("loc_5308")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5390")

    ChrTalk(
        0x9,
        (
            "Whew …… On rainy days\x01",
            "It's tough to take one purchase.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Because it was dirty with mud here and there,\x01",
            "I have to change my clothes before cooking.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5424")

    label("loc_5390")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5424")

    ChrTalk(
        0x9,
        (
            "Hi, welcome.\x01",
            "Whenever you have an order, say it anytime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "For cocktails or knobs,\x01",
            "Abbas直伝の腕前を\x01",
            "Because I will show off to you in full.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5424")

    Return()

    # Function_16_4735 end

    def Function_17_5425(): pass

    label("Function_17_5425")

    Call(0, 18)
    Return()

    # Function_17_5425 end

    def Function_18_5429(): pass

    label("Function_18_5429")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5632")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55B2")

    ChrTalk(
        0xC,
        "\"Trinity\" also resumed business.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Although it became such a situation,\x01",
            "You can spend your everyday life as usual\x01",
            "It's important to be careful.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5566")

    ChrTalk(
        0x105,
        (
            "#10400FHuh, well do your best.\x01",
            "Look forward to shop even at such times\x01",
            "There will be some people doing it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Oh, of course.\x01",
            "You also worked hard for me, Wadi.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55AA")

    label("loc_5566")


    ChrTalk(
        0xC,
        (
            "姉さんやYuggottも\x01",
            "I support you,\x01",
            "I have to stop firmly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55AA")

    SetScenarioFlags(0x0, 5)
    Jump("loc_562D")

    label("loc_55B2")


    ChrTalk(
        0xC,
        (
            "\"Trinity\" also resumes business.\x01",
            "Please feel free to order.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "姉さんやYuggottも\x01",
            "I support you,\x01",
            "I have to stop firmly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_562D")

    Jump("loc_6085")

    label("loc_5632")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5640")
    Jump("loc_6085")

    label("loc_5640")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_56DD")

    ChrTalk(
        0xC,
        (
            "It was being troubled in the city,\x01",
            "How does the declaration of independence stand?\x01",
            "Somehow, I do not mind ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "……姉さんとYuggottの様子を見に\x01",
            "I will probably return home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6085")

    label("loc_56DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_56EB")
    Jump("loc_6085")

    label("loc_56EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_581F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57A1")

    ChrTalk(
        0xC,
        (
            "The mysterious unit that hit Mainz\x01",
            "It seems terribly tougher.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The guard is also pretty\x01",
            "She seems to be struggling, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "……Anyways,\x01",
            "I want the situation to come quickly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_581A")

    label("loc_57A1")


    ChrTalk(
        0xC,
        (
            "In such a case,\x01",
            "I do not know why\x01",
            "I am worried about my family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Later a bit\x01",
            "I wonder if I will go to see the house ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_581A")

    Jump("loc_6085")

    label("loc_581F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_58AB")

    ChrTalk(
        0xC,
        (
            "ヴァルドがあのDinoって新米と\x01",
            "I might have drunk the same medicine ….?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "While being a hostile team,\x01",
            "I am worried about running.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6085")

    label("loc_58AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5A09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5972")

    ChrTalk(
        0xC,
        "Well, it's already noon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "By the way, older sister,\x01",
            "I was saying that I also work today,\x01",
            "I guess it is not impossible again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "As I work,\x01",
            "You can reduce your work\x01",
            "I'm telling you ….\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5A04")

    label("loc_5972")


    ChrTalk(
        0xC,
        (
            "By the way, older sister,\x01",
            "I was saying that I also work today,\x01",
            "I guess it is not impossible again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "As I work,\x01",
            "You can reduce your work\x01",
            "I'm telling you ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A04")

    Jump("loc_6085")

    label("loc_5A09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5BC6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B0B")

    ChrTalk(
        0xC,
        (
            "Keenの奴、\x01",
            "About the future about recently\x01",
            "He seems to be suffering.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "He is smart,\x01",
            "Besides, my parents are also rich.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If it comes to that, anything\x01",
            "I think I can get it ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "What is it …?\x01",
            "Everyone is troubled.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5BC1")

    label("loc_5B0B")


    ChrTalk(
        0xC,
        (
            "そういえば昔、Keenの奴、\x01",
            "My father's existence is complex\x01",
            "I had something to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Even if you do your best and become a doctor\x01",
            "If I can not cross my father,\x01",
            "I was saying that there is no meaning … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BC1")

    Jump("loc_6085")

    label("loc_5BC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5C3B")

    ChrTalk(
        0xC,
        (
            "Abbasってあらゆることに\x01",
            "I am familiar with knowledge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I'm always studying.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6085")

    label("loc_5C3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5CAC")

    ChrTalk(
        0xC,
        "Recently, my job is something fun.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Something like me, like this\x01",
            "I feel like I can work forever.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6085")

    label("loc_5CAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5DB8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D59")

    ChrTalk(
        0xC,
        (
            "The customer of the white coat\x01",
            "Suddenly play billiard confrontation with us\x01",
            "I told you I wanted to do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "As a result, everyone loses\x01",
            "今は最後の砦のLiangとやってるよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DB3")

    label("loc_5D59")


    ChrTalk(
        0xC,
        (
            "However……\x01",
            "It was a really strange customer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "What is it?\x01",
            "I do not want to talk to someone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DB3")

    Jump("loc_6085")

    label("loc_5DB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5E26")

    ChrTalk(
        0xC,
        (
            "Ha, sister also\x01",
            "Even if nothing happens suddenly ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "……whatever,\x01",
            "Now I concentrate on my work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6085")

    label("loc_5E26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5EC8")

    ChrTalk(
        0xC,
        (
            "Liangに教わりながら、\x01",
            "Cocktail occasionally occasionally\x01",
            "I'm making it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Cocktail making\x01",
            "It's tough but deep inside,\x01",
            "I'm having fun doing it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6085")

    label("loc_5EC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6085")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6022")

    ChrTalk(
        0xC,
        (
            "With the introduction of Wazi 's Special Affairs Support Division,\x01",
            "Everyone in the team\x01",
            "I talked about various things … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Tentatively, for the while\x01",
            "We cooperated with \"everyone\" to \"Trinity\"\x01",
            "I decided to help out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Originally doubled as a team hangout\x01",
            "Abbasが細々とやっていた\x01",
            "It's a shop, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "From now on bringing in Bang Bang customers\x01",
            "I'm going to open a business.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6085")

    label("loc_6022")


    ChrTalk(
        0xC,
        "Please keep in mind Trinity.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Menu is also plentiful abundantly,\x01",
            "Please also take advantage of meals only.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6085")

    TalkEnd(0xC)
    Return()

    # Function_18_5429 end

    def Function_19_6089(): pass

    label("Function_19_6089")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_610D")

    ChrTalk(
        0xFE,
        (
            "Soup pasta here,\x01",
            "It's amazingly delicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Clearly,\x01",
            "Of a dish offered at the bar\x01",
            "It exceeds the level.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61C1")

    label("loc_610D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6169")

    ChrTalk(
        0xFE,
        "Was there anything on the waiter?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Somehow my heart is not here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_61C1")

    label("loc_6169")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_61C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6184")
    Call(0, 11)
    Jump("loc_61C1")

    label("loc_6184")


    ChrTalk(
        0xFE,
        (
            "I have heard it in the restaurant … …\x01",
            "It's pretty nice atmosphere.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_61C1")

    TalkEnd(0xFE)
    Return()

    # Function_19_6089 end

    def Function_20_61C5(): pass

    label("Function_20_61C5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_620F")

    ChrTalk(
        0xFE,
        (
            "Huhu, the texture of this penne is\x01",
            "It is irresistible, is not it ~, happy jet\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62BB")

    label("loc_620F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6271")

    ChrTalk(
        0xFE,
        (
            "Hehu, this shop,\x01",
            "I came again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As usual,\x01",
            "It's fashionable and good atmosphere.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62BB")

    label("loc_6271")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_62BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_628C")
    Call(0, 11)
    Jump("loc_62BB")

    label("loc_628C")


    ChrTalk(
        0xFE,
        (
            "Oh, in such a place\x01",
            "You have such a shop.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62BB")

    TalkEnd(0xFE)
    Return()

    # Function_20_61C5 end

    def Function_21_62BF(): pass

    label("Function_21_62BF")

    TalkBegin(0xFE)
    Call(0, 22)
    TalkEnd(0xFE)
    Return()

    # Function_21_62BF end

    def Function_22_62C9(): pass

    label("Function_22_62C9")

    OP_4B(0x12, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_93(0x9, 0x5A, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63BA")

    ChrTalk(
        0x12,
        (
            "Ha ha ha ha, a boy.\x01",
            "I guess there is not much time left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "…… Your older brother, you do quite well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "This is equivalent to Wadi ……\x01",
            "No, it may be more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305F(…… Huh?\x01",
            "Apparently it looks like a big deal. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_640E")

    label("loc_63BA")


    ChrTalk(
        0x12,
        "Now, next time is your turn.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Oh, ah ……\x01",
            "I will think about how to aim for it.\x01",
            "Wait a minute.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_640E")

    OP_4C(0x12, 0xFF)
    OP_4C(0x9, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_22_62C9 end

    def Function_23_641A(): pass

    label("Function_23_641A")

    OP_4B(0x13, 0xFF)
    OP_4B(0x14, 0xFF)
    OP_4B(0x12, 0xFF)

    ChrTalk(
        0x14,
        "CAR, it is amazing!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "Really cool, cool\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Hahah, regarding \"aim\"\x01",
            "I am confident as it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Of course, what I am aiming now is\x01",
            "It is not such a spherical roller,\x01",
            "It is your heart 's heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "Yet, also say such a thing and spray\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "Hehe, you are really good at it.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    SetScenarioFlags(0x1, 2)
    ClearChrFlags(0x13, 0x10)
    ClearChrFlags(0x14, 0x10)
    OP_4C(0x12, 0xFF)
    OP_4C(0x13, 0xFF)
    OP_4C(0x14, 0xFF)
    Return()

    # Function_23_641A end

    def Function_24_6552(): pass

    label("Function_24_6552")


    ChrTalk(
        0x13,
        (
            "Oh, no way\x01",
            "Suddenly I will go out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "If you do like this\x01",
            "I should have listened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Well, indeed the face is\x01",
            "I was cool, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "But a bit\x01",
            "Was not he a strange person?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "You idiot, hey\x01",
            "What is changing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "There is also that person's\x01",
            "It is not one of attraction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "Well, I guess that's something like that.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    SetScenarioFlags(0x1, 2)
    ClearChrFlags(0x13, 0x10)
    ClearChrFlags(0x14, 0x10)
    Return()

    # Function_24_6552 end

    def Function_25_66AD(): pass

    label("Function_25_66AD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6700")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66CC")
    Call(0, 23)
    Jump("loc_66FB")

    label("loc_66CC")


    ChrTalk(
        0xFE,
        (
            "Uhufu, today is\x01",
            "I met a nice person Spraying\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66FB")

    Jump("loc_6778")

    label("loc_6700")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6712")
    Call(0, 24)
    Jump("loc_6778")

    label("loc_6712")


    ChrTalk(
        0xFE,
        (
            "Oh, no way\x01",
            "Suddenly I will go out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you do like this\x01",
            "I should have listened.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6778")

    TalkEnd(0xFE)
    Return()

    # Function_25_66AD end

    def Function_26_677C(): pass

    label("Function_26_677C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_679B")
    Call(0, 23)
    Jump("loc_67D4")

    label("loc_679B")


    ChrTalk(
        0xFE,
        (
            "That man, not just musical instruments\x01",
            "Billiards are also good.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67D4")

    Jump("loc_685F")

    label("loc_67D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67EB")
    Call(0, 24)
    Jump("loc_685F")

    label("loc_67EB")


    ChrTalk(
        0xFE,
        (
            "My face is good, singing and musical instruments are good,\x01",
            "Billiards as well ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But what is it,\x01",
            "I wonder if it came with pins ~.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_685F")

    TalkEnd(0xFE)
    Return()

    # Function_26_677C end

    def Function_27_6863(): pass

    label("Function_27_6863")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6878")
    Call(0, 9)
    Jump("loc_68C9")

    label("loc_6878")


    ChrTalk(
        0xFE,
        (
            "Kuku, drinking from the daytime\x01",
            "There is no delicious thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It will penetrate into five organs.\x02",
    )

    CloseMessageWindow()

    label("loc_68C9")

    TalkEnd(0xFE)
    Return()

    # Function_27_6863 end

    def Function_28_68CD(): pass

    label("Function_28_68CD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6989")

    ChrTalk(
        0xFE,
        (
            "In my brother's bar\x01",
            "I tried to visit with a secret.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At first I was shy\x01",
            "He was entertaining me properly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Working with professionalism is\x01",
            "That's a good thing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_69E1")

    label("loc_6989")


    ChrTalk(
        0xFE,
        "Noisy\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Azelの作った\x01",
            "Non alcoholic cocktail ……\x01",
            "It is quite delicious.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69E1")

    TalkEnd(0xFE)
    Return()

    # Function_28_68CD end

    def Function_29_69E5(): pass

    label("Function_29_69E5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A74")

    ChrTalk(
        0xFE,
        (
            "Who is\x01",
            "みんなAzel兄ちゃんと\x01",
            "It is like a dress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Okay, I also\x01",
            "With all my older brothers\x01",
            "I want a blue hoodie.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6AB8")

    label("loc_6A74")


    ChrTalk(
        0xFE,
        (
            "Okay, I also\x01",
            "With all my older brothers\x01",
            "I want a blue hoodie.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6AB8")

    TalkEnd(0xFE)
    Return()

    # Function_29_69E5 end

    def Function_30_6ABC(): pass

    label("Function_30_6ABC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B4B")

    ChrTalk(
        0xFE,
        (
            "I do not understand it somehow,\x01",
            "Anyway, I'm going to tell that Yoroi\x01",
            "All they do is doing ~!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Waldo's\x01",
            "I'm sure I will!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B8A")

    label("loc_6B4B")


    ChrTalk(
        0xFE,
        (
            "I do not understand it well somehow,\x01",
            "Please decide to Hide! It is!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B8A")

    TalkEnd(0xFE)
    Return()

    # Function_30_6ABC end

    def Function_31_6B8E(): pass

    label("Function_31_6B8E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C1A")

    ChrTalk(
        0xFE,
        (
            "That Yoroy is far from the old city\x01",
            "It does not seem to come in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Once, residents of the neighborhood of Ignis\x01",
            "I evacuated indoors … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6CAD")

    label("loc_6C1A")


    ChrTalk(
        0xFE,
        (
            "Jed also\x01",
            "I hope to help you … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To being separated in such way with Waldo\x01",
            "It does not seem to be satisfied yet,\x01",
            "It can not be helped … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CAD")

    TalkEnd(0xFE)
    Return()

    # Function_31_6B8E end

    def Function_32_6CB1(): pass

    label("Function_32_6CB1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CED")

    ChrTalk(
        0xFE,
        "What exactly is the blue moya outside … …\x02",
    )

    CloseMessageWindow()
    Jump("loc_6D7E")

    label("loc_6CED")


    ChrTalk(
        0xFE,
        (
            "Fu, Hmm, … with the Blue Shu\x01",
            "This is the only time to cooperate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Waldo\x01",
            "As I can come back anytime,\x01",
            "I will protect the old city with us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D7E")

    TalkEnd(0xFE)
    Return()

    # Function_32_6CB1 end

    def Function_33_6D82(): pass

    label("Function_33_6D82")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04100.itp")
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_68(12000, 1000, 12000, 0)
    MoveCamera(33, 27, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, -300, 0, -500, 0)
    SetChrPos(0x102, 500, 0, -500, 0)
    SetChrPos(0x109, -300, 0, -500, 0)
    SetChrPos(0x105, 500, 0, -500, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(4000, 1000, 7000, 8000)
    MoveCamera(25, 17, 0, 8000)
    SetCameraDistance(23500, 8000)
    FadeToBright(2000, 0)
    OP_6F(0x79)
    Fade(500)
    OP_68(500, 1000, 4340, 0)
    MoveCamera(34, 16, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24160, 0)
    SetCameraDistance(23000, 2000)

    def lambda_6EDC():
        OP_96(0xFE, 0xFFFFFCE0, 0x0, 0xA28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6EDC)

    def lambda_6EF6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6EF6)
    Sleep(400)

    def lambda_6F0A():
        OP_96(0xFE, 0x2BC, 0x0, 0x960, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6F0A)

    def lambda_6F24():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6F24)
    Sleep(400)

    def lambda_6F38():
        OP_96(0xFE, 0xFFFFFE0C, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6F38)

    def lambda_6F52():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6F52)
    Sleep(400)

    def lambda_6F66():
        OP_96(0xFE, 0x2BC, 0x0, 0x4B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6F66)

    def lambda_6F80():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6F80)
    WaitChrThread(0x101, 1)

    def lambda_6F95():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6F95)
    WaitChrThread(0x102, 1)

    def lambda_6FA6():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6FA6)
    WaitChrThread(0x109, 1)

    def lambda_6FB7():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6FB7)
    WaitChrThread(0x105, 1)

    def lambda_6FC8():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6FC8)
    WaitChrThread(0x105, 2)
    OP_6F(0x10)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xA, 0x0, 0)

    ChrTalk(
        0xA,
        (
            "Welcome.\x01",
            "How many guests are there … ….\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "You are the Special Affairs Support Division! Is it?\x01",
            "And also Wadi …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005FWell, maybe …\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x8, 500)

    ChrTalk(
        0x105,
        (
            "#12P#10304FHugh, seriously\x01",
            "It seems that it is open.\x01",
            "Anything else.\x02\x03",
            "#10302Fフフ、どうだいAbbas。\x01",
            "I wonder if it's a little flourishing?\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-3430, 1100, 10150, 3000)
    OP_6F(0x79)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x8,
        (
            "… Well, it is a place I said so.\x02\x03",
            "It came a lot better than that.\x01",
            "Because I am troubled, I am relieved#2RRelax#You should leave.\x02",
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
    FadeToDark(500, 0, -1)
    OP_0D()

    def lambda_7223():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7223)

    def lambda_7230():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_7230)

    def lambda_723D():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_723D)

    def lambda_724A():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_724A)

    def lambda_7257():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_7257)
    OP_68(-3700, 1000, 10960, 0)
    MoveCamera(9, 24, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(23630, 0)
    SetChrPos(0xB, 4430, 0, 9820, 270)
    SetChrPos(0xA, 3200, 0, 7580, 270)
    SetChrPos(0x101, -2360, 0, 10680, 295)
    SetChrPos(0x102, -1270, 0, 9630, 295)
    SetChrPos(0x109, -2900, 0, 8830, 340)
    SetChrPos(0x105, -3950, 0, 9870, 340)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        "#04100F… How about Wazi, the Special Affairs Division?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FWell, is that comfortable?\x02\x03",
            "#10304FThe section chief and seniors have understanding,\x01",
            "I'm getting it done comfortably.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FNo, Wasi to be honest\x01",
            "I think it is too easy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10101FThat's right, Wadi.\x01",
            "Even though you are an associate member,\x01",
            "Awareness as a member of the police ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHuh, even if I say such a thing\x01",
            "This is my style.\x02\x03",
            "#10304FYou guys are not too busy,\x01",
            "Is not it okay to break a little more?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00106F…… Ha, to Wazi\x01",
            "No matter what I say wasteful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04100F…… Hmm, well\x01",
            "You seem to be doing it.\x01",
            "Then there is nothing wrong with that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006F(Rather, it's only a problem\x01",
            "It's a feeling … …)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00005Fby the way……\x01",
            "To enter Wazi 's Special Affairs Support Division\x01",
            "Did not you oppose any members?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00105FOh, certainly …\x01",
            "As expected\x01",
            "I wonder if you were perplexed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04100F…… There is nothing opposite.\x01",
            "Everything is decided by Wadi.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x109,
        "#12P#10106F(It is not much answer, but …).\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006F(Yes, this person is\x01",
            "Was it kind of like this …?)\x02",
        )
    )

    CloseMessageWindow()
    OP_68(320, 1500, 10860, 3000)
    MoveCamera(24, 15, 0, 3000)
    OP_6E(360, 3000)
    SetCameraDistance(24690, 3000)
    OP_6F(0x79)

    ChrTalk(
        0x9,
        (
            "#11PWell, indeed I was puzzled … …\x01",
            "Once, talking within the members,\x01",
            "That I was convinced properly.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_77DD():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_77DD)
    Sleep(10)

    def lambda_77ED():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_77ED)

    def lambda_77FA():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_77FA)
    Sleep(10)

    def lambda_780A():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_780A)
    Sleep(10)

    ChrTalk(
        0xA,
        (
            "#12PRepulsion against parents, family circumstances,\x01",
            "It's a member gathered for various reasons ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12PI decided the way the wadi goes\x01",
            "If you leave the team,\x01",
            "Neither do we oppose it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12PRather, we\x01",
            "It might be the opportunity to become independent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PActually, from the time just fighting,\x01",
            "I am assigned Trinity\x01",
            "I feel better now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PWell, there are no Wadi\x01",
            "Surely lonely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00002FHaha … I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#N#10102FIt looks pretty positive.\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#6P#10304FWell, originally Testerants\x01",
            "ほとんどAbbasに任せてたしね。\x02\x03",
            "#10300FEven if I do not exist, everyone\x01",
            "I thought that I could get along well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#6P#04102F……That's how it is.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-3700, 1000, 10960, 0)
    MoveCamera(24, 25, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(23630, 0)
    SetChrPos(0x101, -2360, 0, 10680, 295)
    SetChrPos(0x102, -1270, 0, 9630, 295)
    SetChrPos(0x109, -2900, 0, 8830, 340)
    SetChrPos(0x105, -3950, 0, 9870, 340)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#04100FAbout the affairs support section, Waji\x01",
            "Leave it to you for a while.\x02\x03",
            "Wazi, do not mind here\x01",
            "You should encourage your current job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10304FHuh, that is what I intend.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x102, 500)

    ChrTalk(
        0x105,
        "#6P#10304FThat's why again\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)

    ChrTalk(
        0x101,
        (
            "#11P#00006FWell, oh well\x01",
            "It seems to make me struggle, but …\x02\x03",
            "#00000FKohon, this time again\x01",
            "I will welcome you.\x02",
        )
    )

    CloseMessageWindow()
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0x138, 2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    SetChrPos(0x8, -4720, 0, 11880, 180)
    SetChrPos(0x9, 2980, 0, 14780, 180)
    SetChrPos(0xA, 3200, 0, 7580, 270)
    SetChrPos(0xB, 16149, 0, 12020, 270)
    SetChrPos(0xC, -1090, 0, 14910, 180)
    EventEnd(0x5)
    Return()

    # Function_33_6D82 end

    def Function_34_7CD7(): pass

    label("Function_34_7CD7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(210, 900, 6100, 0)
    MoveCamera(25, 17, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(27360, 0)
    SetChrPos(0x0, 0, 0, -500, 0)
    SetChrPos(0x1, 0, 0, -500, 0)
    SetChrPos(0x2, 0, 0, -500, 0)
    SetChrPos(0x3, 0, 0, -500, 0)
    SetChrPos(0x4, 0, 0, -500, 0)
    SetChrPos(0x5, 0, 0, -500, 0)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x4, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(500, 0)
    OP_0D()

    def lambda_7DDC():
        OP_96(0xFE, 0x384, 0x0, 0x141E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7DDC)

    def lambda_7DF6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_7DF6)
    Sleep(400)

    def lambda_7E0A():
        OP_96(0xFE, 0xFFFFFCE0, 0x0, 0x10FE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7E0A)

    def lambda_7E24():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7E24)
    Sleep(400)

    def lambda_7E38():
        OP_96(0xFE, 0x4BA, 0x0, 0xEA6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7E38)

    def lambda_7E52():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7E52)
    Sleep(400)

    def lambda_7E66():
        OP_96(0xFE, 0xFFFFFDA8, 0x0, 0xBE0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7E66)

    def lambda_7E80():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7E80)
    Sleep(400)

    def lambda_7E94():
        OP_96(0xFE, 0x3E8, 0x0, 0x794, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7E94)

    def lambda_7EAE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7EAE)
    Sleep(400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7EFF")

    def lambda_7ED4():
        OP_96(0xFE, 0xFFFFFC18, 0x0, 0x60E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_7ED4)

    def lambda_7EEE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_7EEE)
    Jump("loc_7F2A")

    label("loc_7EFF")


    def lambda_7F04():
        OP_96(0xFE, 0xFFFFFC18, 0x0, 0x60E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_7F04)

    def lambda_7F1E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_7F1E)

    label("loc_7F2A")

    WaitChrThread(0xF4, 1)
    WaitChrThread(0xF5, 1)

    ChrTalk(
        0x105,
        (
            "#12P#10405FOh, a rare customer\x01",
            "You seem to be coming.\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0x15, 0xFF)
    OP_4B(0x16, 0xFF)
    OP_4B(0x17, 0xFF)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(30)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_802B():
        TurnDirection(0xA, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_802B)

    def lambda_8038():
        TurnDirection(0xB, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_8038)

    def lambda_8045():
        TurnDirection(0x9, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8045)

    def lambda_8052():
        TurnDirection(0x15, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_8052)

    def lambda_805F():
        TurnDirection(0x16, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_805F)
    TurnDirection(0x17, 0x105, 500)

    ChrTalk(
        0x17,
        "#5PYou, you are …! It is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PWow, wax …! Is it?\x01",
            "It's a support department! It is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00005FVIPER TO TESTIMENTS ……\x01",
            "Have you gathered in such a place?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5POh, ah ……\x01",
            "Because the city is in this situation\x01",
            "Let's talk about the future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#5PMore than that … ….\x01",
            "Wadi 's guy, something weird clothes\x01",
            "Do not wear! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThat's right. …\x01",
            "それにAbbasは一緒じゃないのか？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10406FWell, I went home all the way\x01",
            "I do not have time to breathe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00300FNo, well, as expected\x01",
            "Is not the impact great?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203FOnce in a while they also know circumstances\x01",
            "Would you rather explain it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10403FWell, it is an Order of the Church\x01",
            "It will be confusing to say suddenly,\x01",
            "The explanation seems to be long.\x02\x03",
            "#10400FI will explain to you guys later.\x01",
            "Is that okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11POh, oh, that's right.\x01",
            "Now I have to concentrate on this situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10402Fフフ、Even so ……\x01",
            "僕やAbbasの留守をしっかりと\x01",
            "You seem to have kept it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11POf course, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PワジとAbbasは\x01",
            "Be sure to come back\x01",
            "I promised you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIf so, we are also\x01",
            "I just do my best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#5PHmm, we are\x01",
            "I was doing an answering machine of Wadi\x01",
            "I do not mean that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#5PIt was such a thing ……\x01",
            "Where Wald returns home\x01",
            "I want to protect it properly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5POh, the old city is ours\x01",
            "For Saber Viper as well\x01",
            "It's an important place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PSome people, including Jed,\x01",
            "I still want to cooperate\x01",
            "I have not become it ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10404FI see … Thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00109FHehe, very good,\x01",
            "Dino君。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x17)
    TurnDirection(0x17, 0x102, 500)

    ChrTalk(
        0x17,
        "#5PBesides, that's not the case …!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x17, 500)

    ChrTalk(
        0x15,
        (
            "#5Pハハッ、Dinoお前、\x01",
            "What are you shy about!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8739")

    ChrTalk(
        0x10A,
        (
            "#12P#00603FAnyway, in the Old Town\x01",
            "President's manipulation is\x01",
            "It does not appear to be appearing … ….\x02\x03",
            "#00600FLeave it to them here\x01",
            "It will be okay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FYeah, you are right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8886")

    label("loc_8739")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_87D2")

    ChrTalk(
        0x109,
        (
            "#N#12P#10103FAnyway, in the Old Town\x01",
            "President's manipulation is\x01",
            "I do not seem to have come out … ….\x02\x03",
            "#10100FLeave it to them here\x01",
            "It sounds fine.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_8866")

    label("loc_87D2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8866")

    ChrTalk(
        0x106,
        (
            "#N#12P#10703FAnyway, in the Old Town\x01",
            "The enemy's civil servants\x01",
            "It does not seem to have come out … ….\x02\x03",
            "#10702FLeave it to them here\x01",
            "It sounds fine.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_8866")


    ChrTalk(
        0x101,
        "#6P#00000FOh, yes.\x02",
    )

    CloseMessageWindow()

    label("loc_8886")

    TurnDirection(0x17, 0x105, 500)

    ChrTalk(
        0x105,
        (
            "#12P#10404FBecause it is such a thing\x01",
            "We are going to go.\x02\x03",
            "#10400FFor a while now,\x01",
            "Can I be out please?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x105, 500)

    ChrTalk(
        0xA,
        "#11POh, leave it to me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PBe careful, Wadi!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#5PI do not understand it well somehow,\x01",
            "Please decide to Hide! It is!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetChrPos(0x0, 0, 0, 6160, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    ClearMapFlags(0x10000000)
    OP_93(0x15, 0x5A, 0x0)
    OP_93(0x17, 0x5A, 0x0)
    OP_93(0x16, 0x5A, 0x0)
    OP_93(0x9, 0x10E, 0x0)
    OP_93(0xB, 0x10E, 0x0)
    OP_93(0xA, 0x10E, 0x0)
    ClearChrFlags(0x15, 0x10)
    ClearChrFlags(0x17, 0x10)
    ClearChrFlags(0x16, 0x10)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0x9, 0x10)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0x15, 0xFF)
    OP_4C(0x16, 0xFF)
    OP_4C(0x17, 0xFF)
    SetScenarioFlags(0x1BE, 2)
    EventEnd(0x5)
    Return()

    # Function_34_7CD7 end

    SaveToFile()

Try(main)
