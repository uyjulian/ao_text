from ScenarioHelper import *

def main():
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
        "Eric",               # 1
        "Sandra",               # 2
        "Serdan branch chief",         # 3
        "Copan",                 # 4
        "Peter",               # 5
        "Dudley investigator",         # 6
        "Iris",               # 7
        "Bidding bucket",         # 8
        "Olivier",               # 9
        "Nielsen",             # 10
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
        "Function_4_691",          # 04, 4
        "Function_5_695",          # 05, 5
        "Function_6_1EFE",         # 06, 6
        "Function_7_2F31",         # 07, 7
        "Function_8_2FDC",         # 08, 8
        "Function_9_3083",         # 09, 9
        "Function_10_312A",        # 0A, 10
        "Function_11_31AD",        # 0B, 11
        "Function_12_39B2",        # 0C, 12
        "Function_13_3A21",        # 0D, 13
        "Function_14_3A57",        # 0E, 14
        "Function_15_4C8B",        # 0F, 15
        "Function_16_5798",        # 10, 16
        "Function_17_57E8",        # 11, 17
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
            "There is \"a classic menu for businessmen\".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('料理手册', 0x0)"), scpexpr(EXPR_END)), "loc_68D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x17)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68D")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "\"Rich cappuccino\"\x07\x00",
            "I learned the recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_68D")

    TalkEnd(0xFF)
    Return()

    # Function_3_5D6 end

    def Function_4_691(): pass

    label("Function_4_691")

    Call(0, 5)
    Return()

    # Function_4_691 end

    def Function_5_695(): pass

    label("Function_5_695")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x139, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D9")

    ChrTalk(
        0x8,
        "Welcome……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x105, 500)
    Sleep(300)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "Gee\x01",
            "Is not Wasan?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I do not want to be at such a time\x01",
            "It is unusual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FA little\x01",
            "In the middle of patrol.\x02\x03",
            "#10300FEven when there is time this time\x01",
            "I will have you drink it again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Well, I will be waiting.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x139, 3)
    TalkEnd(0x8)
    Return()

    label("loc_7D9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7E3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EFA")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",          # 0
            "to shop\x01",      # 1
            "quit\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_841")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_841")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_861")
    OP_AF(0x42)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1EF5")

    label("loc_861")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_875")
    Jump("loc_1EF5")

    label("loc_875")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EF5")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_A4C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9A6")

    ChrTalk(
        0x8,
        (
            "In the near term, \"black moon\" is a back society\x01",
            "It will be the real power.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Kuroki is like Rubache\x01",
            "Although it does not like conspicuous behavior,\x01",
            "Because its presence is overwhelming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Not a few in this street\x01",
            "The influence will come out.\x01",
            "…… It seems better to be careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A47")

    label("loc_9A6")


    ChrTalk(
        0x8,
        (
            "In the near term, \"black moon\" is a back society\x01",
            "It will be the real power.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Not a few in this street\x01",
            "The influence will come out.\x01",
            "…… It seems better to be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A47")

    Jump("loc_1EF5")

    label("loc_A4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_AE1")

    ChrTalk(
        0x8,
        (
            "Until the back streets are those\x01",
            "You do not seem to be entering.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But, what kind of risk is there?\x01",
            "I do not understand.\x01",
            "Evacuate to the inside of the store freely.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EF5")

    label("loc_AE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_C9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BE5")

    ChrTalk(
        0x8,
        (
            "This declaration of independence is also\x01",
            "It should greatly influence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "From now on by the Defense Forces\x01",
            "Empire, Republic Mafia also\x01",
            "It will be enforced.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It was quite rapid development … …\x01",
            "This is the crossbell\x01",
            "Perhaps you need rough treatment.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C95")

    label("loc_BE5")


    ChrTalk(
        0x8,
        (
            "From now on by the Defense Forces\x01",
            "Empire, Republic Mafia also\x01",
            "It will be enforced.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The declaration of independence was a rapid development … …\x01",
            "This is the crossbell\x01",
            "Perhaps you need rough treatment.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C95")

    Jump("loc_1EF5")

    label("loc_C9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_E25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D89")

    ChrTalk(
        0x8,
        (
            "Crossbell City raid ……\x01",
            "The \"red constellation\" guys\x01",
            "I did a terrible thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Even at this store where information on the back is easy to enter,\x01",
            "I could not feel it even …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Probably, thoroughly from a long time ago\x01",
            "I guess it was planned.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E20")

    label("loc_D89")


    ChrTalk(
        0x8,
        (
            "Even at this store where information on the back is easy to enter,\x01",
            "I could not feel it even …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Crossbell City raid probably,\x01",
            "Thoroughly from long ago\x01",
            "I guess it was planned.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E20")

    Jump("loc_1EF5")

    label("loc_E25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_FC6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F28")

    ChrTalk(
        0x8,
        (
            "\"Red constellation\" people\x01",
            "I noticed that I disappeared,\x01",
            "It is after seeing the hurried appearance of the police.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "They escaped the monitoring of the police through the underground,\x01",
            "It probably went towards Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "…… What does this occupation case mean\x01",
            "I can not resist it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FC1")

    label("loc_F28")


    ChrTalk(
        0x8,
        (
            "\"Red constellation\" people\x01",
            "I noticed that I disappeared,\x01",
            "It is after seeing the hurried appearance of the police.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "…… What does this occupation case mean\x01",
            "I can not resist it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FC1")

    Jump("loc_1EF5")

    label("loc_FC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1131")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10A4")

    ChrTalk(
        0x8,
        (
            "Yesterday's derailment accident ……\x01",
            "A gigantic thing that appeared in the vicinity\x01",
            "There seems to be rumors that it woke up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "However, as the referendum approaches,\x01",
            "I do not think that it is an accident by just a monster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "…… I feel stinky queen.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_112C")

    label("loc_10A4")


    ChrTalk(
        0x8,
        (
            "The reality that the referendum is approaching,\x01",
            "It seems rumored that the derailment accident of yesterday is also rumored\x01",
            "I do not think that it is an accident by just a monster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "…… I feel stinky queen.\x02",
    )

    CloseMessageWindow()

    label("loc_112C")

    Jump("loc_1EF5")

    label("loc_1131")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_118B")

    ChrTalk(
        0x8,
        "An ambulance siren that sounds far away ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "…… I feel cranky.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EF5")

    label("loc_118B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1392")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12F0")

    ChrTalk(
        0x8,
        (
            "Yesterday, in the city of Altair\x01",
            "Republican terrorist arrest play\x01",
            "It seems there was … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "On the other side black people 's guys\x01",
            "It is a rumor that it was working on tracking.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_12A7")

    ChrTalk(
        0x101,
        (
            "#00005F(There was a black moon in that place … …)\x02\x03",
            "#00003F(I did not notice it\x01",
            "It is truly flashy people. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12E8")

    label("loc_12A7")


    ChrTalk(
        0x8,
        (
            "It's what it's like ……\x01",
            "You still have no flash.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12E8")

    SetScenarioFlags(0x0, 0)
    Jump("loc_138D")

    label("loc_12F0")


    ChrTalk(
        0x8,
        (
            "Yesterday at Altair City\x01",
            "In the arrest play of republic terrorists,\x01",
            "It is a rumor that the black moon was moving.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It's what it's like ……\x01",
            "You still have no flash.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_138D")

    Jump("loc_1EF5")

    label("loc_1392")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1540")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14A7")

    ChrTalk(
        0x8,
        (
            "At the time of the Trade Council, \"Red constellation\"\x01",
            "Terrorists at the request of the Imperial Government\x01",
            "Although there are rumors that he repulsed … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The recent Crimson Shokai\x01",
            "There is no big trouble,\x01",
            "It is quiet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "…… Good or bad,\x01",
            "They are professional hunters\x01",
            "You can feel it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_153B")

    label("loc_14A7")


    ChrTalk(
        0x8,
        (
            "It moved greatly at the trade meeting\x01",
            "Crimson Shokai also recently\x01",
            "It is quiet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "…… Good or bad,\x01",
            "They are professional hunters\x01",
            "You can feel it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_153B")

    Jump("loc_1EF5")

    label("loc_1540")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_16E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1638")

    ChrTalk(
        0x8,
        (
            "Hunting Corps \"Red constellation\".\x01",
            "And \"Haruna\" in the port area …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As a result of the plenary session,\x01",
            "Police people also to these forces\x01",
            "You seem to be increasing your vigilance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Police officers seen in the back street also\x01",
            "To a considerable tension state\x01",
            "I feel that it is getting.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16DE")

    label("loc_1638")


    ChrTalk(
        0x8,
        (
            "As a result of the plenary session,\x01",
            "We are also wary of \"red constellation\" \"black moon\"\x01",
            "It seems to be strengthened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Police officers seen in the back street also\x01",
            "To a considerable tension state\x01",
            "I feel that it is getting.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16DE")

    Jump("loc_1EF5")

    label("loc_16E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_18BD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1831")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17B1")

    ChrTalk(
        0x8,
        (
            "Trade meeting ……\x01",
            "Have you finally started?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To protect the back street\x01",
            "The tension of the police people also\x01",
            "I feel it has increased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Again to the Crimson Shokai\x01",
            "The alarming consciousness seems strong.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_182C")

    label("loc_17B1")


    ChrTalk(
        0x8,
        (
            "To protect the back street\x01",
            "The tension of the police people also\x01",
            "I feel it has increased.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Again to the Crimson Shokai\x01",
            "The alarming consciousness seems strong.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_182C")

    Jump("loc_18B8")

    label("loc_1831")


    ChrTalk(
        0x8,
        (
            "Olivier,\x01",
            "It was quite interesting one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If possible, as a stage performer\x01",
            "I wanted to contract formally … …\x01",
            "It will not be a shame.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18B8")

    Jump("loc_1EF5")

    label("loc_18BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1AC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A11")

    ChrTalk(
        0x8,
        (
            "I entered a new building on the back alleys\x01",
            "\"Crimson Shokai\" … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I had no trouble in any way\x01",
            "Compared to Rubache,\x01",
            "It is the impression that those who refrained it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "However, in reality\x01",
            "West Zemria one of the strongest hunting corps\x01",
            "Rumor that it is \"red constellation\" …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Although it is quite ostensible,\x01",
            "Rather than that Rubache\x01",
            "I can not help feeling the presence.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1AC3")

    label("loc_1A11")


    ChrTalk(
        0x8,
        (
            "The fact of the Crimson Shokai is\x01",
            "West Zemria one of the strongest hunting corps\x01",
            "Rumor that it is \"red constellation\" …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Although it is quite ostensible,\x01",
            "Rather than that Rubache\x01",
            "I can not help feeling the presence.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AC3")

    Jump("loc_1EF5")

    label("loc_1AC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 4)), scpexpr(EXPR_END)), "loc_1BA7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B4B")

    ChrTalk(
        0x8,
        (
            "…… Rain gradually\x01",
            "It is getting worse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Mr. Sandra is getting up soon.\x01",
            "It seems better to return.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1BA2")

    label("loc_1B4B")


    ChrTalk(
        0x8,
        "……is there something wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Now, at our shop\x01",
            "There is only me and Mr. Sandra … …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BA2")

    Jump("loc_1EF5")

    label("loc_1BA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1D30")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CA8")

    ChrTalk(
        0x8,
        (
            "The whole area of Rubatse ruins,\x01",
            "Kuro Mun watches as it gets\x01",
            "First of all it will not be wrong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If so, the black moon\x01",
            "To the society behind the crossbell\x01",
            "It will build a solid foothold …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Given the current state of crossbell,\x01",
            "Maybe it is somewhat useless\x01",
            "I do not think so.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1D2B")

    label("loc_1CA8")


    ChrTalk(
        0x8,
        (
            "It is becoming established,\x01",
            "The rise to the back society by black moon … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Given the current state of crossbell,\x01",
            "Maybe it is somewhat useless\x01",
            "I do not think so.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D2B")

    Jump("loc_1EF5")

    label("loc_1D30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1EF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E45")

    ChrTalk(
        0x8,
        (
            "Since Rubache was gone,\x01",
            "Yakuza who had been hiding until now\x01",
            "It is appearing gradually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In that sense,\x01",
            "The security of the back street is rather\x01",
            "It is getting worse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "How much power is Rubache\x01",
            "Were you having … … Where have now disappeared\x01",
            "It is understood.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1EF5")

    label("loc_1E45")


    ChrTalk(
        0x8,
        (
            "Since Rubache was gone,\x01",
            "Yakuza who had been hiding until now\x01",
            "It is appearing gradually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "How much power is Rubache\x01",
            "Were you having … … Where have now disappeared\x01",
            "It is understood.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EF5")

    Jump("loc_7E3")

    label("loc_1EFA")

    TalkEnd(0x8)
    Return()

    # Function_5_695 end

    def Function_6_1EFE(): pass

    label("Function_6_1EFE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_202F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FE0")
    SetChrSubChip(0xFE, 0x2)

    ChrTalk(
        0xFE,
        (
            "Wow … ___ ___ 0\x01",
            "Eric ~ Let's drink ~ ~.\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0xFE,
        (
            "That funny moya was also sunny,\x01",
            "It is a celebrating atmosphere ~ ~?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xFE, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "Because Mr. Sandra, Jama\x01",
            "Please come back to me.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x0)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x0, 1)
    Jump("loc_202A")

    label("loc_1FE0")


    ChrTalk(
        0xFE,
        "Wow, that's Eric's … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "But, such a place is Sue · te · ki\x02",
    )

    CloseMessageWindow()

    label("loc_202A")

    Jump("loc_2F2D")

    label("loc_202F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_20A9")

    ChrTalk(
        0xFE,
        (
            "Mumboppy …\x01",
            "Because the shop is closed due to martial law,\x01",
            "I was drinking and sleeping here ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "What did you do?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F2D")

    label("loc_20A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_21EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2180")

    ChrTalk(
        0xFE,
        (
            "Even at our store, you can go\x01",
            "How to say \"Independence party\"\x01",
            "There seems to be a customer to reserve.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What is difficult for me\x01",
            "I do not understand well ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well everyone seems to be happy\x01",
            "I think it's okay?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_21E6")

    label("loc_2180")


    ChrTalk(
        0xFE,
        (
            "What is difficult for me\x01",
            "I do not understand well ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well everyone seems to be happy\x01",
            "I think it's okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21E6")

    Jump("loc_2F2D")

    label("loc_21EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_23C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2316")

    ChrTalk(
        0xFE,
        (
            "There was a raid incident, and our shops are also\x01",
            "I was refraining from sales,\x01",
            "I will resume from tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, the restoration of the city is also\x01",
            "It seems that the aim has arrived,\x01",
            "I can not take a rest forever ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My club is just a club,\x01",
            "Still there are some customers looking forward to it.\x01",
            "…… Are you going to work hard?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_23C3")

    label("loc_2316")


    ChrTalk(
        0xFE,
        (
            "It seems that the restoration of the city is also going well,\x01",
            "I can not take a rest forever ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "My club is just a club,\x01",
            "Still there are some customers looking forward to it.\x01",
            "…… Are you going to work hard?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23C3")

    Jump("loc_2F2D")

    label("loc_23C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2523")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24AA")

    ChrTalk(
        0xFE,
        (
            "Eric was saying,\x01",
            "What is the Crimson Company?\x01",
            "Were you a hunting company company?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Wha … ….\x01",
            "That famous \"Neue-Blanc\"\x01",
            "The Crimson Shokai is … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was not think that's yakuza's\x01",
            "I am surprised that much.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_251E")

    label("loc_24AA")


    ChrTalk(
        0xFE,
        (
            "That \"Neue-Blanc\"'s\x01",
            "Crimson Shokai is a hunting soldier … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was not think that's yakuza's\x01",
            "I am surprised that much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_251E")

    Jump("loc_2F2D")

    label("loc_2523")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_268E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2615")
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Hey ~ Eric what?\x01",
            "Do not talk about small difficult subjects\x01",
            "Go out for a drink … ……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xFE, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "Sandra also,\x01",
            "Do not just go to bed at a store in my house\x01",
            "Why do not you go home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Already, Eric's IKES - ….\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x0, 1)
    Jump("loc_2689")

    label("loc_2615")


    ChrTalk(
        0xFE,
        (
            "Well, Eric\x01",
            "I do not mind going out ~ Iwane ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "But, that is also Su - teki.\x01",
            "…… な ん ち ゃ っ て 吹 け\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2689")

    Jump("loc_2F2D")

    label("loc_268E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_27B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_274B")

    ChrTalk(
        0xFE,
        (
            "Mumboppy …\x01",
            "How about this sexual harassment … …!\x01",
            "Remembered, this this … …\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        "… … Huh! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "…… What a dream!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    SetScenarioFlags(0x0, 1)
    Jump("loc_27AD")

    label("loc_274B")


    ChrTalk(
        0xFE,
        (
            "Oh ……\x01",
            "I was watching a dream that felt good\x01",
            "I completely woke up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "I … Wake up?\x02",
    )

    CloseMessageWindow()

    label("loc_27AD")

    Jump("loc_2F2D")

    label("loc_27B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_285C")

    ChrTalk(
        0xFE,
        (
            "Mumboppy …\x01",
            "That owl, as always\x01",
            "I feel sticky with a sticky … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm not a store like that,\x01",
            "You always said that.\x01",
            "Konko … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F2D")

    label("loc_285C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2996")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2929")

    ChrTalk(
        0xFE,
        (
            "Something next time, the people are voting\x01",
            "It seems there are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You should definitely go\x01",
            "Eric says,\x01",
            "It is honestly subtle, is not it ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because during the time of the vote\x01",
            "Sleeping, I, I.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2991")

    label("loc_2929")


    ChrTalk(
        0xFE,
        (
            "Residential vote, whether to go\x01",
            "It is honestly subtle, is not it ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because during the time of the vote\x01",
            "Sleeping, I, I.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2991")

    Jump("loc_2F2D")

    label("loc_2996")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2AC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A52")
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Eric~……\x01",
            "Ramkola Okabori … ….\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xFE, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "Mr. Sandra, it's already morning\x01",
            "Please return soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Already, Eric's IKES - ….\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x0, 1)
    Jump("loc_2AC0")

    label("loc_2A52")


    ChrTalk(
        0xFE,
        (
            "Eric's IKES - ….\x01",
            "Sometimes go out with me ~ ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After a long absence,\x01",
            "Because the shop is closed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AC0")

    Jump("loc_2F2D")

    label("loc_2AC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2BCD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B58")

    ChrTalk(
        0xFE,
        (
            "Yesterday, a bad customer came in the store\x01",
            "I was drunk a lot, did not I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well … my head gets caught.\x01",
            "I will get over it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BC8")

    label("loc_2B58")


    ChrTalk(
        0xFE,
        (
            "That person's performance,\x01",
            "It was very good ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was tired from work tired,\x01",
            "I was completely healed ~.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BC8")

    Jump("loc_2F2D")

    label("loc_2BCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2CA7")

    ChrTalk(
        0xFE,
        (
            "\"Neue-Blanc\" in the entertainment district,\x01",
            "Since Crimson Shokai came over here\x01",
            "It seems that the economy has further improved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, after all it becomes a high class club\x01",
            "I guess payment is also good for the difference.\x01",
            "I wonder if I can move, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F2D")

    label("loc_2CA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 4)), scpexpr(EXPR_END)), "loc_2CE8")
    OP_64(0x9)

    ChrTalk(
        0xFE,
        "Kokkuri …… Kokuri …\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)
    Jump("loc_2F2D")

    label("loc_2CE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2E1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DA0")

    ChrTalk(
        0xFE,
        (
            "Faa~……\x01",
            "I was completely sleeping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Always after the work of the hostess\x01",
            "You will drop in at this shop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because it's quiet and comfortable\x01",
            "I can sleep well.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2E15")

    label("loc_2DA0")


    ChrTalk(
        0xFE,
        (
            "Because this shop is always quiet\x01",
            "You can sleep well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Eric also silent\x01",
            "I will go out with you,\x01",
            "It's amazingly cozy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E15")

    Jump("loc_2F2D")

    label("loc_2E1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2F2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EB3")

    ChrTalk(
        0xFE,
        (
            "Everyday, at the club every day\x01",
            "While doing business smile\x01",
            "I am taking care of it all night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Ha\x01",
            "Why me\x01",
            "You do work like this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2F2D")

    label("loc_2EB3")


    ChrTalk(
        0xFE,
        (
            "Ha\x01",
            "Recently, for this work\x01",
            "You feel empty, do not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, because payment is good\x01",
            "I feel like quitting quite\x01",
            "I do not think so.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F2D")

    TalkEnd(0xFE)
    Return()

    # Function_6_1EFE end

    def Function_7_2F31(): pass

    label("Function_7_2F31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F63")
    Call(0, 14)
    Return()

    label("loc_2F63")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "I deserve first to start again\x01",
            "I am looking for a new office.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Members of Lloyd, if there is something again\x01",
            "Let's exchange information.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_2F31 end

    def Function_8_2FDC(): pass

    label("Function_8_2FDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_300E")
    Call(0, 14)
    Return()

    label("loc_300E")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Well, I will go\x01",
            "I guess it's going to go fishing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What is it like raining in rain\x01",
            "I do not care!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_2FDC end

    def Function_9_3083(): pass

    label("Function_9_3083")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_30B5")
    Call(0, 14)
    Return()

    label("loc_30B5")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Even so, that man …\x01",
            "I really can not forgive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I do not know how professional it is,\x01",
            "I can not put it on the winds of the fisherman.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_3083 end

    def Function_10_312A(): pass

    label("Function_10_312A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18F, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_313F")
    Call(0, 11)
    Jump("loc_31A9")

    label("loc_313F")


    ChrTalk(
        0xD,
        (
            "#00600FNow……\x01",
            "If you drink this you return to work.\x02\x03",
            "#00603FThe day of the referendum is near.\x01",
            "I am still out of my mind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31A9")

    TalkEnd(0xFE)
    Return()

    # Function_10_312A end

    def Function_11_31AD(): pass

    label("Function_11_31AD")

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
        "#00005FDudley…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#00603FYou guys.\x01",
            "…… I do not see you meeting in such a place.\x02\x03",
            "#00600FApparently, from today\x01",
            "It seems he resumed his support request?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, fortunately\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FIncidentally\x01",
            "On the way to the \"red constellation\"\x01",
            "Have you got new information?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#00600FHun, that is\x01",
            "It is totally irritable.\x02\x03",
            "Even for the Imperial government,\x01",
            "I am planning to give new comments\x01",
            "It seems not to be in any way.\x02\x03",
            "#00603FIf something happens next\x01",
            "Residents' vote after 3 days ……\x02\x03",
            "#00600FNow just prepare for that day\x01",
            "It's about the utmost.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#5P#10103FThat's right..\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FHeck, but what?\x01",
            "Strangely a melancholy is drifting.\x02\x03",
            "You drowning your worries?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#00603FHun, I like alcohol\x01",
            "There is no reason to drink from daytime.\x02\x03",
            "#00600FThis is just a soft drink\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FHuff, without alcohol\x01",
            "The atmosphere so far\x01",
            "It is brilliant to get out.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xD)

    ChrTalk(
        0xD,
        (
            "#00603F…… Bannings.\x01",
            "Do you drink alcohol?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FYeah well.\x01",
            "I do not drink so much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#00602FHuh, if is\x01",
            "It is very different from guy guy.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005FMr. Dudley, maybe\x01",
            "Have you drunk here with your big brother?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#00603FYeah, he showed me the place\x02\x03",
            "#00600FBy the way, I started this shop in the beginning\x01",
            "What I learned is the introduction of Guy.\x02\x03",
            "#00608FTo pioneer these stores\x01",
            "It was a really good customer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHaha, I guess.\x01",
            "Anyway, that personality.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FBy the way, with you\x01",
            "Lloyd's big brother is who\x01",
            "Was it strong against liquor?\x02\x03",
            "Because it's yours,\x01",
            "You do not even face confrontation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#00603FNo comment\x02\x03",
            "#00602FThe only thing I can say is\x01",
            "Bannings in Orlando …\x01",
            "I and Guy are also stronger than you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#00301FWell, how much I can drink\x01",
            "With nothing knowing ….\x02\x03",
            "#00304FIf it says so far\x01",
            "Will you actually show me this time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#00604FHa, if we have a chance\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FAhah\x02\x03",
            "(Mr. Dudley,\x01",
            "Actually, even in such a place\x01",
            "I do not like to lose. )\x02",
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

    # Function_11_31AD end

    def Function_12_39B2(): pass

    label("Function_12_39B2")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "Anything, I hate it\x01",
            "I wish I was … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Customers did not get off today,\x01",
            "I did it quietly.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_39B2 end

    def Function_13_3A21(): pass

    label("Function_13_3A21")

    TalkBegin(0xFE)

    ChrTalk(
        0xFE,
        (
            "What should I do,\x01",
            "I can not go back home either …\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_3A21 end

    def Function_14_3A57(): pass

    label("Function_14_3A57")

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
        "#6PLloyd, you came.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "Sorry, Lloyd Members.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "Well … … did you come through this?\x01",
            "Then let's go with the strategy meeting immediately.\x02",
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
            "#5PFirst of all, to Lloyd members\x01",
            "I have to explain our situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PActually this past few months ……\x01",
            "The fishing public division was punitive in activities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005FAre you pardoned … ….?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6PYeah, anyway, our fellow\x01",
            "Former member of Joachim will\x01",
            "I have woken up … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PSo, each one again\x01",
            "I decided to rediscover myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00108FBut, it is your responsibility ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5PIt certainly is not related to the case … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PAs a boyfriend who loves fishing,\x01",
            "I spent a lot of time together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P…… However,\x01",
            "To what he thinks deep inside his heart\x01",
            "I did not care as a thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5PBoth social and personal responsibilities are sufficient.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00003FSerdan branch chief …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#5P…… Well, it's time to put it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PMeanwhile, suddenly about a week ago\x01",
            "I have not heard from the real estate company.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PDo you know whether you know the story of punishment,\x01",
            "It seems they do not use buildings\x01",
            "I was told that I canceled my contract.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PIt is also new, \"The Emperor 's Club\"\x01",
            "I have a report with a contract.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6PImmediately after that, with the representative of the crown club\x01",
            "I tried to get a contact\x01",
            "It is hard to go well …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PSo when I ask my office today\x01",
            "I happened to have a representative over there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5PFinally I heard the truth of the contract … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PThen, with Lloyd members\x01",
            "I do not mean I got along.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00005FIndeed, was that so ……\x02\x03",
            "#00003FIn general, I was able to grasp the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PEven so ……\x01",
            "Lake Road 's \"Fisherman' s Club\"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PIf only I want to expand the base of activities\x01",
            "I did not know it separately ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PNo way, forcing the office\x01",
            "I do not mean to imitate it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6PYeah, why are you being an enemy?\x01",
            "I do not understand it at all. ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P……Anyways,\x01",
            "This is obvious harassment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5PJust because,\x01",
            "Whatever I can do\x01",
            "I do not have a … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5POh, for the time being\x01",
            "It seems to only look at the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P…… However, this way\x01",
            "Even as we lose branches\x01",
            "I will not go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PAlthough it can not say enough yet …\x01",
            "I will try to solve punishment now.\x02",
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
            "#6PHehe, then, the fishing public division ·\x01",
            "Crossbell branch, activity resumption.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#11PHuh, I was waiting!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PHowever … …. Everybody went back to beginners\x01",
            "From the \"fleeting fisherman\"\x01",
            "It is a condition to get out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5Pthen,\x01",
            "Regarding \"stage certification exam\" as well\x01",
            "We will stop it for the time being.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xB,
        "#11PHuh……?\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "#11PA little\x01",
            "Please wait.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11PThat means … …\x01",
            "I am already \"Special Class Wrestler\"\x01",
            "Is it that it is not?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x1)

    ChrTalk(
        0xA,
        (
            "#5POh, I'm sorry, that's it.\x01",
            "This is also a keeper.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#11PHeck, my efforts … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6PFairly, Copan.\x01",
            "You better do your best again.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0x87, 0x1F4)

    ChrTalk(
        0xB,
        (
            "#11PUU……\x01",
            "Originally \"Higorogakusha\" stopped\x01",
            "I do not want Peter to tell me.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 0)), scpexpr(EXPR_END)), "loc_46CD")

    ChrTalk(
        0x101,
        (
            "#12P#00012FAhah\x02\x03",
            "#00006F(Cross Bell's \"Fishing Holy\" … ….\x01",
            "It was pretty difficult. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47EF")

    label("loc_46CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 1)), scpexpr(EXPR_END)), "loc_4730")

    ChrTalk(
        0x101,
        (
            "#12P#00012FAhah\x02\x03",
            "#00006F(\"Special Prize Wrestler\" ……\x01",
            "Well, I did a good job. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47EF")

    label("loc_4730")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_47A2")

    ChrTalk(
        0x101,
        (
            "#12P#00009FAhah\x02\x03",
            "#00003F(First of all, \"a fleeting fisherman\"\x01",
            "It is a story I have nothing to do with me. )\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47EF")

    label("loc_47A2")


    ChrTalk(
        0x101,
        (
            "#12P#00009FAhah\x02\x03",
            "#00006F(By this\x01",
            "Is my title also reset? )\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47EF")

    SetChrSubChip(0xA, 0x0)

    ChrTalk(
        0xA,
        (
            "#5POK, well prepared\x01",
            "I will provide a new set of fishing tackle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PPeter, Copan, and Lloyd Members.\x01",
            "Please accept this.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '初级竿'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('初级竿', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '钓鱼手册'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('钓鱼手册', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '蚯蚓'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "× 10\x01",
            scpstr(SCPSTR_CODE_ITEM, '熬炼丸子'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "× 10 was received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('蚯蚓', 10)
    AddItemNumber('熬炼丸子', 10)
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 0)), scpexpr(EXPR_END)), "loc_4A69")

    ChrTalk(
        0xA,
        (
            "#5POnce up to \"Fishing Holy\"\x01",
            "This is also a service for Lloyd members.\x02",
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
            "further,",
            scpstr(SCPSTR_CODE_ITEM, '蚯蚓'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "× 20\x01",
            scpstr(SCPSTR_CODE_ITEM, '熬炼丸子'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "× 20 was received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('蚯蚓', 20)
    AddItemNumber('熬炼丸子', 20)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#12P#00002FOh, thank you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4B80")

    label("loc_4A69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 1)), scpexpr(EXPR_END)), "loc_4B80")

    ChrTalk(
        0xA,
        (
            "#5PI went even once to \"special class wrestler\"\x01",
            "To Copan and Lloyd Members\x01",
            "This is also a service.\x02",
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
            "further,",
            scpstr(SCPSTR_CODE_ITEM, '蚯蚓'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "× 10\x01",
            scpstr(SCPSTR_CODE_ITEM, '熬炼丸子'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "× 10 was received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('蚯蚓', 10)
    AddItemNumber('熬炼丸子', 10)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#12P#00002FOh, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#5PIt will be appreciated.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4B80")

    label("loc_4B80")


    ChrTalk(
        0xA,
        (
            "#5POK, after that\x01",
            "I left it to each one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PI deserve first to start again\x01",
            "I'm planning to find a new office … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5PIncluding trends of the Emperor 's Club,\x01",
            "Let's exchange information again in the near future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYes, I understand.\x02",
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

    # Function_14_3A57 end

    def Function_15_4C8B(): pass

    label("Function_15_4C8B")

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
        "#00005F(O, Olivier - san …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300F(Wow ….\x01",
            "Is not it a good one? )\x02",
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
            "#5P#13904FHydrofluoric acid\x01",
            "Thank you for your attention.\x02",
        )
    )

    CloseMessageWindow()
    Sound(971, 0, 50, 0)

    ChrTalk(
        0x9,
        "Bravo ~!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Older brother, you are very good!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "How is it, for a while here\x01",
            "Trying out the performance … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Some playing fees etc,\x01",
            "I will let you out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#13909FOh, what do you say\x01",
            "It would be a great app!\x02\x03",
            "#13900FCertainly, certainly\x01",
            "I will underwrite it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00007FWait a moment! It is!\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7117", 0)
    OP_68(-7500, 1630, 2280, 3000)
    MoveCamera(325, 17, 0, 3000)
    OP_6E(400, 3000)
    SetCameraDistance(22280, 3000)

    def lambda_50BA():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_50BA)
    Sleep(50)

    def lambda_50D7():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_50D7)
    Sleep(50)

    def lambda_50F4():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_50F4)
    Sleep(50)

    def lambda_5111():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5111)
    Sleep(50)

    def lambda_512E():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_512E)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)
    OP_63(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x10,
        (
            "#5P#13905FOh, why.\x01",
            "Have you already been found …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FWhat, leisurely work\x01",
            "Are you trying to get there!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00306FHey, hey brother, hey ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#13904FFur, please do it.\x01",
            "I'll be embarrassed if you praise me so much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00301FEveryone compliments me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10101FThis time, I will follow you next time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#13910FWhew, you too\x01",
            "I'm sorry for giving up.\x02\x03",
            "#13900FLife is more fun,\x01",
            "I must live cheerfully.\x02\x03",
            "#13904FTo such you,\x01",
            "I will give you once again.\x02",
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
            "#5P#13912FUnravel the rough heart,\x01",
            "Investigation of love and sincerity ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00103FFuu …\x02",
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x10,
        (
            "#5P#13905FGee\x01",
            "What's wrong Mademoiselle.\x02\x03",
            "#13904FThe sorrow including sorrow is\x01",
            "It's nice to have a cheerfulness,\x01",
            "Happiness will escape?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103F……just in case\x01",
            "I will tell you.\x02\x03",
            "#00100FWe, Mr. Muller\x01",
            "\"Bring me whatever you do\"\x01",
            "I have been asked.\x02\x03",
            "#00109FSomewhat, in painful eyes\x01",
            "It seems to be good to be together ….?\x02",
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
            "#5P#13911FWow, I understand!\x01",
            "I will definitely return home!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012F(Ellie, even though you smile\x01",
            "My eyes are not smiling ……)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#5P#13910FWhew ……\x01",
            "Is this a tidal event?\x02\x03",
            "#13900FWell then, to Muller\x01",
            "Will you show me around?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10108FWell, though …\x01",
            "From Muller's side to here\x01",
            "It looks good to have them come.\x02\x03",
            "#10106FI'm sorry to trouble you a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10302FWell, that would be safe.\x01",
            "You can escape while you are taking it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#5P#13910FWell, I do not have credit.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FAnd anyway … …\x01",
            "Do you try to contact the station?\x02",
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

    # Function_15_4C8B end

    def Function_16_5798(): pass

    label("Function_16_5798")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_57E7")
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
    Jump("Function_16_5798")

    label("loc_57E7")

    Return()

    # Function_16_5798 end

    def Function_17_57E8(): pass

    label("Function_17_57E8")

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
            "#00005F#6PJazz bar \"Galante\" ……\x01",
            "Why are you here again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PActually three years ago, here\x01",
            "I will exchange information with Mr. Guy\x01",
            "You made a promise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5P…… The death sentence entered\x01",
            "That was the tip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00006FIs that so……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5P#5P… … If a cult incident happens,\x01",
            "Empire and republican senators were arrested,\x01",
            "A new mayor was born … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PA trade meeting was held,\x01",
            "Crossbell city attacks occurred … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5P…… And now,\x01",
            "It is in a situation declaring national independence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PThey all seem to be apart,\x01",
            "It is an event that occurred by mutual interference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PIn other words, none in the series\x01",
            "It can be said that it happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00101FA series of flows …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PAnd, its flow -\x01",
            "If you can grasp \"big stations\"\x01",
            "Individual events can be seen well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PI will do it again.\x01",
            "Mr. Guy's murder case\x01",
            "Will it be exposed to light -\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PI thought so,\x01",
            "I requested to verify the case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PTo Mr. Lloyd, I have difficulty\x01",
            "I think that it is … ….\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x1388)

    ChrTalk(
        0x101,
        (
            "#6P#00003F…………………….\x02\x03",
            "#00000FNo … It's okay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00108FLloyd …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00208FMr. Lloyd ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303F…… Well, I do not have much time.\x02\x03",
            "#00300FLet's start it anyway.\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7302", 0)

    ChrTalk(
        0x11,
        (
            "#5PI agree……\x01",
            "Let's start right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PFirst of all, Mr. Guy's body\x01",
            "The situation when it was discovered -\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PTime is cloudy / light rainy day three years ago,\x01",
            "The place is the construction site of the current Orkis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PEstimated death time is early morning of the day,\x01",
            "Approximately until it is discovered\x01",
            "Half day passed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#5PAnd cause of death -\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PFrom the back with a conductive gun\x01",
            "It depends on being stamped out of the heart\x01",
            "It is hemorrhagic shock death.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#5P… … There is no mistake, is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00003FYeah … That is right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00101FFrom behind ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00306FIs that so……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00208F…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PHmm … … then when the body was found\x01",
            "Let's shift to the situation of the scene.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PFirst of all, violent\x01",
            "There was evidence of fighting … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PExcept for Gai's remains\x01",
            "It was a situation that was not left at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PAlso from the scene\x01",
            "He should have loved him\x01",
            "Tonfa is taken away … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PIt should have been attached to the chest further\x01",
            "The police emblem was also deprived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#5PI am from the emblem but …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PMembers of the mafia \"Rubache\"\x01",
            "What I took away from the scene,\x01",
            "It seems that it turned out newly, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FYes, for that information\x01",
            "I heard from Mr. Marconi directly.\x02\x03",
            "#00001FIn addition, from interrogation by interrogation\x01",
            "I have obtained a formal statement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#5PHmm, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PWhether or not there are witnesses next,\x01",
            "Let's confirm this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#5P…… In conclusion there are no witnesses.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PAt that time Orkis Tower\x01",
            "Construction was temporarily suspended,\x01",
            "That there was no official concerned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PFurthermore, the early morning of the incident occurrence\x01",
            "Wind and light rain, thunderous echoed … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PNo one comes close to the site\x01",
            "Those who saw the moment of murder\x01",
            "We could not confirm it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PIn addition, Mr. Guy went to the scene\x01",
            "To anyone in the vicinity to head\x01",
            "I was not talking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5P……, About the situation of the incident\x01",
            "That's all I have grasped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#5PMr. Lloyd, are there any supplements?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FNo, especially …\x02\x03",
            "#00001FIt is as I am grasping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00108F(Mr. Nielsen ……\x01",
            "As usual it is terrible information force. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203F(Yes, but with Mr. Guy\x01",
            "Personally friendly\x01",
            "It seems it was being done … …)\x02\x03",
            "#00201F(Regarding this incident,\x01",
            "That's why it may be. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PHM……\x01",
            "Let's move on to the case examination.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PTruth of the case -\x01",
            "It is a consideration of a criminal culprit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PFirst of all as suspect candidate\x01",
            "What is conceivable is \"Rubache\" ……\x01",
            "And, although it is related to \"D∴ G Church\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#5PMr. Lloyd, are the criminals them?\x02",
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 2)
    ClearScenarioFlags(0x0, 3)
    ClearScenarioFlags(0x0, 4)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_65FA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6779")
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
            "#1KGuy is a mafia, or\x01",
            "Was it killed by stakeholders of the D∴G organization?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "The criminal is a mafia official\x01",      # 0
            "The criminal is a religious official\x01",          # 1
            "There can not be both of them\x01",        # 2
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
        (0, "loc_66D9"),
        (1, "loc_670F"),
        (2, "loc_6745"),
        (SWITCH_DEFAULT, "loc_6766"),
    )


    label("loc_66D9")


    ChrTalk(
        0x101,
        "#6P#00006F(… … different, that's not the case -)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6766")

    label("loc_670F")


    ChrTalk(
        0x101,
        "#6P#00006F(… … different, that's not the case -)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6766")

    label("loc_6745")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_675E")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_675E")

    SetScenarioFlags(0x0, 2)
    Jump("loc_6766")

    label("loc_6766")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_6774")
    Jump("loc_6779")

    label("loc_6774")

    Jump("loc_65FA")

    label("loc_6779")


    ChrTalk(
        0x101,
        (
            "#6P#00003FNo, both of them are impossible.\x02\x03",
            "#00008FRegarding Rubache,\x01",
            "From Marconi and his minions -\x02\x03",
            "#00001FFor the cult, from Joachim,\x01",
            "I could not play while planning the killings\x01",
            "I have obtained a statement to the effect.\x02\x03",
            "#00006FAlso, out of reach of their eyes\x01",
            "Other minions and other stakeholders\x01",
            "It is unlikely that it was runaway.\x02\x03",
            "#00013F…… Big brother\x01",
            "Vigilance to these forces\x01",
            "I heard that I did not neglect it.\x02\x03",
            "Such a big brother, easy to live their own life\x01",
            "It is guided by a situation that is deprived … …\x02\x03",
            "I think that possibility is quite low.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00306FI guess it will be.\x02\x03",
            "#00301FAlthough I heard the story, I am fearless\x01",
            "It was a terrible olfactory owner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00206F……Yes.\x02\x03",
            "#00201FTo the mafia and the cult partner\x01",
            "I do not think it is a person taking a delay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PCertainly, every element\x01",
            "I deny those possibilities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PI do not know when it is before the cult incident,\x01",
            "Now that they are the culprit\x01",
            "I guess there is considerable impossibility.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PHmm, then the officials of the two biggest countries -\x01",
            "Let's examine its possibilities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PRepresentative of the Republic, Republican Empire,\x01",
            "And the relationship between them deeply related to them\x01",
            "Government officials, and intelligence officials -\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PMr. Guy,\x01",
            "It hung on the hands of such human beings\x01",
            "Is not there any possibility?\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 2)
    ClearScenarioFlags(0x0, 3)
    ClearScenarioFlags(0x0, 4)

    label("loc_6BB8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6DAE")
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
            "#1KDid Guy be killed by an official of the Empire or the Republic?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "The possibility is high\x01",            # 0
            "Unlikely\x01",            # 1
            "I can not say either\x01",      # 2
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
        (0, "loc_6C7A"),
        (1, "loc_6CF7"),
        (2, "loc_6D18"),
        (SWITCH_DEFAULT, "loc_6D9B"),
    )


    label("loc_6C7A")


    ChrTalk(
        0x101,
        (
            "#6P#00008F(The possibility is high -\x01",
            "……Is that really true? )\x02\x03",
            "#00001F(Think closely again,\x01",
            "Lloyd Bannings -)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6D9B")

    label("loc_6CF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6D10")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6D10")

    SetScenarioFlags(0x0, 2)
    Jump("loc_6D9B")

    label("loc_6D18")


    ChrTalk(
        0x101,
        (
            "#6P#00008F(I can not say either -\x01",
            "……Is that really true? )\x02\x03",
            "#00001F(Think closely again,\x01",
            "Lloyd Bannings -)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_6D9B")

    label("loc_6D9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_6DA9")
    Jump("loc_6DAE")

    label("loc_6DA9")

    Jump("loc_6BB8")

    label("loc_6DAE")


    ChrTalk(
        0x101,
        (
            "#6P#00003FNo, probably\x01",
            "That probability is low.\x02\x03",
            "#00008FCertainly, with this crossbell\x01",
            "There are many stakeholders in the two major powers who work injustice.\x02\x03",
            "Brother is wrongful of those\x01",
            "I heard that there were many things to press.\x02\x03",
            "#00001FAnd, such a deep relationship with them\x01",
            "Intelligence officials frequently crossbell\x01",
            "It is also true that it was in and out.\x02\x03",
            "#00006FBut, to be clear -\x01",
            "For their elder brother's behavior\x01",
            "It should not be a pain either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106FCertainly it will be so …\x02\x03",
            "#00108FIf two major powers feel that way,\x01",
            "Through autonomous state government\x01",
            "Holding down the police itself …\x02\x03",
            "#00101FIf it is a previous system,\x01",
            "Such domineering pressure\x01",
            "It will be easy to hang.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FOh, so much troublesome\x01",
            "Just one investigator\x01",
            "Call out and defer -\x02\x03",
            "#00001FIn the first place,\x01",
            "The merit to justify the cost\x01",
            "It should not exist.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#5PHM……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303FBesides, such people\x01",
            "I was trying to make contact\x01",
            "It is about Lloyd's big brother.\x02\x03",
            "#00300FLike the mafia, be alert.\x01",
            "I guess it will not come close to you carelessly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00206F--I'm with you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PYou guys are all fashionable …\x01",
            "You can also supplement from here\x01",
            "There is none.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#5PLet's see the last consideration -\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PSo far, as a suspect\x01",
            "By counterproposure of a possible person image\x01",
            "I have erased it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PBesides, other possible images of the criminal are\x01",
            "What on earth will it be like?\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 2)
    ClearScenarioFlags(0x0, 3)
    ClearScenarioFlags(0x0, 4)

    label("loc_7293")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_74F0")
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
            "#1KThen, what other possible criminal statues?\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Association of association \"Serving meat snake\"\x01",            # 0
            "Crossbell Police official\x01",                # 1
            "People who know well while Guy is cautious\x01",      # 2
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
        (0, "loc_7373"),
        (1, "loc_73F4"),
        (2, "loc_74BC"),
        (SWITCH_DEFAULT, "loc_74DD"),
    )


    label("loc_7373")


    ChrTalk(
        0x101,
        (
            "#6P#00006F(Although it is certainly a mysterious organization -\x01",
            "Think carefully. )\x02\x03",
            "#00013F(More naturally derived\x01",
            "There should be an answer. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_74DD")

    label("loc_73F4")


    ChrTalk(
        0x101,
        (
            "#6P#00008F(Internal crime by a person with a grudge -\x01",
            "It will not be impossible,\x01",
            "There should be more answers. )\x02\x03",
            "#00013F(Based on the flow so far\x01",
            "The answer that is derived naturally, that is -)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_74DD")

    label("loc_74BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_74D5")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_74D5")

    SetScenarioFlags(0x0, 2)
    Jump("loc_74DD")

    label("loc_74DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_74EB")
    Jump("loc_74F0")

    label("loc_74EB")

    Jump("loc_7293")

    label("loc_74F0")

    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#6P#00003FWhile the big brother is wary of it,\x01",
            "People I knew well -\x02\x03",
            "#00001FSuch a criminal statue\x01",
            "I think that it can be thought.\x02",
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
        "#6P#00205FHuh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00301FThat's … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#5PHmm, what is the reason?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F… … First of all, my brother\x01",
            "Everyone is going to the site\x01",
            "I did not reveal it.\x02\x03",
            "#00008FAnd, from the situation,\x01",
            "What I got aboard alone\x01",
            "There is almost no mistake.\x02\x03",
            "#00013FFrom this point of view,\x01",
            "The possibility that the criminal is \"acquaintance\" is\x01",
            "I think that it can be said that it is quite expensive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00106FWell, indeed …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FI called it from my older brother,\x01",
            "Or was it called? …\x01",
            "I do not know.\x02\x03",
            "#00003FPlace is not popular Construction site -\x02\x03",
            "#00008FIn other words never to others\x01",
            "I do not want to be heard, do not be asked,\x01",
            "It was an important story.\x02\x03",
            "#00013FThere is some exchange there … …\x01",
            "As a result of it breaking down, to lose life\x01",
            "Is not it becoming it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#5PWhat is that exchange …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FSpecifically, I do not know.\x02\x03",
            "#00008FHowever, it is necessary to take away until life\x01",
            "Considering what it was,\x01",
            "The content is also equivalent … …\x02\x03",
            "#00001FFor example, it is …\x01",
            "It is related to \"some intrigue\".\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x103,
        "#6P#00200FConspiracy, are you … ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#5PHM……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F…… Nielsen said,\x01",
            "\"If you grab the majority you can hit the light\"\x01",
            "That's right.\x02\x03",
            "#00000FWhen I heard it, I was drowning\x01",
            "I felt something connected.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x11,
        "#5PLaw\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FThere is a possibility that the big brother was impending\x01",
            "Any conspiracy ……\x02\x03",
            "#00003FIt is D∴ G organization and mafia,\x01",
            "While relating to the empire and the republic\x01",
            "Separate entities from them -\x02\x03",
            "#00008FIt was promoted by such existence,\x01",
            "Or is still being advanced -\x02\x03",
            "#00001FAs such\x01",
            "Can not I guess?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00105FAnother subject … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#6P#00201FIt is also currently in progress …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001FOh, my brother's murderer still\x01",
            "Even from the fact that it has not been found\x01",
            "That can be said.\x02\x03",
            "#00003FAnd that is\x01",
            "The incident is not over yet,\x01",
            "I think like a proof of best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#5P…………………………\x02",
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
            "#00006F…… After all, is there impossible?\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x11)
    Sleep(500)

    ChrTalk(
        0x11,
        (
            "#5PHouse……\x01",
            "I thought it was a wonderful inference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#5P─ ─ Lloyd, Mr. Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PTry verification so far\x01",
            "Did you have someone you thought of?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PThree years ago, I called Guy,\x01",
            "Who is believed to have killed …?\x02",
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
            "#6P#00006FNo, unfortunately …\x02\x03",
            "#00003FEven if you say \"acquaintance\", it gets disgusted\x01",
            "It is about my brother whose face was wide.\x02\x03",
            "#00008F… …. taken away from the scene\x01",
            "Tonfa that is not found yet\x01",
            "The fact that the vital point was shot from behind … …\x02\x03",
            "#00013FPersonally, those elements are\x01",
            "It is likely to be the key to clarifying the incident\x01",
            "I feel like ……\x02\x03",
            "#00006FIf it can be specified by itself\x01",
            "As of three years ago, the Investigation Division\x01",
            "I think I'm keeping track of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#5PHmm, it is reasonable.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PAt the moment, we can identify the criminal\x01",
            "I do not have all the pieces.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5P- But this is\x01",
            "It can be said clearly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PTo find the missing last piece\x01",
            "Mr. Lloyd - You are the only one.\x02",
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
        "#6P#00105FMr. Nielsen …\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)

    ChrTalk(
        0x101,
        "#6P#00004FYeah … that's what I meant.\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7151", 0)

    ChrTalk(
        0x11,
        "#5PHehe, I'm glad I could hear that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5P… … as if three years ago,\x01",
            "We promised to exchange information\x01",
            "I feel like I was able to do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PPlease go out with me.\x01",
            "I'm really thankful to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FNo, thank you.\x01",
            "thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#5PSo I will -\x01",
            "We are looking forward to your success.\x02",
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

    def lambda_8275():
        OP_95(0xFE, -7730, 0, 1910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8275)
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x103, 0x0)
    WaitChrThread(0x11, 1)

    def lambda_82A5():
        OP_95(0xFE, 690, 0, 1520, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_82A5)
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
            "#6P#00202FMr. Nielsen …\x01",
            "As if we were\x01",
            "You seem to have guided it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00004FOh … … Maybe, promises with my brother\x01",
            "I guess you had been careful about it all the time.\x02\x03",
            "#00002FIt was really nice to talk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00109FHehe … … That's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00304FYou know.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x104, 0x1)
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#6P#00301F#12P… … Yoshi, it's been a blast\x01",
            "I suppose I should go!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#5P#00003FOh …… Anyway now\x01",
            "Let's hurry to the president's office of Rubathe's ruins.\x02\x03",
            "#00013FFrom Captain Rector\x01",
            "You should be able to extract some information!\x02",
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
            "Quest 【Verification of Murder of Guy Bannings】\x07\x00",
            "Achieved!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_853B")
    OP_2C(0x95, 0x2)
    Jump("loc_854F")

    label("loc_853B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_854F")
    OP_2C(0x95, 0x1)

    label("loc_854F")

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

    # Function_17_57E8 end

    SaveToFile()

Try(main)
