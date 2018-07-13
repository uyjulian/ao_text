from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e4200.bin",                # FileName
        "e4200",                    # MapName
        "e4200",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e4200",                  # 0
        "Divine Wolf Zeit",       # 1
        "Divine Wolf Zeit",       # 2
        "Lloyd",                  # 3
        "Lloyd",                  # 4
        "SE制御",                 # 5
    ))

    DeclNpc(0,       0,       0,       0,    228,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(20500,   4500,    0,       0,    228,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(15500,   5500,    0,       0,    228,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(16000,   4949,    0,       0,    228,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(328, 0)                                        # 0

    ScpFunction((
        "Function_0_148",          # 00, 0
        "Function_1_158",          # 01, 1
        "Function_2_16D",          # 02, 2
        "Function_3_22ED",         # 03, 3
        "Function_4_2364",         # 04, 4
        "Function_5_2398",         # 05, 5
        "Function_6_23C0",         # 06, 6
        "Function_7_23E8",         # 07, 7
        "Function_8_2405",         # 08, 8
        "Function_9_241B",         # 09, 9
    ))


    def Function_0_148(): pass

    label("Function_0_148")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_157")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)

    label("loc_157")

    Return()

    # Function_0_148 end

    def Function_1_158(): pass

    label("Function_1_158")

    OP_F0(0x1, 0x4B0)
    OP_11(0x7B, 0xB4, 0xD5, 0xA, 0x190, 0x0)
    Return()

    # Function_1_158 end

    def Function_2_16D(): pass

    label("Function_2_16D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51620.itc", 0x20)
    SoundLoad(132)
    SoundLoad(962)
    ClearChrFlags(0x8, 0x80)
    OP_78(0x0, 0x8)
    OP_49()
    SetChrPos(0x8, 16000, 0, 0, 0)
    OP_D5(0x8, 0x0, 0x15F90, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x1000)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0xA, 0x32, 0x1, 0x20)
    SetChrFlags(0x8, 0x1)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x206C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_71(0x0, 0x97, 0xAA, 0x1, 0x20)
    OP_D3(0x101, 0x0, "Null_senaka(42)")
    SetMapObjFrame(0x0, "879mabuta:Layer1(43)", 0x0, 0x1)
    SetMapObjFrame(0x0, "879mabuta:Layer2(44)", 0x0, 0x1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x101, 0x80)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x0)
    OP_52(0x101, 0x24, (scpexpr(EXPR_PUSH_LONG, 0x8C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x101, 0x1)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x1000)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 0x20)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xC, 1, 0, 3)
    BeginChrThread(0xC, 2, 0, 4)
    Sleep(4000)
    PlayBGM("ed7304", 0)
    OP_68(32000, 5000, 0, 0)
    MoveCamera(330, 5, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(69420, 0)
    FadeToBright(1000, 0)
    OP_68(17500, 5800, 0, 6000)
    MoveCamera(320, 18, 0, 6000)
    OP_6E(500, 6000)
    SetCameraDistance(18500, 6000)
    OP_0D()
    OP_6F(0x79)
    EndChrThread(0xC, 0x1)
    EndChrThread(0xC, 0x2)
    OP_68(17550, 6100, 0, 30000)
    MoveCamera(326, 3, 0, 30000)
    OP_6E(500, 30000)
    SetCameraDistance(15500, 30000)
    Sleep(500)

    ChrTalk(
        0xA,
        "#00011F#5PA Goddess-sent divine beast...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PHm, it's quicker if you think\x01",
            "about me in those terms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PThe great "Sept-Terrions" were once\x01",
            "bestowed upon man by the Goddess...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PWe're those who keep existing\x01",
            "in order to watch man's future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#00003F#5P"We"...you mean that...\x02\x03",
            "#00001FEven the "dragon" that appeared\x01",
            "during the Liberl phenomenon...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PHm, you really are sharp.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PThat dragon, Ragnard, is indeed\x01",
            "one of my brethren too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PHe remained in the land of Liberl to\x01",
            "protect the "Sept-Terrion of Space", but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PEven I don't know where he disappeared to,\x01",
            "now that he's been untied from his "duty".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#00006F#5PI hardly get it, but...\x02\x03",
            "#00008FBut then, you too have been staying\x01",
            "in Crossbell since a long time ago...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PHm, since before the "Great Collapse"\x01",
            "of 1200 years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PWhy did the former "Sept-Terrion of\x01",
            "Mirage" ended up disappearing...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PAnd what was done afterwards\x01",
            "to revive that Sept-Terrion...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PI know those things to a certain degree.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(17150, 6100, 0, 0)
    MoveCamera(313, 3, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(12500, 0)
    Fade(500)
    OP_0D()
    BeginChrThread(0x101, 1, 0, 8)
    WaitChrThread(0x101, 1)
    OP_63(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xB)
    Sleep(500)

    ChrTalk(
        0xA,
        (
            "#00006F#5P...Honestly, even if we researched\x01",
            "that part, we couldn't understand it.\x02\x03",
            "#00008FA Goddess' Sept-Terrion...\x01",
            "That the Crois clan inherited...\x02\x03",
            "Why was the Sept-Terrion lost?\x01",
            "Why KeA ended up being\x01",
            "burdened with such a role...?\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 1, 0, 9)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0xA,
        (
            "#00001F#5P──I beg you.\x01",
            "Please, tell me...\x02\x03",
            "The events of 1200 years ago.\x02\x03",
            "And what happened to\x01",
            "KeA 500 years ago.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(18000, 5500, 0, 2500)
    MoveCamera(310, 3, 0, 2500)
    OP_6E(500, 2500)
    SetCameraDistance(11000, 2500)
    Sleep(1000)

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P──Very well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PWell, that's why I\x01",
            "appeared to you.\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()
    Sleep(300)
    SetMapObjFrame(0x0, "879mabuta:Layer1(43)", 0x1, 0x1)
    SetMapObjFrame(0x0, "879mabuta:Layer2(44)", 0x1, 0x1)
    StopBGM(0x1770)
    StopSound(132, 4000, 100)
    StopSound(962, 4000, 60)
    Sleep(800)

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PThe Sept-Terrion handed down to this land...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PIt was called "Demiourgos",\x01",
            "the god that governs "Mirage".\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7573", 0)
    Sleep(800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P"Mirage" is an attribute that controls perception\x01",
            "and cognizance. Furthermore, it governs "karma".\x02\x03",
            "There was something that a part of the humans,\x01",
            "with the Crois clan of back then at the centre\x01",
            "who had the Sept-Terrion's power, wanted...\x02\x03",
            "And that was the role of a "God" of the surface...\x01",
            "Instead of Aidios.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFF000000, 0x0, "c_vis272.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(0, 170, -1, -1)

    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PTo guide the humans by knowing man, knowing\x01",
            "all of the surface, controlling karma...\x02\x03",
            "Apparently, it was something that \x01",
            "even the "Aureole" that limitlessly\x01",
            "granted man's desires, had too.\x02\x03",
            "However, in the case of "Demiourgos"...\x01",
            "It did the same without making mistakes\x01",
            "by being able to award an eminent personality.\x02\x03",
            "Wisdom and discernment to guide on the right\x01",
            "path without corrupting man in the end...\x02\x03",
            "With that power, it should've been able to guide\x01",
            "on the correct path the existence called "man".\x02\x03",
            "──That is, until the Sept-Terrion\x01",
            "own "soul" didn't reach the limit.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFF000000, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFF000000, 0x0, "c_vis273.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(250, 160, -1, -1)

    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PAll the human's "natures" and "karmas",\x01",
            "all the world's irrationalities──\x02\x03",
            "Comprehending those and guiding means\x01",
            "to have the same human "emotions".\x02\x03",
            "So "Demiourgos"'s "soul" gradually\x01",
            "broke and fell ill.\x02\x03",
            ""If it keeps going like this, in time I will go \x01",
            "berserk and hurt the people I should protect..."\x02\x03",
            "The Sept-Terrion who understood that──\x01",
            "After much worries, took a decision.\x02\x03",
            "To dissolve his own karma...\x01",
            "The path to disappear from this world.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_68(16500, 5800, 0, 0)
    MoveCamera(322, 6, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16000, 0)
    Sound(223, 0, 60, 0)
    Sound(934, 0, 70, 0)
    FadeToDark(0, 16777215, -1)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x7D0, 0x0, 0x0)
    Sleep(1000)
    Sound(934, 0, 40, 0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(700)
    Sound(132, 2, 100, 0)
    Sound(962, 2, 60, 0)
    Sleep(300)
    FadeToBright(1500, 16777215)
    OP_0D()
    SetMapObjFrame(0x0, "879mabuta:Layer1(43)", 0x0, 0x1)
    SetMapObjFrame(0x0, "879mabuta:Layer2(44)", 0x0, 0x1)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#00006F#5P...That's what happened...\x02\x03",
            "#00013FBut then, the people\x01",
            "who were left behind...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PHm──they were earnestly bewildered, in sorrow\x01",
            "and scared by the Sept-Terrion's disappearance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PThen, without reflecting upon why \x01",
            "things went that way and about what \x01",
            "the Sept-Terrion was thinking...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PThey became obsessed to create an\x01",
            "existence equal to the lost Sept-Terrion.\x02",
        )
    )

    CloseMessageWindow()
    StopSound(132, 1500, 100)
    StopSound(962, 1500, 60)
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P──Naturally, at the very beginning,\x01",
            "it was just fumbling.\x02\x03",
            "However, across 700 years,\x01",
            "while they gathered many kinds of knowledge,\x01",
            "they worked out a peculiar technique.\x02\x03",
            "Namely, the witchcraft called "Alchemy"\x01",
            "that can bring forth matter from nothing.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFF000000, 0x0, "c_vis274.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(0, 170, -1, -1)

    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PThen, they made an outrageous\x01",
            "grand plan in this land.\x02\x03",
            "They prepared a puppet, a "Cult".\x01",
            "They entrusted them an existence that\x01",
            "would've become the new Sept-Terrion's \x01",
            ""core" and had them raise it...\x02\x03",
            "Then, they prepared in this land\x01",
            "massive "rituals" to which it was applied,\x01",
            "to the extreme, the concept of "education"...\x02\x03",
            "This was the plan the alchemists\x01",
            "of the Crois clan had started──\x01",
            "Several hundred years ago.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFF000000, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFF000000, 0x0, "c_vis275.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(180, 170, -1, -1)

    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PFor that to be financially feasible,\x01",
            "they decided to don the outward\x01",
            "mask of "bankers"...\x02\x03",
            "On the other hand, the "Cult" began\x01",
            "to move to awaken the "core" that was\x01",
            "given to them as an object of worship.\x02\x03",
            "Then, 500 years passed──\x01",
            "And that's how we reached this situation.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFF000000, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    OP_68(17150, 6100, 0, 0)
    MoveCamera(315, 3, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(12500, 0)
    Sound(132, 2, 100, 0)
    Sound(962, 2, 60, 0)
    SetChrSubChip(0x101, 0x2)
    FadeToBright(1500, 0)
    OP_0D()
    OP_63(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xB)

    ChrTalk(
        0xA,
        (
            "#00006F#5P...That's an absurd story.\x02\x03",
            "#00008FBut I feel that...I can finally\x01",
            "begin to see the full picture.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 1, 0, 9)
    WaitChrThread(0x101, 1)
    OP_68(17500, 5800, 0, 2500)

    ChrTalk(
        0xA,
        (
            "#00003F#5P──Zeit.\x01",
            "Miss Mariabell said that KeA\x01",
            "is the "Sept-Terrion of Zero".\x02\x03",
            "#00013FWhat did she mean?\x02\x03",
            "Is that another different thing from\x01",
            "the lost "Sept-Terrion of Mirage"?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PUnfortunately...\x01",
            "I don't know about what you're asking me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PProbably, the Crois clan caught hold\x01",
            "of "something" at the end of their deep\x01",
            "rooted delusion spanning 1200 years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PBecause of that, not only\x01",
            "they reproduced an existence\x01",
            "equal to "Demiourgos"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PBut it seems they completed a Sept-Terrion\x01",
            "which holds powers surpassing his.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0xC, 1, 0, 5)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis276.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(0, 160, -1, -1)

    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P──The powers of that white doll.\x02\x03",
            "Those are not the doll's,\x01",
            "but the "Sept-Terrion"'s.\x02",
        )
    )

    CloseMessageWindow()
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis277.itp")
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CC(0x1, 0x0, 0x0)
    Sleep(300)
    SetMessageWindowPos(0, 150, -1, -1)

    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PAlso, the "Sept-Terrion of Mirage"\x01",
            "didn't posses powers that could do\x01",
            "such a thing in mere moments.\x02",
        )
    )

    CloseMessageWindow()
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis278.itp")
    OP_CB(0x0, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CC(0x1, 0x1, 0x0)
    Sleep(300)
    SetMessageWindowPos(0, 150, -1, -1)

    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PIf anything, the power to make\x01",
            "space disappear origins in the \x01",
            "attribute of "Space".\x02\x03",
            "Assuming that that isn't all...\x01",
            "Even I can't fathom how much\x01",
            "latent faculties it has.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0xC, 2, 0, 6)
    OP_68(17150, 6100, 0, 0)
    MoveCamera(315, 3, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(12500, 0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#00008F#5P...I see...\x02\x03",
            "#00003F............\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xB)
    Sleep(500)

    ChrTalk(
        0xA,
        (
            "#00006F#5P──Tell me one more thing.\x02\x03",
            "#00008FAccording to what I've\x01",
            "heard until now, that kid...\x02\x03",
            "#00001F...KeA...\x01",
            "Is not a human being?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P......Hm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PShe is and she is not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PShe's a made existence as a "core"\x01",
            "to reproduce a "Sept-Terrion"──\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PShe's probably a "Homunculus" that was\x01",
            "educated with alchemy's secret techniques.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#00008F#30W#5P............\x02",
    )

    CloseMessageWindow()
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis279.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis280.itp")
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CC(0x1, 0x0, 0x0)
    Sleep(300)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis281.itp")
    OP_CB(0x0, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CC(0x1, 0x1, 0x0)
    Sleep(300)
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis282.itp")
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CC(0x1, 0x0, 0x0)
    Sleep(300)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(300)
    BeginChrThread(0x101, 1, 0, 8)
    WaitChrThread(0x101, 1)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#00006F#5P#30W(Maybe... She had known about\x01",
            "that already for a while, but...)\x02\x03",
            "(But in front of us,\x01",
            "she smiled like that...)\x02\x03",
            "#00008F(......KeA......)\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 2, 0, 7)
    MoveCamera(30, 5, 0, 6000)
    OP_6E(500, 6000)
    SetCameraDistance(52000, 6000)
    Sleep(1000)
    OP_68(12000, 5000, 0, 5000)
    StopBGM(0x1770)
    Sleep(2000)
    StopSound(132, 4000, 100)
    StopSound(962, 4000, 60)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitBGM()
    EndChrThread(0xC, 0x1)
    EndChrThread(0xC, 0x2)
    SetScenarioFlags(0x22, 0)
    NewScene("e4100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_16D end

    def Function_3_22ED(): pass

    label("Function_3_22ED")

    Sound(132, 2, 20, 0)
    Sleep(200)
    OP_25(0x84, 0x19)
    Sleep(200)
    OP_25(0x84, 0x1E)
    Sleep(200)
    OP_25(0x84, 0x23)
    Sleep(200)
    OP_25(0x84, 0x28)
    Sleep(200)
    OP_25(0x84, 0x2D)
    Sleep(200)
    OP_25(0x84, 0x32)
    Sleep(200)
    OP_25(0x84, 0x37)
    Sleep(200)
    OP_25(0x84, 0x3C)
    Sleep(200)
    OP_25(0x84, 0x41)
    Sleep(200)
    OP_25(0x84, 0x46)
    Sleep(2000)
    OP_25(0x84, 0x4B)
    Sleep(200)
    OP_25(0x84, 0x50)
    Sleep(200)
    OP_25(0x84, 0x55)
    Sleep(200)
    OP_25(0x84, 0x5A)
    Sleep(200)
    OP_25(0x84, 0x5F)
    Sleep(200)
    OP_25(0x84, 0x64)
    Return()

    # Function_3_22ED end

    def Function_4_2364(): pass

    label("Function_4_2364")

    Sleep(200)
    Sound(962, 2, 30, 0)
    Sleep(2000)
    OP_25(0x3C2, 0x23)
    Sleep(400)
    OP_25(0x3C2, 0x28)
    Sleep(400)
    OP_25(0x3C2, 0x2D)
    Sleep(400)
    OP_25(0x3C2, 0x32)
    Sleep(400)
    OP_25(0x3C2, 0x37)
    Sleep(400)
    OP_25(0x3C2, 0x3C)
    Return()

    # Function_4_2364 end

    def Function_5_2398(): pass

    label("Function_5_2398")

    OP_25(0x3C2, 0x37)
    Sleep(100)
    OP_25(0x3C2, 0x32)
    Sleep(100)
    OP_25(0x3C2, 0x2D)
    Sleep(100)
    OP_25(0x3C2, 0x28)
    Sleep(100)
    OP_25(0x3C2, 0x23)
    Sleep(100)
    OP_25(0x3C2, 0x1E)
    Return()

    # Function_5_2398 end

    def Function_6_23C0(): pass

    label("Function_6_23C0")

    OP_25(0x3C2, 0x23)
    Sleep(100)
    OP_25(0x3C2, 0x28)
    Sleep(100)
    OP_25(0x3C2, 0x2D)
    Sleep(100)
    OP_25(0x3C2, 0x32)
    Sleep(100)
    OP_25(0x3C2, 0x37)
    Sleep(100)
    OP_25(0x3C2, 0x3C)
    Return()

    # Function_6_23C0 end

    def Function_7_23E8(): pass

    label("Function_7_23E8")

    SetChrSubChip(0x101, 0x1)
    Sleep(150)
    SetChrSubChip(0x101, 0x0)
    Sleep(850)
    SetChrSubChip(0x101, 0x4)
    Sleep(1500)
    SetChrSubChip(0x101, 0x5)
    Sleep(1000)
    Return()

    # Function_7_23E8 end

    def Function_8_2405(): pass

    label("Function_8_2405")

    SetChrSubChip(0x101, 0x0)
    Sleep(100)
    SetChrSubChip(0x101, 0x1)
    Sleep(150)
    SetChrSubChip(0x101, 0x2)
    Sleep(200)
    Return()

    # Function_8_2405 end

    def Function_9_241B(): pass

    label("Function_9_241B")

    SetChrSubChip(0x101, 0x2)
    Sleep(100)
    SetChrSubChip(0x101, 0x1)
    Sleep(150)
    SetChrSubChip(0x101, 0x0)
    Sleep(200)
    Return()

    # Function_9_241B end

    SaveToFile()

Try(main)
