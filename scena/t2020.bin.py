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
        "Warrant-Officer Mireille",# 1
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
        "Function_5_6F6",          # 05, 5
        "Function_6_D23",          # 06, 6
        "Function_7_17BD",         # 07, 7
        "Function_8_17C1",         # 08, 8
        "Function_9_2808",         # 09, 9
        "Function_10_29F4",        # 0A, 10
        "Function_11_4054",        # 0B, 11
        "Function_12_4DF4",        # 0C, 12
        "Function_13_58ED",        # 0D, 13
        "Function_14_5F81",        # 0E, 14
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
            "The "Let's Make Them At Home!\x01",
            "Soups Special Edition" is here.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_6F2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0xF)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F2")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "You learned the "Milk Potage"\x07\x00",
            " recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_6F2")

    TalkEnd(0xFF)
    Return()

    # Function_4_629 end

    def Function_5_6F6(): pass

    label("Function_5_6F6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_7A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_714")
    Call(0, 12)
    Jump("loc_79C")

    label("loc_714")


    ChrTalk(
        0xFE,
        (
            "#07900FCommander Sonya and Vice Commander Douglas\x01",
            "are having an anti-terrorist meeting now.\x02\x03",
            "#07903FDon't disturb them, all right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_79C")

    Jump("loc_D1F")

    label("loc_7A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_B71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7BC")
    Call(0, 12)
    Jump("loc_B6C")

    label("loc_7BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AB2")

    ChrTalk(
        0xFE,
        (
            "#07900FIf you're looking for Commander Sonya,\x01",
            "today she's directing security\x01",
            "at Michelam Health Resort.\x02\x03",
            "#07903FBecause the state guests were\x01",
            "invited at the guest house, it's the\x01",
            "most important place to guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FSo it means that today it's you who are \x01",
            "coordinatin' the Bellguard Gate's guys\x01",
            "in place of the commander, huh?\x02\x03",
            "#00306F*sigh*, will someone like you,\x01",
            "Mireille, be fit as proxy for\x01",
            "that Commander Sonya?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x104, 500)

    ChrTalk(
        0xFE,
        (
            "#07901FH-How rude...\x02\x03",
            "#07903F...Hmph, I don't need your concern.\x01",
            "It's similar to what I was forced to often do\x01",
            "when the former Commander was here.\x02\x03",
            "#07907FI'll absolutely manage it now that\x01",
            "Commander Sonya is away, you'll see!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FHa ha, if you've got that spirit,\x01",
            "it seems you'll be fine.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_B6C")

    label("loc_AB2")


    ChrTalk(
        0xFE,
        (
            "#07903FAt the time of the former Commander\x01",
            "I was often entrusted the direction\x01",
            "of the gate as proxy.\x02\x03",
            "#07901FI'll absolutely manage it now that\x01",
            "Commander Sonya is away, you'll see!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B6C")

    Jump("loc_D1F")

    label("loc_B71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_D1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B8C")
    Call(0, 12)
    Jump("loc_D1F")

    label("loc_B8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C7C")

    ChrTalk(
        0xFE,
        (
            "#07904FW-Well, setting aside the\x01",
            "story of my promotion...\x02\x03",
            "#07900FHeading towards the Trade Conference, vigilance \x01",
            "was strengthened at the national border gate too.\x02\x03",
            "Be careful to not cause\x01",
            "troubles with travellers.\x01\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_D1F")

    label("loc_C7C")


    ChrTalk(
        0xFE,
        (
            "#07900FHeading towards the Trade Conference, vigilance \x01",
            "was strengthened at the national border gate too.\x02\x03",
            "Be careful to not cause\x01",
            "troubles with travellers.\x01\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D1F")

    TalkEnd(0xFE)
    Return()

    # Function_5_6F6 end

    def Function_6_D23(): pass

    label("Function_6_D23")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_D34")
    Jump("loc_17B9")

    label("loc_D34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_D42")
    Jump("loc_17B9")

    label("loc_D42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_D50")
    Jump("loc_17B9")

    label("loc_D50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1096")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FE0")

    ChrTalk(
        0xFE,
        (
            "#07900FAh, guys...\x02\x03",
            "While you were coming to Bellguard Gate,\x01",
            "did you get into any danger?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FIt seemed there wasn't anything\x01",
            "out of the ordinary...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#07900FI see...\x02\x03",
            "#07903F...It seems that there's\x01",
            "no sign it'll appear today.\x02",
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
            "#07900FNo, don't mind it.\x01",
            "I was talking about work.\x02\x03",
            "#07903FAlthough maybe I'll\x01",
            "probably have to ask\x01",
            "for your advice soon...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FHmmm, I don't really get it, but...\x01",
            "If you need help, call whenever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#07902FYes, I'll be counting on you at that time.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1091")

    label("loc_FE0")


    ChrTalk(
        0xFE,
        (
            "#07903F...It seems that there's\x01",
            "no sign it'll appear today...\x02\x03",
            "#07901FAt any rate, now we must deal with all our might\x01",
            "with the state of tension with the two major powers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1091")

    Jump("loc_17B9")

    label("loc_1096")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_17B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1401")

    ChrTalk(
        0x104,
        (
            "#00309FYo, Warrant-Officer Mireille ma'am.\x01",
            "Been well?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x104, 500)

    ChrTalk(
        0xFE,
        (
            "#07901F...You, you're doing it\x01",
            "on purpose, right?\x02\x03",
            "#07906FDidn't I just tell you the other day\x01",
            "that I was promoted to 2nd Lt....?\x01",
            "Honestly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FAhaha... In any case,\x01",
            "congratulations for your promotion.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x109, 500)

    ChrTalk(
        0xFE,
        (
            "#07909FUh uh, thank you, Master Sergeant.\x02\x03",
            "#07903FI'm grateful for the promotion, but...\x01",
            "The responsibilities I'll have to bear\x01",
            "will gradually become bigger, right?\x02\x03",
            "#07901FFrom now on, I'll have to\x01",
            "apply myself all the more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FOh boy, always the\x01",
            "damn serious gal.\x02\x03",
            "#00302FDoin' only your best will tire you out.\x01",
            "Go on dates, dates!\x02",
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
            "You damn halfwit Randy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112FA-Ahaha...\x01",
            "(Even if she was promoted,\x01",
            "she's the same as always...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16A, 4)
    OP_93(0xFE, 0xB4, 0x0)
    Jump("loc_17B9")

    label("loc_1401")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16F7")

    ChrTalk(
        0x104,
        (
            "#00300FOops, by the way...\x01",
            "Are you wearin' that thing I gave you as a\x01",
            "present as congratulation for your promotion?\x02\x03",
            "The one that I bought you a the\x01",
            "jewelry in Michelam, that one.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1505")

    ChrTalk(
        0x101,
        (
            "#00005FEeh...\x01",
            "You were buying her a present?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1551")

    label("loc_1505")


    ChrTalk(
        0x101,
        (
            "#00002FAh...now that you mention it,\x01",
            "you bought her a brooch, I think?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1551")

    TurnDirection(0xFE, 0x104, 500)

    ChrTalk(
        0xFE,
        (
            "#07906FHey now...\x01",
            "No way I'll be wearing it.\x02\x03",
            "#07900FConsidering my position of CGF officer,\x01",
            "I can't be that flashy, so I'll treasure it and...\x01\x02",
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
            "#07911FT-Tha-That's not it!\x01",
            "I won't treasure it, you know!\x02\x03",
            "#07909FR-Right! I slovenly threw it\x01",
            "in a cooorner of the drawer...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309FWah ha ha, don't blush.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204F(......How cute.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16A, 5)
    OP_93(0xFE, 0xB4, 0x0)
    Jump("loc_17B9")

    label("loc_16F7")


    ChrTalk(
        0xFE,
        (
            "#07902F*c-cough*, anyway...\x01",
            "Since I've been promoted, I intend \x01",
            "to do my best more than before.\x02\x03",
            "#07903FI have to apply myself all the more to be\x01",
            "useful to the Commander at least a little.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17B9")

    TalkEnd(0xFE)
    Return()

    # Function_6_D23 end

    def Function_7_17BD(): pass

    label("Function_7_17BD")

    Call(0, 8)
    Return()

    # Function_7_17BD end

    def Function_8_17C1(): pass

    label("Function_8_17C1")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1E2C")
    OP_52(0x109, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x10)
    TurnDirection(0xA, 0x109, 0)
    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_185E")
    Jump("loc_18A8")

    label("loc_185E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_187E")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_18A8")

    label("loc_187E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_189E")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_18A8")

    label("loc_189E")

    OP_52(0xA, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_18A8")

    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x109, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x109, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D4D")

    ChrTalk(
        0xA,
        "#02008F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FCommander Sonya...\x01",
            "Are you worried about something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#02003F...A little about the CGF reorganization.\x02\x03",
            "#02000FBecause of the grave damage sustained at\x01",
            "Mainz Mountain Path, as expected it's going to\x01",
            "take some time to go back to the former situation.\x02",
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
            "#02000F......Master Sergeant Noｱl.\x01",
            "You look depressed.\x02\x03",
            "#02003FAre you regretting the decision\x01",
            "to be reinstated to the CGF?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103F...No, it's not that.\x02\x03",
            "#10108FIt's just that although the Support\x01",
            "Section is busy too, I find it a little\x01",
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
            "#02003F...I absolutely want your help\x01",
            "to rebuild the CGF, however...\x02\x03",
            "#02000FShould I stop your reinstatement, as I think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103FNo...\x01",
            "It's something I've decided.\x02\x03",
            "#10101FNoｱl Seeker, as soon as my\x01",
            "work is over for the day,\x01",
            "I'll return to the CGF!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#02004FPerfect.\x02\x03",
            "#02000FHowever, naturally you're still a member\x01",
            "transferred to the Support Section.\x02\x03",
            "Go take care of all the remaining jobs\x01",
            "you have so to not regret it later.\x01",
            "...Understood?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FRoger, ma'am!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1E22")

    label("loc_1D4D")


    ChrTalk(
        0xA,
        (
            "#02000F...I absolutely want your help\x01",
            "to rebuild the CGF, Noｱl\x02\x03",
            "#02004FFor the entire day, clear out your\x01",
            "Support Section duties so to not have\x01",
            "any regrets and come back afterwards.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FRoger, ma'am!\x02",
    )

    CloseMessageWindow()

    label("loc_1E22")

    ClearChrFlags(0xA, 0x10)
    Jump("loc_2804")

    label("loc_1E2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_219F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20F9")

    ChrTalk(
        0xA,
        (
            "#02002FLloyd, you did quite the\x01",
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
            "#00100FDo you mean yesterday investigation\x01",
            "at the accident site?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#02003F...At that time, if I had sped up \x01",
            "the repairs, the derailment accident \x01",
            "cause would still be unknown.\x02\x03",
            "#02008FTo think that I would've destroyed with\x01",
            "my hands the proofs to reach the truth...\x01",
            "I was too impatient.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FThinking about the CGF position,\x01",
            "I believe it couldn't be helped...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FYeah, and also, after that\x01",
            "the repairs advanced fast.\x02\x03",
            "#00302FThere's nothing to be\x01",
            "depressed for at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FT-That's right!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#02004F...Uh uh, hearing you say\x01",
            "that saves me too.\x02\x03",
            "#02002FLet me thank you again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16B, 0)
    Jump("loc_219A")

    label("loc_20F9")


    ChrTalk(
        0xA,
        (
            "#02004FIn any case, thanks to you the cause\x01",
            "of the derailment accident was identified.\x02\x03",
            "#02002FThat large-type monster worries me, but...\x01",
            "Leave that to us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_219A")

    Jump("loc_2804")

    label("loc_219F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_24E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2414")

    ChrTalk(
        0xA,
        (
            "#02000FI've read your investigation report.\x01\x02\x03",
            "#02003F"Pleroma Grass"...  To think that\x01",
            "name that came out in the Cult\x01",
            "incident would've appeared again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYes...\x01",
            "Honestly, we were surprised too.\x02\x03",
            "#00001FHow should we proceed with the\x01",
            "investigation from now on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#02003FLet's see, the fact that\x01",
            "the CGF can't act\x01",
            "doesn't change yet, but...\x02\x03",
            "#02000FFor now, I can say that even just \x01",
            "having identified the cause that makes \x01",
            "the "Cryptids" appear is a big progress.\x02\x03",
            "Like you did, you'll continue\x01",
            "to investigate within the\x01",
            "scope that you can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00302FAlright, please leave it to us.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16A, 7)
    Jump("loc_24E1")

    label("loc_2414")


    ChrTalk(
        0xA,
        (
            "#02000FFor now, I can say that even just \x01",
            "having identified the cause that makes \x01",
            "the "Cryptids" appear is a big progress.\x02\x03",
            "Like you did, you'll continue\x01",
            "to investigate within the\x01",
            "scope that you can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24E1")

    Jump("loc_2804")

    label("loc_24E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2702")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_265F")

    ChrTalk(
        0xA,
        (
            "#02001FThe origin of the mysterious\x01",
            "Cryptids... As far as the autonomous\x01",
            "state of Crossbell is concerned, it's\x01",
            "a problem that can't be ignored.\x02\x03",
            "#02003FStill, we CGF need to\x01",
            "focus on the national\x01",
            "borders state of tension...\x02\x03",
            "#02000FPlease, I'm counting on you on the\x01",
            "Cryptids' origin cause investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, please leave it to us.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_26FD")

    label("loc_265F")


    ChrTalk(
        0xA,
        (
            "#02003FWe CGF need to\x01",
            "focus on the national\x01",
            "borders state of tension...\x02\x03",
            "#02000FPlease, I'm counting on you on the\x01",
            "Cryptids' origin cause investigation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26FD")

    Jump("loc_2804")

    label("loc_2702")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2710")
    Jump("loc_2804")

    label("loc_2710")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_271E")
    Jump("loc_2804")

    label("loc_271E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2804")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2739")
    Call(0, 11)
    Jump("loc_2804")

    label("loc_2739")


    ChrTalk(
        0xA,
        (
            "#02003FI'm compelled to say that the "Red Constellation"\x01",
            "Jaeger Corps will require special attention during \x01",
            "the Trade Conference security.\x02\x03",
            "#02000FIf you figure something out,\x01",
            "contact the CGF too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2804")

    TalkEnd(0xA)
    Return()

    # Function_8_17C1 end

    def Function_9_2808(): pass

    label("Function_9_2808")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_29F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2968")

    ChrTalk(
        0xB,
        (
            "The Commander entered the State Guard,\x01",
            "2nd Lt. Mireille and the others began\x01",
            "resistance activities...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Those persons chose each their\x01",
            "own path after careful thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "However, almost all the members\x01",
            "who joined the State Guard were in\x01",
            "high spirits and just went with the flow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "...*sigh*, I'm so pathetic.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_29F0")

    label("loc_2968")


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
        "...We must do our best too.\x02",
    )

    CloseMessageWindow()

    label("loc_29F0")

    TalkEnd(0xFE)
    Return()

    # Function_9_2808 end

    def Function_10_29F4(): pass

    label("Function_10_29F4")

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
            "Afterwards, Lloyd and the others were\x01",
            "clandestinely guided to the Commander room...\x02\x03",
            "They spoke their mind about everything to the Commander\x01",
            "and Noｱl. The situation and the particulars until then\x01",
            "and even the story about the "Sept-Terrion of Zero".\x07\x00\x02",
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
        "#10206F#5PS-Such a thing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10603F#5P...I see.\x02\x03",
            "#10601FI can even finally understand the mysterious\x01",
            "movements of the President faction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305F#12PSo it means, that...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#12P...Will you cooperate with\x01",
            "us to a certain degree?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10603F#5PUnfortunately, that's impossible.\x02\x03",
            "Being it the CGF or the State Guard, the\x01",
            "principle of civilian control doesn't change.\x02\x03",
            "#10608FAlthough we have a problem, since we have a\x01",
            "head of state called President who established\x01",
            "the "Independent State of Crossbell"...\x02\x03",
            "#10601FWe soldiers aren't allowed to use\x01",
            "military might to our own discretion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#12P...I understand.\x02",
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
            "#00306F#12P*sigh*, a regular army is \x01",
            "strict in that regard, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10401F#12PThen, as expected it's\x01",
            "impossible to meet halfway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10603F#5PYes, you're right.\x02\x03",
            "#10608F──Even if it wasn't like that, the\x01",
            "Secretary of Defense Arios is formidable.\x02\x03",
            "Even if the Bellguard Gate\x01",
            "unit were to cooperate with you...\x02\x03",
            "#10601FThe main unit lead by him would end up\x01",
            "suppressing us, as a "rebel army",\x01",
            "in the blink of an eye.\x02",
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
            "#00301F#12PIs that ol' man formidable\x01",
            "even as a Commander!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10606F#5PYes, he was Sergei's former subordinate,\x01",
            "but he was deemed to be called\x01",
            ""Divine Blade" for a reason.\x02\x03",
            "#10601FHis strategic skills, you know...\x01",
            "They say they're on par with those of his senior\x01",
            "swordsmanship schoolmate, the Liberl Royal\x01",
            "Army Commander, Brigadier General Cassius.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xC, 0xB4, 0x1F4)

    ChrTalk(
        0xC,
        (
            "#10206F#11PB-But...!\x02\x03",
            "#10201FEven if Secretary Arios was our opponent, \x01",
            "if we could cooperate with Tangram Gate\x01",
            "Vice Commander Douglas...!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x1)

    ChrTalk(
        0xA,
        (
            "#10605F#5PMy, Noｱl.\x02\x03",
            "#10604FWhy do you presume we'd\x01",
            "cooperate with them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#10208F#11P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F#12PMiss Noｱl...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10409F#12PHa ha, it seems that one-\x01",
            "to-one before was effective.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00003F#12P──Commander Sonya.\x02\x03",
            "#00008FWhat if, for argument's sake, President\x01",
            "Dieter and "validity" of the Independent\x01",
            "State of Crossbell were to sway...\x02\x03",
            "#00001FWhat would be of the State Guard?\x02",
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
        "#10205F#5PWhat...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10712F#12PYou mean...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10604F#5PUh uh, let's see...\x02\x03",
            "It would depend to what extent, but we would\x01",
            "have to "see through the situation with caution"\x01",
            "until the matter is clarified if it's true or not...\x02\x03",
            "#10602FWe'd probably need to do that.\x02",
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
            "#10404F#12PHu hu, I see.\x02\x03",
            "#10402FThen the key point will be\x01",
            "how to make that\x01",
            ""validity" sway.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00004F#5PYeah...\x02\x03",
            "It seems that Elie's judgment would be the\x01",
            "most reliable thing in such a matter, but...\x02\x03",
            "#00000FMaybe the key is\x01",
            "Chairman MacDowell.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3700():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3700)
    Sleep(50)

    def lambda_3710():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3710)
    Sleep(50)

    def lambda_3720():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3720)
    Sleep(50)

    def lambda_3730():
        TurnDirection(0x106, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_3730)
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
        "#00300F#6PMilady's grandfather, huh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10702F#12PIf I remember correctly, he's one of the\x01",
            "autonomous state of Crossbell representatives?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5PYeah, and the other one was none\x01",
            "other than Mayor Dieter.\x02\x03",
            "#00008FI heard that Chairman MacDowell point\x01",
            "of view regarding the independence\x01",
            "declaration was completely forbidden.\x02\x03",
            "#00013FIf we could announce inside and outside\x01",
            "the state his opinion in some form...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#12PThe President and independent state\x01",
            "validity maybe would sway a little...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#10201F#5PThen, the State Guard too...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10602F#5PUh uh...\x01",
            "You did well in noticing that.\x02\x03",
            "#10604FIt seems I didn't even\x01",
            "need to give you a hint.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3A08():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3A08)
    Sleep(50)

    def lambda_3A18():
        OP_93(0x103, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3A18)
    Sleep(50)

    def lambda_3A28():
        OP_93(0x104, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3A28)
    Sleep(50)

    def lambda_3A38():
        OP_93(0x105, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3A38)
    Sleep(50)

    def lambda_3A48():
        OP_93(0x106, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_3A48)
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
            "#10603F#5P──2nd Lt. Noｱl.\x02\x03",
            "#10601FFormer Chairman MacDowell\x01",
            "was at Michelam, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xC, 0xB4, 0x1F4)

    ChrTalk(
        0xC,
        (
            "#10211F#11PEh...oh, yes!\x02\x03",
            "#10203FHe's at house arrest in the guest house\x01",
            "with his granddaughter, Miss Elie.\x02",
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
            "#10608F#5PHmm, if I remember correctly, Michelam security \x01",
            "is handled by the "Red Constellation" unit...\x02\x03",
            "#10601FA unit of the State Guard hasn't\x01",
            "been stationed there, right?\x02",
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
            "#10605F#5PMy, I, of all people, saying inadvertently\x01",
            "something in front of outsiders...\x02\x03",
            "#10604FThat was nothing.\x01",
            "Immediately forget what you've heard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00209F#12PUh uh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F#12PHa ha...\x01",
            "As expected from Commander Sonya.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10402F#12PWhat a pleasant\x01",
            "poker face, eh?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x1)
    Sleep(200)

    ChrTalk(
        0xA,
        (
            "#10603F#5P──Also, 2nd Lt. Noｱl.\x02\x03",
            "#10601FAbout that one-to-one before,\x01",
            "I can't help but say you were soft.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#10206F#11P...Yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10603F#5PAs punishment, instead of indefinitely\x01",
            "suspending you for the time being──\x02\x03",
            "#10602FI order your re-assignment to the\x01",
            "Crossbell Police, Special Support Section.\x02",
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
            "#10604F#5PGo find out for yourself...\x02\x03",
            "What you lacked, \x01",
            "and what you should do...\x02\x03",
            "#10602FFor the sake of Crossbell future.\x02",
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

    # Function_10_29F4 end

    def Function_11_4054(): pass

    label("Function_11_4054")

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
        "#12P#10100FThank you for your hard work, Commander Sonya!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#02000FThank you for yours too, Master Sergeant Noｱl.\x02\x03",
            "#02004FIt seems you're doing your best with your\x01",
            "assignment at the Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10104FYes, I'm really learning many things...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FI see, so she's the CGF Commander,\x01",
            "Sonya Bｴlz, eh?\x02\x03",
            "#10302FThe capable commanding officer\x01",
            "who manages the CGF... Hu hu, she\x01",
            "looks like quite the brave woman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYeah, she's someone who\x01",
            "helped us before too.\x02\x03",
            "#00000F──Long time no see, Commander.\x01",
            "Also...although it's late,\x01",
            "congratulations for your promotion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#02002FUh uh, you're welcome.\x01",
            "Now that you mention it, \x01",
            "it's really been a long time.\x02\x03",
            "#02002FWith the recent security for\x01",
            "the Trade Conference we didn't\x01",
            "had the chance to meet at all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FIt seems you've\x01",
            "really been busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#02000FYes, lately every day I'm \x01",
            "checking the nearby areas \x01",
            "security with the unit.\x02\x03",
            "#02003FBecause we must be\x01",
            "carefully ready for\x01",
            "the unexpected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00306FWell, after all, tomorrow VIPs from\x01",
            "all countries are going to arrive.\x01",
            "It's only obvious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI'm sorry, Commander.\x01",
            "We disturbed you is a\x01",
            "somewhat busy moment...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#02003FNo, rather, you came at the right time.\x02\x03",
            "#02001FI had something I wanted\x01",
            "to tell you no matter what.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10105FWhat...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#02003F──The other day, a certain group\x01",
            "showed up at Bellguard Gate.\x02\x03",
            "#02001FThe "Red Constellation"...\x01",
            "They're said to be the strongest\x01",
            "jaegers in the West Zemuria Continent.\x02",
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
        "#00101FThey came here too...!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#02000FThe Red Constellation, Randy...\x01",
            "There was the story that\x01",
            "they're related to you, eh?\x02\x03",
            "#02003FThat's why I thought I should tell you\x01",
            "directly this eyewitness intel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00301F...What did they come here for?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#02000FAccording to the CGF member who\x01",
            "spotted them, they didn't do anything\x01",
            "particular that stood out.\x02\x03",
            "#02003FAfter arriving, they relaxed for\x01",
            "a while at the mess hall, then...\x02\x03",
            "#02000FThey met a trader who came from the\x01",
            "Empire and they left the gate together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FEeh, they met an Imperial trader, eh?\x02\x03",
            "#10302FTherefore, perhaps someone\x01",
            "related to that "Crimson & Co."\x01",
            "or whatever?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FAh, the dummy company that's\x01",
            "financing the Red Constellation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106FHighly likely, but...\x01",
            "N-Nevertheless, they were quite bold.\x02\x03",
            "#10101FThe CGF is an organization for the public\x01",
            "order maintenance...\x01",
            "To think that they came right in the midst\x01",
            "of the elites who defend the Empire zone...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...Maybe they haven't caused\x01",
            "anything in Crossbell yet.\x02\x03",
            "#00001FThere's also no proof it was them who\x01",
            "caused the recent matter at the old mine...\x01",
            "They aren't even moving stealthily, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303F...You don't manage a grand high class club\x01",
            "if you aren't that brazen-faced, you know.\x02\x03",
            "#00300FCommander Sonya, thanks for the info.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#02003F...You don't need to thank me.\x02\x03",
            "#02001FI'm compelled to say that the "Red Constellation"\x01",
            "jaeger corps will require special attention during \x01",
            "the Trade Conference security.\x02\x03",
            "If you figure something out,\x01",
            "contact the CGF too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F...Understood.\x01",
            "We'll be careful too.\x02",
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

    # Function_11_4054 end

    def Function_12_4DF4(): pass

    label("Function_12_4DF4")

    EventBegin(0x0)
    Fade(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F5F")
    OP_68(-1550, 910, 41080, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4EC6")
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
    Jump("loc_4F53")

    label("loc_4EC6")

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

    label("loc_4F53")

    OP_93(0x8, 0xB4, 0x0)
    Jump("loc_5001")

    label("loc_4F5F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5001")
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

    label("loc_5001")

    OP_4B(0x8, 0xFF)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#07902FOh, the guys from the Support Section.\x01",
            "Long time no see.\x02\x03",
            "#07909FAnd also stupi-R──\x02\x03",
            "#07903F...*cough*.\x01",
            "How have you been, Randy?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_50EE")
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_50EE")

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
            "#6P#00304FHu hu, Mireille.\x01",
            "It seems you started to express them, but...\x01",
            "I know your feelings.\x02\x03",
            "#00302FYou've been feelin' quite lonely since\x01",
            "I went back to the Support Section, right?\x02\x03",
            "#00309F"──Don't go, Randy!\x01",
            "Stay with me from now on too! (falsetto)".\x01",
            "...You were saying stuff like that, huh?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x8)

    ChrTalk(
        0x8,
        (
            "#07907FW-When did I ever say such things!?\x01",
            "...You damn big stupi-Randy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100F(*chuckle chuckle*...\x01",
            "They get along well as always.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHa ha... Warrant-Officer Mireille,\x01",
            "I'm glad you look well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FBy the way, it seems that talks\x01",
            "for a promotion came up.\x01",
            "*giggle*, congratulations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07902F*c-cough*, yes...\x01",
            "Frankly, I feel it's more than I deserve.\x02\x03",
            "#07908FAt the time of the Cult incident, of all\x01",
            "things I lead the assault to the IBC and\x01",
            "committed a serious offense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FWell, at that time you were served\x01",
            "a mysterious drug and manipulated,\x01",
            "so you shouldn't worry about it, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07903F...Yes, I understand\x01",
            "it with my head, but\x01",
            "I can't forgive myself...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FOh boy, always the\x01",
            "stubborn one, aren't you.\x02\x03",
            "#00300FThis promotion is the result of having' been\x01",
            "rightly evaluated for havin' managed things\x01",
            "very well under the former idiot Commander, no?\x02\x03",
            "#00302FHumbly acceptin' it should be\x01",
            "courtesy towards the Commander.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_569E")
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_569E")

    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_56F0")
    OP_64(0x103)

    label("loc_56F0")

    OP_64(0x109)
    OP_64(0x105)
    OP_64(0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_574A")

    ChrTalk(
        0x103,
        (
            "#6P#00205FMr. Randy suddenly\x01",
            "gave a serious opinion...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_578F")

    label("loc_574A")


    ChrTalk(
        0x101,
        (
            "#00006FW-What can I say...\x01",
            "You suddenly gave a serious opinion.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_578F")


    ChrTalk(
        0x104,
        (
            "#6P#00309FHa ha, I'm always\x01",
            "serious, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07902F...Yes, you're right.\x01",
            "I'll humbly accept it.\x02\x03",
            "#07906F#1S......Thank you, Randy.#3S\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00305F...Eh? Did you say something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#07903FI-It was nothing.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x149, 4)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_589C")
    OP_93(0x8, 0x0, 0x0)
    SetChrPos(0x0, -1310, 10, 40450, 0)
    Jump("loc_58C2")

    label("loc_589C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58C2")
    OP_93(0x8, 0x10E, 0x0)
    SetChrPos(0x0, -36300, 0, 2009, 0)

    label("loc_58C2")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_58E6")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_58E6")

    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_12_4DF4 end

    def Function_13_58ED(): pass

    label("Function_13_58ED")

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
            "#5P#02001F──That's all, and it's intel from\x01",
            "a reliable police source.\x02\x03",
            "#02003FI think there's no doubt that the\x01",
            "terrorists will try to infiltrate\x01",
            "with any methods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#12PHm...what a troublesome bunch.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#12PUnderstood.\x01",
            "We'll continue our duty at Tangram Gate\x01",
            "and strengthen security.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#02003FYes, also...\x01",
            "I can't say that the possibilities they'll\x01",
            "infiltrate using airships are zero.\x02\x03",
            "#02000FAnd so, make good use of the radar facilities\x01",
            "that were deployed nearby the national border gates.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#12PHm, those anti-aircraft radars?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#12PUnderstood, again.\x01",
            "I'll contact the officer in charge immediately...\x02",
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
            "#00000FIt seems that they're talking\x01",
            "about today's security system.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes, it seems that anti terrorist\x01",
            "measures are going to be central.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303FStill, radar facilities...?\x01",
            "Were there such things nearby the gates?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FIf I remember correctly, they were\x01",
            "deployed nearby both national border gates.\x02\x03",
            "#10103FI've never dealt with them, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203FI heard that the Foundation\x01",
            "had installed such things\x01",
            "in Crossbell before.\x02\x03",
            "#00200FThey should be very efficient in covering\x01",
            "airships in a pretty wide range inside\x01",
            "the autonomous state airspace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FEeh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FWell, if we have such things, maybe\x01",
            "we can feel safe to a certain degree.\x02",
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

    # Function_13_58ED end

    def Function_14_5F81(): pass

    label("Function_14_5F81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F93")
    Call(0, 13)
    Jump("loc_6029")

    label("loc_5F93")

    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#00000FCommander Sonya and Vice Commander Douglas\x01",
            "seem to be discussing about anti-terrorism measures.\x01",
            "...Let's refrain from going inside.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_6029")

    Return()

    # Function_14_5F81 end

    SaveToFile()

Try(main)
