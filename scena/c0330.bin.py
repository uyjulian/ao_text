from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0330.bin",                # FileName
        "c0330",                    # MapName
        "c0330",                    # Location
        0x002C,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 44, 0, 3, 0, 4],
    )

    BuildStringList((
        "c0330",                  # 0
        "Harold",                 # 1
        "Sophia",                 # 2
        "Colin",                  # 3
        "Cindy",                  # 4
        "Village Chief Tolta",    # 5
        "Lawyer Ian",             # 6
    ))

    AddCharChip((
        "chr/ch09300.itc",                   # 00
        "chr/ch09302.itc",                   # 01
        "chr/ch09400.itc",                   # 02
        "chr/ch09402.itc",                   # 03
        "chr/ch07200.itc",                   # 04
        "chr/ch07202.itc",                   # 05
        "chr/ch22100.itc",                   # 06
        "chr/ch24000.itc",                   # 07
        "chr/ch05900.itc",                   # 08
    ))

    DeclNpc(4294966956, 0,       4409,    315,  261,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(550,     0,       2039,    180,  261,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(37479,   0,       3799,    180,  261,  0x0, 0,   4,   0,   0,   1,   0,   9,   255,  0)
    DeclNpc(4294966806, 0,       5139,    180,  389,  0x0, 0,   6,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(9,       0,       4294967066, 0,    389,  0x0, 0,   7,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(660,     0,       4599,    270,  453,  0x0, 0,   8,   0,   0,   0,   0,   13,  255,  0)

    DeclActor(34620,   0,       7280,    1200,    34620,   1750,    7280,    0x007C, 0,  5,  0x0000)

    ChipFrameInfo(464, 0)                                        # 0

    ScpFunction((
        "Function_0_1D0",          # 00, 0
        "Function_1_288",          # 01, 1
        "Function_2_2B3",          # 02, 2
        "Function_3_2DE",          # 03, 3
        "Function_4_7C5",          # 04, 4
        "Function_5_846",          # 05, 5
        "Function_6_8FE",          # 06, 6
        "Function_7_17A6",         # 07, 7
        "Function_8_2A19",         # 08, 8
        "Function_9_2B03",         # 09, 9
        "Function_10_348B",        # 0A, 10
        "Function_11_3562",        # 0B, 11
        "Function_12_3693",        # 0C, 12
        "Function_13_3923",        # 0D, 13
        "Function_14_3B6B",        # 0E, 14
        "Function_15_42D4",        # 0F, 15
        "Function_16_4632",        # 10, 16
        "Function_17_476E",        # 11, 17
        "Function_18_58BF",        # 12, 18
    ))


    def Function_0_1D0(): pass

    label("Function_0_1D0")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_210"),
        (1, "loc_21C"),
        (2, "loc_228"),
        (3, "loc_234"),
        (4, "loc_240"),
        (5, "loc_24C"),
        (6, "loc_258"),
        (SWITCH_DEFAULT, "loc_264"),
    )


    label("loc_210")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_270")

    label("loc_21C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_270")

    label("loc_228")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_270")

    label("loc_234")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_270")

    label("loc_240")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_270")

    label("loc_24C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_270")

    label("loc_258")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_270")

    label("loc_264")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_270")

    label("loc_270")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_287")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_270")

    label("loc_287")

    Return()

    # Function_0_1D0 end

    def Function_1_288(): pass

    label("Function_1_288")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2B2")
    OP_94(0xFE, 0x9268, 0x157C, 0x8F48, 0x85C, 0x3E8)
    Sleep(300)
    Jump("Function_1_288")

    label("loc_2B2")

    Return()

    # Function_1_288 end

    def Function_2_2B3(): pass

    label("Function_2_2B3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2DD")
    OP_94(0xFE, 0xFFFFF240, 0x80C, 0xC58, 0x139C, 0x3E8)
    Sleep(300)
    Jump("Function_2_2B3")

    label("loc_2DD")

    Return()

    # Function_2_2B3 end

    def Function_3_2DE(): pass

    label("Function_3_2DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_325")
    SetChrPos(0x8, -1780, 0, 4730, 180)
    SetChrPos(0x9, 40940, 0, -550, 180)
    SetChrPos(0xA, 40930, 0, -1640, 90)
    BeginChrThread(0xA, 0, 0, 0)
    Jump("loc_7C4")

    label("loc_325")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_342")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_7C4")

    label("loc_342")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_37D")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0xA, -1000, 0, 3850, 90)
    SetChrPos(0x9, 670, 0, 3900, 270)
    BeginChrThread(0xA, 0, 0, 0)
    Jump("loc_7C4")

    label("loc_37D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_390")
    SetChrFlags(0x8, 0x80)
    Jump("loc_7C4")

    label("loc_390")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3C0")
    SetChrPos(0x8, -490, 0, 5140, 180)
    SetChrPos(0x9, -690, 0, 3590, 0)
    Jump("loc_7C4")

    label("loc_3C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3EA")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0xA, 38280, 0, 11000, 0)
    BeginChrThread(0xA, 0, 0, 0)
    Jump("loc_7C4")

    label("loc_3EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_414")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0xA, -1670, 0, 3900, 45)
    BeginChrThread(0xA, 0, 0, 2)
    Jump("loc_7C4")

    label("loc_414")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_58B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_485")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -690, 0, 3590, 0)
    SetChrPos(0x8, -490, 0, 5140, 180)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0x8, 0x10)
    SetChrPos(0x9, 37670, 0, 3210, 180)
    SetChrPos(0xA, 37670, 0, 1940, 0)
    BeginChrThread(0xA, 0, 0, 0)
    Jump("loc_586")

    label("loc_485")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_507")
    SetChrPos(0xC, -690, 0, 3590, 0)
    SetChrPos(0x8, -490, 0, 5140, 180)
    SetChrPos(0xD, 660, 0, 4600, 270)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xA, 41130, 0, 1090, 90)
    BeginChrThread(0xA, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_502")
    SetChrFlags(0xA, 0x10)

    label("loc_502")

    Jump("loc_586")

    label("loc_507")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_545")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0xA, 32700, 500, 9220, 270)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrChipByIndex(0xA, 0x5)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    Jump("loc_586")

    label("loc_545")

    SetChrFlags(0x8, 0x80)
    SetChrPos(0xA, 41130, 0, 1090, 90)
    BeginChrThread(0xA, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_570")
    SetChrFlags(0xA, 0x10)

    label("loc_570")

    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -10, 0, 5370, 270)

    label("loc_586")

    Jump("loc_7C4")

    label("loc_58B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_59E")
    SetChrFlags(0x8, 0x80)
    Jump("loc_7C4")

    label("loc_59E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_613")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, 40930, 0, -1640, 90)
    SetChrPos(0xA, -690, 0, 3590, 0)
    BeginChrThread(0xA, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E3")
    SetChrFlags(0xA, 0x10)

    label("loc_5E3")

    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -490, 0, 5140, 180)
    BeginChrThread(0xB, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60E")
    SetChrFlags(0xB, 0x10)

    label("loc_60E")

    Jump("loc_7C4")

    label("loc_613")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_66B")
    SetChrPos(0x8, 1940, 200, 6910, 270)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x9, 40940, 0, -550, 180)
    SetChrPos(0xA, 40930, 0, -1640, 90)
    BeginChrThread(0xA, 0, 0, 0)
    Jump("loc_7C4")

    label("loc_66B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_6C4")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, -490, 0, 5140, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_699")
    SetChrFlags(0x9, 0x10)

    label("loc_699")

    SetChrPos(0xA, -690, 0, 3590, 0)
    BeginChrThread(0xA, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6BF")
    SetChrFlags(0xA, 0x10)

    label("loc_6BF")

    Jump("loc_7C4")

    label("loc_6C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_6D7")
    SetChrFlags(0x8, 0x80)
    Jump("loc_7C4")

    label("loc_6D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_74F")
    SetChrPos(0x8, -820, 200, 10200, 180)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0x9, 40930, 0, -1640, 90)
    SetChrPos(0xA, 34300, 0, 1140, 315)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 38720, 0, 510, 270)
    SetChrFlags(0xB, 0x10)
    Jump("loc_7C4")

    label("loc_74F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_7C4")
    SetChrPos(0x8, -820, 200, 10200, 180)
    SetChrPos(0x9, 1940, 200, 8290, 270)
    SetChrPos(0xA, 1940, 200, 6910, 270)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrChipByIndex(0x9, 0x3)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrChipByIndex(0xA, 0x5)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)

    label("loc_7C4")

    Return()

    # Function_3_2DE end

    def Function_4_7C5(): pass

    label("Function_4_7C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_80A")
    SetMapObjFrame(0xFF, "light01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "model05_light", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_80A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_845")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "light01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "model05_light", 0x0, 0x1)

    label("loc_845")

    Return()

    # Function_4_7C5 end

    def Function_5_846(): pass

    label("Function_5_846")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "There is a car magazine, "Monthly Car Mania Vol.1".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x36C, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8FA")
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "You learned the\x01\x07\x02",
            ""Sky Coloring"\x07\x00",
            " paint pattern.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0x36C, 1)

    label("loc_8FA")

    TalkEnd(0xFF)
    Return()

    # Function_5_846 end

    def Function_6_8FE(): pass

    label("Function_6_8FE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_D32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BCE")

    ChrTalk(
        0x8,
        (
            "#03600FOh, everyone. Thank\x01",
            "goodness you're safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FMr. Harold. You're back\x01",
            "from Armorica Village?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03604FYes. I just got back after seeing\x01",
            "that the barrier had disappeared.\x02\x03",
            "#03600FAlthough I'm about\x01",
            "to leave immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203FLooks like you are busy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FYou also have a family,\x01",
            "so shouldn't you take it\x01",
            "easy for a while longer?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03603FNo. Right now, I want\x01",
            "to help everyone all\x01",
            "across Crossbell.\x02\x03",
            "#03600FTo start, I'm planning\x01",
            "on going to Mainz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FI see... That's very\x01",
            "like you, I suppose.\x02\x03",
            "#00002FPlease take care as you make your way there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03609FYes. And the same goes for all of you...\x01",
            "May the Goddess grant you her protection.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CD, 0)
    Jump("loc_D2D")

    label("loc_BCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CA7")

    ChrTalk(
        0x8,
        (
            "#03600FTo start, I'm planning\x01",
            "on going to Mainz.\x02\x03",
            "#03603FRight now, I want to help\x01",
            "everyone all across Crossbell.\x02\x03",
            "#03609FPlease be careful, everyone. \x01",
            "May the Goddess grant you her protection.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D2D")

    label("loc_CA7")


    ChrTalk(
        0x8,
        (
            "#03600FTo start, I'm planning\x01",
            "on going to Mainz.\x02\x03",
            "#03609FPlease be careful, everyone. \x01",
            "May the Goddess grant you her protection.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D2D")

    Jump("loc_17A2")

    label("loc_D32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_D40")
    Jump("loc_17A2")

    label("loc_D40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_D4E")
    Jump("loc_17A2")

    label("loc_D4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_D5C")
    Jump("loc_17A2")

    label("loc_D5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_F3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E7F")

    ChrTalk(
        0x8,
        (
            "#03601FI planned to go to Mainz\x01",
            "today, but... I can't\x01",
            "believe this has happened.\x02\x03",
            "#03603F...I've gone to Mainz many times\x01",
            "for trade deals, and the people\x01",
            "there are very good to me.\x02\x03",
            "#03608FBut even so, it's pathetic that I\x01",
            "can't do a single thing for them...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F35")

    label("loc_E7F")


    ChrTalk(
        0x8,
        (
            "#03603F...I've gone to Mainz many times\x01",
            "for trade deals, and the people\x01",
            "there are very good to me.\x02\x03",
            "#03608FBut even so, it's pathetic that I\x01",
            "can't do a single thing for them...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F35")

    Jump("loc_17A2")

    label("loc_F3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_F48")
    Jump("loc_17A2")

    label("loc_F48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_F56")
    Jump("loc_17A2")

    label("loc_F56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_10A9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1012")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F7D")
    Call(0, 15)
    Jump("loc_100D")

    label("loc_F7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F8F")
    Call(0, 18)
    Jump("loc_100D")

    label("loc_F8F")


    ChrTalk(
        0x8,
        (
            "#03600FI'll be taking the Village Chief and Mr. Grimwood\x01",
            "back to Armorica in my car later.\x02\x03",
            "Everyone, please\x01",
            "be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_100D")

    Jump("loc_10A4")

    label("loc_1012")


    ChrTalk(
        0x8,
        (
            "#03601FAnyway, I'll try to settle\x01",
            "what I learned in\x01",
            "yesterday's investigation.\x02\x03",
            "#03603FAnd, it might be\x01",
            "good to speak with\x01",
            "Lawyer Ian later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10A4")

    Jump("loc_17A2")

    label("loc_10A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_10B7")
    Jump("loc_17A2")

    label("loc_10B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_10C5")
    Jump("loc_17A2")

    label("loc_10C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_1298")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_121A")

    ChrTalk(
        0x8,
        "#03605FOh, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FGood evening, Mr. Harold.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FA nice smell is coming from the second floor...\x01",
            "It seems your wife is preparing dinner.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03609FYes, you're right.\x01",
            "Also, it seems that today\x01",
            "Colin is helping her too.\x02\x03",
            "#03604FMan, I've just returned\x01",
            "from a place and I'm\x01",
            "very hungry.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14A, 6)
    Jump("loc_1293")

    label("loc_121A")


    ChrTalk(
        0x8,
        (
            "#03600FIt seems that today\x01",
            "Colin is helping too.\x01\x02\x03",
            "#03609FUh uh, I can't wait to see\x01",
            "what dishes I'm going to have.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1293")

    Jump("loc_17A2")

    label("loc_1298")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_12A6")
    Jump("loc_17A2")

    label("loc_12A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_12B4")
    Jump("loc_17A2")

    label("loc_12B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_15A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_151E")

    ChrTalk(
        0x8,
        (
            "#03603FPassing time alone\x01",
            "like this, I suddenly\x01",
            "think about things...\x02\x03",
            "That violet-haired girl\x01",
            "who saved Colin before...\x02\x03",
            "#03608FI wonder if it's really impossible\x01",
            "to meet her. Things like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FW-Well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03604FHa ha. For now I don't\x01",
            "have any clues. It's just\x01",
            "a simple hope of mine.\x02\x03",
            "#03600FIf there ever is a chance... I would\x01",
            "like to offer my thanks to that girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F(A violet-haired girl... \x01",
            "Renne returned to Liberl with\x01",
            "Estelle and Joshua, right...?)\x02\x03",
            "#00003F(That girl needs to sort our her\x01",
            "feelings too, but... I'm sure\x01",
            "that day will eventually come.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x134, 0)
    Jump("loc_15A3")

    label("loc_151E")


    ChrTalk(
        0x8,
        (
            "#03603FThat violet-haired girl\x01",
            "who saved Colin before...\x02\x03",
            "#03600FIf I ever do get to meet her,\x01",
            "I would like to offer my thanks.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15A3")

    Jump("loc_17A2")

    label("loc_15A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_17A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15C7")
    TalkEnd(0xFE)
    Call(0, 14)
    Return()

    label("loc_15C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_172F")

    ChrTalk(
        0x8,
        (
            "#03600FMy trade business has\x01",
            "been doing well lately.\x02\x03",
            "#03604FBecause of that, I have\x01",
            "some time to spend\x01",
            "vacationing with my family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F*giggle*, it looks like your continued\x01",
            "efforts are bearing fruit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03609FHa ha... To be honest, it\x01",
            "gives me an uneasy feeling.\x02\x03",
            "#03600FTo me, just providing for\x01",
            "my family would be enough.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17A2")

    label("loc_172F")


    ChrTalk(
        0x8,
        (
            "#03600FEveryone, please let me know\x01",
            "if you ever need anything.\x02\x03",
            "I will do anything in\x01",
            "my power to assist you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17A2")

    TalkEnd(0xFE)
    Return()

    # Function_6_8FE end

    def Function_7_17A6(): pass

    label("Function_7_17A6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1953")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18A7")

    ChrTalk(
        0x9,
        (
            "#03708FIf we just take it easy\x01",
            "awhile longer, I thought...\x02\x03",
            "#03700FKind, considerate and skillful. That\x01",
            "is the man that is Harold Hayworth.\x02\x03",
            "#03709FIf my husband says he wants to help\x01",
            "people, all we can do is support him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_194E")

    label("loc_18A7")


    ChrTalk(
        0x9,
        (
            "#03700FKind, considerate and skillful. That\x01",
            "is the man that is Harold Hayworth.\x02\x03",
            "#03709FIf my husband says he wants to help\x01",
            "people, all we can do is support him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_194E")

    Jump("loc_2A15")

    label("loc_1953")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1961")
    Jump("loc_2A15")

    label("loc_1961")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_19FF")

    ChrTalk(
        0x9,
        (
            "#03708FI wonder what's going\x01",
            "to happen now...\x02\x03",
            "#03710FIf anything happened to Colin or my husband...\x01",
            "Anyway, that's all I'm worried about.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A15")

    label("loc_19FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1BB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B02")

    ChrTalk(
        0x9,
        (
            "#03700FMy husband is going to check on\x01",
            "the situation in Mainz today.\x02\x03",
            "He said because of yesterday's\x01",
            "attack, he wants to do all he\x01",
            "can for the people of Mainz...\x02\x03",
            "#03709FI feel proud of my compassionate\x01",
            "husband all over again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1BAB")

    label("loc_1B02")


    ChrTalk(
        0x9,
        (
            "#03700FHe said because of yesterday's\x01",
            "attack, he wants to do all he\x01",
            "can for the people of Mainz...\x02\x03",
            "#03709FI feel proud of my compassionate\x01",
            "husband all over again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BAB")

    Jump("loc_2A15")

    label("loc_1BB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1CE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C87")

    ChrTalk(
        0x9,
        (
            "#03708FHearing news of the attack,\x01",
            "I immediately thought, "I'm glad\x01",
            "my husband wasn't involved."\x02\x03",
            "Although at this moment,\x01",
            "I fear for the people\x01",
            "of Mainz...\x02\x03",
            "#03710F...I hate myself.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1CDB")

    label("loc_1C87")


    ChrTalk(
        0x9,
        (
            "#03708F...Anyway, I pray to the\x01",
            "Goddess that the incident\x01",
            "is resolved quickly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CDB")

    Jump("loc_2A15")

    label("loc_1CE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1DA5")

    ChrTalk(
        0x9,
        (
            "#03700FMy husband's going to Bellguard\x01",
            "Gate for a delivery today.\x02\x03",
            "#03708FHowever, a giant monster was spotted\x01",
            "on West Crossbell Highway just\x01",
            "yesterday, so I'm a little worried.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A15")

    label("loc_1DA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2032")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F01")

    ChrTalk(
        0x9,
        (
            "#03705FOh, everyone?\x02\x03",
            "If you're looking for my husband,\x01",
            "he went to Armorica Village to\x01",
            "discuss something with the chief...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(We should have followed through on that\x01",
            "investigation, but... Right now, checking\x01",
            "on that accident is our top priority.)\x02\x03",
            "(Let's leave Armorica\x01",
            "Village to Mr. Harold.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16C, 7)
    Jump("loc_202D")

    label("loc_1F01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FBF")

    ChrTalk(
        0x9,
        (
            "#03700FCindy came just some time\x01",
            "ago and she told me that...\x02\x03",
            "It seems a lot of ambulances\x01",
            "passed through West Street.\x02\x03",
            "#03708FI'm getting a bad feeling about this...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_202D")

    label("loc_1FBF")


    ChrTalk(
        0x9,
        (
            "#03708FIt seems a lot of ambulances\x01",
            "passed through West Street.\x02\x03",
            "I'm getting a bad feeling about this...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_202D")

    Jump("loc_2A15")

    label("loc_2032")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2393")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2193")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2102")

    ChrTalk(
        0x9,
        (
            "#03700FMy husband just contacted me.\x01",
            "He says the incident in Armorica\x01",
            "Village was resolved safely.\x02\x03",
            "#03708FBut even so, a swindler...\x01",
            "He must be a very bad person.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_218E")

    label("loc_2102")


    ChrTalk(
        0x9,
        (
            "#03700FIt seems the incident in Armorica\x01",
            "Village was resolved safely.\x02\x03",
            "#03708FBut even so, a swindler...\x01",
            "He must be a very bad person.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_218E")

    Jump("loc_238E")

    label("loc_2193")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2226")

    ChrTalk(
        0x9,
        (
            "#03700FIt seems the village\x01",
            "chief's son got involved in\x01",
            "something troublesome...\x02\x03",
            "#03708FI hope it's resolved\x01",
            "quickly, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_238E")

    label("loc_2226")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2305")

    ChrTalk(
        0x9,
        (
            "#03700FIt seems the village\x01",
            "chief worries too much...\x02\x03",
            "#03708FBut, it is his son, so I suppose\x01",
            "that's only natural..\x02\x03",
            "#03700FWorrying too much is bad for your health. \x01",
            "For now, he's got to calm down.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_238E")

    label("loc_2305")


    ChrTalk(
        0x9,
        (
            "#03700FWorrying too much is bad for your health. \x01",
            "For now, he's got to calm down.\x02\x03",
            "I think I had some calming\x01",
            "herb tea somewhere...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_238E")

    Jump("loc_2A15")

    label("loc_2393")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2464")

    ChrTalk(
        0x9,
        (
            "#03700FMy husband was contacted by\x01",
            "the chief of Armorica Village.\x02\x03",
            "It seems he wanted to discuss something...\x01",
            "It didn't seem like a business negotiation\x01",
            "either. I wonder what it could be...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A15")

    label("loc_2464")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_25BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2537")

    ChrTalk(
        0x9,
        (
            "#03700FI made curry with Colin\x01",
            "last night, but...\x02\x03",
            "I might have made a little too much. \x01",
            "There are a lot of leftovers.\x02\x03",
            "#03709FUh uh, it'll be awhile before\x01",
            "the next curry night.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_25B5")

    label("loc_2537")


    ChrTalk(
        0x9,
        (
            "#03700FI might have made a little\x01",
            "too much curry last night.\x02\x03",
            "#03709FUh uh, it'll be awhile before\x01",
            "the next curry night.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25B5")

    Jump("loc_2A15")

    label("loc_25BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_2642")

    ChrTalk(
        0x9,
        (
            "#03700FAlright, we only need to wait to simmer.\x02\x03",
            "#03709FUh uh, you did well, Colin.\x01",
            "Papa will be delighted for sure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A15")

    label("loc_2642")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_26B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_265D")
    Call(0, 8)
    Jump("loc_26AB")

    label("loc_265D")


    ChrTalk(
        0x9,
        (
            "#03700FI was just about\x01",
            "to go shopping.\x02\x03",
            "#03709FUh uh. \x01",
            "Colin's excited.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26AB")

    Jump("loc_2A15")

    label("loc_26B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_281A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_278B")

    ChrTalk(
        0x9,
        (
            "#03700FMrs. Creil, who lived in the neighborhood,\x01",
            "came to visit me the other day.\x02\x03",
            "It looks like she's finally getting\x01",
            "settled in. She looked relieved...\x02\x03",
            "#03709FUh uh, I'm relieved too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2815")

    label("loc_278B")


    ChrTalk(
        0x9,
        (
            "#03700FIt seems Mrs. Creil and\x01",
            "her family now live in an\x01",
            "apartment on East Street.\x02\x03",
            "It looks like they're\x01",
            "doing ok. That's a relief.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2815")

    Jump("loc_2A15")

    label("loc_281A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2992")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2905")

    ChrTalk(
        0x9,
        (
            "#03700FMr. Bond's family... They used to\x01",
            "live here, but they moved recently.\x02\x03",
            "#03708FThey came to say goodbye when\x01",
            "they left, but I haven't\x01",
            "heard from them since.\x02\x03",
            "I hope they're doing all right, but...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_298D")

    label("loc_2905")


    ChrTalk(
        0x9,
        (
            "#03700FMr. Bond's wife, Mrs. Creil, \x01",
            "often went shopping with me\x01",
            "and we were very close...\x02\x03",
            "#03708FI hope she's doing all right...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_298D")

    Jump("loc_2A15")

    label("loc_2992")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2A15")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29B1")
    TalkEnd(0xFE)
    Call(0, 14)
    Return()

    label("loc_29B1")


    ChrTalk(
        0x9,
        (
            "#03700FYou all did really \x01",
            "a lot for us before.\x02\x03",
            "My husband and I hope\x01",
            "you will help us again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A15")

    TalkEnd(0xFE)
    Return()

    # Function_7_17A6 end

    def Function_8_2A19(): pass

    label("Function_8_2A19")

    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0x9,
        (
            "#03700FCome now, Colin. I wonder what\x01",
            "we're going to buy today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#03805FUmm, umm...\x01",
            "Carrots, potatoes,\x01",
            "onions...\x02\x03",
            "#03809F...and curry roux!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03709FUh uh, right answer.\x01",
            "Shall we go, then?\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_8_2A19 end

    def Function_9_2B03(): pass

    label("Function_9_2B03")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2C25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BB2")

    ChrTalk(
        0xA,
        (
            "#03800FMama made a lunchbox for papa\x01",
            "to take on his trip for work.\x02\x03",
            "#03809FCamille's mom gave us\x01",
            "a lot of veggies. \x01",
            "Ehehe, looks delicious.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2C20")

    label("loc_2BB2")


    ChrTalk(
        0xA,
        (
            "#03800FI want to go to Armorica Village again.\x02\x03",
            "#03809FI promised to play with\x01",
            "Camille and Pooley again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C20")

    Jump("loc_3487")

    label("loc_2C25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2C33")
    Jump("loc_3487")

    label("loc_2C33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2CBE")

    ChrTalk(
        0xA,
        (
            "#03805FLooks like papa and mama are\x01",
            "worried about something.\x02\x03",
            "Although we're going to have fun,\x01",
            "I wonder what happened?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3487")

    label("loc_2CBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2DC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D58")

    ChrTalk(
        0xA,
        (
            "#03800FThis time, I'm\x01",
            "going with papa\x01",
            "and mama to play.\x02\x03",
            "#03809FThey said it's a really nice place. \x01",
            "Ehehe, I can't wait.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2DBD")

    label("loc_2D58")


    ChrTalk(
        0xA,
        (
            "#03800FThis time, I'm going to a\x01",
            "really nice place to play.\x02\x03",
            "#03809FSo excited... I can't wait.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DBD")

    Jump("loc_3487")

    label("loc_2DC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2E41")

    ChrTalk(
        0xA,
        (
            "#03800FPapa said he has work\x01",
            "today, but it looks like\x01",
            "he hasn't left yet.\x02\x03",
            "#3802FMaybe he's\x01",
            "taking a break?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3487")

    label("loc_2E41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2EB2")

    ChrTalk(
        0xA,
        (
            "#03802FLook at that! There's a\x01",
            "frog stuck to the window.\x02\x03",
            "#03809FIt's creepy but cute, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3487")

    label("loc_2EB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2F1D")

    ChrTalk(
        0xA,
        (
            "#03802FSis Cindy gave me\x01",
            "one of her cookies\x01",
            "just now.\x02\x03",
            "#03809FIt was crunchy and yummy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3487")

    label("loc_2F1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_30D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FB3")

    ChrTalk(
        0xA,
        (
            "#03800F"We have something important to\x01",
            "talk about today, so stay on 2F." \x01",
            "That's what they said.\x02\x03",
            "Maybe it's about work?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30D4")

    label("loc_2FB3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3014")

    ChrTalk(
        0xA,
        (
            "#03805FI got tired of\x01",
            "playing by myself.\x02\x03",
            "I wonder when papa\x01",
            "will be back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30D4")

    label("loc_3014")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3078")

    ChrTalk(
        0xA,
        (
            "#03805FAh, there's\x01",
            "honey here.\x02\x03",
            "#03809F*lick*. \x01",
            "Ehehe, sweet and yummy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    ClearChrFlags(0xA, 0x10)
    Jump("loc_30D4")

    label("loc_3078")


    ChrTalk(
        0xA,
        (
            "#03809FPapa brought home this\x01",
            "honey as a souvenir\x01",
            "the other day.\x02\x03",
            "I really love honey.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30D4")

    Jump("loc_3487")

    label("loc_30D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_319C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_315D")

    ChrTalk(
        0xA,
        (
            "#03805FEven though papa's off today, \x01",
            "it looks like he went somewhere.\x02\x03",
            "Is he working\x01",
            "anway?\x01",
            "Aww...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3197")

    label("loc_315D")


    ChrTalk(
        0xA,
        (
            "#03805FPapa promised\x01",
            "he'd play with me\x01",
            "today. Aww...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3197")

    Jump("loc_3487")

    label("loc_319C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_31EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31B7")
    Call(0, 10)
    Jump("loc_31E5")

    label("loc_31B7")


    ChrTalk(
        0xA,
        (
            "#03809FEhehe. Sis Cindy\x01",
            "complimented me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31E5")

    Jump("loc_3487")

    label("loc_31EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_3250")

    ChrTalk(
        0xA,
        (
            "#03802FTonight's dinner\x01",
            "is curry...\x02\x03",
            "#03809FEhehe, I cut\x01",
            "the vegetables.\x01",
            "Cool, eh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3487")

    label("loc_3250")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_32DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_326B")
    Call(0, 8)
    Jump("loc_32DA")

    label("loc_326B")


    ChrTalk(
        0xA,
        (
            "#03800FYou know, \x01",
            "I'm helping with\x01",
            "dinner today.\x02\x03",
            "#03809FI'll surprise papa when he\x01",
            "comes back from work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32DA")

    Jump("loc_3487")

    label("loc_32DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3358")

    ChrTalk(
        0xA,
        (
            "#03800FPapa's working today.\x02\x03",
            "#03802FI wonder if he'll bring me a lot\x01",
            "of souvenirs when he gets back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3487")

    label("loc_3358")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_33EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33B3")

    ChrTalk(
        0xA,
        (
            "#03802F*om, nom*.\x02\x03",
            "#03809F*chew*... \x01",
            "Ehehe, this is great.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_33E5")

    label("loc_33B3")


    ChrTalk(
        0xA,
        (
            "#03809FEhehe. Mama's really\x01",
            "good at cooking.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33E5")

    Jump("loc_3487")

    label("loc_33EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3487")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3409")
    TalkEnd(0xFE)
    Call(0, 14)
    Return()

    label("loc_3409")


    ChrTalk(
        0xA,
        (
            "#03805FI kind of want to meet\x01",
            "that violet-haired girl I\x01",
            "talked to before again.\x02\x03",
            "#03809FEhehe, we'll meet again someday.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3487")

    TalkEnd(0xFE)
    Return()

    # Function_9_2B03 end

    def Function_10_348B(): pass

    label("Function_10_348B")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xA,
        (
            "#03802FYou know what, sis Cindy?\x02\x03",
            "I made curry\x01",
            "last night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Wow, you did?\x01",
            "You're amazing, Colin!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "With this, your cooking is already\x01",
            "better than my brother's, you know.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x10)
    SetScenarioFlags(0x0, 2)
    SetScenarioFlags(0x0, 3)
    Return()

    # Function_10_348B end

    def Function_11_3562(): pass

    label("Function_11_3562")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3635")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3580")
    Call(0, 10)
    Jump("loc_3630")

    label("loc_3580")


    ChrTalk(
        0xFE,
        (
            "Uh uh. Sophia is going to\x01",
            "teach me how to make\x01",
            "delicious sweets today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even though Colin's so little,\x01",
            "he's such a good boy... \x01",
            "I'd like my brother to learn from him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3630")

    Jump("loc_368F")

    label("loc_3635")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_368F")

    ChrTalk(
        0xFE,
        (
            "Ah, Colin grabbed\x01",
            "one of the cookies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Uh uh. Such a mischievous child.\x02",
    )

    CloseMessageWindow()

    label("loc_368F")

    TalkEnd(0xFE)
    Return()

    # Function_11_3562 end

    def Function_12_3693(): pass

    label("Function_12_3693")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_390A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36E6")

    ChrTalk(
        0xFE,
        (
            "Sorry, Harold. \x01",
            "I must be bothering you...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_390A")

    label("loc_36E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36F8")
    Call(0, 15)
    Jump("loc_390A")

    label("loc_36F8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_390A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_37AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3724")
    Call(0, 18)
    Jump("loc_37A9")

    label("loc_3724")


    ChrTalk(
        0xFE,
        (
            "After I help Layer Ian to\x01",
            "find what he's looking for,\x01",
            "I'll go back to the village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You all...\x01",
            "Please take care\x01",
            "of Derrick.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37A9")

    Jump("loc_390A")

    label("loc_37AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3886")

    ChrTalk(
        0xFE,
        (
            "I am pathetic, and unable to do\x01",
            "anything for Derrick. Even though I am\x01",
            "the Village Chief and his father...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please, I beg of you. Please expose the\x01",
            "true identity of the man called Minneth.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_390A")

    label("loc_3886")


    ChrTalk(
        0xFE,
        "I am at a loss, unable to do anything...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please, I beg of you. Please expose the\x01",
            "true identity of the man called Minneth.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_390A")

    TalkEnd(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3922")
    OP_93(0xC, 0x10E, 0x0)

    label("loc_3922")

    Return()

    # Function_12_3693 end

    def Function_13_3923(): pass

    label("Function_13_3923")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3938")
    Call(0, 18)
    Jump("loc_3B67")

    label("loc_3938")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AA1")

    ChrTalk(
        0xD,
        (
            "#02200FThe evidence I'm looking for\x01",
            "will be insurance for after\x01",
            "you've tracked down Minneth.\x02\x03",
            "Anyway, you all should\x01",
            "hurry to Armorica Village.\x02\x03",
            "#02203FIf Minneth really is a crook,\x01",
            "then his plan may be\x01",
            "advancing to its final stage.\x02\x03",
            "#02200FHowever, I'm sure you guys will get\x01",
            "by with the evidence you already\x01",
            "have. I wish you good luck.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3B67")

    label("loc_3AA1")


    ChrTalk(
        0xD,
        (
            "#02203FIf Minneth really is a crook,\x01",
            "then his plan may be\x01",
            "advancing to its final stage.\x02\x03",
            "#02200FHowever, I'm sure you guys will get\x01",
            "by with the evidence you already\x01",
            "have. I wish you good luck.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B67")

    TalkEnd(0xFE)
    Return()

    # Function_13_3923 end

    def Function_14_3B6B(): pass

    label("Function_14_3B6B")

    EventBegin(0x0)
    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0xA, 0x0)
    SetChrSubChip(0x8, 0x0)
    Fade(500)
    OP_68(-960, 1600, 6740, 0)
    MoveCamera(46, 18, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(24100, 0)
    SetChrPos(0x101, -970, 0, 4960, 0)
    SetChrPos(0x102, 640, 0, 4960, 0)
    SetChrPos(0x109, -470, 0, 4260, 0)
    SetChrPos(0x105, 1040, 0, 3960, 0)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x9, 0x1)
    SetChrSubChip(0xA, 0x1)
    Sleep(300)

    ChrTalk(
        0x9,
        "#11P#03705FAh, all of you are...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P#03609FOh, the Support Section!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11P#03802FHello!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FMr. Harold and Mrs. Sophia,\x01",
            "it's been awhile.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00102F*giggle*, Colin\x01",
            "looks well too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#03600FThanks to all of you...\x01",
            "Since then, we've lived\x01",
            "peaceful lives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10105FDo you and Elie\x01",
            "know this family,\x01",
            "Mr. Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FHu hu, looks like something\x01",
            "happened among you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#03600FYes. The Support Section\x01",
            "helped us before when\x01",
            "Colin went missing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#03709FWe really appreciated\x01",
            "your help back then.\x02\x03",
            "#03700FEven now, the only reason we can\x01",
            "be here like this is thanks to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012FN-No... For us it was\x01",
            "really no big deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#03600FYou don't need to say that...\x01",
            "I mean, no matter how much we could\x01",
            "thank you, it wouldn't be enough.\x02\x03",
            "#03608FOrdinarily, I would have\x01",
            "wanted to thank that girl that\x01",
            "helped us as well, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P#03805FThat violet-\x01",
            "haired girl?\x02\x03",
            "#03809FI want to see her again too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#03700FUh uh... That's right. \x01",
            "I too would like to see her again.\x02\x03",
            "Might all of\x01",
            "you know her?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103F...I'm sorry to say, but...\x01",
            "We didn't see the\x01",
            "girl again after that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#03603FHmm, is that so...\x02\x03",
            "#03600FWell, if we are tied by fate,\x01",
            "we'll meet again, right?\x02\x03",
            "I suppose all we can do is be\x01",
            "patient and wait for that chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003F(..."That girl"...\x01",
            "She has already\x01",
            "left Crossbell...)\x02\x03",
            "#00008F(In the end, I can't\x01",
            "explain the situation to\x01",
            "the Hayworths, but...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#03600F...Well then, everyone. Please\x01",
            "don't hesitate to stop by if\x01",
            "you ever need anything.\x02\x03",
            "I will do anything in\x01",
            "my power to assist you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYes, thank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11P#03809FEhehe, come again.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0xA, 0x0)
    Sleep(50)
    SetScenarioFlags(0x12F, 7)
    EventEnd(0x5)
    Return()

    # Function_14_3B6B end

    def Function_15_42D4(): pass

    label("Function_15_42D4")

    EventBegin(0x0)
    OP_4B(0xC, 0xFF)
    OP_4B(0x8, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-2040, 1500, 4340, 0)
    MoveCamera(44, 26, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23010, 0)
    OP_93(0xC, 0x10E, 0x0)
    OP_93(0x8, 0x10E, 0x0)
    SetChrPos(0x101, -2360, 0, 4740, 90)
    SetChrPos(0x102, -2780, 0, 3340, 90)
    SetChrPos(0x103, -2620, 0, 2009, 45)
    SetChrPos(0x104, -3660, 0, 4220, 90)
    SetChrPos(0x109, -3080, 0, 5820, 90)
    SetChrPos(0x105, -2380, 0, 7190, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4567")

    ChrTalk(
        0x101,
        (
            "#00000FExcuse us, Special\x01",
            "Support Section here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Oh, the Special Support Section...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Thanks for coming\x01",
            "again today too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#03600FThank you very much, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FVillage Chief Tolta,\x01",
            "wha exactly happened?\x02\x03",
            "#00003FIt seems there's been some\x01",
            "developments in yesterday's case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Yes... It seems the\x01",
            "situation is more\x01",
            "serious than I thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'd like to discuss the\x01",
            "request immediately. \x01",
            "Do you mind?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45ED")

    label("loc_4567")


    ChrTalk(
        0xC,
        (
            "It seems the situation\x01",
            "is more serious than I\x01",
            "initially thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'd like to discuss the\x01",
            "request immediately. \x01",
            "Do you mind?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45ED")

    Call(0, 16)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -2190, 0, 4360, 225)
    OP_69(0xFF, 0x0)
    OP_93(0xC, 0x0, 0x0)
    OP_93(0x8, 0xB4, 0x0)
    OP_4C(0xC, 0xFF)
    OP_4C(0x8, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_15_42D4 end

    def Function_16_4632(): pass

    label("Function_16_4632")

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
            "[Accept]\x01",      # 0
            "[Quit]\x01",        # 1
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
        (0, "loc_4692"),
        (1, "loc_469A"),
        (SWITCH_DEFAULT, "loc_476D"),
    )


    label("loc_4692")

    Call(0, 17)
    Jump("loc_476D")

    label("loc_469A")


    ChrTalk(
        0x101,
        (
            "#00006FWe're terribly sorry, but...\x01",
            "We're a little busy right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Hmm, is that so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Then, if you have time,\x01",
            "please come again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If possible, I would like\x01",
            "help from all of you.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x177, 1)

    label("loc_476D")

    Return()

    # Function_16_4632 end

    def Function_17_476E(): pass

    label("Function_17_476E")


    ChrTalk(
        0x101,
        "#00000FNo, please fill us in.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYou said the situation's\x01",
            "changed since yesterday...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Yes, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Yesterday evening I went to Derrick,\x01",
            "who's staying at the Ash Tree Inn\x01",
            "and tried to persuade him once again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I told him to stop associating with that\x01",
            "Minneth foreigner because there're many\x01",
            "suspicious points about him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FYou gave it to him\x01",
            "straight, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Yes, but...\x01",
            "In the end, Derrick\x01",
            "wouldn't listen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Instead, I learned\x01",
            "something new.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I hurried to Harold's place to\x01",
            "discuss the matter with him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205FSomething new...?\x02\x03",
            "Did you figure out what\x01",
            "that Minneth is up to?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03603FI was surprised too,\x01",
            "once I heard about it.\x02\x03",
            "#03601FIt seems that Minneth has penetrated the\x01",
            "village even further than we thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FUmm... \x01",
            "What do you mean, exactly?\x02\x03",
            "We knew that he had gained the trust\x01",
            "of the villagers yesterday, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Actually, that Minneth is after...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "...Not just the private\x01",
            "property, but the deeds of all\x01",
            "fields and plots in the village.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FA-All of the deeds...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FHmm... If that's how it is,\x01",
            "it's quite concerning indeed.\x02\x03",
            "#10301FJust how did Mr. Minneth\x01",
            "manage to get his hands\x01",
            "on such important things?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03601FYes, based on what I've heard,\x01",
            "he called it the "lotus fields\x01",
            "expansion project."\x02\x03",
            "By collecting the villagers' fields\x01",
            "little-by-little, he'll expand the lotus\x01",
            "fields and harvest them more efficiently.\x02\x03",
            "#03603FFinally, Quincy Company will take over\x01",
            "management of the fields so it won't be\x01",
            "so difficult to tend and harvest them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FThat connects to...\x01",
            "What we heard yesterday.\x02\x03",
            "#10103FAt first glance it seemed like a fine idea...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FYeah... \x01",
            ""Too good to be true."\x02\x03",
            "#00003FAnd regarding those deeds...\x01",
            "If he abuses them, then you\x01",
            "won't be able to recover.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Yes... Suspicion continues\x01",
            "to surround that Minneth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If it was just our private property,\x01",
            "then even in the worst case there\x01",
            "wouldn't be much financial harm, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "With him using plots throughout\x01",
            "the village, the consequences\x01",
            "are unpredictable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301FI see. You could say there's no\x01",
            "way to escape the agreement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "And so, I figured we\x01",
            "could ask you for help\x01",
            "exposing his true colors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Can we count on the police\x01",
            "to help us with this, even\x01",
            "though he isn't a suspect?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FNo... From the start, we\x01",
            "aren't bound by police rules.\x02\x03",
            "#00000FNow that there're even some little\x01",
            "suspicious point about him...\x01",
            "We will gladly investigate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Thank you...\x01",
            "You all are always\x01",
            "helping us.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00100FThen, from where should\x01",
            "we start investigating?\x02\x03",
            "#00103FWe don't have any clues at the\x01",
            "moment, to be perfectly honest...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FWe don't have anything that\x01",
            "could be called a motive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FThat's true...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03600FIn that case... Why don't\x01",
            "you try asking Lawyer Ian\x01",
            "for help with this?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x102, 0x5A, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x103,
        "#00205FLawyer Ian...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03600FYes. Right now, all we\x01",
            "know is that Minneth\x01",
            "is "suspicious", but...\x02\x03",
            "If you explain the situation to Lawyer Ian, \x01",
            "he might be able to detect some hint of a\x01",
            "crime in Minneth's actions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FI see... \x01",
            "That's not a bad idea.\x02\x03",
            "#00000FIf he gets us even a little closer to what\x01",
            "Minneth is trying to do, it could be a\x01",
            "good starting point for the investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03603FBut Lawyer Ian is very busy\x01",
            "right now with the declaration\x01",
            "of independence and everything.\x02\x03",
            "#03608FIt's possible that\x01",
            "he won't see you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FWell, let's go to his\x01",
            "law office anyway.\x02\x03",
            "We'll think about what to do\x01",
            "next if he really is out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah... \x01",
            "Let's pay him a visit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03600FWe'll leave it\x01",
            "to you then.\x02\x03",
            "I'll see if my business partners\x01",
            "have heard any rumors about\x01",
            "Quincy Company or Minneth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FThat would be\x01",
            "great, thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Thank you...\x01",
            "You're the only ones who can help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'm at a loss, unable\x01",
            "to do anything...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FDon't worry about it.\x01",
            "We'll take care of this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FJust wait here for us,\x01",
            "Village Chief.\x02\x03",
            "And pray to the Goddess\x01",
            "for some good news.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hm...\x01",
            "I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest [Suspicious Trader Investigation]\x07\x00",
            " started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x177, 2)
    OP_29(0x87, 0x1, 0x0)
    ClearChrFlags(0xC, 0x10)
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x9, 550, 0, 2040, 180)
    SetChrPos(0xC, -10, 0, 5370, 270)
    SetChrPos(0x0, -2130, 0, 3860, 270)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_17_476E end

    def Function_18_58BF(): pass

    label("Function_18_58BF")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0xC, 0xFF)
    OP_4B(0x8, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_68(-2330, 1500, 4180, 0)
    MoveCamera(57, 21, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25120, 0)
    SetChrPos(0xC, -690, 0, 3590, 270)
    SetChrPos(0x8, -490, 0, 5140, 270)
    SetChrPos(0xD, 660, 0, 4600, 270)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xD, 0x80)
    OP_93(0xC, 0x10E, 0x0)
    OP_93(0x8, 0x10E, 0x0)
    SetChrPos(0x101, -2360, 0, 4740, 90)
    SetChrPos(0x102, -2780, 0, 3340, 90)
    SetChrPos(0x103, -2620, 0, 2009, 45)
    SetChrPos(0x104, -3660, 0, 4220, 90)
    SetChrPos(0x109, -3080, 0, 5820, 90)
    SetChrPos(0x105, -2380, 0, 7190, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xC,
        "Oh, it's you guys...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11P#02200FIt seems you've returned.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FLawyer Ian...\x01",
            "You came.\x02\x03",
            "You're back too,\x01",
            "Mr. Harold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03604FYes, I just finished asking my business\x01",
            "partners about the current matter.\x02\x03",
            "#03601FHow are things on your end?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThanks to Lawyer Ian, we were\x01",
            "able to find out a few things.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00100FDid you find something\x01",
            "too, Mr. Harold?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#03603FYes... In a manner of speaking.\x02\x03",
            "#03608FAlthough I don't know\x01",
            "what it means...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHu hu, well you went to the\x01",
            "trouble of getting it. It doesn't\x01",
            "matter what it is. Let's hear it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FYes, please. The information\x01",
            "may be connected to the\x01",
            "current situation.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#03603FI suppose you're right.\x02\x03",
            "#03601FNot having any idea about\x01",
            "the name Minneth, I tried\x01",
            "asking my trading partners.\x02\x03",
            "When I did that... Somehow, it seems\x01",
            "Mr. Minneth has been studying a certain\x01",
            "thing ever since he came to Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FA certain thing...you say?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03601FYes, and that is...\x01",
            "The "price of land" in various\x01",
            "places throughout Crossbel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305FThe price of land...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103FSo Mr. Minneth is looking more\x01",
            "like a real estate agent...\x02\x03",
            "#10105FBut, why would he need to look\x01",
            "into something like that...?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00001FThis might be crucial\x01",
            "evidence as to\x01",
            "Minneth's objective.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
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
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xC,
        "R-Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P#02203FYes, that makes sense, actually.\x02\x03",
            "#02200FI found out something that\x01",
            "may be useful as well.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x5A, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00005FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P#02200FHarold, Village Chief Tolta.\x02\x03",
            "Will you help me find\x01",
            "something in my office?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_60C4():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_60C4)
    Sleep(50)

    def lambda_60D4():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_60D4)
    Sleep(300)

    ChrTalk(
        0x8,
        "#03605FLawyer Ian...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I don't particularly mind, but...\x01",
            "Is it that important?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P#02203FWell, I don't think it will be\x01",
            "able to prove anything, but...\x02\x03",
            "#02200FI think we can think of it as\x01",
            "insurance for pinning down Minneth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305FHuh? I don't really get it, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P#02200FWell, I don't know if we'll be in time, \x01",
            "so try not to get your hopes up.\x02\x03",
            "#02203FMore importantly, Special\x01",
            "Support Section. You had\x01",
            "best hurry to Armorica Village.\x02\x03",
            "#02200FIf Minneth really is a crook,\x01",
            "then his plan may be\x01",
            "advancing to its final stage.\x02\x03",
            "However, if it's you guys, I am sure you'll be able\x01",
            "to do something with the evidence you have on hand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F...Alright, understood!\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00001FAlright then, everyone...\x01",
            "Let's head to Armorica Village.\x02\x03",
            "We'll expose Minneth's true colors and\x01",
            "stop him from making any more deals!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_643B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_643B)
    Sleep(50)

    def lambda_644B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_644B)
    Sleep(50)

    def lambda_645B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_645B)
    Sleep(50)

    def lambda_646B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_646B)
    Sleep(50)

    def lambda_647B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_647B)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00101FYes... Let's go!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x87, 0x1, 0x5)
    SetScenarioFlags(0x177, 6)
    ClearMapFlags(0x10000000)
    OP_93(0x8, 0xB4, 0x0)
    OP_93(0xC, 0x0, 0x0)
    OP_4C(0xC, 0xFF)
    OP_4C(0x8, 0xFF)
    OP_4C(0xD, 0xFF)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -2130, 0, 3860, 270)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_18_58BF end

    SaveToFile()

Try(main)
