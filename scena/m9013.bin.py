from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m9013.bin",                # FileName
        "m9013",                    # MapName
        "m9013",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x2A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 100000, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "m9013",                  # 0
        "Guy",                    # 1
        "SE制御",                 # 2
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(276, 0)                                        # 0

    ScpFunction((
        "Function_0_114",          # 00, 0
        "Function_1_124",          # 01, 1
        "Function_2_129",          # 02, 2
        "Function_3_2F00",         # 03, 3
        "Function_4_2F13",         # 04, 4
        "Function_5_2F5A",         # 05, 5
        "Function_6_2F7E",         # 06, 6
        "Function_7_2FA2",         # 07, 7
        "Function_8_303B",         # 08, 8
        "Function_9_305C",         # 09, 9
        "Function_10_3087",        # 0A, 10
        "Function_11_30EE",        # 0B, 11
        "Function_12_311F",        # 0C, 12
        "Function_13_314A",        # 0D, 13
        "Function_14_316B",        # 0E, 14
        "Function_15_3196",        # 0F, 15
        "Function_16_31BA",        # 10, 16
        "Function_17_31F6",        # 11, 17
    ))


    def Function_0_114(): pass

    label("Function_0_114")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_123")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)

    label("loc_123")

    Return()

    # Function_0_114 end

    def Function_1_124(): pass

    label("Function_1_124")

    OP_F0(0x1, 0x320)
    Return()

    # Function_1_124 end

    def Function_2_129(): pass

    label("Function_2_129")

    EventBegin(0x0)
    FadeToDark(0, 16777215, -1)
    Call(0, 17)
    LoadChrToIndex("chr/ch12100.itc", 0x1E)
    LoadChrToIndex("apl/ch51751.itc", 0x1F)
    SoundLoad(111)
    SoundLoad(125)
    SoundLoad(109)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07801.itp")
    OP_68(0, 2500, 0, 0)
    MoveCamera(0, 24, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(27000, 0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)
    SetChrPos(0x101, 0, -750, 750, 0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, -750, -2750, 0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(111, 2, 80, 0)
    Sound(125, 2, 40, 0)
    Sound(109, 2, 30, 0)
    OP_68(40000, 150, -50000, 0)
    MoveCamera(306, 14, 8, 0)
    OP_6E(700, 0)
    SetCameraDistance(35000, 0)
    OP_68(-20000, 150, 25000, 16000)
    MoveCamera(306, 14, 6, 16000)
    OP_6E(700, 16000)
    SetCameraDistance(35000, 16000)
    PlaceName2(340, 200, "c_plac63", 0x0, 6000)
    FadeToBright(3000, 16777215)
    Sleep(15600)
    Fade(500)
    OP_68(0, 750, 250, 0)
    MoveCamera(210, 8, -5, 0)
    OP_6E(700, 0)
    SetCameraDistance(34500, 0)
    OP_68(0, 750, 750, 7500)
    MoveCamera(135, 14, 5, 7500)
    OP_6E(700, 7500)
    SetCameraDistance(18500, 7500)
    OP_6F(0x79)
    SetCameraDistance(13600, 100000)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00005F#11P#30WWhere am I...?\x02\x03",
            "#00008F...Where's everyone...\x01",
            "And KeA gone?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_93(0x101, 0x59, 0x190)
    Sleep(800)
    OP_93(0x101, 0x10F, 0x190)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00006F#5P#30W...This is surely not\x01",
            "a normal place.\x02\x03",
            "#00008FIt also seems that I can't\x01",
            "move around recklessly...\x02\x03",
            "#00003F............\x02",
        )
    )

    CloseMessageWindow()
    MoveCamera(135, 14, 4, 2000)
    SetCameraDistance(13600, 10000)
    Sleep(200)
    OP_93(0x101, 0x0, 0x190)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00003F#11P#30W...I wonder why...\x01",
            "It's such an empty space, and yet...\x02\x03",
            "#00000FFor some reason...I strangely\x01",
            "don't feel any anxiety or fear...\x02\x03",
            "#00008F...What in the world is this place...?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(250, 10, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(
        0xFF,
        (
            "#3C──No matter the circumstances,\x01",
            "remain focused and work to\x01",
            "understand the scene...\x02\x03",
            "Aren't you very much accustomed\x01",
            "to the work as a detective?\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sound(223, 0, 50, 0)
    Sound(920, 0, 50, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(0, 750, 0, 1500)
    MoveCamera(135, 14, 0, 1500)
    OP_6E(700, 1500)
    SetCameraDistance(13600, 1500)

    def lambda_63B():
        OP_95(0xFE, 0, -750, -1400, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_63B)

    def lambda_655():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x4B0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_655)

    def lambda_666():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_666)
    OP_6F(0x79)
    CancelBlur(0)
    SetCameraDistance(13000, 3000)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00005F#6P#30W────────────\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x1000)

    NpcTalk(
        0x8,
        "???",
        "#11P#30WOh, what's wrong Lloyd?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "???",
        (
            "#11P#30WAre you shocked to meet me after a\x01",
            "long time that you can't even speak?\x02",
        )
    )

    CloseMessageWindow()
    PlayBGM("ed7534", 0)
    SetCameraDistance(11000, 100000)
    Sleep(500)
    BeginChrThread(0x9, 1, 0, 16)

    ChrTalk(
        0x101,
        (
            "#00011F#6P#40WB-Big brother...\x02\x03",
            "#00002FIs that...you...?\x02",
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
        0x8,
        (
            "#30W#0CHa ha, "big brother"...\x01",
            "Don't try to show off.\x02\x03",
            "Someone like you should\x01",
            "just say "bro", right?\x02\x03",
            "Because there's only us here,\x01",
            "you can fawn freely, you know?\x02",
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
            "#00006F#6P#30W............\x01",
            "Oh, leave me alone.\x02\x03",
            "#00002FBut this impudent talk...\x01",
            "It really seems my big brother's...\x02\x03",
            "It doesn't even seem I'm dreaming...\x01",
            "What's the meaning of this...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WWell, it seems this place is\x01",
            "a part of that child's interior.\x02\x03",
            "#07808FThe World of "Zero" that comprehends every\x01",
            "possibility and can reorganize the world...\x02\x03",
            "#07800FIt seems it's that kind of place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#6P#30WThe World of "Zero"...\x02\x03",
            "#00013FSo even the fact that bro...\x01",
            "...That big brother can show\x01",
            "up here is related to that?\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 1, 0, 5)
    WaitChrThread(0x8, 1)

    ChrTalk(
        0x8,
        (
            "#07803F#11P#30WYeah. Probably that child came to\x01",
            "know about me after tampering\x01",
            "with the space-time of the past.\x02\x03",
            "#07808FAlso, she probably tried to revive me...\x01",
            "For your, Cecil's...Arios' and Tio's sake too.\x01\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00011F#6P#30WYou've been...revived!?\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 1, 0, 6)
    WaitChrThread(0x8, 1)

    ChrTalk(
        0x8,
        (
            "#07800F#11P#30WWell, to be precise, she probably\x01",
            "spinned anew the present world\x01",
            "into a "world where I didn't die".\x02\x03",
            "#07802F──What do you say, Lloyd?\x02\x03",
            "#07809FWould you be happy if big brother came back?\x01",
            "Or would you consider it annoying?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#6P#40W......Ha ha......\x02\x03",
            "#00004FIsn't it obvious...that I'd be...\x01",
            "...Happy for that...?\x02\x03",
            "#00008F...However...that...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30W──That would negate the time after\x01",
            "I died and so all the efforts of the\x01",
            "people who did their best...\x02\x03",
            "#07810FWell, it's obvious it would turn like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6P#40W............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07803F#11P#30WThe "Special Support Section", eh?\x02\x03",
            "#07802FA possible world where I too\x01",
            "have joined and I solve many\x01",
            "different cases with you all...\x02\x03",
            "#07804FThat's not your current world...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#6P#40W...Yeah...\x02\x03",
            "#00006FIf there was really such a world,\x01",
            "I think it would be so much fun...\x01",
            "...And joyous, and pleasant...\x02\x03",
            "#00008F#50W...But even so...I...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    BeginChrThread(0x101, 1, 0, 9)
    WaitChrThread(0x101, 1)

    def lambda_FCC():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_FCC)
    WaitChrThread(0x101, 2)
    Sleep(750)

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WYeah── that's ok.\x02\x03",
            "#07800FI'm proud that you've \x01",
            "become able to say so.\x02",
        )
    )

    CloseMessageWindow()
    OP_68(0, 750, 500, 1500)
    MoveCamera(135, 14, 3, 1500)
    OP_6E(700, 1500)
    SetCameraDistance(11000, 1500)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x2)
    ClearChrFlags(0x8, 0x1000)
    OP_9B(0x1, 0x8, 0x0, 0x60E, 0x3E8, 0x0)
    OP_6F(0x79)
    BeginChrThread(0x8, 1, 0, 7)
    WaitChrThread(0x8, 1)
    Sleep(500)
    BeginChrThread(0x8, 1, 0, 8)
    WaitChrThread(0x8, 1)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#07809F#11P#40WReally...that spoiled brat has\x01",
            "made it this far and grown so much!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00015F#6P#50WI-I don't have any memories of\x01",
            "having been spoiled by you, b-bro...\x02\x03",
            "#00008F...Aside from sister Cecil...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#07804F#11P#40WHa ha...you're right.\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#07803F#11P#30W...Cecil too...it's a good time\x01",
            "she starts walking for herself.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(120)
    SetChrSubChip(0x8, 0x10)
    Sleep(120)
    SetChrSubChip(0x8, 0x9)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#07802F#11P#30WIf you like, why don't you try to\x01",
            "go to the attack resolutely?\x02\x03",
            "#07809FBut since she's a natural airhead,\x01",
            "it seems she wouldn't realize at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6P#30WShut up...\x01",
            "Don't make fun of sister Cecil.\x02\x03",
            "#00013FShe's a great woman, wasted\x01",
            "for someone like you, bro...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_164E")

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WHa ha, for sure.\x02\x03",
            "#07800FWell, you too seem to have\x01",
            "properly found your partner, so\x01",
            "I could be worrying for nothing.\x02\x03",
            "#07809FElie, is she called?\x01",
            "She's a good girl blessed with both intelligence\x01",
            "and beauty, too good for you.\x02\x03",
            "#07802FAlthough a milady, it seems she has her own beliefs,\x01",
            "ability to take action and broad-mindedness too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#6P#30WHa ha...I think so too.\x02\x03",
            "#00006FIf possible, I would've liked...\x01",
            "For you to have met Elie, big brother.\x02\x03",
            "#00008FAnd also Randy, and Tio too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WTio, eh? It seems a lot has happened to her,\x01",
            "but I'm glad she's grown up into a fine kid.\x02\x03",
            "#07800FThat Randy too, he looks silly \x01",
            "and seems quite the funny guy.\x02\x03",
            "#07809FYou're blessed with nice comrades, eh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28CE")

    label("loc_164E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19E2")

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WHa ha, for sure.\x02\x03",
            "#07800FWell, you too seem to have\x01",
            "properly found your partner, so\x01",
            "I could be worrying for nothing.\x02\x03",
            "#07809FWho would've thought you'd\x01",
            "become intimate with Tio?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#6P#30WIt's not that we have\x01",
            "that kind of relationship...\x02\x03",
            "#00004FBut I guess it's true that I want to\x01",
            "protect her and that she's a precious girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WI see...it seems she's become able to\x01",
            "smile with a very nice happy face.\x02\x03",
            "#07802FWell, I'm sure she promises greatly,\x01",
            "so hold on to her properly, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#6P#30WHa ha...you're too impertinent.\x02\x03",
            "#00006FIf possible, I would've liked...\x01",
            "For you to have met Tio, big brother.\x02\x03",
            "#00008FAnd also Elie, and Randy too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WElie is the intelligent, beautiful\x01",
            "and dynamic milady, eh?\x02\x03",
            "#07800FThat Randy too, he looks silly \x01",
            "and seems quite the funny guy.\x02\x03",
            "#07809FYou're blessed with nice comrades, eh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28CE")

    label("loc_19E2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CD0")

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WHa ha, for sure.\x02\x03",
            "#07800FWell, you too seem to have\x01",
            "properly found your partner, so\x01",
            "I could be worrying for nothing.\x02\x03",
            "#07809FNoｱl, is she called?\x01",
            "It's an honest and nice girl\x01",
            "too good for you.\x02\x03",
            "#07802FEven her one-track mind \x01",
            "seems to go well with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#6P#30WHa ha...I think so too.\x02\x03",
            "#00006FIf possible, I would've liked...\x01",
            "For you to have met Noｱl, big brother.\x02\x03",
            "#00008FElie, Randy and of\x01",
            "course, Tio too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WTio, eh? It seems a lot has happened to her,\x01",
            "but I'm glad she's grown up into a fine kid.\x02\x03",
            "#07800FElie is the intelligent, beautiful\x01",
            "and dynamic milady, eh?\x02\x03",
            "That Randy too, he looks silly \x01",
            "and seems quite the funny guy.\x02\x03",
            "#07809FYou're blessed with nice comrades, eh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28CE")

    label("loc_1CD0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2009")

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WHa ha, for sure.\x02\x03",
            "#07800FWell, you too seem to have\x01",
            "properly found your partner, so\x01",
            "I could be worrying for nothing.\x02\x03",
            "#07809F──Rixia, is she called?\x02\x03",
            "#07802FIt seems she has a lot going on,\x01",
            "but she's a brave and nice girl,\x01",
            "too good for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#6P#30WI-It's not that we have\x01",
            "that kind of relationship...\x02\x03",
            "#00004FBut...I guess it's true that she's\x01",
            "someone I want to protect.\x02\x03",
            "#00008FIf possible, I would've liked...\x01",
            "For you to have met Rixia, bro.\x02\x03",
            "Elie, Randy and of\x01",
            "course, Tio too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WTio, eh? It seems a lot has happened to her,\x01",
            "but I'm glad she's grown up into a fine kid.\x02\x03",
            "#07800FElie is the intelligent, beautiful\x01",
            "and dynamic milady, eh?\x02\x03",
            "That Randy too, he looks silly \x01",
            "and seems quite the funny guy.\x02\x03",
            "#07809FYou're blessed with nice comrades, eh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28CE")

    label("loc_2009")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2314")

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WHa ha, for sure.\x02\x03",
            "#07802FWell, you too, find a\x01",
            "proper partner, okay?\x02\x03",
            "Although I understand that it's fun\x01",
            "hanging out between buddies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6P#30WAh, do you mean Randy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WHe looks quite silly and seems\x01",
            "to be a guy with a backbone.\x02\x03",
            "#07800FIt seems to be in sync with\x01",
            "you who're a serious guy...\x02\x03",
            "#07809FHe seems to be a nice buddy, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6P#30WYeah...I think so too.\x02\x03",
            "#00008FIf possible, I would've liked...\x01",
            "For you to have met Randy, big brother.\x02\x03",
            "And also Tio and Elie too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WTio, eh? It seems a lot has happened to her,\x01",
            "but I'm glad she's grown up into a fine kid.\x02\x03",
            "#07800FElie is the intelligent, beautiful\x01",
            "and dynamic milady, eh?\x02\x03",
            "#07809FYou're blessed with nice comrades, eh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28CE")

    label("loc_2314")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2664")

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WHa ha, for sure.\x02\x03",
            "#07802FWell, you too, find a\x01",
            "proper partner, okay?\x02\x03",
            "Although I understand that it's\x01",
            "fun hanging out between guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6P#30WAh, do you mean Wazy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WIt seems he's a mysterious guy\x01",
            "but someone you can trust.\x02\x03",
            "#07800FIt seems he's in sync with\x01",
            "you who're a serious guy...\x02\x03",
            "#07809FCould this too be some kind of fate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6P#30WYeah...I think so too.\x02\x03",
            "#00008FIf possible, I would've liked...\x01",
            "For you to have met Wazy, big brother.\x02\x03",
            "Elie, Randy and of\x01",
            "course, Tio too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WTio, eh? It seems a lot has happened to her,\x01",
            "but I'm glad she's grown up into a fine kid.\x02\x03",
            "#07800FElie is the intelligent, beautiful\x01",
            "and dynamic milady, eh?\x02\x03",
            "That Randy too, he looks silly \x01",
            "and seems quite the funny guy.\x02\x03",
            "#07809FYou're blessed with nice comrades, eh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28CE")

    label("loc_2664")


    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WHa ha, for sure.\x02\x03",
            "#07803FWell, you too, find a\x01",
            "proper partner, okay?\x02\x03",
            "#07802FAlthough I understand that it's\x01",
            "fun hanging out between comrades.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6P#30WHa ha...I can't deny it.\x02\x03",
            "#00008FIf possible, I would've liked...\x01",
            "For you to have met everyone, big brother.\x02\x03",
            "Elie, Randy and of\x01",
            "course, Tio too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WTio, eh? It seems a lot has happened to her,\x01",
            "but I'm glad she's grown up into a fine kid.\x02\x03",
            "#07800FElie is the intelligent, beautiful\x01",
            "and dynamic milady, eh?\x02\x03",
            "That Randy too, he looks silly \x01",
            "and seems quite the funny guy.\x02\x03",
            "#07809FYou're blessed with nice comrades, eh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28CE")


    ChrTalk(
        0x101,
        "#00002F#6P#30WYeah...they're the best comrades.\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 1, 0, 11)
    BeginChrThread(0x101, 1, 0, 12)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x101, 1)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x2)
    ClearChrFlags(0x8, 0x1000)
    SetChrChipByIndex(0x101, 0xFF)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x1000)
    SetChrSubChip(0x101, 0xE)
    BeginChrThread(0x101, 0, 0, 3)
    OP_68(0, 750, 800, 1500)
    MoveCamera(135, 14, 3, 1500)
    OP_6E(700, 1500)
    SetCameraDistance(12000, 1500)
    WaitChrThread(0x101, 0)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00004F#6P#30W...Big brother, it's time for me to go.\x02\x03",
            "To get back what is precious to me\x01",
            "and return where everyone is.\x02\x03",
            "#00000FWill I be able...to see you again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WYeah, of course.\x02\x03",
            "#07810FI'm near you all.\x02\x03",
            "When you're crying, when you want to\x01",
            "get spoiled, you can call me whenever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6P#30WHa ha...got it.\x02\x03",
            "#00002FHowever, I think that no matter how\x01",
            "painful it is, I'll get over any "barrier"...\x02\x03",
            "#00004FIf it's to grasp the tomorrow that\x01",
            "lies beyond that, with everyone.\x02\x03",
            "#00000F──That's why, I'll be fine.\x01",
            "Don't worry and watch over me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07809F#11P#30WHa ha, listen to how cheeky you're.\x02\x03",
            "#07804F──Considering how you're now, you should\x01",
            "be able to find out that kid, in a real sense.\x02\x03",
            "#07800F#30W#11PFind the princess who holed up\x01",
            "inside a shell and hug her!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x101,
        (
            "#00000F#6P#30W#4SYeah...!\x02\x03",
            "#00014F#3SGoodbye── big brother!\x02",
        )
    )

    CloseMessageWindow()
    OP_68(480, 350, 5260, 3500)
    MoveCamera(34, 8, 0, 3500)
    OP_6E(700, 3500)
    SetCameraDistance(13230, 3500)
    BeginChrThread(0x101, 0, 0, 4)
    OP_6F(0x79)
    WaitChrThread(0x101, 0)
    Sleep(1000)
    Fade(500)
    OP_68(0, 350, 400, 0)
    MoveCamera(135, 9, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(12000, 0)
    SetCameraDistance(10500, 3000)
    Sleep(1500)
    BeginChrThread(0x8, 1, 0, 13)
    WaitChrThread(0x8, 1)
    OP_6F(0x79)
    SetCameraDistance(10000, 15000)

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30W...Right, as long as you're alive,\x01",
            ""barriers" are always going to appear.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    BeginChrThread(0x8, 1, 0, 14)
    WaitChrThread(0x8, 1)
    Sleep(200)

    ChrTalk(
        0x8,
        (
            "#07810F#11P#30WWhat's important is to get over those and\x01",
            "discover what kind of light lies beyond, eh...?\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 1, 0, 15)
    WaitChrThread(0x8, 1)

    ChrTalk(
        0x8,
        "#07804F#11P#30WGo all out── Lloyd Bannings!\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(12000, 3000)
    FadeToDark(2000, 0, -1)
    Sleep(300)
    SetChrSubChip(0x8, 0x16)
    Sleep(143)
    SetChrSubChip(0x8, 0x15)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    StopSound(111, 2000, 30)
    StopSound(125, 2000, 20)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(1000)
    SetScenarioFlags(0x22, 0)
    NewScene("m9014", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_129 end

    def Function_3_2F00(): pass

    label("Function_3_2F00")

    OP_9B(0x1, 0x101, 0x0, 0xFFFFFD12, 0x320, 0x0)
    Sleep(400)
    Return()

    # Function_3_2F00 end

    def Function_4_2F13(): pass

    label("Function_4_2F13")

    OP_93(0xFE, 0x0, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xFA0, 0x1)

    def lambda_2F2E():
        OP_9B(0x0, 0xFE, 0x0, 0x61A8, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2F2E)
    Sleep(3000)

    def lambda_2F46():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2F46)
    Sleep(1500)
    EndChrThread(0xFE, 0x1)
    Return()

    # Function_4_2F13 end

    def Function_5_2F5A(): pass

    label("Function_5_2F5A")

    SetChrChipByIndex(0xFE, 0x1F)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x0)
    Sleep(167)
    SetChrSubChip(0xFE, 0xD)
    Sleep(167)
    SetChrSubChip(0xFE, 0xE)
    Sleep(500)
    Return()

    # Function_5_2F5A end

    def Function_6_2F7E(): pass

    label("Function_6_2F7E")

    SetChrChipByIndex(0xFE, 0x1F)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0xE)
    Sleep(150)
    SetChrSubChip(0xFE, 0xD)
    Sleep(150)
    SetChrSubChip(0xFE, 0x0)
    Sleep(500)
    Return()

    # Function_6_2F7E end

    def Function_7_2FA2(): pass

    label("Function_7_2FA2")

    Sound(812, 0, 50, 0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x0)
    Sleep(125)
    SetChrSubChip(0xFE, 0x1)
    Sleep(125)
    SetChrSubChip(0xFE, 0x2)
    Sleep(125)
    SetChrSubChip(0xFE, 0x3)
    Sleep(125)
    BeginChrThread(0x101, 1, 0, 10)
    Sound(898, 0, 50, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(143)
    SetChrSubChip(0xFE, 0x4)
    Sleep(143)
    SetChrSubChip(0xFE, 0x5)
    Sleep(143)
    SetChrSubChip(0xFE, 0x6)
    Sleep(143)
    SetChrSubChip(0xFE, 0x5)
    Sleep(143)
    SetChrSubChip(0xFE, 0x4)
    Sleep(143)
    SetChrSubChip(0xFE, 0x3)
    Sleep(143)
    SetChrSubChip(0xFE, 0x4)
    Sleep(143)
    SetChrSubChip(0xFE, 0x5)
    Sleep(143)
    SetChrSubChip(0xFE, 0x6)
    Sleep(143)
    SetChrSubChip(0xFE, 0x7)
    Sleep(143)
    SetChrSubChip(0xFE, 0x8)
    Sleep(143)
    SetChrSubChip(0xFE, 0x9)
    WaitChrThread(0x101, 1)
    Return()

    # Function_7_2FA2 end

    def Function_8_303B(): pass

    label("Function_8_303B")

    SetChrChipByIndex(0xFE, 0x1F)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x9)
    Sleep(120)
    SetChrSubChip(0xFE, 0x10)
    Sleep(120)
    SetChrSubChip(0xFE, 0x11)
    Return()

    # Function_8_303B end

    def Function_9_305C(): pass

    label("Function_9_305C")

    SetChrChipByIndex(0xFE, 0x1F)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x18)
    Sleep(120)
    SetChrSubChip(0xFE, 0x19)
    Sleep(120)
    SetChrSubChip(0xFE, 0x1A)
    Sleep(120)
    SetChrSubChip(0xFE, 0x1B)
    Sleep(120)
    Return()

    # Function_9_305C end

    def Function_10_3087(): pass

    label("Function_10_3087")

    SetChrChipByIndex(0xFE, 0x1F)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x1B)
    Sleep(143)
    SetChrSubChip(0xFE, 0x1A)
    Sleep(143)
    SetChrSubChip(0xFE, 0x19)
    Sleep(143)
    SetChrSubChip(0xFE, 0x18)
    Sleep(143)
    SetChrSubChip(0xFE, 0x19)
    Sleep(143)
    SetChrSubChip(0xFE, 0x1A)
    Sleep(143)
    SetChrSubChip(0xFE, 0x1B)
    Sleep(143)
    SetChrSubChip(0xFE, 0x1A)
    Sleep(143)
    SetChrSubChip(0xFE, 0x19)
    Sleep(143)
    SetChrSubChip(0xFE, 0x18)
    Sleep(143)
    SetChrSubChip(0xFE, 0x1D)
    Sleep(143)
    SetChrSubChip(0xFE, 0x1E)
    Sleep(143)
    SetChrSubChip(0xFE, 0x1F)
    Return()

    # Function_10_3087 end

    def Function_11_30EE(): pass

    label("Function_11_30EE")

    SetChrChipByIndex(0xFE, 0x1F)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    Sound(898, 0, 30, 0)
    SetChrSubChip(0xFE, 0x9)
    Sleep(143)
    SetChrSubChip(0xFE, 0xA)
    Sleep(143)
    SetChrSubChip(0xFE, 0xB)
    Sleep(143)
    SetChrSubChip(0xFE, 0x0)
    Sleep(429)
    Return()

    # Function_11_30EE end

    def Function_12_311F(): pass

    label("Function_12_311F")

    SetChrChipByIndex(0xFE, 0x1F)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x1F)
    Sleep(143)
    SetChrSubChip(0xFE, 0x1E)
    Sleep(143)
    SetChrSubChip(0xFE, 0x1D)
    Sleep(143)
    SetChrSubChip(0xFE, 0x18)
    Sleep(429)
    Return()

    # Function_12_311F end

    def Function_13_314A(): pass

    label("Function_13_314A")

    Fade(250)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    Sound(812, 0, 30, 0)
    SetChrSubChip(0xFE, 0x12)
    Sleep(300)
    Return()

    # Function_13_314A end

    def Function_14_316B(): pass

    label("Function_14_316B")

    SetChrChipByIndex(0xFE, 0x1F)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x12)
    Sleep(120)
    SetChrSubChip(0xFE, 0x13)
    Sleep(120)
    SetChrSubChip(0xFE, 0x14)
    Sleep(120)
    SetChrSubChip(0xFE, 0x15)
    Sleep(300)
    Return()

    # Function_14_316B end

    def Function_15_3196(): pass

    label("Function_15_3196")

    SetChrChipByIndex(0xFE, 0x1F)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x15)
    Sleep(150)
    SetChrSubChip(0xFE, 0x16)
    Sleep(150)
    SetChrSubChip(0xFE, 0x17)
    Sleep(500)
    Return()

    # Function_15_3196 end

    def Function_16_31BA(): pass

    label("Function_16_31BA")

    StopSound(109, 1000, 20)
    OP_25(0x6F, 0x4B)
    Sleep(100)
    OP_25(0x6F, 0x46)
    Sleep(100)
    OP_25(0x6F, 0x41)
    Sleep(100)
    OP_25(0x6F, 0x3C)
    Sleep(100)
    OP_25(0x6F, 0x37)
    Sleep(100)
    OP_25(0x6F, 0x32)
    Sleep(100)
    OP_25(0x6F, 0x2D)
    Sleep(100)
    OP_25(0x6F, 0x28)
    Return()

    # Function_16_31BA end

    def Function_17_31F6(): pass

    label("Function_17_31F6")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 1)), scpexpr(EXPR_END)), "loc_3218")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_329A")

    label("loc_3218")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 2)), scpexpr(EXPR_END)), "loc_3230")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_329A")

    label("loc_3230")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 3)), scpexpr(EXPR_END)), "loc_3248")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_329A")

    label("loc_3248")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 4)), scpexpr(EXPR_END)), "loc_3260")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_329A")

    label("loc_3260")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 5)), scpexpr(EXPR_END)), "loc_3278")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_329A")

    label("loc_3278")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 6)), scpexpr(EXPR_END)), "loc_3290")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_329A")

    label("loc_3290")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_329A")

    Return()

    # Function_17_31F6 end

    SaveToFile()

Try(main)
