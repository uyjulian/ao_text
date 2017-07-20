from ScenarioHelper import *

def main():
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
        "Harold",               # 1
        "Sofia",               # 2
        "Choline",                 # 3
        "Cindy",               # 4
        "Mayor of Torta",             # 5
        "Ian lawyer",           # 6
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
        "Function_6_8EE",          # 06, 6
        "Function_7_16DD",         # 07, 7
        "Function_8_2809",         # 08, 8
        "Function_9_2906",         # 09, 9
        "Function_10_3383",        # 0A, 10
        "Function_11_3460",        # 0B, 11
        "Function_12_3585",        # 0C, 12
        "Function_13_37CB",        # 0D, 13
        "Function_14_3A12",        # 0E, 14
        "Function_15_4185",        # 0F, 15
        "Function_16_44C6",        # 10, 16
        "Function_17_45F7",        # 11, 17
        "Function_18_5641",        # 12, 18
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
            "There is a car magazine \"Monthly Carmania vol.1\".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('天空色彩', 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8EA")
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            "Paint pattern\x01\x07\x02",
            "\"Sky color\"\x07\x00",
            "I learned.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber('天空色彩', 1)

    label("loc_8EA")

    TalkEnd(0xFF)
    Return()

    # Function_5_846 end

    def Function_6_8EE(): pass

    label("Function_6_8EE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_CDD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BA2")

    ChrTalk(
        0x8,
        (
            "#03600FAw, everyone.\x01",
            "It is safe and than anything else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FMr. Harold, from the village of Almorika\x01",
            "You are back home, are not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03604FYes, seeing the barrier disappeared\x01",
            "I came back just a while ago.\x02\x03",
            "#03600FFrom now on\x01",
            "Although it is going out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00203FIt seems that you are busy indeed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FI also have families,\x01",
            "Even if you take it a bit more slowly\x01",
            "Is not it something you want?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03603FNo, even now even a little\x01",
            "Crossbells of everyone in the area\x01",
            "I thought that I want to become power.\x02\x03",
            "#03600FFor the beginning, to Mainz\x01",
            "I am going to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FIs that so……\x01",
            "As expected, Mr. Harold.\x02\x03",
            "#00002FPlease be careful, please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03609FYes, everyone ….\x01",
            "I pray for the protection of the goddess.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CD, 0)
    Jump("loc_CD8")

    label("loc_BA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C66")

    ChrTalk(
        0x8,
        (
            "#03600FFor the beginning, to Mainz\x01",
            "I am going to go.\x02\x03",
            "#03603FRight now everyone in our area\x01",
            "I thought that I want to be power …\x02\x03",
            "#03609FEveryone,\x01",
            "I pray for the protection of the goddess.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CD8")

    label("loc_C66")


    ChrTalk(
        0x8,
        (
            "#03600FFor the beginning, to Mainz\x01",
            "I am going to go.\x02\x03",
            "#03609FEveryone,\x01",
            "I pray for the protection of the goddess.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CD8")

    Jump("loc_16D9")

    label("loc_CDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_CEB")
    Jump("loc_16D9")

    label("loc_CEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_CF9")
    Jump("loc_16D9")

    label("loc_CF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_D07")
    Jump("loc_16D9")

    label("loc_D07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_EBE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E16")

    ChrTalk(
        0x8,
        (
            "#03601FI will go to Mainz today.\x01",
            "I was planning … ….\x01",
            "It will not be such a thing.\x02\x03",
            "#03603F…… To many transactions in Mainz\x01",
            "I have heard that, to the people of the town\x01",
            "I am doing very well.\x02\x03",
            "#03608FBut even though I can not do anything\x01",
            "It is a pitiful thought ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_EB9")

    label("loc_E16")


    ChrTalk(
        0x8,
        (
            "#03603F…… To many transactions in Mainz\x01",
            "I have heard that, to the people of the town\x01",
            "I am doing very well.\x02\x03",
            "#03608FBut even though I can not do anything\x01",
            "It is a pitiful thought ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EB9")

    Jump("loc_16D9")

    label("loc_EBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_ECC")
    Jump("loc_16D9")

    label("loc_ECC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_EDA")
    Jump("loc_16D9")

    label("loc_EDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_100E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_F7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F01")
    Call(0, 15)
    Jump("loc_F78")

    label("loc_F01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F13")
    Call(0, 18)
    Jump("loc_F78")

    label("loc_F13")


    ChrTalk(
        0x8,
        (
            "#03600FThe village mayor later, in my car\x01",
            "I will deliver it to the village.\x02\x03",
            "Everyone,\x01",
            "Please take care.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F78")

    Jump("loc_1009")

    label("loc_F7D")


    ChrTalk(
        0x8,
        (
            "#03601FAnyways,\x01",
            "What I found out after examining yesterday\x01",
            "Let's summarize.\x02\x03",
            "#03603FAlso, I went to Mr. Ian later\x01",
            "Those who consulted\x01",
            "It might be nice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1009")

    Jump("loc_16D9")

    label("loc_100E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_101C")
    Jump("loc_16D9")

    label("loc_101C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_102A")
    Jump("loc_16D9")

    label("loc_102A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_11FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_117A")

    ChrTalk(
        0x8,
        "#03605FAw, everyone.\x02",
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
            "#00104FA good smell from the second floor …\x01",
            "Wife prepares for dinner\x01",
            "It seems to be done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03609FWell, that's right.\x01",
            "And also today Colin\x01",
            "He seems to be helping.\x02\x03",
            "#03604FWell, I am from the outset\x01",
            "As I came back,\x01",
            "My stomach is stupid.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14A, 6)
    Jump("loc_11F7")

    label("loc_117A")


    ChrTalk(
        0x8,
        (
            "#03600FApparently today,\x01",
            "Colin is helping cooking\x01",
            "It looks like it.\x02\x03",
            "#03609FHehe, what kind of dish\x01",
            "I am looking forward to coming out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11F7")

    Jump("loc_16D9")

    label("loc_11FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_120A")
    Jump("loc_16D9")

    label("loc_120A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1218")
    Jump("loc_16D9")

    label("loc_1218")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_14EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1465")

    ChrTalk(
        0x8,
        (
            "#03603FIn this way alone\x01",
            "While being quiet,\x01",
            "There is a thing to think.\x02\x03",
            "He says that he helped Collin before.\x01",
            "Violet color hair girl ……\x02\x03",
            "#03608FTo meet that child is\x01",
            "Is it really impossible?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FWell, that is ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03604FHaha, for now\x01",
            "Because there is no clue,\x01",
            "It is only hope.\x02\x03",
            "#03600FIf there was such a chance ……\x01",
            "By all means I would like to thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F(Violet color hair girl ……\x01",
            "Len with the esters\x01",
            "You returned to Libert … …)\x02\x03",
            "#00003F(That girl still has a feeling of arrangement\x01",
            "I guess it is necessary, but …\x01",
            "I hope someday that day will come. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x134, 0)
    Jump("loc_14E9")

    label("loc_1465")


    ChrTalk(
        0x8,
        (
            "#03603FHe says that he helped Collin before.\x01",
            "Violet color hair girl ……\x02\x03",
            "#03600FIf the day is coming,\x01",
            "By all means I would like to thank you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14E9")

    Jump("loc_16D9")

    label("loc_14EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_16D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_150D")
    TalkEnd(0xFE)
    Call(0, 14)
    Return()

    label("loc_150D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1660")

    ChrTalk(
        0x8,
        (
            "#03600FRecently, business has turned upward\x01",
            "It was getting on.\x02\x03",
            "#03604FThus taking a day off\x01",
            "We can afford to provide family services\x01",
            "It is done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FHuhu, Mr. Harold's solid attitude\x01",
            "I guess they have fruit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03609FHaha, that is … …\x01",
            "I am honestly itchy.\x02\x03",
            "#03600FAt the very least, even if my family can nurture it\x01",
            "That alone is sufficient.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16D9")

    label("loc_1660")


    ChrTalk(
        0x8,
        (
            "#03600FEveryone, if there is something again\x01",
            "Please come over here by all means.\x02\x03",
            "If I can become a force\x01",
            "Because I will help you anything.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16D9")

    TalkEnd(0xFE)
    Return()

    # Function_6_8EE end

    def Function_7_16DD(): pass

    label("Function_7_16DD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_187E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17D9")

    ChrTalk(
        0x9,
        (
            "#03708FIf you go a little more slowly,\x01",
            "Well, I think ….\x02\x03",
            "#03700FThat gentle and attentive skill\x01",
            "It is a person named Harold Hayworth.\x02\x03",
            "#03709FIf my husband wishes to be powerful of everyone,\x01",
            "We just support it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1879")

    label("loc_17D9")


    ChrTalk(
        0x9,
        (
            "#03700FThat gentle and attentive skill\x01",
            "It is a person named Harold Hayworth.\x02\x03",
            "#03709FIf my husband wishes to be powerful of everyone,\x01",
            "We just support it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1879")

    Jump("loc_2805")

    label("loc_187E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_188C")
    Jump("loc_2805")

    label("loc_188C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1916")

    ChrTalk(
        0x9,
        (
            "#03708FFrom now on, what will happen\x01",
            "I guess …\x02\x03",
            "#03710FIf anything happens to my husband or Colin ……\x01",
            "Anyway I am only worried about that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2805")

    label("loc_1916")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1A93")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19F9")

    ChrTalk(
        0x9,
        (
            "#03700FToday my husband got to Mainz\x01",
            "I am going to see the state.\x02\x03",
            "Upon receiving the recent raid incident,\x01",
            "As much as possible to yourself\x01",
            "She seems to be doing … …\x02\x03",
            "#03709FAs for a gentle master,\x01",
            "I am proud again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A8E")

    label("loc_19F9")


    ChrTalk(
        0x9,
        (
            "#03700FThe master received a raid incident,\x01",
            "As much as possible to yourself\x01",
            "It seems to be trying to do.\x02\x03",
            "#03709FAs for a gentle master,\x01",
            "I am proud again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A8E")

    Jump("loc_2805")

    label("loc_1A93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1BC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B76")

    ChrTalk(
        0x9,
        (
            "#03708FA moment when I heard the report of the incident\x01",
            "\"It was good that my husband was not involved\"\x01",
            "I thought that.\x02\x03",
            "Right now at this moment,\x01",
            "People in Mainz to fear\x01",
            "Even though I'm frightened …\x02\x03",
            "#03710F… … I hate myself.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1BBF")

    label("loc_1B76")


    ChrTalk(
        0x9,
        (
            "#03708F……Anyways,\x01",
            "I will make sure that the case will be settled as soon as possible.\x01",
            "Let's pray to the goddess.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BBF")

    Jump("loc_2805")

    label("loc_1BC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1C6B")

    ChrTalk(
        0x9,
        (
            "#03700FMy husband headed towards the Belgard gate today.\x01",
            "We are going to wholesale merchandise.\x02\x03",
            "#03708FYesterday there was a gigantic thing in the west road\x01",
            "I heard she was witnessed,\x01",
            "I am a little worried … …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2805")

    label("loc_1C6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1E87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D7A")

    ChrTalk(
        0x9,
        (
            "#03705FOh, everyone?\x02\x03",
            "If you are the master, with the village headman\x01",
            "I headed to Almorika village … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(To the end of the investigation\x01",
            "I wanted to go out with him ……\x01",
            "Confirmation of the accident is the top priority now. )\x02\x03",
            "(In Almorika village\x01",
            "I have no choice but to leave Mr. Harold. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16C, 7)
    Jump("loc_1E82")

    label("loc_1D7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E26")

    ChrTalk(
        0x9,
        (
            "#03700FCindy came by a while ago\x01",
            "It taught me ……\x02\x03",
            "A lot of ambulances\x01",
            "It is said that they passed through Nishi-dori.\x02\x03",
            "#03708FIt makes me cranky …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E82")

    label("loc_1E26")


    ChrTalk(
        0x9,
        (
            "#03708FA lot of ambulances\x01",
            "It is said that they passed through Nishi-dori.\x02\x03",
            "It makes me cranky …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E82")

    Jump("loc_2805")

    label("loc_1E87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_21CE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1FD0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F4D")

    ChrTalk(
        0x9,
        (
            "#03700FThere was contact from my husband earlier.\x01",
            "In the case of Almorika village\x01",
            "I heard that it was settled alright.\x02\x03",
            "#03708FAnyway, it's a fraud … …\x01",
            "There was a really bad person.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1FCB")

    label("loc_1F4D")


    ChrTalk(
        0x9,
        (
            "#03700FIn the case of Almorika village\x01",
            "I heard that it was settled alright.\x02\x03",
            "#03708FAnyway, it's a fraud … …\x01",
            "There was a really bad person.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FCB")

    Jump("loc_21C9")

    label("loc_1FD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2060")

    ChrTalk(
        0x9,
        (
            "#03700FThe village mayor's son\x01",
            "Something is caught up in a trouble\x01",
            "Looks like it …\x02\x03",
            "#03708FEarly place\x01",
            "I hope to work on solutions.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21C9")

    label("loc_2060")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_213C")

    ChrTalk(
        0x9,
        (
            "#03700FMuraagaya, thinking very much\x01",
            "You seem to come …\x02\x03",
            "#03708FBecause it is about my son,\x01",
            "Naturally it is natural … …\x02\x03",
            "#03700FToo much worry will hurt your body,\x01",
            "I have to settle for the moment.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_21C9")

    label("loc_213C")


    ChrTalk(
        0x9,
        (
            "#03700FToo much worry will hurt your body,\x01",
            "I have to settle for the moment.\x02\x03",
            "Certainly, herbal tea with sedative effect\x01",
            "It should have had a reserve …\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21C9")

    Jump("loc_2805")

    label("loc_21CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2276")

    ChrTalk(
        0x9,
        (
            "#03700FFrom the village chief of Almorika village\x01",
            "There was contact with my husband.\x02\x03",
            "There seems to be some consultation … …\x01",
            "It seems not to be a business talk,\x01",
            "What on earth happened … ….\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2805")

    label("loc_2276")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_23AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_233C")

    ChrTalk(
        0x9,
        (
            "#03700FLast night, with Collin\x01",
            "I made curry ……\x02\x03",
            "I wonder if it made a little bit.\x01",
            "There seems to be quite a few extra.\x02\x03",
            "#03709FHuhu, for a while\x01",
            "It looks like the day of curry will continue.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_23AA")

    label("loc_233C")


    ChrTalk(
        0x9,
        (
            "#03700FLast night's curry ……\x01",
            "I wonder if it made a little bit.\x02\x03",
            "#03709FHuhu, for a while\x01",
            "It looks like the day of curry will continue.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23AA")

    Jump("loc_2805")

    label("loc_23AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_242C")

    ChrTalk(
        0x9,
        (
            "#03700FLet's just wait for boiling.\x02\x03",
            "#03709FHehe, well done, Colin.\x01",
            "I'm sure Papa will be pleased.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2805")

    label("loc_242C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_24B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2447")
    Call(0, 8)
    Jump("loc_24AF")

    label("loc_2447")


    ChrTalk(
        0x9,
        (
            "#03700FFrom now on shopping a bit\x01",
            "I'm going.\x02\x03",
            "#03709FHuhuu, Colin said\x01",
            "It is cramped.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24AF")

    Jump("loc_2805")

    label("loc_24B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2612")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_257D")

    ChrTalk(
        0x9,
        (
            "#03700FIn the meantime, I stayed in the neighborhood\x01",
            "Mr. Crayy came to see me.\x02\x03",
            "At last the life seemed calm,\x01",
            "She seemed to be very relieved ……\x02\x03",
            "#03709FHehe, I am relieved.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_260D")

    label("loc_257D")


    ChrTalk(
        0x9,
        (
            "#03700FMr. Kreil,\x01",
            "Now to the apartment in east street\x01",
            "Do you live in Japan?\x02\x03",
            "It seems pretty familiar,\x01",
            "I was relieved for the time being.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_260D")

    Jump("loc_2805")

    label("loc_2612")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_277B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26F2")

    ChrTalk(
        0x9,
        (
            "#03700FThe Bond family who were in the neighborhood\x01",
            "I moved a while ago.\x02\x03",
            "#03708FWhen we are leaving home\x01",
            "I came to say hello ……\x01",
            "Then I have not heard from you yet.\x02\x03",
            "I hope you are doing well, but ….\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2776")

    label("loc_26F2")


    ChrTalk(
        0x9,
        (
            "#03700FWith Mr. Bond's wife,\x01",
            "Do cooking together\x01",
            "They were very close.\x02\x03",
            "#03708FI hope you are doing well, but ….\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2776")

    Jump("loc_2805")

    label("loc_277B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2805")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_279A")
    TalkEnd(0xFE)
    Call(0, 14)
    Return()

    label("loc_279A")


    ChrTalk(
        0x9,
        (
            "#03700FPreviously, to everyone\x01",
            "I was deeply indebted to you.\x02\x03",
            "Together with my husband\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2805")

    TalkEnd(0xFE)
    Return()

    # Function_7_16DD end

    def Function_8_2809(): pass

    label("Function_8_2809")

    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    ChrTalk(
        0x9,
        (
            "#03700FLook, Colin, what are you today?\x01",
            "Did you go buy it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#03805FLet me see … …\x01",
            "To the carrots, potatoes,\x01",
            "Onions …\x02\x03",
            "#03809F…… Curry's roux!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#03709FHehe, the correct answer.\x01",
            "Shall I go then?\x02",
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

    # Function_8_2809 end

    def Function_9_2906(): pass

    label("Function_9_2906")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2A43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29C7")

    ChrTalk(
        0xA,
        (
            "#03800FFor Dad to go to work,\x01",
            "I am making lunch with my mother.\x02\x03",
            "#03809FCamille Kunch's lady\x01",
            "I got a lot of vegetables ~.\x01",
            "Well, that's good taste.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2A3E")

    label("loc_29C7")


    ChrTalk(
        0xA,
        (
            "#03800FI also want to go to Almorika village ~.\x02\x03",
            "#03809FWith Camille and Puri-chan\x01",
            "I made a promise to play again ~.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A3E")

    Jump("loc_337F")

    label("loc_2A43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2A51")
    Jump("loc_337F")

    label("loc_2A51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2ACA")

    ChrTalk(
        0xA,
        (
            "#03805FPapa and Mama,\x01",
            "I hesitate to worry ~.\x02\x03",
            "Although I am going to play now,\x01",
            "What's wrong?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_337F")

    label("loc_2ACA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2BDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B72")

    ChrTalk(
        0xA,
        (
            "#03800FNext time,\x01",
            "With Dad and Mama\x01",
            "I'm going to go play.\x02\x03",
            "#03809FIt's a very beautiful place ~.\x01",
            "I'm looking forward to it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2BD7")

    label("loc_2B72")


    ChrTalk(
        0xA,
        (
            "#03800FNext time ~, In a beautiful place\x01",
            "I'm going to go play.\x02\x03",
            "#03809FIt's exciting … fun.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BD7")

    Jump("loc_337F")

    label("loc_2BDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2C6C")

    ChrTalk(
        0xA,
        (
            "#03800FDad, today\x01",
            "I told you I did a job,\x01",
            "It seems I have not done it yet ~.\x02\x03",
            "#3802FPerhaps,\x01",
            "I wonder if it became good night ~?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_337F")

    label("loc_2C6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2CD7")

    ChrTalk(
        0xA,
        (
            "#03802Flook look,\x01",
            "A frog sticks to the window ~.\x02\x03",
            "#03809FIt is cute and it is cute.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_337F")

    label("loc_2CD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2D5B")

    ChrTalk(
        0xA,
        (
            "#03802FCindy's older sister\x01",
            "I made cookies\x01",
            "You brought me ~.\x02\x03",
            "#03809FHurry up, please!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_337F")

    label("loc_2D5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2F2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DD8")

    ChrTalk(
        0xA,
        (
            "#03800FToday is fine.\x01",
            "Because I have a story\x01",
            "Be on the second floor, though.\x02\x03",
            "Is it strange about the job?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F28")

    label("loc_2DD8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2E3E")

    ChrTalk(
        0xA,
        (
            "#03805FI also play with myself\x01",
            "I got awkward ~.\x02\x03",
            "Dad, quickly\x01",
            "I wonder if it will come back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F28")

    label("loc_2E3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EB7")

    ChrTalk(
        0xA,
        (
            "#03805FOh, in a place like this\x01",
            "There was honey ~.\x02\x03",
            "#03809FHello.\x01",
            "Well, sweet and savory.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    ClearChrFlags(0xA, 0x10)
    Jump("loc_2F28")

    label("loc_2EB7")


    ChrTalk(
        0xA,
        (
            "#03809FThis honey, during this period\x01",
            "Dad is a souvenir\x01",
            "I brought it back ~.\x02\x03",
            "My honey, I love you ~.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F28")

    Jump("loc_337F")

    label("loc_2F2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3028")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FCE")

    ChrTalk(
        0xA,
        (
            "#03805FDad, today was good night\x01",
            "I went somewhere ~.\x02\x03",
            "Bad misfortune\x01",
            "I wonder if it has arrived?\x01",
            "Disappointing ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3023")

    label("loc_2FCE")


    ChrTalk(
        0xA,
        (
            "#03805FToday I will be playing with my dad\x01",
            "It was a promise, though.\x01",
            "Disappointing ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3023")

    Jump("loc_337F")

    label("loc_3028")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3086")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3043")
    Call(0, 10)
    Jump("loc_3081")

    label("loc_3043")


    ChrTalk(
        0xA,
        (
            "#03809FTo Cindy Onee\x01",
            "I was praised.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3081")

    Jump("loc_337F")

    label("loc_3086")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_3109")

    ChrTalk(
        0xA,
        (
            "#03802FToday 's dinner is\x01",
            "It's curry.\x02\x03",
            "#03809FEh, I\x01",
            "I cut a piece of chicken ~.\x01",
            "Is not it amazing?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_337F")

    label("loc_3109")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_31B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3124")
    Call(0, 8)
    Jump("loc_31AF")

    label("loc_3124")


    ChrTalk(
        0xA,
        (
            "#03800FToday,\x01",
            "I am dinner.\x01",
            "Do not hesitate to call me ~.\x02\x03",
            "#03809FPapa returning from your job\x01",
            "I will surprise you ~.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31AF")

    Jump("loc_337F")

    label("loc_31B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3231")

    ChrTalk(
        0xA,
        (
            "#03800FToday is my dad, a job shirt ~.\x02\x03",
            "#03802FAlso, souvenirs\x01",
            "I wonder if it will come back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_337F")

    label("loc_3231")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_32E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_329D")

    ChrTalk(
        0xA,
        (
            "#03802FHey, peck.\x02\x03",
            "#03809FMunching …\x01",
            "Well, it is very tasty ~.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_32DF")

    label("loc_329D")


    ChrTalk(
        0xA,
        (
            "#03809FEh, after all mommy,\x01",
            "The cake is good ~.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32DF")

    Jump("loc_337F")

    label("loc_32E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_337F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3303")
    TalkEnd(0xFE)
    Call(0, 14)
    Return()

    label("loc_3303")


    ChrTalk(
        0xA,
        (
            "#03805FTalking, that again\x01",
            "To violet color older sister\x01",
            "I wanted to see you ~.\x02\x03",
            "#03809FWell, you can meet again someday.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_337F")

    TalkEnd(0xFE)
    Return()

    # Function_9_2906 end

    def Function_10_3383(): pass

    label("Function_10_3383")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    ChrTalk(
        0xA,
        (
            "#03802FCindy 's older sister.\x02\x03",
            "Yes, I cooked curry yesterday.\x01",
            "I made it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Oh, Colin?\x01",
            "Wow wow!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "This is more than our older brother.\x01",
            "You can cook very well.\x02",
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

    # Function_10_3383 end

    def Function_11_3460(): pass

    label("Function_11_3460")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_352B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_347E")
    Call(0, 10)
    Jump("loc_3526")

    label("loc_347E")


    ChrTalk(
        0xFE,
        (
            "Huhu, Mr. Sofia for today\x01",
            "How to make delicious sweets\x01",
            "I am going to tell you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway Colin,\x01",
            "It's great though it's small …\x01",
            "I want to make him an apprentice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3526")

    Jump("loc_3581")

    label("loc_352B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3581")

    ChrTalk(
        0xFE,
        (
            "Oh, Colin, you\x01",
            "I'm going to eat something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Huh, you mischievous ~.\x02",
    )

    CloseMessageWindow()

    label("loc_3581")

    TalkEnd(0xFE)
    Return()

    # Function_11_3460 end

    def Function_12_3585(): pass

    label("Function_12_3585")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_37B2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x82, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35DD")

    ChrTalk(
        0xFE,
        (
            "Sorry, Harold.\x01",
            "Do not bother you …\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37B2")

    label("loc_35DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35EF")
    Call(0, 15)
    Jump("loc_37B2")

    label("loc_35EF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_36A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_361B")
    Call(0, 18)
    Jump("loc_369B")

    label("loc_361B")


    ChrTalk(
        0xFE,
        (
            "I am Professor Ian\x01",
            "After helping the object,\x01",
            "Let's face the village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "You …\x01",
            "About Derrick\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_369B")

    Jump("loc_37B2")

    label("loc_36A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3749")

    ChrTalk(
        0xFE,
        (
            "Being the village head of Armorica,\x01",
            "Derrick's father, I\x01",
            "It is not good to not do anything ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please, I beg you.\x01",
            "Uncover the identity of a man named Minnes.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_37B2")

    label("loc_3749")


    ChrTalk(
        0xFE,
        "Please let me know what I can do to help\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Please, I beg you.\x01",
            "Uncover the identity of a man named Minnes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37B2")

    TalkEnd(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_37CA")
    OP_93(0xC, 0x10E, 0x0)

    label("loc_37CA")

    Return()

    # Function_12_3585 end

    def Function_13_37CB(): pass

    label("Function_13_37CB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37E0")
    Call(0, 18)
    Jump("loc_3A0E")

    label("loc_37E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3950")

    ChrTalk(
        0xD,
        (
            "#02200FThe evidence I am looking for is\x01",
            "After pursuing minnes and lions,\x01",
            "It may become extent of pushing.\x02\x03",
            "Anyway, you guys in Almorika village\x01",
            "You'd better hurry.\x02\x03",
            "#02203FIf the man named Minnes is really a fraudster,\x01",
            "Plan to the final phase\x01",
            "It may not be amazing.\x02\x03",
            "#02200FBut, surely you guys\x01",
            "I can do something with the evidence I have.\x01",
            "I will pray for a good fight.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3A0E")

    label("loc_3950")


    ChrTalk(
        0xD,
        (
            "#02203FIf the man named Minnes is really a fraudster,\x01",
            "Plan to the final phase\x01",
            "It may not be amazing.\x02\x03",
            "#02200FBut, surely you guys\x01",
            "I can do something with the evidence I have.\x01",
            "I will pray for a good fight.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A0E")

    TalkEnd(0xFE)
    Return()

    # Function_13_37CB end

    def Function_14_3A12(): pass

    label("Function_14_3A12")

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
        "#11P#03705FOh, you are …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P#03609FOh, everyone in the support department!\x02",
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
            "#12P#00000FLong time no see,\x01",
            "Mr. Harold, Sophia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00102FHuhu, Colin, you too\x01",
            "You look nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#03600FThanks to you……\x01",
            "Since then, there is nothing wrong\x01",
            "I live peacefully.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10105FLloyd's,\x01",
            "With this family\x01",
            "You seem to know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FHuh, what?\x01",
            "It seems there were various things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#03600FYes, to the support department\x01",
            "When Collin was missing in the past\x01",
            "Thank you for your help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#03709FThat section is really\x01",
            "Thank you very much.\x02\x03",
            "#03700FNow, being able to stay like this,\x01",
            "I think that you owe it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012FNo……\x01",
            "We have such a big deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#03600FPlease do not say that … …\x01",
            "Indeed, no matter how much you appreciate it\x01",
            "It is not enough.\x02\x03",
            "#03608FIf true, at that time\x01",
            "Even girls who helped out\x01",
            "I want to thank you … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P#03805FPerhaps,\x01",
            "About the violet color older sister ~?\x02\x03",
            "#03809FI also want to see you again ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P#03700FHehe … … That's right.\x01",
            "I also want to see you once.\x02\x03",
            "About you, everyone\x01",
            "Do you not know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00103F……Unfortunately……\x01",
            "About her then,\x01",
            "I did not see us either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#03603FHmm, is that so ……\x02\x03",
            "#03600FWell, if you have an edge\x01",
            "Someday you will meet.\x02\x03",
            "I only have to wait for that opportunity\x01",
            "It may not be there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003F(… … \"That child\"\x01",
            "Already already crossbell\x01",
            "You got away … …)\x02\x03",
            "#00008F(After all, Mr. Harold also\x01",
            "Without talking about circumstances\x01",
            "It seems it was … ….)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#03600F… Then, everyone.\x01",
            "If there is something,\x01",
            "Please come at any time.\x02\x03",
            "If I can become a force\x01",
            "Because I will help you anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYeah, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#11P#03809FEh, come back again ~.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0xA, 0x0)
    Sleep(50)
    SetScenarioFlags(0x12F, 7)
    EventEnd(0x5)
    Return()

    # Function_14_3A12 end

    def Function_15_4185(): pass

    label("Function_15_4185")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4403")

    ChrTalk(
        0x101,
        (
            "#00000FExcuse me,\x01",
            "It is a special support support section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Oh the SSS again\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Continuing from yesterday,\x01",
            "Thank you for coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#03600FThank you all again\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FMayor of Torta,\x01",
            "What on earth happened?\x02\x03",
            "#00003FApparently about the case of yesterday\x01",
            "It seems there was progress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well … apparently the situation\x01",
            "Beyond what I thought\x01",
            "It seems that it was getting serious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "About quick request\x01",
            "I'd like to talk ……\x01",
            "Do you mind?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4481")

    label("loc_4403")


    ChrTalk(
        0xC,
        (
            "Apparently the situation is\x01",
            "Beyond what I thought\x01",
            "It seems that it became serious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "About quick request\x01",
            "I'd like to talk ……\x01",
            "Do you mind?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4481")

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

    # Function_15_4185 end

    def Function_16_44C6(): pass

    label("Function_16_44C6")

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
            "【undertake】\x01",      # 0
            "【quit】\x01",          # 1
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
        (0, "loc_4530"),
        (1, "loc_4538"),
        (SWITCH_DEFAULT, "loc_45F6"),
    )


    label("loc_4530")

    Call(0, 17)
    Jump("loc_45F6")

    label("loc_4538")


    ChrTalk(
        0x101,
        (
            "#00006FI'm sorry……\x01",
            "I am a little busy now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "No … No …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Then, when time comes\x01",
            "Please come again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "By all means to you guys\x01",
            "I'd like you to lend me the power.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x177, 1)

    label("loc_45F6")

    Return()

    # Function_16_44C6 end

    def Function_17_45F7(): pass

    label("Function_17_45F7")


    ChrTalk(
        0x101,
        "#00000FYes, please fill us in\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FSince yesterday, the situation has developed\x01",
            "It was ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Yes that's right\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Last night, I stayed at a hotel tavern\x01",
            "Go to Derrick's place\x01",
            "I tried persuading again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "That foreigner named Mininness\x01",
            "Because there are many suspicious places,\x01",
            "Stop going out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FAbsolutely …\x01",
            "I told you straight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Oh, but … ….\x01",
            "Derrick end up listening carefully\x01",
            "I did not have it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Instead,\x01",
            "I have given some new facts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hurry up, to Harold\x01",
            "I was about to consult him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00205FA new fact?\x02\x03",
            "A person named that Minnes\x01",
            "Does that mean you were doing something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03603FWhen I was consulted\x01",
            "I was also surprised … …\x02\x03",
            "#03601FMr. Minnes, apparently more than I expected\x01",
            "It seems that he was digging into the village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00105FEr …\x01",
            "In other words, what is it?\x02\x03",
            "To get credit to the villagers\x01",
            "I understood at the stage of yesterday, but ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Actually that Minnes guy is\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "In addition to the private property of the village,\x01",
            "The field and the land rights document\x01",
            "You seem to have been collecting it.\x02",
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
        "#00005FDeeds for plots of lands!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303FHmm … … but then\x01",
            "There are points to worry about.\x02\x03",
            "#10301FMinnes-san how is he doing\x01",
            "Such an important thing\x01",
            "I wonder if you got it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03601FYes, according to what I hear ……\x01",
            "The nominal is \"expansion of the astragalus field\"\x01",
            "It seems to be said that.\x02\x03",
            "Gather land of the field little by little from the villager,\x01",
            "By expanding the astragalus field\x01",
            "It makes its harvest more efficient …\x02\x03",
            "#03603FFurthermore, management of the field\x01",
            "By being contracted by Quincy\x01",
            "We can reduce labor such as harvest … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10101FThat area ……\x01",
            "It also leads to stories you heard yesterday.\x02\x03",
            "#10103FBut it seemed like a perfectly valid thing yesterday\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FAh……\x01",
            "It is also \"a story that is too good\".\x02\x03",
            "#00003FMoreover, when it comes to land rights … …\x01",
            "If it were to be abused\x01",
            "It will be irreparable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well … … The suspicion of a man named Minneshi\x01",
            "It is a situation where it has not been dispelled at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "If it is private land alone,\x01",
            "Even if something happens\x01",
            "There are few human injuries … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "On the land inside the village\x01",
            "That such a thing is going on\x01",
            "You did not expect it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301FIndeed, if you are a nice guy\x01",
            "It might be a situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "So, to you\x01",
            "The identity of that man in a clearer form\x01",
            "I want to have it exposed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "In the current situation that the charges have not been finalized\x01",
            "This kind of thing to the police\x01",
            "Is it something I can ask …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FNo … Originally we are\x01",
            "It is out of the discipline of the police.\x02\x03",
            "#00000FTo a man named Minnes\x01",
            "The current situation that there is a doubtful point even a little … ….\x01",
            "We will deeply hit the investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Sorry ….\x01",
            "To you\x01",
            "I am sure I will take care of it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00100FWell then, where from\x01",
            "I wonder if I can put on my hands?\x02\x03",
            "#00103FTo be honest, for now\x01",
            "I do not have any clues … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FCertainly, the basis can be said\x01",
            "There is nothing there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FThat's true\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03600FWell then, everyone ….\x01",
            "First to Professor Ian\x01",
            "How about consulting?\x02",
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
        "#00205FIan-sensei?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03600FYeah, now a man named Minnes\x01",
            "Only things like \"doubtful\"\x01",
            "I do not know but …\x02\x03",
            "If I explain the situation to Professor Ian,\x01",
            "Signs for some kind of crime\x01",
            "You may be able to read it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FI see……\x01",
            "It might be a good idea.\x02\x03",
            "#00000FTo what he is going to do\x01",
            "If you approach even a little,\x01",
            "It may be the beginning of the investigation ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03603FHowever, Professor Ian recently,\x01",
            "In connection with the independent declaration of the example\x01",
            "It seems to be considerably busy.\x02\x03",
            "#03608FMaybe, I can not come\x01",
            "There is a possibility, but …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FWell, whatever.\x01",
            "Let's go to a law firm.\x02\x03",
            "If it does not exist,\x01",
            "At that time think about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FAh……\x01",
            "Let's visit quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03600FThen, there\x01",
            "Thank you for your consideration.\x02\x03",
            "I also like business associates\x01",
            "Rumors of Quincy and Minnes\x01",
            "I think I will try it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FThat … … it is saved.\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Sorry ….\x01",
            "You only depend on us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I can not do anything\x01",
            "It is not pretty ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHouse……\x01",
            "Please leave it to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FWell, the village mayor here\x01",
            "I hope you are waiting.\x02\x03",
            "You can do a good report\x01",
            "Please pray to the goddess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Well …\x01",
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
            "Quest 【Investigation of suspicious merchant】\x07\x00",
            "I started!\x02",
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

    # Function_17_45F7 end

    def Function_18_5641(): pass

    label("Function_18_5641")

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
        "Oh, you guys\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#11P#02200FIt seems you made it back\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FMr. Ian … …\x01",
            "You came, did not you?\x02\x03",
            "Harold also\x01",
            "It seems they came back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03604FYeah, to a business associate as usual\x01",
            "Because listening has ended.\x02\x03",
            "#03601FDid you come across some details?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, thanks to you.\x01",
            "I was able to grasp various things.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#00100FIn Harold's way\x01",
            "Have you understood anything?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#03603FYes, a bit\x02\x03",
            "#03608FEven so,\x01",
            "What does this mean …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHuh, it's information.\x01",
            "Try talking about anything you want\x01",
            "Is not it nice?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FYes, please.\x01",
            "With current information\x01",
            "It might be connected.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#03603FThat's right\x02\x03",
            "#03601FI am named Minnes\x01",
            "I do not recognize it,\x01",
            "I asked for trade friends.\x02\x03",
            "Then … apparently Mr. Minnes,\x01",
            "By the time I entered the crossbell,\x01",
            "It seems that I was investigating something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FSomething…?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#03601FYeah, that is ……\x01",
            "Crossbells throughout the region\x01",
            "It seems that it is \"land price\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305FPrice of land….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103FMr. Minnes is like a real estate agent\x01",
            "It was a translation that you were doing … …\x02\x03",
            "#10105FBut why is that such a thing\x01",
            "It is necessary to investigate ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00001Fperhaps……\x01",
            "This will lead to the purpose of Minnes\x01",
            "It may be an important testimony.\x02",
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
        "R-really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P#02203FYes, that makes sense actually\x02\x03",
            "#02200FBesides, even by me\x01",
            "I found something useful.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x5A, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00005FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P#02200FHarold, and Chief Torta\x02\x03",
            "From now on in my office,\x01",
            "Will not you help me with the thing you want?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5DEC():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5DEC)
    Sleep(50)

    def lambda_5DFC():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_5DFC)
    Sleep(300)

    ChrTalk(
        0x8,
        "#03605FIan…\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "I do not mind …\x01",
            "Is it something important?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P#02203FNo, that is decisive\x01",
            "It will not be a proof … …\x02\x03",
            "#02200FAfter pursuing minnes and lions,\x01",
            "It may become extent of pushing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305FWhat? I do not know well …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#11P#02200FWell, I do not know how to make it.\x01",
            "Do not expect too much.\x02\x03",
            "#02203FMore than that, the support department.\x01",
            "You guys in Almorika village\x01",
            "You'd better hurry.\x02\x03",
            "#02200FIf the man named Minnes is really a fraudster,\x01",
            "Plan to the final phase\x01",
            "It may not be amazing.\x02\x03",
            "But, surely you guys,\x01",
            "I can do something with the evidence I have.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FThat makes sense, thank you!\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00001FWell then, everyone ….\x01",
            "Let's head to Armorika village.\x02\x03",
            "Revealing the identity of that minnes,\x01",
            "Do not stop any further transactions!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_610C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_610C)
    Sleep(50)

    def lambda_611C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_611C)
    Sleep(50)

    def lambda_612C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_612C)
    Sleep(50)

    def lambda_613C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_613C)
    Sleep(50)

    def lambda_614C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_614C)
    Sleep(300)

    ChrTalk(
        0x102,
        "#00101FYes, let's go!\x02",
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

    # Function_18_5641 end

    SaveToFile()

Try(main)
