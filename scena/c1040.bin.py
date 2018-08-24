from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Marcy",                  # 1
        "Sarina",                 # 2
        "Hugott",                 # 3
        "Claris",                 # 4
        "Bond",                   # 5
        "Creil",                  # 6
        "Sunita",                 # 7
        "Mary",                   # 8
        "Sepia",                  # 9
        "Oonagh",                 # 10
        "Azel",                   # 11
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
        "Function_9_2957",         # 09, 9
        "Function_10_2C7D",        # 0A, 10
        "Function_11_3E3C",        # 0B, 11
        "Function_12_3F30",        # 0C, 12
        "Function_13_4665",        # 0D, 13
        "Function_14_49F2",        # 0E, 14
        "Function_15_58C8",        # 0F, 15
        "Function_16_5A0E",        # 10, 16
        "Function_17_667D",        # 11, 17
        "Function_18_71A5",        # 12, 18
        "Function_19_7DAE",        # 13, 19
        "Function_20_8088",        # 14, 20
        "Function_21_81C3",        # 15, 21
        "Function_22_82BC",        # 16, 22
        "Function_23_9BE9",        # 17, 23
        "Function_24_A6DB",        # 18, 24
        "Function_25_A885",        # 19, 25
        "Function_26_AB1A",        # 1A, 26
        "Function_27_B179",        # 1B, 27
        "Function_28_BDD1",        # 1C, 28
        "Function_29_BE32",        # 1D, 29
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1170")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FCE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E17")
    Call(0, 9)
    Jump("loc_FC9")

    label("loc_E17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F3E")

    ChrTalk(
        0xFE,
        (
            "If my husband were\x01",
            "alive...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a guardsman, he would've\x01",
            "chosen to fight 'til the\x01",
            "end without giving up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Special Support\x01",
            "Section, please take\x01",
            "care of Noｱl and Fran.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Feel free to work her as\x01",
            "hard as you like to\x01",
            "resolve this situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10109FOh, mom.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_FC9")

    label("loc_F3E")


    ChrTalk(
        0xFE,
        (
            "Special Support Section,\x01",
            "please take care of Noｱl\x01",
            "and Fran.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Feel free to work her as\x01",
            "hard as you like to\x01",
            "resolve this situation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FC9")

    Jump("loc_116B")

    label("loc_FCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10E0")

    ChrTalk(
        0xFE,
        (
            "If my husband were\x01",
            "alive...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a guardsman, he would've\x01",
            "chosen to fight 'til the\x01",
            "end without giving up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Special Support\x01",
            "Section, please take\x01",
            "care of Noｱl and Fran.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Feel free to work her as\x01",
            "hard as you like to\x01",
            "resolve this situation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_116B")

    label("loc_10E0")


    ChrTalk(
        0xFE,
        (
            "Special Support Section,\x01",
            "please take care of Noｱl\x01",
            "and Fran.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Feel free to work her as\x01",
            "hard as you like to\x01",
            "resolve this situation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_116B")

    Jump("loc_2953")

    label("loc_1170")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_12F4")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1270")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_119B")
    Call(0, 9)
    Jump("loc_126B")

    label("loc_119B")


    ChrTalk(
        0xFE,
        (
            "Azel came to help, so\x01",
            "we're fine here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If those monsters come in,\x01",
            "I won't let them lay a\x01",
            "finger on Hugott or Sunita.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_126B")

    ChrTalk(
        0x109,
        "#10101FBe careful, ok mom?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, you guys be\x01",
            "careful too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_126B")

    Jump("loc_12EF")

    label("loc_1270")


    ChrTalk(
        0xFE,
        (
            "Azel came to help, so\x01",
            "we're fine here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If those monsters come in,\x01",
            "I won't let them lay a\x01",
            "finger on Hugott or Sunita.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12EF")

    Jump("loc_2953")

    label("loc_12F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_14C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13D0")

    ChrTalk(
        0xFE,
        (
            "Dieter... I've never\x01",
            "approved of his actions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He has undertaken\x01",
            "several actions by force\x01",
            "in Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "......Our people too...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Haha, sorry.\x01",
            "Nevermind.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_14C4")

    label("loc_13D0")


    ChrTalk(
        0xFE,
        (
            "...But even so, the state guard has\x01",
            "a completely different attitude than\x01",
            "when they called themselves CGF.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe those white\x01",
            "uniforms are a little\x01",
            "too neat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When my husband was alive,\x01",
            "he loved the Guardian\x01",
            "Force uniforms, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14C4")

    Jump("loc_2953")

    label("loc_14C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1770")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16E2")

    ChrTalk(
        0xFE,
        (
            "Umm... I wonder if this\x01",
            "will do for a change of\x01",
            "clothes for Fran.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's right, maybe I\x01",
            "should bring her some\x01",
            "fruit as well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FMom... I'm back.\x02\x03",
            "You said you were going\x01",
            "to St. Ursula Hospital\x01",
            "this afternoon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes, I just got back\x01",
            "from visiting the\x01",
            "patients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...*sigh*, but even so,\x01",
            "thank goodness Fran has\x01",
            "regained consciousness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have to thank that\x01",
            "inspector from Section\x01",
            "Two for protecting her...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103FThat's right... I have\x01",
            "to visit him again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yeah, thanks.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_176B")

    label("loc_16E2")


    ChrTalk(
        0xFE,
        (
            "It looks like you're going to\x01",
            "the hospital? I'm planning on\x01",
            "going there again later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I need to bring Fran a\x01",
            "change of clothes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_176B")

    Jump("loc_2953")

    label("loc_1770")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1939")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18AE")

    ChrTalk(
        0xFE,
        (
            "To think Mainz is occupied... Including the\x01",
            "appearance of terrorists at the trade conference,\x01",
            "these big incidents just keep happening...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They say the CGF is\x01",
            "resolving the problem,\x01",
            "but I'm somehow unsure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you guys are going\x01",
            "there, it would be best\x01",
            "to be extremely cautious.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1934")

    label("loc_18AE")


    ChrTalk(
        0xFE,
        (
            "That occupation incident\x01",
            "makes me uneasy\x01",
            "somehow...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you guys are going\x01",
            "there, it would be best\x01",
            "to be extremely cautious.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1934")

    Jump("loc_2953")

    label("loc_1939")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1A65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19F8")

    ChrTalk(
        0xFE,
        "Rain again today, huh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Going shopping is a bother, so\x01",
            "suitable leftovers will have\x01",
            "to do for dinner tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F(That's rather sloppy,\x01",
            "mom...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1A60")

    label("loc_19F8")


    ChrTalk(
        0xFE,
        (
            "Suitable leftovers will\x01",
            "have to do for dinner\x01",
            "tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Going out in this rain\x01",
            "is such a pain.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A60")

    Jump("loc_2953")

    label("loc_1A65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1B04")

    ChrTalk(
        0xFE,
        (
            "Hugott was telling me\x01",
            "about his Sunday School\x01",
            "homework.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, seeing the problems\x01",
            "reminded me of the time Noｱl\x01",
            "and Fran were in school.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2953")

    label("loc_1B04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1BD5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B70")

    ChrTalk(
        0xFE,
        (
            "Hugott from next door\x01",
            "can watch the house\x01",
            "himself now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Haha, how nice.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1BD0")

    label("loc_1B70")


    ChrTalk(
        0xFE,
        (
            "I've asked Sarina to\x01",
            "check on him\x01",
            "periodically.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think I'll bring him a\x01",
            "snack later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BD0")

    Jump("loc_2953")

    label("loc_1BD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1D53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CB2")

    ChrTalk(
        0xFE,
        (
            "Sarina next door is late getting\x01",
            "back from work today and asked\x01",
            "me to look after Hugott.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sarina will be hungry when she\x01",
            "gets back too... I'll need to\x01",
            "prepare a lot of dinner for them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1D4E")

    label("loc_1CB2")


    ChrTalk(
        0xFE,
        (
            "I love looking after\x01",
            "children.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. Since I don't get chances like\x01",
            "this often, I'll put everything I've got\x01",
            "into making something good for them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D4E")

    Jump("loc_2953")

    label("loc_1D53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1E7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E0E")

    ChrTalk(
        0xFE,
        (
            "Fran said she's busy\x01",
            "with her operator work\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, it is the\x01",
            "trade conference's main\x01",
            "session.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope it ends without\x01",
            "incident, but...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1E76")

    label("loc_1E0E")


    ChrTalk(
        0xFE,
        (
            "Ah... That Fran. She\x01",
            "forgot her lunchbox\x01",
            "again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I guess I'll have to\x01",
            "bring it to her later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E76")

    Jump("loc_2953")

    label("loc_1E7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1E89")
    Jump("loc_2953")

    label("loc_1E89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_21B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2115")

    ChrTalk(
        0xFE,
        (
            "Umm, that expensive cookie I\x01",
            "bought at the department store\x01",
            "should be here somewhere...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FM-Mom? Could it be...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x109, 0)

    ChrTalk(
        0xFE,
        (
            "Yes, I was thinking of\x01",
            "bringing Fran a snack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You police are busy with\x01",
            "the approaching trade\x01",
            "conference, yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FN-Now look here mom. Saying\x01",
            "things like that when we're\x01",
            "working is a little...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I'm sure Fran will\x01",
            "love it, so I'm sure\x01",
            "it's fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ah, that's right. Since you're\x01",
            "here, I'll also prepare one for\x01",
            "the Special Support Section...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106FWe're fine without!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009F(She goes at her own\x01",
            "pace... Fran might be\x01",
            "similar to Claris.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    OP_93(0xB, 0x5A, 0x0)
    ClearChrFlags(0xB, 0x10)
    Jump("loc_21AD")

    label("loc_2115")


    ChrTalk(
        0xFE,
        (
            "You police are busy with\x01",
            "the approaching trade\x01",
            "conference, yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got to bring Fran a\x01",
            "snack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F(I wonder if that's all\x01",
            "right...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21AD")

    Jump("loc_2953")

    label("loc_21B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_248B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2386")

    ChrTalk(
        0xFE,
        (
            "Come to think of it...\x01",
            "You all got an orbal\x01",
            "car, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if Noｱl's become\x01",
            "more annoying. When it comes\x01",
            "to cars, that girl is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112FT-That's not true.\x01",
            "...Right, everyone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FUmm, I feel like it's\x01",
            "not nothing, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FShe was so excited, she\x01",
            "told us its specs and\x01",
            "stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106FWhat!? D-Did I really!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309FHaha. I looks like she\x01",
            "doesn't even remember\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Goodness gracious...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2486")

    label("loc_2386")


    ChrTalk(
        0xFE,
        (
            "This girl can get really\x01",
            "annoying when it comes\x01",
            "to orbal cars.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ever since the first time she rode a CGF\x01",
            "armored car, she's been saying the speed is\x01",
            "like that and the endurance is like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FI-I know that! You can\x01",
            "stop already, mom!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2486")

    Jump("loc_2953")

    label("loc_248B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2953")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27C7")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x109, 0)

    ChrTalk(
        0xFE,
        (
            "Noｱl, it looks like you've\x01",
            "joined that rumored\x01",
            "Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FUmm, it's called a\x01",
            ""transfer", and it's a\x01",
            "little different, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh come now. You've\x01",
            "always cared excessively\x01",
            "about the fine details.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You girls get to work\x01",
            "together. Fran will be so\x01",
            "happy, she'll jump for joy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00102FHaha. I can already\x01",
            "picture it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F*sigh*, that Fran...\x01",
            "She's always so\x01",
            "childlike.\x02\x03",
            "#10109FW-Well, I'm glad too, of\x01",
            "course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHaha. You sisters really\x01",
            "are close.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a parent, I do worry\x01",
            "about them, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They are both so attractive.\x01",
            "That will make it tough for\x01",
            "their future husbands...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106FM-Mom!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(Haha... Not just the sister-sister\x01",
            "relationship, but the mother-\x01",
            "daughter relationship is good too.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12F, 3)
    Jump("loc_2953")

    label("loc_27C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28DF")

    ChrTalk(
        0xFE,
        (
            "Noｱl, you should show\x01",
            "your face here every now\x01",
            "and then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FHuh? But I've been\x01",
            "stopping by often\x01",
            "recently, haven't I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because your workplace is\x01",
            "closer to our house, you\x01",
            "should stop by more often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FC'mon, don't spoil me\x01",
            "that much...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2953")

    label("loc_28DF")


    ChrTalk(
        0xFE,
        (
            "Noｱl, you should show\x01",
            "your face here every now\x01",
            "and then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Your mother will always\x01",
            "be waiting here for you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2953")

    TalkEnd(0xFE)
    Return()

    # Function_8_DE9 end

    def Function_9_2957(): pass

    label("Function_9_2957")

    OP_4B(0xB, 0xFF)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xB, 0x109, 500)

    ChrTalk(
        0xB,
        "My... If it isn't Noｱl!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102FMom... Thank goodness.\x01",
            "I'm glad you're doing\x01",
            "well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "You too. I didn't see\x01",
            "you for a while and was\x01",
            "getting worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "You were working for the\x01",
            "State Guard for a while and\x01",
            "couldn't return, is that it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10108FU-Umm, you see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "...Ahaha, well it's\x01",
            "fine. I'm sure you had\x01",
            "your own circumstances.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I heard Fran was discharged\x01",
            "from the hospital. Are you\x01",
            "guys working together?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, we're doing our\x01",
            "best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Haha, if that's the case\x01",
            "then I've no right to\x01",
            "say anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Noｱl, you now must do as\x01",
            "you please, the way that\x01",
            "you please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "A way such that you will have no\x01",
            "regrets, and won't embarrass your\x01",
            "father, who is with the Goddess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10101F...Yeah, got it!\x02",
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2C72")
    OP_93(0xB, 0x5A, 0x0)
    Jump("loc_2C79")

    label("loc_2C72")

    OP_93(0xB, 0x10E, 0x0)

    label("loc_2C79")

    SetScenarioFlags(0x1BA, 3)
    Return()

    # Function_9_2957 end

    def Function_10_2C7D(): pass

    label("Function_10_2C7D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2DE7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D58")

    ChrTalk(
        0xFE,
        (
            "Azel went to Downtown\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The old me would have been\x01",
            "angry at him for abandoning\x01",
            "his family, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He is doing his very best\x01",
            "to help his friends, and\x01",
            "everyone else, too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2DE2")

    label("loc_2D58")


    ChrTalk(
        0xFE,
        (
            "Azel is already a man,\x01",
            "so I decided to quit\x01",
            "complaining.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He is doing his very best\x01",
            "to help his friends, and\x01",
            "everyone else, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DE2")

    Jump("loc_3E38")

    label("loc_2DE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2F15")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2ED2")
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Azel hurried back from\x01",
            "Downtown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanks to that, the\x01",
            "crying and scared Hugott\x01",
            "finally calmed down...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I-I didn't cry!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xA, 500)

    ChrTalk(
        0xFE,
        (
            "Haha, that's right.\x01",
            "You're a brave boy,\x01",
            "Hugott.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x0, 1)
    Jump("loc_2F10")

    label("loc_2ED2")


    ChrTalk(
        0xFE,
        (
            "...Anyway, I'm relieved\x01",
            "that Azel is back from\x01",
            "Downtown.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F10")

    Jump("loc_3E38")

    label("loc_2F15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_30BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_302A")

    ChrTalk(
        0xFE,
        (
            "The "Unexplained Accidents"\x01",
            "President Dieter spoke of...\x01",
            "I've heard about them myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But to think they were caused by\x01",
            "the major powers... That's pretty\x01",
            "frightening to be quite honest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've always thought we\x01",
            "needed to be\x01",
            "independent.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_30B6")

    label("loc_302A")


    ChrTalk(
        0xFE,
        (
            "When I think Hugott or Azel\x01",
            "might get wrapped up in an\x01",
            ""Unexplained Accident"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've always thought we\x01",
            "needed to be\x01",
            "independent.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30B6")

    Jump("loc_3E38")

    label("loc_30BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_323E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31B4")

    ChrTalk(
        0xFE,
        (
            "I heard Azel is helping his\x01",
            "delinquent friends with the\x01",
            "Downtown reconstruction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Working for the good of\x01",
            "others? The old Azel would\x01",
            "never have done such a thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. As his older\x01",
            "sister, I'm proud of\x01",
            "him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3239")

    label("loc_31B4")


    ChrTalk(
        0xFE,
        (
            "Before he would do anti-\x01",
            "social and mischievous\x01",
            "things, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's really changed. As\x01",
            "his older sister, I'm\x01",
            "proud of him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3239")

    Jump("loc_3E38")

    label("loc_323E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_32C8")

    ChrTalk(
        0xFE,
        (
            "It's scary, isn't it. To\x01",
            "think there's an\x01",
            "occupation incident...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I work, but I'm taking\x01",
            "the day off just in\x01",
            "case.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E38")

    label("loc_32C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3333")

    ChrTalk(
        0xFE,
        (
            "Yesterday, a big monster\x01",
            "was spotted near the\x01",
            "site of the derailment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "How scary...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E38")

    label("loc_3333")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3341")
    Jump("loc_3E38")

    label("loc_3341")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3352")
    Call(0, 11)
    Jump("loc_3E38")

    label("loc_3352")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3431")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33F9")

    ChrTalk(
        0xFE,
        (
            "Hugott is going to\x01",
            "Sunday School today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Azel skipped out on\x01",
            "Sunday School often...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want Hugott to at\x01",
            "least study properly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_342C")

    label("loc_33F9")


    ChrTalk(
        0xFE,
        (
            "Ah, I mustn't... I've\x01",
            "got to go to work soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_342C")

    Jump("loc_3E38")

    label("loc_3431")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_370F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3698")

    ChrTalk(
        0xFE,
        (
            "I heard a strange customer\x01",
            "came to the bar where Azel\x01",
            "works yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He said he was a man with\x01",
            "blonde hair, a while coat\x01",
            "and he was carrying a lute.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He performed without being\x01",
            "asked and made many passes\x01",
            "at the female customers.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 2)), scpexpr(EXPR_END)), "loc_361A")
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
            "#00006F(He was probably talking\x01",
            "about that prince.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F(Probably? I think you\x01",
            "mean "definitely".)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3690")

    label("loc_361A")


    ChrTalk(
        0x101,
        (
            "#00005F(Blond hair and a lute... I\x01",
            "feel like we've seen someone\x01",
            "like that recently?)\x02\x03",
            "#00004F(...Well, I guess.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3690")

    SetScenarioFlags(0x0, 1)
    Jump("loc_370A")

    label("loc_3698")


    ChrTalk(
        0xFE,
        (
            "Normally, Azel doesn't\x01",
            "say anything about his\x01",
            "work at home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That customer must have\x01",
            "been quite strange.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_370A")

    Jump("loc_3E38")

    label("loc_370F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3828")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37C0")

    ChrTalk(
        0xFE,
        (
            "It seems Claris from\x01",
            "next door is away today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Claris is always helping\x01",
            "look after Hugott...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Next time, I've got to\x01",
            "thank her properly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3823")

    label("loc_37C0")


    ChrTalk(
        0xFE,
        (
            "Claris is always helping\x01",
            "look after Hugott...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Next time, I've got to\x01",
            "thank her properly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3823")

    Jump("loc_3E38")

    label("loc_3828")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_395D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38FE")

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
    SetScenarioFlags(0x0, 1)
    Jump("loc_3958")

    label("loc_38FE")


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

    label("loc_3958")

    Jump("loc_3E38")

    label("loc_395D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3A5C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39FE")

    ChrTalk(
        0xFE,
        (
            "He has the day off\x01",
            "today, so I'm spending\x01",
            "the day with my brother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, hmm... As expected,\x01",
            "playing "Bracer" is a\x01",
            "little...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3A57")

    label("loc_39FE")


    ChrTalk(
        0xFE,
        (
            "Playing "Bracer"? What\x01",
            "am I going to do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Azel's never here in\x01",
            "times like this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A57")

    Jump("loc_3E38")

    label("loc_3A5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3E38")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D01")
    TurnDirection(0xFE, 0x105, 0)

    ChrTalk(
        0xFE,
        "My, you all are...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FOh, if I'm remember it\x01",
            "right, you're... Azel's\x01",
            "older sister.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FUmm... Do you know her?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHehe. Her little brother\x01",
            "Azel is a Testaments\x01",
            "member.\x02\x03",
            "#10300FI think you stormed into\x01",
            "Trinity a while back and\x01",
            "made him quit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FS-Stormed into...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Umm, he must have been a\x01",
            "lot of trouble back\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Back then, I wanted Azel\x01",
            "to leave the gang no\x01",
            "matter what...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FI think all the Testaments\x01",
            "were surprised at your\x01",
            "menacing attitude.\x02\x03",
            "#10309FHehe. That's a technique\x01",
            "to build a brother-sister\x01",
            "bond, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(W-Why does he act like\x01",
            "it's not his\x01",
            "problem...?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12F, 4)
    Jump("loc_3E38")

    label("loc_3D01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DCC")

    ChrTalk(
        0xFE,
        (
            "My younger brother Azel\x01",
            "works part time at\x01",
            "Trinity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's a bad part of town,\x01",
            "so I was scared at\x01",
            "first, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was a little relieved\x01",
            "since he's been keeping\x01",
            "up with it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3E38")

    label("loc_3DCC")


    ChrTalk(
        0xFE,
        (
            "*sigh*, that Azel... He\x01",
            "hardly ever tells me\x01",
            "about his gang.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wish he wouldn't worry\x01",
            "me so much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E38")

    TalkEnd(0xFE)
    Return()

    # Function_10_2C7D end

    def Function_11_3E3C(): pass

    label("Function_11_3E3C")

    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EBC")

    ChrTalk(
        0x9,
        (
            "Alright, I'm heading to\x01",
            "work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Be sure to lock the\x01",
            "door, Hugott.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Yeah, leave it to me~.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3F27")

    label("loc_3EBC")


    ChrTalk(
        0x9,
        (
            "Oh yeah, do your homework\x01",
            "properly, even if your\x01",
            "sister isn't watching you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I know that already~\x02",
    )

    CloseMessageWindow()

    label("loc_3F27")

    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_11_3E3C end

    def Function_12_3F30(): pass

    label("Function_12_3F30")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_40E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4051")

    ChrTalk(
        0xFE,
        (
            "I was really scared when\x01",
            "I saw that pale blue tree\x01",
            "appear outside, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My brother was okay, and\x01",
            "that encouraged me\x01",
            "somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even though he's my big brother, I don't\x01",
            "think he can do that much but... Ehehe,\x01",
            "that cheered me up for some reason.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_40DB")

    label("loc_4051")


    ChrTalk(
        0xFE,
        (
            "I was scared seeing that\x01",
            "pale blue tree, but my\x01",
            "brother cheered me up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ehehe, my brother's so\x01",
            "cool. I cheered up\x01",
            "thanks to him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40DB")

    Jump("loc_4661")

    label("loc_40E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_412C")

    ChrTalk(
        0xFE,
        (
            "Because my brother is\x01",
            "here, I'm sure it'll be\x01",
            "all right.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4661")

    label("loc_412C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_41AA")

    ChrTalk(
        0xFE,
        (
            "Crossbell in-de-pen-\x01",
            "dence... What does that\x01",
            "mean?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't get it. I'm sure\x01",
            "Miss Marble would\x01",
            "know...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4661")

    label("loc_41AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_421F")

    ChrTalk(
        0xFE,
        (
            "I wonder if there's\x01",
            "anything I can do to\x01",
            "help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Should I head over to my\x01",
            "brother in Downtown?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4661")

    label("loc_421F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_429B")

    ChrTalk(
        0xFE,
        (
            "It looks like something\x01",
            "terrible has happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder when my brother\x01",
            "Azel is going to be\x01",
            "back...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4661")

    label("loc_429B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4311")

    ChrTalk(
        0xFE,
        (
            "Yesterday, a train fell\x01",
            "over, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How scary... Why did\x01",
            "something like that have\x01",
            "to happen?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4661")

    label("loc_4311")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4425")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43D2")
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xFE,
        "Ah~, I hate homework.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "You can do it, Hugott.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Your grandma has a\x01",
            "reward snack ready for\x01",
            "you, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Really!? Alright, I'll\x01",
            "do my best!\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x0, 2)
    Jump("loc_4420")

    label("loc_43D2")


    ChrTalk(
        0xFE,
        "Umm, 14 times 23 is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, two-column\x01",
            "multiplication sure is\x01",
            "hard.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4420")

    Jump("loc_4661")

    label("loc_4425")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4436")
    Call(0, 11)
    Jump("loc_4661")

    label("loc_4436")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4444")
    Jump("loc_4661")

    label("loc_4444")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_44C4")

    ChrTalk(
        0xFE,
        (
            "Lately, my brother has\x01",
            "been coming back once\x01",
            "every three days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's been bringing\x01",
            "snacks from his work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4661")

    label("loc_44C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_455A")

    ChrTalk(
        0xFE,
        (
            "Claris said she was\x01",
            "going to the cathedral\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Come to think of it, I feel\x01",
            "like she went there on the\x01",
            "same day last month.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4661")

    label("loc_455A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4568")
    Jump("loc_4661")

    label("loc_4568")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_45FB")

    ChrTalk(
        0xFE,
        (
            "My sister says she\x01",
            "doesn't know how to play\x01",
            ""bracer".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Aw, can't be helped I\x01",
            "guess. I wonder if playing\x01",
            ""house" will be ok.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4661")

    label("loc_45FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4661")

    ChrTalk(
        0xFE,
        (
            "Azel is working as a\x01",
            "bartender in Downtown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ehehe, he's so cool. I'm\x01",
            "proud of him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4661")

    TalkEnd(0xFE)
    Return()

    # Function_12_3F30 end

    def Function_13_4665(): pass

    label("Function_13_4665")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4870")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x105, 500)

    ChrTalk(
        0xFE,
        (
            "Huh... W-Wazy!? You're\x01",
            "back in Crossbell!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10400FHaha, it's been a while,\x01",
            "Azel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Those clothes... And\x01",
            "where is Abbas!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404FThere's an explanation for\x01",
            "all of this, but I don't have\x01",
            "time for it right now.\x02\x03",
            "#10400FI'll explain in detail later.\x01",
            "For now, be sure to protect\x01",
            "your brother and sister.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "S-Sure... I get that\x01",
            "it's not time for that\x01",
            "right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But Wazy, thank goodness\x01",
            "you're safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10402FHaha, you too. ...Later,\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BA, 4)
    Jump("loc_49EE")

    label("loc_4870")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_494C")

    ChrTalk(
        0xFE,
        (
            "The monsters wandering\x01",
            "around outside seem to show\x01",
            "no sign of entering homes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...But, we mustn't be\x01",
            "careless. We've got to\x01",
            "keep on guard...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll definitely protect\x01",
            "my brother and sister!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_49EE")

    label("loc_494C")


    ChrTalk(
        0xFE,
        (
            "The monsters wandering around outside\x01",
            "seem to show no sign of entering\x01",
            "homes, but I mustn't be careless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll definitely protect\x01",
            "my brother and sister!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49EE")

    TalkEnd(0xFE)
    Return()

    # Function_13_4665 end

    def Function_14_49F2(): pass

    label("Function_14_49F2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4A03")
    Jump("loc_58C4")

    label("loc_4A03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4A11")
    Jump("loc_58C4")

    label("loc_4A11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4C5A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B01")

    ChrTalk(
        0xFE,
        (
            "I've decided to leave\x01",
            "Crossbell today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I packed in a hurry,\x01",
            "but... This book is too\x01",
            "bulky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you like, I'll give\x01",
            "it to you.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x2F8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x2F8, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x189, 2)
    Jump("loc_4C55")

    label("loc_4B01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BCF")

    ChrTalk(
        0xFE,
        (
            "I received an evacuation\x01",
            "order from the Imperial\x01",
            "government.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm planning on leaving\x01",
            "Crossbell via train\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It looks like the\x01",
            "station's congested, so\x01",
            "I've got to hurry.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4C55")

    label("loc_4BCF")


    ChrTalk(
        0xFE,
        (
            "I didn't expect to leave\x01",
            "Crossbell like this, but...\x01",
            "To me, family is first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems congested, so\x01",
            "I've got to board ASAP.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C55")

    Jump("loc_58C4")

    label("loc_4C5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4DB3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D4D")

    ChrTalk(
        0xFE,
        (
            "My family in the Empire\x01",
            "was worried about me and\x01",
            "sent a letter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That incident happened, and\x01",
            "I'd like to return to my\x01",
            "home country soon as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if I should\x01",
            "consult the main office\x01",
            "about this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4DAE")

    label("loc_4D4D")


    ChrTalk(
        0xFE,
        (
            "My family is worried\x01",
            "about me, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think I'll make plans\x01",
            "to return to the Empire.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DAE")

    Jump("loc_58C4")

    label("loc_4DB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4E75")

    ChrTalk(
        0xFE,
        (
            "To think an armed group has\x01",
            "laid siege to Mainz... That\x01",
            "kind of thing is unheard of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, all I can do is pray to\x01",
            "the Goddess that the\x01",
            "situation's resolved quickly...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58C4")

    label("loc_4E75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4FDE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F48")

    ChrTalk(
        0xFE,
        (
            "My wife and daughter who\x01",
            "came to visit returned\x01",
            "to the Empire today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yesterday's derailment really sent a\x01",
            "chill down my spine... Thank goodness\x01",
            "service was restored quickly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4FD9")

    label("loc_4F48")


    ChrTalk(
        0xFE,
        (
            "But even so... It's been a\x01",
            "while since I was able to spend\x01",
            "time with my wife and daughter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, I might be getting\x01",
            "a little homesick.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FD9")

    Jump("loc_58C4")

    label("loc_4FDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4FEC")
    Jump("loc_58C4")

    label("loc_4FEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_506C")

    ChrTalk(
        0xFE,
        (
            "I see... You're already\x01",
            "going back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll be lonely a while\x01",
            "longer... Please, take\x01",
            "care of our daughter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58C4")

    label("loc_506C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_51D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_513A")

    ChrTalk(
        0xFE,
        (
            "My wife and daughter came\x01",
            "to visit from her parents'\x01",
            "home in the Empire...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was surprised because they\x01",
            "didn't contact me before\x01",
            "coming, but... I-I'm happy.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x10)
    OP_93(0x8, 0x0, 0x0)
    SetScenarioFlags(0x0, 0)
    Jump("loc_51D1")

    label("loc_513A")


    ChrTalk(
        0xFE,
        (
            "Wow, but on yesterday's\x01",
            "train... It would have been\x01",
            "better if they contacted me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sorry I haven't been\x01",
            "able to spend time with\x01",
            "my family.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51D1")

    Jump("loc_58C4")

    label("loc_51D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5277")

    ChrTalk(
        0xFE,
        (
            "The trade conference\x01",
            "developments will likely\x01",
            "influence stock prices...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a securities man,\x01",
            "those movements are\x01",
            "something I can't miss.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58C4")

    label("loc_5277")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_54A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5320")

    ChrTalk(
        0xFE,
        (
            "I heard Mr. Bond's\x01",
            "family cat disappeared\x01",
            "yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I helped look for it, but in\x01",
            "the end we didn't find it...\x01",
            "I wonder what happened?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_54A2")

    label("loc_5320")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5433")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53C0")

    ChrTalk(
        0xFE,
        (
            "Oh, you're looking for\x01",
            "Mr. Bond's family cat?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My daughter can't stop\x01",
            "crying. Poor thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please find her somehow.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_542E")

    label("loc_53C0")


    ChrTalk(
        0xFE,
        (
            "Mr. Bond's cat disappeared\x01",
            "and his daughter won't\x01",
            "stop crying. Poor thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Please find her somehow.\x02",
    )

    CloseMessageWindow()

    label("loc_542E")

    Jump("loc_54A2")

    label("loc_5433")


    ChrTalk(
        0xFE,
        (
            "I heard the little girl\x01",
            "next door's happy voice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems the cat was\x01",
            "found somehow. Thank\x01",
            "goodness.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54A2")

    Jump("loc_58C4")

    label("loc_54A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_562D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5591")

    ChrTalk(
        0xFE,
        (
            "Mr. Bond's family next\x01",
            "door originally lived on\x01",
            "Residential Street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But some things\x01",
            "happened, and they moved\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But even so, their family is\x01",
            "warm and bright. I should\x01",
            "follow their example.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_5628")

    label("loc_5591")


    ChrTalk(
        0xFE,
        (
            "The family next door\x01",
            "moved from Residential\x01",
            "District to here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Some things happened, but...\x01",
            "I want to follow the example\x01",
            "of their brightness.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5628")

    Jump("loc_58C4")

    label("loc_562D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5782")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_570F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5652")
    Call(0, 15)
    Jump("loc_570A")

    label("loc_5652")

    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xC,
        (
            "Thank you for your\x01",
            "concern.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Please let me know if\x01",
            "we're bothering you in\x01",
            "any way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No, no, I should say the\x01",
            "same. Please let me know if\x01",
            "anything's bothering you.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)

    label("loc_570A")

    Jump("loc_577D")

    label("loc_570F")


    ChrTalk(
        0xFE,
        (
            "I seems Mr. Bond is a\x01",
            "securities man, the same\x01",
            "as I.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, he might be a good\x01",
            "conversation partner.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_577D")

    Jump("loc_58C4")

    label("loc_5782")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_58C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5854")

    ChrTalk(
        0xFE,
        (
            "Those bracer kids lived\x01",
            "next door, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's been lonely ever since\x01",
            "they returned to their home\x01",
            "country a few months ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if anyone new\x01",
            "will move in soon...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_58C4")

    label("loc_5854")


    ChrTalk(
        0xFE,
        (
            "It must've been a job\x01",
            "transfer, but even so,\x01",
            "I'm lonely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if anyone will\x01",
            "move in next door...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58C4")

    TalkEnd(0xFE)
    Return()

    # Function_14_49F2 end

    def Function_15_58C8(): pass

    label("Function_15_58C8")

    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0xC,
        "And so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Please let me know if\x01",
            "there's anything\x01",
            "bothering you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Likewise.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Come on. Say hello,\x01",
            "Mary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Meo~w.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha, I'm glad we're all\x01",
            "getting along.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you ever need\x01",
            "anything, don't hesitate\x01",
            "to ask.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "We will. Thank you very\x01",
            "much.\x02",
        )
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

    # Function_15_58C8 end

    def Function_16_5A0E(): pass

    label("Function_16_5A0E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A37")
    Call(0, 22)
    Return()

    label("loc_5A37")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A6B")
    Call(0, 23)
    Return()

    label("loc_5A6B")

    Call(0, 25)
    Return()

    label("loc_5A6F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5C01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B6A")

    ChrTalk(
        0xFE,
        (
            "My business that was at IBC\x01",
            "has resumed operations\x01",
            "using a small rented space.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll be away from work\x01",
            "for a while, so I'll need\x01",
            "to prepare for that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want to do my best for\x01",
            "my the three of us and\x01",
            "our cat.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5BFC")

    label("loc_5B6A")


    ChrTalk(
        0xFE,
        (
            "My business that was at IBC\x01",
            "has resumed operations\x01",
            "using a small rented space.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want to do my best for\x01",
            "my the three of us and\x01",
            "our cat.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BFC")

    Jump("loc_6679")

    label("loc_5C01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5CA4")

    ChrTalk(
        0xFE,
        (
            "Anyway, martial law has been\x01",
            "handed down, so I think it's\x01",
            "best if we stay home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's all right. This\x01",
            "situation can't go on\x01",
            "for too long...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6679")

    label("loc_5CA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5E2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D98")

    ChrTalk(
        0xFE,
        (
            "That declaration must\x01",
            "have strongly provoked\x01",
            "the Empire and Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's possible that\x01",
            "Crossbell will fall into\x01",
            "a dangerous situation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But no matter what\x01",
            "happens, I'll definitely\x01",
            "protect my family.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5E28")

    label("loc_5D98")


    ChrTalk(
        0xFE,
        (
            "Anyway... To get a handle\x01",
            "on this situation, calm\x01",
            "judgment is necessary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll definitely protect\x01",
            "my family... No matter\x01",
            "what happens.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E28")

    Jump("loc_6679")

    label("loc_5E2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_5FE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F48")

    ChrTalk(
        0xFE,
        (
            "The company I work for\x01",
            "moved into the IBC\x01",
            "building, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As you know, it's now a mere\x01",
            "pile of rubble. As a matter of\x01",
            "fact, we're closed right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No one was hurt, so it's\x01",
            "only a matter of time\x01",
            "until we reopen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh*, how troubling.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5FE1")

    label("loc_5F48")


    ChrTalk(
        0xFE,
        (
            "The attackers destroyed\x01",
            "the IBC building and my\x01",
            "business is closed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Although the area around\x01",
            "here wasn't attacked. I\x01",
            "suppose that's good...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FE1")

    Jump("loc_6679")

    label("loc_5FE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6052")

    ChrTalk(
        0xFE,
        (
            "But, this has become a\x01",
            "big problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder what the armed\x01",
            "group's objective is...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6679")

    label("loc_6052")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_60E6")

    ChrTalk(
        0xFE,
        (
            "It's been a while since\x01",
            "I had the day off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's raining too, so I'll\x01",
            "take it easy and spend\x01",
            "the day with my family.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    SetChrSubChip(0xC, 0x1)
    Return()

    label("loc_60E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_60F4")
    Jump("loc_6679")

    label("loc_60F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6102")
    Jump("loc_6679")

    label("loc_6102")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6110")
    Jump("loc_6679")

    label("loc_6110")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6291")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61E9")

    ChrTalk(
        0xFE,
        (
            "Marcy's field is quite\x01",
            "similar to mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For time to time, I try\x01",
            "to predict stock\x01",
            "movements with him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Imperial securities men\x01",
            "have a unique viewpoint.\x01",
            "It's pretty interesting.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_628C")

    label("loc_61E9")


    ChrTalk(
        0xFE,
        (
            "Now then... I've got to\x01",
            "get to work soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm interested in the trade conference,\x01",
            "but... I have no choice but to wait for\x01",
            "news from the Crossbell Times.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_628C")

    Jump("loc_6679")

    label("loc_6291")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_63CD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_636F")

    ChrTalk(
        0xFE,
        (
            "Ah, but I'm really glad\x01",
            "all of you are helping\x01",
            "out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For now, I plan to head\x01",
            "to Central Square to\x01",
            "continue my search.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If anything happens,\x01",
            "please contact me\x01",
            "anytime.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63C8")

    label("loc_636F")


    ChrTalk(
        0xFE,
        (
            "Really, thanks for your\x01",
            "help today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll never forget what\x01",
            "you've done for us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63C8")

    Jump("loc_6679")

    label("loc_63CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6528")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64AF")

    ChrTalk(
        0xFE,
        (
            "Before I had a home\x01",
            "office, but... Here I\x01",
            "have no such luxury.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've begun commuting to\x01",
            "IBC, the same as our\x01",
            "other employees.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've settled in after\x01",
            "moving, and started work\x01",
            "in earnest.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6523")

    label("loc_64AF")


    ChrTalk(
        0xFE,
        (
            "But... The commute to\x01",
            "work isn't too bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm always happy when I\x01",
            "say "I'm home" after a\x01",
            "long day's work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6523")

    Jump("loc_6679")

    label("loc_6528")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6670")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_660A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_654D")
    Call(0, 15)
    Jump("loc_6605")

    label("loc_654D")

    OP_4B(0x8, 0xFF)

    ChrTalk(
        0xC,
        (
            "Thank you for your\x01",
            "concern.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Please let me know if\x01",
            "we're bothering you in\x01",
            "any way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No, no, I should say the\x01",
            "same. Please let me know if\x01",
            "anything's bothering you.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)

    label("loc_6605")

    Jump("loc_666B")

    label("loc_660A")


    ChrTalk(
        0xFE,
        "I'm a very happy man.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is thanks to my\x01",
            "whole family... I'll\x01",
            "treasure them forever.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_666B")

    Jump("loc_6679")

    label("loc_6670")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_6679")

    label("loc_6679")

    TalkEnd(0xFE)
    Return()

    # Function_16_5A0E end

    def Function_17_667D(): pass

    label("Function_17_667D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_66AB")
    Call(0, 22)
    Return()

    label("loc_66AB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_66E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66DF")
    Call(0, 23)
    Return()

    label("loc_66DF")

    Call(0, 25)
    Return()

    label("loc_66E3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6787")

    ChrTalk(
        0xFE,
        (
            "I'm relieved Sophia and\x01",
            "Cindy's home in Residential\x01",
            "District is all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For now anyway, I want\x01",
            "to get back my carefree\x01",
            "everyday life.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_71A1")

    label("loc_6787")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_681D")

    ChrTalk(
        0xFE,
        (
            "I'm worried about my neighbors\x01",
            "from when I lived in\x01",
            "Residential District too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if Sophia and\x01",
            "Cindy are all right...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_71A1")

    label("loc_681D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_68BD")

    ChrTalk(
        0xFE,
        (
            "My wish is not a great one,\x01",
            "but I wonder if Crossbell\x01",
            "City can be as it was before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As long as my family's\x01",
            "happy, that's enough for\x01",
            "me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_71A1")

    label("loc_68BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_69D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6972")

    ChrTalk(
        0xFE,
        "I... saw it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The giant monster that\x01",
            "rampaged through\x01",
            "Downtown...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ah, how terrifying...\x01",
            "Since when did Crossbell\x01",
            "have such scary things...?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_69D2")

    label("loc_6972")


    ChrTalk(
        0xFE,
        (
            "When I think that giant\x01",
            "monster might appear\x01",
            "again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ooh, I just can't stop\x01",
            "shaking.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69D2")

    Jump("loc_71A1")

    label("loc_69D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6A48")

    ChrTalk(
        0xFE,
        (
            "I just can't stand the\x01",
            "smell of blood...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I hope the incident is\x01",
            "resolved safely, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_71A1")

    label("loc_6A48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6B4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6AE0")

    ChrTalk(
        0xFE,
        (
            "Shawawa... Watering\x01",
            "plants heals the heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The sound of the rain is\x01",
            "relaxing too... This is\x01",
            "a nice day to be off.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6B48")

    label("loc_6AE0")


    ChrTalk(
        0xFE,
        (
            "Shawawa... I think I'll\x01",
            "have tea time in a\x01",
            "little while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ah, I've got to give\x01",
            "Mary some food.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B48")

    Jump("loc_71A1")

    label("loc_6B4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6BE7")

    ChrTalk(
        0xFE,
        (
            "I've got to go shopping\x01",
            "later. I wonder if Marte's\x01",
            "holding a sale today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, I'm already\x01",
            "friends with everyone at\x01",
            "the market.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_71A1")

    label("loc_6BE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6D59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CDC")

    ChrTalk(
        0xFE,
        (
            "It seems there's an\x01",
            "important conference today,\x01",
            "and my husband left early.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When we moved here, it\x01",
            "seems he was suddenly\x01",
            "motivated with his work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My husband loves his\x01",
            "family... Haha, that's a\x01",
            "good thing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6D54")

    label("loc_6CDC")


    ChrTalk(
        0xFE,
        (
            "When my husband moved here,\x01",
            "it seems he was suddenly\x01",
            "motivated with his work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, that's a very good\x01",
            "thing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D54")

    Jump("loc_71A1")

    label("loc_6D59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6D67")
    Jump("loc_71A1")

    label("loc_6D67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6EB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E2A")

    ChrTalk(
        0xFE,
        (
            "The man next door shares some\x01",
            "of his profits with everyone\x01",
            "here. He's a very nice man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But somehow, he seems\x01",
            "lonely...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Job transfers must be\x01",
            "lonely too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6EAB")

    label("loc_6E2A")


    ChrTalk(
        0xFE,
        (
            "Job transfers must be\x01",
            "pretty lonely too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Just having my family all\x01",
            "together here would be\x01",
            "enough to call it happiness.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6EAB")

    Jump("loc_71A1")

    label("loc_6EB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6F92")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F39")

    ChrTalk(
        0xFE,
        (
            "Everyone, please take\x01",
            "care of Mary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am sure that girl\x01",
            "really wants to return\x01",
            "home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F8D")

    label("loc_6F39")


    ChrTalk(
        0xFE,
        (
            "Uhuhu, that Sunita\x01",
            "hugged her so tightly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, Mary seemed happy\x01",
            "with it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F8D")

    Jump("loc_71A1")

    label("loc_6F92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_70B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7034")

    ChrTalk(
        0xFE,
        (
            "Our kitchen is a little\x01",
            "small, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It looks like I can use the\x01",
            "flowerpot outside for my\x01",
            "gardening hobby. I kinda like it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_70B3")

    label("loc_7034")


    ChrTalk(
        0xFE,
        (
            "I think it's only a matter\x01",
            "of time before Sunita gets\x01",
            "used to it, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu, it seems there\x01",
            "was no need to worry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_70B3")

    Jump("loc_71A1")

    label("loc_70B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_7198")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7118")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_70DD")
    Call(0, 15)
    Jump("loc_7113")

    label("loc_70DD")


    ChrTalk(
        0xFE,
        (
            "Uhuhu. Thank goodness\x01",
            "the man next door is\x01",
            "nice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7113")

    Jump("loc_7193")

    label("loc_7118")


    ChrTalk(
        0xFE,
        (
            "From now on, we'll get\x01",
            "through anything\x01",
            "together as a family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu, this reminds me\x01",
            "of when we were\x01",
            "newlyweds㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7193")

    Jump("loc_71A1")

    label("loc_7198")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_71A1")

    label("loc_71A1")

    TalkEnd(0xFE)
    Return()

    # Function_17_667D end

    def Function_18_71A5(): pass

    label("Function_18_71A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_71DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71D9")
    Call(0, 23)
    Return()

    label("loc_71D9")

    Call(0, 25)
    Return()

    label("loc_71DD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_72D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7278")

    ChrTalk(
        0xFE,
        (
            "Father, you seem happy\x01",
            "to be working again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, you seem happy\x01",
            "too, Sunita. What do you\x01",
            "think, Mary?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Nya~n?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_72D0")

    label("loc_7278")


    ChrTalk(
        0xFE,
        (
            "Father, you seem happy\x01",
            "to be working again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, you seem happy\x01",
            "too, Sunita.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_72D0")

    Jump("loc_7DAA")

    label("loc_72D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_732F")

    ChrTalk(
        0xFE,
        "Don't worry, ok Mary?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because Sunita will\x01",
            "definitely protect you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7DAA")

    label("loc_732F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7395")

    ChrTalk(
        0xFE,
        (
            "It seems our neighbor is\x01",
            "leaving Crossbell again\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'm getting lonely...\x02",
    )

    CloseMessageWindow()
    Jump("loc_7DAA")

    label("loc_7395")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7416")

    ChrTalk(
        0xFE,
        (
            "I might visit the\x01",
            "charity event with Mary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The rumors say they're\x01",
            "gathering a lot of\x01",
            "pretty girls there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7DAA")

    label("loc_7416")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_7511")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_74A0")

    ChrTalk(
        0xFE,
        (
            "I was told not to go\x01",
            "anywhere far away today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It can't be helped. I'll\x01",
            "stay here and play with\x01",
            "Mary.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_750C")

    label("loc_74A0")


    ChrTalk(
        0xFE,
        (
            "Enough already... We were\x01",
            "supposed to go to the department\x01",
            "store today as a family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "How boring...\x02",
    )

    CloseMessageWindow()

    label("loc_750C")

    Jump("loc_7DAA")

    label("loc_7511")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7595")

    ChrTalk(
        0xFE,
        (
            "Mary washed her face\x01",
            "yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When cats wash their faces,\x01",
            "it'll rain. It's really\x01",
            "true. Sunita's shocked!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7DAA")

    label("loc_7595")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_76B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7667")

    ChrTalk(
        0xFE,
        (
            "Mary seems to be licking\x01",
            "her face really hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When cats wash their faces,\x01",
            "it'll rain. The old street\x01",
            "vendor lady told me that, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Is it going to rain\x01",
            "tomorrow?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_76B0")

    label("loc_7667")


    ChrTalk(
        0xFE,
        (
            "If Mary's washing her\x01",
            "face...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Is it going to rain\x01",
            "tomorrow?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_76B0")

    Jump("loc_7DAA")

    label("loc_76B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_77C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7759")
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xFE,
        (
            "I'm playing with Mary\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*pet, pet pet*...\x02",
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 1200, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1200)

    ChrTalk(
        0xF,
        "Funyaa...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Wah... This really\x01",
            "works!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0xE, 0x10)
    Jump("loc_77C1")

    label("loc_7759")


    ChrTalk(
        0xFE,
        (
            "It's "Green Foxtail"\x01",
            "that the street vendor\x01",
            "told me about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, it looks like Mary\x01",
            "likes it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_77C1")

    Jump("loc_7DAA")

    label("loc_77C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_77D4")
    Jump("loc_7DAA")

    label("loc_77D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_78C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7836")

    ChrTalk(
        0xFE,
        "Mary, remember this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Nyaon...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Nyaon... [I'm tired]\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    ClearChrFlags(0xE, 0x10)
    Jump("loc_78BF")

    label("loc_7836")


    ChrTalk(
        0xFE,
        (
            "So that Mary won't get lost,\x01",
            "I'm teaching her different\x01",
            "things in our house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sure it'll be all\x01",
            "right if I just keep it\x01",
            "up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_78BF")

    Jump("loc_7DAA")

    label("loc_78C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_7B22")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7A33")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_79D7")
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xE,
        "Oh, Mary... I'm sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I... It's because I did\x01",
            "something I shouldn't\x01",
            "have...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Sunita...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F(...We've got to find\x01",
            "her quickly.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(That's right... Anyway,\x01",
            "let's just do our best.)\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x0, 6)
    Jump("loc_7A2E")

    label("loc_79D7")


    ChrTalk(
        0xFE,
        "Oh, Mary... I'm sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I... It's because I did\x01",
            "something I shouldn't\x01",
            "have...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A2E")

    Jump("loc_7B1D")

    label("loc_7A33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7ACE")
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xE,
        (
            "Thank goodness you're\x01",
            "all right, Mary...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "*sigh*... As punishment,\x01",
            "I'm going to hold you\x01",
            "all day long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Nya, nya~n?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    OP_4C(0xF, 0xFF)
    Jump("loc_7B1D")

    label("loc_7ACE")

    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xE,
        (
            "Come now, Mary. Prepare\x01",
            "yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "*huuuug*.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "N-Nyaa～n㈱\x02",
    )

    CloseMessageWindow()
    OP_4C(0xF, 0xFF)

    label("loc_7B1D")

    Jump("loc_7DAA")

    label("loc_7B22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7C3E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7BDA")

    ChrTalk(
        0xFE,
        (
            "Sunita likes our new\x01",
            "home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, Mary has been\x01",
            "looking strange ever\x01",
            "since we came here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe she's shocked\x01",
            "because we moved here so\x01",
            "suddenly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7C39")

    label("loc_7BDA")


    ChrTalk(
        0xFE,
        (
            "Mary seems scared,\x01",
            "somehow...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe she's shocked\x01",
            "because we moved here so\x01",
            "suddenly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C39")

    Jump("loc_7DAA")

    label("loc_7C3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_7DA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7CE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C63")
    Call(0, 15)
    Jump("loc_7CDC")

    label("loc_7C63")


    ChrTalk(
        0xFE,
        (
            "Heheh, it's times like this\x01",
            "when I'm glad I taught Mary\x01",
            "proper greetings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanks to that, I'm not\x01",
            "embarrassed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7CDC")

    Jump("loc_7D9C")

    label("loc_7CE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D37")

    ChrTalk(
        0xFE,
        (
            "Haha, Mary is very well-\x01",
            "behaved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a reward, I'll pet\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D9C")

    label("loc_7D37")


    ChrTalk(
        0xFE,
        (
            "My mom and dad get along\x01",
            "way better than they did\x01",
            "before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sunita is very happy\x01",
            "about that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D9C")

    Jump("loc_7DAA")

    label("loc_7DA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_7DAA")

    label("loc_7DAA")

    TalkEnd(0xFE)
    Return()

    # Function_18_71A5 end

    def Function_19_7DAE(): pass

    label("Function_19_7DAE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7DD0")

    ChrTalk(
        0xFE,
        "...Nyaon...\x02",
    )

    CloseMessageWindow()
    Jump("loc_8084")

    label("loc_7DD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_7DF9")

    ChrTalk(
        0xFE,
        "Nyao? [What's wrong?]\x02",
    )

    CloseMessageWindow()
    Jump("loc_8084")

    label("loc_7DF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7E14")

    ChrTalk(
        0xFE,
        "Nyaa...\x02",
    )

    CloseMessageWindow()
    Jump("loc_8084")

    label("loc_7E14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7E2E")

    ChrTalk(
        0xFE,
        "Myaon.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8084")

    label("loc_7E2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_7E4A")

    ChrTalk(
        0xFE,
        "Funyaan.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8084")

    label("loc_7E4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7E66")

    ChrTalk(
        0xFE,
        "Nyaan...\x02",
    )

    CloseMessageWindow()
    Jump("loc_8084")

    label("loc_7E66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_7E9C")
    TurnDirection(0xF, 0xE, 500)
    Sleep(500)

    ChrTalk(
        0xFE,
        "Nyanya... (*lick, lick*)\x02",
    )

    CloseMessageWindow()
    Jump("loc_8084")

    label("loc_7E9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_7EBB")

    ChrTalk(
        0xFE,
        "Fumyaawn...\x02",
    )

    CloseMessageWindow()
    Jump("loc_8084")

    label("loc_7EBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7EC9")
    Jump("loc_8084")

    label("loc_7EC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7F0C")

    ChrTalk(
        0xFE,
        (
            "Nyaago. [It's been a\x01",
            "while. How have you\x01",
            "been?]\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8084")

    label("loc_7F0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_8004")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FB0")
    OP_4B(0xE, 0xFF)

    ChrTalk(
        0xE,
        (
            "Thank goodness you're\x01",
            "all right, Mary...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "*sigh*... As punishment,\x01",
            "I'm going to hold you\x01",
            "all day long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Nya, nya~n?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    OP_4C(0xE, 0xFF)
    Jump("loc_7FFF")

    label("loc_7FB0")

    OP_4B(0xE, 0xFF)

    ChrTalk(
        0xE,
        (
            "Come now, Mary. Prepare\x01",
            "yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "*huuuug*.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "N-Nyaa～n㈱\x02",
    )

    CloseMessageWindow()
    OP_4C(0xE, 0xFF)

    label("loc_7FFF")

    Jump("loc_8084")

    label("loc_8004")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_801F")

    ChrTalk(
        0xFE,
        "Nyaa...\x02",
    )

    CloseMessageWindow()
    Jump("loc_8084")

    label("loc_801F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_807B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8043")

    ChrTalk(
        0xFE,
        "Meo~w.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8076")

    label("loc_8043")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8066")

    ChrTalk(
        0xFE,
        "Purr, nya～n㈱\x02",
    )

    CloseMessageWindow()
    Jump("loc_8076")

    label("loc_8066")


    ChrTalk(
        0xFE,
        "Nyannyan♪\x02",
    )

    CloseMessageWindow()

    label("loc_8076")

    Jump("loc_8084")

    label("loc_807B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_8084")

    label("loc_8084")

    TalkEnd(0xFE)
    Return()

    # Function_19_7DAE end

    def Function_20_8088(): pass

    label("Function_20_8088")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_8122")
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0xFE,
        (
            "We mustn't interfere\x01",
            "with work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Dear, watch your health\x01",
            "until your work is\x01",
            "finished, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Yeah... I'll be careful.\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    Jump("loc_81BF")

    label("loc_8122")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_81BF")
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Even so, dear, have you\x01",
            "lost weight?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You'll be living alone,\x01",
            "so be sure to eat\x01",
            "properly, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha... Don't be so hard\x01",
            "on me.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)

    label("loc_81BF")

    TalkEnd(0xFE)
    Return()

    # Function_20_8088 end

    def Function_21_81C3(): pass

    label("Function_21_81C3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_8230")

    ChrTalk(
        0xFE,
        (
            "Tch, I've got to head\x01",
            "back already, they said.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want to come visit\x01",
            "papa again...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_82B8")

    label("loc_8230")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_82B8")

    ChrTalk(
        0xFE,
        (
            "You know, papa. In the\x01",
            "parade photo the other day,\x01",
            "you looked really happy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You were a little out of\x01",
            "focus, though~.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_82B8")

    TalkEnd(0xFE)
    Return()

    # Function_21_81C3 end

    def Function_22_82BC(): pass

    label("Function_22_82BC")

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
        (
            "Oh honey, we have\x01",
            "guests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Oh, it's you all...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FWe're with the Crossbell\x01",
            "Police, Special Support\x01",
            "Section.\x02\x03",
            "You're Mr. Bond, correct?\x01",
            "Didn't you get tied up in\x01",
            "the incident with that cult?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_84EC")
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
            "#1KZnK [Search for Lost Cat\x01",
            "Owner]? (debug)\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[No Change]\x01",         # 0
            "[Did it]\x01",            # 1
            "[Didn't do it]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_84D8")
    OP_29(0x8, 0x4, 0x10)
    Jump("loc_84EC")

    label("loc_84D8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_84EC")
    OP_29(0x8, 0x3, 0x10)

    label("loc_84EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_861B")

    ChrTalk(
        0xC,
        (
            "Yeah, how could I\x01",
            "forget.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "You are none other than the team\x01",
            "that freed us from the prison\x01",
            "within that abysmal Fort.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Not to mention you helped\x01",
            "us find our cat Mary once\x01",
            "before as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I always wanted to find a way\x01",
            "to at least express my\x01",
            "gratitude. Thank you so much.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_86F0")

    label("loc_861B")


    ChrTalk(
        0xC,
        (
            "Yeah, how could I\x01",
            "forget.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "You are none other than the team\x01",
            "that freed us from the prison\x01",
            "within that abysmal Fort.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I always wanted to find a way\x01",
            "to at least express my\x01",
            "gratitude. Thank you so much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_86F0")


    ChrTalk(
        0xD,
        (
            "Please allow me to\x01",
            "express my sincere\x01",
            "thanks as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Thank goodness you were\x01",
            "there for my husband\x01",
            "when he was trapped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00004FOh no, please don't\x01",
            "worry about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FBut we are glad to see\x01",
            "that you're all doing\x01",
            "well now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Haha, only because of\x01",
            "all of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "But is there something I\x01",
            "can help you with today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FWell actually....\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "They gave Bond the details of\x01",
            "their investigation and asked\x01",
            "for clarification on their move.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xC,
        (
            "Suspicious residence\x01",
            "change notices, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "So you want to hear the\x01",
            "details of how I sold\x01",
            "the house?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103FYes. Sorry to pry, but we\x01",
            "need to confirm that\x01",
            "nothing illegal occurred.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "No, you aren't prying at\x01",
            "all. I understand where\x01",
            "you're coming from.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well, the sad truth of the matter\x01",
            "is that we had to sell off the\x01",
            "house to repay our debts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The purchaser ended up being the same\x01",
            "real estate agency and all of the\x01",
            "processes were followed correctly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "So I guess you could say that\x01",
            "there's absolutely nothing illegal\x01",
            "about this situation at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00005FSo that's how it is,\x01",
            "huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103FUm, please don't feel that\x01",
            "you have to answer if you'd\x01",
            "prefer not to, but...\x02\x03",
            "#00101FWould you mind discussing\x01",
            "the cause of the debt in\x01",
            "the first place?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "No it's not a problem. I\x01",
            "don't have anything to\x01",
            "hide.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Though it's tough for me\x01",
            "to remember the details\x01",
            "from so long ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I knew the heavy risk I\x01",
            "was taking by investing in\x01",
            "those stupid blue pills.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "And it all came crashing\x01",
            "down at the end of the\x01",
            "case with the cult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10105FOh, so that's what\x01",
            "happened...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Yeah. But actually, I'm\x01",
            "blessed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "By selling all of my property\x01",
            "including my house, I was able\x01",
            "to repay most of the debt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Those were my personal\x01",
            "losses, but fortunately I\x01",
            "didn't end up losing my job.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0x0)

    ChrTalk(
        0xC,
        (
            "And most importantly, my\x01",
            "wife and daughter have not\x01",
            "abandoned my pitiful self.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xD, 0x0)

    ChrTalk(
        0xD,
        (
            "#11PDear... You promised you\x01",
            "wouldn't say things like\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PAfter all, we're the\x01",
            "only family we've got in\x01",
            "this world.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PIt's only natural to\x01",
            "share our troubles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Creil... Thank you so\x01",
            "much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'm so grateful I can\x01",
            "stay with you and\x01",
            "Sunita.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xD)

    ChrTalk(
        0xD,
        (
            "#11PDear, it's kind of\x01",
            "embarrassing hearing you say\x01",
            "that with everyone watching.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10109FHaha, you two really do\x01",
            "share a very strong\x01",
            "bond.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FWell, I guess it doesn't really\x01",
            "matter where you live so long\x01",
            "as you share a strong bond.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0x2)
    SetChrSubChip(0xD, 0x1)

    ChrTalk(
        0xC,
        (
            "Haha, I think that's a\x01",
            "bit of an exaggeration,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Anyway, I plan to make a\x01",
            "fresh start and do my\x01",
            "best from here on out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "And I'll be sure to pay\x01",
            "off the rest of the debt\x01",
            "for my wife and daughter.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xD, 0x0)

    ChrTalk(
        0xD,
        "Dear...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00104FThat's a good attitude.\x02\x03",
            "#00100FPlease let us know if\x01",
            "you need any more help\x01",
            "from now on.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xD, 0x1)

    ChrTalk(
        0x101,
        (
            "#12P#00000FYes, we'll be there for\x01",
            "you then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Haha, I'm grateful that\x01",
            "you'd do that for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Sure, I'll contact you\x01",
            "if anything happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "So, was that all for the\x01",
            "questions?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'll answer any others\x01",
            "you might have...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FNo, we've gotten the\x01",
            "info we need.\x02\x03",
            "#00004FWe appreciate your\x01",
            "cooperation with our\x01",
            "investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FShould we get going,\x01",
            "then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FYes, let's.\x02\x03",
            "#00104FAlright Mr. Bond, we'll\x01",
            "be taking our leave now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10109FPlease keep raising such\x01",
            "a lovely family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Of course!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Uhuhu, we will.\x02",
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

    def lambda_950D():
        OP_95(0xFE, 51400, 0, 2650, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_950D)

    def lambda_9527():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9527)
    Sleep(900)

    def lambda_953B():
        OP_95(0xFE, 52300, 0, 2750, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_953B)

    def lambda_9555():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9555)
    Sleep(900)

    def lambda_9569():
        OP_95(0xFE, 51400, 0, 3650, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9569)

    def lambda_9583():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9583)
    Sleep(900)
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)

    def lambda_95A9():
        OP_95(0xFE, 52300, 0, 3750, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_95A9)

    def lambda_95C3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_95C3)
    Sleep(700)
    Sound(104, 0, 100, 0)
    OP_71(0x1, 0x10, 0x0, 0x0, 0x0)
    OP_79(0x1)
    Sleep(200)

    def lambda_95EF():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_95EF)
    Sleep(50)

    def lambda_95FF():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_95FF)
    Sleep(1000)

    ChrTalk(
        0xE,
        "#6POh, hey guys...\x02",
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

    def lambda_967B():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_967B)
    Sleep(50)

    def lambda_968B():
        OP_93(0x102, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_968B)
    Sleep(50)

    def lambda_969B():
        OP_93(0x109, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_969B)
    Sleep(50)

    def lambda_96AB():
        OP_93(0x105, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_96AB)
    Sleep(50)

    def lambda_96BB():
        OP_95(0x101, 50250, 0, 2650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_96BB)
    Sleep(50)

    def lambda_96D8():
        OP_95(0x102, 50500, 0, 3650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_96D8)
    Sleep(50)

    def lambda_96F5():
        OP_95(0x109, 51500, 0, 2550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_96F5)
    Sleep(50)

    def lambda_9712():
        OP_95(0x105, 51750, 0, 3750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9712)
    SetMapObjFlags(0x1, 0x0)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0xE,
        (
            "#6PDid you guys talk to my\x01",
            "mom and dad?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, we had a little\x01",
            "discussion with them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00100FThey mentioned you too,\x01",
            "Sunita. You have great\x01",
            "parents.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xE,
        "#6PYeah, I know!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#6PEspecially after the\x01",
            "move, they've been so\x01",
            "good to each other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#6PEhehe, they're the best\x01",
            "parents!\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xE, 0x0, 0x1F4)

    ChrTalk(
        0xE,
        "#12PIsn't that right, Mary?\x02",
    )

    CloseMessageWindow()
    OP_93(0xF, 0xB4, 0x1F4)

    ChrTalk(
        0xF,
        "#6PMeow㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102FHaha, her positive\x01",
            "outlook is incredible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, it's wonderful.\x02",
    )

    CloseMessageWindow()

    def lambda_9913():
        OP_93(0x101, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9913)
    Sleep(50)

    def lambda_9923():
        OP_93(0x102, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9923)
    Sleep(50)

    def lambda_9933():
        OP_93(0x109, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9933)
    Sleep(50)

    def lambda_9943():
        OP_93(0x105, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9943)

    ChrTalk(
        0x101,
        (
            "#12P#00003FAlright then. With this,\x01",
            "we've confirmed Mr.\x01",
            "Bond's situation, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x6A, 0x1, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9AA5")
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
            "◆Investigation Status?\x01",
            "(Debug)\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[No Change]\x01",                          # 0
            "[Investigations Remaining]\x01",           # 1
            "[All 6 Investigations Finished]\x01",      # 2
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
        (0, "loc_9A78"),
        (1, "loc_9A7D"),
        (2, "loc_9A91"),
        (SWITCH_DEFAULT, "loc_9AA5"),
    )


    label("loc_9A78")

    Jump("loc_9AA5")

    label("loc_9A7D")

    ClearScenarioFlags(0x131, 5)
    ClearScenarioFlags(0x131, 6)
    ClearScenarioFlags(0x132, 0)
    ClearScenarioFlags(0x132, 1)
    ClearScenarioFlags(0x132, 2)
    Jump("loc_9AA5")

    label("loc_9A91")

    SetScenarioFlags(0x131, 5)
    SetScenarioFlags(0x131, 6)
    SetScenarioFlags(0x132, 0)
    SetScenarioFlags(0x132, 1)
    SetScenarioFlags(0x132, 2)
    Jump("loc_9AA5")

    label("loc_9AA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9B03")

    ChrTalk(
        0x101,
        (
            "#12P#00000FAlright, then let's\x01",
            "continue our\x01",
            "investigation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9B83")

    label("loc_9B03")


    ChrTalk(
        0x101,
        (
            "#12P#00000FAlright! We've finished\x01",
            "our investigation.\x02\x03",
            "Let's head back to the\x01",
            "City Meeting Hall and\x01",
            "make our report.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x6A, 0x1, 0x6)

    label("loc_9B83")

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

    # Function_22_82BC end

    def Function_23_9BE9(): pass

    label("Function_23_9BE9")

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
            "*sob, sob*... Sunita did\x01",
            "a bad thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "It's because Sunita\x01",
            "wasn't watching Mary\x01",
            "properly...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Sunita... You mustn't\x01",
            "blame yourself so much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#5PYeah. And we'll\x01",
            "definitely find Mary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#5PSo cheer up, Sunita.\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xC, 0x10E, 0x1F4)

    ChrTalk(
        0xC,
        "#11POh, it's you guys!\x02",
    )

    CloseMessageWindow()

    def lambda_9DAA():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_9DAA)
    Sleep(50)

    def lambda_9DBA():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_9DBA)
    WaitChrThread(0xD, 1)

    ChrTalk(
        0xD,
        "Ah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FGood day. We're here\x01",
            "about your request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PYou saw it then... I'm\x01",
            "so glad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PTo be perfectly honest, I questioned\x01",
            "whether the Guild is better for this\x01",
            "type of request, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PYou guys came to mind so\x01",
            "I thought I'd ask for\x01",
            "your help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FWe're glad you feel that\x01",
            "way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10103FYou said your kitten\x01",
            "Mary is missing.\x02\x03",
            "#10100FDo you know when she\x01",
            "disappeared?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PI don't know the exact\x01",
            "time, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PIt was sometime after\x01",
            "yesterday evening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "We were looking after\x01",
            "our stall on East Street\x01",
            "when Sunita realized.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "It's as if she suddenly\x01",
            "disappeared when we took\x01",
            "our eyes off her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "After that, everyone in the\x01",
            "shopping district helped us\x01",
            "search nearby, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PYeah, everyone searched\x01",
            "until evening, but in the\x01",
            "end, we didn't find her.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xC, 500)

    ChrTalk(
        0xE,
        (
            "*sob, sob*... You're a\x01",
            "liar, dad!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "You said she'd be back\x01",
            "by morning!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xE, 500)

    ChrTalk(
        0xC,
        "#5PSorry, Sunita...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00108FSunita...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001FBy the way... Were there\x01",
            "any sightings of her?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A1D6():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_A1D6)
    Sleep(50)

    def lambda_A1E6():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_A1E6)
    WaitChrThread(0xE, 2)

    ChrTalk(
        0xC,
        (
            "#11PYeah─ Though all of them\x01",
            "are from yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PBased on the information\x01",
            "we've gotten, she didn't\x01",
            "go out to the highway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PAnd there was someone who\x01",
            "said they saw Mary go in the\x01",
            "direction of Central Square.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PAt that point yesterday it was already\x01",
            "late in the evening. We couldn't chase\x01",
            "her down and gave up the search...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00301FAnd there's been no news\x01",
            "this morning.\x02\x03",
            "#00303FSo if she is in the city,\x01",
            "it's a complete mystery\x01",
            "as to where she's gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FThen our search area is\x01",
            "the entire city?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FHmm. I would really like\x01",
            "a few more clues, but...\x02\x03",
            "#00001FSorry but... Has Mary\x01",
            "ever left home?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PNo, never once, before\x01",
            "now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PMary loves Sunita, you\x01",
            "see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11POn top of that, Mary's timid. If she\x01",
            "got separated from Sunita, it's hard\x01",
            "to believe she'd go anywhere else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PThat's why I think she\x01",
            "lost sight of us for some\x01",
            "reason and got lost.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00003FI see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FAnyway, I guess all we\x01",
            "can do is try searching\x01",
            "in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FYeah, let's start there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PIf I calm down, I intend\x01",
            "to search for her again,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PBut this could take a while,\x01",
            "so I don't mind if you take\x01",
            "care of other things first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FHmm...\x02",
    )

    CloseMessageWindow()
    OP_29(0x74, 0x1, 0x0)
    Call(0, 24)
    EventEnd(0x5)
    Return()

    # Function_23_9BE9 end

    def Function_24_A6DB(): pass

    label("Function_24_A6DB")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Begin the search immediately]\x01",      # 0
            "[Have them wait a bit longer]\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A7BA")

    ChrTalk(
        0x101,
        (
            "#6P#00000FWe're fine for now. I\x01",
            "was thinking of starting\x01",
            "immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PI see. That's great.\x02",
    )

    CloseMessageWindow()
    Call(0, 26)
    Jump("loc_A834")

    label("loc_A7BA")

    OP_29(0x74, 0x1, 0x1)

    ChrTalk(
        0x101,
        (
            "#6P#00000FI'm terribly sorry,\x01",
            "but... Can you wait a\x01",
            "little longer?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PI understand. See you\x01",
            "later, then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A834")

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

    # Function_24_A6DB end

    def Function_25_A885(): pass

    label("Function_25_A885")

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
        "#11PAh, you guys, huh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PCan you begin looking\x01",
            "for Mary?\x02",
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
            "[Begin searching for the kitten]\x01",      # 0
            "[Have them wait a bit longer]\x01",         # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AA4B")

    ChrTalk(
        0x101,
        (
            "#6P#00000FYes, I think we can\x01",
            "begin right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PI see. That's great.\x02",
    )

    CloseMessageWindow()
    Call(0, 26)
    Jump("loc_AACC")

    label("loc_AA4B")


    ChrTalk(
        0x101,
        (
            "#6P#00006FSorry, we have some\x01",
            "preparations to do...\x02\x03",
            "#00000FCan you wait a little\x01",
            "longer for us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PYeah, understood.\x02",
    )

    CloseMessageWindow()

    label("loc_AACC")

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

    # Function_25_A885 end

    def Function_26_AB1A(): pass

    label("Function_26_AB1A")

    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#6P#00100FSo Lloyd, where are we\x01",
            "searching first?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#6P#00003FHmm. It might be a repeat of\x01",
            "yesterday, but...\x02\x03",
            "#00000FTo retrace her steps\x01",
            "yesterday, we should start\x01",
            "with a survey of East Street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00300FYeah, that sounds\x01",
            "logical.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FHehe. Those are the\x01",
            "basics, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100FBy the way, do you have\x01",
            "any idea where Mary might\x01",
            "have gone on East Street?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_ACB2():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_ACB2)
    Sleep(50)

    def lambda_ACC2():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_ACC2)
    Sleep(300)

    ChrTalk(
        0xD,
        (
            "Yes, probably to the\x01",
            "fish seller's stall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Around here, that's the\x01",
            "place she'd probably be\x01",
            "the most interested in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PYeah. We didn't check it this\x01",
            "morning, so it's possible\x01",
            "they might have spotted her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PMarte, the owner, helped us\x01",
            "look for Mary yesterday, so he\x01",
            "would know if she stopped by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PIf it's not too much\x01",
            "trouble, can you ask him\x01",
            "for me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FSure, sounds good.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xC, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#6P#00100FAnyway, what will you\x01",
            "do, Mr. Bond?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "#11PFortunately, I'm off\x01",
            "from work today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PI'm planning to resume\x01",
            "the search from yesterday\x01",
            "in a little while, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PI already asked almost\x01",
            "everyone on East Street\x01",
            "yesterday, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PToday, I was thinking of making a\x01",
            "thorough search of Central Square\x01",
            "and seeing if any info turned up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PIf you learn anything\x01",
            "new, please come tell me\x01",
            "anytime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00300FGot it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FThen first up, we have\x01",
            "an interview with a\x01",
            "certain fishmonger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FYeah, let's head there.\x02",
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
            "Quest [Search for Lost\x01",
            "Kitten]\x07\x00",
            " started!\x02",
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

    # Function_26_AB1A end

    def Function_27_B179(): pass

    label("Function_27_B179")

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
        "#5PMary!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5POh! Where did you run\x01",
            "off to!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5P*sob, sob*... I was\x01",
            "really worried about\x01",
            "you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#12PMeow, meow.\x02",
    )

    CloseMessageWindow()
    OP_97(0xF, 0x0, 0x0, 0x2EE, 0x3E8, 0x0)
    Sleep(300)

    ChrTalk(
        0xE,
        (
            "#5PNo... I'm the sorry one.\x01",
            "Everything is Sunita's\x01",
            "fault.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PBut thank you... You\x01",
            "brought her home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PDon't run off anywhere\x01",
            "by yourself again, ok?\x02",
        )
    )

    CloseMessageWindow()
    OP_97(0xF, 0x0, 0x0, 0x1F4, 0x3E8, 0x0)
    Sleep(300)
    Sound(953, 0, 100, 0)

    ChrTalk(
        0xF,
        "#12PMeow㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00109FHaha, that's great.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10100FCase closed, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I don't know how to\x01",
            "thank you guys...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "You found our precious\x01",
            "Mary...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Yes. How can I ever\x01",
            "thank you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "You found my husband\x01",
            "before, and now Mary...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Our family owes all of\x01",
            "you a great debt...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00002FNo, don't say that...\x02\x03",
            "#00000FBesides, this girl here\x01",
            "did even more to find\x01",
            "her than we did.\x02\x03",
            "She calmed down a very\x01",
            "frightened Mary for us,\x01",
            "you see.\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x1, 0xF, 0xB4, 0xC8, 0x3E8, 0x0)
    TurnDirection(0xF, 0x1A3, 500)
    Sleep(300)
    Sound(953, 0, 100, 0)

    ChrTalk(
        0xF,
        "#5PMeow㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5PMary!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PYou're... not saying you\x01",
            "want to be with this\x01",
            "girl, are you?\x02",
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
        "#12PM-Meow?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#12P#04602FAhaha, don't worry.\x02\x03",
            "#04604FMary says she loves\x01",
            "Sunita, you see.\x02\x03",
            "#04609FHearing her speak so\x01",
            "fondly of you, I've no\x01",
            "choice but to give up.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xE,
        "#5PR-Really, Mary?\x02",
    )

    CloseMessageWindow()
    Sound(953, 0, 100, 0)

    ChrTalk(
        0xF,
        "#12PMeow㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#12P#04609FHaha, then it's about\x01",
            "time for me to be going.\x02\x03",
            "#04604FI'm glad I got to play\x01",
            "with you guys and meet\x01",
            "Mary.\x02\x03",
            "#04611F─Guess I showed you my\x01",
            "trump card, though.㈱\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B819():

        label("loc_B819")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_B819")

    QueueWorkItem2(0x101, 2, lambda_B819)
    Sleep(300)

    ChrTalk(
        0x101,
        "#11P#00005FHuh...\x02",
    )

    CloseMessageWindow()

    def lambda_B845():
        OP_97(0xFE, 0xFFFFF8F8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_B845)
    Sleep(50)

    def lambda_B862():

        label("loc_B862")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_B862")

    QueueWorkItem2(0x102, 2, lambda_B862)
    Sleep(50)

    def lambda_B877():

        label("loc_B877")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_B877")

    QueueWorkItem2(0x104, 2, lambda_B877)
    Sleep(50)

    def lambda_B88C():

        label("loc_B88C")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_B88C")

    QueueWorkItem2(0x109, 2, lambda_B88C)
    Sleep(50)

    def lambda_B8A1():

        label("loc_B8A1")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_B8A1")

    QueueWorkItem2(0x105, 2, lambda_B8A1)
    Sleep(50)

    def lambda_B8B6():

        label("loc_B8B6")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_B8B6")

    QueueWorkItem2(0xC, 2, lambda_B8B6)
    Sleep(50)

    def lambda_B8CB():

        label("loc_B8CB")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_B8CB")

    QueueWorkItem2(0xD, 2, lambda_B8CB)
    Sleep(50)

    def lambda_B8E0():

        label("loc_B8E0")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_B8E0")

    QueueWorkItem2(0xE, 2, lambda_B8E0)
    Sleep(50)

    def lambda_B8F5():

        label("loc_B8F5")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_B8F5")

    QueueWorkItem2(0xF, 2, lambda_B8F5)
    WaitChrThread(0x1A3, 1)

    ChrTalk(
        0x104,
        "#00305FH-Hey!\x02",
    )

    CloseMessageWindow()
    OP_93(0x1A3, 0x87, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x1A3,
        (
            "#6P#04602FAhaha, later!\x02\x03",
            "#04609FWe might meet again\x01",
            "soon, though.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B96F():
        OP_97(0xFE, 0xFFFFF448, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_B96F)
    Sleep(300)

    def lambda_B98C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A3, 2, lambda_B98C)
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
        "#00106F...Umm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106FS-She's like a typhoon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FMore like a tornado, I'd\x01",
            "say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FMan, I wish that uncle\x01",
            "of mine 'd teach her\x01",
            "some manners.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FShe did help us a lot\x01",
            "with this request,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hmm. If possible, I'd\x01",
            "like to thank her, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xC, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "─Anyway. I'd like to\x01",
            "thank you all for your\x01",
            "help once again.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BB98():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BB98)
    Sleep(50)

    def lambda_BBA8():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_BBA8)

    def lambda_BBB5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_BBB5)
    Sleep(50)

    def lambda_BBC5():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_BBC5)

    def lambda_BBD2():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_BBD2)
    Sleep(50)

    def lambda_BBE2():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_BBE2)

    def lambda_BBEF():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_BBEF)
    Sleep(50)

    def lambda_BBFF():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_BBFF)
    WaitChrThread(0x105, 2)

    ChrTalk(
        0xD,
        (
            "We will never forget\x01",
            "your kindness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Um, um, let Sunita say\x01",
            "thank you, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Meow㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00009FHaha, you're very\x01",
            "welcome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FPlease let us know if\x01",
            "there's ever anything we\x01",
            "can do for you.\x02",
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
            "Quest [Search for Lost\x01",
            "Kitten]\x07\x00",
            " complete!\x02",
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

    # Function_27_B179 end

    def Function_28_BDD1(): pass

    label("Function_28_BDD1")

    EventBegin(0x1)
    Sound(807, 0, 100, 0)
    Sleep(300)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It's locked. It seems\x01",
            "the resident is already\x01",
            "gone.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 51800, 0, -4500, 0)
    EventEnd(0x4)
    Return()

    # Function_28_BDD1 end

    def Function_29_BE32(): pass

    label("Function_29_BE32")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The door is locked.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_29_BE32 end

    SaveToFile()

Try(main)
