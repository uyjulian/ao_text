from ScenarioHelper import *

def main():
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
        "Warrant Mireille",           # 1
        "Lieutenant Mireille",           # 2
        "Sonya Command",           # 3
        "Soldier Romeo",             # 4
        "Lieutenant Noel",             # 5
        "Douglas deputy command",         # 6
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
        "Function_5_6E2",          # 05, 5
        "Function_6_BD6",          # 06, 6
        "Function_7_1566",         # 07, 7
        "Function_8_156A",         # 08, 8
        "Function_9_2342",         # 09, 9
        "Function_10_24EB",        # 0A, 10
        "Function_11_3859",        # 0B, 11
        "Function_12_4418",        # 0C, 12
        "Function_13_4E41",        # 0D, 13
        "Function_14_53F6",        # 0E, 14
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
            "\"Let's make it at home!\" Soup feature \".\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('料理手册', 0x0)"), scpexpr(EXPR_END)), "loc_6DE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0xF)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DE")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "\"Milk Potage\"\x07\x00",
            "I learned the recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_6DE")

    TalkEnd(0xFF)
    Return()

    # Function_4_629 end

    def Function_5_6E2(): pass

    label("Function_5_6E2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_77A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_700")
    Call(0, 12)
    Jump("loc_775")

    label("loc_700")


    ChrTalk(
        0xFE,
        (
            "#07900F今、Sonya CommandとDouglas deputy commandが\x01",
            "I am making arrangements for countering terrorism.\x02\x03",
            "#07903FDo not disturb too much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_775")

    Jump("loc_BD2")

    label("loc_77A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_A6B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_795")
    Call(0, 12)
    Jump("loc_A66")

    label("loc_795")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9E1")

    ChrTalk(
        0xFE,
        (
            "#07900FSonya Commandなら、\x01",
            "Today is a resort area Michelin\x01",
            "I am taking command of security.\x02\x03",
            "#07903FState guests to the guesthouse\x01",
            "Because I am invited,\x01",
            "It is the most important security point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FWhat is it\x01",
            "Today you are the commander\x01",
            "Will you put together the Belgard gate?\x02\x03",
            "#00306FHa, Mireille something\x01",
            "あのSonya Commandの\x01",
            "Will the agent act as a proxy?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x104, 500)

    ChrTalk(
        0xFE,
        (
            "#07901FWell, excruciating ……\x02\x03",
            "#07903F…… Hmm, your worries are fine.\x01",
            "When the former commander was there, do something similar\x01",
            "What was well done.\x02\x03",
            "#07907FSonya Commandのお留守は、\x01",
            "I will absolutely protect you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309FHaha, that seems to be okay with that spirit.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_A66")

    label("loc_9E1")


    ChrTalk(
        0xFE,
        (
            "#07903FWhen the former commander was around\x01",
            "Commanding the gate as a proxy\x01",
            "Things that were left.\x02\x03",
            "#07901FSonya Commandのお留守は、\x01",
            "I will absolutely protect you!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A66")

    Jump("loc_BD2")

    label("loc_A6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_BD2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A86")
    Call(0, 12)
    Jump("loc_BD2")

    label("loc_A86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B4C")

    ChrTalk(
        0xFE,
        (
            "#07904FWell,\x01",
            "Aside from my promotion story ……\x02\x03",
            "#07900FFor the trade meeting,\x01",
            "Even at the border gate we are increasing alertness.\x02\x03",
            "Trouble with travelers\x01",
            "Do not wake it up,\x01",
            "Please be careful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_BD2")

    label("loc_B4C")


    ChrTalk(
        0xFE,
        (
            "#07900FFor the trade meeting,\x01",
            "Even at the border gate we are increasing alertness.\x02\x03",
            "Trouble with travelers\x01",
            "Do not wake it up,\x01",
            "Please be careful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BD2")

    TalkEnd(0xFE)
    Return()

    # Function_5_6E2 end

    def Function_6_BD6(): pass

    label("Function_6_BD6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_BE7")
    Jump("loc_1562")

    label("loc_BE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_BF5")
    Jump("loc_1562")

    label("loc_BF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_C03")
    Jump("loc_1562")

    label("loc_C03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_F04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E79")

    ChrTalk(
        0xFE,
        (
            "#07900FOh, you guys ……\x02\x03",
            "On the way to the Belgard gate,\x01",
            "Did not you see anything dangerous?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005Feh……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FA state that changed as usual\x01",
            "There was nothing I thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "#07900Fso……\x02\x03",
            "#07903F…… Apparently today\x01",
            "It does not seem to show signs.\x02",
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
            "#07900FNo, do not mind.\x01",
            "Because it is a story of this work.\x02\x03",
            "#07903FIn the near future,\x01",
            "I might consult you\x01",
            "I do not think so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303FHmm, I do not understand well …\x01",
            "If you need help, please call me anytime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "#07902FYes, at that time I will ask you.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_EFF")

    label("loc_E79")


    ChrTalk(
        0xFE,
        (
            "#07903F…… Apparently today\x01",
            "It does not seem to show up … …\x02\x03",
            "#07901FNow anyway, in a state of tension with the two major powers\x01",
            "I have to go hand in hand with it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EFF")

    Jump("loc_1562")

    label("loc_F04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1562")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_120C")

    ChrTalk(
        0x104,
        (
            "#00309Fいよっ、Warrant Mireille殿。\x01",
            "Were you doing well?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x104, 500)

    ChrTalk(
        0xFE,
        (
            "#07901F……you,\x01",
            "You do it on purpose, do not you?\x02\x03",
            "#07906FDuring this time I got promoted to Sansei\x01",
            "I just said that …\x01",
            "Altogether anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10109FHaha … … Anyway,\x01",
            "Congratulations on your promotion.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x109, 500)

    ChrTalk(
        0xFE,
        (
            "#07909FHehe, thank you very much.\x02\x03",
            "#07903FPromotion is appreciated ….\x01",
            "The responsibility to carry over gradually\x01",
            "It will grow bigger.\x02\x03",
            "#07901FFrom now on,\x01",
            "You have to do your best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306FWhew. As usual\x01",
            "It is a fucking bastard.\x02\x03",
            "#00302FI'll get tired of being just gambling.\x01",
            "Go to Tetchet suddenly with Tetchet.\x02",
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
            "#07901FPeople have a good story\x01",
            "Even though it is … …\x01",
            "This, Blurred Randy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10112FOh, haha ….\x01",
            "(Even if you promote it is as usual …)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16A, 4)
    OP_93(0xFE, 0xB4, 0x0)
    Jump("loc_1562")

    label("loc_120C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14C3")

    ChrTalk(
        0x104,
        (
            "#00300FOops, that's right.\x01",
            "I gave a promotion celebration gift,\x01",
            "Do you have it on?\x02\x03",
            "At the Michelin jewelry store\x01",
            "I bought it, I am.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12D5")

    ChrTalk(
        0x101,
        (
            "#00005FOh\x01",
            "Have you got a present?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1313")

    label("loc_12D5")


    ChrTalk(
        0x101,
        (
            "#00002FOh … that reminds me,\x01",
            "I was buying a brooch.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1313")

    TurnDirection(0xFE, 0x104, 500)

    ChrTalk(
        0xFE,
        (
            "#07906FHa ha ha …\x01",
            "You do not have it on.\x02\x03",
            "#07900FThings that would also be officers of the guard\x01",
            "I can not do that kind of thing,\x01",
            "All right, please …\x02",
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
            "#07911FIt is different, … different from that!\x01",
            "I have not done anything important!\x02\x03",
            "#07909FThat's right! To the corner of the dance\x01",
            "Throw it in fraying … …!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309FWaah, I'm shy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204F(… It is smart.)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16A, 5)
    OP_93(0xFE, 0xB4, 0x0)
    Jump("loc_1562")

    label("loc_14C3")


    ChrTalk(
        0xFE,
        (
            "#07902FKo, Kohon, anyway … …\x01",
            "Because I was promoted,\x01",
            "I will try harder than before.\x02\x03",
            "#07903FIn order to be a force of command even a little,\x01",
            "You have to go a step further.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1562")

    TalkEnd(0xFE)
    Return()

    # Function_6_BD6 end

    def Function_7_1566(): pass

    label("Function_7_1566")

    Call(0, 8)
    Return()

    # Function_7_1566 end

    def Function_8_156A(): pass

    label("Function_8_156A")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1B2C")
    OP_52(0x109, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x10)
    TurnDirection(0xA, 0x109, 0)
    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1607")
    Jump("loc_1651")

    label("loc_1607")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1627")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1651")

    label("loc_1627")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1647")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1651")

    label("loc_1647")

    OP_52(0xA, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1651")

    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x109, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x109, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A6C")

    ChrTalk(
        0xA,
        "#02008F……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FSonya Command……\x01",
            "Is there something wrong with me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#02003F…… About the restructuring of the guard a little.\x02\x03",
            "#02000FDue to the tremendous damage I received at Mainz mountain road\x01",
            "In order to recover to the original state,\x01",
            "It will take some time after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108FIs that correct?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10108F…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#02000F… … Sergeant Noel.\x01",
            "I have a floating face.\x02\x03",
            "#02003FI decided to return to the guard,\x01",
            "I wonder if I regret it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103F…… No, such a thing.\x02\x03",
            "#10108FHowever, the support department is also busy\x01",
            "I only get out\x01",
            "I feel a little incompetent … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FNoel …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#02003F…… To restore the guard\x01",
            "I absolutely want your power … …\x02\x03",
            "#02000FWould you like to stop returning again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103FHouse……\x01",
            "After all it was decided.\x02\x03",
            "#10101FNoel · Seeker,\x01",
            "As soon as the work of the day is over,\x01",
            "I will return to the guard!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#02004Fvery well.\x02\x03",
            "#02000FBut of course, you are still\x01",
            "I'm an employee of the support department.\x02\x03",
            "As there is no regret, the remaining work\x01",
            "Try to clean up everything.\x01",
            "……Good?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FHappy, OK!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1B22")

    label("loc_1A6C")


    ChrTalk(
        0xA,
        (
            "#02000FTo rebuild the guard\x01",
            "Noel's power is certainly wanted.\x02\x03",
            "#02004FToday, I feel regretful\x01",
            "Tidying up the work of the support department,\x01",
            "Then come back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FHappy, OK!\x02",
    )

    CloseMessageWindow()

    label("loc_1B22")

    ClearChrFlags(0xA, 0x10)
    Jump("loc_233E")

    label("loc_1B2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1E1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D90")

    ChrTalk(
        0xA,
        (
            "#02002FLloyd,\x01",
            "I was impressed yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005Feh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYesterday at the accident site\x01",
            "Do you mean surveying?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#02003F…… If that time,\x01",
            "If I was urging recovery\x01",
            "The cause of the derailment accident remained unknown.\x02\x03",
            "#02008FWith this hand the evidence will arrive at the truth\x01",
            "I was trying to crush … ….\x01",
            "I was too impatient.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FAfter considering the position of the guard\x01",
            "It can not be helped ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FOh, and after that\x01",
            "The restoration has proceeded swiftly.\x02\x03",
            "#00302FTo be depressed separately\x01",
            "Is not it not there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FThat's right!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#02004F… … Huhu, say that.\x01",
            "I will be saved if you get it.\x02\x03",
            "#02002FPlease give me another thank you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16B, 0)
    Jump("loc_1E16")

    label("loc_1D90")


    ChrTalk(
        0xA,
        (
            "#02004FAnyway, thanks\x01",
            "I found out the cause of the derailment accident.\x02\x03",
            "#02002FI am worried about large monsters … …\x01",
            "Please leave it to me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E16")

    Jump("loc_233E")

    label("loc_1E1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_20C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_202C")

    ChrTalk(
        0xA,
        (
            "#02000FYour research report\x01",
            "I had you read it.\x02\x03",
            "#02003F\"Pleroma grass\" … … No way,\x01",
            "The name that it came out with a cult incident\x01",
            "It will not appear again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYeah ….\x01",
            "We were also surprised honestly.\x02\x03",
            "#00001FWhat about the future survey\x01",
            "Will you go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#02003FWell, the guard\x01",
            "I can not move\x01",
            "It remains unchanged though ……\x02\x03",
            "#02000FFor the moment, \"eidolon\" appears\x01",
            "Even if the cause was found out\x01",
            "It can be said that it is a big progress.\x02\x03",
            "You guys are like this\x01",
            "Research to the extent possible\x01",
            "Continue please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00302FAiyo, please leave it.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x16A, 7)
    Jump("loc_20C3")

    label("loc_202C")


    ChrTalk(
        0xA,
        (
            "#02000FFor the moment, \"eidolon\" appears\x01",
            "Even if the cause was found out\x01",
            "It can be said that it is a big progress.\x02\x03",
            "You guys are like this\x01",
            "Research to the extent possible\x01",
            "Continue please.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20C3")

    Jump("loc_233E")

    label("loc_20C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2270")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21EA")

    ChrTalk(
        0xA,
        (
            "#02001FAn incomprehensible \"eidolon\" occurrence … …\x01",
            "For the Crossbell Autonomous Region\x01",
            "It is a problem that can never be ignored.\x02\x03",
            "#02003FNonetheless, our guard is\x01",
            "Tension of the border\x01",
            "I need to focus …\x02\x03",
            "#02000FInvestigation of the cause of the occurrence of a phantom beast,\x01",
            "Please do my best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FWell, please leave it to me.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_226B")

    label("loc_21EA")


    ChrTalk(
        0xA,
        (
            "#02003FOur guard is\x01",
            "Tension of the border\x01",
            "I need to focus …\x02\x03",
            "#02000FInvestigation of the cause of the occurrence of a phantom beast,\x01",
            "Please do my best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_226B")

    Jump("loc_233E")

    label("loc_2270")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_227E")
    Jump("loc_233E")

    label("loc_227E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_228C")
    Jump("loc_233E")

    label("loc_228C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_233E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22A7")
    Call(0, 11)
    Jump("loc_233E")

    label("loc_22A7")


    ChrTalk(
        0xA,
        (
            "#02003FThe hunting corps \"red constellation\"\x01",
            "Even in the security of the trade council\x01",
            "It must be said that it is cautionful.\x02\x03",
            "#02000FIf you know something,\x01",
            "Please also contact the guard.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_233E")

    TalkEnd(0xA)
    Return()

    # Function_8_156A end

    def Function_9_2342(): pass

    label("Function_9_2342")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_24E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2471")

    ChrTalk(
        0xB,
        (
            "Commander who accepted Defense Forces,\x01",
            "I started resistance activities\x01",
            "Lieutenant Mireilleたち……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Those people thought into thought\x01",
            "I chose each way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "But as I became a defense army\x01",
            "Most of the members are floating,\x01",
            "It was just being swept away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "…… Ha, I can not treat myself myself.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_24E7")

    label("loc_2471")


    ChrTalk(
        0xB,
        (
            "Sonya CommandもLieutenant Mireilleたちも、\x01",
            "After thinking into ideas\x01",
            "I chose each way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "…… We also have to work hard.\x02",
    )

    CloseMessageWindow()

    label("loc_24E7")

    TalkEnd(0xFE)
    Return()

    # Function_9_2342 end

    def Function_10_24EB(): pass

    label("Function_10_24EB")

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
            "After that, Lloyd's\x01",
            "It was guided to the command room so as not to be noticeable ……\x02\x03",
            "Including circumstances and circumstances until now,\x01",
            "Until the story concerning \"Zero's treasure\"\x01",
            "I confided everything to the commanders.\x07\x00\x02",
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
        "#10206F#5PWell, that's … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10603F#5P……I see.\x02\x03",
            "#10601FInexplicable behavior of the President\x01",
            "It has finally come to light.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00305F#12PDo you mean that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#12P…… to some extent here\x01",
            "Can you cooperate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10603F#5PUnfortunately that is impossible.\x02\x03",
            "Whether it is a guard or a defense army,\x01",
            "Civilian control#8RCivilian control#\"Principle does not change.\x02\x03",
            "#10608FAlthough there are problems,\x01",
            "\"Crossbell independent country\" was established\x01",
            "More than the head of state president is … …\x02\x03",
            "#10601FOur soldiers, at my discretion\x01",
            "It is not permissible to exercise force.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#12P……Is that so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#10208F#5P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12PHaa, what is the regular army?\x01",
            "That place is a strict spirit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10401F#12PThen then\x01",
            "It seems impossible for me to compromise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10603F#5PWell, that will be true.\x02\x03",
            "#10608F── Even if it is not so,\x01",
            "Defense Secretary Arios is excellent.\x02\x03",
            "If the troops of the Belgard gate are\x01",
            "Even if you cooperate with it … …\x02\x03",
            "#10601FTo the main force unit led by him\x01",
            "As \"Rebel Army\" in an instant\x01",
            "It will be suppressed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00201F#12PReally……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F#12PThat osan,\x01",
            "Is he also a good commander?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10606F#5PYes, it is a former subordinate of Sergei\x01",
            "As expected it is only called \"swords and sorcerers\"\x01",
            "Logical#2RA touch#You seem to be familiar with.\x02\x03",
            "#10601FThe skill of that strategy …\x01",
            "Ribeel Army Commander, a senior son,\x01",
            "There is a thing that is compatible with Brigadier General Cassius.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xC, 0xB4, 0x1F4)

    ChrTalk(
        0xC,
        (
            "#10206F#11PBut, it is …!\x02\x03",
            "#10201FEven if you are Arios' counterpart\x01",
            "タングラム門のDouglas deputy commandと\x01",
            "If you can cooperate …!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x1)

    ChrTalk(
        0xA,
        (
            "#10605F#5POh, noel.\x02\x03",
            "#10604FWhy cooperate with them\x01",
            "Is it supposed to be a premise?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#10208F#11P…… Well ………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F#12PNoel ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10409F#12PHahaha, the one-on-one fight earlier\x01",
            "You seem to be working.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00003F#12P──Sonya Command。\x02\x03",
            "#00008FIf President Dieter and\x01",
            "The \"justification\" of the Crossbell independent country is\x01",
            "In case of shaking …\x02\x03",
            "#00001FWhat will happen to the defense force's response?\x02",
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
        "#10205F#5PHuh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        "#10712F#12Pthat's……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10604F#5PHuhu, well … …\x02\x03",
            "It depends to some extent\x01",
            "Until the truth of things is clear\x01",
            "\"Determine the situation carefully\" … …\x02\x03",
            "#10602FIt may be necessary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#10202F#5P……!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10404F#12PHuh, I see.\x02\x03",
            "#10402FAnd then, how\x01",
            "Whether it will shake \"justification\"\x01",
            "It is becoming a key.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00004F#5PAh……\x02\x03",
            "Eli's judgment is like this\x01",
            "It seems to be the most reliable, but ….\x02\x03",
            "#00000FPerhaps the key is McDowell's chairman\x01",
            "I do not think so.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3022():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3022)
    Sleep(50)

    def lambda_3032():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3032)
    Sleep(50)

    def lambda_3042():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3042)
    Sleep(50)

    def lambda_3052():
        TurnDirection(0x106, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_3052)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x106, 0)

    ChrTalk(
        0x103,
        "#00205F#12PAh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00300F#6PIs she your dear Josser? …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x106,
        (
            "#10702F#12PCertainly, in Crossbell Autonomous Region\x01",
            "You become one of the representatives, are not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#5POh, another one is nothing else\x01",
            "Although he was Mayor of Dieter.\x02\x03",
            "#00008FForeign Country Declaration\x01",
            "Mr. MacDaely's opinion is\x01",
            "I heard that it was completely sealed.\x02\x03",
            "#00013FHis opinion, in some way\x01",
            "If it is announced both in Japan and abroad …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F#12PThe legitimacy of the president and the independent nation\x01",
            "It may slightly shake …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#10201F#5PIf so, the defense army … ….!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10602F#5PWhatching\x01",
            "I noticed a nice place.\x02\x03",
            "#10604FApparently a hint\x01",
            "Was it not necessary to issue it?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_329C():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_329C)
    Sleep(50)

    def lambda_32AC():
        OP_93(0x103, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_32AC)
    Sleep(50)

    def lambda_32BC():
        OP_93(0x104, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_32BC)
    Sleep(50)

    def lambda_32CC():
        OP_93(0x105, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_32CC)
    Sleep(50)

    def lambda_32DC():
        OP_93(0x106, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_32DC)
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
            "#10603F#5P──Lieutenant Noel。\x02\x03",
            "#10601FMcDael's former chairman,\x01",
            "I wonder if it was a Michelin?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xC, 0xB4, 0x1F4)

    ChrTalk(
        0xC,
        (
            "#10211F#11PEr … Oh, yes!\x02\x03",
            "#10203FTogether with my granddaughter Ellie\x01",
            "It is under arrest inside the guest house!\x02",
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
            "#10608F#5PHmm, Michelam's security\x01",
            "Undoubtedly the \"red constellation\" unit … …\x02\x03",
            "#10601FThe Defense Forces unit\x01",
            "You did not reside at all, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#10201F#11PThat is right.\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)

    ChrTalk(
        0x101,
        "#00002F#12PSonya Command……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x0)
    Sleep(100)

    ChrTalk(
        0xA,
        (
            "#10605F#5POh, what you have done with me\x01",
            "Inadvertently in front of outsiders ……\x02\x03",
            "#10604FIt's nothing.\x01",
            "Forget about now right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00209F#12PHehu ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F#12PHa ha …\x01",
            "さすがSonya Command。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10402F#12PI feel comfortable\x01",
            "I heard it for the first time.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x1)
    Sleep(200)

    ChrTalk(
        0xA,
        (
            "#10603F#5P──それとLieutenant Noel。\x02\x03",
            "#10601FAlthough it is one fight with the previous time,\x01",
            "It can not be helped even if it is said that it is sweet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#10206F#11P……Yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10603F#5PAs a punishment, for a while,\x01",
            "Indefinite punitive disposition ─ ─\x02\x03",
            "#10602FInstead, crossbell police,\x01",
            "I will order reorientation to the Special Affairs Support Division.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xC,
        "#10202F#11PAh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10604F#5PWhat was missing to me ……\x02\x03",
            "And for the future of Crossbell\x01",
            "What should I do?\x02\x03",
            "#10602FPlease make a firm decision.\x02",
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
        "#10212F#11POK#12RYes Mom#It is!\x02",
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

    # Function_10_24EB end

    def Function_11_3859(): pass

    label("Function_11_3859")

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
        "#12P#10100Fお疲れ様です、Sonya Command！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#02000FGood job, Noel colleague.\x02\x03",
            "#02004FDeployment to the Special Affairs Support Division,\x01",
            "You seem to be working hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10104FYes, I really have a lot to learn …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FIndeed, the command of the Guard Command\x01",
            "It is Sonja Belts.\x02\x03",
            "#10302FA competent commander who gathers the guards … …\x01",
            "Huh, it seems quite a female girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FOh, we also from the front\x01",
            "It is a person who is indebted.\x02\x03",
            "#00000F── Long time no see, commander.\x01",
            "Well … and it is now\x01",
            "Congratulations on your promotion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#02002FHuh, you are welcome.\x01",
            "By the way it was a long time ago.\x02\x03",
            "#02002FRecently there was security of trade council\x01",
            "The opportunity to match face easily\x01",
            "I did not have it … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FAfter all I am busy\x01",
            "It seems that it is done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#02000FWell, recently every day,\x01",
            "Around the guard area with the unit\x01",
            "I have you check it.\x02\x03",
            "#02003FAs if nothing should happen,\x01",
            "Make careful preparations\x01",
            "Because I must keep it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00306FWell, tomorrow VIPs from different countries\x01",
            "Because it is a coming story.\x01",
            "Of course it is natural.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI'm sorry, commander.\x01",
            "Somehow I'm busy\x01",
            "Have you disturbed ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#02003FNo, rather it was exactly right.\x02\x03",
            "#02001FTo you, by all means\x01",
            "Because there was something to tell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10105FHuh……?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#02003F── The other day, at this Belgard gate\x01",
            "A group came.\x02\x03",
            "#02001F\"Red constellation\" … …\x01",
            "In the western part of the continental continent\x01",
            "The honest soldiers are said to be the strongest.\x02",
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
        "#00011FBecome Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00101FTo such a place …! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#02000FRed constellation, Randy …\x01",
            "It is closely related to you\x01",
            "It was a story.\x02\x03",
            "#02003FSo, that sighting information\x01",
            "I thought that I should tell you directly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#12P#00301F…… What are they doing here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#02000FIn the story of a witnessed security crew member,\x01",
            "Special notable thing is\x01",
            "I heard you did not do it.\x02\x03",
            "#02003FAfter arrival, for a while,\x01",
            "After relaxing in the dining room ……\x02\x03",
            "#02000FI greeted a merchant from the empire,\x01",
            "He said he left the gate as it was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FWell, my imperial merchant's welcome.\x02\x03",
            "#10302FSomewhat\x01",
            "With the \"Crimson Shokai\"\x01",
            "Is it a stranger or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FOh, for the red constellation funding\x01",
            "Dummy company ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10106FThe possibility seems high, but …\x01",
            "Well, even so, it's too bold.\x02\x03",
            "#10101FSecurity guard which is security organization ……\x01",
            "It is also an elite to protect the empire\x01",
            "It is coming in the middle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F…… The guys in this crossbell,\x01",
            "I have not done anything yet.\x02\x03",
            "#00001FOne case at the former mine during this time\x01",
            "There is no evidence,\x01",
            "I guess there's nothing to be done with that ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303F…… It is about that the skin of the face is thick,\x01",
            "I do not manage a high-class club dignitely.\x02\x03",
            "#00300FSonya Command、情報どうもッス。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#02003F…… It does not go beyond reward.\x02\x03",
            "#02001FThe hunting corps \"red constellation\"\x01",
            "Even in the security of the trade council\x01",
            "It must be said that it is cautionful.\x02\x03",
            "If you know something,\x01",
            "Please also contact the guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F……I understand.\x01",
            "I will also be careful.\x02",
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

    # Function_11_3859 end

    def Function_12_4418(): pass

    label("Function_12_4418")

    EventBegin(0x0)
    Fade(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4583")
    OP_68(-1550, 910, 41080, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_44EA")
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
    Jump("loc_4577")

    label("loc_44EA")

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

    label("loc_4577")

    OP_93(0x8, 0xB4, 0x0)
    Jump("loc_4625")

    label("loc_4583")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4625")
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

    label("loc_4625")

    OP_4B(0x8, 0xFF)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#07902FOh, everyone in the support department.\x01",
            "Long time no see.\x02\x03",
            "#07909FAlso, there are idiots there -\x02\x03",
            "#07903F…… Kohon.\x01",
            "Randy, how are you doing?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_46FF")
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_46FF")

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
            "#6P#00304FHuff, Mireille.\x01",
            "It seems like it came to say … …\x01",
            "I understand your feelings.\x02\x03",
            "#00302FI got back to the support department,\x01",
            "You are lonely, are not you?\x02\x03",
            "#00309F\"─ ─ Do not go, Randy!\x01",
            "From now on stay with me! (falsetto)\"\x01",
            "… … What are you saying?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x8)

    ChrTalk(
        0x8,
        (
            "#07907FWhen, I said such a thing! Is it?\x01",
            "…… This, big idiot RANDY!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10100F(Couscous……\x01",
            "You are still on good terms. )\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000Fはは……Warrant Mireille、\x01",
            "I'm glad that you are fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100Fby the way,\x01",
            "I heard that there is a story about promotion.\x01",
            "Congratulations, Huhu.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07902FKo, Kohon, yeah ….\x01",
            "To be honest, I feel comfortable.\x02\x03",
            "#07908FWhen it is a cult incident\x01",
            "To lead the IBC attack\x01",
            "I made a serious mistake … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FWell, at that time a strange medicine was served\x01",
            "I'm talking about being manipulated,\x01",
            "You do not have to worry about it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07903F…… Yeah, with the head\x01",
            "I know that,\x01",
            "I wonder if I can not forgive ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FWhew. As usual\x01",
            "Fine, hey, you.\x02\x03",
            "#00300FThis time, even under the previous AHO command\x01",
            "What has been the best command,\x01",
            "It is a result that was justified.\x02\x03",
            "#00302FIt is fortunate to receive,\x01",
            "It would be courtesy to the commander.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4BF7")
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_4BF7")

    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4C49")
    OP_64(0x103)

    label("loc_4C49")

    OP_64(0x109)
    OP_64(0x105)
    OP_64(0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4CA0")

    ChrTalk(
        0x103,
        (
            "#6P#00205FRandy said\x01",
            "Suddenly Mato opinion ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CE0")

    label("loc_4CA0")


    ChrTalk(
        0x101,
        (
            "#00006FWhat is it …?\x01",
            "Suddenly say Matmo 's opinion.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CE0")


    ChrTalk(
        0x104,
        (
            "#6P#00309FHa ha, I always\x01",
            "Matumo, maybe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07902F… Well, that's right.\x01",
            "I will respectfully accept it.\x02\x03",
            "#07906F#1S… …. Thank you, Randy.#3S\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#6P#00305F……What? Did you say something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#07903FNothing, nothing.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x149, 4)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DF0")
    OP_93(0x8, 0x0, 0x0)
    SetChrPos(0x0, -1310, 10, 40450, 0)
    Jump("loc_4E16")

    label("loc_4DF0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E16")
    OP_93(0x8, 0x10E, 0x0)
    SetChrPos(0x0, -36300, 0, 2009, 0)

    label("loc_4E16")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4E3A")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_4E3A")

    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_12_4418 end

    def Function_13_4E41(): pass

    label("Function_13_4E41")

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
            "#5P#02001F─ ─ So far,\x01",
            "Information from a solid source of police.\x02\x03",
            "#02003FPerhaps terrorists\x01",
            "I try to intrude in some way\x01",
            "There is no mistake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#12PHmm … … It is troublesome people.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#12PIt is okay.\x01",
            "Even at the Tangram gate\x01",
            "Let's suppose to strengthen vigilance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#5P#02003FWell, then … …\x01",
            "The possibility of invading by flying boat is also\x01",
            "It can not be said to be zero.\x02\x03",
            "#02000FIt is deployed near the border gate\x01",
            "Try to make effective use of radar facilities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#12PHmm, is that anti-aircraft radar?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#12PAgain, I understood.\x01",
            "Please contact the person in charge immediately.\x02",
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
            "#00000FApparently, today's security system\x01",
            "It seems they are talking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYeah, apparently countermeasures against terrorism\x01",
            "It seems that it is placed in the main spindle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#12P#00303FEven if it is a radar facility ……\x01",
            "Is there such a thing near the gate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10100FIndeed in the vicinity of the border gate\x01",
            "It should be deployed.\x02\x03",
            "#10103FI have never dealt with it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#6P#00203FPreviously, the Foundation\x01",
            "When installed in the crossbell\x01",
            "I have heard of it.\x02\x03",
            "#00200FAutonomous state Provide an airship entering the airspace\x01",
            "Can be supplemented in a fairly wide range\x01",
            "It is a high performance thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FOh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10300FWell, if there is such a thing\x01",
            "You may be able to relieve to some extent.\x02",
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

    # Function_13_4E41 end

    def Function_14_53F6(): pass

    label("Function_14_53F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5408")
    Call(0, 13)
    Jump("loc_547D")

    label("loc_5408")

    TalkBegin(0xFF)

    ChrTalk(
        0x101,
        (
            "#00000FSonya CommandとDouglas deputy commandが\x01",
            "It seems they are talking about terrorism countermeasures.\x01",
            "… … let's stop going inside.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)

    label("loc_547D")

    Return()

    # Function_14_53F6 end

    SaveToFile()

Try(main)
