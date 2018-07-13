from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1560.bin",                # FileName
        "c1560",                    # MapName
        "c1560",                    # Location
        0x00AC,                     # MapIndex
        "ed7151",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 172, 0, 0, 0, 1],
    )

    BuildStringList((
        "c1560",                  # 0
        "President Dieter",       # 1
        "Ogre Sigmund",           # 2
        "Shirley",                # 3
        "Wald",                   # 4
        "Mariabell",              # 5
        "Secretary Arios",        # 6
        "Guard",                  # 7
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(372, 0)                                        # 0

    ScpFunction((
        "Function_0_174",          # 00, 0
        "Function_1_1AC",          # 01, 1
        "Function_2_24B",          # 02, 2
        "Function_3_1988",         # 03, 3
        "Function_4_19D2",         # 04, 4
        "Function_5_1A1C",         # 05, 5
        "Function_6_1D02",         # 06, 6
    ))


    def Function_0_174(): pass

    label("Function_0_174")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_188")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)
    Jump("loc_1AB")

    label("loc_188")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_19C")
    ClearScenarioFlags(0x22, 1)
    Event(0, 5)
    Jump("loc_1AB")

    label("loc_19C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_1AB")
    ClearScenarioFlags(0x22, 2)
    Event(0, 6)

    label("loc_1AB")

    Return()

    # Function_0_174 end

    def Function_1_1AC(): pass

    label("Function_1_1AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_200")
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "out_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_200")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_24A")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "out_add", 0x0, 0x1)

    label("loc_24A")

    Return()

    # Function_1_1AC end

    def Function_2_24B(): pass

    label("Function_2_24B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51716.itc", 0x1E)
    LoadChrToIndex("chr/ch03300.itc", 0x1F)
    LoadChrToIndex("chr/ch05500.itc", 0x20)
    LoadChrToIndex("chr/ch03800.itc", 0x21)
    LoadChrToIndex("chr/ch03400.itc", 0x22)
    LoadChrToIndex("chr/ch02100.itc", 0x23)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x3)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x2)
    SetChrPos(0x8, 18000, 150, 116200, 180)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 16800, 0, 111600, 90)
    OP_52(0x9, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xC, 0x20)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 18000, 0, 111300, 90)
    SetChrChipByIndex(0xD, 0x21)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 19600, 0, 111800, 90)
    OP_52(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xA, 0x22)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0xB, 0x23)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    ClearMapObjFlags(0xC, 0x4)
    VolumeBGM(0x46, 0x7D0)
    OP_68(19500, 2000, 111500, 0)
    MoveCamera(59, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(16000, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    SetMessageWindowPos(250, 90, -1, -1)
    SetChrName("Grace")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──From this point on,\x01",
            "we will tell you many scoops.\x01\x02\x03",
            "First of all, the Crossbell City raid incident\x01",
            "that happened two months ago...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(18000, 1200, 113500, 2000)
    MoveCamera(39, 18, 0, 2000)
    SetCameraDistance(15000, 2000)
    OP_6F(0x79)
    SetChrSubChip(0x8, 0x2)

    ChrTalk(
        0x8,
        (
            "#11301F#5P...How longer will this unpleasant\x01",
            "broadcast continue?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4E3():
        OP_93(0xC, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_4E3)
    Sleep(100)

    def lambda_4F3():
        OP_93(0xD, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_4F3)
    Sleep(100)

    def lambda_503():
        OP_93(0x9, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_503)
    Sleep(100)
    WaitChrThread(0xC, 0)
    WaitChrThread(0xD, 0)
    WaitChrThread(0x9, 0)

    ChrTalk(
        0xC,
        (
            "#12P#02913FAfter finding their intrusion path,\x01",
            "we are just in the middle of doing\x01",
            "a physical jamming.\x02\x03",
            "#02912FProbably another couple of minutes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#10503FWe had already withdrawn it\x01",
            "from the screens in the city.\x02\x03",
            "#10500FSoon, the citizens will go away too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P#11303FHm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P#04500FHu hu, that was a nice surprise attack.\x02\x03",
            "#04504FAn expert of mixing fiction and facts...\x01",
            "The backbone of a veteran, I'd say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11306F#5PYou're saying it like it's none of your business...\x02\x03",
            "#11310FHasn't such a thing happened because\x01",
            "you let the Chairman escape?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#12P#04504FWell, I can only offer you\x01",
            "an apology for that.\x02\x03",
            "#04502FAlthough, if we had done things on our\x01",
            "own accord and crushed all the sources\x01",
            "of trouble, this wouldn't have happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#11303F...You have to consider the Divine Child's...\x02\x03",
            "#11301F...Temperament too. We can't do anything\x01",
            "drastic to the Support Section people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12P#02913FUh uh, it is irritating, but we\x01",
            "can't do anything about this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#10503F...This situation should have a considerable\x01",
            "effect on the State Guard outside the city too.\x02\x03",
            "#10500FI will try to rally them in some way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P#11303FYeah, please.\x02",
    )

    CloseMessageWindow()
    OP_93(0xD, 0xB4, 0x1F4)
    MoveCamera(39, 18, 0, 4000)
    OP_68(18000, 1200, 108500, 4000)

    def lambda_9D1():
        OP_96(0xFE, 0x4650, 0x0, 0x182B8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_9D1)
    Sleep(500)

    def lambda_9EE():

        label("loc_9EE")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_9EE")

    QueueWorkItem2(0x9, 2, lambda_9EE)
    Sleep(100)

    def lambda_A03():

        label("loc_A03")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_A03")

    QueueWorkItem2(0xC, 2, lambda_A03)
    WaitChrThread(0xD, 1)
    Sound(103, 0, 100, 0)
    EndChrThread(0x9, 0x2)
    EndChrThread(0xC, 0x2)
    SetChrFlags(0xD, 0x80)
    OP_6F(0x79)
    Fade(500)
    OP_68(18000, 1200, 113500, 0)
    MoveCamera(49, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    OP_0D()
    Sound(104, 0, 100, 0)
    StopBGM(0xFA0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_A76():
        OP_93(0x9, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_A76)
    Sleep(100)

    def lambda_A86():
        OP_93(0xC, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_A86)
    Sleep(100)
    WaitChrThread(0x9, 0)
    WaitChrThread(0xC, 0)

    ChrTalk(
        0x9,
        (
            "#12P#04503F──Then, we'll set about\x01",
            "in earnest too.\x02\x03",
            "#04504FThe "Heiyue" and the Resistance...\x02\x03",
            "#04502FWe'll put a real effort in hunting them down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#12P#02912FI will go to contact the\x01",
            ""Society" people.\x02\x03",
            "#02913FThe Church's airship and the Support Section...\x01",
            "Something needs to be done about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P#11301FYeah, go.\x02",
    )

    CloseMessageWindow()

    def lambda_BE7():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_BE7)
    WaitChrThread(0xC, 2)
    SetCameraDistance(16000, 3000)

    def lambda_C01():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_C01)
    Sleep(100)

    def lambda_C1E():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_C1E)
    WaitChrThread(0x9, 2)

    def lambda_C2F():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_C2F)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    EndChrThread(0xC, 0xFF)
    EndChrThread(0x9, 0xFF)
    SetChrPos(0x9, 13000, 0, 3000, 180)
    SetChrPos(0xC, 13000, 0, 3000, 180)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7561", 0)
    OP_68(13000, 1300, -1100, 0)
    MoveCamera(51, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    MoveCamera(41, 21, 0, 4000)
    SetCameraDistance(16000, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x0)

    def lambda_D08():
        OP_96(0xFE, 0x32C8, 0x0, 0xFFFFF8F8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_D08)

    def lambda_D22():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_D22)
    Sleep(1000)

    def lambda_D36():
        OP_96(0xFE, 0x32C8, 0x0, 0xFFFFFF9C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_D36)

    def lambda_D50():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_D50)
    WaitChrThread(0xC, 1)
    WaitChrThread(0x9, 1)
    Sound(104, 0, 100, 0)
    OP_71(0x0, 0x5, 0x0, 0x0, 0x0)
    OP_79(0x0)
    OP_6F(0x79)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#5P#04504FHu hu, oh boy.\x02\x03",
            "#04500FYour father doesn't seem to be\x01",
            "quick in making decisions.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x9, 500)

    ChrTalk(
        0xC,
        (
            "#12P#02906FWell, I would like you to think\x01",
            "as he has long-sightedness.\x02\x03",
            "#02913FA grand plan to rearrange a\x01",
            "whole continent's order...\x02\x03",
            "#02902FBeing it done alone by my father\x01",
            "has got its limits, no matter what.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#5P#04504FThat's why he's getting various\x01",
            "help from an excellent staff.\x02\x03",
            "#04500FLike the Divine Blade and that gentleman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#12P#02913FUh uh, precisely.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 27500, 0, -600, 270)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 28400, 0, -1500, 270)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    NpcTalk(
        0xA,
        "Young Girl's Voice",
        "Papa, did you finish talking?\x02",
    )

    CloseMessageWindow()

    def lambda_FE6():
        OP_96(0xFE, 0x3C8C, 0x0, 0xFFFFFDA8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_FE6)
    Sleep(50)

    def lambda_1003():
        OP_96(0xFE, 0x4010, 0x0, 0xFFFFFA24, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1003)

    def lambda_101D():
        OP_93(0x9, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_101D)
    Sleep(50)

    def lambda_102D():
        OP_93(0xC, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_102D)
    Sleep(50)
    WaitChrThread(0x9, 0)
    WaitChrThread(0xC, 0)
    Fade(500)
    OP_68(24500, 1100, -1100, 0)
    MoveCamera(37, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15500, 0)
    OP_68(14500, 1100, -1100, 4500)
    SetCameraDistance(16500, 4500)
    OP_0D()
    WaitChrThread(0xA, 1)
    OP_6F(0x79)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0xA,
        (
            "#11P#04609FAh, it's milady Bell!\x01",
            "Yoo-hoo!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#01608F#11P............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#02909FUh uh, Miss Shirley, you\x01",
            "are always full of energy.\x02\x03",
            "#02902FDid you think about what\x01",
            "we talked before, perhaps?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#11P#04605FYeah, being the head of\x01",
            "your private unit, was it?\x02\x03",
            "#04606FHmm, it seems fun but\x01",
            "I like what I'm doing now...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xC, 500)
    Sleep(100)

    ChrTalk(
        0x9,
        (
            "#5P#04501FOh boy, I'd like you didn't\x01",
            "try to recruit her without\x01",
            "hesitation in front of me.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x9, 500)

    ChrTalk(
        0xC,
        (
            "#12P#02904FOh, my apologies.\x02\x03",
            "#02912FThen, Mr. Sigmund.\x01",
            "Regarding the next plan,\x01",
            "do it like we discussed it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#5P#04504FYeah, I know.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xA, 500)
    Sleep(300)

    ChrTalk(
        0x9,
        (
            "#04500F#5P──Boy.\x01",
            "What will you do?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_132C():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_132C)

    ChrTalk(
        0xB,
        (
            "#01603F#11P...I don't remember\x01",
            "having become your comrade.\x02\x03",
            "#01600FI'll do as I please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#04504FHmph...whatever.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xB, 500)

    ChrTalk(
        0xA,
        (
            "#5P#04602FWald, if you feel inclined,\x01",
            "you can come whenever you want\x01",
            "and I'll train you thoroughly, ok?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#01601F#11PTch...\x02",
    )

    CloseMessageWindow()
    OP_68(19500, 1200, -1100, 4000)
    MoveCamera(51, 17, 0, 4000)
    SetCameraDistance(17500, 4000)
    BeginChrThread(0xA, 3, 0, 4)
    Sleep(100)
    BeginChrThread(0x9, 3, 0, 3)
    Sleep(500)

    def lambda_1475():

        label("loc_1475")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1475")

    QueueWorkItem2(0xB, 2, lambda_1475)
    OP_6F(0x79)
    Sleep(3000)
    OP_68(14700, 1200, -1650, 2000)
    SetCameraDistance(16500, 2000)
    OP_6F(0x79)
    EndChrThread(0xB, 0x2)

    ChrTalk(
        0xC,
        (
            "#6P#02913FHu hu...\x01",
            "What reliable persons they are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#5P#01603F...Those monster father and daughter are trouble.\x02\x03",
            "#01602FAnd you, who compete with them on equal\x01",
            "footing, are quite the woman too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#02909FUhuhu...\x02\x03",
            "#02912FAre you regretting to\x01",
            "have been tempted by me?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xC, 500)

    ChrTalk(
        0xB,
        (
            "#11P#01604FHah! Nonsense.\x02\x03",
            "#01603FThanks to the drug you gave me,\x01",
            "I obtained "power"...\x02\x03",
            "#01602FAn overwhelming "power"\x01",
            "that no one can master.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#02913FUh uh, you are right.\x02\x03",
            "When you demonize, Mr. Wald, you are\x01",
            "the strongest man for physical strength...\x02\x03",
            "#02902FA unique sample for us too.\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#11P#01604FEh eh, I'll gladly become\x01",
            "your guinea pig...\x02\x03",
            "#01601FIf it's to crush that bastard...\x01",
            "To prove who's number one.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(16000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(500)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──Thus, the after-effects of the independent\x01",
            "state declaration of invalidity gradually\x01",
            "spread inside and outside the country.\x02\x03",
            "Movements in the city shrouded by\x01",
            "the barrier were completely unknown...\x02\x03",
            "The unrest among the State Guard soldiers was great\x01",
            "and disorders in the chain of command at Bellguard\x01",
            "Gate and Tangram Gate began to become an issue.\x02\x03",
            "In this situation──\x01",
            "A call from a certain someone reached the Merkabah, \x01",
            "which Lloyd and the others had joined.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x23, 3)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_24B end

    def Function_3_1988(): pass

    label("Function_3_1988")


    def lambda_198D():
        OP_95(0xFE, 35000, 0, -100, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_198D)
    WaitChrThread(0x9, 1)

    def lambda_19AB():
        OP_95(0xFE, 40000, 0, -100, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_19AB)

    def lambda_19C5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_19C5)
    Return()

    # Function_3_1988 end

    def Function_4_19D2(): pass

    label("Function_4_19D2")


    def lambda_19D7():
        OP_95(0xFE, 35000, 0, -700, 2800, 0x1)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_19D7)
    WaitChrThread(0xA, 1)

    def lambda_19F5():
        OP_95(0xFE, 40000, 0, -700, 2800, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_19F5)

    def lambda_1A0F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1A0F)
    Return()

    # Function_4_19D2 end

    def Function_5_1A1C(): pass

    label("Function_5_1A1C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51716.itc", 0x1E)
    LoadChrToIndex("chr/ch28600.itc", 0x1F)
    OP_68(18000, 1300, 104100, 0)
    MoveCamera(37, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19500, 0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x2)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x2)
    SetChrPos(0x8, 18000, 100, 116250, 180)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, 18000, 0, 90000, 0)
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    SetMapObjFlags(0xC, 0x4)
    Sound(103, 0, 100, 0)
    OP_68(18000, 1300, 114100, 7000)
    SetCameraDistance(14500, 7000)
    FadeToBright(2000, 0)
    Sleep(500)
    OP_63(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_1B09():
        OP_96(0xFE, 0x4650, 0x0, 0x1B580, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1B09)
    WaitChrThread(0xE, 1)
    OP_64(0xE)
    OP_6F(0x79)
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    SetChrFlags(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    Sleep(500)

    def lambda_1B58():
        OP_96(0xFE, 0x4650, 0x96, 0x1C520, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1B58)
    OP_82(0x64, 0x64, 0xBB8, 0x1F4)
    SetChrSubChip(0x8, 0x1)
    Sound(886, 0, 100, 0)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#5P#11307F#4SYou say the "barrier" has vanished!?\x02\x03",
            "#11310FKh...\x01",
            "Those guys from the "Society" are worthless.\x02\x03",
            "#11303FNow that this has happened I should assign\x01",
            "all the "Aions" to defend the city...\x02\x03",
            "#11307F──Call the Secretary of Defence!\x01",
            "Bell, Sigmund and the others too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#12PR-Roger that!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(15000, 2000)
    FadeToDark(2000, 0, -1)
    OP_93(0xE, 0xB4, 0x1F4)

    def lambda_1CD9():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFC568, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1CD9)
    OP_0D()
    EndChrThread(0xE, 0xFF)
    OP_6F(0x79)
    SetScenarioFlags(0x23, 0)
    NewScene("c1550", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_5_1A1C end

    def Function_6_1D02(): pass

    label("Function_6_1D02")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05602.itc", 0x1E)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 18000, 200, 116400, 180)
    SetMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xD, 0x4)
    OP_68(18000, 1200, 115600, 0)
    MoveCamera(37, 22, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(13000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Return()

    # Function_6_1D02 end

    SaveToFile()

Try(main)
