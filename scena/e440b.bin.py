from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e440b.bin",                # FileName
        "e440b",                    # MapName
        "e440b",                    # Location
        0x0000,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "e440b",                  # 0
        "Rixia",                  # 1
        "Divine Wolf Zeit",       # 2
        "Elie",                   # 3
        "Tio",                    # 4
        "Randy",                  # 5
        "Noｱl",                  # 6
        "Wazy",                   # 7
        "SE制御",                 # 8
    ))

    AddCharChip((
        "chr/ch03200.itc",                   # 00
        "chr/ch02708.itc",                   # 01
    ))

    DeclNpc(2589,    0,       4294967267, 90,   453,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(4294965747, 0,       4294966337, 180,  405,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(456, 0)                                        # 0

    ScpFunction((
        "Function_0_1C8",          # 00, 0
        "Function_1_278",          # 01, 1
        "Function_2_311",          # 02, 2
        "Function_3_385",          # 03, 3
        "Function_4_A3F",          # 04, 4
        "Function_5_E8F",          # 05, 5
        "Function_6_18BA",         # 06, 6
        "Function_7_1DB5",         # 07, 7
        "Function_8_3832",         # 08, 8
        "Function_9_3871",         # 09, 9
        "Function_10_5846",        # 0A, 10
        "Function_11_5863",        # 0B, 11
        "Function_12_58C4",        # 0C, 12
        "Function_13_58E1",        # 0D, 13
        "Function_14_7F42",        # 0E, 14
        "Function_15_7F5E",        # 0F, 15
        "Function_16_9BEA",        # 10, 16
        "Function_17_C1A3",        # 11, 17
        "Function_18_E409",        # 12, 18
    ))


    def Function_0_1C8(): pass

    label("Function_0_1C8")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_200"),
        (1, "loc_20C"),
        (2, "loc_218"),
        (3, "loc_224"),
        (4, "loc_230"),
        (5, "loc_23C"),
        (6, "loc_248"),
        (SWITCH_DEFAULT, "loc_254"),
    )


    label("loc_200")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_20C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_218")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_224")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_230")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_23C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_248")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_254")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_260")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_277")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_260")

    label("loc_277")

    Return()

    # Function_0_1C8 end

    def Function_1_278(): pass

    label("Function_1_278")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A0")
    ClearChrFlags(0x8, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29B")
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0x8, 0x40)

    label("loc_29B")

    ClearChrFlags(0x9, 0x80)

    label("loc_2A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_310")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 3)), scpexpr(EXPR_END)), "loc_2C0")
    Event(0, 7)
    Jump("loc_310")

    label("loc_2C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 4)), scpexpr(EXPR_END)), "loc_2D1")
    Event(0, 9)
    Jump("loc_310")

    label("loc_2D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 5)), scpexpr(EXPR_END)), "loc_2E2")
    Event(0, 13)
    Jump("loc_310")

    label("loc_2E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 6)), scpexpr(EXPR_END)), "loc_2F3")
    Event(0, 15)
    Jump("loc_310")

    label("loc_2F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 7)), scpexpr(EXPR_END)), "loc_304")
    Event(0, 16)
    Jump("loc_310")

    label("loc_304")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 0)), scpexpr(EXPR_END)), "loc_310")
    Event(0, 17)

    label("loc_310")

    Return()

    # Function_1_278 end

    def Function_2_311(): pass

    label("Function_2_311")

    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0xD0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF0A070D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_F0(0x1, 0x7D0)
    SetMapObjFrame(0x0, "door_l1", 0x0, 0x1)
    SetMapObjFrame(0x0, "door_l2", 0x0, 0x1)
    SetMapObjFrame(0x0, "door_r1", 0x0, 0x1)
    SetMapObjFrame(0x0, "door_r2", 0x0, 0x1)
    Sound(132, 1, 70, 0)
    Sound(497, 1, 40, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_384")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_384")

    Return()

    # Function_2_311 end

    def Function_3_385(): pass

    label("Function_3_385")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x6A), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_450")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A8")
    Call(0, 5)
    Jump("loc_44B")

    label("loc_3A8")


    ChrTalk(
        0x8,
        (
            "#10704F...I want to feel the wind of\x01",
            "this place for a while.\x02\x03",
            "#10702FThere's no need to rush. Please\x01",
            "take your time, and come when\x01",
            "you've finished preparing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44B")

    Jump("loc_A3B")

    label("loc_450")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_992")
    TurnDirection(0x8, 0x101, 0)

    ChrTalk(
        0x8,
        (
            "#10708F...It's finally tomorrow...\x01",
            "Our infiltration of\x01",
            "Crossbell City.\x02\x03",
            "#10702FI haven't been away that\x01",
            "long, so why am I getting\x01",
            "this nostalgic feeling?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FI see...\x02\x03",
            "#00006FThey said the Aions are\x01",
            "focusing on city defense now\x01",
            "that the barrier's down, but...\x02\x03",
            "#00008FI wonder how the people of Arc-\x01",
            "en-Ciel are doing now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#10704FProbably... they're continuing to\x01",
            "practice, even now.\x02\x03",
            "No matter what happens, or when, to\x01",
            "perfect the performing arts, one\x01",
            "must look forward and not waver...\x02\x03",
            "#10710FThat's Ilya's will... and a way of\x01",
            "life at Arc-en-Ciel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FHaha, that might actually\x01",
            "be true.\x02\x03",
            "#00000F...If we liberate Crossbell\x01",
            "and solve this incident...\x01",
            "what do you plan to do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#10704F...I want to see Ilya, and\x01",
            "dance at Arc-en-Ciel as an\x01",
            "artist as I did before...\x02\x03",
            "That will exists, but even\x01",
            "now, I don't understand it.\x02\x03",
            "#10708FWhen I reunite with Ilya and\x01",
            "Sully, what should I say...?\x01",
            "No words come to mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F...I see.\x02\x03",
            "#00000FBut, I'm sure Ilya and Arc-\x01",
            "en-Ciel both will accept\x01",
            "you.\x02\x03",
            "Maybe you shouldn't think\x01",
            "too hard about it, and focus\x01",
            "on what's in front of you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#10704F...Haha, you're\x01",
            "certainly right about\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FAnyway, none of that\x01",
            "will happen if we don't\x01",
            "liberate Crossbell City.\x02\x03",
            "#00000FLet's both do our best\x01",
            "tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#10702FRight...!\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x0)
    SetScenarioFlags(0x1DB, 2)
    Jump("loc_A3B")

    label("loc_992")

    TurnDirection(0x8, 0x101, 0)

    ChrTalk(
        0x8,
        (
            "#10704FStaring lazily at the moon\x01",
            "tonight, I feel my heart\x01",
            "calm.\x02\x03",
            "#10710FTo liberate Crossbell City\x01",
            "and Arc-en-Ciel, I must do\x01",
            "my very best tomorrow.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x0)

    label("loc_A3B")

    TalkEnd(0xFE)
    Return()

    # Function_3_385 end

    def Function_4_A3F(): pass

    label("Function_4_A3F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E10")

    ChrTalk(
        0x9,
        (
            "#01200F#3CThe Crossbell City liberation operation\x01",
            "tomorrow... I plan to disembark in\x01",
            "Crossbell City as a scout.\x02\x03",
            "#01203FI will not be where you all are, but I\x01",
            "will be right there if anything\x01",
            "happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, I'm counting on you.\x02\x03",
            "#00004FCome to think of it, will\x01",
            "your friends in the mountain\x01",
            "district be helping us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01200F#3CYes. I told them to support the\x01",
            "CGF resistance.\x02\x03",
            "If they use the terrain to their\x01",
            "advantage, they should provide an\x01",
            "even match for Red Constellation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FI see... It looks like we'll\x01",
            "be counting on them to support\x01",
            "Lt. Mireille and the others.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#01200F#3CWell, that's all the\x01",
            "assistance my friends can\x01",
            "provide you.\x02\x03",
            "In the end, it will be your\x01",
            "duty to take back KeA.\x02\x03",
            "#01203FVarious difficulties await\x01",
            "you on this path, but I'm\x01",
            "sure you know that already...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYeah... But, I will take\x01",
            "back KeA no matter what\x01",
            "happens.\x02\x03",
            "#00000FPlease watch over us\x01",
            "too, Zeit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        "#01200F#3CYes... I shall.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DB, 6)
    Jump("loc_E8B")

    label("loc_E10")


    ChrTalk(
        0x9,
        (
            "#01200F#3CIn the end, it will be\x01",
            "your duty to take back\x01",
            "KeA.\x02\x03",
            "Can you succeed? I shall\x01",
            "confirm that with my own\x01",
            "eyes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E8B")

    TalkEnd(0xFE)
    Return()

    # Function_4_A3F end

    def Function_5_E8F(): pass

    label("Function_5_E8F")

    EventBegin(0x0)
    Fade(500)
    OP_68(3230, 200, 1330, 0)
    MoveCamera(51, 21, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(11810, 0)
    SetChrPos(0x101, 1070, 0, 280, 90)
    OP_4B(0x8, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 2)), scpexpr(EXPR_END)), "loc_EE9")
    OP_93(0x8, 0x10E, 0x0)

    label("loc_EE9")

    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_161A")

    ChrTalk(
        0x101,
        (
            "#6P#00005FRixia... What are you\x01",
            "doing in a place like\x01",
            "this?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x8, 0x10E, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#11P#10712FAh, Lloyd.\x02\x03",
            "#10710F...Yes, I've finished\x01",
            "preparing for tomorrow, so I\x01",
            "was doing a little thinking.\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x1F4)
    Sleep(300)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#11P#10708F#5P...It's finally tomorrow...\x01",
            "Our infiltration of\x01",
            "Crossbell City.\x02\x03",
            "#10702FI haven't been away that\x01",
            "long, so why am I getting\x01",
            "this nostalgic feeling?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00000FIs that so...\x02\x03",
            "#00006FThey said the Aions are\x01",
            "focusing on city defense now\x01",
            "that the barrier's down, but...\x02\x03",
            "#00008FI wonder how the people of Arc-\x01",
            "en-Ciel are doing now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#10704F#5PProbably... they're continuing to\x01",
            "practice, even now.\x02\x03",
            "No matter what happens, or when, to\x01",
            "perfect the performing arts, one\x01",
            "must look forward and not waver...\x02\x03",
            "#10710FThat's Ilya's way of life... and\x01",
            "the Arc-en-Ciel way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00004FHaha, that might actually\x01",
            "be true.\x02\x03",
            "#00000F...If we liberate Crossbell\x01",
            "and solve this incident...\x01",
            "what do you plan to do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#5P#10704F...I want to see Ilya, and\x01",
            "dance at Arc-en-Ciel as an\x01",
            "artist as I did before...\x02\x03",
            "That will exists, but even\x01",
            "now, I don't understand it.\x02\x03",
            "#10708FWhen I reunite with Ilya and\x01",
            "Sully, what should I say...?\x01",
            "No words come to mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00006FI see...\x02\x03",
            "#00000FBut, I think Ilya and\x01",
            "Arc-en-Ciel both will\x01",
            "surely accept you.\x02\x03",
            "Maybe you should just be\x01",
            "yourself, and not think\x01",
            "too hard about it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#5P#10712F...Be myself...\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)
    Sleep(500)
    OP_93(0x8, 0x10E, 0x1F4)

    ChrTalk(
        0x8,
        (
            "#11P#10703F...Um, Lloyd?\x02\x03",
            "#10701FAfter this, may I take\x01",
            "just a bit of your time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00005FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#10704FHaha. Even if I say so myself, I\x01",
            "think I've been too guarded\x01",
            "lately...\x02\x03",
            "#10710FBefore tomorrow's operation, I\x01",
            "would like to chat with you for a\x01",
            "little while.\x02\x03",
            "When you're through preparing,\x01",
            "would you care to come to the deck\x01",
            "once more, and speak with me?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DB, 2)
    Jump("loc_16E1")

    label("loc_161A")


    ChrTalk(
        0x8,
        (
            "#11P#10704FBefore tomorrow's operation, I\x01",
            "would like to chat with you for a\x01",
            "little while.\x02\x03",
            "#10710FWhen you're through preparing,\x01",
            "would you care to come to the deck\x01",
            "once more, and speak with me?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16E1")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "Accept Rixia's Invitation\x01",      # 0
            "Refuse\x01",                         # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_181E")

    ChrTalk(
        0x101,
        (
            "#6P#00002FYeah, if you're ok with\x01",
            "me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#11P#10709FThank you very much.\x02\x03",
            "#10704F...I want to feel the wind of\x01",
            "this place for a while.\x02\x03",
            "#10702FThere's no need to rush. Please\x01",
            "take your time, and come when\x01",
            "you've finished preparing.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Call(0, 6)
    SetScenarioFlags(0x1AB, 0)
    Jump("loc_18A7")

    label("loc_181E")


    ChrTalk(
        0x8,
        (
            "#11P#10704FI see.\x02\x03",
            "#10702FHaha. If you change your\x01",
            "mind, that's fine. Please\x01",
            "speak with me again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00000FYeah, understood.\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_18A7")

    ClearChrFlags(0x8, 0x10)
    OP_93(0x8, 0x5A, 0x0)
    OP_4C(0x8, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_5_E8F end

    def Function_6_18BA(): pass

    label("Function_6_18BA")

    FadeToDark(500, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 3)), scpexpr(EXPR_END)), "loc_1982")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00006F(...I'll have to\x01",
            "apologize to Elie for\x01",
            "not being able to go.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd apologized to Elie\x01",
            "for not being able to go\x01",
            "as promised.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AA, 3)
    Jump("loc_1DB4")

    label("loc_1982")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 4)), scpexpr(EXPR_END)), "loc_1A3D")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00006F(...I'll have to\x01",
            "apologize to Tio for not\x01",
            "being able to go.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd apologized to Tio\x01",
            "for not being able to go\x01",
            "as promised.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AA, 4)
    Jump("loc_1DB4")

    label("loc_1A3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 5)), scpexpr(EXPR_END)), "loc_1AFC")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00006F(...I'll have to\x01",
            "apologize to Randy for\x01",
            "not being able to go.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd apologized to\x01",
            "Randy for not being able\x01",
            "to go as promised.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AA, 5)
    Jump("loc_1DB4")

    label("loc_1AFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 6)), scpexpr(EXPR_END)), "loc_1BB9")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00006F(...I'll have to\x01",
            "apologize to Noｱl for\x01",
            "not being able to go.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd apologized to Noｱl\x01",
            "for not being able to go\x01",
            "as promised.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AA, 6)
    Jump("loc_1DB4")

    label("loc_1BB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 7)), scpexpr(EXPR_END)), "loc_1C76")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00006F(...I'll have to\x01",
            "apologize to Wazy for\x01",
            "not being able to go.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd apologized to Wazy\x01",
            "for not being able to go\x01",
            "as promised.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AA, 7)
    Jump("loc_1DB4")

    label("loc_1C76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 0)), scpexpr(EXPR_END)), "loc_1D35")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00006F(...I'll have to\x01",
            "apologize to Rixia for\x01",
            "not being able to go.)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd apologized to\x01",
            "Rixia for not being able\x01",
            "to go as promised.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearScenarioFlags(0x1AB, 0)
    Jump("loc_1DB4")

    label("loc_1D35")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x101,
        (
            "#00003F(...I'll head to the deck from\x01",
            "the nap room once my preparations\x01",
            "for tomorrow are complete.)\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_1DB4")

    Return()

    # Function_6_18BA end

    def Function_7_1DB5(): pass

    label("Function_7_1DB5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00100.itc", 0x1E)
    LoadChrToIndex("apl/ch51800.itc", 0x1F)
    LoadChrToIndex("apl/ch5180A.itc", 0x20)
    LoadChrToIndex("apl/ch5180B.itc", 0x21)
    SoundLoad(3411)
    SoundLoad(3412)
    SoundLoad(3413)
    SoundLoad(3414)
    SoundLoad(3415)
    SoundLoad(3416)
    SoundLoad(3417)
    SoundLoad(3418)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00101.itp")
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    OP_F0(0x0, 0x1)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x1, 0x1000)
    OP_71(0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x101, 0, 120, 2750, 180)
    SetChrPos(0xA, 500, 0, -3750, 180)
    OP_63(0xA, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x0)
    OP_68(500, 5500, -3750, 0)
    MoveCamera(135, -15, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(8500, 0)
    PlayBGM("ed7560", 0)
    FadeToBright(2000, 0)
    OP_68(500, 1000, -3750, 8000)
    MoveCamera(135, 10, 0, 8000)
    OP_6E(800, 8000)
    SetCameraDistance(9500, 8000)
    OP_6F(0x79)
    OP_64(0xA)
    Sleep(500)

    ChrTalk(
        0xA,
        "#00108F#5P#30W............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    SetChrPos(0xA, 500, 0, -4250, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 1000, -1500, 0)
    MoveCamera(40, 10, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    SetCameraDistance(19500, 2000)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x8)
    OP_79(0x1)

    def lambda_1F8A():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1F8A)

    def lambda_1F9F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1F9F)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x101,
        (
            "#00002F#5PAh, Elie. You got here\x01",
            "first, huh.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1FED():

        label("loc_1FED")

        TurnDirection(0xA, 0x101, 500)
        Yield()
        Jump("loc_1FED")

    QueueWorkItem2(0xA, 2, lambda_1FED)
    Sleep(300)
    OP_C9(0x0, 0x80000000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    AnonymousTalk(
        0xA,
        (
            "#3411V#30WYeah... Lloyd, good work today.\x02\x03",
            "#3412VAre you finished preparing for\x01",
            "tomorrow?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xD54)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_C9(0x1, 0x80000000)
    OP_68(0, 1000, -4250, 3000)
    MoveCamera(45, 20, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(17000, 3000)
    BeginChrThread(0xF, 1, 0, 8)

    def lambda_2118():
        OP_95(0xFE, -500, 0, -4250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2118)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0xA, 0x0, 0x0, 0x8)
    OP_79(0x1)
    WaitChrThread(0x101, 1)
    OP_6F(0x79)
    OP_68(350, 1000, -3890, 50000)
    MoveCamera(44, 14, 0, 50000)
    OP_6E(500, 50000)
    SetCameraDistance(16880, 50000)

    ChrTalk(
        0x101,
        (
            "#00000F#5PYeah, I'm all set.\x02\x03",
            "#00006FAs expected... I can't\x01",
            "say it's perfect,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(2179, 255, 100, 0)

    ChrTalk(
        0xA,
        "#00109F#11P#30WHaha...\x02",
    )

    CloseMessageWindow()
    EndChrThread(0xA, 0x2)
    OP_93(0xA, 0xB4, 0x190)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#00104F#5P#30W...It's strange... Even\x01",
            "in this critical\x01",
            "situation.\x02\x03",
            "As for why it's strange,\x01",
            "it might be because my\x01",
            "heart is calm.\x02\x03",
            "#00108FBell, "uncle" and KeA...\x02\x03",
            "#00102FThere's a lot of things\x01",
            "I'm anxious or worried\x01",
            "about...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002F#5POh...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)

    ChrTalk(
        0x101,
        (
            "#00004F#5PMe too... I feel the\x01",
            "same.\x02\x03",
            "#00008FMy stomach might be in\x01",
            "knots, but I can see\x01",
            "what I have to do.\x02\x03",
            "#00002FThis too, is thanks to\x01",
            "everyone, yourself\x01",
            "included.\x02\x03",
            "#00009FThanks, really.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#00102F#5PHaha...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#00104F#11PI'm the one who should be\x01",
            "thanking you.\x02\x03",
            "#00108FEven though normally, I\x01",
            "would be beside myself with\x01",
            "worry...\x02\x03",
            "#00102FIt's because you were there\x01",
            "for me that I can stand\x01",
            "here today like this...\x02\x03",
            "#00104F...Thank you. I'm so glad\x01",
            "you were there.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 500)

    ChrTalk(
        0x101,
        (
            "#00005F#6PElie...\x02\x03",
            "#00012FHaha... If I was of use to\x01",
            "you, I'm honored.\x02\x03",
            "#00004FI've grown a little as a\x01",
            "leader, and become able to\x01",
            "rely on all of you, I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#00104F#11PHaha. You've been our\x01",
            "leader for a long time\x01",
            "already.\x02\x03",
            "Without you, I don't think\x01",
            "all of us would have been\x01",
            "able to come this far.\x02\x03",
            "#00108FBut─ That's what I wanted\x01",
            "to say to you.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)

    ChrTalk(
        0x101,
        "#00005F#6PHuh...\x02",
    )

    CloseMessageWindow()
    OP_93(0xA, 0xB4, 0x1F4)
    Fade(1000)
    SetChrPos(0x101, -500, 0, -3750, 90)
    SetChrPos(0xA, 500, 0, -3750, 180)
    OP_68(250, 1000, -4400, 0)
    MoveCamera(145, 15, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(11000, 0)
    OP_68(0, 1000, -3750, 50000)
    MoveCamera(135, 20, 0, 50000)
    OP_6E(800, 50000)
    SetCameraDistance(10000, 50000)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7568", 0)
    Sleep(500)

    ChrTalk(
        0xA,
        (
            "#00106F#5P...This incident.\x02\x03",
            "No matter how it ends, it\x01",
            "will spell big trouble for\x01",
            "Crossbell.\x02\x03",
            "#00108FProbably, our Support Section\x01",
            "won't continue to exist as it\x01",
            "is now...\x02\x03",
            "Each of us needs to use our\x01",
            "skills to the maximum extent\x01",
            "possible in this situation...\x02\x03",
            "#00101FTo rebuild Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12P...Yeah.\x02\x03",
            "#00008FI'll remain a police officer...\x02\x03",
            "Randy will probably want to\x01",
            "cooperate with the CGF after they\x01",
            "revert from being the State Guard.\x02\x03",
            "#00003FTio might want to return to the\x01",
            "foundation in the orbal networking\x01",
            "field...\x02\x03",
            "#00001F...And you, Elie...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#00104F#5P...The administration and\x01",
            "diplomacy fields of crisis\x01",
            "management.\x02\x03",
            "I think what I desire most\x01",
            "is knowledge and ability.\x02\x03",
            "#00108FAnd, I've accumulated a lot\x01",
            "of that through my studies\x01",
            "abroad.\x02\x03",
            "#00102FNaturally, I want to obtain\x01",
            "the power to deal with\x01",
            "incidents like this one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#12P#30W...I see...\x02\x03",
            "#00006F...............\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#00104F#5PHaha... Thank goodness.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#12PHuh...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)
    Sleep(300)

    ChrTalk(
        0xA,
        (
            "#00102F#5PIt seems like you feel a bit lonely\x01",
            "thinking about that.\x02\x03",
            "#00106FIf you said something like "It's all\x01",
            "right, you can do it, Elie", I don't\x01",
            "know what I would have thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#12PHaha...\x02\x03",
            "#00006F...Normally, I'd have to\x01",
            "say it like that, but...\x02\x03",
            "#00008FIt seems we're not so\x01",
            "easily parted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#00104F#5PWhat do you mean by\x01",
            "that?\x02\x03",
            "#00100FIs it because I'm\x01",
            "leaving, just like Tio\x01",
            "and Randy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00011F#12PW-Well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#00113F#5P─Answer, Lloyd.\x02\x03",
            "If I'm worried about\x01",
            "anything right now, it's\x01",
            "how you'll answer...\x02\x03",
            "#00108FYou already know the\x01",
            "answer, right?\x02\x03",
            "#00116FAs to just why I wanted\x01",
            "to talk to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#12P...Elie...\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)
    OP_93(0x101, 0xB4, 0x1F4)
    Fade(1000)
    SetChrPos(0x101, -500, 0, -4250, 180)
    SetChrPos(0xA, 500, 0, -4250, 270)
    OP_68(0, 1000, -4250, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17500, 0)
    OP_68(0, 1000, -4250, 50000)
    MoveCamera(45, 15, 0, 50000)
    OP_6E(500, 50000)
    SetCameraDistance(15500, 50000)
    SetChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7581", 0)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00006F#5PAt first, see... I\x01",
            "looked up to you a\x01",
            "little.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A1(0xA, 0x514, 0x5, 0x0, 0x1, 0x2, 0x1, 0x0)
    Sleep(300)

    ChrTalk(
        0xA,
        "#00105F#11PHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#5PThis girl was sweet and\x01",
            "cold, yet tolerant...\x02\x03",
            "#00000FAnd ever since I met her, I\x01",
            "thought she was a beautiful\x01",
            "person in many ways.\x02\x03",
            "#00002FEven so, at first, I spoke\x01",
            "to her, pretending to be\x01",
            "cool but...\x02\x03",
            "#00012FI'll confess... My heart\x01",
            "has been beating fast this\x01",
            "whole time.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A1(0xA, 0x5DC, 0x4, 0x0, 0x4, 0x5, 0x6)
    Sleep(300)

    ChrTalk(
        0xA,
        "#00112F#11P#30WL-Lloyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#5POf course within a month I\x01",
            "realized she was a young lady\x01",
            "living in a world beyond my reach.\x02\x03",
            "Even so, this whole time... I was\x01",
            "secretly proud of the fact she was\x01",
            "my co-worker.\x02\x03",
            "#00002FShe received advice from me, and I\x01",
            "was happy she was helpful, if only\x01",
            "a little.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#00102F#11P...............\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 500)
    OP_A1(0xA, 0x5DC, 0x4, 0x0, 0x6, 0x7, 0x8)
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#00003F#6POne year passed, and we got\x01",
            "through things both happy\x01",
            "and painful together...\x02\x03",
            "We got split up for a while\x01",
            "but finally reunited...\x02\x03",
            "#00008FEven now is like we're\x01",
            "meeting again...\x02\x03",
            "#00002FNo, it's even more exciting\x01",
            "than that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#00116F#11P...Lloyd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6P─I love you Elie.\x02\x03",
            "As a friend, and as\x01",
            "family, but not just\x01",
            "that.\x02\x03",
            "#00000FYou are my one and only\x01",
            "girl.\x02",
        )
    )

    CloseMessageWindow()
    Sound(812, 0, 70, 0)
    OP_A1(0xA, 0x5DC, 0x4, 0x0, 0xB, 0xC, 0xD)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xA,
        "#00106F#3413V#11PLloyd...\x02",
    )

    CloseMessageWindow()
    OP_A1(0xA, 0x640, 0x4, 0xD, 0xE, 0xF, 0x10)

    def lambda_331F():

        label("loc_331F")

        OP_A0(0xFE, 1000, 0x10, 0x12)
        Yield()
        Jump("loc_331F")

    QueueWorkItem2(0xA, 3, lambda_331F)
    Sleep(500)

    ChrTalk(
        0xA,
        "#00116F#3414V#11PMe too── I love you.\x02",
    )

    CloseMessageWindow()
    OP_24(0xD56)
    Sleep(300)
    EndChrThread(0xA, 0x3)
    SetChrFlags(0xA, 0x20)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x1)
    OP_68(400, 1000, -4250, 1200)

    def lambda_3389():
        OP_9B(0x1, 0xFE, 0x0, 0x190, 0x190, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3389)
    Sleep(50)

    def lambda_33A1():
        OP_A0(0xFE, 1000, 0x1, 0x5)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_33A1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xA, 3)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x0)
    Sound(812, 0, 100, 0)

    def lambda_33D7():
        OP_A0(0xFE, 1000, 0x7, 0x9)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_33D7)

    def lambda_33E4():
        OP_A0(0xFE, 1000, 0x7, 0x9)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_33E4)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xA, 3)
    Fade(800)
    SetCameraDistance(15000, 1000)

    def lambda_3407():
        OP_A0(0xFE, 1000, 0x9, 0xC)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3407)
    OP_A0(0xA, 1000, 0x9, 0xC)
    Sleep(300)
    OP_A0(0xA, 1000, 0x19, 0x1E)
    Sleep(300)

    ChrTalk(
        0xA,
        "#3415V#11P#40W#2S...Mmm...\x02",
    )

    CloseMessageWindow()
    OP_24(0xD57)
    OP_C9(0x1, 0x80000000)
    Sleep(500)
    Sound(812, 0, 100, 0)

    def lambda_345A():
        OP_A0(0xFE, 1000, 0xC, 0xF)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_345A)

    def lambda_3467():
        OP_A0(0xFE, 1000, 0xC, 0xF)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_3467)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xA, 3)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3585")

    ChrTalk(
        0x101,
        (
            "#00004F#6P#30WHaha...\x02\x03",
            "#00002F...Is it finally time to\x01",
            "continue what we started\x01",
            "back then...?\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xA,
        (
            "#00104F#3416V#11P#40W...Yeah...\x02\x03",
            "#00116F#3417VI've waited this whole,\x01",
            "whole time...\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xD59)
    OP_C9(0x1, 0x80000000)

    ChrTalk(
        0x101,
        (
            "#00012F#6P#40WSorry to keep you\x01",
            "waiting.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35E0")

    label("loc_3585")


    ChrTalk(
        0x101,
        (
            "#00004F#6P#30WThis is how I've felt\x01",
            "this whole time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        "#00104F#11P#40W...Me too...\x02",
    )

    CloseMessageWindow()

    label("loc_35E0")

    Sleep(300)

    def lambda_35E8():
        OP_A0(0xFE, 1000, 0xF, 0x12)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_35E8)
    Sleep(50)

    def lambda_35F8():
        OP_A0(0xFE, 1000, 0xF, 0x12)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_35F8)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xA, 3)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00006F#6P#30W─Even if we cannot\x01",
            "follow the same career\x01",
            "paths...\x02\x03",
            "#00004FWe'll always need each\x01",
            "other, and continue to\x01",
            "support each other...\x02\x03",
            "#00002FAre you fine with that\x01",
            "kind of relationship?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_A0(0xA, 1300, 0x12, 0x17)
    Sleep(500)

    ChrTalk(
        0xA,
        "#00109F#3418V#11P#40W...Yes...!\x02",
    )

    CloseMessageWindow()
    OP_24(0xD5A)
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(16500, 3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopSound(132, 1000, 30)
    StopSound(497, 1000, 15)
    StopBGM(0x157C)
    WaitBGM()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21, 2)), scpexpr(EXPR_END)), "loc_3748")
    OP_CC(0x1, 0xFF, 0x0)
    NewScene("b0100", 0, 0, 0)
    IdleLoop()
    Return()

    label("loc_3748")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_375A")
    Jump("loc_380F")

    label("loc_375A")

    Sleep(500)
    Sound(517, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Lloyd and Elie learned\x01",
            "Star Blast Ⅲ.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and Elie's combination\x01",
            "craft, Star Blast, has been\x01",
            "strengthened.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddCraft(0x1, 0x1AE)
    AddCraft(0x0, 0x1AE)

    label("loc_380F")

    OP_CC(0x1, 0xFF, 0x0)
    OP_E0(0x28, 0x0)
    OP_E0(0x80, 0x0)
    SetScenarioFlags(0x1AB, 1)
    OP_29(0xB1, 0x1, 0x1)
    Sleep(2000)
    SetScenarioFlags(0x23, 1)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_7_1DB5 end

    def Function_8_3832(): pass

    label("Function_8_3832")

    OP_25(0x84, 0x41)
    OP_25(0x1F1, 0x23)
    Sleep(300)
    OP_25(0x84, 0x3C)
    OP_25(0x1F1, 0x1E)
    Sleep(300)
    OP_25(0x84, 0x37)
    OP_25(0x1F1, 0x19)
    Sleep(300)
    OP_25(0x84, 0x32)
    OP_25(0x1F1, 0x14)
    Sleep(300)
    OP_25(0x84, 0x2D)
    Sleep(300)
    OP_25(0x84, 0x28)
    Sleep(300)
    OP_25(0x84, 0x23)
    Return()

    # Function_8_3832 end

    def Function_9_3871(): pass

    label("Function_9_3871")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00200.itc", 0x1E)
    LoadChrToIndex("apl/ch51801.itc", 0x1F)
    LoadChrToIndex("apl/ch51802.itc", 0x20)
    SoundLoad(2698)
    SoundLoad(2699)
    SoundLoad(2700)
    SoundLoad(2701)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00201.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00202.itp")
    SetChrFlags(0xB, 0x2)
    SetChrChipByIndex(0xB, 0x1F)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    OP_F0(0x0, 0x1)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x1, 0x1000)
    OP_71(0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x101, 0, 120, 2750, 180)
    SetChrPos(0xB, 500, 0, -4250, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(470, 800, 1980, 0)
    MoveCamera(47, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x8)
    OP_79(0x1)

    def lambda_399F():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_399F)

    def lambda_39B4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_39B4)
    PlayBGM("ed7560", 0)
    SetCameraDistance(14000, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 3)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#5P(Huh, Tio?)\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0xF, 1, 0, 8)
    Fade(1000)
    SetChrPos(0x101, 250, 0, 1250, 180)
    SetChrPos(0xB, 500, 0, -3750, 180)
    OP_68(500, 2300, -3750, 0)
    MoveCamera(125, -5, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(7500, 0)
    OP_68(500, 2300, -3750, 3000)
    MoveCamera(125, -5, 0, 3000)
    OP_6E(800, 3000)
    SetCameraDistance(8500, 3000)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0xB,
        "#00208F#30W...............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00000F#6P#N─Tio?\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sound(100, 0, 100, 0)
    OP_68(320, 1000, -2950, 5000)
    MoveCamera(115, 15, 0, 5000)
    OP_6E(800, 5000)
    SetCameraDistance(9000, 5000)

    def lambda_3B32():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFF92A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3B32)
    OP_63(0xB, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x2)
    OP_0D()

    def lambda_3B7A():

        label("loc_3B7A")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_3B7A")

    QueueWorkItem2(0xB, 2, lambda_3B7A)
    Sleep(1500)
    OP_64(0xB)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0xB, 500)
    Sleep(1000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0xB,
        "#2698V#40WLloyd...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xA8A)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_C9(0x1, 0x80000000)

    ChrTalk(
        0x101,
        (
            "#00012F#6PHaha, you don't see that\x01",
            "every day.\x02\x03",
            "#00002FYou didn't notice me\x01",
            "until I called out to\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xB,
        "#00204F#2699V#11P#40WHaha... That's right.\x02",
    )

    CloseMessageWindow()
    OP_24(0xA8B)
    OP_C9(0x1, 0x80000000)
    OP_68(0, 1000, -3750, 3000)
    MoveCamera(135, 20, 0, 3000)
    OP_6E(800, 3000)
    SetCameraDistance(9000, 3000)
    OP_95(0x101, -500, 0, -3750, 1200, 0x0)
    TurnDirection(0x101, 0xB, 500)
    EndChrThread(0xB, 0x2)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00004F#12PI've finished preparing for tomorrow.\x02\x03",
            "#00000FI can't say it's perfect, but considering\x01",
            "what everyone else is dealing with, I\x01",
            "think this is the best I can do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#00204F#5PRight...\x02\x03",
            "We have to do our best\x01",
            "to meet up with KeA or\x01",
            "the chief.\x02\x03",
            "#00202FI'm worried about Koppe\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12PRight...\x02\x03",
            "#00005F...Come to think of it,\x01",
            "Jona is being sent to\x01",
            "Michelam.\x02\x03",
            "I wonder how the\x01",
            "foundation's Chief\x01",
            "Roberts is doing.\x02\x03",
            "#00008FThe situation being what\x01",
            "it is... maybe he\x01",
            "returned to Lｳman state?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#00206F#5PNo. It seems the chief didn't comply\x01",
            "with the evacuation order.\x02\x03",
            "#00208FIt seems he stayed behind in the city\x01",
            "to monitor the status of the orbal\x01",
            "net Mariabell took control of...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrFlags(0xB, 0x2)
    SetChrChipByIndex(0xB, 0x1F)
    OP_A0(0xB, 1000, 0x1, 0x3)
    OP_0D()
    Sleep(200)

    ChrTalk(
        0xB,
        (
            "#00206F#5PWell considering who it\x01",
            "is, I think he's avoiding\x01",
            "guilt from his laziness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12PI see... I'm a little\x01",
            "worried, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A0(0xB, 1200, 0x3, 0x1)
    Sleep(300)

    ChrTalk(
        0xB,
        "#00202F#5PYes... Just a little.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xFA0)
    Fade(1000)
    SetChrSubChip(0xB, 0x4)
    SetChrPos(0x101, -500, 0, -4250, 90)
    SetChrPos(0xB, 500, 0, -4250, 270)
    OP_68(0, 1100, -4250, 0)
    MoveCamera(35, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    OP_68(0, 1000, -4250, 50000)
    MoveCamera(45, 25, 0, 50000)
    OP_6E(500, 50000)
    SetCameraDistance(16000, 50000)
    OP_71(0x1, 0x0, 0x0, 0x0, 0x0)
    OP_0D()
    OP_63(0xB, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xB)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7568", 0)
    Sleep(500)

    ChrTalk(
        0xB,
        (
            "#00206F#11P─Lloyd.\x02\x03",
            "#00208FCan you give me some\x01",
            "advice?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PYeah, of course.\x02\x03",
            "#00001FCould it be about that\x01",
            "letter I just saw?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#00206F#11PSo you noticed...\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrFlags(0xB, 0x2)
    SetChrChipByIndex(0xB, 0x1F)
    OP_A0(0xB, 1000, 0x4, 0x6)
    Sleep(500)
    Sound(802, 0, 100, 0)
    OP_A0(0xB, 1000, 0x7, 0x8)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#00203F#11PAbbas delivered it to me\x01",
            "yesterday...\x02\x03",
            "#00201FIt's from my parents in\x01",
            "Altair City in the\x01",
            "Republic.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005F#6PHuh!?\x02\x03",
            "#00002FThen, they came all the\x01",
            "way from Remiferia to\x01",
            "see you!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#00206F#11PYes. They couldn't get in contact\x01",
            "via letters or communications ever\x01",
            "since independence was declared...\x02\x03",
            "It seems they relied on\x01",
            "information from the foundation\x01",
            "and came to the border city.\x02\x03",
            "#00208FRight now, because only cargo can\x01",
            "come in, they seem to be staying\x01",
            "out of sight, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6PIs that so...\x02\x03",
            "#00000F...If that's the case, then\x01",
            "tell me sooner! This ship\x01",
            "can go to Altair City and─\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A0(0xB, 1300, 0x8, 0xA)
    Sleep(150)

    ChrTalk(
        0xB,
        (
            "#00204F#11PThat's unnecessary.\x02\x03",
            "I've already told them I'm\x01",
            "safe, the same way I got\x01",
            "their letter.\x02\x03",
            "#00208FAnd, if I see them now,\x01",
            "I'll lose my composure and\x01",
            "be a hindrance tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#6P...B-But...\x02\x03",
            "#00006F#30W...............\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_A0(0xB, 800, 0xA, 0x8)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#00209F#11PHaha... Don't make that\x01",
            "face.\x02\x03",
            "#00202FI'll definitely see my\x01",
            "parents after this\x01",
            "incident is resolved.\x02\x03",
            "#00204FThanks to you, Lloyd, I\x01",
            "was a little homesick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PHuh...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_A0(0xB, 1000, 0xD, 0xB)
    Sleep(500)

    ChrTalk(
        0xB,
        (
            "#00208F#5P#30W...Everyone went their separate\x01",
            "ways...\x02\x03",
            "I was anxious and lonely, and\x01",
            "when I heard you were wanted, I\x01",
            "was so worried my heart ached...\x02\x03",
            "#00206F...Honestly, I was really happy.\x02\x03",
            "That I got to see you again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6P#30WAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#00204F#5P#30WThis reminds of that time.\x02\x03",
            "Yes─ I am alive.\x02\x03",
            "#00208FWhen I think of those\x01",
            "important to me, a lot of\x01",
            "faces come to mind.\x02\x03",
            "#00202F...How should I live, and for\x01",
            "what reason...\x02\x03",
            "#00209FI felt like I understood the\x01",
            "answer to the question I tried\x01",
            "asking Guy three years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000F#6P#30W...Tio...\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_A0(0xB, 1300, 0xB, 0xD)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#00206F#11P#30WSince then, I've met\x01",
            "Elie and Randy as\x01",
            "well...\x02\x03",
            "#00208FAnd we've all done our\x01",
            "very best to come this\x01",
            "far for KeA's sake...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Sound(812, 0, 60, 0)
    OP_A0(0xB, 1200, 0xD, 0x10)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#00212F#11P#30W...And when I read this\x01",
            "letter, my real feelings\x01",
            "gushed forth like melting ice.\x02\x03",
            "#00213FIt's been a while... since\x01",
            "I've seen my mother and\x01",
            "father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00004F#6P...............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(400, 1000, -4250, 1200)
    OP_9A(0x101, 0xB, 0x258, 0x1F4, 0x0)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1F)

    def lambda_4AB4():
        OP_A0(0xFE, 1000, 0x10, 0x13)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_4AB4)

    def lambda_4AC1():
        OP_A0(0xFE, 1000, 0x20, 0x23)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4AC1)
    WaitChrThread(0xB, 3)
    WaitChrThread(0x101, 3)
    Sound(898, 0, 100, 0)
    BeginChrThread(0xB, 3, 0, 10)
    BeginChrThread(0x101, 3, 0, 12)
    WaitChrThread(0xB, 3)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0xB,
        "#00216F#11P#40W#2S...Ah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6P#30W...Thank goodness.\x01",
            "Really, thank\x01",
            "goodness...\x02\x03",
            "I'm a little embarrassed\x01",
            "you'd tell me this...\x02\x03",
            "#00002FBut knowing you feel\x01",
            "that way makes me\x01",
            "happier than anything.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A1(0xB, 0x4B0, 0x5, 0x13, 0x18, 0x19, 0x18, 0x13)
    Sleep(300)

    ChrTalk(
        0xB,
        "#00215F#11P#30W...Lloyd...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xBB8)
    Fade(1000)
    SetChrSubChip(0xB, 0x1)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 0, 0, -3750, 90)
    SetChrPos(0xB, 500, 0, -3750, 270)
    OP_68(0, 1000, -3750, 0)
    MoveCamera(140, 10, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(10000, 0)
    MoveCamera(140, 20, 0, 50000)
    SetCameraDistance(9000, 50000)

    def lambda_4C79():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4C79)
    OP_0D()
    OP_63(0xB, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)
    OP_A1(0xB, 0x320, 0x3, 0x1, 0x2, 0x3)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7581", 0)
    Sleep(500)

    ChrTalk(
        0xB,
        (
            "#00204F#5P#30W...I have two requests.\x02\x03",
            "Will you hear them?\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 1)
    OP_63(0x101, 0x0, 1900, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00002F#12PYeah─ I'll do anything.\x02\x03",
            "#00009FAnd don't hold back.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A1(0xB, 0x3E8, 0x3, 0x3, 0x2, 0x1)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#00208F#5P#30WThen, firstly...\x02\x03",
            "#00208FI really love it when\x01",
            "you pat my head, but...\x02\x03",
            "#00201FOn a beautiful night\x01",
            "like this, I feel it's\x01",
            "too childlike.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#12PR-Really?\x02\x03",
            "#00012FI mean, when my brother or\x01",
            "Randy does it to me, it\x01",
            "makes me feel like a kid.\x02\x03",
            "#00000FUmm, then...\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0xB, 3, 0, 11)
    Sleep(1500)
    OP_63(0x101, 0x0, 1900, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x101, 0x0, 1950, 0x28, 0x2B, 0x64, 0x3)
    Sleep(300)

    ChrTalk(
        0x101,
        "#00011F#12PT-Tio?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xB, 3)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    OP_A1(0xB, 0x3E8, 0x5, 0x1E, 0x2B, 0x2C, 0x2B, 0x1E)
    Sleep(300)

    AnonymousTalk(
        0xB,
        (
            "#40WY-You know...\x02\x03",
            "When I ran and hugged you when we\x01",
            "reunited, it looked a little\x01",
            "painful...\x02\x03",
            "...Are you okay with this?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    ChrTalk(
        0x101,
        (
            "#00000F#12P#30WR-Right...\x02\x03",
            "#00004F............\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(250, 1000, -3750, 1000)
    OP_96(0x101, 0xFFFFFF9C, 0x0, 0xFFFFF15A, 0x1F4, 0x0)
    Fade(250)
    Sound(898, 0, 100, 0)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x20)

    def lambda_5048():
        OP_A0(0xFE, 1000, 0x1E, 0x22)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_5048)

    def lambda_5055():
        OP_A0(0xFE, 1000, 0x36, 0x39)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5055)
    WaitChrThread(0xB, 3)
    WaitChrThread(0x101, 3)
    Sleep(800)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xB,
        (
            "#05524F#2700V#5P#40WHaha... You're so\x01",
            "warm...\x02\x03",
            "#05526F#2701VI'm sorry it doesn't\x01",
            "feel as good as when\x01",
            "Elie does it, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xA8D)
    OP_C9(0x1, 0x80000000)

    ChrTalk(
        0x101,
        (
            "#00012F#12P#30WW-Well, it is what it\x01",
            "is...\x02\x03",
            "#00008F(Or rather, this is\x01",
            "bad... Tio's sweet smell\x01",
            "is...)\x02\x03",
            "#00011F(─No, I mustn't!)\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(812, 0, 60, 0)

    def lambda_518C():
        OP_A0(0xFE, 1000, 0x22, 0x25)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_518C)

    def lambda_5199():
        OP_A0(0xFE, 1000, 0x39, 0x3C)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5199)
    WaitChrThread(0xB, 3)
    WaitChrThread(0x101, 3)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00012F#12PAhem... And, your other\x01",
            "request?\x02\x03",
            "#00000FWe've come this far, so\x01",
            "might as well get on\x01",
            "with it?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A1(0xB, 0x3E8, 0x5, 0x25, 0x2E, 0x2F, 0x2E, 0x25)
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#05524F#5PYes, the other one is...\x02\x03",
            "#05522FWhen this incident is settled and\x01",
            "my parents come to Crossbell, I\x01",
            "want to see them with you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1900, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00009F#12PYes, of course. I'm just\x01",
            "thinking of saying hi to\x01",
            "them.\x02\x03",
            "#00002FBut, I think you'd never\x01",
            "ask for something like\x01",
            "that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#05526F#5PNo, not just a\x01",
            "greeting...\x02\x03",
            "#05528FI want to explain simply\x01",
            "my reason for remaining\x01",
            "in Crossbell.\x02\x03",
            "#05521FIf I don't, they'll\x01",
            "never accept it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#12P???\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#05524F#5PEveryone is here, Mishy is\x01",
            "here, there's an orbal network\x01",
            "and I love Crossbell...\x02\x03",
            "#05528FBut above all, how should I\x01",
            "live, and for what reason...\x02\x03",
            "#05522FI want to live forevermore by\x01",
            "the side of the person who\x01",
            "gave me that answer─\x02\x03",
            "#05529FThat's what I want to tell\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1900, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    ChrTalk(
        0x101,
        (
            "#00007F#12P#4SWhaaa!?#3S\x02\x03",
            "#00011FW-Wait just a minute\x01",
            "here! That's just\x01",
            "like...!\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrSubChip(0xB, 0x2E)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0xB,
        (
            "#05531F#5PAnything, you said,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1900, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    ChrTalk(
        0x101,
        (
            "#00012F#12P─Yeah, okay, I get it!\x02\x03",
            "#00002FOnce this incident is\x01",
            "resolved, I'll meet your\x01",
            "parents with you!\x02\x03",
            "#00006F*sigh*, I'll have to\x01",
            "start thinking of\x01",
            "excuses now...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrSubChip(0xB, 0x3E)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0xB,
        "#05529F#5PHaha... Do your best.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Sound(812, 0, 60, 0)
    SetChrSubChip(0xB, 0x2E)
    Sleep(50)
    SetChrSubChip(0xB, 0x25)
    Sleep(200)
    SetCameraDistance(10500, 3500)

    def lambda_5709():
        OP_A0(0xFE, 1000, 0x26, 0x29)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_5709)

    def lambda_5716():
        OP_A0(0xFE, 1000, 0x3C, 0x39)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5716)
    WaitChrThread(0xB, 3)
    WaitChrThread(0x101, 3)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopSound(132, 1000, 30)
    StopSound(497, 1000, 15)
    StopBGM(0x1388)
    WaitBGM()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21, 2)), scpexpr(EXPR_END)), "loc_575A")
    OP_CC(0x1, 0xFF, 0x0)
    NewScene("b0100", 0, 0, 0)
    IdleLoop()
    Return()

    label("loc_575A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_576C")
    Jump("loc_5823")

    label("loc_576C")

    Sleep(500)
    Sound(517, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Lloyd and Tio learned\x01",
            "Omega Strike Ⅲ.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and Tio's combination\x01",
            "craft, Omega Strike, has\x01",
            "been strengthened.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddCraft(0x2, 0x1AF)
    AddCraft(0x0, 0x1AF)

    label("loc_5823")

    OP_CC(0x1, 0xFF, 0x0)
    OP_E0(0x29, 0x0)
    OP_E0(0x80, 0x0)
    SetScenarioFlags(0x1AB, 2)
    OP_29(0xB1, 0x1, 0x2)
    Sleep(2000)
    SetScenarioFlags(0x23, 1)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_9_3871 end

    def Function_10_5846(): pass

    label("Function_10_5846")

    OP_A1(0xFE, 0x3E8, 0x6, 0x13, 0x14, 0x15, 0x16, 0x15, 0x14)
    OP_A1(0xFE, 0x3E8, 0x6, 0x13, 0x14, 0x15, 0x16, 0x15, 0x14)
    SetChrSubChip(0xFE, 0x13)
    Return()

    # Function_10_5846 end

    def Function_11_5863(): pass

    label("Function_11_5863")

    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x20)
    OP_A0(0xFE, 900, 0x0, 0x3)
    Sleep(300)
    Sound(898, 0, 100, 0)
    OP_A0(0xFE, 900, 0x4, 0xC)
    Sleep(300)
    OP_A0(0xFE, 1000, 0xC, 0xF)
    Sound(318, 0, 100, 0)
    Sleep(200)
    Sound(898, 0, 100, 0)
    OP_A0(0xFE, 1000, 0x10, 0x14)
    Sleep(500)
    Sound(812, 0, 100, 0)
    OP_A0(0xFE, 1000, 0x14, 0x1B)
    Sleep(300)
    OP_A0(0xFE, 1000, 0x1B, 0x1E)
    Return()

    # Function_11_5863 end

    def Function_12_58C4(): pass

    label("Function_12_58C4")

    OP_A1(0xFE, 0x3E8, 0x6, 0x23, 0x24, 0x25, 0x26, 0x25, 0x24)
    OP_A1(0xFE, 0x3E8, 0x6, 0x23, 0x24, 0x25, 0x26, 0x25, 0x24)
    SetChrSubChip(0xFE, 0x23)
    Return()

    # Function_12_58C4 end

    def Function_13_58E1(): pass

    label("Function_13_58E1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00300.itc", 0x1E)
    LoadChrToIndex("apl/ch51804.itc", 0x1F)
    LoadChrToIndex("apl/ch51805.itc", 0x20)
    SoundLoad(2778)
    SoundLoad(2779)
    SoundLoad(2780)
    SoundLoad(2781)
    SoundLoad(2782)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00301.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis266.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis267.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis268.itp")
    CreatePortrait(4, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis316.itp")
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    OP_F0(0x0, 0x1)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x1, 0x1000)
    OP_71(0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x101, 0, 120, 2750, 180)
    SetChrPos(0xC, 500, 0, -4250, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(470, 800, 1980, 0)
    MoveCamera(47, 18, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x8)
    OP_79(0x1)

    def lambda_5A92():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5A92)

    def lambda_5AA7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5AA7)
    PlayBGM("ed7560", 0)
    SetCameraDistance(14000, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 3)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xC,
        "#00300F#2778V#12P#N#30WYo, you came.\x02",
    )

    CloseMessageWindow()
    OP_24(0xADA)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0x101,
        "#00002F#5PRandy.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0xF, 1, 0, 8)
    Fade(1000)
    SetChrPos(0x101, 500, 0, 1250, 180)
    SetChrPos(0xC, 500, 0, -3750, 0)
    OP_68(500, 2300, -3750, 0)
    MoveCamera(125, -5, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(8500, 0)
    OP_68(500, 1600, -3750, 5000)
    MoveCamera(125, 1, 0, 5000)
    OP_6E(800, 5000)
    SetCameraDistance(9500, 5000)
    Sleep(4000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0xC,
        (
            "#2779V#40WDamn. Meeting with a guy like this\x01",
            "really cuts into my nightly\x01",
            "timetable.\x02\x03",
            "#2780VI'm not going to talk to you about\x01",
            "anything sexy, you know?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xADC)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_C9(0x1, 0x80000000)
    OP_68(630, 1000, -3200, 3000)
    MoveCamera(120, 10, 0, 3000)
    OP_6E(800, 3000)
    SetCameraDistance(10000, 3000)
    Sound(100, 0, 100, 0)

    def lambda_5D0D():

        label("loc_5D0D")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_5D0D")

    QueueWorkItem2(0xC, 2, lambda_5D0D)
    OP_95(0x101, 250, 0, -1750, 1200, 0x0)
    TurnDirection(0x101, 0xC, 500)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00006F#6P...So pointless stuff, then.\x02\x03",
            "#00001FIt's before the operation...\x01",
            "I don't have time to think\x01",
            "about stuff like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00306F#11PDummy. It's precisely\x01",
            "because of times like this\x01",
            "that you have to let loose.\x02\x03",
            "#00308F① "Lloyd, I'm worried..."\x02\x03",
            "#00301F② "It's all right, I'm with\x01",
            "you..."\x02\x03",
            "#00309F③ "Kyah!" That's the golden\x01",
            "combo right there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#6PThat last part was a bit\x01",
            "of a jump...\x02\x03",
            "#00012FRandy, I'm getting the\x01",
            "impression that your\x01",
            "cool attitude is fake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#00310F#11POh, really now?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xFA0)
    OP_68(110, 1000, -4070, 4000)
    MoveCamera(135, 15, 0, 4000)
    OP_6E(800, 4000)
    SetCameraDistance(10000, 30000)
    BeginChrThread(0x101, 3, 0, 14)
    Sleep(500)
    EndChrThread(0xC, 0x2)
    OP_93(0xC, 0xB4, 0x190)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7568", 0)
    Sleep(500)

    ChrTalk(
        0xC,
        (
            "#00300F#5P...Are you done\x01",
            "preparing for tomorrow?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PYeah. Honestly, I can't\x01",
            "say it's perfect, but...\x02\x03",
            "#00001FWhen I think about\x01",
            "Mireille and the others,\x01",
            "I think it's good enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00306F#5PI guess...\x02\x03",
            "#00303FThey'll likely send large\x01",
            "numbers of jaegers to the\x01",
            "resistance and Heiyue areas.\x02\x03",
            "#00308FUncle or Shirley won't come\x01",
            "out that easily, though...\x02\x03",
            "#00301FBut if someone like Gareth\x01",
            "appears, it'll be a pretty\x01",
            "tough fight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6PIs that so...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 3)
    EndChrThread(0xC, 0x2)
    OP_63(0x101, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xC, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0xC)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00006F#6PRed Constellation... Their\x01",
            "battle power is more than\x01",
            "their name suggests.\x02\x03",
            "#00000FI feel like I agree with\x01",
            "those who say they're the\x01",
            "strongest in West Zemuria.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00306F#5PWell, they can trace their history all the way\x01",
            "back to the middle ages.\x02\x03",
            "#00301FBerzerker Orlando...\x02\x03",
            "At that time, all warriors who knew his name\x01",
            "were a family.\x02\x03",
            "#00308FBy constantly adopting the latest combat\x01",
            "techniques and strengthening their bodies with\x01",
            "special training methods, they have continued\x01",
            "to be called the "strongest" of the corps...\x02\x03",
            "#00303FAs a jaeger corps of present day, they have\x01",
            "taken up the name of the red scorpion on that\x01",
            "family's coat of arms.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#6PI see...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1850, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0xC, 500)

    ChrTalk(
        0x101,
        (
            "#00005F#12PCould it be that...\x02\x03",
            "#00001FWas the race in Downtown\x01",
            "we did before one of\x01",
            "those?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)
    Sleep(100)

    ChrTalk(
        0xC,
        (
            "#00309F#5PHaha, you noticed.\x02\x03",
            "#00300FThat's an arrangement Red\x01",
            "Constellation uses for combat\x01",
            "training.\x02\x03",
            "#00306FMost of all, it's normally a\x01",
            "substitute for being near a battle,\x01",
            "where you can die at any time.\x02\x03",
            "When I was a kid, I was made to do\x01",
            "it every day 'til I coughed up\x01",
            "blood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#12PI see...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)

    ChrTalk(
        0x101,
        (
            "#00000F#12P...And the one who trained\x01",
            "you like that was your old\x01",
            "man, the War God, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00306F#5PYeah─ Baldur Orlando.\x02\x03",
            "#00308FHe was a strict and\x01",
            "merciless father like a\x01",
            "steel lion.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x1770)
    OP_93(0xC, 0xB4, 0x190)
    Fade(1000)
    OP_71(0x1, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x101, -500, 0, -4250, 90)
    SetChrPos(0xC, 500, 0, -4250, 180)
    OP_68(0, 1000, -4250, 0)
    MoveCamera(45, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    SetCameraDistance(16000, 3000)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)

    ChrTalk(
        0xC,
        (
            "#00303F#5P#30W─Three years ago.\x02\x03",
            "I got a certain mission\x01",
            "from that War God.\x02\x03",
            "#00308FTwo companies of Zephyr,\x01",
            "our longtime rival\x01",
            "jaeger corps...\x02\x03",
            "#00311FThe mission was to\x01",
            "annihilate them with my\x01",
            "own force.\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7567", 0)
    SetCameraDistance(15000, 2500)
    StopSound(132, 2000, 30)
    StopSound(497, 2000, 15)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    Sleep(800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xC,
        (
            "#3C#30WThe enemy's strength was\x01",
            "twice mine...\x02\x03",
            "Thinking about going up\x01",
            "against them, honestly, it\x01",
            "was too severe a difference.\x02\x03",
            "But surprise attacks and use\x01",
            "of terrain advantage were\x01",
            "our forte.\x02\x03",
            "And I...\x02\x03",
            "...There was this village I\x01",
            "usually went to for\x01",
            "supplies.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(800)
    SetMessageWindowPos(280, 145, -1, -1)

    AnonymousTalk(
        0xC,
        (
            "#3C#30WUsing a surprise attack as a\x01",
            "diversion, we drew one company\x01",
            "into the village...\x02\x03",
            "And by deciding to cause a\x01",
            "landslide, the other company\x01",
            "was utterly crushed.\x02\x03",
            "And by exploding a barn on the\x01",
            "outskirts, we caused the enemy\x01",
            "to panic...\x02\x03",
            "Reading their escape route out\x01",
            "of the village, we concentrated\x01",
            "our firepower and crushed them.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xC,
        (
            "#3C#30W...I intended to sacrifice\x01",
            "not a single one of the\x01",
            "villagers.\x02\x03",
            "But, probabilities in\x01",
            "battle are fluid and\x01",
            "unreliable.\x02\x03",
            "In the end, the point at\x01",
            "which we opened fire was 50\x01",
            "arge from the village...\x02\x03",
            "And one house, the general\x01",
            "store, got wrapped up in\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x7D0, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    Sleep(800)
    SetMessageWindowPos(280, 145, -1, -1)

    AnonymousTalk(
        0xC,
        (
            "#3C#40W...I think I could say\x01",
            "they were my first\x01",
            "friends, jaegers excluded.\x02\x03",
            "When I didn't have a\x01",
            "mission, I'd drink at the\x01",
            "bar and pick up ladies...\x02\x03",
            "Before long I'd leave, and\x01",
            "I dreamed of running my\x01",
            "own store one day.\x02\x03",
            "That dream, and life. All\x01",
            "of it was stolen from me.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    Sound(858, 0, 100, 0)
    Sleep(1500)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    Sleep(1300)
    SetMessageWindowPos(280, 170, -1, -1)
    SetChrName("Shirley")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#30WWah! You're pretty good,\x01",
            "Randy!♪\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(30, 150, -1, -1)
    SetChrName("Ogre Sigmund")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x14),
            "#30WHehe─ You pass, Randolph.\x02\x03",
            "Because of this "test", it's\x01",
            "decided that you are the\x01",
            "next War God.\x02\x03",
            "You should work from now on\x01",
            "to be worthy of following in\x01",
            "your old man's footsteps.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sound(132, 2, 35, 0)
    Sound(497, 2, 20, 0)
    MoveCamera(40, 20, 0, 50000)
    SetCameraDistance(16540, 50000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x101,
        "#00008F#6P#30W............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00306F#5P#30W...A pretty disorganized\x01",
            "story, no?\x02\x03",
            "#00308FI didn't particularly want\x01",
            "to leave the battlefield\x01",
            "because of his death.\x02\x03",
            "It's more like I was sick\x01",
            "and tired of the life of a\x01",
            "jaeger.\x02\x03",
            "#00303FI still don't understand\x01",
            "it.\x02\x03",
            "The meagre dream of that\x01",
            "guy, who wanted his own\x01",
            "store someday...\x02\x03",
            "And becoming the War God at\x01",
            "some point, and continuing\x01",
            "to fight until he died...\x02\x03",
            "#00311FI wonder if there's meaning\x01",
            "in both of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#6P#30W...Randy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00303F#5P#30WThat's probably the "fate" I'm\x01",
            "burdened with.\x02\x03",
            "I was born into the Orlando\x01",
            "family, but I can't put everything\x01",
            "I have into fighting. That's me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6P#30W............\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#00006F#6PRandy, do you intend to\x01",
            "break that "fate"?\x02\x03",
            "#00001FBy surpassing your\x01",
            "uncle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00306F#5P...I guess.\x02\x03",
            "#00308FThough now that my old\x01",
            "man's dead, there's no way\x01",
            "of breaking that "fate".\x02\x03",
            "If I can overcome that\x01",
            "monster with my current\x01",
            "strength...\x02\x03",
            "#00300FI feel like I'd finally\x01",
            "settle the score from\x01",
            "three years ago.\x02\x03",
            "#00304FThat's all─ So there you\x01",
            "have it.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_73C6")

    ChrTalk(
        0x101,
        (
            "#00004F#6PI see...\x02\x03",
            "#00000FOf course, you'll allow\x01",
            "me to assist as your\x01",
            "partner, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7436")

    label("loc_73C6")


    ChrTalk(
        0x101,
        (
            "#00004F#6PI see...\x02\x03",
            "#00000FIf you say it like that, then\x01",
            "you'll allow me to assist as\x01",
            "your partner, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7436")

    TurnDirection(0xC, 0x101, 400)
    Sleep(250)

    ChrTalk(
        0xC,
        (
            "#00302F#11PYeah, please do.\x02\x03",
            "#00306FIf possible I'd have liked to\x01",
            "settle the score with my own power,\x01",
            "but that opponent is just too much.\x02\x03",
            "#00300FSorry but, can I count on you?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7585")

    ChrTalk(
        0x101,
        (
            "#00004F#6PYeah, of course.\x02\x03",
            "#00002FYou might be more of a partner\x01",
            "than I deserve... but I'm\x01",
            "happy you're relying on me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7601")

    label("loc_7585")


    ChrTalk(
        0x101,
        (
            "#00004F#6PYeah, of course.\x02\x03",
            "#00002FYou might be more of a friend\x01",
            "than I deserve... but I'm\x01",
            "happy you're relying on me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7601")


    ChrTalk(
        0xC,
        (
            "#00315F#11PHehe... I'm telling you,\x01",
            "I'm not trying to\x01",
            "deceive you.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)

    ChrTalk(
        0x101,
        "#00005F#6PHuh...?\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7581", 0)
    Fade(1000)
    SetChrPos(0x101, -600, 0, -3750, 90)
    SetChrPos(0xC, 600, 0, -3750, 270)
    OP_68(0, 1000, -3750, 0)
    MoveCamera(135, 10, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(10000, 0)
    MoveCamera(140, 15, 0, 70000)
    SetCameraDistance(9000, 70000)
    SetChrFlags(0xC, 0x2)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x1)
    OP_0D()
    Sound(802, 0, 100, 0)
    OP_A1(0xC, 0x3E8, 0x4, 0x1, 0x2, 0x2, 0x2)
    Sound(854, 0, 100, 0)
    OP_A1(0xC, 0x3E8, 0x4, 0x2, 0x3, 0x3, 0x3)
    Sleep(300)
    Fade(250)
    SetChrSubChip(0xC, 0x4)
    OP_0D()
    Sleep(300)
    OP_CB(0x4, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    Sleep(500)

    AnonymousTalk(
        0x101,
        "#00005FIs that... alcohol?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0xC,
        (
            "#00304F#5PIt's rum. The good\x01",
            "stuff.\x02\x03",
            "#00300FIt's the bottle he kept\x01",
            "for me there.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x4, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 1850, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00000F#12P...I see...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(812, 0, 100, 0)
    Sound(857, 0, 100, 0)
    OP_A1(0xC, 0x3E8, 0x5, 0x4, 0x5, 0x6, 0x6, 0x6)

    ChrTalk(
        0xC,
        (
            "#00300F#5PI left it with the rifle,\x01",
            "but things got out of\x01",
            "control.\x02\x03",
            "#00304FBut now, I feel like\x01",
            "drinking down the rest.\x02\x03",
            "#00302FIt'll liven up this night\x01",
            "before battle. Care to\x01",
            "join me for a shot?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)

    ChrTalk(
        0x101,
        "#00002F#12PYeah─ I'd love to.\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_791E():
        OP_A0(0xFE, 1000, 0x7, 0x8)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_791E)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x20)

    def lambda_7934():
        OP_A0(0xFE, 1000, 0x1, 0x2)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7934)
    WaitChrThread(0xC, 3)
    WaitChrThread(0x101, 3)
    Fade(250)
    Sound(855, 0, 100, 0)
    SetChrSubChip(0xC, 0x9)
    OP_0D()
    Sleep(1000)
    Sleep(1000)
    Fade(250)
    Sound(855, 0, 100, 0)
    SetChrSubChip(0xC, 0xA)
    SetChrSubChip(0x101, 0x4)
    OP_0D()
    Sleep(1000)
    Sleep(300)

    def lambda_7979():
        OP_A0(0xFE, 800, 0xA, 0xC)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_7979)
    Sleep(100)

    def lambda_7989():
        OP_A0(0xFE, 1000, 0x4, 0x6)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7989)
    WaitChrThread(0xC, 3)
    WaitChrThread(0x101, 3)
    Sleep(300)

    ChrTalk(
        0xC,
        (
            "#00304F#5P...Just as I was gettin'\x01",
            "hungry, huh.\x02\x03",
            "#00300FDon't push yourself, ok?\x01",
            "Just a little should be\x01",
            "plenty intense.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrSubChip(0xC, 0x8)
    SetChrSubChip(0x101, 0x4)
    OP_0D()
    Sleep(150)

    ChrTalk(
        0x101,
        (
            "#00004F#12PWell, once I grow up a\x01",
            "bit more I'll be fine\x01",
            "with this stuff.\x02\x03",
            "#00000FCheers, Randy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#00302F#5PRight.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_7AB1():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7AB1)

    def lambda_7ACA():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_7ACA)
    Fade(250)
    SetChrSubChip(0x101, 0x7)
    SetChrSubChip(0xC, 0xD)
    Sleep(50)
    Sound(856, 0, 100, 0)
    OP_0D()
    WaitChrThread(0x101, 3)
    WaitChrThread(0xC, 3)
    Sleep(500)
    Fade(250)
    SetChrSubChip(0xC, 0xE)
    SetChrSubChip(0x101, 0x8)
    OP_0D()
    Sleep(1000)

    def lambda_7B16():
        OP_A0(0xFE, 1000, 0xE, 0x10)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_7B16)
    Sound(2030, 255, 60, 0)
    OP_A0(0x101, 1000, 0x9, 0xB)
    OP_A0(0x101, 1000, 0x9, 0xB)
    OP_A0(0x101, 1000, 0x9, 0xB)
    WaitChrThread(0xC, 3)
    OP_A1(0xC, 0x3E8, 0x8, 0x10, 0x11, 0x12, 0x12, 0x13, 0x14, 0x13, 0x12)
    OP_A0(0x101, 1000, 0x9, 0xB)

    ChrTalk(
        0x101,
        (
            "#00015F#12P#40W*cough*...\x02\x01",
            "#00008F#30W...It packs a punch...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#00309F#5PHaha, told you so.\x02\x03",
            "#00302FWell, this stuff has an\x01",
            "adult flavor, you know.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_7BF6():
        OP_A0(0xFE, 1000, 0x15, 0x16)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_7BF6)

    def lambda_7C03():
        OP_A0(0xFE, 1000, 0xC, 0xD)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7C03)
    WaitChrThread(0xC, 3)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x101,
        (
            "#00013F#12PGuh... I'm telling you─\x01",
            "I'm almost an adult.\x02\x03",
            "#00004F...Say, Randy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#00305F#5PHmm, what is it?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(802, 0, 80, 0)
    OP_A0(0x101, 1000, 0xD, 0xE)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00002F#12PLet's go to the Back\x01",
            "Street jazz bar once all\x01",
            "this is over.\x02\x03",
            "There, we can both set\x01",
            "up bottle keeps. Sound\x01",
            "good?\x02\x03",
            "#00012FIf possible, I'd like to\x01",
            "do more adult things.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 1950, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Sound(802, 0, 100, 0)
    OP_A1(0xC, 0x3E8, 0x8, 0x16, 0x17, 0x18, 0x18, 0x19, 0x1A, 0x19, 0x18)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xC,
        "#00302F#2781V#5P#40WYeah... let's.\x02",
    )

    CloseMessageWindow()
    OP_24(0xADD)
    OP_57(0x0)
    OP_5A()
    OP_A1(0xC, 0x3E8, 0x3, 0x18, 0x19, 0x1A)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0xC,
        "#00315F#2782V#5P#40WYeah─ Let's go all out!\x02",
    )

    CloseMessageWindow()
    OP_24(0xADE)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(10500, 3000)
    FadeToDark(2000, 0, -1)
    OP_A1(0xC, 0x3E8, 0x3, 0x1A, 0x19, 0x18)
    OP_0D()
    StopSound(132, 1000, 30)
    StopSound(497, 1000, 15)
    StopBGM(0x1194)
    WaitBGM()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21, 2)), scpexpr(EXPR_END)), "loc_7E54")
    OP_CC(0x1, 0xFF, 0x0)
    NewScene("b0100", 0, 0, 0)
    IdleLoop()
    Return()

    label("loc_7E54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7E66")
    Jump("loc_7F1F")

    label("loc_7E66")

    Sleep(500)
    Sound(517, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Lloyd and Randy learned\x01",
            "Burning Rage Ⅲ.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and Randy's\x01",
            "combination craft, Burning\x01",
            "Rage, has been strengthened.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddCraft(0x3, 0x1B0)
    AddCraft(0x0, 0x1B0)

    label("loc_7F1F")

    OP_CC(0x1, 0xFF, 0x0)
    OP_E0(0x2A, 0x0)
    OP_E0(0x80, 0x0)
    SetScenarioFlags(0x1AB, 3)
    OP_29(0xB1, 0x1, 0x3)
    Sleep(2000)
    SetScenarioFlags(0x23, 1)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_13_58E1 end

    def Function_14_7F42(): pass

    label("Function_14_7F42")

    OP_95(0x101, -500, 0, -3750, 1000, 0x0)
    OP_93(0x101, 0xB4, 0x1F4)
    Return()

    # Function_14_7F42 end

    def Function_15_7F5E(): pass

    label("Function_15_7F5E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02900.itc", 0x1E)
    LoadChrToIndex("apl/ch51020.itc", 0x1F)
    LoadChrToIndex("apl/ch51806.itc", 0x20)
    LoadChrToIndex("apl/ch51807.itc", 0x21)
    SoundLoad(3532)
    SoundLoad(3533)
    SoundLoad(3534)
    SoundLoad(3535)
    SoundLoad(4110)
    SoundLoad(3536)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10100.itp")
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis337.itp")
    CreatePortrait(2, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis338.itp")
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    OP_F0(0x0, 0x1)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x1, 0x1000)
    OP_71(0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x101, 0, 120, 2750, 180)
    SetChrPos(0xD, 500, 0, -3750, 180)
    OP_68(500, 5500, -3750, 0)
    MoveCamera(135, -15, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(8500, 0)
    PlayBGM("ed7560", 0)
    FadeToBright(1000, 0)
    OP_68(500, 1000, -3750, 8000)
    MoveCamera(135, 10, 0, 8000)
    OP_6E(800, 8000)
    SetCameraDistance(9500, 8000)
    OP_6F(0x79)
    BeginChrThread(0xF, 1, 0, 8)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xD,
        (
            "#10106F#3532V#40W...*sigh*... What should I\x01",
            "do...\x02\x03",
            "#10108F#3533VAt a time like this...#400W...\x01",
            "#10101F#40WBut if I let this chance go...!\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xDCD)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetChrPos(0xD, 500, 0, -4250, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 1000, -1500, 0)
    MoveCamera(40, 10, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    SetCameraDistance(19500, 2000)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x8)
    OP_79(0x1)

    def lambda_81F1():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_81F1)

    def lambda_8206():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_8206)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 3)

    ChrTalk(
        0x101,
        (
            "#00002F#5PNoｱl, you got here\x01",
            "first.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1850, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0xD, 0x0, 1850, 0x28, 0x2B, 0x64, 0x3)

    def lambda_8278():

        label("loc_8278")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_8278")

    QueueWorkItem2(0xD, 2, lambda_8278)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xD,
        (
            "#10112F#3534V#12P#40WL-Lloyd! Good work\x01",
            "today!\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xDCE)
    OP_C9(0x1, 0x80000000)
    OP_68(0, 1000, -4250, 3000)
    MoveCamera(35, 20, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(15500, 3000)

    def lambda_82FE():
        OP_95(0xFE, -500, 0, -4250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_82FE)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0xA, 0x0, 0x0, 0x8)
    OP_79(0x1)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0xD, 500)
    EndChrThread(0xD, 0x2)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00004F#6PHaha, same to you.\x02\x03",
            "#00000FIt looks like you're\x01",
            "finished contacting\x01",
            "Commander Sonya?\x02",
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
        0xD,
        (
            "#30WAh, yes.\x02\x03",
            "She said she'll have soldiers from\x01",
            "Bellguard and Tangram Gates standby\x01",
            "until noon.\x02\x03",
            "She said she can't intervene any\x01",
            "more than that, though...\x02",
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
            "#00006F#6PI see... Well, even a\x01",
            "temporary standby is\x01",
            "helpful.\x02\x03",
            "#00013FIf that's the case, then\x01",
            "I think our duty is even\x01",
            "more important.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#10103F#11PRight...\x02\x03",
            "#10108F#30W............\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6P...The State Guard in the\x01",
            "city will likely be\x01",
            "assigned to city defense.\x02\x03",
            "#00001FI think we can avoid\x01",
            "fighting the State Guard\x01",
            "in urban areas.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#10106F#11PNo, I'm already prepared\x01",
            "for that.\x02\x03",
            "#10108FIt's just, I was\x01",
            "thinking I'm kind of\x01",
            "pathetic.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_63(0x101, 0x0, 1850, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#6PHuh...?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetChrPos(0x101, -500, 0, -3750, 90)
    SetChrPos(0xD, 500, 0, -3750, 270)
    OP_68(250, 1000, -4400, 0)
    MoveCamera(145, 15, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(11000, 0)
    OP_68(0, 1000, -3750, 50000)
    MoveCamera(135, 20, 0, 50000)
    OP_6E(800, 50000)
    SetCameraDistance(10000, 50000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7568", 0)
    Sleep(500)

    ChrTalk(
        0xD,
        (
            "#10108F#5P#30WI honestly thought independence\x01",
            "and the State Guard were\x01",
            "mistakes.\x02\x03",
            "#10106FBut I... didn't have the spirit\x01",
            "to join Mireille's resistance and\x01",
            "just went with the flow...\x02\x03",
            "It made me realize that, in a\x01",
            "way, I've been living only within\x01",
            "the small world of the CGF.\x02\x03",
            "#10113FEven though the commander gave me\x01",
            "this opportunity for a temporary\x01",
            "transfer...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#12PEveryone is like that, Noｱl.\x02\x03",
            "#00008FEven me. Were it not for KeA\x01",
            "and everyone, I would have been\x01",
            "swept up by that flow as well.\x02\x03",
            "#00012FOriginally, I didn't have the\x01",
            "personality to do great things,\x01",
            "you know.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1850, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xD,
        (
            "#10112F#5PUmm... I would have\x01",
            "never expected that.\x02\x03",
            "#10114FIf not, then how could\x01",
            "you ever say something\x01",
            "like "You're mine"...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#12PHuh?\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1850, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(
        0xD,
        "#10112F#5PN-No, nothing!\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F#12P???\x02\x03",
            "#00004FIn any case, what's\x01",
            "important is whether\x01",
            "there's a chance.\x02\x03",
            "And you seized that\x01",
            "chance and are here with\x01",
            "us.\x02\x03",
            "#00008FIt's not for me to\x01",
            "decide whether that's\x01",
            "right or wrong, but...\x02\x03",
            "#00002FYou're a great help to\x01",
            "us. ─That makes me\x01",
            "happiest of all.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1850, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xD,
        (
            "#10114F#5PL-Lloyd...\x02\x03",
            "#10106F............\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xD, 0x5A, 0x258)
    Sleep(500)

    ChrTalk(
        0xD,
        (
            "#10108F#11P#30W(C-Calm down, Noｱl Seeker!)\x02\x03",
            "#10103F(Just like in training, you have\x01",
            "to quickly assess the situation\x01",
            "and control your morale!)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005F#12POh right, you said you\x01",
            "needed a favor but...\x02\x03",
            "#00002FUmm, what is it?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1850, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xD, 0x101, 500)

    ChrTalk(
        0xD,
        "#10105F#5PAh, right! About that─\x02",
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)

    ChrTalk(
        0xD,
        (
            "#10106F#5PUmm... Ah...\x02\x03",
            "#10108FI'm gonna ask you\x01",
            "something weird but...\x02\x03",
            "#10101FA-Are you going out with\x01",
            "anyone Lloyd?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1850, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00005F#12PWhat!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#10112F#5PN-No! There's no deep\x01",
            "meaning!\x02\x03",
            "#10102FUmm, yeah, Fran was\x01",
            "wondering about it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00011F#12PO-Oh, I see.\x02\x03",
            "#00012FHaha. Girls like stuff\x01",
            "like that, huh.\x02\x03",
            "#00006FHmm. I'm sorry to say I\x01",
            "don't right now.\x02\x03",
            "#00000FI'm a little disappointed\x01",
            "because there's so many\x01",
            "good girls around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#10112F#5P#30WA-Ahaha... No way. (He's\x01",
            "not doing this on\x01",
            "purpose, right?)\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    Sleep(1200)

    ChrTalk(
        0xD,
        "#10103F#5P#30WAhem...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetChrPos(0x101, -500, 0, -4250, 90)
    SetChrPos(0xD, 500, 0, -4250, 270)
    OP_68(0, 1000, -4250, 0)
    MoveCamera(30, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    SetCameraDistance(16500, 2000)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7581", 0)
    Fade(250)
    Sound(802, 0, 50, 0)
    SetChrFlags(0xD, 0x2)
    SetChrChipByIndex(0xD, 0x20)
    SetChrSubChip(0xD, 0x0)
    OP_0D()
    Sleep(500)
    OP_68(0, 1000, -4250, 70000)
    MoveCamera(35, 20, 0, 70000)
    OP_6E(500, 70000)
    SetCameraDistance(14500, 70000)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xD,
        "#10103F#3535V#11P#40W─Umm, in that case.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrSubChip(0xD, 0x1)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0xD,
        (
            "#10101F#4110V#11P#40WWill you hold on to this\x01",
            "for me for a while?\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0x100E)
    OP_C9(0x1, 0x80000000)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(500)

    AnonymousTalk(
        0x101,
        (
            "#00005FTh-This is...\x02\x03",
            "#00001FYour dog tag from the\x01",
            "Guardian Force?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0xD,
        (
            "#10104F#11PYes. I didn't need it\x01",
            "after changing over to the\x01",
            "State Guard, but...\x02\x03",
            "#10100FSomehow, I couldn't throw\x01",
            "them away, so I've held\x01",
            "onto them this whole time.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00004F#6POh...\x02\x03",
            "#00005FBut, why me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#10106F#11P...Honestly, I think tomorrow's\x01",
            "plan will be difficult.\x02\x03",
            "#10101FIf something happens to me...\x02\x03",
            "#10112FNo─ It's to complete the mission.\x01",
            "In other words, I want you to hold\x01",
            "on to it for me for good luck.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#6PNoｱl...\x02\x03",
            "#00004FGot it. I'll gladly hold\x01",
            "on to it for you.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    Fade(250)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x2)
    OP_0D()
    Sleep(800)
    Fade(250)
    Sound(802, 0, 50, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x2)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0xD,
        (
            "#10109F#11POh... Thank you very\x01",
            "much!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#6PHaha, it's not really something\x01",
            "you have to thank me for,\x01",
            "though.\x02\x03",
            "#00008FAnd you'll be working with all\x01",
            "of us...\x02\x03",
            "#00000FSo please, when you're in a\x01",
            "pinch, don't think of\x01",
            "sacrificing yourself for us, ok?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1850, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xD,
        "#10111F#11P#30WW-Why do you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6PI just know these things.\x02\x03",
            "#00001FLike I said before, you don't\x01",
            "have to worry about the time\x01",
            "you captured us at all.\x02\x03",
            "#00002FIn the end, I want you to\x01",
            "come with us as a member of\x01",
            "the Support Section.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#10114F#11P#30W...Lloyd...\x02\x03",
            "#10116F*sob*... Roger,\x01",
            "understood!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00009F#6PHaha...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(812, 0, 50, 0)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x2)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00000F#6PBut who should I give my\x01",
            "own tag to...?\x02\x03",
            "#00012FHaha, it's kind of like\x01",
            "what lovers would do.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1850, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xD,
        "#10114F#11P...!\x02",
    )

    CloseMessageWindow()
    OP_93(0xD, 0x5A, 0x258)
    Sleep(300)

    def lambda_96CE():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_96CE)
    WaitChrThread(0xD, 2)
    Sleep(500)

    ChrTalk(
        0x101,
        "#00005F#6PHuh─\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#10106F#5P#40W............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001F#6PNoｱl...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)
    Fade(250)
    Sound(812, 0, 60, 0)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x21)
    OP_A1(0x101, 0x320, 0x7, 0x0, 0x1, 0x2, 0x1, 0x2, 0x1, 0x2)
    OP_0D()

    ChrTalk(
        0x101,
        (
            "#00011F#6PUmm, ah...\x02\x03",
            "#00012FIs that really its\x01",
            "meaning?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#10106F#5P#40W......(*nods*)\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6P#30WI-I see...\x02\x03",
            "#00000F............\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x2)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00006F#6PUmm... I don't know if\x01",
            "this is an answer but...\x02\x03",
            "#00000FCould you please hang on\x01",
            "to this for me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#10114F#5P#30WHuh...\x02",
    )

    CloseMessageWindow()
    OP_93(0xD, 0x10E, 0x1F4)
    Fade(250)
    Sound(802, 0, 50, 0)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x3)
    OP_0D()
    Sleep(150)
    Sleep(300)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(300)

    AnonymousTalk(
        0xD,
        (
            "#10105F#11PThis is... from the\x01",
            "Crossbell Police?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    AnonymousTalk(
        0x101,
        (
            "#00002F#6PI really should wear\x01",
            "these as an officer on\x01",
            "duty, but...\x02\x03",
            "#00004FUntil this case is\x01",
            "solved, I want you to\x01",
            "hang on to them, Noｱl.\x02\x03",
            "#00000FAfter that, I'll find\x01",
            "you and give you a real\x01",
            "answer.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)

    ChrTalk(
        0xD,
        "#10116F#11P#30W#2S...Ah...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrFlags(0xD, 0x2)
    SetChrChipByIndex(0xD, 0x20)
    SetChrSubChip(0xD, 0x0)
    OP_0D()
    Sleep(500)
    Fade(250)
    Sound(812, 0, 50, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x2)
    OP_0D()
    Sleep(500)
    Sound(802, 0, 100, 0)
    Fade(250)
    SetChrChipByIndex(0xD, 0x1F)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x2)
    OP_0D()
    Sleep(300)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xD,
        "#10117F#3536V#11P#30WYes─ I'd love to!\x02",
    )

    CloseMessageWindow()
    OP_24(0xDD0)
    OP_C9(0x1, 0x80000000)
    SetCameraDistance(16000, 3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopSound(132, 2000, 30)
    StopSound(497, 2000, 15)
    StopBGM(0x1388)
    WaitBGM()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21, 2)), scpexpr(EXPR_END)), "loc_9AFE")
    OP_CC(0x1, 0xFF, 0x0)
    NewScene("b0100", 0, 0, 0)
    IdleLoop()
    Return()

    label("loc_9AFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9B10")
    Jump("loc_9BC7")

    label("loc_9B10")

    Sleep(500)
    Sound(517, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Lloyd and Noｱl learned\x01",
            "Brave Hearts II.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and Noｱl's combination\x01",
            "craft, Brave Hearts, has\x01",
            "been strengthened.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddCraft(0x0, 0x1A0)
    AddCraft(0x8, 0x1A0)

    label("loc_9BC7")

    OP_CC(0x1, 0xFF, 0x0)
    OP_E0(0x25, 0x0)
    OP_E0(0x80, 0x0)
    SetScenarioFlags(0x1AB, 4)
    OP_29(0xB1, 0x1, 0x4)
    Sleep(2000)
    SetScenarioFlags(0x23, 1)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_15_7F5E end

    def Function_16_9BEA(): pass

    label("Function_16_9BEA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch03100.itc", 0x1E)
    LoadChrToIndex("apl/ch51808.itc", 0x1F)
    LoadChrToIndex("apl/ch51813.itc", 0x20)
    SoundLoad(2926)
    SoundLoad(2927)
    SoundLoad(2928)
    SoundLoad(2929)
    SoundLoad(2930)
    SoundLoad(2430)
    SoundLoad(2431)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10401.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis325.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis349.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis326.itp")
    CreatePortrait(4, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis327.itp")
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    OP_F0(0x0, 0x1)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x1, 0x1000)
    OP_71(0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x101, 0, 120, 2750, 180)
    SetChrPos(0xE, 500, 0, -4250, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 1000, -1500, 0)
    MoveCamera(40, 10, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(18500, 2000)
    PlayBGM("ed7560", 0)
    FadeToBright(1000, 0)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x8)
    OP_79(0x1)

    def lambda_9DB7():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9DB7)

    def lambda_9DCC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_9DCC)
    OP_0D()
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 3)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xE,
        "#10402F#2926V#11P#30WHey, you came.\x02",
    )

    CloseMessageWindow()
    OP_24(0xB6E)
    OP_C9(0x1, 0x80000000)

    ChrTalk(
        0x101,
        "#00000F#5PYeah...\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xF, 1, 0, 8)
    OP_68(0, 1000, -4250, 3000)
    MoveCamera(45, 20, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(15500, 3000)

    def lambda_9E6B():
        OP_95(0xFE, -500, 0, -4250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9E6B)

    def lambda_9E85():

        label("loc_9E85")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_9E85")

    QueueWorkItem2(0xE, 2, lambda_9E85)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0xA, 0x0, 0x0, 0x8)
    OP_79(0x1)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0xE, 500)
    EndChrThread(0xE, 0x2)
    OP_6F(0x79)

    ChrTalk(
        0x101,
        (
            "#00006F#6PYou teased me like that,\x01",
            "so I don't think I had\x01",
            "any choice.\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0xE,
        (
            "#2927V#30WHaha. I like that about you. You're\x01",
            "honest.\x02\x03",
            "#2928VI don't think I'd be too much to\x01",
            "say I love you.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xB70)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_C9(0x1, 0x80000000)

    ChrTalk(
        0x101,
        (
            "#00006F#6PThat aside.\x02\x03",
            "#00001F...What about KeA? Tell\x01",
            "me that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#10404F#11PHaha, roger.\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    SetChrPos(0x101, -920, 0, -3910, 90)
    SetChrPos(0xE, 500, 0, -3750, 270)
    OP_68(-360, 3200, -3950, 0)
    MoveCamera(136, -7, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(9500, 0)
    OP_68(-360, 2100, -3950, 3000)
    MoveCamera(135, 0, 0, 3000)
    OP_6E(800, 3000)
    OP_6F(0x79)
    SetCameraDistance(9000, 50000)

    ChrTalk(
        0xE,
        (
            "#10408F#5PI really shouldn't tell this to an\x01",
            "outsider, but...\x02\x03",
            "#10400FWhen it comes to dealing with the\x01",
            "Sept-Terrion of Zero, the Church has\x01",
            "taken a basically hands-off position.\x02\x03",
            "#10403F─No matter how this case ends.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1850, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#00007F#11PSeriously!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#10406F#5PYeah. The Snakes have retreated,\x01",
            "and now that the original Sept-\x01",
            "Terrion is lost, we can intervene.\x02\x03",
            "#10400FThe meaning of that is, we\x01",
            "couldn't have simply chosen to\x01",
            "take KeA away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11PI see... Thank you for\x01",
            "letting me know.\x02\x03",
            "#00005FBut Wazy, is there any\x01",
            "problem with you continuing\x01",
            "to cooperate with us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#10403F#5PThe Fool and the 7th pillar have\x01",
            "left, but evacuation of the 6th\x01",
            "pillar hasn't been confirmed.\x02\x03",
            "#10408FAnd in the first place, those dolls\x01",
            "they gave to the Crois family will\x01",
            "have a significant influence...\x02\x03",
            "#10400FUntil that influence is gone, we'll\x01",
            "keep intervening, to a minimum\x01",
            "level, at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#11PI see...\x02\x03",
            "#00001FIt seems like, the more I hear,\x01",
            "the more disconnected this\x01",
            "fight is from common sense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#10404F#5PHaha. The world you all live in\x01",
            "is defined by the interaction of\x01",
            "surface and subsurface worlds.\x02\x03",
            "#10402FAnd─ I guess the conclusion of\x01",
            "my two-year infiltration mission\x01",
            "to Crossbell will be a big one.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1850, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00011F#11PCome to think of it...\x01",
            "You're 17, aren't you Wazy.\x02\x03",
            "#00003FThat means you were assigned\x01",
            "this mission two years ago,\x01",
            "when you were 15...\x02\x03",
            "#00001FBut, isn't Dominion a pretty\x01",
            "important position?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#10405F#5PYeah, but a Dominion isn't\x01",
            "something you become through\x01",
            "achievements.\x02\x03",
            "#10400FOnly those on which the "mark"\x01",
            "appears can become one. And\x01",
            "becoming one is preordained...\x02\x03",
            "#10409FWell, that occult stuff is\x01",
            "pretty suspicious, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#11PDon't talk about\x01",
            "yourself like that...\x02\x03",
            "#00001F...But this mark, could\x01",
            "it be that thing I see\x01",
            "sometimes in battle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#10404F#5PYeah...\x02",
    )

    CloseMessageWindow()
    OP_93(0xE, 0xB4, 0x190)
    Fade(500)
    SetChrPos(0x101, -500, 0, -4250, 90)
    SetChrPos(0xE, 500, 0, -4250, 180)
    OP_68(430, 1000, -4460, 0)
    OP_68(430, 1000, -4460, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    MoveCamera(40, 20, 0, 30000)
    OP_6E(500, 30000)
    SetCameraDistance(15000, 30000)
    OP_0D()
    Fade(250)
    Sound(812, 0, 50, 0)
    SetChrFlags(0xE, 0x2)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0xE,
        (
            "#10403F#5P#30WStigma─ That's the name\x01",
            "of this mark.\x02\x03",
            "#10408FA mark engraved on one's\x01",
            "soul... An abominable\x01",
            "source of power.\x02\x03",
            "#10400FIt's been about seven\x01",
            "years since it appeared\x01",
            "on me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005F#6PSeven years ago...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#10404F#5PThis doesn't have\x01",
            "anything to do with the\x01",
            "D∴G Cult. But...\x02\x03",
            "#10402FIf you're free, want to\x01",
            "hear about it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PYes... Please do, if you\x01",
            "don't mind.\x02\x03",
            "#00000FWhen I think about it, I\x01",
            "know almost nothing about\x01",
            "your past, Wazy.\x02\x03",
            "#00012FI understand your\x01",
            "personality and behaviors\x01",
            "pretty well, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#10404F#5PHaha... Very well.\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    StopSound(132, 2000, 30)
    StopSound(497, 2000, 15)
    SetCameraDistance(15000, 3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    WaitBGM()
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xE,
        (
            "#30W#3C─I was born in a certain\x01",
            "remote region of Zemuria.\x02\x03",
            "Contact with the outside\x01",
            "world was prohibited─ It was\x01",
            "a so-called hidden village.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayBGM("ed7568", 0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x640, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(800)
    SetMessageWindowPos(-1, 155, -1, -1)

    AnonymousTalk(
        0xE,
        (
            "#30W#3CIn that village, a Deity, who opposed the\x01",
            "Goddess, had been worshipped since ancient\x01",
            "times.\x02\x03",
            "When I was very young, I bore the role of\x01",
            "Shrine Medium─ one who can hear the voice of\x01",
            "god.\x02\x03",
            "It wasn't voluntary, of course. I'd been\x01",
            "chosen ever since I could remember.\x02\x03",
            "Honestly, ever since I learned this Deity's\x01",
            "true from was a mysterious and ancient magical\x01",
            "tool, I couldn't help but think it ridiculous.\x02\x03",
            "I always wanted to be free from that worthless\x01",
            "role.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xE,
        (
            "#30W#3C...Before long, strange things started\x01",
            "to occur in the village.\x02\x03",
            "The villagers, one after the next,\x01",
            "slipped into comas.\x02\x03",
            "From what I could see, the Deity raged,\x01",
            "and through septium veins, sucked up\x01",
            "their life force into itself...\x02\x03",
            "I advocated sealing it, but the village\x01",
            "elders did not allow it, and even spoke\x01",
            "of offering a sacrifice.\x02\x03",
            "But basically, the tool had such\x01",
            "terrible power, sealing it would have\x01",
            "been impossible...\x02\x03",
            "─That's when the Church knights came\x01",
            "from the outside.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(1000)
    SetMessageWindowPos(180, 160, -1, -1)

    AnonymousTalk(
        0xE,
        (
            "#30W#3C─When I made contact with them,\x01",
            "I learned the Deity was a kind\x01",
            "of ancient artifact...\x02\x03",
            "Knowing it was not an absolute\x01",
            "existence, I took drastic\x01",
            "action.\x02\x03",
            "I dropped the Deity, an tablet\x01",
            "of azure stone, from the top of\x01",
            "a cliff and tried to destroy it.\x02\x03",
            "Having freed the villagers from\x01",
            "the ancient curse, I wanted to\x01",
            "be free─ with my whole heart.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(1000)
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x4B0, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    Sleep(1000)
    SetMessageWindowPos(10, 150, -1, -1)

    AnonymousTalk(
        0xE,
        (
            "#30W#3CBut the Deity's resistance\x01",
            "was fierce, and it tried to\x01",
            "steal all my power.\x02\x03",
            "The knights' assistance\x01",
            "wasn't in time, and just\x01",
            "when my life force ran out─\x02\x03",
            "That "mark" appeared on my\x01",
            "chest.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x4, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x4, 0x3, 0xFFFFFFFF, 0x640, 0x0, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    Sleep(1000)
    FadeToDark(2500, 16777215, -1)
    OP_CB(0x4, 0x3, 0xFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    OP_0D()
    OP_68(-360, 2100, -3950, 0)
    MoveCamera(150, -49, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(5667730, 0)
    Sleep(1500)
    FadeToBright(1500, 16777215)
    OP_0D()
    Sleep(800)
    FadeToDark(0, 0, -1)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xE,
        (
            "#30W#3C─My Stigma, conversely,\x01",
            "stole all the Deity's\x01",
            "power...\x02\x03",
            "And the Deity turned into\x01",
            "an ordinary stone tablet,\x01",
            "and was smashed to pieces.\x02\x03",
            "Then I obtained my freedom─\x01",
            "And was happy to be\x01",
            "banished from the village.\x02\x03",
            "As the sinner who "killed"\x01",
            "the God that the villagers\x01",
            "had worshipped.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x1)
    OP_68(430, 1000, -4460, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15000, 0)
    SetCameraDistance(16000, 3000)
    Sound(132, 2, 35, 0)
    Sound(497, 2, 20, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(150)
    SetChrSubChip(0xE, 0x0)
    Sleep(150)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x2)
    OP_6F(0x79)
    MoveCamera(40, 20, 0, 50000)
    SetCameraDistance(16540, 50000)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00008F#6P#30W...All of that, huh...\x02\x03",
            "#00006F...............\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#10409F#5P#30WHaha... Pretty\x01",
            "ridiculous, no?\x02\x03",
            "#10400FI guess a kid who grew\x01",
            "up in a modern city'd\x01",
            "never believe it, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F#6PNo. Just by seeing your\x01",
            "power, I understand that\x01",
            "it is real.\x02\x03",
            "#00000FSomeone like Zeit, who\x01",
            "is basically a living\x01",
            "legend, is another.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#10402F#5PHaha, there's that too.\x02\x03",
            "#10404FAnd so, invited by the\x01",
            "knights, I went to the Holy\x01",
            "Nation of Arteria...\x02\x03",
            "And, as the possessor of one\x01",
            "of only twelve Stigma, I was\x01",
            "greeted as a Dominion.\x02\x03",
            "#10400FI've known Abbas ever since.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#6PIs that so...\x02\x03",
            "#00006F...But, after that, have\x01",
            "you ever been back to\x01",
            "your hometown?\x02\x03",
            "#00001FYou wouldn't have been\x01",
            "able to see your\x01",
            "family...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#10405F#5P#30WYeah─ Isn't that obvious?\x02\x03",
            "#10403FI smashed that village's\x01",
            "foundations to pieces.\x02\x03",
            "I just wanted to be free...\x01",
            "I didn't think about what\x01",
            "would come after.\x02\x03",
            "#10400FThat is my curse.\x02\x03",
            "#10404FI am hated by my family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F#6P#30W............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#10406F#5P#30WWell, after they heard my\x01",
            "story, the Church went in and\x01",
            "took care of the village.\x02\x03",
            "#10404FThe Deity's curse will\x01",
            "eventually fade into the\x01",
            "past.\x02\x03",
            "I want to go back someday,\x01",
            "after things have cooled\x01",
            "down.\x02\x03",
            "#10402FYou don't have to worry that\x01",
            "much about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F#6P#30WWazy...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1900, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)

    ChrTalk(
        0x101,
        (
            "#00008F#6PThen Wazy... You're\x01",
            "leaving Crossbell after\x01",
            "this case wraps up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#10400F#5PYeah. I have my mission\x01",
            "as a knight, after all.\x02\x03",
            "#10409FHaha, what? Are you\x01",
            "gonna be lonely?\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)

    ChrTalk(
        0x101,
        (
            "#00001F#6PYeah, isn't that\x01",
            "obvious?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1900, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xE, 0x101, 400)
    Sleep(150)

    ChrTalk(
        0xE,
        "#10405F#11PHuh?\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7514", 0)
    Fade(1000)
    SetChrPos(0x101, -920, 0, -3910, 90)
    SetChrPos(0xE, 500, 0, -3750, 270)
    OP_68(-360, 3200, -3950, 0)
    MoveCamera(136, -7, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(10000, 0)
    OP_68(-360, 2100, -3950, 3000)
    MoveCamera(135, 0, 0, 3000)
    OP_6E(800, 3000)
    Sleep(500)
    OP_6F(0x79)
    SetCameraDistance(9000, 30000)

    ChrTalk(
        0x101,
        (
            "#00003F#11P#30WWald became like that, but\x01",
            "I'm sure he'll be back to\x01",
            "normal.\x02\x03",
            "All of the Testaments will\x01",
            "remain in Crossbell.\x02\x03",
            "#00008FAnd this is just\x01",
            "speculation, but all of our\x01",
            "friends will be here too...\x02\x03",
            "#00000FSo please─ Please come\x01",
            "visit us anytime.\x02\x03",
            "#00009FBecause Crossbell is\x01",
            "already your second\x01",
            "hometown. Isn't that right?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    SetChrFlags(0xE, 0x2)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x0)
    Sleep(150)
    SetChrSubChip(0xE, 0x1)
    Sleep(150)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x2)
    Sleep(150)
    SetChrFlags(0xE, 0x2)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x0)
    Sleep(150)
    SetChrSubChip(0xE, 0x1)
    Sleep(150)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x2)
    Sleep(300)

    ChrTalk(
        0xE,
        "#10405F#5P#30W............\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrFlags(0xE, 0x2)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x2)
    OP_0D()

    def lambda_BDC5():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_BDC5)
    WaitChrThread(0xE, 2)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xE,
        "#10404F#2430V#5P#40W#12A...Hehe...\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    SetChrSubChip(0xE, 0x3)

    def lambda_BE1D():
        OP_A6(0xFE, 0x0, 0x1E, 0x320, 0x7D0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_BE1D)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0xE,
        "#10409F#2431V#50W#5P#4S#15AAhahahahaha!\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrFlags(0xE, 0x2)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x2)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00006F#11P#30WI know it's rotten.\x02\x03",
            "#00000FBut, I'm 100% serious,\x01",
            "you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#10411F#5P#40W...Haha, got it. Don't\x01",
            "go too out of control\x01",
            "without me, ok?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrFlags(0xE, 0x2)
    SetChrChipByIndex(0xE, 0x20)
    OP_A0(0xE, 1000, 0x7, 0x5)
    OP_0D()
    Sleep(400)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xE,
        (
            "#10402F#2929V#5P#40W─I'll be sure to visit\x01",
            "whenever I'm feeling\x01",
            "homesick.\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xB71)
    Sleep(150)
    OP_A0(0xE, 1000, 0x5, 0x7)
    Sleep(400)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0xE,
        (
            "#10404F#2930V#5P#40WIt's not a replacement for my hometown\x01",
            "to which I'm unable to return, but I\x01",
            "do have an attachment to you guys.\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xB72)
    OP_C9(0x1, 0x80000000)
    BlurSwitch(0x1770, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(-360, 2100, -3950, 8000)
    MoveCamera(128, 27, 0, 8000)
    OP_6E(800, 8000)
    SetCameraDistance(40590, 8000)
    Sleep(500)
    OP_A0(0xE, 1000, 0x7, 0x5)
    Sleep(2500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopSound(132, 2000, 30)
    StopSound(497, 2000, 15)
    StopBGM(0x1388)
    WaitBGM()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21, 2)), scpexpr(EXPR_END)), "loc_C0C3")
    OP_CC(0x1, 0xFF, 0x0)
    NewScene("b0100", 0, 0, 0)
    IdleLoop()
    Return()

    label("loc_C0C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21C, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C0D9")
    Jump("loc_C180")

    label("loc_C0D9")

    Sleep(500)
    Sound(517, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Lloyd and Wazy learned\x01",
            "Strike Heaven II.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and Wazy's Strike\x01",
            "Heaven has been\x01",
            "strengthened.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddCraft(0x0, 0x1A1)
    AddCraft(0x4, 0x1A1)

    label("loc_C180")

    OP_CC(0x1, 0xFF, 0x0)
    OP_E0(0x26, 0x0)
    OP_E0(0x80, 0x0)
    SetScenarioFlags(0x1AB, 5)
    OP_29(0xB1, 0x1, 0x5)
    Sleep(2000)
    SetScenarioFlags(0x23, 1)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_9BEA end

    def Function_17_C1A3(): pass

    label("Function_17_C1A3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x8, 0x40)
    LoadChrToIndex("chr/ch03200.itc", 0x1E)
    LoadChrToIndex("apl/ch51809.itc", 0x1F)
    LoadChrToIndex("apl/ch51810.itc", 0x20)
    SoundLoad(3265)
    SoundLoad(3266)
    SoundLoad(3267)
    SoundLoad(3268)
    SoundLoad(3269)
    SoundLoad(3270)
    SoundLoad(2634)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10701.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis321.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis322.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis323.itp")
    CreatePortrait(4, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis324.itp")
    EndChrThread(0x8, 0x0)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x1)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    OP_F0(0x0, 0x1)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x1, 0x1000)
    OP_71(0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x101, -250, 120, 2750, 180)
    SetChrPos(0x8, 500, 0, -3750, 180)
    OP_68(500, 5500, -3750, 0)
    MoveCamera(125, -15, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(8000, 0)
    PlayBGM("ed7560", 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(500, 1000, -3750, 8000)
    MoveCamera(115, 15, 0, 8000)
    OP_6E(800, 8000)
    SetCameraDistance(9500, 8000)
    OP_6F(0x79)
    Sound(100, 0, 100, 0)
    Sleep(800)

    ChrTalk(
        0x101,
        (
            "#00002F#6P#30W#N...What a beautiful full\x01",
            "moon.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1850, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x2)
    OP_0D()

    def lambda_C3E5():

        label("loc_C3E5")

        TurnDirection(0xFE, 0x101, 400)
        Yield()
        Jump("loc_C3E5")

    QueueWorkItem2(0x8, 2, lambda_C3E5)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    AnonymousTalk(
        0x8,
        "#3265V#11P#40WLloyd...\x02",
    )

    CloseMessageWindow()
    OP_24(0xCC1)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    BeginChrThread(0xF, 1, 0, 8)
    OP_68(0, 1000, -4200, 4500)
    MoveCamera(130, 20, 0, 4500)
    OP_6E(800, 4500)
    SetCameraDistance(10000, 4500)
    Sound(100, 0, 100, 0)

    def lambda_C4D3():
        OP_95(0xFE, -500, 0, -3750, 1600, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C4D3)
    WaitChrThread(0x101, 1)
    EndChrThread(0x8, 0x2)
    OP_6F(0x79)
    SetCameraDistance(9500, 30000)
    OP_63(0x101, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00004F#6P#30WSomehow, I always feel the\x01",
            "moon is beautiful when I'm\x01",
            "talking with you.\x02\x03",
            "#00002FMaybe there's a reason you\x01",
            "play the role of Moon\x01",
            "Princess?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x8,
        "#10709F#2634V#5P#30WHaha...\x02",
    )

    CloseMessageWindow()
    OP_24(0xA4A)
    OP_57(0x0)
    OP_5A()
    OP_93(0x8, 0xB4, 0x190)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#10704F#3266V#40W#5PThe moon, a light in the\x01",
            "shadows...\x02\x03",
            "#3267VI think it might be because\x01",
            "my very existence is like\x01",
            "the moon itself.\x02\x03",
            "#10708F#3268VNormally, I wouldn't have\x01",
            "ever showed myself anywhere\x01",
            "the sun can reach...\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xCC4)
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x80000000)
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00003F#12P#30WBut, here in Crossbell,\x01",
            "you were able to grasp\x01",
            "the light...\x02\x03",
            "#00001FThat's true, isn't it?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0x8, 0x10E, 0x190)
    Sleep(300)
    Fade(250)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x1F)
    OP_A1(0x8, 0x3E8, 0x5, 0x2, 0x25, 0x26, 0x25, 0x2)
    OP_0D()

    ChrTalk(
        0x8,
        (
            "#10704F#5P#30WYes, I can't deny that\x01",
            "anymore.\x02\x03",
            "#10708FBut I... The flow that\x01",
            "created my existence is\x01",
            "without limit.\x02\x03",
            "#10711FThe teaching of the\x01",
            "secret arts of Yin...\x02\x03",
            "#10703FThe quiet path I\x01",
            "inherited from my\x01",
            "father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F#12P#30WYou said that before\x01",
            "too...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)

    ChrTalk(
        0x101,
        (
            "#00003F#12P#30WIf you don't mind my\x01",
            "asking, can I ask you\x01",
            "about it?\x02\x03",
            "#00008FAbout the you before you\x01",
            "came to Crossbell.\x02\x03",
            "#00001FThe Rixia Mao I don't\x01",
            "know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#10704F#5P#30W...Right.\x02\x03",
            "#10710FSomehow, I feel like I'd\x01",
            "end up telling you\x01",
            "sooner or later.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0x1770)
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x2)
    OP_0D()
    OP_93(0x8, 0xB4, 0x12C)
    Fade(250)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x1)
    Sleep(800)
    OP_63(0x8, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    Sleep(500)

    ChrTalk(
        0x8,
        (
            "#10708F#5P#30W─As far back as I can\x01",
            "remember, I was with my\x01",
            "father.\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(9000, 2500)
    StopSound(132, 2000, 30)
    StopSound(497, 2000, 15)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    WaitBGM()
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x8,
        (
            "#30W#3C─I have no memories of my mother.\x02\x03",
            "I believe my father kept her away so\x01",
            "that I would inherit the path of\x01",
            "Yin.\x02\x03",
            "But to me, that is normal...\x02\x03",
            "Harsh training, dark tools and\x01",
            "talisman techniques I mastered\x01",
            "dispassionately.\x02\x03",
            "I went from place to place, attended\x01",
            "Sunday School, and thereby learned\x01",
            "techniques for contacting people.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7568", 0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x640, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(800)
    SetMessageWindowPos(260, 160, -1, -1)

    AnonymousTalk(
        0x8,
        (
            "#30W#3CFather was neither kind nor\x01",
            "strict. He was only there to\x01",
            "teach.\x02\x03",
            "That is because the things Yin\x01",
            "must inherit are vast.\x02\x03",
            "The memories of generations of\x01",
            "past Yin...\x02\x03",
            "To kill─ No matter the\x01",
            "situation, no matter the means\x01",
            "and no matter the target...\x02\x03",
            "To keep the Yin the same over\x01",
            "generations, it was necessary\x01",
            "to inherit all of it.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x8,
        (
            "#30W#3CAnd when I had inherited all of\x01",
            "it... I became Yin itself.\x02\x03",
            "Though I say that, one does not\x01",
            "become Yin while their father is\x01",
            "alive.\x02\x03",
            "Yin is but a single person... That\x01",
            "will never change.\x02\x03",
            "For a time, quiet days of waiting\x01",
            "for my father to return continued.\x02\x03",
            "And when he returned, he explained\x01",
            "Yin's work to me so that I could\x01",
            "become Yin at any time...\x02\x03",
            "I knew there was something\x01",
            "sinister about it but by that\x01",
            "point it was all that I had.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(800)
    SetMessageWindowPos(20, 160, -1, -1)

    AnonymousTalk(
        0x8,
        (
            "#30W#3C─What shattered that world was when my\x01",
            "father fell to an incurable illness.\x02\x03",
            "My father was particularly strong even\x01",
            "among the many Yin... But disease was\x01",
            "a foe from which he could not run.\x02\x03",
            "He did not fight it, and refused life-\x01",
            "extending surgery...\x02\x03",
            "One day, he called and ordered me.\x02\x03",
            "To kill himself, and become Yin.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(800)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0x8,
        (
            "#30W#3C─I could not do it.\x02\x03",
            "I had never gone against my\x01",
            "father's word before, but\x01",
            "for some reason I couldn't.\x02\x03",
            "...I became scared for the\x01",
            "first time.\x02\x03",
            "I wondered if my father\x01",
            "thought the Yin he had\x01",
            "constructed was a failure.\x02\x03",
            "I wondered if had\x01",
            "disappointed my father on\x01",
            "his deathbed.\x02\x03",
            "I was in agony. My father\x01",
            "cracked a wry smile and\x01",
            "said:\x02\x03",
            ""That is also you."\x02\x03",
            ""You should decide how your\x01",
            "Yin will be."\x02\x03",
            "...And one month later, my\x01",
            "father left this world.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x4B0, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    Sleep(800)
    SetMessageWindowPos(260, 160, -1, -1)

    AnonymousTalk(
        0x8,
        (
            "#30W#3CThen I became Yin.\x02\x03",
            "I inherited my father's connections,\x01",
            "used black clothes and my skills to\x01",
            "manipulate my figure...\x02\x03",
            "Though my skills were not as great\x01",
            "as my father's, I resumed work\x01",
            "immediately.\x02\x03",
            ""You should decide how your Yin will\x01",
            "be."\x02\x03",
            "Without understanding his meaning, I\x01",
            "dispassionately went with the\x01",
            "flow...\x02\x03",
            "─And two years ago, I accepted a\x01",
            "long-term contract with Heiyue.\x02\x03",
            "To help unseat the hegemony in\x01",
            "Crossbell, a trade city on the\x01",
            "western edge of Calvard.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    Sleep(1000)
    OP_CB(0x4, 0x3, 0xFFFFFFFF, 0x4B0, 0x0, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    Sleep(1000)
    SetMessageWindowPos(250, 160, -1, -1)

    AnonymousTalk(
        0x8,
        (
            "#30W#3CI arrived in Crossbell and prepared for battle. As I\x01",
            "was getting the lay of the land in the city, I\x01",
            "entered a certain theater in Entertainment District.\x02\x03",
            "Just then, a public training session was being\x01",
            "held...\x02\x03",
            "...From then on was as you already know, Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x4, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    Sound(132, 2, 35, 0)
    Sound(497, 2, 20, 0)
    FadeToBright(2000, 0)
    OP_68(-360, 3200, -3950, 0)
    MoveCamera(136, -7, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(10000, 0)
    OP_68(-360, 2100, -3950, 3000)
    MoveCamera(135, 0, 0, 3000)
    OP_6E(800, 3000)
    OP_6F(0x79)
    SetCameraDistance(9000, 40000)
    Sleep(300)

    ChrTalk(
        0x101,
        (
            "#00006F#11P#30WI see...\x02\x03",
            "#00000FSo that's when you\x01",
            "caught Ilya's eye?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#10702F#5P#30WHaha. At first, I refused to\x01",
            "join without giving a reason.\x02\x03",
            "#10704FBut Ilya was extremely\x01",
            "overbearing...\x02\x03",
            "Finally, I was beaten down and\x01",
            "decided to join.\x02\x03",
            "I was confident in my physical\x01",
            "strength and disguise, so I\x01",
            "thought it would be good cover.\x02\x03",
            "#10710F...But the training was harder\x01",
            "than I expected, and it was\x01",
            "hard to be both Rixia and Yin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012F#11P#30WHaha...\x02\x03",
            "#00004FThank you, Rixia.\x02\x03",
            "#00000FI'm happy you told me\x01",
            "all of this.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x2)
    OP_93(0x8, 0x10E, 0x190)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#10704F#5P#30WHaha. I don't think it\x01",
            "was that interesting a\x01",
            "story...\x02\x03",
            "#10703FBut─ This is the "path"\x01",
            "I inherited from my\x01",
            "father and ancestors.\x02\x03",
            "#10708FEven if I have obtained\x01",
            "the light called Arc-en-\x01",
            "Ciel...\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x1F)
    OP_A0(0x8, 1000, 0x2, 0x5)
    OP_0D()
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#10704F#5P#30WThat "path" is something\x01",
            "I don't think I can ever\x01",
            "completely abandon.\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x1388)

    ChrTalk(
        0x101,
        (
            "#00003F#11P#30WIs that so...\x02\x03",
            "#00008F............\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1850, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1500)
    Fade(1000)
    SetChrSubChip(0x8, 0x6)
    SetChrPos(0x101, -1000, 0, -4250, 90)
    SetChrPos(0x8, 0, 0, -4250, 270)
    OP_68(-300, 1000, -4250, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17500, 0)
    OP_68(-300, 1000, -4250, 50000)
    MoveCamera(45, 15, 0, 50000)
    OP_6E(500, 50000)
    SetCameraDistance(15500, 50000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7575", 0)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00003F#6P#30W"You should decide how\x01",
            "your Yin will be."\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x8, 0x3E8, 0x5, 0x6, 0x29, 0x2A, 0x29, 0x6)

    ChrTalk(
        0x8,
        "#10712F#11P#30W...Huh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6P#30W...Yin inherits\x01",
            "everything.\x02\x03",
            "Now that you have\x01",
            "discovered the light of\x01",
            "Arc-en-Ciel...\x02\x03",
            "#00002FIs it not also time for\x01",
            "Yin to take up the side\x01",
            "of light?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#10717F#11P#30WW-Well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F#6P#30WIf things change with the\x01",
            "generations, the way things\x01",
            "should be change as well...\x02\x03",
            "#00003FNo, they have to change.\x02\x03",
            "#00008FAnd people inherit history,\x01",
            "and move forward...\x02\x03",
            "#00001FI wonder if that's the\x01",
            "meaning in what your father\x01",
            "said.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#10708F#11P#30W............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6P#30WAs a police officer, I can't\x01",
            "recommend criminal acts,\x01",
            "but...\x02\x03",
            "Even so, I think you should\x01",
            "aim to be your own Yin.\x02\x03",
            "#00000FIn a way, it would be\x01",
            "completely cutting ties with\x01",
            "all the Yin up until now.\x02\x03",
            "#00002FIf you did that... I think\x01",
            "your father wouldn't care,\x01",
            "probably?\x02\x03",
            "#00009F"─That is also you", he\x01",
            "would say, and smile.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#10717F#11P#40W#2S...Ah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6P#30W...What a good father.\x02\x03",
            "#00008FYours was a bit different from\x01",
            "normal families. But your\x01",
            "father loved you, all the same.\x02\x03",
            "#00002FThat's what I think anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#10718F#11P#50W...Father...\x02",
    )

    CloseMessageWindow()
    OP_68(-100, 1000, -4250, 1200)
    SetChrFlags(0x8, 0x20)

    def lambda_DF97():
        OP_A0(0xFE, 1000, 0x6, 0x9)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_DF97)
    OP_96(0x8, 0x96, 0x0, 0xFFFFEF66, 0x1F4, 0x0)
    Sound(812, 0, 60, 0)
    ClearChrFlags(0x8, 0x20)
    OP_A0(0x8, 1000, 0x18, 0x1A)
    OP_A0(0x8, 1000, 0x1A, 0x1C)
    OP_A0(0x8, 1000, 0x1A, 0x1C)
    OP_A0(0x8, 1000, 0x1A, 0x1C)
    OP_A1(0x8, 0x3E8, 0x6, 0x1A, 0x1E, 0x1F, 0x20, 0x21, 0x22)
    OP_A0(0x8, 1000, 0x18, 0x1A)
    OP_63(0x8, 0x0, 1850, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sound(812, 0, 60, 0)
    OP_A0(0x8, 1000, 0xA, 0xC)
    Sleep(300)

    ChrTalk(
        0x8,
        (
            "#10719F#11P#50WWhy...\x02\x03",
            "Even when my father\x01",
            "died...\x02\x03",
            "#10720FI didn't shed... a\x01",
            "single tear... like\x01",
            "this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F#6P#30WYou might have changed\x01",
            "after spending time with\x01",
            "Ilya and the others...\x02\x03",
            "#00008FI don't know what path\x01",
            "you'll follow going\x01",
            "forward, but...\x02\x03",
            "#00000FIf possible, I'd like to\x01",
            "watch over you in place\x01",
            "of your father.\x02\x03",
            "#00002FTo see how you'll change\x01",
            "now that you've found\x01",
            "your light.\x02",
        )
    )

    CloseMessageWindow()
    OP_A0(0x8, 1000, 0xC, 0xF)
    Sleep(300)

    ChrTalk(
        0x8,
        "#10718F#11P#50W...Lloyd...\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 3, 0, 18)
    Sleep(1000)
    OP_68(100, 1000, -4250, 1200)
    SetCameraDistance(15000, 1200)
    OP_9A(0x101, 0x8, 0x1F4, 0x258, 0x0)
    Sleep(300)
    Fade(250)
    Sound(898, 0, 100, 0)
    EndChrThread(0x8, 0x3)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x20)

    def lambda_E22B():
        OP_A0(0xFE, 1000, 0x14, 0x16)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_E22B)

    def lambda_E238():
        OP_A0(0xFE, 1000, 0x5, 0x7)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_E238)
    WaitChrThread(0x8, 3)
    WaitChrThread(0x101, 3)
    OP_0D()
    MoveCamera(44, 23, 0, 15000)
    SetCameraDistance(70000, 15000)
    OP_C9(0x0, 0x80000000)

    ChrTalk(
        0x8,
        "#10720F#11P#3269V#70W#20A...Ooh... Ahhh...\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    ChrTalk(
        0x8,
        "#10713F#11P#3270V#90W#30A#4S...Waaaaaah!\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopSound(132, 1000, 30)
    StopSound(497, 1000, 15)
    StopBGM(0x1770)
    WaitBGM()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21, 2)), scpexpr(EXPR_END)), "loc_E31B")
    OP_CC(0x1, 0xFF, 0x0)
    NewScene("b0100", 0, 0, 0)
    IdleLoop()
    Return()

    label("loc_E31B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E32D")
    Jump("loc_E3E6")

    label("loc_E32D")

    Sleep(500)
    Sound(517, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Lloyd and Rixia learned\x01",
            "True Double Dragon\x01",
            "Strike.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd and Rixia's Double\x01",
            "Dragon Strike has been\x01",
            "strengthened.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddCraft(0x5, 0x1A9)
    AddCraft(0x0, 0x1A9)

    label("loc_E3E6")

    OP_CC(0x1, 0xFF, 0x0)
    OP_E0(0x27, 0x0)
    OP_E0(0x80, 0x0)
    SetScenarioFlags(0x1AB, 6)
    OP_29(0xB1, 0x1, 0x6)
    Sleep(2000)
    SetScenarioFlags(0x23, 1)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_17_C1A3 end

    def Function_18_E409(): pass

    label("Function_18_E409")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E423")
    OP_A0(0xFE, 1000, 0x10, 0x12)
    Sleep(300)
    Jump("Function_18_E409")

    label("loc_E423")

    Return()

    # Function_18_E409 end

    SaveToFile()

Try(main)
