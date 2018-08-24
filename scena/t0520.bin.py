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
        "Function_5_913",          # 05, 5
        "Function_6_917",          # 06, 6
        "Function_7_1CB5",         # 07, 7
        "Function_8_2B90",         # 08, 8
        "Function_9_2CBA",         # 09, 9
        "Function_10_2E7B",        # 0A, 10
        "Function_11_2F6D",        # 0B, 11
        "Function_12_3093",        # 0C, 12
        "Function_13_322D",        # 0D, 13
        "Function_14_33B2",        # 0E, 14
        "Function_15_3463",        # 0F, 15
        "Function_16_3C98",        # 10, 16
        "Function_17_3DCD",        # 11, 17
        "Function_18_4412",        # 12, 18
        "Function_19_480F",        # 13, 19
        "Function_20_4D40",        # 14, 20
        "Function_21_4F1A",        # 15, 21
        "Function_22_4F1E",        # 16, 22
        "Function_23_5019",        # 17, 23
        "Function_24_529D",        # 18, 24
        "Function_25_546E",        # 19, 25
        "Function_26_5608",        # 1A, 26
        "Function_27_6296",        # 1B, 27
        "Function_28_6382",        # 1C, 28
        "Function_29_639E",        # 1D, 29
        "Function_30_63CE",        # 1E, 30
        "Function_31_63FE",        # 1F, 31
        "Function_32_641A",        # 20, 32
        "Function_33_645E",        # 21, 33
        "Function_34_64A2",        # 22, 34
        "Function_35_79E5",        # 23, 35
        "Function_36_8364",        # 24, 36
        "Function_37_8B5D",        # 25, 37
        "Function_38_93D5",        # 26, 38
        "Function_39_9631",        # 27, 39
        "Function_40_97A0",        # 28, 40
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
            "The Fried Fish recipe is\x01",
            "written here.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_90F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_90F")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Learned the \x07\x00",
            ""Fried Fish"\x07\x00\x01",
            "recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_90F")

    TalkEnd(0xFF)
    Return()

    # Function_4_7F2 end

    def Function_5_913(): pass

    label("Function_5_913")

    Call(0, 6)
    Return()

    # Function_5_913 end

    def Function_6_917(): pass

    label("Function_6_917")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_945")
    Call(0, 35)
    Return()

    label("loc_945")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x175, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x175, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_96E")
    Call(0, 36)
    Return()

    label("loc_96E")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_97B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CB1")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",        # 0
            "Shop\x01",        # 1
            "Rest\x01",        # 2
            "Cancel\x01",      # 3
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
    Jump("loc_1CAC")

    label("loc_9FC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A1C")
    OP_AF(0x50)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1CAC")

    label("loc_A1C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A30")
    Jump("loc_1CAC")

    label("loc_A30")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A48")
    TalkEnd(0x8)
    Return()

    label("loc_A48")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CAC")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_B12")

    ChrTalk(
        0x8,
        (
            "Haha. If you eat our steak\x01",
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
    Jump("loc_1CAC")

    label("loc_B12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_CDE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C13")

    ChrTalk(
        0x8,
        (
            "After the disturbance in the\x01",
            "city, some tired bracers and\x01",
            "a crying girl came here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They said they participated\x01",
            "in the Crossbell City\x01",
            "liberation operation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We, who cooperated with\x01",
            "the resistance, want to\x01",
            "thank them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CD9")

    label("loc_C13")


    ChrTalk(
        0x8,
        (
            "It seems the bracers resting below\x01",
            "participated in the Crossbell City\x01",
            "liberation operation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "A different bracer came earlier and\x01",
            "helped us defeat the monster...\x01",
            "We're really in their debt.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CD9")

    Jump("loc_1CAC")

    label("loc_CDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_E05")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D9A")

    ChrTalk(
        0x8,
        (
            "Mireille, the resistance\x01",
            "leader, is here to\x01",
            "resupply.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You guys are doing a big\x01",
            "operation before long,\x01",
            "right?\x02",
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
    Jump("loc_E00")

    label("loc_D9A")


    ChrTalk(
        0x8,
        (
            "You guys are doing a big\x01",
            "operation before long,\x01",
            "right?\x02",
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

    label("loc_E00")

    Jump("loc_1CAC")

    label("loc_E05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_10CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F2C")
    TurnDirection(0x8, 0x104, 0)

    ChrTalk(
        0x8,
        (
            "Randy, you've separated\x01",
            "from the resistance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304FYeah. A certain daughter I\x01",
            "have to save is waiting for\x01",
            "me.\x02\x03",
            "#00302FLady, take care of the people\x01",
            "of Mainz, Mireille and the\x01",
            "others for me for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha, understood. You be\x01",
            "careful yourself.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AD, 7)
    Jump("loc_10C9")

    label("loc_F2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1056")

    ChrTalk(
        0x8,
        (
            "We told the children of the resistance\x01",
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
            "It's not a big deal, but\x01",
            "I want to do everything\x01",
            "I can for them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10C9")

    label("loc_1056")


    ChrTalk(
        0x8,
        (
            "I want the resistance to\x01",
            "do their best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's not a big deal, but\x01",
            "I want to do everything\x01",
            "I can for them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10C9")

    Jump("loc_1CAC")

    label("loc_10CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1247")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11ED")

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
            "...But, what was their\x01",
            "objective? That's what I\x01",
            "don't understand.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1242")

    label("loc_11ED")


    ChrTalk(
        0x8,
        (
            "That armed group... What\x01",
            "was their object?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I really don't\x01",
            "understand that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1242")

    Jump("loc_1CAC")

    label("loc_1247")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_12C5")

    ChrTalk(
        0x8,
        (
            "Hmm, the rain feels\x01",
            "good.\x02",
        )
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
    Jump("loc_1CAC")

    label("loc_12C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_159F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x175, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_147D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13CB")

    ChrTalk(
        0x8,
        (
            "Thank goodness the\x01",
            "Liberl-made drinking\x01",
            "glasses arrived.\x02",
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
            "Haha. Anyway, that must\x01",
            "have been difficult.\x01",
            "Allow me to thank you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1478")

    label("loc_13CB")


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
            "Haha. Anyway, that must\x01",
            "have been difficult.\x01",
            "Allow me to thank you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1478")

    Jump("loc_159A")

    label("loc_147D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_154F")

    ChrTalk(
        0x8,
        (
            "Marlowe finally got his\x01",
            "energy back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even from an outsider's point\x01",
            "of view, Lycka's way of\x01",
            "comforting him was cold...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, if that restored\x01",
            "his energy, I guess it's\x01",
            "all right.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_159A")

    label("loc_154F")


    ChrTalk(
        0x8,
        (
            "Well, at least Marlowe's\x01",
            "in good spirits... Case\x01",
            "closed for now, huh.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_159A")

    Jump("loc_1CAC")

    label("loc_159F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_174A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1697")

    ChrTalk(
        0x8,
        (
            "Recently, I've been\x01",
            "getting the impression\x01",
            "Marlowe hates Lycka.\x02",
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
            "Lycka doesn't realize\x01",
            "this, so it's a tricky\x01",
            "conversation...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1745")

    label("loc_1697")


    ChrTalk(
        0x8,
        (
            "Still, Gantz has some good sides\x01",
            "too... To think he'd go to speak\x01",
            "directly for his friend...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, his partner is Lycka\x01",
            "so it looks like this'll\x01",
            "be a tough battle.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1745")

    Jump("loc_1CAC")

    label("loc_174A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1850")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1807")

    ChrTalk(
        0x8,
        (
            "I heard Marlowe\x01",
            "approached Lycka drunk\x01",
            "yesterday...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "She flatly rejected him,\x01",
            "completely sinking that\x01",
            "ship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Kuhuhu. It was fun to\x01",
            "watch, though.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_184B")

    label("loc_1807")


    ChrTalk(
        0x8,
        "Poor Marlowe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I think I'll give him a\x01",
            "snack on the house.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_184B")

    Jump("loc_1CAC")

    label("loc_1850")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1976")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18DE")

    ChrTalk(
        0x8,
        (
            "The miners have the day\x01",
            "off. They've been\x01",
            "drinking all day.\x02",
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
    Jump("loc_1971")

    label("loc_18DE")


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
            "Haha. Well, that's what's\x01",
            "fun about being in this\x01",
            "business, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1971")

    Jump("loc_1CAC")

    label("loc_1976")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1B3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AAF")

    ChrTalk(
        0x8,
        (
            "Yesterday, Lycka came,\x01",
            "got drunk, and showed\x01",
            "off her drunken laugh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "That girl is normally\x01",
            "antisocial, but she's really\x01",
            "cute when she smiles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It seems Marlowe noticed\x01",
            "this, and totally fell\x01",
            "for her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Kuhuhu. Love affairs are\x01",
            "my favorite. I wonder\x01",
            "what'll happen next.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1B38")

    label("loc_1AAF")


    ChrTalk(
        0x8,
        (
            "It looks like Marlowe\x01",
            "fell for Lycka at\x01",
            "yesterday's party.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Kuhuhu. Love affairs are\x01",
            "my favorite. I wonder\x01",
            "what'll happen next.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B38")

    Jump("loc_1CAC")

    label("loc_1B3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_1CAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C2D")

    ChrTalk(
        0x8,
        (
            "Hey, welcome. You came a\x01",
            "long way to get here,\x01",
            "didn't you.\x02",
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
            "We serve large portions,\x01",
            "so if you like, please\x01",
            "have something.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1CAC")

    label("loc_1C2D")


    ChrTalk(
        0x8,
        (
            "You came all the way\x01",
            "here, so if you like,\x01",
            "please have something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We've got a full menu\x01",
            "that will fill you right\x01",
            "up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CAC")

    Jump("loc_97B")

    label("loc_1CB1")

    TalkEnd(0x8)
    Return()

    # Function_6_917 end

    def Function_7_1CB5(): pass

    label("Function_7_1CB5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1E6C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DDD")

    ChrTalk(
        0x9,
        (
            "Both Gantz and Marlowe\x01",
            "looked happy when they\x01",
            "left for mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I wonder if they're going to\x01",
            "have a party to celebrate\x01",
            "the reopening tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Oh brother. What a\x01",
            "pain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "But, with the situation\x01",
            "outside, it's a relief that\x01",
            "things are back to normal.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E67")

    label("loc_1DDD")


    ChrTalk(
        0x9,
        (
            "With the situation outside,\x01",
            "it's a relief that things\x01",
            "are back to normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Well, I'm here\x01",
            "tonight, so might as\x01",
            "well enjoy it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E67")

    Jump("loc_2B8C")

    label("loc_1E6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2019")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F7D")

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
            "I bet there are a lot of\x01",
            "women who follow her\x01",
            "example.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F75")

    ChrTalk(
        0x109,
        (
            "#10104FYes... I believe that's\x01",
            "true.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F75")

    SetScenarioFlags(0x0, 1)
    Jump("loc_2014")

    label("loc_1F7D")


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
            "I bet there's a lot of\x01",
            "women who follow that\x01",
            "leader's example.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2014")

    Jump("loc_2B8C")

    label("loc_2019")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_22B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2168")

    ChrTalk(
        0x9,
        (
            "I was reading the latest\x01",
            "volume of the serial novel\x01",
            "I've been following lately...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "But in this situation, we won't be\x01",
            "able to get new volumes in, so I'm\x01",
            "holding off on it for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...If you like, I'll\x01",
            "give it to you.\x02",
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
    Jump("loc_22B1")

    label("loc_2168")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2224")

    ChrTalk(
        0x9,
        (
            "Gantz and Marlowe have\x01",
            "been coming here during\x01",
            "the day, lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Well, with the mine closed\x01",
            "and us unable to go to the city,\x01",
            "I guess there's no other choice.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_22B1")

    label("loc_2224")


    ChrTalk(
        0x9,
        (
            "With the mine closed and us\x01",
            "unable to go to the city, I guess\x01",
            "there's nowhere else to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Haha... It's a pain, but\x01",
            "I'll join them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22B1")

    Jump("loc_2B8C")

    label("loc_22B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_242B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23A9")

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
            "But Marlowe was fine the\x01",
            "whole time. That\x01",
            "encouraged me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...I thought he was\x01",
            "unreliable, but I've\x01",
            "changed my opinion of him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2426")

    label("loc_23A9")


    ChrTalk(
        0x9,
        (
            "Back then... They were\x01",
            "so scary, I couldn't\x01",
            "curse at them as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...I have to thank\x01",
            "Marlowe, who encouraged\x01",
            "me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2426")

    Jump("loc_2B8C")

    label("loc_242B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_24B4")

    ChrTalk(
        0x9,
        (
            "I hate rainy days. The\x01",
            "floor gets wet and it's\x01",
            "a pain to clean...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Carlos ate quickly. I\x01",
            "wonder if he'll be back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B8C")

    label("loc_24B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_25BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2579")

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
            "Like Mr. Gantz asked me,\x01",
            "I told him "Why don't\x01",
            "you cheer up", but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, who cares. I've\x01",
            "gotta clean...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_25B7")

    label("loc_2579")


    ChrTalk(
        0x9,
        "...*sigh*, how dull...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I've got to get to\x01",
            "cleaning.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25B7")

    Jump("loc_2B8C")

    label("loc_25BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_265F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25D7")
    Call(0, 8)
    Jump("loc_265A")

    label("loc_25D7")

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
            "all the bills you've\x01",
            "piled up, Mr. Gantz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Huh...? Oh, that\x01",
            "again...\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)

    label("loc_265A")

    Jump("loc_2B8C")

    label("loc_265F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_27D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2772")

    ChrTalk(
        0x9,
        (
            "Marlowe was acting\x01",
            "strange yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "He talked to me way too\x01",
            "much, and invited me to\x01",
            "drink with him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm in a bad mood so I\x01",
            "ignored him. He's\x01",
            "strangely depressed today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "C'mon. What do you want\x01",
            "me to say? Really, it's\x01",
            "a bother.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_27CC")

    label("loc_2772")


    ChrTalk(
        0x9,
        (
            "Seriously. Marlowe was\x01",
            "really annoying\x01",
            "yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "This is why I avoid\x01",
            "drunks...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27CC")

    Jump("loc_2B8C")

    label("loc_27D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2900")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2899")

    ChrTalk(
        0x9,
        (
            "Just because it's a\x01",
            "vacation day, how dare\x01",
            "he drink all day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "When I drink, I get drunk immediately\x01",
            "and can't remember anything, so I\x01",
            "don't think it's a good idea.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_28FB")

    label("loc_2899")


    ChrTalk(
        0x9,
        (
            "How dare he drink all\x01",
            "day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Well, whatever. Looks\x01",
            "like everyone's having a\x01",
            "good time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28FB")

    Jump("loc_2B8C")

    label("loc_2900")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2A3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29B6")

    ChrTalk(
        0x9,
        "My head hurts...\x02",
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
        (
            "...I wonder if I did\x01",
            "anything.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A36")

    label("loc_29B6")


    ChrTalk(
        0x9,
        (
            "Ah, my head hurts... I\x01",
            "can't remember anything\x01",
            "from yesterday at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...I wonder if I did\x01",
            "anything I shouldn't\x01",
            "have.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A36")

    Jump("loc_2B8C")

    label("loc_2A3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_2B8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AF6")

    ChrTalk(
        0x9,
        (
            "Gantz lost big again\x01",
            "gambling the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm glad he stopped grumbling and\x01",
            "complaining just like last time,\x01",
            "but... He's a stubborn one, Gantz is.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2B8C")

    label("loc_2AF6")


    ChrTalk(
        0x9,
        (
            "Even though Gantz lost at\x01",
            "gambling recently, his grumbling\x01",
            "and complaining stopped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...If he lost, how is he\x01",
            "going to pay his bill,\x01",
            "though?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B8C")

    TalkEnd(0xFE)
    Return()

    # Function_7_1CB5 end

    def Function_8_2B90(): pass

    label("Function_8_2B90")

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
            "Umm, Gantz? Why are you\x01",
            "encouraging Marlowe and\x01",
            "I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm telling you. His\x01",
            "depression lately has\x01",
            "nothing to do with me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "W-Well, if pushed, I'd\x01",
            "say there's something\x01",
            "big going down...\x02",
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

    # Function_8_2B90 end

    def Function_9_2CBA(): pass

    label("Function_9_2CBA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2CCB")
    Jump("loc_2E77")

    label("loc_2CCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2E28")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DAD")

    ChrTalk(
        0xA,
        (
            "We finished the septium\x01",
            "transport this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "The rain is heavy and the\x01",
            "surface wet, so it was\x01",
            "hard getting any traction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Even choosing the times\x01",
            "with less peril is a\x01",
            "driving skill.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2E23")

    label("loc_2DAD")


    ChrTalk(
        0xA,
        (
            "We finished the septium\x01",
            "transport this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Even choosing the times\x01",
            "with less peril is a\x01",
            "driving skill.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E23")

    Jump("loc_2E77")

    label("loc_2E28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2E36")
    Jump("loc_2E77")

    label("loc_2E36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2E44")
    Jump("loc_2E77")

    label("loc_2E44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2E52")
    Jump("loc_2E77")

    label("loc_2E52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2E60")
    Jump("loc_2E77")

    label("loc_2E60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2E6E")
    Jump("loc_2E77")

    label("loc_2E6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_2E77")

    label("loc_2E77")

    TalkEnd(0xFE)
    Return()

    # Function_9_2CBA end

    def Function_10_2E7B(): pass

    label("Function_10_2E7B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2E8C")
    Jump("loc_2F69")

    label("loc_2E8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2E9A")
    Jump("loc_2F69")

    label("loc_2E9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2EA8")
    Jump("loc_2F69")

    label("loc_2EA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2EB6")
    Jump("loc_2F69")

    label("loc_2EB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2EC4")
    Jump("loc_2F69")

    label("loc_2EC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2F52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EDF")
    Call(0, 11)
    Jump("loc_2F4D")

    label("loc_2EDF")


    ChrTalk(
        0xB,
        (
            "I have to yell at my kid\x01",
            "properly, for his own\x01",
            "sake.\x02",
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

    label("loc_2F4D")

    Jump("loc_2F69")

    label("loc_2F52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2F60")
    Jump("loc_2F69")

    label("loc_2F60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_2F69")

    label("loc_2F69")

    TalkEnd(0xFE)
    Return()

    # Function_10_2E7B end

    def Function_11_2F6D(): pass

    label("Function_11_2F6D")

    OP_4B(0xB, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xD,
        (
            "But, I was scared of the\x01",
            "mine captain's angry\x01",
            "look yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Just like Alec gets when\x01",
            "I scold him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "You've got to scold your\x01",
            "kids. It's for their own\x01",
            "good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'm sure you'll\x01",
            "understand if you become\x01",
            "parents someday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "So that's what it was...\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xD, 0x10)
    SetScenarioFlags(0x0, 7)
    OP_4C(0xB, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_11_2F6D end

    def Function_12_3093(): pass

    label("Function_12_3093")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_30A4")
    Jump("loc_3229")

    label("loc_30A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_30B2")
    Jump("loc_3229")

    label("loc_30B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_313D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30CD")
    Call(0, 13)
    Jump("loc_3138")

    label("loc_30CD")


    ChrTalk(
        0xC,
        (
            "Because of the\x01",
            "situation, I can't even\x01",
            "drink during the day...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Ah, I want to go to the\x01",
            "casino...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3138")

    Jump("loc_3229")

    label("loc_313D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_314B")
    Jump("loc_3229")

    label("loc_314B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3159")
    Jump("loc_3229")

    label("loc_3159")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3167")
    Jump("loc_3229")

    label("loc_3167")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_31F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3182")
    Call(0, 8)
    Jump("loc_31F1")

    label("loc_3182")


    ChrTalk(
        0xC,
        (
            "(For now, I've got to\x01",
            "console Lycka and cheer\x01",
            "up Marlowe.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "(Hopefully, everything\x01",
            "will turn out ok!)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31F1")

    Jump("loc_3229")

    label("loc_31F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3204")
    Jump("loc_3229")

    label("loc_3204")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3212")
    Jump("loc_3229")

    label("loc_3212")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3220")
    Jump("loc_3229")

    label("loc_3220")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_3229")

    label("loc_3229")

    TalkEnd(0xFE)
    Return()

    # Function_12_3093 end

    def Function_13_322D(): pass

    label("Function_13_322D")

    OP_4B(0xC, 0xFF)
    OP_4B(0xF, 0xFF)

    ChrTalk(
        0xC,
        (
            "Aww... Because of the\x01",
            "situation, I can't go to the\x01",
            "city to play at the casino.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "How long am I gonna have\x01",
            "to live with this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "It's pretty tough\x01",
            "without any amusements.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "On the other hand, the mine's\x01",
            "closed, so I can't give work\x01",
            "everything I've got either.\x02",
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
        "All I can do is sigh.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xF, 0x10)
    OP_4C(0xC, 0xFF)
    OP_4C(0xF, 0xFF)
    Return()

    # Function_13_322D end

    def Function_14_33B2(): pass

    label("Function_14_33B2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_33C3")
    Jump("loc_345F")

    label("loc_33C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_33D1")
    Jump("loc_345F")

    label("loc_33D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_33DF")
    Jump("loc_345F")

    label("loc_33DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_33ED")
    Jump("loc_345F")

    label("loc_33ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_33FB")
    Jump("loc_345F")

    label("loc_33FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3448")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3416")
    Call(0, 11)
    Jump("loc_3443")

    label("loc_3416")


    ChrTalk(
        0xD,
        (
            "Yeah, it must be tough,\x01",
            "being a parent.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3443")

    Jump("loc_345F")

    label("loc_3448")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3456")
    Jump("loc_345F")

    label("loc_3456")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_345F")

    label("loc_345F")

    TalkEnd(0xFE)
    Return()

    # Function_14_33B2 end

    def Function_15_3463(): pass

    label("Function_15_3463")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3C97")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3641")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x89, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3626")
    TalkBegin(0xFE)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3518")
    Jump("loc_3562")

    label("loc_3518")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3538")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3562")

    label("loc_3538")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3558")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3562")

    label("loc_3558")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3562")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)

    ChrTalk(
        0xFE,
        (
            "Everyone, thank you for\x01",
            "joining me for an\x01",
            "interview today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If there's another chance,\x01",
            "I'd like to speak with you\x01",
            "all again, if possible.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_363C")

    label("loc_3626")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 7)), scpexpr(EXPR_END)), "loc_3638")
    Call(0, 39)
    Return()

    label("loc_3638")

    Call(0, 37)
    Return()

    label("loc_363C")

    Jump("loc_3C97")

    label("loc_3641")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B18")
    TalkBegin(0xFE)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_36E9")
    Jump("loc_3733")

    label("loc_36E9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3709")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3733")

    label("loc_3709")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3729")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3733")

    label("loc_3729")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3733")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A83")

    ChrTalk(
        0x101,
        "#00000FNielsen―\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "Hmm. That voice is\x01",
            "Lloyd's, isn't it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Why are you in Mainz\x01",
            "today?\x02",
        )
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
            "Nielsen?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes. Actually, I plan to\x01",
            "interview this town's\x01",
            "mayor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'll ask him about the history of\x01",
            "septium mining in this town, and\x01",
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
            "#10100FHow to say this...\x01",
            "You're looking into\x01",
            "things others wouldn't.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. Thanks to that, I've\x01",
            "been able to take all\x01",
            "these detours, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, you all look busy\x01",
            "as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think things will be\x01",
            "difficult going forward,\x01",
            "but please do your best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FSure, and thanks.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16B, 5)
    Jump("loc_3B0C")

    label("loc_3A83")


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
            "Haha. This is a quiet\x01",
            "and calm room, isn't it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B0C")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Jump("loc_3C97")

    label("loc_3B18")

    TalkBegin(0xFE)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3BAC")
    Jump("loc_3BF6")

    label("loc_3BAC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3BCC")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3BF6")

    label("loc_3BCC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3BEC")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3BF6")

    label("loc_3BEC")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3BF6")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)

    ChrTalk(
        0xFE,
        (
            "Haha. This is a quiet\x01",
            "and calm room, isn't it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think I'll take it\x01",
            "easy until it's time for\x01",
            "my interview.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)

    label("loc_3C97")

    Return()

    # Function_15_3463 end

    def Function_16_3C98(): pass

    label("Function_16_3C98")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3CA9")
    Jump("loc_3DC9")

    label("loc_3CA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_3CB7")
    Jump("loc_3DC9")

    label("loc_3CB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3DC9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CD2")
    Call(0, 13)
    Jump("loc_3DC9")

    label("loc_3CD2")

    SetChrSubChip(0xF, 0x2)

    ChrTalk(
        0xF,
        (
            "(The first time I met\x01",
            "Lycka I thought she\x01",
            "wasn't too bad, but...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "(After staying at the bar\x01",
            "awhile, I don't get that\x01",
            "impression at all...)\x02",
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
        (
            "(...I wonder what he's\x01",
            "looking at.)\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_93(0x9, 0x10E, 0x0)
    SetChrSubChip(0xF, 0x0)

    label("loc_3DC9")

    TalkEnd(0xFE)
    Return()

    # Function_16_3C98 end

    def Function_17_3DCD(): pass

    label("Function_17_3DCD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3DDE")
    Jump("loc_440E")

    label("loc_3DDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_4405")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42A6")

    ChrTalk(
        0x10,
        (
            "#07901FRandy, and the Support Section...\x01",
            "Please listen to what I have to say.\x02\x03",
            "#07903FNow that the declaration of\x01",
            "independence is invalid, at least the\x01",
            "State Guard can't act freely anymore.\x02\x03",
            "#07901FNow if we could just do something\x01",
            "about that Barrier surrounding the\x01",
            "city...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FThat will be our best\x01",
            "chance to liberate\x01",
            "Crossbell City, right?\x02",
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
            "#00303FBut, Red Constellation is, of\x01",
            "course, already prepared for\x01",
            "that situation.\x02\x03",
            "#00301FWe've got to start the\x01",
            "operation before they begin\x01",
            "resistance-hunting in earnest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FIt seems best to\x01",
            "hurry...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#07903FAnyway, we'll get ready to begin the\x01",
            "operation.\x02\x03",
            "We have the help of the divine\x01",
            "wolves, so we'll be able to fight Red\x01",
            "Constellation better than before.\x02\x03",
            "#07901FSo please, do something about that\x01",
            "barrier.\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_420F")
    Jump("loc_4259")

    label("loc_420F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_422F")
    OP_52(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4259")

    label("loc_422F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_424F")
    OP_52(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4259")

    label("loc_424F")

    OP_52(0x10, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4259")

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
    Jump("loc_4400")

    label("loc_42A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4390")

    ChrTalk(
        0x10,
        (
            "#07903FAnyway, we'll get ready to begin the\x01",
            "operation.\x02\x03",
            "We have the help of the divine\x01",
            "wolves, so we'll be able to fight Red\x01",
            "Constellation better than before.\x02\x03",
            "#07901FPlease take care of that barrier,\x01",
            "everyone.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4400")

    label("loc_4390")


    ChrTalk(
        0x10,
        (
            "#07903FAnyway, we'll get ready\x01",
            "to begin the operation.\x02\x03",
            "#07901FPlease take care of that\x01",
            "barrier, everyone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4400")

    Jump("loc_440E")

    label("loc_4405")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_440E")

    label("loc_440E")

    TalkEnd(0xFE)
    Return()

    # Function_17_3DCD end

    def Function_18_4412(): pass

    label("Function_18_4412")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4712")

    ChrTalk(
        0x11,
        (
            "#00802F#30W...Everyone. Be\x01",
            "extremely careful, ok?\x02\x03",
            "#00808FDoing your best is fine,\x01",
            "but don't end up like\x01",
            "Pater-Mater, you hear?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah... I know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00308FIf you think about it,\x01",
            "we owe our very lives to\x01",
            "you guys...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F...I would have been nice if\x01",
            "we talked longer when we met\x01",
            "at the workshop earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#00808F#30WYeah... I would have\x01",
            "liked to talk longer\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x11)

    ChrTalk(
        0x11,
        (
            "#00804F#30W...But no matter what, I'm\x01",
            "worried about Renne.\x02\x03",
            "#00800FThese experiences I've had over\x01",
            "the past half year have made me\x01",
            "stronger in a real sense...\x02\x03",
            "#00802FMy precious friends are here\x01",
            "with me, so I'm sure I'll be\x01",
            "able to get through it...\x02",
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
            "#00100FPlease say hello for us\x01",
            "when she wakes up.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_480B")

    label("loc_4712")


    ChrTalk(
        0x11,
        (
            "#00804F#30WNo matter what, I'm worried\x01",
            "about Renne.\x02\x03",
            "#00800FThese experiences I've had over\x01",
            "the past half year have made me\x01",
            "stronger in a real sense...\x02\x03",
            "#00802FMy precious friends are here\x01",
            "with me, so I'm sure I'll be\x01",
            "able to get through it...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_480B")

    TalkEnd(0xFE)
    Return()

    # Function_18_4412 end

    def Function_19_480F(): pass

    label("Function_19_480F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CA6")

    ChrTalk(
        0x12,
        (
            "#00903F#30W...It seems Dr. Novartis\x01",
            "has already left this land.\x02\x03",
            "#00901FIt must be a relief to know\x01",
            "Ouroboros will not oppose\x01",
            "you any further, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FHonestly, we have no\x01",
            "idea what they were\x01",
            "after.\x02\x03",
            "#00003FIt seems like they're\x01",
            "planning something in\x01",
            "Erebonia, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#00903F#30W...The "Phantom Blaze\x01",
            "Plan", right?\x02\x03",
            "#00901FIt looks like a large-scale\x01",
            "plan based on the events in\x01",
            "Crossbell, but...\x02\x03",
            "#00908F...I'm worried about\x01",
            "Olivier and the others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00205FOlivier, you said...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FYou must be talking\x01",
            "about Prince Olivert.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#00903F#30WYes. Ever since the start of\x01",
            "the civil war, we haven't been\x01",
            "able to get in touch with him.\x02\x03",
            "#00908FAs long as Muller's with him,\x01",
            "I think he'll be safe, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108FEven so, I'm worried...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CA1")
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x12,
        (
            "#00900F#30WThat's right...\x01",
            "Everyone, will you take\x01",
            "this?\x02",
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
        "#00005FThis is...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#00900F#30WPater-Mater dropped this\x01",
            "during his final\x01",
            "moments.\x02\x03",
            "#00903F...It's probably an\x01",
            ""Aion" part. You might\x01",
            "find a good use for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FUnderstood... We'll\x01",
            "gladly accept it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CA1")

    Jump("loc_4D3C")

    label("loc_4CA6")


    ChrTalk(
        0x12,
        (
            "#00903F#30WThat Azure Tree...\x02\x03",
            "I think it exceeds even\x01",
            "the scale of the Liber Ark\x01",
            "that appeared in Liberl.\x02\x03",
            "#00900FPlease, be extremely\x01",
            "careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D3C")

    TalkEnd(0xFE)
    Return()

    # Function_19_480F end

    def Function_20_4D40(): pass

    label("Function_20_4D40")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E39")

    ChrTalk(
        0x13,
        (
            "#03900FPater-Mater's logic unit\x01",
            "was not originally designed\x01",
            "for autonomous functions.\x02\x03",
            "You could say he obtained a\x01",
            ""heart" through meeting\x01",
            "Renne...\x02\x03",
            "#03903F...I've been a doll maker\x01",
            "for decades. I still have\x01",
            "much to learn.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_4F16")

    label("loc_4E39")


    ChrTalk(
        0x13,
        (
            "#03900F...This incident might have an\x01",
            "unexpectedly positive effect on\x01",
            "Renne.\x02\x03",
            "#03903FThis was a good experience for\x01",
            "her, as she has not experienced\x01",
            ""parting" in the past...\x02\x03",
            "#03900FEverything begins now, doesn't\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F16")

    TalkEnd(0xFE)
    Return()

    # Function_20_4D40 end

    def Function_21_4F1A(): pass

    label("Function_21_4F1A")

    Call(0, 22)
    Return()

    # Function_21_4F1A end

    def Function_22_4F1E(): pass

    label("Function_22_4F1E")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FBA")

    ChrTalk(
        0x14,
        (
            "#03317F#2S#40W...Pater-Mater...\x02\x03",
            "#2S#40W...Why...... ...Why did\x01",
            "you...\x02",
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
        "#00103F...Let's leave her be.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_5015")

    label("loc_4FBA")


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
            "Renne, tired of weeping,\x01",
            "is sleeping.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_5015")

    TalkEnd(0x14)
    Return()

    # Function_22_4F1E end

    def Function_23_5019(): pass

    label("Function_23_5019")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51C3")

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
            "We've exterminated the wanted monsters\x01",
            "in the surrounding areas, so we're safe\x01",
            "for now... is what I'd like to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The emotional scars the people of Mainz suffered\x01",
            "from the incident are pretty severe. There are\x01",
            "people so anxious, they can't sleep at night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We consulted with Michel\x01",
            "and decided to extend\x01",
            "our stay here.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_5299")

    label("loc_51C3")


    ChrTalk(
        0xFE,
        (
            "The emotional scars the people of Mainz suffered\x01",
            "from the incident are pretty severe. There are\x01",
            "people so anxious, they can't sleep at night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We consulted with Michel\x01",
            "and decided to extend\x01",
            "our stay here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5299")

    TalkEnd(0xFE)
    Return()

    # Function_23_5019 end

    def Function_24_529D(): pass

    label("Function_24_529D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53C5")

    ChrTalk(
        0xFE,
        (
            "Because of that attack,\x01",
            "St. Ursula Hospital has\x01",
            "its hands full.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's why I'm taking responsibility\x01",
            "for healing as many patients as\x01",
            "possible, right here in Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Things are pretty difficult...\x01",
            "But it's in times like these that\x01",
            "we have to divide and conquer.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_546A")

    label("loc_53C5")


    ChrTalk(
        0xFE,
        (
            "I'm taking responsibility for\x01",
            "healing as many patients as\x01",
            "possible, right here in Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's times like these\x01",
            "that make me glad I got\x01",
            "my medical license.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_546A")

    TalkEnd(0xFE)
    Return()

    # Function_24_529D end

    def Function_25_546E(): pass

    label("Function_25_546E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_556B")

    ChrTalk(
        0xFE,
        (
            "My partner Wenzel are\x01",
            "working separately\x01",
            "today.\x02",
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
            "Exterminating monsters and\x01",
            "such is tougher, but we'll\x01",
            "get through it somehow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 3)
    Jump("loc_5604")

    label("loc_556B")


    ChrTalk(
        0xFE,
        (
            "My partner Wenzel are\x01",
            "working separately\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Exterminating monsters and such\x01",
            "is tougher, but we'll get through\x01",
            "this labor shortage somehow.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5604")

    TalkEnd(0xFE)
    Return()

    # Function_25_546E end

    def Function_26_5608(): pass

    label("Function_26_5608")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5750")
    BeginChrThread(0x109, 1, 0, 27)
    WaitChrThread(0x109, 1)
    Sleep(600)

    label("loc_5750")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_576D")
    BeginChrThread(0x105, 1, 0, 27)
    WaitChrThread(0x105, 1)
    Sleep(600)

    label("loc_576D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_578A")
    BeginChrThread(0x106, 1, 0, 27)
    WaitChrThread(0x106, 1)
    Sleep(600)

    label("loc_578A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_57A7")
    BeginChrThread(0x10A, 1, 0, 27)
    WaitChrThread(0x10A, 1)
    Sleep(600)

    label("loc_57A7")

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
        (
            "#5P#00102FSo this is where you\x01",
            "were, huh...\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7568", 0)

    ChrTalk(
        0x104,
        (
            "#5P#00300FI heard. That giant doll\x01",
            "got splendidly beaten,\x01",
            "huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#00202FAs expected of your\x01",
            "Pater-Mater.\x02",
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
            "#12P#00903F#30W...Well, the entire fact\x01",
            "that we won was due to\x01",
            ""his" sacrifice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#5P#00005FHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#5P#00105FBy the way... How is\x01",
            "Renne?\x02",
        )
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

    def lambda_5B1A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_5B1A)
    Sleep(50)

    def lambda_5B2A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_5B2A)
    Sleep(50)

    def lambda_5B3A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_5B3A)
    Sleep(50)

    def lambda_5B4A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_5B4A)
    Sleep(50)

    def lambda_5B5A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_5B5A)
    Sleep(50)

    def lambda_5B6A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x5, 1, lambda_5B6A)
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
        (
            "#00203F...So this is where you\x01",
            "were.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#11P#03903FYes... I received their\x01",
            "message.\x02\x03",
            "#03900FTerrible things are happening,\x01",
            "but since Pater-Mater has\x01",
            "died, I had to show up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FThat doll... died?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305FWhoa, could it be...?\x02",
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
            "#12P#00808F#30W...Yeah... That giant\x01",
            "doll went to the sky...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#12P#00908F#30W...It probably used its\x01",
            "self-destruct function.\x02\x03",
            "#00903FAccording to its own\x01",
            "judgment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00003F...So that's what\x01",
            "happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#5P#00208FA machine made that kind\x01",
            "of decision...?\x02",
        )
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
            "#11P#03317F#2S#40W...*sob*... ......Pater-\x01",
            "Mater...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FSleeping because she's\x01",
            "exhausted from cryin',\x01",
            "huh...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F...That's understandable...\x01",
            "I can relate to those\x01",
            "feelings...\x02",
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
            "#11P#03903F...Pater-Mater resigned himself to\x01",
            "his fate...\x02\x03",
            "#03900FI have nothing but respect for his\x01",
            ""heart" that chose to protect the\x01",
            "girl and throw away his own life.\x02\x03",
            "As a doll maker, it is more than I\x01",
            "deserve.\x02",
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
            "#12P#00801F#30W─I heard. I guess things\x01",
            "have gotten tough?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#12P#00900F#30WDepending on when we\x01",
            "heal up, we're planning\x01",
            "on assisting you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00004FThanks, you two.\x02\x03",
            "#00000FBut for right now, give\x01",
            "resting your bodies the\x01",
            "highest priority.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#5P#00303FThat girl isn't a\x01",
            "doll...\x02\x03",
            "#00300FBut right now, we have\x01",
            "to do everything we can\x01",
            "for Keddo.\x02",
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
            "#12P#00904F#30W...May the goddess\x01",
            "protect you. Be\x01",
            "extremely careful.\x02",
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

    # Function_26_5608 end

    def Function_27_6296(): pass

    label("Function_27_6296")

    SetChrPos(0xFE, 94200, 0, 6500, 180)

    def lambda_62AC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_62AC)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_62DC")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 28)
    Jump("loc_6381")

    label("loc_62DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6300")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 29)
    Jump("loc_6381")

    label("loc_6300")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6324")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 30)
    Jump("loc_6381")

    label("loc_6324")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6348")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 31)
    Jump("loc_6381")

    label("loc_6348")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_636C")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 2, 0, 32)
    Jump("loc_6381")

    label("loc_636C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6381")
    BeginChrThread(0xFE, 2, 0, 33)

    label("loc_6381")

    Return()

    # Function_27_6296 end

    def Function_28_6382(): pass

    label("Function_28_6382")

    OP_95(0xFE, 94200, 0, 3030, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_28_6382 end

    def Function_29_639E(): pass

    label("Function_29_639E")

    OP_95(0xFE, 94200, 0, 4850, 2000, 0x0)
    OP_95(0xFE, 93110, 0, 3070, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_29_639E end

    def Function_30_63CE(): pass

    label("Function_30_63CE")

    OP_95(0xFE, 94200, 0, 4850, 2000, 0x0)
    OP_95(0xFE, 95280, 0, 3120, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_30_63CE end

    def Function_31_63FE(): pass

    label("Function_31_63FE")

    OP_95(0xFE, 94210, 0, 4150, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_31_63FE end

    def Function_32_641A(): pass

    label("Function_32_641A")

    OP_95(0xFE, 94260, 0, 5260, 2000, 0x0)
    OP_95(0xFE, 93580, 0, 4960, 2000, 0x0)
    OP_95(0xFE, 93270, 0, 4310, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_32_641A end

    def Function_33_645E(): pass

    label("Function_33_645E")

    OP_95(0xFE, 94260, 0, 5260, 2000, 0x0)
    OP_95(0xFE, 95020, 0, 4960, 2000, 0x0)
    OP_95(0xFE, 95250, 0, 4350, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_33_645E end

    def Function_34_64A2(): pass

    label("Function_34_64A2")

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
            "#00306F#11P─I see. Then, it looks\x01",
            "like this is going to be\x01",
            "another unthinkable story.\x02\x03",
            "#00301FAnd what's more, Keddo has\x01",
            "been...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#02106F#5PHmm. I feel like I can't\x01",
            "actually write an article\x01",
            "this crazy, but...\x02\x03",
            "#02101FYou guys are planning on\x01",
            "doing whatever it takes\x01",
            "to bring her back, right?\x02",
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
        (
            "#00203F#6PThat goes without\x01",
            "saying.\x02",
        )
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
            "#07904F#11P...Randy. Our resistance will\x01",
            "be fine.\x02\x03",
            "#07902FThat condition of your Support\x01",
            "Section friends saving you has\x01",
            "been cleared, right?\x02",
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
        (
            "#00008F#6P...So that's how it is,\x01",
            "huh.\x02",
        )
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
            "#07904F#11POriginally, my resistance was\x01",
            "that of a stubborn CGF member who\x01",
            "couldn't accept the State Guard.\x02\x03",
            "#07902FAs one who separated from the\x01",
            "CGF, should help your own\x01",
            "friends.\x02\x03",
            "#07909FGoing forward, it seems those\x01",
            "wolves will be helping us too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x107,
        (
            "#01203F#6P#3CYes. I once again\x01",
            "instructed them to\x01",
            "assist you.\x02\x03",
            "#01200FI am sure they will be\x01",
            "of help in your battles\x01",
            "in the mountains.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#5P...Thanks, that's a big\x01",
            "help.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6A7D():
        OP_93(0x104, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6A7D)
    Sleep(50)

    def lambda_6A8D():
        OP_93(0x10, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_6A8D)
    Sleep(50)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x10, 0)

    ChrTalk(
        0x104,
        (
            "#00300F#11PLloyd, PeTiote. I'm\x01",
            "coming with you!\x02\x03",
            "As a member of the\x01",
            "Support Section, and a\x01",
            "guardian of KeA!\x02",
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
        "#00204F#6P...Thank goodness.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10709F#5PHaha... That's\x01",
            "heartening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#02103F#5PHmm, that's right.\x02\x03",
            "#02102FI wonder if I can come\x01",
            "along too.\x02",
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

    def lambda_6C5F():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6C5F)
    Sleep(50)

    def lambda_6C6F():
        TurnDirection(0x103, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_6C6F)
    Sleep(50)

    def lambda_6C7F():
        TurnDirection(0x104, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6C7F)
    Sleep(50)

    def lambda_6C8F():
        TurnDirection(0x105, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_6C8F)
    Sleep(50)

    def lambda_6C9F():
        TurnDirection(0x106, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_6C9F)
    Sleep(50)

    def lambda_6CAF():
        TurnDirection(0x10, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_6CAF)
    Sleep(50)

    def lambda_6CBF():
        TurnDirection(0x107, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_6CBF)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x10, 0)
    WaitChrThread(0x107, 0)
    SetChrSubChip(0x107, 0x5)

    ChrTalk(
        0x101,
        "#00011F#6PWhat!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211F#6PWhat's this all of\x01",
            "sudden?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#02104F#5PI mean, going forward, it\x01",
            "looks like all the action\x01",
            "will be centered on you guys.\x02\x03",
            "#02110FAs a journalist I can't very\x01",
            "well overlook it.\x02",
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
            "#10406F#6PHmm. I don't really mind,\x01",
            "though.\x02\x03",
            "#10400FAbbas 'll probably be annoyed\x01",
            "that I'm bringing someone\x01",
            "from the media along, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10706F#6P...It would be bad for\x01",
            "me to end up in an\x01",
            "article as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#02105F#5POh don't worry.\x02\x03",
            "#02104FThere's a mountain of things I\x01",
            "want to write articles about,\x01",
            "but now's not the time for that.\x02\x03",
            "#02106FAll I want to know right now is\x01",
            "what will happen to Crossbell\x01",
            "Independent State.\x02\x03",
            "#02101FWill this new order filled with\x01",
            "deceit be chosen by history, in\x01",
            "the end?\x02",
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
            "#02103F#5PLet me just say this.\x01",
            "The entire continent is\x01",
            "in chaos.\x02\x03",
            "I can't deny that\x01",
            "President Dieter is a\x01",
            "cause, but...\x02\x03",
            "#02101FWill the danger be over,\x01",
            "just by casting him\x01",
            "aside?\x02",
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
            "#07906F#12PHonestly... This might\x01",
            "be difficult.\x02",
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
            "President Dieter is saying the same\x01",
            "things, isn't he.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6P...............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10708F#6P(The assassination drama\x01",
            "100 years ago...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#02106F#5PThough, given the\x01",
            "situation, I can't say\x01",
            "he's correct.\x02\x03",
            "#02100F─And so, that's what I\x01",
            "want to find out.\x02\x03",
            "The path that Crossbell\x01",
            "will choose.\x02\x03",
            "And how that decision\x01",
            "will be recorded in\x01",
            "history.\x02\x03",
            "#02109FIf feel like I'll be\x01",
            "able to see it if I go\x01",
            "with you guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6P...Grace.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302F#12PHmm... You really\x01",
            "thought about it that\x01",
            "much, did you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00202F#6PYou're so serious, it's\x01",
            "like you're like a\x01",
            "different person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#02109F#5PAhaha. Well the main\x01",
            "reason is that it seems\x01",
            "interesting.\x02\x03",
            "#02110FAnd I've got a pipe back\x01",
            "to Crossbell News.\x02\x03",
            "What if I could offer\x01",
            "you info from within the\x01",
            "city?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00004F#6P─Understood. We have no\x01",
            "objection.\x02\x03",
            "#00000FWazy, Rixia. Do either\x01",
            "of you mind?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10710F#6PAs long as I don't end\x01",
            "up in an article.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#6PHaha, I don't mind\x01",
            "either.\x02\x03",
            "#10402FWell, convincing Abbas\x01",
            "might be difficult,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x18,
        (
            "#02109F#5PThanks! I'm in your\x01",
            "debt!\x02\x03",
            "#02110FAll right! Fuelitzer\x01",
            "Prize, here we come!\x02",
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
            "#00012F#6PWell, it's not the case\x01",
            "that we're helping you\x01",
            "out, Grace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00211F#6PWell, it is Grace, after\x01",
            "all.\x02",
        )
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
            "After that, and after greeting Mayor\x01",
            "Bickson, who was secretly cooperating with\x01",
            "the resistance...\x02\x03",
            "They discussed the plan going forward. After\x01",
            "that, Mireille and the others said goodbye\x01",
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

    # Function_34_64A2 end

    def Function_35_79E5(): pass

    label("Function_35_79E5")

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
            "Oh, hello. Welcome to\x01",
            "Red Brick Pavilion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FExcuse us, we're from\x01",
            "the Special Support\x01",
            "Section...\x02",
        )
    )

    CloseMessageWindow()
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
        0x8,
        (
            "Ah, it's you guys. I\x01",
            "heard about you from\x01",
            "Crossbell News.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Then, how about I make you\x01",
            "guys this mining town's\x01",
            "specialty, Stamina Steak?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00206F...Sounds like it'll\x01",
            "make an impact on our\x01",
            "stomachs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yeah. You guys have to at\x01",
            "eat at a bunch of different\x01",
            "places, don't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In that case, I'll bring\x01",
            "them to you bite-size.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F*giggle*. Thank you very\x01",
            "much.\x02",
        )
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
            "Lloyd and friends ate\x01",
            "the Stamina Steak.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x104,
        (
            "#00309F*chew, chew*... Ah, even\x01",
            "though it's bite size,\x01",
            "it's filling as a meal.\x02\x03",
            "#00304FAll steaks should be\x01",
            "like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10102FYes. You can indeed feel\x01",
            "power welling up inside\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha. To a miner,\x01",
            "stamina is life, after\x01",
            "all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Pair this with a beer,\x01",
            "and you'd be ready to\x01",
            "work all day!\x02",
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
            "#00009FHaha. Gantz and the\x01",
            "others seem to enjoy it,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha. They're the strong\x01",
            "men of a mining town,\x01",
            "after all.\x02",
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
        (
            "#00300FYeah, don't mind if we\x01",
            "do.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x2, 0)
    SetScenarioFlags(0x173, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 1)), scpexpr(EXPR_END)), "loc_8045")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8045")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 2)), scpexpr(EXPR_END)), "loc_8062")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8062")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 3)), scpexpr(EXPR_END)), "loc_8075")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8075")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 4)), scpexpr(EXPR_END)), "loc_8088")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8088")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 5)), scpexpr(EXPR_END)), "loc_80A5")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_80A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 6)), scpexpr(EXPR_END)), "loc_80B8")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_80B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x172, 7)), scpexpr(EXPR_END)), "loc_80D5")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_80D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 0)), scpexpr(EXPR_END)), "loc_80E8")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_80E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 1)), scpexpr(EXPR_END)), "loc_8105")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8105")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 2)), scpexpr(EXPR_END)), "loc_8118")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8118")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x173, 3)), scpexpr(EXPR_END)), "loc_8135")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8135")

    OP_29(0x80, 0x1, 0x8)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8246")
    SetChrName("")
    Sound(17, 0, 100, 0)
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_823D")

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

    label("loc_823D")

    SetScenarioFlags(0x178, 7)
    OP_29(0x80, 0x1, 0xD)

    label("loc_8246")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8334")
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

    label("loc_8334")

    OP_4C(0x8, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 3700, 0, 2090, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_35_79E5 end

    def Function_36_8364(): pass

    label("Function_36_8364")

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
            "#3PHey, if it isn't the\x01",
            "police kids from\x01",
            "earlier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PWill you be staying with\x01",
            "us today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FUhhm, we came because we\x01",
            "wanted to ask you\x01",
            "something...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FWas a strange package\x01",
            "delivered here recently?\x02",
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
            "#3POh, oh, that's right,\x01",
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
        "#00003FUhh, actually...\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained about\x01",
            "the misdelivered\x01",
            "packages.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x8,
        (
            "#3PAha, so that's what\x01",
            "happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PSo that package was\x01",
            "supposed to go to St.\x01",
            "Ursula.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PNo wonder there were\x01",
            "scalpels and stuff\x01",
            "inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FIt must have seemed\x01",
            "weird for such things to\x01",
            "suddenly arrive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#3PI was shocked!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PLycka was weirded out by them,\x01",
            "so I was going to put it out\x01",
            "with the trash tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FJ-Just in the nick of\x01",
            "time, I guess...\x02",
        )
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
        "#3POh, thanks. Let's see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PAh, these are those\x01",
            "Liberlian glasses I\x01",
            "ordered a while back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PI'm sure this one's\x01",
            "ours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309FWell good then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FThen, I was wondering if\x01",
            "we could get the\x01",
            "misdelivered one from you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#3PIt's here somewhere. One\x01",
            "moment please.\x02",
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
            "#3PHere it is. Thanks for\x01",
            "taking care of the rest.\x02",
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
            "#00000FAlright, let's head for\x01",
            "St. Ursula Hospital\x01",
            "next.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FLet's try asking at\x01",
            "their reception desk.\x02",
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

    # Function_36_8364 end

    def Function_37_8B5D(): pass

    label("Function_37_8B5D")

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
        "#00005FNielsen―\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8CC9")
    Jump("loc_8D13")

    label("loc_8CC9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8CE9")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8D13")

    label("loc_8CE9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8D09")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8D13")

    label("loc_8D09")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8D13")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)

    ChrTalk(
        0xE,
        (
            "Hmm. That voice is\x01",
            "Lloyd's, isn't it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FI'm honored you remember\x01",
            "me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Haha. It's because I've\x01",
            "interviewed you before.\x01",
            "There's no way I'd forget.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205F(Could this person\x01",
            "be...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300F(Yeah. He's a famous journalist\x01",
            "who interviewed Lloyd and the\x01",
            "others before, huh.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100F(Yes, his name is\x01",
            "Nielsen.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FUmm, why are you in\x01",
            "Mainz again today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Yes. Actually, I plan to\x01",
            "interview this town's\x01",
            "mayor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I'll ask him about the history of\x01",
            "septium mining in this town, and\x01",
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
            "#10100FHow to say this...\x01",
            "You're looking into\x01",
            "things others wouldn't.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Haha. Thanks to that, I've\x01",
            "been able to take all\x01",
            "these detours, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "By the way, I heard you contributed to the\x01",
            "capture of the terrorists that attacked\x01",
            "the trade conference a while back.\x02",
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
            "I'm wondering what meaning the\x01",
            "terror attacks on the trade\x01",
            "conference could have...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "I think there's something\x01",
            "to be learned by talking\x01",
            "it over with you all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FThe "meaning" of the\x01",
            "terror attacks...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208FBut that's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes. Information on this case is\x01",
            "restricted to state government\x01",
            "and police personnel.\x02\x03",
            "I think what we'll be able to\x01",
            "talk about is limited, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Of course, I understand\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Even so, I still think\x01",
            "there's meaning in discussing\x01",
            "this. What do you say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FHmm...\x02\x03",
            "(Our last interview with\x01",
            "him was indeed\x01",
            "beneficial.)\x02\x03",
            "#00008F(If we have the time, I\x01",
            "think we should take him\x01",
            "up on it.)\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 38)
    Return()

    # Function_37_8B5D end

    def Function_38_93D5(): pass

    label("Function_38_93D5")

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
            "Cooperate with Nielsen\x01",      # 0
            "Refuse\x01",                      # 1
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
        (0, "loc_9443"),
        (1, "loc_953B"),
        (SWITCH_DEFAULT, "loc_9630"),
    )


    label("loc_9443")


    ChrTalk(
        0x101,
        (
            "#00000FUnderstood. We accept\x01",
            "your interview.\x02",
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
        (
            "Then, let's begin our\x01",
            "discussion immediately.\x02",
        )
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
            "Quest [Terror Incident\x01",
            "Coverage Support]\x07\x00\x01",
            "started!\x02",
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
    Jump("loc_9630")

    label("loc_953B")


    ChrTalk(
        0x101,
        (
            "#00006FSorry. We don't have the\x01",
            "time right now...\x02\x03",
            "Can we ask about it\x01",
            "again, later?\x02",
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
            "Once you think you can\x01",
            "handle it, please come\x01",
            "speak with me.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 0x0)
    OP_69(0xFF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9628")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 104410, 2000, 2730, 180)
    EventEnd(0x5)

    label("loc_9628")

    SetScenarioFlags(0x177, 7)
    Jump("loc_9630")

    label("loc_9630")

    Return()

    # Function_38_93D5 end

    def Function_39_9631(): pass

    label("Function_39_9631")

    TalkBegin(0xE)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_96C5")
    Jump("loc_970F")

    label("loc_96C5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_96E5")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_970F")

    label("loc_96E5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9705")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_970F")

    label("loc_9705")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_970F")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)

    ChrTalk(
        0xE,
        "...You're Lloyd, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "Care to join me for an\x01",
            "interview regarding the\x01",
            "terror incident?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Call(0, 38)
    TalkEnd(0xE)
    Return()

    # Function_39_9631 end

    def Function_40_97A0(): pass

    label("Function_40_97A0")

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
            "#11PThank you very much for\x01",
            "joining me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PThe theme of this interview will be\x01",
            "the terror attacks that occurred at\x01",
            "the trade conference a few days ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PFirst of all, I'd like\x01",
            "to confirm the terrorist\x01",
            "groups.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PYou know this, don't\x01",
            "you, Lloyd?\x02",
        )
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
            "#1KTerror groups that\x01",
            "attacked the conference?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Imperial Liberation Front of Erebonia\x01",      # 0
            "Anti-Immigration League of Calvard\x01",         # 1
            "Both of them\x01",                               # 2
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
        (0, "loc_9AA8"),
        (1, "loc_9B70"),
        (2, "loc_9C37"),
        (SWITCH_DEFAULT, "loc_9D33"),
    )


    label("loc_9AA8")


    ChrTalk(
        0x101,
        (
            "#00001F#5PYes, the "Imperial Liberation\x01",
            "Front" of Erebonia.\x02\x03",
            "#00011F(―Wait, it wasn't just them.)\x02\x03",
            "#00003FAnd also, the anti-immigration\x01",
            "faction of Calvard, the "Anti-\x01",
            "Immigration League".\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D33")

    label("loc_9B70")


    ChrTalk(
        0x101,
        (
            "#00001F#5PYes, the anti-immigration\x01",
            "faction of Calvard, the\x01",
            ""Anti-Immigration League".\x02\x03",
            "#00011F(―Wait, it wasn't just\x01",
            "them.)\x02\x03",
            "#00003FAnd also, the "Imperial\x01",
            "Liberation Front" of\x01",
            "Erebonia.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D33")

    label("loc_9C37")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(
        0x101,
        (
            "#00006F#5PYes, the criminals were terror\x01",
            "groups from both nations―\x02\x03",
            "#00008FOne of them was the "Imperial\x01",
            "Liberation Front" of Erebonia.\x02\x03",
            "#00013FThe other was the anti-\x01",
            "immigration faction of Calvard,\x01",
            "the "Anti-Immigration League".\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D33")

    label("loc_9D33")


    ChrTalk(
        0xE,
        (
            "#11PYes, it was surely those\x01",
            "two.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PRegarding their backgrounds\x01",
            "and arguments, I will not dare\x01",
            "to go over them here, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PBut it is a fact that these two,\x01",
            "sharing nothing in common until\x01",
            "now, put up a united front.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PAccording to rumor, it is said a\x01",
            "secret organization called Ouroboros\x01",
            "was cooperating with them...\x02",
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
            "#00013F#5PThe society of Ouroboros...\x02\x03",
            "#00008F(Come to think of it, the\x01",
            "terrorists were using doll\x01",
            "weapons at the conference.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00108F#6PNielsen, you know of\x01",
            "Ouroboros?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PYes. Although it's\x01",
            "certain they are\x01",
            "something of an enigma.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PBut, it seems you all\x01",
            "are aware of them as\x01",
            "well, aren't you.\x02",
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
            "#00211F#6PThe more we learn about\x01",
            "them, the more shady\x01",
            "they seem...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11P...Anyhow, they may be working\x01",
            "towards an objective, but it's\x01",
            "a complete mystery to me.\x02",
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
        (
            "#00006F#5PI agree with that\x01",
            "assessment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PThen, let's move on to\x01",
            "the next topic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PThe next thing I want to confirm―\x01",
            "is the positions of the major\x01",
            "powers on these terror attacks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PAccording to sources, each\x01",
            "country secretly employed\x01",
            "an outside force.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PThose forces contributed\x01",
            "greatly to the resolution\x01",
            "of the incident, but―\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PAlthough they knew about\x01",
            "attacks, they intentionally\x01",
            "allowed them go forward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PWhat were both leaders\x01",
            "trying to achieve? What\x01",
            "do you think, Lloyd?\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x1, 1)
    ClearScenarioFlags(0x1, 2)
    ClearScenarioFlags(0x1, 3)

    label("loc_A36F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A76B")
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
            "Expose terror groups\x01",           # 0
            "Defeat opposing factions\x01",       # 1
            "Mayor Dieter's retirement\x01",      # 2
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
        (0, "loc_A486"),
        (1, "loc_A52C"),
        (2, "loc_A682"),
        (SWITCH_DEFAULT, "loc_A758"),
    )


    label("loc_A486")


    ChrTalk(
        0x101,
        (
            "#00005F#5P(Could it have been to expose\x01",
            "the terror groups?)\x02\x03",
            "#00006F(No. To begin with, both nations\x01",
            "already knew about their\x01",
            "respective terror groups.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_A758")

    label("loc_A52C")


    ChrTalk(
        0x101,
        (
            "#00003F#5PThey were trying to land a\x01",
            "blow on the opposing factions\x01",
            "employing the terrorists―\x02\x03",
            "I think both leaders were\x01",
            "trying to keep them in check.\x02\x03",
            "#00008FChancellor Osborne is trying\x01",
            "to hold back noble influence.\x02\x03",
            "#00001FPresident Rocksmith was\x01",
            "trying to restrain rogue\x01",
            "elements in his own country.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A67A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_A67A")

    SetScenarioFlags(0x1, 1)
    Jump("loc_A758")

    label("loc_A682")


    ChrTalk(
        0x101,
        (
            "#00008F#5P(The terrorist incidents\x01",
            "are proof that our state\x01",
            "is insecure.)\x02\x03",
            "(They were trying to use\x01",
            "it to force Mayor\x01",
            "Dieter's retirement...\x02\x03",
            "#00011F(No, no. That's the\x01",
            "wrong scale for this\x01",
            "question.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_A758")

    label("loc_A758")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_A766")
    Jump("loc_A76B")

    label("loc_A766")

    Jump("loc_A36F")

    label("loc_A76B")


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
            "#00203F#6PI see. So it became\x01",
            "material for political\x01",
            "attacks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PThat may be what you\x01",
            "think, Lloyd, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PCan I ask you what else\x01",
            "they might be after?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#5PThat's...\x02",
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
        "#10108F#5P...............\x02",
    )

    CloseMessageWindow()
    OP_64(0x101)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00006F#5PAnother big objective―\x02\x03",
            "#00013FI think it was to gain a\x01",
            "real foothold in their\x01",
            "advance into Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#11PHmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F#6PAdvance into Crossbell―\x02\x03",
            "#10301FThat's easy to understand. Both countries\x01",
            "proposed stationing their troops in\x01",
            "Crossbell at the trade conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#6PThe terror attack was more\x01",
            "proof that Crossbell's\x01",
            "security is insufficient―\x02\x03",
            "#00201FThat they needed to get\x01",
            "Crossbell to agree to the\x01",
            "proposal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#6PYes. That means the "Anti-Aggression\x01",
            "Pact" has lost its effect...\x02\x03",
            "#00108FAnd with the independence proposal,\x01",
            "public opinion in those countries is\x01",
            "focused on Crossbell.\x02\x03",
            "#00101FIt could be connected to a need to\x01",
            "deflect opposition or dissatisfaction\x01",
            "within their own countries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205F#6PTheir objective was all\x01",
            "of that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#5P*sigh*. One stone, many\x01",
            "birds, I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11P...Hmm. It seems you all\x01",
            "have considered this in\x01",
            "detail.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11P―Then, let us move to\x01",
            "our final point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PIt is clear this incident\x01",
            "was orchestrated by the\x01",
            "two countries, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PDoes this mean the two\x01",
            "countries have an\x01",
            "alliance?\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x1, 1)
    ClearScenarioFlags(0x1, 2)
    ClearScenarioFlags(0x1, 3)

    label("loc_AD95")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B044")
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
            "#1KHave the Empire and Republic\x01",
            "formed an alliance through\x01",
            "the terror incident?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Yes, a temporary one\x01",          # 0
            "Yes, a permanent one\x01",          # 1
            "It's out of the question\x01",      # 2
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
        (0, "loc_AE93"),
        (1, "loc_AEFB"),
        (2, "loc_AF8B"),
        (SWITCH_DEFAULT, "loc_B031"),
    )


    label("loc_AE93")


    ChrTalk(
        0x101,
        (
            "#00008F#5P(A temporary one... Why\x01",
            "do I think that?)\x02\x03",
            "#00003F(No, it can't be that\x01",
            "simple.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_B031")

    label("loc_AEFB")


    ChrTalk(
        0x101,
        (
            "#00005F#5P(I don't believe it.\x01",
            "Could they have formed a\x01",
            "permanent alliance?)\x02\x03",
            "#00006F(―That's nonsense. That\x01",
            "would never happen.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_B031")

    label("loc_AF8B")


    ChrTalk(
        0x101,
        (
            "#5P#00003FNo... I think it's out of\x01",
            "the question.\x02\x03",
            "#00013F─Both countries' ultimate\x01",
            "objective is singular\x01",
            "rule over Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B029")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_B029")

    SetScenarioFlags(0x1, 1)
    Jump("loc_B031")

    label("loc_B031")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_B03F")
    Jump("loc_B044")

    label("loc_B03F")

    Jump("loc_AD95")

    label("loc_B044")


    ChrTalk(
        0xE,
        "#11PYes― Exactly right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PIn the end, this\x01",
            "incident was a temporary\x01",
            "step.\x02",
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
            "#11PThis incident informs us that\x01",
            "both nations have designs to\x01",
            "make it their own.\x02",
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
        "#00108F#6P...............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00211F#6P...It's too blunt.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306F#6PWe've got to be ready\x01",
            "for when the battle\x01",
            "starts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PYes─ The intelligence war\x01",
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
            "make a reappearance─\x02",
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
        "#00305F#5PMysterious accidents?\x02",
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
            "#11PNo─ It seems I said\x01",
            "something I shouldn't\x01",
            "have.\x02",
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
            "#11PWe sorted several things\x01",
            "out. I'm glad I asked\x01",
            "you all to join me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#11PI thank you for your\x01",
            "cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5P...We feel the same.\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F#6PI feel like we\x01",
            "understand the current\x01",
            "situation a lot better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106F#5P...I learned a lot.\x02",
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
            "#11PIf there's another chance,\x01",
            "I would love to speak with\x01",
            "you all again like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#5PI'll be looking forward\x01",
            "to it.\x02",
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
            "Quest [Terror Incident\x01",
            "Coverage Support]\x07\x00\x01",
            "completed!\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B677")
    OP_2C(0x89, 0x2)
    Jump("loc_B68B")

    label("loc_B677")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B68B")
    OP_2C(0x89, 0x1)

    label("loc_B68B")

    OP_29(0x89, 0x1, 0x0)
    OP_29(0x89, 0x4, 0x10)
    EventEnd(0x5)
    Return()

    # Function_40_97A0 end

    SaveToFile()

Try(main)
