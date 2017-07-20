from ScenarioHelper import *

def main():
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
        "A guy",                   # 1
        "SE control",                 # 2
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(276, 0)                                        # 0

    ScpFunction((
        "Function_0_114",          # 00, 0
        "Function_1_124",          # 01, 1
        "Function_2_129",          # 02, 2
        "Function_3_2AA9",         # 03, 3
        "Function_4_2ABC",         # 04, 4
        "Function_5_2B03",         # 05, 5
        "Function_6_2B27",         # 06, 6
        "Function_7_2B4B",         # 07, 7
        "Function_8_2BE4",         # 08, 8
        "Function_9_2C05",         # 09, 9
        "Function_10_2C30",        # 0A, 10
        "Function_11_2C97",        # 0B, 11
        "Function_12_2CC8",        # 0C, 12
        "Function_13_2CF3",        # 0D, 13
        "Function_14_2D14",        # 0E, 14
        "Function_15_2D3F",        # 0F, 15
        "Function_16_2D63",        # 10, 16
        "Function_17_2D9F",        # 11, 17
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
            "#00005F#11P#30WThis is…\x02\x03",
            "#00008F……Everyone……\x01",
            "Where did Kiaa go?\x02",
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
            "#00006F#5P#30W…… Whatever you think\x01",
            "It looks like it's not an ordinary place.\x02\x03",
            "#00008FEven as I move around indiscriminately\x01",
            "I heard he will not go ……\x02\x03",
            "#00003F….\x02",
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
            "#00003F#11P#30W……Why.\x01",
            "Even though there is not such a place ……\x02\x03",
            "#00000FWhy? … Anxiety and fear are\x01",
            "I do not feel such a mysterious thing …\x02\x03",
            "#00008FWhat is this place…?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(250, 10, -1, -1)
    SetChrName("voice")

    AnonymousTalk(
        0xFF,
        (
            "#3C── In any situation\x01",
            "Trampling without panic\x01",
            "We strive to grasp the site …\x02\x03",
            "As a lot of investigators\x01",
            "You come with the board, are not you?\x02",
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

    def lambda_60B():
        OP_95(0xFE, 0, -750, -1400, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_60B)

    def lambda_625():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x4B0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_625)

    def lambda_636():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_636)
    OP_6F(0x79)
    CancelBlur(0)
    SetCameraDistance(13000, 3000)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00005F#6P#30W…..\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x1000)

    NpcTalk(
        0x8,
        "Is it? Is it? Is it?",
        "#11P#30WWhat's wrong Lloyd?\x02",
    )

    CloseMessageWindow()

    NpcTalk(
        0x8,
        "Is it? Is it? Is it?",
        (
            "#11P#30WFor the first time in a while\x01",
            "Was it surprised that you could not speak to your mouth?\x02",
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
            "#00011F#6P#40WB-Brother…\x02\x03",
            "#00002FAre you my … Brother?\x02",
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
            "#30W#0CHa ha, what a \"big brother\"\x01",
            "You do not have parentheses attached.\x02\x03",
            "As if I was saying \"Onii-chan\"\x01",
            "Shall I call you?\x02\x03",
            "Because there are only two people\x01",
            "Please do not hesitate to spare me.\x02",
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
            "#00006F#6P#30W…… ~~~~ っ …\x01",
            "Leave me alone!\x02\x03",
            "#00002FBut, its decreasing … …\x01",
            "I definitely want to be your big brother …\x02\x03",
            "It looks like it's not a dream ……\x01",
            "What the hell is that …?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WOh, apparently here\x01",
            "It seems to be part of the inner face of that child.\x02\x03",
            "#07808FIncluding all possibilities,\x01",
            "A world of \"zero\" that can reconstruct the world ……\x02\x03",
            "#07800FIt looks like that's the kind of place\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005F#6P#30WThe World of Zero?\x02\x03",
            "#00013FOnii-chan …\x01",
            "…… Big brother is also appearing\x01",
            "Is there a relationship?\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 1, 0, 5)
    WaitChrThread(0x8, 1)

    ChrTalk(
        0x8,
        (
            "#07803F#11P#30WOh, probably that girl,\x01",
            "By interfering with the past spatio-temporal space\x01",
            "I know the existence of me#2RTo#I guess.\x02\x03",
            "#07808FAnd you and Cecil ……\x01",
            "Also for Arios and Tio\x01",
            "Maybe I tried to bring me back.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00011F#6P#30WBrother… resurrected?!\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 1, 0, 6)
    WaitChrThread(0x8, 1)

    ChrTalk(
        0x8,
        (
            "#07800F#11P#30WWell exactly, the world now\x01",
            "\"In the world where I did not die\"\x01",
            "I guess it will be spinning.\x02\x03",
            "#07802FWhat do you think, Lloyd?\x02\x03",
            "#07809FWould you be happy if your older brother comes back?\x01",
            "Or do you want to do it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#6P#40WAhaha…\x02\x03",
            "#00004FSuch a … … I'm happy.\x01",
            "… … It will be decided … ….?\x02\x03",
            "#00008FBut… that is…\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30W── Time after I died,\x01",
            "The efforts of the people who have worked there\x01",
            "It will also be denying … ….\x02\x03",
            "#07810FWell, of course that's what would happen\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6P#40W….\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07803F#11P#30WThe Special Support Section, was it?\x02\x03",
            "#07802FI joined and together with you\x01",
            "The world that solves various cases also\x01",
            "Perhaps it was possible … …\x02\x03",
            "#07804FBut that's not your world now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#6P#40WYeah……\x02\x03",
            "#00006FIf there really was such a world,\x01",
            "No matter how pleasant and happy ……\x01",
            "…… I think I'll be happy, but …\x02\x03",
            "#00008F#50WEven so… I…\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    BeginChrThread(0x101, 1, 0, 9)
    WaitChrThread(0x101, 1)

    def lambda_EE1():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_EE1)
    WaitChrThread(0x101, 2)
    Sleep(750)

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WYeah… that's enough\x02\x03",
            "#07800FI can say that you can say so\x01",
            "I am proud.\x02",
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
            "#07809F#11P#40WReally … That girlfriend\x01",
            "It was a lot of decadence so far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00015F#6P#50WTo my older brother\x01",
            "I do not have amenable memory …\x02\x03",
            "#00008FI was to Cecil I guess\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#07804F#11P#40WHaha, I guess so\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#07803F#11P#30W…… Cecil also for myself\x01",
            "It is a good time to start walking.\x02",
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
            "#07802F#11P#30WWhat would you do, dare you\x01",
            "Why do not you try attacking?\x02\x03",
            "#07809FBecause it is natural blur, it's pretty\x01",
            "I do not notice it, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6P#30WNoisy……\x01",
            "Do not make a fool of Cecil 's older sister.\x02\x03",
            "#00013FTo older brothers are unnecessary,\x01",
            "You are the best woman … ….\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1499")

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WHaha, no doubt\x02\x03",
            "#07800FWell you too, your opponent\x01",
            "Because I seemed to have found it properly\x01",
            "I do not care too much.\x02\x03",
            "#07809FDid you say Erie?\x01",
            "It seems unnecessary for you\x01",
            "He is a good boy with a very good age.\x02\x03",
            "#07802FMy heart is passing though it is a lady\x01",
            "He seems to have action power and tolerance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#6P#30WHaha … I also think so.\x02\x03",
            "#00006FIf you can, my big brother …\x01",
            "I wanted you to meet Ellie.\x02\x03",
            "#00008FAlso to Tiio and Randy ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WTio …… There seems to be various things\x01",
            "I grew up as a good boy and I'm nothing more than anything.\x02\x03",
            "#07800FRandy is stupid too\x01",
            "It looks pretty funny.\x02\x03",
            "#07809FLooks like you found some great friends\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2521")

    label("loc_1499")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17C2")

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WHaha, no doubt\x02\x03",
            "#07800FWell you too, your opponent\x01",
            "Because I seemed to have found it properly\x01",
            "I do not care too much.\x02\x03",
            "#07809FNo way, you and Tio\x01",
            "I did not expect to stick together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#6P#30WBeside that kind of thing\x01",
            "It does not mean that I have a relationship … …\x02\x03",
            "#00004FBut I want to watch over you,\x01",
            "I wonder if it is an important child.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WThat's right …… with a very good face\x01",
            "It seems they started to laugh.\x02\x03",
            "#07802FWell, there is no mistake in the future\x01",
            "Why are you stopping it properly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#6P#30WHahaha …. It is too early.\x02\x03",
            "#00006F…… If you can, my big brother\x01",
            "I wanted Tio to meet.\x02\x03",
            "#00008FAnd also to Ellie and Randy ……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WEli is a talented person\x01",
            "Was it a lady with action ability?\x02\x03",
            "#07800FRandy is stupid too\x01",
            "It looks pretty funny.\x02\x03",
            "#07809FLooks like you found some great friends\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2521")

    label("loc_17C2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A6D")

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WHaha, no doubt\x02\x03",
            "#07800FWell you too, your opponent\x01",
            "Because I seemed to have found it properly\x01",
            "I do not care too much.\x02\x03",
            "#07809FDid you say Noel?\x01",
            "It seems unnecessary for you\x01",
            "It is straight and is a good girl.\x02\x03",
            "#07802FEven a single point\x01",
            "He seems to fit you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002F#6P#30WHaha … I also think so.\x02\x03",
            "#00006FIf you can, my big brother …\x01",
            "I wanted you to meet Noel.\x02\x03",
            "#00008FEli and Randy,\x01",
            "And of course Tio …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WTio …… There seems to be various things\x01",
            "I grew up as a good boy and I'm nothing more than anything.\x02\x03",
            "#07800FEli is a talented person\x01",
            "Was it a lady with action ability?\x02\x03",
            "Randy is stupid too\x01",
            "It looks pretty funny.\x02\x03",
            "#07809FLooks like you found some great friends\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2521")

    label("loc_1A6D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D57")

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WHaha, no doubt\x02\x03",
            "#07800FWell you too, your opponent\x01",
            "Because I seemed to have found it properly\x01",
            "I do not care too much.\x02\x03",
            "#07809F── Did you mention Lisha?\x02\x03",
            "#07802FIt seems to be holding a lot,\x01",
            "It seems unnecessary for you\x01",
            "He is a good and nice girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#6P#30WBeside that kind of thing\x01",
            "It does not mean that I have a relationship … …\x02\x03",
            "#00004FBut … I want to watch over you\x01",
            "I wonder if it is an existence.\x02\x03",
            "#00008FIf you can, my big brother …\x01",
            "I wanted you to meet Risha.\x02\x03",
            "Eli and Randy,\x01",
            "And of course Tio …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WTio …… There seems to be various things\x01",
            "I grew up as a good boy and I'm nothing more than anything.\x02\x03",
            "#07800FEli is a talented person\x01",
            "Was it a lady with action ability?\x02\x03",
            "Randy is stupid too\x01",
            "It looks pretty funny.\x02\x03",
            "#07809FLooks like you found some great friends\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2521")

    label("loc_1D57")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2005")

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WHaha, no doubt\x02\x03",
            "#07802FWell you too, your opponent\x01",
            "Have you found it properly?\x02\x03",
            "Hanging with each other's buddies\x01",
            "I also know that it's fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6P#30WOh, what about Randy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WIt seems quite stupid,\x01",
            "You look like a guy with a core.\x02\x03",
            "#07800FWhat is serious you?\x01",
            "It seems that my breath is in line … …\x02\x03",
            "#07809FIs not it like a good buddy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6P#30WOh … I also think so.\x02\x03",
            "#00008FIf you can, my big brother …\x01",
            "I wanted you to see Randy.\x02\x03",
            "Also to Tio and Eli … …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WTio …… There seems to be various things\x01",
            "I grew up as a good boy and I'm nothing more than anything.\x02\x03",
            "#07800FEli is a talented person\x01",
            "Was it a lady with action ability?\x02\x03",
            "#07809FLooks like you found some great friends\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2521")

    label("loc_2005")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22F9")

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WHaha, no doubt\x02\x03",
            "#07802FWell you too, your opponent\x01",
            "Have you found it properly?\x02\x03",
            "There are bastards hanging with each other\x01",
            "I also know that it's fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6P#30WOh, what about Wadi?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WIt's a mysterious guy\x01",
            "You can trust it.\x02\x03",
            "#07800FEvery serious person\x01",
            "To the contrary it seems that it matches … …\x02\x03",
            "#07809FThis is something of a bond?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6P#30WOh … I also think so.\x02\x03",
            "#00008FIf you can, my big brother …\x01",
            "I wanted you to meet Wazi.\x02\x03",
            "Eli and Randy,\x01",
            "And of course Tio …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WTio …… There seems to be various things\x01",
            "I grew up as a good boy and I'm nothing more than anything.\x02\x03",
            "#07800FEli is a talented person\x01",
            "Was it a lady with action ability?\x02\x03",
            "Randy is stupid too\x01",
            "It looks pretty funny.\x02\x03",
            "#07809FLooks like you found some great friends\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2521")

    label("loc_22F9")


    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WHaha, no doubt\x02\x03",
            "#07803FWell you too, your opponent\x01",
            "Have you found it properly?\x02\x03",
            "#07802FHanging friends with each other\x01",
            "I also know that it's fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6P#30WHaha … I can not deny it.\x02\x03",
            "#00008FIf you can, my big brother …\x01",
            "I wanted you to meet everyone.\x02\x03",
            "Eli and Randy,\x01",
            "And of course Tio …\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WTio …… There seems to be various things\x01",
            "I grew up as a good boy and I'm nothing more than anything.\x02\x03",
            "#07800FEli is a talented person\x01",
            "Was it a lady with action ability?\x02\x03",
            "Randy is stupid too\x01",
            "It looks pretty funny.\x02\x03",
            "#07809FLooks like you found some great friends\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2521")


    ChrTalk(
        0x101,
        "#00002F#6P#30WYeah…they're the best friends you could ask for\x02",
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
            "#00004F#6P#30WBrother… I'm going now\x02\x03",
            "Take back the important things\x01",
            "To return to everyone's place.\x02\x03",
            "#00000FWe'll be able to meet again sometime right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07804F#11P#30WYeah. Of course\x02\x03",
            "#07810FI'm always nearby \x02\x03",
            "If I want to cry, I want to give up\x01",
            "It is nice to call you anytime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6P#30WHaha, got it\x02\x03",
            "#00002FBut no matter how painful she is\x01",
            "I think that \"wall\" can be overcome.\x02\x03",
            "#00004FEveryone is there, beyond that\x01",
            "If it's to grab tomorrow …\x02\x03",
            "#00000F─ ─ So it's okay.\x01",
            "Please watch with confidence.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#07809F#11P#30WHahah, don't get cocky\x02\x03",
            "#07804F── If you are the one you are, I will give that girl\x01",
            "It should be found in the true sense.\x02\x03",
            "#07800F#30W#11PA princess shut up in the shell\x01",
            "Find out and hug me!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    ChrTalk(
        0x101,
        (
            "#00000F#6P#30W#4SYeah!\x02\x03",
            "#00014F#3SFarewell… Brother!\x02",
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
            "#07804F#11P#30W…… Yes, as long as I live,\x01",
            "\"Wall\" will always appear.\x02",
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
            "#07810F#11P#30WWhat is important is the intention to overcome\x01",
            "What kind of light will be found in the future …\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 1, 0, 15)
    WaitChrThread(0x8, 1)

    ChrTalk(
        0x8,
        "#07804F#11P#30WGo all out, Lloyd Bannings.\x02",
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

    def Function_3_2AA9(): pass

    label("Function_3_2AA9")

    OP_9B(0x1, 0x101, 0x0, 0xFFFFFD12, 0x320, 0x0)
    Sleep(400)
    Return()

    # Function_3_2AA9 end

    def Function_4_2ABC(): pass

    label("Function_4_2ABC")

    OP_93(0xFE, 0x0, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xFA0, 0x1)

    def lambda_2AD7():
        OP_9B(0x0, 0xFE, 0x0, 0x61A8, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2AD7)
    Sleep(3000)

    def lambda_2AEF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2AEF)
    Sleep(1500)
    EndChrThread(0xFE, 0x1)
    Return()

    # Function_4_2ABC end

    def Function_5_2B03(): pass

    label("Function_5_2B03")

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

    # Function_5_2B03 end

    def Function_6_2B27(): pass

    label("Function_6_2B27")

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

    # Function_6_2B27 end

    def Function_7_2B4B(): pass

    label("Function_7_2B4B")

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

    # Function_7_2B4B end

    def Function_8_2BE4(): pass

    label("Function_8_2BE4")

    SetChrChipByIndex(0xFE, 0x1F)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x9)
    Sleep(120)
    SetChrSubChip(0xFE, 0x10)
    Sleep(120)
    SetChrSubChip(0xFE, 0x11)
    Return()

    # Function_8_2BE4 end

    def Function_9_2C05(): pass

    label("Function_9_2C05")

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

    # Function_9_2C05 end

    def Function_10_2C30(): pass

    label("Function_10_2C30")

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

    # Function_10_2C30 end

    def Function_11_2C97(): pass

    label("Function_11_2C97")

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

    # Function_11_2C97 end

    def Function_12_2CC8(): pass

    label("Function_12_2CC8")

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

    # Function_12_2CC8 end

    def Function_13_2CF3(): pass

    label("Function_13_2CF3")

    Fade(250)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    Sound(812, 0, 30, 0)
    SetChrSubChip(0xFE, 0x12)
    Sleep(300)
    Return()

    # Function_13_2CF3 end

    def Function_14_2D14(): pass

    label("Function_14_2D14")

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

    # Function_14_2D14 end

    def Function_15_2D3F(): pass

    label("Function_15_2D3F")

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

    # Function_15_2D3F end

    def Function_16_2D63(): pass

    label("Function_16_2D63")

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

    # Function_16_2D63 end

    def Function_17_2D9F(): pass

    label("Function_17_2D9F")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 1)), scpexpr(EXPR_END)), "loc_2DC1")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E43")

    label("loc_2DC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 2)), scpexpr(EXPR_END)), "loc_2DD9")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E43")

    label("loc_2DD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 3)), scpexpr(EXPR_END)), "loc_2DF1")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E43")

    label("loc_2DF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 4)), scpexpr(EXPR_END)), "loc_2E09")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E43")

    label("loc_2E09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 5)), scpexpr(EXPR_END)), "loc_2E21")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E43")

    label("loc_2E21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 6)), scpexpr(EXPR_END)), "loc_2E39")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2E43")

    label("loc_2E39")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2E43")

    Return()

    # Function_17_2D9F end

    SaveToFile()

Try(main)
