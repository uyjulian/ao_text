from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t113b.bin",                # FileName
        "t113b",                    # MapName
        "t113b",                    # Location
        0x0049,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 73, 0, 0, 0, 1],
    )

    BuildStringList((
        "t113b",                  # 0
        "Keya",                 # 1
        "Franc",                 # 2
        "Cecil",                 # 3
        "Ilia",                 # 4
        "Lisha",               # 5
        "Shuri",                 # 6
        "Marybele",             # 7
        "Mayor of Dieter",         # 8
        "Erie",                 # 9
        "Tio",                 # 10
        "Randy",               # 11
        "Noel",                 # 12
        "Waji",                   # 13
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(524, 0)                                        # 0

    ScpFunction((
        "Function_0_20C",          # 00, 0
        "Function_1_21C",          # 01, 1
        "Function_2_21D",          # 02, 2
    ))


    def Function_0_20C(): pass

    label("Function_0_20C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_21B")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)

    label("loc_21B")

    Return()

    # Function_0_20C end

    def Function_1_21C(): pass

    label("Function_1_21C")

    Return()

    # Function_1_21C end

    def Function_2_21D(): pass

    label("Function_2_21D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_23A")
    RemoveParty(0x1, 0xFF)
    Jump("loc_279")

    label("loc_23A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_24B")
    RemoveParty(0x2, 0xFF)
    Jump("loc_279")

    label("loc_24B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_25C")
    RemoveParty(0x3, 0xFF)
    Jump("loc_279")

    label("loc_25C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_26D")
    RemoveParty(0x8, 0xFF)
    Jump("loc_279")

    label("loc_26D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_279")
    RemoveParty(0x4, 0xFF)

    label("loc_279")

    LoadChrToIndex("chr/ch08202.itc", 0x1E)
    LoadChrToIndex("chr/ch08502.itc", 0x1F)
    LoadChrToIndex("chr/ch05202.itc", 0x20)
    LoadChrToIndex("chr/ch05102.itc", 0x21)
    LoadChrToIndex("chr/ch07502.itc", 0x22)
    LoadChrToIndex("chr/ch10002.itc", 0x23)
    LoadChrToIndex("chr/ch05502.itc", 0x24)
    LoadChrToIndex("chr/ch05602.itc", 0x25)
    LoadChrToIndex("chr/ch00102.itc", 0x26)
    LoadChrToIndex("chr/ch00202.itc", 0x27)
    LoadChrToIndex("chr/ch00302.itc", 0x28)
    LoadChrToIndex("chr/ch02902.itc", 0x29)
    LoadChrToIndex("chr/ch03002.itc", 0x2A)
    LoadChrToIndex("chr/ch00002.itc", 0x2B)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02800.itp")
    OP_68(2100, 3100, -8280, 0)
    MoveCamera(28, 11, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(26140, 0)
    SetChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0x2B)
    SetChrSubChip(0x101, 0x1)
    SetChrPos(0x101, -2000, 180, -4900, 90)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x1)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -2000, 180, -8900, 90)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x2)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 2000, 180, -16900, 270)
    SetChrChipByIndex(0xC, 0x20)
    SetChrSubChip(0xC, 0x2)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 2000, 180, -8900, 270)
    SetChrChipByIndex(0xB, 0x21)
    SetChrSubChip(0xB, 0x2)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 2000, 180, -6900, 270)
    SetChrChipByIndex(0xA, 0x22)
    SetChrSubChip(0xA, 0x2)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 2000, 180, -12900, 270)
    SetChrChipByIndex(0xD, 0x23)
    SetChrSubChip(0xD, 0x2)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 2000, 180, -10900, 270)
    SetChrChipByIndex(0xE, 0x24)
    SetChrSubChip(0xE, 0x2)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, 2000, 180, -4900, 270)
    SetChrChipByIndex(0xF, 0x25)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 0, 180, -1500, 180)
    SetChrChipByIndex(0x10, 0x26)
    SetChrSubChip(0x10, 0x1)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, -2000, 180, -6900, 90)
    SetChrChipByIndex(0x11, 0x27)
    SetChrSubChip(0x11, 0x1)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, -2000, 180, -10900, 90)
    SetChrChipByIndex(0x12, 0x28)
    SetChrSubChip(0x12, 0x1)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, -2000, 180, -12900, 90)
    SetChrChipByIndex(0x13, 0x29)
    SetChrSubChip(0x13, 0x2)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 2000, 180, -14900, 270)
    SetChrChipByIndex(0x14, 0x2A)
    SetChrSubChip(0x14, 0x1)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, -2000, 180, -14900, 90)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Eventually all Lloyd members,\x01",
            "The guest house guest#4REducation#We gather in between \"…\x02\x03",
            "程なくしてMayor of Dieterと\x01",
            "娘のMarybeleも到着した。\x02\x03",
            "And apologize for late arrival\x01",
            "Mayor of Dieterの挨拶を合図に……\x02\x03",
            "It is luxurious but cozy\x01",
            "The dinner party began.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayBGM("ed7162", 0)
    OP_68(2100, 1100, -8280, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    MoveCamera(32, 11, 0, 100000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    AnonymousTalk(
        0xF,
        (
            "No no, really.\x01",
            "I could not tell you late.\x02\x03",
            "The invited party was delayed\x01",
            "It should not exist as originally.\x02",
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
        0x101,
        (
            "#00004F#6PNo, the mayor is busy\x01",
            "As expected it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#00202F#6PThank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#02904F#11PWell, in the case of your father,\x01",
            "I am busy with my own work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02809F#5PHa ha ha ha.\x01",
            "Well that's true.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#00106F#6PAlready, if the bell ……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#01703F#11PHowever, practice and performance only\x01",
            "I do not know the details, but ……\x02\x03",
            "#01700FI also dared to quite a while\x01",
            "You seem to have made a suggestion?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02804F#5PHaha, in fact from the age of inauguration\x01",
            "In the idea I thought.\x02\x03",
            "Actually at that timing\x01",
            "I did not intend to give out … …\x01",
            "I could not say that.\x02\x03",
            "#02800FSo I was drunk\x01",
            "I got you tossed a rhinoceros.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#01704F#11PHuh, I see.\x02\x03",
            "#01702FAnd the stage where curtains came up\x01",
            "It is necessary to keep dancing until the end …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02803F#5PExactly.\x02\x03",
            "#02800FIf you ask, alkane shell\x01",
            "\"Golden Sun, Silver Moon\"\x01",
            "Trying to challenge renewal.\x02\x03",
            "Actually, the following week of the first show\x01",
            "A referendum on the national independence question\x01",
            "I decided to do it.\x02\x03",
            "#02804FSo, I thought that this was also a borderline,\x01",
            "I will invite you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PIs that so……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#01709F#11PHahaha, thanks to you\x01",
            "I had a good vacation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#01804F#11PThank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#04203F#11P… ….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#05902F#11PHuhu, because I am an outsider\x01",
            "I'm sorry but ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02805F#5PNo, no way.\x02\x03",
            "#02800FFrom officials of Ursula Hospital\x01",
            "I always hear about you rumors.\x02\x03",
            "With the return of the saint Ursula anything\x01",
            "It's like a hard worker told me.\x02\x03",
            "#02809FI am honored to meet you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#05905F#11PSurely, that is\x01",
            "I think whether it is exaggerated … ….\x02\x03",
            "#05904FIt is an honor to be able to say so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#02906F#11PAlright, if your father.\x01",
            "Only female offspring from the past\x01",
            "Praise me ……\x02\x03",
            "#02900FLloyd's also\x01",
            "Labor#2RNekira#How is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02805F#5POops, this is rude.\x02\x03",
            "#02809FNo, nothing but beautiful ladies\x01",
            "It seems that it is rising without age.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F#6Pmy mother……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#00309F#6PWell, but you invited me\x01",
            "It was truly a blessing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#10304F#6P#NYeah.\x01",
            "It became a good change.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x13,
        "#10109F#11PMayor, thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#06409F#11PIt was a lot of fun!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#01109F#6PKeyaも楽しかったー。\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#02804F#5PHaha, that's nothing but something.\x02",
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xF)

    ChrTalk(
        0xF,
        (
            "#02803F#5P── Although it is bad to steam it\x01",
            "That was a truly unhappy incident.\x02\x03",
            "#02801FHow much does the tower blow up\x01",
            "The criminal who tried#6Rterrorist#Although……\x02\x03",
            "Living in such a form\x01",
            "The more you have to drop it\x01",
            "I do not think he was sinful.\x02\x03",
            "#02803FNever again such an incident\x01",
            "I will do my best not to get up.\x02\x03",
            "#02800FIf \"justice\" exists in this world\x01",
            "It is also to encourage everyone to believe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#10108F#11PAh……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6PMayor of Dieter……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#00104F#6P…… If you say so\x01",
            "I feel I could use my chest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#00203F#6PBut I ask about the independence of that independence\x01",
            "It is a referendum … …\x02\x03",
            "#00200FIf the agreement is exceeded,\x01",
            "Is it really possible to be independent?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02806F#5PNo, in the referendum itself\x01",
            "There is no decision power to enable independence.\x02\x03",
            "#02804FHowever, the result is definitely\x01",
            "It should be an indication of intention to foreign countries.\x02\x03",
            "Then gradually form international public opinion,\x01",
            "Somehow from two major powers\x01",
            "Tear off \"independence\" …\x02\x03",
            "#02800FThat's my scenario.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#00303F#6PI see …\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#10302F#6P#NI'm telling you this way\x01",
            "It is quite a steep road, is not it?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x13,
        "#10101F#11Pワ、Waji君……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02803F#5PNo, as you pointed out.\x02\x03",
            "#02801FFrom a geopolitical point of view\x01",
            "Crossbell's national independence is\x01",
            "It is in a very difficult situation ……\x02\x03",
            "#02800FBut, human beings\x01",
            "Just being thrown into the situation\x01",
            "I do not believe it is a living thing.\x02\x03",
            "In pursuit of the ideal even in suffering,\x01",
            "I am proud to be proud … …\x02\x03",
            "#02804FSuch power and possibility\x01",
            "It seems like it is hidden.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#00102F#6P……uncle……\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PTo be proud\x01",
            "Power and possibility, is … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#01808F#11P…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#01704F#11PHmm … I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02803F#5PThe way the crossbell walks in the future\x01",
            "It will be difficult … ….\x02\x03",
            "Of course, we adults\x01",
            "With the preparedness and efforts of the crusher\x01",
            "I will open up that path.\x02\x03",
            "#02800FBut, following that\x01",
            "What aims for height\x01",
            "I think you guys are responsible for young people.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Mayor of Dieterは席を見渡して\x01",
            "I bowed my head deeply.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)

    ChrTalk(
        0xF,
        (
            "#02804F#5PHello everyone, too - ─\x01",
            "In your own way\x01",
            "I want you to do the crossbell tomorrow.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(2100, 1350, -8280, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "After that, the banquet was over,\x01",
            "After returning to hotel's 3F ……\x02\x03",
            "While being enveloped in a magical euphoria\x01",
            "Lloyds who were tired from play\x01",
            "I decided to take a day off as soon as possible.\x02\x03",
            "And ──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x22, 1)
    NewScene("e430B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_21D end

    SaveToFile()

Try(main)
