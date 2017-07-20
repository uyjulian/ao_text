from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t5000.bin",                # FileName
        "t5000",                    # MapName
        "t5000",                    # Location
        0x0000,                     # MapIndex
        "ed7102",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x27,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "t5000",                  # 0
        "Father Kevin",             # 1
        "Sister clothing girl",         # 2
        "Dudley's car",           # 3
        "car",                     # 4
        "car",                     # 5
        "Citizen",                   # 6
        "Citizen",                   # 7
        "Citizen",                   # 8
        "Citizen",                   # 9
        "Citizen",                   # 10
        "Citizen",                   # 11
        "Citizen",                   # 12
        "Citizen",                   # 13
        "Citizen",                   # 14
        "Republic Bus",             # 15
        "Escort car",                 # 16
        "Fake brand quotient",           # 17
        "Republican soldier",             # 18
        "Republican soldier",             # 19
        "Black moon member",             # 20
        "Black moon member",             # 21
        "SE control",                 # 22
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(836, 0)                                        # 0

    ScpFunction((
        "Function_0_344",          # 00, 0
        "Function_1_3F4",          # 01, 1
        "Function_2_418",          # 02, 2
        "Function_3_419",          # 03, 3
        "Function_4_2753",         # 04, 4
        "Function_5_27E3",         # 05, 5
        "Function_6_2817",         # 06, 6
        "Function_7_286F",         # 07, 7
        "Function_8_28EF",         # 08, 8
        "Function_9_2929",         # 09, 9
        "Function_10_2970",        # 0A, 10
        "Function_11_29CB",        # 0B, 11
        "Function_12_2A2C",        # 0C, 12
        "Function_13_2A48",        # 0D, 13
        "Function_14_3B58",        # 0E, 14
        "Function_15_3C71",        # 0F, 15
        "Function_16_3C9E",        # 10, 16
        "Function_17_3CD8",        # 11, 17
    ))


    def Function_0_344(): pass

    label("Function_0_344")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_37C"),
        (1, "loc_388"),
        (2, "loc_394"),
        (3, "loc_3A0"),
        (4, "loc_3AC"),
        (5, "loc_3B8"),
        (6, "loc_3C4"),
        (SWITCH_DEFAULT, "loc_3D0"),
    )


    label("loc_37C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_3DC")

    label("loc_388")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_3DC")

    label("loc_394")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_3DC")

    label("loc_3A0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_3DC")

    label("loc_3AC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_3DC")

    label("loc_3B8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_3DC")

    label("loc_3C4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3DC")

    label("loc_3D0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3DC")

    label("loc_3DC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3F3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3DC")

    label("loc_3F3")

    Return()

    # Function_0_344 end

    def Function_1_3F4(): pass

    label("Function_1_3F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_408")
    ClearScenarioFlags(0x22, 0)
    Event(0, 3)
    Jump("loc_417")

    label("loc_408")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_417")
    ClearScenarioFlags(0x22, 1)
    Event(0, 13)

    label("loc_417")

    Return()

    # Function_1_3F4 end

    def Function_2_418(): pass

    label("Function_2_418")

    Return()

    # Function_2_418 end

    def Function_3_419(): pass

    label("Function_3_419")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch11400.itc", 0x1E)
    LoadChrToIndex("apl/ch51026.itc", 0x1F)
    LoadChrToIndex("chr/ch25600.itc", 0x20)
    LoadChrToIndex("chr/ch21102.itc", 0x21)
    LoadChrToIndex("chr/ch21302.itc", 0x22)
    LoadChrToIndex("chr/ch26000.itc", 0x23)
    LoadChrToIndex("chr/ch25000.itc", 0x24)
    LoadChrToIndex("chr/ch44200.itc", 0x25)
    LoadChrToIndex("chr/ch44100.itc", 0x26)
    LoadChrToIndex("chr/ch44000.itc", 0x27)
    LoadChrToIndex("chr/ch44400.itc", 0x28)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13800.itp")
    SetChrPos(0x101, 0, 0, 8400, 0)
    SetChrPos(0x109, -1300, 0, 8200, 0)
    SetChrPos(0x10A, -700, 0, 10900, 180)
    SetChrPos(0x108, 700, 0, 11200, 180)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 1500, 0, 8200, 315)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x2)
    ClearChrFlags(0xA, 0x80)
    OP_78(0xA, 0xA)
    SetMapObjFrame(0xA, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0xA, 0, 0, 13500, 0)
    OP_D5(0xA, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0xA, 0x1000)
    OP_74(0xA, 0x1E)
    OP_70(0xA, 0x0)
    ClearChrFlags(0xB, 0x80)
    OP_78(0x6, 0xB)
    OP_49()
    SetChrPos(0xB, 5000, 0, -3500, 0)
    OP_D5(0xB, 0x0, 0x15F90, 0x0, 0x0)
    SetMapObjFlags(0x6, 0x1000)
    ClearChrFlags(0xC, 0x80)
    OP_78(0x7, 0xC)
    OP_49()
    SetChrPos(0xC, -19000, 0, 2200, 0)
    OP_D5(0xC, 0x0, 0x15F90, 0x0, 0x0)
    SetMapObjFlags(0x7, 0x1000)
    ClearChrFlags(0x16, 0x80)
    OP_78(0x9, 0x16)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x16, -35000, 0, 17500, 0)
    OP_D5(0x16, 0x0, 0x15F90, 0x0, 0x0)
    SetMapObjFlags(0x9, 0x1000)
    OP_74(0x9, 0x1E)
    OP_70(0x9, 0x0)
    OP_71(0x9, 0x79, 0xB4, 0x0, 0x20)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrChipByIndex(0xD, 0x20)
    SetChrPos(0xD, 5800, 0, -5400, 225)
    BeginChrThread(0xD, 0, 0, 0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrChipByIndex(0xE, 0x21)
    SetChrSubChip(0xE, 0x2)
    SetChrPos(0xE, -2300, 50, -2750, 225)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0xF, 0x22)
    SetChrSubChip(0xF, 0x1)
    SetChrPos(0xF, -2950, 50, -2200, 225)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x10, 0x23)
    SetChrPos(0x10, 14700, 0, -6400, 270)
    BeginChrThread(0x10, 0, 0, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x11, 0x24)
    SetChrPos(0x11, -22200, 0, 900, 270)
    BeginChrThread(0x11, 0, 0, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x12, 0x25)
    SetChrPos(0x12, 0, 0, -23000, 0)
    BeginChrThread(0x12, 1, 0, 6)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x13, 0x26)
    SetChrPos(0x13, 21500, 180, 6000, 270)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x14, 0x27)
    SetChrPos(0x14, 12000, 0, 9000, 0)
    BeginChrThread(0x14, 0, 0, 8)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x15, 0x28)
    SetChrPos(0x15, -23500, 0, 900, 90)
    BeginChrThread(0x15, 0, 0, 0)
    OP_68(0, 1900, -21500, 0)
    MoveCamera(45, 35, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(18000, 0)
    OP_68(0, 2000, 0, 8000)
    MoveCamera(30, 17, 0, 8000)
    SetCameraDistance(41000, 8000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    PlaceName2(100, 200, "c_plac35", 0x0, 0)
    Sleep(500)
    Sleep(1000)
    BeginChrThread(0x16, 0, 0, 4)
    BeginChrThread(0x16, 1, 0, 5)
    BeginChrThread(0x1D, 1, 0, 12)
    Sleep(2000)
    BeginChrThread(0x13, 0, 0, 7)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(-11500, 1900, 7700, 0)
    MoveCamera(23, 27, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(18000, 0)
    OP_0D()
    WaitChrThread(0x16, 1)
    Sleep(1000)
    Fade(500)
    OP_68(0, 11000, 17800, 0)
    MoveCamera(31, -15, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(26000, 0)
    OP_68(0, 5000, 17800, 7000)
    MoveCamera(39, 10, 0, 7000)
    SetCameraDistance(29000, 7000)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(0, 1100, 9600, 0)
    MoveCamera(40, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#12P#00004F─ ─ Mr. Dudley.\x01",
            "Thank you for your advice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        "#00600F#5POh, leave it alone.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x8, 500)
    Sleep(300)

    ChrTalk(
        0x10A,
        (
            "#00603F#5P__ - Father Kevin.\x01",
            "Let me thank you.\x02\x03",
            "#00600FWell, if it is true in advance,\x01",
            "police#4RHere#I wanted you to contact.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9BF():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9BF)
    Sleep(50)

    def lambda_9CF():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9CF)
    Sleep(100)

    ChrTalk(
        0x8,
        (
            "#04306F#11PWell, ~ I want to do that\x01",
            "I did it in the mountains.\x02\x03",
            "#04300FHow many minutes, the Order#6RUchi et al#For\x01",
            "Crossbell is a demon gate ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00606F#5PCross Bell parish chief,\x01",
            "The intention of Archbishop Elderda?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00005FThat's right, Mr. Marble said before\x01",
            "Legal experts ……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)
    Sleep(150)

    ChrTalk(
        0x8,
        (
            "#04303F#11POh, that's what we do.\x02\x03",
            "#04300FWell, there are various, and to the archbishop\x01",
            "You are hated by me.\x02\x03",
            "At the crossbell\x01",
            "About the activity of the Star Cup\x01",
            "I'm forbidden at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10108FArchbishop Elderda ……\x02\x03",
            "#10106FI have met him, but\x01",
            "It is a very strict person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04306F#11PStrictness is also strict.\x01",
            "I have never seen such a bad guy.\x02\x03",
            "#04308FWell, as we all do well\x01",
            "From a true person like him\x01",
            "Maybe I can not stand it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00011FYes, various things ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#5P#01403FWell, incident concerning \"ancient relics\"\x01",
            "It means that we can not finish with just beautiful things.\x02\x03",
            "#01402F__ - Father Kevin.\x01",
            "Anyway this time I was saved.\x02\x03",
            "Please let me thank you again.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x0, 0x1F4)
    Sleep(150)

    ChrTalk(
        0x8,
        (
            "#04302F#12PHello, to Arios\x01",
            "I have borrowed a big deal ahead of time.\x02\x03",
            "#04304FIf it is true, including cases of the example cult\x01",
            "I'm looking forward to go with it, though.\x02\x03",
            "#04311FWell, I do not want to stimulate the archbishop\x01",
            "Please tell me if you know something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#5P#01404FOh, through the guild\x01",
            "Let me get in touch with you.\x02\x03",
            "#01402F─ ─ Lloyd, Noel also served.\x01",
            "This time it did really well.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_EDD():
        TurnDirection(0xFE, 0x108, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_EDD)
    Sleep(50)

    def lambda_EED():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_EED)
    Sleep(50)
    TurnDirection(0x109, 0x10A, 500)
    Sleep(200)

    ChrTalk(
        0x109,
        (
            "#6P#10112FHaha, to be honest\x01",
            "I could not help you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00002FNo, she is really\x01",
            "It helped me.\x02\x03",
            "#00006F… … That's where I am\x01",
            "After all it is still immature.\x02\x03",
            "#00008FIf true, until arrested properly\x01",
            "I have to pull everyone\x01",
            "I should have never … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        "#5P#01405FHM……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00606F#5PHun, self in love#4RA hollow#Do not.\x02\x03",
            "#00601FArrest by support department\x01",
            "To the end is to be built\x01",
            "You also valve#2RAside#You ought to have said.\x02\x03",
            "On top of that, myself really\x01",
            "Do you think it was useless?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00005FWell, that is ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00603F#5PSelf-support is good, but objective self-evaluation and\x01",
            "Situation judgment is mandatory for senior agents.\x02\x03",
            "#00600FAlthough I was in training, I was in one department\x01",
            "You should save that area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00002FMr. Dudley …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10112FHehu ……\x01",
            "It is not really frank.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#5P#01404FFluor, about a word of well done\x01",
            "Say what you should do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10A,
        (
            "#00610F#5PWell, it's noisy.\x02\x03",
            "#00606F── Anyway Bannings.\x01",
            "This is the end of the first department training.\x02\x03",
            "#00602FTogether with what I learned in this case\x01",
            "Use it for a new start.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00002FYes……\x01",
            "Thank you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x108,
        (
            "#5P#01404FWell then,\x01",
            "Let me go ahead.\x02\x03",
            "#01402FIf there is something to cooperate with\x01",
            "I'm counting on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00000FYes, this is it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10109FGood morning!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#04309F#12PThen, I'm fine ~!\x02",
    )

    CloseMessageWindow()
    OP_71(0xA, 0x12D, 0x14A, 0x0, 0x0)
    Sound(462, 0, 100, 0)
    OP_79(0xA)
    BeginChrThread(0x10A, 3, 0, 9)
    Sleep(1000)
    BeginChrThread(0x108, 3, 0, 9)
    WaitChrThread(0x108, 3)

    def lambda_1409():

        label("loc_1409")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_1409")

    QueueWorkItem2(0x101, 2, lambda_1409)

    def lambda_141B():

        label("loc_141B")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_141B")

    QueueWorkItem2(0x109, 2, lambda_141B)

    def lambda_142D():

        label("loc_142D")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_142D")

    QueueWorkItem2(0x8, 2, lambda_142D)
    OP_71(0xA, 0x14B, 0x168, 0x0, 0x0)
    Sound(461, 0, 100, 0)
    OP_79(0xA)
    Sound(470, 0, 80, 0)
    OP_71(0xA, 0x3C, 0x5A, 0x0, 0x0)
    OP_79(0xA)
    Sound(494, 0, 90, 0)
    OP_71(0xA, 0x79, 0xB4, 0x0, 0x20)
    OP_68(-2000, 1100, 9600, 2000)

    def lambda_148C():
        OP_96(0xFE, 0xFFFFD6FC, 0x0, 0x34BC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_148C)
    Sleep(2000)
    Sound(457, 0, 100, 0)
    Fade(500)
    EndChrThread(0xA, 0x1)
    SetChrPos(0xA, -15000, 0, 18000, 0)

    def lambda_14C9():
        OP_96(0xFE, 0xFFFF3CB0, 0x0, 0x4650, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_14C9)
    OP_68(-18000, 900, 18000, 0)
    MoveCamera(60, 27, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(16500, 0)
    OP_68(-30000, 900, 18000, 4000)
    MoveCamera(60, 21, 0, 4000)
    SetCameraDistance(23500, 4000)
    OP_6F(0x79)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x8, 0x2)
    Fade(500)
    StopSound(457, 500, 90)
    OP_68(500, 1000, 8500, 0)
    MoveCamera(40, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x101, -800, 0, 8900, 270)
    SetChrPos(0x109, -900, 0, 7600, 270)
    SetChrPos(0x8, 1500, 0, 8500, 270)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#04309F#11PNo, you are lucky too.\x02\x03",
            "#04311FEven if belonging to a different senior\x01",
            "Does not it seem to be blessed?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1618():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1618)
    Sleep(50)
    TurnDirection(0x109, 0x8, 500)

    ChrTalk(
        0x101,
        "#00002F#6PYes, I really think so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10104FI agree……\x01",
            "Sergei also seems so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04300F#11PSo what do you do?\x02\x03",
            "By train as it is\x01",
            "Are you planning on going back to the crossbell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PYes, I will do so.\x02\x03",
            "#00005FThat's it……\x01",
            "Kevin Father, what are your plans for the rest of this time?\x02\x03",
            "#00000FIt's only one station to crossbell … ….\x01",
            "If you do not mind, please drop in\x01",
            "I'd like to thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04306F#11PNo, thank you.\x01",
            "I have a meeting in the future.\x02\x03",
            "#04308FIf true, also about the cult of the example\x01",
            "I want to hear a detailed story, but ….\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00013F#6PD∴ G church, is … …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10101FAs I thought, the church, too\x01",
            "Are you grabbing something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04306F#11PNo, that is totally.\x02\x03",
            "#04300FWhat we were involved with the cult was\x01",
            "It was the last incident for about 4 years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10105FFour years ago ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#6PArmies and guilds from various countries cooperated\x01",
            "It is after the simultaneous suppression / cautionary operation, is not it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04303F#11POh, I got it from that\x01",
            "I controlled one of the lodges.\x02\x03",
            "#04308F…… Story only here, among the cults\x01",
            "It is the worst lodge.\x02\x03",
            "#04301FTo be honest, it seems like human experience\x01",
            "They did the ceremonial rituals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#6P……Is that so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        (
            "#6P#10106Ftruly……\x01",
            "It was the lowest guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04304F#11PWell, actually, at the time, Mr. Arios\x01",
            "You have been helped by me.\x02\x03",
            "#04311FI made it while I was borrowing a big deal\x01",
            "This time, I was saved because I helped you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#6PIs that so……\x02\x03",
            "#00004FBut thanks to that, keeping the criminal alive\x01",
            "I was able to catch it.\x02\x03",
            "#00000FThank you\x01",
            "……it was a great help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04304F#11PNo, no.\x02\x03",
            "#04302FEven those with glasses just before said that\x01",
            "Thanks to you that managed to do something.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#6PIs it mine?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04304F#11POh, that older brother\x01",
            "I kept it at the limit\x01",
            "It is because you had a word.\x02\x03",
            "#04300FEven if I treat you otherwise\x01",
            "Perhaps she could not have been helped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#6PI see.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(200)

    ChrTalk(
        0x109,
        (
            "#12P#10109FWell, it sure is!\x02\x03",
            "#10102FBecause Mr. Lloyd desperately spoke\x01",
            "He seems to have regained myself!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)
    Sleep(150)

    ChrTalk(
        0x101,
        "#00005F#5PSergeant …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04309F#11PHa ha …\x01",
            "Did you do \"the mission support section\"?\x02\x03",
            "#04302FIf there is another opportunity\x01",
            "Let me hear a detailed story.\x02\x03",
            "The matter of the cult\x01",
            "It was supposed to have been stolen along the way\x01",
            "There may be something again.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1E9B():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1E9B)
    Sleep(50)
    TurnDirection(0x109, 0x8, 500)

    ChrTalk(
        0x101,
        (
            "#00004F#6POkay, I understand.\x02\x03",
            "#00000F… Well then we\x01",
            "Excuse me around here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x109,
        "#6P#10109FThank you for your hard work!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#04311F#11PAh!\x01",
            "It is very tired there.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(500, 1000, 11400, 4000)

    def lambda_1F6D():

        label("loc_1F6D")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_1F6D")

    QueueWorkItem2(0x8, 2, lambda_1F6D)
    BeginChrThread(0x101, 3, 0, 10)
    BeginChrThread(0x109, 3, 0, 11)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x109, 3)
    EndChrThread(0x8, 0x2)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#04300F#11PLloyd, you ……\x01",
            "It seems likely that there is a good chance.\x02\x03",
            "#04304FAs for the power of the escha\x01",
            "She seems to have become a palm.\x02\x03",
            "#04308FSuddenly burned …… just this time\x01",
            "It may be a little bad.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x9, 7100, 0, 2300, 315)
    ClearChrFlags(0x9, 0x80)

    NpcTalk(
        0x9,
        "Daughter's voice",
        "── Kevin.\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(5300, 1000, 3800, 0)
    MoveCamera(83, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    OP_68(2300, 1000, 7800, 3500)
    SetCameraDistance(16500, 3500)

    def lambda_20E5():
        OP_95(0xFE, 3100, 0, 7300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_20E5)
    OP_0D()
    TurnDirection(0x8, 0x9, 500)
    WaitChrThread(0x9, 1)
    TurnDirection(0x9, 0x8, 500)
    EndChrThread(0x8, 0x2)
    OP_6F(0x79)

    ChrTalk(
        0x8,
        (
            "#6P#04302FOh, I guess it was late.\x02\x03",
            "#04305F…… What is that paper bag?\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0x9,
        (
            "I sold it at a stall there\x01",
            "Grilled chestnut of Altair specialties.\x02\x03",
            "Hokkeoku and exquisite sweetness\x01",
            "I have a good job.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    ChrTalk(
        0x8,
        (
            "#6P#04306FThat's why a lot of paper bags\x01",
            "I will not buy it.\x02\x03",
            "#04301FAbsolutely, in such a condition\x01",
            "Are you OK from now?\x02\x03",
            "As I expected, I still have …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#13806F#11P……No good.\x01",
            "Kevin 's infamous name is too known.\x02\x03",
            "#13811FIf the infiltration falls on Archbishop Ellarda\x01",
            "It may be burned out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6P#04305FNo matter how much\x01",
            "It will not be done until that! Is it?\x02\x03",
            "#04308FNo, but even the Liturgy Ministry\x01",
            "Did Owen's case exist …?\x02\x03",
            "#04306FWith that one attitude to the Ministry of Construction\x01",
            "She seems to have hardened more and more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#13803F#11POn that point, if I alone\x01",
            "It is perfect for eye blinders.\x02\x03",
            "#13801FIt's also in Kevin\x01",
            "You know what?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6P#04306FOh no … … I knew!\x02\x03",
            "#04308FNot at all also the president\x01",
            "What's more, thanks ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#13804F#11PAccurate selection.\x02\x03",
            "#13802FKevin is the best while I am away,\x01",
            "Do not be unreasonable.\x02\x03",
            "To Cesar and Marcus\x01",
            "Do not worry too much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6P#04303FOh yeah, I got it.\x02\x03",
            "#04301F… … but leasing.\x01",
            "Honma, Watch out?\x02\x03",
            "The place you go from now\x01",
            "To be honest, nothing is wrong.\x02\x03",
            "When it comes to getting into trouble, I will call myself,\x01",
            "Do you rely on the trump card?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#13805F#11PI know that but ….\x02\x03",
            "#13801F…… So bad situation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#6P#04306FAh……\x01",
            "It is the meaning of both saints and sundries.\x02\x03",
            "#04301FApparently \"people\"\x01",
            "She seems to move secretly.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    SetCameraDistance(17000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    WaitBGM()
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x8,
        (
            "#30WCross Bell City ──\x01",
            "It may be as its name suggests.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CC(0x1, 0xFF, 0x0)
    RemoveParty(0x9, 0xFF)
    RemoveParty(0x7, 0xFF)
    SetScenarioFlags(0x25, 2)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x235), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1500)
    SetScenarioFlags(0x22, 2)
    NewScene("e4800", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_3_419 end

    def Function_4_2753(): pass

    label("Function_4_2753")

    OP_96(0x16, 0xFFFFBF8C, 0x0, 0x445C, 0x1770, 0x0)
    OP_9E(0x16, 0xFFFFBF8C, 0x30D4, 0x15F90, 0x1388, 0x1)
    OP_96(0x16, 0xFFFFD314, 0x0, 0x5DC, 0x1770, 0x0)
    OP_9E(0x16, 0xFFFFBBA4, 0x5DC, 0x15F90, 0x1388, 0x1)
    OP_96(0x16, 0xFFFF9A70, 0x0, 0xFFFFEE6C, 0x1770, 0x0)
    OP_9E(0x16, 0xFFFF9A70, 0xFFFFDAE4, 0xFFFEA070, 0x1388, 0x1)
    OP_96(0x16, 0xFFFF86E8, 0x0, 0xFFFF88DC, 0x1770, 0x0)
    Return()

    # Function_4_2753 end

    def Function_5_27E3(): pass

    label("Function_5_27E3")

    Sleep(5500)
    OP_68(-24960, 1900, -3590, 6000)
    MoveCamera(24, 19, 0, 6000)
    OP_6E(700, 6000)
    SetCameraDistance(24000, 6000)
    OP_6F(0x79)
    Return()

    # Function_5_27E3 end

    def Function_6_2817(): pass

    label("Function_6_2817")

    OP_95(0x12, 0, 0, -10500, 2000, 0x0)
    OP_95(0x12, 4700, 0, -5400, 2000, 0x0)

    def lambda_2844():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_2844)
    TurnDirection(0x12, 0xD, 500)
    BeginChrThread(0x12, 0, 0, 0)
    Sleep(1000)
    OP_63(0x12, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Return()

    # Function_6_2817 end

    def Function_7_286F(): pass

    label("Function_7_286F")

    ClearMapObjFlags(0x0, 0x10)
    OP_74(0x0, 0xA)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)

    def lambda_288D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_288D)
    OP_95(0x13, 10500, 0, 6000, 2000, 0x0)
    OP_95(0x13, 10500, 0, -5000, 2000, 0x0)
    OP_9E(0x13, 0x7D0, 0xFFFFEC78, 0x15F90, 0x7D0, 0x1)
    OP_95(0x13, 2000, 0, -30000, 2000, 0x0)
    OP_70(0x0, 0x0)
    Return()

    # Function_7_286F end

    def Function_8_28EF(): pass

    label("Function_8_28EF")

    OP_95(0x14, 12000, 0, 15500, 2000, 0x0)
    OP_95(0x14, 30000, 0, 15500, 2000, 0x0)

    def lambda_291C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_291C)
    Return()

    # Function_8_28EF end

    def Function_9_2929(): pass

    label("Function_9_2929")

    OP_92(0xFE, 0xFFFFFE70, 0x2EE0, 0x1F4)
    OP_95(0xFE, -400, 0, 12000, 2000, 0x0)

    def lambda_294F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_294F)
    OP_95(0xFE, -400, 150, 13500, 1500, 0x0)
    Return()

    # Function_9_2929 end

    def Function_10_2970(): pass

    label("Function_10_2970")

    OP_92(0xFE, 0xFFFFFE70, 0x4074, 0x1F4)
    OP_95(0xFE, -400, 0, 16500, 2500, 0x0)
    OP_95(0xFE, -400, 1100, 20500, 2500, 0x0)

    def lambda_29AA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_29AA)
    OP_95(0xFE, -400, 1100, 22500, 2500, 0x0)
    Return()

    # Function_10_2970 end

    def Function_11_29CB(): pass

    label("Function_11_29CB")

    Sleep(100)
    OP_92(0xFE, 0xFFFFFDA8, 0x4074, 0x1F4)
    Sleep(300)
    OP_95(0xFE, -600, 0, 16500, 2500, 0x0)
    OP_95(0xFE, -600, 1100, 20500, 2500, 0x0)

    def lambda_2A0B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2A0B)
    OP_95(0xFE, -600, 1100, 22500, 2500, 0x0)
    Return()

    # Function_11_29CB end

    def Function_12_2A2C(): pass

    label("Function_12_2A2C")

    Sleep(2000)
    Sound(467, 0, 80, 0)
    Sleep(200)
    Sound(465, 0, 100, 0)
    Sleep(5300)
    Sound(471, 0, 100, 0)
    Return()

    # Function_12_2A2C end

    def Function_13_2A48(): pass

    label("Function_13_2A48")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-1960, 5600, 11900, 0)
    MoveCamera(40, 14, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(13600, 0)
    SetChrPos(0x101, 80, 0, 15350, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2AB9")
    SetChrPos(0x102, -1100, 0, 15350, 180)
    Jump("loc_2B4C")

    label("loc_2AB9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2ADF")
    SetChrPos(0x103, -1100, 0, 15350, 180)
    Jump("loc_2B4C")

    label("loc_2ADF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2B05")
    SetChrPos(0x104, -1100, 0, 15350, 180)
    Jump("loc_2B4C")

    label("loc_2B05")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2B2B")
    SetChrPos(0x109, -1100, 0, 15350, 180)
    Jump("loc_2B4C")

    label("loc_2B2B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2B4C")
    SetChrPos(0x105, -1100, 0, 15350, 180)

    label("loc_2B4C")

    SetChrPos(0x1A1, 1150, 0, 15350, 180)
    LoadChrToIndex("chr/ch24100.itc", 0x1E)
    LoadChrToIndex("chr/ch41200.itc", 0x1F)
    LoadChrToIndex("chr/ch31400.itc", 0x20)
    LoadChrToIndex("chr/ch31500.itc", 0x21)
    SetChrChipByIndex(0x18, 0x1E)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, -50, 0, 11950, 0)
    SetChrChipByIndex(0x19, 0x1F)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, -840, 0, 11950, 0)
    SetChrChipByIndex(0x1A, 0x1F)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 720, 0, 11950, 0)
    SetChrChipByIndex(0x1B, 0x20)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, -20430, 0, 2990, 45)
    SetChrChipByIndex(0x1C, 0x21)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, -21600, 0, 2950, 45)
    ClearChrFlags(0x17, 0x80)
    OP_78(0xA, 0x17)
    OP_49()
    SetChrPos(0x17, -500, 0, 8940, 0)
    OP_D5(0x17, 0x0, 0x41EB0, 0x0, 0x0)
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xA, 0x1000)
    OP_74(0xA, 0x1E)
    OP_70(0xA, 0x0)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    OP_68(-1960, 1900, 11900, 5000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    ChrTalk(
        0x19,
        (
            "Cross Bell police,\x01",
            "It was a pain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "They are responsible for us,\x01",
            "I will carry it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FThank you\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A1,
        "Ok, thank you ~.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Ok then let's get going\x02",
    )

    CloseMessageWindow()

    def lambda_2D53():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_2D53)

    def lambda_2D60():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_2D60)
    Sleep(300)
    OP_93(0x18, 0xB4, 0x1F4)

    def lambda_2D77():
        OP_95(0xFE, -840, 0, 10950, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_2D77)

    def lambda_2D91():
        OP_95(0xFE, 720, 0, 10950, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_2D91)

    def lambda_2DAB():
        OP_95(0xFE, -50, 0, 10950, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_2DAB)
    WaitChrThread(0x18, 1)
    Sleep(500)
    OP_93(0x18, 0x0, 0x1F4)

    ChrTalk(
        0x18,
        "You guys…\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x18,
        (
            "#5SI will definitely return this borrowing,\x01",
            "Look forward to it!#3S\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1A1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_93(0x1A, 0x10E, 0x1F4)

    ChrTalk(
        0x1A,
        "Ok get in\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x18, 0x1A, 500)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x18,
        (
            "#5SNoisy!\x01",
            "This Ponkotsu soldier!#3S\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    ChrTalk(
        0x18,
        (
            "#5SLadee is more\x01",
            "You treat it graciously!#3S\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A,
        "Wannabes?\x02",
    )

    CloseMessageWindow()
    OP_93(0x19, 0x5A, 0x1F4)

    ChrTalk(
        0x19,
        "It's fine, get her in\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Sound(462, 0, 100, 0)
    OP_74(0xA, 0x1E)
    OP_71(0xA, 0x169, 0x186, 0x1, 0x8)
    Sleep(1500)
    SetChrFlags(0x18, 0x40)
    SetChrFlags(0x18, 0x4)
    SetChrFlags(0x1A, 0x40)
    SetChrFlags(0x1A, 0x4)
    BeginChrThread(0x18, 1, 0, 15)
    BeginChrThread(0x1A, 1, 0, 16)
    WaitChrThread(0x1A, 1)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x1A, 0x80)
    Sound(461, 0, 100, 0)
    OP_71(0xA, 0x187, 0x1A4, 0x1, 0x8)
    Sleep(1500)

    ChrTalk(
        0x101,
        (
            "#00006FWhat, what to say ……\x01",
            "I really hate to appear again.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3045")

    ChrTalk(
        0x102,
        "#00106FI agree …\x02",
    )

    CloseMessageWindow()
    Jump("loc_30F6")

    label("loc_3045")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3071")

    ChrTalk(
        0x103,
        "#00206FAgreed\x02",
    )

    CloseMessageWindow()
    Jump("loc_30F6")

    label("loc_3071")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_309B")

    ChrTalk(
        0x104,
        "#00306FI agree.\x02",
    )

    CloseMessageWindow()
    Jump("loc_30F6")

    label("loc_309B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_30C9")

    ChrTalk(
        0x109,
        "#10106FI'm with you……\x02",
    )

    CloseMessageWindow()
    Jump("loc_30F6")

    label("loc_30C9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_30F6")

    ChrTalk(
        0x105,
        "#10302FHuh, I agree.\x02",
    )

    CloseMessageWindow()

    label("loc_30F6")

    OP_93(0x19, 0x0, 0x1F4)

    ChrTalk(
        0x19,
        (
            "…… so that there is not such a thing,\x01",
            "I am going to do it well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x19,
        (
            "Anyway, it was a pain.\x01",
            "Take care of you guys as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FRight, thanks a lot\x02",
    )

    CloseMessageWindow()
    OP_93(0x19, 0xB4, 0x1F4)
    Sound(462, 0, 100, 0)
    OP_71(0xA, 0xF1, 0x10E, 0x1, 0x8)
    Sleep(1500)
    SetChrFlags(0x19, 0x40)
    SetChrFlags(0x19, 0x4)

    def lambda_31C9():
        OP_95(0xFE, -840, 150, 9610, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_31C9)
    OP_A7(0x19, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Sound(461, 0, 100, 0)
    OP_71(0xA, 0x10F, 0x12C, 0x1, 0x8)
    Sleep(1500)
    Sound(470, 0, 50, 0)
    OP_71(0xA, 0x3C, 0x5A, 0x1, 0x8)
    Sleep(1000)
    Sound(457, 0, 100, 0)
    OP_71(0xA, 0x79, 0xB4, 0x1, 0x20)
    OP_68(-8150, 1900, 6710, 2500)
    MoveCamera(35, 31, 0, 2500)
    OP_6E(580, 2500)
    SetCameraDistance(18500, 2500)
    BeginChrThread(0x17, 1, 0, 17)
    OP_6F(0x79)
    Sleep(2000)
    StopSound(457, 1000, 90)
    Fade(500)
    EndChrThread(0x17, 0x1)
    SetMapObjFlags(0xA, 0x4)
    OP_68(-810, 1900, 13320, 0)
    MoveCamera(27, 23, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(13600, 0)
    SetChrPos(0x101, -200, 0, 15570, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_32D8")
    SetChrPos(0x102, -1040, 0, 14270, 45)
    Jump("loc_336B")

    label("loc_32D8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_32FE")
    SetChrPos(0x103, -1040, 0, 14270, 45)
    Jump("loc_336B")

    label("loc_32FE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3324")
    SetChrPos(0x104, -1040, 0, 14270, 45)
    Jump("loc_336B")

    label("loc_3324")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_334A")
    SetChrPos(0x109, -1040, 0, 14270, 45)
    Jump("loc_336B")

    label("loc_334A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_336B")
    SetChrPos(0x105, -1040, 0, 14270, 45)

    label("loc_336B")

    SetChrPos(0x1A1, 750, 0, 14180, 315)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00003FFuu …\x01",
            "Was it only to do this in the long run?\x02\x03",
            "#00001FSomehow with our own hands\x01",
            "I just wanted to catch it.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3464")

    ChrTalk(
        0x102,
        (
            "#00100FNo … but …\x01",
            "There is no choice.\x02\x03",
            "#00104FEven if I did not escape\x01",
            "I have to do it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3669")

    label("loc_3464")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_34E1")

    ChrTalk(
        0x103,
        (
            "#00200FI understand your feelings … ….\x01",
            "It can not be helped.\x02\x03",
            "#00204FEven if I did not escape\x01",
            "Let's be right.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3669")

    label("loc_34E1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_355A")

    ChrTalk(
        0x104,
        (
            "#00306FIf so to say\x01",
            "I see.\x02\x03",
            "#00300FWell, even if I did not escape\x01",
            "Let's do it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3669")

    label("loc_355A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_35DE")

    ChrTalk(
        0x109,
        (
            "#10106FI agree……\x01",
            "It is a little disappointing.\x02\x03",
            "#10100FBut …\x01",
            "I did not escape\x01",
            "The result is it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3669")

    label("loc_35DE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3669")

    ChrTalk(
        0x105,
        (
            "#10300FHuh, I caught you\x01",
            "It does not change,\x01",
            "Is not it good?\x02\x03",
            "#10304FEven if I did not escape\x01",
            "I have to do it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3669")


    ChrTalk(
        0x1A1,
        (
            "Yes Yes!\x01",
            "I have also been saved a lot!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A1,
        (
            "Well, it was good.\x01",
            "This is the Donovan\x01",
            "I can seem to have a good report ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000Fmy mother……\x01",
            "That's right.\x02\x03",
            "Now……\x01",
            "Well then, in Crosbell City\x01",
            "Are you going to go back?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_379E")

    ChrTalk(
        0x102,
        (
            "#00100FYeah, well.\x01",
            "Not too long to stay here\x01",
            "It will not be good.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38D9")

    label("loc_379E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_37F0")

    ChrTalk(
        0x103,
        (
            "#00200FI agree.\x01",
            "Not too long here\x01",
            "I can not.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38D9")

    label("loc_37F0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_383E")

    ChrTalk(
        0x104,
        (
            "#00300FYou know.\x01",
            "My leisure time to stay long\x01",
            "It looks unlikely.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38D9")

    label("loc_383E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_388E")

    ChrTalk(
        0x109,
        (
            "#10100Fis not it.\x01",
            "I do not have much time to spare\x01",
            "It seems not to be.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38D9")

    label("loc_388E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_38D9")

    ChrTalk(
        0x105,
        (
            "#10300FYeah.\x01",
            "It's too lonely\x01",
            "I think so.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38D9")


    ChrTalk(
        0x1A1,
        (
            "Well, but I'm sorry.\x01",
            "I came to the Republic … ….\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1A1,
        (
            "Well, somewhere\x01",
            "I want to go sightseeing, too ~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006FN-not this time\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x0, 1, 0, 14)
    Sleep(50)
    BeginChrThread(0x1, 1, 0, 14)
    Sleep(50)
    BeginChrThread(0x1A1, 1, 0, 14)
    Sleep(1000)
    OP_68(-18880, 1900, 2270, 5000)
    MoveCamera(41, 24, 0, 5000)
    OP_6E(700, 5000)
    SetCameraDistance(15100, 5000)
    OP_6F(0x79)

    ChrTalk(
        0x1B,
        (
            "What is this ending?\x01",
            "It was unexpected …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "… … Well,\x01",
            "I will not let the remnants escape\x01",
            "The minimum purpose has been reached.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1C,
        (
            "For the time being\x01",
            "I will return to the report.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x1B,
        "Yeah right\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x1A1, 0x1)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x1A1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "After that, Lloyd's are as it is\x01",
            "Wait for the train bound for Crossbell ……\x02\x03",
            "Raymond dressed behind on a souvenir shop\x01",
            "While tilting, I left the Republic.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    SetScenarioFlags(0x22, 6)
    NewScene("c0800", 0, 0, 0)
    IdleLoop()
    EventEnd(0x5)
    Return()

    # Function_13_2A48 end

    def Function_14_3B58(): pass

    label("Function_14_3B58")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3C70")
    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_3B9B"),
        (1, "loc_3BB5"),
        (2, "loc_3BCF"),
        (3, "loc_3BE9"),
        (4, "loc_3C03"),
        (5, "loc_3C1D"),
        (6, "loc_3C37"),
        (SWITCH_DEFAULT, "loc_3C51"),
    )


    label("loc_3B9B")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_3C6B")

    label("loc_3BB5")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2000)
    Jump("loc_3C6B")

    label("loc_3BCF")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(3000)
    Jump("loc_3C6B")

    label("loc_3BE9")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_3C6B")

    label("loc_3C03")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1800)
    Jump("loc_3C6B")

    label("loc_3C1D")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    Jump("loc_3C6B")

    label("loc_3C37")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_3C6B")

    label("loc_3C51")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_3C6B")

    label("loc_3C6B")

    Jump("Function_14_3B58")

    label("loc_3C70")

    Return()

    # Function_14_3B58 end

    def Function_15_3C71(): pass

    label("Function_15_3C71")

    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_3C7D():
        OP_96(0xFE, 0xFFFFFFCE, 0x96, 0x258A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3C7D)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_15_3C71 end

    def Function_16_3C9E(): pass

    label("Function_16_3C9E")

    OP_95(0xFE, -50, 0, 10950, 1000, 0x0)

    def lambda_3CB7():
        OP_95(0xFE, -50, 150, 9610, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3CB7)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_16_3C9E end

    def Function_17_3CD8(): pass

    label("Function_17_3CD8")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -500, 0, 8940)
    OP_9F(0x1, -6550, 0, 8940)
    OP_9F(0x1, -7500, 0, 8400)
    OP_9F(0x1, -8100, 0, 7000)
    OP_9F(0x1, -8200, 0, 4200)
    OP_9F(0x1, -8360, 0, -4860)
    OP_9F(0x2, 0xFE, 4500, 0x6)
    Return()

    # Function_17_3CD8 end

    SaveToFile()

Try(main)
