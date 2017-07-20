from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t0530.bin",                # FileName
        "t0530",                    # MapName
        "t0530",                    # Location
        0x0040,                     # MapIndex
        "ed7121",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x18,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 64, 0, 1, 0, 2],
    )

    BuildStringList((
        "t0530",                  # 0
        "Bekkarai",             # 1
        "Kimi",                 # 2
        "Harold",               # 3
    ))

    AddCharChip((
        "chr/ch23400.itc",                   # 00
        "chr/ch23900.itc",                   # 01
        "chr/ch09300.itc",                   # 02
    ))

    DeclNpc(4294967167, 0,       3640,    180,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(4294962766, 0,       4500,    320,  261,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(4294963896, 0,       3559,    315,  389,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)

    DeclActor(4294967256, 0,       2120,    1000,    4294967166, 1500,    3640,    0x007E, 0,  3,  0x0000)

    ChipFrameInfo(312, 0)                                        # 0

    ScpFunction((
        "Function_0_138",          # 00, 0
        "Function_1_1F0",          # 01, 1
        "Function_2_309",          # 02, 2
        "Function_3_342",          # 03, 3
        "Function_4_346",          # 04, 4
        "Function_5_1422",         # 05, 5
        "Function_6_1B22",         # 06, 6
        "Function_7_1C29",         # 07, 7
    ))


    def Function_0_138(): pass

    label("Function_0_138")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_178"),
        (1, "loc_184"),
        (2, "loc_190"),
        (3, "loc_19C"),
        (4, "loc_1A8"),
        (5, "loc_1B4"),
        (6, "loc_1C0"),
        (SWITCH_DEFAULT, "loc_1CC"),
    )


    label("loc_178")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_184")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_190")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_19C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1A8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1B4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1C0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1CC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1D8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1EF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1EF")

    Return()

    # Function_0_138 end

    def Function_1_1F0(): pass

    label("Function_1_1F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1FE")
    Jump("loc_308")

    label("loc_1FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_20C")
    Jump("loc_308")

    label("loc_20C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_21A")
    Jump("loc_308")

    label("loc_21A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_245")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 1000, 0, 1600, 315)
    TurnDirection(0x8, 0xA, 0)
    Jump("loc_308")

    label("loc_245")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_253")
    Jump("loc_308")

    label("loc_253")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_261")
    Jump("loc_308")

    label("loc_261")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_26F")
    Jump("loc_308")

    label("loc_26F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_282")
    SetChrFlags(0x9, 0x80)
    Jump("loc_308")

    label("loc_282")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_290")
    Jump("loc_308")

    label("loc_290")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2A3")
    SetChrFlags(0x9, 0x80)
    Jump("loc_308")

    label("loc_2A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_2B1")
    Jump("loc_308")

    label("loc_2B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2D5")
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x10)
    TurnDirection(0x9, 0xA, 0)
    SetChrFlags(0x9, 0x10)
    Jump("loc_308")

    label("loc_2D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2E3")
    Jump("loc_308")

    label("loc_2E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_2F1")
    Jump("loc_308")

    label("loc_2F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2FF")
    Jump("loc_308")

    label("loc_2FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_308")

    label("loc_308")

    Return()

    # Function_1_1F0 end

    def Function_2_309(): pass

    label("Function_2_309")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_31B")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_31B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_341")
    SetMapObjFrame(0xFF, "hikari_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_341")

    Return()

    # Function_2_309 end

    def Function_3_342(): pass

    label("Function_3_342")

    Call(0, 4)
    Return()

    # Function_3_342 end

    def Function_4_346(): pass

    label("Function_4_346")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_353")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_141E")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "talk\x01",          # 0
            "to shop\x01",      # 1
            "quit\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B1")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3B1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_401")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3D0")
    OP_AF(0x58)
    Jump("loc_3F2")

    label("loc_3D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3E0")
    OP_AF(0x57)
    Jump("loc_3F2")

    label("loc_3E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3F0")
    OP_AF(0x56)
    Jump("loc_3F2")

    label("loc_3F0")

    OP_AF(0x55)

    label("loc_3F2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1419")

    label("loc_401")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_415")
    Jump("loc_1419")

    label("loc_415")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_42D")
    TalkEnd(0x8)
    Return()

    label("loc_42D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1419")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52A")

    ChrTalk(
        0x8,
        (
            "The mine is of Mainz residents\x01",
            "It is a pride itself that I can not yield.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In any abnormal situation,\x01",
            "As long as you do not forget your pride\x01",
            "I am sure to get over it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Something that can not be given off,\x01",
            "There must be something for you, too.\x01",
            "Definitely do not forget it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_5C0")

    label("loc_52A")


    ChrTalk(
        0x8,
        (
            "In any abnormal situation,\x01",
            "As long as you do not forget your pride\x01",
            "I am sure to get over it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Something that can not be given off,\x01",
            "There must be something for you, too.\x01",
            "Definitely do not forget it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C0")

    Jump("loc_1419")

    label("loc_5C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_772")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D4")

    ChrTalk(
        0x8,
        (
            "I do not have much learning,\x01",
            "It is an invalid declaration\x01",
            "I do not understand well …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Early place Kimi and the bastards\x01",
            "In a world where you can live with peace of mind\x01",
            "I want you to become it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "…… To that end resistance\x01",
            "The reason for leaving dangerous things is that,\x01",
            "It is a miserable story.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_76D")

    label("loc_6D4")


    ChrTalk(
        0x8,
        (
            "Dangerous things to resistance\x01",
            "It is miserable to leave it to me … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Kimi and the bastards\x01",
            "Even for the world that can live with peace of mind,\x01",
            "I want you to work hard.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_76D")

    Jump("loc_1419")

    label("loc_772")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_961")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D8")

    ChrTalk(
        0x8,
        (
            "Before starting resistance hunting,\x01",
            "The hunters down to the mayor's town\x01",
            "I heard that he came to greet us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Wonder what you're going through\x01",
            "\"Please be careful not to get out of town\"\x01",
            "He told me what he said.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To ours cooperating with resistance\x01",
            "I guess I was going to check it … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If there was present in place\x01",
            "In return of the occupation case\x01",
            "I did hit him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_95C")

    label("loc_8D8")


    ChrTalk(
        0x8,
        (
            "If you ask, the hunters will be on the mountain road tunnel\x01",
            "It seems that they have tried to landmines.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "If it was there\x01",
            "I definitely hit him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_95C")

    Jump("loc_1419")

    label("loc_961")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A7C")

    ChrTalk(
        0x8,
        (
            "They're in Mainz,\x01",
            "Because of the occupation of example hunters\x01",
            "It is still sinking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Because I am also a party\x01",
            "I understand the feeling of that … …\x01",
            "It does not start even if it sinks forever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Anyhow, it seems like me and miners\x01",
            "Only those who are fine are those of the handle,\x01",
            "Let 's keep everyone exciting.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B11")

    label("loc_A7C")


    ChrTalk(
        0x8,
        (
            "That hunter was terrible, but …\x01",
            "It does not start even if it sinks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "It seems like me and miners\x01",
            "Only those who are fine are those of the handle,\x01",
            "Let 's keep everyone exciting.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B11")

    Jump("loc_1419")

    label("loc_B16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_B86")

    ChrTalk(
        0x8,
        (
            "I got injured on my feet,\x01",
            "I also retired from the miners\x01",
            "It was such a rainy day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "…… Old wounds hurt pain.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1419")

    label("loc_B86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_CFA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C5C")

    ChrTalk(
        0x8,
        (
            "Kimi is today with Hoffman and this\x01",
            "You should play with the buddy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "…… I got few people in the same age,\x01",
            "It is nice to get along well ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In the future, going out with a relationship\x01",
            "I wonder what it's like to expand … ….?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CF5")

    label("loc_C5C")


    ChrTalk(
        0x8,
        (
            "Kimi with Hoffman and this bishop\x01",
            "In the future, things like mistakes\x01",
            "It can not be said that there is no … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "…… To Huffman's guy,\x01",
            "Do not mention kitchen nails.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CF5")

    Jump("loc_1419")

    label("loc_CFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_E61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DEE")

    ChrTalk(
        0x8,
        (
            "Anything, at a trade meeting this time\x01",
            "The story of national independence has been lifted\x01",
            "That's not it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The new mayor Sun, too,\x01",
            "I have some pretty things to think about.\x01",
            "Well, that's fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To pecopeco empire and the republic,\x01",
            "I have to stop at here.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E5C")

    label("loc_DEE")


    ChrTalk(
        0x8,
        "Independence of the country, it is quite fine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "We are also cross-\x01",
            "From now on will be more proud\x01",
            "I have to go live.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E5C")

    Jump("loc_1419")

    label("loc_E61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_102F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F82")

    ChrTalk(
        0x8,
        (
            "A little while ago, worried about Kimi too much\x01",
            "In the class of Sunday school\x01",
            "There are things that have broken into.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I have bothered the trouble at the time.\x01",
            "My strength#4REffortlessly#And other kids too\x01",
            "She seems to have made it faint ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To Kimi any more\x01",
            "It can not be a shame.\x01",
            "I have to try not to stop it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_102A")

    label("loc_F82")


    ChrTalk(
        0x8,
        (
            "A little while ago, worried about Kimi too much\x01",
            "In the class of Sunday school\x01",
            "There are things that have broken into.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "To Kimi any more\x01",
            "It can not be a shame.\x01",
            "I have to try not to stop it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_102A")

    Jump("loc_1419")

    label("loc_102F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_113B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10C9")

    ChrTalk(
        0x8,
        (
            "Oops, Harold's guy is\x01",
            "You seem to have come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "The ingredients purchased last time something\x01",
            "It is about time to get rid of it.\x01",
            "Well, it was exactly right.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1136")

    label("loc_10C9")


    ChrTalk(
        0x8,
        (
            "Harold 's guy,\x01",
            "With a good timing\x01",
            "You will come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Alright, this time for purchase price\x01",
            "Can you color it?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1136")

    Jump("loc_1419")

    label("loc_113B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_12D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1231")

    ChrTalk(
        0x8,
        (
            "I do not have to learn anymore.\x01",
            "I do not understand difficult things … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "In short it is a trade meeting,\x01",
            "The smart guys gathered\x01",
            "It's a place to talk a lot, do not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Young people for the future as well\x01",
            "By all means, good discussion\x01",
            "I want you to do it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12CF")

    label("loc_1231")


    ChrTalk(
        0x8,
        (
            "In short it is a trade meeting,\x01",
            "The smart guys gathered\x01",
            "It's a place to talk a lot, do not you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Young people for the future as well\x01",
            "By all means, good discussion\x01",
            "I want you to do it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12CF")

    Jump("loc_1419")

    label("loc_12D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_1419")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1394")

    ChrTalk(
        0x8,
        (
            "Recently, young miners\x01",
            "My face is getting better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Will you be able to do it ahead?\x01",
            "I was only worried a bit … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "I wonder\x01",
            "It seems unnecessary to take care of me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1419")

    label("loc_1394")


    ChrTalk(
        0x8,
        (
            "Gantz to the cult's case\x01",
            "When it gets involved,\x01",
            "I thought what would happen … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "Hello, I got it\x01",
            "There was nothing to worry about.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1419")

    Jump("loc_353")

    label("loc_141E")

    TalkEnd(0x8)
    Return()

    # Function_4_346 end

    def Function_5_1422(): pass

    label("Function_5_1422")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_155C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14E7")

    ChrTalk(
        0x9,
        (
            "It is somewhat sloppy outside\x01",
            "It seems that trees are growing ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Dad, than that\x01",
            "The mine resumed\x01",
            "It seems to be very happy ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Eh, Kimi is happy too.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1557")

    label("loc_14E7")


    ChrTalk(
        0x9,
        (
            "It is somewhat sloppy outside\x01",
            "It seems that trees are growing ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Dad seems to be happy\x01",
            "Kimi, do not mind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1557")

    Jump("loc_1B1E")

    label("loc_155C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_15C4")

    ChrTalk(
        0x9,
        (
            "Sunday school classes, too,\x01",
            "I have not received it for a while ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Sister,\x01",
            "I hope you are fine.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B1E")

    label("loc_15C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1661")

    ChrTalk(
        0x9,
        (
            "Dad, after doing it\x01",
            "He is always mad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Dukuritzu is a good thing before\x01",
            "I was told …\x01",
            "Was it not good after all?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B1E")

    label("loc_1661")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_175D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16F7")

    ChrTalk(
        0x9,
        (
            "Kimmy always\x01",
            "Smile, Smile ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "As long as you are smiling at all times\x01",
            "To be in good health,\x01",
            "Daddy was saying that.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1758")

    label("loc_16F7")


    ChrTalk(
        0x9,
        (
            "Kimmy always\x01",
            "Smile, Smile ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Everyone in the town\x01",
            "It is getting better soon.\x01",
            "I hope you do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1758")

    Jump("loc_1B1E")

    label("loc_175D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_186A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_180D")

    ChrTalk(
        0x9,
        (
            "Dad, on a rainy day\x01",
            "It looks somewhat lonely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "After all the work of the miners\x01",
            "I wanted to continue it all the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "But Kimi,\x01",
            "I love my current dad too!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1865")

    label("loc_180D")


    ChrTalk(
        0x9,
        (
            "Dad, on a rainy day\x01",
            "It looks somewhat lonely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Kimi cheered me up\x01",
            "I have to give it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1865")

    Jump("loc_1B1E")

    label("loc_186A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1878")
    Jump("loc_1B1E")

    label("loc_1878")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_190A")

    ChrTalk(
        0x9,
        (
            "Kimi still,\x01",
            "What is Dokitsu?\x01",
            "I do not know … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Daddy is dorking\x01",
            "It's a good thing,\x01",
            "Kimi also agrees.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B1E")

    label("loc_190A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1918")
    Jump("loc_1B1E")

    label("loc_1918")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1960")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1933")
    Call(0, 6)
    Jump("loc_195B")

    label("loc_1933")


    ChrTalk(
        0x9,
        "Wow, Michii's stuffed animal!\x02",
    )

    CloseMessageWindow()

    label("loc_195B")

    Jump("loc_1B1E")

    label("loc_1960")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1A0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19E9")

    ChrTalk(
        0x9,
        (
            "Kimi, when it gets bigger\x01",
            "I'm going to shop with Dad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "A lot of now\x01",
            "You must remember your job.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A05")

    label("loc_19E9")


    ChrTalk(
        0x9,
        "Assistance, help you ~ ♪\x02",
    )

    CloseMessageWindow()

    label("loc_1A05")

    Jump("loc_1B1E")

    label("loc_1A0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 5)), scpexpr(EXPR_END)), "loc_1B1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AB4")

    ChrTalk(
        0x9,
        (
            "Dad,\x01",
            "It used to be the biggest minister in the town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "So, to all the miners\x01",
            "There are many things that kibishi comb,\x01",
            "Actually it really cares.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1B1E")

    label("loc_1AB4")


    ChrTalk(
        0x9,
        (
            "Dad,\x01",
            "It used to be the biggest minister in the town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "It is always millet,\x01",
            "I'm really very kind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B1E")

    TalkEnd(0xFE)
    Return()

    # Function_5_1422 end

    def Function_6_1B22(): pass

    label("Function_6_1B22")

    OP_4B(0xA, 0xFF)
    OP_4B(0x9, 0xFF)

    ChrTalk(
        0x9,
        "Oh, Harold Otachi.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "Do you negotiate with your father today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#03600FOh, that kind of place.\x01",
            "In the place where I bought various items.\x02\x03",
            "#03609FHehe, I wanted you before.\x01",
            "I brought Michishiguguri too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "Wow, really! Is it?\x01",
            "You did it!\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 3)
    OP_4C(0xA, 0xFF)
    OP_4C(0x9, 0xFF)
    Return()

    # Function_6_1B22 end

    def Function_7_1C29(): pass

    label("Function_7_1C29")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1DE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D70")

    ChrTalk(
        0x101,
        (
            "#00000FMr. Harold … …\x01",
            "You came to Mainz, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#03600FYeah, from Almorica\x01",
            "Crops I have purchased\x01",
            "I have just come to deliver.\x02\x03",
            "#03603F…… People in town recently,\x01",
            "Day to be frightened by the nightmare of raids\x01",
            "It seems to have been spared.\x02\x03",
            "#03608FAlthough the victims did not appear,\x01",
            "The rash of the raid surely\x01",
            "It seems they are left behind …\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1DDE")

    label("loc_1D70")


    ChrTalk(
        0xA,
        (
            "#03603FTo merchants like me\x01",
            "I can not do anything serious … …\x02\x03",
            "#03600FI managed to recover my energy\x01",
            "I want it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DDE")

    Jump("loc_1E33")

    label("loc_1DE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1E33")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DFE")
    Call(0, 6)
    Jump("loc_1E33")

    label("loc_1DFE")


    ChrTalk(
        0xA,
        (
            "#03609Fmy mother……\x01",
            "After all, children\x01",
            "Your energy is best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E33")

    TalkEnd(0xFE)
    Return()

    # Function_7_1C29 end

    SaveToFile()

Try(main)
