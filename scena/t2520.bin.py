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
        "Function_6_608",          # 06, 6
        "Function_7_1698",         # 07, 7
        "Function_8_1820",         # 08, 8
        "Function_9_1872",         # 09, 9
        "Function_10_3E14",        # 0A, 10
        "Function_11_49FD",        # 0B, 11
        "Function_12_4B48",        # 0C, 12
        "Function_13_4B78",        # 0D, 13
        "Function_14_4BD0",        # 0E, 14
        "Function_15_4C28",        # 0F, 15
        "Function_16_4C73",        # 10, 16
        "Function_17_4CBE",        # 11, 17
        "Function_18_4DEE",        # 12, 18
        "Function_19_4FDB",        # 13, 19
        "Function_20_61AE",        # 14, 20
        "Function_21_69EB",        # 15, 21
        "Function_22_6B1B",        # 16, 22
        "Function_23_764C",        # 17, 23
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
            "The "Delicious Hot Pot Dishes -\x01",
            "Earthenware Pot Edition" is here.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_604")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_604")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "You learned the "Rich Sea Hot Pot"\x07\x00",
            " recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_604")

    TalkEnd(0xFF)
    Return()

    # Function_5_532 end

    def Function_6_608(): pass

    label("Function_6_608")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D7")

    NpcTalk(
        0x8,
        "Soldier Flammie",
        (
            "At present, it seems that Vice Commander\x01",
            "Douglas is studying the future course of\x01",
            "action in Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Flammie",
        (
            "That azure pale tree, a possible to occur\x01",
            "invasion from the Empire and Republic...\x01",
            "There's still a heap of problems.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Flammie",
        (
            "As the State Guard, I don't know\x01",
            "how much we'll be able to do, but...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Flammie",
        (
            "Somehow I want to do my best\x01",
            "without abandoning hope.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_8DE")

    label("loc_7D7")


    NpcTalk(
        0x8,
        "Soldier Flammie",
        (
            "At present, it seems that Vice Commander\x01",
            "Douglas is studying the future course of\x01",
            "action in Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Soldier Flammie",
        (
            "As the State Guard, I don't know\x01",
            "how much we'll be able to do, but...\x01",
            "In a way or another, I want to do my best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8DE")

    Jump("loc_1694")

    label("loc_8E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A97")

    ChrTalk(
        0x8,
        (
            "Master Sergeant Noｱl...\x01",
            "I'm really glad for you that\x01",
            "your younger sister is safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108FYes...although considering the CGF damage,\x01",
            "I can't honestly rejoice about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...Yes, frankly speaking,\x01",
            "it's unbearable for us too, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Right because the situation is like this,\x01",
            "the fact that Miss Noｱl's younger sister\x01",
            "is safe is a very happy thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103F...Thank you.\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B2F")

    label("loc_A97")


    ChrTalk(
        0x8,
        (
            "Right because the situation is like this,\x01",
            "we have to endure.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To burn and sacrifice our lives\x01",
            "to protect Crossbell...\x01",
            "That's the CGF mission.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B2F")

    Jump("loc_1694")

    label("loc_B34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_CF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C46")

    ChrTalk(
        0x8,
        "Yesterday train derailment accident...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Thinking about the timing it happened,\x01",
            "the local referendum getting closer,\x01",
            "as suspected the two major powers...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...I know we can't clearly\x01",
            "say it, but one ends up\x01",
            "being suspicious, after all.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CF2")

    label("loc_C46")


    ChrTalk(
        0x8,
        (
            "Yesterday train derailment accident...\x01",
            "As suspected, one of the two major powers...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "With the pressure rising day by day,\x01",
            "one ends up being suspicious, after all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CF2")

    Jump("loc_1694")

    label("loc_CF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_F7A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E7F")

    ChrTalk(
        0x8,
        (
            "As for the local referendum results,\x01",
            "it's said it's still uncertain if the\x01",
            "independence will take off for real...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Thinking about this situation with additional\x01",
            "pressures from the Empire and Republic,\x01",
            "those influences are perceived as a threat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The local referendum seems to be\x01",
            "having a bigger effect on the neighboring\x01",
            "countries than we're thinking.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F75")

    label("loc_E7F")


    ChrTalk(
        0x8,
        (
            "Thinking about this situation with additional\x01",
            "pressures from the Empire and Republic,\x01",
            "those influences are perceived as a threat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The local referendum seems to be\x01",
            "having a bigger effect on the neighboring\x01",
            "countries than we're thinking.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F75")

    Jump("loc_1694")

    label("loc_F7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1015")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F95")
    Call(0, 7)
    Jump("loc_1010")

    label("loc_F95")


    ChrTalk(
        0x8,
        (
            "It seems that the Republic is increasing\x01",
            "their pressures day by day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "As expected, we can't let our guard down...\x02",
    )

    CloseMessageWindow()

    label("loc_1010")

    Jump("loc_1694")

    label("loc_1015")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_11B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10FA")

    ChrTalk(
        0x8,
        (
            "Vice Commander Douglas headed to\x01",
            "Bellguard Gate for an anti-terrorists\x01",
            "measures meeting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "You'd want to have a perfect security\x01",
            "system no matter what by the start\x01",
            "of the conference, after all.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11B2")

    label("loc_10FA")


    ChrTalk(
        0x8,
        (
            "Vice Commander Douglas headed to\x01",
            "Bellguard Gate for an anti-terrorists\x01",
            "measures meeting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "With Commander Sonya, I'm\x01",
            "sure they'll be able to prepare\x01",
            "a perfect security system.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11B2")

    Jump("loc_1694")

    label("loc_11B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_14BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1414")

    ChrTalk(
        0x8,
        (
            "Commander Sonya's shuffle\x01",
            "and Sergeant Noｱl's transfer\x01",
            "ended up overlapping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Due to this, the female percentage\x01",
            "of Tangram Gate decreased...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FUhhm, although there's nothing\x01",
            "to do about it, it's a pity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Uuh, how said, the people to\x01",
            "gossip with at night decreased...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FEhhm...\x01",
            "Well, isn't it ok to talk to\x01",
            "the male members?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHu hu, you don't get it, eh?\x02\x03",
            "#10309FWomen gossips can't\x01",
            "almost be done if a man\x01",
            "is in the same place, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(I-I think there's some prejudice in there, but...\x01",
            "I subtly feel something scary.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_14BA")

    label("loc_1414")


    ChrTalk(
        0x8,
        (
            "Sergeant Noｱl... Please,\x01",
            "return to the CGF quick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Until then, I'll save up\x01",
            "a lot of gossips!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106F(I-It seems I'll have it hard when I come back...)\x02",
    )

    CloseMessageWindow()

    label("loc_14BA")

    Jump("loc_1694")

    label("loc_14BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1694")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1603")

    ChrTalk(
        0x8,
        (
            "It seems that Vice Commander Douglas\x01",
            "was demoted previously and he has been in\x01",
            "service for a long time at the Police Academy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But the other day, due to Commander\x01",
            "Sonya's request, it was decided his\x01",
            "reinstatement in the CGF.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We too are very glad about\x01",
            "the Vice Commander comeback.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1694")

    label("loc_1603")


    ChrTalk(
        0x8,
        (
            "Vice Commander Douglas is known\x01",
            "as a very excellent CGF member\x01",
            "since the past.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We too are very glad about\x01",
            "the Vice Commander comeback.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1694")

    TalkEnd(0xFE)
    Return()

    # Function_6_608 end

    def Function_7_1698(): pass

    label("Function_7_1698")

    OP_4B(0x8, 0xFF)

    ChrTalk(
        0x8,
        "──This ends my report.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I understand, sham battles\x01",
            "at Tangram Hill, eh...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Although they're on a small scale,\x01",
            "it's clearly a method to\x01",
            "put pressure on us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Yes, as expected, we can't let our\x01",
            "guard down until the local referendum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We can only watch out while we\x01",
            "keep cooperating with all quarters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Good job, continue to surveille.\x02",
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

    # Function_7_1698 end

    def Function_8_1820(): pass

    label("Function_8_1820")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1849")
    Call(0, 11)
    Return()

    label("loc_1849")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_186E")
    Call(0, 20)
    Return()

    label("loc_186E")

    Call(0, 9)
    Return()

    # Function_8_1820 end

    def Function_9_1872(): pass

    label("Function_9_1872")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_189B")
    Call(0, 11)
    Return()

    label("loc_189B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18C0")
    Call(0, 20)
    Return()

    label("loc_18C0")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2766")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_2276")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ADE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A2A")

    ChrTalk(
        0x9,
        (
            "I already called to open the\x01",
            "Ancient Battlefield sealed area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Head towards the monster outbreak point\x01",
            "from the Armorica Old Road area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "As CGF, not having personnel to spare for\x01",
            "monster extermination is a sorry feeling, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If it's you guys, I believe that\x01",
            "you'll resolve this matter.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1AD9")

    label("loc_1A2A")


    ChrTalk(
        0x9,
        (
            "I already called to open the\x01",
            "Ancient Battlefield sealed area.\x02\x03",
            "Head to the site from the Old Road area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If it's you guys, I believe that\x01",
            "you'll resolve this matter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AD9")

    Jump("loc_2272")

    label("loc_1ADE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21BF")

    ChrTalk(
        0x9,
        "Thank you for your hard work, Support Section.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We still have a heap of problems,\x01",
            "but thanks to you, one pending\x01",
            "problem has been solved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Because of the damage we sustained due\x01",
            "to the raid incident, we're short on staff.\x01",
            "You really have my appreciation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FNo, we're all equal in times of trouble.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F...The CGF damage was\x01",
            "really severe, right?\x02\x03",
            "#00101FI wonder how much time will it take\x01",
            "for the expected future reconstruction.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Having also to deal with this state of tension,\x01",
            "I honestly can't say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "However, if Master Sergeant Noｱl returned to the CGF,\x01",
            "it would made you become shorthanded too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In that case we'll absolutely have\x01",
            "her contribute to the organization\x01",
            "rebuilding from a proper post.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DF5")
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)

    label("loc_1DF5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E18")
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)

    label("loc_1E18")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E3B")
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)

    label("loc_1E3B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E5B")
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_1E5B")

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
            "...In a certain sense, this time, the\x01",
            "greatest damage the CGF received\x01",
            "was "morale" damage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The experienced shock due to their comrades\x01",
            "being victims gave rise to many of them being\x01",
            "gnawed at by the terror of the CGF duty itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "A part of the members seem to be\x01",
            "somehow enduring that relying on\x01",
            "anger or pride, however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F...Right.\x01",
            "They're keenly conveying\x01",
            "those kind of feelings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In order to get back the lost morale,\x01",
            "we need excellent officers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The matter is not certain yet, but...\x01",
            "You have plenty of that ability.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103F...I don't know if I'll be able to\x01",
            "do like 2nd Lt. Mireille, but...\x02\x03",
            "#10101FIf that's the case, then humbly\x01",
            "allow me to fulfill my mission.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Thank you.\x01",
            "Hard times will probably continue\x01",
            "for a while, but I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x19D, 3)
    Jump("loc_2272")

    label("loc_21BF")


    ChrTalk(
        0x9,
        (
            "In order to reconstruct the CGF too,\x01",
            "I want to have the Master Sergeant\x01",
            "help from a proper post.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hard times will probably continue\x01",
            "for a while, but I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2272")

    TalkEnd(0x9)
    Return()

    label("loc_2276")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26AE")

    ChrTalk(
        0x9,
        (
            "The damage the CGF received from that\x01",
            "series of incidents is immeasurable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In the event that Sergeant Noｱl returns\x01",
            "to the CGF, we'll have her contribute to the\x01",
            "organization rebuilding from a proper post.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FYou mean...\x02",
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
            "...In a certain sense, this time, the\x01",
            "greatest damage the CGF received\x01",
            "was "morale" damage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "There're quite many who are undermined by\x01",
            "the terror of the CGF duty itself after they\x01",
            "were shocked by their comrades' deaths.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "A part of the members seem to be\x01",
            "somehow enduring that relying on\x01",
            "anger or pride, however...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203F...Right.\x01",
            "They're keenly conveying\x01",
            "those kind of feelings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "In order to get back the lost morale,\x01",
            "we need excellent officers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The matter is not certain yet, but...\x01",
            "You have plenty of that ability.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10103F...I don't know if I'll be able to\x01",
            "do like 2nd Lt. Mireille, but...\x02\x03",
            "#10101FIf that's the case, then humbly\x01",
            "allow me to fulfill my mission.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "...Thank you.\x01",
            "Hard times will probably continue\x01",
            "for a while, but I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18E, 3)
    Jump("loc_2761")

    label("loc_26AE")


    ChrTalk(
        0x9,
        (
            "In order to reconstruct the CGF too,\x01",
            "I want to have the Master Sergeant\x01",
            "help from a proper post.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hard times will probably continue\x01",
            "for a while, but I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2761")

    Jump("loc_3E10")

    label("loc_2766")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2E23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x170, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A93")

    ChrTalk(
        0x9,
        (
            "You guys, it seems that you\x01",
            "were of great help on the scene\x01",
            "of yesterday's derailment accident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FHa ha, the leader of our Support Section\x01",
            "played a very active part in it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FWait...\x01",
            "You're really praising me too much there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00100F*giggle*, that's not true.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "At the time of Police Academy I\x01",
            "mainly taught you Crafts, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Lloyd, you've grown into\x01",
            "a fine detective, eh?\x01",
            "Somehow, I'm deeply moved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FY-You too, Vice Commander...\x02\x03",
            "#00003F...I really have a long way to go.\x01",
            "I can't even hold a candle to my big brother.\x02\x03",
            "#00000FI can only do it because I've got\x01",
            "comrades who fill that gap for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200FMr. Lloyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hu hu, that's fine.\x01",
            "That way, you'll be able\x01",
            "to grow thoroughly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I'm looking forward to the future, Lloyd.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x170, 2)
    Jump("loc_2E1E")

    label("loc_2A93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C78")

    ChrTalk(
        0x9,
        "Ah, by the way...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Would you like to\x01",
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
        "#00105FThis is a...light novel?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309FHow unexpected that big bro Douglas\x01",
            "reads stuff like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Ha ha, even I read novels.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "That was recommended to me\x01",
            "by Commander Sonya, but...\x01",
            "As you know, recently I'm busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, that's the story so you should\x01",
            "enjoy it when you have time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, thank you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E1E")

    label("loc_2C78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D67")

    ChrTalk(
        0x9,
        "Well then, leaving that aside...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It's passed too less time after the derailment\x01",
            "accident. It's early to feel completely relieved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Maybe the CGF should stay\x01",
            "on the watch out nearby the\x01",
            "railroad for a while.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2E1E")

    label("loc_2D67")


    ChrTalk(
        0x9,
        (
            "It's passed too less time after the derailment\x01",
            "accident. It's early to feel completely relieved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Maybe the CGF should stay\x01",
            "on the watch out nearby the\x01",
            "railroad for a while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E1E")

    Jump("loc_3E10")

    label("loc_2E23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_325C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x170, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3185")

    ChrTalk(
        0x9,
        (
            "That "Pleroma Grass" or how it's called\x01",
            "that we found out in your investigation...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It's said to be the base ingredient\x01",
            "of that "Gnosis", huh?\x02",
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
            "#00005FOh, right...\x01",
            "Vice Commander, you were at the Police Academy \x01",
            "at the time of the Cult incident too, right?\x02\x03",
            "#00003FAt that site the controlled\x01",
            "CGF attacked first...\x02",
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
            "In the end, the Police Academy staff\x01",
            "and I couldn't deal with them...and\x01",
            "Ernest slipped out from prison.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00108FIs that so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "A raw ingredient that holds so much power...\x01",
            "And it was also the cause of the Cryptids appearance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The current Cryptids disturbance...\x01",
            "It could be considered the most\x01",
            "dangerous critical point of all.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x170, 1)
    Jump("loc_3257")

    label("loc_3185")


    ChrTalk(
        0x9,
        (
            "A raw ingredient that holds so much power...\x01",
            "And it was also the cause of the Cryptids appearance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "The current Cryptids disturbance...\x01",
            "It could be considered the most\x01",
            "dangerous critical point of all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3257")

    Jump("loc_3E10")

    label("loc_325C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3324")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3277")
    Call(0, 7)
    Jump("loc_331F")

    label("loc_3277")


    ChrTalk(
        0x9,
        (
            "As you can see, I don't really have time\x01",
            "to take measures against the "Cryptids".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm putting you to a lot of trouble but\x01",
            "I'm counting on your investigation.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_331F")

    Jump("loc_3E10")

    label("loc_3324")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3332")
    Jump("loc_3E10")

    label("loc_3332")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3B99")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A3A")

    ChrTalk(
        0x109,
        "#10100FVice Commander, thank you for your hard work!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Oh, it's you guys.\x01",
            "You've come just at the right time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I was just thinking to take a break,\x01",
            "so since you're here let's take it\x01",
            "at leisure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300F*sigh*, knowin' you, you were\x01",
            "goin' to say again something like\x01",
            "to keep you company with practice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hmm, I'd really like to do that,\x01",
            "but I don't have that much time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa ha...\x01",
            "As expected, you look to be busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "After all, the conference\x01",
            "is tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, I intend to make the security system \x01",
            "during the Trade Conference perfect, \x01",
            "but the situation is always changing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'll need to arrange a meeting again\x01",
            "tomorrow morning with Commander\x01",
            "Sonya who is guarding Michelam.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103FI understand...\x01",
            "The state guests are going to\x01",
            "meet all at Orchis Tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10300FNo matter how much you're prepared,\x01",
            "it probably is never too much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FWell, if things are entrusted to the CGF,\x01",
            "we can probably feel relieved for the time bein'.\x02\x03",
            "#00304FAfter all, in the current CGF there's\x01",
            "also "Thunderclap Douglas"...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3795")
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)

    label("loc_3795")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37BF")
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)

    label("loc_37BF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37E9")
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)

    label("loc_37E9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3810")
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    label("loc_3810")

    Sleep(1000)

    ChrTalk(
        0x109,
        "#10105FThunderclap...is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Ha ha, you've brought out\x01",
            "another nostalgic name.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "There was a time when some called\x01",
            "me like that, before I got thrown\x01",
            "to the Police Academy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "At any rate, thunderclap this, ogre that...\x01",
            "They all call me with the names they want.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FHa ha, I think that\x01",
            "both suit you, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Don't make fun of me, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "*cough*, back to the topic...\x01",
            "I intend to make the Trade\x01",
            "Conference security perfect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You don't bother too much about it\x01",
            "and do your own work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes, we'll do.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x159, 0)
    Jump("loc_3B94")

    label("loc_3A3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B14")

    ChrTalk(
        0x9,
        (
            ""Thunderclap", eh...?\x01",
            "Ha ha, what a nostalgic alias.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "*cough*, anyway...\x01",
            "I intend to make the Trade\x01",
            "Conference security perfect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You don't bother too much about it\x01",
            "and do your own work.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3B94")

    label("loc_3B14")


    ChrTalk(
        0x9,
        (
            "I intend to make the Trade\x01",
            "Conference security perfect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "You shouldn't bother too much \x01",
            "about it and do your own work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B94")

    Jump("loc_3E10")

    label("loc_3B99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3E10")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3E10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D7F")

    ChrTalk(
        0x9,
        (
            "#4PThank you for taking part into practice.\x01",
            "I'll count on you if something comes up again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#4PThen, about the matter just now...\x01",
            "Could you do your best to\x01",
            "keep it "among us"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FU-Understood.\x01",
            "In any case, we'll be\x01",
            "careful to not──\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F...Next time, we\x01",
            "must tell Tio too♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10309FHu hu, you're right.\x01",
            "It would be unfair.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011FH-Hey, you two!\x01",
            "Don't eat your words right away!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#4P...I'm counting on you.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3E10")

    label("loc_3D7F")


    ChrTalk(
        0x9,
        (
            "#4PThank you for taking part into practice.\x01",
            "I'll count on you if something comes up again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#4P...Keep that matter\x01",
            "too "among us", eh?\x01\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E10")

    TalkEnd(0x9)
    Return()

    # Function_9_1872 end

    def Function_10_3E14(): pass

    label("Function_10_3E14")

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
        "#11P──You've finally come.\x02",
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

    def lambda_401A():
        OP_98(0xFE, 0x9C4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_401A)
    Sleep(100)

    def lambda_4037():
        OP_98(0xFE, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4037)
    Sleep(100)

    def lambda_4054():
        OP_98(0xFE, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4054)
    Sleep(100)

    def lambda_4071():
        OP_98(0xFE, 0xAF0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4071)
    Sleep(100)

    def lambda_408E():
        OP_98(0xFE, 0x9C4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_408E)
    Sleep(1000)
    OP_6F(0x79)
    OP_0D()

    ChrTalk(
        0x109,
        (
            "#10100FVice Commander Douglas...\x01",
            "Thank you for your hard work!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PHi, Master Sergeant Noｱl.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PHow are you feeling at the\x01",
            "Special Support Section?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FSir!\x01",
            "I'm learning many\x01",
            "things every day!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PHa ha, I'm glad to hear that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PYou should steadily focus on\x01",
            "that for the future too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#12P#00105FMiss Noｱl, this person is...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P...Oh, we haven't been\x01",
            "introduced yet, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PMy name is Douglas.\x01",
            "I'm the person who was recently\x01",
            "appointed as CGF Vice Commander.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI've heard in detail about all of\x01",
            "you from the Commander.\x01",
            "Pleased to make your acquaintance.\x02",
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
        "#6P#10302FHu hu, he looks the part.\x01\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00300FYou seem in good health as\x01",
            "always, big bro Douglas.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PYou too, Randy.\x01",
            "Thank you for the rehabilitation\x01",
            "training at Bellguard Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAnd── Lloyd.\x01",
            "We haven't met for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PYou seem to have done a great\x01",
            "part in that Cult incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FHa ha...\x01",
            "Long time no see.\x02\x03",
            "#00004FWhen I heard my instructor\x01",
            "became the Vice Commander,\x01",
            "I was really surprised.\x02\x03",
            "#00012FThe memories of getting strongly\x01",
            "squeezed by that "Douglas the Ogre"\x01",
            "came vividly back to me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PHey hey, don't bring out\x01",
            "my old nickname, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PHonestly, it's embarrassing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100F(Uhhm, he seems to have been a very \x01",
            "strict person at the Police Academy...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P...Well, let's leave\x01",
            "it at that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI've made you come here today\x01",
            "on purpose for a job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FA job...\x01",
            "The "Training Participation" request?\x02",
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
            "#11PThe purpose of this training is to beat\x01",
            "the Special Support Section into shape.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI'll have you properly take\x01",
            "my iiintense training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00005FHuh...\x01",
            "It's not for the CGF,\x01",
            "but for us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWell, of course it'll be a good\x01",
            "experience for the CGF members too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PFurthermore, I already explained it\x01",
            "to the police higher ups.\x01",
            "On paper, it's an official joint training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00300FI see...\x01",
            "More than a Support Request it\x01",
            "seems a sort of regular training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PHa ha, well, that's how it is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11POur preparations are already done.\x01",
            "The rest depends on you...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(500)

    ChrTalk(
        0x102,
        (
            "#12P#00100FIt could be good to\x01",
            "prepare for now.\x02\x03",
            "#00104FMaybe it wouldn't be a bad idea\x01",
            "to reorganize our Quartz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWhat do you want to do, can\x01",
            "we begin the training immediately?\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x6F, 0x1, 0x0)
    Call(0, 17)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_10_3E14 end

    def Function_11_49FD(): pass

    label("Function_11_49FD")

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
            "#11PI absolutely want you as\x01",
            "sparring partners for the\x01",
            "CGF members' training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11POur preparations are already done.\x01",
            "Can we begin the training immediately?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 17)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_11_49FD end

    def Function_12_4B48(): pass

    label("Function_12_4B48")


    def lambda_4B4D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4B4D)

    def lambda_4B5E():
        OP_98(0xFE, 0x157C, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4B5E)
    WaitChrThread(0x101, 1)
    Return()

    # Function_12_4B48 end

    def Function_13_4B78(): pass

    label("Function_13_4B78")


    def lambda_4B7D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4B7D)

    def lambda_4B8E():
        OP_98(0xFE, 0xFA0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4B8E)
    WaitChrThread(0x109, 1)
    OP_97(0x109, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
    OP_97(0x109, 0x3E8, 0x0, 0x0, 0x7D0, 0x0)
    Return()

    # Function_13_4B78 end

    def Function_14_4BD0(): pass

    label("Function_14_4BD0")


    def lambda_4BD5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4BD5)

    def lambda_4BE6():
        OP_98(0xFE, 0xFA0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4BE6)
    WaitChrThread(0x102, 1)
    OP_97(0x102, 0x0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
    OP_97(0x102, 0x3E8, 0x0, 0x0, 0x7D0, 0x0)
    Return()

    # Function_14_4BD0 end

    def Function_15_4C28(): pass

    label("Function_15_4C28")


    def lambda_4C2D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4C2D)

    def lambda_4C3E():
        OP_98(0xFE, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4C3E)
    WaitChrThread(0x104, 1)
    OP_97(0x104, 0x3E8, 0x0, 0x2BC, 0x7D0, 0x0)
    OP_93(0x104, 0x5A, 0x1F4)
    Return()

    # Function_15_4C28 end

    def Function_16_4C73(): pass

    label("Function_16_4C73")


    def lambda_4C78():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_4C78)

    def lambda_4C89():
        OP_98(0xFE, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4C89)
    WaitChrThread(0x105, 1)
    OP_97(0x105, 0x3E8, 0x0, 0xFFFFFD44, 0x7D0, 0x0)
    OP_93(0x105, 0x5A, 0x1F4)
    Return()

    # Function_16_4C73 end

    def Function_17_4CBE(): pass

    label("Function_17_4CBE")

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
            "[Begin the Training]\x01",           # 0
            "[We Are Not Prepared Yet]\x01",      # 1
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
        (0, "loc_4D3D"),
        (1, "loc_4D45"),
        (SWITCH_DEFAULT, "loc_4DED"),
    )


    label("loc_4D3D")

    Call(0, 18)
    Jump("loc_4DED")

    label("loc_4D45")


    ChrTalk(
        0x101,
        (
            "#6P#00000FI'm sorry, but...\x01",
            "Can you give us a little time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PHm, is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThen talk with me once more\x01",
            "when your preparations are done.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x152, 0)
    Jump("loc_4DED")

    label("loc_4DED")

    Return()

    # Function_17_4CBE end

    def Function_18_4DEE(): pass

    label("Function_18_4DEE")


    ChrTalk(
        0x101,
        (
            "#6P#00000FYes, we're\x01",
            "ready too.\x02",
        )
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
            "#11PMaster Sergeant Seeker, don't\x01",
            "be perplexed just because the\x01",
            "CGF is your opponent, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PBy facing the CGF members, there\x01",
            "should be new things you could learn.\x02",
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
            "#11PThen, let's commence\x01",
            "training immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PEveryone, move to the\x01",
            "parking lot outdoors.\x02",
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
            "Quest [CGF Training Participation]\x07\x00",
            " started!\x02",
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

    # Function_18_4DEE end

    def Function_19_4FDB(): pass

    label("Function_19_4FDB")

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
            "#11P──I want to thank you for taking\x01",
            "part in the training once again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIt should have been a good\x01",
            "experience for the members too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FNo, it's us who must thank you.\x01",
            "It was a very good experience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FStill, you haven't weakened\x01",
            "even a tiny bit.\x02\x03",
            "#00300FI've remembered when I was beaten\x01",
            "durin' my first practice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAnd you my dear, seem to\x01",
            "have grown quite a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIt also seems that you even have completely \x01",
            "mastered the Stunhalberd that I taught you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304FSure I have. Now I evolved it\x01",
            "into the super stylish &\x01",
            "elegant Randy School.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FThe Stunhalberd...\x01",
            "So that how it was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00109F*giggle*, he's a person\x01",
            "Randy is indebted to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWell, since this guy didn't want\x01",
            "to handle a rifle, I focused\x01",
            "on training him in that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIt's just a halberd, but as its merit\x01",
            "it has a lot of power when trusting\x01",
            "it in a straight line.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThat seemed also the cause why you\x01",
            "were hated by the former Commander.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00300FHa ha, well, bein' bound by rules\x01",
            "is not in my disposition, you know.\x02\x03",
            "#00309FLuckily I was transferred to the\x01",
            "Support Section and I'm feelin' good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FHu hu, for better or worse,\x01",
            "I guess everything is thanks\x01",
            "to the Vice Commander.\x02\x03",
            "#10302FAs expected, your demotion to\x01",
            "the Police Academy seemed to\x01",
            "have been a command error.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10100FUntil that Cult incident,\x01",
            "the CGF was managed under\x01",
            "that former Commander.\x02\x03",
            "#10109FEven so, the Vice Commander was\x01",
            "very much trusted by his subordinates\x01",
            "and even had skills...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIt's not such a big deal, but...\x01",
            "Well, it probably was an unpleasant sight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAfter I went to the Police Academy,\x01",
            "I focused on nurturing men of talent\x01",
            "who could reform that rotten system.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThinking about it now, in a certain \x01",
            "sense maybe that was fortunate.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI could instruct future CGF members\x01",
            "and police officers who hadn't taken\x01",
            "on any ways yet.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#6P#00012FI really think you were too\x01",
            "strict back then, though.\x02\x03",
            "#00006FSomeone like Frantz\x01",
            "occasionally cried...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PHa ha, well, don't say that.\x01",
            "It was worth it, was it not?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWell, many things happened\x01",
            "and thus, I came back to the CGF.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PFrom now on I'll cooperate\x01",
            "with you all too and together\x01",
            "we'll protect the autonomous state.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00100F*giggle*...\x01",
            "We will do our best.\x02\x03",
            "#00104FAlthough, people like us are still\x01",
            "inexperienced in some ways.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PCome on, no need to be modest.\x01",
            "You all have that much strength.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIt's thanks to that that you're doing\x01",
            "a proper job at the Special Support\x01",
            "Section that senior Sergei formed.\x02",
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
        "#6P#00005FSenior Sergei...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00305FWhat, you're an acquaintance\x01",
            "of that ol' man?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PHuh? More than acquaintance...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI've been indebted to senior\x01",
            "Sergei and senior Sonya\x01",
            "since in the past, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAt least I did the go-between\x01",
            "for their marriage.\x02",
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
        "#6P#00011FMA...!!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#4S#6P#00105FMARRIAGE......!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#4S#10111FCommander Sonya\x01",
            "and Chief Sergei!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#6P#10305FEeh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00306FHey hey hey, don't you\x01",
            "suddenly go throwin'\x01",
            "at us such a fact...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P...W-What.\x01",
            "You didn't know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWell, they divorced\x01",
            "five years ago, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PA lot of things overlapped,\x01",
            "like senior Sergei's demotion\x01",
            "and senior Sonya's promotion...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10304FHu hu, I see.\x01",
            "It seems there was none other\x01",
            "than an adult man and woman drama.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FEeeeh...\x01",
            "Commander Sonya...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00303FIt's true that I thought those two\x01",
            "were sooomehow suspicious, but...\x02\x03",
            "#00309FWhat can I say, I feel like\x01",
            "a mystery was solved♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00011FH-Hey, everyone...\x01",
            "Stop thinking fun of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00109F(I-I'm a little\x01",
            "curious too...)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            "#11P...Damn. \x01",
            "It escaped my lips.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PA-At any rate, mum's\x01",
            "the word regarding\x01",
            "this matter, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P*cough*, anyway...\x01",
            "Thank you for the training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PI'll count on you if something comes up again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FY-Yes.\x01",
            "We will look forward to hearing from you.\x02",
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
            "Quest [CGF Training Participation]\x07\x00",
            " completed!\x02",
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

    # Function_19_4FDB end

    def Function_20_61AE(): pass

    label("Function_20_61AE")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x19B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_696E")

    ChrTalk(
        0x101,
        (
            "#6P#00000FVice Commander Douglas, \x01",
            "thank you for your hard work.\x02",
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
            "#11PIt seems you saw the\x01",
            "request and came, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00300FWell, it's as you say, but...\x02\x03",
            "#00303F...Big bro Douglas, somehow\x01",
            "you seem to be on edge.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_65DA")

    ChrTalk(
        0x9,
        (
            "#11PYou should've keenly felt it too\x01",
            "when you entered the gate...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAt present, the CGF is\x01",
            "in a state of high alert.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PFurthermore, it even happened\x01",
            "that a wanted criminal forced\x01",
            "his way through the gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PFor that motive, we're in a situation\x01",
            "where we can't let our guard down at all.\x02",
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
            "#11PWell, it seems that wanted criminal\x01",
            "was caught by you, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PLet me thank you in\x01",
            "regard to that matter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FNo, we only did what it was expected.\x02\x03",
            "#00001F...Is the present request\x01",
            "related to that too?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68DC")

    label("loc_65DA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_67C8")

    ChrTalk(
        0x9,
        (
            "#11PYou should've keenly felt it too\x01",
            "when you entered the gate...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAt present, the CGF is\x01",
            "in a state of high alert.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PFurthermore, it even happened\x01",
            "that a scoundrel forced his\x01",
            "way through the gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PFor that motive, we're in a situation\x01",
            "where we can't let our guard down.\x02",
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
            "#6P#00003F(The medical supplies larcenist\x01",
            "who we failed to catch, eh...?)\x02\x03",
            "#00001F...But, does it mean that the present\x01",
            "request is related to that?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68DC")

    label("loc_67C8")


    ChrTalk(
        0x9,
        (
            "#11PYou should've keenly felt it too\x01",
            "when you entered the gate...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAt present, the CGF is\x01",
            "in a state of high alert.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWe're in a situation where we can't\x01",
            "let our guard down even a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00001FI see...\x01",
            "So the present request is\x01",
            "related to that too?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68DC")


    ChrTalk(
        0x9,
        "#11PYeah, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI'd like to explain the job\x01",
            "contents immediately, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAre you going to\x01",
            "accept the request?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_69BC")

    label("loc_696E")


    ChrTalk(
        0x9,
        "#11PAre you free?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PI'd like you to accept the request at once...\x02",
    )

    CloseMessageWindow()

    label("loc_69BC")

    Call(0, 21)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 2710, 0, -330, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_20_61AE end

    def Function_21_69EB(): pass

    label("Function_21_69EB")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A4C")
    Call(0, 22)
    Jump("loc_6B1A")

    label("loc_6A4C")


    ChrTalk(
        0x101,
        (
            "#6P#00006F...I'm sorry, our hands\x01",
            "are full right now...\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PHm...\x01",
            "Well, times are what they're,\x01",
            "so I guess it can't be helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAlright, in case you get free,\x01",
            "ask me again.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x19B, 3)

    label("loc_6B1A")

    Return()

    # Function_21_69EB end

    def Function_22_6B1B(): pass

    label("Function_22_6B1B")


    ChrTalk(
        0x101,
        "#6P#00000FYes, we accept.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PHm, I'm in your debt.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P──I wrote it in the request too, but recently \x01",
            "we received eyewitness reports about the \x01",
            "appearance of mysterious "black monsters".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIt seems there's damage to\x01",
            "crops and cattle in the vicinity\x01",
            "of Armorica Village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00105FBlack monsters...\x01",
            "I have the impression I once\x01",
            "heard about this somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00303FIt also rings me a bell the\x01",
            "the fact they attack crops.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10105FCould it be...\x01",
            "Similar to the "Wolf-Type Monsters" \x01",
            "incident that happened before...?\x02\x03",
            "#10103FAt that time, the culprit were military\x01",
            "dogs controlled by the mafia...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11P...After I read the report\x01",
            "on that incident I was\x01",
            "worried about it too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIn practice, Revache has been dismantled\x01",
            "but the whereabouts of the great number of\x01",
            "military dogs in their possession is unknown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PThe probability is definitely not low.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FTo what extent the investigation\x01",
            "by the CGF has progressed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWe inspected the damaged\x01",
            "scenes and we inquired lightly\x01",
            "the residents in the environs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAs a result, we identified that\x01",
            "the "black monsters" come from\x01",
            "the Ancient Battlefield area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PSo, I want you to head to\x01",
            "the Ancient Battlefield.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI want you to investigate these monsters\x01",
            "and, if possible, exterminate them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10302FI understand the situation in general.\x02\x03",
            "#10303FStill, you really look\x01",
            "to be quite busy, eh?\x02\x03",
            "#10300FI thought that things\x01",
            "like this were what\x01",
            "the CGF do, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI'd want to do that, but...\x01",
            "Like I told you before, the\x01",
            "CGF is in a state of high alert.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThe "Red Constellation", confirmed to have\x01",
            "been the Crossbell City raid perpetrators,\x01",
            "have vanished, and we don't have any leads.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PFurthermore, we're in a situation where\x01",
            "the Empire and Republic have begun\x01",
            "massive training maneuvers...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_72D9")

    ChrTalk(
        0x9,
        (
            "#11PIn order for something like that to\x01",
            "not happen again, as CGF we need to\x01",
            "especially strictly guard the borders.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_731C")

    label("loc_72D9")


    ChrTalk(
        0x9,
        (
            "#11PAs CGF, we need to especially\x01",
            "strictly guard the borders.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_731C")


    ChrTalk(
        0x102,
        (
            "#6P#00108FJust right before the "Non-Aggression Pact" \x01",
            "was signed...\x01",
            "It's becoming a situation similar to that one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11P...Hm.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PNo matter if they're monsters damage,\x01",
            "as you expect, in the situation we're in,\x01",
            "they're of low priority.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThe damage confirmed wasn't\x01",
            "even that much...and I can't\x01",
            "spare any men.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00304F...True, it's not the case to\x01",
            "make the CGF do something\x01",
            "like a monster extermination.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003F...We understand the outline of the situation.\x02\x03",
            "#00000FThen, please leave the "black monsters"\x01",
            "investigation to us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PHm, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PI'm counting on you, Special Support Section.\x02",
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
            "Quest [Ancient Battlefield Investigation]\x07\x00",
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

    # Function_22_6B1B end

    def Function_23_764C(): pass

    label("Function_23_764C")

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
            "#6P#00000F──And so, these are the present request facts.\x02\x03",
            "#00003FI think that there probably won't be any\x01",
            "more damage from the military dogs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11P...I understand...\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x9)

    ChrTalk(
        0x101,
        "#6P#00012FE-Eehm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#6P#00305FWhat, big bro Douglas.\x01",
            "You're totally silent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FAs I thought, not exterminating\x01",
            "the military dogs was bad?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11P...No, you did good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PI'm just a little surprised by the results\x01",
            "having surpassed my expectations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#6P#10300FWell, I guess.\x02\x03",
            "#10309FSomething like having "persuaded the military dogs"\x01",
            "would normally be a cock-and-bull story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00106FI-It really can be\x01",
            "unbelievable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FHowever, because it is the truth,\x01",
            "I think there are no problems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11P...No, it's all right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PIt's the best of all if you could\x01",
            "solve it in a peaceful way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PThank you, ladies and gentlemen of the Support Section.\x01",
            "Thanks to you, one of our\x01",
            "pending problems was cleared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00004FI'm glad to hear that.\x02\x03",
            "#00000FPlease call us whenever\x01",
            "something comes up again.\x02",
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
            "#11P──Then, we will continue to\x01",
            "be in a state of high alert.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PYou too, be careful.\x02",
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
            "Quest [Ancient Battlefield Investigation]\x07\x00",
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

    # Function_23_764C end

    SaveToFile()

Try(main)
