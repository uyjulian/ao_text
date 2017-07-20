from ScenarioHelper import *

def main():
    CreateScenaFile(
        "r0210.bin",                # FileName
        "r0210",                    # MapName
        "r0210",                    # Location
        0x00A5,                     # MapIndex
        "ed7121",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x04,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "r0210",                  # 0
        "Penetrating",         # 1
        "Falsehood",               # 2
        "僼傿 僢僔 儍乕",           # 3
        "儗僀 僋儘 乕僪 嘨悽",       # 4
        "棾媨 僇僌 儎",             # 5
    ))

    AddCharChip((
        "chr/ch32200.itc",                   # 00
        "chr/ch24200.itc",                   # 01
        "chr/ch46100.itc",                   # 02
        "chr/ch45600.itc",                   # 03
        "chr/ch45800.itc",                   # 04
    ))

    DeclNpc(4294966907, 0,       4294966147, 188,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(1080,    0,       4294966186, 270,  389,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(6010,    0,       4294959076, 0,    389,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(529,     0,       4294966147, 270,  389,  0x0, 0,   3,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(4294966847, 0,       4294966106, 90,   389,  0x0, 0,   4,   0,   0,   0,   0,   9,   255,  0)

    DeclActor(1510,    0,       3420,    1200,    1510,    750,     3420,    0x007C, 0,  3,  0x0000)

    ChipFrameInfo(384, 0)                                        # 0

    ScpFunction((
        "Function_0_180",          # 00, 0
        "Function_1_230",          # 01, 1
        "Function_2_39C",          # 02, 2
        "Function_3_3E7",          # 03, 3
        "Function_4_498",          # 04, 4
        "Function_5_162E",         # 05, 5
        "Function_6_1B9C",         # 06, 6
        "Function_7_1C53",         # 07, 7
        "Function_8_1D96",         # 08, 8
        "Function_9_2532",         # 09, 9
    ))


    def Function_0_180(): pass

    label("Function_0_180")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_1B8"),
        (1, "loc_1C4"),
        (2, "loc_1D0"),
        (3, "loc_1DC"),
        (4, "loc_1E8"),
        (5, "loc_1F4"),
        (6, "loc_200"),
        (SWITCH_DEFAULT, "loc_20C"),
    )


    label("loc_1B8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_1C4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_1D0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_1DC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_1E8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_1F4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_200")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_20C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_218")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_22F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_22F")

    Return()

    # Function_0_180 end

    def Function_1_230(): pass

    label("Function_1_230")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_243")
    SetChrFlags(0x8, 0x80)
    Jump("loc_39B")

    label("loc_243")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_274")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26A")
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)

    label("loc_26A")

    SetChrFlags(0x8, 0x80)
    Jump("loc_39B")

    label("loc_274")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_287")
    SetChrFlags(0x8, 0x80)
    Jump("loc_39B")

    label("loc_287")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2BB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_2B6")
    SetChrPos(0xA, 1080, 0, -1110, 270)
    ClearChrFlags(0xA, 0x80)
    TurnDirection(0x8, 0xA, 0)

    label("loc_2B6")

    Jump("loc_39B")

    label("loc_2BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2C9")
    Jump("loc_39B")

    label("loc_2C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_308")
    SetChrPos(0x8, -390, 0, -1150, 90)
    SetChrFlags(0x8, 0x10)
    SetChrPos(0x9, 1080, 0, -1110, 270)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0x9, 0x80)
    Jump("loc_39B")

    label("loc_308")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_316")
    Jump("loc_39B")

    label("loc_316")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_324")
    Jump("loc_39B")

    label("loc_324")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_341")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33C")
    SetChrFlags(0x8, 0x80)

    label("loc_33C")

    Jump("loc_39B")

    label("loc_341")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_34F")
    Jump("loc_39B")

    label("loc_34F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_35D")
    Jump("loc_39B")

    label("loc_35D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_37A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_375")
    SetChrFlags(0x8, 0x80)

    label("loc_375")

    Jump("loc_39B")

    label("loc_37A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_38D")
    SetChrFlags(0x8, 0x80)
    Jump("loc_39B")

    label("loc_38D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_39B")
    SetChrFlags(0x8, 0x80)

    label("loc_39B")

    Return()

    # Function_1_230 end

    def Function_2_39C(): pass

    label("Function_2_39C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_3AE")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E6")
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_3E6")

    Return()

    # Function_2_39C end

    def Function_3_3E7(): pass

    label("Function_3_3E7")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "\"The second volume of sweets kingdom\" is.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('料理手册', 0x0)"), scpexpr(EXPR_END)), "loc_494")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x12)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_494")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "\"Slippery Annin Tofu\"\x07\x00",
            "I learned the recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_494")

    TalkEnd(0xFF)
    Return()

    # Function_3_3E7 end

    def Function_4_498(): pass

    label("Function_4_498")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8C7")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "Oh, Lloyd Members.\x01",
            "Did you finally give your face?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FSerdan branch manager, here is …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, this building originally\x01",
            "It was a boat hut for rent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Since discontinuing several years ago,\x01",
            "It seems she was left unattended for a long time\x01",
            "I was able to borrow it cheaply.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, to us leaving again\x01",
            "It is a new branch oriented to customs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "More than that, members of Lloyd, you as well\x01",
            "\"Bombing with the Emperor 's Club#4REmbankment#About the game\x01",
            "I would like to explain … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FWell, \"Bomb victory\" is … ….?\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00003FIndeed, the crown club's\x01",
            "Is it \"a battle for bombing\" with five members … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, that's why.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For those who win,\x01",
            "We manage somehow\x01",
            "I am going though …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If possible, even Lloyd members\x01",
            "Please give me cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYes, I also love you\x01",
            "It is impossible to fish\x01",
            "Because I am sorry.\x02\x03",
            "#00000FAs much as possible, I will try hard.\x02",
        )
    )

    CloseMessageWindow()
    Sound(814, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "To the members of the Emperor 's Club,\x01",
            "I began to challenge \"bomb victory\".\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Detailed information on the game is,\x01",
            "I am in 'The Emperor' s Club at East Street '\x01",
            "You can hear from the receptionist Sailram.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x1C0, 0)

    label("loc_8C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9D4")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "Oh, Lloyd Members.\x01",
            "Did you come right now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As you can see there is nothing,\x01",
            "Well, please relax.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Also, due to lack of materials\x01",
            "I will put a price, but a little\x01",
            "We have prepared for sale, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "If you do not mind, please feel free to look at it.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15F, 7)

    label("loc_9D4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9DE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_162A")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A41")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_A56")

    label("loc_A41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A56")
    TurnDirection(0xFE, 0x0, 0)

    label("loc_A56")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ABB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 5)), scpexpr(EXPR_END)), "loc_A85")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_A7E")
    OP_AF(0x37)
    Jump("loc_A80")

    label("loc_A7E")

    OP_AF(0x3B)

    label("loc_A80")

    Jump("loc_A97")

    label("loc_A85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_A95")
    OP_AF(0x36)
    Jump("loc_A97")

    label("loc_A95")

    OP_AF(0x3A)

    label("loc_A97")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AB6")
    TurnDirection(0xFE, 0x9, 0)

    label("loc_AB6")

    Jump("loc_1625")

    label("loc_ABB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1625")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_B71")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "Bomb victory with the Emperor 's Club ……\x01",
            "Please also cooperate with Lloyd members.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, to this match\x01",
            "The future of the fishing public division is going on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1625")

    label("loc_B71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_B7F")
    Jump("loc_1625")

    label("loc_B7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1040")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_C1C")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "Hmm, to Mr. Lloyd\x01",
            "I do not really have a word of gratitude.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With this condition, we will continue to do so in the future\x01",
            "To create a legend\x01",
            "I'm expecting you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_103B")

    label("loc_C1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C8B")

    ChrTalk(
        0xFE,
        (
            "Hmm, if I do a little more\x01",
            "You can come to that one … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Then be sure … …!\x02",
    )

    CloseMessageWindow()
    Jump("loc_103B")

    label("loc_C8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FB1")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "Members of Lloyd, their medals ……\x01",
            "No way, have you killed all four heavenly kings?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah … I managed to do something.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hu ha ha, drift is a member of Lloyd!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, if you are a member of Lloyd\x01",
            "I can trust this guy with confidence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please, our\x01",
            "Receive the \"soul\"!\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '虹丸ＥＸ'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('虹丸ＥＸ', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00005FTh-This is……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's because of the opponent's club\x01",
            "While we are breathing out blood stagnation\x01",
            "It is the ultimate fishing bait that we have succeeded in developing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because we make sepis as a material, we can stretch the value ……\x01",
            "You can produce as much as you want to say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FI see.\x01",
            "It is blood and sweat crystal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Oh, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How about Lloyd Members ……\x01",
            "That guy, at that Lake Road\x01",
            "Fold me your nose!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you are a member of Lloyd,\x01",
            "You surely can do it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FIs, yes … I will try!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x190, 5)
    Jump("loc_103B")

    label("loc_FB1")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "Members of Lloyd … … ours\x01",
            "With my thoughts, that Lake Road's\x01",
            "Fold me your nose!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you are a member of Lloyd,\x01",
            "You surely can do it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_103B")

    Jump("loc_1625")

    label("loc_1040")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_104E")
    Jump("loc_1625")

    label("loc_104E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_108F")

    ChrTalk(
        0xFE,
        (
            "Hmm, but\x01",
            "The final weapon is the final weapon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1625")

    label("loc_108F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_109D")
    Jump("loc_1625")

    label("loc_109D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_11C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1140")

    ChrTalk(
        0xFE,
        "Damn, next time it's over again!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "\"Ginza\" Triton ……\x01",
            "He is a really horrible man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The four principal heavenly heads to drift\x01",
            "Why is it different?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11C0")

    label("loc_1140")


    ChrTalk(
        0xFE,
        (
            "\"Ginza\" Triton ……\x01",
            "He is a really horrible man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I surely put that Atari ……\x01",
            "Does he see the bottom of the water surface?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11C0")

    Jump("loc_1625")

    label("loc_11C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1241")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11DD")
    Jump("loc_123C")

    label("loc_11DD")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "Members of Lloyd,\x01",
            "Thank you so much for today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanks tonight\x01",
            "I'm going to be able to sleep soundly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_123C")

    Jump("loc_1625")

    label("loc_1241")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_13FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1362")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        "Does Lloyd Members know?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When you kill the Emperor 's Club,\x01",
            "Something strange in the title\x01",
            "You seem to get it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the way, I got it yesterday\x01",
            "You have defeated Naruses.\x01",
            "You got the title \"Water Mad Hunter\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Fuha, while the taste prepared by the enemy\x01",
            "This is a little fun.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_13F7")

    label("loc_1362")


    ChrTalk(
        0xFE,
        (
            "I got home yesterday\x01",
            "You have defeated Naruses.\x01",
            "You got the title \"Water Mad Hunter\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Fuha, while the taste prepared by the enemy\x01",
            "This is a little fun.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13F7")

    Jump("loc_1625")

    label("loc_13FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1582")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14F0")

    ChrTalk(
        0xFE,
        (
            "But with this feeling\x01",
            "Working on fishing is\x01",
            "I wonder when it was first time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I was young I was on dawn\x01",
            "Bet fishing tackle and make a battle for bombing\x01",
            "Although I also challenged … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What's wrong, oddly\x01",
            "I am disappointed that I am excited.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_157D")

    label("loc_14F0")


    ChrTalk(
        0xFE,
        (
            "Hmm, this feeling\x01",
            "Working on fishing is\x01",
            "I wonder when it was first time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What's wrong, oddly\x01",
            "I am disappointed that I am excited.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_157D")

    Jump("loc_1625")

    label("loc_1582")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_160E")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "At any rate,\x01",
            "Fishing public division · crossbell branch\x01",
            "I will start again from here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Members of Lloyd, to each other\x01",
            "Let 's try hard and go.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1625")

    label("loc_160E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_161C")
    Jump("loc_1625")

    label("loc_161C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1625")

    label("loc_1625")

    Jump("loc_9DE")

    label("loc_162A")

    TalkEnd(0xFE)
    Return()

    # Function_4_498 end

    def Function_5_162E(): pass

    label("Function_5_162E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_19F6")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('绀碧竿', 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber('琥珀轴', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('翡翠线', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('红莲钩', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1662")
    Jump("loc_19F6")

    label("loc_1662")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('绀碧竿', 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber('琥珀轴', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('翡翠线', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "GetItemNumber('红莲钩', 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_19F6")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x101, 500)

    ChrTalk(
        0xFE,
        "Lloyd, that is … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYeah, definitely fishing tackle\x01",
            "I think it is a part,\x01",
            "It is very beautiful, is not it?\x02\x03",
            "#00000FAt the fishing spot recovered from the four heavenly kings\x01",
            "I caught an unusual fish ….\x01",
            "That fish spit out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "……There is no mistake.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It was once a great fighter of travel\x01",
            "It is a part of the legendary fishing gear that I was using.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When he leaves the crossbell,\x01",
            "It was sealed in this place\x01",
            "I was listening … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No way,\x01",
            "What you can find out like this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FWell, so much\x01",
            "Was it amazing ……\x02\x03",
            "#00003FBut what shall I do.\x01",
            "If you return to that person … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "No, that is not necessary.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "… … because he said.\x01",
            "The fishing tackle can be used by those who found it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lloyd,\x01",
            "There are four parts in all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you get all that\x01",
            "Please come to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If I am using that part\x01",
            "It can be assembled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FI see, I see … ….\x01",
            "Okay, I will remember.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x8, 0)
    SetScenarioFlags(0x0, 3)
    SetScenarioFlags(0x1C0, 1)
    TalkEnd(0xFE)
    Return()

    label("loc_19F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1A84")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "Legendary fishing tackle sealed once\x01",
            "What is said to appear at such times …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, Lloyd.\x01",
            "This may be destiny, is not it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x8, 0)
    Jump("loc_1B98")

    label("loc_1A84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1A92")
    Jump("loc_1B98")

    label("loc_1A92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1AA0")
    Jump("loc_1B98")

    label("loc_1AA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1AAE")
    Jump("loc_1B98")

    label("loc_1AAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1B2D")

    ChrTalk(
        0xFE,
        (
            "Copan also\x01",
            "I hit the wall\x01",
            "I do not think so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Again, our power alone\x01",
            "No matter what more we can do ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B98")

    label("loc_1B2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1B3B")
    Jump("loc_1B98")

    label("loc_1B3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1B49")
    Jump("loc_1B98")

    label("loc_1B49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1B57")
    Jump("loc_1B98")

    label("loc_1B57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1B65")
    Jump("loc_1B98")

    label("loc_1B65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1B73")
    Jump("loc_1B98")

    label("loc_1B73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1B81")
    Jump("loc_1B98")

    label("loc_1B81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1B8F")
    Jump("loc_1B98")

    label("loc_1B8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1B98")

    label("loc_1B98")

    TalkEnd(0xFE)
    Return()

    # Function_5_162E end

    def Function_6_1B9C(): pass

    label("Function_6_1B9C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1BAD")
    Jump("loc_1C4F")

    label("loc_1BAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1C4F")
    TurnDirection(0xFE, 0x101, 0)

    NpcTalk(
        0xFE,
        "Head of Fisher",
        (
            "Master Lloyd, you are my\x01",
            "It is the pride of the fishing public division.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Head of Fisher",
        (
            "If there is opportunity, by all means Libert\x01",
            "I would like to fish together.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C4F")

    TalkEnd(0xFE)
    Return()

    # Function_6_1B9C end

    def Function_7_1C53(): pass

    label("Function_7_1C53")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C70")
    Call(0, 8)
    TalkEnd(0xFE)
    Return()

    label("loc_1C70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1CFF")

    ChrTalk(
        0xB,
        (
            "To us, survival technique\x01",
            "There is knowledge and there are also Enigma.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you understand, I do not need to worry\x01",
            "Go out quickly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D92")

    label("loc_1CFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1D0D")
    Jump("loc_1D92")

    label("loc_1D0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1D7B")

    ChrTalk(
        0xB,
        (
            "Hmm, even so\x01",
            "Independent invalid declaration ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "This more and more involved the turbulence\x01",
            "It has become development.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D92")

    label("loc_1D7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_1D89")
    Jump("loc_1D92")

    label("loc_1D89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1D92")

    label("loc_1D92")

    TalkEnd(0xFE)
    Return()

    # Function_7_1C53 end

    def Function_8_1D96(): pass

    label("Function_8_1D96")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E5E")

    ChrTalk(
        0xB,
        (
            "To advocate \"Continental Union Association\"\x01",
            "Civil war of the motherland Elevenia …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "No way, in about this month\x01",
            "The secular is going to move so far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Yes … What is the Blue Sky's Honor?\x01",
            "That is exactly this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F46")

    label("loc_1E5E")


    ChrTalk(
        0xB,
        (
            "To advocate \"Continental Union Association\"\x01",
            "Civil war of the motherland Elevenia …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "No way, in about this month\x01",
            "The secular is going to move so far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "… …. Furthermore, come here\x01",
            "It came with an independent ineffective declaration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Yes … What is the Blue Sky's Honor?\x01",
            "That is exactly this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F46")

    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xB, 0x101, 500)
    Sleep(500)
    TurnDirection(0xC, 0x101, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2008")
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
            "【It does not change】\x01",        # 0
            "【Defeated】\x01",        # 1
            "【Not defeated】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FF6")
    SetScenarioFlags(0x191, 1)
    Jump("loc_2008")

    label("loc_1FF6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2008")
    ClearScenarioFlags(0x191, 1)

    label("loc_2008")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_2049")

    ChrTalk(
        0xB,
        (
            "Hmm, you are the fishing public division's\x01",
            "Lloyd Bannings?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_207C")

    label("loc_2049")


    ChrTalk(
        0xB,
        (
            "Hmm, you are the fishing public division's\x01",
            "Lloyd Bannings?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_207C")


    ChrTalk(
        0x101,
        (
            "#00005FYou are the crown club\x01",
            "Mr. Lake Road ……\x01",
            "Why in a place like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hunt, by no means anything\x01",
            "It is to practice fishing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Anyway I am the head of a club …\x01",
            "While losing the game, I am sorry\x01",
            "It will not be good to return home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FI see, I see … ….\x02\x03",
            "#00001FBut, in such a place\x01",
            "For being there forever ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FYes, we\x01",
            "I will deliver it to Almorika village\x01",
            "Get ready for evacuation soon ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hmm, that's about us\x01",
            "Could you please leave me alone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "People who are anglers, from daily\x01",
            "I'm used to dangers outside,\x01",
            "I do not have to worry about starving.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Oh, if it says it is dangerous\x01",
            "I think that it is the same no matter where you are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FOkay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Anyway, we have Enigma\x01",
            "Clearly speaking it is unnecessary care for worrying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "When you understand, go out quickly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FHaha …\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_250B")
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "Oh … but it came at the pains.\x01",
            "I will give you souvenirs for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "I'm overfishing a bit.\x01",
            "We alone have a good time to eat.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '鲤鱼'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I received 10 animals.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('鲤鱼', 10)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0xB,
        (
            "In the meantime,\x01",
            "The fish spit out.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '还魂粉'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('还魂粉', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00005FOh, thank you.\x02",
    )

    CloseMessageWindow()

    label("loc_250B")

    SetScenarioFlags(0x1BD, 2)
    SetScenarioFlags(0x0, 4)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    TurnDirection(0xB, 0xC, 0)
    TurnDirection(0xC, 0xB, 0)
    Return()

    # Function_8_1D96 end

    def Function_9_2532(): pass

    label("Function_9_2532")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_254F")
    Call(0, 8)
    TalkEnd(0xFE)
    Return()

    label("loc_254F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_25C9")

    ChrTalk(
        0xC,
        "… … Is not the story already enough?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "We are also busy with various things.\x01",
            "I do not want to disturb you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_267F")

    label("loc_25C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_25D7")
    Jump("loc_267F")

    label("loc_25D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2668")

    ChrTalk(
        0xC,
        (
            "Even if I have difficulty\x01",
            "Together with Lake Road Mr.\x01",
            "I am prepared to go over it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Rather, rather\x01",
            "As it is just for two people …… spray\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_267F")

    label("loc_2668")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_2676")
    Jump("loc_267F")

    label("loc_2676")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_267F")

    label("loc_267F")

    TalkEnd(0xFE)
    Return()

    # Function_9_2532 end

    SaveToFile()

Try(main)
