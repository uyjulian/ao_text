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
        "Function_7_1C9B",         # 07, 7
        "Function_8_21FC",         # 08, 8
        "Function_9_234C",         # 09, 9
        "Function_10_24DF",        # 0A, 10
        "Function_11_368D",        # 0B, 11
        "Function_12_37A3",        # 0C, 12
        "Function_13_3878",        # 0D, 13
        "Function_14_4831",        # 0E, 14
        "Function_15_4850",        # 0F, 15
        "Function_16_4A2E",        # 10, 16
        "Function_17_57F6",        # 11, 17
        "Function_18_57FA",        # 12, 18
        "Function_19_65C9",        # 13, 19
        "Function_20_6731",        # 14, 20
        "Function_21_684D",        # 15, 21
        "Function_22_6857",        # 16, 22
        "Function_23_69B6",        # 17, 23
        "Function_24_6ADC",        # 18, 24
        "Function_25_6C15",        # 19, 25
        "Function_26_6CD9",        # 1A, 26
        "Function_27_6DEE",        # 1B, 27
        "Function_28_6E6D",        # 1C, 28
        "Function_29_6F9B",        # 1D, 29
        "Function_30_705C",        # 1E, 30
        "Function_31_7105",        # 1F, 31
        "Function_32_7234",        # 20, 32
        "Function_33_7305",        # 21, 33
        "Function_34_83D0",        # 22, 34
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
    Jump("loc_1C97")

    label("loc_C0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_C3C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C25")
    Jump("loc_C37")

    label("loc_C25")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C37")
    Jump("loc_C37")

    label("loc_C37")

    Jump("loc_1C97")

    label("loc_C3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_CDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C57")
    Call(0, 7)
    Jump("loc_CDA")

    label("loc_C57")


    ChrTalk(
        0x8,
        (
            "#04100FWe plan to continue our\x01",
            "search for Wald.\x02\x03",
            "We'll contact you immediately\x01",
            "if we learn anything, so\x01",
            "please wait for that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CDA")

    Jump("loc_1C97")

    label("loc_CDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_D40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CFA")
    Call(0, 8)
    Jump("loc_D3B")

    label("loc_CFA")


    ChrTalk(
        0x8,
        (
            "#04100FWe're taking care of\x01",
            "compiling info related\x01",
            "to Wald.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D3B")

    Jump("loc_1C97")

    label("loc_D40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_DA5")

    ChrTalk(
        0x8,
        (
            "#04100F...It seems this work is\x01",
            "urgent.\x02\x03",
            "If you need anything,\x01",
            "just say the word.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C97")

    label("loc_DA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1093")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1014")

    ChrTalk(
        0x8,
        (
            "#04100FIt seems the Vipers have\x01",
            "started to search for\x01",
            "Wald.\x02\x03",
            "It seems he hasn't been\x01",
            "seen at all these past\x01",
            "few days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301FNot even once, huh... I\x01",
            "wonder where he is and\x01",
            "what he's doing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10301F...You guys haven't seen\x01",
            "him either, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x105, 0)

    ChrTalk(
        0x8,
        (
            "#04100FYeah. Not at all this\x01",
            "past week.\x02\x03",
            "Before then, he'd show\x01",
            "every so often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10308FIs that so...\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x8)

    ChrTalk(
        0x8,
        (
            "#04100F...Don't worry, Wazy.\x02\x03",
            "It's only been a few\x01",
            "days since he\x01",
            "disappeared.\x02\x03",
            "And, we have nothing\x01",
            "else we have to do right\x01",
            "now, right?\x02",
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
    Jump("loc_108E")

    label("loc_1014")

    TurnDirection(0x8, 0x105, 0)

    ChrTalk(
        0x8,
        (
            "#04100FWe're concerned about\x01",
            "Wald too.\x02\x03",
            "And so, Wazy, don't worry\x01",
            "needlessly, and focus on\x01",
            "your current work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_108E")

    Jump("loc_1C97")

    label("loc_1093")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_11D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10AE")
    Call(0, 9)
    Jump("loc_11D2")

    label("loc_10AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_116E")
    TurnDirection(0x8, 0x105, 0)

    ChrTalk(
        0x8,
        (
            "#04100FWazy... So you came.\x02\x03",
            "If you want to relax in the\x01",
            "store, just say the word. We'll\x01",
            "have you seated right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FHaha. Thanks, Abbas.\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x2D, 0x0)
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 1)
    Jump("loc_11D2")

    label("loc_116E")


    ChrTalk(
        0x8,
        (
            "#04100FIf you want to relax in the\x01",
            "store, just say the word. We'll\x01",
            "have you seated right away.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11D2")

    Jump("loc_1C97")

    label("loc_11D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1344")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12AA")

    ChrTalk(
        0x8,
        (
            "#04100F...Downtown has been\x01",
            "relatively peaceful these\x01",
            "days.\x02\x03",
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
    Jump("loc_133F")

    label("loc_12AA")


    ChrTalk(
        0x8,
        (
            "#04100F...Downtown has been\x01",
            "relatively peaceful these\x01",
            "days.\x02\x03",
            "And so, Wazy, don't worry\x01",
            "about this place and focus on\x01",
            "your Support Section work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_133F")

    Jump("loc_1C97")

    label("loc_1344")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_169C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1491")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1449")

    ChrTalk(
        0x8,
        (
            "#04105FThat customer, could he\x01",
            "be...\x02\x03",
            "#04102F...Hah, I don't believe\x01",
            "it.\x02",
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
        (
            "#00305F(Yeah, that's rare for\x01",
            "him...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F(Oh man... Just what are\x01",
            "you guys thinking about\x01",
            "Abbas?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_148C")

    label("loc_1449")


    ChrTalk(
        0x8,
        (
            "#04102FThat customer, could he\x01",
            "be... Hah, I don't\x01",
            "believe it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_148C")

    Jump("loc_1697")

    label("loc_1491")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1644")

    ChrTalk(
        0x8,
        "#04100F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FThinking about\x01",
            "something, Abbas?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x105, 0)

    ChrTalk(
        0x8,
        (
            "#04100FWazy, huh...\x02\x03",
            "...Yeah. I was just thinking\x01",
            "there are all kinds of\x01",
            "people in this world.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309FHaha, you said it.\x02\x03",
            "#10304FWe're in it too, you\x01",
            "know.\x02",
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
            "#00000F(He's spoken with Wazy\x01",
            "quite a bit.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F(Haha. They're probably\x01",
            "close just because of\x01",
            "that.)\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 0)
    Jump("loc_1697")

    label("loc_1644")


    ChrTalk(
        0x8,
        (
            "#04100F............\x02\x03",
            "...There's definitely\x01",
            "all kinds of people in\x01",
            "this world.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1697")

    Jump("loc_1C97")

    label("loc_169C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_17F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_179E")

    ChrTalk(
        0x8,
        (
            "#04100FIt looks like there's\x01",
            "many officers patrolling\x01",
            "Downtown.\x02\x03",
            "You're not hindering the\x01",
            "Support Section's work,\x01",
            "are you Wazy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FWell, there's no special\x01",
            "problem with the current\x01",
            "case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#04100FI see. Good then.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17F0")

    label("loc_179E")


    ChrTalk(
        0x8,
        (
            "#04100FIt seems several\x01",
            "officers have come to\x01",
            "Downtown.\x02\x03",
            "...How troublesome.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17F0")

    Jump("loc_1C97")

    label("loc_17F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_END)), "loc_197B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1934")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x105, 0)

    ChrTalk(
        0x8,
        (
            "#04100FWazy, are you all right?\x01",
            "You look pale.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FYeah, I'm fine. No need\x01",
            "to worry.\x02",
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
            "#10106F(These two... They're\x01",
            "strangely casual with\x01",
            "each other.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F(Yes, but they have a\x01",
            "weird way of\x01",
            "communicating.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1976")

    label("loc_1934")

    TurnDirection(0x8, 0x105, 0)

    ChrTalk(
        0x8,
        (
            "#04100FWazy, if you need our\x01",
            "help, just say the word.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1976")

    Jump("loc_1C97")

    label("loc_197B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1A7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A2C")

    ChrTalk(
        0x8,
        (
            "#04100FIf you have an order,\x01",
            "I'll take it.\x02\x03",
            "Please feel free to ask.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(Feel free with this\x01",
            "guy, huh... That seems\x01",
            "difficult somehow.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A76")

    label("loc_1A2C")


    ChrTalk(
        0x8,
        (
            "#04100FIf you have an order,\x01",
            "I'll take it.\x02\x03",
            "Please feel free to ask.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A76")

    Jump("loc_1C97")

    label("loc_1A7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1C97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C34")

    ChrTalk(
        0x8,
        (
            "#04100FWazy, leave everything\x01",
            "about the Testaments to\x01",
            "me.\x02\x03",
            "You should do what you\x01",
            "want to do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FYeah, I will.\x02\x03",
            "#10304FI'll be stopping by Trinity\x01",
            "every now and then, so\x01",
            "manage that for me, too.\x02\x03",
            "#10302FHaha. If it goes under,\x01",
            "there'll be fewer cozy\x01",
            "places.\x02",
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
        (
            "#00003F(These two have a\x01",
            "strange relationship...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F(What kind of past do\x01",
            "they have, I wonder.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C97")

    label("loc_1C34")


    ChrTalk(
        0x8,
        (
            "#04100FWazy, leave everything\x01",
            "about the Testaments to\x01",
            "me.\x02\x03",
            "You should do what you\x01",
            "want to do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C97")

    TalkEnd(0xFE)
    Return()

    # Function_6_BF9 end

    def Function_7_1C9B(): pass

    label("Function_7_1C9B")

    OP_4B(0x8, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FC6")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x105, 0)
    Sleep(1000)
    TurnDirection(0xB, 0x105, 0)
    TurnDirection(0xA, 0x105, 0)

    ChrTalk(
        0x8,
        (
            "#04100FWazy... It looks like\x01",
            "you're having a tough\x01",
            "time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Actually, Veysset and I\x01",
            "saw a redheaded man this\x01",
            "morning...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DE5")
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x109,
        (
            "#10108FI knew it... He came to\x01",
            "Downtown.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DE5")


    ChrTalk(
        0xB,
        (
            "How to say this... F-From\x01",
            "his expression, he looked\x01",
            "worried about something.\x02",
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
            "#04100FI see...\x02\x03",
            "However, if you ever\x01",
            "need our help, just say\x01",
            "the word.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FYeah, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F(Just you wait, Randy.\x01",
            "We'll definitely catch\x01",
            "you.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16E, 2)
    Jump("loc_21DA")

    label("loc_1FC6")


    ChrTalk(
        0x105,
        (
            "#10300FBy the way Abbas... Did\x01",
            "you gather the info\x01",
            "regarding Wald?\x02",
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
            "#04100FNo... We haven't been able\x01",
            "to get any promising info\x01",
            "as of yet.\x02\x03",
            "Most likely he's trying to\x01",
            "stay hidden. There's hardly\x01",
            "any sightings of him.\x02\x03",
            "It's honestly hard for me\x01",
            "to think of any way he\x01",
            "could get that drug.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10303FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04100FBut even so, we plan to\x01",
            "continue our investigation.\x02\x03",
            "We'll contact you immediately\x01",
            "if we learn anything, so\x01",
            "please wait for that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10300FYeah, understood.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x16E, 1)

    label("loc_21DA")

    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0x8, 0xFF)
    OP_93(0xA, 0x5A, 0x0)
    OP_93(0xB, 0x0, 0x0)
    OP_93(0x8, 0xE1, 0x0)
    Return()

    # Function_7_1C9B end

    def Function_8_21FC(): pass

    label("Function_8_21FC")

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
            "#04100FWazy, huh... Leave\x01",
            "gathering intel on Wald\x01",
            "to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "O-Once our plan is\x01",
            "complete, we'll look for\x01",
            "clues right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "So Wazy, focus on your\x01",
            "Support Section work for\x01",
            "us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FThanks. I'm counting on\x01",
            "you.\x02",
        )
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

    # Function_8_21FC end

    def Function_9_234C(): pass

    label("Function_9_234C")

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
            "I'm so jealous... Feel\x01",
            "free to give me a share,\x01",
            "ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04102FHmph, you're not doing\x01",
            "so bad yourself, are\x01",
            "you.\x02",
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
        (
            "#00000F(Those two look like\x01",
            "they're having fun.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302F(Haha. They're both\x01",
            "oddballs, so they think\x01",
            "alike.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211F(...On that note, I\x01",
            "think you're one too,\x01",
            "Wazy.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 6)
    OP_4C(0xD, 0xFF)
    OP_4C(0x8, 0xFF)
    ClearChrFlags(0xD, 0x10)
    Return()

    # Function_9_234C end

    def Function_10_24DF(): pass

    label("Function_10_24DF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2624")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25B4")

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
            "I managed to contact my\x01",
            "father, but it seems he\x01",
            "was busy doing the rounds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I've got to do my\x01",
            "best, too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_261F")

    label("loc_25B4")


    ChrTalk(
        0xFE,
        (
            "I don't know if I'll be\x01",
            "able to follow my old\x01",
            "man's path, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I've got to do my\x01",
            "best, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_261F")

    Jump("loc_3689")

    label("loc_2624")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2741")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26CE")

    ChrTalk(
        0xFE,
        (
            "I've got to prioritize\x01",
            "the safety of the\x01",
            "neighborhood citizens.\x02",
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
    Jump("loc_273C")

    label("loc_26CE")


    ChrTalk(
        0xFE,
        (
            "We're trying to do\x01",
            "something about this\x01",
            "situation ourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Come back safely for us\x01",
            "too, you guys.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_273C")

    Jump("loc_3689")

    label("loc_2741")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2A78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29AA")

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
            "He didn't tell us where\x01",
            "he was going. I wonder\x01",
            "if something happened...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FAbbas said that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FMaybe he's with Wazy?\x02",
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
        (
            "C-Could they have been\x01",
            "arrested?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00201FI can't think Wazy or\x01",
            "Abbas would make such a\x01",
            "blunder, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FHmm... Well anyway, I\x01",
            "think you should calm\x01",
            "down. Don't you think so?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Yeah. Anyway, we've\x01",
            "got to protect the\x01",
            "store...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2A73")

    label("loc_29AA")


    ChrTalk(
        0xFE,
        (
            "Though I'm worried about Wazy and\x01",
            "Abbas... I wonder if my dad at\x01",
            "St. Ursula Hospital is all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure my dad is treating\x01",
            "patients even in this situation,\x01",
            "because that's just who he is.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A73")

    Jump("loc_3689")

    label("loc_2A78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2A86")
    Jump("loc_3689")

    label("loc_2A86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2B40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AA1")
    Call(0, 7)
    Jump("loc_2B3B")

    label("loc_2AA1")


    ChrTalk(
        0xFE,
        (
            "Even so... That redhead had\x01",
            "a huge amount of luggage,\x01",
            "even though it's raining.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It looked heavy, but I\x01",
            "was surprised at how\x01",
            "fast he was moving.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B3B")

    Jump("loc_3689")

    label("loc_2B40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2C72")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B5B")
    Call(0, 8)
    Jump("loc_2C6D")

    label("loc_2B5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C25")

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
            "It seems several people were\x01",
            "severely wounded... Looks like\x01",
            "my old man's going to be busy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2C6D")

    label("loc_2C25")


    ChrTalk(
        0xFE,
        (
            "My dad's amazing... We\x01",
            "can rely on him even at\x01",
            "a time like this...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C6D")

    Jump("loc_3689")

    label("loc_2C72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2D84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D01")

    ChrTalk(
        0xFE,
        (
            "I... Just what do I want\x01",
            "to be?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Damn. No matter how\x01",
            "much I think about it, the\x01",
            "answer just won't come.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2D7F")

    label("loc_2D01")


    ChrTalk(
        0xFE,
        (
            "Thinking back on it, I\x01",
            "didn't hate studying\x01",
            "that much, did I...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I sit at a desk\x01",
            "again, I wonder what\x01",
            "I'll see...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D7F")

    Jump("loc_3689")

    label("loc_2D84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2F1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E95")

    ChrTalk(
        0xFE,
        (
            "When I was small, I\x01",
            "remember wanting to be a\x01",
            "doctor like my dad...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But at some point, I\x01",
            "realized I'm not as\x01",
            "smart as him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...I can't even put it\x01",
            "into words.\x02",
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
    Jump("loc_2F15")

    label("loc_2E95")


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
            "They pay a salary here,\x01",
            "so I've got to focus on\x01",
            "being a good waiter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F15")

    Jump("loc_3689")

    label("loc_2F1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3151")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30CA")

    ChrTalk(
        0xFE,
        (
            "How to say this...\x01",
            "Everyone's been lively\x01",
            "lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if it's just me\x01",
            "who feels that they're\x01",
            "half a man...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*... What ever\x01",
            "shall I do?\x02",
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
            "#10304F(Yeah. For a while now,\x01",
            "each of the Testaments\x01",
            "has been independent.)\x02\x03",
            "#10300F(It's not my place to\x01",
            "interfere.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211F(...That reminds me of\x01",
            "Chief Sergei for some\x01",
            "reason.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_314C")

    label("loc_30CA")


    ChrTalk(
        0xFE,
        (
            "Everyone's been lively lately.\x01",
            "I wonder if it's just me who\x01",
            "feels they're half a man...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*... What ever\x01",
            "shall I do?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_314C")

    Jump("loc_3689")

    label("loc_3151")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3298")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_324F")

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
            "learned from Abbas. It was\x01",
            "surprisingly effective.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3293")

    label("loc_324F")


    ChrTalk(
        0xFE,
        (
            "A peaceful approach,\x01",
            "huh... We have a lot to\x01",
            "learn from Abbas.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3293")

    Jump("loc_3689")

    label("loc_3298")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_344B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_332E")

    ChrTalk(
        0xFE,
        (
            "A-Amazing. That blond\x01",
            "customer...\x02",
        )
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
    Jump("loc_3446")

    label("loc_332E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33DF")

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
        (
            "Could it be because of\x01",
            "that customer just\x01",
            "now...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Well, whatever. It's\x01",
            "best not to worry about\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3446")

    label("loc_33DF")


    ChrTalk(
        0xFE,
        (
            "Could it be because of\x01",
            "that customer just\x01",
            "now...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Well, whatever. I\x01",
            "won't worry about it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3446")

    Jump("loc_3689")

    label("loc_344B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3495")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3466")
    Call(0, 11)
    Jump("loc_3490")

    label("loc_3466")


    ChrTalk(
        0xFE,
        (
            "This way then, ladies\x01",
            "and gentlemen.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3490")

    Jump("loc_3689")

    label("loc_3495")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3521")

    ChrTalk(
        0xFE,
        (
            "*sigh*. No matter what I\x01",
            "do, my mood sinks on\x01",
            "rainy days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My hair's a mess when it\x01",
            "gets wet... I hope it\x01",
            "ends soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3689")

    label("loc_3521")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3689")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3616")

    ChrTalk(
        0xFE,
        (
            "I'm not especially\x01",
            "suited for waiting\x01",
            "tables, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There were no other roles\x01",
            "for me, so I had no choice\x01",
            "but to take up waiting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But even so, now that I've\x01",
            "taken it up, I can only\x01",
            "make a proper effort.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3689")

    label("loc_3616")


    ChrTalk(
        0xFE,
        (
            "Welcome. If you'd like a\x01",
            "seat, I'd be happy to\x01",
            "show you to one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's what a waiter\x01",
            "does, more or less.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3689")

    TalkEnd(0xFE)
    Return()

    # Function_10_24DF end

    def Function_11_368D(): pass

    label("Function_11_368D")

    OP_4B(0xA, 0xFF)
    OP_4B(0x10, 0xFF)
    OP_4B(0x11, 0xFF)

    ChrTalk(
        0xA,
        (
            "Um, there's two of you,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "We have counter and\x01",
            "table seats. Which would\x01",
            "you prefer?\x02",
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
            "Understood. Right this\x01",
            "way, please.\x02",
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

    # Function_11_368D end

    def Function_12_37A3(): pass

    label("Function_12_37A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_386E")
    TalkBegin(0xB)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_37C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_386A")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3815")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3815")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3835")
    OP_AF(0xB3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3865")

    label("loc_3835")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3849")
    Jump("loc_3865")

    label("loc_3849")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3865")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 13)

    label("loc_3865")

    Jump("loc_37C3")

    label("loc_386A")

    TalkEnd(0xB)
    Return()

    label("loc_386E")

    TalkBegin(0xB)
    Call(0, 13)
    TalkEnd(0xB)
    Return()

    # Function_12_37A3 end

    def Function_13_3878(): pass

    label("Function_13_3878")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3B24")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A84")

    ChrTalk(
        0xB,
        (
            "Even so... That's surprising.\x01",
            "Who knew Wazy and Abbas were\x01",
            "Church officials?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3A27")

    ChrTalk(
        0xB,
        (
            "They suddenly seem so\x01",
            "far away from us for\x01",
            "some reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10402FHaha. We actually haven't changed\x01",
            "at all. I'd like you to treat us\x01",
            "like you usually do.\x02\x03",
            "#10404FYou could say the "Wazy\x01",
            "Hemisphere" who ran the Testaments\x01",
            "with you is the real me as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I-I see... I'm happy to\x01",
            "hear you say that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A7C")

    label("loc_3A27")


    ChrTalk(
        0xB,
        (
            "Up until now, you never\x01",
            "acted like it. H-Honestly, I\x01",
            "can't even believe it now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A7C")

    SetScenarioFlags(0x0, 3)
    Jump("loc_3B1F")

    label("loc_3A84")


    ChrTalk(
        0xB,
        (
            "T-To think Wazy and Abbas\x01",
            "were Church officials\x01",
            "this whole time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Up until now, you never\x01",
            "acted like it. H-Honestly, I\x01",
            "can't even believe it now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B1F")

    Jump("loc_4830")

    label("loc_3B24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3C09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BB1")

    ChrTalk(
        0xB,
        (
            "It's best to avoid\x01",
            "confronting those\x01",
            "monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "They're not attacking\x01",
            "us, so it's best to\x01",
            "leave them alone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C04")

    label("loc_3BB1")


    ChrTalk(
        0xB,
        (
            "Azel went back to East\x01",
            "Street to be with his\x01",
            "family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "I-I hope he's safe.\x02",
    )

    CloseMessageWindow()

    label("loc_3C04")

    Jump("loc_4830")

    label("loc_3C09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3C99")

    ChrTalk(
        0xB,
        (
            "Abbas too... There's\x01",
            "some kind of situation,\x01",
            "isn't there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "For now, we've got to\x01",
            "protect the shop, just\x01",
            "like he ordered.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4830")

    label("loc_3C99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3CA7")
    Jump("loc_4830")

    label("loc_3CA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3D59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CC2")
    Call(0, 7)
    Jump("loc_3D54")

    label("loc_3CC2")


    ChrTalk(
        0xB,
        (
            "H-His expression...\x01",
            "There was this amazing\x01",
            "intensity to it.\x02",
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

    label("loc_3D54")

    Jump("loc_4830")

    label("loc_3D59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3DD1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D74")
    Call(0, 8)
    Jump("loc_3DCC")

    label("loc_3D74")


    ChrTalk(
        0xB,
        "We plan to gather info.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I hope we're able to\x01",
            "find the source of the\x01",
            "Gnosis...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DCC")

    Jump("loc_4830")

    label("loc_3DD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3FAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F54")

    ChrTalk(
        0xB,
        (
            "T-This cocktail is\x01",
            "called "explosion".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "A bold idea brought\x01",
            "forth an unprecedented\x01",
            "invention.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "But... Maybe it was a little\x01",
            "beyond what I can do. ...I\x01",
            "feel like my ability's gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "And so... I-I've stopped\x01",
            "making cocktails.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "My final work... G-Get\x01",
            "rid of it for me.\x02",
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
    Jump("loc_3FA5")

    label("loc_3F54")


    ChrTalk(
        0xB,
        (
            "I-I've stopped making\x01",
            "cocktails.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "...I don't want to\x01",
            "become a murderer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FA5")

    Jump("loc_4830")

    label("loc_3FAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_41AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4116")

    ChrTalk(
        0xB,
        (
            "Ashley bought a great\x01",
            "many of my cocktails.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The taste and appearance aside,\x01",
            "she praised their ability to be\x01",
            "used on the battlefield.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hmm...? D-Did she praise\x01",
            "me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "A-Anyway... Ashley\x01",
            "approves of my\x01",
            "cocktails.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I-If you like, please\x01",
            "take one.\x02",
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
    Jump("loc_41A6")

    label("loc_4116")


    ChrTalk(
        0xB,
        (
            "My cocktails can be used on the\x01",
            "battlefield... I-In other words,\x01",
            "they're just that nutritious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It smells, but... J-Just\x01",
            "gulp it down.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41A6")

    Jump("loc_4830")

    label("loc_41AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_43DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_433B")

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
            "T-That's why I want to\x01",
            "try making them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Well, theirs look ugly so we can't\x01",
            "sell them, but... It's certain that\x01",
            "their ingredients are good for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I-If you like, please\x01",
            "take one.\x02",
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
        "#00005FS-Sure... Thanks.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16E, 3)
    Jump("loc_43DA")

    label("loc_433B")


    ChrTalk(
        0xB,
        (
            "I have absolute confidence in my\x01",
            "cocktail ingredients. I-It's\x01",
            "certain that they're good for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It does look like that,\x01",
            "but... J-Just gulp it\x01",
            "down.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43DA")

    Jump("loc_4830")

    label("loc_43DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4558")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44F3")

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
            "thinking, but Kientz was\x01",
            "able to stop them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I couldn't believe a technique\x01",
            "like that got the Vipers to\x01",
            "withdraw... What a discovery!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4553")

    label("loc_44F3")


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
            "can't work here, you\x01",
            "see.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4553")

    Jump("loc_4830")

    label("loc_4558")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4615")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45BE")

    ChrTalk(
        0xB,
        "Damn, even Liang...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "That blond hair and\x01",
            "white coat... What\x01",
            "courage.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4610")

    label("loc_45BE")


    ChrTalk(
        0xB,
        (
            "That blond hair and white\x01",
            "coat... That customer was\x01",
            "almost like a whirlwind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4610")

    Jump("loc_4830")

    label("loc_4615")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_46AF")

    ChrTalk(
        0xB,
        (
            "T-Thanks to that, we've\x01",
            "had more customers\x01",
            "lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "It's just, perhaps due to\x01",
            "lack of public order, we\x01",
            "don't get so many at night.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4830")

    label("loc_46AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_47AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_474B")

    ChrTalk(
        0xB,
        (
            "After I serve you, you\x01",
            "can play billiards all\x01",
            "you want.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "H-However, the condition\x01",
            "is that you order at\x01",
            "least one drink.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_47A6")

    label("loc_474B")


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
        (
            "It's limited to bar\x01",
            "customers only, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47A6")

    Jump("loc_4830")

    label("loc_47AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4830")

    ChrTalk(
        0xB,
        (
            "I'm in charge of\x01",
            "billiards instruction\x01",
            "and scoring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you don't know how to\x01",
            "hit the ball or the\x01",
            "rules, just ask.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4830")

    Return()

    # Function_13_3878 end

    def Function_14_4831(): pass

    label("Function_14_4831")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_484C")
    Call(0, 12)
    Jump("loc_484F")

    label("loc_484C")

    Call(0, 15)

    label("loc_484F")

    Return()

    # Function_14_4831 end

    def Function_15_4850(): pass

    label("Function_15_4850")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4959")
    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48AB")

    ChrTalk(
        0x9,
        (
            "Ah, if Wazy or Abbas\x01",
            "were here at a time like\x01",
            "this...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4955")

    label("loc_48AB")


    ChrTalk(
        0x9,
        (
            "So the day's finally\x01",
            "come for us to cooperate\x01",
            "with the Vipers, has it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, we understand their\x01",
            "strength better than anyone. I\x01",
            "couldn't ask for better allies.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4955")

    TalkEnd(0x9)
    Return()

    label("loc_4959")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4976")
    TalkBegin(0x9)
    Call(0, 22)
    TalkEnd(0x9)
    Return()

    label("loc_4976")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4983")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A2A")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_49D5")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_49D5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49F5")
    OP_AF(0xB3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4A25")

    label("loc_49F5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A09")
    Jump("loc_4A25")

    label("loc_4A09")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A25")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 16)

    label("loc_4A25")

    Jump("loc_4983")

    label("loc_4A2A")

    TalkEnd(0x9)
    Return()

    # Function_15_4850 end

    def Function_16_4A2E(): pass

    label("Function_16_4A2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4B4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B01")

    ChrTalk(
        0x9,
        (
            "It sometimes happens\x01",
            "that Abbas disappears\x01",
            "for a while, but...\x02",
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
            "...I hope he gets back\x01",
            "soon.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4B49")

    label("loc_4B01")


    ChrTalk(
        0x9,
        (
            "I wonder how long he'll\x01",
            "be gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...I hope he gets back\x01",
            "soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B49")

    Jump("loc_57F5")

    label("loc_4B4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4E4B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BE1")

    ChrTalk(
        0x9,
        (
            "I'm making a special\x01",
            "drink for the people\x01",
            "working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Because everyone drinks\x01",
            "here. The mixer's\x01",
            "running full speed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E46")

    label("loc_4BE1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DC0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D4E")

    ChrTalk(
        0x9,
        (
            "You're helping with\x01",
            "reconstruction too,\x01",
            "right Support Section?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Take these. My special\x01",
            "drinks for everyone, on\x01",
            "the house.\x02",
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
            " x6 received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x1CF, 6)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#00005FYou're giving us this\x01",
            "many?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FHaha, it's enough for\x01",
            "all of us. Thanks,\x01",
            "Liang.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Haha, you're welcome.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18D, 4)
    Jump("loc_4DBB")

    label("loc_4D4E")


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
        (
            "Haha, that's the Special\x01",
            "Support Section for you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DBB")

    Jump("loc_4E46")

    label("loc_4DC0")


    ChrTalk(
        0x9,
        (
            "Looks like the pork miso\x01",
            "Azel and the others made\x01",
            "was a hit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It's weird to say it,\x01",
            "but that emergency food\x01",
            "warmed my heart.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E46")

    Jump("loc_57F5")

    label("loc_4E4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5005")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F6D")

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
            "If those rumors are true, and\x01",
            "even if they're not, it's\x01",
            "something we can't allow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5000")

    label("loc_4F6D")


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
            "Or even if not, it's\x01",
            "something we can't\x01",
            "allow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5000")

    Jump("loc_57F5")

    label("loc_5005")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5062")

    ChrTalk(
        0x9,
        (
            "Wald... I wonder what\x01",
            "he's doing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It wasn't alcohol... but\x01",
            "a drug...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57F5")

    label("loc_5062")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5190")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50E9")

    ChrTalk(
        0x9,
        (
            "Looks like those\x01",
            "customers love our pasta\x01",
            "soup.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Haha. That's Abbas'\x01",
            "special secret recipe\x01",
            "for ya.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_518B")

    label("loc_50E9")


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
            "Cooking is rather\x01",
            "difficult, but I feel like\x01",
            "it's totally rewarded.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_518B")

    Jump("loc_57F5")

    label("loc_5190")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_535D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52BD")

    ChrTalk(
        0x9,
        (
            "Two Vipers came in\x01",
            "yesterday.\x02",
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
            "They were just trying to\x01",
            "save face, coming here\x01",
            "to ask about Wald.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The underlings are that worried\x01",
            "about him, huh. Wald... I\x01",
            "wonder what he's doing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5358")

    label("loc_52BD")


    ChrTalk(
        0x9,
        (
            "Though we were enemies\x01",
            "before, I have a little\x01",
            "respect for them now, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "To put it bluntly, Wald\x01",
            "is unqualified to be\x01",
            "their leader right now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5358")

    Jump("loc_57F5")

    label("loc_535D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_53FD")

    ChrTalk(
        0x9,
        (
            "Veysset put something\x01",
            "suspicious in the shaker.\x01",
            "Will he be all right...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If he had consulted with\x01",
            "me, I could've given him\x01",
            "some advice.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57F5")

    label("loc_53FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5566")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54C6")

    ChrTalk(
        0x9,
        "Hey, welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I recommend our daily\x01",
            "special, a bowl filled with\x01",
            "fresh, seasonal ingredients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We have a lunch menu\x01",
            "too, so please feel free\x01",
            "to ask me about it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5561")

    label("loc_54C6")


    ChrTalk(
        0x9,
        (
            "I recommend our daily\x01",
            "special, a bowl filled with\x01",
            "fresh, seasonal ingredients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We have a lunch menu\x01",
            "too, so please feel free\x01",
            "to ask me about it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5561")

    Jump("loc_57F5")

    label("loc_5566")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_563A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_557E")
    Jump("loc_5635")

    label("loc_557E")


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
            "In this world, there is\x01",
            "always someone better than\x01",
            "you. It's really true, huh.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5635")

    Jump("loc_57F5")

    label("loc_563A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_56B8")

    ChrTalk(
        0x9,
        (
            "Haha, Azel's sister is\x01",
            "such a worrywart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "But watching the\x01",
            "exchange of those two is\x01",
            "enjoyable somehow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57F5")

    label("loc_56B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_574C")

    ChrTalk(
        0x9,
        (
            "Man... Even just\x01",
            "stocking one thing is\x01",
            "hard in this rain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "There's mud stains\x01",
            "everywhere. I've got to\x01",
            "change before cooking.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57F5")

    label("loc_574C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_57F5")

    ChrTalk(
        0x9,
        (
            "Hey, welcome. Let me\x01",
            "know if you'd like to\x01",
            "order.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Whether it's a cocktail or snacks,\x01",
            "we'd be happy to show you as much\x01",
            "of Abbas' skill as you'd like.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57F5")

    Return()

    # Function_16_4A2E end

    def Function_17_57F6(): pass

    label("Function_17_57F6")

    Call(0, 18)
    Return()

    # Function_17_57F6 end

    def Function_18_57FA(): pass

    label("Function_18_57FA")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5A31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59AB")

    ChrTalk(
        0xC,
        (
            "Trinity has resumed\x01",
            "operation as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Although the situation's like\x01",
            "this, it's important to spend\x01",
            "days normally like this.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_595A")

    ChrTalk(
        0x105,
        (
            "#10400FHaha, well do your best, ok? There are\x01",
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
    Jump("loc_59A3")

    label("loc_595A")


    ChrTalk(
        0xC,
        (
            "My sister and Hugott are\x01",
            "rooting for me, so I've\x01",
            "got to do my best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59A3")

    SetScenarioFlags(0x0, 5)
    Jump("loc_5A2C")

    label("loc_59AB")


    ChrTalk(
        0xC,
        (
            "Trinity has resumed\x01",
            "operation. Feel free to\x01",
            "order.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "My sister and Hugott are\x01",
            "rooting for me, so I've\x01",
            "got to do my best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A2C")

    Jump("loc_65C5")

    label("loc_5A31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5A3F")
    Jump("loc_65C5")

    label("loc_5A3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5AE0")

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
            "...I think I'll go home\x01",
            "to check on my sister\x01",
            "and Hugott.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65C5")

    label("loc_5AE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5AEE")
    Jump("loc_65C5")

    label("loc_5AEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5C63")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BD7")

    ChrTalk(
        0xC,
        (
            "The mysterious force that\x01",
            "attacked Mainz seems\x01",
            "terribly formidable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It seems like the CGF\x01",
            "are having a tough time\x01",
            "dealing with them too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...Anyway, I hope the\x01",
            "situation's resolved\x01",
            "quickly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5C5E")

    label("loc_5BD7")


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

    label("loc_5C5E")

    Jump("loc_65C5")

    label("loc_5C63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5D0B")

    ChrTalk(
        0xC,
        (
            "They say Wald might have\x01",
            "taken the same medicine\x01",
            "that newbie Dino did, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Even though he's in an\x01",
            "opposing group, I'm\x01",
            "still worried about him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65C5")

    label("loc_5D0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5EBD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E04")

    ChrTalk(
        0xC,
        (
            "*sigh*, it's already\x01",
            "past noon, huh.\x02",
        )
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
            "to work as much because I'm\x01",
            "working, but...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5EB8")

    label("loc_5E04")


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
            "to work as much because I'm\x01",
            "working, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5EB8")

    Jump("loc_65C5")

    label("loc_5EBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_60AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FED")

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
            "He has a good head, and\x01",
            "on top of that, his\x01",
            "parents are rich.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "He feels like that, but\x01",
            "he can be whatever he\x01",
            "wants...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "How to say it...\x01",
            "Everyone is worried\x01",
            "about different things.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_60A6")

    label("loc_5FED")


    ChrTalk(
        0xC,
        (
            "I think I remember\x01",
            "Kientz once said he had\x01",
            "a daddy complex.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Even if he works hard and becomes a\x01",
            "doctor, he'll never surpass his father\x01",
            "so there's no meaning in it, he said...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60A6")

    Jump("loc_65C5")

    label("loc_60AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6125")

    ChrTalk(
        0xC,
        (
            "Abbas has a wealth of\x01",
            "expert knowledge from\x01",
            "many fields.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'm always learning new\x01",
            "things from him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65C5")

    label("loc_6125")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_61BF")

    ChrTalk(
        0xC,
        (
            "I've been enjoying work\x01",
            "lately for some reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "For some reason, I feel like\x01",
            "it'll be all right if I work\x01",
            "here forever like this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65C5")

    label("loc_61BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_62DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6265")

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
            "In the end, only Liang\x01",
            "was left standing. The\x01",
            "rest of us lost.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62D8")

    label("loc_6265")


    ChrTalk(
        0xC,
        (
            "But... That customer was\x01",
            "really something else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "How to say it... I can't\x01",
            "help wanting to talk to\x01",
            "people.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_62D8")

    Jump("loc_65C5")

    label("loc_62DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6367")

    ChrTalk(
        0xC,
        (
            "*sigh*, my sister\x01",
            "suddenly came in for no\x01",
            "reason...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...Well, whatever. Right\x01",
            "now, I've just got to\x01",
            "focus on work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65C5")

    label("loc_6367")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_63F9")

    ChrTalk(
        0xC,
        (
            "Liang's teaching me and\x01",
            "lets me make the\x01",
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
    Jump("loc_65C5")

    label("loc_63F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_65C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6551")

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
            "For the time being, we\x01",
            "all decided to cooperate\x01",
            "and help operate Trinity.\x02",
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
            "From here on, we plan to\x01",
            "attract more customers\x01",
            "and business.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_65C5")

    label("loc_6551")


    ChrTalk(
        0xC,
        (
            "Please continue to come\x01",
            "to Trinity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "We have an extensive\x01",
            "selection. Feel free to\x01",
            "order only food as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_65C5")

    TalkEnd(0xC)
    Return()

    # Function_18_57FA end

    def Function_19_65C9(): pass

    label("Function_19_65C9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6666")

    ChrTalk(
        0xFE,
        (
            "This pasta soup is\x01",
            "earth-shatteringly\x01",
            "delicious.\x02",
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
    Jump("loc_672D")

    label("loc_6666")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_66C3")

    ChrTalk(
        0xFE,
        (
            "Did something happen to\x01",
            "our waiter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He looks absent minded,\x01",
            "somehow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_672D")

    label("loc_66C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_672D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66DE")
    Call(0, 11)
    Jump("loc_672D")

    label("loc_66DE")


    ChrTalk(
        0xFE,
        (
            "I heard about this place\x01",
            "through word of mouth. It\x01",
            "has a nice atmosphere.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_672D")

    TalkEnd(0xFE)
    Return()

    # Function_19_65C9 end

    def Function_20_6731(): pass

    label("Function_20_6731")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6780")

    ChrTalk(
        0xFE,
        (
            "Haha, this penne texture\x01",
            "is irresistable! I'm so\x01",
            "happy㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6849")

    label("loc_6780")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_67E9")

    ChrTalk(
        0xFE,
        (
            "Haha. I'll come here\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As always, it has a\x01",
            "fashionable and nice\x01",
            "atmosphere.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6849")

    label("loc_67E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6849")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6804")
    Call(0, 11)
    Jump("loc_6849")

    label("loc_6804")


    ChrTalk(
        0xFE,
        (
            "Heh, to think there was\x01",
            "a place like this in a\x01",
            "place like this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6849")

    TalkEnd(0xFE)
    Return()

    # Function_20_6731 end

    def Function_21_684D(): pass

    label("Function_21_684D")

    TalkBegin(0xFE)
    Call(0, 22)
    TalkEnd(0xFE)
    Return()

    # Function_21_684D end

    def Function_22_6857(): pass

    label("Function_22_6857")

    OP_4B(0x12, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_93(0x9, 0x5A, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_694B")

    ChrTalk(
        0x12,
        (
            "Ha ha ha, young man. I\x01",
            "see you've got nothing\x01",
            "left.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "...You're good, mister.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You're on the same level\x01",
            "as Wazy... No, maybe\x01",
            "even more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305F(...Hmm? It looks like\x01",
            "he has considerable\x01",
            "skill.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_69AA")

    label("loc_694B")


    ChrTalk(
        0x12,
        (
            "Come, it's your turn\x01",
            "next.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "S-Sure... Wait a moment,\x01",
            "I'm thinking about where\x01",
            "to aim.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69AA")

    OP_4C(0x12, 0xFF)
    OP_4C(0x9, 0xFF)
    TalkEnd(0xFE)
    Return()

    # Function_22_6857 end

    def Function_23_69B6(): pass

    label("Function_23_69B6")

    OP_4B(0x13, 0xFF)
    OP_4B(0x14, 0xFF)
    OP_4B(0x12, 0xFF)

    ChrTalk(
        0x14,
        "Kyah, amazing!\x02",
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
            "Haha. "Aim" is the same\x01",
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
        (
            "Ah! And he even said\x01",
            "that㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "Haha, he's really good.\x02",
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

    # Function_23_69B6 end

    def Function_24_6ADC(): pass

    label("Function_24_6ADC")


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
            "But I'm glad he found\x01",
            "where he was staying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "Hmm. He really did have\x01",
            "a nice face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "But, wasn't he a bit\x01",
            "strange?\x02",
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
        "Yeah, you said it.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    SetScenarioFlags(0x1, 2)
    ClearChrFlags(0x13, 0x10)
    ClearChrFlags(0x14, 0x10)
    Return()

    # Function_24_6ADC end

    def Function_25_6C15(): pass

    label("Function_25_6C15")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C60")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C34")
    Call(0, 23)
    Jump("loc_6C5B")

    label("loc_6C34")


    ChrTalk(
        0xFE,
        (
            "Uhuhu. I met a dreamy\x01",
            "man today㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C5B")

    Jump("loc_6CD5")

    label("loc_6C60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C72")
    Call(0, 24)
    Jump("loc_6CD5")

    label("loc_6C72")


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
            "But I'm glad he found\x01",
            "where he was staying.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CD5")

    TalkEnd(0xFE)
    Return()

    # Function_25_6C15 end

    def Function_26_6CD9(): pass

    label("Function_26_6CD9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CF8")
    Call(0, 23)
    Jump("loc_6D48")

    label("loc_6CF8")


    ChrTalk(
        0xFE,
        (
            "That man wasn't just good\x01",
            "at playing music, we was\x01",
            "good at billiards, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D48")

    Jump("loc_6DEA")

    label("loc_6D4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D5F")
    Call(0, 24)
    Jump("loc_6DEA")

    label("loc_6D5F")


    ChrTalk(
        0xFE,
        (
            "He had a nice face, his singing\x01",
            "and playing were good, and he\x01",
            "was even good at billiards...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But somehow, I felt like\x01",
            "I know him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DEA")

    TalkEnd(0xFE)
    Return()

    # Function_26_6CD9 end

    def Function_27_6DEE(): pass

    label("Function_27_6DEE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E03")
    Call(0, 9)
    Jump("loc_6E69")

    label("loc_6E03")


    ChrTalk(
        0xFE,
        (
            "Hehe. There's nothing\x01",
            "better than drinking\x01",
            "during the day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It spreads throughout\x01",
            "your body.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E69")

    TalkEnd(0xFE)
    Return()

    # Function_27_6DEE end

    def Function_28_6E6D(): pass

    label("Function_28_6E6D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F3D")

    ChrTalk(
        0xFE,
        (
            "I secretly visited the\x01",
            "bar where my little\x01",
            "brother works.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He was embarrassed at\x01",
            "first but then served me\x01",
            "properly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm glad he's\x01",
            "approaching his work\x01",
            "with professionalism.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_6F97")

    label("loc_6F3D")


    ChrTalk(
        0xFE,
        "Moment by moment...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The non-alcoholic\x01",
            "cocktail Azel made... It\x01",
            "was pretty good.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F97")

    TalkEnd(0xFE)
    Return()

    # Function_28_6E6D end

    def Function_29_6F9B(): pass

    label("Function_29_6F9B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_701F")

    ChrTalk(
        0xFE,
        (
            "Uwah! Everyone's wearing\x01",
            "the same thing as Azel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Aww. I want a blue parka\x01",
            "so I can match my\x01",
            "brother.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7058")

    label("loc_701F")


    ChrTalk(
        0xFE,
        (
            "Aww. I want a blue parka\x01",
            "so I can match my\x01",
            "brother.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7058")

    TalkEnd(0xFE)
    Return()

    # Function_29_6F9B end

    def Function_30_705C(): pass

    label("Function_30_705C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_70D1")

    ChrTalk(
        0xFE,
        (
            "I don't really get it,\x01",
            "but for now, let's smash\x01",
            "those armors!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure Wald would\x01",
            "agree!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7101")

    label("loc_70D1")


    ChrTalk(
        0xFE,
        (
            "I don't really get it,\x01",
            "but let's do this!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7101")

    TalkEnd(0xFE)
    Return()

    # Function_30_705C end

    def Function_31_7105(): pass

    label("Function_31_7105")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_719D")

    ChrTalk(
        0xFE,
        (
            "It looks like those\x01",
            "armors haven't entered\x01",
            "Downtown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For now, we made the\x01",
            "residents near Ignis take\x01",
            "shelter indoors, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7230")

    label("loc_719D")


    ChrTalk(
        0xFE,
        (
            "I wish Jed and the\x01",
            "others would help...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't think I'll ever understand\x01",
            "why Wald left us like that, but I\x01",
            "guess it can't be helped...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7230")

    TalkEnd(0xFE)
    Return()

    # Function_31_7105 end

    def Function_32_7234(): pass

    label("Function_32_7234")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_727C")

    ChrTalk(
        0xFE,
        (
            "Just what is that blue\x01",
            "mist outside, I\x01",
            "wonder...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7301")

    label("loc_727C")


    ChrTalk(
        0xFE,
        (
            "H-Hmm... We're only\x01",
            "going to cooperate with\x01",
            "those baldies this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We'll protect Downtown,\x01",
            "for whenever Wald comes\x01",
            "back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7301")

    TalkEnd(0xFE)
    Return()

    # Function_32_7234 end

    def Function_33_7305(): pass

    label("Function_33_7305")

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

    def lambda_745F():
        OP_96(0xFE, 0xFFFFFCE0, 0x0, 0xA28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_745F)

    def lambda_7479():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7479)
    Sleep(400)

    def lambda_748D():
        OP_96(0xFE, 0x2BC, 0x0, 0x960, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_748D)

    def lambda_74A7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_74A7)
    Sleep(400)

    def lambda_74BB():
        OP_96(0xFE, 0xFFFFFE0C, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_74BB)

    def lambda_74D5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_74D5)
    Sleep(400)

    def lambda_74E9():
        OP_96(0xFE, 0x2BC, 0x0, 0x4B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_74E9)

    def lambda_7503():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_7503)
    WaitChrThread(0x101, 1)

    def lambda_7518():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7518)
    WaitChrThread(0x102, 1)

    def lambda_7529():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7529)
    WaitChrThread(0x109, 1)

    def lambda_753A():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_753A)
    WaitChrThread(0x105, 1)

    def lambda_754B():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_754B)
    WaitChrThread(0x105, 2)
    OP_6F(0x10)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xA, 0x0, 0)

    ChrTalk(
        0xA,
        (
            "Welcome. How many of you\x01",
            "are there...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "Hey, you're the Special\x01",
            "Support Section!? And\x01",
            "Wazy's with you!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005FW-Welcome, you said...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x8, 500)

    ChrTalk(
        0x105,
        (
            "#12P#10304FHehe. Most importantly, it\x01",
            "looks like you're running\x01",
            "a real business now.\x02\x03",
            "#10302FWhat about you, Abbas?\x01",
            "Doing well for yourselves,\x01",
            "I guess?\x02",
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
            "More importantly, how nice of you\x01",
            "to come. Since you're here, make\x01",
            "yourselves at home.\x02",
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

    def lambda_77DE():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_77DE)

    def lambda_77EB():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_77EB)

    def lambda_77F8():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_77F8)

    def lambda_7805():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_7805)

    def lambda_7812():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_7812)
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
        (
            "#04100F...Wazy, how is the\x01",
            "Special Support Section?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FWell, I guess it's pretty\x01",
            "comfortable?\x02\x03",
            "#10304FChief and my co-workers\x01",
            "are understanding, and\x01",
            "it's a carefree workplace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FI think you're a little\x01",
            "too carefree, Wazy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10101FThat's right, Wazy. Although you're\x01",
            "an associate member, you are aware\x01",
            "you're a police officer, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FHehe. Though you say that,\x01",
            "this is my style.\x02\x03",
            "#10304FIf you guys are too strict,\x01",
            "a little more and you'll\x01",
            "break into pieces, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00106F...*sigh*. No matter\x01",
            "what you say to Wazy,\x01",
            "it's useless.\x02",
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
            "#12P#00006F(Or rather, I feel like\x01",
            "there's nothing but\x01",
            "problems...)\x02",
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
            "#12P#00105FAnd, might you be lost\x01",
            "without him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04100F...None of us were opposed.\x01",
            "Everything is decided by\x01",
            "Wazy, after all.\x02",
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
        (
            "#12P#10106F(That wasn't much of an\x01",
            "answer...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006F(I wonder if that's just\x01",
            "how he is...)\x02",
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
            "#11PWell, we are lost, but...\x01",
            "We discussed it amongst\x01",
            "the members and agreed.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7DF7():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7DF7)
    Sleep(10)

    def lambda_7E07():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7E07)

    def lambda_7E14():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7E14)
    Sleep(10)

    def lambda_7E24():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7E24)
    Sleep(10)

    ChrTalk(
        0xA,
        (
            "#12POpposition to our parents, situations\x01",
            "at home... For various reasons, these\x01",
            "members have gathered, but...\x02",
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
            "#12PRather, we wonder if our\x01",
            "own opportunities to be\x01",
            "independent are out there.\x02",
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
        "#6P#00002FHaha. I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#N#10102FYou guys seem quite\x01",
            "positive about this.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    ChrTalk(
        0x105,
        (
            "#6P#10304FWell from the start,\x01",
            "Abbas has been in charge\x01",
            "of almost all of Trinity.\x02\x03",
            "#10300FEven if I'm not here, I\x01",
            "think they'll do just\x01",
            "fine on their own.\x02",
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
            "#04100FSpecial Support Section,\x01",
            "we're leaving Wazy to\x01",
            "you for the time being.\x02\x03",
            "Wazy, you too should pay\x01",
            "us no heed, and focus on\x01",
            "your current work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FHehe. I planned to do\x01",
            "that from the start.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x102, 500)

    ChrTalk(
        0x105,
        (
            "#6P#10304FAnd so, I once again\x01",
            "would like to say how\x01",
            "great it is to be here㈱\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)

    ChrTalk(
        0x101,
        (
            "#11P#00006FW-Well, this is going to\x01",
            "be rather difficult,\x01",
            "but...\x02\x03",
            "#00000FAhem, allow me to give\x01",
            "you a warm welcome once\x01",
            "again as well.\x02",
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

    # Function_33_7305 end

    def Function_34_83D0(): pass

    label("Function_34_83D0")

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

    def lambda_84D5():
        OP_96(0xFE, 0x384, 0x0, 0x141E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_84D5)

    def lambda_84EF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_84EF)
    Sleep(400)

    def lambda_8503():
        OP_96(0xFE, 0xFFFFFCE0, 0x0, 0x10FE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8503)

    def lambda_851D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_851D)
    Sleep(400)

    def lambda_8531():
        OP_96(0xFE, 0x4BA, 0x0, 0xEA6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8531)

    def lambda_854B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_854B)
    Sleep(400)

    def lambda_855F():
        OP_96(0xFE, 0xFFFFFDA8, 0x0, 0xBE0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_855F)

    def lambda_8579():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8579)
    Sleep(400)

    def lambda_858D():
        OP_96(0xFE, 0x3E8, 0x0, 0x794, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_858D)

    def lambda_85A7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_85A7)
    Sleep(400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_85F8")

    def lambda_85CD():
        OP_96(0xFE, 0xFFFFFC18, 0x0, 0x60E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_85CD)

    def lambda_85E7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_85E7)
    Jump("loc_8623")

    label("loc_85F8")


    def lambda_85FD():
        OP_96(0xFE, 0xFFFFFC18, 0x0, 0x60E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_85FD)

    def lambda_8617():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_8617)

    label("loc_8623")

    WaitChrThread(0xF4, 1)
    WaitChrThread(0xF5, 1)

    ChrTalk(
        0x105,
        (
            "#12P#10405FOh, it looks like a rare\x01",
            "customer has come in.\x02",
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

    def lambda_8729():
        TurnDirection(0xA, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_8729)

    def lambda_8736():
        TurnDirection(0xB, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_8736)

    def lambda_8743():
        TurnDirection(0x9, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8743)

    def lambda_8750():
        TurnDirection(0x15, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_8750)

    def lambda_875D():
        TurnDirection(0x16, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_875D)
    TurnDirection(0x17, 0x105, 500)

    ChrTalk(
        0x17,
        "#5PY-You!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PW-Wazy!? And the Support\x01",
            "Section!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00005FTestaments and Vipers...\x01",
            "So this is where you all\x01",
            "are.\x02",
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
            "Abbas' the same?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10406FMan. I come back and\x01",
            "there's no room to\x01",
            "breathe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00300FAh, well you make a big\x01",
            "impact, don't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203FFor now, I think it's\x01",
            "best to outline the\x01",
            "situation for them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10403FWell if I suddenly start talking\x01",
            "about orders and the church and such,\x01",
            "the explanation would be kinda long.\x02\x03",
            "#10400FI'll explain it to you guys later.\x01",
            "...That all right with you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11PS-Sure... That aside, we\x01",
            "need to focus on the\x01",
            "current situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10402FHaha, but even so... It\x01",
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
            "#11PT-That's why we did our\x01",
            "very best.\x02",
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
            "#5PSomething like that has happened,\x01",
            "but... We have to make sure Wald\x01",
            "has a place to come back to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PYeah, it's a place\x01",
            "that's important to us\x01",
            "Downtown Saber Vipers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "#5PSome of us, Jed included,\x01",
            "still don't feel like\x01",
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
            "#12P#00109FHaha. You've become a\x01",
            "fine man, Dino.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x17)
    TurnDirection(0x17, 0x102, 500)

    ChrTalk(
        0x17,
        "#5PI-I didn't mean!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x15, 0x17, 500)

    ChrTalk(
        0x15,
        (
            "#5PHaha. It's nothing to be\x01",
            "ashamed of, Dino.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8E53")

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
    Jump("loc_8FE7")

    label("loc_8E53")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8F0C")

    ChrTalk(
        0x109,
        (
            "#N#12P#10103FAnyway, it seems the\x01",
            "President's monsters haven't\x01",
            "appeared in Downtown...\x02\x03",
            "#10100FI think it'll be alright if\x01",
            "we leave this place to these\x01",
            "guys.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_8FCB")

    label("loc_8F0C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8FCB")

    ChrTalk(
        0x106,
        (
            "#N#12P#10703FAnyway, it seems the monsters\x01",
            "the enemy is employing haven't\x01",
            "appeared in Downtown...\x02\x03",
            "#10702FI think it'll be alright if we\x01",
            "leave this place to these\x01",
            "guys.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_8FCB")


    ChrTalk(
        0x101,
        "#6P#00000FYeah, right.\x02",
    )

    CloseMessageWindow()

    label("loc_8FE7")

    TurnDirection(0x17, 0x105, 500)

    ChrTalk(
        0x105,
        (
            "#12P#10404FThere you have it. It's\x01",
            "time for us to go.\x02\x03",
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
            "#5PI don't really get it,\x01",
            "but let's do this!!\x02",
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

    # Function_34_83D0 end

    SaveToFile()

Try(main)
