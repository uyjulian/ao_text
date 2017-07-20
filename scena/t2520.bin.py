from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t2520.bin",                # FileName
        "t2520",                    # MapName
        "t2520",                    # Location
        0x005A,                     # MapIndex
        "ed7126",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1B,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 90, 0, 3, 0, 4],
    )

    BuildStringList((
        "t2520",                  # 0
        "Frighty member",           # 1
        "Douglas deputy command",         # 2
    ))

    AddCharChip((
        "chr/ch34100.itc",                   # 00
        "chr/ch44902.itc",                   # 01
        "chr/ch41800.itc",                   # 02
    ))

    DeclNpc(4294934546, 9,       40700,   0,    261,  0x0, 0,   0,   0,   0,   1,   0,   6,   255,  0)
    DeclNpc(6210,    150,     4294967146, 270,  325,  0x0, 0,   1,   0,   255, 255, 0,   9,   255,  0)

    DeclActor(4760,    0,       4294967016, 1200,    6210,    1500,    4294967146, 0x007E, 0,  8,  0x0000)
    DeclActor(4294883616, 0,       22050,   1200,    4294883616, 1200,    22050,   0x007C, 0,  5,  0x0000)

    ChipFrameInfo(384, 0)                                        # 0

    ScpFunction((
        "Function_0_180",          # 00, 0
        "Function_1_238",          # 01, 1
        "Function_2_263",          # 02, 2
        "Function_3_2C4",          # 03, 3
        "Function_4_40A",          # 04, 4
        "Function_5_532",          # 05, 5
        "Function_6_5DD",          # 06, 6
        "Function_7_1371",         # 07, 7
        "Function_8_14CA",         # 08, 8
        "Function_9_151C",         # 09, 9
        "Function_10_357B",        # 0A, 10
        "Function_11_4045",        # 0B, 11
        "Function_12_4177",        # 0C, 12
        "Function_13_41A7",        # 0D, 13
        "Function_14_41FF",        # 0E, 14
        "Function_15_4257",        # 0F, 15
        "Function_16_42A2",        # 10, 16
        "Function_17_42ED",        # 11, 17
        "Function_18_4403",        # 12, 18
        "Function_19_45CD",        # 13, 19
        "Function_20_560F",        # 14, 20
        "Function_21_5DBA",        # 15, 21
        "Function_22_5F09",        # 16, 22
        "Function_23_6851",        # 17, 23
    ))


    def Function_0_180(): pass

    label("Function_0_180")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_1C0"),
        (1, "loc_1CC"),
        (2, "loc_1D8"),
        (3, "loc_1E4"),
        (4, "loc_1F0"),
        (5, "loc_1FC"),
        (6, "loc_208"),
        (SWITCH_DEFAULT, "loc_214"),
    )


    label("loc_1C0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_220")

    label("loc_1CC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_220")

    label("loc_1D8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_220")

    label("loc_1E4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_220")

    label("loc_1F0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_220")

    label("loc_1FC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_220")

    label("loc_208")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_220")

    label("loc_214")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_220")

    label("loc_220")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_237")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_220")

    label("loc_237")

    Return()

    # Function_0_180 end

    def Function_1_238(): pass

    label("Function_1_238")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_262")
    OP_94(0xFE, 0xFFFF86E8, 0xA5A0, 0xFFFF793C, 0x9858, 0x3E8)
    Sleep(300)
    Jump("Function_1_238")

    label("loc_262")

    Return()

    # Function_1_238 end

    def Function_2_263(): pass

    label("Function_2_263")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2C3")
    OP_95(0xFE, -33890, 0, 4560, 2000, 0x0)
    OP_95(0xFE, -33890, 0, -11290, 2000, 0x0)
    OP_95(0xFE, -33890, 0, 4560, 2000, 0x0)
    OP_95(0xFE, -53890, 0, 4560, 2000, 0x0)
    Jump("Function_2_263")

    label("loc_2C3")

    Return()

    # Function_2_263 end

    def Function_3_2C4(): pass

    label("Function_3_2C4")

    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_303")
    SetChrChipByIndex(0x8, 0x2)
    SetChrFlags(0x9, 0x80)
    SetChrPos(0x8, -40000, 0, 4560, 90)
    BeginChrThread(0x8, 0, 0, 2)
    Jump("loc_3B9")

    label("loc_303")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_311")
    Jump("loc_3B9")

    label("loc_311")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_31F")
    Jump("loc_3B9")

    label("loc_31F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_32D")
    Jump("loc_3B9")

    label("loc_32D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_366")
    SetChrPos(0x8, 3900, 0, -150, 90)
    BeginChrThread(0x8, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_361")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)

    label("loc_361")

    Jump("loc_3B9")

    label("loc_366")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_390")
    SetChrPos(0x8, 740, 0, 4470, 0)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrFlags(0x9, 0x80)
    Jump("loc_3B9")

    label("loc_390")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_39E")
    Jump("loc_3B9")

    label("loc_39E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3B9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B9")
    SetChrFlags(0x9, 0x80)

    label("loc_3B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_3CD")
    ClearScenarioFlags(0x22, 0)
    Event(0, 19)
    Jump("loc_3DC")

    label("loc_3CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_3DC")
    ClearScenarioFlags(0x22, 1)
    Event(0, 23)

    label("loc_3DC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_409")
    Event(0, 10)

    label("loc_409")

    Return()

    # Function_3_2C4 end

    def Function_4_40A(): pass

    label("Function_4_40A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_426")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_438")

    label("loc_426")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_438")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x236), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_438")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_44A")
    OP_65(0x0, 0x1)
    Jump("loc_4C0")

    label("loc_44A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_458")
    Jump("loc_4C0")

    label("loc_458")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_466")
    Jump("loc_4C0")

    label("loc_466")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_474")
    Jump("loc_4C0")

    label("loc_474")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_486")
    OP_65(0x0, 0x1)
    Jump("loc_4C0")

    label("loc_486")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_498")
    OP_65(0x0, 0x1)
    Jump("loc_4C0")

    label("loc_498")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4A6")
    Jump("loc_4C0")

    label("loc_4A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4C0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C0")
    OP_65(0x0, 0x1)

    label("loc_4C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E6")
    SetMapObjFrame(0xFF, "hikari_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_4E6")

    SetMapObjFrame(0xFF, "bear", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_519")
    SetMapObjFrame(0xFF, "cgf2", 0x1, 0x1)
    SetMapObjFrame(0xFF, "cda2", 0x0, 0x1)
    Jump("loc_531")

    label("loc_519")

    SetMapObjFrame(0xFF, "cgf2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "cda2", 0x1, 0x1)

    label("loc_531")

    Return()

    # Function_4_40A end

    def Function_5_532(): pass

    label("Function_5_532")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "\"Delicious hot pot dish pot\" is available.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('料理手册', 0x0)"), scpexpr(EXPR_END)), "loc_5D9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D9")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "\"Yu Feng Shaoxing pot\"\x07\x00",
            "I learned the recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_5D9")

    TalkEnd(0xFF)
    Return()

    # Function_5_532 end

    def Function_6_5DD(): pass

    label("Function_6_5DD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_812")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_749")

    NpcTalk(
        0x8,
        "Soldier Furmy",
        (
            "Douglas deputy commander,\x01",
            "Today's response in Crosbell City\x01",
            "It seems that we are considering it.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Furmy",
        (
            "That pale big tree, it is likely to happen\x01",
            "Invasion of the Empire and the Republic … …\x01",
            "Because there are still many problems.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Furmy",
        (
            "As a defense army, how much\x01",
            "I do not know if I can do it … …\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Furmy",
        (
            "Do not abandon hope\x01",
            "I want to do my best.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_80D")

    label("loc_749")


    NpcTalk(
        0x8,
        "Soldier Furmy",
        (
            "Douglas deputy commander,\x01",
            "Today's response in Crosbell City\x01",
            "It seems that we are considering it.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Furmy",
        (
            "As a defense army, how much\x01",
            "I do not know if I can do it … …\x01",
            "I want to do my best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_80D")

    Jump("loc_136D")

    label("loc_812")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_A09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_960")

    ChrTalk(
        0x8,
        (
            "Noel's serious … …\x01",
            "Little sister, really saved\x01",
            "It was good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108FYeah … … Looking at the damage of the guard\x01",
            "Frankly I am not happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "…… Yeah, honest\x01",
            "We have endured it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Because of this situation\x01",
            "Noel's sister's saved things\x01",
            "I am very happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103F……Excuse me.\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A04")

    label("loc_960")


    ChrTalk(
        0x8,
        (
            "Because of this situation,\x01",
            "We have to endure\x01",
            "I do not think so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To protect the crossbell\x01",
            "Burn its life and devote … …\x01",
            "Because that is the mission of the guard.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A04")

    Jump("loc_136D")

    label("loc_A09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_B75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AF0")

    ChrTalk(
        0x8,
        "Yesterday's train derailment accident ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Residents' voting is approaching\x01",
            "What happened at this timing\x01",
            "Thinking again, the two major countries … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "…… Branding should not be done\x01",
            "I understand it,\x01",
            "I will absolutely oblige you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B70")

    label("loc_AF0")


    ChrTalk(
        0x8,
        (
            "Yesterday's train derailment accident,\x01",
            "After all either of the two major powers … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The pressure is increasing day by day,\x01",
            "I will absolutely oblige you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B70")

    Jump("loc_136D")

    label("loc_B75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_D53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C98")

    ChrTalk(
        0x8,
        (
            "As a result of the referendum,\x01",
            "Whether it is actually going to be independent\x01",
            "It is said that it is still uncertain … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Empire and republic pressure is increasing\x01",
            "Given this situation, its influence is\x01",
            "It should be regarded as a threat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The referendum is that we\x01",
            "Beyond thinking, to neighboring countries\x01",
            "It seems to have a big impact.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D4E")

    label("loc_C98")


    ChrTalk(
        0x8,
        (
            "Empire and republic pressure is increasing\x01",
            "Given this situation, its influence is\x01",
            "It should be regarded as a threat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The referendum is that we\x01",
            "Beyond thinking, to neighboring countries\x01",
            "It seems to have a big impact.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D4E")

    Jump("loc_136D")

    label("loc_D53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_DCC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D6E")
    Call(0, 7)
    Jump("loc_DC7")

    label("loc_D6E")


    ChrTalk(
        0x8,
        (
            "The Republic is pressuring day by day\x01",
            "It seems to be strengthening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I can not get rid of it …\x02",
    )

    CloseMessageWindow()

    label("loc_DC7")

    Jump("loc_136D")

    label("loc_DCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_F28")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E8B")

    ChrTalk(
        0x8,
        (
            "Douglas deputy commander,\x01",
            "For a meeting of measures against terrorism\x01",
            "I headed to the Belgard gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Before the plenary session begins,\x01",
            "Anyway, we have a security system\x01",
            "I want to be perfect.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F23")

    label("loc_E8B")


    ChrTalk(
        0x8,
        (
            "Douglas deputy commander,\x01",
            "For a meeting of measures against terrorism\x01",
            "I headed to the Belgard gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If it is Sonja Commander,\x01",
            "Perfect security system surely\x01",
            "You will be able to arrange it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F23")

    Jump("loc_136D")

    label("loc_F28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_11FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1152")

    ChrTalk(
        0x8,
        (
            "Transfer of Sonja Command\x01",
            "Sergeant Noel's supervisor\x01",
            "It has overlapped, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Thanks to the Tangram gate\x01",
            "Girls ratio has fallen … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FWell, it can not be helped\x01",
            "I'm sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Well, someone to rumor in the middle of the night\x01",
            "I got lost, I'm lonely ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FEr …\x01",
            "It is against male members\x01",
            "Do not talk about it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHuh, I do not know.\x02\x03",
            "#10309FAs for girls' rumors,\x01",
            "If there were a man on the spot\x01",
            "Almost nothing you can not do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(To, I think it is prejudiced … …\x01",
            "Do not feel delicious things. )\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11F5")

    label("loc_1152")


    ChrTalk(
        0x8,
        (
            "Noel Sergeant … … as soon as possible to the guard\x01",
            "Please come back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "By then, a lot of gossip\x01",
            "I'm stocking it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106F(Well, it seems to be difficult if I return … …)\x02",
    )

    CloseMessageWindow()

    label("loc_11F5")

    Jump("loc_136D")

    label("loc_11FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_136D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12E8")

    ChrTalk(
        0x8,
        (
            "Prior to Douglas,\x01",
            "It has been released and for a long time to the police school\x01",
            "I heard he was working … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The other day, at the request of Sonya command\x01",
            "Again to work for the guard\x01",
            "I became it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We also want to return the deputy commander\x01",
            "I am very pleased.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_136D")

    label("loc_12E8")


    ChrTalk(
        0x8,
        (
            "Douglas deputy commander, from long ago\x01",
            "As a very good security guard\x01",
            "It was known.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We also want to return the deputy commander\x01",
            "I am very pleased.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_136D")

    TalkEnd(0xFE)
    Return()

    # Function_6_5DD end

    def Function_7_1371(): pass

    label("Function_7_1371")

    OP_4B(0x8, 0xFF)

    ChrTalk(
        0x8,
        "── The report is over.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "got it,\x01",
            "Mimic exercises at Tangram Hills ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Although it is a small scale,\x01",
            "How to apply pressure obviously\x01",
            "I am getting ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes, until the referendum\x01",
            "I can not relax.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Cooperating with each direction\x01",
            "There will only be warning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "It was a hard work, I will continue to ask for monitoring.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Ha!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 2)
    OP_4C(0x8, 0xFF)
    Return()

    # Function_7_1371 end

    def Function_8_14CA(): pass

    label("Function_8_14CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14F3")
    Call(0, 11)
    Return()

    label("loc_14F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1518")
    Call(0, 20)
    Return()

    label("loc_1518")

    Call(0, 9)
    Return()

    # Function_8_14CA end

    def Function_9_151C(): pass

    label("Function_9_151C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1545")
    Call(0, 11)
    Return()

    label("loc_1545")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_156A")
    Call(0, 20)
    Return()

    label("loc_156A")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_21E3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_1DAE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1732")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1695")

    ChrTalk(
        0x9,
        (
            "Seems to release the blockade of the battlefield\x01",
            "I have already contacted you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "From the Almorica Kodo direction\x01",
            "Toward the occurrence of the demonic beast.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "As a guard, to devastate monsters\x01",
            "It is a heartbreaking thought not to break hands ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you guys have this matter\x01",
            "I believe it will solve it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_172D")

    label("loc_1695")


    ChrTalk(
        0x9,
        (
            "Seems to release the blockade of the battlefield\x01",
            "I have already contacted you.\x02\x03",
            "Toward the site from the old road direction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you guys have this matter\x01",
            "I believe it will solve it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_172D")

    Jump("loc_1DAA")

    label("loc_1732")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D15")

    ChrTalk(
        0x9,
        "It was a pleasure, the support department.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Although there are still many problems,\x01",
            "Thanks to what I was pondering\x01",
            "I got one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Because of the damage received in that raid incident,\x01",
            "It was a place where manpower was not enough.\x01",
            "I really appreciate it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FNo, when in trouble you are mutually exclusive.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F…… The damage of the guard\x01",
            "It was truly enormous.\x02\x03",
            "#00101FThe prospect of rebuilding in the future,\x01",
            "How long is it standing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "… … In response to this tension condition,\x01",
            "I have not told you to be honest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "However, if Noel's return to the guard\x01",
            "You will be able to turn your hands there as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In that case, by all means at the right post\x01",
            "Have the organization contribute to rebuilding\x01",
            "It will be.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19BC")
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)

    label("loc_19BC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19DF")
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)

    label("loc_19DF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A02")
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)

    label("loc_1A02")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A22")
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_1A22")

    Sleep(1000)

    ChrTalk(
        0x104,
        "#00305FThat's … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10108F…… Do you mean promotion?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "…… The damage of the guard this time\x01",
            "In a way it was the biggest one,\x01",
            "It is damage to \"morale\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Under the shock of fellow sacrifice,\x01",
            "To the fear of the role of the guard itself\x01",
            "There will be quite a few people eroded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Some of the members,\x01",
            "Based on anger and arrogance\x01",
            "It seems that somehow it keeps it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F……I agree.\x01",
            "Such feelings\x01",
            "It is communicating with Shishihashi.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "To regain lost morale,\x01",
            "An excellent officer is certainly necessary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Although it is not a definite matter yet …\x01",
            "You have that ability\x01",
            "There should be enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103F… … like three lieutenant Mireille\x01",
            "I do not know if I can do it … …\x02\x03",
            "#10101FIf that happens, please respectfully,\x01",
            "I will do my mission.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm sorry.\x01",
            "It will be a painful time for a while,\x01",
            "I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x19D, 3)
    Jump("loc_1DAA")

    label("loc_1D15")


    ChrTalk(
        0x9,
        (
            "In order to rebuild the guard,\x01",
            "About the proper post to the sergeant\x01",
            "You will be asked to lend your power.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It will be a painful time for a while,\x01",
            "I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DAA")

    TalkEnd(0x9)
    Return()

    label("loc_1DAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2149")

    ChrTalk(
        0x9,
        (
            "I received in that series of events\x01",
            "The damage of the guard is immeasurable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "As soon as Sergeant Noel returns to the guard,\x01",
            "To properly rebuild the organization with appropriate post\x01",
            "It will be a contribution.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005Fthat's……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10108F…… Do you mean promotion?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "…… The damage of the guard this time\x01",
            "In a way it was the biggest one,\x01",
            "It is damage to \"morale\".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Under the shock of fellow death,\x01",
            "To the fear of the role of the guard itself\x01",
            "There will be quite a few people eroded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Some of the members,\x01",
            "Based on anger and arrogance\x01",
            "It seems that somehow it keeps it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F……I agree.\x01",
            "Such feelings\x01",
            "It is communicating with Shishihashi.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "To regain lost morale,\x01",
            "An excellent officer is certainly necessary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Although it is not a definite matter yet …\x01",
            "You have that ability\x01",
            "There should be enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103F… … like three lieutenant Mireille\x01",
            "I do not know if I can do it … …\x02\x03",
            "#10101FIf that happens, please respectfully,\x01",
            "I will do my mission.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm sorry.\x01",
            "It will be a painful time for a while,\x01",
            "I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18E, 3)
    Jump("loc_21DE")

    label("loc_2149")


    ChrTalk(
        0x9,
        (
            "In order to rebuild the guard,\x01",
            "About the proper post to the sergeant\x01",
            "You will be asked to lend your power.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It will be a painful time for a while,\x01",
            "I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21DE")

    Jump("loc_3577")

    label("loc_21E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_27DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x170, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_249A")

    ChrTalk(
        0x9,
        (
            "You guys,\x01",
            "Yesterday at the scene of derailment accident\x01",
            "I heard that it was of great utility.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FThe leader of our support department\x01",
            "He was a big success.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FChopper\x01",
            "As expected it lifts too much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100FHehe, it will not be such a thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I taught at the police school is\x01",
            "Battle technology was the main … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Lloyd, you are\x01",
            "I was growing up as a fine investigator.\x01",
            "You are deeply impressed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FFu, to deputy commander ……\x02\x03",
            "#00003F…… I really do not have that much yet.\x01",
            "It does not extend to my brother 's feet.\x02\x03",
            "#00000FI will fill the difference\x01",
            "Because I only have friends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FMr. Lloyd ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Huh, that is fine.\x01",
            "As it is, you are everywhere\x01",
            "You can grow up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I am looking forward to the future, Lloyd.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x170, 2)
    Jump("loc_27D5")

    label("loc_249A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2691")

    ChrTalk(
        0x9,
        "Oh, remember that … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You guys,\x01",
            "Why do not you read this book?\x02",
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
            scpstr(SCPSTR_CODE_ITEM, '沐浴阳光的阿尼艾丝９卷'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "I got it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('沐浴阳光的阿尼艾丝９卷', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x189, 0)

    ChrTalk(
        0x102,
        "#00105FIs this … … an entertainment novel?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FDouglas' older brother,\x01",
            "It is surprising that you read such monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Haha, I even read novels.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "That's the Sonja command\x01",
            "I was advised, but ….\x01",
            "As you know, I am busy lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, that's why.\x01",
            "You may enjoy it even when you have time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah, thank you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_27D5")

    label("loc_2691")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_274C")

    ChrTalk(
        0x9,
        "Well, as it is … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It's been overnight since the derailment accident.\x01",
            "It will be soon to be completely relieved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "For a while the guard\x01",
            "Those who were alarmed near the railroad\x01",
            "It might be nice.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_27D5")

    label("loc_274C")


    ChrTalk(
        0x9,
        (
            "It's been overnight since the derailment accident.\x01",
            "It will be soon to be completely relieved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "For a while the guard\x01",
            "Those who were alarmed near the railroad\x01",
            "It might be nice.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27D5")

    Jump("loc_3577")

    label("loc_27DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2B22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x170, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A86")

    ChrTalk(
        0x9,
        (
            "I found out by your investigation\x01",
            "Doing with \"pre-prince grass\" ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "That \"Gnostic\"\x01",
            "It was a raw material.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It's a nasty medicine\x01",
            "I thought that … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FReally……\x01",
            "The deputy commander is also a case incident\x01",
            "You were at the police school, were not you?\x02\x03",
            "#00003FThe manipulated guard is\x01",
            "At that scene where I first attacked … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FAh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "…… Members are being manipulated\x01",
            "When suddenly attacking,\x01",
            "To be honest, I was surprised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "After all, I and the police school personnel\x01",
            "I could not cope … from the detention center\x01",
            "A secretary#4RErnest#I got missed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108FIs that so……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "A medicine which is powdered with that power only,\x01",
            "It was also the cause of the appearance of eidolons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "This bastard beast commotion ……\x01",
            "Beyond being thoughtful Yama\x01",
            "Maybe it is.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x170, 1)
    Jump("loc_2B1D")

    label("loc_2A86")


    ChrTalk(
        0x9,
        (
            "A medicine which is powdered with that power only,\x01",
            "It was also the cause of the appearance of eidolons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "This bastard beast commotion ……\x01",
            "Beyond being thoughtful Yama\x01",
            "Maybe it is.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B1D")

    Jump("loc_3577")

    label("loc_2B22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2BC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B3D")
    Call(0, 7)
    Jump("loc_2BC3")

    label("loc_2B3D")


    ChrTalk(
        0x9,
        (
            "As you can see, it is very \"a phantom beast\"\x01",
            "There seems to be no room to spare hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You have trouble with you,\x01",
            "I asked for the survey.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BC3")

    Jump("loc_3577")

    label("loc_2BC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2BD6")
    Jump("loc_3577")

    label("loc_2BD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3338")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31F1")

    ChrTalk(
        0x109,
        "#10100FDeputy commander, good job!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Oh, you guys.\x01",
            "You came here exactly right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I will try my best to relax.\x01",
            "I was just thinking,\x01",
            "Because it is a point, go slowly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FBecause it's about my older brother.\x01",
            "Also, socializing with exercises\x01",
            "I thought I should tell him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It is mountains that I want to do,\x01",
            "As expected it is not long time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009Fmy mother……\x01",
            "It looks like you are busy indeed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Anyway\x01",
            "Because it is a plenary session tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Once, the security system during the trade conference\x01",
            "Although I intend to do it perfectly,\x01",
            "The situation always changes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I guard Michelam\x01",
            "Both Sonja Commander and Miyuji again\x01",
            "You will need to make arrangements.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FI agree……\x01",
            "The state guests at the Orchis Tower\x01",
            "We will meet together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FNo matter how much you prepare\x01",
            "It probably will not be too much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FWell, let's leave it to the guard\x01",
            "You can rest assured for the time being.\x02\x03",
            "#00304FAnyway, the current security guard,\x01",
            "There is also \"Douglas of the Thunder\".\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F75")
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)

    label("loc_2F75")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F9F")
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)

    label("loc_2F9F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FC9")
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)

    label("loc_2FC9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FF0")
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    label("loc_2FF0")

    Sleep(1000)

    ChrTalk(
        0x109,
        "#10105FAmidst … ….?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Haha, I also have a nostalgic name\x01",
            "I brought it out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Before toba in police school,\x01",
            "It was called partly like that\x01",
            "There is a time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "However, it is a thunderous demon ……\x01",
            "Everyone's a selfish name\x01",
            "I will call you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHahaha\x01",
            "I think that it suits you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Do not be crowded Do not crowd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Kohon, I will return the story, but …\x01",
            "The security of the trade council is thoroughly\x01",
            "I will do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You do not care much about you,\x01",
            "Please serve our own work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, I will.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x159, 0)
    Jump("loc_3333")

    label("loc_31F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32BD")

    ChrTalk(
        0x9,
        (
            "\"Thunder\"? ….\x01",
            "Haha, I have two nostalgic names.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Kohon, anyway … …\x01",
            "The security of the trade council is thoroughly\x01",
            "I will do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You do not care much about you,\x01",
            "Please serve our own work.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3333")

    label("loc_32BD")


    ChrTalk(
        0x9,
        (
            "The security of the trade council is thoroughly\x01",
            "I will do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You do not care much about you,\x01",
            "You should try your own work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3333")

    Jump("loc_3577")

    label("loc_3338")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3577")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3577")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34FA")

    ChrTalk(
        0x9,
        (
            "#4PParticipation in the exercise was a pain.\x01",
            "If there is something again I will ask.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#4PAlso, although it's about a while ago ……\x01",
            "Especially in the \"story only here\"\x01",
            "Will you keep it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FI understand.\x01",
            "Anyway here\x01",
            "Be careful - ─\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F…… Next time, for Tiio\x01",
            "I have to tell you ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309FHuh, that's right.\x01",
            "It is unfair.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011FHey there!\x01",
            "Do not let me retract the predecessor with haste!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#4P… … I asked for it.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3577")

    label("loc_34FA")


    ChrTalk(
        0x9,
        (
            "#4PParticipation in the exercise was a pain.\x01",
            "If there is something again I will ask.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#4P…… Also,\x01",
            "To \"Only this story\"\x01",
            "Please do it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3577")

    TalkEnd(0x9)
    Return()

    # Function_9_151C end

    def Function_10_357B(): pass

    label("Function_10_357B")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-1120, 900, -310, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x9, 6630, 0, -20, 270)
    SetChrPos(0x101, -5500, 0, -20, 90)
    SetChrPos(0x102, -5500, 0, -20, 90)
    SetChrPos(0x104, -5500, 0, -20, 90)
    SetChrPos(0x109, -5500, 0, -20, 90)
    SetChrPos(0x105, -5500, 0, -20, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(105, 0, 100, 0)
    BeginChrThread(0x101, 3, 0, 12)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 13)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 14)
    OP_68(930, 900, -520, 3000)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 15)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 16)
    WaitChrThread(0x105, 3)
    OP_6F(0x79)

    ChrTalk(
        0x9,
        "#11P─ ─ We finally came.\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#00002FAh……\x02",
    )

    CloseMessageWindow()
    OP_68(3420, 900, 80, 3000)
    MoveCamera(45, 19, 0, 3000)
    OP_6E(350, 3000)
    SetCameraDistance(25500, 3000)

    def lambda_377E():
        OP_98(0xFE, 0x9C4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_377E)
    Sleep(100)

    def lambda_379B():
        OP_98(0xFE, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_379B)
    Sleep(100)

    def lambda_37B8():
        OP_98(0xFE, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_37B8)
    Sleep(100)

    def lambda_37D5():
        OP_98(0xFE, 0xAF0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_37D5)
    Sleep(100)

    def lambda_37F2():
        OP_98(0xFE, 0x9C4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_37F2)
    Sleep(1000)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x109,
        (
            "#10100FDouglas deputy commander ……\x01",
            "Is cheers for good work!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PYeah, seeker, sergeant.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWith the Special Affairs Support Division\x01",
            "How is comfortable?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FHa!\x01",
            "Let me study various things everyday\x01",
            "We have it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PHaha, that is the most important.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PFor the future as well,\x01",
            "You better steadfastly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00105FNoel, this one … ….?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P…… Oops, self-introduction\x01",
            "It was not yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PMy name is Douglas.\x01",
            "This time, the\x01",
            "He is the one who took office as a deputy commander.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAbout you\x01",
            "I heard from the commander in detail.\x01",
            "I hope to keep you informed later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00100FThank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FHuff, as it looks\x01",
            "It looks like a person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00300FYou look good as usual,\x01",
            "Douglas's older brother.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PYou also, Randy.\x01",
            "Rehabilitation training at the Belgard gate,\x01",
            "It was a pain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAlso with Lloyd.\x01",
            "It is a long time to see you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIn the case of the previous cult,\x01",
            "He seems to have played a lot for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000Fmy mother……\x01",
            "long time no see.\x02\x03",
            "#00004FInstructor to deputy commander\x01",
            "I heard you got it.\x01",
            "I was really surprised.\x02\x03",
            "#00012FTo that \"Douglas of demons\"\x01",
            "Memory that was narrowed down\x01",
            "It is said that it revived clearly ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PHey, old nickname something\x01",
            "I will not bring it out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PIt would be embarrassing at all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100F(Well, at the police school\x01",
            "You seem to be a tough person … …)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P…… Oops,\x01",
            "I will keep it for about this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PBother for work today.\x01",
            "Because you had me come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FWhen I say work …\x01",
            "\"Request for participation in exercises\" is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11POh, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThis exercise, you\x01",
            "The purpose is to rethink the Special Affairs Support Division.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PMy strict training\x01",
            "You will receive patchy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00005FHeck …\x01",
            "Not a guard,\x01",
            "Is it for us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWell, of course, also to security guards\x01",
            "It will be a nice experience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIn addition, in the upper part of the police\x01",
            "You have already talked.\x01",
            "It is a nominal official joint training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00300FI see……\x01",
            "Rather than a support request\x01",
            "It is a proper training and discretion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PHa ha, that's what it is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI am already prepared for this.\x01",
            "The rest depends on you … …\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(500)

    ChrTalk(
        0x102,
        (
            "#12P#00100FOnce you arrange the equipment\x01",
            "It might be nice.\x02\x03",
            "#00104FThe composition of quartz is also\x01",
            "It might be better to review.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11Pwhat will you do,\x01",
            "Can I start exercises soon?\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x6F, 0x1, 0x0)
    Call(0, 17)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_10_357B end

    def Function_11_4045(): pass

    label("Function_11_4045")

    EventBegin(0x0)
    Fade(500)
    OP_68(3420, 900, 80, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, 2500, 0, -20, 90)
    SetChrPos(0x109, 2500, 0, 980, 90)
    SetChrPos(0x102, 2500, 0, -1020, 90)
    SetChrPos(0x104, 1300, 0, 680, 90)
    SetChrPos(0x105, 1000, 0, -720, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()

    ChrTalk(
        0x9,
        (
            "#11PFor the training of the men,\x01",
            "Please do exercise opportunities\x01",
            "I wanted you to do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI am already prepared for this.\x01",
            "Can I start exercises soon?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 17)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_11_4045 end

    def Function_12_4177(): pass

    label("Function_12_4177")


    def lambda_417C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_417C)

    def lambda_418D():
        OP_98(0xFE, 0x157C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_418D)
    WaitChrThread(0x101, 1)
    Return()

    # Function_12_4177 end

    def Function_13_41A7(): pass

    label("Function_13_41A7")


    def lambda_41AC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_41AC)

    def lambda_41BD():
        OP_98(0xFE, 0xFA0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_41BD)
    WaitChrThread(0x109, 1)
    OP_97(0x109, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
    OP_97(0x109, 0x3E8, 0x0, 0x0, 0x7D0, 0x0)
    Return()

    # Function_13_41A7 end

    def Function_14_41FF(): pass

    label("Function_14_41FF")


    def lambda_4204():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4204)

    def lambda_4215():
        OP_98(0xFE, 0xFA0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4215)
    WaitChrThread(0x102, 1)
    OP_97(0x102, 0x0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
    OP_97(0x102, 0x3E8, 0x0, 0x0, 0x7D0, 0x0)
    Return()

    # Function_14_41FF end

    def Function_15_4257(): pass

    label("Function_15_4257")


    def lambda_425C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_425C)

    def lambda_426D():
        OP_98(0xFE, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_426D)
    WaitChrThread(0x104, 1)
    OP_97(0x104, 0x3E8, 0x0, 0x2BC, 0x7D0, 0x0)
    OP_93(0x104, 0x5A, 0x1F4)
    Return()

    # Function_15_4257 end

    def Function_16_42A2(): pass

    label("Function_16_42A2")


    def lambda_42A7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_42A7)

    def lambda_42B8():
        OP_98(0xFE, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_42B8)
    WaitChrThread(0x105, 1)
    OP_97(0x105, 0x3E8, 0x0, 0xFFFFFD44, 0x7D0, 0x0)
    OP_93(0x105, 0x5A, 0x1F4)
    Return()

    # Function_16_42A2 end

    def Function_17_42ED(): pass

    label("Function_17_42ED")

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
            "【Start exercise】\x01",            # 0
            "【Not ready】\x01",      # 1
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
        (0, "loc_4365"),
        (1, "loc_436D"),
        (SWITCH_DEFAULT, "loc_4402"),
    )


    label("loc_4365")

    Call(0, 18)
    Jump("loc_4402")

    label("loc_436D")


    ChrTalk(
        0x101,
        (
            "#6P#00000Fexcuse me……\x01",
            "Can I have a little time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PHmm, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThen, when you are ready\x01",
            "Try call me again.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x152, 0)
    Jump("loc_4402")

    label("loc_4402")

    Return()

    # Function_17_42ED end

    def Function_18_4403(): pass

    label("Function_18_4403")


    ChrTalk(
        0x101,
        (
            "#6P#00000FWell, also here\x01",
            "I am ready.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x5A, 0x1F4)
    Sleep(500)

    ChrTalk(
        0x9,
        "#11PAlright.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PSergeant Caucha,\x01",
            "Because the guard is the other party\x01",
            "Do not be confused.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PBy opposing security guards\x01",
            "There will be new things to learn as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FHah, I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThen,\x01",
            "You will start practicing quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PEveryone, outdoor parking lot\x01",
            "Please move.\x02",
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
            "Quest 【Request to participate in guard exercises】\x07\x00",
            "I started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x6F, 0x1, 0x1)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x22, 1)
    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_18_4403 end

    def Function_19_45CD(): pass

    label("Function_19_45CD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(3420, 900, 80, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x9, 6630, 0, -20, 270)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x101, 2500, 0, -20, 90)
    SetChrPos(0x109, 2500, 0, 980, 90)
    SetChrPos(0x102, 2500, 0, -1020, 90)
    SetChrPos(0x104, 1300, 0, 680, 90)
    SetChrPos(0x105, 1000, 0, -720, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x9,
        (
            "#11P── Once again,\x01",
            "It was a hard time to participate in the exercise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAlso for men\x01",
            "It should have been a nice experience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FNo, thank you for us.\x01",
            "I think that it was a very good experience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FHurry up, you\x01",
            "I have not decayed at all.\x02\x03",
            "#00300FIn the first exercise\x01",
            "I remembered that it was torn down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThat kind of you\x01",
            "You seem to have grown quite easily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PStanhalvard I taught, too,\x01",
            "You seem to have made it completely yours.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304FOh yeah, it must be now\x01",
            "Super stylish & elegant\x01",
            "I evolved into Randy style.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FStan Halberd … ….\x01",
            "Is that so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00109FHehe, for Randy\x01",
            "It was like a benefactor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWell, this guy makes a rifle\x01",
            "I did not want to handle it\x01",
            "That's why I concentrated on it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIs that worth it?\x01",
            "Halvard alone can make a good difference\x01",
            "You are trying to get your strength.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIt dislikes the former commander\x01",
            "It seems that it also became a factor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00300FWell, well-disciplined is\x01",
            "It is not my sex.\x02\x03",
            "#00309FThanks to you I moved to the support department,\x01",
            "I am sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FHuff, better or worse\x01",
            "Thanks to Deputy Commander\x01",
            "I guess.\x02\x03",
            "#10302FGoing back to the police school\x01",
            "After all it was a misunderstanding\x01",
            "Looks like it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FUntil the example of the cult incident,\x01",
            "The guard is the former commander\x01",
            "Because I was under command.\x02\x03",
            "#10109FEven without it, the deputy commander,\x01",
            "Trust from subordinates is thick\x01",
            "There was also ability.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIt's not such a big monke … …\x01",
            "Well, I guess it was an eyesore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAfter going to the police school,\x01",
            "I can rebuild that rotten regime\x01",
            "I was concentrating on developing human resources.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PNow thinking, in a sense\x01",
            "It might have been lucky either.\x01",
            "I do not think so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIt has not been tinted in any color yet\x01",
            "Keep guards and police officers eggs\x01",
            "I was educated.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00012FAs expected\x01",
            "I thought it was too strict.\x02\x03",
            "#00006FFranz something\x01",
            "I was crying once in a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWell, do not say so.\x01",
            "I guess it's getting nice?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWell, there were various\x01",
            "I came back to the guard in this way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PFrom now on you both\x01",
            "Together, both autonomous states\x01",
            "I will protect you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FWhatching\x01",
            "I will do my best.\x02\x03",
            "#00104FHow much more are we?\x01",
            "Immature is also a nice place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PNothing will be humble.\x01",
            "You guys have that power\x01",
            "You should have it properly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PSergei Senpai launched\x01",
            "At the Special Affairs Support Division, firmly\x01",
            "Thanks for working.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#6P#00005FSergei senior … …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00305FWhy, both that fellow\x01",
            "Did you know him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PAh? I do not know anything …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWith Sergei seniors\x01",
            "To Senya,\x01",
            "You have been taken care of from long ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI, the marriage of those two\x01",
            "You got mediated.\x02",
        )
    )

    CloseMessageWindow()
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

    ChrTalk(
        0x101,
        "#6P#00011FKEEP! It is! It is! It is!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4S#6P#00105Fmarriage…………! Is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#4S#10111FWith Sonya command,\x01",
            "Sergei section manager! Is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10305FWow ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FCome on,\x01",
            "Suddenly shocking facts\x01",
            "Bukkake fighting ……!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P…… What, what.\x01",
            "You did not know them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWell, about five years ago\x01",
            "I have parted because of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PSergei's seniors' transition\x01",
            "Promotion of Senya's seniors,\x01",
            "Because various kinds overlapped ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FHuh, I see.\x01",
            "Adult man and woman unique\x01",
            "It seems there was a drama.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FWow …\x01",
            "That Sonja command … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00303FSurely nothing\x01",
            "I thought that it was suspicious … …\x02\x03",
            "#00309FSomehow, a mystery\x01",
            "I feel like I could solve it ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00011FWait, hey guys ……\x01",
            "Do not stop being interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00109F(Wow, me too\x01",
            "I am worried … …)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#11P……Oops.\x01",
            "Have you slipped your mouth carelessly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAnd anyway.\x01",
            "Not much about this matter\x01",
            "Do not speak anything with fluent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PKohon, for now tentatively …\x01",
            "It was a pain to work on the exercise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PIf there is something again, I will ask you for my best regards.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FYes.\x01",
            "I am waiting for contact.\x02",
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
            "Quest 【Request to participate in guard exercises】\x07\x00",
            "Achieved!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_29(0x6F, 0x1, 0x4)
    OP_29(0x6F, 0x1, 0x5)
    OP_29(0x6F, 0x4, 0x10)
    OP_29(0xA3, 0x1, 0x4)
    SetChrPos(0x0, 3000, 0, 0, 90)
    EventEnd(0x5)
    Return()

    # Function_19_45CD end

    def Function_20_560F(): pass

    label("Function_20_560F")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(3420, 900, 80, 0)
    MoveCamera(44, 23, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, 2500, 0, -20, 90)
    SetChrPos(0x102, 2300, 0, -1020, 90)
    SetChrPos(0x103, 2300, 0, 980, 90)
    SetChrPos(0x104, 1000, 0, -20, 90)
    SetChrPos(0x109, 900, 0, 980, 90)
    SetChrPos(0x105, 900, 0, -1020, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_93(0x9, 0x10E, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D35")

    ChrTalk(
        0x101,
        (
            "#6P#00000FDouglas deputy commander,\x01",
            "Is cheers for good work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAre you … like you …?\x01",
            "Good work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PApparently, looking at the request\x01",
            "You seem to have come?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00300FYeah, that's right\x02\x03",
            "#00303F…… Brother Douglas,\x01",
            "I'm kind of sick.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_59E6")

    ChrTalk(
        0x9,
        (
            "#11PAs you enter the gate\x01",
            "I guess you are feeling confusion … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PCurrently, the Crossbell Guard\x01",
            "You are in a strict caution.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PBesides, wanted burgers\x01",
            "To force things through the gate\x01",
            "It has happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThat's why more and more\x01",
            "I am out of my mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00100FOh really……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWell, if you wanted a person you wanted\x01",
            "She seems to have caught it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PRegarding that,\x01",
            "Let me thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FNo, until we did the obvious thing.\x02\x03",
            "#00001F…… The request for this time\x01",
            "Is that related?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CA0")

    label("loc_59E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_5BA1")

    ChrTalk(
        0x9,
        (
            "#11PAs you enter the gate\x01",
            "I guess you are feeling confusion … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PCurrently, the Crossbell Guard\x01",
            "You are in a strict caution.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PBesides, unwilling fellows\x01",
            "To force things through the gate\x01",
            "It has happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThat's why,\x01",
            "I am out of my mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00100FOh really……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F(We missed it.\x01",
            "Is it thieves of medical supplies … …)\x02\x03",
            "#00001F…… But even this request\x01",
            "Is that related?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5CA0")

    label("loc_5BA1")


    ChrTalk(
        0x9,
        (
            "#11PAs you enter the gate\x01",
            "I guess you are feeling confusion … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PCurrently, the Crossbell Guard\x01",
            "You are in a strict caution.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PA little idiot,\x01",
            "I am out of my mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001FI see……\x01",
            "The request for this time also\x01",
            "Is that related?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CA0")


    ChrTalk(
        0x9,
        "#11PYes, exactly\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PImmediately, the contents of work\x01",
            "I will try to explain it … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PYou guys,\x01",
            "Will you accept the request?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D8B")

    label("loc_5D35")


    ChrTalk(
        0x9,
        "#11PHave you got your hands empty?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PI would like you to undertake the request immediately …\x02",
    )

    CloseMessageWindow()

    label("loc_5D8B")

    Call(0, 21)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 2710, 0, -330, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_20_560F end

    def Function_21_5DBA(): pass

    label("Function_21_5DBA")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E25")
    Call(0, 22)
    Jump("loc_5F08")

    label("loc_5E25")


    ChrTalk(
        0x101,
        (
            "#6P#00006F……Excuse me.\x01",
            "This is also a job I have on hand\x01",
            "It is full a lot ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PHM……\x01",
            "Well, it's such a time\x01",
            "Maybe it can not be helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11POkay, if my hands are empty\x01",
            "Let's ask again.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x19B, 3)

    label("loc_5F08")

    Return()

    # Function_21_5DBA end

    def Function_22_5F09(): pass

    label("Function_22_5F09")


    ChrTalk(
        0x101,
        "#6P#00000FYes, go ahead\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11POh great\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P─ ─ As I was writing on the request,\x01",
            "Recently, a mysterious \"black devil\" comes out\x01",
            "Eyewitness information has been received.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIn the vicinity of Almorika village etc.\x01",
            "For crops and livestock\x01",
            "It seems that damage has occurred.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105FBlack devil … …\x01",
            "What I heard somewhere\x01",
            "It is such an impression.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00303FEven attacking crops\x01",
            "It sounds familiar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FDid you mean ……\x01",
            "In the case of the \"wolf-shaped devil\" that occurred before\x01",
            "I guess they are similar.\x02\x03",
            "#10103FAt that time, the mafia manipulates\x01",
            "A military dog was the culprit … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P…… I also found that incident\x01",
            "Because I was reading in the report,\x01",
            "It is worrisome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIn fact, although Rubache was dismantled\x01",
            "Many of the owned military dogs\x01",
            "I do not understand where I am.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PBut there might be some connection to the same mechanism\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FTo what extent is the guard\x01",
            "Is the investigation progressing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PVerification of the damage site and\x01",
            "Listening to local residents\x01",
            "I just went lightly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAs a result, \"Black Demonic Beast\"\x01",
            "From the direction of the old battlefield\x01",
            "That turned out to be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThere,\x01",
            "I want you to head to the battlefield.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PSurvey of this monsters,\x01",
            "If possible, have them get rid of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FI think we get the details\x02\x03",
            "#10303FEven so, after all\x01",
            "You seem to be busy, are not you?\x02\x03",
            "#10300FThis kind of work\x01",
            "With the guard\x01",
            "I thought that … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI would like to do that … ….\x01",
            "As I said earlier,\x01",
            "The guard is in strict attitude.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIt is witnessed as Crossbell City attacker\x01",
            "\"Red constellation\" also disappears,\x01",
            "I do not even have a tail.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIn addition the Empire and the Republic\x01",
            "Trying to start a huge exercise\x01",
            "This situation ……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_6547")

    ChrTalk(
        0x9,
        (
            "#11PThere seems to be nothing like the previous one\x01",
            "As a guard, security at the border\x01",
            "It will need to be particularly strict.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_658E")

    label("loc_6547")


    ChrTalk(
        0x9,
        (
            "#11PAs a guard, security at the border\x01",
            "It will need to be particularly strict.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_658E")


    ChrTalk(
        0x102,
        (
            "#6P#00108FJust before concluding a \"non-war treaty\" ……\x01",
            "In a situation equivalent to that\x01",
            "Is not it becoming it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PRight\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PEven though much how much monster beasts are damaged,\x01",
            "Truly in this situation,\x01",
            "The priority order is lowered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThere is a serious damage to that\x01",
            "It is not confirmed,\x01",
            "I can not afford to spare people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304F……surely,\x01",
            "Militia extermination to the guard\x01",
            "It will not be a case to do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FI think we get the idea\x02\x03",
            "#00000FThen, \"Black Demonic Beast\"\x01",
            "Please leave the survey here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PRight. Sorry to spring this on you\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PWe're counting on you, SSS\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Quest 【Battlefield Research】\x07\x00",
            "I started!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x19B, 4)
    OP_29(0x91, 0x1, 0x0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 2710, 0, -330, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_22_5F09 end

    def Function_23_6851(): pass

    label("Function_23_6851")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(3420, 1800, 80, 0)
    MoveCamera(44, 23, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    SetChrPos(0x101, 2500, 0, -20, 90)
    SetChrPos(0x102, 2300, 0, -1020, 90)
    SetChrPos(0x103, 2300, 0, 980, 90)
    SetChrPos(0x104, 1000, 0, -20, 90)
    SetChrPos(0x109, 900, 0, 980, 90)
    SetChrPos(0x105, 900, 0, -1020, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_93(0x9, 0x10E, 0x0)
    OP_68(3420, 900, 80, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x101,
        (
            "#6P#00000FThat's the end of the report\x02\x03",
            "#00003FPerhaps, no more by military dogs\x01",
            "I do not think there will be any damage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PI see…\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x9)

    ChrTalk(
        0x101,
        "#6P#00012FU-uhh\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00305FWhat, Douglas's older brother.\x01",
            "Always keep silent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FI did not get rid of military dogs\x01",
            "Was it probably masculinated?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PNo, it was good work\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIt is a result beyond expectation\x01",
            "I was surprised a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FWell that's true\x02\x03",
            "#10309F\"I persuaded military dogs\"\x01",
            "Usually it is a story of a bastard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106FI certainly can not believe it\x01",
            "It might be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FBut, as it is a fact\x01",
            "I wonder if there are any problems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PNo, that's fine\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIf a peaceful solution is possible\x01",
            "It has not been better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIt was a pleasure, the support department.\x01",
            "Thanks to what I was pondering\x01",
            "I got it one by one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00004FThat's great\x02\x03",
            "#00000FAlso whenever something happens\x01",
            "please call me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PYes, will do\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P── Then we will continue to\x01",
            "Continue to take precautionary attitude.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PTake care you all\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FRight!\x02",
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
            "Quest 【Battlefield Research】\x07\x00",
            "Achieved!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x91, 0x1, 0x2)
    OP_29(0x91, 0x1, 0x3)
    OP_29(0x91, 0x4, 0x10)
    OP_50(0x6A, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 2710, 0, -330, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_23_6851 end

    SaveToFile()

Try(main)
