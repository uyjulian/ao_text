from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c1040.bin",                # FileName
        "c1040",                    # MapName
        "c1040",                    # Location
        0x0015,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 21, 0, 6, 0, 7],
    )

    BuildStringList((
        "c1040",                  # 0
        "Mercy",               # 1
        "Salina",                 # 2
        "Yuggott",               # 3
        "Claris",               # 4
        "bond",                 # 5
        "Craig",               # 6
        "Sanita",               # 7
        "Mary",                 # 8
        "sepia",                 # 9
        "Ohna",                 # 10
        "Azel",                 # 11
    ))

    AddCharChip((
        "chr/ch27600.itc",                   # 00
        "chr/ch33300.itc",                   # 01
        "chr/ch34400.itc",                   # 02
        "chr/ch39000.itc",                   # 03
        "chr/ch27602.itc",                   # 04
        "chr/ch33302.itc",                   # 05
        "chr/ch34200.itc",                   # 06
        "chr/ch10400.itc",                   # 07
        "chr/ch33200.itc",                   # 08
        "chr/ch21802.itc",                   # 09
        "chr/ch22300.itc",                   # 0A
        "chr/ch21800.itc",                   # 0B
        "chr/ch34202.itc",                   # 0C
        "chr/ch34402.itc",                   # 0D
        "chr/ch20500.itc",                   # 0E
        "apl/ch50375.itc",                   # 0F
    ))

    DeclNpc(48880,   29,      4294912296, 135,  261,  0x0, 0,   11,  0,   0,   2,   0,   14,  255,  0)
    DeclNpc(3789,    0,       55279,   90,   261,  0x0, 0,   14,  0,   0,   0,   0,   10,  255,  0)
    DeclNpc(4294964886, 29,      52169,   225,  261,  0x0, 0,   6,   0,   0,   1,   0,   12,  255,  0)
    DeclNpc(3660,    29,      4294910697, 90,   261,  0x0, 0,   7,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(53729,   0,       52729,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(53729,   0,       50729,   0,    261,  0x0, 0,   1,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(53729,   0,       51729,   90,   261,  0x0, 0,   2,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(48349,   0,       3900,    90,   261,  0x0, 0,   3,   0,   0,   3,   0,   19,  255,  0)
    DeclNpc(48880,   29,      4294912296, 135,  389,  0x0, 0,   8,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(48880,   29,      4294912296, 135,  389,  0x0, 0,   10,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(4294949907, 4294966996, 16750,   90,   389,  0x0, 0,   15,  0,   0,   0,   0,   13,  255,  0)

    DeclEvent(0x0000, 0, 28,  52.0,                  -6.980000019073486,    -1.0,                  4.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -26.0,                 3.490000009536743,     0.20000000298023224,   1.0])

    DeclActor(51870,   0,       5760,    2000,    51870,   2000,    5760,    0x007C, 0,  29, 0x0000)

    ChipFrameInfo(772, 0)                                        # 0

    ScpFunction((
        "Function_0_304",          # 00, 0
        "Function_1_3BC",          # 01, 1
        "Function_2_3E7",          # 02, 2
        "Function_3_412",          # 03, 3
        "Function_4_43D",          # 04, 4
        "Function_5_468",          # 05, 5
        "Function_6_493",          # 06, 6
        "Function_7_D35",          # 07, 7
        "Function_8_DE9",          # 08, 8
        "Function_9_27DE",         # 09, 9
        "Function_10_2ACD",        # 0A, 10
        "Function_11_3BF6",        # 0B, 11
        "Function_12_3CF7",        # 0C, 12
        "Function_13_4402",        # 0D, 13
        "Function_14_474B",        # 0E, 14
        "Function_15_5512",        # 0F, 15
        "Function_16_5695",        # 10, 16
        "Function_17_6282",        # 11, 17
        "Function_18_6D53",        # 12, 18
        "Function_19_7A2F",        # 13, 19
        "Function_20_7D10",        # 14, 20
        "Function_21_7E4F",        # 15, 21
        "Function_22_7F32",        # 16, 22
        "Function_23_9703",        # 17, 23
        "Function_24_A218",        # 18, 24
        "Function_25_A3AD",        # 19, 25
        "Function_26_A645",        # 1A, 26
        "Function_27_AC2A",        # 1B, 27
        "Function_28_B938",        # 1C, 28
        "Function_29_B995",        # 1D, 29
    ))


    def Function_0_304(): pass

    label("Function_0_304")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_344"),
        (1, "loc_350"),
        (2, "loc_35C"),
        (3, "loc_368"),
        (4, "loc_374"),
        (5, "loc_380"),
        (6, "loc_38C"),
        (SWITCH_DEFAULT, "loc_398"),
    )


    label("loc_344")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_350")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_35C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_368")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_374")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_380")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_38C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_398")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_3A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3BB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_3BB")

    Return()

    # Function_0_304 end

    def Function_1_3BC(): pass

    label("Function_1_3BC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3E6")
    OP_94(0xFE, 0xFFFFF204, 0xCD3C, 0xFFFFFA24, 0xC602, 0x3E8)
    Sleep(300)
    Jump("Function_1_3BC")

    label("loc_3E6")

    Return()

    # Function_1_3BC end

    def Function_2_3E7(): pass

    label("Function_2_3E7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_411")
    OP_94(0xFE, 0xBC16, 0xFFFF213A, 0xBDCE, 0xFFFF2FB8, 0x3E8)
    Sleep(300)
    Jump("Function_2_3E7")

    label("loc_411")

    Return()

    # Function_2_3E7 end

    def Function_3_412(): pass

    label("Function_3_412")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_43C")
    OP_94(0xFE, 0xC8B4, 0xC9C2, 0xD426, 0xC602, 0x3E8)
    Sleep(300)
    Jump("Function_3_412")

    label("loc_43C")

    Return()

    # Function_3_412 end

    def Function_4_43D(): pass

    label("Function_4_43D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_467")
    OP_94(0xFE, 0xB734, 0xDAC0, 0xAF64, 0xD642, 0x3E8)
    Sleep(300)
    Jump("Function_4_43D")

    label("loc_467")

    Return()

    # Function_4_43D end

    def Function_5_468(): pass

    label("Function_5_468")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_492")
    OP_94(0xFE, 0xC832, 0xFFFF3396, 0xD188, 0xFFFF2036, 0x3E8)
    Sleep(300)
    Jump("Function_5_468")

    label("loc_492")

    Return()

    # Function_5_468 end

    def Function_6_493(): pass

    label("Function_6_493")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_506")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xE, 0x10)
    SetChrPos(0xD, 50370, 30, 55730, 0)
    SetChrPos(0xC, 52120, 120, 53450, 270)
    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrPos(0xF, 54250, 30, 52430, 180)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrPos(0xE, 54290, 0, 50940, 0)
    Jump("loc_D25")

    label("loc_506")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5D2")
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 5800, 30, -100, 270)
    SetChrPos(0xB, 5800, 30, -1290, 270)
    SetChrPos(0x9, -340, 30, 55650, 270)
    SetChrPos(0xA, -1340, 30, 55650, 90)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrFlags(0x8, 0x80)
    SetChrPos(0xC, 50330, 30, 52130, 90)
    SetChrPos(0xD, 51660, 30, 52130, 270)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xD, 0x10)
    SetChrPos(0xE, 46100, 500, 54620, 180)
    SetChrChipByIndex(0xE, 0xD)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    SetChrFlags(0xE, 0x10)
    SetChrPos(0xF, 47200, 20, 53740, 300)
    BeginChrThread(0xF, 0, 0, 0)
    Jump("loc_D25")

    label("loc_5D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_63B")
    SetChrPos(0xD, 50370, 30, 55730, 0)
    SetChrPos(0xC, 52120, 120, 53450, 270)
    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrPos(0xF, 54250, 30, 52430, 180)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrPos(0xE, 54290, 0, 50940, 0)
    Jump("loc_D25")

    label("loc_63B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_END)), "loc_652")
    SetChrFlags(0xB, 0x80)

    label("loc_652")

    SetChrPos(0xD, 50370, 30, 55730, 0)
    SetChrPos(0xC, 52120, 120, 53450, 270)
    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrPos(0xE, 46100, 500, 54620, 180)
    SetChrChipByIndex(0xE, 0xD)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    SetChrPos(0xF, 47200, 20, 53740, 300)
    BeginChrThread(0xF, 0, 0, 0)
    Jump("loc_D25")

    label("loc_6C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_73D")
    SetChrPos(0xC, 52120, 120, 53450, 270)
    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrPos(0xD, 49270, 130, 53870, 90)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrPos(0xF, 47420, 0, 3460, 90)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrPos(0xE, 48680, 0, 3250, 270)
    Jump("loc_D25")

    label("loc_73D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7CE")
    SetChrPos(0xC, 45360, 500, 54620, 180)
    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrSubChip(0xC, 0x1)
    SetChrPos(0xE, 46100, 500, 54620, 180)
    SetChrChipByIndex(0xE, 0xD)
    SetChrSubChip(0xE, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrBattleFlags(0xE, 0x4)
    SetChrSubChip(0xE, 0x2)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x40)
    SetChrPos(0xF, 51660, 0, 51090, 315)
    BeginChrThread(0xF, 0, 0, 3)
    SetChrPos(0xD, 48180, 0, 4450, 270)
    SetChrFlags(0xD, 0x10)
    Jump("loc_D25")

    label("loc_7CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_863")
    SetChrFlags(0x9, 0x80)
    SetChrPos(0xB, 1230, 30, 54660, 225)
    SetChrPos(0xA, 1600, 130, 53880, 270)
    SetChrFlags(0xA, 0x10)
    SetChrChipByIndex(0xA, 0xC)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0xD, 50370, 30, 55730, 45)
    SetChrPos(0xF, 51660, 0, 51090, 315)
    BeginChrThread(0xF, 0, 0, 3)
    SetChrPos(0xE, 54290, 0, 50940, 0)
    TurnDirection(0xE, 0xF, 0)
    Jump("loc_D25")

    label("loc_863")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_94E")
    SetChrPos(0x9, 760, 0, 55810, 270)
    SetChrFlags(0x9, 0x10)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrPos(0xA, -1320, 0, 56010, 90)
    SetChrFlags(0xA, 0x10)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0xD, 52980, 30, 55720, 45)
    SetChrPos(0xF, 54250, 30, 52430, 180)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrFlags(0xF, 0x10)
    SetChrPos(0xE, 54290, 0, 50940, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F6")
    SetChrFlags(0xE, 0x10)

    label("loc_8F6")

    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x8, 49050, 30, -54780, 0)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrFlags(0x8, 0x10)
    SetChrPos(0x10, 49280, 30, -52920, 180)
    SetChrPos(0x11, 52690, 30, -54950, 135)
    SetChrFlags(0x10, 0x10)
    BeginChrThread(0x11, 0, 0, 5)
    Jump("loc_D25")

    label("loc_94E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_9D0")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x8, 49050, 30, -54780, 0)
    BeginChrThread(0x8, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_99F")
    SetChrFlags(0x8, 0x10)

    label("loc_99F")

    SetChrPos(0x10, 49280, 30, -52920, 180)
    SetChrPos(0x11, 47330, 30, -54190, 135)
    SetChrFlags(0x11, 0x10)
    SetChrFlags(0x10, 0x10)
    Jump("loc_D25")

    label("loc_9D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_A48")
    SetChrPos(0xC, 52120, 20, 53450, 270)
    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrPos(0xD, 52980, 30, 55720, 45)
    SetChrPos(0xF, 45490, 650, 55410, 180)
    SetChrFlags(0xF, 0x40)
    BeginChrThread(0xF, 0, 0, 4)
    SetChrFlags(0xF, 0x10)
    SetChrPos(0xE, 46740, 30, 53780, 300)
    SetChrFlags(0xE, 0x10)
    Jump("loc_D25")

    label("loc_A48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_B5E")
    SetChrFlags(0xB, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ACA")
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0xC, 0x40)
    BeginChrThread(0xC, 0, 0, 0)
    SetChrPos(0xC, 53730, 0, 52730, 180)
    ClearChrFlags(0xD, 0x40)
    BeginChrThread(0xD, 0, 0, 0)
    SetChrPos(0xD, 53730, 0, 50730, 0)
    ClearChrFlags(0xE, 0x40)
    SetChrPos(0xE, 53730, 0, 51730, 90)
    Jump("loc_B59")

    label("loc_ACA")

    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xF, 0x40)
    SetChrFlags(0xF, 0x10)
    SetChrPos(0xF, 48700, 30, 54850, 0)
    BeginChrThread(0xF, 0, 0, 0)
    ClearChrFlags(0xC, 0x40)
    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrPos(0xC, 46190, 380, 52360, 0)
    ClearChrFlags(0xD, 0x40)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrPos(0xD, 45240, 380, 52380, 0)
    ClearChrFlags(0xE, 0x40)
    SetChrFlags(0xE, 0x10)
    SetChrPos(0xE, 48700, 0, 55600, 180)

    label("loc_B59")

    Jump("loc_D25")

    label("loc_B5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_BDB")
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrPos(0xC, 52120, 20, 53450, 270)
    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrPos(0xD, 52980, 30, 55720, 45)
    SetChrPos(0xF, 45430, 0, 53990, 90)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrPos(0xE, 46740, 30, 53780, 270)
    SetChrFlags(0xE, 0x10)
    Jump("loc_D25")

    label("loc_BDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_D08")
    SetChrFlags(0xE, 0x10)
    SetChrFlags(0xF, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_END)), "loc_C7B")
    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrPos(0xC, 49200, 150, 53560, 90)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    SetChrPos(0xD, 52040, 150, 53650, 270)
    SetChrPos(0xE, 48350, 0, 2900, 0)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrPos(0xF, 48350, 0, 3900, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 7)), scpexpr(EXPR_END)), "loc_C76")
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x10)

    label("loc_C76")

    Jump("loc_D03")

    label("loc_C7B")

    SetChrPos(0x8, 48470, 30, -54870, 0)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0xC, 49040, 20, -52990, 180)
    SetChrPos(0xD, 47900, 20, -52950, 180)
    SetChrPos(0xE, 49070, 20, -51720, 180)
    SetChrPos(0xF, 48050, 20, -51680, 180)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xD, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_CFD")
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x10)
    ClearChrFlags(0xD, 0x10)

    label("loc_CFD")

    BeginChrThread(0xF, 0, 0, 0)

    label("loc_D03")

    Jump("loc_D25")

    label("loc_D08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_D25")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)

    label("loc_D25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_D34")
    ClearScenarioFlags(0x22, 0)
    Event(0, 27)

    label("loc_D34")

    Return()

    # Function_6_493 end

    def Function_7_D35(): pass

    label("Function_7_D35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D7E")
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_D7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DBD")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)

    label("loc_DBD")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_DD0")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_DD0")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DE8")
    ClearMapObjFlags(0x1, 0x10)
    OP_66(0x0, 0x1)

    label("loc_DE8")

    Return()

    # Function_7_D35 end

    def Function_8_DE9(): pass

    label("Function_8_DE9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1130")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E17")
    Call(0, 9)
    Jump("loc_FB0")

    label("loc_E17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F36")

    ChrTalk(
        0xFE,
        "If my dad was alive ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a guard after all,\x01",
            "Do not give up and fight until the end\x01",
            "You must have chosen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… The members of the Special Affairs Division,\x01",
            "Please give me Noel and Fran.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In order to solve this situation,\x01",
            "Please use it perfectly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10109FAlready … … Mother.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_FB0")

    label("loc_F36")


    ChrTalk(
        0xFE,
        (
            "Everyone in the Special Affairs Division,\x01",
            "Please give me Noel and Fran.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In order to solve this situation,\x01",
            "Please use it perfectly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FB0")

    Jump("loc_112B")

    label("loc_FB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10B1")

    ChrTalk(
        0xFE,
        "If my dad was alive ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a guard after all,\x01",
            "Do not give up and fight until the end\x01",
            "You must have chosen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… The members of the Special Affairs Division,\x01",
            "Please give me Noel and Fran.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In order to solve this situation,\x01",
            "Please use it perfectly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_112B")

    label("loc_10B1")


    ChrTalk(
        0xFE,
        (
            "Everyone in the Special Affairs Division,\x01",
            "Please give me Noel and Fran.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In order to solve this situation,\x01",
            "Please use it perfectly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_112B")

    Jump("loc_27DA")

    label("loc_1130")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_12F4")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1258")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_115B")
    Call(0, 9)
    Jump("loc_1253")

    label("loc_115B")


    ChrTalk(
        0xFE,
        (
            "Azel君も手伝いに来てくれてるし、\x01",
            "It's okay here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if that herb enters,\x01",
            "Yuggott君やSanitaちゃんには\x01",
            "Because I can not touch a finger.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1253")

    ChrTalk(
        0x109,
        "#10101FMother, be careful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Heho, those of Noel\x01",
            "Be careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_1253")

    Jump("loc_12EF")

    label("loc_1258")


    ChrTalk(
        0xFE,
        (
            "Azel君も手伝いに来てくれてるし、\x01",
            "It's okay here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even if that herb enters,\x01",
            "Yuggott君やSanitaちゃんには\x01",
            "Because I can not touch a finger.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12EF")

    Jump("loc_27DA")

    label("loc_12F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1517")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1436")

    ChrTalk(
        0xFE,
        (
            "Mr. Dieter …\x01",
            "Until now, he can be convinced\x01",
            "I guess it was not there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It has happened in this crossbell,\x01",
            "I have no other choice but to convince\x01",
            "To numerous unreasonable events ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…………………………………….\x01",
            "…… His home also ………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FHuh…………?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Hehe, I'm sorry.\x01",
            "It's nothing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1512")

    label("loc_1436")


    ChrTalk(
        0xFE,
        (
            "Anyway, defense forces,\x01",
            "From around the time of the guard\x01",
            "It is hard to get close to the atmosphere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That white uniform is something\x01",
            "Are you trying too hard?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I was living my father,\x01",
            "I liked the uniform of the guard, but hey.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1512")

    Jump("loc_27DA")

    label("loc_1517")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1798")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1719")

    ChrTalk(
        0xFE,
        (
            "Uh……\x01",
            "Change of franc\x01",
            "I wonder if this is the place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's right, I was a little\x01",
            "I wonder if I hold fruits …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FMother ……\x01",
            "I was back.\x02\x03",
            "In the morning I am in Ursula hospital\x01",
            "I told you to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yeah, I just got it\x01",
            "I came back from my wedlock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… Fuu, even so\x01",
            "I'm glad that the franc consciousness is back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Eaves#2RHippopotamus#I told you\x01",
            "To the police of the second division\x01",
            "I really appreciate … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103FYeah……\x01",
            "Again there\x01",
            "I'll come and visit you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yes, I have asked you well.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1793")

    label("loc_1719")


    ChrTalk(
        0xFE,
        (
            "You seem to go to the hospital, are not you?\x01",
            "I am going to go again later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Change clothes to franc\x01",
            "I have to go to the delivery.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1793")

    Jump("loc_27DA")

    label("loc_1798")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1905")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1896")

    ChrTalk(
        0xFE,
        (
            "It is occupation of Mainz … ….\x01",
            "It is called a terrorist who appeared at the trade meeting,\x01",
            "A big incident will continue …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When the guard is working on a solution\x01",
            "It was a story to say,\x01",
            "It makes me cranky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you head for us\x01",
            "You'd better be careful enough.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1900")

    label("loc_1896")


    ChrTalk(
        0xFE,
        (
            "Examples of occupation cases,\x01",
            "It makes me cranky …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you head for us\x01",
            "You'd better be careful enough.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1900")

    Jump("loc_27DA")

    label("loc_1905")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1A1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19BA")

    ChrTalk(
        0xFE,
        "It will rain today, too ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is also a burden to go shopping,\x01",
            "Today 's dinner is properly leftovers\x01",
            "I wonder if I can finish it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F(It's quiet and quiet, right?\x01",
            "Mother ……)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1A1A")

    label("loc_19BA")


    ChrTalk(
        0xFE,
        (
            "Today 's dinner is suitable leftovers\x01",
            "Let's finish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can not put it in the rain\x01",
            "It is troublesome.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A1A")

    Jump("loc_27DA")

    label("loc_1A1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1AC2")

    ChrTalk(
        0xFE,
        (
            "Yuggott君に日曜学校の宿題を\x01",
            "I am teaching you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, looking at the problem\x01",
            "I taught Noel and Fran to study\x01",
            "My memories will revive …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27DA")

    label("loc_1AC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1BC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B4D")

    ChrTalk(
        0xFE,
        (
            "お向かいのYuggott君、\x01",
            "Recently alone with an answering machine\x01",
            "It seems I got to be able to do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hehe, it is kind of awkward.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1BC0")

    label("loc_1B4D")


    ChrTalk(
        0xFE,
        (
            "Salinaちゃんには\x01",
            "As you see the situation regularly\x01",
            "I'm being asked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even snacks later\x01",
            "I wonder if I should take it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BC0")

    Jump("loc_27DA")

    label("loc_1BC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1D17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C9C")

    ChrTalk(
        0xFE,
        (
            "今日は向かいのSalinaちゃんが\x01",
            "It seems to be late at work,\x01",
            "Yuggottくんの世話を頼まれてるの。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Salinaちゃんも帰ってきたら\x01",
            "It will be hungry … …\x01",
            "I have to prepare lots of dinner.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1D12")

    label("loc_1C9C")


    ChrTalk(
        0xFE,
        "I love caring for my kids, do not you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, that's so hard\x01",
            "Stick with delicious things with your arms\x01",
            "Let's make it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D12")

    Jump("loc_27DA")

    label("loc_1D17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1E38")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DD0")

    ChrTalk(
        0xFE,
        (
            "Today Franc\x01",
            "The job of the operator\x01",
            "I was told I was busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyhow,\x01",
            "The commerce conference is also real production.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If it ends without anything\x01",
            "I do not mind ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1E33")

    label("loc_1DD0")


    ChrTalk(
        0xFE,
        (
            "Ah……\x01",
            "If it francs, again\x01",
            "Forget the box lunch ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It can not be helped, later\x01",
            "Let's say that we will deliver it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E33")

    Jump("loc_27DA")

    label("loc_1E38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1E46")
    Jump("loc_27DA")

    label("loc_1E46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2113")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_207D")

    ChrTalk(
        0xFE,
        (
            "Well, I bought it at a department store\x01",
            "Premium cookies\x01",
            "It should have been somewhere ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FOr, Mother?\x01",
            "Did you mean ……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x109, 0)

    ChrTalk(
        0xFE,
        (
            "Yeah, to the franc\x01",
            "I was thinking of putting it in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The police, too, the commerce meeting is approaching\x01",
            "You're busy quite a bit, are not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FOh, that's my mum.\x01",
            "I'm at work.\x01",
            "That's not much …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, Fran is pleased\x01",
            "Something else is wrong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, yes, because it's been a big deal\x01",
            "Also to the mission support department next time ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106FYou do not have to come!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009F(This is my pace … ….\x01",
            "  フランはClarisさんに\x01",
            "It may be similar. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    OP_93(0xB, 0x5A, 0x0)
    ClearChrFlags(0xB, 0x10)
    Jump("loc_210E")

    label("loc_207D")


    ChrTalk(
        0xFE,
        (
            "The police, too, the commerce meeting is approaching\x01",
            "I guess you are busy … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Insert into the franc\x01",
            "I have to take it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106F(Is it okay …?)\x02",
    )

    CloseMessageWindow()

    label("loc_210E")

    Jump("loc_27DA")

    label("loc_2113")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_239D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22DA")

    ChrTalk(
        0xFE,
        (
            "by the way……\x01",
            "You guys, driving a car\x01",
            "You got it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Noel was not noisy?\x01",
            "This child, when it comes to car … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112FWell, that's not the case.\x01",
            "…… Hey, everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FWell, nothing also\x01",
            "I do not feel like it is ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FTaking a story about performance by being crazy\x01",
            "You taught me a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106FYeah! Is that so? Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309FHuff, unexpectedly\x01",
            "It sounds like you did not realize.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Whew ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2398")

    label("loc_22DA")


    ChrTalk(
        0xFE,
        (
            "As this child, if it comes to a driving car\x01",
            "It's really annoying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even when I got on the armored car for the first time in the guard,\x01",
            "How is speed, durability like this …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FOkay, I know.\x01",
            "Stop it already Mom!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2398")

    Jump("loc_27DA")

    label("loc_239D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_27DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2692")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x109, 0)

    ChrTalk(
        0xFE,
        (
            "Noel,\x01",
            "Rumored to the Special Affairs Division\x01",
            "I heard that he entered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FWell, strictly\x01",
            "Because it is the name of \"seconded\"\x01",
            "Somewhat different …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Already, you do\x01",
            "You have pretty detailed character.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You can work with you,\x01",
            "I was pleased as Fran Franca was dancing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102FHuhu, you can see the sight.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FHa, when Fran? …\x01",
            "untill forever\x01",
            "It seems like a child.\x02\x03",
            "#10109FWell, of course\x01",
            "I am also happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHuh, you guys sisters\x01",
            "Really, you are on good terms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In a sense, as a parent,\x01",
            "I am worried about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even though both of them are in good condition,\x01",
            "In this case the giver's giver\x01",
            "I am in trouble ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106FOr, mother ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(my mother……\x01",
            "Not only my sisters\x01",
            "My parents and children are also good friends. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12F, 3)
    Jump("loc_27DA")

    label("loc_2692")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2786")

    ChrTalk(
        0xFE,
        (
            "Noel, occasionally at home\x01",
            "Let's face it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FWell, but recently\x01",
            "You looked very well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since my workplace was getting closer,\x01",
            "You said I should come more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FAlready, so much\x01",
            "If I can not be tolerated …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_27DA")

    label("loc_2786")


    ChrTalk(
        0xFE,
        (
            "Noel, occasionally\x01",
            "Let's face it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mother, anytime\x01",
            "I'll be waiting here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27DA")

    TalkEnd(0xFE)
    Return()

    # Function_8_DE9 end

    def Function_9_27DE(): pass

    label("Function_9_27DE")

    OP_4B(0xB, 0xFF)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xB, 0x109, 500)

    ChrTalk(
        0xB,
        "Oh … it is not Noel!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102FMother … good.\x01",
            "He seems to be doing fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "You are for a while\x01",
            "I was worried because I did not show my face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "For a while I'm working in a national defense army\x01",
            "Did not you go home?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10108FWell, that is ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "…… Haha, that's okay.\x01",
            "You did it a lot too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I heard that Fran was also discharged from the hospital,\x01",
            "You act with you, do not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, accompany us\x01",
            "I am doing my best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Huhu, if it was you then to me\x01",
            "I have no right to say anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Noel, later\x01",
            "As you will feel better,\x01",
            "Follow your favorite path.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Being a goddess\x01",
            "To be ashamed to your father,\x01",
            "Do not regret your way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F… Yeah, I got it!\x02",
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2AC2")
    OP_93(0xB, 0x5A, 0x0)
    Jump("loc_2AC9")

    label("loc_2AC2")

    OP_93(0xB, 0x10E, 0x0)

    label("loc_2AC9")

    SetScenarioFlags(0x1BA, 3)
    Return()

    # Function_9_27DE end

    def Function_10_2ACD(): pass

    label("Function_10_2ACD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2C3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BAB")

    ChrTalk(
        0xFE,
        (
            "Azelは今日は\x01",
            "I am going to the old town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Before me,\x01",
            "When you leave your family at such a time\x01",
            "It may be angry, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now for friends and everyone,\x01",
            "I just want you to work very hard.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2C38")

    label("loc_2BAB")


    ChrTalk(
        0xFE,
        (
            "Azelも一人前ですし、\x01",
            "What I'm saying at random\x01",
            "I decided to stop it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Now for friends and everyone,\x01",
            "I just want you to work very hard.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C38")

    Jump("loc_3BF2")

    label("loc_2C3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2D76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D36")
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Azelが大急ぎで旧市街から\x01",
            "I came back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanks to you being scared and crying\x01",
            "Yuggottも落ち着いてくれて……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "No, I'm not crying!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xA, 500)

    ChrTalk(
        0xFE,
        (
            "Hehe, that's right.\x01",
            "Yuggottは強い子だもんね。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x0, 1)
    Jump("loc_2D71")

    label("loc_2D36")


    ChrTalk(
        0xFE,
        (
            "……とにかく、Azelが\x01",
            "I was relieved to come back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D71")

    Jump("loc_3BF2")

    label("loc_2D76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2EEC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E64")

    ChrTalk(
        0xFE,
        (
            "President Dieter was saying\x01",
            "\"Inexplicable accident\" … …\x01",
            "I was listening to the story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But that is what the two great countries have made\x01",
            "It was because of …\x01",
            "It is honest and horrible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, independence is\x01",
            "I think that it is necessary.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2EE7")

    label("loc_2E64")


    ChrTalk(
        0xFE,
        (
            "もし、YuggottやAzelが\x01",
            "\"Inexplicable accident\"\x01",
            "I thought it would be caught … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, independence is\x01",
            "I think that it is necessary.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EE7")

    Jump("loc_3BF2")

    label("loc_2EEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3045")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FC4")

    ChrTalk(
        0xFE,
        (
            "Azel、チームの仲間と一緒に\x01",
            "Reconstruction of old city\x01",
            "I seem to be helping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Let's work for others\x01",
            "I can not think of that old girl\x01",
            "It is an action.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, as my sister\x01",
            "It is somehow proud.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3040")

    label("loc_2FC4")


    ChrTalk(
        0xFE,
        (
            "Tsunken to the front anyway,\x01",
            "I was a child who was going to do something ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My younger brother really changed.\x01",
            "姉としてIt is somehow proud.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3040")

    Jump("loc_3BF2")

    label("loc_3045")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_30B6")

    ChrTalk(
        0xFE,
        "It's scary, is not it an occupation … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Today is my job,\x01",
            "I will take a day off just in case.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BF2")

    label("loc_30B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3125")

    ChrTalk(
        0xFE,
        (
            "Yesterday, there was a derailment accident around\x01",
            "I heard that a big monster has been witnessed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I am scared somewhat ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3BF2")

    label("loc_3125")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3133")
    Jump("loc_3BF2")

    label("loc_3133")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3144")
    Call(0, 11)
    Jump("loc_3BF2")

    label("loc_3144")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3241")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31FC")

    ChrTalk(
        0xFE,
        (
            "今日は、Yuggottは\x01",
            "I am going to Sunday school.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Azelは日曜学校を\x01",
            "It was a child that tends to skimp … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "せめてYuggottには\x01",
            "I want you to study hard.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_323C")

    label("loc_31FC")


    ChrTalk(
        0xFE,
        (
            "Oh, no\x01",
            "I have to go to work soon\x01",
            "You can not do it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_323C")

    Jump("loc_3BF2")

    label("loc_3241")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_34FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_346D")

    ChrTalk(
        0xFE,
        (
            "昨日、Azelの働いているバーに\x01",
            "It seems that weird customers came.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With a white coat on blond hair,\x01",
            "He was the one who carried the lute\x01",
            "I see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although I was not asking, I started playing,\x01",
            "You urinate a female customer who was coming\x01",
            "I thought that it was all you wanted to do.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 2)), scpexpr(EXPR_END)), "loc_3400")
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
        "#00006F(It is a story of His Imperial Highness, probably.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F(Probably, it certainly is.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3465")

    label("loc_3400")


    ChrTalk(
        0x101,
        (
            "#00005F(Lute on blond … ….\x01",
            "Like the one I saw somewhere recently …? )\x02\x03",
            "#00004F(… well, nothing).\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3465")

    SetScenarioFlags(0x0, 1)
    Jump("loc_34F9")

    label("loc_346D")


    ChrTalk(
        0xFE,
        (
            "I usually do things at a store at home\x01",
            "あまり報告しないAzelが\x01",
            "Because I said that … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That customer,\x01",
            "Happy Hen\x01",
            "I guess it was.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34F9")

    Jump("loc_3BF2")

    label("loc_34FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3649")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35CE")

    ChrTalk(
        0xFE,
        (
            "今日は、向かいのClarisさんは\x01",
            "I seem to be out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Clarisさんには\x01",
            "いつもYuggottを見てもらって\x01",
            "I am indebted to you … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "今度、お礼をしないとYou can not do it.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3644")

    label("loc_35CE")


    ChrTalk(
        0xFE,
        (
            "Clarisさんには\x01",
            "いつもYuggottを見てもらって\x01",
            "I am indebted to you … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "今度、お礼をしないとYou can not do it.\x02",
    )

    CloseMessageWindow()

    label("loc_3644")

    Jump("loc_3BF2")

    label("loc_3649")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3768")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_370B")

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
    SetScenarioFlags(0x0, 1)
    Jump("loc_3763")

    label("loc_370B")


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

    label("loc_3763")

    Jump("loc_3BF2")

    label("loc_3768")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3857")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37EE")

    ChrTalk(
        0xFE,
        (
            "Since work is off today,\x01",
            "I spend it with my brother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, well ….\x01",
            "Pissing guardian in a running pedestrian\x01",
            "A little……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3852")

    label("loc_37EE")


    ChrTalk(
        0xFE,
        (
            "I do not care about hunger\x01",
            "What should I do ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Only in such a case\x01",
            "Azelはいないんですよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3852")

    Jump("loc_3BF2")

    label("loc_3857")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3BF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AC2")
    TurnDirection(0xFE, 0x105, 0)

    ChrTalk(
        0xFE,
        "Oh, are you …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FOh, sure.\x01",
            "Azelの姉上だったかな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FEr …\x01",
            "Are you acquainted?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304Fフフ、彼女の弟のAzelは\x01",
            "It is a member of Tests.\x02\x03",
            "#10300FCertainly before Oita, let me quit him\x01",
            "\"Trinity\" until\x01",
            "Have not you got in?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FTo get in, …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Um, that section\x01",
            "We apologize for the inconvenience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At that time absolutely,\x01",
            "Azelをチームから\x01",
            "I want to let you go … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FIn that sword curtain\x01",
            "Everyone of the tests\x01",
            "It seems she was surprised.\x02\x03",
            "#10309FHuh, that is what she loves\x01",
            "It is a puzzle to make it work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F(Why, what is the strangers … …)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12F, 4)
    Jump("loc_3BF2")

    label("loc_3AC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B7D")

    ChrTalk(
        0xFE,
        (
            "弟のAzelは《トリニティ》で\x01",
            "I am working part-time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because it is a place where security is bad\x01",
            "At first I was worried ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because it continues properly\x01",
            "I am a little relieved.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3BF2")

    label("loc_3B7D")


    ChrTalk(
        0xFE,
        (
            "ふう、Azelったら\x01",
            "Most of the team\x01",
            "He does not talk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Do not worry too much.\x01",
            "I want it but ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BF2")

    TalkEnd(0xFE)
    Return()

    # Function_10_2ACD end

    def Function_11_3BF6(): pass

    label("Function_11_3BF6")

    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C86")

    ChrTalk(
        0x9,
        (
            "Well then, my sister,\x01",
            "I will go to work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Yuggott、\x01",
            "Please close the door properly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Yes, leave it to me.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3CEE")

    label("loc_3C86")


    ChrTalk(
        0x9,
        (
            "Yes Yes,\x01",
            "Even if your sister does not see it,\x01",
            "You must do homework properly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I know, I know ~.\x02",
    )

    CloseMessageWindow()

    label("loc_3CEE")

    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_11_3BF6 end

    def Function_12_3CF7(): pass

    label("Function_12_3CF7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3E8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DFC")

    ChrTalk(
        0xFE,
        (
            "Look at the pale tree that went outside\x01",
            "I was very scared ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Onii-chan\x01",
            "It's all right, I do something.\x01",
            "It encouraged me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No matter how much older brother he is\x01",
            "I do not think I can do it ….\x01",
            "Thanks, I cheerfully came.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3E87")

    label("loc_3DFC")


    ChrTalk(
        0xFE,
        (
            "I am afraid of looking at pale trees\x01",
            "お兄ちゃんがIt encouraged me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Eh, after all\x01",
            "Older brother is cool.\x01",
            "Thanks to you I'm fine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E87")

    Jump("loc_43FE")

    label("loc_3E8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3ECD")

    ChrTalk(
        0xFE,
        (
            "If you get on your brother\x01",
            "Surely it's okay.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43FE")

    label("loc_3ECD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3F5B")

    ChrTalk(
        0xFE,
        (
            "Crossbell gets drilled ……\x01",
            "After all, what is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I do not understand well.\x01",
            "I wonder if mr. marble understands … ….\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43FE")

    label("loc_3F5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3FC9")

    ChrTalk(
        0xFE,
        (
            "I, too, something\x01",
            "I wonder if I can help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To the older brother in the old city\x01",
            "Let's go or go?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43FE")

    label("loc_3FC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4031")

    ChrTalk(
        0xFE,
        (
            "To some extent seriously\x01",
            "It seems to be getting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Azel兄ちゃん、\x01",
            "I wonder if I will come back …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43FE")

    label("loc_4031")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_40A4")

    ChrTalk(
        0xFE,
        (
            "Yesterday, the train\x01",
            "You said you fell down?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's scary, is not it?\x01",
            "Why is that so\x01",
            "Have they become it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43FE")

    label("loc_40A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_41B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4163")
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xFE,
        "Oh, I do not want any homework.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "がんばって、Yuggott君。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "My aunt rewards me\x01",
            "I have prepared a snack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "really~! Is it?\x01",
            "Well, I will do my best!\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x0, 2)
    Jump("loc_41AC")

    label("loc_4163")


    ChrTalk(
        0xFE,
        "Well, 14 × 23 is …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, the multiplication of two digits is\x01",
            "It is difficult.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41AC")

    Jump("loc_43FE")

    label("loc_41B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_41C2")
    Call(0, 11)
    Jump("loc_43FE")

    label("loc_41C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_41D0")
    Jump("loc_43FE")

    label("loc_41D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_425C")

    ChrTalk(
        0xFE,
        (
            "Recently, about once every 3 days\x01",
            "My older brother is coming back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Try something like snacks at the store\x01",
            "It brings us back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43FE")

    label("loc_425C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_42E4")

    ChrTalk(
        0xFE,
        (
            "Clarisおばちゃん、\x01",
            "I told you I am going to the cathedral today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the way, the same day last month\x01",
            "I feel like I went there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43FE")

    label("loc_42E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_42F2")
    Jump("loc_43FE")

    label("loc_42F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4376")

    ChrTalk(
        0xFE,
        (
            "My sister, I'm a prison fighter\x01",
            "I do not understand how to do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I guess we have no choice.\x01",
            "Is it okay with your residence?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43FE")

    label("loc_4376")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_43FE")

    ChrTalk(
        0xFE,
        (
            "Azel兄ちゃん、\x01",
            "Bartender in old town\x01",
            "I'm doing it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hey, that's cool.\x01",
            "It is my brother pride ~.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43FE")

    TalkEnd(0xFE)
    Return()

    # Function_12_3CF7 end

    def Function_13_4402(): pass

    label("Function_13_4402")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4609")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x105, 500)

    ChrTalk(
        0xFE,
        (
            "That … … Wow, Wadi! Is it?\x01",
            "Did you return to the crossbells!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10400Fフフ、久しぶりAzel。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That dress is united … and to it\x01",
            "Where is Abbas? Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404FWhat I'd like to hear\x01",
            "There will be various things,\x01",
            "I am bad but I do not have time now.\x02\x03",
            "#10400FI will explain slowly later,\x01",
            "Now my sister and my brother\x01",
            "You should keep it firmly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "あ、あAh……\x01",
            "Indeed it is such a case now\x01",
            "I do not think so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "But I'm glad that it was okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10402FHuh, you too.\x01",
            "… Well then, see you later.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BA, 4)
    Jump("loc_4747")

    label("loc_4609")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46C8")

    ChrTalk(
        0xFE,
        (
            "The monster wandering outside\x01",
            "There is no appearance coming inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… However, I am not prohibited.\x01",
            "I have to watch out for sure … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "姉さんとYuggottは\x01",
            "I'll definitely protect … …!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4747")

    label("loc_46C8")


    ChrTalk(
        0xFE,
        (
            "A monster wandering outside\x01",
            "There is no appearance of entering inside … …\x01",
            "I am not prohibited.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "姉さんとYuggottは\x01",
            "I'll definitely protect … …!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4747")

    TalkEnd(0xFE)
    Return()

    # Function_13_4402 end

    def Function_14_474B(): pass

    label("Function_14_474B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_475C")
    Jump("loc_550E")

    label("loc_475C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_476A")
    Jump("loc_550E")

    label("loc_476A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_499D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4860")

    ChrTalk(
        0xFE,
        (
            "Today, crossbells\x01",
            "You are supposed to leave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I packed up in a hurry, but ….\x01",
            "This book seems to be bulky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I will give it to you if it's okay.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '沐浴阳光的阿尼艾丝11卷'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('沐浴阳光的阿尼艾丝11卷', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x189, 2)
    Jump("loc_4998")

    label("loc_4860")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4903")

    ChrTalk(
        0xFE,
        (
            "From the Imperial government\x01",
            "An evacuation order is coming down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Today crossbells on the railroad\x01",
            "I will leave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The station seems to be considerably crowded,\x01",
            "I have to hurry.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4998")

    label("loc_4903")


    ChrTalk(
        0xFE,
        (
            "Crossover in this form\x01",
            "Although I thought that I would leave … …\x01",
            "My family is the first for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems to be crowded,\x01",
            "I have to catch the train as soon as possible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4998")

    Jump("loc_550E")

    label("loc_499D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4AC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A64")

    ChrTalk(
        0xFE,
        (
            "Families in the Empire\x01",
            "I worried you and gave me a letter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There was such a case,\x01",
            "Me too early\x01",
            "I would like to return to my hometown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Once at the head office\x01",
            "I wonder if I need to consult.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4ABE")

    label("loc_4A64")


    ChrTalk(
        0xFE,
        (
            "Family worry\x01",
            "I tried it but … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I managed to get back to the empire\x01",
            "I have to take a setup.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4ABE")

    Jump("loc_550E")

    label("loc_4AC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4B54")

    ChrTalk(
        0xFE,
        (
            "Armed group to Mainz\x01",
            "I do not know why …\x01",
            "It is unheard of, this is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, to solve it sooner\x01",
            "There is no choice but to wish for the goddess … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_550E")

    label("loc_4B54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4C6C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BF0")

    ChrTalk(
        0xFE,
        (
            "My wife and daughter who came to play,\x01",
            "I went back to the empire today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The derailment accident of yesterday\x01",
            "The liver really got cold … …\x01",
            "I wish it was recovered soon.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4C67")

    label("loc_4BF0")


    ChrTalk(
        0xFE,
        (
            "Even so ……\x01",
            "With my wife and daughter for the first time in a while\x01",
            "I was able to spend it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, somehow in reverse\x01",
            "Although the relief has arrived.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C67")

    Jump("loc_550E")

    label("loc_4C6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4C7A")
    Jump("loc_550E")

    label("loc_4C7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4D03")

    ChrTalk(
        0xFE,
        (
            "Really……\x01",
            "You are leaving already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Still feeling a lonely feeling for a while\x01",
            "I will let you … ….\x01",
            "I asked for your kind regards to my child.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_550E")

    label("loc_4D03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4E2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DA7")

    ChrTalk(
        0xFE,
        (
            "My wife and daughter from my parents' home\x01",
            "He came to see me ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I will come without contact\x01",
            "I was surprised, but …\x01",
            "I'm happy.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x10)
    OP_93(0x8, 0x0, 0x0)
    SetScenarioFlags(0x0, 0)
    Jump("loc_4E29")

    label("loc_4DA7")


    ChrTalk(
        0xFE,
        (
            "Okay, then yesterday's train ……\x01",
            "I wish they had contacted me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can not do any family service\x01",
            "I am sorry, are not you?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E29")

    Jump("loc_550E")

    label("loc_4E2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4EA6")

    ChrTalk(
        0xFE,
        (
            "Depending on the development of the trade meeting\x01",
            "It will also affect the stock price … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a securities man I\x01",
            "I can not miss the trend.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_550E")

    label("loc_4EA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5114")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F50")

    ChrTalk(
        0xFE,
        (
            "From around yesterday,\x01",
            "向かいのbondさん一家の\x01",
            "It seems that the domestic cat has gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I also cooperated and looked for it,\x01",
            "I can not find it after all …\x01",
            "What should I do?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_510F")

    label("loc_4F50")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5090")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_500A")

    ChrTalk(
        0xFE,
        (
            "おや、bondさん一家の猫を\x01",
            "Are you going searching?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My daughter started crying since yesterday.\x01",
            "I feel sorry for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I managed to figure it out\x01",
            "Do it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_508B")

    label("loc_500A")


    ChrTalk(
        0xFE,
        (
            "As the cats are gone,\x01",
            "My daughter started crying since yesterday.\x01",
            "I feel sorry for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I managed to figure it out\x01",
            "Do it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_508B")

    Jump("loc_510F")

    label("loc_5090")


    ChrTalk(
        0xFE,
        (
            "Okae's daughter's\x01",
            "I heard a joyful voice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Apparently cats\x01",
            "You seem to have found it safely.\x01",
            "It was good.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_510F")

    Jump("loc_550E")

    label("loc_5114")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_5278")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51F4")

    ChrTalk(
        0xFE,
        (
            "お向かいのbondさん一家は、\x01",
            "Originally in a residential area\x01",
            "I heard he lived there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "However, there are various circumstances\x01",
            "I heard he came here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even though,\x01",
            "That family is warm and bright.\x01",
            "I want to learn an apprentice.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_5273")

    label("loc_51F4")


    ChrTalk(
        0xFE,
        (
            "Oppasan is\x01",
            "From the prime location of the residential area\x01",
            "I came here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems that there are various circumstances … …\x01",
            "I want to learn their brightness.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5273")

    Jump("loc_550E")

    label("loc_5278")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_53D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_535A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_529D")
    Call(0, 15)
    Jump("loc_5355")

    label("loc_529D")

    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xC,
        (
            "A variety of thoughts\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It will cause inconvenience,\x01",
            "Thank you for your consideration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No, no problem.\x01",
            "If there is something in trouble\x01",
            "Please say anything.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)

    label("loc_5355")

    Jump("loc_53CE")

    label("loc_535A")


    ChrTalk(
        0xFE,
        (
            "何でも、bondさんは\x01",
            "It is the same securities man as me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, this is a good negotiation\x01",
            "Maybe it will be.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53CE")

    Jump("loc_550E")

    label("loc_53D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_550E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54AC")

    ChrTalk(
        0xFE,
        (
            "The destructive wrestlers are opposite\x01",
            "I lived there … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I came home a few months ago,\x01",
            "I'm completely sad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Early,\x01",
            "Someone new people\x01",
            "I wonder if I will move …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_550E")

    label("loc_54AC")


    ChrTalk(
        0xFE,
        (
            "After all, if you are single appointment,\x01",
            "It is truly lonely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Across the street\x01",
            "I wonder if I will move …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_550E")

    TalkEnd(0xFE)
    Return()

    # Function_14_474B end

    def Function_15_5512(): pass

    label("Function_15_5512")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0xC,
        "And that's why ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It is also troublesome from now on\x01",
            "I think that it is,\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "ほら、Maryも挨拶するのよ。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Meow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Huhu, everyone\x01",
            "You seem to be friendly, are not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If there is something troubled,\x01",
            "Please depend on it anytime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "ええ、Thank you very much.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x10)
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x10)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    OP_4C(0xF, 0xFF)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x0, 7)
    Return()

    # Function_15_5512 end

    def Function_16_5695(): pass

    label("Function_16_5695")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_56BE")
    Call(0, 22)
    Return()

    label("loc_56BE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_56F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56F2")
    Call(0, 23)
    Return()

    label("loc_56F2")

    Call(0, 25)
    Return()

    label("loc_56F6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5886")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57EC")

    ChrTalk(
        0xFE,
        (
            "A company that was in IBC,\x01",
            "A small lending property to the office\x01",
            "It is supposed to be resumed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because I was away from work for a while\x01",
            "I have to prepare properly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To support three people and one family member\x01",
            "I would like to do my best.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5881")

    label("loc_57EC")


    ChrTalk(
        0xFE,
        (
            "A company that was in IBC,\x01",
            "A small lending property to the office\x01",
            "It is supposed to be resumed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To support three people and one family member\x01",
            "I would like to do my best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5881")

    Jump("loc_627E")

    label("loc_5886")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5912")

    ChrTalk(
        0xFE,
        (
            "Anyway, there is also a martial decree coming out\x01",
            "You'd better stay inside the house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's okay, this situation\x01",
            "There is no reason to continue so much ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_627E")

    label("loc_5912")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5A65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59E8")

    ChrTalk(
        0xFE,
        (
            "That declaration, the Empire and the Republic\x01",
            "I guessed it strongly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe Cross Bell\x01",
            "It may be in a dangerous situation …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But no matter what happens\x01",
            "My family will absolutely protect them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5A60")

    label("loc_59E8")


    ChrTalk(
        0xFE,
        (
            "Anyways……\x01",
            "Now that we grasp the situation\x01",
            "I need calm judgment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Family absolutely\x01",
            "I will protect you … ….\x01",
            "No matter what happens.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A60")

    Jump("loc_627E")

    label("loc_5A65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5BFF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B69")

    ChrTalk(
        0xFE,
        (
            "The company I work for is\x01",
            "I was in the IBC building … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As you know,\x01",
            "Now turn it into rubble.\x01",
            "In fact, it is closed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although there were no human injuries,\x01",
            "By business restart\x01",
            "It will take time …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It's a troubling thing.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5BFA")

    label("loc_5B69")


    ChrTalk(
        0xFE,
        (
            "Because the attacker destroyed the IBC building\x01",
            "My company is also closed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "…… The circumference of our house is raid\x01",
            "Even if I was not pleased,\x01",
            "It might be good to be … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BFA")

    Jump("loc_627E")

    label("loc_5BFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5C61")

    ChrTalk(
        0xFE,
        (
            "But,\x01",
            "It became a serious thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The aim of the armed group and the\x01",
            "What is it ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_627E")

    label("loc_5C61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5CEA")

    ChrTalk(
        0xFE,
        (
            "after a long time,\x01",
            "I got a day off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It is also raining,\x01",
            "Today with my family\x01",
            "I will spend it relaxing.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    SetChrSubChip(0xC, 0x1)
    Return()

    label("loc_5CEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5CF8")
    Jump("loc_627E")

    label("loc_5CF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_5D06")
    Jump("loc_627E")

    label("loc_5D06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5D14")
    Jump("loc_627E")

    label("loc_5D14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5E6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DF0")

    ChrTalk(
        0xFE,
        (
            "Mercyさんとは\x01",
            "The fields of work are very similar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sometimes in that room,\x01",
            "Together with stock movements\x01",
            "I predict it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Empire's securities man also\x01",
            "I have unique eyes.\x01",
            "It's pretty funny.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5E69")

    label("loc_5DF0")


    ChrTalk(
        0xFE,
        (
            "Well … … soon\x01",
            "I have to go to the office.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am also worried about the trade meeting … …\x01",
            "Crossbell Times'\x01",
            "I have no choice but to wait for coverage.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E69")

    Jump("loc_627E")

    label("loc_5E6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5FAE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5F5F")

    ChrTalk(
        0xFE,
        (
            "No, but to you guys\x01",
            "I can not help being helped\x01",
            "I'm really happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Tentatively, after a while\x01",
            "I also went to the central square\x01",
            "I am going to continue the search.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If something happen,\x01",
            "I want you to call out anytime.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FA9")

    label("loc_5F5F")


    ChrTalk(
        0xFE,
        "You guys, thank you very much for today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I will never forget this kindness.\x02",
    )

    CloseMessageWindow()

    label("loc_5FA9")

    Jump("loc_627E")

    label("loc_5FAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6127")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60B3")

    ChrTalk(
        0xFE,
        (
            "Before you can work at home\x01",
            "I had facilities, but ….\x01",
            "I did not do that here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Like other employees,\x01",
            "To a company in IBC\x01",
            "I decided to commute to work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To some extent after moving\x01",
            "It calms down,\x01",
            "I have to get down to business.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6122")

    label("loc_60B3")


    ChrTalk(
        0xFE,
        (
            "But …\x01",
            "Commuting is also not bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I got tired and came home\x01",
            "What you can say \"going home\"\x01",
            "I'm pretty happy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6122")

    Jump("loc_627E")

    label("loc_6127")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6275")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6209")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_614C")
    Call(0, 15)
    Jump("loc_6204")

    label("loc_614C")

    OP_4B(0x8, 0xFF)

    ChrTalk(
        0xC,
        (
            "A variety of thoughts\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "It will cause inconvenience,\x01",
            "Thank you for your consideration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No, no problem.\x01",
            "If there is something in trouble\x01",
            "Please say anything.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)

    label("loc_6204")

    Jump("loc_6270")

    label("loc_6209")


    ChrTalk(
        0xFE,
        "I am truly happy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is all thanks to the family ……\x01",
            "I have to cherish my eyes as much as I can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6270")

    Jump("loc_627E")

    label("loc_6275")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_627E")

    label("loc_627E")

    TalkEnd(0xFE)
    Return()

    # Function_16_5695 end

    def Function_17_6282(): pass

    label("Function_17_6282")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_62B0")
    Call(0, 22)
    Return()

    label("loc_62B0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_62E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62E4")
    Call(0, 23)
    Return()

    label("loc_62E4")

    Call(0, 25)
    Return()

    label("loc_62E8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_638A")

    ChrTalk(
        0xFE,
        (
            "Sophia in the residential area and\x01",
            "Cindy's house also\x01",
            "I was relieved that it was safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, I was relaxed now\x01",
            "I want to regain everyday life.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D4F")

    label("loc_638A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6404")

    ChrTalk(
        0xFE,
        (
            "When I lived in a residential area\x01",
            "Neighborhood is also worried ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sophia, Cindy,\x01",
            "Is it okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D4F")

    label("loc_6404")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_649D")

    ChrTalk(
        0xFE,
        (
            "Because I do not want much,\x01",
            "In the crossbell city as it is\x01",
            "I wonder if you can not stay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If my family is happy\x01",
            "That is all I need.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D4F")

    label("loc_649D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_65A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_654A")

    ChrTalk(
        0xFE,
        (
            "Me……\x01",
            "I have seen it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Rampage in old city,\x01",
            "Huge monster … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, horrible … …\x01",
            "Since when was the crossbell\x01",
            "In such a horrible place ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_659D")

    label("loc_654A")


    ChrTalk(
        0xFE,
        (
            "Also, that huge monster\x01",
            "I think that it will … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uu, I can not stop trembling.\x02",
    )

    CloseMessageWindow()

    label("loc_659D")

    Jump("loc_6D4F")

    label("loc_65A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6608")

    ChrTalk(
        0xFE,
        (
            "Me, bloody thing is\x01",
            "I'm really weak.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If the case finishes successfully\x01",
            "Is it okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D4F")

    label("loc_6608")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_66FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6690")

    ChrTalk(
        0xFE,
        (
            "Shaba …\x01",
            "When water is raised to plants,\x01",
            "My mind is healed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The sound of rain is comfortable ……\x01",
            "It's a peaceful holiday.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_66F5")

    label("loc_6690")


    ChrTalk(
        0xFE,
        (
            "Shaba …\x01",
            "in a while\x01",
            "Let's make it tea time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "あっ、Maryにも\x01",
            "I have to feed them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66F5")

    Jump("loc_6D4F")

    label("loc_66FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_678F")

    ChrTalk(
        0xFE,
        (
            "I should go shopping later.\x01",
            "Today Marte's place\x01",
            "I wonder if it was cheap ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Huhu, people in the market too\x01",
            "Everyone is already familiar.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D4F")

    label("loc_678F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_68E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6872")

    ChrTalk(
        0xFE,
        (
            "There seems to be an important meeting today,\x01",
            "My husband left early in the morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since I moved here,\x01",
            "Motivation also suddenly in work\x01",
            "It seems that it came out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My husband takes care of my family … …\x01",
            "Hehe, it is a very good thing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_68DD")

    label("loc_6872")


    ChrTalk(
        0xFE,
        (
            "主人はSince I moved here,\x01",
            "仕事にも俄然やる気がIt seems that it came out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hehe, it is a very good thing.\x02",
    )

    CloseMessageWindow()

    label("loc_68DD")

    Jump("loc_6D4F")

    label("loc_68E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_68F0")
    Jump("loc_6D4F")

    label("loc_68F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6A35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69BD")

    ChrTalk(
        0xFE,
        (
            "If you are headed for\x01",
            "You often have a good time to share,\x01",
            "He is a very nice person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But after all somewhere\x01",
            "Let me feel lonely ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a single assignment,\x01",
            "It must be lonely.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6A30")

    label("loc_69BD")


    ChrTalk(
        0xFE,
        (
            "It is also said that I will be a single employee\x01",
            "It will be quite lonesome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My family is\x01",
            "Even if it is complete\x01",
            "You can say that I am happy enough.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A30")

    Jump("loc_6D4F")

    label("loc_6A35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6B46")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6ADB")

    ChrTalk(
        0xFE,
        (
            "皆さん、どうかMaryのことを\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That girl is surely in this house\x01",
            "You ought to want to go home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B41")

    label("loc_6ADB")


    ChrTalk(
        0xFE,
        (
            "うふふ、Sanitaったら\x01",
            "Hold me so strongly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "でも、Maryも\x01",
            "I do not seem to be in a pity.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B41")

    Jump("loc_6D4F")

    label("loc_6B46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6C5A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6BE6")

    ChrTalk(
        0xFE,
        (
            "This room is\x01",
            "The kitchen is somewhat narrow, but ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hobby gardening is also\x01",
            "It seems to be possible with flower pots on the table,\x01",
            "I like it very much.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6C55")

    label("loc_6BE6")


    ChrTalk(
        0xFE,
        (
            "Sanitaが慣れるのに\x01",
            "Whether it takes time\x01",
            "I thought that … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhufu, that worry\x01",
            "It sounds like you did not have it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C55")

    Jump("loc_6D4F")

    label("loc_6C5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6D46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C7F")
    Call(0, 15)
    Jump("loc_6CBF")

    label("loc_6C7F")


    ChrTalk(
        0xFE,
        (
            "Uhufu, next door\x01",
            "In a person who seems kind\x01",
            "It was really good.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CBF")

    Jump("loc_6D41")

    label("loc_6CC4")


    ChrTalk(
        0xFE,
        (
            "From now on, all the family members\x01",
            "Anything\x01",
            "I will overcome it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhufu, somehow my newlywed\x01",
            "I remember my feeling\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D41")

    Jump("loc_6D4F")

    label("loc_6D46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6D4F")

    label("loc_6D4F")

    TalkEnd(0xFE)
    Return()

    # Function_17_6282 end

    def Function_18_6D53(): pass

    label("Function_18_6D53")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6D8B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D87")
    Call(0, 23)
    Return()

    label("loc_6D87")

    Call(0, 25)
    Return()

    label("loc_6D8B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6EA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E35")

    ChrTalk(
        0xFE,
        (
            "Father, I can return to work\x01",
            "It looks very happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "ふふ、Sanitaもとっても嬉しいっ。\x01",
            "Maryもそう思うでしょう？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Meow?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_6E9B")

    label("loc_6E35")


    ChrTalk(
        0xFE,
        (
            "Father, I can return to work\x01",
            "It looks very happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "ふふ、Sanitaも\x01",
            "I am very happy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E9B")

    Jump("loc_7A2B")

    label("loc_6EA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6F03")

    ChrTalk(
        0xFE,
        "Mary、心配しないでね。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "MaryはSanitaが\x01",
            "I will definitely protect you … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A2B")

    label("loc_6F03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6F71")

    ChrTalk(
        0xFE,
        (
            "Mr. Oppa, san also today\x01",
            "Go out of the crossbell\x01",
            "It is said that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Do you feel sad?\x02",
    )

    CloseMessageWindow()
    Jump("loc_7A2B")

    label("loc_6F71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7000")

    ChrTalk(
        0xFE,
        (
            "Maryといっしょに、\x01",
            "To Charity Event\x01",
            "I wonder if I should go play.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In rumors, the kirei people\x01",
            "It seems that they will gather a lot.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A2B")

    label("loc_7000")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_70F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7094")

    ChrTalk(
        0xFE,
        (
            "Today is too far away\x01",
            "Do not try to do it\x01",
            "I was told.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It can not be helped,\x01",
            "ここでMaryと遊んでますの。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_70EC")

    label("loc_7094")


    ChrTalk(
        0xFE,
        (
            "Already……\x01",
            "Today all the family members\x01",
            "You should have been to a department store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "It's boring …\x02",
    )

    CloseMessageWindow()

    label("loc_70EC")

    Jump("loc_7A2B")

    label("loc_70F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7182")

    ChrTalk(
        0xFE,
        (
            "Mary、きのう\x01",
            "I was washing your face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's said that it will rain when a cat washes his face,\x01",
            "Was it true?\x01",
            "Sanita、びっくりですの！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A2B")

    label("loc_7182")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_7287")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7239")

    ChrTalk(
        0xFE,
        (
            "Maryったら\x01",
            "Somehow my face is scrubbing\x01",
            "I am washing it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's said that it will rain when a cat washes his face,\x01",
            "The aunt of the stall\x01",
            "I said that … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…… Is it raining tomorrow?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7282")

    label("loc_7239")


    ChrTalk(
        0xFE,
        (
            "Maryが顔を洗っている\x01",
            "That means …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…… Is it raining tomorrow?\x02",
    )

    CloseMessageWindow()

    label("loc_7282")

    Jump("loc_7A2B")

    label("loc_7287")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_73C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7348")
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Mary、今日はこれで\x01",
            "I will play it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Bushy tassel ……\x02",
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 1200, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1200)

    ChrTalk(
        0xF,
        "Fukaa ah ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "わAh……\x01",
            "It really works, is not this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0xE, 0x10)
    Jump("loc_73BB")

    label("loc_7348")


    ChrTalk(
        0xFE,
        (
            "To the stalls of the stalls\x01",
            "I was taught,\x01",
            "It is \"cat plaster\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "ふふ、Maryったら\x01",
            "She seems to like it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_73BB")

    Jump("loc_7A2B")

    label("loc_73C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_73CE")
    Jump("loc_7A2B")

    label("loc_73CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_74E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7462")

    ChrTalk(
        0xFE,
        (
            "That's your father's bed.\x01",
            "This time with my mother\x01",
            "Sanitaのベッドですわ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Mary、覚えたかしら？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Nyao\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    ClearChrFlags(0xE, 0x10)
    Jump("loc_74DF")

    label("loc_7462")


    ChrTalk(
        0xFE,
        (
            "Maryがまたどこかに\x01",
            "In order not to go,\x01",
            "I am remembering things at home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Continuing this,\x01",
            "Surely it will be fine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_74DF")

    Jump("loc_7A2B")

    label("loc_74E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_774C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7651")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_75F4")
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xE,
        (
            "うう、Mary……\x01",
            "I am sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I, I\x01",
            "Because I was wrong ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Sanita……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F(… … I have to find it soon.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(That's right ……\x01",
            "Anyway, let's do our best. )\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x0, 6)
    Jump("loc_764C")

    label("loc_75F4")


    ChrTalk(
        0xFE,
        (
            "うう、Mary……\x01",
            "I am sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I, I\x01",
            "Because I was wrong ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_764C")

    Jump("loc_7747")

    label("loc_7651")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_76DE")
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xE,
        "本当によかった、Mary……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "As anymore … as a part today\x01",
            "I can hold him a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "にゃ、Meow?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    OP_4C(0xF, 0xFF)
    Jump("loc_7747")

    label("loc_76DE")

    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xE,
        (
            "さあ、Mary。\x01",
            "I decide my resolution.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Tsuku ~~~~~~ っ.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Nya, Oh yeah …\x02",
    )

    CloseMessageWindow()
    OP_4C(0xF, 0xFF)

    label("loc_7747")

    Jump("loc_7A2B")

    label("loc_774C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7899")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7827")

    ChrTalk(
        0xFE,
        (
            "New house,\x01",
            "Sanitaは結構\x01",
            "I like it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "でもMaryは、なんだか\x01",
            "After coming to this room\x01",
            "The state is strange.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With a sudden move\x01",
            "Maybe I was surprised\x01",
            "I do not think so.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7894")

    label("loc_7827")


    ChrTalk(
        0xFE,
        (
            "Mary、なんだか\x01",
            "Looks like I'm afraid … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With a sudden move\x01",
            "Maybe I was surprised\x01",
            "I do not think so.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7894")

    Jump("loc_7A2B")

    label("loc_7899")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_7A22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7942")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_78BE")
    Call(0, 15)
    Jump("loc_793D")

    label("loc_78BE")


    ChrTalk(
        0xFE,
        (
            "Fuh, for such a time\x01",
            "Maryにあいさつをおしえて\x01",
            "It was good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanks, Haji\x01",
            "I did not need it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_793D")

    Jump("loc_7A1D")

    label("loc_7942")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_79AB")

    ChrTalk(
        0xFE,
        (
            "ふふ、Maryはほんとうに\x01",
            "Mr. Riko.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well,\x01",
            "I will give you a throat.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A1D")

    label("loc_79AB")


    ChrTalk(
        0xFE,
        (
            "Father and mother are more than before\x01",
            "I was on good terms with each other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sanitaは、それがとっても\x01",
            "I am glad.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A1D")

    Jump("loc_7A2B")

    label("loc_7A22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_7A2B")

    label("loc_7A2B")

    TalkEnd(0xFE)
    Return()

    # Function_18_6D53 end

    def Function_19_7A2F(): pass

    label("Function_19_7A2F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7A56")

    ChrTalk(
        0xFE,
        "……Nyao\x02",
    )

    CloseMessageWindow()
    Jump("loc_7D0C")

    label("loc_7A56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_7A72")

    ChrTalk(
        0xFE,
        "Nya\x02",
    )

    CloseMessageWindow()
    Jump("loc_7D0C")

    label("loc_7A72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7A90")

    ChrTalk(
        0xFE,
        "Meow……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7D0C")

    label("loc_7A90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7AAE")

    ChrTalk(
        0xFE,
        "Published.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7D0C")

    label("loc_7AAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_7ACE")

    ChrTalk(
        0xFE,
        "Fuya-chan.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7D0C")

    label("loc_7ACE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7AEE")

    ChrTalk(
        0xFE,
        "Nyan\x02",
    )

    CloseMessageWindow()
    Jump("loc_7D0C")

    label("loc_7AEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_7B2F")
    TurnDirection(0xF, 0xE, 500)
    Sleep(500)

    ChrTalk(
        0xFE,
        (
            "Meowy\x01",
            "(Scrubbing, scrubbing)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D0C")

    label("loc_7B2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7B51")

    ChrTalk(
        0xFE,
        "Fumi ah ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7D0C")

    label("loc_7B51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7B5F")
    Jump("loc_7D0C")

    label("loc_7B5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7B7D")

    ChrTalk(
        0xFE,
        "Nice to meet you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7D0C")

    label("loc_7B7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_7C81")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C13")
    OP_4B(0xE, 0xFF)

    ChrTalk(
        0xE,
        "本当によかった、Mary……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "As anymore … as a part today\x01",
            "I can hold him a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "にゃ、Meow?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    OP_4C(0xE, 0xFF)
    Jump("loc_7C7C")

    label("loc_7C13")

    OP_4B(0xE, 0xFF)

    ChrTalk(
        0xE,
        (
            "さあ、Mary。\x01",
            "I decide my resolution.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Tsuku ~~~~~~ っ.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Nya, Oh yeah …\x02",
    )

    CloseMessageWindow()
    OP_4C(0xE, 0xFF)

    label("loc_7C7C")

    Jump("loc_7D0C")

    label("loc_7C81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7C9F")

    ChrTalk(
        0xFE,
        "Meow……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7D0C")

    label("loc_7C9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_7D03")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7CC7")

    ChrTalk(
        0xFE,
        "Meow.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7CFE")

    label("loc_7CC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7CEA")

    ChrTalk(
        0xFE,
        "Powered by Translate\x02",
    )

    CloseMessageWindow()
    Jump("loc_7CFE")

    label("loc_7CEA")


    ChrTalk(
        0xFE,
        "Nyan-chan ♪\x02",
    )

    CloseMessageWindow()

    label("loc_7CFE")

    Jump("loc_7D0C")

    label("loc_7D03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_7D0C")

    label("loc_7D0C")

    TalkEnd(0xFE)
    Return()

    # Function_19_7A2F end

    def Function_20_7D10(): pass

    label("Function_20_7D10")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7DAD")
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Even if you get in the way of work\x01",
            "You can not do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Until you get to work\x01",
            "Do not let your health go down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Well … I will be careful.\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    Jump("loc_7E4B")

    label("loc_7DAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7E4B")
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Even so,\x01",
            "You did not lean, did you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because I am living alone,\x01",
            "Only suitable ones\x01",
            "Do not eat it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Haha … … It is harsh.\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)

    label("loc_7E4B")

    TalkEnd(0xFE)
    Return()

    # Function_20_7D10 end

    def Function_21_7E4F(): pass

    label("Function_21_7E4F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7EB3")

    ChrTalk(
        0xFE,
        (
            "Well, I gotta go home\x01",
            "You do not have to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I want to see you again.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7F2E")

    label("loc_7EB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7F2E")

    ChrTalk(
        0xFE,
        (
            "Hey, Dad.\x01",
            "Picture of the last parade,\x01",
            "It looked very fun!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I was a bit lazy, though.\x02",
    )

    CloseMessageWindow()

    label("loc_7F2E")

    TalkEnd(0xFE)
    Return()

    # Function_21_7E4F end

    def Function_22_7F32(): pass

    label("Function_22_7F32")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(50090, 1430, 52450, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, 49700, 30, 51700, 360)
    SetChrPos(0x102, 50700, 30, 51700, 360)
    SetChrPos(0x109, 49600, 30, 50700, 360)
    SetChrPos(0x105, 50800, 30, 50700, 360)
    SetChrSubChip(0xC, 0x2)
    SetChrSubChip(0xD, 0x1)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xD,
        "Oh, it is a customer.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Oh, you guys ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FWe are the crossbell police ·\x01",
            "It is a person of the affairs support department.\x02\x03",
            "bondさんですね？\x01",
            "See you at the time of a cult incident\x01",
            "Ever since I think … …\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_815D")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KPrequel \"Find the owner of a lost cat\" quest? (for test)\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【It does not change】\x01",        # 0
            "【Are doing】\x01",        # 1
            "【not doing】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8149")
    OP_29(0x8, 0x4, 0x10)
    Jump("loc_815D")

    label("loc_8149")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_815D")
    OP_29(0x8, 0x3, 0x10)

    label("loc_815D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_829E")

    ChrTalk(
        0xC,
        "Oh, of course I remember.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Anyway, at that \"fort\"\x01",
            "It was that we released us from prison\x01",
            "Because you are the unbelievable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "By the way, to you guys\x01",
            "Maryを飼うことになった時にも\x01",
            "Were you indebted for it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "No, to you guys again\x01",
            "I thought I had to say thank you.\x01",
            "Thank you so much for that time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8374")

    label("loc_829E")


    ChrTalk(
        0xC,
        "Oh, of course I remember.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Anyway, at that \"fort\"\x01",
            "It was that we released us from prison\x01",
            "Because you are the unbelievable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "No, to you guys again\x01",
            "I thought I had to say thank you.\x01",
            "Thank you so much for that time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8374")


    ChrTalk(
        0xD,
        (
            "Thank you also from me\x01",
            "I will tell you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "That section is the master\x01",
            "Thank you for all the help you have given me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00004FNo, nothing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FYeah, anyway\x01",
            "I'm glad that you are fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Haha, thanks to you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "By the way, today\x01",
            "Have you also been in charge of something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYes, in fact …\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "bondに調査の説明をした上で、\x01",
            "I asked about how I moved.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xC,
        (
            "I see,\x01",
            "Suspicious resident change notification … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "So I parted that house\x01",
            "Do you want to hear the background?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103FYes, I understand rude,\x01",
            "Was there any illegality in the procedure etc\x01",
            "I want to check if … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "No, I do not feel rude.\x01",
            "There is plenty to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well, to a large extent,\x01",
            "The house is for its own debt repayment\x01",
            "I sold it out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The seller is the same real estate company as the purchaser\x01",
            "Procedures are also genuine … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "In that sense illegal places are\x01",
            "Can you say that there is nothing at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005FIs that so……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103FUm, I guess this should not hurt\x01",
            "I do not mind ……\x02\x03",
            "#00101FOn the cause of debt itself\x01",
            "Is it OK if I ask you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Oh, I do not mind.\x01",
            "A simple story …\x01",
            "This is also a rust from the body.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The memory of those days\x01",
            "I am not sure so much ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "During the time I was taking that blue medicine\x01",
            "Apparently to a dangerous market with high risk\x01",
            "He seems to have put out his hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "By the time the cult incident was over\x01",
            "It suddenly crashes … …\x01",
            "I've done a lot of debts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10105FThat's … such a thing ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Ah.\x01",
            "Just well, I am blessed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "By selling out all the assets including the house\x01",
            "I was able to return much of the debt … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Damage was within the range of individuals,\x01",
            "I managed to finish off my company anyhow.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0x0)

    ChrTalk(
        0xC,
        (
            "Anyway to it …\x01",
            "I can not do anything like this\x01",
            "My wife and daughter did not let go.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xD, 0x0)

    ChrTalk(
        0xD,
        (
            "#11Pyou……\x01",
            "It is a promise not to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PIn general, we are in the world\x01",
            "Because it is only one family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11PIt is natural that you should struggle together.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Craig……本当にありがとう。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "君とSanitaには\x01",
            "I appreciate it from the bottom of my heart.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xD)

    ChrTalk(
        0xD,
        (
            "#11POh, you …\x01",
            "Before everyone's watching\x01",
            "It's embarrassing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10109FHehu, with a very strong bond\x01",
            "You are tied up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FWell, before the family ties\x01",
            "Is it not related to the place to live?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0x2)
    SetChrSubChip(0xD, 0x1)

    ChrTalk(
        0xC,
        (
            "Well, even such a big talk\x01",
            "I do not think so ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Anyway, turning my heartfelt\x01",
            "I will do my best from here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I finished all the remaining debts,\x01",
            "To give back to my wife and daughter.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xD, 0x0)

    ChrTalk(
        0xD,
        "you……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00104FI think that it is a respectable mind.\x02\x03",
            "#00100FUm, if something in the future\x01",
            "If you have any problems\x01",
            "Please do not hesitate to ask us.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xD, 0x1)

    ChrTalk(
        0x101,
        (
            "#12P#00000FYeah, that time\x01",
            "Because I can come soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Haha, until you guys\x01",
            "To be said like that\x01",
            "It is a truly amazing story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Yeah, when it's time for something\x01",
            "I will depend on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "By the way, if you talk\x01",
            "Was it ok with this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If there is anything else\x01",
            "I will let you answer anything ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FYeah, the necessary information is\x01",
            "It is enough as it is obtained.\x02\x03",
            "#00004FThanks for your cooperation in the investigation,\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10300FWell then, shall we go on ahead?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FYeah, well.\x02\x03",
            "#00104Fでは、bondさん。\x01",
            "We will be rude with this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10109FFrom now on, all the family members\x01",
            "Please get along.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Oh, of course!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Uhufu, okay.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(49250, 1400, 2740, 0)
    MoveCamera(44, 23, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(17020, 0)
    OP_4B(0xE, 0xFF)
    OP_4B(0xF, 0xFF)
    SetChrPos(0x101, 52000, 0, 6750, 180)
    SetChrPos(0x109, 52000, 0, 6750, 180)
    SetChrPos(0x102, 52000, 0, 6750, 180)
    SetChrPos(0x105, 52000, 0, 6750, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0x10, 0x0, 0x0)
    OP_79(0x1)
    Sleep(500)

    def lambda_903F():
        OP_95(0xFE, 51400, 0, 2650, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_903F)

    def lambda_9059():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9059)
    Sleep(900)

    def lambda_906D():
        OP_95(0xFE, 52300, 0, 2750, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_906D)

    def lambda_9087():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9087)
    Sleep(900)

    def lambda_909B():
        OP_95(0xFE, 51400, 0, 3650, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_909B)

    def lambda_90B5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_90B5)
    Sleep(900)
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)

    def lambda_90DB():
        OP_95(0xFE, 52300, 0, 3750, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_90DB)

    def lambda_90F5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_90F5)
    Sleep(700)
    Sound(104, 0, 100, 0)
    OP_71(0x1, 0x10, 0x0, 0x0, 0x0)
    OP_79(0x1)
    Sleep(200)

    def lambda_9121():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_9121)
    Sleep(50)

    def lambda_9131():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_9131)
    Sleep(1000)

    ChrTalk(
        0xE,
        "#6POh, older brothers ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_91B4():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_91B4)
    Sleep(50)

    def lambda_91C4():
        OP_93(0x102, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_91C4)
    Sleep(50)

    def lambda_91D4():
        OP_93(0x109, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_91D4)
    Sleep(50)

    def lambda_91E4():
        OP_93(0x105, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_91E4)
    Sleep(50)

    def lambda_91F4():
        OP_95(0x101, 50250, 0, 2650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_91F4)
    Sleep(50)

    def lambda_9211():
        OP_95(0x102, 50500, 0, 3650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9211)
    Sleep(50)

    def lambda_922E():
        OP_95(0x109, 51500, 0, 2550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_922E)
    Sleep(50)

    def lambda_924B():
        OP_95(0x105, 51750, 0, 3750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_924B)
    SetMapObjFlags(0x1, 0x0)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0xE,
        (
            "#6PFather and mother\x01",
            "Were there also something errands?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh, just a bit.\x01",
            "I was talking to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00100FSanitaちゃんと言ったかしら。\x01",
            "I have good parents.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xE,
        "#6PDo you understand?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#6PThat's right.\x01",
            "Especially since I moved\x01",
            "Both of us are very close each other … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#6PVery, very\x01",
            "It is a summer holiday.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xE, 0x0, 0x1F4)

    ChrTalk(
        0xE,
        "#12Pね、Maryもそう思うでしょう？\x02",
    )

    CloseMessageWindow()
    OP_93(0xF, 0xB4, 0x1F4)

    ChrTalk(
        0xF,
        "#6PNyanjin\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10102FHehuu can be saved positively.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOh, what is more important.\x02",
    )

    CloseMessageWindow()

    def lambda_9475():
        OP_93(0x101, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9475)
    Sleep(50)

    def lambda_9485():
        OP_93(0x102, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9485)
    Sleep(50)

    def lambda_9495():
        OP_93(0x109, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9495)
    Sleep(50)

    def lambda_94A5():
        OP_93(0x105, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_94A5)

    ChrTalk(
        0x101,
        (
            "#12P#00003Fさてと、これでbondさんの\x01",
            "I could confirm the situation … …\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x6A, 0x1, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_95EE")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "◆ \"What is the investigation situation? (For testing)\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【It does not change】\x01",                  # 0
            "【There is still a rest】\x01",              # 1
            "【Confirmation of 6 places ended】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_95C1"),
        (1, "loc_95C6"),
        (2, "loc_95DA"),
        (SWITCH_DEFAULT, "loc_95EE"),
    )


    label("loc_95C1")

    Jump("loc_95EE")

    label("loc_95C6")

    ClearScenarioFlags(0x131, 5)
    ClearScenarioFlags(0x131, 6)
    ClearScenarioFlags(0x132, 0)
    ClearScenarioFlags(0x132, 1)
    ClearScenarioFlags(0x132, 2)
    Jump("loc_95EE")

    label("loc_95DA")

    SetScenarioFlags(0x131, 5)
    SetScenarioFlags(0x131, 6)
    SetScenarioFlags(0x132, 0)
    SetScenarioFlags(0x132, 1)
    SetScenarioFlags(0x132, 2)
    Jump("loc_95EE")

    label("loc_95EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_964A")

    ChrTalk(
        0x101,
        (
            "#12P#00000FAlright, then continue\x01",
            "We will respond to the rest of the survey.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_969D")

    label("loc_964A")


    ChrTalk(
        0x101,
        (
            "#12P#00000FOK, this is the end of the investigation.\x02\x03",
            "Let's return to the municipal hall.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x6A, 0x1, 0x6)

    label("loc_969D")

    OP_93(0xE, 0x5A, 0x0)
    OP_93(0xF, 0x5A, 0x0)
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0xF, 0x10)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_71(0x1, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x1, 0x10)
    OP_4C(0xE, 0xFF)
    OP_4C(0xF, 0xFF)
    OP_93(0xE, 0x0, 0x0)
    OP_93(0xF, 0xB4, 0x0)
    SetScenarioFlags(0x131, 7)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 51000, 0, 3400, 225)
    EventEnd(0x5)
    Return()

    # Function_22_7F32 end

    def Function_23_9703(): pass

    label("Function_23_9703")

    EventBegin(0x0)
    Fade(500)
    OP_68(51550, 1420, 51330, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(18950, 0)
    SetChrPos(0x101, 51730, 0, 52230, 90)
    SetChrPos(0x102, 51730, 0, 51030, 90)
    SetChrPos(0x109, 50530, 0, 52230, 90)
    SetChrPos(0x105, 50530, 0, 51030, 90)
    SetChrPos(0x104, 49330, 0, 51530, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    OP_0D()

    ChrTalk(
        0xE,
        (
            "Higuri, hit ……\x01",
            "Sanitaがいけないんですの。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "SanitaがMaryを\x01",
            "Because I did not look properly … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Sanita……そんなに\x01",
            "Do not blame yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5POh, and to it\x01",
            "Maryは必ず見つかるさ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5Pだから、Sanita。\x01",
            "Take care.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xC, 0x10E, 0x1F4)

    ChrTalk(
        0xC,
        "#11POh, you guys …!\x02",
    )

    CloseMessageWindow()

    def lambda_98DE():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_98DE)
    Sleep(50)

    def lambda_98EE():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_98EE)
    WaitChrThread(0xD, 1)

    ChrTalk(
        0xD,
        "oh dear……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FHello.\x01",
            "I saw the request and asked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PYou saw it properly, did not you?\x01",
            "…… Thankful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PHonestly, rather than police\x01",
            "Like to ask the guild\x01",
            "I thought it was content … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PBecause you kept on my mind\x01",
            "I have relied on it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FYeah, if you can say so\x01",
            "It is also appreciated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10103F何でも仔猫のMaryちゃんが\x01",
            "Although it is missing … …\x02\x03",
            "#10100FFrom when\x01",
            "Do you understand that it's gone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11POh, clear time\x01",
            "I do not know but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PIt has been since yesterday evening.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Everyone in the family's east\x01",
            "When looking at the stalls\x01",
            "Sanitaが気付いたんですの。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Suddenly in the gap we are keeping our eyes on\x01",
            "It seems I got turned …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "After that, everyone in the shopping district\x01",
            "I need your help\x01",
            "I searched for a neighborhood ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11POh, so until the evening\x01",
            "Everyone I searched for,\x01",
            "I did not find it after all.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xC, 500)

    ChrTalk(
        0xE,
        (
            "Ug, uh huh ……\x01",
            "Your father is a liar!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "If this morning comes\x01",
            "I told you I'm coming home!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xE, 500)

    ChrTalk(
        0xC,
        "#5Pすまない、Sanita……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00108FSanitaちゃん……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001FBy the way …\x01",
            "Is there sighting information on something?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9D36():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_9D36)
    Sleep(50)

    def lambda_9D46():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_9D46)
    WaitChrThread(0xE, 2)

    ChrTalk(
        0xC,
        (
            "#11POh, but all\x01",
            "Though it is of yesterday's stage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PAccording to those information,\x01",
            "As expected to the highway\x01",
            "I do not seem to be out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PHead towards Central square\x01",
            "Maryを見たという人がいてね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PYesterday was already late at night\x01",
            "I could not catch up any more,\x01",
            "I pulled up the search … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00301F……, with no words\x01",
            "Is it because this morning?\x02\x03",
            "#00303FAnd if it is in the city\x01",
            "No matter where you go\x01",
            "It might not be strange.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FIn other words, the search range is\x01",
            "Is it a whole area of the city?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FWell, something a little more\x01",
            "It is a place I want clues ….\x02\x03",
            "#00001FExcuse me……\x01",
            "これまでにMaryちゃんが\x01",
            "What have you gone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PNo, it has never been.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11P何しろ、Maryは\x01",
            "Sanitaによく懐いていてね。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PBesides, I am a cowardly child.\x01",
            "I will go away somewhere away from me\x01",
            "It is hard to think hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PSo lose sight of us with a clap of something\x01",
            "I think I got lost.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00003FI see. Is that so …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FAnyway, first go out to the city\x01",
            "I have no choice but to search it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FOh, for the time being\x01",
            "It seems to only start from there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PIf I calm down\x01",
            "I will go looking for it again ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PIt is likely to be a long-term place,\x01",
            "If there is any other errands\x01",
            "You do not mind if I tidy up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FI agree……\x02",
    )

    CloseMessageWindow()
    OP_29(0x74, 0x1, 0x0)
    Call(0, 24)
    EventEnd(0x5)
    Return()

    # Function_23_9703 end

    def Function_24_A218(): pass

    label("Function_24_A218")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【Start searching quickly】\x01",      # 0
            "【Having a little wait】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A2E2")

    ChrTalk(
        0x101,
        (
            "#6P#00000FNo, others are okay\x01",
            "I would like to start the search immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PWell, that will be helpful.\x02",
    )

    CloseMessageWindow()
    Call(0, 26)
    Jump("loc_A35C")

    label("loc_A2E2")

    OP_29(0x74, 0x1, 0x1)

    ChrTalk(
        0x101,
        (
            "#6P#00000FSo sorry, but …\x01",
            "Wait a while.\x01",
            "Can I get it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11POk, then again later.\x02",
    )

    CloseMessageWindow()

    label("loc_A35C")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_93(0xC, 0xB4, 0x0)
    OP_93(0xD, 0x0, 0x0)
    OP_93(0xE, 0x5A, 0x0)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    SetScenarioFlags(0x155, 0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 51730, 0, 52230, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_24_A218 end

    def Function_25_A3AD(): pass

    label("Function_25_A3AD")

    EventBegin(0x0)
    Fade(500)
    OP_68(51550, 1420, 51330, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(18950, 0)
    SetChrPos(0x101, 51730, 0, 52230, 90)
    SetChrPos(0x102, 51730, 0, 51030, 90)
    SetChrPos(0x109, 50530, 0, 52230, 90)
    SetChrPos(0x105, 50530, 0, 51030, 90)
    SetChrPos(0x104, 49330, 0, 51530, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    OP_93(0xC, 0x10E, 0x0)
    OP_93(0xD, 0x10E, 0x0)
    OP_93(0xE, 0x10E, 0x0)
    OP_0D()

    ChrTalk(
        0xC,
        "#11POh, you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PMaryの捜索を\x01",
            "You can get started?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【Start searching for kitten】\x01",      # 0
            "【Having a little wait】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A568")

    ChrTalk(
        0x101,
        (
            "#6P#00000FYes, hereafter\x01",
            "I would like to conduct a search.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PWell, that will be helpful.\x02",
    )

    CloseMessageWindow()
    Call(0, 26)
    Jump("loc_A5F7")

    label("loc_A568")


    ChrTalk(
        0x101,
        (
            "#6P#00006FI'm sorry, a bit\x01",
            "There is something I want to prepare ……\x02\x03",
            "#00000FJust a little more\x01",
            "待ってCan I get it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11POh, I got it.\x02",
    )

    CloseMessageWindow()

    label("loc_A5F7")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_93(0xC, 0xB4, 0x0)
    OP_93(0xD, 0x0, 0x0)
    OP_93(0xE, 0x5A, 0x0)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 51730, 0, 52230, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_25_A3AD end

    def Function_26_A645(): pass

    label("Function_26_A645")

    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#6P#00100FWell then, Lloyd.\x01",
            "Where do you start from first?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#6P#00003FYeah, yesterday's repetition\x01",
            "Maybe it will be ……\x02\x03",
            "#00000FIn the meaning of following the footsteps first\x01",
            "I should investigate from east street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00300FWell, is reasonable or not valid?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10304FHuh, that is basics of the investigation.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FBy the way, on this east street\x01",
            "Maryちゃんが行きそうな場所に\x01",
            "Do you recognize it?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A7D0():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A7D0)
    Sleep(50)

    def lambda_A7E0():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A7E0)
    Sleep(300)

    ChrTalk(
        0xD,
        (
            "Yeah, then\x01",
            "It is a fish store in the stalls.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "The best in this area\x01",
            "It's a favorite place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11POh, I have not confirmed this morning\x01",
            "Perhaps, I take it away\x01",
            "You may be showing us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PTo the store owner Marte\x01",
            "Because I had you help me search for you yesterday.\x01",
            "If you come, you ought to know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PIf you like it, that person\x01",
            "Can you ask me a story?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FOk, I understand.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xC, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#6P#00100Fところで、bondさんの方は\x01",
            "What are you going to do now?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0xC,
        "#11PFortunately, I am off work today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11Pin a while\x01",
            "Search on yesterday's continuation\x01",
            "I'm going to start … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PTo people on east street within yesterday\x01",
            "I roughly spoken around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PNow turn towards the central square\x01",
            "Turn around to the information\x01",
            "I'm thinking of collecting it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PIf something happen\x01",
            "I want you to call out anytime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00300FAcknowledgment.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FWell then, first of all the stalls\x01",
            "Do you hear it at a fish store?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FOh, let's move on.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest 【Request for kitten search】\x07\x00",
            "I started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_93(0xC, 0xB4, 0x0)
    OP_93(0xD, 0x0, 0x0)
    OP_93(0xE, 0x5A, 0x0)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    SetScenarioFlags(0x154, 7)
    OP_29(0x74, 0x1, 0x2)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 51730, 0, 52230, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_26_A645 end

    def Function_27_AC2A(): pass

    label("Function_27_AC2A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(50170, 1420, 530, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(18950, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 51040, 30, 1350, 0)
    SetChrPos(0xC, 49720, 0, 3350, 180)
    SetChrPos(0xD, 52360, 0, 3350, 180)
    SetChrPos(0xE, 51040, 0, 3350, 180)
    SetChrPos(0x101, 52320, 20, 0, 0)
    SetChrPos(0x1A3, 50960, 20, 0, 0)
    SetChrPos(0x102, 51680, 20, -980, 0)
    SetChrPos(0x104, 51340, 0, -3020, 0)
    SetChrPos(0x109, 50390, 30, -1740, 0)
    SetChrPos(0x105, 52250, 30, -1900, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    OP_4B(0xF, 0xFF)
    SetCameraDistance(21000, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    ChrTalk(
        0xE,
        "#5PMary……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5PAlready … … Where have you been?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PHiguri, hit ……\x01",
            "I am really worried ……\x01",
            "… … … so … … so … … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#12Pにゃ、Meow.\x02",
    )

    CloseMessageWindow()
    OP_97(0xF, 0x0, 0x0, 0x2EE, 0x3E8, 0x0)
    Sleep(300)

    ChrTalk(
        0xE,
        (
            "#5PNo … I'm sorry.\x01",
            "わるいのはSanitaだもの。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5Pbut thanks……\x01",
            "So they came home ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PFrom now on by arbitrary alone\x01",
            "You can not go anywhere.\x02",
        )
    )

    CloseMessageWindow()
    OP_97(0xF, 0x0, 0x0, 0x1F4, 0x3E8, 0x0)
    Sleep(300)
    Sound(953, 0, 100, 0)

    ChrTalk(
        0xF,
        "#12PNyanjin\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00109FHehe, it was good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10100FThis is one case settled.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "To you guys\x01",
            "What can I thank for ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "我が家の大切なMaryを\x01",
            "Thank you so much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Well, I do not have a word of appreciation.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Previously,\x01",
            "そして今度はMaryを……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Everyone is our family\x01",
            "It is a great big benefactor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00002FNo, such a thing ….\x02\x03",
            "#00000FBetter than us this time\x01",
            "Here she is\x01",
            "It contributed the most.\x02\x03",
            "I was completely scared\x01",
            "Maryを落ち着かせてくれて……\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x1, 0xF, 0xB4, 0xC8, 0x3E8, 0x0)
    TurnDirection(0xF, 0x1A3, 500)
    Sleep(300)
    Sound(953, 0, 100, 0)

    ChrTalk(
        0xF,
        "#5PNyanjin\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5P……Mary！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PYou, maybe\x01",
            "With that older sister\x01",
            "You mean I want to … ….\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 1200, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xF, 0xE, 500)
    OP_63(0xF, 0x0, 1200, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xF)

    ChrTalk(
        0xF,
        "#12PWell, yeah yeah … ….?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#12P#04602FHaha, do not worry.\x02\x03",
            "#04604FMaryからSanitaのことは\x01",
            "I heard that I love you so much.\x02\x03",
            "#04609FTold me a long story\x01",
            "About to come over.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xE,
        "#5Pそ、そうなの、Mary？\x02",
    )

    CloseMessageWindow()
    Sound(953, 0, 100, 0)

    ChrTalk(
        0xF,
        "#12PNyanjin\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#12P#04609FHuh, then\x01",
            "Is Charlie going home soon?\x02\x03",
            "#04604FI also played with my older brothers,\x01",
            "Maryとも知り合いになれたし。\x02\x03",
            "#04611F── Any words to say\x01",
            "I have found the best thing\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B35C():

        label("loc_B35C")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_B35C")

    QueueWorkItem2(0x101, 2, lambda_B35C)
    Sleep(300)

    ChrTalk(
        0x101,
        "#11P#00005FHuh……\x02",
    )

    CloseMessageWindow()

    def lambda_B388():
        OP_97(0xFE, 0xFFFFF8F8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_B388)
    Sleep(50)

    def lambda_B3A5():

        label("loc_B3A5")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_B3A5")

    QueueWorkItem2(0x102, 2, lambda_B3A5)
    Sleep(50)

    def lambda_B3BA():

        label("loc_B3BA")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_B3BA")

    QueueWorkItem2(0x104, 2, lambda_B3BA)
    Sleep(50)

    def lambda_B3CF():

        label("loc_B3CF")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_B3CF")

    QueueWorkItem2(0x109, 2, lambda_B3CF)
    Sleep(50)

    def lambda_B3E4():

        label("loc_B3E4")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_B3E4")

    QueueWorkItem2(0x105, 2, lambda_B3E4)
    Sleep(50)

    def lambda_B3F9():

        label("loc_B3F9")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_B3F9")

    QueueWorkItem2(0xC, 2, lambda_B3F9)
    Sleep(50)

    def lambda_B40E():

        label("loc_B40E")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_B40E")

    QueueWorkItem2(0xD, 2, lambda_B40E)
    Sleep(50)

    def lambda_B423():

        label("loc_B423")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_B423")

    QueueWorkItem2(0xE, 2, lambda_B423)
    Sleep(50)

    def lambda_B438():

        label("loc_B438")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_B438")

    QueueWorkItem2(0xF, 2, lambda_B438)
    WaitChrThread(0x1A3, 1)

    ChrTalk(
        0x104,
        "#00305FHey, hey …! Is it?\x02",
    )

    CloseMessageWindow()
    OP_93(0x1A3, 0x87, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x1A3,
        (
            "#6P#04602FHaha, you wait!\x02\x03",
            "#04609FSee you soon,\x01",
            "Maybe we can meet but Sa!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B4CD():
        OP_97(0xFE, 0xFFFFF448, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_B4CD)
    Sleep(300)

    def lambda_B4EA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A3, 2, lambda_B4EA)
    WaitChrThread(0x1A3, 1)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    EndChrThread(0xC, 0xFF)
    EndChrThread(0xD, 0xFF)
    EndChrThread(0xE, 0xFF)
    EndChrThread(0xF, 0xFF)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)

    ChrTalk(
        0x102,
        "#00106FWell ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FSomething\x01",
            "It was like a typhoon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHuh, rather than a typhoon,\x01",
            "I felt like a tornado.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FWell, my uncle, too\x01",
            "Let's say a bit more to discipline … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FWell, as for this time\x01",
            "I had a lot of help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well, as much as possible to her\x01",
            "I wanted to say thank you ….\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xC, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "Anyway, you guys.\x01",
            "I will reward you again.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B706():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B706)
    Sleep(50)

    def lambda_B716():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_B716)

    def lambda_B723():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B723)
    Sleep(50)

    def lambda_B733():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_B733)

    def lambda_B740():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B740)
    Sleep(50)

    def lambda_B750():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_B750)

    def lambda_B75D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_B75D)
    Sleep(50)

    def lambda_B76D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_B76D)
    WaitChrThread(0x105, 2)

    ChrTalk(
        0xD,
        "I will never forget this kindness.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "えとえと、Sanitaからも\x01",
            "Please let me say thanks!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Nyanni\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00009FHaha, you are welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FIf there is something again\x01",
            "Please do not hesitate to contact me.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest 【Request for kitten search】\x07\x00",
            "Achieved!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x74, 0x1, 0x8)
    OP_29(0x74, 0x4, 0x10)
    OP_C9(0x1, 0x1000)
    OP_29(0xA3, 0x1, 0xE)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    SetChrPos(0xC, 53730, 0, 52730, 180)
    SetChrPos(0xD, 53730, 0, 50730, 0)
    SetChrPos(0xE, 53730, 0, 51730, 270)
    SetChrPos(0xF, 52730, 0, 51730, 90)
    BeginChrThread(0xF, 0, 0, 0)
    RemoveParty(0xA2, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 50960, 20, 0, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_27_AC2A end

    def Function_28_B938(): pass

    label("Function_28_B938")

    EventBegin(0x1)
    Sound(807, 0, 100, 0)
    Sleep(300)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It is locked.\x01",
            "The residents seem to have already left.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 51800, 0, -4500, 0)
    EventEnd(0x4)
    Return()

    # Function_28_B938 end

    def Function_29_B995(): pass

    label("Function_29_B995")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a lock on the door.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_29_B995 end

    SaveToFile()

Try(main)
