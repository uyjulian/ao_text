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
        "Function_4_672",          # 04, 4
        "Function_5_299B",         # 05, 5
        "Function_6_2BF3",         # 06, 6
        "Function_7_2BF7",         # 07, 7
        "Function_8_3EDB",         # 08, 8
        "Function_9_41F5",         # 09, 9
        "Function_10_4255",        # 0A, 10
        "Function_11_4501",        # 0B, 11
        "Function_12_4562",        # 0C, 12
        "Function_13_45C3",        # 0D, 13
        "Function_14_4626",        # 0E, 14
        "Function_15_4782",        # 0F, 15
        "Function_16_494D",        # 10, 16
        "Function_17_4D41",        # 11, 17
        "Function_18_524D",        # 12, 18
        "Function_19_5FFF",        # 13, 19
        "Function_20_633C",        # 14, 20
        "Function_21_6B65",        # 15, 21
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
            "The "Exciting Family\x01",
            "Lunch" is here.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_66E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0xE)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66E")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "Learned the \x07\x02",
            ""Picnic\x01",
            "Lunch Box"\x07\x00",
            " recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_66E")

    TalkEnd(0xFF)
    Return()

    # Function_3_5BB end

    def Function_4_672(): pass

    label("Function_4_672")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_693")
    Call(0, 18)
    Return()

    label("loc_693")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A5")
    Call(0, 20)
    Return()

    label("loc_6A5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_829")

    ChrTalk(
        0xFE,
        (
            "Coincident with the\x01",
            "President's arrest, that\x01",
            "Huge Tree appeared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "With the barrier gone, we've got to\x01",
            "be on guard against the major\x01",
            "powers... We're in a difficult spot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe... This is getting\x01",
            "interesting, isn't it. As a weapons\x01",
            "merchant, this concerns me greatly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FHaha, how promising.\x01",
            "...You couldn't ask for\x01",
            "better circumstances.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_8E0")

    label("loc_829")


    ChrTalk(
        0xFE,
        (
            "Now that we're on guard\x01",
            "against the major powers,\x01",
            "I've gotten more requests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe... This is getting\x01",
            "interesting, isn't it. As a weapons\x01",
            "merchant, this concerns me greatly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E0")

    Jump("loc_2997")

    label("loc_8E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_D6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CB8")

    ChrTalk(
        0xFE,
        "Oh, you guys, huh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe... It's been a\x01",
            "while. You guys look\x01",
            "surprisingly well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FAshley, it's been a\x01",
            "while.\x02\x03",
            "#00012F...Or rather, it looks\x01",
            "like you're not fazed by\x01",
            "this situation at all.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A6C")

    ChrTalk(
        0x10A,
        (
            "#00600FShe's supporting the\x01",
            "police's underground\x01",
            "activities.\x02\x03",
            "#00603FIf you thought about the\x01",
            "possible situations,\x01",
            "this one isn't strange.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B0E")

    label("loc_A6C")


    ChrTalk(
        0xFE,
        (
            "Well, I vaguely\x01",
            "suspected a situation\x01",
            "like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Because I'm helping with Dudley and\x01",
            "the others' underground activities.\x01",
            "Isn't that a matter of course?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B0E")


    ChrTalk(
        0x102,
        "#00105FS-So that's how it is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FIt looks like civilians\x01",
            "are helping you too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FWell, you're used to\x01",
            "dealing with underground\x01",
            "organizations, aren't you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe, you said it.\x01",
            "Thanks to that, I can\x01",
            "earn a profit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...We're in the middle of\x01",
            "getting things ready in\x01",
            "case the worst happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm pulling all the good stuff\x01",
            "out of the warehouse. If needed,\x01",
            "you can negotiate with Jingo.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BE, 4)
    Jump("loc_D6A")

    label("loc_CB8")


    ChrTalk(
        0xFE,
        (
            "...We're in the middle of\x01",
            "getting things ready in\x01",
            "case the worst happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I'm pulling all the good stuff\x01",
            "out of the warehouse. If needed,\x01",
            "you can negotiate with Jingo.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D6A")

    Jump("loc_2997")

    label("loc_D6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_FF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F25")

    ChrTalk(
        0xFE,
        (
            "Crossbell independence,\x01",
            "huh... Hah, that bank had a\x01",
            "lot to do with it, I bet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Hehe, redhead. Careful,\x01",
            "alright? I smell the scent\x01",
            "of approaching war.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00301F...You said it. I can't\x01",
            "think the major powers\x01",
            "'ll remain silent...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hehe. As a weapons\x01",
            "merchant, my blood's\x01",
            "boiling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was thinking of leaving Crossbell,\x01",
            "but now that things are like this,\x01",
            "I'll have to stay here until the end.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FF2")

    label("loc_F25")


    ChrTalk(
        0xFE,
        (
            "I smell a battlefield nearby...\x01",
            "Hehe. As a weapons merchant, it\x01",
            "makes my blood boil.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I was thinking of leaving Crossbell,\x01",
            "but now that things are like this,\x01",
            "I'll have to stay here until the end.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FF2")

    Jump("loc_2997")

    label("loc_FF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_16BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1610")
    OP_4B(0xFE, 0xFF)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x0, 0)

    ChrTalk(
        0xFE,
        "Aah, the SSS, huh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "The attack the other\x01",
            "day... What do you guys\x01",
            "think of it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...Right.\x02\x03",
            "#00001FThere's a lot of things\x01",
            "we don't know at the\x01",
            "moment, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101FHowever, the fact that Red\x01",
            "Constellation caused the incident\x01",
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
            "Yeah, there's a rumor\x01",
            "like that already\x01",
            "spreading in the city.\x02",
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
            "It was tough fighting\x01",
            "against him... Looks like he\x01",
            "used that strange drug, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I wonder where he got his\x01",
            "hands on a drug that can turn\x01",
            "you into a monster like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10108FThere's that too...\x02\x03",
            "#10106FWe're continuing to investigate,\x01",
            "but no way he could have gotten\x01",
            "it has come to light...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh, so you guys are the\x01",
            "same. I hate how we know\x01",
            "absolutely nothing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Anyway, because of the public\x01",
            "order problem in the state after\x01",
            "the incident, business isn't bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I've been here a long\x01",
            "time, but for this to\x01",
            "happen to Downtown...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    ChrTalk(
        0xFE,
        (
            "...It'll be time to\x01",
            "leave before long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FAshley...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10303F...Well, maybe it can't\x01",
            "be helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00300FI'm sure you've got\x01",
            "connections...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, I haven't made up\x01",
            "my mind yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's Jingo, too.\x01",
            "She'll need to decide\x01",
            "her future before long.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    OP_4C(0xFE, 0xFF)
    SetScenarioFlags(0x18D, 6)
    Jump("loc_16B9")

    label("loc_1610")


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
            "With all these unknown\x01",
            "things, Jingo is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There's Jingo, too.\x01",
            "She'll need to decide\x01",
            "her future before long.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16B9")

    Jump("loc_2997")

    label("loc_16BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1791")

    ChrTalk(
        0xFE,
        (
            "If you guys are going to\x01",
            "tangle with those dangerous\x01",
            "guys, be plenty careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I think you understand already, but\x01",
            "I'll tell you anyway: You'll get beat\x01",
            "if you go in without firm resolve.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2997")

    label("loc_1791")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_185E")

    ChrTalk(
        0xFE,
        (
            "It's gotten a little harder\x01",
            "to get products in after\x01",
            "the trade conference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard the major powers have started\x01",
            "regulating things behind the scenes.\x01",
            "I wish they'd give me a break.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2997")

    label("loc_185E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1AD4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19EB")

    ChrTalk(
        0xFE,
        (
            "Come to think of it, I heard remnants of the\x01",
            ""Anti-Immigration League" that attacked the\x01",
            "trade conference were captured yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard there was a disturbance\x01",
            "with Heiyue aboard the train, but I\x01",
            "wish it could be a little quieter.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x81, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_19BC")

    ChrTalk(
        0x101,
        (
            "#00012F(That's Ashley for you.\x01",
            "She hears everything so\x01",
            "quickly.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19E3")

    label("loc_19BC")


    ChrTalk(
        0x101,
        (
            "#00005F(So that happened,\x01",
            "huh...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19E3")

    SetScenarioFlags(0x0, 0)
    Jump("loc_1ACF")

    label("loc_19EB")


    ChrTalk(
        0xFE,
        (
            "I heard the remnants of the "Anti-\x01",
            "Immigration League" that attacked the\x01",
            "trade conference were captured yesterday.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I heard there was a disturbance\x01",
            "with Heiyue aboard the train, but I\x01",
            "wish it could be a little quieter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ACF")

    Jump("loc_2997")

    label("loc_1AD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1B6C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AEF")
    Call(0, 10)
    Jump("loc_1B67")

    label("loc_1AEF")


    ChrTalk(
        0xFE,
        (
            "Even so, it's strangely\x01",
            "busy today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Good grief... Since when\x01",
            "did this place become a\x01",
            "squirts' gathering spot?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B67")

    Jump("loc_2997")

    label("loc_1B6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1B7A")
    Jump("loc_2997")

    label("loc_1B7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1C01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B95")
    Call(0, 5)
    Jump("loc_1BFC")

    label("loc_1B95")


    ChrTalk(
        0xFE,
        (
            "Now that I think about\x01",
            "it, we've gotten busier\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Good grief... I'm\x01",
            "already this old, huh.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BFC")

    Jump("loc_2997")

    label("loc_1C01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1E95")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 2)), scpexpr(EXPR_END)), "loc_1E01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D92")

    ChrTalk(
        0xFE,
        (
            "There was a noisy guy on the\x01",
            "roof, so I was thinking of\x01",
            "firing off a shell, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "There'd be a hole in the\x01",
            "roof, so I left him to\x01",
            "Jingo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FThere's no way we could\x01",
            "let gunfire in the city\x01",
            "pass, of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmph. I didn't do it,\x01",
            "did I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...But even so that\x01",
            "blondie... I feel like\x01",
            "I've seen him before...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, must be my\x01",
            "imagination.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1DFC")

    label("loc_1D92")


    ChrTalk(
        0xFE,
        (
            "...But even so that\x01",
            "blondie... I feel like\x01",
            "I've seen him before...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Hmm, must be my\x01",
            "imagination.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DFC")

    Jump("loc_1E90")

    label("loc_1E01")


    ChrTalk(
        0xFE,
        (
            "The VIPs from each\x01",
            "country are all in\x01",
            "Crossbell, huh...\x02",
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

    label("loc_1E90")

    Jump("loc_2997")

    label("loc_1E95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_21AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14D, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20F2")
    OP_4B(0xFE, 0xFF)

    ChrTalk(
        0xFE,
        "Oh, if it isn't redhead.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Looks like you've\x01",
            "returned to the Support\x01",
            "Section.\x02",
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
            "Hah, my bad. We're an insignificant\x01",
            "operation, so we don't have time to\x01",
            "care about outside appearances.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "By the way, in Back\x01",
            "Street...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "...Yeah, looks like it. If you poked\x01",
            "your nose in there carelessly, it'd\x01",
            "only make things worse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00303F(...Hah. Based on this, it you\x01",
            "must've looked into my relationship\x01",
            "with Red Constellation.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00101F(I wonder just how much\x01",
            "she knows...)\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xFE, 0xFF)
    SetScenarioFlags(0x14D, 4)
    Jump("loc_21A7")

    label("loc_20F2")


    ChrTalk(
        0xFE,
        (
            "But because of that trade conference\x01",
            "or whatever, they've got officers\x01",
            "they don't normally here today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Oh brother... If they\x01",
            "come here, it'll be a\x01",
            "pain dealing with them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21A7")

    Jump("loc_2997")

    label("loc_21AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_262D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_250B")
    OP_4B(0xFE, 0xFF)

    ChrTalk(
        0xFE,
        (
            "Come to think of it,\x01",
            "guys... Where's shorty\x01",
            "and redhead?\x02",
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
            "#00000FYeah... She means Tio\x01",
            "and Randy.\x02\x03",
            "#00003FThey're not back yet\x01",
            "from their respective\x01",
            "assignments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FYes. It seems we're\x01",
            "meeting up with them\x01",
            "later.\x02",
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
            "rehabilitation training.\x02",
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
        "#00005FW-Why do you know that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10302FHehe. She's just showing\x01",
            "off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, when you run a\x01",
            "shop like mine, you get\x01",
            "to know these things.\x02",
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
        "#00105FAshley?\x02",
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
            "Well, if you're working\x01",
            "hard, that's good\x01",
            "enough.\x02",
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
    Jump("loc_2628")

    label("loc_250B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25EC")

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
            "I'm not certain of the\x01",
            "information anyway, and I've\x01",
            "no obligation to tell you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Well, you should try to\x01",
            "find out the rest on\x01",
            "your own.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2628")

    label("loc_25EC")


    ChrTalk(
        0xFE,
        (
            "Well, you should try to\x01",
            "find out the rest on\x01",
            "your own.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2628")

    Jump("loc_2997")

    label("loc_262D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2997")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_290F")
    OP_4B(0xFE, 0xFF)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x0, 500)

    ChrTalk(
        0xFE,
        (
            "Oh, if it isn't the\x01",
            "Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "I haven't seen you guys\x01",
            "in quite a while, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FAha, nice to see you\x01",
            "again as well.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x105, 500)

    ChrTalk(
        0xFE,
        (
            "Heh, I heard the rumors\x01",
            "but I never thought I'd\x01",
            "see you here.\x02",
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
            "#10304FWell, I just felt like\x01",
            "it.\x02\x03",
            "#10302FNext time, I'd like to\x01",
            "chat over drinks at\x01",
            "Trinity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        "Humph. Well whatever.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "So then? What do you\x01",
            "need?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "That Revache auction was\x01",
            "taken care of, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(She knew that much\x01",
            "already, huh...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FWell, we didn't came for\x01",
            "anything in particular today.\x01",
            "Sorry for bothering you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xFE,
        (
            "Is that so. Well, feel\x01",
            "free to look around.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x0, 0x0)
    OP_4C(0xFE, 0xFF)
    SetScenarioFlags(0x137, 5)
    Jump("loc_2997")

    label("loc_290F")

    TurnDirection(0xFE, 0x105, 0)

    ChrTalk(
        0xFE,
        (
            "But Wazy, I can't\x01",
            "believe you joined the\x01",
            "Special Support Section.\x02",
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

    label("loc_2997")

    TalkEnd(0xFE)
    Return()

    # Function_4_672 end

    def Function_5_299B(): pass

    label("Function_5_299B")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    TurnDirection(0x8, 0x9, 0)

    ChrTalk(
        0x8,
        (
            "Oh, Jingo. Do you remember\x01",
            "what I did with the grenades\x01",
            "you brought in yesterday?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I think I put them\x01",
            "somewhere around here,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 0)

    ChrTalk(
        0x9,
        "Mom, do you remember?\x02",
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
            "Thanks, Jingo. You're\x01",
            "good at this.\x02",
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
            "#00006F(Moving grenades, like\x01",
            "it's a normal\x01",
            "conversation...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00200F(It's usual for them.)\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BD0")
    OP_4C(0x9, 0xFF)

    label("loc_2BD0")

    OP_4C(0x8, 0xFF)
    OP_93(0x8, 0x87, 0x0)
    OP_93(0x9, 0xE1, 0x0)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    Return()

    # Function_5_299B end

    def Function_6_2BF3(): pass

    label("Function_6_2BF3")

    Call(0, 7)
    Return()

    # Function_6_2BF3 end

    def Function_7_2BF7(): pass

    label("Function_7_2BF7")

    TalkBegin(0x9)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2C0E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3ED7")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                   # 0
            "Exchange (Weapon)\x01",      # 1
            "Exchange (Quartz)\x01",      # 2
            "Exchange (Other)\x01",       # 3
            "Cancel\x01",                 # 4
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2C9A")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2C9A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CBA")
    OP_AF(0x8C)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3ED2")

    label("loc_2CBA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CDA")
    OP_AF(0x96)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3ED2")

    label("loc_2CDA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D77")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2D26")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2FB, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AF(0xA3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2FB, 0x0)"), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2D21")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D1E")
    ClearScenarioFlags(0x0, 1)

    label("loc_2D1E")

    SetScenarioFlags(0x189, 5)

    label("loc_2D21")

    Jump("loc_2D68")

    label("loc_2D26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2D36")
    OP_AF(0xA2)
    Jump("loc_2D68")

    label("loc_2D36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2D46")
    OP_AF(0xA1)
    Jump("loc_2D68")

    label("loc_2D46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2D56")
    OP_AF(0xA1)
    Jump("loc_2D68")

    label("loc_2D56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2D66")
    OP_AF(0xA0)
    Jump("loc_2D68")

    label("loc_2D66")

    OP_AF(0xA0)

    label("loc_2D68")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3ED2")

    label("loc_2D77")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D8B")
    Jump("loc_3ED2")

    label("loc_2D8B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3ED2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3259")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 5)), scpexpr(EXPR_END)), "loc_2F87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F13")

    ChrTalk(
        0x9,
        (
            "Ooh... As expected,\x01",
            "Kagemaru goods are\x01",
            "stylish and gallant, huh!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Oh yeah, there's a katana\x01",
            "in the warehouse. It'd be\x01",
            "great if you took it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Vaan and Roser wear\x01",
            "these and sword fight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FT-That's a little beyond\x01",
            "the category of child's\x01",
            "play.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200FThe Kagemaru character\x01",
            "too is conveyed slightly\x01",
            "wrong.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2F82")

    label("loc_2F13")


    ChrTalk(
        0x9,
        (
            "As expected, Kagemaru\x01",
            "goods are stylish and\x01",
            "gallant, huh!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Vaan and Roser wear\x01",
            "these and sword fight.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F82")

    Jump("loc_3254")

    label("loc_2F87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3068")

    ChrTalk(
        0x9,
        (
            "Customers, do you know a\x01",
            "black cat?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FA black cat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00200F...You must be talking\x01",
            "about "Kagemaru".\x02",
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
        (
            "Jingo's looking for his\x01",
            "clothes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Get a lot and bring me\x01",
            "them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x189, 6)
    Jump("loc_3254")

    label("loc_3068")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31C5")

    ChrTalk(
        0x9,
        (
            "Customers, did you see\x01",
            "that huuuge tree?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Amazing, isn't it. If you\x01",
            "cut it down, how many guns\x01",
            "do you think it'd make?\x02",
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
        (
            "#00106F(A dangerous child, as\x01",
            "always...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3254")

    label("loc_31C5")


    ChrTalk(
        0x9,
        (
            "If you cut down that\x01",
            "tree, I wonder how many\x01",
            "guns it'd make.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Nishishi... Though maybe\x01",
            "it'd even be hard with\x01",
            "lots of Imperial tanks.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3254")

    Jump("loc_3ED2")

    label("loc_3259")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_33DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33A5")

    ChrTalk(
        0x9,
        "Oh, customers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It's dangerous out\x01",
            "there. Buy some\x01",
            "protection!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you want to blow up the\x01",
            "armors outside, we might\x01",
            "have grenades for that.\x02",
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
            "#00006F(Those are probably for\x01",
            "self-defense...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_33D9")

    label("loc_33A5")


    ChrTalk(
        0x9,
        (
            "It's dangerous out\x01",
            "there. Buy some\x01",
            "protection!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33D9")

    Jump("loc_3ED2")

    label("loc_33DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_3460")

    ChrTalk(
        0x9,
        (
            "I talked it over with\x01",
            "mom, and we decided to\x01",
            "stay in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you want something,\x01",
            "just say the word.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3ED2")

    label("loc_3460")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_34F0")

    ChrTalk(
        0x9,
        (
            "As usual, everyone's\x01",
            "busy with the\x01",
            "reconstruction work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Give Jingo and mom some\x01",
            "credit. We help too\x01",
            "every now and then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3ED2")

    label("loc_34F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3652")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35EF")

    ChrTalk(
        0x9,
        "*fuwaah*, so sleepy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "An urgent job came in last night, and\x01",
            "mom banged around in the warehouse so\x01",
            "I didn't get much sleep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "But, mom gets urgent\x01",
            "orders like that often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Was mom that close with\x01",
            "that customer?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_364D")

    label("loc_35EF")


    ChrTalk(
        0x9,
        (
            "But, mom gets urgent\x01",
            "orders like that often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Was mom that close with\x01",
            "that customer?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_364D")

    Jump("loc_3ED2")

    label("loc_3652")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_36CD")

    ChrTalk(
        0x9,
        (
            "Hmm, it's still\x01",
            "drizzling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If it has to rain, it\x01",
            "might as well come pouring\x01",
            "down and be over with.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3ED2")

    label("loc_36CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_375C")
    OP_93(0x9, 0x10E, 0x0)

    ChrTalk(
        0x9,
        (
            "Well, they learn from\x01",
            "experience, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Mom slapped my hand before,\x01",
            "so it's not like I'm going\x01",
            "to forget, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3ED2")

    label("loc_375C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_37D7")

    ChrTalk(
        0x9,
        (
            "Hey customers. You don't\x01",
            "have to worry about\x01",
            "this, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We've got good stuff\x01",
            "today. Let's exchange!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3ED2")

    label("loc_37D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_38B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3876")

    ChrTalk(
        0x9,
        "Mom went to drink.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I've been busy sorting\x01",
            "inventory since morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "She says she's having a\x01",
            "little drink as a\x01",
            "reward.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_38B4")

    label("loc_3876")


    ChrTalk(
        0x9,
        (
            "Mom is strict with our\x01",
            "customers, but she's\x01",
            "sweet to me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38B4")

    Jump("loc_3ED2")

    label("loc_38B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3947")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38D4")
    Call(0, 5)
    Jump("loc_3942")

    label("loc_38D4")

    TurnDirection(0x9, 0x0, 0)

    ChrTalk(
        0x9,
        (
            "She sometimes forgets\x01",
            "stuff, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Nishishi... I always\x01",
            "knew it'd be bad if I\x01",
            "wasn't here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3942")

    Jump("loc_3ED2")

    label("loc_3947")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3AE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 2)), scpexpr(EXPR_END)), "loc_39EB")

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
            "It would have been\x01",
            "better if I kicked him\x01",
            "harder, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AE3")

    label("loc_39EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AA1")

    ChrTalk(
        0x9,
        (
            "We rarely close up shop, but mom\x01",
            "and I are going to close and go\x01",
            "see the unveiling ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "That building really is\x01",
            "ridiculously big. Jingo\x01",
            "was shocked.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3AE3")

    label("loc_3AA1")


    ChrTalk(
        0x9,
        (
            "That building really is\x01",
            "ridiculously big. Jingo\x01",
            "was shocked.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AE3")

    Jump("loc_3ED2")

    label("loc_3AE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3BF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B90")

    ChrTalk(
        0x9,
        (
            "A new sister came to\x01",
            "read us a book, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It seems like she always\x01",
            "gives us other books for\x01",
            "homework.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "I kind of hate her...\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3BF3")

    label("loc_3B90")


    ChrTalk(
        0x9,
        (
            "I kind of hate that\x01",
            "sister...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Well, since she brought\x01",
            "it... I guess I'll read\x01",
            "this book.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BF3")

    Jump("loc_3ED2")

    label("loc_3BF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3E0F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C13")
    Call(0, 8)
    Jump("loc_3E0A")

    label("loc_3C13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D8A")

    ChrTalk(
        0x9,
        (
            "Damn you rain. Damp,\x01",
            "humid, wet, gloomy... So\x01",
            "depressing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you fire an orbal gun\x01",
            "into a rain cloud, will\x01",
            "it disappear?\x02",
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
            "#00106F(Hmm. What's with this\x01",
            "kid...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106F(Yes... I don't have\x01",
            "anything to say back to\x01",
            "her.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3E0A")

    label("loc_3D8A")


    ChrTalk(
        0x9,
        (
            "Damn you rain. Damp,\x01",
            "humid, wet, gloomy... So\x01",
            "depressing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I wonder if you can blow\x01",
            "away rain clouds with\x01",
            "orbal bombs?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E0A")

    Jump("loc_3ED2")

    label("loc_3E0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3ED2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E2A")
    Call(0, 8)
    Jump("loc_3ED2")

    label("loc_3E2A")


    ChrTalk(
        0x9,
        (
            "I think you already\x01",
            "know, but I trade\x01",
            "products with customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We've got medicine, quartz,\x01",
            "accessories... and other stuff\x01",
            "ready for you, so come take a look.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3ED2")

    Jump("loc_2C0E")

    label("loc_3ED7")

    TalkEnd(0x9)
    Return()

    # Function_7_2BF7 end

    def Function_8_3EDB(): pass

    label("Function_8_3EDB")


    ChrTalk(
        0x9,
        (
            "Oh, customers. It's been\x01",
            "a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We can't sell you\x01",
            "weapons, but want to\x01",
            "trade?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "We've got a good\x01",
            "selection of stuff for\x01",
            "the general public too.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FA0")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_3FA0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FC6")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_3FC6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FEC")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_3FEC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4012")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_4012")

    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006FA-A dangerous remark, as\x01",
            "always.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#10106FUmm, is it really all\x01",
            "right for your store to\x01",
            "deal in those?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00100FW-Well on the surface,\x01",
            "those goods don't seem\x01",
            "illegal...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHaha. Then I guess\x01",
            "there's no problem,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Ah, also. We've been\x01",
            "doing more business\x01",
            "lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "If you've got good\x01",
            "stuff, why bring some of\x01",
            "it here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'll trade you some\x01",
            "equally good stuff for\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FHaha, got it. We'll be\x01",
            "using your services once\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x137, 7)
    Return()

    # Function_8_3EDB end

    def Function_9_41F5(): pass

    label("Function_9_41F5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_420A")
    Call(0, 10)
    Jump("loc_4251")

    label("loc_420A")


    ChrTalk(
        0xFE,
        (
            "A h-hundred thousand\x01",
            "mira, huh... I've never\x01",
            "even seen that much.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4251")

    TalkEnd(0xFE)
    Return()

    # Function_9_41F5 end

    def Function_10_4255(): pass

    label("Function_10_4255")

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
            "Watch this. If you hold\x01",
            "it to your ear, it\x01",
            "becomes a communicator.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "Y-You're right. It's\x01",
            "really true.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "And the police and the\x01",
            "bracers... and now Wazy\x01",
            "too have been using them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "By the way, Ashley. How\x01",
            "much would it be to get one\x01",
            "of these on the up-and-up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hmm? Well they're all\x01",
            "made to order. 100,000\x01",
            "mira, minimum, I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "But if you're interested\x01",
            "in one of my knock-offs,\x01",
            "I can be flexible...\x02",
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
        (
            "A h-hundred thousand\x01",
            "mira...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "A h-hundred thousand\x01",
            "one-mira chocolates...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Haha, I got a good\x01",
            "reaction out of you\x01",
            "guys, didn't I.\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x16E, 5)
    Return()

    # Function_10_4255 end

    def Function_11_4501(): pass

    label("Function_11_4501")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4516")
    Call(0, 10)
    Jump("loc_455E")

    label("loc_4516")


    ChrTalk(
        0xFE,
        (
            "A h-hundred thousand\x01",
            "one-mira chocolates...\x01",
            "H-How many is 100,000?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_455E")

    TalkEnd(0xFE)
    Return()

    # Function_11_4501 end

    def Function_12_4562(): pass

    label("Function_12_4562")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_45B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4580")
    Call(0, 14)
    Jump("loc_45AE")

    label("loc_4580")


    ChrTalk(
        0xFE,
        (
            "Crap, Jingo's mom is as\x01",
            "scary as always.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45AE")

    Jump("loc_45BF")

    label("loc_45B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_45BF")
    Call(0, 15)

    label("loc_45BF")

    TalkEnd(0xFE)
    Return()

    # Function_12_4562 end

    def Function_13_45C3(): pass

    label("Function_13_45C3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4616")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45E1")
    Call(0, 14)
    Jump("loc_4611")

    label("loc_45E1")


    ChrTalk(
        0xFE,
        (
            "*chuckle*... Another\x01",
            "failed operation, eh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4611")

    Jump("loc_4622")

    label("loc_4616")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4622")
    Call(0, 15)

    label("loc_4622")

    TalkEnd(0xFE)
    Return()

    # Function_13_45C3 end

    def Function_14_4626(): pass

    label("Function_14_4626")

    OP_4B(0x8, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)

    ChrTalk(
        0xC,
        (
            "Woah, so this is an\x01",
            "orbal gun, huh. How\x01",
            "cool!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "Hey Vaan. Can you roast\x01",
            "meat with that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hmm. Well I guess you\x01",
            "could. Nihihi, I think\x01",
            "I'll test it out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "...Hey kids.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xC, 0)

    ChrTalk(
        0x8,
        (
            "Don't touch the\x01",
            "merchandise around here.\x01",
            "(*glare*)\x02",
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
            "*chuckle*... Jingo's mom\x01",
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

    # Function_14_4626 end

    def Function_15_4782(): pass

    label("Function_15_4782")

    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_489D")

    ChrTalk(
        0xC,
        (
            "Hey Jingo. We came to\x01",
            "visit.\x02",
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
        "Oh, you guys. Got mira?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "Hyahaha, I did but spent\x01",
            "the last of it\x01",
            "yesterday.\x02",
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
            "*sigh*... As usual, you\x01",
            "never plan anything, do\x01",
            "you guys.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4940")

    label("loc_489D")


    ChrTalk(
        0xC,
        (
            "Stop being impertinent\x01",
            "and give us somethin',\x01",
            "Jingo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hmm? You guys still look\x01",
            "pretty good right now,\x01",
            "so no way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "*chuckle*... You're a\x01",
            "demon, Jingo.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4940")

    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    Return()

    # Function_15_4782 end

    def Function_16_494D(): pass

    label("Function_16_494D")

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
            "suspicious air, like\x01",
            "always.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#6P#00108FLooks like Jingo's\x01",
            "looking after the store,\x01",
            "as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10103FThis store is one of the\x01",
            "black markets in Crossbell\x01",
            "City, huh.\x02\x03",
            "#10101FThere's rumors within the CGF\x01",
            "about this place dealing with\x01",
            "weapons and ammunition...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FWell, they're honest\x01",
            "folks compared to most\x01",
            "stores like this.\x02\x03",
            "#10300FThe owner is quite the\x01",
            "character, though.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4BC5():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4BC5)
    Sleep(50)

    def lambda_4BD5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4BD5)
    Sleep(50)
    TurnDirection(0x102, 0x105, 500)

    ChrTalk(
        0x101,
        (
            "#5P#00003FIt sure seems that\x01",
            "way...\x02\x03",
            "#00001FAnyway, if we have\x01",
            "business here, let's\x01",
            "finish it quickly.\x02",
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
            "※At Exchange Shop Neinvalli,\x01",
            "you can exchange specific\x01",
            "items for high rarity ones.\x02\x03",
            "※To make an exchange, talk\x01",
            "to Jingo at the counter and\x01",
            "select [Trade].\x07\x00\x02",
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

    # Function_16_494D end

    def Function_17_4D41(): pass

    label("Function_17_4D41")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x10000000)
    SetChrPos(0x101, -600, 0, 1800, 0)
    SetChrPos(0x102, 600, 0, 1800, 0)
    SetChrPos(0x109, 900, 0, 700, 0)
    SetChrPos(0x105, -900, 0, 700, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x138, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5112")
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
            "suspicious air, like\x01",
            "always.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x9, 500)
    Sleep(300)

    ChrTalk(
        0x102,
        (
            "#6P#00108FLooks like Jingo's\x01",
            "looking after the store,\x01",
            "as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10103FThis store is one of the\x01",
            "black markets in Crossbell\x01",
            "City, huh.\x02\x03",
            "#10101FThere's rumors within the CGF\x01",
            "about this place dealing with\x01",
            "weapons and ammunition...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#12P#10304FWell, they're honest\x01",
            "folks compared to most\x01",
            "stores like this.\x02\x03",
            "#10300FThe owner is quite the\x01",
            "character, though.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4FC3():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4FC3)
    Sleep(50)

    def lambda_4FD3():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4FD3)
    Sleep(50)
    TurnDirection(0x102, 0x105, 500)

    ChrTalk(
        0x101,
        (
            "#5P#00003FIt sure seems that\x01",
            "way...\x02\x03",
            "#00001FAnyway, let's ask Ashley\x01",
            "about that man.\x02",
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
            "※At Exchange Shop Neinvalli,\x01",
            "you can exchange specific\x01",
            "items for high rarity ones.\x02\x03",
            "※To make an exchange, talk\x01",
            "to Jingo at the counter and\x01",
            "select [Trade].\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_5233")

    label("loc_5112")

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
            "#12P#00106FThat's right. No matter how\x01",
            "many times I come here, I\x01",
            "can't get used to it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    ChrTalk(
        0x102,
        (
            "#11P#00101FAnyway, let's ask Ashley\x01",
            "about that man.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()

    label("loc_5233")

    SetChrPos(0x0, 0, 0, 1000, 0)
    SetScenarioFlags(0x138, 5)
    SetScenarioFlags(0x128, 3)
    EventEnd(0x5)
    Return()

    # Function_17_4D41 end

    def Function_18_524D(): pass

    label("Function_18_524D")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5590")

    ChrTalk(
        0x8,
        (
            "#5POh, if it isn't the\x01",
            "Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI haven't seen you guys\x01",
            "in quite a while, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012FAha, nice to see you\x01",
            "again as well.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x105, 500)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#5PHeh, I heard the rumors\x01",
            "but I never thought I'd\x01",
            "see you here.\x02",
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
            "#10304FWell, I just felt like\x01",
            "it.\x02\x03",
            "#10302FNext time, I'd like to\x01",
            "chat over drinks at\x01",
            "Trinity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PHumph. Well whatever.\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#5PSo then? What do you\x01",
            "need?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThat Revache auction was\x01",
            "taken care of, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006F(She knew that much\x01",
            "already, huh...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103FActually, we have a\x01",
            "question for you,\x01",
            "Ashley.\x02\x03",
            "#00100FAs a former arms dealer.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x137, 5)
    Jump("loc_5641")

    label("loc_5590")


    ChrTalk(
        0x8,
        (
            "#5POh, the Special Support\x01",
            "Section, huh?\x02",
        )
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
            "question for you,\x01",
            "Ashley.\x02\x03",
            "#00100FAs a former arms dealer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5641")

    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x8,
        (
            "#5PHmm? And what would that\x01",
            "be?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAbout the fact that Cao\x01",
            "and his pals have\x01",
            "started making moves?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00003FSo you already know,\x01",
            "huh.\x02\x03",
            "#00001FThough this is probably\x01",
            "a bit different...\x02",
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
        (
            "#5PA huge, one-eyed,\x01",
            "redheaded... man?\x02",
        )
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
            "It's likely that he's\x01",
            "connected to the\x01",
            "underworld somehow...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThere are a few people\x01",
            "who fit that\x01",
            "description.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PBut, if it's someone who\x01",
            "would come to Crossbell\x01",
            "in these circumstances...\x02",
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
        "#6P#00108FU-Umm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10305FWhoa, is he that\x01",
            "dangerous?\x02",
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
            "#5PThere's no way in hell\x01",
            "you'll be able to match\x01",
            "him in combat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#6P#00101FThat bad...?\x02",
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
        "#5PHehe, I wonder.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIf it really is him, I\x01",
            "hung out with him for a\x01",
            "time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI can't just speak\x01",
            "willy-nilly about him.\x02",
        )
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
            "#12P#00006F─Whether he's a Jaeger\x01",
            "or not, if he's a\x01",
            "terrorist, we must act.\x02\x03",
            "#00003FEven in Crossbell there\x01",
            "are laws against acts of\x01",
            "terrorism.\x02\x03",
            "#00013FCan't you even give us a\x01",
            "bare minimum of\x01",
            "information?\x02",
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
        "#5PHmhm, not bad.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P─-Guy's younger brother,\x01",
            "huh? You've got a good\x01",
            "head on your shoulders.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00005FAshley, you knew my\x01",
            "brother!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PDudley shows his face\x01",
            "around here every once\x01",
            "in a while these days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PBut back then, it was that\x01",
            "unpredictable detective that\x01",
            "came to canvass Downtown.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P....We lost an\x01",
            "interesting one, didn't\x01",
            "we?\x02",
        )
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
            "#5PWell, for the sake of\x01",
            "that idiot, I'll give\x01",
            "you this much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIn the worst case\x01",
            "scenario, he's definitely\x01",
            "not a terrorist.\x02",
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
        "#12P#10108FM-man-eating tiger...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10306FOh my... Sounds like\x01",
            "someone we don't want to\x01",
            "mess with.\x02",
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
            "#5PHe was alone, right? The\x01",
            "guy you saw?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PBecause the guy I'm\x01",
            "thinking of is usually with\x01",
            "subordinates or companions.\x02",
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
            "#6P#00101FIn that case... Is it\x01",
            "someone related to the\x01",
            "military?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHehe, that's as much as\x01",
            "I can give.\x02",
        )
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
        (
            "#6P#00104FThank you for the\x01",
            "information.\x02",
        )
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

    # Function_18_524D end

    def Function_19_5FFF(): pass

    label("Function_19_5FFF")

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
        "#5PHmm. Still raining, huh?\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x13B, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#11POh right, mom. Can we\x01",
            "unpack the goods we got\x01",
            "yesterday?\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x87, 0x0)

    ChrTalk(
        0x8,
        (
            "Sure, but no need to\x01",
            "rush when the weather's\x01",
            "like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "...More importantly,\x01",
            "Jingo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Did you see anyone weird\x01",
            "when you went out\x01",
            "yesterday?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PWeirdos? Aren't there\x01",
            "plenty of those?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PLike a young man\x01",
            "vacationing or a sister\x01",
            "buying lots of bread.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#11PAnd that Wazy is a\x01",
            "weirdo too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I see. Well, that's fine\x01",
            "then.\x02",
        )
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
        (
            "#5P(...Maybe I'm\x01",
            "overthinking it.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P(If he came to the city,\x01",
            "he'd bring his daughter\x01",
            "as well.)\x02",
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

    # Function_19_5FFF end

    def Function_20_633C(): pass

    label("Function_20_633C")

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
            "#5PI thought you might stop\x01",
            "by around now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00001FThen that means... Randy\x01",
            "stopped by?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYeah, he called me yesterday\x01",
            "evening and picked up some\x01",
            "things early this morning.\x02",
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
            "#6P#00101FThen... What did Randy\x01",
            "end up buying?\x02",
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
            "#5PNo it wasn't anything\x01",
            "quite so respectable.\x02",
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
            "#5PHe cleaned me out,\x01",
            "actually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PAlso, an unregistered\x01",
            "ENIGMA Ⅱ.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00006FI see...\x02\x03",
            "#00008F...He's nothing if not\x01",
            "thorough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00206FYes... If he's using an\x01",
            "unregistered ENIGMA, we\x01",
            "won't know its number.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#12P#10105FBut, he didn't buy any\x01",
            "actual weapons?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PYeah, well I was planning on\x01",
            "dealing in powerful orbal\x01",
            "and gunpowder rifles, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PIt seems that would rub\x01",
            "the Red Constellation\x01",
            "leader the wrong way.\x02",
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
        "#12P#00011FAshley...\x02",
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
            "#5PHa, of course.\x01",
            "Information is life,\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PHe tried to scare the\x01",
            "hell out of me, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5POgre Rosso and Bloody\x01",
            "Shirley are the real\x01",
            "monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PThat half-wit former\x01",
            "jaeger will surely get\x01",
            "himself killed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#12P#00201F...We won't let that\x01",
            "happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00013FWe're here to try to\x01",
            "stop that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x105,
        (
            "#10304FHaha, it's been that way\x01",
            "for a while.\x02\x03",
            "#10302FBut it looks like\x01",
            "provoking him won't\x01",
            "work?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5PYeah, looks that way.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PWell, if that idiot kicks\x01",
            "the bucket, don't come\x01",
            "cryin' to me, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5PI'd hate to lose a\x01",
            "regular customer. Save\x01",
            "him for me, will ya?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#12P#10101FRight!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#6P#00103FThank you for all your\x01",
            "help.\x02",
        )
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

    # Function_20_633C end

    def Function_21_6B65(): pass

    label("Function_21_6B65")

    EventBegin(0x1)
    OP_4B(0x9, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6C34")

    ChrTalk(
        0x9,
        (
            "Are you heading to the\x01",
            "warehouse?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Hmm... Well, if you're\x01",
            "customers...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Don't touch anything\x01",
            "weird. You might die.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F...Thanks for your\x01",
            "consideration.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x189, 7)
    ModifyEventFlags(0, 0, 0x80)
    Jump("loc_6D53")

    label("loc_6C34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CE2")

    ChrTalk(
        0x9,
        (
            "...Hey, customer. Don't\x01",
            "try to deceive the eyes\x01",
            "of Jingo.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Basement warehouse entry is\x01",
            "permitted for staff only. If\x01",
            "you're buying, right this way!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6D53")

    label("loc_6CE2")


    ChrTalk(
        0x9,
        (
            "Hey, customer? Did you\x01",
            "hear Jingo?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "I'm telling you not to go\x01",
            "down there!! If you're\x01",
            "buying, this way!!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D53")

    Sleep(50)
    SetChrPos(0x0, 9940, 0, 11910, 180)
    OP_4C(0x9, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_21_6B65 end

    SaveToFile()

Try(main)
