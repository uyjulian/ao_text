from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Abbas",                  # 1
        "Liang",                  # 2
        "Kientz",                 # 3
        "Veysset",                # 4
        "Azel",                   # 5
        "Ashley",                 # 6
        "Sarina",                 # 7
        "Hugott",                 # 8
        "Citizen",                # 9
        "Citizen",                # 10
        "Blond Young Man",        # 11
        "Citizen",                # 12
        "Citizen",                # 13
        "Luganov",                # 14
        "Kｷki",                  # 15
        "Dino",                   # 16
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
        "Function_7_1CBF",         # 07, 7
        "Function_8_2226",         # 08, 8
        "Function_9_2370",         # 09, 9
        "Function_10_2508",        # 0A, 10
        "Function_11_36A0",        # 0B, 11
        "Function_12_37B7",        # 0C, 12
        "Function_13_388A",        # 0D, 13
        "Function_14_484F",        # 0E, 14
        "Function_15_486E",        # 0F, 15
        "Function_16_4A4B",        # 10, 16
        "Function_17_5817",        # 11, 17
        "Function_18_581B",        # 12, 18
        "Function_19_65ED",        # 13, 19
        "Function_20_6756",        # 14, 20
        "Function_21_6877",        # 15, 21
        "Function_22_6881",        # 16, 22
        "Function_23_69FC",        # 17, 23
        "Function_24_6B2D",        # 18, 24
        "Function_25_6C76",        # 19, 25
        "Function_26_6D48",        # 1A, 26
        "Function_27_6E5F",        # 1B, 27
        "Function_28_6ED5",        # 1C, 28
        "Function_29_6FFB",        # 1D, 29
        "Function_30_70D0",        # 1E, 30
        "Function_31_7181",        # 1F, 31
        "Function_32_72B9",        # 20, 32
        "Function_33_738D",        # 21, 33
        "Function_34_8485",        # 22, 34
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
    Jump("loc_1CBB")

    label("loc_C0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_C3C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C25")
    Jump("loc_C37")

    label("loc_C25")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C37")
    Jump("loc_C37")

    label("loc_C37")

    Jump("loc_1CBB")

    label("loc_C3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_CDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C57")
    Call(0, 7)
    Jump("loc_CDA")

    label("loc_C57")


    ChrTalk(
        0x8,
        (
            "#04100FWe plan to continue\x01",
            "our search for Wald.\x02\x03",
            "We'll contact you immediately if we\x01",
            "learn anything, so please wait for that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CDA")

    Jump("loc_1CBB")

    label("loc_CDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_D3F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CFA")
    Call(0, 8)
    Jump("loc_D3A")

    label("loc_CFA")


    ChrTalk(
        0x8,
        (
            "#04100FLet us take care of compiling\x01",
            "info related to Wald.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D3A")

    Jump("loc_1CBB")

    label("loc_D3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_DA4")

    ChrTalk(
        0x8,
        (
            "#04100F...It seems this\x01",
            "work is urgent.\x02\x03",
            "If you need anything, just say the word.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CBB")

    label("loc_DA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_108C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_100D")

    ChrTalk(
        0x8,
        (
            "#04100FIt seems the Vipers have\x01",
            "started to search for Wald.\x02\x03",
            "It seems he hasn't been seen\x01",
            "at all these past few days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301FNot even once, huh... I wonder\x01",
            "where he's and what he's doin'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10301F...You guys haven't\x01",
            "seen him either, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x105, 0)

    ChrTalk(
        0x8,
        (
            "#04100FYeah. Not at all this past week.\x02\x03",
            "Before then, he'd\x01",
            "show every so often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10308FI see...\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x8)

    ChrTalk(
        0x8,
        (
            "#04100F...Don't worry, Wazy.\x02\x03",
            "It's only been a few days\x01",
            "since he disappeared.\x02\x03",
            "And, we have nothing\x01",
            "else we have to do\x01",
            "right now, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FYeah... You're right.\x02\x03",
            "#10302FThanks, Abbas.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16E, 6)
    Jump("loc_1087")

    label("loc_100D")

    TurnDirection(0x8, 0x105, 0)

    ChrTalk(
        0x8,
        (
            "#04100FWe're concerned\x01",
            "about Wald too.\x02\x03",
            "And so, Wazy, don't worry needlessly,\x01",
            "and focus on your current work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1087")

    Jump("loc_1CBB")

    label("loc_108C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_11D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10A7")
    Call(0, 9)
    Jump("loc_11CD")

    label("loc_10A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1169")
    TurnDirection(0x8, 0x105, 0)

    ChrTalk(
        0x8,
        (
            "#04100FWazy... So you came.\x02\x03",
            "If you want to relax in the store, just say\x01",
            "the word. We'll have you seated right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHu hu. \x01",
            "Thanks, Abbas.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x2D, 0x0)
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 1)
    Jump("loc_11CD")

    label("loc_1169")


    ChrTalk(
        0x8,
        (
            "#04100FIf you want to relax in the store, just say\x01",
            "the word. We'll have you seated right away.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11CD")

    Jump("loc_1CBB")

    label("loc_11D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_133F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12A5")

    ChrTalk(
        0x8,
        (
            "#04100F...Downtown has been relatively peaceful these days.\x02\x03",
            "And so, Wazy, don't worry\x01",
            "about this place and focus on\x01",
            "your Support Section work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FI will. Thanks, Abbas.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_133A")

    label("loc_12A5")


    ChrTalk(
        0x8,
        (
            "#04100F...Downtown has been relatively peaceful these days.\x02\x03",
            "And so, Wazy, don't worry\x01",
            "about this place and focus on\x01",
            "your Support Section work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_133A")

    Jump("loc_1CBB")

    label("loc_133F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_16B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1493")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_144B")

    ChrTalk(
        0x8,
        (
            "#04105FThat customer, could he be...\x02\x03",
            "#04102F...Hah, I don't believe it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F(W-Was that a smile?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305F(Yeah, that's rare for him...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F(Oh boy... Hu hu, just what\x01",
            "are you guys thinking\x01",
            "about Abbas?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_148E")

    label("loc_144B")


    ChrTalk(
        0x8,
        (
            "#04102FThat customer, could he be...\x01",
            "Hah, I don't believe it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_148E")

    Jump("loc_16AC")

    label("loc_1493")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1659")

    ChrTalk(
        0x8,
        "#04100F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FThinking about something, Abbas?\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x105, 0)

    ChrTalk(
        0x8,
        (
            "#04100FWazy, huh...\x02\x03",
            "...Yeah. I was just thinking there are\x01",
            "all kinds of people in this world.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309FHa ha, you said it.\x02\x03",
            "#10304FWe're among them\x01",
            "too, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#04102FHah... Damn straight.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(This man...\x01",
            "He speaks quite a bit with Wazy.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F(*giggle*, that's probably\x01",
            "because they're very close.)\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 0)
    Jump("loc_16AC")

    label("loc_1659")


    ChrTalk(
        0x8,
        (
            "#04100F............\x02\x03",
            "...There's definitely all\x01",
            "kinds of people in this world.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16AC")

    Jump("loc_1CBB")

    label("loc_16B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1800")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17A9")

    ChrTalk(
        0x8,
        (
            "#04100FIt looks like there's many\x01",
            "officers patrolling Downtown.\x02\x03",
            "You're not hindering the Support \x01",
            "Section's work, are you Wazy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FWell, there's no special\x01",
            "problems right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#04100FI see. Good then.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17FB")

    label("loc_17A9")


    ChrTalk(
        0x8,
        (
            "#04100FIt seems several officers\x01",
            "have come to Downtown.\x02\x03",
            "...How troublesome.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17FB")

    Jump("loc_1CBB")

    label("loc_1800")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_END)), "loc_198F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1948")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x105, 0)

    ChrTalk(
        0x8,
        (
            "#04100FWazy, are you all right?\x01",
            "You look a little pale.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FYeah, I'm fine.\x01",
            "No need to worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#04100F...I see. Understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F(These two... They're strangely\x01",
            "casual with each other.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F(Yes, but they have a weird\x01",
            "way of communicating.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_198A")

    label("loc_1948")

    TurnDirection(0x8, 0x105, 0)

    ChrTalk(
        0x8,
        (
            "#04100FWazy, if you need our\x01",
            "help, just say the word.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_198A")

    Jump("loc_1CBB")

    label("loc_198F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1A8F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A40")

    ChrTalk(
        0x8,
        (
            "#04100FIf you have an\x01",
            "order, I'll take it.\x02\x03",
            "Please feel free to ask.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(Feel free with this guy, huh...\x01",
            "That seems difficult somehow.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A8A")

    label("loc_1A40")


    ChrTalk(
        0x8,
        (
            "#04100FIf you have an\x01",
            "order, I'll take it.\x02\x03",
            "Please feel free to ask.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A8A")

    Jump("loc_1CBB")

    label("loc_1A8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1CBB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C58")

    ChrTalk(
        0x8,
        (
            "#04100FWazy, leave everything\x01",
            "about the Testaments to me.\x02\x03",
            "You should do what\x01",
            "you want to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FYeah, I will.\x02\x03",
            "#10304FI'll be stopping by Trinity every \x01",
            "now and then, but do your best\x01",
            "with managing the place.\x02\x03",
            "#10302FHu hu. If it goes under,\x01",
            "there'll be fewer cozy places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#04102FYes, I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F(These two have a strange relationship...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100F(What kind of past do they have, I wonder.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1CBB")

    label("loc_1C58")


    ChrTalk(
        0x8,
        (
            "#04100FWazy, leave everything\x01",
            "about the Testaments to me.\x02\x03",
            "You should do what\x01",
            "you want to do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CBB")

    TalkEnd(0xFE)
    Return()

    # Function_6_BF9 end

    def Function_7_1CBF(): pass

    label("Function_7_1CBF")

    OP_4B(0x8, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FF3")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x105, 0)
    Sleep(1000)
    TurnDirection(0xB, 0x105, 0)
    TurnDirection(0xA, 0x105, 0)

    ChrTalk(
        0x8,
        (
            "#04100FWazy... It seems\x01",
            "things are turning\x01",
            "for the worse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Actually, Veysset and I saw a\x01",
            "redheaded man this morning...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E0B")
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#10108FI knew it... \x01",
            "He came to Downtown.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E0B")


    ChrTalk(
        0xB,
        (
            "How to say this... F-From his expression,\x01",
            "he looked worried about something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I think we saw him by\x01",
            "the exchange shop, but\x01",
            "he left immediately...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "D-Did something happen?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FYeah, a little something.\x02\x03",
            "#10300FBut this is a Support\x01",
            "Section matter. There's no\x01",
            "need for you all to worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04100F...I see.\x02\x03",
            "However, if you ever need\x01",
            "our help, just say the word.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FYeah, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F(Just you wait, Randy. \x01",
            "We'll definitely catch you...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16E, 2)
    Jump("loc_2204")

    label("loc_1FF3")


    ChrTalk(
        0x105,
        (
            "#10300FBy the way Abbas... Did you\x01",
            "gather any info regarding Wald?\x02",
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
            "#04100FNo... We haven't been\x01",
            "able to get any promising\x01",
            "info as of yet.\x02\x03",
            "Most likely he's trying to\x01",
            "stay hidden. There's hardly\x01",
            "any sightings of him.\x02\x03",
            "It's honestly hard for me to think\x01",
            "of any way he could get that drug.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10303F...I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04100FBut even so, we plan to\x01",
            "continue our investigation.\x02\x03",
            "We'll contact you immediately if we\x01",
            "learn anything, so please wait for that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FYeah, got it.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x16E, 1)

    label("loc_2204")

    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0x8, 0xFF)
    OP_93(0xA, 0x5A, 0x0)
    OP_93(0xB, 0x0, 0x0)
    OP_93(0x8, 0xE1, 0x0)
    Return()

    # Function_7_1CBF end

    def Function_8_2226(): pass

    label("Function_8_2226")

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
            "#04100FWazy, huh... \x01",
            "Leave gathering intel\x01",
            "on Wald to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "O-Once our plan is complete,\x01",
            "we'll look for clues right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "So Wazy, focus on your\x01",
            "Support Section work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FThanks. I'm counting on you.\x02",
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

    # Function_8_2226 end

    def Function_9_2370(): pass

    label("Function_9_2370")

    OP_4B(0x8, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xD,
        (
            "This store seems to be\x01",
            "thriving lately, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "I'm so jealous... Feel free\x01",
            "to give me a share, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04102FHmph, you're not doing so\x01",
            "bad yourself, are you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Well, I won't deny it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F(Those two look like they're having fun.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F(Hu hu. They're both oddballs,\x01",
            "so they think alike.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211F(...On that note, I think\x01",
            "you're one too, Mr. Wazy.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 6)
    OP_4C(0xD, 0xFF)
    OP_4C(0x8, 0xFF)
    ClearChrFlags(0xD, 0x10)
    Return()

    # Function_9_2370 end

    def Function_10_2508(): pass

    label("Function_10_2508")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2654")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25E5")

    ChrTalk(
        0xFE,
        (
            "A large number of\x01",
            "patients were sent to\x01",
            "St. Ursula Hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I managed to contact my father,\x01",
            "but it seems he was somehow\x01",
            "busy doing the rounds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...I've got to do my best, too.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_264F")

    label("loc_25E5")


    ChrTalk(
        0xFE,
        (
            "I don't know if I'll be able to\x01",
            "follow my father's path, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...I've got to do my best, too.\x02",
    )

    CloseMessageWindow()

    label("loc_264F")

    Jump("loc_369C")

    label("loc_2654")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2761")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26FE")

    ChrTalk(
        0xFE,
        (
            "I've got to prioritize the safety\x01",
            "of the neighborhood citizens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just in case, I think\x01",
            "it's a good idea to check\x01",
            "on East Street as well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_275C")

    label("loc_26FE")


    ChrTalk(
        0xFE,
        (
            "We'll somehow try to\x01",
            "do something here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You guys too, come\x01",
            "back safely in some way.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_275C")

    Jump("loc_369C")

    label("loc_2761")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2A91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29BD")

    ChrTalk(
        0xFE,
        (
            "This morning, Abbas gathered everyone\x01",
            "and said "For the time being, take care\x01",
            "of Trinity" and went off somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He didn't tell us where he was going.\x01",
            "I wonder if something happened...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FAbbas said that...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FMaybe he's\x01",
            "with Wazy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We don't know. Those State\x01",
            "Guard or whatever are\x01",
            "wandering the town, see...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "C-Could they have been arrested?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201FI can't think they would\x01",
            "make such a blunder, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FHmm... Well anyway, \x01",
            "you should calm down.\x01",
            "Don't you think so?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Yeah. Anyway, we've got\x01",
            "to protect the store...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2A8C")

    label("loc_29BD")


    ChrTalk(
        0xFE,
        (
            "Though I'm worried about Wazy and\x01",
            "Abbas... I wonder if my father at\x01",
            "St. Ursula Hospital is all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure my father is treating patients even in\x01",
            "this situation, because that's just who he is.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A8C")

    Jump("loc_369C")

    label("loc_2A91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2A9F")
    Jump("loc_369C")

    label("loc_2A9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2B5B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2ABA")
    Call(0, 7)
    Jump("loc_2B56")

    label("loc_2ABA")


    ChrTalk(
        0xFE,
        (
            "Even so... That redhead had\x01",
            "a huge amount of luggage,\x01",
            "even though it was raining.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It looked heavy, but I was surprised\x01",
            "at how fast he was moving.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B56")

    Jump("loc_369C")

    label("loc_2B5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2C8F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B76")
    Call(0, 8)
    Jump("loc_2C8A")

    label("loc_2B76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C3F")

    ChrTalk(
        0xFE,
        (
            "Come to think of it, a\x01",
            "derailment occurred along West\x01",
            "Crossbell Highway yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems several people were severely wounded...\x01",
            "Looks like my father's going to be busy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2C8A")

    label("loc_2C3F")


    ChrTalk(
        0xFE,
        (
            "My father's amazing... We can rely\x01",
            "on him even at a time like this...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C8A")

    Jump("loc_369C")

    label("loc_2C8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2DA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D1E")

    ChrTalk(
        0xFE,
        "I... Just what do I want to be?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Damn. No matter how much I think\x01",
            "about it, the answer just won't come.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2D9C")

    label("loc_2D1E")


    ChrTalk(
        0xFE,
        (
            "Thinking back on it, I didn't\x01",
            "hate studying that much, did I...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I sit at a desk again,\x01",
            "I wonder what I'll see...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D9C")

    Jump("loc_369C")

    label("loc_2DA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2F41")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EBC")

    ChrTalk(
        0xFE,
        (
            "When I was small, I\x01",
            "thought I said I wanted to\x01",
            "be a doctor like my father...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But at some point, I realized\x01",
            "I'm not as smart as him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I can't even\x01",
            "put it into words.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*... It's because\x01",
            "I'm hesitant like this\x01",
            "that I'm half a man.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2F3C")

    label("loc_2EBC")


    ChrTalk(
        0xFE,
        (
            "Or rather, it's bad for\x01",
            "a waiter to be hesitant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They pay a salary here, so I've got\x01",
            "to focus on being a good waiter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F3C")

    Jump("loc_369C")

    label("loc_2F41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_316D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30EA")

    ChrTalk(
        0xFE,
        (
            "How to say this... \x01",
            "Everyone's been lively lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if it's just me who\x01",
            "feels that I'm half a man...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*... What\x01",
            "ever shall I do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F(Wazy... You're not\x01",
            "going to say anything?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304F(Yeah. Since in the past, each of the\x01",
            "Testaments have been independent.)\x02\x03",
            "#10300F(It's not my place\x01",
            "to interfere.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211F(...Somehow, that reminds\x01",
            "me of Chief Sergei.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3168")

    label("loc_30EA")


    ChrTalk(
        0xFE,
        (
            "Everyone's been lively lately. I wonder if\x01",
            "it's just me who feels I'm half a man...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*... What\x01",
            "ever shall I do?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3168")

    Jump("loc_369C")

    label("loc_316D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_32B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_326C")

    ChrTalk(
        0xFE,
        (
            "This morning, some Vipers\x01",
            "came to fight using a bump on\x01",
            "the shoulder as an excuse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But when we honestly\x01",
            "apologized, they\x01",
            "awkwardly withdrew.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's an approach we\x01",
            "learned from Abbas. \x01",
            "It was surprisingly effective.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_32B0")

    label("loc_326C")


    ChrTalk(
        0xFE,
        (
            "A peaceful approach, huh...\x01",
            "We have a lot to\x01",
            "learn from Abbas.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32B0")

    Jump("loc_369C")

    label("loc_32B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3469")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_334B")

    ChrTalk(
        0xFE,
        "A-Amazing. That blond customer...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After he suddenly showed us\x01",
            "his performance, he tore us\x01",
            "to shreds at billiards...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3464")

    label("loc_334B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33FD")

    ChrTalk(
        0xFE,
        (
            "S-Somehow, it was a\x01",
            "little noisy outside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Could it be because of that customer just now...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Well, whatever. \x01",
            "It's best not to worry about it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3464")

    label("loc_33FD")


    ChrTalk(
        0xFE,
        "Could it be because of that customer just now...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...Well, whatever. I won't worry about it.\x02",
    )

    CloseMessageWindow()

    label("loc_3464")

    Jump("loc_369C")

    label("loc_3469")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_34A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3484")
    Call(0, 11)
    Jump("loc_34A3")

    label("loc_3484")


    ChrTalk(
        0xFE,
        "This way then, customers.\x02",
    )

    CloseMessageWindow()

    label("loc_34A3")

    Jump("loc_369C")

    label("loc_34A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3534")

    ChrTalk(
        0xFE,
        (
            "*sigh*. No matter what I do,\x01",
            "my mood sinks on rainy days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My hair's a mess when it gets wet...\x01",
            "I hope it ends soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_369C")

    label("loc_3534")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_369C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3629")

    ChrTalk(
        0xFE,
        "I'm not especially suited for waiting tables, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There were no other roles for me, so I\x01",
            "had no choice but to take up waiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But even so, now that I've taken it up,\x01",
            "I can only make a proper effort.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_369C")

    label("loc_3629")


    ChrTalk(
        0xFE,
        (
            "Welcome. If you'd like a seat,\x01",
            "I'd be happy to show you to one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "That's what a waiter does, more or less.\x02",
    )

    CloseMessageWindow()

    label("loc_369C")

    TalkEnd(0xFE)
    Return()

    # Function_10_2508 end

    def Function_11_36A0(): pass

    label("Function_11_36A0")

    OP_4B(0xA, 0xFF)
    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)

    ChrTalk(
        0xA,
        "Um, there's two of you, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We have counter and table seats.\x01",
            "Which would you prefer?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "Hmm... We don't come here\x01",
            "so often, so should we go\x01",
            "with counter seats?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "Yeah, let's do it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Understood. \x01",
            "Right this way, please.\x02",
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

    # Function_11_36A0 end

    def Function_12_37B7(): pass

    label("Function_12_37B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3880")
    TalkBegin(0xB)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_37D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_387C")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3827")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3827")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3847")
    OP_AF(0xB3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3877")

    label("loc_3847")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_385B")
    Jump("loc_3877")

    label("loc_385B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3877")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 13)

    label("loc_3877")

    Jump("loc_37D7")

    label("loc_387C")

    TalkEnd(0xB)
    Return()

    label("loc_3880")

    TalkBegin(0xB)
    Call(0, 13)
    TalkEnd(0xB)
    Return()

    # Function_12_37B7 end

    def Function_13_388A(): pass

    label("Function_13_388A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3B34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A94")

    ChrTalk(
        0xB,
        (
            "Even so... That's surprising. Who knew\x01",
            "Wazy and Abbas were Church officials?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3A37")

    ChrTalk(
        0xB,
        (
            "S-Somehow, they suddenly\x01",
            "seem so far away from us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10402FHu hu. We actually haven't changed at all.\x01",
            "I'd like you to treat us like you usually do.\x02\x03",
            "#10404FYou could say the "Wazy Hemisphere"\x01",
            "who ran the "Testaments" with you\x01",
            "is the real me as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I-I see... I'm happy\x01",
            "to hear you say that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A8C")

    label("loc_3A37")


    ChrTalk(
        0xB,
        (
            "Up until now, you never acted like it.\x01",
            "H-Honestly, I can't even believe it now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A8C")

    SetScenarioFlags(0x0, 3)
    Jump("loc_3B2F")

    label("loc_3A94")


    ChrTalk(
        0xB,
        (
            "T-To think Wazy and Abbas were\x01",
            "Church officials this whole time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Up until now, you never acted like it.\x01",
            "H-Honestly, I can't even believe it now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B2F")

    Jump("loc_484E")

    label("loc_3B34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3C19")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BC1")

    ChrTalk(
        0xB,
        (
            "It's best to\x01",
            "avoid confronting\x01",
            "those monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "They're not attacking us, so\x01",
            "it's best to leave them alone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C14")

    label("loc_3BC1")


    ChrTalk(
        0xB,
        (
            "Azel went back to East Street\x01",
            "to be with his family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I-I hope he's safe.\x02",
    )

    CloseMessageWindow()

    label("loc_3C14")

    Jump("loc_484E")

    label("loc_3C19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3CA7")

    ChrTalk(
        0xB,
        (
            "Abbas too... H-He must have\x01",
            "some circumstances, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "For now, we've got to protect\x01",
            "the store, just like he ordered.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_484E")

    label("loc_3CA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3CB5")
    Jump("loc_484E")

    label("loc_3CB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3D6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CD0")
    Call(0, 7)
    Jump("loc_3D69")

    label("loc_3CD0")


    ChrTalk(
        0xB,
        (
            "H-His expression... Somehow, there\x01",
            "was an amazing intensity to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "T-Thinking back on it, it\x01",
            "was frightening... Honestly,\x01",
            "I was really scared.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D69")

    Jump("loc_484E")

    label("loc_3D6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3E02")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D89")
    Call(0, 8)
    Jump("loc_3DFD")

    label("loc_3D89")


    ChrTalk(
        0xB,
        (
            "We plan to go around to\x01",
            "gather many information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I hope we're able to find where\x01",
            "that Gnosis came from...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DFD")

    Jump("loc_484E")

    label("loc_3E02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3FCE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F7B")

    ChrTalk(
        0xB,
        "T-This cocktail is a bomb.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "A bold idea brought forth\x01",
            "an unprecedented invention.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "But... Maybe it was a little\x01",
            "beyond what I can do. \x01",
            "...It seems I don't have the talent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "And so... I-I'll stop\x01",
            "making cocktails.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "My final work... \x01",
            "G-Get rid of it for me.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x1D7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x1D7, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x17C, 5)
    Jump("loc_3FC9")

    label("loc_3F7B")


    ChrTalk(
        0xB,
        "I-I'll stop making cocktails.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "...I don't want to become a murderer.\x02",
    )

    CloseMessageWindow()

    label("loc_3FC9")

    Jump("loc_484E")

    label("loc_3FCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_41DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4147")

    ChrTalk(
        0xB,
        (
            "M-Miss Ashley bought\x01",
            "a great many of\x01",
            "my cocktails.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "T-The taste and appearance aside, she praised\x01",
            "their ability to be used on the battlefield.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Hm...? D-Did she praise me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "A-Anyway...\x01",
            "Miss Ashley approves\x01",
            "of my cocktails.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I-If you like, please take one.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1D4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x1D4, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x17C, 4)
    Jump("loc_41D7")

    label("loc_4147")


    ChrTalk(
        0xB,
        (
            "My cocktails can be used on the battlefield...\x01",
            "I-In other words, they're just that nutritious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It smells, but...\x01",
            "J-Just gulp it down.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41D7")

    Jump("loc_484E")

    label("loc_41DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_43FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4366")

    ChrTalk(
        0xB,
        (
            "A-Azel and Liang are\x01",
            "always enjoying themselves\x01",
            "researching cocktails.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "T-That's why I tried\x01",
            "to make one too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hmph, they said it looked bad so\x01",
            "we can't sell it, but... I'm sure\x01",
            "its ingredients are good for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I-If you like, please take it.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1D1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x1D1, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00005FS-Sure... Thank you.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16E, 3)
    Jump("loc_43FA")

    label("loc_4366")


    ChrTalk(
        0xB,
        (
            "I have absolute confidence\x01",
            "in my cocktail ingredients. \x01",
            "I-I'm sure it's good for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It does look like that, but...\x01",
            "J-Just gulp it down.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43FA")

    Jump("loc_484E")

    label("loc_43FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4579")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4514")

    ChrTalk(
        0xB,
        (
            "I-I left with Kientz to\x01",
            "restock this morning, and\x01",
            "we came across some Vipers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "They got angry without\x01",
            "thinking, but Kientz\x01",
            "was able to stop them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I couldn't believe a technique like\x01",
            "that got the Vipers to withdraw... \x01",
            "What a discovery!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4574")

    label("loc_4514")


    ChrTalk(
        0xB,
        (
            "W-We won't fight\x01",
            "needlessly anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I-If I get a bruise, I\x01",
            "can't work here, you see.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4574")

    Jump("loc_484E")

    label("loc_4579")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_463A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45E1")

    ChrTalk(
        0xB,
        "Damn, even Liang...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "That blond man with a\x01",
            "white coat... What courage.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4635")

    label("loc_45E1")


    ChrTalk(
        0xB,
        (
            "That blond man with a white coat...\x01",
            "That customer was almost like a whirlwind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4635")

    Jump("loc_484E")

    label("loc_463A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_46CF")

    ChrTalk(
        0xB,
        (
            "L-Luckily we're having\x01",
            "more customers lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It's just, perhaps due to lack of public\x01",
            "order, we don't get so many at night.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_484E")

    label("loc_46CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_47CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_476B")

    ChrTalk(
        0xB,
        (
            "After I serve you, you can\x01",
            "play billiards all you want.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "H-However, the condition is that\x01",
            "you order at least one drink.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_47C6")

    label("loc_476B")


    ChrTalk(
        0xB,
        (
            "You can play billiards\x01",
            "all you want.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "It's limited to bar customers only, though.\x02",
    )

    CloseMessageWindow()

    label("loc_47C6")

    Jump("loc_484E")

    label("loc_47CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_484E")

    ChrTalk(
        0xB,
        (
            "I'm in charge as\x01",
            "billiards instructor\x01",
            "and scorer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you don't know how to hit the\x01",
            "ball or the rules, just ask.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_484E")

    Return()

    # Function_13_388A end

    def Function_14_484F(): pass

    label("Function_14_484F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_486A")
    Call(0, 12)
    Jump("loc_486D")

    label("loc_486A")

    Call(0, 15)

    label("loc_486D")

    Return()

    # Function_14_484F end

    def Function_15_486E(): pass

    label("Function_15_486E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4978")
    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48C9")

    ChrTalk(
        0x9,
        (
            "Ah, if Wazy or Abbas were\x01",
            "here at a time like this...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4974")

    label("loc_48C9")


    ChrTalk(
        0x9,
        (
            "So the day's finally come for us to\x01",
            "cooperate with the Vipers, has it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, we understand their\x01",
            "strength better than anyone. \x01",
            "I couldn't ask for better allies.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4974")

    TalkEnd(0x9)
    Return()

    label("loc_4978")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4995")
    TalkBegin(0x9)
    Call(0, 22)
    TalkEnd(0x9)
    Return()

    label("loc_4995")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_49A2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A47")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_49F2")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_49F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A12")
    OP_AF(0xB3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4A42")

    label("loc_4A12")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A26")
    Jump("loc_4A42")

    label("loc_4A26")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A42")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 16)

    label("loc_4A42")

    Jump("loc_49A2")

    label("loc_4A47")

    TalkEnd(0x9)
    Return()

    # Function_15_486E end

    def Function_16_4A4B(): pass

    label("Function_16_4A4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4B6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B1D")

    ChrTalk(
        0x9,
        (
            "It sometimes happens\x01",
            "that Abbas disappears\x01",
            "for awhile, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "This time, I feel like his\x01",
            "expression was more serious\x01",
            "and grave than usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...I hope he\x01",
            "gets back soon.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4B65")

    label("loc_4B1D")


    ChrTalk(
        0x9,
        (
            "I wonder how long\x01",
            "he'll be gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...I hope he\x01",
            "gets back soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B65")

    Jump("loc_5816")

    label("loc_4B6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4E71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C04")

    ChrTalk(
        0x9,
        (
            "I'm making special\x01",
            "drinks for the people\x01",
            "hard at work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Everyone drinks a lot, you know.\x01",
            "The mixer's running full speed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E6C")

    label("loc_4C04")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D73")

    ChrTalk(
        0x9,
        (
            "You're helping with reconstruction\x01",
            "too, right Support Section?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Take these. My special\x01",
            "drinks for everyone,\x01",
            "on the house.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x1CF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x6 obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x1CF, 6)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00005FYou're giving us this many?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHu hu, it's enough for all\x01",
            "of us. Thanks, Liang.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Ha ha, you're welcome.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18D, 4)
    Jump("loc_4DE1")

    label("loc_4D73")


    ChrTalk(
        0x9,
        (
            "Thanks for helping with\x01",
            "the reconstruction work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Uh uh, that's the Special Support Section for you.\x02",
    )

    CloseMessageWindow()

    label("loc_4DE1")

    Jump("loc_4E6C")

    label("loc_4DE6")


    ChrTalk(
        0x9,
        (
            "Looks like the pork miso Azel\x01",
            "and the others made was a hit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It's weird to say it, but that\x01",
            "emergency food warmed my heart.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E6C")

    Jump("loc_5816")

    label("loc_4E71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5019")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F87")

    ChrTalk(
        0x9,
        (
            "Looks like they're saying\x01",
            "the Mainz occupation could\x01",
            "be an Imperial plot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I also heard the incident could\x01",
            "be a pretext for stationing\x01",
            "Imperial troops in Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If those rumors were true,\x01",
            "by no means that's\x01",
            "something we can allow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5014")

    label("loc_4F87")


    ChrTalk(
        0x9,
        (
            "If it's true that the Imperial\x01",
            "government caused this occupation\x01",
            "for political motives...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "By no means it's\x01",
            "something we can allow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5014")

    Jump("loc_5816")

    label("loc_5019")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5076")

    ChrTalk(
        0x9,
        (
            "Wald... I wonder\x01",
            "what he's doing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "It wasn't alcohol... But a drug...\x02",
    )

    CloseMessageWindow()
    Jump("loc_5816")

    label("loc_5076")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_51A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50FF")

    ChrTalk(
        0x9,
        (
            "Looks like those\x01",
            "customers love\x01",
            "our soup pasta.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Uh uh. That's Abbas' special\x01",
            "secret recipe for you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_51A1")

    label("loc_50FF")


    ChrTalk(
        0x9,
        (
            "It must be a wonderful thing\x01",
            "to make people smile with\x01",
            "something you yourself made.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Cooking is rather difficult, but I\x01",
            "feel like it's totally rewarded.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51A1")

    Jump("loc_5816")

    label("loc_51A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5374")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52CE")

    ChrTalk(
        0x9,
        (
            "Two Vipers came\x01",
            "in yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "They were extremely\x01",
            "threatening. I thought they\x01",
            "came here to pick a fight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "They were just trying to save face,\x01",
            "coming here to ask about Wald.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The underlings are that worried about him.\x01",
            "Wald... I wonder what he's doing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_536F")

    label("loc_52CE")


    ChrTalk(
        0x9,
        (
            "Though we were enemies before,\x01",
            "I thought he had some sides of \x01",
            "him I could respect a bit, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "To put it bluntly, now Wald\x01",
            "is a failure of a leader.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_536F")

    Jump("loc_5816")

    label("loc_5374")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_541F")

    ChrTalk(
        0x9,
        (
            "Veysset put something\x01",
            "suspicious in the shaker. \x01",
            "I wonder if he'll be all right...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If he had consulted with me,\x01",
            "I could've given him some advice.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5816")

    label("loc_541F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5588")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54E8")

    ChrTalk(
        0x9,
        "Hey, welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I recommend our daily special, a bowl\x01",
            "filled with fresh, seasonal ingredients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We have a lunch menu too, so please\x01",
            "feel free to ask me about it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5583")

    label("loc_54E8")


    ChrTalk(
        0x9,
        (
            "I recommend our daily special, a bowl\x01",
            "filled with fresh, seasonal ingredients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We have a lunch menu too, so please\x01",
            "feel free to ask me about it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5583")

    Jump("loc_5816")

    label("loc_5588")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_564D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55A0")
    Jump("loc_5648")

    label("loc_55A0")


    ChrTalk(
        0x9,
        (
            "In the end, the match with that\x01",
            "customer wasn't finished, but...\x01",
            "To put it bluntly, I failed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            ""In this world, there is always \x01",
            "someone  better than you", eh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5648")

    Jump("loc_5816")

    label("loc_564D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_56CC")

    ChrTalk(
        0x9,
        (
            "Ha ha, Azel's sister\x01",
            "is such a worrywart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "But watching the exchange of\x01",
            "those two is somehow enjoyable.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5816")

    label("loc_56CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5765")

    ChrTalk(
        0x9,
        (
            "Man... Even just stocking one\x01",
            "thing is hard in this rain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I've got mud stains everywhere,\x01",
            "so I'll have to change before cooking.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5816")

    label("loc_5765")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5816")

    ChrTalk(
        0x9,
        (
            "Hey, welcome. Let me know\x01",
            "if you'd like to order.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Whether it's a cocktail or snacks, I'd be\x01",
            "happy to show you plenty of the skills\x01",
            "I've inherited from Abbas.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5816")

    Return()

    # Function_16_4A4B end

    def Function_17_5817(): pass

    label("Function_17_5817")

    Call(0, 18)
    Return()

    # Function_17_5817 end

    def Function_18_581B(): pass

    label("Function_18_581B")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5A57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59CB")

    ChrTalk(
        0xC,
        ""Trinity" too has resumed operation.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Although we're in such a situation,\x01",
            "it's important to spend\x01",
            "days normally like this.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_597A")

    ChrTalk(
        0x105,
        (
            "#10400FHu hu, well do your best, ok? There are\x01",
            "people who enjoy coming to the store\x01",
            "even in times like these, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Yeah, of course. You do\x01",
            "your best too, Wazy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_59C3")

    label("loc_597A")


    ChrTalk(
        0xC,
        (
            "My sister and Hugott\x01",
            "are rooting for me, so\x01",
            "I've got to do my best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59C3")

    SetScenarioFlags(0x0, 5)
    Jump("loc_5A52")

    label("loc_59CB")


    ChrTalk(
        0xC,
        (
            ""Trinity" too has resumed\x01",
            "operation. Feel free to order.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "My sister and Hugott\x01",
            "are rooting for me, so\x01",
            "I've got to do my best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A52")

    Jump("loc_65E9")

    label("loc_5A57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5A65")
    Jump("loc_65E9")

    label("loc_5A65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5B06")

    ChrTalk(
        0xC,
        (
            "It's noisy in town. I wonder\x01",
            "what the declaration of\x01",
            "independence will mean...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...I think I'll go home to\x01",
            "check on my sister and Hugott.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65E9")

    label("loc_5B06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5B14")
    Jump("loc_65E9")

    label("loc_5B14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5C88")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BFC")

    ChrTalk(
        0xC,
        (
            "The mysterious force that attacked\x01",
            "Mainz seem terribly formidable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It seems like the CGF are having a\x01",
            "tough time dealing with them too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...Anyway, I hope the\x01",
            "situation's resolved quickly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5C83")

    label("loc_5BFC")


    ChrTalk(
        0xC,
        (
            "In times like these, I get\x01",
            "worried about my family\x01",
            "for some unknown reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I think I'll go check on\x01",
            "things at home later...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C83")

    Jump("loc_65E9")

    label("loc_5C88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5D29")

    ChrTalk(
        0xC,
        (
            "They say Wald might have taken the \x01",
            "same drug that newbie Dino did, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Even though he's in a rival group,\x01",
            "I'm still worried about him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65E9")

    label("loc_5D29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5EE5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E27")

    ChrTalk(
        0xC,
        "*sigh*, it's already past noon, huh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Come to think of it, my sister said\x01",
            "she had work today too. I wonder if\x01",
            "she's overdoing it again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I told her she doesn't have\x01",
            "to work as much because \x01",
            "I'm working too, but...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5EE0")

    label("loc_5E27")


    ChrTalk(
        0xC,
        (
            "Come to think of it, my sister said\x01",
            "she had work today too. I wonder if\x01",
            "she's overdoing it again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I told her she doesn't have\x01",
            "to work as much because \x01",
            "I'm working too, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5EE0")

    Jump("loc_65E9")

    label("loc_5EE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_60CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6010")

    ChrTalk(
        0xC,
        (
            "That Kientz. It looks like\x01",
            "he's been worried about his\x01",
            "future this whole time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "He has a good head, and on top\x01",
            "of that, his parents are rich.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If he felt like, he could\x01",
            "be whatever he wants...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "How to say it... Everyone is\x01",
            "worried about different things.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_60CA")

    label("loc_6010")


    ChrTalk(
        0xC,
        (
            "I think I remember\x01",
            "Kientz once said he\x01",
            "had a father complex.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Even if he works hard and becomes\x01",
            "a doctor, he'll never surpass his father\x01",
            "so there's no meaning in it, he said...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60CA")

    Jump("loc_65E9")

    label("loc_60CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6149")

    ChrTalk(
        0xC,
        (
            "Abbas has a wealth of expert\x01",
            "knowledge from many fields.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "I'm always learning new things from him.\x02",
    )

    CloseMessageWindow()
    Jump("loc_65E9")

    label("loc_6149")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_61E3")

    ChrTalk(
        0xC,
        "I've been enjoying work lately for some reason.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "For some reason, I feel like it'll be all\x01",
            "right if I work here forever like this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65E9")

    label("loc_61E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_62FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6289")

    ChrTalk(
        0xC,
        (
            "That customer in the white\x01",
            "coat suddenly challenged\x01",
            "us to billiards.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "In the end, only Liang was left\x01",
            "standing. The rest of us lost.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62F8")

    label("loc_6289")


    ChrTalk(
        0xC,
        (
            "But... That customer\x01",
            "was really an oddball.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "How to say it... I can't help\x01",
            "wanting to talk to people.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62F8")

    Jump("loc_65E9")

    label("loc_62FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6387")

    ChrTalk(
        0xC,
        (
            "*sigh*, my sister suddenly\x01",
            "came in for no reason...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...Well, whatever. Right now,\x01",
            "I've just got to focus on work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65E9")

    label("loc_6387")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_641A")

    ChrTalk(
        0xC,
        (
            "Liang's teaching me,\x01",
            "and lets me make the\x01",
            "cocktails sometimes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Though making cocktails\x01",
            "is complex and\x01",
            "difficult, it's fun.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65E9")

    label("loc_641A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_65E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6574")

    ChrTalk(
        0xC,
        (
            "When Wazy joined the Special\x01",
            "Support Section, the group\x01",
            "discussed things, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "For the time being, we all\x01",
            "decided to cooperate and\x01",
            "help operate "Trinity".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Originally, this store was\x01",
            "just our group's meeting\x01",
            "place. Abbas ran the place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "From here on, we plan to attract\x01",
            "more customers and business.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_65E9")

    label("loc_6574")


    ChrTalk(
        0xC,
        "Please continue to come to Trinity.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "We have an extensive selection. \x01",
            "Feel free to order only food as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_65E9")

    TalkEnd(0xC)
    Return()

    # Function_18_581B end

    def Function_19_65ED(): pass

    label("Function_19_65ED")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_668B")

    ChrTalk(
        0xFE,
        (
            "This soup pasta is earth-\x01",
            "shatteringly delicious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This goes above the level of\x01",
            "bar a-la-carte service to be\x01",
            "quite honest with you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6752")

    label("loc_668B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_66E8")

    ChrTalk(
        0xFE,
        "Did something happen to the waiter?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "He looks absent minded, somehow.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6752")

    label("loc_66E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6752")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6703")
    Call(0, 11)
    Jump("loc_6752")

    label("loc_6703")


    ChrTalk(
        0xFE,
        (
            "I heard about this place through word\x01",
            "of mouth. It has a nice atmosphere.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6752")

    TalkEnd(0xFE)
    Return()

    # Function_19_65ED end

    def Function_20_6756(): pass

    label("Function_20_6756")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_67A9")

    ChrTalk(
        0xFE,
        (
            "Uh uh, these penne's texture is\x01",
            "irresistible! I'm so happy㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6873")

    label("loc_67A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6818")

    ChrTalk(
        0xFE,
        (
            "Uh uh. I've come\x01",
            "here once again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As always, it has a fashionable\x01",
            "and nice atmosphere.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6873")

    label("loc_6818")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6873")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6833")
    Call(0, 11)
    Jump("loc_6873")

    label("loc_6833")


    ChrTalk(
        0xFE,
        (
            "Eeh, to think there was\x01",
            "such a store in a place like this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6873")

    TalkEnd(0xFE)
    Return()

    # Function_20_6756 end

    def Function_21_6877(): pass

    label("Function_21_6877")

    TalkBegin(0xFE)
    Call(0, 22)
    TalkEnd(0xFE)
    Return()

    # Function_21_6877 end

    def Function_22_6881(): pass

    label("Function_22_6881")

    OP_4B(0x12, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_93(0x9, 0x5A, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6991")

    ChrTalk(
        0x12,
        (
            "Ha ha ha, young man. \x01",
            "I see it's the end of the road for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "...You're pretty good, mister...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You're on the same level as Wazy...\x01",
            "No, maybe you're even better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305F(...Hmm? It looks like he\x01",
            "has considerable skill.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_69F0")

    label("loc_6991")


    ChrTalk(
        0x12,
        "Come, it's your turn next.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "S-Sure... Wait a\x01",
            "moment, I'm thinking\x01",
            "about where to aim.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69F0")

    OP_4C(0x12, 0xFF)
    OP_4C(0x9, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_22_6881 end

    def Function_23_69FC(): pass

    label("Function_23_69FC")

    OP_4B(0x13, 0xFF)
    OP_4B(0x14, 0xFF)
    OP_4B(0x12, 0xFF)

    ChrTalk(
        0x14,
        "Eek, amazing!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "Really. He's so cool㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Ha ha. "Aim" is the same\x01",
            "as confidence, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "Furthermore, what I'm aiming\x01",
            "for now is not just the ball,\x01",
            "but your hearts as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "Ahn! He's saying those things again㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "Uh uh, he's really good.\x02",
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

    # Function_23_69FC end

    def Function_24_6B2D(): pass

    label("Function_24_6B2D")


    ChrTalk(
        0x13,
        (
            "Aww. I can't believe\x01",
            "he'd leave so suddenly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "In this case, I should've asked\x01",
            "him where he's staying...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Hmm. He really did\x01",
            "have a nice face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "But, wasn't he\x01",
            "a bit strange?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Nonsense. So what if he\x01",
            "was a little strange.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "Also, he had a certain\x01",
            "charm about him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "Y-Yeah, you said it.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    SetScenarioFlags(0x1, 2)
    ClearChrFlags(0x13, 0x10)
    ClearChrFlags(0x14, 0x10)
    Return()

    # Function_24_6B2D end

    def Function_25_6C76(): pass

    label("Function_25_6C76")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CC1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C95")
    Call(0, 23)
    Jump("loc_6CBC")

    label("loc_6C95")


    ChrTalk(
        0xFE,
        (
            "Uhuhu. I met a\x01",
            "dreamy man today㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CBC")

    Jump("loc_6D44")

    label("loc_6CC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CD3")
    Call(0, 24)
    Jump("loc_6D44")

    label("loc_6CD3")


    ChrTalk(
        0xFE,
        (
            "Aww. I can't believe\x01",
            "he'd leave so suddenly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In this case, I should've asked\x01",
            "him where he's staying...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D44")

    TalkEnd(0xFE)
    Return()

    # Function_25_6C76 end

    def Function_26_6D48(): pass

    label("Function_26_6D48")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DBC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D67")
    Call(0, 23)
    Jump("loc_6DB7")

    label("loc_6D67")


    ChrTalk(
        0xFE,
        (
            "That man wasn't just good at playing\x01",
            "music, he was good at billiards, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DB7")

    Jump("loc_6E5B")

    label("loc_6DBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DCE")
    Call(0, 24)
    Jump("loc_6E5B")

    label("loc_6DCE")


    ChrTalk(
        0xFE,
        (
            "He had a nice face, his singing and playing\x01",
            "were good, and he was even good at billiards...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But somehow, I felt\x01",
            "like I know him...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E5B")

    TalkEnd(0xFE)
    Return()

    # Function_26_6D48 end

    def Function_27_6E5F(): pass

    label("Function_27_6E5F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E74")
    Call(0, 9)
    Jump("loc_6ED1")

    label("loc_6E74")


    ChrTalk(
        0xFE,
        (
            "Hehe. There's nothing better\x01",
            "than drinking during the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It penetrates the body.\x02",
    )

    CloseMessageWindow()

    label("loc_6ED1")

    TalkEnd(0xFE)
    Return()

    # Function_27_6E5F end

    def Function_28_6ED5(): pass

    label("Function_28_6ED5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6FA6")

    ChrTalk(
        0xFE,
        (
            "I secretly visited the bar\x01",
            "where my younger brother works.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He was embarrassed at first\x01",
            "but then served me properly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm glad he's approaching his\x01",
            "work with professionalism.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_6FF7")

    label("loc_6FA6")


    ChrTalk(
        0xFE,
        "*glug glug*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The non-alcoholic\x01",
            "cocktail Azel made...\x01",
            "Is pretty good.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6FF7")

    TalkEnd(0xFE)
    Return()

    # Function_28_6ED5 end

    def Function_29_6FFB(): pass

    label("Function_29_6FFB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_708F")

    ChrTalk(
        0xFE,
        (
            "Uwah! Everyone's\x01",
            "wearing the same\x01",
            "thing as big brother Azel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Aww. I want a blue\x01",
            "parka so I too can\x01",
            "match my brother.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_70CC")

    label("loc_708F")


    ChrTalk(
        0xFE,
        (
            "Aww. I want a blue\x01",
            "parka so I too can\x01",
            "match my brother.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_70CC")

    TalkEnd(0xFE)
    Return()

    # Function_29_6FFB end

    def Function_30_70D0(): pass

    label("Function_30_70D0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7149")

    ChrTalk(
        0xFE,
        (
            "I don't really get it,\x01",
            "but for now, let's\x01",
            "smash those armors!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure Mr. Wald\x01",
            "would agree!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_717D")

    label("loc_7149")


    ChrTalk(
        0xFE,
        (
            "I don't really get it, but\x01",
            "go break two legs!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_717D")

    TalkEnd(0xFE)
    Return()

    # Function_30_70D0 end

    def Function_31_7181(): pass

    label("Function_31_7181")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7219")

    ChrTalk(
        0xFE,
        (
            "It looks like those armors\x01",
            "haven't entered Downtown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For now, we made the residents near\x01",
            "Ignis take shelter indoors, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_72B5")

    label("loc_7219")


    ChrTalk(
        0xFE,
        (
            "I wish Mr. Jed and the\x01",
            "others would help...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't think I'll ever understand\x01",
            "why Mr. Wald left us like that, \x01",
            "but I guess it can't be helped...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_72B5")

    TalkEnd(0xFE)
    Return()

    # Function_31_7181 end

    def Function_32_72B9(): pass

    label("Function_32_72B9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7301")

    ChrTalk(
        0xFE,
        "Just what is that blue mist outside, I wonder...\x02",
    )

    CloseMessageWindow()
    Jump("loc_7389")

    label("loc_7301")


    ChrTalk(
        0xFE,
        (
            "H-Hmph.. We're only going to cooperate\x01",
            "with those baldies this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We'll protect Downtown\x01",
            "for whenever Mr.\x01",
            "Wald comes back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7389")

    TalkEnd(0xFE)
    Return()

    # Function_32_72B9 end

    def Function_33_738D(): pass

    label("Function_33_738D")

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

    def lambda_74E7():
        OP_96(0xFE, 0xFFFFFCE0, 0x0, 0xA28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_74E7)

    def lambda_7501():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7501)
    Sleep(400)

    def lambda_7515():
        OP_96(0xFE, 0x2BC, 0x0, 0x960, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7515)

    def lambda_752F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_752F)
    Sleep(400)

    def lambda_7543():
        OP_96(0xFE, 0xFFFFFE0C, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7543)

    def lambda_755D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_755D)
    Sleep(400)

    def lambda_7571():
        OP_96(0xFE, 0x2BC, 0x0, 0x4B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7571)

    def lambda_758B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_758B)
    WaitChrThread(0x101, 1)

    def lambda_75A0():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_75A0)
    WaitChrThread(0x102, 1)

    def lambda_75B1():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_75B1)
    WaitChrThread(0x109, 1)

    def lambda_75C2():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_75C2)
    WaitChrThread(0x105, 1)

    def lambda_75D3():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_75D3)
    WaitChrThread(0x105, 2)
    OP_6F(0x10)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xA, 0x0, 0)

    ChrTalk(
        0xA,
        (
            "Welcome. How many\x01",
            "of you are there...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "Hey, you guys are the Special\x01",
            "Support Section!? And Wazy too!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005F"W-Welcome", you said...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x8, 500)

    ChrTalk(
        0x105,
        (
            "#12P#10304FHu hu. Most importantly, it\x01",
            "looks like you're running\x01",
            "a real business now.\x02\x03",
            "#10302FHu hu, what about you, Abbas?\x01",
            "Doing well for yourselves, I guess?\x02",
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
            "...Well, we're doing all right.\x02\x03",
            "More importantly, how nice of\x01",
            "you to come. Since you're here,\x01",
            "make yourselves at home.\x02",
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

    def lambda_786F():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_786F)

    def lambda_787C():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_787C)

    def lambda_7889():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_7889)

    def lambda_7896():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_7896)

    def lambda_78A3():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_78A3)
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
        "#04100F...Wazy, how is the Special Support Section?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FWell, I guess it's pretty comfortable?\x02\x03",
            "#10304FThe Chief and my co-workers are understanding,\x01",
            "and it's a carefree workplace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FNo, I think YOU are a little\x01",
            "too carefree, Wazy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10101FThat's right, Wazy. Although you're\x01",
            "an associate member, you're aware\x01",
            "you're a police officer, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHu hu. Though you say\x01",
            "that, this is my style.\x02\x03",
            "#10304FIf you guys are too strict, a little more\x01",
            "and you'll break into pieces, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00106F...*sigh*. No matter what you\x01",
            "say to Wazy, it's useless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04100F...Hmm. You seem to be\x01",
            "getting along well. In that\x01",
            "case, there's no problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006F(Or rather, I feel like there's\x01",
            "nothing but problems...)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00005FCome to think of it... Were there\x01",
            "any members opposed to Wazy joining\x01",
            "the Special Support Section?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00105FOh, indeed...\x01",
            "I wonder if you were perplexed\x01",
            "about various things?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04100F...None of us were opposed. \x01",
            "Everything is decided by Wazy, after all.\x02",
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
        "#12P#10106F(That wasn't much of an answer...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006F(I wonder if that's\x01",
            "just how he is...)\x02",
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
            "#11PWell, we were perplexed, but...\x01",
            "We discussed it amongst\x01",
            "the members and agreed.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7EB7():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7EB7)
    Sleep(10)

    def lambda_7EC7():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7EC7)

    def lambda_7ED4():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7ED4)
    Sleep(10)

    def lambda_7EE4():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7EE4)
    Sleep(10)

    ChrTalk(
        0xA,
        (
            "#12POpposition to our parents, situations at home... For\x01",
            "various reasons, these members have gathered, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12PIf Wazy has decided the path\x01",
            "he'll follow and leaves the\x01",
            "group, we're not opposed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#12PRather, we wonder if our own opportunities\x01",
            "to be independent are out there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PBasically, things have gotten better\x01",
            "since we did nothing but fight, now\x01",
            "that we're in charge of Trinity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PWell, it's certainly\x01",
            "lonely with Wazy gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00002FHa ha...I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#N#10102FYou guys seem quite positive about this.\x02",
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#6P#10304FWell from the start, Abbas has been\x01",
            "in charge of almost all of Trinity.\x02\x03",
            "#10300FEven if I'm not here, I think\x01",
            "you'll do just fine on your own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#6P#04102F...There you have it.\x02",
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
            "#04100FSpecial Support Section, we're leaving\x01",
            "Wazy to you for the time being.\x02\x03",
            "Wazy, you too should pay no heed to\x01",
            "us, and focus on your current work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10304FHu hu. I planned to do that from the start.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x102, 500)

    ChrTalk(
        0x105,
        "#6P#10304FSo, once again, it's nice to be working with you㈱\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)

    ChrTalk(
        0x101,
        (
            "#11P#00006FW-Well, there'll be many\x01",
            "difficulties, but...\x02\x03",
            "#00000F*ahem*, allow me to give you a\x01",
            "warm welcome once again as well.\x02",
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

    # Function_33_738D end

    def Function_34_8485(): pass

    label("Function_34_8485")

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

    def lambda_858A():
        OP_96(0xFE, 0x384, 0x0, 0x141E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_858A)

    def lambda_85A4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_85A4)
    Sleep(400)

    def lambda_85B8():
        OP_96(0xFE, 0xFFFFFCE0, 0x0, 0x10FE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_85B8)

    def lambda_85D2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_85D2)
    Sleep(400)

    def lambda_85E6():
        OP_96(0xFE, 0x4BA, 0x0, 0xEA6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_85E6)

    def lambda_8600():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8600)
    Sleep(400)

    def lambda_8614():
        OP_96(0xFE, 0xFFFFFDA8, 0x0, 0xBE0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8614)

    def lambda_862E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_862E)
    Sleep(400)

    def lambda_8642():
        OP_96(0xFE, 0x3E8, 0x0, 0x794, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8642)

    def lambda_865C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_865C)
    Sleep(400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_86AD")

    def lambda_8682():
        OP_96(0xFE, 0xFFFFFC18, 0x0, 0x60E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_8682)

    def lambda_869C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_869C)
    Jump("loc_86D8")

    label("loc_86AD")


    def lambda_86B2():
        OP_96(0xFE, 0xFFFFFC18, 0x0, 0x60E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_86B2)

    def lambda_86CC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_86CC)

    label("loc_86D8")

    WaitChrThread(0xF4, 1)
    WaitChrThread(0xF5, 1)

    ChrTalk(
        0x105,
        (
            "#12P#10405FOh, it looks like some unusual\x01",
            "customers have come in.\x02",
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

    def lambda_87E6():
        TurnDirection(0xA, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_87E6)

    def lambda_87F3():
        TurnDirection(0xB, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_87F3)

    def lambda_8800():
        TurnDirection(0x9, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8800)

    def lambda_880D():
        TurnDirection(0x15, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_880D)

    def lambda_881A():
        TurnDirection(0x16, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_881A)
    TurnDirection(0x17, 0x105, 500)

    ChrTalk(
        0x17,
        "#5PY-You...!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PW-Wazy!? And the\x01",
            "Support Section!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00005FTestaments and Vipers...\x01",
            "So this is where you all are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PY-Yeah... We're discussing\x01",
            "what to do about the\x01",
            "situation in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#5PMore importantly... Wazy,\x01",
            "what's with those strange\x01",
            "clothes you're wearing!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PA-And also... Isn't\x01",
            "Abbas with you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10406FOh boy. I come back and\x01",
            "there's no room to breathe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00300FOh, well you make a\x01",
            "big impact, don't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203FFor now, I think it's best to\x01",
            "outline the situation for them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10403FWell if I suddenly start talking\x01",
            "about Knights and the Church and such,\x01",
            "the explanation would be kinda long.\x02\x03",
            "#10400FI'll explain it to you guys later.\x01",
            "...Is that all right with you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PS-Sure... That aside, we need to\x01",
            "focus on the current situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10402FHu hu, but even so... It\x01",
            "looks like you protected\x01",
            "this place for Abbas and I.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PO-Of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIt's because you and\x01",
            "Abbas promised to\x01",
            "return.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PT-That's why we\x01",
            "did our very best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#5PHmph. It's not like we\x01",
            "were watching the place on\x01",
            "account of Wazy, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x17,
        (
            "#5PSomething like that has happened, but...\x01",
            "We have to make sure Mr. Wald\x01",
            "has a place to come back to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PYeah, Downtown is a\x01",
            "place important to us\x01",
            "Saber Vipers too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PSome of us, including Mr.\x01",
            "Jed, still haven't felt like\x01",
            "cooperating though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10404FI see... Thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00109F*giggle*. You've become\x01",
            "a fine man, Dino.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x17)
    TurnDirection(0x17, 0x102, 500)

    ChrTalk(
        0x17,
        "#5PI-It's not that...!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x17, 500)

    ChrTalk(
        0x15,
        (
            "#5PHa ha. It's nothing to\x01",
            "be ashamed of, Dino.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8F27")

    ChrTalk(
        0x10A,
        (
            "#12P#00603FAnyway, it seems the\x01",
            "President's monsters haven't\x01",
            "appeared in Downtown...\x02\x03",
            "#00600FIt'll be alright if we leave\x01",
            "this place to these guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FYes, I agree.\x02",
    )

    CloseMessageWindow()
    Jump("loc_90B6")

    label("loc_8F27")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8FDA")

    ChrTalk(
        0x109,
        (
            "#N#12P#10103FAnyway, it seems the\x01",
            "President's monsters haven't\x01",
            "appeared in Downtown...\x02\x03",
            "#10100FI think it'll be alright if we\x01",
            "leave this place to them.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_9093")

    label("loc_8FDA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9093")

    ChrTalk(
        0x106,
        (
            "#N#12P#10703FAnyway, it seems the monsters\x01",
            "the enemy is employing haven't\x01",
            "appeared in Downtown...\x02\x03",
            "#10702FI think it'll be alright if we\x01",
            "leave this place to them.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_9093")


    ChrTalk(
        0x101,
        "#6P#00000FYeah, you're right.\x02",
    )

    CloseMessageWindow()

    label("loc_90B6")

    TurnDirection(0x17, 0x105, 500)

    ChrTalk(
        0x105,
        (
            "#12P#10404FThere you have it. \x01",
            "It's time for us to go.\x02\x03",
            "#10400FCan you watch the place\x01",
            "a little longer for me?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x105, 500)

    ChrTalk(
        0xA,
        "#11PYeah, leave it to us!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PBe careful, Wazy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "#5PI don't really get it, but\x01",
            "go break two legs!!\x02",
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

    # Function_34_8485 end

    SaveToFile()

Try(main)
