from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Flammie",                # 1
        "Vice Commander Douglas", # 2
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
        "Function_6_602",          # 06, 6
        "Function_7_1604",         # 07, 7
        "Function_8_178B",         # 08, 8
        "Function_9_17DD",         # 09, 9
        "Function_10_3CD7",        # 0A, 10
        "Function_11_4829",        # 0B, 11
        "Function_12_4956",        # 0C, 12
        "Function_13_4986",        # 0D, 13
        "Function_14_49DE",        # 0E, 14
        "Function_15_4A36",        # 0F, 15
        "Function_16_4A81",        # 10, 16
        "Function_17_4ACC",        # 11, 17
        "Function_18_4BE1",        # 12, 18
        "Function_19_4DEF",        # 13, 19
        "Function_20_5E6C",        # 14, 20
        "Function_21_65ED",        # 15, 21
        "Function_22_6729",        # 16, 22
        "Function_23_71D2",        # 17, 23
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
            ""Delicious Hot Pot\x01",
            "Dishes - Earthenware Pot\x01",
            "Edition" is here.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_5FE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FE")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Learned the \x07\x02",
            ""Rich Sea\x01",
            "Hot Pot"\x07\x00",
            " recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_5FE")

    TalkEnd(0xFF)
    Return()

    # Function_5_532 end

    def Function_6_602(): pass

    label("Function_6_602")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B7")

    NpcTalk(
        0x8,
        "Soldier Flammie",
        (
            "I heard Vice Commander Douglas is\x01",
            "studying the future course of action\x01",
            "in Crossbell City at present.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Flammie",
        (
            "That pale blue tree, possible invasions\x01",
            "from the Empire and Republic... There's\x01",
            "still a heap of problems.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Flammie",
        (
            "As the State Guard, I\x01",
            "don't know how much we'll\x01",
            "be able to do, but...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Flammie",
        (
            "I want to do my best\x01",
            "without abandoning hope.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_8B4")

    label("loc_7B7")


    NpcTalk(
        0x8,
        "Soldier Flammie",
        (
            "I heard Vice Commander Douglas is\x01",
            "studying the future course of action\x01",
            "in Crossbell City at present.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Flammie",
        (
            "As the State Guard, I don't know how\x01",
            "much we'll be able to do, but...\x01",
            "Somehow or other, I want to do my best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B4")

    Jump("loc_1600")

    label("loc_8B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_AF4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A51")

    ChrTalk(
        0x8,
        (
            "Sergeant Major Noｱl...\x01",
            "I'm really glad your\x01",
            "sister is safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108FYes... Although considering the\x01",
            "damage to the CGF, I honestly\x01",
            "can't be happy about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Yes. To be honest,\x01",
            "it's unbearable for us\x01",
            "too, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Precisely because the situation is\x01",
            "like this, the fact that your sister\x01",
            "is safe is a very happy thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103F...Thank you. Thank you\x01",
            "very much.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_AEF")

    label("loc_A51")


    ChrTalk(
        0x8,
        (
            "Precisely because\x01",
            "situation is like this,\x01",
            "we have to endure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To burn and sacrifice our\x01",
            "lives to protect Crossbell...\x01",
            "That's the mission of the CGF.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AEF")

    Jump("loc_1600")

    label("loc_AF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_C9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BF0")

    ChrTalk(
        0x8,
        (
            "Yesterday's derailment\x01",
            "accident...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Thinking about its timing and\x01",
            "the approaching referendum, as\x01",
            "suspected the major powers...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...I know we can't say for\x01",
            "sure, but it's suspicious, no\x01",
            "matter how you look at it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C97")

    label("loc_BF0")


    ChrTalk(
        0x8,
        (
            "Yesterday derailment\x01",
            "accident... As suspected,\x01",
            "one of the major powers...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "With the pressure rising day\x01",
            "by day, it's suspicious no\x01",
            "matter how you look at it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C97")

    Jump("loc_1600")

    label("loc_C9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_EFC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E12")

    ChrTalk(
        0x8,
        (
            "Even after the result of the referendum,\x01",
            "they say it's still uncertain if\x01",
            "independence will take off for real...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Thinking about this situation with additional\x01",
            "pressure from the Empire and Republic, those\x01",
            "influences are perceived as a threat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The referendum seems to be having\x01",
            "bigger effect on neighboring\x01",
            "countries than we thought.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_EF7")

    label("loc_E12")


    ChrTalk(
        0x8,
        (
            "Thinking about this situation with additional\x01",
            "pressure from the Empire and Republic, those\x01",
            "influences are perceived as a threat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The referendum seems to be having\x01",
            "bigger effect on neighboring\x01",
            "countries than we thought.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EF7")

    Jump("loc_1600")

    label("loc_EFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_F90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F17")
    Call(0, 7)
    Jump("loc_F8B")

    label("loc_F17")


    ChrTalk(
        0x8,
        (
            "Pressure from the\x01",
            "Republic seems to be\x01",
            "increasing day by day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "As expected, we can't\x01",
            "let our guard down...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F8B")

    Jump("loc_1600")

    label("loc_F90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1142")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1079")

    ChrTalk(
        0x8,
        (
            "Vice Commander Douglas headed\x01",
            "to Bellguard Gate for a meeting\x01",
            "about anti-terrorism measures.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You'd want to do whatever it takes\x01",
            "to have perfect security by the\x01",
            "start of the conference, after all.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_113D")

    label("loc_1079")


    ChrTalk(
        0x8,
        (
            "Vice Commander Douglas headed\x01",
            "to Bellguard Gate for a meeting\x01",
            "about anti-terrorism measures.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If Commander Sonya is there, I'm\x01",
            "sure they'll be able to plan out\x01",
            "a perfect security system.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_113D")

    Jump("loc_1600")

    label("loc_1142")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_144A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_139E")

    ChrTalk(
        0x8,
        (
            "Commander Sonya's and\x01",
            "Sergeant Noｱl's transfers\x01",
            "ended up overlapping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Due to this, the percentage\x01",
            "of female guardsmen at\x01",
            "Tangram Gate decreased...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FHmm. Although there's\x01",
            "nothing I can do about\x01",
            "it, it's a pity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ooh, how sad. There's\x01",
            "fewer people to gossip\x01",
            "with at night...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FUmm... Well, isn't it ok\x01",
            "to talk to the male\x01",
            "members?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHehe. You don't get it,\x01",
            "do you?\x02\x03",
            "#10309FGirl gossip can't be\x01",
            "done if a man is\x01",
            "present, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(I-I think there's some prejudice\x01",
            "mixed in there, but... It feels a\x01",
            "little bit scary, too.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1445")

    label("loc_139E")


    ChrTalk(
        0x8,
        (
            "Sergeant Noｱl... Please,\x01",
            "return to the CGF soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Until then, I'll save up\x01",
            "a lot of gossip!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F(I-It seems I'll have a\x01",
            "hard time when I get\x01",
            "back...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1445")

    Jump("loc_1600")

    label("loc_144A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1600")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1575")

    ChrTalk(
        0x8,
        (
            "It seems Vice Commander Douglas was\x01",
            "previously demoted and served at the\x01",
            "police academy for a long time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But the other day, due to Commander\x01",
            "Sonya's request, it his reinstatement\x01",
            "to the CGF was decided.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We're glad to have the\x01",
            "vice commander back as\x01",
            "well.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1600")

    label("loc_1575")


    ChrTalk(
        0x8,
        (
            "Vice Commander Douglas has\x01",
            "been an excellent CGF\x01",
            "member for a long time now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We're glad to have the\x01",
            "vice commander back as\x01",
            "well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1600")

    TalkEnd(0xFE)
    Return()

    # Function_6_602 end

    def Function_7_1604(): pass

    label("Function_7_1604")

    OP_4B(0x8, 0xFF)

    ChrTalk(
        0x8,
        "─That ends my report.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I understand. Sham\x01",
            "battles at Tangram Hill,\x01",
            "eh...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Though they're small in scale,\x01",
            "they're clearly designed to\x01",
            "put pressure on us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes. As expected, we\x01",
            "can't let our guard down\x01",
            "until the referendum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We can only watch out while\x01",
            "continuing to cooperate\x01",
            "with the other units.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Good work. Continue\x01",
            "surveillance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "Sir!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 2)
    OP_4C(0x8, 0xFF)
    Return()

    # Function_7_1604 end

    def Function_8_178B(): pass

    label("Function_8_178B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17B4")
    Call(0, 11)
    Return()

    label("loc_17B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17D9")
    Call(0, 20)
    Return()

    label("loc_17D9")

    Call(0, 9)
    Return()

    # Function_8_178B end

    def Function_9_17DD(): pass

    label("Function_9_17DD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1806")
    Call(0, 11)
    Return()

    label("loc_1806")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_182B")
    Call(0, 20)
    Return()

    label("loc_182B")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_265E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_21B5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19B4")

    ChrTalk(
        0x9,
        (
            "I've already contacted my unit\x01",
            "to have them remove the barrier\x01",
            "to the Ancient Battlefield.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Head towards the point\x01",
            "the monsters were sighted\x01",
            "from Armorica Old Road.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "As the CGF, not having\x01",
            "personnel to spare for monster\x01",
            "extermination is tough, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm sure that all of you\x01",
            "will be able to resolve\x01",
            "this matter for us.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A88")

    label("loc_19B4")


    ChrTalk(
        0x9,
        (
            "I've already contacted my unit\x01",
            "to have them remove the barrier\x01",
            "to the Ancient Battlefield.\x02\x03",
            "Head to the site from Armorica\x01",
            "Old Road.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm sure that all of you\x01",
            "will be able to resolve\x01",
            "this matter for us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A88")

    Jump("loc_21B1")

    label("loc_1A8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20F8")

    ChrTalk(
        0x9,
        (
            "Good work, Special\x01",
            "Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We still have a heap of\x01",
            "problems, but thanks to\x01",
            "you, we have one less.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Because of the damage we sustained\x01",
            "in the attack, we're short staffed.\x01",
            "You really have my appreciation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FNo, we're all equal in\x01",
            "these difficult times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F...The damage to the CGF\x01",
            "was really severe,\x01",
            "right?\x02\x03",
            "#00101FI wonder how long it\x01",
            "will take the CGF to\x01",
            "rebuild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Having to also deal with\x01",
            "this state of tension, I\x01",
            "honestly can't say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "However, if Sergeant Major Noｱl\x01",
            "returned to the CGF, it would\x01",
            "make you shorthanded as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In that case we'd love to have her\x01",
            "contribute to the reconstruction\x01",
            "from a proper post.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D5C")
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)

    label("loc_1D5C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D7F")
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)

    label("loc_1D7F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DA2")
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)

    label("loc_1DA2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DC2")
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_1DC2")

    Sleep(1000)

    ChrTalk(
        0x104,
        "#00305FThat's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10108F...A promotion, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...In a certain sense, the\x01",
            "damage the CGF suffered this\x01",
            "time was "morale" damage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The shock they experienced due to their comrades\x01",
            "being sacrificed caused many of them to be worn\x01",
            "down by the terror of CGF duty itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Some of the members seem to\x01",
            "be holding out relying on\x01",
            "anger or pride, however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F...Indeed. I feel those\x01",
            "emotions strongly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In order to get back the\x01",
            "lost morale, we need\x01",
            "excellent officers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The matter is not yet\x01",
            "settled, but... You have\x01",
            "plenty of that ability.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103F...I don't know if I'll\x01",
            "be as good as 2nd Lt.\x01",
            "Mireille, but...\x02\x03",
            "#10101FIf that's the case, then\x01",
            "please allow me to\x01",
            "fulfill my mission.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Thank you. Hard times will\x01",
            "probably continue for a while,\x01",
            "but I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x19D, 3)
    Jump("loc_21B1")

    label("loc_20F8")


    ChrTalk(
        0x9,
        (
            "In order to reconstruct the CGF as\x01",
            "well, I want to have the Sergeant\x01",
            "Major help us from a proper post.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hard times will probably\x01",
            "continue for a while,\x01",
            "but I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21B1")

    TalkEnd(0x9)
    Return()

    label("loc_21B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25A0")

    ChrTalk(
        0x9,
        (
            "The damage the CGF received\x01",
            "from that series of\x01",
            "incidents is immeasurable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "When Sergeant Noｱl returns to the CGF,\x01",
            "we'll have her contribute to rebuilding\x01",
            "our organization from a proper post.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FThen...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10108F...A promotion, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...In a certain sense, the\x01",
            "damage the CGF suffered this\x01",
            "time was "morale" damage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Many are being worn down by the terror\x01",
            "of CGF duty itself after being shocked\x01",
            "by the deaths of their comrades.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Some of the members seem to\x01",
            "be holding out relying on\x01",
            "anger or pride, however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F...Indeed. I feel those\x01",
            "emotions strongly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In order to get back the\x01",
            "lost morale, we need\x01",
            "excellent officers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The matter is not yet\x01",
            "settled, but... You have\x01",
            "plenty of that ability.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103F...I don't know if I'll\x01",
            "be as good as 2nd Lt.\x01",
            "Mireille, but...\x02\x03",
            "#10101FIf that's the case, then\x01",
            "please allow me to\x01",
            "fulfill my mission.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Thank you. Hard times will\x01",
            "probably continue for a while,\x01",
            "but I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18E, 3)
    Jump("loc_2659")

    label("loc_25A0")


    ChrTalk(
        0x9,
        (
            "In order to reconstruct the CGF as\x01",
            "well, I want to have the Sergeant\x01",
            "Major help us from a proper post.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hard times will probably\x01",
            "continue for a while,\x01",
            "but I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2659")

    Jump("loc_3CD3")

    label("loc_265E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2D2B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x170, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2991")

    ChrTalk(
        0x9,
        (
            "You guys, it seems that you were\x01",
            "of great help at the scene of\x01",
            "yesterday's derailment accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FHaha, the leader of our\x01",
            "Support Section played a\x01",
            "very active role in it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FWait... That's really\x01",
            "more praise than I\x01",
            "deserve.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100F*giggle*, that's not\x01",
            "true.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "At the police academy I\x01",
            "mainly taught you\x01",
            "crafts, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Lloyd, you've grown into a\x01",
            "fine detective, haven't you?\x01",
            "I'm deeply moved somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FY-You too, Vice\x01",
            "Commander...?\x02\x03",
            "#00003F...I really have a long way\x01",
            "to go. I can't hold a candle\x01",
            "to my big brother yet.\x02\x03",
            "#00000FI could only do it because\x01",
            "I've have allies to fill\x01",
            "that gap for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FLloyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hehe, that's fine. The way\x01",
            "you're going, I wonder how\x01",
            "much you'll grow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm very much looking\x01",
            "forward to seeing that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x170, 2)
    Jump("loc_2D26")

    label("loc_2991")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B8A")

    ChrTalk(
        0x9,
        (
            "Yes, now that you\x01",
            "mention it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Would you all like to\x01",
            "read this book?\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x2F6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x2F6, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x189, 0)

    ChrTalk(
        0x102,
        (
            "#00105FThis is a... light\x01",
            "novel?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FHow unexpected that big\x01",
            "bro Douglas reads stuff\x01",
            "like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Haha. Even I read\x01",
            "novels.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Commander Sonya recommended\x01",
            "it to me, but... As you know,\x01",
            "I've gotten busy recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, that's how it is,\x01",
            "so you should enjoy it\x01",
            "when you have time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FSure, and thanks.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D26")

    label("loc_2B8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C74")

    ChrTalk(
        0x9,
        (
            "Well then, leaving that\x01",
            "aside...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Not much time has passed since the\x01",
            "derailment accident. It's too\x01",
            "early to feel completely relieved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Maybe the CGF should\x01",
            "stay on the watch near\x01",
            "the tracks for a while.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2D26")

    label("loc_2C74")


    ChrTalk(
        0x9,
        (
            "Not much time has passed since the\x01",
            "derailment accident. It's too\x01",
            "early to feel completely relieved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Maybe the CGF should\x01",
            "stay on the watch near\x01",
            "the tracks for a while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D26")

    Jump("loc_3CD3")

    label("loc_2D2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3143")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x170, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3071")

    ChrTalk(
        0x9,
        (
            "That Pleroma Grass or\x01",
            "whatever your found in\x01",
            "your investigation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It's said to be the base\x01",
            "ingredient of that\x01",
            "Gnosis, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I thought it was a\x01",
            "dangerous drug, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FOh, right... Vice Commander, you\x01",
            "were at the police academy during\x01",
            "the cult incident yourself, right?\x02\x03",
            "#00003FThat's the first place the\x01",
            "manipulated CGF members\x01",
            "attacked...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10105FAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...When we were suddenly attacked\x01",
            "by the controlled CGF members,\x01",
            "honestly, we were bewildered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In the end, the academy staff\x01",
            "and I couldn't deal with them...\x01",
            "and Earnest escaped from prison.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "A raw ingredient that holds so\x01",
            "much power... And it is also the\x01",
            "cause of the cryptids' appearance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The current cryptid disturbance...\x01",
            "We can consider it the most\x01",
            "dangerous critical point of all.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x170, 1)
    Jump("loc_313E")

    label("loc_3071")


    ChrTalk(
        0x9,
        (
            "A raw ingredient that holds so\x01",
            "much power... And it is also the\x01",
            "cause of the cryptids' appearance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The current cryptid disturbance...\x01",
            "We can consider it the most\x01",
            "dangerous critical point of all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_313E")

    Jump("loc_3CD3")

    label("loc_3143")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_320C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_315E")
    Call(0, 7)
    Jump("loc_3207")

    label("loc_315E")


    ChrTalk(
        0x9,
        (
            "As you can see, I don't really\x01",
            "have time to take measures\x01",
            "against the Cryptids.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I know it'll be difficult for\x01",
            "you all, but I'm counting on\x01",
            "you to investigate.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3207")

    Jump("loc_3CD3")

    label("loc_320C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_321A")
    Jump("loc_3CD3")

    label("loc_321A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3A43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38F3")

    ChrTalk(
        0x109,
        (
            "#10100FVice Commander, good\x01",
            "morning!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Oh, it's you guys.\x01",
            "You've come at just the\x01",
            "right time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I was just thinking of taking\x01",
            "a break, so since you're here\x01",
            "I'll take it easy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300F*sigh*, knowin' you, you were goin'\x01",
            "to say something like that get me\x01",
            "to join your practice again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hmm, I'd really like to,\x01",
            "but I don't have that\x01",
            "much time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha... As expected, you\x01",
            "look busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "After all, the\x01",
            "conference is tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, I intend to make the security system\x01",
            "during the trade conference perfect, but\x01",
            "the situation is ever-changing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'll need to arrange another meeting\x01",
            "with Commander Sonya tomorrow morning,\x01",
            "who is currently guarding Michelam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FI understand... The state\x01",
            "guests are going to all\x01",
            "meet at Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FNo matter how prepared\x01",
            "you are, it's probably\x01",
            "never too much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FWell, if we leave things to\x01",
            "the CGF, we can probably rest\x01",
            "easy for the time bein'.\x02\x03",
            "#00304FAfter all, "Thunderclap\x01",
            "Douglas" is also a member...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3643")
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)

    label("loc_3643")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_366D")
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)

    label("loc_366D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3697")
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)

    label("loc_3697")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36BE")
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    label("loc_36BE")

    Sleep(1000)

    ChrTalk(
        0x109,
        "#10105FThunderclap... is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Haha, you've brought out\x01",
            "another nostalgic name.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "There was a time when people\x01",
            "called me that, before I got\x01",
            "thrown into the police academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "At any rate, thunderclap this,\x01",
            "demon that... They all call me\x01",
            "all the names they want.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHaha, I think both suit\x01",
            "you, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Don't make fun of me,\x01",
            "ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "*cough*, back to the issue at\x01",
            "hand... I intend to make trade\x01",
            "conference security perfect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Don't worry about it too\x01",
            "much and focus on your\x01",
            "own work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FAlright, we'll do just\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x159, 0)
    Jump("loc_3A3E")

    label("loc_38F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39C6")

    ChrTalk(
        0x9,
        (
            ""Thunderclap", huh...\x01",
            "Haha, what a nostalgic\x01",
            "alias.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Ahem, anyway... I intend\x01",
            "to make trade conference\x01",
            "security perfect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Don't worry about it too\x01",
            "much and focus on your\x01",
            "own work.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3A3E")

    label("loc_39C6")


    ChrTalk(
        0x9,
        (
            "I intend to make trade\x01",
            "conference security\x01",
            "perfect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Don't worry about it too\x01",
            "much and focus on your\x01",
            "own work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A3E")

    Jump("loc_3CD3")

    label("loc_3A43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3CD3")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3CD3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C39")

    ChrTalk(
        0x9,
        (
            "#4PThanks for taking part in my\x01",
            "training. I'll be counting on\x01",
            "you if something comes up again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#4PThen, about the matter just\x01",
            "now... Could you do your best\x01",
            "to keep it "between us"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FU-Understood. In any\x01",
            "case, we'll be careful\x01",
            "not to─\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F...Next time, we've got\x01",
            "to tell Tio too♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309FHehe, you're right. That\x01",
            "would be unfair.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011FH-Hey, you two! Don't go\x01",
            "back on your word right\x01",
            "away!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#4P...I'm counting on you.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3CD3")

    label("loc_3C39")


    ChrTalk(
        0x9,
        (
            "#4PThanks for taking part in my\x01",
            "training. I'll be counting on\x01",
            "you if something comes up again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#4P...Keep that matter\x01",
            ""between us" as well,\x01",
            "ok?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CD3")

    TalkEnd(0x9)
    Return()

    # Function_9_17DD end

    def Function_10_3CD7(): pass

    label("Function_10_3CD7")

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
        "#11P─You've finally come.\x02",
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
        "#6P#00002FAh...\x02",
    )

    CloseMessageWindow()
    OP_68(3420, 900, 80, 3000)
    MoveCamera(45, 19, 0, 3000)
    OP_6E(350, 3000)
    SetCameraDistance(25500, 3000)

    def lambda_3EDB():
        OP_98(0xFE, 0x9C4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3EDB)
    Sleep(100)

    def lambda_3EF8():
        OP_98(0xFE, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3EF8)
    Sleep(100)

    def lambda_3F15():
        OP_98(0xFE, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3F15)
    Sleep(100)

    def lambda_3F32():
        OP_98(0xFE, 0xAF0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3F32)
    Sleep(100)

    def lambda_3F4F():
        OP_98(0xFE, 0x9C4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3F4F)
    Sleep(1000)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x109,
        (
            "#10100FVice Commander Douglas!\x01",
            "Good morning sir!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PYo, Sergeant Major\x01",
            "Seeker.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PHow are things at that\x01",
            "Support Section or\x01",
            "whatever?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FSir! I'm learning many\x01",
            "things every day!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PHaha, glad to hear it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PYou should focus on that\x01",
            "from here on out, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00105FNoｱl, this man is...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11POh, I guess I didn't'\x01",
            "introduce myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI am Douglas. I've\x01",
            "assumed the office of\x01",
            "CGF Vice Commander.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI heard all about you guys\x01",
            "from the Commander. Pleased\x01",
            "to make your acquaintance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00100FNice to meet you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FHehe, I see he's quite\x01",
            "the character.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00300FYou look well, Mr.\x01",
            "Douglas.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PYou too Randy. Nice work\x01",
            "rehabilitating the\x01",
            "Bellguard Gate troops.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAnd Lloyd. It's been a\x01",
            "while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PBut it seems you played\x01",
            "a big role in that cult\x01",
            "incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FHaha... Long time no see.\x02\x03",
            "#00004FI was surprised when I heard\x01",
            "you'd been appointed Vice\x01",
            "Commander, instructor.\x02\x03",
            "#00012FPainful memories of being put\x01",
            "through the ringer by "Demon\x01",
            "Douglas" are coming back to me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PHey, don't bring up my\x01",
            "old nickname, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PHonestly, it's\x01",
            "embarrassing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100F(Hmm, he seems to have\x01",
            "been quite strict at the\x01",
            "police academy...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P...Well, let's leave it\x01",
            "at that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI called you here today\x01",
            "for a job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FA job... The "CGF\x01",
            "Training Participation\x01",
            "Request" request, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PYeah, exactly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThe objective of this training\x01",
            "is to beat the Special Support\x01",
            "Section into shape.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI'll have you take the\x01",
            "full brunt of my\x01",
            "iiintense training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00005FHuh...? It's not for the\x01",
            "CGF, but for us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIt'll be good experience\x01",
            "for us too, of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAlso, I've already informed\x01",
            "police leadership. This will\x01",
            "be an official joint training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00300FI see... Rather than a\x01",
            "support request, it seems\x01",
            "more like regular training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PHaha, well that's how it\x01",
            "is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWe're ready on our end.\x01",
            "The rest depends on\x01",
            "you...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(500)

    ChrTalk(
        0x102,
        (
            "#12P#00100FMaybe we should make\x01",
            "sure our equipment is in\x01",
            "order.\x02\x03",
            "#00104FWe might want to take\x01",
            "another look at our\x01",
            "quartz setup as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PHow 'bout it? Will you\x01",
            "begin the training\x01",
            "immediately?\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x6F, 0x1, 0x0)
    Call(0, 17)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_10_3CD7 end

    def Function_11_4829(): pass

    label("Function_11_4829")

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
            "#11PI'd like you to serve as\x01",
            "sparring partners for\x01",
            "training my troops.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWe're ready on our end.\x01",
            "Shall we begin right\x01",
            "away?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 17)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_11_4829 end

    def Function_12_4956(): pass

    label("Function_12_4956")


    def lambda_495B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_495B)

    def lambda_496C():
        OP_98(0xFE, 0x157C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_496C)
    WaitChrThread(0x101, 1)
    Return()

    # Function_12_4956 end

    def Function_13_4986(): pass

    label("Function_13_4986")


    def lambda_498B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_498B)

    def lambda_499C():
        OP_98(0xFE, 0xFA0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_499C)
    WaitChrThread(0x109, 1)
    OP_97(0x109, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
    OP_97(0x109, 0x3E8, 0x0, 0x0, 0x7D0, 0x0)
    Return()

    # Function_13_4986 end

    def Function_14_49DE(): pass

    label("Function_14_49DE")


    def lambda_49E3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_49E3)

    def lambda_49F4():
        OP_98(0xFE, 0xFA0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_49F4)
    WaitChrThread(0x102, 1)
    OP_97(0x102, 0x0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
    OP_97(0x102, 0x3E8, 0x0, 0x0, 0x7D0, 0x0)
    Return()

    # Function_14_49DE end

    def Function_15_4A36(): pass

    label("Function_15_4A36")


    def lambda_4A3B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4A3B)

    def lambda_4A4C():
        OP_98(0xFE, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4A4C)
    WaitChrThread(0x104, 1)
    OP_97(0x104, 0x3E8, 0x0, 0x2BC, 0x7D0, 0x0)
    OP_93(0x104, 0x5A, 0x1F4)
    Return()

    # Function_15_4A36 end

    def Function_16_4A81(): pass

    label("Function_16_4A81")


    def lambda_4A86():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_4A86)

    def lambda_4A97():
        OP_98(0xFE, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4A97)
    WaitChrThread(0x105, 1)
    OP_97(0x105, 0x3E8, 0x0, 0xFFFFFD44, 0x7D0, 0x0)
    OP_93(0x105, 0x5A, 0x1F4)
    Return()

    # Function_16_4A81 end

    def Function_17_4ACC(): pass

    label("Function_17_4ACC")

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
            "[Begin the Training]\x01",      # 0
            "[We're Not Ready]\x01",         # 1
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
        (0, "loc_4B43"),
        (1, "loc_4B4B"),
        (SWITCH_DEFAULT, "loc_4BE0"),
    )


    label("loc_4B43")

    Call(0, 18)
    Jump("loc_4BE0")

    label("loc_4B4B")


    ChrTalk(
        0x101,
        (
            "#6P#00000FSorry, but... Can you\x01",
            "give us a little more\x01",
            "time?\x02",
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
            "#11PThen, speak with me\x01",
            "again once you're ready.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x152, 0)
    Jump("loc_4BE0")

    label("loc_4BE0")

    Return()

    # Function_17_4ACC end

    def Function_18_4BE1(): pass

    label("Function_18_4BE1")


    ChrTalk(
        0x101,
        "#6P#00000FYes, we're ready too.\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0x5A, 0x1F4)
    Sleep(500)

    ChrTalk(
        0x9,
        "#11PGood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAnd Sergeant Seeker, don't question\x01",
            "the value of this training just\x01",
            "because the CGF is your opponent, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThere must be new things\x01",
            "even you can learn by facing\x01",
            "CGF opponents, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10100FSir, roger that!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThen, let's begin the\x01",
            "training immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PEveryone, move to the\x01",
            "outdoor parking lot.\x02",
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
            "Quest [CGF Training\x01",
            "Participation Request]\x07\x00\x01",
            "started!\x02",
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

    # Function_18_4BE1 end

    def Function_19_4DEF(): pass

    label("Function_19_4DEF")

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
            "#11P─I'll say it again. Good\x01",
            "work on today's\x01",
            "training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIt was a good experience\x01",
            "for the CGF members,\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FFor us, too. That was a\x01",
            "great experience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FStill, you haven't\x01",
            "weakened even a tiny\x01",
            "bit.\x02\x03",
            "#00300FIt reminds me of how\x01",
            "thoroughly beaten I was\x01",
            "in my first training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAnd it seems you've\x01",
            "grown quite a bit\x01",
            "yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAlso, It seems you've\x01",
            "completely mastered the\x01",
            "Stunhalberd I taught you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304FSure have. I've evolved\x01",
            "it into the super stylish\x01",
            "and elegant Randy school.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FThe Stunhalberd... So\x01",
            "that what it was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00109FHaha, it seems Randy\x01",
            "owes him a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWell, since this guy didn't want\x01",
            "to handle a rifle, I focused on\x01",
            "training him in that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThough it's just a halberd,\x01",
            "it can put a lot of power\x01",
            "into a straight line.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIt seems that was also\x01",
            "why I was hated by the\x01",
            "previous commander.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00300FHehe. Well, being bound\x01",
            "by rules isn't in my\x01",
            "nature, you know.\x02\x03",
            "#00309FLuckily, I transferred\x01",
            "to the Support Section\x01",
            "and I'm feelin' good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FHehe. For better or worse, I\x01",
            "guess everything is thanks\x01",
            "to the Vice Commander.\x02\x03",
            "#10302FLooks like your demotion to\x01",
            "the police academy was a\x01",
            "mistake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FIt's because the CGF was under the\x01",
            "command of the former commander up\x01",
            "until the cult incident.\x02\x03",
            "#10109FEven so, your subordinates trust\x01",
            "you so much, and your skills...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIt's not a big deal\x01",
            "but... It was probably\x01",
            "because I was an eyesore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAfter I went to the police academy,\x01",
            "I focused on training people who\x01",
            "could reform that rotten system.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThinking about it now,\x01",
            "maybe it was fortunate,\x01",
            "in a way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAfter all, I got to instruct\x01",
            "CGF and police beginners who\x01",
            "were still green.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00012FI really think you were\x01",
            "too strict back then,\x01",
            "though.\x02\x03",
            "#00006FPeople like Frantz even\x01",
            "cried sometimes, you\x01",
            "see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PNow now, don't say that.\x01",
            "It did you good, didn't\x01",
            "it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWell, things happened\x01",
            "and I've returned to the\x01",
            "CGF.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PFrom now on I'll cooperate\x01",
            "with all of you in the\x01",
            "protection of our state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100FHaha... We'll do our\x01",
            "best.\x02\x03",
            "#00104FAlthough, people like us\x01",
            "are still inexperienced\x01",
            "in some ways.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PCome on, no need to be\x01",
            "modest. You all have\x01",
            "that much strength.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIt's thanks to that that you're\x01",
            "doing a proper job at the Special\x01",
            "Support Section Sergei formed.\x02",
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
        "#6P#00005FChief Sergei?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00305FWhat, you know that old\x01",
            "man?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PHuh? Not only do I know\x01",
            "him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI owe both Sergei and\x01",
            "Sonya a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI even mediated their\x01",
            "marriage.\x02",
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
        "#6P#00011FM...!!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4S#6P#00105FMARRIAGE!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#4S#10111FCommander Sonya and\x01",
            "Chief Sergei!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10305FWow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FHey now, don't go\x01",
            "hitting us with the\x01",
            "naked truth so suddenly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P...W-What. You didn't\x01",
            "know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThey divorced five years\x01",
            "ago, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PA lot of things overlapped,\x01",
            "like Sergei's demotion and\x01",
            "Sonya's promotion...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FHehe, I see. Looks like it\x01",
            "was just some drama between\x01",
            "an adult man and woman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FHuuuh...? Commander\x01",
            "Sonya got...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00303FI thought those two were\x01",
            "acting suspicious,\x01",
            "but...\x02\x03",
            "#00309FWhat can I say? Mystery\x01",
            "solved, I guess♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00011FH-Hey everyone... Stop\x01",
            "making fun of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00109F(I-I'm a little curious\x01",
            "though...)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#11P...Damn, it got away\x01",
            "from me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PA-Anyway. Not a word of\x01",
            "this to anyone else, you\x01",
            "hear?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAhem, anyway... Good\x01",
            "work on today's\x01",
            "training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI'll be counting on you\x01",
            "if something comes up\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FY-Yes, sir. We look\x01",
            "forward to hearing from\x01",
            "you.\x02",
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
            "Quest [CGF Training\x01",
            "Participation Request]\x07\x00\x01",
            "completed!\x02",
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

    # Function_19_4DEF end

    def Function_20_5E6C(): pass

    label("Function_20_5E6C")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6568")

    ChrTalk(
        0x101,
        (
            "#6P#00000FVice Commander Douglas,\x01",
            "thank you for your hard\x01",
            "work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P...Hey, it's you guys.\x01",
            "Thank you too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PYou're here for my\x01",
            "request, aren't you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00300FWe are, but...\x02\x03",
            "#00303F...You seem on edge.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_621F")

    ChrTalk(
        0x9,
        (
            "#11PYou all must've felt it\x01",
            "too when you entered the\x01",
            "gate...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThe CGF is in a state of\x01",
            "high alert, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAnd to think a wanted criminal\x01",
            "forced his way through the\x01",
            "gate on top of that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAnd so, we can't let our\x01",
            "guard down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00100FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWell, looks like you\x01",
            "caught that wanted\x01",
            "criminal for us, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAllow me to thank you\x01",
            "for that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FWell, it was the natural\x01",
            "thing to do.\x02\x03",
            "#00001F...Is the present\x01",
            "request related to that?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_64DF")

    label("loc_621F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_63D4")

    ChrTalk(
        0x9,
        (
            "#11PYou all must've felt it\x01",
            "too when you entered the\x01",
            "gate...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThe CGF is in a state of\x01",
            "high alert, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAnd to think a scoundrel\x01",
            "forced his way through\x01",
            "the gate on top of that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAnd so, we can't let our\x01",
            "guard down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00100FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F(The medical supplies\x01",
            "thief we failed to\x01",
            "catch, huh...)\x02\x03",
            "#00001F...But, does that mean\x01",
            "that the present request\x01",
            "is related to that?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_64DF")

    label("loc_63D4")


    ChrTalk(
        0x9,
        (
            "#11PYou all must've felt it\x01",
            "too when you entered the\x01",
            "gate...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThe CGF is in a state of\x01",
            "high alert, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThe situation is such\x01",
            "that we can't let our\x01",
            "guard down even a little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001FI see... So the present\x01",
            "request is related to\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_64DF")


    ChrTalk(
        0x9,
        "#11PYeah, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI'd like to explain the\x01",
            "job immediately, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAre you going to accept\x01",
            "the request?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65BE")

    label("loc_6568")


    ChrTalk(
        0x9,
        "#11PAre you free?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI'd like you to accept\x01",
            "the request right away,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_65BE")

    Call(0, 21)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 2710, 0, -330, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_20_5E6C end

    def Function_21_65ED(): pass

    label("Function_21_65ED")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6650")
    Call(0, 22)
    Jump("loc_6728")

    label("loc_6650")


    ChrTalk(
        0x101,
        (
            "#6P#00006F...Sorry, our hands are\x01",
            "full right now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PHmm... Well, times being\x01",
            "what they are, I suppose\x01",
            "it can't be helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAlright, if by any\x01",
            "chance you do get free,\x01",
            "ask me again.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x19B, 3)

    label("loc_6728")

    Return()

    # Function_21_65ED end

    def Function_22_6729(): pass

    label("Function_22_6729")


    ChrTalk(
        0x101,
        "#6P#00000FYes, please go ahead.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PI'm in your debt.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P─I wrote it in my request as well, but we\x01",
            "recently received reports of the\x01",
            "appearance of mysterious "black monsters".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIt seems they damaged\x01",
            "crops and livestock near\x01",
            "Armorica Village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105FBlack monsters... I get the\x01",
            "impression I've heard about\x01",
            "them somewhere before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00303FThe fact that they\x01",
            "attack crops rings a\x01",
            "bell too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FCould they be... similar to the\x01",
            "ones in the "Wolf-Type\x01",
            "Monsters" case?\x02\x03",
            "#10103FMilitary dogs controlled by the\x01",
            "mafia were responsible for the\x01",
            "damage in that case, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI've been worried about\x01",
            "them ever since I read\x01",
            "the report on that case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PRevache is virtually dissolved,\x01",
            "but a large number of their\x01",
            "military dogs have gone missing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI can't say the chances\x01",
            "are particularly low.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FHow is the CGF's own\x01",
            "investigation going?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWe briefly surveyed the\x01",
            "damage and spoke with\x01",
            "the citizens nearby.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAs a result, we established that\x01",
            "these "black monsters" come from\x01",
            "the Ancient Battlefield area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAnd so, I want you to\x01",
            "head to the Ancient\x01",
            "Battlefield.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PInvestigate these\x01",
            "monsters, and if possible,\x01",
            "exterminate them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FWe understand the\x01",
            "general situation.\x02\x03",
            "#10303FStill, you seem quite\x01",
            "busy, eh?\x02\x03",
            "#10300FI think this type of job\x01",
            "is something the CGF\x01",
            "usually handles...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI'd like to take care of it,\x01",
            "but... Like I just told you,\x01",
            "the CGF is on high alert.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PRed Constellation, the perpetrators of\x01",
            "the attack on Crossbell City, have\x01",
            "vanished, and we don't have any leads.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PFurthermore, we're in a situation\x01",
            "where the Empire and Republic have\x01",
            "begun massive training excercises...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_6E6E")

    ChrTalk(
        0x9,
        (
            "#11PAs the CGF responsible for ensuring\x01",
            "something like that doesn't happen again, we\x01",
            "need to make the border especially secure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6EB1")

    label("loc_6E6E")


    ChrTalk(
        0x9,
        (
            "#11PAs the CGF, we need to\x01",
            "make the border\x01",
            "especially secure.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6EB1")


    ChrTalk(
        0x102,
        (
            "#6P#00108FRight before the Non-Aggression Pact\x01",
            "was signed... The current situation is\x01",
            "becoming similar to how it was then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11P...Yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PEven if it is monster damage, as\x01",
            "you might expect, it's a low\x01",
            "priority in a situation like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThe damage we surveyed\x01",
            "wasn't all that severe,\x01",
            "and no one was injured.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304FIndeed. This is no time for\x01",
            "the CGF to be dealing with\x01",
            "monster extermination.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F...We understand the\x01",
            "general situation.\x02\x03",
            "#00000FThen, please leave the\x01",
            ""black monsters"\x01",
            "investigation to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PYes, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI'm counting on you,\x01",
            "Special Support Section.\x02",
        )
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
            "Quest [Ancient\x01",
            "Battlefield\x01",
            "Investigation]\x07\x00",
            " started!\x02",
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

    # Function_22_6729 end

    def Function_23_71D2(): pass

    label("Function_23_71D2")

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
            "#6P#00000F─And so, those are the\x01",
            "details of this request.\x02\x03",
            "#00003FI don't think those\x01",
            "military dogs will cause\x01",
            "any more damage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11P...I see...\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x9)

    ChrTalk(
        0x101,
        "#6P#00012FU-Umm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00305FWhat? You're totally\x01",
            "silent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FPerhaps not exterminating\x01",
            "those dogs doesn't sit\x01",
            "well with you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P...No, that was well\x01",
            "done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI'm just a little surprised\x01",
            "that your results exceeded\x01",
            "my expectations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FWell, I guess.\x02\x03",
            "#10309FIf someone said they "persuaded\x01",
            "the military dogs", normally\x01",
            "you'd think they made it up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106FIt really might be too\x01",
            "hard to believe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FHowever, because it's\x01",
            "the truth, I think\x01",
            "there's no problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11P...No, it's fine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIf you found a peaceful\x01",
            "solution, then nothing\x01",
            "could be better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThanks for your help\x01",
            "everyone. Thanks to you,\x01",
            "we've one fewer problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00004FI'm glad to hear it.\x02\x03",
            "#00000FPlease let us know if\x01",
            "you ever need our help\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PYeah, I'll do that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P─Then, we continue to be\x01",
            "on high alert.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PYou guys should be\x01",
            "careful too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000F...Sir!\x02",
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
            "Quest [Ancient\x01",
            "Battlefield\x01",
            "Investigation]\x07\x00",
            " completed!\x02",
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

    # Function_23_71D2 end

    SaveToFile()

Try(main)
