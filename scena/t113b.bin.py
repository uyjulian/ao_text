from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "KeA",                    # 1
        "Fran",                   # 2
        "Cecil",                  # 3
        "Ilya",                   # 4
        "Rixia",                  # 5
        "Sully",                  # 6
        "Mariabell",              # 7
        "Mayor Dieter",           # 8
        "Elie",                   # 9
        "Tio",                    # 10
        "Randy",                  # 11
        "Noｱl",                  # 12
        "Wazy",                   # 13
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
            "Before long, Lloyd and the others all\x01",
            "gathered at the guest house "banquet hall".\x02\x03",
            "Shortly thereafter, Mayor Dieter and\x01",
            "her daughter Mariabell arrived too.\x02\x03",
            "Then, with the greetings of\x01",
            "Mayor Dieter who had arrived late...\x02\x03",
            "A wonderful though comfortable\x01",
            "dinner party started.\x07\x00\x02",
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
            "My my, I'm really sorry\x01",
            "for having arrived late.\x02\x03",
            "It's unforgivable that who has\x01",
            "invited you arrives late.\x02",
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
            "#00004F#6PNo, we know very well that\x01",
            "you're busy, Mayor Dieter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        "#00202F#6PThank you for all you do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#02904F#11PWell, in case of my father the fact that he's\x01",
            "busy is the consequence of what he sows.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02809F#5PHah hah hah.\x01",
            "Well, it's as you say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#00106F#6POh, Bell...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#01703F#11PDue to only practicing and performing\x01",
            "I don't know the details well, but...\x02\x03",
            "#01700FIt seems you did another \x01",
            "quite drastic proposal?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02804F#5PHa ha, actually that was an idea I thought\x01",
            "of since my assumption of office.\x02\x03",
            "The truth is that I didn't intend\x01",
            "to use it at that point, but...\x01",
            "I couldn't stand it anymore.\x02\x03",
            "#02800FAnd so, I resolutely\x01",
            "cast the die.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#01704F#11PHu hu, I see.\x02\x03",
            "#01702FSo you have to keep dancing until the end\x01",
            "on the stage with the curtain risen...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02803F#5PPrecisely.\x02\x03",
            "#02800FI heard that Arc-en-ciel is\x01",
            "undertaking a renewal of\x01",
            ""Golden Sun, Silver Moon"...\x02\x03",
            "Actually, I decided to carry out the\x01",
            "local referendum to question the state\x01",
            "independence proposal on the following\x01",
            "week of your first performance.\x02\x03",
            "#02804FSo, thinking it was fate,\x01",
            "I allowed myself to invite you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PIs that so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#01709F#11PHu hu, thanks to you,\x01",
            "we could spend a fun break.\x02",
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
        "#04203F#11P...Thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#05902F#11PUh uh, since I am an outsider, maybe\x01",
            "it is not appropriate to be here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02805F#5PNo no, not at all.\x02\x03",
            "#02800FYou're someone related to St. Ursula Hospital\x01",
            "and I always hear rumors about you.\x02\x03",
            "Like you're a hard worker said to be\x01",
            "Saint Ursula's second coming and so on...\x02\x03",
            "#02809FIt's an honor to meet you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#05905F#11PA-As you might expect,\x01",
            "I think that is an exaggeration...\x02\x03",
            "#05904FBut I am honored to be told that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#02906F#11POh, father.\x01",
            "Since before you did nothing but\x01",
            "singing the praise of the young women...\x02\x03",
            "#02900FWhat about praising Lloyd\x01",
            "and the others a little too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02805F#5POh, my apologies.\x02\x03",
            "#02809FDear me, it seems that I was elated despite\x01",
            "my age due to all the beautiful young ladies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F#6PHa ha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#00309F#6PWell, I'm really happy\x01",
            "you invited us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#10304F#6P#NRight.\x01",
            "It was a good change of pace.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x13,
        "#10109F#11PMayor, thank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#06409F#11PIt was super fun!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#01109F#6PKeA had fun too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        "#02804F#5PHa ha, I'm glad to hear that.\x02",
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xF)

    ChrTalk(
        0xF,
        (
            "#02803F#5P──I'm sorry to bring it up again,\x01",
            "but that was really an unfortunate incident.\x02\x03",
            "#02801FNo matter that the terrorists\x01",
            "tried even to blow up the tower...\x02\x03",
            "I can't think they were\x01",
            "sinful to have to lose\x01",
            "their lives in that way.\x02\x03",
            "#02803FI intend to exert myself so that such\x01",
            "an incident doesn't happen again.\x02\x03",
            "#02800FAlso to make everyone believe\x01",
            "that "justice" exists in this world.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        "#10108F#11PAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6PMayor Dieter...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#00104F#6P...Hearing you say that I feel like what I \x01",
            "had been weighing on my mind has gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#00203F#6PHowever, about that local referendum\x01",
            "to question the independence...\x02\x03",
            "#00200FIn case it is approved, can we\x01",
            "really become independent?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02806F#5PNo, the local referendum itself doesn't have\x01",
            "the power to to realize the independence.\x02\x03",
            "#02804FHowever, its result will become a declaration\x01",
            "of intent to all the other countries, for sure.\x02\x03",
            "Then, an international public opinion will\x01",
            "gradually form and we will possibly snatch\x01",
            ""independence" from the two major powers.\x02\x03",
            "#02800FThat's my scenario.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        "#00303F#6PI get it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#10302F#6P#NYou say it like this, but it's going to\x01",
            "be quite a tough road ahead, eh?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x13,
        "#10101F#11PW-Wazy...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02803F#5PWell, it's like you pointed out.\x02\x03",
            "#02801FEven from a geopolitical point of view,\x01",
            "the state independence of Crossbell\x01",
            "is a pretty complex situation...\x02\x03",
            "#02800FHowever, I believe that "man"\x01",
            "is not just a living being to be\x01",
            "swept away by the state of things.\x02\x03",
            "Even in time of trouble, it pursues \x01",
            "an ideal and it aims at it with pride...\x02\x03",
            "#02804FI feel that "man" has such\x01",
            "hidden power and potential.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        "#00102F#6P..."Uncle"...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PA power and potential\x01",
            "to be proud of...is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#01808F#11P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#01704F#11PHm...I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02803F#5PThe path Crossbell will walk on in \x01",
            "the future could be a difficult one...\x02\x03",
            "Naturally we adults intend to cut \x01",
            "through that path by being very \x01",
            "prepared and with great efforts.\x02\x03",
            "#02800FHowever, it will be the duty\x01",
            "of you young ones to aim\x01",
            "high following on that path.\x02",
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
            "Mayor Dieter took an extensive view\x01",
            "of the seats and bowed very deeply.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)

    ChrTalk(
        0xF,
        (
            "#02804F#5PPlease, you too──\x01",
            "I want you to devote yourselves to Crossbell\x01",
            "future doing things in your own way.\x02",
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
            "Afterwards, the dinner party ended...\x01",
            "And after having gone back to the hotel 3F...\x02\x03",
            "Although enveloped in a mysterious elation,\x01",
            "Lloyd and the others, tired by the fun day,\x01",
            "decided to go rest early.\x02\x03",
            "Then──\x07\x00\x02",
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
