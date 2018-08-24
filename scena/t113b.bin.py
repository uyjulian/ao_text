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
            "And so, Lloyd and the others\x01",
            "gathered at the guest house\x01",
            "Banquet Hall...\x02\x03",
            "Shortly thereafter, Mayor\x01",
            "Dieter and his daughter\x01",
            "Mariabell arrived.\x02\x03",
            "Then, after Mayor Dieter\x01",
            "greeted everyone and apologized\x01",
            "for his late arrival...\x02\x03",
            "A wonderful though comfortable\x01",
            "dinner party began.\x07\x00\x02",
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
            "No, no, I really am sorry for being\x01",
            "late.\x02\x03",
            "For the host to be late is simply\x01",
            "inexcusable.\x02",
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
            "#00004F#6PWe know how busy you\x01",
            "are, Mr. Mayor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#00202F#6PThank you for all that\x01",
            "you do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#02904F#11PWell in my father's\x01",
            "case, being busy is his\x01",
            "own choice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02809F#5PHah hah hah. Well, it is\x01",
            "as you say.\x02",
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
            "#01703F#11PI've been practicing and\x01",
            "performing so I don't\x01",
            "know the details, but...\x02\x03",
            "#01700FIt seems you made\x01",
            "another drastic\x01",
            "proposal?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02804F#5PHaha. Actually, it's an idea I've\x01",
            "been thinking about ever since I\x01",
            "took office.\x02\x03",
            "Truth is, I didn't intend to\x01",
            "reveal it with this timing, but...\x01",
            "I couldn't stand it anymore.\x02\x03",
            "#02800FAnd so, I resolutely cast the die.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#01704F#11PHuhu, I see.\x02\x03",
            "#01702FAnd now that the curtain has\x01",
            "risen, you have to keep dancing\x01",
            "onstage until the end...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02803F#5PPrecisely.\x02\x03",
            "#02800FI heard that Arc-en-Ciel is\x01",
            "undertaking a renewal of "Golden\x01",
            "Sun, Silver Moon"...\x02\x03",
            "Actually, it has been decided that\x01",
            "the referendum on the question of\x01",
            "state independence will be held the\x01",
            "week after its first performance.\x02\x03",
            "#02804FSo, thinking it was fate, I invited\x01",
            "you.\x02",
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
            "#01709F#11PHuhu. Thanks to you, we\x01",
            "got to enjoy a nice\x01",
            "holiday.\x02",
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
        "#04203F#11P...Thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#05902F#11PHaha. Since I'm an outsider,\x01",
            "maybe it's not appropriate\x01",
            "for me to be here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02805F#5PNo no, not at all.\x02\x03",
            "#02800FI hear rumors about you constantly\x01",
            "from the St. Ursula Hospital staff.\x02\x03",
            "I'm told you're such a hard worker\x01",
            "that you could be the second coming\x01",
            "of St. Ursula herself and such.\x02\x03",
            "#02809FIt's an honor to meet you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#05905F#11PThat's obviously an\x01",
            "exaggeration, but...\x02\x03",
            "#05904FBut I am honored you\x01",
            "would say that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#02906F#11POh, father. You've been doing\x01",
            "nothing but singing the praises\x01",
            "of the young women here...\x02\x03",
            "#02900FHow about a little praise for\x01",
            "Lloyd and the others as well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02805F#5POh, my apologies.\x02\x03",
            "#02809FPardon me. It seems I got more carried\x01",
            "away than a man of my age should because\x01",
            "of all these beautiful young ladies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F#6PHaha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#00309F#6PWell, I'm really glad\x01",
            "you invited us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#10304F#6P#NRight. It made a good\x01",
            "change of pace.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x13,
        (
            "#10109F#11PMr. Mayor, thank you\x01",
            "very much.\x02",
        )
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
        (
            "#02804F#5PHaha, I'm glad to hear\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xF)

    ChrTalk(
        0xF,
        (
            "#02803F#5P─I'm sorry to bring it up\x01",
            "again, but that really was an\x01",
            "unfortunate incident.\x02\x03",
            "#02801FEven though the terrorists did\x01",
            "try to blow up the tower...\x02\x03",
            "I cannot think their sins were\x01",
            "so great as to have their\x01",
            "lives ended in such a manner.\x02\x03",
            "#02803FI intend to work to ensure\x01",
            "that such an incident doesn't\x01",
            "happen again.\x02\x03",
            "#02800FAnd to make everyone believe\x01",
            "that Justice exists in this\x01",
            "world.\x02",
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
            "#00104F#6P...Hearing you say that\x01",
            "makes me feel like a load\x01",
            "has been taken off my chest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#00203F#6PHowever, about the\x01",
            "referendum on the question\x01",
            "of independence...\x02\x03",
            "#00200FIf it is approved, can we\x01",
            "really become independent?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02806F#5PNo, the referendum itself doesn't have the\x01",
            "power to realize the independence.\x02\x03",
            "#02804FHowever, it will be a declaration of intent\x01",
            "to all foreign countries for sure.\x02\x03",
            "Then, international opinion will gradually\x01",
            "take hold, and we will snatch "independence"\x01",
            "from the major powers somehow or other...\x02\x03",
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
            "#10302F#6P#NYou say that, but it's\x01",
            "going to be quite a\x01",
            "tough road ahead, eh?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x13,
        "#10101F#11PW-Wazy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02803F#5PNo, it's like you pointed out.\x02\x03",
            "#02801FEven from a geopolitical point of\x01",
            "view, Crossbell State independence\x01",
            "is a rather complex situation...\x02\x03",
            "#02800FHowever, I believe "man" is not a\x01",
            "thing that lives by merely going\x01",
            "with the flow.\x02\x03",
            "Even if there may be trouble, he\x01",
            "pursues an ideal and works towards\x01",
            "it with pride...\x02\x03",
            "#02804FI feel that "man" has such hidden\x01",
            "power and potential.\x02",
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
            "for the sake of pride...\x01",
            "is it?\x02",
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
        "#01704F#11PHm... I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02803F#5PCrossbell will likely walk a\x01",
            "difficult path going\x01",
            "forward...\x02\x03",
            "Naturally we adults intend to\x01",
            "cut through that path by being\x01",
            "prepared and working hard.\x02\x03",
            "#02800FHowever, it will be the duty\x01",
            "of you young ones to aim high\x01",
            "and continue along it.\x02",
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
            "Mayor Dieter looked over\x01",
            "the seats and bowed very\x01",
            "deeply.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)

    ChrTalk(
        0xF,
        (
            "#02804F#5PI implore all of you─ Please\x01",
            "devote yourselves to Crossbell's\x01",
            "future, each in your own way.\x02",
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
            "Afterwards, the dinner party ended, and\x01",
            "after they returned to the hotel's 3F...\x02\x03",
            "Though enveloped by a mysterious elation,\x01",
            "Lloyd and the others, tired by the fun\x01",
            "day, decided to rest early that night.\x02\x03",
            "And then─\x07\x00\x02",
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
