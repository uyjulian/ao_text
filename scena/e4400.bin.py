from ScenarioHelper import *

def main():
    CreateScenaFile(
        "e4400.bin",                # FileName
        "e4400",                    # MapName
        "e4400",                    # Location
        0x0000,                     # MapIndex
        "ed7570",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0xFF,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "e4400",                  # 0
        "Erie",                 # 1
        "Lisha",               # 2
        "God wolf Zeit",           # 3
        "Grace",               # 4
    ))

    AddCharChip((
        "chr/ch00100.itc",                   # 00
        "chr/ch03200.itc",                   # 01
        "chr/ch02708.itc",                   # 02
        "chr/ch06000.itc",                   # 03
    ))

    DeclNpc(4294964366, 0,       509,     270,  389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(2589,    0,       4294967267, 90,   389,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(4294965747, 0,       4294966337, 180,  405,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(4294964366, 0,       509,     270,  389,  0x0, 0,   3,   0,   0,   0,   0,   9,   255,  0)

    ChipFrameInfo(324, 0)                                        # 0

    ScpFunction((
        "Function_0_144",          # 00, 0
        "Function_1_1F4",          # 01, 1
        "Function_2_2BE",          # 02, 2
        "Function_3_382",          # 03, 3
        "Function_4_577",          # 04, 4
        "Function_5_9B5",          # 05, 5
        "Function_6_D63",          # 06, 6
        "Function_7_105E",         # 07, 7
        "Function_8_1432",         # 08, 8
        "Function_9_1611",         # 09, 9
        "Function_10_1D3F",        # 0A, 10
        "Function_11_1F83",        # 0B, 11
    ))


    def Function_0_144(): pass

    label("Function_0_144")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_17C"),
        (1, "loc_188"),
        (2, "loc_194"),
        (3, "loc_1A0"),
        (4, "loc_1AC"),
        (5, "loc_1B8"),
        (6, "loc_1C4"),
        (SWITCH_DEFAULT, "loc_1D0"),
    )


    label("loc_17C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_188")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_194")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_1A0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_1AC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_1B8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_1C4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_1D0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_1DC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1F3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_1F3")

    Return()

    # Function_0_144 end

    def Function_1_1F4(): pass

    label("Function_1_1F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_207")
    ClearChrFlags(0xB, 0x80)
    Jump("loc_2A8")

    label("loc_207")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_21A")
    ClearChrFlags(0xB, 0x80)
    Jump("loc_2A8")

    label("loc_21A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_22D")
    ClearChrFlags(0xB, 0x80)
    Jump("loc_2A8")

    label("loc_22D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_240")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_2A8")

    label("loc_240")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_253")
    ClearChrFlags(0x8, 0x80)
    Jump("loc_2A8")

    label("loc_253")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_266")
    ClearChrFlags(0xB, 0x80)
    Jump("loc_2A8")

    label("loc_266")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_279")
    ClearChrFlags(0xA, 0x80)
    Jump("loc_2A8")

    label("loc_279")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_28C")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_2A8")

    label("loc_28C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_29A")
    Jump("loc_2A8")

    label("loc_29A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2A8")
    ClearChrFlags(0xA, 0x80)

    label("loc_2A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_2BD")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    Event(0, 11)

    label("loc_2BD")

    Return()

    # Function_1_1F4 end

    def Function_2_2BE(): pass

    label("Function_2_2BE")

    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0xD0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2E4")
    Sound(132, 1, 70, 0)
    Sound(497, 1, 30, 0)
    ClearScenarioFlags(0x0, 1)
    Jump("loc_2F0")

    label("loc_2E4")

    Sound(132, 1, 100, 0)
    Sound(497, 1, 100, 0)

    label("loc_2F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_305")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_305")

    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF032877), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_F0(0x1, 0x7D0)
    SetMapFlags(0x10000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_345")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33C")
    OP_7D(0xD7, 0xFF, 0xFF, 0x0, 0x0)
    Jump("loc_345")

    label("loc_33C")

    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)

    label("loc_345")

    SetMapObjFrame(0x0, "door_l1", 0x0, 0x1)
    SetMapObjFrame(0x0, "door_l2", 0x0, 0x1)
    SetMapObjFrame(0x0, "door_r1", 0x0, 0x1)
    SetMapObjFrame(0x0, "door_r2", 0x0, 0x1)
    Return()

    # Function_2_2BE end

    def Function_3_382(): pass

    label("Function_3_382")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_397")
    Call(0, 4)
    Jump("loc_573")

    label("loc_397")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B9")

    ChrTalk(
        0xFE,
        (
            "#00103FInvalid declaration of 'Independent State' …\x01",
            "Whether it's really correct\x01",
            "I do not know yet ….\x02\x03",
            "#00101FSacrificing Kia-chan\x01",
            "To be given peace,\x01",
            "It is absolutely wrong.\x02\x03",
            "#00103FRetrieve Ka'a-chan …\x01",
            "In order to take that first step,\x01",
            "You must make this strategy sure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_573")

    label("loc_4B9")


    ChrTalk(
        0xFE,
        (
            "#00103FInvalid declaration of 'Independent State' …\x01",
            "Whether it's really correct\x01",
            "I do not know yet ….\x02\x03",
            "#00100FRetrieve Ka'a-chan …\x01",
            "In order to take that first step,\x01",
            "You must make this strategy sure.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_573")

    TalkEnd(0xFE)
    Return()

    # Function_3_382 end

    def Function_4_577(): pass

    label("Function_4_577")


    ChrTalk(
        0x8,
        (
            "#00103FInvalid declaration of 'Crossbell independent country' …\x01",
            "After that the timing of hacking\x01",
            "I just want to measure it.\x02\x03",
            "#00106F…… Well, maybe I am getting nervous somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FHaha … … It is not surprising.\x02\x03",
            "#00003FIt exists in the place called Cros Bell\x01",
            "Temporary peace, with our hands\x01",
            "Because I'm rocking.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)

    ChrTalk(
        0x8,
        (
            "#00108F…… What we are about to do\x01",
            "I wonder if it is really correct.\x02\x03",
            "#00103FMany people living in Crossbell,\x01",
            "Thanks to my uncle\x01",
            "It is protected from two major powers and is spending peacefully …\x02\x03",
            "#00108FWe will do it,\x01",
            "It is trying to take away … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F……Ah.\x02\x03",
            "#00001FBut today's peace is\x01",
            "To President Dieter\x01",
            "It is made in a form to be used.\x02\x03",
            "#00003FSuch a situation, most citizens\x01",
            "I do not know about that ….\x01",
            "It's a big problem for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#00108F… Well, yeah.\x02\x03",
            "#00103FSacrificing Kia-chan\x01",
            "To be given peace,\x01",
            "It is absolutely wrong.\x02\x03",
            "#00100F… …. Hehe, thank you Lloyd.\x01",
            "Thanks a little bit\x01",
            "I feel my hesitancy has disappeared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FWell, I wish I could become a force.\x02\x03",
            "#00000FTake back Ka'a …\x01",
            "To that end, this strategy\x01",
            "I hope to succeed absolutely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#00100FYeah … … Let's do our best.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D6, 0)
    Return()

    # Function_4_577 end

    def Function_5_9B5(): pass

    label("Function_5_9B5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_9C6")
    Jump("loc_D5F")

    label("loc_9C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_B9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AEF")

    ChrTalk(
        0x9,
        (
            "#10703F\"Steel's Saint\" … …\x02\x03",
            "#10701FBy the way,\x01",
            "Borrowed the mask of \"silver\" crushed\x01",
            "I have not returned it.\x02\x03",
            "#10706FTo the experts to that extent\x01",
            "How far I can go down\x01",
            "I do not know but …\x02\x03",
            "#10701FI will never yield to me now,\x01",
            "There is a mission to fulfill.\x01",
            "…… I can not lose.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_B97")

    label("loc_AEF")


    ChrTalk(
        0x9,
        (
            "#10703FTo \"master of steel\" as much as an expert\x01",
            "How far I can go down\x01",
            "I do not know but …\x02\x03",
            "#10701FI will never yield to me now,\x01",
            "There is a mission to fulfill.\x01",
            "…… I can not lose.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B97")

    Jump("loc_D5F")

    label("loc_B9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_D5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D8, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB7")
    Call(0, 6)
    Jump("loc_D5F")

    label("loc_BB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CDB")

    ChrTalk(
        0x9,
        (
            "#10703FInformation on resistance forces in the direction of Mainz,\x01",
            "When hiding in the battlefield\x01",
            "I got it from the Defense Army.\x02\x03",
            "#10708F…… If you think about \"black moon\" as well\x01",
            "I was indebted to various people.\x02\x03",
            "In a manner like that\x01",
            "I let it destroy … ….\x02\x03",
            "#10703FTo Mr. Tsao,\x01",
            "Which should I borrow back?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_D5F")

    label("loc_CDB")


    ChrTalk(
        0x9,
        (
            "#10708F…… If you think about \"black moon\" as well\x01",
            "I was indebted to various people.\x02\x03",
            "#10703FTo Mr. Tsao,\x01",
            "Which should I borrow back?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D5F")

    TalkEnd(0xFE)
    Return()

    # Function_5_9B5 end

    def Function_6_D63(): pass

    label("Function_6_D63")


    ChrTalk(
        0x9,
        (
            "#10702FMr. Ilya ……\x01",
            "The consciousness was back and it was really good.\x02\x03",
            "#10703F……………………………………………….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F……Lisha、イリアさんに\x01",
            "When I want to meet again,\x01",
            "Do not hesitate to say anytime.\x02\x03",
            "#00000FAbsolutely find the interval,\x01",
            "I will make him head to Ursula hospital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10702FHehe, anxiety\x01",
            "Thank you very much.\x02\x03",
            "#10703FBut now I am cross-border city\x01",
            "To release the alkane shell\x01",
            "I decided to pour full effort.\x02\x03",
            "#10701FBefore Mr. Ilya,\x01",
            "To stretch my heart and stand up\x01",
            "In order to become … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F……I see.\x01",
            "Then, as soon as possible\x01",
            "You have to achieve it.\x02\x03",
            "#00004FそれでLishaがイリアさんに\x01",
            "If you were to be able to meet,\x01",
            "I think we can do better as well.\x02\x03",
            "#00000FKia, Iria, and\x01",
            "Even for friends ……\x01",
            "お互い力を尽くそう、Lisha。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#10702FYes……!\x01",
            "Thank you for your consideration!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D8, 3)
    Return()

    # Function_6_D63 end

    def Function_7_105E(): pass

    label("Function_7_105E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_106F")
    Jump("loc_142E")

    label("loc_106F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_1270")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11C9")

    ChrTalk(
        0xA,
        (
            "#01203F#3CMembers of the support department also\x01",
            "It seems that it gathers gradually.\x02\x03",
            "#01200FOilly direct help\x01",
            "When it is not necessary, I will return again\x01",
            "I am going to let him go down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FOh … I know.\x02\x03",
            "#00000FBut until then\x01",
            "I'm begging you, Zeit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#01200F#3CHuh, of course.\x01",
            "The responsibility as a police dog is\x01",
            "I will let it go.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_126B")

    label("loc_11C9")


    ChrTalk(
        0xA,
        (
            "#01200F#3COilly direct help\x01",
            "When it is not necessary, I will return again\x01",
            "I let you go down to the back.\x02\x03",
            "ただ、The responsibility as a police dog is\x01",
            "Because I will let it go\x01",
            "Do not worry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_126B")

    Jump("loc_142E")

    label("loc_1270")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_142E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_128B")
    Call(0, 8)
    Jump("loc_142E")

    label("loc_128B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1396")

    ChrTalk(
        0xA,
        (
            "#01203F#3CI have a nice guy\x01",
            "Tactical Orgement and Learning\x01",
            "I can not use it ……\x02\x03",
            "#01200FAs a god warrior there is some understanding of art,\x01",
            "Strategy of war as usual\x01",
            "You can become a power of your own power.\x02\x03",
            "Lloyd, sonny also\x01",
            "Leaderboard\x01",
            "I will have you see me again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_142E")

    label("loc_1396")


    ChrTalk(
        0xA,
        (
            "#01200F#3CLloyd, sonny also\x01",
            "Leaderboard\x01",
            "I will have you see me again.\x02\x03",
            "#01203FHooves, my power to be a goddess\x01",
            "Try to draw out to yourself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_142E")

    TalkEnd(0xFE)
    Return()

    # Function_7_105E end

    def Function_8_1432(): pass

    label("Function_8_1432")


    ChrTalk(
        0xA,
        (
            "#01200F#3CUrsula Hospital? …………\x02\x03",
            "#01203F………………………….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FZeit …?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#01203F#3CHuh, nothing.\x01",
            "I remember a while ago.\x02\x03",
            "#01200FEven so, some times ever\x01",
            "Although I had helped Oil, … …\x02\x03",
            "Together going down the highway#2RYu#To be honest\x01",
            "Was this the first time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha … that is true.\x02\x03",
            "#00000FPlease for a while.\x01",
            "I'm counting on you Zeit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#01200F#3CHuhu, you are also the owl\x01",
            "Leaderboard\x01",
            "I will have you see me again.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D8, 7)
    Return()

    # Function_8_1432 end

    def Function_9_1611(): pass

    label("Function_9_1611")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_17D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_162F")
    Call(0, 10)
    Jump("loc_17D1")

    label("loc_162F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_174D")

    ChrTalk(
        0xB,
        (
            "#02105FNo way Lloyd's guys\x01",
            "That Arios McClein\x01",
            "I will not beat it.\x02\x03",
            "#02102FHuhu,\x01",
            "He grew big\x01",
            "Your sister is happy ☆\x02\x03",
            "#02104FIf you guys, what are you doing any longer?\x01",
            "I think I can get over it.\x02\x03",
            "#02109FWith everyone as it is,\x01",
            "Have a great happy ending!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_17D1")

    label("loc_174D")


    ChrTalk(
        0xB,
        (
            "#02104FIf you guys, what are you doing any longer?\x01",
            "I think I can get over it.\x02\x03",
            "#02109FWith everyone as it is,\x01",
            "Have a great happy ending!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17D1")

    Jump("loc_1D3B")

    label("loc_17D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_196D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18F8")

    ChrTalk(
        0xB,
        (
            "#02104FWhile I am in \"Taiki\"\x01",
            "I will take pictures as much as possible.\x02\x03",
            "#02100FAlso, returning to the correspondent\x01",
            "The truth of this incident\x01",
            "There must be an article …\x02\x03",
            "#02102FSo Lloyd guys,\x01",
            "Good luck and solve this incident!\x02\x03",
            "#02109FI have the best three-page article\x01",
            "Please write me!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1968")

    label("loc_18F8")


    ChrTalk(
        0xB,
        (
            "#02100FLloyd guys,\x01",
            "Good luck and solve this incident!\x02\x03",
            "#02109FI have the best three-page article\x01",
            "Please write me!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1968")

    Jump("loc_1D3B")

    label("loc_196D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1B2A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AA3")

    ChrTalk(
        0xB,
        (
            "#02106FNo way to wetlands\x01",
            "Such a \"big tree\" will not appear ~.\x02\x03",
            "#02100FBeyond the Orkis Tower\x01",
            "It's the same size, even from the empire and the republic\x01",
            "I wonder if I can see it.\x02\x03",
            "#02103FTogether with Crosbell\x01",
            "The whole continent should be paying attention …\x02\x03",
            "#02102FIf that happens, let me also live\x01",
            "I will follow you!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1B25")

    label("loc_1AA3")


    ChrTalk(
        0xB,
        (
            "#02103FTogether with Crosbell\x01",
            "The whole continent should be paying attention …\x02\x03",
            "#02102FIf that happens, let me also live\x01",
            "I will follow you!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B25")

    Jump("loc_1D3B")

    label("loc_1B2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_1D3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C94")

    ChrTalk(
        0xB,
        (
            "#02103FHe is one of the autonomous state representatives\x01",
            "I will help Mr. MacDowell,\x01",
            "To announce his words both at home and abroad …\x02\x03",
            "#02100FIf you do, at least the defense army\x01",
            "I will not be in a state of wait\x01",
            "You will not get it.\x02\x03",
            "#02104FMeans to announce the words of the chairman\x01",
            "I need to prepare it separately ….\x01",
            "It looks like the best scoop!\x02\x03",
            "#02102FHaha, good luck\x01",
            "Please help the Chair!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1D3B")

    label("loc_1C94")


    ChrTalk(
        0xB,
        (
            "#02104FPresentation of McDaill's opinion ……\x01",
            "In order to shake the validity of an independent country,\x01",
            "I wonder if there are any more hands.\x02\x03",
            "#02102FHaha, good luck\x01",
            "Please help the Chair!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D3B")

    TalkEnd(0xFE)
    Return()

    # Function_9_1611 end

    def Function_10_1D3F(): pass

    label("Function_10_1D3F")


    ChrTalk(
        0xB,
        (
            "#02105FThat Arios McClein\x01",
            "You seem to have defeated?\x02\x03",
            "#02106FHa ~ …\x01",
            "No way Lloyd's guys\x01",
            "I will not do that … …\x02\x03",
            "#02109F\"Cross Bell hero\" also\x01",
            "I wonder if the time has come for substitution.\x01",
            "No, it's not big scoop!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FHaha …. It's lifting too much.\x02\x03",
            "#00000FAnd for Crossbell\x01",
            "Arios is a hero\x01",
            "I still think that it will not change.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#02104FHehu ……\x01",
            "Lloyd also grew up.\x02\x03",
            "#02102FIt exceeds Arios.\x01",
            "If you guys, what are you doing any longer?\x01",
            "I think I can get over it.\x02\x03",
            "#02109FWith everyone as it is,\x01",
            "Have a great happy ending!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYes! It is!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DA, 0)
    Return()

    # Function_10_1D3F end

    def Function_11_1F83(): pass

    label("Function_11_1F83")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x5, 0xFF, 0xFF)
    OP_32(0xFF, 0xFE, 0x0)
    PartySelect(1)
    RemoveParty(0x4, 0xFF)
    RemoveParty(0x8, 0xFF)
    RemoveParty(0x5, 0xFF)
    SetChrFlags(0xB, 0x80)
    PlayBGM("ed7534", 0)
    SetChrPos(0x101, 0, 0, -2000, 180)
    SetChrPos(0x102, 1050, 0, -2950, 270)
    SetChrPos(0x103, -950, 0, -3250, 90)
    SetChrPos(0x104, 0, 0, -4250, 0)
    OP_68(1840, 1100, 14830, 0)
    MoveCamera(51, 25, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(27300, 0)
    OP_68(0, 1100, -3000, 7000)
    MoveCamera(51, 25, 0, 7000)
    OP_6E(800, 7000)
    SetCameraDistance(18480, 7000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(0, 1100, -3000, 0)
    MoveCamera(51, 25, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(10200, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x104,
        (
            "#00306F#12PToo far, to think far away\x01",
            "Do not feel like coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00208F#6PI agree……\x01",
            "I am in a narrow crossbell\x01",
            "Even though it does not change.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#11P…… Maybe not just us,\x01",
            "Crossbell, no whole continent\x01",
            "I think that it is because it is starting to move.\x02\x03",
            "#00108FPerhaps at the turning point of history\x01",
            "It may be in presence … ….\x02\x03",
            "…………………………………….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#5P……Erie。\x02\x03",
            "#00008FAfter all, with Mariavell\x01",
            "Is there resistance to setting things?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00106F#11PWell … for me\x01",
            "Because they were familiar people.\x02\x03",
            "#00108FAnd from a political point of view\x01",
            "What they are going to do\x01",
            "There are others who can not deny … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00208F#6P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#5P……Really……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00306F#12PWell, it is not a bureaucrat of iron and blood,\x01",
            "Those who do more engaging\x01",
            "I guess there will be more mountains … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00103F#11P─ ─ But, I can say only this.\x02\x03",
            "#00101FWhether the situation will change\x01",
            "We are \"mission support department\".\x02\x03",
            "Only that part\x01",
            "I think there will not be shaking no matter what.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#5PErie……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00202F#6P……Erieさん……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00309F#12PHey, what is your daughter.\x02\x03",
            "#00302FAfter all, police officers,\x01",
            "Was not it about the seat?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        (
            "#00109F#11PHuhu, about the first time.\x02\x03",
            "#00104F…… But it is useless.\x01",
            "I have gotten dyed.\x02\x03",
            "Perhaps, in the future what kind of road\x01",
            "Even if you decide to choose … ….\x02\x03",
            "#00102FThe days I spent with you\x01",
            "For the future I will continue to root\x01",
            "I feel like I keep on coming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#5P……I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        "#00204F#6PI, too, have the same feeling.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        (
            "#00304F#12PHa ha, that's the meaning.\x01",
            "The section chief also made a causal department\x01",
            "I started it.\x02\x03",
            "#00305FNo, speaking of the former\x01",
            "Lloyd's older brother's idea?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#5PHaha, big brother as expected\x01",
            "I do not think that it will be such a situation\x01",
            "I think that I did not imagine.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00001F#5P… … regain the keya,\x01",
            "To solve the incident this time.\x02\x03",
            "Perhaps as a mission support section\x01",
            "It may be a symbol of the mission to fulfill.\x02\x03",
            "#00004FHowever, such a reason\x01",
            "I think that you do not have to think forcefully.\x02\x03",
            "For us\x01",
            "For what I think is important ……\x02\x03",
            "#00000FJust for now, let's go forward and let's go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x102,
        "#00102F#11PYeah … …!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x103,
        (
            "#00204F#6PThe section chief who is out of communication also\x01",
            "I have to look for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x104,
        "#00309F#12PHa ha … … right.\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(9200, 3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopSound(132, 1000, 70)
    StopSound(497, 1000, 30)
    StopBGM(0xFA0)
    WaitBGM()
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Erieがパーティに加入しました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    Sound(517, 0, 100, 0)
    AddCraft(0x1, 0x11F)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ErieがＳクラフト\x01\x07\x02",
            "\"Devine Crusade\"\x07\x05",
            "I have learned.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 52, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "\"Devine Crusade\"\x07\x05",
            "Do you want to register S break?",
            scpstr(0x6),
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        208,
        0,
        (
            "【Yes】\x01",      # 0
            "【No】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_57(0x0)
    OP_60(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29CF")
    SetChrChipPat(0x1, 0x6, 0x11F)

    label("loc_29CF")

    OP_5A()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Erieが加入したことにより、\x01",
            "The capacity of the party exceeded six people.\x02\x03",
            "From the following members\x01",
            "Participating members\x01",
            "Please select again.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PartySelect(0)
    PartySelect(2)
    Sleep(500)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "After that, you are at the bridge\x01",
            "By talking to Abbas\x01",
            "Party organization can be done.\x02\x03",
            "Furthermore, when advancing the story,\x01",
            "Located at the eastern end of Mercapa's movement map\x01",
            "Please choose \"booster point\".\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    SetScenarioFlags(0x1A4, 1)
    OP_29(0xAF, 0x1, 0x14)
    SetScenarioFlags(0x31, 6)
    SetScenarioFlags(0x31, 7)
    EventEnd(0x5)
    NewScene("e3020", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_11_1F83 end

    SaveToFile()

Try(main)
