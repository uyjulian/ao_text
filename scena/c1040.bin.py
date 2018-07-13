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
        "Function_9_29D6",         # 09, 9
        "Function_10_2D21",        # 0A, 10
        "Function_11_3F22",        # 0B, 11
        "Function_12_4022",        # 0C, 12
        "Function_13_47B7",        # 0D, 13
        "Function_14_4B67",        # 0E, 14
        "Function_15_5A5D",        # 0F, 15
        "Function_16_5BDC",        # 10, 16
        "Function_17_685F",        # 11, 17
        "Function_18_73B5",        # 12, 18
        "Function_19_800B",        # 13, 19
        "Function_20_82EE",        # 14, 20
        "Function_21_844F",        # 15, 21
        "Function_22_8547",        # 16, 22
        "Function_23_9E87",        # 17, 23
        "Function_24_A991",        # 18, 24
        "Function_25_AB34",        # 19, 25
        "Function_26_ADBB",        # 1A, 26
        "Function_27_B416",        # 1B, 27
        "Function_28_C09E",        # 1C, 28
        "Function_29_C100",        # 1D, 29
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1176")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_FD1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E17")
    Call(0, 9)
    Jump("loc_FCC")

    label("loc_E17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F40")

    ChrTalk(
        0xFE,
        "If my husband were alive...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a guardsman, he would've\x01",
            "chosen to fight until the\x01",
            "end without giving up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Special Support Section, please\x01",
            "take care of Noｱl and Fran.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Feel free to work them as hard as\x01",
            "you like to resolve this situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10109FOh, mom.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_FCC")

    label("loc_F40")


    ChrTalk(
        0xFE,
        (
            "Special Support Section, please\x01",
            "take care of Noｱl and Fran.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Feel free to work them as hard as\x01",
            "you like to resolve this situation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FCC")

    Jump("loc_1171")

    label("loc_FD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10E5")

    ChrTalk(
        0xFE,
        "If my husband were alive...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a guardsman, he would've\x01",
            "chosen to fight until the\x01",
            "end without giving up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Special Support Section, please\x01",
            "take care of Noｱl and Fran.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Feel free to work them as hard as\x01",
            "you like to resolve this situation.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1171")

    label("loc_10E5")


    ChrTalk(
        0xFE,
        (
            "Special Support Section, please\x01",
            "take care of Noｱl and Fran.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Feel free to work them as hard as\x01",
            "you like to resolve this situation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1171")

    Jump("loc_29D2")

    label("loc_1176")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1303")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_127B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11A1")
    Call(0, 9)
    Jump("loc_1276")

    label("loc_11A1")


    ChrTalk(
        0xFE,
        (
            "Azel too came to help,\x01",
            "so we're fine here.\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1276")

    ChrTalk(
        0x109,
        "#10101FBe careful, ok mom?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, you guys\x01",
            "be careful too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_1276")

    Jump("loc_12FE")

    label("loc_127B")


    ChrTalk(
        0xFE,
        (
            "Azel too came to help,\x01",
            "so we're fine here.\x02",
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

    label("loc_12FE")

    Jump("loc_29D2")

    label("loc_1303")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1526")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_142B")

    ChrTalk(
        0xFE,
        (
            "Mr. Dieter... \x01",
            "Until now, probably even he\x01",
            "was not able to accept...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The several unreasonable facts\x01",
            "that happened in Crossbell that\x01",
            "we could only be forced to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "............\x01",
            "...My husband too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Uh uh, I'm sorry.\x01",
            "It's nothing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1521")

    label("loc_142B")


    ChrTalk(
        0xFE,
        (
            "...But even so, the State Guard has\x01",
            "a completely different attitude than\x01",
            "when they called themselves CGF.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Maybe those white uniforms\x01",
            "are a little too neat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But I loved the CGF unifors of the\x01",
            "time when my husband was alive, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1521")

    Jump("loc_29D2")

    label("loc_1526")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_17C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1737")

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
            "That's right, maybe I should\x01",
            "bring her some fruit as well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FMom...\x01",
            "I'm back.\x02\x03",
            "You said you were going to St.\x01",
            "Ursula Hospital this afternoon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes, I just got back\x01",
            "from visiting her..\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...*sigh*, but even so, thank goodness\x01",
            "Fran has regained consciousness.\x02",
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
            "#10103FThat's right...\x01",
            "I have to visit\x01",
            "him too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yes, please do.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_17C0")

    label("loc_1737")


    ChrTalk(
        0xFE,
        (
            "It looks like you're going to the hospital?\x01",
            "I'm planning on going there again later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I need to bring Fran\x01",
            "a change of clothes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17C0")

    Jump("loc_29D2")

    label("loc_17C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1984")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18FE")

    ChrTalk(
        0xFE,
        (
            "To think Mainz is occupied... Including the\x01",
            "appearance of terrorists at the Trade Conference,\x01",
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
            "If you are going there, it would\x01",
            "be best to be extremely cautious.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_197F")

    label("loc_18FE")


    ChrTalk(
        0xFE,
        (
            "That occupation incident\x01",
            "makes me uneasy somehow...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you are going there, it would\x01",
            "be best to be extremely cautious.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_197F")

    Jump("loc_29D2")

    label("loc_1984")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1AB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A43")

    ChrTalk(
        0xFE,
        "Rain again today, eh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Going shopping is a bother,\x01",
            "so suitable leftovers will have\x01",
            "to do for dinner tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F(That's rather\x01",
            "sloppy, mom...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1AAB")

    label("loc_1A43")


    ChrTalk(
        0xFE,
        (
            "Suitable leftovers will have\x01",
            "to do for dinner tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Going out in this\x01",
            "rain is such a pain.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AAB")

    Jump("loc_29D2")

    label("loc_1AB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1B4F")

    ChrTalk(
        0xFE,
        (
            "Hugott was telling me about\x01",
            "his Sunday School homework.\x02",
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
    Jump("loc_29D2")

    label("loc_1B4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1C3E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BD0")

    ChrTalk(
        0xFE,
        (
            "Hugott from next door has\x01",
            "become able to watch the\x01",
            "house himself recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uh uh, how nice.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1C39")

    label("loc_1BD0")


    ChrTalk(
        0xFE,
        (
            "I've been asked by \x01",
            "Sarina to check on\x01",
            "him periodically.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think I'll bring\x01",
            "him a snack later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C39")

    Jump("loc_29D2")

    label("loc_1C3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1DC6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D24")

    ChrTalk(
        0xFE,
        (
            "Sarina next door will be late getting\x01",
            "back from work today, and I was\x01",
            "asked to look after Hugott.\x02",
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
    Jump("loc_1DC1")

    label("loc_1D24")


    ChrTalk(
        0xFE,
        "I love looking after children.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh. Since I don't get chances like\x01",
            "this often, I'll put everything I've got\x01",
            "into making something good for them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DC1")

    Jump("loc_29D2")

    label("loc_1DC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1EEE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E81")

    ChrTalk(
        0xFE,
        (
            "Fran said she's busy\x01",
            "with her operator\x01",
            "work today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all, it is the Trade\x01",
            "Conference's main session.\x02",
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
    Jump("loc_1EE9")

    label("loc_1E81")


    ChrTalk(
        0xFE,
        (
            "Ah... That Fran.\x01",
            "She forgot her\x01",
            "lunchbox again...\x02",
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

    label("loc_1EE9")

    Jump("loc_29D2")

    label("loc_1EEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1EFC")
    Jump("loc_29D2")

    label("loc_1EFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2229")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_218C")

    ChrTalk(
        0xFE,
        (
            "Umm, those expensive cookies\x01",
            "I bought at the department store\x01",
            "should be here somewhere...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FM-Mom?\x01",
            "Could it be...\x02",
        )
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
            "Police will be busy with the\x01",
            "approaching Trade Conference, yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FN-Now look here mom.\x01",
            "She's working, so doing\x01",
            "a thing like that would be...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, Fran will love it,\x01",
            "so I'm sure it's fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ah, that's right. Since I have them, I'll bring\x01",
            "some to the Special Support Section too later...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106FYou don't have to come!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009F(She goes at her own pace...\x01",
            "Fran might have taken\x01",
            "after Mrs. Claris.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    OP_93(0xB, 0x5A, 0x0)
    ClearChrFlags(0xB, 0x10)
    Jump("loc_2224")

    label("loc_218C")


    ChrTalk(
        0xFE,
        (
            "You police are busy with the\x01",
            "approaching trade conference, yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've got to bring\x01",
            "Fran a snack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106F(I wonder if that's all right...)\x02",
    )

    CloseMessageWindow()

    label("loc_2224")

    Jump("loc_29D2")

    label("loc_2229")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_250B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2405")

    ChrTalk(
        0xFE,
        (
            "Come to think of it...\x01",
            "You all got an\x01",
            "orbal car, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if Noｱl's become more annoying.\x01",
            "When it comes to cars, this girl is...\x02",
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
            "not "not true"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FYou were so excited that you\x01",
            "told us all its specs and stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106FWhat! I-Is that so!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309FHu hu. It looks like she\x01",
            "doesn't even remember that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Goodness gracious...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2506")

    label("loc_2405")


    ChrTalk(
        0xFE,
        (
            "This girl can get really annoying\x01",
            "when it comes to orbal cars.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even when she rode a CGF armored \x01",
            "vehicle for the first time, she said the speed\x01",
            "is like that and the endurance is like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FI-I've got it! You can\x01",
            "stop already, mooom!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2506")

    Jump("loc_29D2")

    label("loc_250B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_29D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2842")
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
            "Oh come know. You've always\x01",
            "cared for fine details.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You girls get to work together. Fran\x01",
            "was so happy she was jumping for joy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F*giggle*. I can picture it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F*sigh*, that Fran...\x01",
            "She's always\x01",
            "so childlike.\x02\x03",
            "#10109FW-Well, I'm glad\x01",
            "too, of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHu hu. You sisters\x01",
            "really are close.\x02",
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
            "They are both so attractive,\x01",
            "and yet it seems they'll be trouble\x01",
            "for their future husbands...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106FM-Mom...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F(Ha ha... Not just the sister-sister\x01",
            "relationship, but the mother-\x01",
            "daughter relationship is good too.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12F, 3)
    Jump("loc_29D2")

    label("loc_2842")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_295C")

    ChrTalk(
        0xFE,
        (
            "Noｱl, you should show your face\x01",
            "here every once in awhile.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FHuh? But I've been stopping\x01",
            "by often recently, haven't I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because your workplace is closer to our\x01",
            "house, you should stop by more often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FC'mon, don't spoil\x01",
            "me that much...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_29D2")

    label("loc_295C")


    ChrTalk(
        0xFE,
        (
            "Noｱl, you should show your face\x01",
            "here every once in awhile.\x02",
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

    label("loc_29D2")

    TalkEnd(0xFE)
    Return()

    # Function_8_DE9 end

    def Function_9_29D6(): pass

    label("Function_9_29D6")

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
            "#10102FMom... Thank goodness. \x01",
            "I'm glad you're doing well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "You too. I didn't see you for\x01",
            "awhile and was getting worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "You were working for the State Guard for\x01",
            "awhile and couldn't return, is that it?\x02",
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
            "...Ahaha, well it's fine. I'm sure\x01",
            "you had your own circumstances.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I heard Fran was discharged from the hospial.\x01",
            "Are the girls working together with you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, they're, and they're\x01",
            "doing their very best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Uh uh, if that's the case then\x01",
            "I've no right to say anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Noｱl, proceed on the\x01",
            "path you two like so\x01",
            "to be satisfied with it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "A path such that you will have no\x01",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2D16")
    OP_93(0xB, 0x5A, 0x0)
    Jump("loc_2D1D")

    label("loc_2D16")

    OP_93(0xB, 0x10E, 0x0)

    label("loc_2D1D")

    SetScenarioFlags(0x1BA, 3)
    Return()

    # Function_9_29D6 end

    def Function_10_2D21(): pass

    label("Function_10_2D21")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2E8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DFC")

    ChrTalk(
        0xFE,
        (
            "Azel went to\x01",
            "Downtown today.\x02",
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
            "He is doing his very best to help\x01",
            "his friends, and everyone else, too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2E87")

    label("loc_2DFC")


    ChrTalk(
        0xFE,
        (
            "Azel is already a man, \x01",
            "so I decided to\x01",
            "quit complaining.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He is doing his very best to help\x01",
            "his friends, and everyone else, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E87")

    Jump("loc_3F1E")

    label("loc_2E8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2FBE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F7B")
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Azel hurried back\x01",
            "from Downtown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanks to that, the crying and\x01",
            "scared Hugott finally calmed down...\x02",
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
            "Uh uh, that's right. \x01",
            "You're a brave child, Hugott.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x0, 1)
    Jump("loc_2FB9")

    label("loc_2F7B")


    ChrTalk(
        0xFE,
        (
            "...Anyway, I'm relieved that\x01",
            "Azel is back from Downtown.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FB9")

    Jump("loc_3F1E")

    label("loc_2FBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_315D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30CF")

    ChrTalk(
        0xFE,
        (
            "The "unexplained accidents"\x01",
            "President Dieter spoke of...\x01",
            "I've heard about them myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But to think they were caused by\x01",
            "the two major powers... \x01",
            "That's pretty frightening to be honest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I always thought we\x01",
            "needed to be independent.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3158")

    label("loc_30CF")


    ChrTalk(
        0xFE,
        (
            "When I think Hugott or Azel\x01",
            "might get wrapped up in an\x01",
            ""unexplained accident"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I always thought we\x01",
            "needed to be independent.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3158")

    Jump("loc_3F1E")

    label("loc_315D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_32DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3256")

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
            "Uh uh. I'm proud of him\x01",
            "as his older sister.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_32DA")

    label("loc_3256")


    ChrTalk(
        0xFE,
        (
            "Before he would do anti-social\x01",
            "and mischievous things, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's really changed. As his\x01",
            "older sister, I'm proud of him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32DA")

    Jump("loc_3F1E")

    label("loc_32DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_335D")

    ChrTalk(
        0xFE,
        "An occupation incident, how scary...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I have work today, but maybe I'll\x01",
            "take the day off just in case.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F1E")

    label("loc_335D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_33C8")

    ChrTalk(
        0xFE,
        (
            "Yesterday, a big monster was spotted\x01",
            "near the site of the derailment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "How scary...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F1E")

    label("loc_33C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_33D6")
    Jump("loc_3F1E")

    label("loc_33D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_33E7")
    Call(0, 11)
    Jump("loc_3F1E")

    label("loc_33E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_34C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_348E")

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
    Jump("loc_34BD")

    label("loc_348E")


    ChrTalk(
        0xFE,
        (
            "Ah, oh no...\x01",
            "I've got to go\x01",
            "to work soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34BD")

    Jump("loc_3F1E")

    label("loc_34C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_37A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_372C")

    ChrTalk(
        0xFE,
        (
            "I heard a strange customer came to\x01",
            "the bar where Azel works yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He said he was a man with\x01",
            "blonde hair, a white coat\x01",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 2)), scpexpr(EXPR_END)), "loc_36AB")
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
        "#00006F(He was probably talking about that prince.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F(Probably? I think you mean "definitely.")\x02",
    )

    CloseMessageWindow()
    Jump("loc_3724")

    label("loc_36AB")


    ChrTalk(
        0x101,
        (
            "#00005F(Blond hair and a lute... I feel like\x01",
            "we've seen someone like that recently?)\x02\x03",
            "#00004F(...N-No, impossible.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3724")

    SetScenarioFlags(0x0, 1)
    Jump("loc_37A3")

    label("loc_372C")


    ChrTalk(
        0xFE,
        (
            "Normally, Azel doesn't\x01",
            "say anything about his\x01",
            "work at home...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That customer\x01",
            "must have been\x01",
            "quite the weirdo.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37A3")

    Jump("loc_3F1E")

    label("loc_37A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3904")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3880")

    ChrTalk(
        0xFE,
        (
            "Today, it seems that Mrs.\x01",
            "Claris from next door is away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Mrs. Claris always look\x01",
            "after Hugott for me and\x01",
            "I really owe her a lot...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Next time, I've got to thank her properly.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_38FF")

    label("loc_3880")


    ChrTalk(
        0xFE,
        (
            "Mrs. Claris always look\x01",
            "after Hugott for me and\x01",
            "I really owe her a lot...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Next time, I've got to thank her properly.\x02",
    )

    CloseMessageWindow()

    label("loc_38FF")

    Jump("loc_3F1E")

    label("loc_3904")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3A31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39DB")

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
    SetScenarioFlags(0x0, 1)
    Jump("loc_3A2C")

    label("loc_39DB")


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

    label("loc_3A2C")

    Jump("loc_3F1E")

    label("loc_3A31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3B39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AD4")

    ChrTalk(
        0xFE,
        (
            "I have the day off today, so I'm\x01",
            "spending it with my little brother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, hmm...\x01",
            "As expected, "playing\x01",
            "Bracer" is a little...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3B34")

    label("loc_3AD4")


    ChrTalk(
        0xFE,
        (
            ""Playing Bracer"? \x01",
            "What am I supposed to do...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Azel's never here\x01",
            "in times like this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B34")

    Jump("loc_3F1E")

    label("loc_3B39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3F1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DE0")
    TurnDirection(0xFE, 0x105, 0)

    ChrTalk(
        0xFE,
        "My, you are...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FOh, if I'm remember it right,\x01",
            "you're... Azel's older sister.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FUmm... \x01",
            "Do you know her?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHu hu. Her younger brother\x01",
            "Azel is a Testaments member.\x02\x03",
            "#10300FDidn't you, quite a while ago,\x01",
            "stormed into "Trinity" to\x01",
            "make him quit...?\x02",
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
            "Umm, I'm sorry to have\x01",
            "caused you trouble back then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At that time, I wanted Azel\x01",
            "to leave the gang no\x01",
            "matter what...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FI think all the\x01",
            "Testaments were surprised\x01",
            "at your menacing attitude.\x02\x03",
            "#10309FHu hu, that was none other\x01",
            "than a brother-sister bond.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F(W-Why does he act like it's not his problem...?)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12F, 4)
    Jump("loc_3F1E")

    label("loc_3DE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EB0")

    ChrTalk(
        0xFE,
        (
            "My younger brother Azel \x01",
            "works part time at "Trinity".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's a bad part of town, so I\x01",
            "was scared at first, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was a little relieved since\x01",
            "he has been keeping up with it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3F1E")

    label("loc_3EB0")


    ChrTalk(
        0xFE,
        (
            "*sigh*, that Azel...\x01",
            "He hardly ever tells\x01",
            "me about his gang.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wish he wouldn't\x01",
            "worry me so much...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F1E")

    TalkEnd(0xFE)
    Return()

    # Function_10_2D21 end

    def Function_11_3F22(): pass

    label("Function_11_3F22")

    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FAA")

    ChrTalk(
        0x9,
        (
            "Alright, big sis is\x01",
            "heading to work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Be sure to lock\x01",
            "the door, Hugott.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Yeah, leave it to meee.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4019")

    label("loc_3FAA")


    ChrTalk(
        0x9,
        (
            "Oh, right, do your homework\x01",
            "properly, even if your\x01",
            "sister isn't watching you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "I know that alreadyyy.\x02",
    )

    CloseMessageWindow()

    label("loc_4019")

    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_11_3F22 end

    def Function_12_4022(): pass

    label("Function_12_4022")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_420B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_417C")

    ChrTalk(
        0xFE,
        (
            "I was really scared when I saw that\x01",
            "azure pale tree appear outside, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My brother said that he'd have done something\x01",
            "about it and everything would've been alright...\x01",
            "And that cheered me up,\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even though he's my big brother,\x01",
            "I think he can't do that much, but... \x01",
            "Ehehe, that cheered me up somehow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4206")

    label("loc_417C")


    ChrTalk(
        0xFE,
        (
            "I was scared seeing the azure pale\x01",
            "tree, but my brother cheered me up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ehehe, my brother's\x01",
            "so cool. I cheered\x01",
            "up thanks to him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4206")

    Jump("loc_47B3")

    label("loc_420B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4257")

    ChrTalk(
        0xFE,
        (
            "Because my brother is here,\x01",
            "I'm sure it'll be all right.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47B3")

    label("loc_4257")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_42E3")

    ChrTalk(
        0xFE,
        (
            "Crossbell in-de-pen-dence...\x01",
            "In the end, what does that mean?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't get it. I'm sure\x01",
            "Teacher Marble would know...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47B3")

    label("loc_42E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_435C")

    ChrTalk(
        0xFE,
        (
            "I wonder if there's anything\x01",
            "I too can do to help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Should I head over to\x01",
            "my brother in Downtown?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47B3")

    label("loc_435C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_43D8")

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
            "Azel is going to be back...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47B3")

    label("loc_43D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_444E")

    ChrTalk(
        0xFE,
        (
            "Yesterday, a train\x01",
            "fell over, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How scary... Why did\x01",
            "something like that\x01",
            "have to happen?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47B3")

    label("loc_444E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_455E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_450B")
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xFE,
        "*haah*, I hate homework.\x02",
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
            "Auntie has a reward snack\x01",
            "ready for you, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Really!? Alright,\x01",
            "I'll do my best!\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x0, 2)
    Jump("loc_4559")

    label("loc_450B")


    ChrTalk(
        0xFE,
        "Umm, 14 times 23 is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, two-column\x01",
            "multiplication sure is hard.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4559")

    Jump("loc_47B3")

    label("loc_455E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_456F")
    Call(0, 11)
    Jump("loc_47B3")

    label("loc_456F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_457D")
    Jump("loc_47B3")

    label("loc_457D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_45FD")

    ChrTalk(
        0xFE,
        (
            "Lately, my brother has been coming\x01",
            "back once every three days.\x02",
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
    Jump("loc_47B3")

    label("loc_45FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_469A")

    ChrTalk(
        0xFE,
        (
            "Auntie Claris said she was\x01",
            "going to the cathedral today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Come to think of it, I feel like she\x01",
            "went there on the same day last month.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47B3")

    label("loc_469A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_46A8")
    Jump("loc_47B3")

    label("loc_46A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4742")

    ChrTalk(
        0xFE,
        (
            "My sister says she doesn't know\x01",
            "how "playing Bracer" is done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Aw, can't be helped I guess. \x01",
            "I wonder if playing house will be ok.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47B3")

    label("loc_4742")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_47B3")

    ChrTalk(
        0xFE,
        (
            "Azel is working\x01",
            "as a bartender\x01",
            "in Downtown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ehehe, he's so cool.\x01",
            "I'm proud of my big brother.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47B3")

    TalkEnd(0xFE)
    Return()

    # Function_12_4022 end

    def Function_13_47B7(): pass

    label("Function_13_47B7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BA, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_49E5")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x105, 500)

    ChrTalk(
        0xFE,
        (
            "Huh... W-Wazy!?\x01",
            "You're back in Crossbell!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10400FHu hu, it's been awhile, Azel.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What're those clothes and...\x01",
            "And where is Abbas!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404FThere's an explanation for\x01",
            "all of this, but I don't\x01",
            "have time for it right now.\x02\x03",
            "#10400FI'll explain it carefully to you later.\x01",
            "For now, be sure to protect your\x01",
            "older sister and little brother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "S-Sure... I get\x01",
            "that it's not time\x01",
            "for that right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "But Wazy, thank goodness you're safe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10402FHu hu, you too.\x01",
            "...Later, then.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BA, 4)
    Jump("loc_4B63")

    label("loc_49E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AC1")

    ChrTalk(
        0xFE,
        (
            "The monsters wandering around outside\x01",
            "seem to show no sign of entering homes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...But, we mustn't be careless.\x01",
            "We've got to keep on guard...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll definitely protect\x01",
            "my sister and brother!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4B63")

    label("loc_4AC1")


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
            "my sister and brother!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B63")

    TalkEnd(0xFE)
    Return()

    # Function_13_47B7 end

    def Function_14_4B67(): pass

    label("Function_14_4B67")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4B78")
    Jump("loc_5A59")

    label("loc_4B78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4B86")
    Jump("loc_5A59")

    label("loc_4B86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4DD0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C77")

    ChrTalk(
        0xFE,
        (
            "I decided to leave\x01",
            "from Crossbell today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I packed in a hurry and...\x01",
            "This book is too bulky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "If you like, I'll give it to you.\x02",
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
    Jump("loc_4DCB")

    label("loc_4C77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D45")

    ChrTalk(
        0xFE,
        (
            "I received an evacuation order\x01",
            "from the Imperial government.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm planning on leaving\x01",
            "Crossbell via train today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It looks like the station's\x01",
            "congested, so I've got to hurry.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4DCB")

    label("loc_4D45")


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

    label("loc_4DCB")

    Jump("loc_5A59")

    label("loc_4DD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4F2B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EC5")

    ChrTalk(
        0xFE,
        (
            "My family in the Empire was worried\x01",
            "about me and sent a letter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Such an incident happened,\x01",
            "so I'd like to return to my\x01",
            "home country soon as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if I should consult\x01",
            "the main office about this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4F26")

    label("loc_4EC5")


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

    label("loc_4F26")

    Jump("loc_5A59")

    label("loc_4F2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4FED")

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
            "Anyway, all I can do is pray to the Goddess\x01",
            "that the situation's resolved quickly...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A59")

    label("loc_4FED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5156")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50C0")

    ChrTalk(
        0xFE,
        (
            "My wife and daughter who came to\x01",
            "visit returned to the Empire today.\x02",
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
    Jump("loc_5151")

    label("loc_50C0")


    ChrTalk(
        0xFE,
        (
            "But even so... It's been awhile\x01",
            "since I was able to spend time\x01",
            "with my wife and daughter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ha ha, I might be getting\x01",
            "a little homesick.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5151")

    Jump("loc_5A59")

    label("loc_5156")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5164")
    Jump("loc_5A59")

    label("loc_5164")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_51EA")

    ChrTalk(
        0xFE,
        (
            "I see...\x01",
            "You're already going back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll still be lonely awhile longer...\x01",
            "Please, take care of our daughter.\x01\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A59")

    label("loc_51EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5355")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52B8")

    ChrTalk(
        0xFE,
        (
            "My wife and daughter came to visit from\x01",
            "her parents' home in the Empire...\x02",
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
    Jump("loc_5350")

    label("loc_52B8")


    ChrTalk(
        0xFE,
        (
            "Wow, with yesterday's train then... \x01",
            "It would've been better if you contacted me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm sorry I haven't been able\x01",
            "to spend time with my family.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5350")

    Jump("loc_5A59")

    label("loc_5355")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_53F6")

    ChrTalk(
        0xFE,
        (
            "The Trade Conference developments\x01",
            "will likely influence stock prices...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a securities man, those movements\x01",
            "are something I can't miss.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A59")

    label("loc_53F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5629")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54A3")

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
            "I too helped look for it, but in\x01",
            "the end we didn't find it...\x01",
            "I wonder what happened?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5624")

    label("loc_54A3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5543")

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
            "His daughter can't stop\x01",
            "crying. Poor thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please find\x01",
            "it somehow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_55B0")

    label("loc_5543")


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
        (
            "Please find\x01",
            "it somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55B0")

    Jump("loc_5624")

    label("loc_55B5")


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
            "It seems the cat\x01",
            "was found somehow.\x01",
            "Thank goodness.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5624")

    Jump("loc_5A59")

    label("loc_5629")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_57AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5713")

    ChrTalk(
        0xFE,
        (
            "Mr. Bond's family next\x01",
            "door originally lived in\x01",
            "Residential Street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But some things happened,\x01",
            "and they moved here.\x02",
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
    Jump("loc_57A8")

    label("loc_5713")


    ChrTalk(
        0xFE,
        (
            "The family next door\x01",
            "moved from Residential\x01",
            "Street to here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Some things happened, but... I want to\x01",
            "follow the example of their brightness.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57A8")

    Jump("loc_5A59")

    label("loc_57AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5914")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_589F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57D2")
    Call(0, 15)
    Jump("loc_589A")

    label("loc_57D2")

    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xC,
        (
            "Thank you for\x01",
            "your concern.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "We may cause you some bothers,\x01",
            "but it's nice to make your acquaintance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No, no, I should say the same.\x01",
            "Please let me know if\x01",
            "you ever need anything.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)

    label("loc_589A")

    Jump("loc_590F")

    label("loc_589F")


    ChrTalk(
        0xFE,
        (
            "It seems Mr. Bond is a\x01",
            "securities man, the same as I.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, he might be a good\x01",
            "conversation partner.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_590F")

    Jump("loc_5A59")

    label("loc_5914")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5A59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59E6")

    ChrTalk(
        0xFE,
        (
            "Those Bracer kids lived\x01",
            "next door, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's been lonely ever since they returned\x01",
            "to their home country a few months ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if\x01",
            "anyone new will\x01",
            "move in soon...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_5A59")

    label("loc_59E6")


    ChrTalk(
        0xFE,
        (
            "It must've been a job transfer,\x01",
            "but even so, I feel lonely.\x02",
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

    label("loc_5A59")

    TalkEnd(0xFE)
    Return()

    # Function_14_4B67 end

    def Function_15_5A5D(): pass

    label("Function_15_5A5D")

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
            "I think we may cause you \x01",
            "some bothers, but it's nice \x01",
            "to make your acquaintance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Nice to meet you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Come on. Say hello too, Mary.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Nya～n.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Uh uh, I'm glad you all seem\x01",
            "to be getting along very well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you ever need anything,\x01",
            "don't hesitate to ask.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Yes, thank you very much.\x02",
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

    # Function_15_5A5D end

    def Function_16_5BDC(): pass

    label("Function_16_5BDC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C05")
    Call(0, 22)
    Return()

    label("loc_5C05")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C39")
    Call(0, 23)
    Return()

    label("loc_5C39")

    Call(0, 25)
    Return()

    label("loc_5C3D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5DCA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D36")

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
            "I've been away from work for awhile,\x01",
            "so I'll need to properly prepare.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I want to do my best for\x01",
            "the three of us and our cat.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5DC5")

    label("loc_5D36")


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
            "the three of us and our cat.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DC5")

    Jump("loc_685B")

    label("loc_5DCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5E69")

    ChrTalk(
        0xFE,
        (
            "Anyway, martial law has been handed down,\x01",
            "so I think it's best if we stay home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's all right. This situation\x01",
            "can't go on too long...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_685B")

    label("loc_5E69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5FF4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F5E")

    ChrTalk(
        0xFE,
        (
            "That declaration must have strongly\x01",
            "provoked the Empire and Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's possible that Crossbell will\x01",
            "fall into a dangerous situation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But no matter what happens, \x01",
            "I'll definitely protect my family.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5FEF")

    label("loc_5F5E")


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
            "my family... \x01",
            "No matter what happens.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FEF")

    Jump("loc_685B")

    label("loc_5FF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_61B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6115")

    ChrTalk(
        0xFE,
        (
            "The company I work for had\x01",
            "moved into the IBC building, but...\x02",
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
            "No one was hurt, so\x01",
            "it's only a matter of\x01",
            "time until we reopen...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "*sigh*, how troubling.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_61AF")

    label("loc_6115")


    ChrTalk(
        0xFE,
        (
            "The attackers destroyed the IBC\x01",
            "building and my business is closed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Although the area around\x01",
            "here wasn't attacked. \x01",
            "I suppose that's good...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_61AF")

    Jump("loc_685B")

    label("loc_61B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6220")

    ChrTalk(
        0xFE,
        (
            "But, this has become\x01",
            "a big problem.\x02",
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
    Jump("loc_685B")

    label("loc_6220")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_62B3")

    ChrTalk(
        0xFE,
        (
            "It's been awhile since\x01",
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

    label("loc_62B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_62C1")
    Jump("loc_685B")

    label("loc_62C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_62CF")
    Jump("loc_685B")

    label("loc_62CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_62DD")
    Jump("loc_685B")

    label("loc_62DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6464")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63BC")

    ChrTalk(
        0xFE,
        (
            "Mr. Marcy's field is \x01",
            "quite similar to mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For time to time, \x01",
            "I try to predict stock\x01",
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
    Jump("loc_645F")

    label("loc_63BC")


    ChrTalk(
        0xFE,
        (
            "Now then... I've got\x01",
            "to get to work soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm interested in the Trade Conference,\x01",
            "but... I have no choice but to wait for\x01",
            "news from the Crossbell Times.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_645F")

    Jump("loc_685B")

    label("loc_6464")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_659E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6540")

    ChrTalk(
        0xFE,
        (
            "Well, I'm really\x01",
            "glad all of you\x01",
            "are helping out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For now, I plan to\x01",
            "head to Central Square\x01",
            "to continue my search.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If anything happens,\x01",
            "please contact me anytime.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6599")

    label("loc_6540")


    ChrTalk(
        0xFE,
        "Really, thanks for your help today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'll never forget what you've done for us.\x02",
    )

    CloseMessageWindow()

    label("loc_6599")

    Jump("loc_685B")

    label("loc_659E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_66FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6680")

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
            "I've begun commuting\x01",
            "to IBC, the same as\x01",
            "our other employees.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've settled in after\x01",
            "moving, and started\x01",
            "work in earnest.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_66F5")

    label("loc_6680")


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
            "I'm always happy when\x01",
            "I say "I'm home" after\x01",
            "a long day of work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66F5")

    Jump("loc_685B")

    label("loc_66FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_6852")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_671F")
    Call(0, 15)
    Jump("loc_67E7")

    label("loc_671F")

    OP_4B(0x8, 0xFF)

    ChrTalk(
        0xC,
        (
            "Thank you for\x01",
            "your concern.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "We may cause you some bothers,\x01",
            "but it's nice to make your acquaintance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "No, no, I should say the same.\x01",
            "Please let me know if\x01",
            "you ever need anything.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)

    label("loc_67E7")

    Jump("loc_684D")

    label("loc_67EC")


    ChrTalk(
        0xFE,
        "I'm a very happy man.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "This is thanks to my whole family...\x01",
            "I'll treasure them forever.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_684D")

    Jump("loc_685B")

    label("loc_6852")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_685B")

    label("loc_685B")

    TalkEnd(0xFE)
    Return()

    # Function_16_5BDC end

    def Function_17_685F(): pass

    label("Function_17_685F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_688D")
    Call(0, 22)
    Return()

    label("loc_688D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_68C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68C1")
    Call(0, 23)
    Return()

    label("loc_68C1")

    Call(0, 25)
    Return()

    label("loc_68C5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6977")

    ChrTalk(
        0xFE,
        (
            "I'm relieved Mrs. Sophia and\x01",
            "Miss Cindy's families in \x01",
            "Residential Street are all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For now anyway, I want to get\x01",
            "back my carefree everyday life.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73B1")

    label("loc_6977")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6A15")

    ChrTalk(
        0xFE,
        (
            "I'm worried about my neighbors from when\x01",
            "I lived in Residential Street too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder if Mrs. Sophia and\x01",
            "Miss Cindy are all right...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73B1")

    label("loc_6A15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_6AB5")

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
            "happy, that's enough for me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73B1")

    label("loc_6AB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_6BD2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B6D")

    ChrTalk(
        0xFE,
        (
            "I...\x01",
            "Saw it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The giant monster that\x01",
            "rampaged through Downtown...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Aah, how terrifying...\x01",
            "Since when did Crossbell\x01",
            "become such a scary place...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6BCD")

    label("loc_6B6D")


    ChrTalk(
        0xFE,
        (
            "When I think that giant\x01",
            "monster might appear again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ooh, I just can't stop shaking.\x02",
    )

    CloseMessageWindow()

    label("loc_6BCD")

    Jump("loc_73B1")

    label("loc_6BD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_6C43")

    ChrTalk(
        0xFE,
        (
            "I just can't stand\x01",
            "the smell of blood...\x02",
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
    Jump("loc_73B1")

    label("loc_6C43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_6D47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CDB")

    ChrTalk(
        0xFE,
        (
            "*shaa*......\x01",
            "Watering plants\x01",
            "heals the heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The sound of the rain is relaxing too.\x01",
            "This is a nice day to be off.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6D42")

    label("loc_6CDB")


    ChrTalk(
        0xFE,
        (
            "*shaa*... I think\x01",
            "I'll have tea time\x01",
            "in a little while.\x02",
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

    label("loc_6D42")

    Jump("loc_73B1")

    label("loc_6D47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_6DE8")

    ChrTalk(
        0xFE,
        (
            "I've got to go shopping later. \x01",
            "I wonder if Mrs. Marte's\x01",
            "holding a sale today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, I'm already friends\x01",
            "with everyone at the market.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73B1")

    label("loc_6DE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6F5C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EDE")

    ChrTalk(
        0xFE,
        (
            "It seems there's an important conference\x01",
            "today, and my husband left early.\x02",
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
            "My husband loves his family...\x01",
            "Uh uh, that's a good thing.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_6F57")

    label("loc_6EDE")


    ChrTalk(
        0xFE,
        (
            "When my husband moved here, it seems he\x01",
            "was suddenly motivated with his work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uh uh, that's a very good thing.\x02",
    )

    CloseMessageWindow()

    label("loc_6F57")

    Jump("loc_73B1")

    label("loc_6F5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6F6A")
    Jump("loc_73B1")

    label("loc_6F6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_70B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_702D")

    ChrTalk(
        0xFE,
        (
            "The man next door shares some\x01",
            "of his profits with everyone here.\x01",
            "He's a very nice man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But somehow,\x01",
            "he seems lonely...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Job transfers must\x01",
            "be lonely too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_70AE")

    label("loc_702D")


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

    label("loc_70AE")

    Jump("loc_73B1")

    label("loc_70B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_719F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7142")

    ChrTalk(
        0xFE,
        (
            "Everyone, please\x01",
            "take care of Mary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I am sure that little one really\x01",
            "wants to return home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_719A")

    label("loc_7142")


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
            "But, Mary seemed\x01",
            "happy with it too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_719A")

    Jump("loc_73B1")

    label("loc_719F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_72C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7244")

    ChrTalk(
        0xFE,
        (
            "Our kitchen is a\x01",
            "little small, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It looks like I can use the flowerpot\x01",
            "outside for my gardening hobby. \x01",
            "I like it somehow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_72C3")

    label("loc_7244")


    ChrTalk(
        0xFE,
        (
            "I think it's only a matter\x01",
            "of time before Sunita\x01",
            "gets used to it, but...\x02",
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

    label("loc_72C3")

    Jump("loc_73B1")

    label("loc_72C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_73A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7328")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72ED")
    Call(0, 15)
    Jump("loc_7323")

    label("loc_72ED")


    ChrTalk(
        0xFE,
        (
            "Uhuhu. Thank\x01",
            "goodness the man\x01",
            "next door is nice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7323")

    Jump("loc_73A3")

    label("loc_7328")


    ChrTalk(
        0xFE,
        (
            "From now on, we'll\x01",
            "get through anything\x01",
            "together as a family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uhuhu, this reminds me of\x01",
            "when we were newlyweds㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_73A3")

    Jump("loc_73B1")

    label("loc_73A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_73B1")

    label("loc_73B1")

    TalkEnd(0xFE)
    Return()

    # Function_17_685F end

    def Function_18_73B5(): pass

    label("Function_18_73B5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_73ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x155, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_73E9")
    Call(0, 23)
    Return()

    label("loc_73E9")

    Call(0, 25)
    Return()

    label("loc_73ED")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_74D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_747F")

    ChrTalk(
        0xFE,
        (
            "Father looks happy\x01",
            "to be working again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, Sunita is happy too.\x01",
            "What do you think, Mary?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Nya～n?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_74D2")

    label("loc_747F")


    ChrTalk(
        0xFE,
        (
            "Father looks happy\x01",
            "to be working again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, Sunita\x01",
            "is very happy too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_74D2")

    Jump("loc_8007")

    label("loc_74D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_7531")

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
    Jump("loc_8007")

    label("loc_7531")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_7593")

    ChrTalk(
        0xFE,
        (
            "It seems our neighbor\x01",
            "is going to leave\x01",
            "Crossbell today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I'll miss him...\x02",
    )

    CloseMessageWindow()
    Jump("loc_8007")

    label("loc_7593")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_7614")

    ChrTalk(
        0xFE,
        (
            "I might visit\x01",
            "the charity\x01",
            "event with Mary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The rumors say they're gathering\x01",
            "a lot of pretty girls there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8007")

    label("loc_7614")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_770F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_769E")

    ChrTalk(
        0xFE,
        (
            "I was told not\x01",
            "to go anywhere\x01",
            "far away today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It can't be helped. I'll stay\x01",
            "here and play with Mary.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_770A")

    label("loc_769E")


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

    label("loc_770A")

    Jump("loc_8007")

    label("loc_770F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_7795")

    ChrTalk(
        0xFE,
        (
            "Mary washed her\x01",
            "face yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            ""When cats wash their faces,\x01",
            "it'll rain." It's really true.\x01",
            "Sunita's shocked!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8007")

    label("loc_7795")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_78B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7869")

    ChrTalk(
        0xFE,
        (
            "Mary seems to be\x01",
            "licking her face\x01",
            "really hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            ""When cats wash their faces,\x01",
            "it'll rain." The old street\x01",
            "vendor lady told me that, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...Is it going to rain tomorrow?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_78B2")

    label("loc_7869")


    ChrTalk(
        0xFE,
        (
            "If Mary's washing\x01",
            "her face...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...Is it going to rain tomorrow?\x02",
    )

    CloseMessageWindow()

    label("loc_78B2")

    Jump("loc_8007")

    label("loc_78B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_79CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_795B")
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xFE,
        (
            "I'm playing with\x01",
            "Mary today.\x02",
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
            "Wow.. \x01",
            "This really works!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    OP_4C(0xF, 0xFF)
    ClearChrFlags(0xE, 0x10)
    Jump("loc_79C8")

    label("loc_795B")


    ChrTalk(
        0xFE,
        (
            "It's "Green Foxtail"\x01",
            "that the street vendor\x01",
            "man told me about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Uh uh, it looks like\x01",
            "Mary likes it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_79C8")

    Jump("loc_8007")

    label("loc_79CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_79DB")
    Jump("loc_8007")

    label("loc_79DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7B04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A76")

    ChrTalk(
        0xFE,
        (
            "That's father's bed.\x01",
            "And this one is mother\x01",
            "and Sunita's bed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Mary, did you understand?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Nyaon...[I'm tired]\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    ClearChrFlags(0xE, 0x10)
    Jump("loc_7AFF")

    label("loc_7A76")


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
            "I'm sure it'll be all right\x01",
            "if I just keep it up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7AFF")

    Jump("loc_8007")

    label("loc_7B04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_7D64")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7C75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C18")
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xE,
        (
            "Ooh, Mary...\x01",
            "I'm sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I... It's because I did\x01",
            "something I shouldn't have...\x02",
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
        "#00100F(...We've got to find her quickly.)\x02",
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
    Jump("loc_7C70")

    label("loc_7C18")


    ChrTalk(
        0xFE,
        (
            "Ooh, Mary...\x01",
            "I'm sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I... It's because I did\x01",
            "something I shouldn't have...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C70")

    Jump("loc_7D5F")

    label("loc_7C75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D10")
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xE,
        "Thank goodness you're all right, Mary...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "*sigh*... As punishment, I'm\x01",
            "going to hold you aaall day long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "N-Nya～n?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    OP_4C(0xF, 0xFF)
    Jump("loc_7D5F")

    label("loc_7D10")

    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xE,
        (
            "Come now, Mary.\x01",
            "Prepare yourself.\x02",
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

    label("loc_7D5F")

    Jump("loc_8007")

    label("loc_7D64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7E8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E29")

    ChrTalk(
        0xFE,
        (
            "Sunita likes\x01",
            "this new home\x01",
            "quite a lot.\x02",
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
            "because we moved\x01",
            "here so suddenly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_7E88")

    label("loc_7E29")


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
            "because we moved\x01",
            "here so suddenly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E88")

    Jump("loc_8007")

    label("loc_7E8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_7FFE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F30")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7EB2")
    Call(0, 15)
    Jump("loc_7F2B")

    label("loc_7EB2")


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
            "Thanks to that, I'm\x01",
            "not embarrassed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F2B")

    Jump("loc_7FF9")

    label("loc_7F30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F8D")

    ChrTalk(
        0xFE,
        (
            "Uh uh, you're really\x01",
            "well-behaved, Mary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As a reward,\x01",
            "I'll pet you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7FF9")

    label("loc_7F8D")


    ChrTalk(
        0xFE,
        (
            "My father and mother get along \x01",
            "way better than they did before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Sunita is very\x01",
            "happy about that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7FF9")

    Jump("loc_8007")

    label("loc_7FFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_8007")

    label("loc_8007")

    TalkEnd(0xFE)
    Return()

    # Function_18_73B5 end

    def Function_19_800B(): pass

    label("Function_19_800B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8038")

    ChrTalk(
        0xFE,
        "...Nyaon...[I'm tired]\x02",
    )

    CloseMessageWindow()
    Jump("loc_82EA")

    label("loc_8038")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_8060")

    ChrTalk(
        0xFE,
        "Nyao?[What's wrong?]\x02",
    )

    CloseMessageWindow()
    Jump("loc_82EA")

    label("loc_8060")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_807B")

    ChrTalk(
        0xFE,
        "Nyaa...\x02",
    )

    CloseMessageWindow()
    Jump("loc_82EA")

    label("loc_807B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_8095")

    ChrTalk(
        0xFE,
        "Myaon.\x02",
    )

    CloseMessageWindow()
    Jump("loc_82EA")

    label("loc_8095")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_80B2")

    ChrTalk(
        0xFE,
        "Funyaawn.\x02",
    )

    CloseMessageWindow()
    Jump("loc_82EA")

    label("loc_80B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_80CE")

    ChrTalk(
        0xFE,
        "Nyaan...\x02",
    )

    CloseMessageWindow()
    Jump("loc_82EA")

    label("loc_80CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_8104")
    TurnDirection(0xF, 0xE, 500)
    Sleep(500)

    ChrTalk(
        0xFE,
        (
            "Nyanya...\x01",
            "(*lick, lick*)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_82EA")

    label("loc_8104")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_8122")

    ChrTalk(
        0xFE,
        "Fumyawn...\x02",
    )

    CloseMessageWindow()
    Jump("loc_82EA")

    label("loc_8122")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_8130")
    Jump("loc_82EA")

    label("loc_8130")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_8172")

    ChrTalk(
        0xFE,
        "Nyaago.[It's been a while. How have you been?]\x02",
    )

    CloseMessageWindow()
    Jump("loc_82EA")

    label("loc_8172")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_826A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8216")
    OP_4B(0xE, 0xFF)

    ChrTalk(
        0xE,
        "Thank goodness you're all right, Mary...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "*sigh*... As punishment, I'm\x01",
            "going to hold you aaall day long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "N-Nya～n?\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    OP_4C(0xE, 0xFF)
    Jump("loc_8265")

    label("loc_8216")

    OP_4B(0xE, 0xFF)

    ChrTalk(
        0xE,
        (
            "Come now, Mary.\x01",
            "Prepare yourself.\x02",
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

    label("loc_8265")

    Jump("loc_82EA")

    label("loc_826A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_8285")

    ChrTalk(
        0xFE,
        "Nyaa...\x02",
    )

    CloseMessageWindow()
    Jump("loc_82EA")

    label("loc_8285")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_82E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_82AA")

    ChrTalk(
        0xFE,
        "Nya～n.\x02",
    )

    CloseMessageWindow()
    Jump("loc_82DC")

    label("loc_82AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_82CC")

    ChrTalk(
        0xFE,
        "purr nya～n㈱\x02",
    )

    CloseMessageWindow()
    Jump("loc_82DC")

    label("loc_82CC")


    ChrTalk(
        0xFE,
        "Nyannyan♪\x02",
    )

    CloseMessageWindow()

    label("loc_82DC")

    Jump("loc_82EA")

    label("loc_82E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_82EA")

    label("loc_82EA")

    TalkEnd(0xFE)
    Return()

    # Function_19_800B end

    def Function_20_82EE(): pass

    label("Function_20_82EE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_8398")
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0xFE,
        (
            "We won't be interfering\x01",
            "with your work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Dear, watch out for your health\x01",
            "until your work is finished, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Yeah... I'll be careful.\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    Jump("loc_844B")

    label("loc_8398")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_844B")
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Even so, dear,\x01",
            "haven't you lost weight?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since you're living alone,\x01",
            "that's no excuse to not\x01",
            "eat properly, alright?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Ha ha... Don't be so hard on me.\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)

    label("loc_844B")

    TalkEnd(0xFE)
    Return()

    # Function_20_82EE end

    def Function_21_844F(): pass

    label("Function_21_844F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_84BC")

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
        "I want to come visit papa again...\x02",
    )

    CloseMessageWindow()
    Jump("loc_8543")

    label("loc_84BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_8543")

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
        "You were a little out of focus, though.\x02",
    )

    CloseMessageWindow()

    label("loc_8543")

    TalkEnd(0xFE)
    Return()

    # Function_21_844F end

    def Function_22_8547(): pass

    label("Function_22_8547")

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
        "Oh, we have guests.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Oh, it's you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FWe're with the Crossbell Police,\x01",
            "Special Support Section.\x02\x03",
            "You're Mr. Bond, correct?\x01",
            "I think you got tied up in\x01",
            "the incident with that Cult...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_877F")
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
            "#1KWhat about the "Search for a lost cat" in Zero? (Debug)\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[No change]\x01",         # 0
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_876B")
    OP_29(0x8, 0x4, 0x10)
    Jump("loc_877F")

    label("loc_876B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_877F")
    OP_29(0x8, 0x3, 0x10)

    label("loc_877F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_88B1")

    ChrTalk(
        0xC,
        "Yeah, how could I forget.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "You are none other than the team\x01",
            "that freed us from the prison\x01",
            "within that abysmal "fort".\x02",
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
            "to at least express my gratitude. \x01",
            "Thank you so much.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8989")

    label("loc_88B1")


    ChrTalk(
        0xC,
        "Yeah, how could I forget.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "You are none other than the team\x01",
            "that freed us from the prison\x01",
            "within that abysmal "fort".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I always wanted to find a way\x01",
            "to at least express my gratitude. \x01",
            "Thank you so much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8989")


    ChrTalk(
        0xD,
        (
            "Please allow me to express\x01",
            "my sincere thanks as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Thank goodness you were there for\x01",
            "my husband when he was trapped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00004FOh no, please don't worry about it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FBut we are glad to see\x01",
            "you all doing well now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Ha ha, only because of all of you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "But is there something\x01",
            "we can help with today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYes, actually....\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Explained the investigation to Bond and\x01",
            "asked the details about their move.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xC,
        (
            "I see, suspicious residence\x01",
            "change notices, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "So you want to hear the details\x01",
            "of how I sold the house?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103FYes, sorry to pry, but we\x01",
            "need to confirm that\x01",
            "nothing illegal occurred.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "No, you aren't prying at all. \x01",
            "I understand where you're coming from.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well, the sad truth of the\x01",
            "matter is that we had to sell\x01",
            "off the house to repay debts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "The purchaser ended up being the same real\x01",
            "estate agency and all of the processes \x01",
            "were followed correctly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "So I guess you could say that there's absolutely\x01",
            "nothing illegal about this situation at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005FI understand...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103FUm, please don't feel that you have to\x01",
            "answer if you'd prefer not to, but...\x02\x03",
            "#00101FWould you mind discussing the cause\x01",
            "of the debt in the first place?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "No, it's not a problem. \x01",
            "It's something simple...\x01",
            "And also a consequence of my actions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Though it's tough for me to remember\x01",
            "the details from so long ago.\x02",
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
            "case with the Cult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10105FOh, so that's what happened...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Yeah. But actually,\x01",
            "I'm blessed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "By selling all of my property including my\x01",
            "house, I was able to repay most of the debt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Those were my personal losses, but\x01",
            "fortunately I didn't end up losing my job.\x02",
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
            "wouldn't say things like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11PAfter all, we're the only\x01",
            "family we've got in this world.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11PIt's only natural to share our troubles.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Creil... Thank you so much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'm so grateful I can\x01",
            "stay with you and Sunita.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xD)

    ChrTalk(
        0xD,
        (
            "#11PD-Dear, it's kind of\x01",
            "embarrassing hearing you say\x01",
            "that with everyone watching.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10109FUh uh, you two really\x01",
            "share such a strong bond.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FWell, I guess it doesn't really matter where you\x01",
            "live so long as you share such strong bonds.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0x2)
    SetChrSubChip(0xD, 0x1)

    ChrTalk(
        0xC,
        (
            "Ha ha, I think that's a bit\x01",
            "of an exaggeration, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Anyway, I plan to make a fresh start\x01",
            "and do my best from here on out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "And I'll be sure to pay off the rest\x01",
            "of the debt for my wife and daughter.\x02",
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
            "#12P#00104FThat's a splendid attitude.\x02\x03",
            "#00100FPlease let us know\x01",
            "if you need any more\x01",
            "help from now on.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xD, 0x1)

    ChrTalk(
        0x101,
        (
            "#12P#00000FYes, we'll be there\x01",
            "for you then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Ha ha, I'm grateful\x01",
            "that you'd do that\x01",
            "for me.\x02",
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
            "So, was that all\x01",
            "for the questions?\x02",
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
            "#12P#00000FNo, we've gotten\x01",
            "the info we need.\x02\x03",
            "#00004FWe appreciate your cooperation\x01",
            "with our investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#12P#10300FShould we get going, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FYes, let's.\x02\x03",
            "#00104FThen, Mr. Bond, we'll\x01",
            "be taking our leave now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10109FPlease keep raising\x01",
            "such a lovely family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Yeah, of course!\x02",
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

    def lambda_97B6():
        OP_95(0xFE, 51400, 0, 2650, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_97B6)

    def lambda_97D0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_97D0)
    Sleep(900)

    def lambda_97E4():
        OP_95(0xFE, 52300, 0, 2750, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_97E4)

    def lambda_97FE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_97FE)
    Sleep(900)

    def lambda_9812():
        OP_95(0xFE, 51400, 0, 3650, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9812)

    def lambda_982C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_982C)
    Sleep(900)
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)

    def lambda_9852():
        OP_95(0xFE, 52300, 0, 3750, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9852)

    def lambda_986C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_986C)
    Sleep(700)
    Sound(104, 0, 100, 0)
    OP_71(0x1, 0x10, 0x0, 0x0, 0x0)
    OP_79(0x1)
    Sleep(200)

    def lambda_9898():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_9898)
    Sleep(50)

    def lambda_98A8():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_98A8)
    Sleep(1000)

    ChrTalk(
        0xE,
        "#6POh, misters...\x02",
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

    def lambda_9923():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9923)
    Sleep(50)

    def lambda_9933():
        OP_93(0x102, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9933)
    Sleep(50)

    def lambda_9943():
        OP_93(0x109, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9943)
    Sleep(50)

    def lambda_9953():
        OP_93(0x105, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9953)
    Sleep(50)

    def lambda_9963():
        OP_95(0x101, 50250, 0, 2650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9963)
    Sleep(50)

    def lambda_9980():
        OP_95(0x102, 50500, 0, 3650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9980)
    Sleep(50)

    def lambda_999D():
        OP_95(0x109, 51500, 0, 2550, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_999D)
    Sleep(50)

    def lambda_99BA():
        OP_95(0x105, 51750, 0, 3750, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_99BA)
    SetMapObjFlags(0x1, 0x0)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0xE,
        (
            "#6PDid you talk to my\x01",
            "father and mother?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, we had a little\x01",
            "chat with them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#11P#00100FYou're Sunita, right?\x01",
            "You have great parents.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xE,
        "#6PI-I know!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#6PEspecially after the move,\x01",
            "they've been getting along\x01",
            "so good with each other...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#6PEhehe, they're\x01",
            "the best parents!\x02",
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
        "#6PNya～n㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10102FUh uh, her positive outlook is incredible.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, it's wonderful.\x02",
    )

    CloseMessageWindow()

    def lambda_9BBD():
        OP_93(0x101, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9BBD)
    Sleep(50)

    def lambda_9BCD():
        OP_93(0x102, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9BCD)
    Sleep(50)

    def lambda_9BDD():
        OP_93(0x109, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9BDD)
    Sleep(50)

    def lambda_9BED():
        OP_93(0x105, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9BED)

    ChrTalk(
        0x101,
        (
            "#12P#00003FAlright then. With this, we've \x01",
            "confirmed Mr. Bond's situation...\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x6A, 0x1, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9D47")
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
            "◆Investigation Status? (Debug)\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "  [No changes]\x01",                          # 0
            "  [Some remains]\x01",                        # 1
            "  [Finished checking the 6 places]\x01",      # 2
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
        (0, "loc_9D1A"),
        (1, "loc_9D1F"),
        (2, "loc_9D33"),
        (SWITCH_DEFAULT, "loc_9D47"),
    )


    label("loc_9D1A")

    Jump("loc_9D47")

    label("loc_9D1F")

    ClearScenarioFlags(0x131, 5)
    ClearScenarioFlags(0x131, 6)
    ClearScenarioFlags(0x132, 0)
    ClearScenarioFlags(0x132, 1)
    ClearScenarioFlags(0x132, 2)
    Jump("loc_9D47")

    label("loc_9D33")

    SetScenarioFlags(0x131, 5)
    SetScenarioFlags(0x131, 6)
    SetScenarioFlags(0x132, 0)
    SetScenarioFlags(0x132, 1)
    SetScenarioFlags(0x132, 2)
    Jump("loc_9D47")

    label("loc_9D47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9DA5")

    ChrTalk(
        0x101,
        (
            "#12P#00000FAlright, then let's continue\x01",
            "our investigation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9E21")

    label("loc_9DA5")


    ChrTalk(
        0x101,
        (
            "#12P#00000FAlright, we've finished our investigation.\x02\x03",
            "Let's head back to City Meeting Hall\x01",
            "and make our report.\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x6A, 0x1, 0x6)

    label("loc_9E21")

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

    # Function_22_8547 end

    def Function_23_9E87(): pass

    label("Function_23_9E87")

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
            "*sob, sob*... \x01",
            "Sunita did a bad thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "It's because Sunita wasn't\x01",
            "watching Mary properly...\x02",
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
        (
            "#5PSo cheer up,\x01",
            "Sunita.\x02",
        )
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

    def lambda_A049():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_A049)
    Sleep(50)

    def lambda_A059():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_A059)
    WaitChrThread(0xD, 1)

    ChrTalk(
        0xD,
        "My...\x02",
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
            "#11PYou saw it then...\x01",
            "...I'm so glad.\x02",
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
            "#11PYou guys came to mind so I\x01",
            "thought I'd ask for your help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FWe're glad you\x01",
            "feel that way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10103FYou said your kitty\x01",
            "Mary is missing.\x02\x03",
            "#10100FDo you know when\x01",
            "she disappeared?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PI don't know the\x01",
            "exact time, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PIt was sometime after yesterday evening.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "We were looking at\x01",
            "the stalls on East Street\x01",
            "when Sunita realized.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "It's as if she suddenly disappeared\x01",
            "when we took our eyes off her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "After that, everyone in the\x01",
            "shopping street helped us\x01",
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
            "*sob, sob*...\x01",
            "You're a liar, dad!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "You said she'd be\x01",
            "back by morning!\x02",
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

    def lambda_A473():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_A473)
    Sleep(50)

    def lambda_A483():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_A483)
    WaitChrThread(0xE, 2)

    ChrTalk(
        0xC,
        (
            "#11PYeah── Though all of\x01",
            "them are from yesterday.\x02",
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
            "#11PAnd there was someone who said they saw\x01",
            "Mary go in the direction of Central Square.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PAt that point, it was already late\x01",
            "in the evening. We couldn't chase\x01",
            "her down and gave up the search...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00301FAnd there's been no\x01",
            "news this morning.\x02\x03",
            "#00303FSo if she's in the city,\x01",
            "it's a complete mystery\x01",
            "as to where she's gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FThen our search area\x01",
            "is the entire city?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FHmm. I would really like\x01",
            "a few more clues...\x02\x03",
            "#00001FExcuse me, but...\x01",
            "Has Mary ever\x01",
            "left home?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PNo, never once, before now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PMary is very attached\x01",
            "to Sunita, you see.\x02",
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
            "#11PThat's why I think she lost sight\x01",
            "of us for some reason and got lost.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00003FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FAnyway I guess all we can do\x01",
            "is try searching in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FYeah, we can only\x01",
            "start from there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PWhen I've calmed down, I intend\x01",
            "to search for her again too, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PThis could take a while,\x01",
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

    # Function_23_9E87 end

    def Function_24_A991(): pass

    label("Function_24_A991")

    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "[Begin the Search Immediately]\x01",      # 0
            "[Ask to Wait a Little]\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AA69")

    ChrTalk(
        0x101,
        (
            "#6P#00000FWe're fine for now. I was\x01",
            "thinking of starting immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PI see. That's great.\x02",
    )

    CloseMessageWindow()
    Call(0, 26)
    Jump("loc_AAE3")

    label("loc_AA69")

    OP_29(0x74, 0x1, 0x1)

    ChrTalk(
        0x101,
        (
            "#6P#00000FI'm terribly sorry, but...\x01",
            "Can you wait\x01",
            "a little longer?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#11PI understand. See you later, then.\x02",
    )

    CloseMessageWindow()

    label("loc_AAE3")

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

    # Function_24_A991 end

    def Function_25_AB34(): pass

    label("Function_25_AB34")

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
        "#11PAh, you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PCan you begin\x01",
            "looking for Mary?\x02",
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
            "[Begin the Search Immediately]\x01",      # 0
            "[Ask to Wait a Little]\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ACEC")

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
    Jump("loc_AD6D")

    label("loc_ACEC")


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

    label("loc_AD6D")

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

    # Function_25_AB34 end

    def Function_26_ADBB(): pass

    label("Function_26_ADBB")

    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#6P#00100FSo Lloyd, where're\x01",
            "we searching first?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#6P#00003FHmm. It might be a repeat\x01",
            "of yesterday, but...\x02\x03",
            "#00000FTo retrace her steps, we should\x01",
            "start with a survey of East Street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00300FYeah, that sounds logical.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10304FHu hu. Those are the basics, eh?\x02",
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

    def lambda_AF49():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AF49)
    Sleep(50)

    def lambda_AF59():
        TurnDirection(0xFE, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_AF59)
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
            "Around here, that's the place she'd\x01",
            "probably be the most interested in.\x02",
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
            "#11PMrs. Marte, the owner, helped us\x01",
            "look for Mary yesterday, so she\x01",
            "would know if she stopped by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#11PIf it's not too much trouble,\x01",
            "can you ask her for me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FSure, sounds goods.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xC, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#6P#00100FAnyway, what will\x01",
            "you do, Mr. Bond?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0xC,
        "#11PFortunately, I'm off from work today.\x02",
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
            "#11PI already asked almost everyone on\x01",
            "East Street yesterday, you see.\x02",
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
            "#11PIf you learn anything new,\x01",
            "please come tell me anytime.\x02",
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
            "#12P#10300FThen first up, we have an interview\x01",
            "with a certain fishmonger.\x02",
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
            "Quest [Search for Lost Kitty]\x07\x00",
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

    # Function_26_ADBB end

    def Function_27_B416(): pass

    label("Function_27_B416")

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
        "#5PMary...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5POh! Where did you run off to!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5P*sob, sob*... \x01",
            "I was really...worried...\x01",
            "about you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#12PN-Nya～n.\x02",
    )

    CloseMessageWindow()
    OP_97(0xF, 0x0, 0x0, 0x2EE, 0x3E8, 0x0)
    Sleep(300)

    ChrTalk(
        0xE,
        (
            "#5PNo... I'm the sorry one.\x01",
            "Everything is Sunita's fault.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PBut thank you...\x01",
            "You brought her home.\x02",
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
        "#12PNya～n㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00109F*giggle*, that's great.\x02",
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
            "You found our\x01",
            "precious Mary...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Yes. How can I ever thank you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "You helped my husband\x01",
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
            "#00000FBesides, this girl\x01",
            "here did even more to\x01",
            "find her than we did.\x02\x03",
            "She calmed down a very\x01",
            "frightened Mary for us, you see.\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x1, 0xF, 0xB4, 0xC8, 0x3E8, 0x0)
    TurnDirection(0xF, 0x1A3, 500)
    Sleep(300)
    Sound(953, 0, 100, 0)

    ChrTalk(
        0xF,
        "#5PNya～n㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#5P...Mary!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#5PYou're...not saying\x01",
            "you want to be with\x01",
            "that girl, are you?\x02",
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
        "#12PN-Nyaun...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#12P#04602FAhaha, don't worry.\x02\x03",
            "#04604FMary says she loves\x01",
            "Sunita, you see.\x02\x03",
            "#04609FHearing her speak so fondly of you,\x01",
            "I've no choice but to give up.\x02",
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
        "#12PNya～n㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A3,
        (
            "#12P#04609FUh uh, then it's about\x01",
            "time for me to be going.\x02\x03",
            "#04604FI'm glad I got to play with\x01",
            "you all and meet Mary.\x02\x03",
            "#04611F──And after all, I found\x01",
            "something valuable㈱\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BAD0():

        label("loc_BAD0")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_BAD0")

    QueueWorkItem2(0x101, 2, lambda_BAD0)
    Sleep(300)

    ChrTalk(
        0x101,
        "#11P#00005FHuh...\x02",
    )

    CloseMessageWindow()

    def lambda_BAFC():
        OP_97(0xFE, 0xFFFFF8F8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_BAFC)
    Sleep(50)

    def lambda_BB19():

        label("loc_BB19")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_BB19")

    QueueWorkItem2(0x102, 2, lambda_BB19)
    Sleep(50)

    def lambda_BB2E():

        label("loc_BB2E")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_BB2E")

    QueueWorkItem2(0x104, 2, lambda_BB2E)
    Sleep(50)

    def lambda_BB43():

        label("loc_BB43")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_BB43")

    QueueWorkItem2(0x109, 2, lambda_BB43)
    Sleep(50)

    def lambda_BB58():

        label("loc_BB58")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_BB58")

    QueueWorkItem2(0x105, 2, lambda_BB58)
    Sleep(50)

    def lambda_BB6D():

        label("loc_BB6D")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_BB6D")

    QueueWorkItem2(0xC, 2, lambda_BB6D)
    Sleep(50)

    def lambda_BB82():

        label("loc_BB82")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_BB82")

    QueueWorkItem2(0xD, 2, lambda_BB82)
    Sleep(50)

    def lambda_BB97():

        label("loc_BB97")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_BB97")

    QueueWorkItem2(0xE, 2, lambda_BB97)
    Sleep(50)

    def lambda_BBAC():

        label("loc_BBAC")

        TurnDirection(0xFE, 0x1A3, 500)
        Yield()
        Jump("loc_BBAC")

    QueueWorkItem2(0xF, 2, lambda_BBAC)
    WaitChrThread(0x1A3, 1)

    ChrTalk(
        0x104,
        "#00305FH-Hey...!\x02",
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

    def lambda_BC29():
        OP_97(0xFE, 0xFFFFF448, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A3, 1, lambda_BC29)
    Sleep(300)

    def lambda_BC46():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A3, 2, lambda_BC46)
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
        (
            "#10106FS-She's like\x01",
            "a typhoon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHu hu, more like a\x01",
            "tornado, I'd say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FMan, I wish that uncle of mine\x01",
            "taught her some manners.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FS-She did help us a lot with\x01",
            "this request, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hmm. If possible, I would\x01",
            "have liked to thank her, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xC, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "──Anyway. I'd like to thank you\x01",
            "all for your help once again.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BE65():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BE65)
    Sleep(50)

    def lambda_BE75():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_BE75)

    def lambda_BE82():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_BE82)
    Sleep(50)

    def lambda_BE92():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_BE92)

    def lambda_BE9F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_BE9F)
    Sleep(50)

    def lambda_BEAF():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_BEAF)

    def lambda_BEBC():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_BEBC)
    Sleep(50)

    def lambda_BECC():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_BECC)
    WaitChrThread(0x105, 2)

    ChrTalk(
        0xD,
        "We will never forget your kindness.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Um, um, let Sunita\x01",
            "say thank you, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "Nyan㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00009FHa ha, you're very welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00100FPlease let us know if there's\x01",
            "ever anything we can do for you.\x02",
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
            "Quest [Search for Lost Kitty]\x07\x00",
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

    # Function_27_B416 end

    def Function_28_C09E(): pass

    label("Function_28_C09E")

    EventBegin(0x1)
    Sound(807, 0, 100, 0)
    Sleep(300)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "It is locked. It seems the\x01",
            "resident is already gone.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 51800, 0, -4500, 0)
    EventEnd(0x4)
    Return()

    # Function_28_C09E end

    def Function_29_C100(): pass

    label("Function_29_C100")

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

    # Function_29_C100 end

    SaveToFile()

Try(main)
