from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1440.bin",                # FileName
        "c1440",                    # MapName
        "c1440",                    # Location
        0x0031,                     # MapIndex
        "ed7101",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 49, 0, 1, 0, 2],
    )

    BuildStringList((
        "c1440",                  # 0
        "Ashley",                 # 1
        "Jingo",                  # 2
        "Dino",                   # 3
        "Kｷki",                  # 4
        "Vaan",                   # 5
        "Roser",                  # 6
    ))

    AddCharChip((
        "chr/ch09200.itc",                   # 00
        "chr/ch23900.itc",                   # 01
        "chr/ch06800.itc",                   # 02
        "chr/ch23000.itc",                   # 03
        "chr/ch24700.itc",                   # 04
        "chr/ch30800.itc",                   # 05
    ))

    DeclNpc(4294964437, 0,       13750,   0,    261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(5670,    29,      8649,    225,  261,  0x0, 0,   1,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(0,       0,       15090,   225,  389,  0x0, 0,   2,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(2000,    0,       15090,   0,    389,  0x0, 0,   5,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(9640,    0,       850,     180,  389,  0x0, 0,   3,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(10279,   0,       4294966746, 315,  389,  0x0, 0,   4,   0,   0,   0,   0,   13,  255,  0)

    DeclEvent(0x0000, 0, 21,  9.899999618530273,     14.0,                  -0.5,                  16.0,                  [0.25,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -2.4749999046325684,   -7.0,                  0.10000000149011612,   1.0])

    DeclActor(4590,    0,       7540,    1000,    5670,    1500,    8650,    0x007E, 0,  6,  0x0000)
    DeclActor(4294916276, 0,       6820,    1200,    4294916276, 1150,    6820,    0x007C, 0,  3,  0x0000)

    ChipFrameInfo(596, 0)                                        # 0

    ScpFunction((
        "Function_0_254",          # 00, 0
        "Function_1_304",          # 01, 1
        "Function_2_4F2",          # 02, 2
        "Function_3_5BB",          # 03, 3
        "Function_4_674",          # 04, 4
        "Function_5_2ADD",         # 05, 5
        "Function_6_2D6F",         # 06, 6
        "Function_7_2D73",         # 07, 7
        "Function_8_4102",         # 08, 8
        "Function_9_4432",         # 09, 9
        "Function_10_4492",        # 0A, 10
        "Function_11_474A",        # 0B, 11
        "Function_12_47C0",        # 0C, 12
        "Function_13_4821",        # 0D, 13
        "Function_14_4884",        # 0E, 14
        "Function_15_49E6",        # 0F, 15
        "Function_16_4BB5",        # 10, 16
        "Function_17_4FAF",        # 11, 17
        "Function_18_54C3",        # 12, 18
        "Function_19_62BE",        # 13, 19
        "Function_20_6630",        # 14, 20
        "Function_21_6E8C",        # 15, 21
    ))


    def Function_0_254(): pass

    label("Function_0_254")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_28C"),
        (1, "loc_298"),
        (2, "loc_2A4"),
        (3, "loc_2B0"),
        (4, "loc_2BC"),
        (5, "loc_2C8"),
        (6, "loc_2D4"),
        (SWITCH_DEFAULT, "loc_2E0"),
    )


    label("loc_28C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_298")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2A4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2B0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2BC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2C8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2D4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2E0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_2EC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_303")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2EC")

    label("loc_303")

    Return()

    # Function_0_254 end

    def Function_1_304(): pass

    label("Function_1_304")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_312")
    Jump("loc_4DB")

    label("loc_312")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_320")
    Jump("loc_4DB")

    label("loc_320")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_32E")
    Jump("loc_4DB")

    label("loc_32E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_34B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_346")
    SetChrFlags(0x8, 0x10)

    label("loc_346")

    Jump("loc_4DB")

    label("loc_34B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_359")
    Jump("loc_4DB")

    label("loc_359")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3A7")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xC, -2960, 20, 8530, 315)
    SetChrPos(0xD, -3010, 30, 7170, 315)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A2")
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xD, 0x10)

    label("loc_3A2")

    Jump("loc_4DB")

    label("loc_3A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_441")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x8, -2240, 20, 13000, 225)
    SetChrPos(0xB, -2630, 20, 11000, 0)
    SetChrPos(0xA, -3850, 0, 11830, 45)
    SetChrFlags(0xB, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_406")
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0x8, 0x10)

    label("loc_406")

    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xC, 4930, 0, 4600, 315)
    SetChrPos(0xD, 5930, 0, 4600, 315)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xD, 0x10)
    Jump("loc_4DB")

    label("loc_441")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_454")
    SetChrFlags(0x8, 0x80)
    Jump("loc_4DB")

    label("loc_454")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_491")
    SetChrPos(0x8, 1750, 30, 10220, 135)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47D")
    SetChrFlags(0x8, 0x10)

    label("loc_47D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48C")
    SetChrFlags(0x9, 0x10)

    label("loc_48C")

    Jump("loc_4DB")

    label("loc_491")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_49F")
    Jump("loc_4DB")

    label("loc_49F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4AD")
    Jump("loc_4DB")

    label("loc_4AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4BB")
    Jump("loc_4DB")

    label("loc_4BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x138, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D6")
    SetMapFlags(0x10000000)
    Event(0, 16)

    label("loc_4D6")

    SetChrFlags(0x8, 0x10)

    label("loc_4DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F1")
    SetMapFlags(0x10000000)
    Event(0, 17)

    label("loc_4F1")

    Return()

    # Function_1_304 end

    def Function_2_4F2(): pass

    label("Function_2_4F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_505")
    OP_1B(0x0, 0x0, 0x13)

    label("loc_505")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_51E")
    OP_10(0x0, 0x0)
    OP_10(0x3, 0x1)
    Jump("loc_524")

    label("loc_51E")

    OP_10(0x0, 0x1)
    OP_10(0x3, 0x0)

    label("loc_524")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 7)), scpexpr(EXPR_END)), "loc_532")
    ModifyEventFlags(0, 0, 0x80)

    label("loc_532")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_57B")
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_57B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5BA")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)

    label("loc_5BA")

    Return()

    # Function_2_4F2 end

    def Function_3_5BB(): pass

    label("Function_3_5BB")

    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "The "Exciting Family Lunch" is here.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_670")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0xE)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_670")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "You learned the "Picnic Lunch Box"\x07\x00",
            " recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_670")

    TalkEnd(0xFF)
    Return()

    # Function_3_5BB end

    def Function_4_674(): pass

    label("Function_4_674")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_695")
    Call(0, 18)
    Return()

    label("loc_695")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A7")
    Call(0, 20)
    Return()

    label("loc_6A7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_907")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_83C")

    ChrTalk(
        0xFE,
        (
            "Coincident with the\x01",
            "President's arrest, that\x01",
            ""huge tree" appeared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With the barrier gone, we've got to\x01",
            "be on guard against the two major\x01",
            "powers... We're in a difficult spot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe... This is getting interesting, isn't it. \x01",
            "As a weapons merchant, \x01",
            "I'll have to get greatly involved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FHa ha, how reliable.\x01",
            "...We'll trouble you for your services again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_902")

    label("loc_83C")


    ChrTalk(
        0xFE,
        (
            "Now that we're on guard against the two\x01",
            "major powers, I've gotten more requests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe... This is getting interesting, isn't it. \x01",
            "As a weapons merchant, \x01",
            "I'll have to get greatly involved.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_902")

    Jump("loc_2AD9")

    label("loc_907")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_DA2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CE5")

    ChrTalk(
        0xFE,
        "Oh, it's you guys, huh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe... It's been awhile. \x01",
            "You guys look surprisingly well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FMiss Ashley, it's been awhile.\x02\x03",
            "#00012F...Or rather, it looks like you're not\x01",
            "disturbed at all by the situation.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A9C")

    ChrTalk(
        0x10A,
        (
            "#00600FShe's supporting the police's\x01",
            "underground activities.\x02\x03",
            "#00603FThinking about the possible situation,\x01",
            "there's nothing strange in this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B26")

    label("loc_A9C")


    ChrTalk(
        0xFE,
        "Well, I vaguely suspected such a situation.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It's only natural I'm helping with Dudley \x01",
            "and the others' underground activities. \x02",
        )
    )

    CloseMessageWindow()

    label("loc_B26")


    ChrTalk(
        0x102,
        "#00105FS-So that's how it is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FIt looks like there are helpers\x01",
            "too among the civilians.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FWell, you're used to dealing with\x01",
            "underground organizations, aren't you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, you said it. Thanks\x01",
            "to that, I can earn a profit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...We too are in the middle of getting\x01",
            "things ready in case the worst happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm pulling all the good stuff out of\x01",
            "the warehouse. If you need anything,\x01",
            "discuss it with Jingo.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BE, 4)
    Jump("loc_D9D")

    label("loc_CE5")


    ChrTalk(
        0xFE,
        (
            "We too are in the middle of getting\x01",
            "things ready in case the worst happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm pulling all the good stuff out of\x01",
            "the warehouse. If you need anything,\x01",
            "discuss it with Jingo.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D9D")

    Jump("loc_2AD9")

    label("loc_DA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_103B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F60")

    ChrTalk(
        0xFE,
        (
            "Crossbell independence, eh?\x01",
            "Hah, that banker had a\x01",
            "lot to do with it, I bet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Hehe, redhead. Careful,\x01",
            "alright? I smell the scent\x01",
            "of an approaching battle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F...You said it. I can't think the two\x01",
            "major powers 'll remain silent too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe. As a weapons dealer,\x01",
            "my blood's boiling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I even thought to leave Crossbell,\x01",
            "but now that things are like this, \x01",
            "I'll have to stick here to the end.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1036")

    label("loc_F60")


    ChrTalk(
        0xFE,
        (
            "I smell the scent of an approaching battle...\x01",
            "Hehe. As a weapons dealer,\x01",
            "it makes my blood boil.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I even thought to leave Crossbell,\x01",
            "but now that things are like this, \x01",
            "I'll have to stick here to the end.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1036")

    Jump("loc_2AD9")

    label("loc_103B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1769")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16B7")
    OP_4B(0xFE, 0xFF)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x0, 0)

    ChrTalk(
        0xFE,
        "Oh, the Special Support Section...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The raid incident the other day...\x01",
            "What do you guys think of it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...Right.\x02\x03",
            "#00001FThere's a lot of things we don't\x01",
            "know at the moment, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FHowever, the fact that the "Red\x01",
            "Constellation" caused the incident\x01",
            "is the unmistakable truth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00203FBecause of that, it's natural to\x01",
            "think their employer, the Imperial\x01",
            "government, instigated it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yeah, there's a rumor like that\x01",
            "already spreading in the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That wouldn't explain\x01",
            "their immediate retreat,\x01",
            "though... Hmph, whatever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00305FOh yeah, you guys fought\x01",
            "against the demonized\x01",
            "Wald around here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Yeah. That was\x01",
            "definitely Wald.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "It was tough fighting against him... \x01",
            "Looks like he used that strange drug, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder where he got his hands on that drug\x01",
            "that can turn you into a monster like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108FThere is that too...\x02\x03",
            "#10106FWe're continuing to investigate,\x01",
            "but no way he could have gotten\x01",
            "it has come to light...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hah, so it's the same for you guys too.\x01",
            "I hate how we know\x01",
            "absolutely nothing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, because of the public order problem\x01",
            "resurfacing in the state after that incident,\x01",
            "business has become bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've been here a long time, but\x01",
            "for this to happen to Downtown...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    ChrTalk(
        0xFE,
        (
            "...Maybe it's time to\x01",
            "leave before long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FMiss Ashley...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10303F...Well, maybe it can't be helped.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FI'm sure someone like you\x01",
            "has got many connections...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, I haven't made up my mind yet.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's Jingo, too... Before long, I'll\x01",
            "have to plan out our future actions.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    OP_4C(0xFE, 0xFF)
    SetScenarioFlags(0x18D, 6)
    Jump("loc_1764")

    label("loc_16B7")


    ChrTalk(
        0xFE,
        (
            "...It might be time to\x01",
            "leave Crossbell soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Not knowing anything\x01",
            "is annoying...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's Jingo, too... Before long, I'll\x01",
            "have to plan out our future actions.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1764")

    Jump("loc_2AD9")

    label("loc_1769")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_182B")

    ChrTalk(
        0xFE,
        (
            "If you guys are going to\x01",
            "tangle with that dangerous\x01",
            "lot, be plenty careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think you understand that already,\x01",
            "but you'll get beaten if you\x01",
            "go in without firm resolve.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AD9")

    label("loc_182B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_18FC")

    ChrTalk(
        0xFE,
        (
            "It's gotten a little harder\x01",
            "to get products in after\x01",
            "the Trade Conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard the two major powers have started\x01",
            "regulating things behind the scenes.\x01",
            "I wish they'd give me a break.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AD9")

    label("loc_18FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1BA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AAA")

    ChrTalk(
        0xFE,
        (
            "Come to think of it, I heard remnants of the\x01",
            ""Anti-Immigration Policy Leauge" who attacked the\x01",
            "Trade Conference were captured yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard the Heiyue got involved and\x01",
            "there was a commotion in a train...\x01",
            "Couldn't have they done it a little more discretely?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1A7B")

    ChrTalk(
        0x101,
        (
            "#00012F(That's Miss Ashley for you.\x01",
            "She hears everything so quickly.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AA2")

    label("loc_1A7B")


    ChrTalk(
        0x101,
        "#00005F(So that happened, huh...)\x02",
    )

    CloseMessageWindow()

    label("loc_1AA2")

    SetScenarioFlags(0x0, 0)
    Jump("loc_1B9E")

    label("loc_1AAA")


    ChrTalk(
        0xFE,
        (
            "I heard remnants of the "Anti-Immigration\x01",
            "Policy" who attacked the Trade Conference\x01",
            "were captured yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard the Heiyue got involved and\x01",
            "there was a commotion in a train...\x01",
            "Couldn't have they done it a little more discretely?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B9E")

    Jump("loc_2AD9")

    label("loc_1BA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1C3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BBE")
    Call(0, 10)
    Jump("loc_1C38")

    label("loc_1BBE")


    ChrTalk(
        0xFE,
        (
            "Even so, it's strangely\x01",
            "lively today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Good grief...\x01",
            "Since when did this place\x01",
            "become a squirts' gathering spot?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C38")

    Jump("loc_2AD9")

    label("loc_1C3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1C4B")
    Jump("loc_2AD9")

    label("loc_1C4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1CDB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C66")
    Call(0, 5)
    Jump("loc_1CD6")

    label("loc_1C66")


    ChrTalk(
        0xFE,
        (
            "Now that I think about it,\x01",
            "I was the one who moved them, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Good grief... \x01",
            "I'm getting old too, huh.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CD6")

    Jump("loc_2AD9")

    label("loc_1CDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1F86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 2)), scpexpr(EXPR_END)), "loc_1EF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E81")

    ChrTalk(
        0xFE,
        (
            "There was a noisy guy on\x01",
            "the roof, so I was thinking\x01",
            "of firing off a shell, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There'd be a hole in the roof,\x01",
            "so I left it to Jingo to take care of him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FT-There's no way we could let\x01",
            "gunfire in a city pass, of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmph. I didn't do it, did I?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...But even so that blondie... \x01",
            "I feel like I've seen him before...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, must be my imagination.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1EED")

    label("loc_1E81")


    ChrTalk(
        0xFE,
        (
            "...But even so that blondie... \x01",
            "I feel like I've seen him before...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Well, must be my imagination.\x02",
    )

    CloseMessageWindow()

    label("loc_1EED")

    Jump("loc_1F81")

    label("loc_1EF2")


    ChrTalk(
        0xFE,
        (
            "The VIPs from each country\x01",
            "are all in Crossbell, huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I can't honestly say\x01",
            "what'll happen. I just hope\x01",
            "I don't get involved in it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F81")

    Jump("loc_2AD9")

    label("loc_1F86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_22AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21F5")
    OP_4B(0xFE, 0xFF)

    ChrTalk(
        0xFE,
        "Oh, if it isn't redhead.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Looks like you've returned\x01",
            "to the Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FYeah, thankfully.\x02\x03",
            "#00306FEven so... Your store's\x01",
            "suspicious as always.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hah, my bad. Unfortunately, we're an insignificant\x01",
            "business, so we don't have the leisure to worry\x01",
            "about outside appearances.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "By the way, in Back Street...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Yeah, looks like it. Poking\x01",
            "my nose into that carelessly\x01",
            "would only make things worse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F(...Hah. Based on that, she must've\x01",
            "looked into my relationship with\x01",
            "the "Red Constellation".)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F(I wonder just how\x01",
            "much she knows...)\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xFE, 0xFF)
    SetScenarioFlags(0x14D, 4)
    Jump("loc_22A6")

    label("loc_21F5")


    ChrTalk(
        0xFE,
        (
            "Because of that Trade Conference\x01",
            "or whatever, they've got officers\x01",
            "they don't normally here today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Good grief... If they\x01",
            "come here, it'll be a\x01",
            "pain dealing with them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22A6")

    Jump("loc_2AD9")

    label("loc_22AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2756")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2634")
    OP_4B(0xFE, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Come to think of it, guys...\x01",
            "Where's shorty and redhead?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#10106FS-Shorty and redhead...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah... \x01",
            "She means Tio and Randy.\x02\x03",
            "#00003FThey're not back yet from\x01",
            "their respective assignments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes. It seems it will be still a\x01",
            "little while since they join us again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I see. I don't know\x01",
            "about shorty, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Redhead is probably in the\x01",
            "middle of helping with CGF\x01",
            "rehabilitation training, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FH-How do you know that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10302FHu hu. She's just showing off.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, when you run a shop like mine, \x01",
            "you get to know these things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00105FMiss Ashley?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Ah... No, nevermind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, if you're working hard, \x01",
            "that's good enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "For now, you should\x01",
            "train yourselves so you\x01",
            "don't fall behind him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FS-Sure.\x02",
    )

    CloseMessageWindow()
    OP_4C(0xFE, 0xFF)
    SetScenarioFlags(0x137, 6)
    Jump("loc_2751")

    label("loc_2634")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2715")

    ChrTalk(
        0xFE,
        (
            "Guys, it's useless\x01",
            "trying to get anything\x01",
            "else out of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm not certain of the information anyway,\x01",
            "and I've no obligation to tell you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, you should try to find\x01",
            "out the rest on your own.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2751")

    label("loc_2715")


    ChrTalk(
        0xFE,
        (
            "Well, you should try to find\x01",
            "out the rest on your own.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2751")

    Jump("loc_2AD9")

    label("loc_2756")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2AD9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A51")
    OP_4B(0xFE, 0xFF)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x0, 500)

    ChrTalk(
        0xFE,
        "Oh, if it isn't the Special Support Section.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I haven't seen you guys\x01",
            "in quite a while, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHa ha, nice to see\x01",
            "you again as well.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x105, 500)

    ChrTalk(
        0xFE,
        (
            "Hu hu, I heard the rumors but I\x01",
            "never thought you'd joined them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "What's going on here,\x01",
            "Wazy Hemisphere?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FEh, I just felt like it.\x02\x03",
            "#10302FNext time, I'd like to chat\x01",
            "over drinks at Trinity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Hmph. Well, whatever.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So then? \x01",
            "What do you need?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "If it's about the Revache's goods,\x01",
            "that's been taken care of, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F(She knew that much already, huh...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FWell, we didn't came for anything in\x01",
            "particular today. Sorry for bothering you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Is that so.\x01",
            "Well, feel free\x01",
            "to look around.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x0, 0x0)
    OP_4C(0xFE, 0xFF)
    SetScenarioFlags(0x137, 5)
    Jump("loc_2AD9")

    label("loc_2A51")

    TurnDirection(0xFE, 0x105, 0)

    ChrTalk(
        0xFE,
        (
            "But Wazy, I can't believe you\x01",
            "joined the Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Every cloud will rain\x01",
            "sooner or later, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x0, 0x0)

    label("loc_2AD9")

    TalkEnd(0xFE)
    Return()

    # Function_4_674 end

    def Function_5_2ADD(): pass

    label("Function_5_2ADD")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    TurnDirection(0x8, 0x9, 0)

    ChrTalk(
        0x8,
        (
            "Hey, Jingo. Do you remember\x01",
            "what I did with the grenades\x01",
            "you brought in yesterday?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I think I put them somewhere\x01",
            "around here, but...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 0)

    ChrTalk(
        0x9,
        "Mama, don't you remember?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "They were in the way so\x01",
            "you moved them to the\x01",
            "basement warehouse.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "Oh, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Thanks, Jingo.\x01",
            "Really, what you should have, is a daughter.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F(Moving grenades, like it's\x01",
            "a normal conversation...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F(As usual, these mother\x01",
            "and daughter are peculiar.)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D4C")
    OP_4C(0x9, 0xFF)

    label("loc_2D4C")

    OP_4C(0x8, 0xFF)
    OP_93(0x8, 0x87, 0x0)
    OP_93(0x9, 0xE1, 0x0)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    Return()

    # Function_5_2ADD end

    def Function_6_2D6F(): pass

    label("Function_6_2D6F")

    Call(0, 7)
    Return()

    # Function_6_2D6F end

    def Function_7_2D73(): pass

    label("Function_7_2D73")

    TalkBegin(0x9)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2D8A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40FE")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                       # 0
            "Exchange (Equipments)\x01",      # 1
            "Exchange (Quartz)\x01",          # 2
            "Exchange (Other)\x01",           # 3
            "Cancel\x01",                     # 4
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2E1A")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2E1A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E3A")
    OP_AF(0x8C)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_40F9")

    label("loc_2E3A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E5A")
    OP_AF(0x96)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_40F9")

    label("loc_2E5A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2EA6")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2FB, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AF(0xA3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2FB, 0x0)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2EA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E9E")
    ClearScenarioFlags(0x0, 1)

    label("loc_2E9E")

    SetScenarioFlags(0x189, 5)

    label("loc_2EA1")

    Jump("loc_2EE8")

    label("loc_2EA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2EB6")
    OP_AF(0xA2)
    Jump("loc_2EE8")

    label("loc_2EB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2EC6")
    OP_AF(0xA1)
    Jump("loc_2EE8")

    label("loc_2EC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2ED6")
    OP_AF(0xA1)
    Jump("loc_2EE8")

    label("loc_2ED6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2EE6")
    OP_AF(0xA0)
    Jump("loc_2EE8")

    label("loc_2EE6")

    OP_AF(0xA0)

    label("loc_2EE8")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_40F9")

    label("loc_2EF7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F0B")
    Jump("loc_40F9")

    label("loc_2F0B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40F9")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_344C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 5)), scpexpr(EXPR_END)), "loc_3155")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30C2")

    ChrTalk(
        0x9,
        (
            "Ooh...\x01",
            "As expected, Kagemaru goods\x01",
            "are stylish and gallant, huh!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Wait, guess there're katanas in the warehouse.\x01",
            "If they had those, they'd be perfect, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Guess I'll make Vaan and Roser wear\x01",
            "them too and then it's chanbara time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FT-That's a little beyond the\x01",
            "category of child's play.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FThe Kagemaru character too\x01",
            "is conveyed slightly wrong.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3150")

    label("loc_30C2")


    ChrTalk(
        0x9,
        (
            "As expected, Kagemaru goods\x01",
            "are stylish and gallant, huh!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Guess I'll make Vaan and Roser wear\x01",
            "them too and then it's chanbara time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3150")

    Jump("loc_3447")

    label("loc_3155")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3247")

    ChrTalk(
        0x9,
        "Customers, do you know a total black cat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FA total black cat...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F...You must be talking\x01",
            "about..."Kagemaru"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "That's it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Jingo's looking for his clothes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Get a lot and bring me them.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x189, 6)
    Jump("loc_3447")

    label("loc_3247")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33AA")

    ChrTalk(
        0x9,
        "Customers, did you see that huuuge tree?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Amazing, isn't it. If you\x01",
            "cut it down, how many orbal\x01",
            "guns do you think it'd make?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00006F(She's super excited...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00106F(A dangerous child, as always...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3447")

    label("loc_33AA")


    ChrTalk(
        0x9,
        (
            "If you cut down that tree, I wonder\x01",
            "how many orbal guns it'd make.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Nishishi...\x01",
            "Although maybe it would be difficult\x01",
            "even with many Imperial tanks.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3447")

    Jump("loc_40F9")

    label("loc_344C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_35D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_359C")

    ChrTalk(
        0x9,
        "Oh, customers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It's dangerous out there.\x01",
            "Buy some protection!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you want to blow up the armors outside, \x01",
            "we might have grenades for that.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00006F(Those probably aren't for self-defense...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_35D0")

    label("loc_359C")


    ChrTalk(
        0x9,
        (
            "It's dangerous out there.\x01",
            "Buy some protection!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35D0")

    Jump("loc_40F9")

    label("loc_35D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3663")

    ChrTalk(
        0x9,
        (
            "I talked it over with mama, and\x01",
            "we decided to stay in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Customers, if you want\x01",
            "something, just say the word.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40F9")

    label("loc_3663")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_36F0")

    ChrTalk(
        0x9,
        (
            "As usual, everyone's busy\x01",
            "with the reconstruction work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Give Jingo and mama\x01",
            "some credit. We help\x01",
            "too every so often.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40F9")

    label("loc_36F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3862")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37FD")

    ChrTalk(
        0x9,
        "*yaaawn*, so sleepy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "An urgent job came in last night and since\x01",
            "I rummaged around the warehouse with\x01",
            "mama, I couldn't get much sleep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "But, mama gets urgent\x01",
            "orders like that often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Was mama that close\x01",
            "with that customer?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_385D")

    label("loc_37FD")


    ChrTalk(
        0x9,
        (
            "But, mama gets urgent\x01",
            "orders like that often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Was mama that close\x01",
            "with that customer?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_385D")

    Jump("loc_40F9")

    label("loc_3862")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_38DF")

    ChrTalk(
        0x9,
        "Mrr, it's still drizzling.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If it's got to rain, might as\x01",
            "well come pouring down\x01",
            "and be over with it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40F9")

    label("loc_38DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3953")
    OP_93(0x9, 0x10E, 0x0)

    ChrTalk(
        0x9,
        "Well, they never learn too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Did they totally forget they got\x01",
            "slapped before by mama?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40F9")

    label("loc_3953")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_39D2")

    ChrTalk(
        0x9,
        (
            "Hey customers. You\x01",
            "don't have to worry\x01",
            "about them, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We've got good stuff\x01",
            "today too. Let's exchange!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40F9")

    label("loc_39D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3ABC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A73")

    ChrTalk(
        0x9,
        "Mama went to drink.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "She's been busy sorting\x01",
            "inventory since morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "She says she's having a\x01",
            "little drink as a reward.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3AB7")

    label("loc_3A73")


    ChrTalk(
        0x9,
        (
            "Mama is strict with our customers,\x01",
            "but she's very sweet to me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AB7")

    Jump("loc_40F9")

    label("loc_3ABC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3B4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AD7")
    Call(0, 5)
    Jump("loc_3B49")

    label("loc_3AD7")

    TurnDirection(0x9, 0x0, 0)

    ChrTalk(
        0x9,
        "She sometimes forgets stuff, though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Nishishi... Jingo always knew\x01",
            "it'd be bad if I wasn't here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B49")

    Jump("loc_40F9")

    label("loc_3B4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3CDE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 2)), scpexpr(EXPR_END)), "loc_3BF2")

    ChrTalk(
        0x9,
        (
            "That blondie was pretty\x01",
            "lively even though he\x01",
            "jumped down from the roof.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Maybe it would've been better\x01",
            "if I had kicked him harder.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CD9")

    label("loc_3BF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C97")

    ChrTalk(
        0x9,
        (
            "We rarely close up shop, but mama and\x01",
            "I went to see the unveiling ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "That building really\x01",
            "is ridiculously big.\x01",
            "Jingo was shocked.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3CD9")

    label("loc_3C97")


    ChrTalk(
        0x9,
        (
            "That building really\x01",
            "is ridiculously big.\x01",
            "Jingo was shocked.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CD9")

    Jump("loc_40F9")

    label("loc_3CDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3E06")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DA7")

    ChrTalk(
        0x9,
        (
            "A new Sister came to\x01",
            "read us a book, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "She said it won't be the same as always and this\x01",
            "time she left us another book for "homework".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I kinda hate her...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3E01")

    label("loc_3DA7")


    ChrTalk(
        0x9,
        (
            "I kinda hate\x01",
            "that Sister...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, since she brought it...\x01",
            "I guess I'll read it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E01")

    Jump("loc_40F9")

    label("loc_3E06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4024")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E21")
    Call(0, 8)
    Jump("loc_401F")

    label("loc_3E21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F9F")

    ChrTalk(
        0x9,
        (
            "Damn you rain. Damp, humid, wet, gloomy...\x01",
            "So depressing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you fire an orbal gun into a\x01",
            "rain cloud, will it disappear?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005FU-Umm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F(Hmm. What should\x01",
            "we reply to her...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F(Yes... I don't have anything\x01",
            "to say back to her.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_401F")

    label("loc_3F9F")


    ChrTalk(
        0x9,
        (
            "Damn you rain. Damp, humid, wet, gloomy...\x01",
            "So depressing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I wonder if you can blow away\x01",
            "rain clouds with orbal bombs?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_401F")

    Jump("loc_40F9")

    label("loc_4024")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_40F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_403F")
    Call(0, 8)
    Jump("loc_40F9")

    label("loc_403F")


    ChrTalk(
        0x9,
        (
            "I think you already know,\x01",
            "but the only thing we can't\x01",
            "exchange are stolen goods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We've got medicine, Quartz,\x01",
            "accessories... and other stuff ready\x01",
            "for you, so come take a look.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40F9")

    Jump("loc_2D8A")

    label("loc_40FE")

    TalkEnd(0x9)
    Return()

    # Function_7_2D73 end

    def Function_8_4102(): pass

    label("Function_8_4102")


    ChrTalk(
        0x9,
        "Oh, customers. It's been awhile.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We can't sell you weapons,\x01",
            "but want to exchange?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We've got a good selection of\x01",
            "stuff for the general public too.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_41C9")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_41C9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_41EF")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_41EF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4215")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4215")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_423B")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_423B")

    Sleep(1000)

    ChrTalk(
        0x101,
        "#00006FA-A dangerous remark, as always.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FUmm, is it really all right for us\x01",
            "to make use of this store...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FW-Well, on the surface those\x01",
            "goods don't seem illegal...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHu hu. Then in a manner of speaking,\x01",
            "there's no problem, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Ah, also. We've been active\x01",
            "in more areas recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you've got good stuff,\x01",
            "why not taking some here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'll trade you some\x01",
            "equally good stuff for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FHa ha, got it. We'll be\x01",
            "using your services again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x137, 7)
    Return()

    # Function_8_4102 end

    def Function_9_4432(): pass

    label("Function_9_4432")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4447")
    Call(0, 10)
    Jump("loc_448E")

    label("loc_4447")


    ChrTalk(
        0xFE,
        (
            "A h-hundred thousand mira, huh...\x01",
            "I've never even seen that much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_448E")

    TalkEnd(0xFE)
    Return()

    # Function_9_4432 end

    def Function_10_4492(): pass

    label("Function_10_4492")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0x8, 0xFF)

    ChrTalk(
        0x8,
        (
            "Oh, you must be talking\x01",
            "about that ENIGMA.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Watch this. If you hold it to your ear, \x01",
            "it becomes a communicator.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "Y-You're right. It's really true.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "By the way, the police and the Bracers...\x01",
            "And Wazy too have been using them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "By the way, Miss Ashley. \x01",
            "How much would it be to get one\x01",
            "of these on the up-and-up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm? Well they're all made to\x01",
            "order. I think 100,000 mira,\x01",
            "minimum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But if you're interested in one of\x01",
            "my knock-offs, I can be flexible...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Whoa, do you guys\x01",
            "actually want one?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "A h-hundred thousand mira...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "A h-hundred thousand one-mira chocolates...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Ha hah, I got a good reaction\x01",
            "out of you guys, didn't I.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x16E, 5)
    Return()

    # Function_10_4492 end

    def Function_11_474A(): pass

    label("Function_11_474A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_475F")
    Call(0, 10)
    Jump("loc_47BC")

    label("loc_475F")


    ChrTalk(
        0xFE,
        (
            "A h-hundred thousand one-mira chocolates...\x01",
            "H-How many are a hundred thousand of those?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47BC")

    TalkEnd(0xFE)
    Return()

    # Function_11_474A end

    def Function_12_47C0(): pass

    label("Function_12_47C0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4811")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47DE")
    Call(0, 14)
    Jump("loc_480C")

    label("loc_47DE")


    ChrTalk(
        0xFE,
        (
            "Crap, Jingo's mom\x01",
            "is as scary as always.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_480C")

    Jump("loc_481D")

    label("loc_4811")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_481D")
    Call(0, 15)

    label("loc_481D")

    TalkEnd(0xFE)
    Return()

    # Function_12_47C0 end

    def Function_13_4821(): pass

    label("Function_13_4821")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4874")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_483F")
    Call(0, 14)
    Jump("loc_486F")

    label("loc_483F")


    ChrTalk(
        0xFE,
        (
            "*chuckle*...\x01",
            "Another failed operation, eh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_486F")

    Jump("loc_4880")

    label("loc_4874")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4880")
    Call(0, 15)

    label("loc_4880")

    TalkEnd(0xFE)
    Return()

    # Function_13_4821 end

    def Function_14_4884(): pass

    label("Function_14_4884")

    OP_4B(0x8, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xC,
        (
            "Woah, so this is an orbal\x01",
            "gun, huh. How cool!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Hey Vaan. Can you\x01",
            "roast meat with that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hmm. Well I guess you could.\x01",
            "Nihihi, I think I'll test it out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "...Hey squirts.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xC, 0)

    ChrTalk(
        0x8,
        (
            "Don't touch the merchandise\x01",
            "around here. (*glare*)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "O-Okay...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "*chuckle*...\x01",
            "Jingo's mother\x01",
            "is powerful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    OP_93(0x8, 0x0, 0x0)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xD, 0x10)
    OP_4C(0x8, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_14_4884 end

    def Function_15_49E6(): pass

    label("Function_15_49E6")

    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B04")

    ChrTalk(
        0xC,
        (
            "Hey Jingo. \x01",
            "We came to play.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "Give us somethin'.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Ooh, you guys.\x01",
            "Got mira?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hya ha ha, I did but spent\x01",
            "the last of it yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "*chuckle*... We ate\x01",
            "meat, remember? Meat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "*sigh*... As usual, you never\x01",
            "plan anything, do you guys.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4BA8")

    label("loc_4B04")


    ChrTalk(
        0xC,
        (
            "Stop being impertinent and\x01",
            "give us somethin', Jingo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hmm? You guys still look pretty\x01",
            "good right now, so no way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "*chuckle*... \x01",
            "You're a demon, Jingo.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BA8")

    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_15_49E6 end

    def Function_16_4BB5(): pass

    label("Function_16_4BB5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x10000000)
    OP_68(0, 1100, 12800, 0)
    MoveCamera(50, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, -600, 0, 1800, 0)
    SetChrPos(0x102, 600, 0, 1800, 0)
    SetChrPos(0x109, 900, 0, 700, 0)
    SetChrPos(0x105, -900, 0, 700, 0)
    OP_68(0, 1100, 2800, 6000)
    MoveCamera(45, 19, 0, 6000)
    SetCameraDistance(18500, 6000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#12P#00001FHmm, this store has a\x01",
            "suspicious air, like always.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#6P#00108FLooks like Jingo's looking\x01",
            "after the store, as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10103FThis store is one of the black\x01",
            "markets in Crossbell City, huh.\x02\x03",
            "#10101FThere's rumors amongst the CGF about this\x01",
            "place dealing with weapons and ammunition...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FWell, they're honest folks\x01",
            "compared to most stores like this.\x02\x03",
            "#10300FThe owner is quite the character, though.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4E2E():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4E2E)
    Sleep(50)

    def lambda_4E3E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4E3E)
    Sleep(50)
    TurnDirection(0x102, 0x105, 500)

    ChrTalk(
        0x101,
        (
            "#5P#00003FIt sure seems that way...\x02\x03",
            "#00001FAnyway, if we have business\x01",
            "here, let's finish it quickly.\x02",
        )
    )

    CloseMessageWindow()
    Sound(814, 0, 100, 0)
    SetChrName("")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※At Exchange Shop "Neinvalli",\x01",
            "you can exchange specific\x01",
            "items for high rarity ones.\x02\x03",
            "※To make an exchange,\x01",
            "talk to Jingo at the counter\x01",
            "and select "Exchange".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 0, 0, 1000, 0)
    SetScenarioFlags(0x138, 4)
    EventEnd(0x5)
    Return()

    # Function_16_4BB5 end

    def Function_17_4FAF(): pass

    label("Function_17_4FAF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x10000000)
    SetChrPos(0x101, -600, 0, 1800, 0)
    SetChrPos(0x102, 600, 0, 1800, 0)
    SetChrPos(0x109, 900, 0, 700, 0)
    SetChrPos(0x105, -900, 0, 700, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x138, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5383")
    OP_68(0, 1100, 12800, 0)
    MoveCamera(50, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    OP_68(0, 1100, 2800, 6000)
    MoveCamera(45, 19, 0, 6000)
    SetCameraDistance(18500, 6000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#12P#00001FHmm, this store has a\x01",
            "suspicious air, like always.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#6P#00108FLooks like Jingo's looking\x01",
            "after the store, as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10103FThis store is one of the black\x01",
            "markets in Crossbell City, huh.\x02\x03",
            "#10101FThere's rumors amongst the CGF about this\x01",
            "place dealing with weapons and ammunition...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FWell, they're honest folks\x01",
            "compared to most stores like this.\x02\x03",
            "#10300FThe owner is quite the character, though.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5232():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5232)
    Sleep(50)

    def lambda_5242():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_5242)
    Sleep(50)
    TurnDirection(0x102, 0x105, 500)

    ChrTalk(
        0x101,
        (
            "#5P#00003FLooks that way...\x02\x03",
            "#00001FAnyway, let's ask Miss\x01",
            "Ashley about that man.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(814, 0, 100, 0)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※At Exchange Shop "Neinvalli",\x01",
            "you can exchange specific\x01",
            "items for high rarity ones.\x02\x03",
            "※To make an exchange,\x01",
            "talk to Jingo at the counter\x01",
            "and select "Exchange".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_54A9")

    label("loc_5383")

    OP_68(0, 1100, 2800, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#12P#00006FHmm. This really is a\x01",
            "suspicious store, huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#12P#00106FThat's right. No matter how many times\x01",
            "I come here, I can't get used to it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#11P#00101FAnyway, let's ask Miss\x01",
            "Ashley about that man.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()

    label("loc_54A9")

    SetChrPos(0x0, 0, 0, 1000, 0)
    SetScenarioFlags(0x138, 5)
    SetScenarioFlags(0x128, 3)
    EventEnd(0x5)
    Return()

    # Function_17_4FAF end

    def Function_18_54C3(): pass

    label("Function_18_54C3")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    Fade(500)
    OP_68(-2860, 1000, 12800, 0)
    MoveCamera(37, 22, 0, 0)
    OP_6E(460, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, -3100, 20, 11800, 0)
    SetChrPos(0x102, -4400, 20, 11000, 45)
    SetChrPos(0x109, -2900, 20, 10800, 0)
    SetChrPos(0x105, -1700, 20, 12000, 315)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x8, 0xB4, 0x1F4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5827")

    ChrTalk(
        0x8,
        "#5POh, if it isn't the Special Support Section.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI haven't seen you guys\x01",
            "in quite a while, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012FHa ha, nice to see\x01",
            "you again as well.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x105, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#5PHu hu, I heard the rumors but I\x01",
            "never thought you'd joined them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWhat's going on here,\x01",
            "Wazy Hemisphere?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FEh, I just felt like it.\x02\x03",
            "#10302FNext time, I'd like to chat\x01",
            "over drinks at Trinity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PHmph. Well, whatever.\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#5PSo then? \x01",
            "What do you need?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIf it's about the Revache's goods,\x01",
            "that's been taken care of, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00006F(She knew that much already, huh...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103FActually, we have a\x01",
            "question for you, Miss Ashley.\x02\x03",
            "#00100FAs a former weapons dealer.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x137, 5)
    Jump("loc_58E8")

    label("loc_5827")


    ChrTalk(
        0x8,
        "#5POh, the Special Support Section, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PNeed something with me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103FYes. Actually, we have a\x01",
            "question for you, Miss Ashley.\x02\x03",
            "#00100FTo you, as a former weapons dealer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58E8")

    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        "#5PHmm? And what would that be?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAbout the fact that Cao and his\x01",
            "pals have started making moves?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FSo you already know, huh.\x02\x03",
            "#00001FMaybe this is a different\x01",
            "matter from that one, but...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_64(0x8)

    ChrTalk(
        0x8,
        "#5PAn one-eyed, huge red haired...man?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FAny ideas?\x02\x03",
            "It's likely that he's connected\x01",
            "to the underworld somehow...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThere're a few people\x01",
            "who fit that description.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PBut, if it's someone who would come to\x01",
            "Crossbell in these circumstances...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00108FU-Uhm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305FWow, you're that\x01",
            "sure about him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PWell...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI was just imagining the\x01",
            "worst case scenario.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThere's no way in hell you'll\x01",
            "be able to match him in combat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00101FReally...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10101FS-So he really is a\x01",
            "jaeger or terrorist?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PUh uh, I wonder.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIf it really is him, I hung\x01",
            "out with him for a time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PI can't just speak willy-nilly about him.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10107FB-But...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006F──Whether he's a jaeger or not,\x01",
            "if he's a terrorist, we must act.\x02\x03",
            "#00003FEven in Crossbell there're\x01",
            "laws against acts of terrorism.\x02\x03",
            "#00013FCan't you even give us the\x01",
            "bare minimum information?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00108FLloyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PUh uh, not bad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P──Guy's younger brother, huh?\x01",
            "You've got a good head on your shoulders.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00005FMiss Ashley, you knew\x01",
            "my big brother...!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PDudley shows his face around here\x01",
            "every once in awhile these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PBut back then, it was that\x01",
            "unpredictable detective that\x01",
            "came to canvas Downtown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PWe lost an interesting one, didn't we?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00008F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWell, for the sake of that\x01",
            "idiot, I'll give you this much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIn my worst case scenario, \x01",
            "he's definitely not a terrorist.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PBut he's dangerous...\x01",
            "Like a man-eating tiger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10108FM-Man-eating tiger...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306FOh boy... Sounds like someone\x01",
            "we don't want to mess with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWell, I'm not sure\x01",
            "whether it's him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHe was alone, right?\x01",
            "The guy you saw?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PBecause the guy I'm thinking of is\x01",
            "usually with subordinates or companions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005FI-Is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00101FIn that case... Is it someone\x01",
            "related to the military?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PUh uh, that's as much as I can give.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYou'll have to get the\x01",
            "rest for yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00006F...I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00104FThank you for the information.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_93(0x8, 0x0, 0x0)
    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, -2860, 20, 11750, 180)
    SetScenarioFlags(0x128, 4)
    OP_1B(0x0, 0x0, 0x13)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_18_54C3 end

    def Function_19_62BE(): pass

    label("Function_19_62BE")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(300, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    SetChrFlags(0x0, 0x8)
    SetChrFlags(0x1, 0x8)
    SetChrFlags(0x2, 0x8)
    SetChrFlags(0x3, 0x8)
    OP_68(0, 1200, 500, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20000, 0)
    Sleep(500)
    OP_68(5100, 1200, 8100, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    OP_93(0x9, 0xB4, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x9,
        "#5PMrr. Still drizzling, huh?\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x13B, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#11POh right, mama. Can we unpack\x01",
            "the goods we got yesterday?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x87, 0x0)

    ChrTalk(
        0x8,
        (
            "Sure, but no need to rush\x01",
            "when the weather's like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "...More importantly, Jingo.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Did you see anyone weird\x01",
            "when you went out yesterday?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWeirdos? There were\x01",
            "plenty of those, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PLike a youngster dressed like he was\x01",
            "on vacation or a Sister who was buying\x01",
            "a mountain of bread...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#11PAnd that Wazy is a weirdo too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "I see. Well, that's fine then.\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_68(-2860, 1200, 13750, 3500)
    MoveCamera(15, 26, 0, 3500)
    OP_6F(0x79)
    OP_64(0x8)
    Sleep(500)

    ChrTalk(
        0x8,
        "#5P(...Maybe I'm overthinking it.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P(If he came to the city, he'd be\x01",
            "bringing his daughter as well.)\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(19500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    ClearChrFlags(0x0, 0x8)
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    SetScenarioFlags(0x22, 0)
    NewScene("c1400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_19_62BE end

    def Function_20_6630(): pass

    label("Function_20_6630")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    Fade(500)
    OP_68(-2860, 1000, 12800, 0)
    MoveCamera(37, 22, 0, 0)
    OP_6E(460, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, -3100, 20, 11800, 0)
    SetChrPos(0x102, -4400, 20, 11000, 45)
    SetChrPos(0x103, -3700, 20, 10500, 0)
    SetChrPos(0x109, -2600, 20, 10800, 0)
    SetChrPos(0x105, -1900, 20, 12000, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x8, 0xB4, 0x1F4)

    ChrTalk(
        0x8,
        "#5POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI thought you might\x01",
            "stop by around now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FThen that means...\x01",
            "Randy came here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYeah, he called me yesterday and\x01",
            "picked up some things this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHe begged me to play innocent\x01",
            "if you guys came, but I'm not\x01",
            "obligated to do that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        "#10309FAhaha, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00101FThen... What did\x01",
            "Randy order?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00201FAn orbal rifle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PNo, it wasn't anything\x01",
            "that common.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PExplosives, armor piercing\x01",
            "rounds, grenades, and even\x01",
            "old-style gunpowder ammo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHe bought up the entire\x01",
            "stock I had in the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAlso, an unregistered "ENIGMA II"\x01",
            "that showed up in the black market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FI see...\x02\x03",
            "#00008F...He is nothing if not thorough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00206FYes... If he's even using an unregistered\x01",
            "ENIGMA, we won't know its number.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10105FBut, he didn't buy\x01",
            "any actual weapons?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYeah, well I wanted to\x01",
            "suggest powerful orbal\x01",
            "and gunpowder rifles, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIt seems that the "Red Constellation"\x01",
            "next leader didn't like them.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00011FMiss Ashley...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00106FSo you knew...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHah, of course. \x01",
            "Information is life, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PSeems he plans to scare\x01",
            "the hell out of them, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P"Ogre Rosso" and\x01",
            ""Bloody Shirley" are\x01",
            "the real monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThat half-wit former jaeger\x01",
            "will surely get killed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#12P#00201F...We won't let that happen.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00013FWe're here to try\x01",
            "to stop that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHu hu, it's been that\x01",
            "way for awhile.\x02\x03",
            "#10302FLooks like provoking them won't work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PGood grief, looks that way.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWell, if that idiot kicks the bucket,\x01",
            "it wouldn't be my problem, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI'd hate to lose a regular customer.\x01",
            "Save him for me, will you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10101FYes...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00103FThank you very much for the information.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_93(0x8, 0x0, 0x0)
    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, -2860, 20, 11750, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x165, 6)
    OP_29(0xAA, 0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_20_6630 end

    def Function_21_6E8C(): pass

    label("Function_21_6E8C")

    EventBegin(0x1)
    OP_4B(0x9, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F88")

    ChrTalk(
        0x9,
        "Are you heading to the warehouse?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hmm... Well, since you're\x01",
            "customers, I guess it's fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Don't touch anything weird.\x01",
            "I won't be responsible if you die.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F...T-Thank you for your consideration.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x189, 7)
    ModifyEventFlags(0, 0, 0x80)
    Jump("loc_70B8")

    label("loc_6F88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_703B")

    ChrTalk(
        0x9,
        (
            "...Hey, customers. Don't try\x01",
            "to deceive the eyes of Jingo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Basement warehouse entry is\x01",
            "permitted to staff only.\x01",
            "If you're buying, it's right this way!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_70B8")

    label("loc_703B")


    ChrTalk(
        0x9,
        (
            "Hey, customers?\x01",
            "Did you hear what Jingo say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm telling you not to go down there!!\x01",
            "If you're buying, do it here!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_70B8")

    Sleep(50)
    SetChrPos(0x0, 9940, 0, 11910, 180)
    OP_4C(0x9, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_21_6E8C end

    SaveToFile()

Try(main)
