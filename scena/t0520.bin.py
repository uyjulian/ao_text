from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Norma",                  # 1
        "Lycka",                  # 2
        "Carlos",                 # 3
        "Mine Captain Hoffman",   # 4
        "Miner Gantz",            # 5
        "Miner Max",              # 6
        "Nielsen",                # 7
        "Miner Marlow",           # 8
        "2nd Lt. Mireille",       # 9
        "Estelle",                # 10
        "Joshua",                 # 11
        "Meister Jｶrg",          # 12
        "Renne",                  # 13
        "Bracer Ling",            # 14
        "Bracer Eolia",           # 15
        "Bracer Scott",           # 16
        "Grace",                  # 17
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
        "Function_5_915",          # 05, 5
        "Function_6_919",          # 06, 6
        "Function_7_1D28",         # 07, 7
        "Function_8_2C87",         # 08, 8
        "Function_9_2DC7",         # 09, 9
        "Function_10_2F9A",        # 0A, 10
        "Function_11_30A3",        # 0B, 11
        "Function_12_31F1",        # 0C, 12
        "Function_13_33AC",        # 0D, 13
        "Function_14_3534",        # 0E, 14
        "Function_15_35E7",        # 0F, 15
        "Function_16_3E15",        # 10, 16
        "Function_17_3F52",        # 11, 17
        "Function_18_45C5",        # 12, 18
        "Function_19_49AD",        # 13, 19
        "Function_20_4EFB",        # 14, 20
        "Function_21_50D6",        # 15, 21
        "Function_22_50DA",        # 16, 22
        "Function_23_51DA",        # 17, 23
        "Function_24_5462",        # 18, 24
        "Function_25_5635",        # 19, 25
        "Function_26_57D9",        # 1A, 26
        "Function_27_64CB",        # 1B, 27
        "Function_28_65B7",        # 1C, 28
        "Function_29_65D3",        # 1D, 29
        "Function_30_6603",        # 1E, 30
        "Function_31_6633",        # 1F, 31
        "Function_32_664F",        # 20, 32
        "Function_33_6693",        # 21, 33
        "Function_34_66D7",        # 22, 34
        "Function_35_7C79",        # 23, 35
        "Function_36_8631",        # 24, 36
        "Function_37_8E59",        # 25, 37
        "Function_38_96D5",        # 26, 38
        "Function_39_9921",        # 27, 39
        "Function_40_9A89",        # 28, 40
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
            "★Der Ziegel Inn Recommended Recipe★\x01",
            "　　 ～It's just regular\x01",
            "　　　    fried fish, though～\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The Fried Fish recipe is written down.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_911")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_911")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "You learned the "Fried Fish"\x07\x00",
            " recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_911")

    TalkEnd(0xFF)
    Return()

    # Function_4_7F2 end

    def Function_5_915(): pass

    label("Function_5_915")

    Call(0, 6)
    Return()

    # Function_5_915 end

    def Function_6_919(): pass

    label("Function_6_919")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_947")
    Call(0, 35)
    Return()

    label("loc_947")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x175, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x175, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_970")
    Call(0, 36)
    Return()

    label("loc_970")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_97D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D24")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",      # 0
            "Shop\x01",      # 1
            "Rest\x01",      # 2
            "Quit\x01",      # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9DC")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_9DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9FC")
    OP_AF(0x52)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1D1F")

    label("loc_9FC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A1C")
    OP_AF(0x50)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1D1F")

    label("loc_A1C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A30")
    Jump("loc_1D1F")

    label("loc_A30")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A48")
    TalkEnd(0x8)
    Return()

    label("loc_A48")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D1F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_B13")

    ChrTalk(
        0x8,
        (
            "Uh uh, if you eat our steak\x01",
            "special, you'll feel a surge of\x01",
            "energy within you immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Everyone, please come\x01",
            "here whenever you want\x01",
            "to eat your fill.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D1F")

    label("loc_B13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_CE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C1E")

    ChrTalk(
        0x8,
        (
            "After the disturbance in the city, \x01",
            "some exhausted Bracers and\x01",
            "a crying girl came here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It seems they participated in the\x01",
            "Crossbell City liberation operation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We, who cooperated\x01",
            "with the Resistance,\x01",
            "would like to thank them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CE1")

    label("loc_C1E")


    ChrTalk(
        0x8,
        (
            "It seems the Bracers resting below\x01",
            "participated in the Crossbell City\x01",
            "liberation operation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "A different Bracer came earlier\x01",
            "and helped us defeat monsters...\x01",
            "We're really in their debt.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CE1")

    Jump("loc_1D1F")

    label("loc_CE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_E12")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DA7")

    ChrTalk(
        0x8,
        (
            "Miss Mireille, the Resistance\x01",
            "leader, is here to resupply.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You guys are doing a big\x01",
            "operation before long, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We're rooting for you.\x01",
            "Do your best.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E0D")

    label("loc_DA7")


    ChrTalk(
        0x8,
        (
            "You guys are doing a big\x01",
            "operation before long, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We're rooting for you.\x01",
            "Do your best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E0D")

    Jump("loc_1D1F")

    label("loc_E12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_10DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F41")
    TurnDirection(0x8, 0x104, 0)

    ChrTalk(
        0x8,
        (
            "Randy, you've separated\x01",
            "from the Resistance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FYeah. A certain beloved daughter\x01",
            "I have to save is waitin' for me.\x02\x03",
            "#00302FLady, take care of the people\x01",
            "of Mainz, Mireille and the\x01",
            "others for me for awhile.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ha ha, understood.\x01",
            "You be careful yourself.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AD, 7)
    Jump("loc_10DA")

    label("loc_F41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1067")

    ChrTalk(
        0x8,
        (
            "We told the guys of the Resistance\x01",
            "about good hiding spots in the\x01",
            "mountains and helped them resupply...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "When the State Guard come\x01",
            "looking, we pretend not to know\x01",
            "them, because they're helping us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's not a big deal, but I want\x01",
            "to do everything I can for them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10DA")

    label("loc_1067")


    ChrTalk(
        0x8,
        (
            "I want the Resistance\x01",
            "to do their best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's not a big deal, but I want\x01",
            "to do everything I can for them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10DA")

    Jump("loc_1D1F")

    label("loc_10DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1258")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11FE")

    ChrTalk(
        0x8,
        (
            "In the end, that armed\x01",
            "group didn't lay hand on\x01",
            "any townsman or our food.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The fact that it was scary hasn't\x01",
            "changed, but we received relatively\x01",
            "little damage compared to the CGF.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...But, what was their objective?\x01",
            "That's what I don't understand.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1253")

    label("loc_11FE")


    ChrTalk(
        0x8,
        (
            "That armed group...\x01",
            "What was their object?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I really don't understand that.\x02",
    )

    CloseMessageWindow()

    label("loc_1253")

    Jump("loc_1D1F")

    label("loc_1258")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_12D7")

    ChrTalk(
        0x8,
        "Hmm, what a pleasant rain.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We don't have many guests\x01",
            "on days like today, so I\x01",
            "think I'll take it easy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D1F")

    label("loc_12D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_15D7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x175, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13E6")

    ChrTalk(
        0x8,
        (
            "Thank goodness the Liberl-made\x01",
            "drinking glasses arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I was startled when I saw\x01",
            "the scalpels and stuff in\x01",
            "the misdelivered package.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ha ha. Anyway, that must\x01",
            "have been tough for you too.\x01",
            "Allow me to thank you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_149C")

    label("loc_13E6")


    ChrTalk(
        0x8,
        (
            "Thank goodness the Liberl-\x01",
            "made drinking glasses I\x01",
            "ordered arrived.\x02\x03",
            "Honestly, I was startled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ha ha. Anyway, that must\x01",
            "have been tough for you too.\x01",
            "Allow me to thank you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_149C")

    Jump("loc_15D2")

    label("loc_14A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_157D")

    ChrTalk(
        0x8,
        (
            "Mr. Marlow finally\x01",
            "got his energy back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even looked from an outsider's\x01",
            "point of view, Lycka's way of\x01",
            "comforting him was cold...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, if that got back his\x01",
            "energy, I guess it's all right.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15D2")

    label("loc_157D")


    ChrTalk(
        0x8,
        (
            "Well, at least Mr. Marlow\x01",
            "seems to have gotten better.\x01",
            "So, case closed for now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15D2")

    Jump("loc_1D1F")

    label("loc_15D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_17A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16EE")

    ChrTalk(
        0x8,
        (
            "Recently, I've been getting the\x01",
            "impression that Mr. Marlow\x01",
            "thinks Lycka hates him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "He doesn't show up at my\x01",
            "bar, and doesn't try hard at\x01",
            "work, so that's troubling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Lycka herself doesn't realize this,\x01",
            "so it's become a tricky situation...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17A1")

    label("loc_16EE")


    ChrTalk(
        0x8,
        (
            "Still, Mr. Gantz has some\x01",
            "good sides too... To think he'd\x01",
            "go to speak directly for his friend...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, his opponent is Lycka so it\x01",
            "looks like this'll be a tough battle.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17A1")

    Jump("loc_1D1F")

    label("loc_17A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_18BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1872")

    ChrTalk(
        0x8,
        (
            "It seems Mr. Marlow\x01",
            "tried a pass on Lycka\x01",
            "while drunk yesterday...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "She flatly rejected him,\x01",
            "completely sinking that ship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "...Kuhuhu. It was fun to watch, though.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_18B9")

    label("loc_1872")


    ChrTalk(
        0x8,
        "Poor Mr. Marlow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I think I'll give him\x01",
            "a snack on the house.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18B9")

    Jump("loc_1D1F")

    label("loc_18BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_19E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_194C")

    ChrTalk(
        0x8,
        (
            "The miners have the day off.\x01",
            "They've been drinking all day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If you like, why not\x01",
            "have a drink with them?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_19E2")

    label("loc_194C")


    ChrTalk(
        0x8,
        (
            "Goodness. On days the\x01",
            "mine is closed, I really\x01",
            "have no time to rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Uh uh. Well, that's fun,\x01",
            "and after all, I run a\x01",
            "business of this type.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19E2")

    Jump("loc_1D1F")

    label("loc_19E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1BB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B1F")

    ChrTalk(
        0x8,
        (
            "Yesterday, Lycka was drunk and\x01",
            "showed off she's a merry drinker.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Normally that girl is antisocial, but\x01",
            "she's really cute when she smiles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It seems Mr. Marlow noticed\x01",
            "that and totally fell for her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Kuhuhu. Love affairs are my favorite.\x01",
            "I wonder what'll happen next.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BAB")

    label("loc_1B1F")


    ChrTalk(
        0x8,
        (
            "It looks like Mr. Marlow fell\x01",
            "for Lycka at yesterday's party.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Kuhuhu. Love affairs are my favorite.\x01",
            "I wonder what'll happen next.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BAB")

    Jump("loc_1D1F")

    label("loc_1BB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_1D1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CA0")

    ChrTalk(
        0x8,
        (
            "Hey, welcome. You came a long\x01",
            "way to get here, didn't you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We serve the miners, so\x01",
            "we've got a full menu that\x01",
            "will fill your stomach.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We serve large portions, so if\x01",
            "you like, please have something.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1D1F")

    label("loc_1CA0")


    ChrTalk(
        0x8,
        (
            "You came all the way here, so if\x01",
            "you like, please have something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We've got a full menu that\x01",
            "will fill you right up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D1F")

    Jump("loc_97D")

    label("loc_1D24")

    TalkEnd(0x8)
    Return()

    # Function_6_919 end

    def Function_7_1D28(): pass

    label("Function_7_1D28")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1EFF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E63")

    ChrTalk(
        0x9,
        (
            "Both Mr. Gantz and Mr. Marlow looked\x01",
            "happy when they went to the mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I wonder if they're going to have a party\x01",
            "to celebrate the reopening tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "...Oh brother. What a pain.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "But, with the situation outside,\x01",
            "it's a relief that some things\x01",
            "are the same as before.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1EFA")

    label("loc_1E63")


    ChrTalk(
        0x9,
        (
            "With the situation outside,\x01",
            "it's a relief that some things\x01",
            "are the same as before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Well, I'll be here tonight,\x01",
            "so might as well enjoy it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EFA")

    Jump("loc_2C83")

    label("loc_1EFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_20A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_200B")

    ChrTalk(
        0x9,
        (
            "That leader is super\x01",
            "strong, isn't she.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "She challenged the new\x01",
            "order before everyone else.\x01",
            "Not even the men did that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I bet there are a lot of women \x01",
            "who follow her example.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2003")

    ChrTalk(
        0x109,
        "#10104FYes... I feel the same.\x02",
    )

    CloseMessageWindow()

    label("loc_2003")

    SetScenarioFlags(0x0, 1)
    Jump("loc_20A2")

    label("loc_200B")


    ChrTalk(
        0x9,
        (
            "She challenged the new\x01",
            "order before everyone else.\x01",
            "Not even the men did that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I bet there's a lot of women who\x01",
            "follow that leader's example.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20A2")

    Jump("loc_2C83")

    label("loc_20A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2349")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21EE")

    ChrTalk(
        0x9,
        (
            "I read the latest volume of the serial\x01",
            "novel I've been following lately...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "But in this situation, we won't\x01",
            "be able to get new volumes in,\x01",
            "so I'm holding off on it for awhile.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "...If you like, I'll give it to you.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2F9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x2F9, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x189, 3)
    Jump("loc_2344")

    label("loc_21EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22AD")

    ChrTalk(
        0x9,
        (
            "Mr. Gantz and Mr. Marlow have \x01",
            "been coming here during the day, lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Well, with the mine closed\x01",
            "and us unable to go to the city,\x01",
            "I guess it can't be helped.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2344")

    label("loc_22AD")


    ChrTalk(
        0x9,
        (
            "With the mine closed and us unable\x01",
            "to go to the city, I guess you want\x01",
            "to drink from the morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "*sigh*... It's a pain,\x01",
            "but I'll join them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2344")

    Jump("loc_2C83")

    label("loc_2349")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_24EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2466")

    ChrTalk(
        0x9,
        (
            "When the town was occupied...\x01",
            "I could only shiver in a\x01",
            "corner of the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "But Mr. Marlow kept\x01",
            "encouraging me saying that it\x01",
            "was ok, we would've been saved...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...I thought he was unreliable, but I've\x01",
            "changed my opinion of him. Just a little.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_24E9")

    label("loc_2466")


    ChrTalk(
        0x9,
        (
            "Back then... I was so\x01",
            "scared I couldn't even\x01",
            "call them names as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...I have to thank Mr. Marlow,\x01",
            "who encouraged me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24E9")

    Jump("loc_2C83")

    label("loc_24EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2572")

    ChrTalk(
        0x9,
        (
            "I hate rainy days. The floor gets\x01",
            "wet and it's a pain to clean...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Can't Mr. Carlos eat\x01",
            "quickly and go home?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C83")

    label("loc_2572")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_267E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_263B")

    ChrTalk(
        0x9,
        (
            "...In the end, I wonder\x01",
            "what happened yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Like Mr. Gantz asked\x01",
            "me, I told him "Why don't\x01",
            "you cheer up", but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, who cares.\x01",
            "I've gotta clean now...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2679")

    label("loc_263B")


    ChrTalk(
        0x9,
        "...*sigh*, how dull...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I've got to get to cleaning.\x02",
    )

    CloseMessageWindow()

    label("loc_2679")

    Jump("loc_2C83")

    label("loc_267E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2738")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2699")
    Call(0, 8)
    Jump("loc_2733")

    label("loc_2699")

    OP_4B(0xC, 0xFF)

    ChrTalk(
        0x9,
        "Well, yeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I could do it if you paid\x01",
            "all the bills you've piled\x01",
            "up, Mr. Gantz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Huh... No, you see,\x01",
            "that's a different matter...\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)

    label("loc_2733")

    Jump("loc_2C83")

    label("loc_2738")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_28A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2845")

    ChrTalk(
        0x9,
        (
            "Mr. Marlow was acting\x01",
            "strange yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "He talked to me way\x01",
            "too much, and invited\x01",
            "me to drink with him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I was in a bad mood so I ignored him.\x01",
            "He's strangely depressed today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Honestly, how hopeless.\x01",
            "Really, what a bother.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_28A2")

    label("loc_2845")


    ChrTalk(
        0x9,
        (
            "Seriously. Mr. Marlow was\x01",
            "really annoying yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "This is why I avoid drunks...\x02",
    )

    CloseMessageWindow()

    label("loc_28A2")

    Jump("loc_2C83")

    label("loc_28A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_29EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_297E")

    ChrTalk(
        0x9,
        (
            "Just because it's a\x01",
            "vacation date, how can\x01",
            "they drink from morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "When I drink, I get drunk immediately\x01",
            "and can't remember anything, so I\x01",
            "don't get what good there's to do it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_29E6")

    label("loc_297E")


    ChrTalk(
        0x9,
        (
            "How can they drink\x01",
            "from morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Well, whatever. Looks like\x01",
            "everyone's having a good time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29E6")

    Jump("loc_2C83")

    label("loc_29EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2B2B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AA6")

    ChrTalk(
        0x9,
        "Ow...my head hurts...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I joined the miners'\x01",
            "party yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I carelessly drank, and\x01",
            "can't remember anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "...I wonder if I did anything.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2B26")

    label("loc_2AA6")


    ChrTalk(
        0x9,
        (
            "Ah, my head hurts... I can't remember\x01",
            "anything from yesterday at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...I wonder if I did\x01",
            "anything I shouldn't have.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B26")

    Jump("loc_2C83")

    label("loc_2B2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_2C83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BE1")

    ChrTalk(
        0x9,
        (
            "Mr. Gantz lost big again\x01",
            "gambling the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm glad he stopped grumbling and\x01",
            "complaining just like last time, but... \x01",
            "He's a stubborn one.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2C83")

    label("loc_2BE1")


    ChrTalk(
        0x9,
        (
            "Even though Mr. Gantz lost at\x01",
            "gambling recently, his grumbling\x01",
            "and complaining stopped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...If he keeps losing, how is he\x01",
            "going to pay his bill, though?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C83")

    TalkEnd(0xFE)
    Return()

    # Function_7_1D28 end

    def Function_8_2C87(): pass

    label("Function_8_2C87")

    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xC,
        (
            "Say, Lycka. I'm counting\x01",
            "on you. Just like this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Umm, Mr. Gantz? \x01",
            "Why should I be the one\x01",
            "to cheer up Mr. Marlow?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm telling you. His depression\x01",
            "lately has nothing to do with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "W-Well, if pushed, I'd say it's\x01",
            "REALLY got something to do with you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "...I don't get it.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x0, 6)
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_8_2C87 end

    def Function_9_2DC7(): pass

    label("Function_9_2DC7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2DD8")
    Jump("loc_2F96")

    label("loc_2DD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2F47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2ECA")

    ChrTalk(
        0xA,
        (
            "I finished transporting \x01",
            "Septium by this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "If the rain got heavier and the\x01",
            "surface muddy, it would've been\x01",
            "hard to get any traction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Even choosing the times with\x01",
            "less peril is a driving skill.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2F42")

    label("loc_2ECA")


    ChrTalk(
        0xA,
        (
            "I finished transporting \x01",
            "Septium by this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Even choosing the times with\x01",
            "less peril is a driving skill.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F42")

    Jump("loc_2F96")

    label("loc_2F47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2F55")
    Jump("loc_2F96")

    label("loc_2F55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2F63")
    Jump("loc_2F96")

    label("loc_2F63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2F71")
    Jump("loc_2F96")

    label("loc_2F71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2F7F")
    Jump("loc_2F96")

    label("loc_2F7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2F8D")
    Jump("loc_2F96")

    label("loc_2F8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_2F96")

    label("loc_2F96")

    TalkEnd(0xFE)
    Return()

    # Function_9_2DC7 end

    def Function_10_2F9A(): pass

    label("Function_10_2F9A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2FAB")
    Jump("loc_309F")

    label("loc_2FAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2FB9")
    Jump("loc_309F")

    label("loc_2FB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2FC7")
    Jump("loc_309F")

    label("loc_2FC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2FD5")
    Jump("loc_309F")

    label("loc_2FD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2FE3")
    Jump("loc_309F")

    label("loc_2FE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3088")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FFE")
    Call(0, 11)
    Jump("loc_3083")

    label("loc_2FFE")


    ChrTalk(
        0xB,
        (
            "When is time to scold them,\x01",
            "you have to do it properly\x01",
            "for your kid's sake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "A parent's job is not to\x01",
            "spoil their children.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3083")

    Jump("loc_309F")

    label("loc_3088")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3096")
    Jump("loc_309F")

    label("loc_3096")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_309F")

    label("loc_309F")

    TalkEnd(0xFE)
    Return()

    # Function_10_2F9A end

    def Function_11_30A3(): pass

    label("Function_11_30A3")

    OP_4B(0xB, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xD,
        (
            "Anyway, your threatening attitude\x01",
            "scared us yesterday, mine captain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "You got mad at Alec the same\x01",
            "way as when you get mad at us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "When is time to scold them,\x01",
            "you have to do it properly\x01",
            "for your kids' sake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'm sure you'll understand \x01",
            "if you become a\x01",
            "parent someday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "Is that so...\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xD, 0x10)
    SetScenarioFlags(0x0, 7)
    OP_4C(0xB, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_11_30A3 end

    def Function_12_31F1(): pass

    label("Function_12_31F1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3202")
    Jump("loc_33A8")

    label("loc_3202")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_3210")
    Jump("loc_33A8")

    label("loc_3210")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_32B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_322B")
    Call(0, 13)
    Jump("loc_32AE")

    label("loc_322B")


    ChrTalk(
        0xC,
        (
            "Because of the situation,\x01",
            "I don't even feel in the mood\x01",
            "to drink during the day...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "*sigh*, I want to go to the casino...\x02",
    )

    CloseMessageWindow()

    label("loc_32AE")

    Jump("loc_33A8")

    label("loc_32B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_32C1")
    Jump("loc_33A8")

    label("loc_32C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_32CF")
    Jump("loc_33A8")

    label("loc_32CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_32DD")
    Jump("loc_33A8")

    label("loc_32DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3375")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32F8")
    Call(0, 8)
    Jump("loc_3370")

    label("loc_32F8")


    ChrTalk(
        0xC,
        (
            "(In any case, if Lycka \x01",
            "consoles him, Marlow\x01",
            "should cheer up...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "(Hopefully, everything\x01",
            "will turn out ok...!)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3370")

    Jump("loc_33A8")

    label("loc_3375")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3383")
    Jump("loc_33A8")

    label("loc_3383")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3391")
    Jump("loc_33A8")

    label("loc_3391")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_339F")
    Jump("loc_33A8")

    label("loc_339F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_33A8")

    label("loc_33A8")

    TalkEnd(0xFE)
    Return()

    # Function_12_31F1 end

    def Function_13_33AC(): pass

    label("Function_13_33AC")

    OP_4B(0xC, 0xFF)
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xC,
        (
            "Aww... Because of the situation, I can't\x01",
            "go to the city to play at the casino.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "How long am I gonna have to live with this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "It's pretty tough,\x01",
            "without any amusements.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "On the other hand, the mine's closed, so I\x01",
            "can't give work everything I've got either.\x02",
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
        "*sigh*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "All you can do is sigh.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xF, 0x10)
    OP_4C(0xC, 0xFF)
    OP_4C(0xF, 0xFF)
    Return()

    # Function_13_33AC end

    def Function_14_3534(): pass

    label("Function_14_3534")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3545")
    Jump("loc_35E3")

    label("loc_3545")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3553")
    Jump("loc_35E3")

    label("loc_3553")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3561")
    Jump("loc_35E3")

    label("loc_3561")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_356F")
    Jump("loc_35E3")

    label("loc_356F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_357D")
    Jump("loc_35E3")

    label("loc_357D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_35CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3598")
    Call(0, 11)
    Jump("loc_35C7")

    label("loc_3598")


    ChrTalk(
        0xD,
        (
            "Hmm, it must be tough\x01",
            "being a parent too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35C7")

    Jump("loc_35E3")

    label("loc_35CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_35DA")
    Jump("loc_35E3")

    label("loc_35DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_35E3")

    label("loc_35E3")

    TalkEnd(0xFE)
    Return()

    # Function_14_3534 end

    def Function_15_35E7(): pass

    label("Function_15_35E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3E14")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_37B1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x89, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3796")
    TalkBegin(0xFE)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_369C")
    Jump("loc_36E6")

    label("loc_369C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_36BC")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_36E6")

    label("loc_36BC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_36DC")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_36E6")

    label("loc_36DC")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_36E6")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)

    ChrTalk(
        0xFE,
        (
            "Everyone, thank you\x01",
            "for joining me for\x01",
            "an interview today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If there's another chance, \x01",
            "I would like to to talk more.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_37AC")

    label("loc_3796")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 7)), scpexpr(EXPR_END)), "loc_37A8")
    Call(0, 39)
    Return()

    label("loc_37A8")

    Call(0, 37)
    Return()

    label("loc_37AC")

    Jump("loc_3E14")

    label("loc_37B1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C94")
    TalkBegin(0xFE)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3859")
    Jump("loc_38A3")

    label("loc_3859")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3879")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_38A3")

    label("loc_3879")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3899")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_38A3")

    label("loc_3899")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_38A3")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BFE")

    ChrTalk(
        0x101,
        "#00000FMr. Nielsen―\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "Hmm. That voice is Lloyd's, isn't it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Why are you in Mainz today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWe just thought we'd\x01",
            "stop by on patrol.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FAre you newsgathering,\x01",
            "Mr. Nielsen?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes. Actually, I plan to\x01",
            "interview this town's mayor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll ask him about the history of\x01",
            "Septium mining in this town, and\x01",
            "about changes in the modern day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because of the question of\x01",
            "independence, I want to look\x01",
            "once more at state history.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FWow, that's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FHow to say this... You look\x01",
            "into things others wouldn't.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ha ha. Thanks to that, I've been able\x01",
            "to take all these detours, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, you all look\x01",
            "busy as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think things will be difficult going\x01",
            "forward, but please do your best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, thank you very much.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16B, 5)
    Jump("loc_3C88")

    label("loc_3BFE")


    ChrTalk(
        0xFE,
        (
            "Now then. I have some time\x01",
            "before my next interview,\x01",
            "so I'll take it easy here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ha ha. This is a quiet\x01",
            "and calm room, isn't it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C88")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_3E14")

    label("loc_3C94")

    TalkBegin(0xFE)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3D28")
    Jump("loc_3D72")

    label("loc_3D28")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3D48")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3D72")

    label("loc_3D48")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3D68")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3D72")

    label("loc_3D68")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3D72")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)

    ChrTalk(
        0xFE,
        (
            "Ha ha. This is a quiet\x01",
            "and calm room, isn't it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think I'll take it easy until\x01",
            "it's time for my interview.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)

    label("loc_3E14")

    Return()

    # Function_15_35E7 end

    def Function_16_3E15(): pass

    label("Function_16_3E15")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3E26")
    Jump("loc_3F4E")

    label("loc_3E26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_3E34")
    Jump("loc_3F4E")

    label("loc_3E34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3F4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E4F")
    Call(0, 13)
    Jump("loc_3F4E")

    label("loc_3E4F")

    SetChrSubChip(0xF, 0x2)

    ChrTalk(
        0xF,
        (
            "(At first, I thought that it wasn't that\x01",
            "bad since I could see Lycka, but...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "(Staying at the bar too long doesn't\x01",
            "give a very good impression...)\x02",
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
        "(...I wonder what he's looking at.)\x02",
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_93(0x9, 0x10E, 0x0)
    SetChrSubChip(0xF, 0x0)

    label("loc_3F4E")

    TalkEnd(0xFE)
    Return()

    # Function_16_3E15 end

    def Function_17_3F52(): pass

    label("Function_17_3F52")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3F63")
    Jump("loc_45C1")

    label("loc_3F63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_45B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4453")

    ChrTalk(
        0x10,
        (
            "#07901FRandy, and the Support Section...\x01",
            "Please listen to what I have to say.\x02\x03",
            "#07903FNow that the declaration of\x01",
            "independence is invalid, at least the\x01",
            "State Guard can't act freely anymore.\x02\x03",
            "#07901FNow, if we could just do something about\x01",
            "that "barrier" surrounding the city...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FThat will be our best chance to\x01",
            "liberate Crossbell City, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FWe'll make that barrier\x01",
            "disappear somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FBut, the "Red Constellation" is, of course,\x01",
            "already prepared for that situation.\x02\x03",
            "#00301FIf we hand it poorly, they could\x01",
            "begin a Resistance-hunt in earnest\x01",
            "before we set the operation in motion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00103FIt seems best to hurry...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#07903FAnyway, we'll get ready\x01",
            "to begin the operation.\x02\x03",
            "We have the help of the Divine Wolves,\x01",
            "so we'll be able to fight the "Red\x01",
            "Constellation" better than before.\x02\x03",
            "#07901FSo please, do something\x01",
            "about that barrier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FYeah, leave it to us.\x02\x03",
            "#00301F...Be careful, Mireille.\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_43BC")
    Jump("loc_4406")

    label("loc_43BC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_43DC")
    OP_52(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4406")

    label("loc_43DC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_43FC")
    OP_52(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4406")

    label("loc_43FC")

    OP_52(0x10, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4406")

    OP_52(0x10, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x104, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x10, 0x10)

    ChrTalk(
        0x10,
        "#07902FYeah, you too.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AF, 0)
    ClearChrFlags(0x10, 0x10)
    Jump("loc_45B3")

    label("loc_4453")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4543")

    ChrTalk(
        0x10,
        (
            "#07903FAnyway, we'll get ready\x01",
            "to begin the operation.\x02\x03",
            "We have the help of the Divine Wolves,\x01",
            "so we'll be able to fight the "Red\x01",
            "Constellation" better than before.\x02\x03",
            "#07901FPlease take care of\x01",
            "that barrier, everyone.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_45B3")

    label("loc_4543")


    ChrTalk(
        0x10,
        (
            "#07903FAnyway, we'll get ready\x01",
            "to begin the operation.\x02\x03",
            "#07901FPlease take care of\x01",
            "that barrier, everyone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45B3")

    Jump("loc_45C1")

    label("loc_45B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_45C1")

    label("loc_45C1")

    TalkEnd(0xFE)
    Return()

    # Function_17_3F52 end

    def Function_18_45C5(): pass

    label("Function_18_45C5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48B6")

    ChrTalk(
        0x11,
        (
            "#00802F#30W...Everyone. \x01",
            "Be extremely careful, ok?\x02\x03",
            "#00808FDoing your best is fine,\x01",
            "but don't end up like\x01",
            ""Pater-Mater", you hear?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah... Understood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00308FThinkin' about it, we owe our\x01",
            "very lives to you guys...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F...It would have been nice if we talked\x01",
            "longer when we met at the studio earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#00808F#30WYeah... I would have\x01",
            "liked to talk longer too.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x11)

    ChrTalk(
        0x11,
        (
            "#00804F#30W...Please, don't worry about Renne.\x01\x02\x03",
            "#00800FThe experiences she had over the past half\x01",
            "year have made her stronger in a real sense...\x02\x03",
            "#00802FShe has precious friends with her, so\x01",
            "I'm sure she'll be able to get through it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00004FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FPlease say hi for us\x01",
            "when she wakes up.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_49A9")

    label("loc_48B6")


    ChrTalk(
        0x11,
        (
            "#00804F#30WPlease, don't be worried about Renne.\x02\x03",
            "#00800FThe experiences she had over the past half\x01",
            "year have made her stronger in a real sense...\x02\x03",
            "#00802FShe has precious friends with her, so\x01",
            "I'm sure she'll be able to get through it...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49A9")

    TalkEnd(0xFE)
    Return()

    # Function_18_45C5 end

    def Function_19_49AD(): pass

    label("Function_19_49AD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E5C")

    ChrTalk(
        0x12,
        (
            "#00903F#30W...It seems Dr. Novartis\x01",
            "has already left this land.\x02\x03",
            "#00901FIt must be a relief to know the "Society"\x01",
            "will not oppose you any further, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FHonestly, we have no idea\x01",
            "what they were after.\x02\x03",
            "#00003FIt seems like they're planning\x01",
            "something in the Empire, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#00903F#30W...The "Phantasmal Blaze Plan", right?\x02\x03",
            "#00901FIt looks like a large-scale plan based\x01",
            "on the events in Crossbell, but...\x02\x03",
            "#00908F...I'm worried about Mr. Olivier and the others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205FMr. Olivier, you said...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00303FYou must be talkin' about Prince Olivert?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#00903F#30WYes. Ever since the start of the civil war, we\x01",
            "haven't been able to get in touch with him.\x02\x03",
            "#00908FAs long as Mr. Mueller's with him,\x01",
            "I think he'll be safe, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108FEven so, it's worrying...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E57")
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x12,
        (
            "#00900F#30WOh, right... Everyone,\x01",
            "will you take this?\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x394),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x394, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x18A, 3)

    ChrTalk(
        0x101,
        "#00005FAnd this is...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#00900F#30WIt was at the place where\x01",
            ""Pater-Mater" passed away.\x02\x03",
            "#00903F...It's probably an\x01",
            ""Aion" part. You might\x01",
            "find a good use for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FUnderstood...\x01",
            "We gladly accept it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E57")

    Jump("loc_4EF7")

    label("loc_4E5C")


    ChrTalk(
        0x12,
        (
            "#00903F#30WThat "Tree of Azure"...\x02\x03",
            "I think it exceeds even the scale of\x01",
            "the Liber Ark that appeared in Liberl.\x02\x03",
            "#00900FPlease, be extremely careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EF7")

    TalkEnd(0xFE)
    Return()

    # Function_19_49AD end

    def Function_20_4EFB(): pass

    label("Function_20_4EFB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FF9")

    ChrTalk(
        0x13,
        (
            "#03900F"Pater-Mater"'s logic unit\x01",
            "was not originally designed\x01",
            "for autonomous functions.\x02\x03",
            "Does it mean he obtained a\x01",
            ""soul" through meeting Renne...?\x02\x03",
            "#03903F...I've been a doll maker for decades,\x01",
            "but I still have much to learn.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_50D2")

    label("loc_4FF9")


    ChrTalk(
        0x13,
        (
            "#03900F...Conversely, this incident might have\x01",
            "a positive effect on Renne.\x02\x03",
            "#03903FShe couldn't experience what "parting" is in\x01",
            "a real sense in the past, but now she has...\x02\x03",
            "#03900FEverything for her begins now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50D2")

    TalkEnd(0xFE)
    Return()

    # Function_20_4EFB end

    def Function_21_50D6(): pass

    label("Function_21_50D6")

    Call(0, 22)
    Return()

    # Function_21_50D6 end

    def Function_22_50DA(): pass

    label("Function_22_50DA")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_517B")

    ChrTalk(
        0x14,
        (
            "#03317F#2S#40W...Pater-Mater...\x02\x03",
            "#2S#40W...Why......\x01",
            "...Why did you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F...Renne...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00103F...Let's leave her quietly.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_51D6")

    label("loc_517B")


    ChrTalk(
        0x14,
        "#03317F#2S#40W...Papa... ...Mama...\x02",
    )

    CloseMessageWindow()
    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Renne, tired of weeping, is sleeping.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_51D6")

    TalkEnd(0x14)
    Return()

    # Function_22_50DA end

    def Function_23_51DA(): pass

    label("Function_23_51DA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5389")

    ChrTalk(
        0xFE,
        (
            "Eolia and I are\x01",
            "performing aftercare for\x01",
            "the occupation incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We've exterminated the Wanted Monsters\x01",
            "in the surrounding areas, so they're safe\x01",
            "for now... That's what I'd like to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The emotional scars the people of Mainz received\x01",
            "from the incident are pretty severe. There're\x01",
            "people so anxious, they can't sleep at night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We consulted with\x01",
            "Michel and decided to\x01",
            "extend our stay here.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_545E")

    label("loc_5389")


    ChrTalk(
        0xFE,
        (
            "The emotional scars the people of Mainz received\x01",
            "from the incident are pretty severe. There're\x01",
            "people so anxious, they can't sleep at night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We consulted with\x01",
            "Michel and decided to\x01",
            "extend our stay here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_545E")

    TalkEnd(0xFE)
    Return()

    # Function_23_51DA end

    def Function_24_5462(): pass

    label("Function_24_5462")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_558C")

    ChrTalk(
        0xFE,
        (
            "Because of that attack, St. Ursula\x01",
            "Hospital has their hands full.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's why I'm taking responsibility for healing\x01",
            "as many patients as possible, right here in Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Things are pretty difficult... But it's in times\x01",
            "like these that we have to divide and conquer.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_5631")

    label("loc_558C")


    ChrTalk(
        0xFE,
        (
            "I'm taking responsibility for healing as many\x01",
            "patients as possible, right here in Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's times like these that make\x01",
            "me glad I got my medical license.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5631")

    TalkEnd(0xFE)
    Return()

    # Function_24_5462 end

    def Function_25_5635(): pass

    label("Function_25_5635")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5737")

    ChrTalk(
        0xFE,
        (
            "Today, I'm working separately\x01",
            "from my partner, Wenzel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We've gotten more irregular\x01",
            "shifts like this to cover the\x01",
            "hole left by Estelle and Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Exterminating monsters and such is\x01",
            "tough, but we'll get through it somehow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 3)
    Jump("loc_57D5")

    label("loc_5737")


    ChrTalk(
        0xFE,
        (
            "Today, I'm working separately\x01",
            "from my partner, Wenzel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Exterminating monsters and such\x01",
            "is tough, but we'll get through\x01",
            "this labor shortage somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57D5")

    TalkEnd(0xFE)
    Return()

    # Function_25_5635 end

    def Function_26_57D9(): pass

    label("Function_26_57D9")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5921")
    BeginChrThread(0x109, 1, 0, 27)
    WaitChrThread(0x109, 1)
    Sleep(600)

    label("loc_5921")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_593E")
    BeginChrThread(0x105, 1, 0, 27)
    WaitChrThread(0x105, 1)
    Sleep(600)

    label("loc_593E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_595B")
    BeginChrThread(0x106, 1, 0, 27)
    WaitChrThread(0x106, 1)
    Sleep(600)

    label("loc_595B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5978")
    BeginChrThread(0x10A, 1, 0, 27)
    WaitChrThread(0x10A, 1)
    Sleep(600)

    label("loc_5978")

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
        "#12P#00805F#30WAh, everyone...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#12P#00902F#30W...Hey...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00005FEstelle and Joshua!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#00102FSo you came here...?\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7568", 0)

    ChrTalk(
        0x104,
        (
            "#5P#00300FI heard. It seems you kicked\x01",
            "the ass of that giant doll, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#00202FAs expected from you\x01",
            "all and "Pater-Mater".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#12P#00802F#30WAhaha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#12P#00903F#30W...Well, the entire fact that we\x01",
            "won was due to "his" sacrifice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00005FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#5P#00105FNow that you mention it... Where's Renne?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x13,
        "Elderly Voice",
        "...Renne is sleeping.\x02",
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

    def lambda_5D01():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_5D01)
    Sleep(50)

    def lambda_5D11():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_5D11)
    Sleep(50)

    def lambda_5D21():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_5D21)
    Sleep(50)

    def lambda_5D31():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_5D31)
    Sleep(50)

    def lambda_5D41():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_5D41)
    Sleep(50)

    def lambda_5D51():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x5, 1, lambda_5D51)
    OP_6F(0x79)

    ChrTalk(
        0x14,
        "#11P#03317F#40W#2S............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FMeister Jｶrg!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203F...So you were here too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#11P#03903FHm... I received their message.\x02\x03",
            "#03900FTerrible things are occurring,\x01",
            "and since "Pater-Mater" has\x01",
            "died, I had to show up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FThat doll...died?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305FHey now, could it be...\x02",
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
            "#12P#00808F#30W...Yeah... \x01",
            "He grabbed that giant doll,\x01",
            "took it to the skies and then...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#12P#00908F#30W...He probably used his\x01",
            "self-destruct function...\x02\x03",
            "#00903FThat too, according to his own judgment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00003F...So that's what happened...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#5P#00208FA machine made that kind of decision...?\x02",
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
            "#11P#03317F#2S#40W...*sob*...\x01",
            "......Pater-Mater...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FSleeping because she's\x01",
            "exhausted from cryin', huh...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F...That's understandable... \x01",
            "I can relate to those feelings...\x02",
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
            "#11P#03903F..."Pater-Mater" resigned\x01",
            "himself to his fate...\x02\x03",
            "#03900FI have nothing but respect for his\x01",
            ""soul", that chose to protect the\x01",
            "girl and threw away his own life.\x02\x03",
            "As a doll maker, it is more than I deserve.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FMeister...\x02",
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
            "#12P#00801F#30W──We heard about the situation.\x01",
            "Things have gotten serious, hm?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#12P#00900F#30WDepending on when we heal up,\x01",
            "we're planning on assisting you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00004FThanks, you two.\x02\x03",
            "#00000FBut for right now, give resting\x01",
            "your bodies the highest priority.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00303FYou aren't like that missy's doll...\x02\x03",
            "#00300FNow's the time we've got to do\x01",
            "anything in our power for Keddo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#12P#00802F#30WI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#12P#00904F#30W...May the Goddess protect\x01",
            "you. Be extremely careful.\x02",
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

    # Function_26_57D9 end

    def Function_27_64CB(): pass

    label("Function_27_64CB")

    SetChrPos(0xFE, 94200, 0, 6500, 180)

    def lambda_64E1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_64E1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6511")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 28)
    Jump("loc_65B6")

    label("loc_6511")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6535")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 29)
    Jump("loc_65B6")

    label("loc_6535")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6559")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 30)
    Jump("loc_65B6")

    label("loc_6559")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_657D")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 31)
    Jump("loc_65B6")

    label("loc_657D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_65A1")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 32)
    Jump("loc_65B6")

    label("loc_65A1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_65B6")
    BeginChrThread(0xFE, 2, 0, 33)

    label("loc_65B6")

    Return()

    # Function_27_64CB end

    def Function_28_65B7(): pass

    label("Function_28_65B7")

    OP_95(0xFE, 94200, 0, 3030, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_28_65B7 end

    def Function_29_65D3(): pass

    label("Function_29_65D3")

    OP_95(0xFE, 94200, 0, 4850, 2000, 0x0)
    OP_95(0xFE, 93110, 0, 3070, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_29_65D3 end

    def Function_30_6603(): pass

    label("Function_30_6603")

    OP_95(0xFE, 94200, 0, 4850, 2000, 0x0)
    OP_95(0xFE, 95280, 0, 3120, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_30_6603 end

    def Function_31_6633(): pass

    label("Function_31_6633")

    OP_95(0xFE, 94210, 0, 4150, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_31_6633 end

    def Function_32_664F(): pass

    label("Function_32_664F")

    OP_95(0xFE, 94260, 0, 5260, 2000, 0x0)
    OP_95(0xFE, 93580, 0, 4960, 2000, 0x0)
    OP_95(0xFE, 93270, 0, 4310, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_32_664F end

    def Function_33_6693(): pass

    label("Function_33_6693")

    OP_95(0xFE, 94260, 0, 5260, 2000, 0x0)
    OP_95(0xFE, 95020, 0, 4960, 2000, 0x0)
    OP_95(0xFE, 95250, 0, 4350, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_33_6693 end

    def Function_34_66D7(): pass

    label("Function_34_66D7")

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
            "#00306F#11P──I see. Then, it looks\x01",
            "like this is going to be\x01",
            "another absurd story.\x02\x03",
            "#00301FAnd what's more, Keddo has been...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#02106F#5PHmm. I feel like I can't actually write\x01",
            "an article that's this crazy, but...\x02\x03",
            "#02101FYou guys are planning on doing whatever\x01",
            "it takes to bring her back, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#6PYes, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203F#6PThat goes without saying.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00308F#11P............\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x104, 500)
    Sleep(100)

    ChrTalk(
        0x10,
        (
            "#07904F#11P...Randy. \x01",
            "Our Resistance will be fine.\x02\x03",
            "#07902FOriginally, you helped us on\x01",
            "the condition we saved your\x01",
            "Support Section friends, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x10, 500)

    ChrTalk(
        0x104,
        "#00305F#5PAh, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6P...So that's how it is, huh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#6P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#6PWell, it's certain that\x01",
            "you joining with us\x01",
            "would be a big help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#07904F#11POriginally, our Resistance was that\x01",
            "of stubborn CGF members who\x01",
            "couldn't accept the State Guard.\x02\x03",
            "#07902FYou, who separated from the CGF,\x01",
            "should help your own comrades.\x02\x03",
            "#07909FGoing forward, it seems\x01",
            "those wolves will help us too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01203F#6P#3CYes. I once again instructed\x01",
            "them to assist you.\x02\x03",
            "#01200FI'm sure they will be of help\x01",
            "in battles in the mountains.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#5P...Thanks, that's a big help.\x02",
    )

    CloseMessageWindow()

    def lambda_6CB0():
        OP_93(0x104, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6CB0)
    Sleep(50)

    def lambda_6CC0():
        OP_93(0x10, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_6CC0)
    Sleep(50)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x10, 0)

    ChrTalk(
        0x104,
        (
            "#00300F#11PLloyd, peTiote.\x01",
            "I'm comin' with you!\x02\x03",
            "As a member of the Support Section, \x01",
            "and one of Keddo's guardians!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#6PYeah...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204F#6P...Thank goodness.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10709F#5PUh uh... That's heartening.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#02103F#5PHmm, that's right.\x02\x03",
            "#02102FI wonder if I can\x01",
            "come along too...?\x02",
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

    def lambda_6EA1():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6EA1)
    Sleep(50)

    def lambda_6EB1():
        TurnDirection(0x103, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_6EB1)
    Sleep(50)

    def lambda_6EC1():
        TurnDirection(0x104, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6EC1)
    Sleep(50)

    def lambda_6ED1():
        TurnDirection(0x105, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_6ED1)
    Sleep(50)

    def lambda_6EE1():
        TurnDirection(0x106, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_6EE1)
    Sleep(50)

    def lambda_6EF1():
        TurnDirection(0x10, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_6EF1)
    Sleep(50)

    def lambda_6F01():
        TurnDirection(0x107, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_6F01)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x10, 0)
    WaitChrThread(0x107, 0)
    SetChrSubChip(0x107, 0x5)

    ChrTalk(
        0x101,
        "#00011F#6PHuh...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00211F#6PWhat is this all of a sudden...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#02104F#5PI mean, going forward, it looks like all\x01",
            "the action will be centered on you guys.\x02\x03",
            "#02110FAs a journalist I can't\x01",
            "very well overlook it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F#6PNo, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10406F#6PHmm. I don't really mind, though.\x02\x03",
            "#10400FAbbas will probably be annoyed that I'm\x01",
            "bringing someone from the media along, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10706F#6P...It would be bad for me to\x01",
            "end up in an article too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#02105F#5POh, don't worry.\x02\x03",
            "#02104FThere's a mountain of things I want to write\x01",
            "articles about, but now's not the time for that.\x02\x03",
            "#02106FAll I want to know right now is what will\x01",
            "happen to the independent state of Crossbell.\x02\x03",
            "#02101FWill this new order filled with deceit\x01",
            "be chosen by history, in the end?\x02",
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
        "#00005F#6PChosen by history...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#02103F#5PLet me just say this. \x01",
            "The entire continent is in chaos.\x02\x03",
            "I can't deny that President\x01",
            "Dieter is a cause, but...\x02\x03",
            "#02101FWill the danger be over,\x01",
            "just by casting him aside?\x02",
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
        "#00011F#6P...Well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#07906F#12PHonestly... \x01",
            "It might be difficult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#02106F#5PActually, 100 years ago, when Calvard\x01",
            "became a democracy, the revolutionary\x01",
            "government did a lot of dirty things.\x02\x03",
            "#02103FAssassinations were par for the\x01",
            "course. There was a plot like the\x01",
            "attack on Crossbell City, too.\x02\x03",
            "#02101FBut to a certain extent, their\x01",
            "actions are justified now.\x02\x03",
            "Even what President Dieter has done\x01",
            "can be said to be the same, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10708F#6P(...The assassination series 100 years ago...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#02106F#5PThough, given the situation,\x01",
            "I too can't say he's correct.\x02\x03",
            "#02100F──And so, that's what I want to find out.\x02\x03",
            "The path that\x01",
            "Crossbell will choose.\x02\x03",
            "And how that decision will\x01",
            "be recorded in history.\x02\x03",
            "#02109FI feel like I'll be able to\x01",
            "see it if I go with you guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6P...Miss Grace.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F#12PHmm... You really thought\x01",
            "about it that much, did you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202F#6PYou are so serious you are\x01",
            "like a different person...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#02109F#5PAhaha. Well the main reason\x01",
            "is that it seems interesting.\x02\x03",
            "#02110FAnd I've got channels\x01",
            "at Crossbell News.\x02\x03",
            "What if I could offer you\x01",
            "info from within the city?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00004F#6P──Understood. \x01",
            "We have no objection.\x02\x03",
            "#00000FWazy, Rixia. \x01",
            "Do either of you mind?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10710F#6PAs long as I don't\x01",
            "end up in an article...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#6PHu hu, I don't mind either.\x02\x03",
            "#10402FWell, convincing Abbas\x01",
            "might be difficult, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#02109F#5PThanks! I'm in your debt!\x02\x03",
            "#02110FAll right! Let's all do our best\x01",
            "and aim for the Fulitzer Prize!\x02",
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
            "#00012F#6PWell, it's not the case that\x01",
            "we're helping you out, Miss Grace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00211F#6PWell, it is Miss Grace, after all.\x02",
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
            "Afterwards, after greeting Bickson,\x01",
            "Town Mayor of Mainz, who was secretly\x01",
            "cooperating with the Resistance...\x02\x03",
            "They discussed their future plans. \x01",
            "After that, Mireille and the others said goodbye\x01",
            "and returned to their base in the mountains.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x22, 5)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_34_66D7 end

    def Function_35_7C79(): pass

    label("Function_35_7C79")

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
            "Oh, hello. Welcome\x01",
            "to "Der Ziegel" Inn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FExcuse us, we're from the\x01",
            "Special Support Section...\x02",
        )
    )

    CloseMessageWindow()
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
        0x8,
        (
            "Ah, so it's you guys. I heard\x01",
            "about you from Crossbell News.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Then, how about I make you\x01",
            "guys this mining town's\x01",
            "specialty, "Stamina Steak"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F...Sounds like it will pack\x01",
            "a punch on our stomachs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yeah. You guys have to go\x01",
            "around and eat at various\x01",
            "places, don't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In that case,\x01",
            "I'll bring them\x01",
            "to you bite-size.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F*giggle*. Thank you very much.\x02",
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
            "Lloyd and friends ate the Stamina Steak.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00309F*chew, chew*... \x01",
            "Man, even though it's bite size,\x01",
            "it's quite fillin' as a meal.\x02\x03",
            "#00304FAs expected, a steak\x01",
            "should be like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102FYes. You can indeed feel\x01",
            "power welling up inside you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Uh uh. To a miner, \x01",
            "stamina is life, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Pair this with a beer,\x01",
            "and you'll be ready to\x01",
            "work like a work-horse.\x02",
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
            "#10306FBeing a miner sounds\x01",
            "like hard work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa ha. Mr. Gantz and the\x01",
            "others seem to enjoy it, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Uh uh. They're the strong men\x01",
            "of a mining town, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Everyone, please come\x01",
            "here whenever you want\x01",
            "to eat your fill.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FYeah, we'll do!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x2, 0)
    SetScenarioFlags(0x173, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_82FF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_82FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_831C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_831C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_832F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_832F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_8342")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8342")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_835F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_835F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_8372")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8372")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_838F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_838F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_83A2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_83A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_83BF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_83BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_83D2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_83D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_83EF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_83EF")

    OP_29(0x80, 0x1, 0x8)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_851D")
    SetChrName("")
    Sound(17, 0, 100, 0)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8514")

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

    label("loc_8514")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_851D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8601")
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

    label("loc_8601")

    OP_4C(0x8, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 3700, 0, 2090, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_35_7C79 end

    def Function_36_8631(): pass

    label("Function_36_8631")

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
            "#3PHi, if it isn't the police\x01",
            "kids from before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PHave you come to\x01",
            "stay here today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FUhhm, we came because\x01",
            "we wanted to ask you\x01",
            "something...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FWas a strange\x01",
            "package delivered\x01",
            "here recently?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3PA strange package...?\x02",
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
            "#3POh...oh! That's right,\x01",
            "there was something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PWhy did something like\x01",
            "that come here again...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PDo you guys know\x01",
            "something about it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300FBingo.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FUhhm, actually...\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained about the\x01",
            "misdelivered packages.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#3POh, so that's\x01",
            "what happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PSo that package\x01",
            "was supposed to go\x01",
            "to St. Ursula, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PNo wonder there're scalpels\x01",
            "and other stuff mixed inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FIt must have seemed weird for\x01",
            "such things to suddenly arrive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3PWell, I was shocked!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PLycka was weirded out by them,\x01",
            "so she was going to put them\x01",
            "out with the trash tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106FJ-Just in the nick of time, I guess...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FLet me give you the\x01",
            "package you should have\x01",
            "gotten originally. Here.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x331),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " handed over.\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber(0x331, 1)

    ChrTalk(
        0x8,
        (
            "#3POh, thanks.\x01",
            "Let's see...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3P...Yeah, these are those\x01",
            "Liberlian glasses I\x01",
            "ordered awhile back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PI'm sure this\x01",
            "one's ours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309FI'm glad for you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FThen, I was wondering if we could\x01",
            "get the misdelivered one from you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PAlright!\x01",
            "One moment please.\x02",
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
            "#3PHere it is what I received.\x01",
            "I'll leave the rest to you.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x330),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x330, 1)
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
            "#00000F...Alright, let's head for\x01",
            "St. Ursula Hospital next.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FIt would be good to ask about\x01",
            "the situation at the reception.\x02",
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

    # Function_36_8631 end

    def Function_37_8E59(): pass

    label("Function_37_8E59")

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
        "#00005FMr. Nielsen―\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8FC9")
    Jump("loc_9013")

    label("loc_8FC9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8FE9")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9013")

    label("loc_8FE9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9009")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9013")

    label("loc_9009")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9013")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)

    ChrTalk(
        0xE,
        "Hmm. That voice is Lloyd's, isn't it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, I'm honored you remember me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Uh uh. It's because I've\x01",
            "interviewed you before.\x01",
            "There's no way I'd forget.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F(Could this person be...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300F(Yeah, the famous journalist\x01",
            "who interviewed Lloyd and\x01",
            "the others before, huh.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100F(Yes, he's Mr. Nielsen.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FUmm, why are you\x01",
            "in Mainz today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Yes. Actually, I plan to\x01",
            "interview this town's mayor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I'll ask him about the history of\x01",
            "Septium mining in this town, and\x01",
            "about changes in the modern day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Because of the question of\x01",
            "independence, I want to look\x01",
            "once more at state history.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10304FHmm, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FHow to say this... You look\x01",
            "into things others wouldn't.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Ha ha. Thanks to that, I've been able\x01",
            "to take all these detours, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "By the way, I heard you contributed to the capture of the\x01",
            "terrorists who attacked the Trade Conference awhile back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "...Hmm, that's right. If you\x01",
            "like, would you care to join\x01",
            "me for another interview?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I'm wondering what meaning there was in\x01",
            "the Trade Conference terror incident...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I think I could learn something\x01",
            "by talking it over with you all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FThe "meaning" of the terror attack...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208FBut that is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes. Information on this case is\x01",
            "restricted to the autonomous state \x01",
            "government and police personnel.\x02\x03",
            "I think what we'll be able to\x01",
            "talk about is limited, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Of course, I understand that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Even so, I still think there\x01",
            "would be meaning in discussing\x01",
            "this. What do you say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FHmm...\x02\x03",
            "(Our last interview with\x01",
            "him was indeed beneficial.)\x02\x03",
            "#00008F(If we have the time, I think\x01",
            "we should take him up on it...)\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 38)
    Return()

    # Function_37_8E59 end

    def Function_38_96D5(): pass

    label("Function_38_96D5")

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
            "Accept\x01",      # 0
            "Quit\x01",        # 1
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
        (0, "loc_9731"),
        (1, "loc_982A"),
        (SWITCH_DEFAULT, "loc_9920"),
    )


    label("loc_9731")


    ChrTalk(
        0x101,
        (
            "#00000FUnderstood. \x01",
            "We accept your interview.\x02",
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
        "Then, let's begin our discussion immediately.\x02",
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
            "Quest [Terror Incident Coverage Support]\x07\x00",
            " started!\x02",
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
    Jump("loc_9920")

    label("loc_982A")


    ChrTalk(
        0x101,
        (
            "#00006FWe're sorry. We don't have\x01",
            "the time right now...\x02\x03",
            "Can we ask about it again, later?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "Yes, I don't mind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Please come speak with me\x01",
            "when it's convenient for you.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0x0)
    OP_69(0xFF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9918")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 104410, 2000, 2730, 180)
    EventEnd(0x5)

    label("loc_9918")

    SetScenarioFlags(0x177, 7)
    Jump("loc_9920")

    label("loc_9920")

    Return()

    # Function_38_96D5 end

    def Function_39_9921(): pass

    label("Function_39_9921")

    TalkBegin(0xE)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_99B5")
    Jump("loc_99FF")

    label("loc_99B5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_99D5")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_99FF")

    label("loc_99D5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_99F5")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_99FF")

    label("loc_99F5")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_99FF")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)

    ChrTalk(
        0xE,
        "...You are Mr. Lloyd, correct?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Care to join me for the\x01",
            "terror incident coverage?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Call(0, 38)
    TalkEnd(0xE)
    Return()

    # Function_39_9921 end

    def Function_40_9A89(): pass

    label("Function_40_9A89")

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
            "#11PThank you very much\x01",
            "for joining me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PThe theme of this interview will be\x01",
            "the terror attack that occurred at\x01",
            "the Trade Conference some time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PFirst of all, I'd\x01",
            "like to confirm the\x01",
            "terrorist groups...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#11PYou know them, don't you, Mr. Lloyd?\x02",
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
            "#1KThe terror groups that attacked the conference were?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Imperial Liberation Front of Erebonia\x01",          # 0
            "Anti-Immigration Policy League of Calvard\x01",      # 1
            "Both of Them\x01",                                   # 2
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
        (0, "loc_9DA5"),
        (1, "loc_9E78"),
        (2, "loc_9F4B"),
        (SWITCH_DEFAULT, "loc_A05A"),
    )


    label("loc_9DA5")


    ChrTalk(
        0x101,
        (
            "#00001F#5PYes, the "Imperial Liberation\x01",
            "Front" of Erebonia.\x02\x03",
            "#00011F(―Wait, \x01",
            "it wasn't just them.)\x02\x03",
            "#00003FAlso, the immigration opposition\x01",
            "faction of Calvard, the "Anti- \x01",
            "Immigration Policy League".\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A05A")

    label("loc_9E78")


    ChrTalk(
        0x101,
        (
            "#00001F#5PYes, the immigration opposition\x01",
            "faction of Calvard, the "Anti-\x01",
            "Immigration Policy League".\x02\x03",
            "#00011F(―Wait, \x01",
            "it wasn't just them.)\x02\x03",
            "#00003FAlso, the "Imperial Liberation \x01",
            "Front" of Erebonia.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A05A")

    label("loc_9F4B")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00006F#5PYes, the criminals were terror groups\x01",
            "from the two major powers.\x02\x03",
            "#00008FOne of them was the "Imperial\x01",
            "Liberation Front" of Erebonia.\x02\x03",
            "#00013FThe other was the immigration\x01",
            "opposition faction of Calvard, the\x01",
            ""Anti-Immigration Policy League".\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A05A")

    label("loc_A05A")


    ChrTalk(
        0xE,
        "#11PYes, it was surely those two.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PI won't reference here about their\x01",
            "backgrounds and principles, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PIt is a fact that those two,\x01",
            "sharing nothing in common until\x01",
            "now, put up a united front.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PAccording to rumors, it is said a secret\x01",
            "organization called "Ouroboros" was\x01",
            "cooperating with them...\x02",
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
            "#00013F#5PThe Society of "Ouroboros"...\x02\x03",
            "#00008F(Come to think of it,\x01",
            "the terrorists were using \x01",
            "Archaisms at the conference.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#6PMr. Nielsen, you know\x01",
            "of the "Society"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PYes. Although it's certain they\x01",
            "are something of an enigma.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PBut, it seems you all are aware\x01",
            "of them as well, aren't you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00306F#5PWell, just a little bit.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211F#6PThe more we learn about them,\x01",
            "the more shady they seem...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11P...At any rate, it seems certain they're\x01",
            "a completely obscure and mysterious\x01",
            "group working for some purpose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PIt's useless to try to\x01",
            "deduce their objective\x01",
            "at the present time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#5PI agree with that assessment.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#11PThen, let's move on to the next topic.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PThe next thing I want to confirm―\x01",
            "is the positions of the two major\x01",
            "powers on this terror attack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PAccording to sources, each country\x01",
            "secretly employed an outside force.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PThose forces contributed greatly to\x01",
            "the resolution of the incident, but―\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PAlthough they knew about the terror attack,\x01",
            "they left them at large, I would dare say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PWhat were both leaders trying to achieve? \x01",
            "What do you think, Mr. Lloyd?\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x1, 1)
    ClearScenarioFlags(0x1, 2)
    ClearScenarioFlags(0x1, 3)

    label("loc_A6B0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AAD6")
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
            "#1KWhat were Chancellor Osborne and President\x01",
            "Rocksmith's objectives regarding the terror incident?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Expose Terror Groups\x01",           # 0
            "Contain Opposing Factions\x01",      # 1
            "Mayor Dieter's Retirement\x01",      # 2
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
        (0, "loc_A7C8"),
        (1, "loc_A882"),
        (2, "loc_A9E3"),
        (SWITCH_DEFAULT, "loc_AAC3"),
    )


    label("loc_A7C8")


    ChrTalk(
        0x101,
        (
            "#00005F#5P(Could it have been to\x01",
            "expose the terror groups?)\x02\x03",
            "#00006F(...No, that's not it. To begin with, \x01",
            "both nations already knew about \x01",
            "their respective terror groups.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_AAC3")

    label("loc_A882")


    ChrTalk(
        0x101,
        (
            "#00003F#5PThey were trying to contain the opposing\x01",
            "factions which side with and employ terrorists―\x02\x03",
            "I think both leaders' goal was\x01",
            "to try to keep them in check.\x02\x03",
            "#00008FChancellor Osborne is trying\x01",
            "to hold back noble influence.\x02\x03",
            "#00001FPresident Rocksmith was\x01",
            "trying to restrain rogue\x01",
            "elements in his own country.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A9DB")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A9DB")

    SetScenarioFlags(0x1, 1)
    Jump("loc_AAC3")

    label("loc_A9E3")


    ChrTalk(
        0x101,
        (
            "#00008F#5P(The terrorist incident is proof that\x01",
            "our autonomous state is insecure.)\x02\x03",
            "(They were trying to use it to\x01",
            "force Mayor Dieter's retirement...)\x02\x03",
            "#00011F(No, no. That's the wrong\x01",
            "scale for this question.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_AAC3")

    label("loc_AAC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_AAD1")
    Jump("loc_AAD6")

    label("loc_AAD1")

    Jump("loc_A6B0")

    label("loc_AAD6")


    ChrTalk(
        0xE,
        (
            "#11PHmm, it's as you say.\x01",
            "Indeed, that's what they\x01",
            "were most likely after.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PAnd indeed, voices against those\x01",
            "factions have risen in both\x01",
            "countries since the incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#6PI see. So it became material\x01",
            "for a political attack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PYou said what was their number one\x01",
            "objective, Mr. Lloyd, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PCould you tell me, if you want,\x01",
            "what could've been another objective?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#5PWell...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)

    ChrTalk(
        0x102,
        "#00108F#6PLloyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10108F#5P............\x02",
    )

    CloseMessageWindow()
    OP_64(0x101)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00006F#5PAnother big objective―\x02\x03",
            "#00013FI think it was to gain a real foothold\x01",
            "in their advance into Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#11PHm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F#6PAdvance into Crossbell―\x02\x03",
            "#10301FThat's easy to understand. Both countries\x01",
            "forwarded the proposal to station their\x01",
            "troops in Crossbell at the Trade Conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#6PThe terror attack was more proof that\x01",
            "Crossbell security is insufficient―\x02\x03",
            "#00201FThat they needed to get Crossbell\x01",
            "to agree to those proposals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#6PYes. That means the "Non-\x01",
            "Aggression Pact" signed in\x01",
            "Liberl has lost its effect...\x02\x03",
            "#00108FAnd with the independence proposal,\x01",
            "public opinion in those countries\x01",
            "has turned toward Crossbell.\x02\x03",
            "#00101FIt could be connected to a need to\x01",
            "deflect opposition or dissatisfaction\x01",
            "within their own countries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F#6PTheir objective was all of that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#5P*sigh*. I guess you could say\x01",
            "killin' many birds with one stone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11P...Hm. It seems you all have\x01",
            "considered this in detail.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11P―Then, let us move\x01",
            "to our final point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PIt's clear this incident\x01",
            "was orchestrated by those\x01",
            "two countries, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PDoes this mean they\x01",
            "have an alliance?\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x1, 1)
    ClearScenarioFlags(0x1, 2)
    ClearScenarioFlags(0x1, 3)

    label("loc_B15A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B3F5")
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
            "#1KHave the Empire and Republic formed an\x01",
            "alliance through the terror incident?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "A Temporary One\x01",          # 0
            "A Permanent One\x01",          # 1
            "Out of the Question\x01",      # 2
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
        (0, "loc_B249"),
        (1, "loc_B2B1"),
        (2, "loc_B33A"),
        (SWITCH_DEFAULT, "loc_B3E2"),
    )


    label("loc_B249")


    ChrTalk(
        0x101,
        (
            "#00008F#5P(A temporary one...\x01",
            "Why do I think that?)\x02\x03",
            "#00003F(No, it can't be\x01",
            "that simple.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_B3E2")

    label("loc_B2B1")


    ChrTalk(
        0x101,
        (
            "#00005F#5P(I don't believe it. Could they\x01",
            "have formed a permanent alliance?)\x02\x03",
            "#00006F(―Nonsense. That\x01",
            "would never happen.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_B3E2")

    label("loc_B33A")


    ChrTalk(
        0x101,
        (
            "#5P#00003FNo... I think it's\x01",
            "out of the question.\x02\x03",
            "#00013F──Both countries' ultimate objective\x01",
            "is singular rule over Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B3DA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B3DA")

    SetScenarioFlags(0x1, 1)
    Jump("loc_B3E2")

    label("loc_B3E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_B3F0")
    Jump("loc_B3F5")

    label("loc_B3F0")

    Jump("loc_B15A")

    label("loc_B3F5")


    ChrTalk(
        0xE,
        "#11PYes― Exactly right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PIn the end, this incident\x01",
            "was a temporary step.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PCrossbell holds too much\x01",
            "power as a buffer zone―\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PAnd they want to obtain control over\x01",
            "such a unique and important land...\x01",
            "It implied the confirmation of such an intention.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10113F#5PThat's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108F#6P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00211F#6P...Too suggestive.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#6PIt was nothing more than preliminary works for\x01",
            "when they'll go at each other in earnest, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PYes── The intelligence war\x01",
            "between the countries will only\x01",
            "grow more intense from here on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PThe increase in activity by\x01",
            "crime syndicates and jaegers\x01",
            "may be due to that situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PDue to that, the mysterious\x01",
            "accidents of the past may\x01",
            "make a reappearance──\x02",
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
        "#00305F#5PMysterious accidents...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205F#6PWhat do you mean by...\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)

    ChrTalk(
        0xE,
        (
            "#11PNo── It seems I said\x01",
            "something I shouldn't have.\x02",
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
            "#11PWe sorted several things out.\x01",
            "I'm glad I asked you all to join me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#11PI thank you for your cooperation.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F#5P...We feel the same. Thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F#6PI feel like we understand the\x01",
            "current situation a lot better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106F#5P...I really learned a lot.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#11PThank you for saying so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PIf there's another chance, I would love\x01",
            "to speak with you all again like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#5PYes, we'll be looking forward to it.\x02",
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
            "Quest [Terror Incident Coverage Support]\x07\x00",
            " completed!\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BA94")
    OP_2C(0x89, 0x2)
    Jump("loc_BAA8")

    label("loc_BA94")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BAA8")
    OP_2C(0x89, 0x1)

    label("loc_BAA8")

    OP_29(0x89, 0x1, 0x0)
    OP_29(0x89, 0x4, 0x10)
    EventEnd(0x5)
    Return()

    # Function_40_9A89 end

    SaveToFile()

Try(main)
