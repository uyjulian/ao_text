from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0570.bin",                # FileName
        "c0570",                    # MapName
        "c0570",                    # Location
        0x0027,                     # MapIndex
        "ed7117",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 39, 0, 1, 0, 2],
    )

    BuildStringList((
        "c0570",                  # 0
        "Eric",                   # 1
        "Sandra",                 # 2
        "Branch Manager Celdan",  # 3
        "Coppen",                 # 4
        "Peter",                  # 5
        "Detective Dudley",       # 6
        "Iris",                   # 7
        "Barker Bish",            # 8
        "Olivier",                # 9
        "Nielsen",                # 10
    ))

    AddCharChip((
        "chr/ch32202.itc",                   # 00
        "chr/ch23600.itc",                   # 01
        "chr/ch24202.itc",                   # 02
        "chr/ch22000.itc",                   # 03
        "chr/ch26802.itc",                   # 04
        "chr/ch00902.itc",                   # 05
        "chr/ch26900.itc",                   # 06
        "chr/ch26700.itc",                   # 07
    ))

    DeclNpc(0,       0,       6400,    180,  261,  0x0, 0,   3,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(4294962597, 79,      4449,    0,    261,  0x0, 0,   4,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   2,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(2109,    150,     4250,    0,    389,  0x0, 0,   5,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(4294961876, 0,       1649,    90,   385,  0x0, 0,   6,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(4294966206, 0,       3950,    135,  385,  0x0, 0,   7,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    405,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(0,       0,       5000,    1000,    0,       1500,    6400,    0x007E, 0,  4,  0x0000)
    DeclActor(4294959696, 750,     5400,    1200,    4294959696, 800,     5400,    0x007C, 0,  3,  0x0000)

    ChipFrameInfo(604, 0)                                        # 0

    ScpFunction((
        "Function_0_25C",          # 00, 0
        "Function_1_314",          # 01, 1
        "Function_2_52D",          # 02, 2
        "Function_3_5D6",          # 03, 3
        "Function_4_695",          # 04, 4
        "Function_5_699",          # 05, 5
        "Function_6_21FC",         # 06, 6
        "Function_7_3293",         # 07, 7
        "Function_8_336A",         # 08, 8
        "Function_9_3404",         # 09, 9
        "Function_10_34D0",        # 0A, 10
        "Function_11_3572",        # 0B, 11
        "Function_12_3E02",        # 0C, 12
        "Function_13_3E60",        # 0D, 13
        "Function_14_3EAD",        # 0E, 14
        "Function_15_5356",        # 0F, 15
        "Function_16_5E8B",        # 10, 16
        "Function_17_5EDB",        # 11, 17
    ))


    def Function_0_25C(): pass

    label("Function_0_25C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_29C"),
        (1, "loc_2A8"),
        (2, "loc_2B4"),
        (3, "loc_2C0"),
        (4, "loc_2CC"),
        (5, "loc_2D8"),
        (6, "loc_2E4"),
        (SWITCH_DEFAULT, "loc_2F0"),
    )


    label("loc_29C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2FC")

    label("loc_2A8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2FC")

    label("loc_2B4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2FC")

    label("loc_2C0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2FC")

    label("loc_2CC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2FC")

    label("loc_2D8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2FC")

    label("loc_2E4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2FC")

    label("loc_2F0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2FC")

    label("loc_2FC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_313")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2FC")

    label("loc_313")

    Return()

    # Function_0_25C end

    def Function_1_314(): pass

    label("Function_1_314")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A7")
    ClearChrFlags(0xA, 0x40)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x0)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrPos(0xA, -8400, 100, -500, 90)
    ClearChrFlags(0xB, 0x40)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -8900, 0, 1500, 90)
    ClearChrFlags(0xC, 0x40)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x2)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrPos(0xC, -5800, 100, -2050, 0)

    label("loc_3A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DB")
    SetScenarioFlags(0x0, 5)
    SetMapFlags(0x10000000)
    Event(0, 15)

    label("loc_3DB")

    SetChrChipByIndex(0x9, 0x4)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3FA")
    Jump("loc_50E")

    label("loc_3FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_412")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jump("loc_50E")

    label("loc_412")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_420")
    Jump("loc_50E")

    label("loc_420")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_444")
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)
    Jump("loc_50E")

    label("loc_444")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_452")
    Jump("loc_50E")

    label("loc_452")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_465")
    SetChrFlags(0x9, 0x10)
    Jump("loc_50E")

    label("loc_465")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_482")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47D")
    SetChrFlags(0x9, 0x10)

    label("loc_47D")

    Jump("loc_50E")

    label("loc_482")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_495")
    SetChrFlags(0x9, 0x10)
    Jump("loc_50E")

    label("loc_495")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4A3")
    Jump("loc_50E")

    label("loc_4A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4B6")
    SetChrFlags(0x9, 0x10)
    Jump("loc_50E")

    label("loc_4B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4C4")
    Jump("loc_50E")

    label("loc_4C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4D2")
    Jump("loc_50E")

    label("loc_4D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 4)), scpexpr(EXPR_END)), "loc_4F7")
    SetChrFlags(0x9, 0x10)
    OP_63(0x9, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)
    Jump("loc_50E")

    label("loc_4F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_505")
    Jump("loc_50E")

    label("loc_505")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_50E")

    label("loc_50E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_52C")
    ClearScenarioFlags(0x22, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x95, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_52C")
    SetScenarioFlags(0x0, 6)
    Event(0, 17)

    label("loc_52C")

    Return()

    # Function_1_314 end

    def Function_2_52D(): pass

    label("Function_2_52D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_549")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_594")

    label("loc_549")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_565")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_594")

    label("loc_565")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_57F")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x243), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 5)
    Jump("loc_594")

    label("loc_57F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_594")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 6)

    label("loc_594")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5B5")
    Sound(128, 1, 50, 0)

    label("loc_5B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5CC")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)

    label("loc_5CC")

    OP_10(0x0, 0x1)
    OP_10(0x1, 0x0)
    OP_10(0x2, 0x0)
    Return()

    # Function_2_52D end

    def Function_3_5D6(): pass

    label("Function_3_5D6")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The "Regular Menu For Businessmen" is here.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_691")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x17)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_691")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "You learned the "Rich Cappuccino"\x07\x00",
            " recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_691")

    TalkEnd(0xFF)
    Return()

    # Function_3_5D6 end

    def Function_4_695(): pass

    label("Function_4_695")

    Call(0, 5)
    Return()

    # Function_4_695 end

    def Function_5_699(): pass

    label("Function_5_699")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x139, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7C6")

    ChrTalk(
        0x8,
        "Welcome...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x105, 500)
    Sleep(300)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "Oh... If it isn't\x01",
            "Mr. Wazy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's rare to see you\x01",
            "around this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FHu hu. I'm in the middle\x01",
            "of a little patrol.\x02\x03",
            "#10300FI'll come here again to\x01",
            "drink whenever I have time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Alright. I'll be waiting.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x139, 3)
    TalkEnd(0x8)
    Return()

    label("loc_7C6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7D0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21F8")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_820")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_820")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_840")
    OP_AF(0x42)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_21F3")

    label("loc_840")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_854")
    Jump("loc_21F3")

    label("loc_854")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21F3")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_A48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_99C")

    ChrTalk(
        0x8,
        (
            "Before long, "Heiyue" will grab\x01",
            "the real power in the underworld.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Heiyue dislikes conspicuous actions\x01",
            "like those of Revache, but even so,\x01",
            "their presence is overwhelming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's certain they have no small\x01",
            "influence even in Back Street.\x01",
            "You guys should be careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A43")

    label("loc_99C")


    ChrTalk(
        0x8,
        (
            "Before long, "Heiyue" will grab\x01",
            "the real power in the underworld.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's certain they have no small\x01",
            "influence even in Back Street.\x01",
            "You guys should be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A43")

    Jump("loc_21F3")

    label("loc_A48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_AE2")

    ChrTalk(
        0x8,
        (
            "It looks like those monsters\x01",
            "didn't enter Back Street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But I have no idea how\x01",
            "dangerous it is. Feel free\x01",
            "to take shelter in here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21F3")

    label("loc_AE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_CDB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BFE")

    ChrTalk(
        0x8,
        (
            "The declaration of independence will\x01",
            "greatly influence the underworld.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "From now on, the State Guard\x01",
            "will crack down on both the\x01",
            "Imperial and Republican mafias.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This development was so\x01",
            "sudden... But it might be what\x01",
            "Crossbell needs right now.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CD6")

    label("loc_BFE")


    ChrTalk(
        0x8,
        (
            "From now on, the State Guard\x01",
            "will crack down on both the\x01",
            "Imperial and Republican mafias.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Though the declaration of independence was\x01",
            "a sudden development... Maybe Crossbell\x01",
            "needs drastic measures right now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CD6")

    Jump("loc_21F3")

    label("loc_CDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_EB6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DF5")

    ChrTalk(
        0x8,
        (
            "An attack on Crossbell City...\x01",
            "The "Red Constellation"\x01",
            "has done the unthinkable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even in this store where it's easy to get underworld\x01",
            "information, I didn't sense any ill omens...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Most likely, it was planned in\x01",
            "detail quite a long time ago.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_EB1")

    label("loc_DF5")


    ChrTalk(
        0x8,
        (
            "Even in this store where it's easy to get underworld\x01",
            "information, I didn't sense any ill omens...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The attack on Crossbell City\x01",
            "was most likely planned in\x01",
            "detail a long time ago.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EB1")

    Jump("loc_21F3")

    label("loc_EB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1078")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FC9")

    ChrTalk(
        0x8,
        (
            "Ever since they realized that\x01",
            "the "Red Constellation" is gone, \x01",
            "the police seem to be in a panic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Those guys evaded detection by moving\x01",
            "underground, and headed for Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...I don't know the significance\x01",
            "of this occupation incident.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1073")

    label("loc_FC9")


    ChrTalk(
        0x8,
        (
            "Ever since they realized that\x01",
            "the "Red Constellation" is gone, \x01",
            "the police seem to be in a panic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...I don't know the significance\x01",
            "of this occupation incident.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1073")

    Jump("loc_21F3")

    label("loc_1078")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1232")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_118D")

    ChrTalk(
        0x8,
        (
            "Yesterday's derailment accident... \x01",
            "According to rumors, it was caused by \x01",
            "a giant monster that appeared nearby.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But with the referendum approaching, \x01",
            "I can't think it was any ordinary monster accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "...I feel it's very suspicious.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_122D")

    label("loc_118D")


    ChrTalk(
        0x8,
        (
            "With the referendum approaching, I can't\x01",
            "think yesterday's derailment was due to\x01",
            "any normal monster, like rumors say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "...I feel it's very suspicious.\x02",
    )

    CloseMessageWindow()

    label("loc_122D")

    Jump("loc_21F3")

    label("loc_1232")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1295")

    ChrTalk(
        0x8,
        "I heard sirens in the distance...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "...I'm getting a bad feeling about this.\x02",
    )

    CloseMessageWindow()
    Jump("loc_21F3")

    label("loc_1295")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1502")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1435")

    ChrTalk(
        0x8,
        (
            "I heard some Republican\x01",
            "terrorists were arrested\x01",
            "yesterday at Altair City...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "According to underworld rumors,\x01",
            "it was Heiyue that tracked them down.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_13D1")

    ChrTalk(
        0x101,
        (
            "#00005F(So Heiyue operatives were there, huh...)\x02\x03",
            "#00003F(I didn't notice them, but they\x01",
            "don't miss a beat, do they.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_142D")

    label("loc_13D1")


    ChrTalk(
        0x8,
        (
            "I don't know if I should've expected it, but...\x01",
            "Those guys don't miss a beat, do they.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_142D")

    SetScenarioFlags(0x0, 0)
    Jump("loc_14FD")

    label("loc_1435")


    ChrTalk(
        0x8,
        (
            "According to rumor, Heiyue had a\x01",
            "hand in the arrest of Republican\x01",
            "terrorists at Altair City yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I don't know if I should've expected it, but...\x01",
            "Those guys don't miss a beat, do they.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14FD")

    Jump("loc_21F3")

    label("loc_1502")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_16D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1632")

    ChrTalk(
        0x8,
        (
            "Rumor has it the Republican government\x01",
            "asked "Red Constellation" to intercept\x01",
            "terrorists at the Trade Conference, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Recently, Crimson & Co. hasn't\x01",
            "been causing any trouble.\x01",
            "They've been rather quiet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Those guys are\x01",
            "real pro jaegers,\x01",
            "for better or worse.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16CC")

    label("loc_1632")


    ChrTalk(
        0x8,
        (
            "Crimson & Co. too, that acted\x01",
            "during the Trade Conference,\x01",
            "has been very quiet lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Those guys are\x01",
            "real pro jaegers,\x01",
            "for better or worse.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16CC")

    Jump("loc_21F3")

    label("loc_16D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_18AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17F2")

    ChrTalk(
        0x8,
        (
            "The "Red Constellation" Jaeger group.\x01",
            "And "Heiyue" of Waterfront Area...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "This being the day of the main session,\x01",
            "the police have reinforced their guard\x01",
            "against the power of those groups.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The officers who I\x01",
            "saw on Back Street\x01",
            "looked quite nervous.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_18A8")

    label("loc_17F2")


    ChrTalk(
        0x8,
        (
            "This being the day of the main session,\x01",
            "the guard against "Red Constellation"\x01",
            "and "Heiyue" has been reinforced.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The officers who I\x01",
            "saw on Back Street\x01",
            "looked quite nervous.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18A8")

    Jump("loc_21F3")

    label("loc_18AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1AAF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_198F")

    ChrTalk(
        0x8,
        (
            "The Trade Conference...\x01",
            "So it's finally started.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I feel the nervousness\x01",
            "of the officers patrolling\x01",
            "Back Street building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The guards assigned to\x01",
            "Crimson & Co. seem strong.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A13")

    label("loc_198F")


    ChrTalk(
        0x8,
        (
            "I feel the nervousness\x01",
            "of the officers patrolling\x01",
            "Back Street building.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The guards assigned to\x01",
            "Crimson & Co. seem strong.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A13")

    Jump("loc_1AAA")

    label("loc_1A18")


    ChrTalk(
        0x8,
        (
            "Mr. Olivier is a pretty\x01",
            "interesting fellow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If possible I'd like to offer\x01",
            "him a contract to perform for\x01",
            "us, but... It's really too bad.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AAA")

    Jump("loc_21F3")

    label("loc_1AAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1D28")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C35")

    ChrTalk(
        0x8,
        (
            ""Crimson & Co." just moved\x01",
            "into the back alley building...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I get the impression\x01",
            "they're more discerning,\x01",
            "compared to Revache.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But rumor has it they're actually\x01",
            "an arm of "Red Constellation", the\x01",
            "strongest jaegers on western Zemuria.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Although they have a calm exterior,\x01",
            "one can't help but feel their presence\x01",
            "is even bigger than Revache's was.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1D23")

    label("loc_1C35")


    ChrTalk(
        0x8,
        (
            "Rumor has that Crimson & Co. is\x01",
            "actually a part of the "Red Constellation",\x01",
            "the strongest jaegers on western Zemuria.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Although they have a calm exterior,\x01",
            "one can't help but feel their presence\x01",
            "is even bigger than Revache's was.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D23")

    Jump("loc_21F3")

    label("loc_1D28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 4)), scpexpr(EXPR_END)), "loc_1E05")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DA8")

    ChrTalk(
        0x8,
        (
            "...The rain's steadily\x01",
            "getting worse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Miss Sandra said maybe we\x01",
            "should close up shop soon.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1E00")

    label("loc_1DA8")


    ChrTalk(
        0x8,
        "...Did something happen?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Right now, Miss Sandra and\x01",
            "I are the only ones here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E00")

    Jump("loc_21F3")

    label("loc_1E05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1FE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F2B")

    ChrTalk(
        0x8,
        (
            "It's certain Heiyue is\x01",
            "trying to obtain all of\x01",
            "Revache's old property.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If they succeed, they'll\x01",
            "have gained a foothold in\x01",
            "Crossbell's underworld.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "When I think about the state of\x01",
            "Crossbell, I think that nothing can\x01",
            "be done about it, in a certain sense.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1FDC")

    label("loc_1F2B")


    ChrTalk(
        0x8,
        (
            "At the same time, there's the\x01",
            "rise of Heiyue to worry about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "When I think about the state of\x01",
            "Crossbell, I think that nothing can\x01",
            "be done about it, in a certain sense.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FDC")

    Jump("loc_21F3")

    label("loc_1FE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_21F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_212B")

    ChrTalk(
        0x8,
        (
            "Ever since Revache disappeared, mafia\x01",
            "that have remained hidden until now\x01",
            "have been showing up more and more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The meaning of that is, rather\x01",
            "than becoming more orderly, Back\x01",
            "Street has actually gotten worse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Now that they're gone,\x01",
            "I understand a little better\x01",
            "how much power Revache had.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_21F3")

    label("loc_212B")


    ChrTalk(
        0x8,
        (
            "Ever since Revache disappeared, mafia\x01",
            "that have remained hidden until now\x01",
            "have been showing up more and more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Now that they're gone,\x01",
            "I understand a little better\x01",
            "how much power Revache had.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21F3")

    Jump("loc_7D0")

    label("loc_21F8")

    TalkEnd(0x8)
    Return()

    # Function_5_699 end

    def Function_6_21FC(): pass

    label("Function_6_21FC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_232E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22DB")
    SetChrSubChip(0xFE, 0x2)

    ChrTalk(
        0xFE,
        (
            "*hiiiiiic*...\x01",
            "Eriiic, let's drink.\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0xFE,
        (
            "That weird mist is gone. \x01",
            "Isn't that cause for celebration?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xFE, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "Miss Sandra, you're disturbing.\x01",
            "Just go home already.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x0)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x0, 1)
    Jump("loc_2329")

    label("loc_22DB")


    ChrTalk(
        0xFE,
        "*hiiiiiic*. You're so mean, Eric...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "But, I l-o-v-e that about you㈱\x02",
    )

    CloseMessageWindow()

    label("loc_2329")

    Jump("loc_328F")

    label("loc_232E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_23BA")

    ChrTalk(
        0xFE,
        (
            "So sleepy... Because we're\x01",
            "closed due to martial law, \x01",
            "I drank here and fell asleep...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "H-Huh? Did something happen?\x02",
    )

    CloseMessageWindow()
    Jump("loc_328F")

    label("loc_23BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2502")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2494")

    ChrTalk(
        0xFE,
        (
            "There was a customer that\x01",
            "booked an "Independence\x01",
            "Anniversary Party" right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't understand\x01",
            "difficult things, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They all look happy, so I\x01",
            "guess it's a good thing?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_24FD")

    label("loc_2494")


    ChrTalk(
        0xFE,
        (
            "I don't understand\x01",
            "difficult things, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "They all look happy, so I\x01",
            "guess it's a good thing?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24FD")

    Jump("loc_328F")

    label("loc_2502")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2705")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2636")

    ChrTalk(
        0xFE,
        (
            "We closed our store due\x01",
            "to the attack, but we're\x01",
            "reopening tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, with the reconstruction\x01",
            "mostly complete, I'm never\x01",
            "gonna get a vacation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We're just a simple club, but even we\x01",
            "have regulars who look forward to coming.\x01",
            "...Gotta do our best for now, I guess.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2700")

    label("loc_2636")


    ChrTalk(
        0xFE,
        (
            "With the reconstruction mostly complete,\x01",
            "I'm never gonna get a vacation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We're just a simple club, but even we\x01",
            "have regulars who look forward to coming.\x01",
            "...Gotta do our best for now, I guess.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2700")

    Jump("loc_328F")

    label("loc_2705")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_285C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27D7")

    ChrTalk(
        0xFE,
        (
            "Eric said it, but is\x01",
            "Crimson & Co. really\x01",
            "run by jaegers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ahh... Crimson & Co. \x01",
            "runs the famed\x01",
            ""Neue-Blanc", right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I thought it was run by the mafia.\x01",
            "I was surprised.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2857")

    label("loc_27D7")


    ChrTalk(
        0xFE,
        (
            "Crimson & Co. that runs "Neue-\x01",
            "Blanc" are actually jaegers, uh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I thought it was run by the mafia.\x01",
            "I was surprised.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2857")

    Jump("loc_328F")

    label("loc_285C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_29CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2948")
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Hey, Eric. Don't\x01",
            "just talk. Come have\x01",
            "a drink with me...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xFE, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "You too Miss Sandra. \x01",
            "Don't just always sleep here.\x01",
            "Why not going back home?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Aww, you're such a meanie, Eric...\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x0, 1)
    Jump("loc_29C9")

    label("loc_2948")


    ChrTalk(
        0xFE,
        (
            "Tch, that Eric. He's such a meanie\x01",
            "when it comes to things like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, I l-o-v-e that about him.\x01",
            "...Just kidding㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29C9")

    Jump("loc_328F")

    label("loc_29CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2AF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A8F")

    ChrTalk(
        0xFE,
        (
            "*mumble mumble*...\x01",
            "Get this, you old lecheeer...!\x01",
            "Know your place! And take this, and that...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "...Wah!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...Oh, a dream.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    SetScenarioFlags(0x0, 1)
    Jump("loc_2AED")

    label("loc_2A8F")


    ChrTalk(
        0xFE,
        (
            "Aww... It was such\x01",
            "a nice dream but I\x01",
            "forgot it already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmm? Did something happen?\x02",
    )

    CloseMessageWindow()

    label("loc_2AED")

    Jump("loc_328F")

    label("loc_2AF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2B7D")

    ChrTalk(
        0xFE,
        (
            "So sleepy... \x01",
            "That old man's \x01",
            "clingy as always...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We're not that kind of\x01",
            "store! I keep telling\x01",
            "him that. Dammit...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_328F")

    label("loc_2B7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2CCC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C43")

    ChrTalk(
        0xFE,
        (
            "It seems there'll\x01",
            "be a referendum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Eric says I should\x01",
            "go, but it's kinda\x01",
            "complicated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I mean, the voting hours are right\x01",
            "in the middle of my sleeping time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2CC7")

    label("loc_2C43")


    ChrTalk(
        0xFE,
        (
            "I'm not sure if I'll\x01",
            "participate in the referendum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I mean, the voting hours are right\x01",
            "in the middle of my sleeping time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CC7")

    Jump("loc_328F")

    label("loc_2CCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2E02")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D95")
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Eric... Give me\x01",
            "another Rum and Cola...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xFE, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "Miss Sandra, it's already morning.\x01",
            "Please go home already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Aww, you're such a meanie, Eric...\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x0, 1)
    Jump("loc_2DFD")

    label("loc_2D95")


    ChrTalk(
        0xFE,
        (
            "Eric's so mean... I wish\x01",
            "he'd go along sometimes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's been awhile since\x01",
            "we closed the store.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DFD")

    Jump("loc_328F")

    label("loc_2E02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2EFD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E8E")

    ChrTalk(
        0xFE,
        (
            "Yesterday, a mean customer\x01",
            "came and he drank a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ooh... I have a headache.\x01",
            "I went and did it again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EF8")

    label("loc_2E8E")


    ChrTalk(
        0xFE,
        (
            "That guy's performance\x01",
            "was very skillful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was dead tired from work,\x01",
            "but it fixed me right up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EF8")

    Jump("loc_328F")

    label("loc_2EFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2FE9")

    ChrTalk(
        0xFE,
        (
            ""Neue-Blanc" in Entertainment\x01",
            "District has been doing better ever\x01",
            "since Crimson & Co. arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, there must be a big difference\x01",
            "in revenue between a high-class club\x01",
            "and this place. Maybe I should transfer.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_328F")

    label("loc_2FE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 4)), scpexpr(EXPR_END)), "loc_301F")
    OP_64(0x9)

    ChrTalk(
        0xFE,
        "*zzz, zzz*...\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)
    Jump("loc_328F")

    label("loc_301F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3165")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30E1")

    ChrTalk(
        0xFE,
        (
            "*yawn*... \x01",
            "I was sleeping like a log.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I always drop by this place\x01",
            "when I'm finished hostessing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I mean, it's quiet and\x01",
            "comfortable so I can sleep well.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3160")

    label("loc_30E1")


    ChrTalk(
        0xFE,
        (
            "This store is always quiet,\x01",
            "so I can sleep well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Eric is quiet and goes\x01",
            "along with it. It's an\x01",
            "amazingly cozy place.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3160")

    Jump("loc_328F")

    label("loc_3165")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_328F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3203")

    ChrTalk(
        0xFE,
        (
            "Day after day, I pour\x01",
            "drinks at the club while\x01",
            "wearing my business smile.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*... I wonder\x01",
            "why I do this sort\x01",
            "of work.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_328F")

    label("loc_3203")


    ChrTalk(
        0xFE,
        (
            "*sigh*... Lately, I've\x01",
            "been feeling like this\x01",
            "work is pointless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, the pay is good,\x01",
            "so I guess I have no\x01",
            "real desire to quit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_328F")

    TalkEnd(0xFE)
    Return()

    # Function_6_21FC end

    def Function_7_3293(): pass

    label("Function_7_3293")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_32C5")
    Call(0, 14)
    Return()

    label("loc_32C5")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "To start with, I plan to look for a suitable\x01",
            "office from which to restart activities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Member Lloyd, let's exchange\x01",
            "information if anything happens.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_3293 end

    def Function_8_336A(): pass

    label("Function_8_336A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_339C")
    Call(0, 14)
    Return()

    label("loc_339C")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Now then, I think I'll\x01",
            "go fishing immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What? A little rain\x01",
            "is no bother to me!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_336A end

    def Function_9_3404(): pass

    label("Function_9_3404")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3436")
    Call(0, 14)
    Return()

    label("loc_3436")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Even so, that man...\x01",
            "He truly can't be forgiven.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't care if he's a pro or anything, but\x01",
            "pretending to be a fisherman just won't do.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_3404 end

    def Function_10_34D0(): pass

    label("Function_10_34D0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34E5")
    Call(0, 11)
    Jump("loc_356E")

    label("loc_34E5")


    ChrTalk(
        0xD,
        (
            "#00600FNow then... I'll drink this\x01",
            "and then get back to work.\x02\x03",
            "#00603FThe day of the referendum is\x01",
            "nearing. I can't lose focus now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_356E")

    TalkEnd(0xFE)
    Return()

    # Function_10_34D0 end

    def Function_11_3572(): pass

    label("Function_11_3572")

    EventBegin(0x0)
    Fade(500)
    OP_68(1500, 1430, 2330, 0)
    MoveCamera(328, 28, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21430, 0)
    SetChrPos(0xD, 1920, 0, 3850, 180)
    SetChrPos(0x101, 680, 0, 2770, 45)
    SetChrPos(0x102, 1730, 0, 2320, 0)
    SetChrPos(0x103, 920, 0, 1020, 0)
    SetChrPos(0x104, -160, 0, 1970, 45)
    SetChrPos(0x109, -640, 0, 3120, 90)
    SetChrPos(0x105, 2330, 0, 910, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrSubChip(0xD, 0x0)
    OP_0D()

    ChrTalk(
        0x101,
        "#00005FMr. Dudley.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#00603FYou guys, huh. Never\x01",
            "thought I'd see you here.\x02\x03",
            "#00600FI'm told you're resuming your\x01",
            "support request activities today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, fortunately.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FBy the way, is there any\x01",
            "new info on the location\x01",
            "of "Red Constellation"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#00600FHmph, that's been\x01",
            "nothing but trouble.\x02\x03",
            "We've been expecting something\x01",
            "out of the Imperial government on\x01",
            "that front, but not a single peep.\x02\x03",
            "#00603FIf something's going to happen, it'll be in three\x01",
            "days when the independence referendum is held.\x02\x03",
            "#00600FWe're working tirelessly\x01",
            "to prepare for that day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10103FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FYou look\x01",
            "depressed, though.\x02\x03",
            "Are you drunk?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#00603FHmph. I'm a modest drinker but there's\x01",
            "no reason to start drinking at noon.\x02\x03",
            "#00600FThis is just a soft drink.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FHu hu, good work\x01",
            "on giving off that\x01",
            "atmosphere alcohol-free.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xD)

    ChrTalk(
        0xD,
        (
            "#00603F...Do you drink,\x01",
            "Bannings?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FYes, but not\x01",
            "that often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#00602FHmph. In that case, you're\x01",
            "very different from Guy.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005FMight you have come here for drinks\x01",
            "with my big brother, Dudley?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#00603FWell, not that often.\x02\x03",
            "#00600FBy the way, Guy is the one who\x01",
            "introduced me to this place.\x02\x03",
            "#00608FTrailblazing like\x01",
            "that was his forte.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHa ha, I bet. With that\x01",
            "personality of his and all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FSo who could hold\x01",
            "their liquor better, \x01",
            "you or him?\x02\x03",
            "It was you guys. You must've thrown\x01",
            "down with each other at some point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#00603FHmph, I have no comment on that.\x02\x03",
            "#00602FI will say one thing, though,\x01",
            "Bannings. Guy could and I can hold\x01",
            "my liquor better than any of you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#00301FBoastin' like that when you don't\x01",
            "even know how much I can drink...\x02\x03",
            "#00304FYou're practically\x01",
            "beggin' me to show you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#00604FHmph, if there's a chance.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FAhaha...\x02\x03",
            "(Mr. Dudley hates\x01",
            "to lose even in this\x01",
            "department, huh.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x18F, 3)
    OP_50(0x6B, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_69(0xFF, 0x0)
    SetChrPos(0xD, 2110, 150, 4250, 0)
    SetChrPos(0x0, 1210, 0, 2500, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_11_3572 end

    def Function_12_3E02(): pass

    label("Function_12_3E02")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Oh man, we're in\x01",
            "a real fix now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No customers today,\x01",
            "so I'll take it easy.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_3E02 end

    def Function_13_3E60(): pass

    label("Function_13_3E60")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "What am I going to do?\x01",
            "If it's like this, I can't return home...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_3E60 end

    def Function_14_3EAD(): pass

    label("Function_14_3EAD")

    EventBegin(0x0)
    OP_4B(0xB, 0xFF)
    Fade(500)
    OP_68(-5430, 1430, 390, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, -6170, 0, 1680, 180)
    SetChrPos(0x102, -5200, 0, 1810, 180)
    SetChrPos(0x109, -5400, 0, 3000, 180)
    SetChrPos(0x105, -4200, 0, 2000, 225)
    OP_0D()

    ChrTalk(
        0xC,
        "#6POh, Lloyd, you made it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Sorry to drag you here, Member Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well then, we're all here.\x01",
            "Let's start the meeting.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    OP_68(-4570, 1630, -1220, 0)
    MoveCamera(318, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20220, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrPos(0xB, -8400, 0, 1500, 90)
    SetChrPos(0x101, -3100, 100, -1000, 270)
    SetChrPos(0x102, -3100, 100, 0, 270)
    SetChrPos(0x105, -4690, 0, 1380, 225)
    SetChrPos(0x109, -3190, 0, 1380, 225)
    SetChrSubChip(0xC, 0x2)
    FadeToBright(1000, 0)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7117", 0)

    ChrTalk(
        0xA,
        (
            "#5PFirst, we have to update Member\x01",
            "Lloyd on our current status.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PActually, the Fisherman's Guild activities have been\x01",
            "suspended for months due to a restraining order.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005FR-Restraining order...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6PYes, because Dr. Joachim,\x01",
            "one of our members, caused\x01",
            "that incident, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PAnd so, each of us decided to take\x01",
            "a fresh look inside ourselves...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00108FBut, none of you were responsible for that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5PIt's true that we weren't involved in the incident...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PBut we spent so much time with\x01",
            "him as fellow lovers of fishing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P...And even so, we never once\x01",
            "realized what he was plotting\x01",
            "in the depths of his soul.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PHonestly, we bear plenty of social\x01",
            "and personal responsibility.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00003FBranch Manager Celdan...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5P...Well anyway, let's set all of that aside for now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PAbout a week ago, in the middle of all that,\x01",
            "we were contacted by the real estate company.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PI don't know if it was due to the restraining\x01",
            "order, but they said because the building\x01",
            "looked unused, our contract was terminated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PAlso, they informed us that they formed a new\x01",
            "contract with the "Fishing Emperor Club".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6PAfter that, we tried contacting a\x01",
            "Fishing Emperor Club representative,\x01",
            "but it didn't go so well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PAnd so today, when we stopped by the office,\x01",
            "their representative just happened to be there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5PAnd we finally learned the truth about the contract...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PAfter that, I asked Member Lloyd\x01",
            "and the others to gather.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00005FI see.\x02\x03",
            "#00003FI think I understand the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PBut even so... The Lakelord Corporation's\x01",
            ""Fishing Emperor Club", huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PIf they were merely expanding the scope of their activities, \x01",
            "I wouldn't have thought anything of it, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PI never thought they would stoop so\x01",
            "low as to take our office by force.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6PYes, I don't even understand\x01",
            "their reason for hating us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P...Anyway, with this, their\x01",
            "hate of us is clear as day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PBut it's not like we\x01",
            "can do anything\x01",
            "about the situation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PWell for now, it seems all we\x01",
            "can do is keep an eye on things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P...But at this rate,\x01",
            "our guild might end\x01",
            "up dissolving.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PI know it's not enough... But right now, we have to\x01",
            "seize the moment and think of a way out of this.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xB, 0xB4, 0x1F4)
    SetChrSubChip(0xC, 0x1)

    ChrTalk(
        0xC,
        (
            "#6PHehe, well then. I hereby declare that the Fisherman's\x01",
            "Guild, Crossbell Branch, has restarted operations!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#11PAlright! I've been waiting for this!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PBut... All members\x01",
            "will be starting over at\x01",
            ""Novice Fisherman" level.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PAnd, the "Rank Advancement\x01",
            "Exam" is temporarily\x01",
            "suspended, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xB,
        "#11PHuh...?\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "#11PW-wait a\x01",
            "minute...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PYou mean...\x01",
            "I'm no longer a\x01",
            ""Master Fisherman"?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x1)

    ChrTalk(
        0xA,
        (
            "#5PSorry, but that's how it is.\x01",
            "This is for taking responsibility too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#11P*shock*, all my efforts...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6PCome now Coppen. If you do your\x01",
            "best, everything will be fine.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0x87, 0x1F4)

    ChrTalk(
        0xB,
        (
            "#11POoh... I don't want to hear that\x01",
            "from you, who stopped advancing\x01",
            "at the "Hobby Fisherman" level.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 0)), scpexpr(EXPR_END)), "loc_4D1C")

    ChrTalk(
        0x101,
        (
            "#12P#00012FAhaha...\x02\x03",
            "#00006F(I was a "Divine Fisherman" of Crossbell...\x01",
            "This is pretty hard to take.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E6D")

    label("loc_4D1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 1)), scpexpr(EXPR_END)), "loc_4D87")

    ChrTalk(
        0x101,
        (
            "#12P#00012FAhaha...\x02\x03",
            "#00006F(I was a "Master Fisherman"...\x01",
            "I worked pretty hard on it.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E6D")

    label("loc_4D87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4E16")

    ChrTalk(
        0x101,
        (
            "#12P#00009FAhaha...\x02\x03",
            "#00003F(I was only a "Novice Fisherman" in the\x01",
            " first place, so I've got nothing to worry about.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E6D")

    label("loc_4E16")


    ChrTalk(
        0x101,
        (
            "#12P#00009FAhaha...\x02\x03",
            "#00006F(*sigh*. With this, my rank\x01",
            " will be reset too, huh.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E6D")

    SetChrSubChip(0xA, 0x0)

    ChrTalk(
        0xA,
        (
            "#5PWell then, we'll supply you\x01",
            "with a new set of fishing gear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PPeter, Coppen, and Member\x01",
            "Lloyd too. Take these.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0xB4, 0x1F4)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x14),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x14, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x3),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x3, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x189),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x10\x01",
            scpstr(SCPSTR_CODE_ITEM, 0x187),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x10 received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x189, 10)
    AddItemNumber(0x187, 10)
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 0)), scpexpr(EXPR_END)), "loc_50E7")

    ChrTalk(
        0xA,
        (
            "#5PThese too are freebies for Member Lloyd,\x01",
            "who once rose to the rank of "Divine Fisherman".\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "Furthermore, received ",
            scpstr(SCPSTR_CODE_ITEM, 0x189),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x20 and\x01",
            scpstr(SCPSTR_CODE_ITEM, 0x187),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x20.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x189, 20)
    AddItemNumber(0x187, 20)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#12P#00002FT-Thank you very much.\x02",
    )

    CloseMessageWindow()
    Jump("loc_520C")

    label("loc_50E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 1)), scpexpr(EXPR_END)), "loc_520C")

    ChrTalk(
        0xA,
        (
            "#5PThese too are freebies for Coppen\x01",
            "and Member Lloyd, who were\x01",
            "once "Master Fishermen".\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "Furthermore, received ",
            scpstr(SCPSTR_CODE_ITEM, 0x189),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x10 and\x01",
            scpstr(SCPSTR_CODE_ITEM, 0x187),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x10.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x189, 10)
    AddItemNumber(0x187, 10)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#12P#00002FT-Thank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5PI'll accept them thankfully.\x02",
    )

    CloseMessageWindow()
    Jump("loc_520C")

    label("loc_520C")


    ChrTalk(
        0xA,
        (
            "#5PWell then, I'll leave\x01",
            "the rest to you guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PAs for me, I plan on searching\x01",
            "for a new office for us, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PLet's have another meeting soon to exchange\x01",
            "info regarding how best to contain the\x01",
            "activities of the Fishing Emperor Club.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYes, all right.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x1F)
    SetChrSubChip(0xC, 0x0)
    StopSound(128, 2000, 40)
    StopBGM(0xBB8)
    WaitBGM()
    SetScenarioFlags(0x22, 4)
    NewScene("c0500", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_14_3EAD end

    def Function_15_5356(): pass

    label("Function_15_5356")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch46500.itc", 0x1E)
    LoadChrToIndex("apl/ch51230.itc", 0x1F)
    LoadChrToIndex("apl/ch51270.itc", 0x20)
    OP_68(1350, 1830, 1580, 0)
    MoveCamera(315, 26, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, -100, 0, 1950, 270)
    SetChrPos(0x102, -100, 0, 3150, 270)
    SetChrPos(0x104, 1060, 0, 2520, 270)
    SetChrPos(0x109, 2020, 0, 1660, 270)
    SetChrPos(0x105, 1590, 0, 3440, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 0x1F)
    SetChrSubChip(0x10, 0x0)
    EndChrThread(0x10, 0x0)
    SetChrBattleFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x2)
    SetChrFlags(0x10, 0x10)
    SetChrFlags(0x10, 0x20)
    SetChrPos(0x10, -13920, 550, 4900, 45)
    BeginChrThread(0x10, 0, 0, 16)
    OP_4B(0x8, 0xFF)
    SetChrSubChip(0x9, 0x1)
    SetChrPos(0x8, -5430, 0, 6530, 0)
    TurnDirection(0x8, 0x10, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(-13000, 1830, 4650, 3000)
    MoveCamera(292, 17, 0, 3000)
    OP_6E(400, 3000)
    SetCameraDistance(19150, 3000)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        "#00005F(M-Mr. Olivier...?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F(Wow... He's pretty\x01",
            "good, isn't he.)\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-7750, 1830, 3690, 3000)
    MoveCamera(301, 22, 0, 3000)
    OP_6E(400, 3000)
    SetCameraDistance(21280, 3000)
    OP_6F(0x79)
    StopBGM(0x3E8)
    WaitBGM()
    Fade(500)
    SetChrFlags(0x10, 0x8000)
    ClearChrFlags(0x10, 0x4)
    ClearChrFlags(0x10, 0x2)
    ClearChrFlags(0x10, 0x10)
    ClearChrFlags(0x10, 0x20)
    EndChrThread(0x10, 0x0)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x10, 0x1E)
    SetChrSubChip(0x10, 0x0)
    SetChrPos(0x10, -11230, 400, 3690, 90)
    OP_0D()

    ChrTalk(
        0x10,
        (
            "#5P#13904FHmph... \x01",
            "Thank you for listening.\x02",
        )
    )

    CloseMessageWindow()
    Sound(971, 0, 50, 0)

    ChrTalk(
        0x9,
        "Bravooo!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "You're amazingly good, mister!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Would you like to play\x01",
            "for us for a while?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I could pay you a\x01",
            "little something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#13909FOoh, that is\x01",
            "quite tempting!\x02\x03",
            "#13900FOf course, I\x01",
            "gladly accept.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00007FW-Wait a minute there!!\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7117", 0)
    OP_68(-7500, 1630, 2280, 3000)
    MoveCamera(325, 17, 0, 3000)
    OP_6E(400, 3000)
    SetCameraDistance(22280, 3000)

    def lambda_5758():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5758)
    Sleep(50)

    def lambda_5775():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5775)
    Sleep(50)

    def lambda_5792():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5792)
    Sleep(50)

    def lambda_57AF():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_57AF)
    Sleep(50)

    def lambda_57CC():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_57CC)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)
    OP_63(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x10,
        (
            "#5P#13905FW-What's this now?\x01",
            "So you've found me already...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FW-What're you doing going\x01",
            "around taking jobs randomly!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00306FDamn. This guy's crazy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#13904FHmph, cease and desist, I say.\x01",
            "I am embarrassed by such flattery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00301FNo one is complimentin' you!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10101FThis time, we're taking you with us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#13910FNow, now. I see all of you don't\x01",
            "know when to give up either.\x02\x03",
            "#13900FA life must be lived more\x01",
            "cheerfully, more enjoyably.\x02\x03",
            "#13904FI now give you the\x01",
            "following words of advice.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x10, 0x20)
    SetChrSubChip(0x10, 0x0)
    OP_0D()

    ChrTalk(
        0x10,
        (
            "#5P#13912FSoften your hardened hearts, \x01",
            "and let love and devotion be your guide...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00103F*sigh*...\x02",
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x10,
        (
            "#5P#13905FOh... What ever is the\x01",
            "matter, mademoiselle?\x02\x03",
            "#13904FA gloomy sigh has its\x01",
            "own sex appeal. Has\x01",
            "happiness escaped you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103FLet me be clear,\x01",
            "just in case.\x02\x03",
            "#00100FWe were asked by Mr. Mueller\x01",
            "to bring you back no matter\x01",
            "what we have to do.\x02\x03",
            "#00109FIt seems we can even use\x01",
            "a little force on you...?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x10)
    Fade(500)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x10, 0x1E)
    SetChrSubChip(0x10, 0x0)
    OP_0D()

    ChrTalk(
        0x10,
        (
            "#5P#13911FO-Ok! \x01",
            "I'll go back! I promise!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012F(Elie, that smile is\x01",
            "really creepy...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#13910FAw, man... I suppose\x01",
            "it's about time anyway.\x02\x03",
            "#13900FVery well then. Will you\x01",
            "show me the way to Mueller?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10108FHmm, but... I think it\x01",
            "would be better to have\x01",
            "Mr. Mueller come here.\x02\x03",
            "#10106FThis one might cause trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FWell, that's the safest option. He might\x01",
            "try to run away while we're escorting him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#5P#13910FOh boy, you guys don't trust me, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FA-Anyway, \x01",
            "I'll try contacting the station.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 5)
    NewScene("c0500", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_5356 end

    def Function_16_5E8B(): pass

    label("Function_16_5E8B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5EDA")
    SetChrSubChip(0xFE, 0x0)
    Sleep(200)
    SetChrSubChip(0xFE, 0x1)
    Sleep(200)
    SetChrSubChip(0xFE, 0x2)
    Sleep(200)
    SetChrSubChip(0xFE, 0x3)
    Sleep(200)
    SetChrSubChip(0xFE, 0x4)
    Sleep(200)
    SetChrSubChip(0xFE, 0x3)
    Sleep(200)
    SetChrSubChip(0xFE, 0x2)
    Sleep(200)
    SetChrSubChip(0xFE, 0x1)
    Sleep(200)
    SetChrSubChip(0xFE, 0x0)
    Sleep(200)
    Jump("Function_16_5E8B")

    label("loc_5EDA")

    Return()

    # Function_16_5E8B end

    def Function_17_5EDB(): pass

    label("Function_17_5EDB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("chr/ch45100.itc", 0x22)
    LoadChrToIndex("chr/ch45102.itc", 0x23)
    OP_68(-7510, 900, -380, 0)
    MoveCamera(300, 15, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(20290, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x1)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x1)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x1)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, -7000, 100, -2050, 0)
    SetChrPos(0x102, -5800, 100, -2050, 0)
    SetChrPos(0x103, -4600, 100, -2050, 0)
    SetChrPos(0x104, -3100, 100, -500, 270)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 0x23)
    SetChrSubChip(0x11, 0x2)
    SetChrPos(0x11, -8400, 100, -500, 90)
    ClearChrFlags(0x11, 0x8000)
    PlayBGM("ed7117", 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00005F#6PJazz Bar "Garante"...\x01",
            "Why are we here again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PThree years ago, I promised\x01",
            "Guy I'd exchange information\x01",
            "with him here, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PIt was just about to when I\x01",
            "heard the news of his death.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00006FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5P#5P...The cause of the Cult incident, the arrest\x01",
            "of the Imperial and Republican Faction\x01",
            "congressmen and the election of a new mayor...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PThe opening of the Trade Conference,\x01",
            "the attack on Crossbell City...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5P...And now, the declaration\x01",
            "of independence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PAll of these appear unrelated, but the\x01",
            "events all have the same mutual cause.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PWhat I'm trying to say is, all of the\x01",
            "events are part of the same chain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00101FA single chain of events...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PAnd in order to grasp the "main\x01",
            "points" of that chain, I'll need to\x01",
            "take a good look at each event in it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PBy doing that, I think I\x01",
            "can shed new light on the\x01",
            "Guy Bannings murder case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PThinking this, I suggested\x01",
            "this case review.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PMr. Lloyd, I know that this\x01",
            "can be hard on you, however...\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x1388)

    ChrTalk(
        0x101,
        (
            "#6P#00003F............\x02\x03",
            "#00000FNo... I'm all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00108FLloyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00208FMr. Lloyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303F...Well, we don't have time.\x02\x03",
            "#00300FAnyway, let's get started.\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7302", 0)

    ChrTalk(
        0x11,
        (
            "#5PYes... \x01",
            "Let's begin right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PFirst, the situation in which\x01",
            "Mr. Guy's remains were found―\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PIt was three years ago. The weather was cloudy, \x01",
            "with light rain. The place was the Orchis Tower \x01",
            "construction site, where it now stands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PThe time of death was just after\x01",
            "dawn, although it was half a day\x01",
            "before his body was found.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#5PAnd as for the cause of death―\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PIt was blood loss from the shock\x01",
            "of being shot through the heart\x01",
            "from behind by an orbal gun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#5P...Any mistakes so far?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00003FNo... It happened just as you've said.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00101FFrom behind...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00306FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00208F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PYes... Then, the crime scene at the time\x01",
            "the body was discovered was surveyed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PFirst of all, there were traces of a\x01",
            "fierce battle all around the scene, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PNot a thing remained except\x01",
            "for Mr. Guy's belongings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PFurthermore, his\x01",
            "favorite tonfas had been\x01",
            "taken from the scene...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PThe police badge that was on his\x01",
            "chest had been taken as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#5PThe badge was found recently, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PIs it possible to prove the\x01",
            "badge was taken by a member\x01",
            "of the "Revache" mafia?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FYes. We heard that information\x01",
            "directly from President Marconi.\x02\x03",
            "#00001FFurthermore, the member that\x01",
            "took it confessed to the police.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#5PHmm, I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PThen, let's also confirm\x01",
            "there were no witnesses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#5P...No one saw the conclusion of the fight.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PAt the time of Mr. Guy's death,\x01",
            "construction was suspended\x01",
            "and no staff were present.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PFurthermore, it was just after dawn. There\x01",
            "were echoes of wind, light rain and thunder...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PThere was no one near the scene,\x01",
            "so no one could have seen the\x01",
            "moment of Mr. Guy's murder.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PFurthermore, Mr. Guy hadn't\x01",
            "spoken with anyone on his\x01",
            "way to the scene.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5P...That's all I've been able to learn about\x01",
            "the circumstances surrounding the event.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#5PMr. Lloyd, can you add anything?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FNo, nothing in particular...\x02\x03",
            "#00001FMy understanding is the same as you've explained it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00108F(Mr. Nielsen... His information collecting\x01",
            "ability is amazing as always.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203F(Yes. And it seems\x01",
            "he knew Mr. Guy\x01",
            "personally...)\x02\x03",
            "#00201F(That might be why he's so\x01",
            "interested in this case.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PYes... Let's move on\x01",
            "to the case review.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PTo get to the truth of this case,\x01",
            "we must consider the criminal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PWe have to think about the\x01",
            "most likely suspects...\x01",
            ""Revache" or the "D∴G Cult" staff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#5PMr. Lloyd, you think either could be the criminal?\x02",
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 2)
    ClearScenarioFlags(0x0, 3)
    ClearScenarioFlags(0x0, 4)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6ED3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7092")
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
            "#1KCould Guy have been killed by the mafia, \x01",
            "or by someone from the D∴G Cult?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "The criminal is someone from the mafia\x01",      # 0
            "The criminal is someone from the Cult\x01",       # 1
            "It couldn't be either of them\x01",               # 2
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
        (0, "loc_6FF8"),
        (1, "loc_702B"),
        (2, "loc_705E"),
        (SWITCH_DEFAULT, "loc_707F"),
    )


    label("loc_6FF8")


    ChrTalk(
        0x101,
        "#6P#00006F(...No, that's not right―)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_707F")

    label("loc_702B")


    ChrTalk(
        0x101,
        "#6P#00006F(...No, that's not right―)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_707F")

    label("loc_705E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7077")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7077")

    SetScenarioFlags(0x0, 2)
    Jump("loc_707F")

    label("loc_707F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_708D")
    Jump("loc_7092")

    label("loc_708D")

    Jump("loc_6ED3")

    label("loc_7092")


    ChrTalk(
        0x101,
        (
            "#6P#00003FNo. It couldn't have been either of them.\x02\x03",
            "#00008FRegarding Revache, it couldn't\x01",
            "be Marconi or that subordinate―\x02\x03",
            "#00001FRegarding the Cult, Joachim himself\x01",
            "said although he planned the murder,\x01",
            "he didn't get the chance to carry it out.\x02\x03",
            "#00006FFurthermore, it's hard to believe\x01",
            "another staff member unbeknownst to\x01",
            "them would rampage and do such a thing.\x02\x03",
            "#00013F...On top of that, I heard my\x01",
            "brother was on guard against\x01",
            "those two forces.\x02\x03",
            "My brother wouldn't be led into a\x01",
            "situation where his life could be taken...\x02\x03",
            "I think that possibility is very remote.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00306F...I know, right.\x02\x03",
            "#00301FBased on what I heard, on top of his audacity\x01",
            "he also had a terrifically keen nose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00206F...Yes.\x02\x03",
            "#00201FI don't think he is the type to fall behind\x01",
            "his opponents, the mafia and the Cult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PIt is certainly true that each component\x01",
            "negates those possibilities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PPerhaps before the Cult incident it\x01",
            "was, but now, it's quite impossible\x01",
            "for either party to be the culprit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PYes. Next, we'll consider the possibility it was\x01",
            "done by someone from the two major powers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PWe must also consider congressmen of Imperial and\x01",
            "Republican Factions that coveted right, government\x01",
            "officials deeply involved with either country and\x01",
            "intelligence agencies' staff―\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PIs it possible that Guy\x01",
            "fell into the hands of\x01",
            "someone like that?\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 2)
    ClearScenarioFlags(0x0, 3)
    ClearScenarioFlags(0x0, 4)

    label("loc_75F8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_77E3")
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
            "#1KWas Guy killed by Imperial or Republican staff?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "It is highly likely\x01",      # 0
            "It is unlikely\x01",           # 1
            "Impossible to say\x01",        # 2
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
        (0, "loc_76CB"),
        (1, "loc_773B"),
        (2, "loc_775C"),
        (SWITCH_DEFAULT, "loc_77D0"),
    )


    label("loc_76CB")


    ChrTalk(
        0x101,
        (
            "#6P#00008F(It's highly likely...\x01",
            "...Is that really right?)\x02\x03",
            "#00001F(Think again,\x01",
            "Lloyd Bannings―)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_77D0")

    label("loc_773B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7754")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7754")

    SetScenarioFlags(0x0, 2)
    Jump("loc_77D0")

    label("loc_775C")


    ChrTalk(
        0x101,
        (
            "#6P#00008F(It's impossible to say...\x01",
            "...Is that really right?)\x02\x03",
            "#00001F(Think again,\x01",
            "Lloyd Bannings―)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_77D0")

    label("loc_77D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_77DE")
    Jump("loc_77E3")

    label("loc_77DE")

    Jump("loc_75F8")

    label("loc_77E3")


    ChrTalk(
        0x101,
        (
            "#6P#00003FNo. I think\x01",
            "that's unlikely.\x02\x03",
            "#00008FIt's true there're a lot of staff within the two\x01",
            "major powers who did injustice in Crossbell.\x02\x03",
            "I even heard that my brother was\x01",
            "closing in on a number of them.\x02\x03",
            "#00001FAdditionally, it's confirmed\x01",
            "that intelligence staff were\x01",
            "frequently visiting Crossbell.\x02\x03",
            "#00006FBut, to put it bluntly― If my\x01",
            "brother seriously wounded any of\x01",
            "them, nothing would come of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106FYou're certainly right about that...\x02\x03",
            "#00108FIf the two major powers felt like it,\x01",
            "they could have controlled the police\x01",
            "through the state government...\x02\x03",
            "#00101FIn the previous governmental\x01",
            "structure, that kind of pressure\x01",
            "would have been easy to apply.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FYeah. No matter how troublesome\x01",
            "he was, luring a lone detective\x01",
            "somewhere to get rid of him would be―\x02\x03",
            "#00001FFrom the start, such\x01",
            "an action would not\x01",
            "be worth its cost.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#5PHm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303FFor argument's sake,\x01",
            "let's say Lloyd's bro was\x01",
            "in contact with them.\x02\x03",
            "#00300FIt's the same as the mafia. He'd\x01",
            "never fall into a trap unprepared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00206FI agree.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PAs expected from you all...\x01",
            "I have nothing to add.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#5PLet's move on to our final consideration―\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PWe've been able to\x01",
            "eliminate all suspects\x01",
            "considered thus far, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PCould there be anyone else who\x01",
            "fits the criminal's profile?\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 2)
    ClearScenarioFlags(0x0, 3)
    ClearScenarioFlags(0x0, 4)

    label("loc_7D18")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7FB5")
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
            "#1KThen, someone else who fits the criminal's profile?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Someone from "Ouroboros"\x01",           # 0
            "Someone from Crossbell Police\x01",      # 1
            "Someone Guy knew very well\x01",         # 2
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
        (0, "loc_7E0C"),
        (1, "loc_7EA6"),
        (2, "loc_7F81"),
        (SWITCH_DEFAULT, "loc_7FA2"),
    )


    label("loc_7E0C")


    ChrTalk(
        0x101,
        (
            "#6P#00006F(That organization is certainly full of\x01",
            "mysteries, but... Think a little harder.)\x02\x03",
            "#00013F(There should be a\x01",
            "more natural answer.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_7FA2")

    label("loc_7EA6")


    ChrTalk(
        0x101,
        (
            "#6P#00008F(An inside job by someone with a grudge.\x01",
            "I can't eliminate that possibility, but\x01",
            "there should be a better answer.)\x02\x03",
            "#00013F(Based on the flow up until now, there\x01",
            "should be a more natural answer.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_7FA2")

    label("loc_7F81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7F9A")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7F9A")

    SetScenarioFlags(0x0, 2)
    Jump("loc_7FA2")

    label("loc_7FA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_7FB0")
    Jump("loc_7FB5")

    label("loc_7FB0")

    Jump("loc_7D18")

    label("loc_7FB5")

    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#6P#00003FSomeone my big brother knew very well,\x01",
            "even though he was cautious.\x02\x03",
            "#00001FI think it might be someone\x01",
            "with that kind of profile.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#6P#00205FEh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00301FThat's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#5PYes, and your reasons?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FFirst of all, big brother didn't\x01",
            "reveal the fact he was heading\x01",
            "to the scene to anyone.\x02\x03",
            "#00008FBecause of that,\x01",
            "it's certain he\x01",
            "went there alone.\x02\x03",
            "#00013FIf you think about it, I think\x01",
            "you can say it's likely the criminal\x01",
            "was an "acquaintance" of his.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00106FY-You're right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FDid my brother call his acquaintance\x01",
            "to the scene? Or was he himself there?\x01",
            "We don't know.\x02\x03",
            "#00003FThe crime scene was a construction\x01",
            "site where no one was present―\x02\x03",
            "#00008FIn other words, there must have been an\x01",
            "important conversation. He needed to make sure\x01",
            "what he didn't want to be heard, couldn't be.\x02\x03",
            "#00013FSome kind of exchange took place there... \x01",
            "When it broke down, he lost his life. \x01",
            "Could that have been it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#5PAnd as for that exchange...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FI have no idea of the specifics.\x02\x03",
            "#00008FIt's just that, because\x01",
            "he lost his life over it, it\x01",
            "must've been very important...\x02\x03",
            "#00001FFor example... It might have been related\x01",
            "to "some kind of conspiracy" or something.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#6P#00200FA conspiracy, you say...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#5PHm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F...Mr. Nielsen, you said to\x01",
            ""grasp the main points and \x01",
            "shine a light on them".\x02\x03",
            "#00000FWhen I heard them, although it's\x01",
            "faint, I feel they're connected.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x11,
        "#5POoh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FIt's possible my brother was asked\x01",
            "to join some kind of conspiracy...\x02\x03",
            "#00003FWhether it's the D∴G Cult or the\x01",
            "mafia, the Empire or the Republic\x01",
            "or someone else entirely...\x02\x03",
            "#00008FThey were advancing their plans. It's possible\x01",
            "they're still advancing them, even now.\x02\x03",
            "#00001FBut in the end, that's\x01",
            "only a guess, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00105FSomeone else...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00201FAnd also, that it could still be in progress...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001FYeah. I can only say that\x01",
            "because my brother's killer\x01",
            "still hasn't been found.\x02\x03",
            "#00003FAnd these incidents haven't\x01",
            "ended either. That's the\x01",
            "best proof of all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#5P............\x02",
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00005FMr. Nielsen?\x02\x03",
            "#00006F...As expected, is it unreasonable?\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x11)
    Sleep(500)

    ChrTalk(
        0x11,
        (
            "#5PNo... I think that's\x01",
            "sound reasoning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#5P──I'll be frank, Mr. Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PWhile we were conducting this review,\x01",
            "did a certain character come to mind?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PA character who you could think, three years ago,\x01",
            "called Mr. Guy out the construction site and killed him?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#6P#00006FNo, unfortunately...\x02\x03",
            "#00003FAlthough it was an "acquaintance", my brother\x01",
            "knew a staggering amount of people.\x02\x03",
            "#00008F...It's the truth that, at the scene, \x01",
            "he was shot from behind\x01",
            "and his tonfas were taken...\x02\x03",
            "#00013FPersonally, I feel like those\x01",
            "elements are the key to\x01",
            "explaining the incident, but...\x02\x03",
            "#00006FIf it were possible to identify someone\x01",
            "with just that, Section One would have\x01",
            "already done it three years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#5PHmm, it's possible.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PAt present, all of the pieces that\x01",
            "point to the criminal aren't in place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5P―However, there's only\x01",
            "something I can clearly say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PThe one who can find the missing pieces\x01",
            "is you, Mr. Lloyd── and you alone.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x102,
        "#6P#00105FMr. Nielsen...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)

    ChrTalk(
        0x101,
        "#6P#00004FYes... And I plan to do just that.\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7151", 0)

    ChrTalk(
        0x11,
        "#5PHu hu, glad to hear it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5P...I feel almost as if I've kept my\x01",
            "promise to exchange information\x01",
            "with Mr. Guy three years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PI'd like to thank all of you\x01",
            "for joining me for this review.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FWe should be thanking you too.\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PI'll excuse myself then... I'm looking\x01",
            "forward to your future activities.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x11, 0x22)
    ClearChrFlags(0x11, 0x4)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, -8170, 0, -500, 90)
    OP_0D()
    Sleep(500)

    def lambda_8F50():
        OP_95(0xFE, -7730, 0, 1910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8F50)
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x103, 0x0)
    WaitChrThread(0x11, 1)

    def lambda_8F80():
        OP_95(0xFE, 690, 0, 1520, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8F80)
    SetChrSubChip(0x101, 0x2)
    Sleep(50)
    SetChrSubChip(0x102, 0x2)
    Sleep(50)
    SetChrSubChip(0x103, 0x2)
    Sleep(50)
    SetChrSubChip(0x104, 0x2)
    WaitChrThread(0x11, 1)
    SetChrSubChip(0x101, 0x2)
    Sleep(50)
    SetChrSubChip(0x102, 0x2)
    Sleep(50)
    SetChrSubChip(0x103, 0x2)
    Sleep(50)
    SetChrSubChip(0x104, 0x2)

    ChrTalk(
        0x103,
        (
            "#6P#00202FMr. Nielsen... \x01",
            "It is almost as if\x01",
            "he was guiding us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00004FYeah... Probably, his promise to my brother\x01",
            "has been weighing on his mind this whole time.\x02\x03",
            "#00002FI'm glad I spoke to him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00109F*giggle*... I agree.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00304FI know, right?\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x104, 0x1)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#6P#00301F#12P...Alright, this stuff has motivated me.\x01",
            "It's time to go!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00003FYeah... Anyway, let's hurry to the president's\x01",
            "room in the old Revache building.\x02\x03",
            "#00013FThere should be some intel we\x01",
            "can get from Captain Lechter!\x02",
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
            "Quest [Guy Bannings Murder Case Review]\x07\x00",
            " completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9255")
    OP_2C(0x95, 0x2)
    Jump("loc_9269")

    label("loc_9255")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9269")
    OP_2C(0x95, 0x1)

    label("loc_9269")

    ClearChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x11, 0x0)
    SetChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x104, 0x4)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    SetChrPos(0x0, -4660, 0, 1270, 90)
    OP_69(0xFF, 0x0)
    OP_29(0x95, 0x1, 0x0)
    OP_29(0x95, 0x4, 0x10)
    EventEnd(0x5)
    Return()

    # Function_17_5EDB end

    SaveToFile()

Try(main)
