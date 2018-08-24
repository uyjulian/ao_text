from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t2020.bin",                # FileName
        "t2020",                    # MapName
        "t2020",                    # Location
        0x0059,                     # MapIndex
        "ed7126",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1C,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 89, 0, 2, 0, 3],
    )

    BuildStringList((
        "t2020",                  # 0
        "Warrant Officer Mireille",# 1
        "2nd Lt. Mireille",       # 2
        "Commander Sonya",        # 3
        "Soldier Romeo",          # 4
        "2nd Lt. Noｱl",          # 5
        "Vice Commander Douglas", # 6
    ))

    AddCharChip((
        "chr/ch32600.itc",                   # 00
        "chr/ch05702.itc",                   # 01
        "chr/ch41400.itc",                   # 02
    ))

    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(4294967046, 0,       1409,    0,    389,  0x0, 0,   2,   0,   0,   1,   0,   9,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(48900,   0,       4294940036, 1200,    48900,   850,     4294940036, 0x007C, 0,  4,  0x0000)
    DeclActor(4294965296, 0,       4294962776, 1200,    4294965296, 1000,    4294962776, 0x007C, 0,  14, 0x0000)
    DeclActor(4294928546, 0,       0,       1200,    4294926996, 1500,    0,       0x007E, 0,  7,  0x0000)

    ChipFrameInfo(496, 0)                                        # 0

    ScpFunction((
        "Function_0_1F0",          # 00, 0
        "Function_1_2A0",          # 01, 1
        "Function_2_301",          # 02, 2
        "Function_3_511",          # 03, 3
        "Function_4_629",          # 04, 4
        "Function_5_6F0",          # 05, 5
        "Function_6_CB6",          # 06, 6
        "Function_7_16D3",         # 07, 7
        "Function_8_16D7",         # 08, 8
        "Function_9_268E",         # 09, 9
        "Function_10_2877",        # 0A, 10
        "Function_11_3ED5",        # 0B, 11
        "Function_12_4BC2",        # 0C, 12
        "Function_13_55FB",        # 0D, 13
        "Function_14_5BFF",        # 0E, 14
    ))


    def Function_0_1F0(): pass

    label("Function_0_1F0")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_228"),
        (1, "loc_234"),
        (2, "loc_240"),
        (3, "loc_24C"),
        (4, "loc_258"),
        (5, "loc_264"),
        (6, "loc_270"),
        (SWITCH_DEFAULT, "loc_27C"),
    )


    label("loc_228")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_234")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_240")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_24C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_258")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_264")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_270")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_27C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_288")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_29F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_288")

    label("loc_29F")

    Return()

    # Function_0_1F0 end

    def Function_1_2A0(): pass

    label("Function_1_2A0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_300")
    OP_95(0xFE, -250, 0, 4390, 2000, 0x0)
    OP_95(0xFE, 19540, 0, 4390, 2000, 0x0)
    OP_95(0xFE, -250, 0, 4390, 2000, 0x0)
    OP_95(0xFE, -250, 0, -11650, 2000, 0x0)
    Jump("Function_1_2A0")

    label("loc_300")

    Return()

    # Function_1_2A0 end

    def Function_2_301(): pass

    label("Function_2_301")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_314")
    ClearChrFlags(0xB, 0x80)
    Jump("loc_4FE")

    label("loc_314")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_349")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -40300, 150, 0, 90)
    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    Jump("loc_4FE")

    label("loc_349")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_37E")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -40300, 150, 0, 90)
    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    Jump("loc_4FE")

    label("loc_37E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3B3")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -40300, 150, 0, 90)
    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    Jump("loc_4FE")

    label("loc_3B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3FE")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -1310, 0, 42250, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -40300, 150, 0, 90)
    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    Jump("loc_4FE")

    label("loc_3FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_449")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -1310, 0, 42250, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -40300, 150, 0, 90)
    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    Jump("loc_4FE")

    label("loc_449")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_494")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -1310, 0, 42250, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -40300, 150, 0, 90)
    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    Jump("loc_4FE")

    label("loc_494")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4B8")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -36160, 0, 3980, 0)
    Jump("loc_4FE")

    label("loc_4B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4FE")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -1310, 0, 42250, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -40300, 150, 0, 90)
    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)

    label("loc_4FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_510")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    Event(0, 10)

    label("loc_510")

    Return()

    # Function_2_301 end

    def Function_3_511(): pass

    label("Function_3_511")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_52B")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)
    Jump("loc_559")

    label("loc_52B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_547")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_559")

    label("loc_547")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_559")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x236), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_559")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_578")
    OP_10(0xB, 0x0)
    OP_10(0xD, 0x1)
    OP_10(0xC, 0x0)
    OP_10(0xE, 0x1)
    Jump("loc_584")

    label("loc_578")

    OP_10(0xB, 0x1)
    OP_10(0xD, 0x0)
    OP_10(0xC, 0x1)
    OP_10(0xE, 0x0)

    label("loc_584")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5AA")
    SetMapObjFrame(0xFF, "hikari_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_5AA")

    SetMapObjFrame(0xFF, "cgf1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "cda1", 0x0, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5E8")
    SetMapObjFrame(0xFF, "cgf1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "cda1", 0x1, 0x1)

    label("loc_5E8")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_604")
    ClearMapObjFlags(0x2, 0x10)
    OP_66(0x1, 0x1)

    label("loc_604")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_616")
    OP_65(0x2, 0x1)
    Jump("loc_628")

    label("loc_616")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_628")
    OP_65(0x2, 0x1)

    label("loc_628")

    Return()

    # Function_3_511 end

    def Function_4_629(): pass

    label("Function_4_629")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            ""Let's Make Them At\x01",
            "Home! Soups Special\x01",
            "Edition" is here.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_6EC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0xF)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EC")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Learned the \x07\x02",
            ""Milk\x01",
            "Potage"\x07\x00",
            " recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_6EC")

    TalkEnd(0xFF)
    Return()

    # Function_4_629 end

    def Function_5_6F0(): pass

    label("Function_5_6F0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_70E")
    Call(0, 12)
    Jump("loc_7A6")

    label("loc_70E")


    ChrTalk(
        0xFE,
        (
            "#07900FCommander Sonya and Vice Commander\x01",
            "Douglas are having a meeting\x01",
            "regarding terrorism countermeasures.\x02\x03",
            "#07903FDon't disturb them, all right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A6")

    Jump("loc_CB2")

    label("loc_7AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_B35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C6")
    Call(0, 12)
    Jump("loc_B30")

    label("loc_7C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A90")

    ChrTalk(
        0xFE,
        (
            "#07900FIf you're looking for Commander\x01",
            "Sonya, she's directing security at\x01",
            "Michelam Health Resort today.\x02\x03",
            "#07903FBecause the state guests were\x01",
            "invited to the guest house, that's\x01",
            "the most important place to guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FSo that means you're commandin'\x01",
            "the Bellguard Gate guys in\x01",
            "place of the commander, huh?\x02\x03",
            "#00306F*sigh*, can someone like you,\x01",
            "Mireille, really stand in for\x01",
            "Commander Sonya?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x104, 500)

    ChrTalk(
        0xFE,
        (
            "#07901FH-How rude...\x02\x03",
            "#07903F...Hmph, I don't need your concern. It's\x01",
            "nothing different than I did while the\x01",
            "previous commander was stationed here.\x02\x03",
            "#07907FI'll definitely manage with Commander\x01",
            "Sonya away, you'll see!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FHaha, well if that's\x01",
            "your attitude, you'll be\x01",
            "fine.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_B30")

    label("loc_A90")


    ChrTalk(
        0xFE,
        (
            "#07903FI often served in place of\x01",
            "the former commander and\x01",
            "directed gate operations.\x02\x03",
            "#07901FI'll definitely manage\x01",
            "with Commander Sonya away,\x01",
            "you'll see!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B30")

    Jump("loc_CB2")

    label("loc_B35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_CB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B50")
    Call(0, 12)
    Jump("loc_CB2")

    label("loc_B50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C21")

    ChrTalk(
        0xFE,
        (
            "#07904FW-Well, news of my promotion\x01",
            "aside...\x02\x03",
            "#07900FHeading into the trade conference,\x01",
            "security was strengthened at the\x01",
            "border gates as well.\x02\x03",
            "Be careful not to trouble the\x01",
            "travellers.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_CB2")

    label("loc_C21")


    ChrTalk(
        0xFE,
        (
            "#07900FHeading into the trade conference,\x01",
            "security was strengthened at the\x01",
            "border gates as well.\x02\x03",
            "Be careful not to trouble the\x01",
            "travellers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CB2")

    TalkEnd(0xFE)
    Return()

    # Function_5_6F0 end

    def Function_6_CB6(): pass

    label("Function_6_CB6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_CC7")
    Jump("loc_16CF")

    label("loc_CC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_CD5")
    Jump("loc_16CF")

    label("loc_CD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_CE3")
    Jump("loc_16CF")

    label("loc_CE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_FD0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F2B")

    ChrTalk(
        0xFE,
        (
            "#07900FAh, guys...\x02\x03",
            "Did you encounter any\x01",
            "trouble getting here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FThere wasn't anything\x01",
            "especially out of the\x01",
            "ordinary...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#07900FI see...\x02\x03",
            "#07903F...It seems it won't\x01",
            "appear today.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "#07900FNo, nevermind. I was\x01",
            "talking about work.\x02\x03",
            "#07903FAlthough I might need to\x01",
            "ask for your advice\x01",
            "soon...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FHmm. I don't really get\x01",
            "it, but... Call us\x01",
            "whenever you need help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#07902FYes, I'll be counting on\x01",
            "you then.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_FCB")

    label("loc_F2B")


    ChrTalk(
        0xFE,
        (
            "#07903F...It seems it won't appear today...\x02\x03",
            "#07901FAnyhow, we must now put all our\x01",
            "effort into dealing with this tension\x01",
            "between us and the major powers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FCB")

    Jump("loc_16CF")

    label("loc_FD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_16CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_134D")

    ChrTalk(
        0x104,
        (
            "#00309FYo, Warrant Officer\x01",
            "Mireille. How've you\x01",
            "been?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x104, 500)

    ChrTalk(
        0xFE,
        (
            "#07901F...You, you're just doing\x01",
            "this on purpose, aren't you.\x02\x03",
            "#07906FDidn't I tell you just the\x01",
            "other day that I was promoted\x01",
            "to 2nd Lt....? Honestly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FAhaha... In any case,\x01",
            "congratulations on your\x01",
            "promotion.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x109, 500)

    ChrTalk(
        0xFE,
        (
            "#07909FHaha. Thank you, Sergeant Major.\x02\x03",
            "#07903FI'm grateful for the promotion, but...\x01",
            "The responsibilities I'll have to bear\x01",
            "will become greater too, right?\x02\x03",
            "#07901FI'll have to apply myself even more\x01",
            "from now on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FOh boy, always the damn\x01",
            "serious gal.\x02\x03",
            "#00302FDoin' your best all the time\x01",
            "will just tire you out. Go\x01",
            "on dates, dates I tell you!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x104, 500)
    OP_63(0xFE, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xFE,
        (
            "#07901FAnd just when people were\x01",
            "having a nice conversation...\x01",
            "You stupid Randy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112FA-Ahaha... (Even if she\x01",
            "was promoted, she's the\x01",
            "same as always...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16A, 4)
    OP_93(0xFE, 0xB4, 0x0)
    Jump("loc_16CF")

    label("loc_134D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1616")

    ChrTalk(
        0x104,
        (
            "#00300FWhoops, by the way... Are you\x01",
            "wearin' that thing I gave you\x01",
            "as a gift for your promotion?\x02\x03",
            "The one I bought you at\x01",
            "Michelam.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1424")

    ChrTalk(
        0x101,
        (
            "#00005FWow... So you even\x01",
            "bought her a present.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1471")

    label("loc_1424")


    ChrTalk(
        0x101,
        (
            "#00002FAh... Now that you\x01",
            "mention it, you bought\x01",
            "her a brooch, I think?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1471")

    TurnDirection(0xFE, 0x104, 500)

    ChrTalk(
        0xFE,
        (
            "#07906FHey now... There's no way I can\x01",
            "wear that.\x02\x03",
            "#07900FConsidering my position of CGF\x01",
            "officer, I can't be that flashy,\x01",
            "so I'll treasure it and...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    ChrTalk(
        0xFE,
        (
            "#07911FT-Tha-That's not it! I\x01",
            "won't treasure it, you\x01",
            "know!\x02\x03",
            "#07909FR-Right! I slovenly\x01",
            "threw it in a corner of\x01",
            "my drawer!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FWah ha ha, don't blush\x01",
            "now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204F(...How cute.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16A, 5)
    OP_93(0xFE, 0xB4, 0x0)
    Jump("loc_16CF")

    label("loc_1616")


    ChrTalk(
        0xFE,
        (
            "#07902FA-Ahem. Anyway... Since I've\x01",
            "been promoted, I intend to\x01",
            "do better than I have been.\x02\x03",
            "#07903FI'll need to apply myself\x01",
            "even more to be of at least\x01",
            "some use to the commander.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16CF")

    TalkEnd(0xFE)
    Return()

    # Function_6_CB6 end

    def Function_7_16D3(): pass

    label("Function_7_16D3")

    Call(0, 8)
    Return()

    # Function_7_16D3 end

    def Function_8_16D7(): pass

    label("Function_8_16D7")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1D3B")
    OP_52(0x109, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x10)
    TurnDirection(0xA, 0x109, 0)
    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1774")
    Jump("loc_17BE")

    label("loc_1774")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1794")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_17BE")

    label("loc_1794")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_17B4")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_17BE")

    label("loc_17B4")

    OP_52(0xA, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_17BE")

    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x109, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x109, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C52")

    ChrTalk(
        0xA,
        "#02008F...............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FCommander Sonya... Are\x01",
            "you worried about\x01",
            "something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#02003F...A little. It's about the CGF\x01",
            "reorganization.\x02\x03",
            "#02000FBecause of the grave damage sustained\x01",
            "at Mainz Mountain Path, it's going to\x01",
            "take some until we're back to normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108FI thought so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10108F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#02000F...Sergeant Major Noｱl.\x01",
            "You look depressed.\x02\x03",
            "#02003FAre you regretting your\x01",
            "decision to return to\x01",
            "the CGF?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103F...No, that's not it.\x02\x03",
            "#10108FIt's just that, even though the Support\x01",
            "Section is so busy, I find it a little\x01",
            "cruel to be the only one getting away...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FNoｱl...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#02003F...I would be delighted to\x01",
            "have your help in rebuilding\x01",
            "the CGF. However...\x02\x03",
            "#02000FShall I cancel your\x01",
            "reinstatement?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103FNo... This is something\x01",
            "I've decided on.\x02\x03",
            "#10101FI'll return to the CGF\x01",
            "as soon as my work is\x01",
            "over for the day!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#02004FVery well.\x02\x03",
            "#02000FBut of course, for now you're\x01",
            "still on temporary transfer to the\x01",
            "Support Section.\x02\x03",
            "Go take care of all your remaining\x01",
            "work so you have no regrets later.\x01",
            "...Do I make myself clear?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FYes ma'am!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1D31")

    label("loc_1C52")


    ChrTalk(
        0xA,
        (
            "#02000F...I would love to have your help\x01",
            "rebuilding the CGF, Noｱl.\x02\x03",
            "#02004FFor the rest of the day, take care of\x01",
            "your Support Section duties so as not to\x01",
            "have any regrets, and return after that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FYes ma'am!\x02",
    )

    CloseMessageWindow()

    label("loc_1D31")

    ClearChrFlags(0xA, 0x10)
    Jump("loc_268A")

    label("loc_1D3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_206C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FDD")

    ChrTalk(
        0xA,
        (
            "#02002FLloyd, that was quite an\x01",
            "achievement yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FDo you mean yesterday at\x01",
            "the accident scene?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#02003F...If I had hurried the repairs then,\x01",
            "the cause of the accident would still\x01",
            "be unknown.\x02\x03",
            "#02008FTo think I could have destroyed\x01",
            "evidence needed to reach the truth with\x01",
            "my own hands... I was too impatient.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FThinking about the CGF's\x01",
            "position, I think it's\x01",
            "understandable...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FYeah, and also, repairs\x01",
            "were completed quickly\x01",
            "afterwards.\x02\x03",
            "#00302FThere's nothing to be\x01",
            "sorry for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FY-Yeah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#02004F...Haha. I'm glad to\x01",
            "hear you say that.\x02\x03",
            "#02002FLet me thank you again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16B, 0)
    Jump("loc_2067")

    label("loc_1FDD")


    ChrTalk(
        0xA,
        (
            "#02004FAnyhow, the cause of the\x01",
            "derailment identified\x01",
            "thanks to you.\x02\x03",
            "#02002FThat large monster\x01",
            "worries me, but... Leave\x01",
            "that to us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2067")

    Jump("loc_268A")

    label("loc_206C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2396")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22CA")

    ChrTalk(
        0xA,
        (
            "#02000FI read your investigation\x01",
            "report.\x02\x03",
            "#02003FPleroma Grass... To think the\x01",
            "name that came out in the cult\x01",
            "incident would appear again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYes... Honestly, we were\x01",
            "surprised too.\x02\x03",
            "#00001FHow should we proceed\x01",
            "with the investigation\x01",
            "from now on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#02003FLet's see, the fact that the CGF can't\x01",
            "act hasn't changed, but...\x02\x03",
            "#02000FFor now, I can say that even just\x01",
            "having identified the cause of the\x01",
            "Cryptid appearances is great progress.\x02\x03",
            "As you did before, please continue to\x01",
            "investigate to the extent that you\x01",
            "can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00302FAlright, please leave it\x01",
            "to us.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16A, 7)
    Jump("loc_2391")

    label("loc_22CA")


    ChrTalk(
        0xA,
        (
            "#02000FFor now, I can say that even just\x01",
            "having identified the cause of the\x01",
            "Cryptid appearances is great progress.\x02\x03",
            "As you did before, please continue to\x01",
            "investigate to the extent that you\x01",
            "can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2391")

    Jump("loc_268A")

    label("loc_2396")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2586")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24F8")

    ChrTalk(
        0xA,
        (
            "#02001FThe origin of the mysterious Cryptids...\x01",
            "As far as Crossbell State is concerned,\x01",
            "it's a problem that can't be ignored.\x02\x03",
            "#02003FStill, we CGF need to focus on the state\x01",
            "of tension at the borders...\x02\x03",
            "#02000FPlease, I'm counting on you to\x01",
            "investigate the Cryptids' origins.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYes, of course. Leave it\x01",
            "to us.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2581")

    label("loc_24F8")


    ChrTalk(
        0xA,
        (
            "#02003FWe CGF need to focus on\x01",
            "tensions at the\x01",
            "borders...\x02\x03",
            "#02000FPlease, I'm counting on\x01",
            "you to investigate the\x01",
            "Cryptids' origins.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2581")

    Jump("loc_268A")

    label("loc_2586")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2594")
    Jump("loc_268A")

    label("loc_2594")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_25A2")
    Jump("loc_268A")

    label("loc_25A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_268A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25BD")
    Call(0, 11)
    Jump("loc_268A")

    label("loc_25BD")


    ChrTalk(
        0xA,
        (
            "#02003FI'm compelled to say that the "Red\x01",
            "Constellation" jaeger corps will\x01",
            "require special attention with\x01",
            "respect to trade conference security.\x02\x03",
            "#02000FIf you learn anything, contact the\x01",
            "CGF as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_268A")

    TalkEnd(0xA)
    Return()

    # Function_8_16D7 end

    def Function_9_268E(): pass

    label("Function_9_268E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2873")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27EB")

    ChrTalk(
        0xB,
        (
            "The commander entered the State\x01",
            "Guard, and 2nd Lt. Mireille and the\x01",
            "others began resistance activities...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Each person chose their\x01",
            "own path after careful\x01",
            "thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "However, almost all the members who\x01",
            "joined the State Guard were in high\x01",
            "spirits and just went with the flow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "...*sigh*, I'm so\x01",
            "pathetic.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2873")

    label("loc_27EB")


    ChrTalk(
        0xB,
        (
            "Commander Sonya, 2nd Lt. Mireille\x01",
            "and the others each chose their\x01",
            "own path after careful thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "...We must do our best\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2873")

    TalkEnd(0xFE)
    Return()

    # Function_9_268E end

    def Function_10_2877(): pass

    label("Function_10_2877")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch03900.itc", 0x1E)
    LoadChrToIndex("chr/ch12202.itc", 0x1F)
    LoadChrToIndex("apl/ch51533.itc", 0x20)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -36600, 0, 0, 270)
    SetChrPos(0x106, -35830, 0, 870, 270)
    SetChrPos(0x103, -35240, 0, -680, 270)
    SetChrPos(0x104, -35430, 0, -1680, 270)
    SetChrPos(0x107, -34080, 0, 1450, 270)
    SetChrPos(0x105, -34350, 0, -80, 270)
    SetChrSubChip(0x107, 0x5)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -40000, 0, 2000, 90)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -40150, 100, 0, 90)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Afterwards, Lloyd and the others were quietly guided to\x01",
            "the Commander's room...\x02\x03",
            "They explained everything to Noｱl and the Commander.\x01",
            "The situation and events that had transpired up to then\x01",
            "and even the story regarding the Sept-Terrion of Zero.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7566", 0)
    OP_68(-40000, 1100, 1000, 0)
    MoveCamera(320, 18, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    FadeToBright(1000, 0)
    OP_68(-38000, 1100, 1000, 4000)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0xC,
        "#10206F#5PT-That's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10603F#5P...I see.\x02\x03",
            "#10601FI finally understand the reason\x01",
            "behind the mysterious movements\x01",
            "of the President's faction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305F#12PSo does that mean...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#12P...You'll cooperate with\x01",
            "us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10603F#5PUnfortunately, that's out of the question.\x02\x03",
            "Be it the CGF or the State Guard, the\x01",
            "principle of civilian control doesn't change.\x02\x03",
            "#10608FAlthough we have a problem on our hands, since\x01",
            "we have a so-called President who established\x01",
            "the "Independent State of Crossbell"...\x02\x03",
            "#10601FWe soldiers aren't allowed to use military\x01",
            "force based on our own judgment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#12PI see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#10208F#5P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12P*sigh*, a regular army\x01",
            "does feel a little strict\x01",
            "in that regard, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10401F#12PThen, as expected, it's\x01",
            "impossible to come to a\x01",
            "compromise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10603F#5PYes, you're right.\x02\x03",
            "#10608F─Even if it wasn't like that, the\x01",
            "Secretary of Defense, Arios, is\x01",
            "formidable.\x02\x03",
            "Even if the Bellguard Gate unit were\x01",
            "to cooperate with you...\x02\x03",
            "#10601FThe main unit led by him would end\x01",
            "up making short work of us, a "rebel\x01",
            "faction", in the blink of an eye.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#12PIs that so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#12PThat ol' man is\x01",
            "formidable even as a\x01",
            "commander!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10606F#5PYes, he was Sergei's former subordinate, but\x01",
            "he was deemed a Divine Blade for a reason.\x02\x03",
            "#10601FHis strategic skills, you know... They say\x01",
            "they're on par with those of his senior\x01",
            "swordsmanship practitioner, Brigadier General\x01",
            "Cassius, commander of the Liberl Royal Army.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xC, 0xB4, 0x1F4)

    ChrTalk(
        0xC,
        (
            "#10206F#11PB-But...!\x02\x03",
            "#10201FEven if Secretary Arios was our opponent,\x01",
            "if we could cooperate with Vice Commander\x01",
            "Douglas at Tangram Gate...!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x1)

    ChrTalk(
        0xA,
        (
            "#10605F#5PMy my, Noｱl.\x02\x03",
            "#10604FWhy do you assume they'd\x01",
            "cooperate with us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#10208F#11P......\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F#12PNoｱl...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10409F#12PHaha, it seems that one-\x01",
            "on-one before was pretty\x01",
            "effective.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00003F#12P─Commander Sonya.\x02\x03",
            "#00008FWhat if, for argument's sake, President\x01",
            "Dieter and the validity of the Independent\x01",
            "State of Crossbell were to waver...\x02\x03",
            "#00001FWhat would become of the State Guard?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x106, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0xA, 0x0)
    OP_93(0xC, 0x5A, 0x1F4)

    ChrTalk(
        0xC,
        "#10205F#5PHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10712F#12PThen...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10604F#5PHaha. Hmm...\x02\x03",
            "It would depend to what extent, but we would\x01",
            "need to "see through the situation with\x01",
            "caution" until the matter was clarified...\x02\x03",
            "#10602FThat is most likely what we'd do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#10202F#5P...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#12PHehe, I see.\x02\x03",
            "#10402FThen the key point will\x01",
            "be how to make that\x01",
            ""validity" sway.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00004F#5PYeah...\x02\x03",
            "It seems that Elie's judgment\x01",
            "would be most reliable in this\x01",
            "kind of situation, but...\x02\x03",
            "#00000FMaybe the key is Chairman\x01",
            "MacDowell.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_356E():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_356E)
    Sleep(50)

    def lambda_357E():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_357E)
    Sleep(50)

    def lambda_358E():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_358E)
    Sleep(50)

    def lambda_359E():
        TurnDirection(0x106, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_359E)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x106, 0)

    ChrTalk(
        0x103,
        "#00205F#12PAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300F#6PMilady's grandfather,\x01",
            "huh...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10702F#12PIf I remember correctly,\x01",
            "he was one of Crossbell's\x01",
            "representatives?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PYeah, and the other was none other than\x01",
            "Mayor Dieter.\x02\x03",
            "#00008FI heard that Chairman MacDowell's point\x01",
            "of view regarding the declaration of\x01",
            "independence was completely ignored.\x02\x03",
            "#00013FIf there was some way we could publicly\x01",
            "announce his opinion to the state,\x01",
            "then...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#12PThe legitimacy of the President and\x01",
            "the validity of the independent\x01",
            "state would waver a little...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#10201F#5PThen, the State Guard as\x01",
            "well would...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10602F#5PHaha... You did well to\x01",
            "notice that.\x02\x03",
            "#10604FI didn't even need to\x01",
            "give you a hint.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_387C():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_387C)
    Sleep(50)

    def lambda_388C():
        OP_93(0x103, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_388C)
    Sleep(50)

    def lambda_389C():
        OP_93(0x104, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_389C)
    Sleep(50)

    def lambda_38AC():
        OP_93(0x105, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_38AC)
    Sleep(50)

    def lambda_38BC():
        OP_93(0x106, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_38BC)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x106, 0)
    SetChrSubChip(0xA, 0x1)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#10603F#5P─2nd Lt. Noｱl.\x02\x03",
            "#10601FFormer Chairman\x01",
            "MacDowell was at\x01",
            "Michelam, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xC, 0xB4, 0x1F4)

    ChrTalk(
        0xC,
        (
            "#10211F#11PHuh... Oh, yeah!\x02\x03",
            "#10203FHe's under house arrest\x01",
            "in the guest house with\x01",
            "his granddaughter, Elie.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "#10608F#5PHmm, if I remember correctly,\x01",
            "Michelam security is handled\x01",
            "by a Red Constellation unit...\x02\x03",
            "#10601FA unit of the State Guard\x01",
            "hasn't been stationed there,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#10201F#11PYes, precisely.\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)

    ChrTalk(
        0x101,
        "#00002F#12PCommander Sonya...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x0)
    Sleep(100)

    ChrTalk(
        0xA,
        (
            "#10605F#5POh my, I, of all people, let\x01",
            "such important information slip\x01",
            "out in front of our guests...\x02\x03",
            "#10604FYou didn't hear anything,\x01",
            "alright? Immediately forget\x01",
            "what you've heard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00209F#12PHaha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F#12PHaha... As expected of\x01",
            "the Commander.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10402F#12PWhat a pleasant poker\x01",
            "face, eh?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x1)
    Sleep(200)

    ChrTalk(
        0xA,
        (
            "#10603F#5P─Also, 2nd Lt. Noｱl.\x02\x03",
            "#10601FRegarding that one-on-\x01",
            "one before, I can't help\x01",
            "but say you were soft.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#10206F#11P...Right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10603F#5PAs punishment, instead of\x01",
            "indefinitely suspending\x01",
            "you─\x02\x03",
            "#10602FI order your reassignment\x01",
            "to the Crossbell Police,\x01",
            "Special Support Section.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xC,
        "#10202F#11PAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10604F#5PGo find out for\x01",
            "yourself...\x02\x03",
            "What you were missing,\x01",
            "and what you should\x01",
            "do...\x02\x03",
            "#10602FFor the sake of the\x01",
            "future of Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetCameraDistance(25200, 0)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xC, 0x20)
    SetChrSubChip(0xC, 0x0)
    OP_0D()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0xC,
        "#10212F#11PYes ma'am!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(25000, 1000)
    OP_6F(0x79)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 6)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_10_2877 end

    def Function_11_3ED5(): pass

    label("Function_11_3ED5")

    EventBegin(0x0)
    Fade(500)
    OP_68(-38900, 900, 260, 0)
    MoveCamera(314, 22, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25180, 0)
    SetChrPos(0x101, -37250, 0, 0, 270)
    SetChrPos(0x102, -37250, 0, 980, 270)
    SetChrPos(0x109, -37250, 0, -1020, 270)
    SetChrPos(0x104, -36050, 0, -720, 270)
    SetChrPos(0x105, -35700, 0, 680, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrSubChip(0xA, 0x0)
    OP_0D()

    ChrTalk(
        0x109,
        (
            "#12P#10100FGood morning, Commander\x01",
            "Sonya!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#02000FOh, same to you, Sergeant\x01",
            "Major Noｱl.\x02\x03",
            "#02004FYou seem to be doing well\x01",
            "with your assignment at the\x01",
            "Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10104FYes, there's so much to\x01",
            "learn...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FAh, so this is the Guardian\x01",
            "Force's Commander, Sonya Bｴlz.\x02\x03",
            "#10302FThe capable commanding officer\x01",
            "of the CGF... Quite the brave\x01",
            "woman, don't you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYeah, she's assisted us quite\x01",
            "a bit in the past.\x02\x03",
            "#00000F─Long time no see, Commander.\x01",
            "And congratulations on your\x01",
            "promotion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#02002FHaha, thank you. And it's nice to see\x01",
            "you as well.\x02\x03",
            "#02002FI've been tied up with trade conference\x01",
            "security so much lately that I had no\x01",
            "opportunity to visit you all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FWe figured you were\x01",
            "busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#02000FYes, I've been checking\x01",
            "the security perimeter\x01",
            "daily with my unit.\x02\x03",
            "#02003FWe have to be ready for\x01",
            "anything, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00306FWell, the international VIPs are\x01",
            "coming tomorrow, after all. It's\x01",
            "only natural you'd be doing that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FSorry to disturb you\x01",
            "when you're so busy,\x01",
            "commander.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#02003FActually, your timing is\x01",
            "perfect.\x02\x03",
            "#02001FThere's something I\x01",
            "wanted to tell all of\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10105FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#02003FYesterday, a certain group came\x01",
            "to visit Bellguard Gate.\x02\x03",
            "#02001FIt was Red Constellation... One\x01",
            "of the strongest and most\x01",
            "fearsome jaeger corps in Zemuria.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00011FWha...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101FThey came here too!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#02000FRegarding Red Constellation...\x01",
            "They say you're directly\x01",
            "connected to them, Randy.\x02\x03",
            "#02003FAccordingly, I thought I\x01",
            "should covey this eyewitness\x01",
            "report to you all directly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00301F...What did they do\x01",
            "here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#02000FAccording to the CGF member who\x01",
            "spotted them, they didn't do anything\x01",
            "in particular that stood out.\x02\x03",
            "#02003FAfter arriving, they relaxed for a\x01",
            "while at the mess hall.\x02\x03",
            "#02000FThey then met a trader from the\x01",
            "Empire and left the gate together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FHmm. They met an\x01",
            "Imperial merchant, eh?\x02\x03",
            "#10302FI wonder if they had any\x01",
            "connection to that\x01",
            "Crimson & Co.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FAh, that's the shell\x01",
            "company Red Constellation\x01",
            "is using for fundraising...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106FIt seems likely, but even so, coming here\x01",
            "directly was quite bold.\x02\x03",
            "#10101FThe CGF is a security organization... To think\x01",
            "that they came right into the midst of the\x01",
            "elites who defend the Imperial border zone...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...Maybe they haven't done anything in\x01",
            "Crossbell yet.\x02\x03",
            "#00001FThere's no proof it was them behind the\x01",
            "old mine case the other day either.\x01",
            "Maybe they've no reason to use stealth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303F...You don't run a high-class\x01",
            "club out in the open like\x01",
            "that without some thick skin.\x02\x03",
            "#00300FCommander Sonya, thanks for\x01",
            "the info.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#02003FNo need to thank me.\x02\x03",
            "#02001FI'm compelled to say that the "Red\x01",
            "Constellation" jaeger corps will\x01",
            "require special attention with\x01",
            "respect to trade conference security.\x02\x03",
            "If you learn anything, contact the\x01",
            "CGF as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F...Understood. We'll\x01",
            "keep an eye out for\x01",
            "them.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x149, 5)
    OP_29(0xA3, 0x1, 0x2)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -37250, 0, 0, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_11_3ED5 end

    def Function_12_4BC2(): pass

    label("Function_12_4BC2")

    EventBegin(0x0)
    Fade(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D2D")
    OP_68(-1550, 910, 41080, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4C94")
    SetChrPos(0x101, -1850, 10, 40450, 0)
    SetChrPos(0x104, -590, 10, 40320, 0)
    SetChrPos(0x102, -2060, 10, 39240, 0)
    SetChrPos(0x103, -720, 10, 39190, 0)
    SetChrPos(0x109, -2140, 10, 38080, 0)
    SetChrPos(0x105, -540, 10, 37980, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Jump("loc_4D21")

    label("loc_4C94")

    OP_68(-1940, 910, 41470, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, -1850, 10, 40450, 0)
    SetChrPos(0x104, -590, 10, 40320, 0)
    SetChrPos(0x102, -2060, 10, 39240, 0)
    SetChrPos(0x109, -720, 10, 39190, 0)
    SetChrPos(0x105, -1740, 10, 38080, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_4D21")

    OP_93(0x8, 0xB4, 0x0)
    Jump("loc_4DCF")

    label("loc_4D2D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DCF")
    OP_68(-37130, 700, 3380, 0)
    MoveCamera(313, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, -36980, 0, 2200, 0)
    SetChrPos(0x104, -35490, 0, 2200, 0)
    SetChrPos(0x102, -36980, 0, 1200, 0)
    SetChrPos(0x109, -35490, 0, 1200, 0)
    SetChrPos(0x105, -36250, 0, 600, 0)
    OP_93(0x8, 0xB4, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_4DCF")

    OP_4B(0x8, 0xFF)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#07902FMy, it's the Support\x01",
            "Section.\x02\x03",
            "#07909FAnd, stupid─\x02\x03",
            "#07903FAhem. Randy, how have\x01",
            "you been?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4E94")
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4E94")

    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x104,
        (
            "#6P#00304FHah, Mireille. You tried to\x01",
            "say it, but... I know how\x01",
            "you really feel.\x02\x03",
            "#00302FYou've been feelin' quite\x01",
            "lonely since I went back to\x01",
            "the Support Section, right?\x02\x03",
            "#00309F─Don't go, Randy! Stay with\x01",
            "me! Stuff like that, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x8)

    ChrTalk(
        0x8,
        (
            "#07907FW-When did I ever say say\x01",
            "anything of the sort!? ...You\x01",
            "damn big stupid Randy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100F(*chuckle*... They\x01",
            "always have such a good\x01",
            "relationship.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHaha... I'm glad you're\x01",
            "doing well, Warrant\x01",
            "Officer Mireille.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FBy the way, I heard you\x01",
            "were promoted. Haha,\x01",
            "congratulations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07902FA-Ahem, yes... To be honest,\x01",
            "it's more than I deserve.\x02\x03",
            "#07908FOf all things, I led the assault\x01",
            "on IBC during the cult incident.\x01",
            "That was a grave error...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FYou were dosed with that strange\x01",
            "drug and manipulated. You don't have\x01",
            "anything to worry about, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07903F...Yes, I understand it\x01",
            "with my head, but I\x01",
            "can't forgive myself...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FMan, always the stubborn one, aren't\x01",
            "you.\x02\x03",
            "#00300FYou did your best to take command, even\x01",
            "under that idiot former commander.\x01",
            "Isn't this exactly what you deserve?\x02\x03",
            "#00302FAccepting it is just good manners\x01",
            "toward the commander.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_53C3")
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_53C3")

    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5415")
    OP_64(0x103)

    label("loc_5415")

    OP_64(0x109)
    OP_64(0x105)
    OP_64(0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_546B")

    ChrTalk(
        0x103,
        (
            "#6P#00205FRandy suddenly gave an\x01",
            "honest opinion...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_54AD")

    label("loc_546B")


    ChrTalk(
        0x101,
        (
            "#00006FW-What can I say... That\x01",
            "got serious all of a\x01",
            "sudden.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54AD")


    ChrTalk(
        0x104,
        (
            "#6P#00309FHaha. I'm always\x01",
            "serious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07902F...Yeah, you're right.\x01",
            "I've decided to accept\x01",
            "it.\x02\x03",
            "#07906F#1S...Thanks, Randy.#3S\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00305F...Huh? Did you say\x01",
            "something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#07903FN-Nevermind.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x149, 4)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55AA")
    OP_93(0x8, 0x0, 0x0)
    SetChrPos(0x0, -1310, 10, 40450, 0)
    Jump("loc_55D0")

    label("loc_55AA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55D0")
    OP_93(0x8, 0x10E, 0x0)
    SetChrPos(0x0, -36300, 0, 2009, 0)

    label("loc_55D0")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_55F4")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_55F4")

    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_12_4BC2 end

    def Function_13_55FB(): pass

    label("Function_13_55FB")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch44900.itc", 0x1E)
    OP_68(-39050, 900, 70, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, -37300, 0, 0, 270)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xA,
        (
            "#5P#02001F─That info was from a\x01",
            "reliable police source.\x02\x03",
            "#02003FThe terrorists will no\x01",
            "doubt try anything to\x01",
            "penetrate our defenses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#12PHmm... What a\x01",
            "troublesome bunch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#12PUnderstood. We'll continue\x01",
            "to focus on security at\x01",
            "Tangram Gate as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#02003FYes, and... I can't say the\x01",
            "possibility they'll infiltrate\x01",
            "using airships is zero.\x02\x03",
            "#02000FAccordingly, make good use of\x01",
            "the radar facilities deployed\x01",
            "near the border gates.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#12PHmm, those anti-aircraft\x01",
            "radars?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#12PUnderstood. I'll get in\x01",
            "charge with those\x01",
            "responsible...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0xD, 0x80)
    OP_68(-1850, 900, -4540, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, -1050, 0, -4470, 270)
    SetChrPos(0x102, -650, 0, -3490, 270)
    SetChrPos(0x103, -550, 0, -5500, 270)
    SetChrPos(0x104, 950, 0, -4470, 270)
    SetChrPos(0x109, 650, 0, -5500, 270)
    SetChrPos(0x105, 1050, 0, -3200, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(500, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00000FIt looks like they're\x01",
            "discussing today's\x01",
            "security operations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes. It looks like anti-\x01",
            "terror measures will be\x01",
            "central.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303FEven so, radar facilities,\x01",
            "huh... Do we really have\x01",
            "them near the border gates?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FIf I remember correctly,\x01",
            "they're deployed near\x01",
            "both gates.\x02\x03",
            "#10103FI've never operated\x01",
            "them, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203FI heard the foundation\x01",
            "installed them in Crossbell\x01",
            "some time ago.\x02\x03",
            "#00200FThey should be able to detect\x01",
            "airships entering Crossbell\x01",
            "airspace across a wide area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FWow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FWell, I guess we can\x01",
            "feel safer knowing we\x01",
            "have them.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x149, 6)
    OP_D7(0x1E)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -1050, 0, -4470, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_13_55FB end

    def Function_14_5BFF(): pass

    label("Function_14_5BFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C11")
    Call(0, 13)
    Jump("loc_5C9A")

    label("loc_5C11")

    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#00000FIt looks like Commander Sonya and Vice\x01",
            "Commander Douglas are discussing anti-\x01",
            "terror measures. Let's not disturb them.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_5C9A")

    Return()

    # Function_14_5BFF end

    SaveToFile()

Try(main)
