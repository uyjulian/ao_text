from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Branch Manager Celdan",  # 1
        "Peter",                  # 2
        "Fisher",                 # 3
        "Lakelord III",           # 4
        "Kaguya, the Dragon Queen",# 5
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
        "Function_4_4A3",          # 04, 4
        "Function_5_1857",         # 05, 5
        "Function_6_1E04",         # 06, 6
        "Function_7_1ECF",         # 07, 7
        "Function_8_204C",         # 08, 8
        "Function_9_2876",         # 09, 9
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
            ""The Kingdom of Sweets\x01",
            "Vol.2" is here.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_49F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x12)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49F")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Learned the \x07\x02",
            ""Smooth\x01",
            "Almond Jelly"\x07\x00",
            " recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_49F")

    TalkEnd(0xFF)
    Return()

    # Function_3_3E7 end

    def Function_4_4A3(): pass

    label("Function_4_4A3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_91D")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "Oh, member Lloyd. You've\x01",
            "finally come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FBranch Manager Celdan,\x01",
            "this place...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes, this building was\x01",
            "originally a boat livery\x01",
            "shed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems it was abandoned after\x01",
            "cessation of business, many, many years\x01",
            "ago, and so I borrowed it for cheap.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, it's an ideal\x01",
            "location for us to make\x01",
            "a fresh start.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "More importantly, I'd like to\x01",
            "explain the Angler Duels against\x01",
            "the Imperial Fishing Club to you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FA-Angler Duels...?\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00003FI see, Angler Duels against\x01",
            "the five members of the\x01",
            "Imperial Fishing Club...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yes, that's it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "We plan to do something\x01",
            "about the matches,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If possible, I'd like to\x01",
            "ask for your cooperation\x01",
            "as well, Member Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FRight. I don't want to\x01",
            "be unable to fish in my\x01",
            "favorite spots, either.\x02\x03",
            "#00000FI'll support you as much\x01",
            "as I can.\x02",
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
            "You are now able to challenge\x01",
            "Imperial Fishing Club members\x01",
            "to Angler Duels.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You can ask the details of the matches\x01",
            "from Receptionist Sylum at the "East\x01",
            "Street Imperial Fishing Club".\x07\x00\x02",
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

    label("loc_91D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A52")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "Oh, member Lloyd. You\x01",
            "came right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As you can see, there's\x01",
            "nothing here, but please,\x01",
            "make yourself at home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Also, although prices are high\x01",
            "because supplies are scarce, we've\x01",
            "prepared a few things for sale.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If you like, please feel\x01",
            "free to have a look.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15F, 7)

    label("loc_A52")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A5C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1853")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AB3")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_AC8")

    label("loc_AB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AC8")
    TurnDirection(0xFE, 0x0, 0)

    label("loc_AC8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 5)), scpexpr(EXPR_END)), "loc_AF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_AF0")
    OP_AF(0x37)
    Jump("loc_AF2")

    label("loc_AF0")

    OP_AF(0x3B)

    label("loc_AF2")

    Jump("loc_B09")

    label("loc_AF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_B07")
    OP_AF(0x36)
    Jump("loc_B09")

    label("loc_B07")

    OP_AF(0x3A)

    label("loc_B09")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B28")
    TurnDirection(0xFE, 0x9, 0)

    label("loc_B28")

    Jump("loc_184E")

    label("loc_B2D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_184E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_C29")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "The Angler Duels against the Imperial\x01",
            "Fishing Club... I'm begging for your\x01",
            "cooperation as well, Member Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "After all is said and done,\x01",
            "the future of the Fisherman's\x01",
            "Guild rests on these duels.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_184E")

    label("loc_C29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_C37")
    Jump("loc_184E")

    label("loc_C37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_116F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_CD7")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "Yes, words can never\x01",
            "express my thanks to\x01",
            "you, Master Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At this rate, I expect\x01",
            "new legends to be born\x01",
            "from now on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_116A")

    label("loc_CD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D44")

    ChrTalk(
        0xFE,
        (
            "Hmm, he should be coming\x01",
            "in a little while...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "And then, for sure...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_116A")

    label("loc_D44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10D7")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "Member Lloyd, those medals...\x01",
            "Impossible, did you defeat\x01",
            "all of the Elite Four?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes... I managed it,\x01",
            "somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Bwah ha ha, as expected\x01",
            "from you, Member Lloyd!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes. If it's you, Member\x01",
            "Lloyd, I can rest assured\x01",
            "and entrust you with this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please, accept our\x01",
            ""soul"!!\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x18B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x18B, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00005FThis is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's the ultimate fishing bait we\x01",
            "developed and obtained while spitting blood\x01",
            "competing against the Imperial Fishing Club.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's pricey since it uses sepith as\x01",
            "ingredient, but... If you say the\x01",
            "word, we can make as much as you like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FI see... A quartz made\x01",
            "of everyone's blood and\x01",
            "sweat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Yeah, exactly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please, Member Lloyd... Use\x01",
            "that to knock that Lakelord\x01",
            "down a peg or two!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If it's you, Member\x01",
            "Lloyd, I'm sure you can\x01",
            "do it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FY-Yes... I'll try!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x190, 5)
    Jump("loc_116A")

    label("loc_10D7")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "Member Lloyd... Knock that\x01",
            "Lakelord down a peg or two\x01",
            "with our feelings, too!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If it's you, Member\x01",
            "Lloyd, I'm sure you can\x01",
            "do it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_116A")

    Jump("loc_184E")

    label("loc_116F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_117D")
    Jump("loc_184E")

    label("loc_117D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_11C7")

    ChrTalk(
        0xFE,
        (
            "Hmm. Anyhow, an ultimate\x01",
            "weapon is an ultimate\x01",
            "weapon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_184E")

    label("loc_11C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_11D5")
    Jump("loc_184E")

    label("loc_11D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1349")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12BF")

    ChrTalk(
        0xFE,
        (
            "Damn, how many times has\x01",
            "it been already!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Triton, the Silver\x01",
            "Orca... He's a really\x01",
            "frightening man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "He's not the leader of the Elite\x01",
            "Four for nothing. The others are\x01",
            "nothing compared to him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1344")

    label("loc_12BF")


    ChrTalk(
        0xFE,
        (
            "Triton, the Silver\x01",
            "Orca... He's a really\x01",
            "frightening man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Those hit streaks... Can\x01",
            "that guy see beneath the\x01",
            "water surface?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1344")

    Jump("loc_184E")

    label("loc_1349")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_13D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1361")
    Jump("loc_13D3")

    label("loc_1361")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "Member Lloyd, thank you\x01",
            "very much for today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanks to you, it seems\x01",
            "I'll sleep soundly\x01",
            "tonight.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13D3")

    Jump("loc_184E")

    label("loc_13D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_15E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1539")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "Member Lloyd, did you\x01",
            "know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems that if you defeat members\x01",
            "of the Imperial Fishing Club, you\x01",
            "obtain some kind of bizarre title.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Incidentally, I beat that\x01",
            "Narses guy yesterday and earned\x01",
            "the "Crazy Wave Hunter" title.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Bwah ha ha, although it's an\x01",
            "enemy idea, I'll slightly\x01",
            "look forward to this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15E3")

    label("loc_1539")


    ChrTalk(
        0xFE,
        (
            "Yesterday I beat that Narses\x01",
            "guy, you see. I earned the\x01",
            ""Crazy Wave Hunter" title.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Bwah ha ha, although it's an\x01",
            "enemy idea, I'll slightly\x01",
            "look forward to this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15E3")

    Jump("loc_184E")

    label("loc_15E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_17A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1704")

    ChrTalk(
        0xFE,
        (
            "Anyway, I wonder how long\x01",
            "it's been since I've tackled\x01",
            "fishing with such feelings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When I was young, I even challenged\x01",
            "the Angler Duels betting my fishing\x01",
            "gear recklessly, however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How to say it, it's\x01",
            "troublesome but I'm\x01",
            "strangely excited.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_179B")

    label("loc_1704")


    ChrTalk(
        0xFE,
        (
            "Hmm. I wonder how long has\x01",
            "it been since I've tackled\x01",
            "fishing with such feelings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How to say it, it's\x01",
            "troublesome but I'm\x01",
            "strangely excited.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_179B")

    Jump("loc_184E")

    label("loc_17A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1837")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "In any case, the Crossbell\x01",
            "Branch of the Fisherman's\x01",
            "Guild starts anew from here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Member Lloyd, let's both\x01",
            "do our best.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_184E")

    label("loc_1837")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1845")
    Jump("loc_184E")

    label("loc_1845")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_184E")

    label("loc_184E")

    Jump("loc_A5C")

    label("loc_1853")

    TalkEnd(0xFE)
    Return()

    # Function_4_4A3 end

    def Function_5_1857(): pass

    label("Function_5_1857")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C45")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x344, 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x345, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x346, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x347, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_188B")
    Jump("loc_1C45")

    label("loc_188B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x344, 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x345, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x346, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x347, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1C45")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x101, 500)

    ChrTalk(
        0xFE,
        "Lloyd, that's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYes, there's no mistaking it. It's\x01",
            "a fishing gear part. And a very\x01",
            "pretty one at that.\x02\x03",
            "#00000FI caught a rare fish from a fishing\x01",
            "spot I recovered from the Elite\x01",
            "Four... The fish spat that out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...No doubt.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's a part of the legendary\x01",
            "gear that was once used by a\x01",
            "remarkable wandering angler.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard he sealed it in\x01",
            "this land when he left\x01",
            "Crossbell, however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "To think you found it\x01",
            "like that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FI-Is it that amazing?\x02\x03",
            "#00003FThen, what do we do? We\x01",
            "should give it back to\x01",
            "him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No, there's no need for\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Because he said that\x01",
            "he who finds his fishing\x01",
            "gear, may use it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lloyd, there are 4 parts\x01",
            "in total.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please come to my place\x01",
            "if you manage to obtain\x01",
            "all of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I should be able to put\x01",
            "the parts together for\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FI-I see... I understand,\x01",
            "I'll keep that in mind.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x8, 0)
    SetScenarioFlags(0x0, 3)
    SetScenarioFlags(0x1C0, 1)
    TalkEnd(0xFE)
    Return()

    label("loc_1C45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1CDF")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "To think that the once sealed\x01",
            "legendary fishing gear would\x01",
            "appear at a time like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lloyd, could this be\x01",
            "fate?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x8, 0)
    Jump("loc_1E00")

    label("loc_1CDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1CED")
    Jump("loc_1E00")

    label("loc_1CED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1CFB")
    Jump("loc_1E00")

    label("loc_1CFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1D09")
    Jump("loc_1E00")

    label("loc_1D09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1D95")

    ChrTalk(
        0xFE,
        (
            "Coppen seems to have hit\x01",
            "a wall as well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As I thought, we can't do\x01",
            "any more than this with\x01",
            "our abilities alone...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E00")

    label("loc_1D95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1DA3")
    Jump("loc_1E00")

    label("loc_1DA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1DB1")
    Jump("loc_1E00")

    label("loc_1DB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1DBF")
    Jump("loc_1E00")

    label("loc_1DBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1DCD")
    Jump("loc_1E00")

    label("loc_1DCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1DDB")
    Jump("loc_1E00")

    label("loc_1DDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1DE9")
    Jump("loc_1E00")

    label("loc_1DE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1DF7")
    Jump("loc_1E00")

    label("loc_1DF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1E00")

    label("loc_1E00")

    TalkEnd(0xFE)
    Return()

    # Function_5_1857 end

    def Function_6_1E04(): pass

    label("Function_6_1E04")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1E15")
    Jump("loc_1ECB")

    label("loc_1E15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1ECB")
    TurnDirection(0xFE, 0x101, 0)

    NpcTalk(
        0xFE,
        "Leader Fisher",
        (
            "Master Lloyd, you're the\x01",
            "pride of our Fisherman's\x01",
            "Guild.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Leader Fisher",
        (
            "If the opportunity arises,\x01",
            "I'd really like to fish\x01",
            "with you in Liberl.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ECB")

    TalkEnd(0xFE)
    Return()

    # Function_6_1E04 end

    def Function_7_1ECF(): pass

    label("Function_7_1ECF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EEC")
    Call(0, 8)
    TalkEnd(0xFE)
    Return()

    label("loc_1EEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1F8A")

    ChrTalk(
        0xB,
        (
            "We know survival skills\x01",
            "and we also have\x01",
            "ENIGMAs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you get it, just go away\x01",
            "already, because you don't\x01",
            "need to worry about us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2048")

    label("loc_1F8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1F98")
    Jump("loc_2048")

    label("loc_1F98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2031")

    ChrTalk(
        0xB,
        (
            "Hmm. Anyhow, the\x01",
            "independence declaration\x01",
            "of invalidity, huh...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "The developments are\x01",
            "just getting more and\x01",
            "more troubling, huh.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2048")

    label("loc_2031")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_203F")
    Jump("loc_2048")

    label("loc_203F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2048")

    label("loc_2048")

    TalkEnd(0xFE)
    Return()

    # Function_7_1ECF end

    def Function_8_204C(): pass

    label("Function_8_204C")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2147")

    ChrTalk(
        0xB,
        (
            "The "Continental Alliance"\x01",
            "proposal and the civil war\x01",
            "in our native Erebonia...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "To think that the world\x01",
            "would've moved that much\x01",
            "in just about a month...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Yes... This is truly\x01",
            "what you call "a bolt\x01",
            "from the blue".\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_227C")

    label("loc_2147")


    ChrTalk(
        0xB,
        (
            "The "Continental Alliance"\x01",
            "proposal and the civil war\x01",
            "in our native Erebonia...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "To think that the world\x01",
            "would've moved that much\x01",
            "in just about a month...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "...Furthermore, after we\x01",
            "came here, the declaration\x01",
            "of invalidity came too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Yes... This is truly\x01",
            "what you call "a bolt\x01",
            "from the blue".\x02",
        )
    )

    CloseMessageWindow()

    label("loc_227C")

    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xB, 0x101, 500)
    Sleep(500)
    TurnDirection(0xC, 0x101, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2333")
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
            "[No Change]\x01",       # 0
            "[Defeated]\x01",        # 1
            "[Undefeated]\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2321")
    SetScenarioFlags(0x191, 1)
    Jump("loc_2333")

    label("loc_2321")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2333")
    ClearScenarioFlags(0x191, 1)

    label("loc_2333")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_2379")

    ChrTalk(
        0xB,
        (
            "Hmm, Lloyd Bannings of\x01",
            "the Fisherman's Guild,\x01",
            "huh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23B1")

    label("loc_2379")


    ChrTalk(
        0xB,
        (
            "Hmm, Lloyd Bannings of\x01",
            "the Fisherman's Guild,\x01",
            "huh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23B1")


    ChrTalk(
        0x101,
        (
            "#00005FYou're Mr. Lakelord of\x01",
            "the Imperial Fishing\x01",
            "Club... Why are you here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hmph, surely for fishing\x01",
            "training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "After all, I'm the club president...\x01",
            "I can't go back in shame after being\x01",
            "defeated like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FI-I see...\x02\x03",
            "#00001FHowever, you can't stay\x01",
            "here forever...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FYes, we'll escort you to\x01",
            "Armorica Village, so please\x01",
            "prepare to evacuate at once...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hmph, can't you leave us\x01",
            "be?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "An angler is normally used the dangers\x01",
            "of the out of doors, and there's no\x01",
            "need to worry about us starving either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Yeah, and if you say it's\x01",
            "dangerous, I think it'd be\x01",
            "the same anywhere we go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FB-But...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "At any rate, we also have ENIGMAs\x01",
            "and frankly, worrying about us is\x01",
            "none of your business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you get it, leave at\x01",
            "once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FR-Right...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_284F")
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "Ah...but since you've\x01",
            "come... I'll give you a\x01",
            "present.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We've fished a little\x01",
            "too much. We can't eat\x01",
            "all of them.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x168),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " x10 received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x168, 10)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0xB,
        (
            "Also, these were spit\x01",
            "out by the fish.\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x1FE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " received.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x1FE, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        "#00005FT-Thank you very much.\x02",
    )

    CloseMessageWindow()

    label("loc_284F")

    SetScenarioFlags(0x1BD, 2)
    SetScenarioFlags(0x0, 4)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    TurnDirection(0xB, 0xC, 0)
    TurnDirection(0xC, 0xB, 0)
    Return()

    # Function_8_204C end

    def Function_9_2876(): pass

    label("Function_9_2876")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2893")
    Call(0, 8)
    TalkEnd(0xFE)
    Return()

    label("loc_2893")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2900")

    ChrTalk(
        0xC,
        "...Are you finished?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "We're busy. I would\x01",
            "appreciate it if you\x01",
            "didn't bother us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29C6")

    label("loc_2900")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_290E")
    Jump("loc_29C6")

    label("loc_290E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_29AF")

    ChrTalk(
        0xC,
        (
            "No matter the distress, I\x01",
            "am prepared to get through\x01",
            "it with Sir Lakelord.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Rather, I prefer it like\x01",
            "this, alone, just the\x01",
            "two of us...㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29C6")

    label("loc_29AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_29BD")
    Jump("loc_29C6")

    label("loc_29BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_29C6")

    label("loc_29C6")

    TalkEnd(0xFE)
    Return()

    # Function_9_2876 end

    SaveToFile()

Try(main)
