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
        "Function_3_21E6",         # 03, 3
        "Function_4_225D",         # 04, 4
        "Function_5_2291",         # 05, 5
        "Function_6_22B9",         # 06, 6
        "Function_7_22E1",         # 07, 7
        "Function_8_22FE",         # 08, 8
        "Function_9_2314",         # 09, 9
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
        (
            "#00011F#5PA Goddess-sent divine\x01",
            "beast...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PYes, it's quicker if you\x01",
            "think of me in those\x01",
            "terms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PThe great Sept-Terrions\x01",
            "were once bestowed upon\x01",
            "man by the Goddess...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PWe are they who continue\x01",
            "to exist to keep watch\x01",
            "over man's future.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#00003F#5PBy "We", you mean...\x02\x03",
            "#00001FEven the "dragon" that\x01",
            "appeared during the\x01",
            "Liberl phenomenon...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PHm, you really are quite\x01",
            "sharp.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PThat dragon, Ragnard, is\x01",
            "indeed one of my\x01",
            "brethren.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PHe remained in the land of\x01",
            "Liberl to protect the Sept-\x01",
            "Terrion of Space, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PEven I don't know where he\x01",
            "disappeared to, now that he's\x01",
            "been released from his "duty".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#00006F#5PI-I don't really get\x01",
            "it...\x02\x03",
            "#00008FBut then, you've been in\x01",
            "this land of Crossbell\x01",
            "for a long time...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PYes, since before the\x01",
            "Great Collapse 1200\x01",
            "years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PWhy did the former Sept-\x01",
            "Terrion of Mirage\x01",
            "disappear...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PAnd afterwards, what was\x01",
            "done to revive that\x01",
            "Sept-Terrion...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PI know those things to a\x01",
            "certain degree.\x02",
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
            "#00006F#5P...Honestly, even if we tried\x01",
            "to research those things,\x01",
            "there'd be parts we couldn't.\x02\x03",
            "#00008FOne of the Goddess' Sept-\x01",
            "Terrion... that the Crois\x01",
            "clan inherited...\x02\x03",
            "Why was the Sept-Terrion\x01",
            "lost? Why did KeA have to be\x01",
            "burdened with such a role...?\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 1, 0, 9)
    WaitChrThread(0x101, 1)

    ChrTalk(
        0xA,
        (
            "#00001F#5P─I beg you. Please, tell\x01",
            "me...\x02\x03",
            "The events of 1200 years\x01",
            "ago.\x02\x03",
            "And what happened to KeA\x01",
            "500 years ago as well.\x02",
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
            "#11P─Very well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PWell, that's why I\x01",
            "appeared before you.\x02",
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
            "#11PThe Sept-Terrion handed\x01",
            "down to this land...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PIt was called\x01",
            "Demiourgos, the god that\x01",
            "governs "Mirage".\x02",
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
            "#11P"Mirage" is an attribute that controls\x01",
            "perception and cognizance. Furthermore, it\x01",
            "governs Fate.\x02\x03",
            "There was something that some humans, with\x01",
            "the Crois clan of back then with the Sept-\x01",
            "Terrion's power at the center, wanted...\x02\x03",
            "And that was the role of a God of the\x01",
            "surface... instead of Aidios.\x07\x00\x02",
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
            "#11PTo guide mankind by knowing humans,\x01",
            "knowing the entire world and\x01",
            "controlling fate...\x02\x03",
            "At first glance, it could be understood\x01",
            "as similar to the Aureole that granted\x01",
            "human desires without limit.\x02\x03",
            "However, Demiourgos avoided the same\x01",
            "faults by choosing eminent personality.\x02\x03",
            "In the end, it had wisdom and judgment\x01",
            "to guide humans without corrupting\x01",
            "them...\x02\x03",
            "With those powers, it should have been\x01",
            "able to guide the existence called\x01",
            ""man" on the correct path.\x02\x03",
            "─That is, if the "heart" of the Sept-\x01",
            "Terrion itself had not reached its\x01",
            "limit.\x07\x00\x02",
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
            "#11PAll of human nature and fate,\x01",
            "all the world's\x01",
            "irrationalities─\x02\x03",
            "Comprehending them and guiding\x01",
            "is the same as having human\x01",
            ""emotions".\x02\x03",
            "And so, Demiourgos' "heart"\x01",
            "gradually deteriorated and\x01",
            "fell ill.\x02\x03",
            ""At this rate, I will\x01",
            "eventually go berserk and harm\x01",
            "those I should protect"...\x02\x03",
            "The Sept-Terrion sensed this─\x01",
            "And after much worry, reached\x01",
            "a decision.\x02\x03",
            "It would unbind its own fate,\x01",
            "and disappear from this world.\x02",
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
            "#00006F#5P...That much, huh...\x02\x03",
            "#00013FBut then, the people who\x01",
            "were left behind...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PYes─ They were earnestly\x01",
            "bewildered, sorrowed and scared by\x01",
            "the Sept-Terrion's disappearance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PThen, without reflecting upon\x01",
            "why it happened or what the\x01",
            "Sept-Terrion was thinking...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PThey became obsessed with the\x01",
            "creation of an existence equal\x01",
            "to the lost Sept-Terrion.\x02",
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
            "#11P─Naturally, at the very\x01",
            "beginning, it was just fumbling.\x02\x03",
            "However, across 700 years, they\x01",
            "gathered much knowledge and\x01",
            "worked out a peculiar technique.\x02\x03",
            "Namely, the witchcraft called\x01",
            "Alchemy that can bring forth\x01",
            "matter from nothing.\x07\x00\x02",
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
            "#11PThen, they made a grand plan for this land.\x02\x03",
            "They prepared a puppet, a Cult. They entrusted\x01",
            "them an existence that would become the new\x01",
            "Sept-Terrion's "core" and had them raise it...\x02\x03",
            "Then, in the name of "education", they\x01",
            "prepared massive "rituals" in this land...\x02\x03",
            "This was the plan the alchemists of the Crois\x01",
            "clan started─ several hundred years ago.\x07\x00\x02",
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
            "#11PFor that to be financially\x01",
            "feasible, they decided to don the\x01",
            "outward mask of "bankers"...\x02\x03",
            "On the other hand, the Cult began\x01",
            "to awaken the "core" that was given\x01",
            "to them as an object of worship.\x02\x03",
            "Then, 500 years passed─ which\x01",
            "brings us to the current situation.\x07\x00\x02",
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
            "#00006F#5P...That's an absurd\x01",
            "story.\x02\x03",
            "#00008FBut I feel that... I can\x01",
            "finally begin to see the\x01",
            "full picture.\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 1, 0, 9)
    WaitChrThread(0x101, 1)
    OP_68(17500, 5800, 0, 2500)

    ChrTalk(
        0xA,
        (
            "#00003F#5P─Zeit. Mariabell said\x01",
            "that KeA is the Sept-\x01",
            "Terrion of Zero.\x02\x03",
            "#00013FWhat did she mean?\x02\x03",
            "Is that different from\x01",
            "the lost Sept-Terrion of\x01",
            "Mirage?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PUnfortunately... I do\x01",
            "not know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PMost likely, the Crois clan grabbed\x01",
            "hold of "something" during their deep\x01",
            "rooted delusion spanning 1200 years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PBecause of that, they not\x01",
            "only reproduced an existence\x01",
            "equal to Demiourgos...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PBut it seems they produced\x01",
            "a Sept-Terrion holding\x01",
            "powers surpassing its.\x02",
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
            "#11P─The powers of that\x01",
            "white doll.\x02\x03",
            "Those are not the\x01",
            "doll's, but the Sept-\x01",
            "Terrion's.\x02",
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
            "#11PAlso, the Sept-Terrion of Mirage\x01",
            "didn't posses powers that could\x01",
            "do such things in mere moments.\x02",
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
            "#11PIf pushed, I'd say the power to\x01",
            "create void lies in the attribute\x01",
            "of "Space".\x02\x03",
            "If that isn't the limit of its\x01",
            "abilities... I can only imagine\x01",
            "what sort of powers it might have.\x07\x00\x02",
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
            "#00006F#5P─Tell me one more thing.\x02\x03",
            "#00008FAccording to what I've\x01",
            "heard until now, that\x01",
            "kid...\x02\x03",
            "#00001F...KeA... She's not a\x01",
            "human being?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P......Yes.\x02",
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
            "#11PShe is a created\x01",
            "existence to serve as the\x01",
            ""core" of a Sept-Terrion─\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11PMost likely a Homunculus\x01",
            "created using the secret\x01",
            "techniques of alchemy.\x02",
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
            "#00006F#5P#30W(She has probably known\x01",
            "that for quite a while,\x01",
            "but...)\x02\x03",
            "(But in front of us, she\x01",
            "smiled like that...)\x02\x03",
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

    def Function_3_21E6(): pass

    label("Function_3_21E6")

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

    # Function_3_21E6 end

    def Function_4_225D(): pass

    label("Function_4_225D")

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

    # Function_4_225D end

    def Function_5_2291(): pass

    label("Function_5_2291")

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

    # Function_5_2291 end

    def Function_6_22B9(): pass

    label("Function_6_22B9")

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

    # Function_6_22B9 end

    def Function_7_22E1(): pass

    label("Function_7_22E1")

    SetChrSubChip(0x101, 0x1)
    Sleep(150)
    SetChrSubChip(0x101, 0x0)
    Sleep(850)
    SetChrSubChip(0x101, 0x4)
    Sleep(1500)
    SetChrSubChip(0x101, 0x5)
    Sleep(1000)
    Return()

    # Function_7_22E1 end

    def Function_8_22FE(): pass

    label("Function_8_22FE")

    SetChrSubChip(0x101, 0x0)
    Sleep(100)
    SetChrSubChip(0x101, 0x1)
    Sleep(150)
    SetChrSubChip(0x101, 0x2)
    Sleep(200)
    Return()

    # Function_8_22FE end

    def Function_9_2314(): pass

    label("Function_9_2314")

    SetChrSubChip(0x101, 0x2)
    Sleep(100)
    SetChrSubChip(0x101, 0x1)
    Sleep(150)
    SetChrSubChip(0x101, 0x0)
    Sleep(200)
    Return()

    # Function_9_2314 end

    SaveToFile()

Try(main)
