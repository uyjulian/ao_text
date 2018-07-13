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
        "Function_4_4A5",          # 04, 4
        "Function_5_185D",         # 05, 5
        "Function_6_1E1C",         # 06, 6
        "Function_7_1EE0",         # 07, 7
        "Function_8_204F",         # 08, 8
        "Function_9_2880",         # 09, 9
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
            ""The Kingdom of Sweets Vol.2" is here.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_4A1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x12)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A1")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "You learned the "Smooth Almond Jelly"\x07\x00",
            " recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_4A1")

    TalkEnd(0xFF)
    Return()

    # Function_3_3E7 end

    def Function_4_4A5(): pass

    label("Function_4_4A5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_968")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "Ooh, member Lloyd.\x01",
            "You've finally come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FBranch Manager Celdan, this place...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yes, this building was originally\x01",
            "a renting boat shed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems it has been abandoned after\x01",
            "cessation of business, many, many years\x01",
            "ago, and so I could borrow it for cheap.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, it's the most suitable new branch\x01",
            "for us who're making a fresh start.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "More importantly, I'd like to explain to\x01",
            "member Lloyd too the "Angler Duels" \x01",
            "against the Fishing Emperor Club...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F"A-Angler Duels"...?\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00003FI see, "Angler Duels" against the five\x01",
            "members of the Fishing Emperor Club...\x02",
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
            "We plan to take care\x01",
            "of the matches in\x01",
            "some way, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If possible, I'd like to ask for\x01",
            "member Lloyd cooperation too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYes, I too don't want to\x01",
            "become unable to fish \x01",
            "in my favorite spots.\x02\x03",
            "#00000FI'll support you as much as I can.\x02",
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
            "You have become able to challenge the Fishing\x01",
            "Emperor Club members to the "Angler Duels".\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "You can hear from receptionist Sylum, who\x01",
            "is at the "East Street Fishing Emperor Club",\x01",
            "the detailed contents of the matches.\x07\x00\x02",
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

    label("loc_968")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A9E")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "Ooh, member Lloyd.\x01",
            "You've come immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As you can see, there's nothing,\x01",
            "but, please, make yourself at home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Also, since the supplies are scarce,\x01",
            "the prices are high and we also\x01",
            "prepared something for sale.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "If you want, please feel free to have a look.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15F, 7)

    label("loc_A9E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AA8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1859")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AFD")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_B12")

    label("loc_AFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B12")
    TurnDirection(0xFE, 0x0, 0)

    label("loc_B12")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B77")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 5)), scpexpr(EXPR_END)), "loc_B41")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_B3A")
    OP_AF(0x37)
    Jump("loc_B3C")

    label("loc_B3A")

    OP_AF(0x3B)

    label("loc_B3C")

    Jump("loc_B53")

    label("loc_B41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_B51")
    OP_AF(0x36)
    Jump("loc_B53")

    label("loc_B51")

    OP_AF(0x3A)

    label("loc_B53")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B72")
    TurnDirection(0xFE, 0x9, 0)

    label("loc_B72")

    Jump("loc_1854")

    label("loc_B77")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1854")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_C5A")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "The Angler Duels against \x01",
            "the Fishing Emperor Club...\x01",
            "I beg you to cooperate too, member Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "On these duels runs the future of\x01",
            "the Fisherman's Guild, to say the least.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1854")

    label("loc_C5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_C68")
    Jump("loc_1854")

    label("loc_C68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_118E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_D02")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "Hm, I haven't enough words\x01",
            "of thanks for Master Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "At this rate, I expect\x01",
            "new legends to be\x01",
            "born from now on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1189")

    label("loc_D02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D77")

    ChrTalk(
        0xFE,
        (
            "Hm, that person should be\x01",
            "coming in a little while...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "And then, for sure...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1189")

    label("loc_D77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x190, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10F8")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "Member Lloyd, those medals...\x01",
            "Impossible, did you defeat all the Elite Four?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes...I managed, somehow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Bwah ha ha, as expected from member Lloyd!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hm, if it's you, member Lloyd, I can\x01",
            "rest assure and entrust you with this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please, accept\x01",
            "our "soul"!!\x02",
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
        "#00005FT-This is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's the ultimate fishing bait we developed \x01",
            "and obtained while spitting blood for competing \x01",
            "against the Fishing Emperor Club.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's pricy since it uses Sepith as ingredient, but...\x01",
            "If you say the word, we can make as much as you like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FI see...a quartz made of\x01",
            "everyone's blood and sweat.\x02",
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
            "Please member Lloyd...\x01",
            "Use that to put Lakelord\x01",
            "down a peg or two!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If it's you, member Lloyd,\x01",
            "I'm sure you can do it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FY-Yes...I'll try!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x190, 5)
    Jump("loc_1189")

    label("loc_10F8")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "Member Lloyd... Put that\x01",
            "Lakelord down a peg or two\x01",
            "using our feelings too!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If it's you, member Lloyd,\x01",
            "I'm sure you can do it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1189")

    Jump("loc_1854")

    label("loc_118E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_119C")
    Jump("loc_1854")

    label("loc_119C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_11E4")

    ChrTalk(
        0xFE,
        (
            "Hmmm, at any rate, a final\x01",
            "weapon is a final weapon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1854")

    label("loc_11E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_11F2")
    Jump("loc_1854")

    label("loc_11F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_135D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12D1")

    ChrTalk(
        0xFE,
        "Damn, how many times will be the next one!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Triton, the "Silver Orca"...\x01",
            "That's really a frightening man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "No wonder he's the Elite Four head,\x01",
            "you can't compare him with the others.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1358")

    label("loc_12D1")


    ChrTalk(
        0xFE,
        (
            "Triton, the "Silver Orca"...\x01",
            "That's really a frightening man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Those hit streaks...\x01",
            "Can that guy see under the water surface?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1358")

    Jump("loc_1854")

    label("loc_135D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_13EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x17A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1375")
    Jump("loc_13E7")

    label("loc_1375")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "Member Lloyd, thank\x01",
            "you very much for today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Thanks to you, it seems\x01",
            "I'll sleep soundly tonight.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13E7")

    Jump("loc_1854")

    label("loc_13EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_15F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1541")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        "Member Lloyd, do you know?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It seems that if you defeat the\x01",
            "Fishing Emperor Club, you can\x01",
            "have some kind of bizarre title.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Incidentally, I beat that\x01",
            "Narses guy yesterday.\x01",
            "I earned the "Crazy Wave Hunter" title.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Bwah ha ha, although it's an enemy idea,\x01",
            "I'll slightly look forward to this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15EB")

    label("loc_1541")


    ChrTalk(
        0xFE,
        (
            "Yesterday I beat that\x01",
            "Narses guy, you see.\x01",
            "I earned the "Crazy Wave Hunter" title.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Bwah ha ha, although it's an enemy idea,\x01",
            "I'll slightly look forward to this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15EB")

    Jump("loc_1854")

    label("loc_15F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_17AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_170F")

    ChrTalk(
        0xFE,
        (
            "Anyway, I wonder how long has \x01",
            "it been since I've tackled fishing\x01",
            "with such feelings.\x02",
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
            "How to say it, it's troublesome\x01",
            "but I'm strangely excited.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17A6")

    label("loc_170F")


    ChrTalk(
        0xFE,
        (
            "Hm, I wonder how long has \x01",
            "it been since I've tackled\x01",
            "fishing with such feelings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "How to say it, it's troublesome\x01",
            "but I'm strangely excited.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17A6")

    Jump("loc_1854")

    label("loc_17AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_183D")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "In any case, the Fisherman's\x01",
            "Guild - Crossbell Branch\x01",
            "starts anew from here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Member Lloyd, let's\x01",
            "both do our best.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1854")

    label("loc_183D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_184B")
    Jump("loc_1854")

    label("loc_184B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1854")

    label("loc_1854")

    Jump("loc_AA8")

    label("loc_1859")

    TalkEnd(0xFE)
    Return()

    # Function_4_4A5 end

    def Function_5_185D(): pass

    label("Function_5_185D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C61")
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x344, 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x345, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x346, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x347, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1891")
    Jump("loc_1C61")

    label("loc_1891")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x344, 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x345, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x346, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x347, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1C61")
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
            "#00003FYes, it's a part of a fishing\x01",
            "gear without a doubt...\x01",
            "It's very beautiful.\x02\x03",
            "#00000FI caught a rare fish from a fishing spot\x01",
            "I recovered from the Elite Fours...\x01",
            "It was that fish that spat it out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "...No doubt. \x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That's a part of the legendary gear that was\x01",
            "used by a wandering remarkable angler, once.\x02",
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
            "To think it was\x01",
            "found like that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FI-Is it such an\x01",
            "amazing thing...?\x02\x03",
            "#00003FThen, what do we do?\x01",
            "We should give it back to that person...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "No, there is no need for that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Because that person said that who\x01",
            "finds that fishing gear, can use it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Lloyd, there are\x01",
            "4 parts in total.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "When you have obtained all of them,\x01",
            "please come to my place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I should be able to\x01",
            "put those parts together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FI-I see...\x01",
            "I understand, I'll keep it in mind.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x8, 0)
    SetScenarioFlags(0x0, 3)
    SetScenarioFlags(0x1C0, 1)
    TalkEnd(0xFE)
    Return()

    label("loc_1C61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1CFA")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(
        0xFE,
        (
            "To think that the once sealed legendary\x01",
            "fishing gear would appear at such a time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hm, Lloyd.\x01",
            "Could this be fate?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x8, 0)
    Jump("loc_1E18")

    label("loc_1CFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1D08")
    Jump("loc_1E18")

    label("loc_1D08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1D16")
    Jump("loc_1E18")

    label("loc_1D16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1D24")
    Jump("loc_1E18")

    label("loc_1D24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1DAD")

    ChrTalk(
        0xFE,
        (
            "Coppen too seems\x01",
            "to have hit a wall...\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "As I thought, with our abilities only,\x01",
            "we can't do any more than this...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E18")

    label("loc_1DAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1DBB")
    Jump("loc_1E18")

    label("loc_1DBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1DC9")
    Jump("loc_1E18")

    label("loc_1DC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1DD7")
    Jump("loc_1E18")

    label("loc_1DD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1DE5")
    Jump("loc_1E18")

    label("loc_1DE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1DF3")
    Jump("loc_1E18")

    label("loc_1DF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1E01")
    Jump("loc_1E18")

    label("loc_1E01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1E0F")
    Jump("loc_1E18")

    label("loc_1E0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1E18")

    label("loc_1E18")

    TalkEnd(0xFE)
    Return()

    # Function_5_185D end

    def Function_6_1E1C(): pass

    label("Function_6_1E1C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1E2D")
    Jump("loc_1EDC")

    label("loc_1E2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1EDC")
    TurnDirection(0xFE, 0x101, 0)

    NpcTalk(
        0xFE,
        "Leader Fisher",
        (
            "Master Lloyd, you're our\x01",
            "Fisherman's Guild pride.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0xFE,
        "Leader Fisher",
        (
            "If the opportunity arises, I'd really\x01",
            "like to fish with you in Liberl.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EDC")

    TalkEnd(0xFE)
    Return()

    # Function_6_1E1C end

    def Function_7_1EE0(): pass

    label("Function_7_1EE0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EFD")
    Call(0, 8)
    TalkEnd(0xFE)
    Return()

    label("loc_1EFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1F97")

    ChrTalk(
        0xB,
        (
            "We know survival skills\x01",
            "and we also have ENIGMAs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "If you get it, just go away already,\x01",
            "because you don't need to be worried.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_204B")

    label("loc_1F97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1FA5")
    Jump("loc_204B")

    label("loc_1FA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2034")

    ChrTalk(
        0xB,
        (
            "Hm, at any rate, the independence\x01",
            "declaration of invalidity, eh...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "A development that brought\x01",
            "more and more troubles.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_204B")

    label("loc_2034")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_2042")
    Jump("loc_204B")

    label("loc_2042")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_204B")

    label("loc_204B")

    TalkEnd(0xFE)
    Return()

    # Function_7_1EE0 end

    def Function_8_204F(): pass

    label("Function_8_204F")

    OP_4B(0xB, 0xFF)
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2148")

    ChrTalk(
        0xB,
        (
            "The "Continental Alliance" proposal\x01",
            "and the civil war in our native Erebonia...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "To think that the world would've\x01",
            "moved that much in about a month...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Yes... This is truly what is\x01",
            "called "a bolt out of the blue".\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2288")

    label("loc_2148")


    ChrTalk(
        0xB,
        (
            "The "Continental Alliance" proposal\x01",
            "and the civil war in our native Erebonia...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "To think that the world would've\x01",
            "moved that much in about a month...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "...Furthermore, after we came here, the\x01",
            "independence declaration of invalidity came too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Yes... This is truly what is\x01",
            "called "a bolt out of the blue".\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2288")

    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xB, 0x101, 500)
    Sleep(500)
    TurnDirection(0xC, 0x101, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_233F")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_232D")
    SetScenarioFlags(0x191, 1)
    Jump("loc_233F")

    label("loc_232D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_233F")
    ClearScenarioFlags(0x191, 1)

    label("loc_233F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_2386")

    ChrTalk(
        0xB,
        (
            "Hm, you're Lloyd Bannings\x01",
            "of the Fisherman's Guild?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23C2")

    label("loc_2386")


    ChrTalk(
        0xB,
        (
            "Hm, so you're Lloyd Bannings\x01",
            "of the Fisherman's Guild?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23C2")


    ChrTalk(
        0x101,
        (
            "#00005FYou're Mr. Lakelord of the\x01",
            "Fishing Emperor Club...\x01",
            "Why are you here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Hmph, surely for\x01",
            "fishing training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "After all, I'm the club president...\x01",
            "I can't go back in shame after\x01",
            "having been defeated like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FI-I see...\x02\x03",
            "#00001FHowever, you can't\x01",
            "stay here all the time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FYes, we will escort you to\x01",
            "Armorica Village, so please\x01",
            "prepare to evacuate at once...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hmph, can you not\x01",
            "leave us be?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "An angler is normally used\x01",
            "to outside dangers, there is\x01",
            "even no need to worry for starving.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Yeah, also if you say it's dangerous, I think \x01",
            "it would be the same everywhere we go.\x02",
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
            "At any rate, we have ENIGMAs too and\x01",
            "frankly, worrying is none of your business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "If you get it, go away at once.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FR-Right...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_2859")
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xB,
        (
            "Ah...but since you've come...\x01",
            "I'll give you a present.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "We've fished a little too much.\x01",
            "We only can't eat them all.\x02",
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

    label("loc_2859")

    SetScenarioFlags(0x1BD, 2)
    SetScenarioFlags(0x0, 4)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)
    OP_4C(0xB, 0xFF)
    OP_4C(0xC, 0xFF)
    TurnDirection(0xB, 0xC, 0)
    TurnDirection(0xC, 0xB, 0)
    Return()

    # Function_8_204F end

    def Function_9_2880(): pass

    label("Function_9_2880")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_289D")
    Call(0, 8)
    TalkEnd(0xFE)
    Return()

    label("loc_289D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2922")

    ChrTalk(
        0xC,
        "...Did you not talk enough?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "We too are busy with many things.\x01",
            "I would be glad if you did not bother us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29DA")

    label("loc_2922")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2930")
    Jump("loc_29DA")

    label("loc_2930")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_29C3")

    ChrTalk(
        0xC,
        (
            "No matter which distress,\x01",
            "I am prepared to get over\x01",
            "it with Sir Lakelord.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Rather, I prefer this,\x01",
            "the two of us, alone...㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29DA")

    label("loc_29C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_29D1")
    Jump("loc_29DA")

    label("loc_29D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_29DA")

    label("loc_29DA")

    TalkEnd(0xFE)
    Return()

    # Function_9_2880 end

    SaveToFile()

Try(main)
