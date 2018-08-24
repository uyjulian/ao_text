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
        "Function_4_68F",          # 04, 4
        "Function_5_693",          # 05, 5
        "Function_6_21EC",         # 06, 6
        "Function_7_3266",         # 07, 7
        "Function_8_333D",         # 08, 8
        "Function_9_33D7",         # 09, 9
        "Function_10_34A3",        # 0A, 10
        "Function_11_3545",        # 0B, 11
        "Function_12_3DCE",        # 0C, 12
        "Function_13_3E3C",        # 0D, 13
        "Function_14_3E89",        # 0E, 14
        "Function_15_526A",        # 0F, 15
        "Function_16_5D80",        # 10, 16
        "Function_17_5DD0",        # 11, 17
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
            ""Regular Menu For\x01",
            "Businessmen" is here.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_68B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x17)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68B")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Learned the \x07\x00",
            ""Rich\x01",
            "Cappuccino"\x07\x00",
            " recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_68B")

    TalkEnd(0xFF)
    Return()

    # Function_3_5D6 end

    def Function_4_68F(): pass

    label("Function_4_68F")

    Call(0, 5)
    Return()

    # Function_4_68F end

    def Function_5_693(): pass

    label("Function_5_693")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x139, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7BB")

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
        "Oh... If it isn't Wazy.\x02",
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
            "#10303FHaha. I'm in the middle\x01",
            "of a little patrol.\x02\x03",
            "#10300FI'll come here again to\x01",
            "drink whenever I have\x01",
            "time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Alright. I'll be\x01",
            "waiting.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x139, 3)
    TalkEnd(0x8)
    Return()

    label("loc_7BB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7C5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21E8")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_817")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_817")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_837")
    OP_AF(0x42)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_21E3")

    label("loc_837")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_84B")
    Jump("loc_21E3")

    label("loc_84B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21E3")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_A3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_991")

    ChrTalk(
        0x8,
        (
            "Before long, Heiyue will\x01",
            "grab the real power in\x01",
            "the underworld.\x02",
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
    Jump("loc_A36")

    label("loc_991")


    ChrTalk(
        0x8,
        (
            "Before long, Heiyue will\x01",
            "grab the real power in\x01",
            "the underworld.\x02",
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

    label("loc_A36")

    Jump("loc_21E3")

    label("loc_A3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_AD5")

    ChrTalk(
        0x8,
        (
            "It looks like those\x01",
            "monsters didn't enter\x01",
            "Back Street.\x02",
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
    Jump("loc_21E3")

    label("loc_AD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_CC6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BED")

    ChrTalk(
        0x8,
        (
            "The declaration of\x01",
            "independence will greatly\x01",
            "influence the underworld.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "From now on, the State Guard\x01",
            "will crack down on both\x01",
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
    Jump("loc_CC1")

    label("loc_BED")


    ChrTalk(
        0x8,
        (
            "From now on, the State Guard\x01",
            "will crack down on both\x01",
            "Imperial and Republican mafias.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Though the declaration of independence was\x01",
            "a sudden development... maybe Crossbell\x01",
            "needs drastic measures right now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CC1")

    Jump("loc_21E3")

    label("loc_CC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_E9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DDD")

    ChrTalk(
        0x8,
        (
            "The attack on Crossbell\x01",
            "City... "Red Constellation"\x01",
            "has done the unthinkable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even in this store where it's easy\x01",
            "to get underworld information, I\x01",
            "didn't sense any ill omens...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Most likely, it was\x01",
            "planned in detail quite\x01",
            "a long time ago.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E99")

    label("loc_DDD")


    ChrTalk(
        0x8,
        (
            "Even in this store where it's easy\x01",
            "to get underworld information, I\x01",
            "didn't sense any ill omens...\x02",
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

    label("loc_E99")

    Jump("loc_21E3")

    label("loc_E9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_107B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FBE")

    ChrTalk(
        0x8,
        (
            "Even though they realized "Red\x01",
            "Constellation" is gone, the police\x01",
            "look like they're in a panic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Those guys evaded detection\x01",
            "by moving underground and\x01",
            "headed for Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Although I couldn't tell\x01",
            "you the significance of\x01",
            "this occupation incident.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1076")

    label("loc_FBE")


    ChrTalk(
        0x8,
        (
            "Even though they realized "Red\x01",
            "Constellation" is gone, the police\x01",
            "look like they're in a panic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Although I couldn't tell\x01",
            "you the significance of\x01",
            "this occupation incident.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1076")

    Jump("loc_21E3")

    label("loc_107B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_121F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_117A")

    ChrTalk(
        0x8,
        (
            "Yesterday's derailment... According\x01",
            "to rumor, it was caused by a giant\x01",
            "monster that appeared nearby.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But with the referendum\x01",
            "approaching, I can't think\x01",
            "it was any ordinary monster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...I feel it's very\x01",
            "suspicious.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_121A")

    label("loc_117A")


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
        (
            "...I feel it's very\x01",
            "suspicious.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_121A")

    Jump("loc_21E3")

    label("loc_121F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1281")

    ChrTalk(
        0x8,
        (
            "I hear sirens in the\x01",
            "distance...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...I'm getting a bad\x01",
            "feeling about this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21E3")

    label("loc_1281")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_14EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1421")

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
            "According to underworld\x01",
            "rumors, it was Heiyue\x01",
            "that tracked them down.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_13BD")

    ChrTalk(
        0x101,
        (
            "#00005F(So Heiyue operatives\x01",
            "were there, huh...)\x02\x03",
            "#00003F(I didn't notice them,\x01",
            "but they don't miss a\x01",
            "beat, do they.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1419")

    label("loc_13BD")


    ChrTalk(
        0x8,
        (
            "I don't know if I should've\x01",
            "expected it, but... Those guys\x01",
            "don't miss a beat, do they.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1419")

    SetScenarioFlags(0x0, 0)
    Jump("loc_14E9")

    label("loc_1421")


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
            "I don't know if I should've\x01",
            "expected it, but... Those guys\x01",
            "don't miss a beat, do they.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14E9")

    Jump("loc_21E3")

    label("loc_14EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_16C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1623")

    ChrTalk(
        0x8,
        (
            "Rumor has it that the Republican government\x01",
            "asked "Red Constellation" to intercept\x01",
            "terrorists at the trade conference, but...\x02",
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
            "...Those guys are real\x01",
            "pro jaegers, for better\x01",
            "or worse.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16BD")

    label("loc_1623")


    ChrTalk(
        0x8,
        (
            "Crimson & Co. too, that acted\x01",
            "during the trade conference,\x01",
            "has been very quiet lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Those guys are real\x01",
            "pro jaegers, for better\x01",
            "or worse.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16BD")

    Jump("loc_21E3")

    label("loc_16C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1896")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17DF")

    ChrTalk(
        0x8,
        (
            "The "Red Constellation"\x01",
            "jaeger corps. And "Heiyue"\x01",
            "of Waterfront Area...\x02",
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
            "The officers I saw on\x01",
            "Back Street looked quite\x01",
            "nervous.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1891")

    label("loc_17DF")


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
            "The officers I saw on\x01",
            "Back Street looked quite\x01",
            "nervous.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1891")

    Jump("loc_21E3")

    label("loc_1896")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1A94")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1978")

    ChrTalk(
        0x8,
        (
            "The trade conference...\x01",
            "So it's finally started.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I feel the building\x01",
            "nervousness of the officers\x01",
            "patrolling Back Street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The guards assigned to\x01",
            "Crimson & Co. seem\x01",
            "strong.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_19FC")

    label("loc_1978")


    ChrTalk(
        0x8,
        (
            "I feel the building\x01",
            "nervousness of the officers\x01",
            "patrolling Back Street.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The guards assigned to\x01",
            "Crimson & Co. seem\x01",
            "strong.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19FC")

    Jump("loc_1A8F")

    label("loc_1A01")


    ChrTalk(
        0x8,
        (
            "Olivier is a pretty\x01",
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

    label("loc_1A8F")

    Jump("loc_21E3")

    label("loc_1A94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1D0F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C1B")

    ChrTalk(
        0x8,
        (
            "Crimson & Co. just moved\x01",
            "in to the back alley\x01",
            "building...\x02",
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
            "But rumor has it they're actually an\x01",
            "arm of "Red Constellation", the\x01",
            "strongest jaeger corps in West Zemuria.\x02",
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
    Jump("loc_1D0A")

    label("loc_1C1B")


    ChrTalk(
        0x8,
        (
            "Rumor has that Crimson & Co. is actually\x01",
            "an arm of "Red Constellation", the\x01",
            "strongest jaegers corps in West Zemuria...\x02",
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

    label("loc_1D0A")

    Jump("loc_21E3")

    label("loc_1D0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 4)), scpexpr(EXPR_END)), "loc_1DE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D8B")

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
            "Sandra said we might\x01",
            "want to close up shop\x01",
            "soon.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1DDE")

    label("loc_1D8B")


    ChrTalk(
        0x8,
        "...Did something happen?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Right now, Sandra and I\x01",
            "are the only ones here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DDE")

    Jump("loc_21E3")

    label("loc_1DE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1FBF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F09")

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
    Jump("loc_1FBA")

    label("loc_1F09")


    ChrTalk(
        0x8,
        (
            "At the same time,\x01",
            "there's the rise of\x01",
            "Heiyue to worry about.\x02",
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

    label("loc_1FBA")

    Jump("loc_21E3")

    label("loc_1FBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_21E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2112")

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
            "How much power did Revache\x01",
            "have? Now that they're gone, I\x01",
            "understand it a little better.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_21E3")

    label("loc_2112")


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
            "How much power did Revache\x01",
            "have? Now that they're gone, I\x01",
            "understand it a little better.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21E3")

    Jump("loc_7C5")

    label("loc_21E8")

    TalkEnd(0x8)
    Return()

    # Function_5_693 end

    def Function_6_21EC(): pass

    label("Function_6_21EC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2307")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22BE")
    SetChrSubChip(0xFE, 0x2)

    ChrTalk(
        0xFE,
        (
            "Ooh... Eric~, let's\x01",
            "drink~.\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0xFE,
        (
            "That weird mist is gone.\x01",
            "Isn't that cause for\x01",
            "celebration~?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xFE, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "Sandra, you're in my\x01",
            "way. Just go home\x01",
            "already.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x0)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x0, 1)
    Jump("loc_2302")

    label("loc_22BE")


    ChrTalk(
        0xFE,
        (
            "Ooh. You're so mean,\x01",
            "Eric...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, I love that about\x01",
            "you㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2302")

    Jump("loc_3262")

    label("loc_2307")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2392")

    ChrTalk(
        0xFE,
        (
            "So sleepy... Because we're\x01",
            "closed due to martial law, I\x01",
            "drank here and fell asleep...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "H-Huh? Did something\x01",
            "happen?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3262")

    label("loc_2392")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_24DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2468")

    ChrTalk(
        0xFE,
        (
            "There was a customer that\x01",
            "booked an "Independence\x01",
            "Day Party" right away.\x02",
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
            "They all looked happy,\x01",
            "so I guess that's a good\x01",
            "thing?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_24D5")

    label("loc_2468")


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
            "They all looked happy,\x01",
            "so I guess that's a good\x01",
            "thing?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24D5")

    Jump("loc_3262")

    label("loc_24DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_26E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2610")

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
            "gonna get a vacation~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We're just a simple club, but even we\x01",
            "have regulars who look forward to coming.\x01",
            "...Gotta do our best for now, I guess~.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_26DC")

    label("loc_2610")


    ChrTalk(
        0xFE,
        (
            "With the reconstruction\x01",
            "mostly complete, I'm never\x01",
            "gonna get a vacation~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We're just a simple club, but even we\x01",
            "have regulars who look forward to coming.\x01",
            "...Gotta do our best for now, I guess~.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26DC")

    Jump("loc_3262")

    label("loc_26E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2842")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27B9")

    ChrTalk(
        0xFE,
        (
            "Eric said it, but is\x01",
            "Crimson & Co. really run\x01",
            "by jaegers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ahh~... Crimson & Co.\x01",
            "runs the famed Neue-\x01",
            "Blanc, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I thought it was run by\x01",
            "run by the mafia. I was\x01",
            "surprised.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_283D")

    label("loc_27B9")


    ChrTalk(
        0xFE,
        (
            "Crimson & Co. that runs\x01",
            "Neue-Blanc are actually\x01",
            "jaegers, uh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I thought it was run by\x01",
            "run by the mafia. I was\x01",
            "surprised.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_283D")

    Jump("loc_3262")

    label("loc_2842")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_29AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2926")
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Hey, Eric~. Don't just\x01",
            "talk. Come have a drink\x01",
            "with me~...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xFE, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "You too Sandra. Don't\x01",
            "just sleep here. You\x01",
            "have a home, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Aww, you're such a\x01",
            "meanie, Eric~...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x0, 1)
    Jump("loc_29A7")

    label("loc_2926")


    ChrTalk(
        0xFE,
        (
            "Tch, that Eric. He's such\x01",
            "a meanie when it comes to\x01",
            "things like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, I l-o-v-e that\x01",
            "about him. ...Just\x01",
            "kidding㈱\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29A7")

    Jump("loc_3262")

    label("loc_29AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2AD2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A70")

    ChrTalk(
        0xFE,
        (
            "So sleepy... How do you like this,\x01",
            "you old lecher~! Know your place~!\x01",
            "And take this, and that...\x02",
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
    Jump("loc_2ACD")

    label("loc_2A70")


    ChrTalk(
        0xFE,
        (
            "Aww... I was such a nice\x01",
            "dream but I forgot it\x01",
            "already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm? Did something\x01",
            "happen?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2ACD")

    Jump("loc_3262")

    label("loc_2AD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2B56")

    ChrTalk(
        0xFE,
        (
            "So sleepy... That old\x01",
            "man's clingy as always~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We're not that kind of\x01",
            "store! I keep telling\x01",
            "him. Dammit~...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3262")

    label("loc_2B56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2CA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C1C")

    ChrTalk(
        0xFE,
        (
            "I heard there'll be a\x01",
            "referendum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Eric says I should go,\x01",
            "but it's kinda\x01",
            "complicated~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I mean, the voting hours\x01",
            "are right in the middle\x01",
            "of my sleeping time.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2CA0")

    label("loc_2C1C")


    ChrTalk(
        0xFE,
        (
            "I'm not sure if I'll\x01",
            "participate in the\x01",
            "referendum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I mean, the voting hours\x01",
            "are right in the middle\x01",
            "of my sleeping time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CA0")

    Jump("loc_3262")

    label("loc_2CA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2DE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D6A")
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Eric... Give me another\x01",
            "rum and cola...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xFE, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "Sandra, it's already\x01",
            "morning. Please go home\x01",
            "already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Aww, you're such a\x01",
            "meanie, Eric~...\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x0, 1)
    Jump("loc_2DDC")

    label("loc_2D6A")


    ChrTalk(
        0xFE,
        (
            "Eric's so mean... I wish\x01",
            "he'd go along with me\x01",
            "sometimes~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's been a while since\x01",
            "we closed the store.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DDC")

    Jump("loc_3262")

    label("loc_2DE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2EDA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E6B")

    ChrTalk(
        0xFE,
        (
            "Yesterday, a mean\x01",
            "customer came and drank\x01",
            "a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ooh~... I have a\x01",
            "headache. I went and did\x01",
            "it again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ED5")

    label("loc_2E6B")


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
            "I was dead tired from\x01",
            "work, but it fixed me\x01",
            "right up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2ED5")

    Jump("loc_3262")

    label("loc_2EDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2FC4")

    ChrTalk(
        0xFE,
        (
            "Neue-Blanc in Entertainment\x01",
            "District has been doing better\x01",
            "ever since Crimson & Co. arrived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "*sigh*, there must be a big difference\x01",
            "in revenue between a high-class club and\x01",
            "this place. Maybe I should transfer.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3262")

    label("loc_2FC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 4)), scpexpr(EXPR_END)), "loc_2FFA")
    OP_64(0x9)

    ChrTalk(
        0xFE,
        "*zzz, zzz*...\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)
    Jump("loc_3262")

    label("loc_2FFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3138")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30B4")

    ChrTalk(
        0xFE,
        (
            "*yawn*... I slept like a\x01",
            "log.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I always drop by this\x01",
            "place when I'm finished\x01",
            "hostessing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I mean, it's quiet and\x01",
            "comfortable so I can\x01",
            "sleep well.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3133")

    label("loc_30B4")


    ChrTalk(
        0xFE,
        (
            "This store is always\x01",
            "quiet, so I can sleep\x01",
            "well.\x02",
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

    label("loc_3133")

    Jump("loc_3262")

    label("loc_3138")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3262")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31D6")

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
            "*sigh*... I wonder why I\x01",
            "do this sort of work.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3262")

    label("loc_31D6")


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

    label("loc_3262")

    TalkEnd(0xFE)
    Return()

    # Function_6_21EC end

    def Function_7_3266(): pass

    label("Function_7_3266")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3298")
    Call(0, 14)
    Return()

    label("loc_3298")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "To start with, I plan to look\x01",
            "for a suitable office from\x01",
            "which to restart activities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Member Lloyd, let's\x01",
            "exchange information if\x01",
            "anything happens.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_3266 end

    def Function_8_333D(): pass

    label("Function_8_333D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_336F")
    Call(0, 14)
    Return()

    label("loc_336F")

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
            "What? A little rain is\x01",
            "no bother to me!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_333D end

    def Function_9_33D7(): pass

    label("Function_9_33D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3409")
    Call(0, 14)
    Return()

    label("loc_3409")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Even so, that man... He\x01",
            "truly can't be forgiven.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I don't know if he's a pro or\x01",
            "anything, but pretending to\x01",
            "be a fisherman just won't do.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_33D7 end

    def Function_10_34A3(): pass

    label("Function_10_34A3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34B8")
    Call(0, 11)
    Jump("loc_3541")

    label("loc_34B8")


    ChrTalk(
        0xD,
        (
            "#00600FNow then... I'll drink\x01",
            "this and then get back\x01",
            "to work.\x02\x03",
            "#00603FThe day of the\x01",
            "referendum is nearing. I\x01",
            "can't lose focus now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3541")

    TalkEnd(0xFE)
    Return()

    # Function_10_34A3 end

    def Function_11_3545(): pass

    label("Function_11_3545")

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
        "#00005FDetective Dudley.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#00603FYou guys, huh. Never\x01",
            "thought I'd see you\x01",
            "here.\x02\x03",
            "#00600FI'm told you're resuming\x01",
            "your support request\x01",
            "activities today?\x02",
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
            "of Red Constellation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#00600FHmph, that's been nothing but\x01",
            "trouble.\x02\x03",
            "We've been expecting something out\x01",
            "of the Imperial government on that\x01",
            "front, but not a single peep.\x02\x03",
            "#00603FIf something's going to happen,\x01",
            "it'll be in three days when the\x01",
            "independence referendum is held.\x02\x03",
            "#00600FWe're working tirelessly to\x01",
            "prepare for that day.\x02",
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
            "#00302FYou look depressed,\x01",
            "though.\x02\x03",
            "Are you drunk?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#00603FHmph. I'm a modest drinker\x01",
            "but there's no reason to\x01",
            "start drinking at noon.\x02\x03",
            "#00600FThis is just a soft drink.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FHaha, good work on\x01",
            "giving off that alcohol-\x01",
            "free atmosphere.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xD)

    ChrTalk(
        0xD,
        (
            "#00603F...Bannings, do you\x01",
            "drink?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FYes, but not that much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#00602FHmph. In that case,\x01",
            "you're very different\x01",
            "from Guy.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005FMight you have come here\x01",
            "for drinks with my\x01",
            "brother, Dudley?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#00603FWell, not that often.\x02\x03",
            "#00600FBy the way, Guy is the\x01",
            "one who introduced me to\x01",
            "this place.\x02\x03",
            "#00608FTrailblazing like that\x01",
            "was his forte.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHaha, I bet. With that\x01",
            "personality of his and\x01",
            "all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FSo who could hold their\x01",
            "liquor better, you or\x01",
            "him?\x02\x03",
            "It was you guys. You\x01",
            "must've thrown down with\x01",
            "each other at some point.\x02",
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
            "#00301FBoasting like that when\x01",
            "you don't even know how\x01",
            "much I can drink...\x02\x03",
            "#00304FYou're practically\x01",
            "begging me to show you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#00604FHmph, if there's a\x01",
            "chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FAhaha...\x02\x03",
            "(Dudley hates to lose\x01",
            "even in this department,\x01",
            "huh.)\x02",
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

    # Function_11_3545 end

    def Function_12_3DCE(): pass

    label("Function_12_3DCE")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Oh man, we're in a real\x01",
            "fix now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's no customers\x01",
            "today, so I guess I'll\x01",
            "take it easy.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_3DCE end

    def Function_13_3E3C(): pass

    label("Function_13_3E3C")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "What am I going to do?\x01",
            "If it's like this, I\x01",
            "can't return home...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_3E3C end

    def Function_14_3E89(): pass

    label("Function_14_3E89")

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
        (
            "Sorry to drag you here,\x01",
            "Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well then, we're all\x01",
            "here. Let's start the\x01",
            "meeting.\x02",
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
            "#5PFirst, we have to update\x01",
            "Lloyd on our current\x01",
            "status.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PActually, Fisherman's Guild\x01",
            "activities have been suspended for\x01",
            "months due to a restraining order.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005FR-Restraining order?\x02",
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
            "#5PAnd so, each of us\x01",
            "decided to take a fresh\x01",
            "look inside ourselves...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00108FBut, none of you were\x01",
            "responsible for that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PIt's true that we\x01",
            "weren't involved in the\x01",
            "incident...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PBut we spent so much\x01",
            "time with him as fellow\x01",
            "lovers of fishing.\x02",
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
            "#5PHonestly, we bear plenty\x01",
            "of social and personal\x01",
            "responsibility.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00003FCeldan...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P...Well anyway, let's\x01",
            "set all of that aside\x01",
            "for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PAbout a week ago, in the middle\x01",
            "of all that, we were contacted\x01",
            "by the real estate company.\x02",
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
            "#5PAlso, they informed us that\x01",
            "they formed a new contract with\x01",
            "the Imperial Fishing Club.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6PAfter that, we tried contacting an\x01",
            "Imperial Fishing Club representative,\x01",
            "but it didn't go so well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PAnd so today, when we stopped by\x01",
            "the office, their representative\x01",
            "just happened to be there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PThere, we finally\x01",
            "learned the truth about\x01",
            "the contract...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PThat's when all of you\x01",
            "came in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00005FI see.\x02\x03",
            "#00003FI think I understand the\x01",
            "situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PBut even so... The Lakelord\x01",
            "Company's Imperial Fishing\x01",
            "Club, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PIf they were merely expanding the\x01",
            "scope of their activities, I wouldn't\x01",
            "have thought anything of it, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PI never thought they\x01",
            "would stoop so low as to\x01",
            "take our office by force.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6PYes, they lack a good\x01",
            "reason to hate us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P...Anyway, with this,\x01",
            "their hate of us is\x01",
            "clear as day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PBut it's not like we can\x01",
            "do anything about the\x01",
            "situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PWell for now, it seems\x01",
            "all we can do is keep an\x01",
            "eye on things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P...But at this rate, our\x01",
            "guild might end up\x01",
            "dissolving.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PI know it's not enough... But right\x01",
            "now, we have to seize the moment\x01",
            "and think of a way out of this.\x02",
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
            "#6PHehe, well then. I hereby declare\x01",
            "that the Fisherman's Guild, Crossbell\x01",
            "Branch, has restarted operations!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PAlright! I've been\x01",
            "waiting for this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PBut... All members will\x01",
            "be starting over at\x01",
            "Novice Angler level.\x02",
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
        "#11PHuh?\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0xB,
        "#11PW-Wait a minute.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PYou mean... I'm no\x01",
            "longer a High-Rank\x01",
            "Angler?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x1)

    ChrTalk(
        0xA,
        (
            "#5PSorry, but that's how it\x01",
            "is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#11PBut all my effort...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6PCome now Coppen. If you\x01",
            "do your best, everything\x01",
            "will be fine.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0x87, 0x1F4)

    ChrTalk(
        0xB,
        (
            "#11POoh... I don't want to hear that\x01",
            "from you, who stopped advancing\x01",
            "at Hobby Angler level.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 0)), scpexpr(EXPR_END)), "loc_4C5F")

    ChrTalk(
        0x101,
        (
            "#12P#00012FAhaha...\x02\x03",
            "#00006F(I was a Divine Fisherman\x01",
            "of Crossbell... This is\x01",
            "pretty hard to take.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DAA")

    label("loc_4C5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 1)), scpexpr(EXPR_END)), "loc_4CC8")

    ChrTalk(
        0x101,
        (
            "#12P#00012FAhaha...\x02\x03",
            "#00006F(I was a Master\x01",
            "Fisherman... I worked\x01",
            "pretty hard on it.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DAA")

    label("loc_4CC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4D54")

    ChrTalk(
        0x101,
        (
            "#12P#00009FAhaha...\x02\x03",
            "#00003F(I was only a Novice Fisherman\x01",
            "in the first place, so I've\x01",
            "got nothing to worry about.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DAA")

    label("loc_4D54")


    ChrTalk(
        0x101,
        (
            "#12P#00009FAhaha...\x02\x03",
            "#00006F(*sigh*. With this, my\x01",
            "rank will be reset too,\x01",
            "huh.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DAA")

    SetChrSubChip(0xA, 0x0)

    ChrTalk(
        0xA,
        (
            "#5PWell then, we'll supply\x01",
            "you with a new set of\x01",
            "fishing gear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PPeter, Coppen, and you\x01",
            "too, Lloyd. Take these.\x02",
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
            " x10\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x189, 10)
    AddItemNumber(0x187, 10)
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 0)), scpexpr(EXPR_END)), "loc_5007")

    ChrTalk(
        0xA,
        (
            "#5PI have some extra freebies\x01",
            "for Member Lloyd, a former\x01",
            "Divine Fisherman.\x02",
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
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x189),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x20 and\x01",
            scpstr(SCPSTR_CODE_ITEM, 0x187),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x20, additionally.\x02",
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
    Jump("loc_511F")

    label("loc_5007")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 1)), scpexpr(EXPR_END)), "loc_511F")

    ChrTalk(
        0xA,
        (
            "#5PI have some extra freebies\x01",
            "for Member Lloyd, a former\x01",
            "Master Fisherman.\x02",
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
            "Received ",
            scpstr(SCPSTR_CODE_ITEM, 0x189),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x10 and\x01",
            scpstr(SCPSTR_CODE_ITEM, 0x187),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x10, additionally.\x02",
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
        (
            "#5PI'll accept them\x01",
            "thankfully.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_511F")

    label("loc_511F")


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
            "#5PAs for me, I plan to\x01",
            "look for a new office\x01",
            "for us, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PLet's have another meeting soon to exchange\x01",
            "info regarding how best to contain the\x01",
            "activities of the Imperial Fishing Club.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FAlright, understood.\x02",
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

    # Function_14_3E89 end

    def Function_15_526A(): pass

    label("Function_15_526A")

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
        "#00005F(O-Olivier?)\x02",
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
            "#5P#13904FHmph... Thank you for\x01",
            "listening.\x02",
        )
    )

    CloseMessageWindow()
    Sound(971, 0, 50, 0)

    ChrTalk(
        0x9,
        "Bravo!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "You're amazingly good!\x02",
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
            "I can pay you a little\x01",
            "something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#13909FOh, that is quite\x01",
            "tempting!\x02\x03",
            "#13900FOf course. I gladly\x01",
            "accept.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00007FW-Wait a minute!!\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7117", 0)
    OP_68(-7500, 1630, 2280, 3000)
    MoveCamera(325, 17, 0, 3000)
    OP_6E(400, 3000)
    SetCameraDistance(22280, 3000)

    def lambda_5651():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5651)
    Sleep(50)

    def lambda_566E():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_566E)
    Sleep(50)

    def lambda_568B():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_568B)
    Sleep(50)

    def lambda_56A8():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_56A8)
    Sleep(50)

    def lambda_56C5():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_56C5)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)
    OP_63(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x10,
        (
            "#5P#13905FWhat's this now? So\x01",
            "you've found me again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FW-What are you doing\x01",
            "going around taking jobs\x01",
            "randomly!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00306FDamn. This guy's crazy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#13904FCease and desist, I say.\x01",
            "I am embarrassed by such\x01",
            "flattery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00301FNo one is complimenting\x01",
            "you!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10101FThis time, we're taking\x01",
            "you with us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#13910FNow, now. I see all of\x01",
            "you don't know when to\x01",
            "give up either.\x02\x03",
            "#13900FA life must be lived\x01",
            "more cheerfully, more\x01",
            "enjoyably.\x02\x03",
            "#13904FI now give you the\x01",
            "following words of\x01",
            "advice.\x02",
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
            "#5P#13912FSoften your hardened\x01",
            "hearts, and let love and\x01",
            "devotion be your guide...\x02",
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
            "#13904FAlthough a gloomy sigh has\x01",
            "its own sex appeal, has\x01",
            "happiness escaped you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103FLet me be perfectly clear.\x02\x03",
            "#00100FMueller's instructions were\x01",
            "to "bring him to me no\x01",
            "matter what you have to do."\x02\x03",
            "#00109FWouldn't a little pain be\x01",
            "just the perfect thing to\x01",
            "bring you in line?\x02",
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
            "#5P#13911FO-Ok! I'll go back! I\x01",
            "promise!\x02",
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
            "show me the way to\x01",
            "Mueller?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10108FHmm, but... I think it\x01",
            "would be better to have\x01",
            "Mueller come here.\x02\x03",
            "#10106FThis one might cause\x01",
            "trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FWell, that's the safest\x01",
            "option. He might try to run\x01",
            "while we're escorting him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#13910FMan, you guys don't\x01",
            "trust me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FA-Anyway, I'll try\x01",
            "contacting the station.\x02",
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

    # Function_15_526A end

    def Function_16_5D80(): pass

    label("Function_16_5D80")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5DCF")
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
    Jump("Function_16_5D80")

    label("loc_5DCF")

    Return()

    # Function_16_5D80 end

    def Function_17_5DD0(): pass

    label("Function_17_5DD0")

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
            "#00005F#6PJazz Bar Galante... Why\x01",
            "are we here again?\x02",
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
            "#5PI was just about to when\x01",
            "I heard the news of his\x01",
            "death.\x02",
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
            "#5P#5P...The cause of the cult incident, the arrest\x01",
            "of Imperial and Republic faction congressmen\x01",
            "and the election of a new mayor...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PThe opening of the trade\x01",
            "conference, the attack\x01",
            "on Crossbell City...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5P...And now, the\x01",
            "declaration of\x01",
            "independence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PAll of these appear\x01",
            "unrelated, but the events all\x01",
            "have the same mutual cause.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PWhat I'm trying to say\x01",
            "is, all of the events are\x01",
            "part of the same chain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00101FA single chain of\x01",
            "events...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PAnd in order to grasp the "main\x01",
            "point" of that chain, I'll need to\x01",
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
            "#5PThinking this, I\x01",
            "suggested this case\x01",
            "review.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PLloyd and friends, I know that\x01",
            "many of these events were hard\x01",
            "on all of you, but...\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x1388)

    ChrTalk(
        0x101,
        (
            "#6P#00003F............\x02\x03",
            "#00000FNo... We're all right.\x02",
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
        "#6P#00208FLloyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303F...Well, we don't have\x01",
            "time.\x02\x03",
            "#00300FAnyway, let's get\x01",
            "started.\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7302", 0)

    ChrTalk(
        0x11,
        (
            "#5PYes... Let's begin right\x01",
            "away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PFirst, the situation in\x01",
            "which Guy's remains were\x01",
            "found―\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PIt was three years ago. The weather was cloudy,\x01",
            "with light rain. The place was the Orchis Tower\x01",
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
        (
            "#5PAnd as for the cause of\x01",
            "death―\x02",
        )
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
        (
            "#6P#00003FNo... It happened just\x01",
            "as you've said.\x02",
        )
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
            "#5PYes... From there, the crime\x01",
            "scene at the time the body\x01",
            "was discovered was surveyed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PFirst of all, there were\x01",
            "traces of a fierce battle\x01",
            "all around the body, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PNot a thing remained\x01",
            "except for Guy's\x01",
            "belongings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PFurthermore, Guy's\x01",
            "favorite tonfas had been\x01",
            "taken from the scene...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PThe police badge that\x01",
            "was on his chest had\x01",
            "been taken as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PThe badge was found\x01",
            "recently, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PIs it possible to prove the\x01",
            "badge was taken by members\x01",
            "of the Revache mafia?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FYes. We heard that\x01",
            "information directly\x01",
            "from President Marconi.\x02\x03",
            "#00001FFurthermore, the member\x01",
            "that took it confessed\x01",
            "to the police.\x02",
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
            "#5PI'll need to confirm\x01",
            "that with the witness\x01",
            "later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5P...But no one saw the\x01",
            "conclusion of the fight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PAt the time of Guy's death,\x01",
            "construction was suspended\x01",
            "and no staff were present.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PFurthermore, it was just after\x01",
            "dawn. There were echoes of\x01",
            "wind, light rain and thunder...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PThere was no one near the scene,\x01",
            "so no one could have seen the\x01",
            "moment of Guy's murder.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PFurthermore, Guy hadn't\x01",
            "spoken with anyone on\x01",
            "his way to the scene.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5P...That's all I've been able to\x01",
            "learn about the circumstances\x01",
            "surrounding the event.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PLloyd, can you add\x01",
            "anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FNo, nothing in\x01",
            "particular...\x02\x03",
            "#00001FMy understanding is the\x01",
            "same as you've explained\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00108F(Nielsen... He's full of\x01",
            "information, as always.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203F(Yes. And it seems he\x01",
            "knew Guy personally...)\x02\x03",
            "#00201F(That might be why he's\x01",
            "so interested in this\x01",
            "case.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PYes... Let's move on to\x01",
            "the case review.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PTo get to the truth of\x01",
            "this case, we must\x01",
            "consider the criminal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PWe have to think about the\x01",
            "most likely suspects...\x01",
            "Revache or D∴G Cult staff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PLloyd, you think either\x01",
            "could be the criminal?\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 2)
    ClearScenarioFlags(0x0, 3)
    ClearScenarioFlags(0x0, 4)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6D9A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6F37")
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
            "#1KCould Guy have been killed by\x01",
            "the mafia, or by D∴G Cult staff?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "The criminal is mafia staff\x01",        # 0
            "The criminal is cult staff\x01",         # 1
            "It couldn't be either of them\x01",      # 2
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
        (0, "loc_6E9D"),
        (1, "loc_6ED0"),
        (2, "loc_6F03"),
        (SWITCH_DEFAULT, "loc_6F24"),
    )


    label("loc_6E9D")


    ChrTalk(
        0x101,
        (
            "#6P#00006F(...No, that's not\x01",
            "right―)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6F24")

    label("loc_6ED0")


    ChrTalk(
        0x101,
        (
            "#6P#00006F(...No, that's not\x01",
            "right―)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6F24")

    label("loc_6F03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F1C")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6F1C")

    SetScenarioFlags(0x0, 2)
    Jump("loc_6F24")

    label("loc_6F24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_6F32")
    Jump("loc_6F37")

    label("loc_6F32")

    Jump("loc_6D9A")

    label("loc_6F37")


    ChrTalk(
        0x101,
        (
            "#6P#00003FNo. It couldn't have been either of\x01",
            "them.\x02\x03",
            "#00008FRegarding Revache, it couldn't be\x01",
            "Marconi or that subordinate―\x02\x03",
            "#00001FRegarding the cult, Joachim himself said\x01",
            "although he planned the murder, he\x01",
            "didn't get the chance to carry it out.\x02\x03",
            "#00006FFurthermore, it's hard to believe\x01",
            "another staff member unbeknownst to them\x01",
            "would break ranks and do such a thing.\x02\x03",
            "#00013F...On top of that, I heard my brother\x01",
            "was on guard against the power of those\x01",
            "two.\x02\x03",
            "My brother wouldn't be led into a\x01",
            "situation where his life could be\x01",
            "taken...\x02\x03",
            "I think that possibility is very remote.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00306F...I know, right.\x02\x03",
            "#00301FBased on what I heard, on top\x01",
            "of his boldness and ferocity,\x01",
            "he had a good sense of smell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00206F...Yes.\x02\x03",
            "#00201FI don't think he's the type\x01",
            "to fall behind his opponents\x01",
            "- the mafia and the cult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PIt certainly true that\x01",
            "each component negates\x01",
            "those possibilities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PPerhaps before the cult incident it\x01",
            "was, but now, it's quite impossible\x01",
            "for either party to be the culprit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PYes. Next, we'll consider the\x01",
            "possibility it was done by either\x01",
            "of the major powers or their staff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PWe must also consider congressmen of Imperial\x01",
            "and Republic factions that coveted power,\x01",
            "government officials deeply involved with\x01",
            "either country and intelligence division staff―\x02",
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

    label("loc_74AF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7692")
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
            "#1KWas Guy killed by Imperial\x01",
            "or Republican staff?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "It's highly likely\x01",      # 0
            "It's unlikely\x01",           # 1
            "Impossible to say\x01",       # 2
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
        (0, "loc_7580"),
        (1, "loc_75ED"),
        (2, "loc_760E"),
        (SWITCH_DEFAULT, "loc_767F"),
    )


    label("loc_7580")


    ChrTalk(
        0x101,
        (
            "#6P#00008F(It's highly likely...\x01",
            "Is that really right?)\x02\x03",
            "#00001F(Think again, Lloyd\x01",
            "Bannings―)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_767F")

    label("loc_75ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7606")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7606")

    SetScenarioFlags(0x0, 2)
    Jump("loc_767F")

    label("loc_760E")


    ChrTalk(
        0x101,
        (
            "#6P#00008F(It's impossible to\x01",
            "say... Is that really\x01",
            "right?)\x02\x03",
            "#00001F(Think again, Lloyd\x01",
            "Bannings―)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_767F")

    label("loc_767F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_768D")
    Jump("loc_7692")

    label("loc_768D")

    Jump("loc_74AF")

    label("loc_7692")


    ChrTalk(
        0x101,
        (
            "#6P#00003FNo. I think that's unlikely.\x02\x03",
            "#00008FIt's true there are a lot of staff\x01",
            "within the two major powers that\x01",
            "committed injustices in Crossbell.\x02\x03",
            "I even heard that my brother was\x01",
            "closing in on a number of them.\x02\x03",
            "#00001FAdditionally, it's confirmed that\x01",
            "intelligence staff were frequently\x01",
            "visiting Crossbell.\x02\x03",
            "#00006FBut, to put it bluntly― If my\x01",
            "brother seriously wounded any of\x01",
            "them, nothing would come of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106FYou're certainly right about\x01",
            "that...\x02\x03",
            "#00108FIf the two major powers felt like\x01",
            "it, they could control the police\x01",
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
            "#6P#00003FYeah. No matter how troublesome he\x01",
            "was, luring a lone detective\x01",
            "somewhere to get rid of him would be―\x02\x03",
            "#00001FFrom the start, such an action would\x01",
            "not be worth its cost.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#5PHmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303FFor argument's sake,\x01",
            "let's say Lloyd's brother\x01",
            "was in contact with them.\x02\x03",
            "#00300FIt's the same as the\x01",
            "mafia. He'd never fall\x01",
            "into a trap unprepared.\x02",
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
            "#5PYou have great detective\x01",
            "skills, everyone. I have\x01",
            "nothing to add.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PLet's move on to our\x01",
            "final consideration―\x02",
        )
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
            "#5PCould there be anyone\x01",
            "else who fits the\x01",
            "criminal's profile?\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 2)
    ClearScenarioFlags(0x0, 3)
    ClearScenarioFlags(0x0, 4)

    label("loc_7BDB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7E62")
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
            "#1KThen, someone else who fits\x01",
            "the criminal's profile?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Ouroboros staff\x01",             # 0
            "Crossbell Police staff\x01",      # 1
            "Someone Guy knew well\x01",       # 2
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
        (0, "loc_7CBA"),
        (1, "loc_7D54"),
        (2, "loc_7E2E"),
        (SWITCH_DEFAULT, "loc_7E4F"),
    )


    label("loc_7CBA")


    ChrTalk(
        0x101,
        (
            "#6P#00006F(That organization is\x01",
            "certainly full of mysteries,\x01",
            "but... Think a little harder.)\x02\x03",
            "#00013F(There should be a more\x01",
            "natural answer.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_7E4F")

    label("loc_7D54")


    ChrTalk(
        0x101,
        (
            "#6P#00008F(An inside job by someone with a grudge.\x01",
            "I can't eliminate that possibility, but\x01",
            "there should be a better answer.)\x02\x03",
            "#00013F(Based on how things have gone, there\x01",
            "should be a more natural answer.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_7E4F")

    label("loc_7E2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7E47")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7E47")

    SetScenarioFlags(0x0, 2)
    Jump("loc_7E4F")

    label("loc_7E4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_7E5D")
    Jump("loc_7E62")

    label("loc_7E5D")

    Jump("loc_7BDB")

    label("loc_7E62")

    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#6P#00003FSomeone my brother knew\x01",
            "well, even though he was\x01",
            "cautious.\x02\x03",
            "#00001FI think it might be\x01",
            "someone with that kind\x01",
            "of profile.\x02",
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
        "#6P#00205FHuh...\x02",
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
            "#6P#00003FFirst of all, my brother didn't\x01",
            "reveal the fact he was heading to\x01",
            "the scene to anyone.\x02\x03",
            "#00008FBecause of that, it's certain he\x01",
            "went there alone.\x02\x03",
            "#00013FIf you think about it, I think\x01",
            "you can say it's likely the\x01",
            "criminal was a "friend" of Guy's.\x02",
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
            "#6P#00006FDid my brother call his friend to the scene?\x01",
            "Or was he himself called? We don't know.\x02\x03",
            "#00003FThe crime scene was that construction site\x01",
            "where no one was present―\x02\x03",
            "#00008FIn other words, there must have been an\x01",
            "important conversation. He needed to make sure\x01",
            "what he didn't want to be heard, couldn't be.\x02\x03",
            "#00013FSome kind of exchange took place there... When\x01",
            "it broke down, he lost his life. Could that\x01",
            "have been it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PAnd as for that\x01",
            "exchange?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FI have no idea of the\x01",
            "specifics.\x02\x03",
            "#00008FIt's just that, because he\x01",
            "lost his life over it, it\x01",
            "must've been very important...\x02\x03",
            "#00001FFor example... It might have\x01",
            "been related to "some\x01",
            "conspiracy" or something.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x103,
        (
            "#6P#00200FA conspiracy, you\x01",
            "say...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#5PHmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F...You said "grasp the\x01",
            "main points and shine a\x01",
            "light on them".\x02\x03",
            "#00000FWhen I heard them,\x01",
            "although it's faint, I\x01",
            "feel they are connected.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x11,
        "#5POh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FIt's possible my brother was\x01",
            "asked to join some kind of\x01",
            "conspiracy...\x02\x03",
            "#00003FWhether it's the D∴G cult or the\x01",
            "mafia, the Empire or the Republic\x01",
            "or someone else entirely...\x02\x03",
            "#00008FThey were advancing their plans.\x01",
            "It's possible they're still\x01",
            "advancing them, even now.\x02\x03",
            "#00001FBut in the end, that's only a\x01",
            "guess, right?\x02",
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
        (
            "#6P#00201FAnd also, that it could\x01",
            "still be in progress...\x02",
        )
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
            "#6P#00005FNielsen?\x02\x03",
            "#00006F...As expected, it's\x01",
            "impossible, right?\x02",
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
        "#5P─I'll be frank, Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PWhile we were conducting\x01",
            "this review, did a certain\x01",
            "character come to mind?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PA character who, three years ago,\x01",
            "called Guy out the construction\x01",
            "site and killed him?\x02",
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
            "#00003FAlthough it was a "friend", my brother\x01",
            "knew a staggering number of people.\x02\x03",
            "#00008F...It's the truth that, at the scene,\x01",
            "he was shot from behind and his tonfas\x01",
            "were taken...\x02\x03",
            "#00013FPersonally, I feel like those elements\x01",
            "are the key to explaining the incident,\x01",
            "but...\x02\x03",
            "#00006FIf it were possible to identify someone\x01",
            "with just that, Section One would have\x01",
            "already done it three years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PHmm, so it's impossible\x01",
            "is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PAt present, all of the\x01",
            "pieces that point to the\x01",
            "criminal aren't in place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5P―But that's not all we\x01",
            "can say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PThe one who can find the\x01",
            "missing piece is you,\x01",
            "Lloyd─ and you alone.\x02",
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
        "#6P#00105FNielsen...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#6P#00004FYes... And I plan to do\x01",
            "just that.\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7151", 0)

    ChrTalk(
        0x11,
        "#5PHaha, glad to hear it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5P...I feel almost as if I've kept\x01",
            "my promise to exchange information\x01",
            "with Guy three years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PI'd like to thank all of\x01",
            "you for joining me for\x01",
            "this review.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FWe should be thanking\x01",
            "you too. Thank you,\x01",
            "Nielsen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PI'll excuse myself then...\x01",
            "I'm looking forward to\x01",
            "seeing how this turns out.\x02",
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

    def lambda_8D95():
        OP_95(0xFE, -7730, 0, 1910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8D95)
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x103, 0x0)
    WaitChrThread(0x11, 1)

    def lambda_8DC5():
        OP_95(0xFE, 690, 0, 1520, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8DC5)
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
            "#6P#00202FNielsen... It's almost\x01",
            "as if he's guiding us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00004FYeah... Probably, his promise\x01",
            "to my brother has been weighing\x01",
            "on his mind this whole time.\x02\x03",
            "#00002FI'm glad he got to speak with\x01",
            "us.\x02",
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
            "#6P#00301F#12P...Alright, this stuff\x01",
            "has motivated me. It's\x01",
            "time to go!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00003FYeah... Anyway, let's hurry\x01",
            "to president's room in the\x01",
            "old Revache building.\x02\x03",
            "#00013FThere's some info Captain\x01",
            "Lechter wants to show us!\x02",
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
            "Quest [Guy Bannings\x01",
            "Murder Case Review]\x07\x00\x01",
            "completed!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_908F")
    OP_2C(0x95, 0x2)
    Jump("loc_90A3")

    label("loc_908F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_90A3")
    OP_2C(0x95, 0x1)

    label("loc_90A3")

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

    # Function_17_5DD0 end

    SaveToFile()

Try(main)
