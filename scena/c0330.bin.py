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
        "Function_6_8F8",          # 06, 6
        "Function_7_174E",         # 07, 7
        "Function_8_2970",         # 08, 8
        "Function_9_2A59",         # 09, 9
        "Function_10_33F8",        # 0A, 10
        "Function_11_34D4",        # 0B, 11
        "Function_12_3607",        # 0C, 12
        "Function_13_3895",        # 0D, 13
        "Function_14_3AD5",        # 0E, 14
        "Function_15_4218",        # 0F, 15
        "Function_16_4577",        # 10, 16
        "Function_17_46AB",        # 11, 17
        "Function_18_57C5",        # 12, 18
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
            "It's a car magazine,\x01",
            ""Monthly Car Mania\x01",
            "Vol.1".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x36C, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8F4")
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Learned the \x07\x02",
            ""Sky\x01",
            "Coloring"\x07\x00",
            " paint pattern.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber(0x36C, 1)

    label("loc_8F4")

    TalkEnd(0xFF)
    Return()

    # Function_5_846 end

    def Function_6_8F8(): pass

    label("Function_6_8F8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_D1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB9")

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
            "#00000FHarold. You're back from\x01",
            "Armorica Village?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03604FYes. I just got back\x01",
            "after seeing that the\x01",
            "barrier had disappeared.\x02\x03",
            "#03600FAlthough I was just\x01",
            "about to leave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FLooks like you're going\x01",
            "to be busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FYour family's here, so\x01",
            "shouldn't you take it\x01",
            "easy a while longer?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03603FNo. Right now, I want to\x01",
            "help everyone all across\x01",
            "Crossbell.\x02\x03",
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
            "#00002FPlease take care on your\x01",
            "way there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03609FYes. And the same goes for\x01",
            "all of you... May the Goddess\x01",
            "grant you her protection.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CD, 0)
    Jump("loc_D16")

    label("loc_BB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C91")

    ChrTalk(
        0x8,
        (
            "#03600FTo start, I'm planning on\x01",
            "going to Mainz.\x02\x03",
            "#03603FRight now, I want to help\x01",
            "everyone all across\x01",
            "Crossbell.\x02\x03",
            "#03609FPlease be careful,\x01",
            "everyone. May the Goddess\x01",
            "grant you her protection.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D16")

    label("loc_C91")


    ChrTalk(
        0x8,
        (
            "#03600FTo start, I'm planning on\x01",
            "going to Mainz.\x02\x03",
            "#03609FPlease be careful,\x01",
            "everyone. May the Goddess\x01",
            "grant you her protection.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D16")

    Jump("loc_174A")

    label("loc_D1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_D29")
    Jump("loc_174A")

    label("loc_D29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_D37")
    Jump("loc_174A")

    label("loc_D37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_D45")
    Jump("loc_174A")

    label("loc_D45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_F23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E68")

    ChrTalk(
        0x8,
        (
            "#03601FI planned to go to Mainz today,\x01",
            "but... I can't believe this has\x01",
            "happened.\x02\x03",
            "#03603F...I've gone to Mainz many times\x01",
            "for trade deals, and the people\x01",
            "there are very good to me.\x02\x03",
            "#03608FBut even so, it's pathetic that\x01",
            "I can't do a single thing for\x01",
            "them...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F1E")

    label("loc_E68")


    ChrTalk(
        0x8,
        (
            "#03603F...I've gone to Mainz many times\x01",
            "for trade deals, and the people\x01",
            "there are very good to me.\x02\x03",
            "#03608FBut even so, it's pathetic that\x01",
            "I can't do a single thing for\x01",
            "them...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F1E")

    Jump("loc_174A")

    label("loc_F23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_F31")
    Jump("loc_174A")

    label("loc_F31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_F3F")
    Jump("loc_174A")

    label("loc_F3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1088")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_FF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F66")
    Call(0, 15)
    Jump("loc_FEC")

    label("loc_F66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F78")
    Call(0, 18)
    Jump("loc_FEC")

    label("loc_F78")


    ChrTalk(
        0x8,
        (
            "#03600FI'll be taking the chief\x01",
            "and the others back to\x01",
            "Armorica in my car later.\x02\x03",
            "Everyone, please be\x01",
            "careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FEC")

    Jump("loc_1083")

    label("loc_FF1")


    ChrTalk(
        0x8,
        (
            "#03601FAnyway, I'll try to settle\x01",
            "what I learned in\x01",
            "yesterday's investigation.\x02\x03",
            "#03603FAnd, it might be good to\x01",
            "speak with Lawyer Ian\x01",
            "later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1083")

    Jump("loc_174A")

    label("loc_1088")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1096")
    Jump("loc_174A")

    label("loc_1096")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_10A4")
    Jump("loc_174A")

    label("loc_10A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_125D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11E4")

    ChrTalk(
        0x8,
        "#03605FOh, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FGood evening, Harold.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00104FA nice smell is coming from\x01",
            "the second floor... It seems\x01",
            "your wife is preparing dinner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03609FYes, you're right. And\x01",
            "it seems Colin is\x01",
            "helping her today, too.\x02\x03",
            "#03604FMan, I've just gotten\x01",
            "home and I'm very\x01",
            "hungry.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14A, 6)
    Jump("loc_1258")

    label("loc_11E4")


    ChrTalk(
        0x8,
        (
            "#03600FIt seems Colin is\x01",
            "helping too today.\x02\x03",
            "#03609FHaha, I can't wait to\x01",
            "see what dishes we're\x01",
            "going to have.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1258")

    Jump("loc_174A")

    label("loc_125D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_126B")
    Jump("loc_174A")

    label("loc_126B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1279")
    Jump("loc_174A")

    label("loc_1279")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1558")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14CE")

    ChrTalk(
        0x8,
        (
            "#03603FPassing time alone like\x01",
            "this, I had a sudden\x01",
            "idea.\x02\x03",
            "That violet-haired girl\x01",
            "who saved Colin\x01",
            "before...\x02\x03",
            "#03608FI wonder if it's really\x01",
            "impossible to meet her,\x01",
            "I thought.\x02",
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
            "#03604FHaha. For now I don't have\x01",
            "any clues. It's just a\x01",
            "simple hope of mine.\x02\x03",
            "#03600FIf there ever is a chance...\x01",
            "I would like to offer my\x01",
            "thanks to that girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F(A violet-haired girl... Renne\x01",
            "returned to Liberl with Estelle\x01",
            "and Joshua, right...?)\x02\x03",
            "#00003F(That girl needs to sort out her\x01",
            "feelings too, but... I'm sure\x01",
            "that day will eventually come.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x134, 0)
    Jump("loc_1553")

    label("loc_14CE")


    ChrTalk(
        0x8,
        (
            "#03603FThat violet-haired girl\x01",
            "who saved Colin\x01",
            "before...\x02\x03",
            "#03600FIf I ever do get to meet\x01",
            "her, I would like to\x01",
            "offer my thanks.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1553")

    Jump("loc_174A")

    label("loc_1558")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_174A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1577")
    TalkEnd(0xFE)
    Call(0, 14)
    Return()

    label("loc_1577")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16D7")

    ChrTalk(
        0x8,
        (
            "#03600FMy trade business has been\x01",
            "doing well lately.\x02\x03",
            "#03604FBecause of that, I have\x01",
            "some time to spend\x01",
            "vacationing with my family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FHaha. Looks like your\x01",
            "continued efforts are\x01",
            "bearing fruit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03609FHaha... To be honest, it\x01",
            "gives me an uneasy\x01",
            "feeling.\x02\x03",
            "#03600FTo me, just providing\x01",
            "for my family would be\x01",
            "enough.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_174A")

    label("loc_16D7")


    ChrTalk(
        0x8,
        (
            "#03600FEveryone, please let me\x01",
            "know if you ever need\x01",
            "anything.\x02\x03",
            "I will do anything in my\x01",
            "power to assist you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_174A")

    TalkEnd(0xFE)
    Return()

    # Function_6_8F8 end

    def Function_7_174E(): pass

    label("Function_7_174E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_18FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1850")

    ChrTalk(
        0x9,
        (
            "#03708FIf we just take it easy a\x01",
            "while longer, I\x01",
            "thought...\x02\x03",
            "#03700FKind, considerate and\x01",
            "skillful. That is the man\x01",
            "that is Harold Hayworth.\x02\x03",
            "#03709FIf my husband says he\x01",
            "wants to help people, all\x01",
            "we can do is support him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_18F7")

    label("loc_1850")


    ChrTalk(
        0x9,
        (
            "#03700FKind, considerate and\x01",
            "skillful. That is the man\x01",
            "that is Harold Hayworth.\x02\x03",
            "#03709FIf my husband says he\x01",
            "wants to help people, all\x01",
            "we can do is support him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18F7")

    Jump("loc_296C")

    label("loc_18FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_190A")
    Jump("loc_296C")

    label("loc_190A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_19A8")

    ChrTalk(
        0x9,
        (
            "#03708FI wonder what's going to\x01",
            "happen now...\x02\x03",
            "#03710FIf anything happened to Colin\x01",
            "or my husband... Anyway,\x01",
            "that's all I'm worried about.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_296C")

    label("loc_19A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1B59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AAB")

    ChrTalk(
        0x9,
        (
            "#03700FMy husband is going to check\x01",
            "on the situation in Mainz\x01",
            "today.\x02\x03",
            "He said because of yesterday's\x01",
            "attack, he wants to do all he\x01",
            "can for the people of Mainz...\x02\x03",
            "#03709FI feel proud of my\x01",
            "compassionate husband all over\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1B54")

    label("loc_1AAB")


    ChrTalk(
        0x9,
        (
            "#03700FHe said because of yesterday's\x01",
            "attack, he wants to do all he\x01",
            "can for the people of Mainz...\x02\x03",
            "#03709FI feel proud of my\x01",
            "compassionate husband all over\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B54")

    Jump("loc_296C")

    label("loc_1B59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1C82")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C29")

    ChrTalk(
        0x9,
        (
            "#03708FHearing news of the attack, I\x01",
            "immediately thought, "I hope\x01",
            "my husband's not involved."\x02\x03",
            "Even at this moment, I fear\x01",
            "for the people of Mainz...\x02\x03",
            "#03710F...I hate myself.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C7D")

    label("loc_1C29")


    ChrTalk(
        0x9,
        (
            "#03708F...Anyway, I pray to the\x01",
            "Goddess that the incident\x01",
            "is resolved quickly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C7D")

    Jump("loc_296C")

    label("loc_1C82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1D47")

    ChrTalk(
        0x9,
        (
            "#03700FMy husband's going to Bellguard Gate\x01",
            "for a delivery today.\x02\x03",
            "#03708FHowever, a giant monster was spotted\x01",
            "on West Crossbell Highway just\x01",
            "yesterday, so I'm a little worried.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_296C")

    label("loc_1D47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1FBC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E97")

    ChrTalk(
        0x9,
        (
            "#03705FOh, everyone?\x02\x03",
            "If you're looking for my husband,\x01",
            "he went to Armorica to discuss\x01",
            "something with the chief...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(We should have followed through on that\x01",
            "investigation, but... Right now, checking\x01",
            "on that accident is our top priority.)\x02\x03",
            "(Let's leave Armorica Village to Harold.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16C, 7)
    Jump("loc_1FB7")

    label("loc_1E97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F49")

    ChrTalk(
        0x9,
        (
            "#03700FCindy came earlier for\x01",
            "her lesson, but...\x02\x03",
            "It seems a lot of\x01",
            "ambulances passed\x01",
            "through West Street.\x02\x03",
            "#03708FI'm getting a bad\x01",
            "feeling about this...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1FB7")

    label("loc_1F49")


    ChrTalk(
        0x9,
        (
            "#03708FIt seems a lot of\x01",
            "ambulances passed\x01",
            "through West Street.\x02\x03",
            "I'm getting a bad\x01",
            "feeling about this...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FB7")

    Jump("loc_296C")

    label("loc_1FBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2319")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2115")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2084")

    ChrTalk(
        0x9,
        (
            "#03700FMy husband just contacted me.\x01",
            "He says the incident in\x01",
            "Armorica was resolved safely.\x02\x03",
            "#03708FBut even so, a swindler... He\x01",
            "must be a very bad person.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2110")

    label("loc_2084")


    ChrTalk(
        0x9,
        (
            "#03700FIt seems the incident in\x01",
            "Armorica Village was\x01",
            "resolved safely.\x02\x03",
            "#03708FBut even so, a\x01",
            "swindler... He must be a\x01",
            "very bad person.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2110")

    Jump("loc_2314")

    label("loc_2115")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21A8")

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
    Jump("loc_2314")

    label("loc_21A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_228C")

    ChrTalk(
        0x9,
        (
            "#03700FIt seems the village\x01",
            "chief worries too much...\x02\x03",
            "#03708FBut, it is his son, so I\x01",
            "suppose that's only\x01",
            "natural, but...\x02\x03",
            "#03700FWorrying too much is bad\x01",
            "for your health. For now,\x01",
            "he's got to calm down.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2314")

    label("loc_228C")


    ChrTalk(
        0x9,
        (
            "#03700FWorrying too much is bad\x01",
            "for your health. For now,\x01",
            "he's got to calm down.\x02\x03",
            "I think my calming herb\x01",
            "tea will do the trick...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2314")

    Jump("loc_296C")

    label("loc_2319")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_23EA")

    ChrTalk(
        0x9,
        (
            "#03700FMy husband was contacted by the chief of\x01",
            "Armorica Village.\x02\x03",
            "It seems he wanted to discuss something...\x01",
            "It didn't seem like a business negotiation\x01",
            "either. I wonder what it could be...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_296C")

    label("loc_23EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_253F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24BC")

    ChrTalk(
        0x9,
        (
            "#03700FI made curry with Colin\x01",
            "last night, but...\x02\x03",
            "I might have made a\x01",
            "little too much. There\x01",
            "are a lot of leftovers.\x02\x03",
            "#03709FHaha, it'll be a while\x01",
            "before the next curry\x01",
            "night.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_253A")

    label("loc_24BC")


    ChrTalk(
        0x9,
        (
            "#03700FI might have made a\x01",
            "little too much curry\x01",
            "last night.\x02\x03",
            "#03709FHaha, it'll be a while\x01",
            "before the next curry\x01",
            "night.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_253A")

    Jump("loc_296C")

    label("loc_253F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_25C9")

    ChrTalk(
        0x9,
        (
            "#03700FAlright, we only need to\x01",
            "let it simmer.\x02\x03",
            "#03709FHaha. You did well,\x01",
            "Colin. Your dad will be\x01",
            "delighted for sure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_296C")

    label("loc_25C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2635")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25E4")
    Call(0, 8)
    Jump("loc_2630")

    label("loc_25E4")


    ChrTalk(
        0x9,
        (
            "#03700FI was just about to go\x01",
            "shopping.\x02\x03",
            "#03709FHaha. Colin's excited.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2630")

    Jump("loc_296C")

    label("loc_2635")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2771")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26E7")

    ChrTalk(
        0x9,
        (
            "#03700FCreil came to visit the\x01",
            "other day.\x02\x03",
            "It looks like she's\x01",
            "finally getting settled\x01",
            "in. She looked relieved...\x02\x03",
            "#03709FHaha, I'm relieved too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_276C")

    label("loc_26E7")


    ChrTalk(
        0x9,
        (
            "#03700FThey say Creil and her\x01",
            "family now live in an\x01",
            "apartment on East STreet.\x02\x03",
            "It looks like they're\x01",
            "doing ok. That's a\x01",
            "relief.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_276C")

    Jump("loc_296C")

    label("loc_2771")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_28E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_285C")

    ChrTalk(
        0x9,
        (
            "#03700FMr. Bond's family... They\x01",
            "used to live here, but they\x01",
            "moved recently.\x02\x03",
            "#03708FThey came to say goodbye when\x01",
            "they left, but I haven't\x01",
            "heard from them since.\x02\x03",
            "I hope they're doing all\x01",
            "right, but...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_28E2")

    label("loc_285C")


    ChrTalk(
        0x9,
        (
            "#03700FMr. Bond's wife Creil often\x01",
            "went shopping with me, and\x01",
            "we were very close, but...\x02\x03",
            "#03708FI hope she's doing all\x01",
            "right...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28E2")

    Jump("loc_296C")

    label("loc_28E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_296C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2906")
    TalkEnd(0xFE)
    Call(0, 14)
    Return()

    label("loc_2906")


    ChrTalk(
        0x9,
        (
            "#03700FYou all were a great\x01",
            "help to us back then.\x02\x03",
            "My husband and I hope\x01",
            "you will help us again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_296C")

    TalkEnd(0xFE)
    Return()

    # Function_7_174E end

    def Function_8_2970(): pass

    label("Function_8_2970")

    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0x9,
        (
            "#03700FCome now, Colin. I\x01",
            "wonder what we're going\x01",
            "to buy today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#03805FUmm, umm... Carrots,\x01",
            "potatoes, onions...\x02\x03",
            "#03809F...and curry roux!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03709FHaha, right answer.\x01",
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

    # Function_8_2970 end

    def Function_9_2A59(): pass

    label("Function_9_2A59")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2B80")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B08")

    ChrTalk(
        0xA,
        (
            "#03800FMom made a lunchbox for\x01",
            "dad to take on his trip\x01",
            "for work.\x02\x03",
            "#03809FAunt Camille gave us a\x01",
            "lot of veggies. Ehehe,\x01",
            "they look delicious.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2B7B")

    label("loc_2B08")


    ChrTalk(
        0xA,
        (
            "#03800FI want to go to Armorica\x01",
            "Village again.\x02\x03",
            "#03809FI promised to play with\x01",
            "Aunt Camille and Pooley\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B7B")

    Jump("loc_33F4")

    label("loc_2B80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2B8E")
    Jump("loc_33F4")

    label("loc_2B8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2C15")

    ChrTalk(
        0xA,
        (
            "#03805FLooks like mom and dad\x01",
            "are worried about\x01",
            "something~.\x02\x03",
            "I'm going to play after\x01",
            "this. I wonder what\x01",
            "happened~?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33F4")

    label("loc_2C15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2D1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CAE")

    ChrTalk(
        0xA,
        (
            "#03800FThis time, I'm going\x01",
            "with mom and dad to\x01",
            "play~.\x02\x03",
            "#03809FThey said it's a really\x01",
            "nice place. Ehehe, I\x01",
            "can't wait~.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2D15")

    label("loc_2CAE")


    ChrTalk(
        0xA,
        (
            "#03800FThis time, I'm going to\x01",
            "a really nice place to\x01",
            "play~.\x02\x03",
            "#03809FSo excited... I can't\x01",
            "wait~.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D15")

    Jump("loc_33F4")

    label("loc_2D1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2D99")

    ChrTalk(
        0xA,
        (
            "#03800FDad said he has work\x01",
            "today, but it looks like\x01",
            "he hasn't left yet.\x02\x03",
            "#3802FMaybe he's taking a\x01",
            "break~?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33F4")

    label("loc_2D99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2E0C")

    ChrTalk(
        0xA,
        (
            "#03802FLook at this! There's a\x01",
            "frog stuck to the\x01",
            "window~.\x02\x03",
            "#03809FIt's creepy but cute,\x01",
            "right~?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33F4")

    label("loc_2E0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2E75")

    ChrTalk(
        0xA,
        (
            "#03802FCindy gave me one of her\x01",
            "cookies just now~.\x02\x03",
            "#03809FIt was crunchy and\x01",
            "yummy~.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33F4")

    label("loc_2E75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3037")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F0F")

    ChrTalk(
        0xA,
        (
            "#03800FWe have something important to\x01",
            "talk about today, so don't come\x01",
            "to 2F. That's what they said.\x02\x03",
            "Maybe it's about work~?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3032")

    label("loc_2F0F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2F6E")

    ChrTalk(
        0xA,
        (
            "#03805FI give up on playing by\x01",
            "myself~.\x02\x03",
            "I wonder when dad 'll be\x01",
            "back~.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3032")

    label("loc_2F6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FDF")

    ChrTalk(
        0xA,
        (
            "#03805FAh, there's honey this\x01",
            "time of year~.\x02\x03",
            "#03809F*burp*. Ehehe, sweet and\x01",
            "yummy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    ClearChrFlags(0xA, 0x10)
    Jump("loc_3032")

    label("loc_2FDF")


    ChrTalk(
        0xA,
        (
            "#03809FMy dad gave me this\x01",
            "honey as a souvenir the\x01",
            "other day~.\x02\x03",
            "I love honey.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3032")

    Jump("loc_33F4")

    label("loc_3037")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3101")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30BD")

    ChrTalk(
        0xA,
        (
            "#03805FEven though dad's off\x01",
            "today, it looks like he\x01",
            "went somewhere~.\x02\x03",
            "Is he working anyway~?\x01",
            "Aww~...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_30FC")

    label("loc_30BD")


    ChrTalk(
        0xA,
        (
            "#03805FAnd dad promised he'd\x01",
            "play with me today~.\x01",
            "Aww~...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30FC")

    Jump("loc_33F4")

    label("loc_3101")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_314C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_311C")
    Call(0, 10)
    Jump("loc_3147")

    label("loc_311C")


    ChrTalk(
        0xA,
        (
            "#03809FEhehe. Cindy\x01",
            "complimented me~.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3147")

    Jump("loc_33F4")

    label("loc_314C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_31B3")

    ChrTalk(
        0xA,
        (
            "#03802FTonight's dinner is\x01",
            "curry...\x02\x03",
            "#03809FEhehe, I cut the\x01",
            "vegetables. Cool, huh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33F4")

    label("loc_31B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3246")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31CE")
    Call(0, 8)
    Jump("loc_3241")

    label("loc_31CE")


    ChrTalk(
        0xA,
        (
            "#03800FYou know, I'm helping\x01",
            "with dinner tonight~.\x02\x03",
            "#03809FDad's not back from work\x01",
            "yet. He'll be\x01",
            "surprised~.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3241")

    Jump("loc_33F4")

    label("loc_3246")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_32C0")

    ChrTalk(
        0xA,
        (
            "#03800FDad's working today~.\x02\x03",
            "#03802FI wonder if he'll bring\x01",
            "me a lot of souvenirs\x01",
            "when he gets back~.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33F4")

    label("loc_32C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3355")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_331B")

    ChrTalk(
        0xA,
        (
            "#03802F*om, nom*.\x02\x03",
            "#03809F*chew*... Ehehe, this is\x01",
            "great~.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3350")

    label("loc_331B")


    ChrTalk(
        0xA,
        (
            "#03809FEhehe. My mom's really\x01",
            "good at cooking~.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3350")

    Jump("loc_33F4")

    label("loc_3355")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_33F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3374")
    TalkEnd(0xFE)
    Call(0, 14)
    Return()

    label("loc_3374")


    ChrTalk(
        0xA,
        (
            "#03805FI kind of want to meet\x01",
            "that violet-haired girl I\x01",
            "talked to before again~.\x02\x03",
            "#03809FEhehe, we'll meet again\x01",
            "someday~.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33F4")

    TalkEnd(0xFE)
    Return()

    # Function_9_2A59 end

    def Function_10_33F8(): pass

    label("Function_10_33F8")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xA,
        (
            "#03802FYou know what, Cindy?\x02\x03",
            "I made curry last\x01",
            "night~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Wow, all by yourself?\x01",
            "You're amazing, Colin!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "With this, your cooking\x01",
            "is already better than\x01",
            "my brother's, you know.\x02",
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

    # Function_10_33F8 end

    def Function_11_34D4(): pass

    label("Function_11_34D4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_35AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34F2")
    Call(0, 10)
    Jump("loc_35A6")

    label("loc_34F2")


    ChrTalk(
        0xFE,
        (
            "Haha. Sophia is going to\x01",
            "teach me how to make\x01",
            "delicious sweets today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Even though Colin's so little,\x01",
            "he's such a good boy~... I wish my\x01",
            "brother would follow his example.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35A6")

    Jump("loc_3603")

    label("loc_35AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3603")

    ChrTalk(
        0xFE,
        (
            "Ah, Colin grabbed one of\x01",
            "my cookies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Haha. Such a mischievous\x01",
            "child.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3603")

    TalkEnd(0xFE)
    Return()

    # Function_11_34D4 end

    def Function_12_3607(): pass

    label("Function_12_3607")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_387C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3659")

    ChrTalk(
        0xFE,
        (
            "Sorry, Harold. I must be\x01",
            "bothering you...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_387C")

    label("loc_3659")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_366B")
    Call(0, 15)
    Jump("loc_387C")

    label("loc_366B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_387C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3720")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3697")
    Call(0, 18)
    Jump("loc_371B")

    label("loc_3697")


    ChrTalk(
        0xFE,
        (
            "Now that we've found what\x01",
            "Lawyer Ian was looking for,\x01",
            "let's head for the village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You all... Please take\x01",
            "care of Derrick.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_371B")

    Jump("loc_387C")

    label("loc_3720")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37F8")

    ChrTalk(
        0xFE,
        (
            "I am pathetic, and unable to do\x01",
            "anything for Derrick. Even though I am\x01",
            "the village chief and his father...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please, I beg of you. Please\x01",
            "expose the true identity of\x01",
            "the man called Minneth.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_387C")

    label("loc_37F8")


    ChrTalk(
        0xFE,
        (
            "I am at a loss, unable\x01",
            "to do anything...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please, I beg of you. Please\x01",
            "expose the true identity of\x01",
            "the man called Minneth.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_387C")

    TalkEnd(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3894")
    OP_93(0xC, 0x10E, 0x0)

    label("loc_3894")

    Return()

    # Function_12_3607 end

    def Function_13_3895(): pass

    label("Function_13_3895")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38AA")
    Call(0, 18)
    Jump("loc_3AD1")

    label("loc_38AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A0B")

    ChrTalk(
        0xD,
        (
            "#02200FThe evidence I'm looking for will\x01",
            "be insurance for after you've\x01",
            "tracked down Minneth.\x02\x03",
            "Anyway, you all should hurry to\x01",
            "Armorica.\x02\x03",
            "#02203FIf Minneth really is a crook, then\x01",
            "his plan may be advancing to its\x01",
            "final stage.\x02\x03",
            "#02200FHowever, I'm sure you guys will get\x01",
            "by with the evidence you already\x01",
            "have. I wish you good luck.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3AD1")

    label("loc_3A0B")


    ChrTalk(
        0xD,
        (
            "#02203FIf Minneth really is a crook, then\x01",
            "his plan may be advancing to its\x01",
            "final stage.\x02\x03",
            "#02200FHowever, I'm sure you guys will get\x01",
            "by with the evidence you already\x01",
            "have. I wish you good luck.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AD1")

    TalkEnd(0xFE)
    Return()

    # Function_13_3895 end

    def Function_14_3AD5(): pass

    label("Function_14_3AD5")

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
        "#11P#03802FHello~!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FHarold and Sophia. It's\x01",
            "been a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00102FHaha. Colin seems well.\x02",
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
            "#12P#10105FDo you and Elie know\x01",
            "this family?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FHehe. It looks like\x01",
            "something happened\x01",
            "between you.\x02",
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
            "#11P#03709FWe really appreciate\x01",
            "your help back then.\x02\x03",
            "#03700FEven now, the only\x01",
            "reason we're still here\x01",
            "is thanks to you.\x02",
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
            "#5P#03600FYou don't need to say that... I\x01",
            "mean, no matter what kind of thanks\x01",
            "I give you, it wouldn't be enough.\x02\x03",
            "#03608FOrdinarily, I would have wanted to\x01",
            "thank that girl that helped us as\x01",
            "well, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P#03805FThat violet-haired\x01",
            "girl~?\x02\x03",
            "#03809FI want to see her again\x01",
            "too~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#03700FHaha... that's right. I\x01",
            "too would like to see\x01",
            "her again.\x02\x03",
            "Might all of you know\x01",
            "her?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103F...I'm sorry to say,\x01",
            "but... We didn't see the\x01",
            "girl again after that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#03603FHmm, is that so...\x02\x03",
            "#03600FWell, if we are tied by\x01",
            "fate, we'll meet again,\x01",
            "right?\x02\x03",
            "I suppose all we can do\x01",
            "is be patient and wait\x01",
            "for that chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003F(..."That girl" has\x01",
            "already left Crossbell,\x01",
            "right?)\x02\x03",
            "#00008F(In the end, I can't\x01",
            "explain the situation to\x01",
            "the Hayworths, but...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#03600F...Well then, everyone.\x01",
            "Please don't hesitate to stop\x01",
            "by if you ever need anything.\x02\x03",
            "I will do anything in my\x01",
            "power to assist you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FSure, and thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11P#03809FEhehe, come again~.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0xA, 0x0)
    Sleep(50)
    SetScenarioFlags(0x12F, 7)
    EventEnd(0x5)
    Return()

    # Function_14_3AD5 end

    def Function_15_4218(): pass

    label("Function_15_4218")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44AD")

    ChrTalk(
        0x101,
        (
            "#00000FExcuse us, we're the\x01",
            "Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Oh the ladies and\x01",
            "gentlemen of the SSS...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Thanks for coming after\x01",
            "what happened yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#03600FThank you, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FChief, what exactly\x01",
            "happened?\x02\x03",
            "#00003FIt seems there's been\x01",
            "some developments in\x01",
            "yesterday's case.\x02",
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
            "request immediately. Do\x01",
            "you mind?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4532")

    label("loc_44AD")


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
            "request immediately. Do\x01",
            "you mind?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4532")

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

    # Function_15_4218 end

    def Function_16_4577(): pass

    label("Function_16_4577")

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
            "[Cancel]\x01",      # 1
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
        (0, "loc_45D9"),
        (1, "loc_45E1"),
        (SWITCH_DEFAULT, "loc_46AA"),
    )


    label("loc_45D9")

    Call(0, 17)
    Jump("loc_46AA")

    label("loc_45E1")


    ChrTalk(
        0x101,
        (
            "#00006FWe're terribly sorry,\x01",
            "but... We're a little\x01",
            "busy right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Hmm, I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Then, please come again\x01",
            "if you have time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If possible, I'd like\x01",
            "help from all of you.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x177, 1)

    label("loc_46AA")

    Return()

    # Function_16_4577 end

    def Function_17_46AB(): pass

    label("Function_17_46AB")


    ChrTalk(
        0x101,
        "#00000FNo, please fill us in.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYou said the situation's\x01",
            "changed since\x01",
            "yesterday...\x02",
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
            "who's staying at the inn, and tried\x01",
            "to persuade him once again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I pointed out to him the suspicious\x01",
            "points of Minneth and asked him to\x01",
            "stop associating with him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FYou gave it to 'im\x01",
            "straight, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Yes, but... In the end,\x01",
            "Derrick wouldn't listen.\x02",
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
            "I hurried to Harold's\x01",
            "place to discuss the\x01",
            "matter with him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205FSomething new?\x02\x03",
            "Did you figure out what\x01",
            "Minneth is up to?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03603FI was surprised too, once I\x01",
            "heard about it.\x02\x03",
            "#03601FIt seems that Minneth has\x01",
            "penetrated the village even\x01",
            "further than we thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FUmm... What do you mean,\x01",
            "exactly?\x02\x03",
            "We knew that Minneth had\x01",
            "gained the trust of the\x01",
            "villagers yesterday, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Actually, that Minneth\x01",
            "is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "After not just the private\x01",
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
        "#00005FAll of the deeds!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FHmm... If that's how it\x01",
            "is, it's quite concerning\x01",
            "indeed.\x02\x03",
            "#10301FJust how did Minneth\x01",
            "manage to get his hands\x01",
            "on such important things?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03601FYes, well based on what I've heard, he\x01",
            "called it the "lotus fields expansion\x01",
            "project".\x02\x03",
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
            "#10101FBased on what we heard\x01",
            "yesterday... We already\x01",
            "knew all of that.\x02\x03",
            "#10103FAt first glance it\x01",
            "seemed like a fine\x01",
            "idea...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FYeah... "Too good to be\x01",
            "true."\x02\x03",
            "#00003FAnd regarding those deeds...\x01",
            "If he abuses them then you\x01",
            "won't be able to recover.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Yes... Suspicion\x01",
            "continues to surround\x01",
            "Minneth.\x02",
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
            "#00301FI see. You could say\x01",
            "there's no way to escape\x01",
            "the agreement.\x02",
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
            "#00000FMinneth is only a little\x01",
            "suspicious... Allow us to\x01",
            "respectfully investigate him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Sorry... You all are\x01",
            "always helping us.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00100FThen, we should we start\x01",
            "investigating?\x02\x03",
            "#00103FWe don't have any clues\x01",
            "at the moment, to be\x01",
            "perfectly honest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FWe don't have anything\x01",
            "that could be called a\x01",
            "motive.\x02",
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
        "#00205FLawyer Ian?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03600FYes. Right now, all we know is that\x01",
            "Minneth is "suspicious."\x02\x03",
            "If you explain the situation to Lawyer\x01",
            "Ian, he might be able to detect some\x01",
            "hint of a crime in Minneth's actions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FI see... That's not a bad idea.\x02\x03",
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
            "#03608FIt's possible that he won't see\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FWell, let's go to his\x01",
            "law office anyway.\x02\x03",
            "We'll think about what\x01",
            "to do next if he really\x01",
            "is out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah... Let's pay him a\x01",
            "visit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03600FWe'll leave it to you then.\x02\x03",
            "I'll see if my business partners\x01",
            "have heard any rumors about\x01",
            "Quincy Company or Minneth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FThat would be great,\x01",
            "thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I'm terribly sorry...\x01",
            "You are the only ones\x01",
            "who can help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I am at a loss, unable\x01",
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
            "Chief.\x02\x03",
            "And pray to the Goddess\x01",
            "for some good news.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Alright... Thank you.\x02",
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
            "Quest [Investigating the\x01",
            "Suspicious Trader]\x07\x00\x01",
            "started!\x02",
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

    # Function_17_46AB end

    def Function_18_57C5(): pass

    label("Function_18_57C5")

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
        "Oh, it's you all...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P#02200FIt seems you've\x01",
            "returned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FLawyer Ian... You came.\x02\x03",
            "You're here too, Harold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03604FYes, I just finished asking\x01",
            "my business partners about\x01",
            "the current matter.\x02\x03",
            "#03601FHow are things on your end?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FThanks to Lawyer Ian, we\x01",
            "were able to find out a\x01",
            "few things.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00100FDid you find something\x01",
            "too, Harold?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#03603FYes... In a manner a\x01",
            "speaking.\x02\x03",
            "#03608FAlthough I don't know\x01",
            "what it means...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHaha, well you went to the\x01",
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
            "#03601FNot having any idea about the\x01",
            "name Minneth, I tried asking my\x01",
            "trading partners.\x02\x03",
            "When I did... It seems Minneth\x01",
            "has been studying a certain thing\x01",
            "ever since he came to Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FA certain thing... you\x01",
            "say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03601FYes, and that is... the\x01",
            ""price of land" in various\x01",
            "places throughout our state.\x02",
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
            "#10103FSo Minneth is looking\x01",
            "more like a real estate\x01",
            "agent...\x02\x03",
            "#10105FBut, why would he need\x01",
            "to look into something\x01",
            "like that...?\x02",
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
            "evidence as to Minneth's\x01",
            "objective.\x02",
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
            "#11P#02203FYes, that makes sense,\x01",
            "actually.\x02\x03",
            "#02200FI found out something\x01",
            "that may be useful as\x01",
            "well.\x02",
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
            "#11P#02200FHarold, Chief Tolta.\x02\x03",
            "Will you help me find\x01",
            "something in my office?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5FA3():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5FA3)
    Sleep(50)

    def lambda_5FB3():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5FB3)
    Sleep(300)

    ChrTalk(
        0x8,
        "#03605FLawyer Ian?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I don't particularly\x01",
            "mind, but... Is it that\x01",
            "important?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P#02203FWell, I don't think it\x01",
            "will be able to prove\x01",
            "anything, but...\x02\x03",
            "#02200FI think we can think of\x01",
            "it as insurance for\x01",
            "pinning down Minneth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FHuh? I don't really get\x01",
            "it, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P#02200FWell, I don't know if we'll be in\x01",
            "time, so try not to get your hopes\x01",
            "up.\x02\x03",
            "#02203FMore importantly, Special Support\x01",
            "Section. You had best hurry to\x01",
            "Armorica.\x02\x03",
            "#02200FIf Minneth really is a crook, then\x01",
            "his plan may be advancing to its\x01",
            "final stage.\x02\x03",
            "However, if it is you guys, I am\x01",
            "sure you'll be able to do something\x01",
            "with the evidence you have on hand.\x02",
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
            "Let's hurry to Armorica.\x02\x03",
            "We'll expose Minneth's true\x01",
            "colors and stop him from\x01",
            "making any more deals!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6308():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6308)
    Sleep(50)

    def lambda_6318():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6318)
    Sleep(50)

    def lambda_6328():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6328)
    Sleep(50)

    def lambda_6338():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6338)
    Sleep(50)

    def lambda_6348():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6348)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00101FYeah... Let's go!\x02",
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

    # Function_18_57C5 end

    SaveToFile()

Try(main)
