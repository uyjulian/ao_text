from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t0520.bin",                # FileName
        "t0520",                    # MapName
        "t0520",                    # Location
        0x003F,                     # MapIndex
        "ed7121",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x18,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 63, 0, 2, 0, 3],
    )

    BuildStringList((
        "t0520",                  # 0
        "Norma",                 # 1
        "Lucca",               # 2
        "Carlos",               # 3
        "Mining head Hoffman",         # 4
        "Miner Gantz",             # 5
        "Miner Max",           # 6
        "Nielsen",             # 7
        "Miners Mallo",             # 8
        "Lieutenant Mireille",           # 9
        "ester",               # 10
        "Joshua",               # 11
        "Jorgg Aged",             # 12
        "Len",                   # 13
        "Zookoist Rin",             # 14
        "Friend Aolia",         # 15
        "Mushroute Scott",         # 16
        "Grace",               # 17
    ))

    AddCharChip((
        "chr/ch23500.itc",                   # 00
        "chr/ch25700.itc",                   # 01
        "chr/ch23602.itc",                   # 02
        "chr/ch26302.itc",                   # 03
        "chr/ch30700.itc",                   # 04
        "chr/ch26202.itc",                   # 05
        "chr/ch45102.itc",                   # 06
        "chr/ch32602.itc",                   # 07
        "chr/ch30702.itc",                   # 08
        "chr/ch00602.itc",                   # 09
        "chr/ch00702.itc",                   # 0A
        "chr/ch06602.itc",                   # 0B
        "apl/ch51771.itc",                   # 0C
        "chr/ch32002.itc",                   # 0D
        "chr/ch32102.itc",                   # 0E
        "chr/ch27202.itc",                   # 0F
    ))

    DeclNpc(3700,    0,       4289,    180,  261,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(4294962416, 4294966546, 4294966436, 270,  261,  0x0, 0,   1,   0,   0,   1,   0,   7,   255,  0)
    DeclNpc(4294961097, 4294966696, 4199,    270,  389,  0x0, 0,   2,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(4294957786, 4294966696, 4294966096, 180,  389,  0x0, 0,   3,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(4294960907, 4294966546, 4294966436, 90,   389,  0x0, 0,   4,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(4294958656, 4294966696, 4294962916, 0,    389,  0x0, 0,   5,   0,   255, 255, 0,   14,  255,  0)
    DeclNpc(104349,  2150,    1330,    270,  405,  0x0, 0,   6,   0,   255, 255, 0,   15,  255,  0)
    DeclNpc(4294958656, 4294966696, 4294962916, 0,    453,  0x0, 0,   5,   0,   255, 255, 0,   16,  255,  0)
    DeclNpc(4294959706, 4294966696, 5769,    180,  453,  0x0, 0,   7,   0,   255, 255, 0,   17,  255,  0)
    DeclNpc(94790,   600,     79,      270,  452,  0x0, 0,   9,   0,   255, 255, 0,   18,  255,  0)
    DeclNpc(92949,   550,     79,      90,   452,  0x0, 0,   10,  0,   255, 255, 0,   19,  255,  0)
    DeclNpc(104349,  2150,    1330,    270,  453,  0x0, 0,   11,  0,   255, 255, 0,   20,  255,  0)
    DeclNpc(107339,  2650,    4500,    90,   471,  0x0, 1,   12,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(4294961097, 4294966696, 4199,    270,  452,  0x0, 0,   13,  0,   255, 255, 0,   23,  255,  0)
    DeclNpc(4294958007, 4294966696, 3869,    90,   452,  0x0, 0,   14,  0,   255, 255, 0,   24,  255,  0)
    DeclNpc(4294957786, 4294966696, 4294966096, 180,  452,  0x0, 0,   15,  0,   255, 255, 0,   25,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(3700,    0,       2920,    1000,    3700,    1500,    4290,    0x007E, 0,  5,  0x0000)
    DeclActor(4294963676, 0,       8000,    1200,    4294963676, 700,     8000,    0x007C, 0,  4,  0x0000)
    DeclActor(107320,  2000,    3670,    1000,    107240,  3800,    4600,    0x007E, 0,  21, 0x0000)

    ChipFrameInfo(960, 0)                                        # 0

    ScpFunction((
        "Function_0_3C0",          # 00, 0
        "Function_1_470",          # 01, 1
        "Function_2_4F2",          # 02, 2
        "Function_3_799",          # 03, 3
        "Function_4_7F2",          # 04, 4
        "Function_5_90C",          # 05, 5
        "Function_6_910",          # 06, 6
        "Function_7_1BE6",         # 07, 7
        "Function_8_2A3C",         # 08, 8
        "Function_9_2B6C",         # 09, 9
        "Function_10_2D22",        # 0A, 10
        "Function_11_2E1B",        # 0B, 11
        "Function_12_2F4B",        # 0C, 12
        "Function_13_30FE",        # 0D, 13
        "Function_14_3254",        # 0E, 14
        "Function_15_3309",        # 0F, 15
        "Function_16_3B02",        # 10, 16
        "Function_17_3C2F",        # 11, 17
        "Function_18_41EE",        # 12, 18
        "Function_19_454D",        # 13, 19
        "Function_20_4A35",        # 14, 20
        "Function_21_4BF1",        # 15, 21
        "Function_22_4BF5",        # 16, 22
        "Function_23_4D1D",        # 17, 23
        "Function_24_4F10",        # 18, 24
        "Function_25_507A",        # 19, 25
        "Function_26_51FA",        # 1A, 26
        "Function_27_5E84",        # 1B, 27
        "Function_28_5F70",        # 1C, 28
        "Function_29_5F8C",        # 1D, 29
        "Function_30_5FBC",        # 1E, 30
        "Function_31_5FEC",        # 1F, 31
        "Function_32_6008",        # 20, 32
        "Function_33_604C",        # 21, 33
        "Function_34_6090",        # 22, 34
        "Function_35_74D7",        # 23, 35
        "Function_36_7E0D",        # 24, 36
        "Function_37_861F",        # 25, 37
        "Function_38_8DEB",        # 26, 38
        "Function_39_9038",        # 27, 39
        "Function_40_9194",        # 28, 40
    ))


    def Function_0_3C0(): pass

    label("Function_0_3C0")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_3F8"),
        (1, "loc_404"),
        (2, "loc_410"),
        (3, "loc_41C"),
        (4, "loc_428"),
        (5, "loc_434"),
        (6, "loc_440"),
        (SWITCH_DEFAULT, "loc_44C"),
    )


    label("loc_3F8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_458")

    label("loc_404")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_458")

    label("loc_410")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_458")

    label("loc_41C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_458")

    label("loc_428")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_458")

    label("loc_434")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_458")

    label("loc_440")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_458")

    label("loc_44C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_458")

    label("loc_458")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_46F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_458")

    label("loc_46F")

    Return()

    # Function_0_3C0 end

    def Function_1_470(): pass

    label("Function_1_470")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4F1")
    OP_95(0xFE, -6300, -750, 390, 2000, 0x0)
    OP_95(0xFE, -7800, -750, -1400, 2000, 0x0)
    Sleep(1800)
    OP_93(0xFE, 0x2D, 0x190)
    Sleep(100)
    OP_95(0xFE, -6300, -750, 390, 2000, 0x0)
    OP_95(0xFE, -6300, -750, 3160, 2000, 0x0)
    OP_93(0xFE, 0x13B, 0x190)
    Sleep(1800)
    OP_93(0xFE, 0xB4, 0x190)
    Sleep(100)
    Jump("Function_1_470")

    label("loc_4F1")

    Return()

    # Function_1_470 end

    def Function_2_4F2(): pass

    label("Function_2_4F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_50A")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)

    label("loc_50A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_570")
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 0x9)
    SetChrSubChip(0x11, 0x0)
    EndChrThread(0x11, 0x0)
    SetChrBattleFlags(0x11, 0x4)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 0xA)
    SetChrSubChip(0x12, 0x0)
    EndChrThread(0x12, 0x0)
    SetChrBattleFlags(0x12, 0x4)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x13, 0xB)
    SetChrSubChip(0x13, 0x0)
    EndChrThread(0x13, 0x0)
    SetChrBattleFlags(0x13, 0x4)
    SetChrFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    OP_93(0x14, 0x0, 0x0)
    Jump("loc_789")

    label("loc_570")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_5AB")
    SetChrPos(0x9, 11090, 0, -760, 90)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrChipByIndex(0x10, 0x7)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_789")

    label("loc_5AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_621")
    SetChrPos(0x9, -4840, -750, 1710, 270)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrChipByIndex(0xF, 0x5)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x10)
    SetChrChipByIndex(0xC, 0x8)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrPos(0xC, -9510, -600, -1200, 180)
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61C")
    SetChrFlags(0xC, 0x10)

    label("loc_61C")

    Jump("loc_789")

    label("loc_621")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_65B")
    ClearChrFlags(0x15, 0x80)
    SetChrChipByIndex(0x15, 0xD)
    SetChrSubChip(0x15, 0x0)
    EndChrThread(0x15, 0x0)
    SetChrBattleFlags(0x15, 0x4)
    ClearChrFlags(0x16, 0x80)
    SetChrChipByIndex(0x16, 0xE)
    SetChrSubChip(0x16, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrBattleFlags(0x16, 0x4)
    Jump("loc_789")

    label("loc_65B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_669")
    Jump("loc_789")

    label("loc_669")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_68D")
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    Jump("loc_789")

    label("loc_68D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_69B")
    Jump("loc_789")

    label("loc_69B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_6A9")
    Jump("loc_789")

    label("loc_6A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_6D6")
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C6")
    SetChrFlags(0xC, 0x10)

    label("loc_6C6")

    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0x9, 0x10)
    Jump("loc_789")

    label("loc_6D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_6E4")
    Jump("loc_789")

    label("loc_6E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_6F2")
    Jump("loc_789")

    label("loc_6F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_740")
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_73B")
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xD, 0x10)

    label("loc_73B")

    Jump("loc_789")

    label("loc_740")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_764")
    ClearChrFlags(0x17, 0x80)
    SetChrChipByIndex(0x17, 0xF)
    SetChrSubChip(0x17, 0x0)
    EndChrThread(0x17, 0x0)
    SetChrBattleFlags(0x17, 0x4)
    Jump("loc_789")

    label("loc_764")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_772")
    Jump("loc_789")

    label("loc_772")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_780")
    Jump("loc_789")

    label("loc_780")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_789")

    label("loc_789")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_798")
    ClearScenarioFlags(0x22, 0)
    Event(0, 34)

    label("loc_798")

    Return()

    # Function_2_4F2 end

    def Function_3_799(): pass

    label("Function_3_799")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_7AB")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D1")
    SetMapObjFrame(0xFF, "hikari_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_7D1")

    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_7F1")
    OP_66(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F1")
    OP_1B(0x3, 0x0, 0x1A)

    label("loc_7F1")

    Return()

    # Function_3_799 end

    def Function_4_7F2(): pass

    label("Function_4_7F2")

    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "★ Red Brick Tea · Recipe ★\x01",
            "~ Although it is a classic one\x01",
            "Friedfish ~\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "A recipe of fried fish is written.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('料理手册', 0x0)"), scpexpr(EXPR_END)), "loc_908")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_908")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "\"Friedfish\"\x07\x00",
            "I learned the recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_908")

    TalkEnd(0xFF)
    Return()

    # Function_4_7F2 end

    def Function_5_90C(): pass

    label("Function_5_90C")

    Call(0, 6)
    Return()

    # Function_5_90C end

    def Function_6_910(): pass

    label("Function_6_910")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_93E")
    Call(0, 35)
    Return()

    label("loc_93E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x175, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x175, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_967")
    Call(0, 36)
    Return()

    label("loc_967")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_974")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BE2")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",          # 0
            "to shop\x01",      # 1
            "To take a break\x01",        # 2
            "quit\x01",            # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9E7")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_9E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A07")
    OP_AF(0x52)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1BDD")

    label("loc_A07")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A27")
    OP_AF(0x50)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1BDD")

    label("loc_A27")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A3B")
    Jump("loc_1BDD")

    label("loc_A3B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A53")
    TalkEnd(0x8)
    Return()

    label("loc_A53")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BDD")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_B02")

    ChrTalk(
        0x8,
        (
            "Hoofu, specialty of mining town\x01",
            "If you eat steak,\x01",
            "Someday the power comes up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Also,\x01",
            "When you want to eat Gatszuri\x01",
            "You are coming to Uchi again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BDD")

    label("loc_B02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_CB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C06")

    ChrTalk(
        0x8,
        (
            "After the commotion in the city,\x01",
            "With the exhausted appearance of being exhausted,\x01",
            "A crying face girl came.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They are also in Crossbell City\x01",
            "She seems to have participated in the liberation strategy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Cooperating with resistance\x01",
            "As we are, by all means\x01",
            "It is a place I want to labor.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CB2")

    label("loc_C06")


    ChrTalk(
        0x8,
        (
            "The hypocrite men who are absent below,\x01",
            "In Crossbell City\x01",
            "She seems to have participated in the liberation strategy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Another hit prisoner came also\x01",
            "He helped out the demonic beasts … …\x01",
            "Really to care for them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CB2")

    Jump("loc_1BDD")

    label("loc_CB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_DE2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D79")

    ChrTalk(
        0x8,
        (
            "Now, resistance leader\x01",
            "Mireille san's Toko has come to supply.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You guys, soon\x01",
            "You do big strategy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We also support you.\x01",
            "You will feel better.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_DDD")

    label("loc_D79")


    ChrTalk(
        0x8,
        (
            "You guys, soon\x01",
            "You do big strategy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We also support you.\x01",
            "You will feel better.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DDD")

    Jump("loc_1BDD")

    label("loc_DE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1083")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EFB")
    TurnDirection(0x8, 0x104, 0)

    ChrTalk(
        0x8,
        (
            "From Randy, Resistance\x01",
            "Have you ever been away?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FOh, I have to help you\x01",
            "My daughter is waiting.\x02\x03",
            "#00302FOba-chan, for a while\x01",
            "With the guys in Mainz\x01",
            "I asked Mireille.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Okay, that's OK.\x01",
            "You should be careful too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AD, 7)
    Jump("loc_107E")

    label("loc_EFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_100A")

    ChrTalk(
        0x8,
        (
            "For children of resistance,\x01",
            "Teaching good hiding places in mountainous areas,\x01",
            "Help me with food and medicine supply ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even though the defense troops come to search\x01",
            "Doing it thoroughly,\x01",
            "Well I guessed a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's not a big deal,\x01",
            "I have to do as much as I can.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_107E")

    label("loc_100A")


    ChrTalk(
        0x8,
        (
            "Resistance is\x01",
            "I want you to work hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I can not do much help,\x01",
            "I have to do as much as I can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_107E")

    Jump("loc_1BDD")

    label("loc_1083")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_11F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_119D")

    ChrTalk(
        0x8,
        (
            "Those guys in that armed group,\x01",
            "In the end people and food in town\x01",
            "I did not take any hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To what I had a terrible eye\x01",
            "It does not change but it suffered great damage\x01",
            "It might be better than the guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "…… But what was the purpose?\x01",
            "I do not really understand Wake.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11EE")

    label("loc_119D")


    ChrTalk(
        0x8,
        (
            "A group of armed groups ……\x01",
            "What was the purpose?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I do not really understand Wake.\x02",
    )

    CloseMessageWindow()

    label("loc_11EE")

    Jump("loc_1BDD")

    label("loc_11F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1265")

    ChrTalk(
        0x8,
        "Well, I have a pleasant rain.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "On such a day\x01",
            "The number of guests at night will also decrease,\x01",
            "I guess it's nonbilli.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BDD")

    label("loc_1265")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_152C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x175, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1415")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1362")

    ChrTalk(
        0x8,
        (
            "Libert made glass,\x01",
            "It was nice to receive it properly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To the baggage that arrived by mistake\x01",
            "When female or something is in it\x01",
            "It was really fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha, you too\x01",
            "It was a pain.\x01",
            "I will thank you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1410")

    label("loc_1362")


    ChrTalk(
        0x8,
        (
            "I ordered it a while ago.\x01",
            "Libert made glass,\x01",
            "It was nice to receive it properly.\x02\x03",
            "It was really fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha, you too\x01",
            "It was a pain.\x01",
            "I will thank you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1410")

    Jump("loc_1527")

    label("loc_1415")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14D9")

    ChrTalk(
        0x8,
        (
            "Mr. Maruro,\x01",
            "It seems that he finally got well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "How to comfort Lucca,\x01",
            "Even from the view of the grove\x01",
            "I thought it was not blatant … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, you himself\x01",
            "I wish I was fine.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1527")

    label("loc_14D9")


    ChrTalk(
        0x8,
        (
            "Well, this also Mr. Maruro\x01",
            "It seems I got better … …\x01",
            "I guess it's time for a while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1527")

    Jump("loc_1BDD")

    label("loc_152C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_16AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_161A")

    ChrTalk(
        0x8,
        (
            "Recently, Mr. Maruro\x01",
            "I was hated by Lucca\x01",
            "It seems to be thinking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I do not put a face on the bar,\x01",
            "I can not get into work either.\x01",
            "It seems to be in trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Lucca himself does not have consciousness\x01",
            "It's a subtle story, is not it?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16A9")

    label("loc_161A")


    ChrTalk(
        0x8,
        (
            "But, Gantz also\x01",
            "There is a nice place.\x01",
            "It is a direct talk for friends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, because the other party is that Lucca\x01",
            "It looks like he is struggling.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16A9")

    Jump("loc_1BDD")

    label("loc_16AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_17DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1784")

    ChrTalk(
        0x8,
        (
            "Mr. Maruro, yesterday to Lucca\x01",
            "Let yourself get drunk and approach\x01",
            "It seems I was calling … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ignored by the absence of perfection,\x01",
            "It seems I've completely sunk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "…… Hehe, it was fun to watch.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17D9")

    label("loc_1784")


    ChrTalk(
        0x8,
        "Mr. Maruro is sorry, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Which, next time you have snacks\x01",
            "I'd like to serve you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17D9")

    Jump("loc_1BDD")

    label("loc_17DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_18F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1867")

    ChrTalk(
        0x8,
        (
            "Miners are on holiday today.\x01",
            "I have been drinking since the daytime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you do not mind, you are\x01",
            "How about when you drink?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_18EB")

    label("loc_1867")


    ChrTalk(
        0x8,
        (
            "Whew.\x01",
            "Even if the mine is closed\x01",
            "I have no time to rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hehe, well it was fun\x01",
            "I'm doing this business\x01",
            "I guess it is.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18EB")

    Jump("loc_1BDD")

    label("loc_18F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1A9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A15")

    ChrTalk(
        0x8,
        (
            "Yesterday, Lucca got drunk\x01",
            "I was showing off the crap and Laughing Ueto.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That child is usually Buiaiso,\x01",
            "To tell the truth, it is very cute if you laugh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Mr. Maruro noticed it,\x01",
            "It seems that it was completely holed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Kuufu, love affair is my favorite.\x01",
            "I wonder what will be the future.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A95")

    label("loc_1A15")


    ChrTalk(
        0x8,
        (
            "Mr. Maruro, at the banquet yesterday\x01",
            "It seems that Hole got lost in Lucca.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Kuufu, love affair is my favorite.\x01",
            "I wonder what will be the future.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A95")

    Jump("loc_1BDD")

    label("loc_1A9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_1BDD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B77")

    ChrTalk(
        0x8,
        (
            "Come here, come in.\x01",
            "You came often from a distance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Uchi is good for miners,\x01",
            "I can have you eaten full\x01",
            "The menu is pounding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I will make it a heap of magnitude,\x01",
            "If you do not mind, please eat something.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BDD")

    label("loc_1B77")


    ChrTalk(
        0x8,
        (
            "I came all the way,\x01",
            "If you do not mind, please eat something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There is a menu that can be full\x01",
            "It is pushing me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BDD")

    Jump("loc_974")

    label("loc_1BE2")

    TalkEnd(0x8)
    Return()

    # Function_6_910 end

    def Function_7_1BE6(): pass

    label("Function_7_1BE6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1D90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D02")

    ChrTalk(
        0x9,
        (
            "Mr. Gantz and Maruro,\x01",
            "I joyfully went out to the mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Even at the banquet commemorating the resumption tonight\x01",
            "I wonder if I am going to do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "…… Boy, it is awkward.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "But outside situation is like that\x01",
            "There are things that are the same as before\x01",
            "I feel relieved somewhat.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1D8B")

    label("loc_1D02")


    ChrTalk(
        0x9,
        (
            "Outside is such a situation,\x01",
            "There are things that are the same as before\x01",
            "I feel relieved somewhat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "… Well, I'm worried tonight\x01",
            "Shall I enjoy also?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D8B")

    Jump("loc_2A38")

    label("loc_1D90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1F30")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E9A")

    ChrTalk(
        0x9,
        (
            "That leader,\x01",
            "It's a very strong core.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In the wrong regime\x01",
            "To say differently the first,\x01",
            "A man can do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "That posture, as a woman\x01",
            "There are many places to emulate.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1E92")

    ChrTalk(
        0x109,
        "#10104FYeah … I really think so.\x02",
    )

    CloseMessageWindow()

    label("loc_1E92")

    SetScenarioFlags(0x0, 1)
    Jump("loc_1F2B")

    label("loc_1E9A")


    ChrTalk(
        0x9,
        (
            "In the wrong regime\x01",
            "To say differently the first,\x01",
            "A man can do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "To that leader's attitude,\x01",
            "There seems to be places to emulate as women.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F2B")

    Jump("loc_2A38")

    label("loc_1F30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2180")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2047")

    ChrTalk(
        0x9,
        (
            "From me\x01",
            "I'm reading the following novels ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Because this is the situation\x01",
            "Continued publications are not arriving,\x01",
            "Should I stop reading for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "… … If it's okay, I will give it.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '沐浴阳光的阿尼艾丝12卷'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('沐浴阳光的阿尼艾丝12卷', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x189, 3)
    Jump("loc_217B")

    label("loc_2047")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20F6")

    ChrTalk(
        0x9,
        (
            "Mr. Gantz and Maruro,\x01",
            "Recently I have been passing since daytime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "…… Well, after the mine was closed\x01",
            "In the current situation where you can not go out to the city,\x01",
            "It may be useless.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_217B")

    label("loc_20F6")


    ChrTalk(
        0x9,
        (
            "After the mine was closed down,\x01",
            "You can not go to the city with movement restrictions\x01",
            "You also want to drink from daytime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Ha\x01",
            "It's troublesome, but I will go out with you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_217B")

    Jump("loc_2A38")

    label("loc_2180")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2306")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2276")

    ChrTalk(
        0x9,
        (
            "When the town was occupied ……\x01",
            "I only have trembling in the corner of the shop\x01",
            "I could not do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "But, Mr. Maruro always\x01",
            "It's all right, I bet you'll be saved\x01",
            "Please encourage me …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "…… I thought he was an unreliable person,\x01",
            "I reviewed a bit.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2301")

    label("loc_2276")


    ChrTalk(
        0x9,
        (
            "At that time ……\x01",
            "Even curse like usual\x01",
            "I was scared as I could not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "…… To Mr. Maruro who encouraged me\x01",
            "You must thank him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2301")

    Jump("loc_2A38")

    label("loc_2306")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_238C")

    ChrTalk(
        0x9,
        (
            "The rainy day is nothing.\x01",
            "Cleaning is troublesome because the floor gets wet … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Carlos also ate quickly,\x01",
            "I wonder if you will return.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A38")

    label("loc_238C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2498")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2453")

    ChrTalk(
        0x9,
        (
            "…… After all, yesterday's\x01",
            "I wonder what was it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "As Ganz asked me,\x01",
            "\"If you do not mind?\" \"\x01",
            "I only said that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, whatever.\x01",
            "Rapidly cleaning and cleaning ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2493")

    label("loc_2453")


    ChrTalk(
        0x9,
        "…… Fua ~, Daruu ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Clean up quickly.\x02",
    )

    CloseMessageWindow()

    label("loc_2493")

    Jump("loc_2A38")

    label("loc_2498")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2547")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24B3")
    Call(0, 8)
    Jump("loc_2542")

    label("loc_24B3")

    OP_4B(0xC, 0xFF)

    ChrTalk(
        0x9,
        "Well, well … well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Mr. Ganz\x01",
            "If you pay the accumulated money\x01",
            "You can do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Um … … no it is that,\x01",
            "It's called another story ……\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)

    label("loc_2542")

    Jump("loc_2A38")

    label("loc_2547")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_26B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2659")

    ChrTalk(
        0x9,
        (
            "Mr. Maruro, what is it?\x01",
            "Yesterday was strange.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Talking to me briefly,\x01",
            "\"Do you want to drink together?\" \"And\x01",
            "Inviting me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Since it is annoying,\x01",
            "Today is depressed strangely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, what do you want me to do?\x01",
            "It is really troublesome.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_26B0")

    label("loc_2659")


    ChrTalk(
        0x9,
        (
            "Well, yesterday's Mr. Maruro\x01",
            "It was really troublesome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "So this is drunk … …\x02",
    )

    CloseMessageWindow()

    label("loc_26B0")

    Jump("loc_2A38")

    label("loc_26B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_27C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2764")

    ChrTalk(
        0x9,
        (
            "Because it is a holiday\x01",
            "Good day to day day\x01",
            "It makes me feel like drinking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I got drunk soon after drinking\x01",
            "I will lose my memory,\x01",
            "I do not quite understand the goodness.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_27C4")

    label("loc_2764")


    ChrTalk(
        0x9,
        (
            "Good day to day day\x01",
            "It makes me feel like drinking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "… Well, somewhere.\x01",
            "Everyone looks like fun.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27C4")

    Jump("loc_2A38")

    label("loc_27C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_28F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2896")

    ChrTalk(
        0x9,
        "Ah you want to be ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Yesterday, at the banquet of the miners\x01",
            "Have been dated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I can not drink drinking alcohol well\x01",
            "There is no memory in drinking it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "…… I wonder if I did something.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_28F4")

    label("loc_2896")


    ChrTalk(
        0x9,
        (
            "Ah, I want to head ….\x01",
            "There is no memory of yesterday at all either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "…… I, doing something extra\x01",
            "You do not think so.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28F4")

    Jump("loc_2A38")

    label("loc_28F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_2A38")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29AB")

    ChrTalk(
        0x9,
        (
            "In the meantime, Mr. Gans again\x01",
            "I got a loss of gambling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "As before, with the guts\x01",
            "It is nice to complain that … ….\x01",
            "…… That person also does not understand.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A38")

    label("loc_29AB")


    ChrTalk(
        0x9,
        (
            "Mr. Gantz, recently\x01",
            "Even though I lose in gambling\x01",
            "I'm no longer complaining like Gutikuchi.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "… … losing if I lose,\x01",
            "I do not know how to drink with chicken.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A38")

    TalkEnd(0xFE)
    Return()

    # Function_7_1BE6 end

    def Function_8_2A3C(): pass

    label("Function_8_2A3C")

    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xC,
        (
            "Lucca chan.\x01",
            "Let's ask this, this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hey, Mr. Gantz.\x01",
            "Why do I bother to say Mr. Maruro\x01",
            "Do I have to encourage them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "He is not energetic recently,\x01",
            "It is a story I do not care about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "No, no, rather\x01",
            "Is it a big alias or something ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "…… I do not know the meaning.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x0, 6)
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_8_2A3C end

    def Function_9_2B6C(): pass

    label("Function_9_2B6C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2B7D")
    Jump("loc_2D1E")

    label("loc_2B7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2CCF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C56")

    ChrTalk(
        0xA,
        (
            "Today we will transport seven ice stone\x01",
            "I did it in the morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "It's getting rainy.\x01",
            "When the ground muddy,\x01",
            "Tire is taken and it's tough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "You can choose a less dangerous time\x01",
            "It is because of driving skills.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2CCA")

    label("loc_2C56")


    ChrTalk(
        0xA,
        (
            "Today we will transport seven ice stone\x01",
            "I did it in the morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "You can choose a less dangerous time\x01",
            "It is because of driving skills.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CCA")

    Jump("loc_2D1E")

    label("loc_2CCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2CDD")
    Jump("loc_2D1E")

    label("loc_2CDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2CEB")
    Jump("loc_2D1E")

    label("loc_2CEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2CF9")
    Jump("loc_2D1E")

    label("loc_2CF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2D07")
    Jump("loc_2D1E")

    label("loc_2D07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2D15")
    Jump("loc_2D1E")

    label("loc_2D15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_2D1E")

    label("loc_2D1E")

    TalkEnd(0xFE)
    Return()

    # Function_9_2B6C end

    def Function_10_2D22(): pass

    label("Function_10_2D22")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2D33")
    Jump("loc_2E17")

    label("loc_2D33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2D41")
    Jump("loc_2E17")

    label("loc_2D41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2D4F")
    Jump("loc_2E17")

    label("loc_2D4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2D5D")
    Jump("loc_2E17")

    label("loc_2D5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2D6B")
    Jump("loc_2E17")

    label("loc_2D6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2E00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D86")
    Call(0, 11)
    Jump("loc_2DFB")

    label("loc_2D86")


    ChrTalk(
        0xB,
        (
            "When you scold me,\x01",
            "Do not scold me,\x01",
            "If it is a child's tame, hey.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "To pamper\x01",
            "It was not my parent's job.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DFB")

    Jump("loc_2E17")

    label("loc_2E00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2E0E")
    Jump("loc_2E17")

    label("loc_2E0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_2E17")

    label("loc_2E17")

    TalkEnd(0xFE)
    Return()

    # Function_10_2D22 end

    def Function_11_2E1B(): pass

    label("Function_11_2E1B")

    OP_4B(0xB, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xD,
        (
            "However, yesterday's mine head\x01",
            "I was surprised at the curtain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "With the same condition as getting angry with us\x01",
            "I'm angry with Alec.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "When you scold me,\x01",
            "Do not scold me,\x01",
            "For the sake of the child, hey.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If we become parents too\x01",
            "My feelings\x01",
            "You will surely understand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "I do not feel like that …\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xD, 0x10)
    SetScenarioFlags(0x0, 7)
    OP_4C(0xB, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_11_2E1B end

    def Function_12_2F4B(): pass

    label("Function_12_2F4B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2F5C")
    Jump("loc_30FA")

    label("loc_2F5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2F6A")
    Jump("loc_30FA")

    label("loc_2F6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2FF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F85")
    Call(0, 13)
    Jump("loc_2FED")

    label("loc_2F85")


    ChrTalk(
        0xC,
        (
            "Because this is the situation\x01",
            "From daytime sake too\x01",
            "I do not feel like it …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Oh, go to the casino …\x02",
    )

    CloseMessageWindow()

    label("loc_2FED")

    Jump("loc_30FA")

    label("loc_2FF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3000")
    Jump("loc_30FA")

    label("loc_3000")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_300E")
    Jump("loc_30FA")

    label("loc_300E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_301C")
    Jump("loc_30FA")

    label("loc_301C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_30C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3037")
    Call(0, 8)
    Jump("loc_30C2")

    label("loc_3037")


    ChrTalk(
        0xC,
        (
            "(For the time being, Lucca-chan\x01",
            "Comfort me, Maruro too\x01",
            "I should be fine. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "(Anyway OK\x01",
            "You gotta know …! )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30C2")

    Jump("loc_30FA")

    label("loc_30C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_30D5")
    Jump("loc_30FA")

    label("loc_30D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_30E3")
    Jump("loc_30FA")

    label("loc_30E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_30F1")
    Jump("loc_30FA")

    label("loc_30F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_30FA")

    label("loc_30FA")

    TalkEnd(0xFE)
    Return()

    # Function_12_2F4B end

    def Function_13_30FE(): pass

    label("Function_13_30FE")

    OP_4B(0xC, 0xFF)
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xC,
        (
            "Oh …… In such a situation\x01",
            "I can not go to the casino in the town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "How long will this life last?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "There is no entertainment\x01",
            "After all there is something painful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "However, the mine is closed\x01",
            "I can not get into work either.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xC)
    OP_64(0xF)

    ChrTalk(
        0xC,
        "Huh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "I only have a sigh.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xF, 0x10)
    OP_4C(0xC, 0xFF)
    OP_4C(0xF, 0xFF)
    Return()

    # Function_13_30FE end

    def Function_14_3254(): pass

    label("Function_14_3254")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3265")
    Jump("loc_3305")

    label("loc_3265")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3273")
    Jump("loc_3305")

    label("loc_3273")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3281")
    Jump("loc_3305")

    label("loc_3281")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_328F")
    Jump("loc_3305")

    label("loc_328F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_329D")
    Jump("loc_3305")

    label("loc_329D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_32EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32B8")
    Call(0, 11)
    Jump("loc_32E9")

    label("loc_32B8")


    ChrTalk(
        0xD,
        (
            "Well, my parents\x01",
            "It is quite difficult.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32E9")

    Jump("loc_3305")

    label("loc_32EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_32FC")
    Jump("loc_3305")

    label("loc_32FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_3305")

    label("loc_3305")

    TalkEnd(0xFE)
    Return()

    # Function_14_3254 end

    def Function_15_3309(): pass

    label("Function_15_3309")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3B01")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_34D1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x89, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_34B6")
    TalkBegin(0xFE)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_33BE")
    Jump("loc_3408")

    label("loc_33BE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_33DE")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3408")

    label("loc_33DE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_33FE")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3408")

    label("loc_33FE")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3408")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)

    ChrTalk(
        0xFE,
        (
            "Everyone, for today's interview\x01",
            "To associate\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If there is another opportunity,\x01",
            "I hope I can talk.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_34CC")

    label("loc_34B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 7)), scpexpr(EXPR_END)), "loc_34C8")
    Call(0, 39)
    Return()

    label("loc_34C8")

    Call(0, 37)
    Return()

    label("loc_34CC")

    Jump("loc_3B01")

    label("loc_34D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3999")
    TalkBegin(0xFE)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3579")
    Jump("loc_35C3")

    label("loc_3579")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3599")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_35C3")

    label("loc_3599")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_35B9")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_35C3")

    label("loc_35B9")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_35C3")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3904")

    ChrTalk(
        0x101,
        "#00000FMr. Nielsen -\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "Hmm, that voice is Mr. Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Why are you going to Mainz today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, on a patrol\x01",
            "It is a place to stop by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FIf you are Nielsen,\x01",
            "Did you get in the interview?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yeah, in fact to the mayor here\x01",
            "I am planning to interview you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "History of the seven ix and stone mining of this town\x01",
            "Regarding the transition in modern times,\x01",
            "I am planning to tell you a story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The question of independence is questioned\x01",
            "Because now it is again in the history of autonomous state\x01",
            "I thought about focusing on it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FOh, that is …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FSomehow,\x01",
            "The eyes are different.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha, thanks always\x01",
            "I am only taking a long way around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But you also\x01",
            "I hear you are as busy as ever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think that it will be various difficulties in the future,\x01",
            "Please do your best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, thank you.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16B, 5)
    Jump("loc_398D")

    label("loc_3904")


    ChrTalk(
        0xFE,
        (
            "Well, until the time of news coverage\x01",
            "I still have plenty of time to spare\x01",
            "I will relax.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, this is quiet.\x01",
            "It is a nice room to calm down.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_398D")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_3B01")

    label("loc_3999")

    TalkBegin(0xFE)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3A2D")
    Jump("loc_3A77")

    label("loc_3A2D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3A4D")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3A77")

    label("loc_3A4D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3A6D")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3A77")

    label("loc_3A6D")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3A77")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)

    ChrTalk(
        0xFE,
        (
            "Hehe, this is quiet.\x01",
            "It is a nice room to calm down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Until the time of coverage\x01",
            "It seems that I can relax.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)

    label("loc_3B01")

    Return()

    # Function_15_3309 end

    def Function_16_3B02(): pass

    label("Function_16_3B02")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3B13")
    Jump("loc_3C2B")

    label("loc_3B13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_3B21")
    Jump("loc_3C2B")

    label("loc_3B21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3C2B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B3C")
    Call(0, 13)
    Jump("loc_3C2B")

    label("loc_3B3C")

    SetChrSubChip(0xF, 0x2)

    ChrTalk(
        0xF,
        (
            "(Because I can meet Lucca at first\x01",
            "I also thought it was not bad so far … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "(I thought I was immersed in the bar\x01",
            "Impression is not very good … …)\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x9, 0xFF)
    TurnDirection(0x9, 0xF, 500)
    OP_63(0x9, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        "(… I wonder what you are watching.\x02",
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_93(0x9, 0x10E, 0x0)
    SetChrSubChip(0xF, 0x0)

    label("loc_3C2B")

    TalkEnd(0xFE)
    Return()

    # Function_16_3B02 end

    def Function_17_3C2F(): pass

    label("Function_17_3C2F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3C40")
    Jump("loc_41EA")

    label("loc_3C40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_41E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4092")

    ChrTalk(
        0x10,
        (
            "#07901FRandy, everyone at the support department ……\x01",
            "The story was heard.\x02\x03",
            "#07903FNow that the declaration of independence became ineffective,\x01",
            "At least the president\x01",
            "You should not be able to move freely.\x02\x03",
            "#07901FThen wrap around the city\x01",
            "Even if \"barrier\" disappears … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FRelease Crossbell City\x01",
            "It is the biggest opportunity, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThe direction of the barrier is with us\x01",
            "I manage to erase it somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FBut, of course, \"red constellation\" also\x01",
            "I am prepared for that situation.\x02\x03",
            "#00301FBefore you decide to do strategy strategy\x01",
            "Full-fledged resistance hunting\x01",
            "It may start.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00103FIt seems better to hurry …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#07903FAnyway, now for the beginning of the strategy\x01",
            "I will prepare for everything.\x02\x03",
            "You can borrow help from the gods,\x01",
            "Both are \"red constellation\"\x01",
            "I think I can do a good game.\x02\x03",
            "#07901FSo, the way of the barrier\x01",
            "I'm begging for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FOh, leave it to me.\x02\x03",
            "#00301F… … Be careful, Mireille.\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0x104, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x10, 0x10)
    TurnDirection(0x10, 0x104, 0)
    OP_52(0x10, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3FF7")
    Jump("loc_4041")

    label("loc_3FF7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4017")
    OP_52(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4041")

    label("loc_4017")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4037")
    OP_52(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4041")

    label("loc_4037")

    OP_52(0x10, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4041")

    OP_52(0x10, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x104, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x10, 0x10)

    ChrTalk(
        0x10,
        "#07902FWell, there too.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AF, 0)
    ClearChrFlags(0x10, 0x10)
    Jump("loc_41DC")

    label("loc_4092")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_416E")

    ChrTalk(
        0x10,
        (
            "#07903FAnyway, now for the beginning of the strategy\x01",
            "I will prepare for everything.\x02\x03",
            "You can borrow help from the gods,\x01",
            "Both are \"red constellation\"\x01",
            "I think I can do a good game.\x02\x03",
            "#07901FYou guys in the barrier\x01",
            "I'm begging for you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_41DC")

    label("loc_416E")


    ChrTalk(
        0x10,
        (
            "#07903FTowards the beginning of the operation now\x01",
            "I will prepare for everything.\x02\x03",
            "#07901FYou guys in the barrier\x01",
            "I'm begging for you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41DC")

    Jump("loc_41EA")

    label("loc_41E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_41EA")

    label("loc_41EA")

    TalkEnd(0xFE)
    Return()

    # Function_17_3C2F end

    def Function_18_41EE(): pass

    label("Function_18_41EE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_449C")

    ChrTalk(
        0x11,
        (
            "#00802F#30W…… Lloyd guys.\x01",
            "Be careful again.\x02\x03",
            "#00808FIt is good to work hard,\x01",
            "Like \"Patel-Mattel\"\x01",
            "Is not it wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FOh … I know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00308FThink about it, for us too\x01",
            "It was a benefactor of life …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F…… When I visited the studio before\x01",
            "I wish I had talked more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#00808F#30WYeah … I also\x01",
            "I should have talked more.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x11)

    ChrTalk(
        0x11,
        (
            "#00804F#30W…… Ren's thing is\x01",
            "Please do not worry.\x02\x03",
            "#00800FOver the past six months, I have had various experiences\x01",
            "It is getting stronger in the true sense … …\x02\x03",
            "#00802FI also have important friends\x01",
            "I think it will surely be overcome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00004FI see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F…… If you wake up\x01",
            "Please say hello to me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_4549")

    label("loc_449C")


    ChrTalk(
        0x11,
        (
            "#00804F#30WDo not worry about Len.\x02\x03",
            "#00800FOver the past six months, I have had various experiences\x01",
            "It is getting stronger in the true sense … …\x02\x03",
            "#00802FI also have important friends\x01",
            "I think it will surely be overcome.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4549")

    TalkEnd(0xFE)
    Return()

    # Function_18_41EE end

    def Function_19_454D(): pass

    label("Function_19_454D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4990")

    ChrTalk(
        0x12,
        (
            "#00903F#30W…… Dr. Novartis already\x01",
            "You seem to have left this place.\x02\x03",
            "#00901FThis time \"association\" more than this,\x01",
            "I can saved you not going to the enemy … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FTo be honest, what are you aiming at?\x01",
            "I did not understand it here.\x02\x03",
            "#00003FSomething in the direction of the empire\x01",
            "It seems like I'm planning … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#00903F#30W…… \"Phantom flame plan\".\x02\x03",
            "#00901FBegan the Crossbell incident\x01",
            "It seems to be a large-scale plan ….\x02\x03",
            "#00908F…… Olivier are worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205FOlivier said … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303FIs that Oliver's Prince of Olva?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#00903F#30WYes, since the civil war began in the empire,\x01",
            "I can not contact you.\x02\x03",
            "#00908FAs long as Muller is with you,\x01",
            "I think that rare things are not … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108FStill worried ….\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_498B")
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x12,
        (
            "#00900F#30WThat's right, you guys …\x01",
            "Will you accept this?\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '塞姆里亚石碎片'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('塞姆里亚石碎片', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x18A, 3)

    ChrTalk(
        0x101,
        "#00005Fthis is……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#00900F#30WThe end of \"Patel-Mattel\"\x01",
            "I was falling down to the place I got up to.\x02\x03",
            "#00903F… …. Maybe, \"Shinkin plane\"\x01",
            "I think that it is part of parts.\x01",
            "It might be useful for something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FI understood……\x01",
            "I will thank you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_498B")

    Jump("loc_4A31")

    label("loc_4990")


    ChrTalk(
        0x12,
        (
            "#00903F#30WThat \"Big Tree\" ……\x02\x03",
            "Floating city that appeared in Libert#8RLiber-arc#than\x01",
            "I think that it is larger than the scale.\x02\x03",
            "#00900FPlease be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A31")

    TalkEnd(0xFE)
    Return()

    # Function_19_454D end

    def Function_20_4A35(): pass

    label("Function_20_4A35")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B3C")

    ChrTalk(
        0x13,
        (
            "#03900F\"Thinking unit of\" Patel-Mattel \"\x01",
            "Originally, such autonomous behavior\x01",
            "It was not designed to be taken.\x02\x03",
            "By meeting Ren he also\x01",
            "I mean that I got a \"heart\" ……\x02\x03",
            "#03903F…… It has been decades after becoming a doll maker.\x01",
            "It is still learned still.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_4BED")

    label("loc_4B3C")


    ChrTalk(
        0x13,
        (
            "#03900F…… This case, for Len\x01",
            "Conversely, it may work in a good direction.\x02\x03",
            "#03903F\"Farewell\" that I could not experience in the past\x01",
            "Because I experienced it in the real sense … …\x02\x03",
            "#03900FEverything will be from now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BED")

    TalkEnd(0xFE)
    Return()

    # Function_20_4A35 end

    def Function_21_4BF1(): pass

    label("Function_21_4BF1")

    Call(0, 22)
    Return()

    # Function_21_4BF1 end

    def Function_22_4BF5(): pass

    label("Function_22_4BF5")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CB8")

    ChrTalk(
        0x14,
        (
            "#03317F#2S#40W……… Patel-Mattel …………\x02\x03",
            "#2S#40W……why………\x01",
            "………… Why do you call Len ………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F……Len…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00103F… … let's leave it.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_4D19")

    label("loc_4CB8")


    ChrTalk(
        0x14,
        "#03317F#2S#40W……… Dad ……… Mama …………\x02",
    )

    CloseMessageWindow()
    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Ren got tired of crying and fell asleep.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_4D19")

    TalkEnd(0x14)
    Return()

    # Function_22_4BF5 end

    def Function_23_4D1D(): pass

    label("Function_23_4D1D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E6C")

    ChrTalk(
        0xFE,
        (
            "Together with Eolia,\x01",
            "Aftercare of the occupation case\x01",
            "I was hit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Arranged monsters that were out there\x01",
            "I was able to get rid of it, for the time being\x01",
            "It is a place I'd like to say safe ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "People in Mainz accepted\x01",
            "My heart's wounds seem to be considerable.\x01",
            "Many people are uneasy and can not sleep at night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Consulting Michelle,\x01",
            "Let's stay a little more\x01",
            "You should postpone it better.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_4F0C")

    label("loc_4E6C")


    ChrTalk(
        0xFE,
        (
            "People in Mainz accepted\x01",
            "My heart's wounds seem to be considerable.\x01",
            "Many people are uneasy and can not sleep at night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Consulting Michelle,\x01",
            "Let's stay a little more\x01",
            "You should postpone it better.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F0C")

    TalkEnd(0xFE)
    Return()

    # Function_23_4D1D end

    def Function_24_4F10(): pass

    label("Function_24_4F10")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FF2")

    ChrTalk(
        0xFE,
        (
            "Because of that raid incident,\x01",
            "Ursula hospital seems to have been full.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So, who can treat with Mainz\x01",
            "I am under contract as much as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's serious but … this kind of time\x01",
            "I have to share the roles properly.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_5076")

    label("loc_4FF2")


    ChrTalk(
        0xFE,
        (
            "Patients who can treat with Mainz\x01",
            "I am under contract as much as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "In such a case, taking a doctor's license\x01",
            "I think I was really good.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5076")

    TalkEnd(0xFE)
    Return()

    # Function_24_4F10 end

    def Function_25_507A(): pass

    label("Function_25_507A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5161")

    ChrTalk(
        0xFE,
        (
            "Today with my partner Wenzel\x01",
            "Take another action.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The holes where esters escaped\x01",
            "To cover it, like this\x01",
            "Anomalous shift is also increasing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although it suffers at the time of devils of monsters,\x01",
            "I have to manage it somehow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 3)
    Jump("loc_51F6")

    label("loc_5161")


    ChrTalk(
        0xFE,
        (
            "Today with my partner Wenzel\x01",
            "Take another action.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Although it suffers at the time of devils of monsters,\x01",
            "To cover lack of personnel\x01",
            "I have to manage it somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51F6")

    TalkEnd(0xFE)
    Return()

    # Function_25_507A end

    def Function_26_51FA(): pass

    label("Function_26_51FA")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(94170, 1500, 6300, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(34000, 0)
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
    FadeToBright(1000, 0)
    OP_0D()
    StopBGM(0xFA0)
    Sound(105, 0, 100, 0)
    OP_74(0x2, 0x1E)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0x5, 0x1, 0x8)
    Sleep(500)
    OP_68(93680, 1500, 1310, 3000)
    MoveCamera(41, 20, 0, 3000)
    OP_6E(260, 3000)
    SetCameraDistance(34000, 3000)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x101, 1, 0, 27)
    WaitChrThread(0x101, 1)
    Sleep(600)
    BeginChrThread(0x102, 1, 0, 27)
    WaitChrThread(0x102, 1)
    Sleep(600)
    BeginChrThread(0x103, 1, 0, 27)
    WaitChrThread(0x103, 1)
    Sleep(600)
    BeginChrThread(0x104, 1, 0, 27)
    WaitChrThread(0x104, 1)
    Sleep(600)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5342")
    BeginChrThread(0x109, 1, 0, 27)
    WaitChrThread(0x109, 1)
    Sleep(600)

    label("loc_5342")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_535F")
    BeginChrThread(0x105, 1, 0, 27)
    WaitChrThread(0x105, 1)
    Sleep(600)

    label("loc_535F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_537C")
    BeginChrThread(0x106, 1, 0, 27)
    WaitChrThread(0x106, 1)
    Sleep(600)

    label("loc_537C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5399")
    BeginChrThread(0x10A, 1, 0, 27)
    WaitChrThread(0x10A, 1)
    Sleep(600)

    label("loc_5399")

    OP_6F(0x79)
    Sleep(700)
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(20)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(20)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(20)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(20)
    OP_63(0x4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(20)
    OP_63(0x5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x11, 0x2)
    SetChrSubChip(0x12, 0x1)

    ChrTalk(
        0x11,
        "#12P#00805F#30WOh, Lloyd's guys …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#12P#00902F#30WHey … … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00005FEsther, Joshua! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#00102FDid you come here …?\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7568", 0)

    ChrTalk(
        0x104,
        (
            "#5P#00300FI heard that the decubitus doll\x01",
            "I heard that he skipped a spectacular thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#00202FAs expected, with Esther\x01",
            "It's \"Patel-Mattel\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#12P#00802F#30WHaha ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#12P#00903F#30W… Well, everything that I can win,\x01",
            "Thanks to the sacrifice of \"He\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00005FHuh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#00105FBy the way … is Len-chan?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x13,
        "Voice of an old man",
        "… … If it is Ren, I am asleep.\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(20)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(20)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(20)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(20)
    OP_63(0x4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(20)
    OP_63(0x5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(104580, 3500, 2720, 5000)
    MoveCamera(57, 16, 0, 5000)
    OP_6E(260, 5000)
    SetCameraDistance(34000, 5000)

    def lambda_5729():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_5729)
    Sleep(50)

    def lambda_5739():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_5739)
    Sleep(50)

    def lambda_5749():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_5749)
    Sleep(50)

    def lambda_5759():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_5759)
    Sleep(50)

    def lambda_5769():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_5769)
    Sleep(50)

    def lambda_5779():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x5, 1, lambda_5779)
    OP_6F(0x79)

    ChrTalk(
        0x14,
        "#11P#03317F#40W#2S…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FJorg Meister!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203F… … Were you having it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#11P#03903FWell … … Have their contacts.\x02\x03",
            "#03900FIt seems to be a serious thing to happen\x01",
            "If \"Patel-Mattel\" has passed\x01",
            "It can not be that we do not have a face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FThat doll passed away … …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305FOoi, maybe ……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(93680, 1500, 1310, 0)
    MoveCamera(41, 20, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(34000, 0)
    OP_93(0x0, 0xB4, 0x0)
    OP_93(0x1, 0xB4, 0x0)
    OP_93(0x2, 0xB4, 0x0)
    OP_93(0x3, 0xB4, 0x0)
    OP_93(0x4, 0xB4, 0x0)
    OP_93(0x5, 0xB4, 0x0)
    OP_70(0x2, 0x0)
    OP_0D()

    ChrTalk(
        0x11,
        (
            "#12P#00808F#30W……Yup……\x01",
            "Lift that Deckai doll\x01",
            "Carry it to the sky as it is … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#12P#00908F#30W……Maybe……\x01",
            "I guess you started the self-destruct system.\x02\x03",
            "#00903FEven at its own discretion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00003F……Is that so……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5P#00208FMachine makes such judgment ……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(107070, 3500, 4380, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(29150, 0)
    OP_0D()

    ChrTalk(
        0x14,
        (
            "#11P#03317F#2S#40W……… Gus …………\x01",
            "………… Patel-Mattel …………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305FDid you cry tired and slept asleep?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F… … It's not surprising …\x01",
            "My heart was in communication so much … …\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(104580, 3500, 2720, 0)
    MoveCamera(57, 16, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(34000, 0)
    OP_0D()

    ChrTalk(
        0x13,
        (
            "#11P#03903F…… About \"Patel = Mattel\"\x01",
            "There is only fate and give up.\x02\x03",
            "#03900FI, in order to protect this child\x01",
            "His \"heart\" who threw himself down\x01",
            "I want to respect it.\x02\x03",
            "It is said that it is exhausted as a puppeteer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FMeister……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(93680, 1500, 1310, 0)
    MoveCamera(41, 20, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(34000, 0)
    OP_0D()

    ChrTalk(
        0x11,
        (
            "#12P#00801F#30W── I heard the story.\x01",
            "Is it a serious thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#12P#00900F#30WAs we recover,\x01",
            "I'm planning to help you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00004FThank you, both of us.\x02\x03",
            "#00000FBut now that I can rest my body\x01",
            "Please give top priority.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00303FMy daughter is not her daughter … …\x02\x03",
            "#00300FFor now we are for the keebou\x01",
            "It is time you should do your best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#12P#00802F#30WI see……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#12P#00904F#30W…… Protecting the goddess.\x01",
            "Be careful.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7563", 0)
    SetChrSubChip(0x11, 0x0)
    SetChrSubChip(0x12, 0x0)
    SetChrPos(0x0, 94240, 0, 3400, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetMapObjFlags(0x2, 0x10)
    OP_1B(0x3, 0xFF, 0xFFFF)
    SetScenarioFlags(0x1CE, 2)
    EventEnd(0x5)
    Return()

    # Function_26_51FA end

    def Function_27_5E84(): pass

    label("Function_27_5E84")

    SetChrPos(0xFE, 94200, 0, 6500, 180)

    def lambda_5E9A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_5E9A)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5ECA")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 28)
    Jump("loc_5F6F")

    label("loc_5ECA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5EEE")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 29)
    Jump("loc_5F6F")

    label("loc_5EEE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F12")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 30)
    Jump("loc_5F6F")

    label("loc_5F12")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F36")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 31)
    Jump("loc_5F6F")

    label("loc_5F36")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F5A")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 32)
    Jump("loc_5F6F")

    label("loc_5F5A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F6F")
    BeginChrThread(0xFE, 2, 0, 33)

    label("loc_5F6F")

    Return()

    # Function_27_5E84 end

    def Function_28_5F70(): pass

    label("Function_28_5F70")

    OP_95(0xFE, 94200, 0, 3030, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_28_5F70 end

    def Function_29_5F8C(): pass

    label("Function_29_5F8C")

    OP_95(0xFE, 94200, 0, 4850, 2000, 0x0)
    OP_95(0xFE, 93110, 0, 3070, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_29_5F8C end

    def Function_30_5FBC(): pass

    label("Function_30_5FBC")

    OP_95(0xFE, 94200, 0, 4850, 2000, 0x0)
    OP_95(0xFE, 95280, 0, 3120, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_30_5FBC end

    def Function_31_5FEC(): pass

    label("Function_31_5FEC")

    OP_95(0xFE, 94210, 0, 4150, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_31_5FEC end

    def Function_32_6008(): pass

    label("Function_32_6008")

    OP_95(0xFE, 94260, 0, 5260, 2000, 0x0)
    OP_95(0xFE, 93580, 0, 4960, 2000, 0x0)
    OP_95(0xFE, 93270, 0, 4310, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_32_6008 end

    def Function_33_604C(): pass

    label("Function_33_604C")

    OP_95(0xFE, 94260, 0, 5260, 2000, 0x0)
    OP_95(0xFE, 95020, 0, 4960, 2000, 0x0)
    OP_95(0xFE, 95250, 0, 4350, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_33_604C end

    def Function_34_6090(): pass

    label("Function_34_6090")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch32600.itc", 0x1E)
    LoadChrToIndex("chr/ch06000.itc", 0x1F)
    LoadChrToIndex("chr/ch02702.itc", 0x20)
    SetChrChipByIndex(0x10, 0x1E)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x18, 0x1F)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    SetMapObjFlags(0x4, 0x4)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrSubChip(0x107, 0x5)
    SetChrPos(0x101, 101200, 2000, 1500, 90)
    SetChrPos(0x107, 100150, 2000, 3100, 135)
    SetChrPos(0x105, 101400, 2000, 600, 90)
    SetChrPos(0x106, 103700, 2000, 3500, 180)
    SetChrPos(0x103, 101790, 2000, 2800, 135)
    SetChrChipByIndex(0x107, 0x20)
    BeginChrThread(0x107, 3, 0, 0)
    SetChrPos(0x104, 104400, 2000, 1300, 270)
    SetChrPos(0x10, 104250, 2000, 100, 270)
    SetChrPos(0x18, 105000, 2000, 2950, 225)
    OP_68(102370, 3400, 1380, 0)
    MoveCamera(59, 15, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(33500, 0)
    SetCameraDistance(35500, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x104,
        (
            "#00306F#11P─ ─ I see.\x01",
            "Absolutely nothing\x01",
            "It seems to be a story.\x02\x03",
            "#00301FAnd KeA…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#02106F#5PWell, crazy is too little\x01",
            "I feel like I can not write in articles ….\x02\x03",
            "#02101FLloyd's guys at all\x01",
            "You're gonna regain her, are not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#6PYes. Of course\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203F#6PYou don't even have to ask\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00308F#11P…\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x104, 500)
    Sleep(100)

    ChrTalk(
        0x10,
        (
            "#07904F#11P…… Randy.\x01",
            "we#6Rresistance#You are fine.\x02\x03",
            "#07902FOriginally, the companions of the support department\x01",
            "On the condition of rescuing\x01",
            "You lent the power, were not you?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x10, 500)

    ChrTalk(
        0x104,
        "#00305F#5PNo but \x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6PI see…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#6P…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#6PWell, as here\x01",
            "If you can join you\x01",
            "It certainly will be saved, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#07904F#11POriginally, our resistance activity\x01",
            "I could not convince the Defense Forces\x01",
            "It is a nuisance as a security guard.\x02\x03",
            "#07902FYou are away from the guard\x01",
            "We should be the power of our colleagues.\x02\x03",
            "#07909FFrom now on, those wolves also\x01",
            "It seems to be a power.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01203F#6P#3CWell, it seems like to cooperate with the new year\x01",
            "I told you again.\x02\x03",
            "#01200FIf it is a battle at a mountain area\x01",
            "It will be powerful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#5PSorry. That helps\x02",
    )

    CloseMessageWindow()

    def lambda_6609():
        OP_93(0x104, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6609)
    Sleep(50)

    def lambda_6619():
        OP_93(0x10, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_6619)
    Sleep(50)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x10, 0)

    ChrTalk(
        0x104,
        (
            "#00300F#11PLloyd, Tio Sukei.\x01",
            "Let me get involved too!\x02\x03",
            "As a member of the support department,\x01",
            "As a guardian of the keeb!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#6PYeah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204F#6PThank goodness…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10709F#5PEhe, that makes me feel better\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#02103F#5PHmm. In that case\x02\x03",
            "#02102FI also to you\x01",
            "Would you let me accompany you?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_67F4():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_67F4)
    Sleep(50)

    def lambda_6804():
        TurnDirection(0x103, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_6804)
    Sleep(50)

    def lambda_6814():
        TurnDirection(0x104, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6814)
    Sleep(50)

    def lambda_6824():
        TurnDirection(0x105, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_6824)
    Sleep(50)

    def lambda_6834():
        TurnDirection(0x106, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_6834)
    Sleep(50)

    def lambda_6844():
        TurnDirection(0x10, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_6844)
    Sleep(50)

    def lambda_6854():
        TurnDirection(0x107, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_6854)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x10, 0)
    WaitChrThread(0x107, 0)
    SetChrSubChip(0x107, 0x5)

    ChrTalk(
        0x101,
        "#00011F#6PHuh!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00211F#6PWhat are you saying now\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#02104F#5PBecause the center of the future movement\x01",
            "You are going to be you.\x02\x03",
            "#02110FAs a journalist\x01",
            "You can not miss it for a moment!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F#6PNo but \x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#6PHmm. I don't really mind but\x02\x03",
            "#10400FIf you put the mass media people\x01",
            "Abbas would be noisy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10706F#6P…… If I also get an article\x01",
            "I am in trouble for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#02105F#5POh don't worry\x02\x03",
            "#02104FI want to post articles in the mountains\x01",
            "Now that's not the situation.\x02\x03",
            "#02106FI am cross-border independent country\x01",
            "I just want to know what will happen.\x02\x03",
            "#02101FThis deceitful new regime\x01",
            "Will it be chosen as history?#18R噵 噵 噵 噵 噵 噵 噵 噵 噵#That's it.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x106, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#6PChosen by history?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#02103F#5PI have to say like this,\x01",
            "The turmoil throughout the continent is pretty.\x02\x03",
            "One reason is that President Dieter\x01",
            "I can not deny that there is something … …\x02\x03",
            "#02101FHe retires#2RA number#Just because it was,\x01",
            "Can this crisis be overcome?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00011F#6PThat is\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#07906F#12PTo be honest …\x01",
            "It may be difficult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#02106F#5PIndeed, 100 years ago Calvado\x01",
            "Even when democratizing, by the revolutionary government\x01",
            "It seems that there was a considerable ingenious thing done.\x02\x03",
            "#02103FAssassination or something is natural.\x01",
            "In addition to the attack on Cross Bell City\x01",
            "There seemed to be a similar conspiracy play nearly.\x02\x03",
            "#02101FHowever,\x01",
            "It has been justified to some extent.\x02\x03",
            "Even President Dieter did\x01",
            "Can I say the same thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6P….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10708F#6P(The assassination play of 100 years ago)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#02106F#5PThat said, even though this situation\x01",
            "I do not think that it is right.\x02\x03",
            "#02100FSo that's what I want to confirm\x02\x03",
            "From now on, crossbell\x01",
            "What kind of road will you choose?\x02\x03",
            "And,\x01",
            "How can we communicate to history?\x02\x03",
            "#02109FIf you follow along with you\x01",
            "I feel like I can see it ~ ne ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6PGrace…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F#12PWhat is it?\x01",
            "I never thought he was thinking so far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202F#6PSomewhat serious too\x01",
            "It looks like a different person, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#02109F#5PHaha, well the best reason\x01",
            "It seems interesting, but.\x02\x03",
            "#02110FAnd to the correspondent\x01",
            "I left the pipe.\x02\x03",
            "Perhaps the information in the city\x01",
            "You may be able to offer it?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00004F#6P─ ─ All right.\x01",
            "We do not have a dispute.\x02\x03",
            "#00000FWasi, Lisha.\x01",
            "Is that OK?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10710F#6PI……\x01",
            "If you do not write it as an article.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#6PAha, I don't mind either\x02\x03",
            "#10402FWell persuade Abbas\x01",
            "It may be a hard time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#02109F#5PThanks! You won't regret it\x02\x03",
            "#02110FOkay, let's put in a spirit with everyone\x01",
            "Let's aim for the Fuerzza Prize!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x10, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00012F#6PNo, Mr. Grace's\x01",
            "I will help you …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00211F#6PWell it is Grace\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(37500, 2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "After that, Lloyd's\x01",
            "Cooperate secretly with resistance\x01",
            "After greeting a mayor of Mainz in Vixen … …\x02\x03",
            "After talking about future arrangements\x01",
            "Base in the mountain area#4Rbase#Back to the Mireille\x01",
            "It was to say good-by.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x22, 5)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_34_6090 end

    def Function_35_74D7(): pass

    label("Function_35_74D7")

    EventBegin(0x0)
    Fade(500)
    OP_68(2960, 1500, 1030, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(30500, 0)
    SetChrPos(0x101, 3100, 0, 2000, 0)
    SetChrPos(0x102, 4300, 0, 2000, 0)
    SetChrPos(0x103, 3100, 0, 800, 0)
    SetChrPos(0x109, 4300, 0, 800, 0)
    SetChrPos(0x104, 3100, 0, -400, 0)
    SetChrPos(0x105, 4300, 0, -400, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "Well come.\x01",
            "You often came to \"Red Brick Tea\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FExcuse me,\x01",
            "I am a person in the mission support department … …\x02",
        )
    )

    CloseMessageWindow()
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
        0x8,
        (
            "Oh, were you.\x01",
            "I heard a story from a communications company.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well then, specialties from the mining town\x01",
            "\"Stamina Steak\"\x01",
            "I will burn it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F…… Dosun in the stomach\x01",
            "It seems to be stagnant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Oh, you do a lot\x01",
            "I have to go eat and eat\x01",
            "Is not it OK?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well then\x01",
            "Cut it into a bite size\x01",
            "Would you like to bring it with you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FHehe, thank you.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    FadeToBright(1000, 0)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyds ate stamina steak.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00309FMunching …\x01",
            "Well, even if you have a bite size\x01",
            "It is quite easy to eat.\x02\x03",
            "#00304FAfter all if you steak\x01",
            "This is not it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102FYeah, how powerful is it\x01",
            "It seems to spring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Huhu, mine guys\x01",
            "Because physical fitness is life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "There is a beer with this guy,\x01",
            "That's like a horse carriage\x01",
            "Dimensions to work.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x105,
        (
            "#10306FAs I thought, the miners\x01",
            "It sounds like a tough job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, Mr. Ganz\x01",
            "It looks like I'm enjoying it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Huff, in the mining town\x01",
            "That's why it is a mighty man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Also,\x01",
            "When you want to eat Gatszuri\x01",
            "You are coming to Uchi again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FOh, let me do so.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x2, 0)
    SetScenarioFlags(0x173, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_7B13")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7B13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_7B30")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7B30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_7B43")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7B43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_7B56")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7B56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_7B73")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7B73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_7B86")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7B86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_7BA3")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7BA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_7BB6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7BB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_7BD3")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7BD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_7BE6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7BE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_7C03")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7C03")

    OP_29(0x80, 0x1, 0x8)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D0C")
    SetChrName("")
    Sound(17, 0, 100, 0)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7D03")

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

    label("loc_7D03")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_7D0C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7DDD")
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

    label("loc_7DDD")

    OP_4C(0x8, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 3700, 0, 2090, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_35_74D7 end

    def Function_36_7E0D(): pass

    label("Function_36_7E0D")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(3290, 1500, 1670, 0)
    MoveCamera(52, 28, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(33630, 0)
    SetChrPos(0x101, 3250, 0, 1590, 0)
    SetChrPos(0x102, 4210, 0, 1500, 0)
    SetChrPos(0x103, 2730, 0, 570, 0)
    SetChrPos(0x109, 2780, 0, -510, 0)
    SetChrPos(0x104, 3820, 0, 430, 0)
    SetChrPos(0x105, 4200, 0, -450, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#3PHello, It's usual\x01",
            "You are a police boy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PFor today we stayed\x01",
            "Did you come over?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FUh, a little\x01",
            "What you want to ask\x01",
            "I was there ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FRecently, here\x01",
            "I do not remember my baggage\x01",
            "Did not you receive it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3PLuggage I do not memorize ……?\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#3POh, remember that.\x01",
            "It certainly arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PWhy is such a Mong again\x01",
            "I heard it arrived … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PYou guys,\x01",
            "Do you know anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FIt looks like hit.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FEr, actually …\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd's luggage misallocation\x01",
            "I explained that there was.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#3PHahaan,\x01",
            "Was that something like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PWhat is that baggage?\x01",
            "To Ursula Hospital\x01",
            "It was a luggage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PReasoning, female and something something\x01",
            "It is a momentary incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FIf such a thing suddenly arrives\x01",
            "It's pretty creepy, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3PThat 's awfully bad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PLucca something disgusting,\x01",
            "Trying to put it out for garbage even tomorrow\x01",
            "I did it for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106FWell, that was a long time …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOriginally delivered to here\x01",
            "I also keep luggage that was supposed to be.\x01",
            "Please accept it.\x02",
        )
    )

    CloseMessageWindow()
    OP_97(0x101, 0x0, 0x0, 0x1F4, 0x3E8, 0x0)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '易碎品的小包裹'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            ".\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber('易碎品的小包裹', 1)

    ChrTalk(
        0x8,
        (
            "#3POh, thanks.\x01",
            "let's see……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3P……Ah,\x01",
            "I ordered it a while ago.\x01",
            "It is a glass made by Libert.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PCertainly the luggage addressed to us\x01",
            "Looks like it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309FThat was good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FWell then, that baggage is\x01",
            "Can you take me over?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PI broke up.\x01",
            "Please wait a moment.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x0, 0x1F4)
    OP_95(0x8, 3700, 0, 6080, 2000, 0x0)
    OP_0D()
    Sleep(1000)
    OP_93(0x8, 0xB4, 0x1F4)
    OP_95(0x8, 3700, 0, 4290, 2000, 0x0)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#3PThis is the package that arrived.\x01",
            "I will ask you afterwards.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '沉重货物'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('沉重货物', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00004FThank you very much.\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00000F…… OK, next\x01",
            "Let's face Ursula hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FAs I listened to the circumstances at the reception\x01",
            "It might be nice.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x175, 6)
    OP_29(0x85, 0x1, 0x1)
    OP_4C(0x8, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 3700, 0, 2090, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_36_7E0D end

    def Function_37_861F(): pass

    label("Function_37_861F")

    EventBegin(0x0)
    Fade(500)
    OP_68(103580, 3500, 1840, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(34000, 0)
    SetChrPos(0x101, 104410, 2000, 2730, 180)
    SetChrPos(0x102, 105590, 2000, 2850, 225)
    SetChrPos(0x103, 103990, 2000, 3850, 180)
    SetChrPos(0x109, 105160, 2000, 3900, 180)
    SetChrPos(0x104, 104700, 2000, 5020, 180)
    SetChrPos(0x105, 103250, 2000, 4800, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    ChrTalk(
        0x101,
        "#00005FMr. Nielsen -\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x101, 0)
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8794")
    Jump("loc_87DE")

    label("loc_8794")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_87B4")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_87DE")

    label("loc_87B4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_87D4")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_87DE")

    label("loc_87D4")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_87DE")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)

    ChrTalk(
        0xE,
        "Hmm, that voice is Mr. Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FWell, it is an honor to be able to remember.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Huhu, let me interview once\x01",
            "Because it is the voice of the person who got it.\x01",
            "It can not be forgotten.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F(Maybe this person ……)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300F(Oh, before Lloyd's\x01",
            "I got an interview,\x01",
            "A famous journalist? )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100F(Yes, Mr. Nielsen.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FUm, how come today again\x01",
            "To Mainz?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Yeah, in fact to the mayor here\x01",
            "I am planning to interview you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "History of the seven ix and stone mining of this town\x01",
            "Regarding the transition in modern times,\x01",
            "I am planning to tell you a story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "The question of independence is questioned\x01",
            "Because now it is again in the history of autonomous state\x01",
            "I thought about focusing on it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10304FWell, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FSomehow,\x01",
            "The eyes are different.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Haha, thanks always\x01",
            "I am only taking a long way around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "By the way, everyone at the previous trade meeting\x01",
            "They contributed to the capture of terrorists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "…… Hmm, that's right.\x01",
            "If it's okay again, to my interview\x01",
            "Could you please go out with me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "To the terrorist case in the trade meeting\x01",
            "What was the meaning of the meaning?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "By letting you talk with everyone,\x01",
            "I think there is something to see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105F\"Meaning\" of terrorism incident ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208FBut it is …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, how rude\x01",
            "This case is the autonomous state government and the police\x01",
            "It involves confidentiality.\x02\x03",
            "To talk to us is\x01",
            "I think that it will be limited …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Of course, that is defying.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Still, the significance of speaking\x01",
            "I think there will be sure … …\x01",
            "What do you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI agree……\x02\x03",
            "(To be sure, the previous interview was\x01",
            "It was also useful for us. )\x02\x03",
            "#00008F(If you have time, receive it\x01",
            "It seems better to have him … …)\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 38)
    Return()

    # Function_37_861F end

    def Function_38_8DEB(): pass

    label("Function_38_8DEB")

    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Cooperate with Nielsen's coverage\x01",      # 0
            "To give up\x01",                      # 1
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
        (0, "loc_8E61"),
        (1, "loc_8F4B"),
        (SWITCH_DEFAULT, "loc_9037"),
    )


    label("loc_8E61")


    ChrTalk(
        0x101,
        (
            "#00000FI understand.\x01",
            "I will accept stories about coverage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Thank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Let's start talking at once.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest 【Interview coverage on terrorist incidents】\x07\x00",
            "I started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x89, 0x4, 0x2)
    Call(0, 40)
    Jump("loc_9037")

    label("loc_8F4B")


    ChrTalk(
        0x101,
        (
            "#00006FExcuse me.\x01",
            "Now I can not take the time ……\x02\x03",
            "Is it fine whether I ask you again later?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Well, I do not mind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Then, if convenient,\x01",
            "Please call out anytime.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0x0)
    OP_69(0xFF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_902F")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 104410, 2000, 2730, 180)
    EventEnd(0x5)

    label("loc_902F")

    SetScenarioFlags(0x177, 7)
    Jump("loc_9037")

    label("loc_9037")

    Return()

    # Function_38_8DEB end

    def Function_39_9038(): pass

    label("Function_39_9038")

    TalkBegin(0xE)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_90CC")
    Jump("loc_9116")

    label("loc_90CC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_90EC")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9116")

    label("loc_90EC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_910C")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9116")

    label("loc_910C")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9116")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)

    ChrTalk(
        0xE,
        "…… Mr. Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Interview on terrorist incidents,\x01",
            "Could you go out with me?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Call(0, 38)
    TalkEnd(0xE)
    Return()

    # Function_39_9038 end

    def Function_40_9194(): pass

    label("Function_40_9194")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    WaitBGM()
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x1)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrSubChip(0xE, 0x0)
    OP_68(102190, 3600, 1510, 0)
    MoveCamera(49, 21, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(32220, 0)
    SetChrPos(0x101, 102650, 2150, 3330, 180)
    SetChrPos(0x102, 101250, 2150, 1740, 90)
    SetChrPos(0x103, 102610, 2150, -110, 0)
    SetChrPos(0x109, 103400, 2000, 4800, 180)
    SetChrPos(0x104, 102060, 2000, 4800, 180)
    SetChrPos(0x105, 100750, 2000, 3680, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xE,
        (
            "#11PPlease get in touch with the interview,\x01",
            "thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PThis time,\x01",
            "It occurred during the previous trade meeting\x01",
            "It is about the terrorist incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PFirst of all as a premise,\x01",
            "About the terrorist group that is the criminal\x01",
            "I'd like to confirm ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#11PMr. Lloyd, you know well?\x02",
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
            "#1KWhat is a terrorist group aimed at a trade meeting?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Empire of the Eleventh Empire Liberation Front\x01",          # 0
            "Immigration policy opponents of the Republic of Calvert\x01",      # 1
            "Both\x01",                              # 2
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
        (0, "loc_947F"),
        (1, "loc_9548"),
        (2, "loc_9611"),
        (SWITCH_DEFAULT, "loc_96EE"),
    )


    label("loc_947F")


    ChrTalk(
        0x101,
        (
            "#00001F#5PYeah, the Eleven Empire\x01",
            "It is \"Empire Liberation Front\".\x02\x03",
            "#00011F(- Well,\x01",
            "That's not all, right? )\x02\x03",
            "#00003FIn addition, in the Republic of Calvert\x01",
            "Immigrant policy opposition -\x01",
            "It is a part of \"anti-immigration policyism\".\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_96EE")

    label("loc_9548")


    ChrTalk(
        0x101,
        (
            "#00001F#5PYeah, the Republic of Calvert\x01",
            "Immigrant policy opposition -\x01",
            "It is a part of \"anti-immigration policyism\".\x02\x03",
            "#00011F(- Well,\x01",
            "That's not all, right? )\x02\x03",
            "#00003FIn addition, the Eleven Empire\x01",
            "It is \"Empire liberation front\".\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_96EE")

    label("loc_9611")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00006F#5PYeah, the culprit is in two major powers\x01",
            "Terrorist groups that exist respectively -\x02\x03",
            "#00008FOne of the Eleven Empire\x01",
            "\"Empire Liberation Front\" -\x02\x03",
            "#00013FThe other is the Republic of Calvert\x01",
            "Immigrant policy opposition -\x01",
            "It is a part of \"anti-immigration policyism\".\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_96EE")

    label("loc_96EE")


    ChrTalk(
        0xE,
        "#11PYes, they are the two of them.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PRegarding their background and principle of assertiveness,\x01",
            "I will not mention it on this occasion … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PThe point here is that,\x01",
            "Both fighters with no normal contact point\x01",
            "Is that stretched?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PIn the rumor, once danced in Libert\x01",
            "Organization called \"snake snake\"\x01",
            "It is said that they were cooperating, but … …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00013F#5PSociety \"snake snake\" ……\x02\x03",
            "#00008FBy the way, at a trade meeting\x01",
            "Terrorists put puppet weapons\x01",
            "I was using it. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#6PMr. Nielsen said,\x01",
            "You know \"association\" is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PYeah, that kind of mysterious organization\x01",
            "To the extent that it certainly exists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PBut after all\x01",
            "You seem to have known.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#5PWell, it's just a bit of a thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211F#6PThe more I know it\x01",
            "There is only increasing disgusting odor … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11P…… Anyway\x01",
            "It is unknown what is moving for what purpose\x01",
            "It seems to be certainly a mysterious group.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PAbout that intention\x01",
            "I can not infer at this moment\x01",
            "It would be better if you put it on hold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#5PCertainly, that looks good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#11PLet's go ahead with the story.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PWhat I would like to check next -\x01",
            "In this terrorist incident,\x01",
            "It is the intention and position of the two major powers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PAccording to sources, the two countries are in advance\x01",
            "Secretly prepared an external production unit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PIts existence is to settle the terrorist case\x01",
            "Although it is said that it made a big contribution -\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PWhile grasping the movement of terrorism,\x01",
            "This behavior that you can also say that you dare swim.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PWhat was the purpose of the two leaders -\x01",
            "What do you think Mr. Lloyd thinks?\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x1, 1)
    ClearScenarioFlags(0x1, 2)
    ClearScenarioFlags(0x1, 3)

    label("loc_9CDC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A08C")
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
            "#1KIn the terrorist case, with Prime Minister Osborne\x01",
            "What is the aim of President Rock Smith?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Broadcasting of terrorist groups\x01",        # 0
            "Check on domestic opponents\x01",      # 1
            "Retirement of Mayor Dieter\x01",      # 2
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
        (0, "loc_9DC9"),
        (1, "loc_9E75"),
        (2, "loc_9FAF"),
        (SWITCH_DEFAULT, "loc_A079"),
    )


    label("loc_9DC9")


    ChrTalk(
        0x101,
        (
            "#00005F#5P(Well, if you have a terrorist group\x01",
            "The aim of roasting … ….? )\x02\x03",
            "#00006F(… … no, different, in the first place\x01",
            "The actual situation of terrorists in both countries\x01",
            "It should be grasping as it is. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_A079")

    label("loc_9E75")


    ChrTalk(
        0x101,
        (
            "#00003F#5PIt is the side that released terrorists\x01",
            "Opponents to the current administration -\x02\x03",
            "The check on them\x01",
            "I think that the aims of the two leaders.\x02\x03",
            "#00008FTo the Osborne president,\x01",
            "Check against hostile aristocratic factions.\x02\x03",
            "#00001FFor President Rock Smith,\x01",
            "Suppression of domestic disturbing molecules\x01",
            "Is not it the primary objective?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9FA7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9FA7")

    SetScenarioFlags(0x1, 1)
    Jump("loc_A079")

    label("loc_9FAF")


    ChrTalk(
        0x101,
        (
            "#00008F#5P(It was proved again in the terrorist case\x01",
            "Lack of security in Autonomous State. )\x02\x03",
            "(By pursuing it\x01",
            "To the request of retirement to Mayor Dieter … ….)\x02\x03",
            "#00011F(No no, this is\x01",
            "It's not about that scale. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_A079")

    label("loc_A079")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_A087")
    Jump("loc_A08C")

    label("loc_A087")

    Jump("loc_9CDC")

    label("loc_A08C")


    ChrTalk(
        0xE,
        (
            "#11PHmm, that's right.\x01",
            "Certainly that\x01",
            "It is considered to be the maximum aim.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PActually, in both countries since the incident,\x01",
            "Voices of accusations against those forces are also\x01",
            "It seems that it is increasing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#6PIndeed, a formidable in political fighting\x01",
            "Is it an attack material?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PBy the way Lloyd is\x01",
            "I mentioned that it was the primary object … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PIf it's okay, as for other aims\x01",
            "Could you please?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#5Pthat is……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)

    ChrTalk(
        0x102,
        "#00108F#6PLloyd …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10108F#5P….\x02",
    )

    CloseMessageWindow()
    OP_64(0x101)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00006F#5PAnother big aim -\x02\x03",
            "#00013FIt's a foothold in advancing to Crosbell\x01",
            "I think that it is for building in earnest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#11PHM……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F#6PCrossbell Advancement -\x02\x03",
            "#10301FThe easiest thing is,\x01",
            "Proposed by both countries at the trade meeting\x01",
            "It is a guy who holds the military.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#6PIt was proved again in the terrorist case\x01",
            "Crossbell security lack -\x02\x03",
            "#00201FTo solve it\x01",
            "That was a necessary proposal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#6PYeah, by that\x01",
            "The \"non-war treaty\" concluded with Libert\x01",
            "I lost a deterrent greatly …\x02\x03",
            "#00108FIncluding further independent advocacy\x01",
            "The public opinion of the two major powers now is crossbell\x01",
            "I have great interest.\x02\x03",
            "#00101FAs a result, domestic conflict and discontent\x01",
            "It seems that it also led to diverting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F#6PThe aim is to such a place ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#5PHaa, what on earth?\x01",
            "It is a stone what a bird.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11P…… Hmm, everyone is\x01",
            "It seems that it is considered quite deeply.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11P- Then, around here\x01",
            "Let's shift to the last point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PEven from the situation, this case\x01",
            "There is agreement between the two countries\x01",
            "Although it can be said that it was obvious … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PThis is an alliance relationship between the two countries\x01",
            "Is it a meaning?\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x1, 1)
    ClearScenarioFlags(0x1, 2)
    ClearScenarioFlags(0x1, 3)

    label("loc_A684")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A8FE")
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
            "#1KThrough dealing with terrorist incidents,\x01",
            "Did the Empire and the Republic establish an alliance?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Temporarily tied\x01",      # 0
            "It tied permanently\x01",      # 1
            "impossible\x01",          # 2
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
        (0, "loc_A759"),
        (1, "loc_A7CC"),
        (2, "loc_A84F"),
        (SWITCH_DEFAULT, "loc_A8EB"),
    )


    label("loc_A759")


    ChrTalk(
        0x101,
        (
            "#00008F#5P(Temporarily ……\x01",
            "Can you think? )\x02\x03",
            "#00003F(No, like that\x01",
            "It can not be a simple story. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_A8EB")

    label("loc_A7CC")


    ChrTalk(
        0x101,
        (
            "#00005F#5P(No doubt, with this\x01",
            "Permanent alliance -)\x02\x03",
            "#00006F(- It is stupid.\x01",
            "There can not be such a thing. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_A8EB")

    label("loc_A84F")


    ChrTalk(
        0x101,
        (
            "#5P#00003FHouse……\x01",
            "I think that is impossible.\x02\x03",
            "#00013F─ ─ The ultimate goal of both is\x01",
            "Crossbell will be the sole rule.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A8E3")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A8E3")

    SetScenarioFlags(0x1, 1)
    Jump("loc_A8EB")

    label("loc_A8EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_A8F9")
    Jump("loc_A8FE")

    label("loc_A8F9")

    Jump("loc_A684")

    label("loc_A8FE")


    ChrTalk(
        0xE,
        "#11PYeah - That's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PThis case is temporarily temporary\x01",
            "I guess I just arranged my steps.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PCrossbell\x01",
            "Buff-over area with too much power -\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PSuch a unique and important place\x01",
            "Which one can fit in hand,\x01",
            "Include such confirmation implicitly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10113F#5Pthat is……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#6P….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00211F#6P…… It is too blatant.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#6PBefore we got to know each other\x01",
            "It's preliminary preparation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PYeah ─ ─ In the future\x01",
            "The intelligence warfare between the two countries is increasingly\x01",
            "It is also possible to intensify.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PIn such a situation\x01",
            "Movement of criminal organizations and hunting corps\x01",
            "It will also lead to activation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PThen, in the past frequently\x01",
            "The incomprehensible accident that occurred again\x01",
            "It may reveal its appearance ──\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x104,
        "#00305F#5PInexplicable accident … ….?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F#6PWhat does that mean ……\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)

    ChrTalk(
        0xE,
        (
            "#11PNo. No thing to do\x01",
            "You seem to have told me.\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7121", 0)
    Sleep(1000)

    ChrTalk(
        0xE,
        (
            "#11PI was able to organize variously,\x01",
            "I got a meaningful story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#11PI really appreciate your cooperation.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F#5P… Well, this is it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F#6PWe also have Oita,\x01",
            "I feel I was able to organize the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106F#5P…… I learned a lot.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#11PIf you can say so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PIf there is another opportunity,\x01",
            "Please tell me the story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#5PYes, at that time, come on.\x02",
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
            "Quest 【Interview coverage on terrorist incidents】\x07\x00",
            "Achieved!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x103, 0x4)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 104500, 2000, 3740, 180)
    OP_69(0xFF, 0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AEE5")
    OP_2C(0x89, 0x2)
    Jump("loc_AEF9")

    label("loc_AEE5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AEF9")
    OP_2C(0x89, 0x1)

    label("loc_AEF9")

    OP_29(0x89, 0x1, 0x0)
    OP_29(0x89, 0x4, 0x10)
    EventEnd(0x5)
    Return()

    # Function_40_9194 end

    SaveToFile()

Try(main)
