from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e3020_1.bin",                # FileName
        "e3020",                    # MapName
        "e3020",                    # Location
        0x0000,                     # MapIndex
        "ed7570",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [312, 2237, 3097, 7666, 8355, 9536, 10208, 13862, 15091, 0, 15628, 0, 16625, 17468, 18296, 21568, 0, 22497, 0, 104, 90, 0, 0],
    )

    BuildStringList((
        "e3020_1",                # 0
    ))

    ChipFrameInfo(312, 0)                                        # 0

    ScpFunction((
        "Function_0_138",          # 00, 0
        "Function_1_8BD",          # 01, 1
        "Function_2_C19",          # 02, 2
        "Function_3_1DF2",         # 03, 3
        "Function_4_20A3",         # 04, 4
        "Function_5_2540",         # 05, 5
        "Function_6_27E0",         # 06, 6
        "Function_7_3626",         # 07, 7
        "Function_8_3AF3",         # 08, 8
        "Function_9_3D0C",         # 09, 9
        "Function_10_40F1",        # 0A, 10
        "Function_11_443C",        # 0B, 11
        "Function_12_4778",        # 0C, 12
        "Function_13_5440",        # 0D, 13
        "Function_14_57E1",        # 0E, 14
        "Function_15_5A68",        # 0F, 15
        "Function_16_75A4",        # 10, 16
        "Function_17_7796",        # 11, 17
        "Function_18_7C45",        # 12, 18
        "Function_19_80B6",        # 13, 19
        "Function_20_8F68",        # 14, 20
        "Function_21_9303",        # 15, 21
        "Function_22_9651",        # 16, 22
        "Function_23_A687",        # 17, 23
        "Function_24_A9CA",        # 18, 24
        "Function_25_B198",        # 19, 25
        "Function_26_B4D5",        # 1A, 26
        "Function_27_D3EF",        # 1B, 27
        "Function_28_D6FC",        # 1C, 28
        "Function_29_D814",        # 1D, 29
        "Function_30_DADF",        # 1E, 30
        "Function_31_DE43",        # 1F, 31
        "Function_32_F87A",        # 20, 32
        "Function_33_FD7C",        # 21, 33
        "Function_34_10057",       # 22, 34
        "Function_35_10A39",       # 23, 35
        "Function_36_10C9D",       # 24, 36
        "Function_37_10EBF",       # 25, 37
        "Function_38_11435",       # 26, 38
        "Function_39_11BB1",       # 27, 39
        "Function_40_1209D",       # 28, 40
        "Function_41_1235D",       # 29, 41
        "Function_42_1275E",       # 2A, 42
        "Function_43_12762",       # 2B, 43
        "Function_44_13B12",       # 2C, 44
        "Function_45_13E85",       # 2D, 45
        "Function_46_13E89",       # 2E, 46
        "Function_47_14FBC",       # 2F, 47
        "Function_48_151C6",       # 30, 48
        "Function_49_15315",       # 31, 49
        "Function_50_1594B",       # 32, 50
        "Function_51_15A86",       # 33, 51
        "Function_52_1604A",       # 34, 52
        "Function_53_16A09",       # 35, 53
        "Function_54_173B9",       # 36, 54
        "Function_55_176FB",       # 37, 55
        "Function_56_178C9",       # 38, 56
    ))


    def Function_0_138(): pass

    label("Function_0_138")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_3A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_156")
    Call(1, 1)
    Jump("loc_3A0")

    label("loc_156")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E2")

    ChrTalk(
        0x11,
        (
            "#00101FBell is most likely participating\x01",
            "in this plan for her own reasons.\x02\x03",
            "#00108FA lot of things about Bell amaze\x01",
            "me, her personality included. Maybe\x01",
            "that's what's fascinates me...\x02\x03",
            "#00103F...But no matter the reason, a plan\x01",
            "that sacrifices someone can't be\x01",
            "forgiven.\x02\x03",
            "#00100FI've been friends with Bell since\x01",
            "we were little... I'll definitely\x01",
            "make her correct her ways.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3A0")

    label("loc_2E2")


    ChrTalk(
        0x11,
        (
            "#00103FNo matter the reason, a plan that\x01",
            "sacrifices someone can never be\x01",
            "allowed.\x02\x03",
            "#00100FI've been friends with Bell since\x01",
            "we were little... I'll definitely\x01",
            "make her correct her ways.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A0")

    Jump("loc_8B9")

    label("loc_3A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_4F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47A")

    ChrTalk(
        0x11,
        (
            "#00103FAs a Crois, Bell is\x01",
            "likely deeply involved\x01",
            "with this plan.\x02\x03",
            "#00108FI'm sure she and Lawyer\x01",
            "Ian have the truth we\x01",
            "are seeking...\x02\x03",
            "#00101F...Let's go, Lloyd. To\x01",
            "take back KeA!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4F2")

    label("loc_47A")


    ChrTalk(
        0x11,
        (
            "#00108FI'm sure Bell and Lawyer\x01",
            "Ian have the truth we\x01",
            "are seeking...\x02\x03",
            "#00101F...Let's go, Lloyd. To\x01",
            "take back KeA!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F2")

    Jump("loc_8B9")

    label("loc_4F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62B")

    ChrTalk(
        0x11,
        (
            "#00108FBell... I wonder if she\x01",
            "planned to discard "uncle"\x01",
            "from the start.\x02\x03",
            "And, to think Lawyer Ian was\x01",
            "the mastermind...\x02\x03",
            "#00106F...It's no good, I'm\x01",
            "confusing myself... I've got\x01",
            "to put my thoughts in order.\x02\x03",
            "#00100FAnyway, we have no choice\x01",
            "but to go. To that Azure\x01",
            "Tree...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6B4")

    label("loc_62B")


    ChrTalk(
        0x11,
        (
            "#00108F...Too much has happened\x01",
            "and I've gotten\x01",
            "confused, but...\x02\x03",
            "#00100FAnyway, we have no\x01",
            "choice but to go. To\x01",
            "that Azure Tree...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B4")

    Jump("loc_8B9")

    label("loc_6B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_8B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FE")

    ChrTalk(
        0x11,
        (
            "#00103FIt looks my grandfather's independence\x01",
            "invalidity declaration is having\x01",
            "significant effects everywhere.\x02\x03",
            "#00108FNow that the State Guard has\x01",
            "withdrawn, unrest might appear in\x01",
            "various places...\x02\x03",
            "#00100FIt might be a good idea to visit\x01",
            "various places in between stopping the\x01",
            "Great Bells.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_8B9")

    label("loc_7FE")


    ChrTalk(
        0x11,
        (
            "#00103FThe independence invalidity\x01",
            "declaration is having\x01",
            "significant effects everywhere.\x02\x03",
            "#00100FIt might be a good idea to\x01",
            "visit various places in between\x01",
            "stopping the Great Bells.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B9")

    TalkEnd(0xFE)
    Return()

    # Function_0_138 end

    def Function_1_8BD(): pass

    label("Function_1_8BD")


    ChrTalk(
        0x11,
        (
            "#00100FFinally... The path to\x01",
            "the place KeA is waiting\x01",
            "for us is open.\x02\x03",
            "#00108FAnd Lawyer Ian, the\x01",
            "mastermind, and Bell are\x01",
            "there too...\x02\x03",
            "#00103F...............\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FElie...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#00103FBell is most likely participating\x01",
            "in this plan for her own reasons.\x02\x03",
            "#00108FA lot of things about Bell amaze\x01",
            "me, her personality included. Maybe\x01",
            "that's what's fascinates me...\x02\x03",
            "#00101F...But no matter the reason, a plan\x01",
            "that sacrifices someone can't be\x01",
            "forgiven.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...Yeah, that's right.\x02\x03",
            "#00001FThough we don't know what Lawyer Ian and\x01",
            "Mariabell's plan is, we can't let them\x01",
            "use KeA any more than they already have.\x02\x03",
            "#00003FElie, it might be hard fighting against\x01",
            "her... But please, lend me your aid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x11,
        (
            "#00103F...Yes, I'm prepared for that.\x02\x03",
            "#00101FI've been friends with Bell since\x01",
            "we were little... I'll definitely\x01",
            "make her correct her ways.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D6, 1)
    Return()

    # Function_1_8BD end

    def Function_2_C19(): pass

    label("Function_2_C19")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C3D")
    Call(1, 56)
    Jump("loc_E0E")

    label("loc_C3D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C5D")
    RunExpression(0xA, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TurnDirection(0xB, 0x101, 0)

    label("loc_C5D")


    ChrTalk(
        0xB,
        (
            "#00200FLloyd, if you like,\x01",
            "please accept this.\x02",
        )
    )

    CloseMessageWindow()
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "[Tio's Account]\x07\x00\x01",
            "obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x28, 1)
    OP_E4(0x3)

    ChrTalk(
        0x101,
        "#00005FA "Pom!" account?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#00204FPrecisely because of the\x01",
            "current situation, leisure\x01",
            "is important, I think.\x02\x03",
            "#00202FI'll be your opponent\x01",
            "anytime, so please feel\x01",
            "free to challenge me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, got it.\x02\x03",
            "#00004F(Tio is a formidable\x01",
            "opponent... But I've got\x01",
            "to try my best somehow.)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E0E")
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E0E")

    Jump("loc_1DEE")

    label("loc_E13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_F8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E2E")
    Call(1, 5)
    Jump("loc_F89")

    label("loc_E2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F15")

    ChrTalk(
        0xB,
        (
            "#00208FLawyer Ian is an opponent not\x01",
            "even Guy was able to reach...\x01",
            "We have to think about that.\x02\x03",
            "#00203FIt's possible that Ian will\x01",
            "be the ultimate test of our\x01",
            "resolve...\x02\x03",
            "#00202F...Let's do our best, Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_F89")

    label("loc_F15")


    ChrTalk(
        0xB,
        (
            "#00203FIt's possible that Ian\x01",
            "will be the ultimate\x01",
            "test of our resolve...\x02\x03",
            "#00202F...Let's do our best,\x01",
            "Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F89")

    Jump("loc_1DEE")

    label("loc_F8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_11A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10E1")

    ChrTalk(
        0xB,
        (
            "#00200FStrange dimensions have formed within the\x01",
            "Azure Tree.\x02\x03",
            "#00203FFar exceeding the "fields" created by the\x01",
            "resonance of the great bells in the\x01",
            "Temple and Tower, a world that completely\x01",
            "disregards the laws of physics...\x02\x03",
            "#00201FOur common sense won't be any good\x01",
            "here... Let's be cautious as we proceed.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_11A1")

    label("loc_10E1")


    ChrTalk(
        0xB,
        (
            "#00203FStrange dimensions that completely\x01",
            "disregard the laws of physics have\x01",
            "formed in the Azure Tree.\x02\x03",
            "#00201FOur common sense won't be any good\x01",
            "here... Let's be cautious as we\x01",
            "proceed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11A1")

    Jump("loc_1DEE")

    label("loc_11A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_132D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_128F")

    ChrTalk(
        0xB,
        (
            "#00200FIndeed, I sense KeA-like\x01",
            "waves from that Huge Tree.\x02\x03",
            "Mariabell said that Huge\x01",
            "Tree is KeA herself, but...\x02\x03",
            "#00206F...I don't understand. What\x01",
            "is she planning, making\x01",
            "something like that appear.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1328")

    label("loc_128F")


    ChrTalk(
        0xB,
        (
            "#00200FMariabell said that Huge\x01",
            "Tree is KeA herself, but...\x02\x03",
            "#00206F...I don't understand. What\x01",
            "is she planning, making\x01",
            "something like that appear.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1328")

    Jump("loc_1DEE")

    label("loc_132D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1517")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_145A")

    ChrTalk(
        0xB,
        (
            "#00200FBecause we've found this new\x01",
            "Gap, I've handed my all my\x01",
            "shipboard duties to Jona.\x02\x03",
            "#00203FOur opponent, Ouroboros...\x01",
            "Whatever they're planning, it's\x01",
            "not something to be understood.\x02\x03",
            "#00200FI have to make sure I'm always\x01",
            "ready to face them, orbal staff\x01",
            "included.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1512")

    label("loc_145A")


    ChrTalk(
        0xB,
        (
            "#00203FOur opponent, Ouroboros...\x01",
            "Whatever they're planning, it's\x01",
            "not something to be understood.\x02\x03",
            "#00200FI have to make sure I'm always\x01",
            "ready to face them, orbal staff\x01",
            "included.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1512")

    Jump("loc_1DEE")

    label("loc_1517")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_1692")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1532")
    Call(1, 4)
    Jump("loc_168D")

    label("loc_1532")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15EA")

    ChrTalk(
        0xB,
        (
            "#00204FIt was only for a short time,\x01",
            "but... I'm glad Zeit was able\x01",
            "to travel with you guys.\x02\x03",
            "#00202FFrom now on, we have to work\x01",
            "hard to repay him for his\x01",
            "help.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_168D")

    label("loc_15EA")


    ChrTalk(
        0xB,
        (
            "#00204FNow then, I have to work on\x01",
            "the final hacking\x01",
            "preparations.\x02\x03",
            "#00211FAlthough I believe in Jona's\x01",
            "ability, I can't deny that\x01",
            "his endgame is a bit weak.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_168D")

    Jump("loc_1DEE")

    label("loc_1692")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_1873")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17AD")

    ChrTalk(
        0xB,
        (
            "#00200FOnce save Elie, the entire\x01",
            "Support Section will be back.\x02\x03",
            "#00203FBecause Chairman MacDowell is\x01",
            "confined there, security will\x01",
            "be pretty tight...\x02\x03",
            "#00202FZeit volunteered to participate\x01",
            "in this dangerous battle, so\x01",
            "I'm sure it will be a success.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_186E")

    label("loc_17AD")


    ChrTalk(
        0xB,
        (
            "#00203FBecause Elie and Chairman\x01",
            "MacDowell are jailed, security\x01",
            "must be pretty tight...\x02\x03",
            "#00200FZeit volunteered to participate\x01",
            "in this dangerous battle, so\x01",
            "I'm sure it will be a success.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_186E")

    Jump("loc_1DEE")

    label("loc_1873")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_1A22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_196D")

    ChrTalk(
        0xB,
        (
            "#00200FWe can go to Bellguard Gate\x01",
            "and the police academy from\x01",
            "West Crossbell Highway...\x02\x03",
            "#00206F*sigh*. A less than ideal\x01",
            "place in which to find a\x01",
            "Gap, huh.\x02\x03",
            "#00200F...But right now, all we\x01",
            "can do is go where we can.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1A1D")

    label("loc_196D")


    ChrTalk(
        0xB,
        (
            "#00206FWe can go to Bellguard Gate\x01",
            "and the police academy from\x01",
            "West Crossbell Highway...\x02\x03",
            "#00200FThe place isn't ideal,\x01",
            "but... For now anyway,\x01",
            "let's just go where we can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A1D")

    Jump("loc_1DEE")

    label("loc_1A22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_1AC6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A3D")
    Call(1, 3)
    Jump("loc_1AC1")

    label("loc_1A3D")


    ChrTalk(
        0xB,
        (
            "#00208FZeit's subordinates... I\x01",
            "wonder what they're\x01",
            "doing now.\x02\x03",
            "#00203FIt's reassuring to be\x01",
            "able to receive their\x01",
            "aid, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AC1")

    Jump("loc_1DEE")

    label("loc_1AC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_1DEE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AE1")
    Call(1, 56)
    Jump("loc_1DEE")

    label("loc_1AE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D65")
    EndChrThread(0x8, 0x0)

    ChrTalk(
        0xB,
        (
            "#00203FCooperation between the foundation\x01",
            "and the church... I heard the rumors,\x01",
            "but I finally obtained proof.\x02\x03",
            "#00202FAnyway, it looks like I'll be able to\x01",
            "use the terminals without problems.\x02\x03",
            "I was thinking of using them with my\x01",
            "Aeon System to widen the search for\x01",
            "Gaps.\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x8, 0)
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1C95")
    Jump("loc_1CDF")

    label("loc_1C95")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1CB5")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1CDF")

    label("loc_1CB5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1CD5")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1CDF")

    label("loc_1CD5")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1CDF")

    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)

    ChrTalk(
        0xB,
        (
            "#00200FAbbas, thank you for\x01",
            "showing me how to use\x01",
            "them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        "#12100FSure.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x0)
    BeginChrThread(0x8, 0, 0, 0)
    SetScenarioFlags(0x0, 4)
    Jump("loc_1DEE")

    label("loc_1D65")


    ChrTalk(
        0xB,
        (
            "#00203FUsing my Aeon System, it\x01",
            "seems like we'll be able to\x01",
            "widen the search for Gaps.\x02\x03",
            "#00200FLeave this place to Fran\x01",
            "and myself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DEE")

    TalkEnd(0xFE)
    Return()

    # Function_2_C19 end

    def Function_3_1DF2(): pass

    label("Function_3_1DF2")

    OP_4B(0xB, 0xFF)
    OP_4B(0x13, 0xFF)

    ChrTalk(
        0xB,
        (
            "#00205FThat's right... Zeit's\x01",
            "subordinates are gathering\x01",
            "on the mountain path.\x02\x03",
            "#00200FAre they "Divine Wolves"\x01",
            "the same as yourself,\x01",
            "Zeit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01203F#3CNo, they're just normal wolves.\x02\x03",
            "#01200FIt's just, I have been leading them ever\x01",
            "since back when Ursula was alive, and\x01",
            "I've come to think of them as my family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#00203FA divine wolf's family... No wonder you\x01",
            "were able to overpower the military dogs\x01",
            "so easily in that Revache incident.\x02\x03",
            "#00208FI hope they're safe...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01203F#3CRegarding that, I gave them detailed\x01",
            "instructions before leaving, so\x01",
            "there's no need to worry.\x02\x03",
            "#01200FRight now, they're watching over the\x01",
            "situation from somewhere.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    OP_4C(0xB, 0xFF)
    OP_4C(0x13, 0xFF)
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x1, 1)
    Return()

    # Function_3_1DF2 end

    def Function_4_20A3(): pass

    label("Function_4_20A3")

    OP_4B(0xB, 0xFF)
    OP_4B(0x13, 0xFF)

    ChrTalk(
        0xB,
        (
            "#00203F...Alright, there we go.\x01",
            "With this your treatment\x01",
            "is complete.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01200F#3CRight. I'm in your debt,\x01",
            "Tio.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x13, 500)

    ChrTalk(
        0x101,
        (
            "#00005FZeit... Is that a wound\x01",
            "from the battle earlier?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01203F#3CYes. With those Red\x01",
            "Constellation troops.\x02\x03",
            "#01200FThe wound itself should heal\x01",
            "quickly... But their skill can't\x01",
            "be compared to the State Guard.\x02\x03",
            "The surprise attack worked well\x01",
            "as a diversion, but the same\x01",
            "technique won't work again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FIs that so...\x02\x03",
            "#00002FBut you really helped us\x01",
            "out back there. Thank\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01203F#3CHaha. Thanks are unnecessary.\x02\x03",
            "#01200F...Now then. It seems there is no longer\x01",
            "a need for me to accompany you, now that\x01",
            "you've recovered your battle strength.\x02\x03",
            "I will be on reserve, the same as\x01",
            "before. Call if I am needed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#00200FWith orbal waves from the\x01",
            "orbal staff, the same as\x01",
            "before, right? ...Understood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01200F#3CIf you do, I shall rush\x01",
            "into battle in my\x01",
            "original form.\x02\x03",
            "#01203FBy doing so, I should be\x01",
            "able to finish off the\x01",
            "monsters in one gulp.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha. It's reassuring\x01",
            "that you'll be in your\x01",
            "original form.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#00202FAlright then, Zeit. Once\x01",
            "again, I look forward to\x01",
            "working with you.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    OP_4C(0xB, 0xFF)
    OP_4C(0x13, 0xFF)
    SetScenarioFlags(0x1D7, 0)
    Return()

    # Function_4_20A3 end

    def Function_5_2540(): pass

    label("Function_5_2540")


    ChrTalk(
        0xB,
        (
            "#00203F...Hearing that Lawyer Ian killed Guy\x01",
            "personally, when he should have been his close\x01",
            "friend... That makes me a little uneasy.\x02\x03",
            "#00208FHe didn't have to do that for the "Azure-Zero\x01",
            "Plan", so why...\x02\x03",
            "#00206FMost of all, I wonder whether we can reach\x01",
            "this opponent not even Guy could...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...Right. That is indeed\x01",
            "concerning.\x02\x03",
            "#00008FLawyer Ian's resolve is\x01",
            "likely even greater than\x01",
            "Arios'.\x02\x03",
            "#00001FBut... That's exactly why\x01",
            "we need to show resolve\x01",
            "even greater than Ian's.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#00208FResolve even greater that\x01",
            "Lawyer Ian's... That's\x01",
            "right.\x02\x03",
            "#00201FLet's do our best, Lloyd.\x01",
            "The time to surpass Guy\x01",
            "has finally come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FYeah... Of course!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D6, 2)
    Return()

    # Function_5_2540 end

    def Function_6_27E0(): pass

    label("Function_6_27E0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_29F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27FE")
    Call(1, 11)
    Jump("loc_29EC")

    label("loc_27FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2943")

    ChrTalk(
        0xE,
        (
            "#00300FOur final opponents are the\x01",
            "slippery Mariabell and Ian,\x01",
            "the mastermind.\x02\x03",
            "#00303FBecause they're using Keddo,\x01",
            "the Sept-Terrion of Zero,\x01",
            "they'll definitely be trouble.\x02\x03",
            "#00302FBut of course, we can't take\x01",
            "even one step backwards.\x02\x03",
            "#00309FShe's our cute, beloved\x01",
            "daughter. It's time we faced\x01",
            "them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_29EC")

    label("loc_2943")


    ChrTalk(
        0xE,
        (
            "#00302FWe don't know what kind of\x01",
            "opponents they are, but we can't\x01",
            "take even one step backwards.\x02\x03",
            "#00309FShe's our cute, beloved\x01",
            "daughter. It's time we faced\x01",
            "them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29EC")

    Jump("loc_3622")

    label("loc_29F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 0)), scpexpr(EXPR_END)), "loc_2ABF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A0C")
    Call(1, 10)
    Jump("loc_2ABA")

    label("loc_2A0C")


    ChrTalk(
        0xE,
        (
            "#00303FFrom now on, I'll have to\x01",
            "keep showin' them the\x01",
            "foothold I've found...\x02\x03",
            "#00302FThough it's not perfect, I\x01",
            "have to do my best, for my\x01",
            "late old man and uncle both.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2ABA")

    Jump("loc_3622")

    label("loc_2ABF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 3)), scpexpr(EXPR_END)), "loc_2B64")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2ADA")
    Call(1, 9)
    Jump("loc_2B5F")

    label("loc_2ADA")


    ChrTalk(
        0xE,
        (
            "#00303FPast here, I have to\x01",
            "settle things with my\x01",
            "uncle, a real monster.\x02\x03",
            "#00301FI've got to change the\x01",
            "head while I still can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B5F")

    Jump("loc_3622")

    label("loc_2B64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_2D20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C80")

    ChrTalk(
        0xE,
        (
            "#00301FWe drove off Red Constellation's\x01",
            "airship, but it looks like that\x01",
            "was just a preliminary test.\x02\x03",
            "#00303FShirley and uncle are ready and\x01",
            "waiting for us past here...\x02\x03",
            "#00301FWe don't know what they have in\x01",
            "store for us. We can't let down\x01",
            "our guard.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2D1B")

    label("loc_2C80")


    ChrTalk(
        0xE,
        (
            "#00303FShirley and uncle are\x01",
            "ready and waiting for us\x01",
            "past here...\x02\x03",
            "#00301FWe don't know what they\x01",
            "have in store for us. We\x01",
            "can't let down our guard.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D1B")

    Jump("loc_3622")

    label("loc_2D20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2EA6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E36")

    ChrTalk(
        0xE,
        (
            "#00300FNo matter what that Huge\x01",
            "Tree is, to us it's small.\x01",
            "...Right, Lloyd?\x02\x03",
            "#00304FKeA will return to our side.\x01",
            "As long as we remember that,\x01",
            "everything will be ok.\x02\x03",
            "#00300FIf we have time to think\x01",
            "about it, let's start the\x01",
            "infiltration already.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2EA1")

    label("loc_2E36")


    ChrTalk(
        0xE,
        (
            "#00304FI've maintained my\x01",
            "halberd and Berserker\x01",
            "properly.\x02\x03",
            "#00300FLet's go and take back\x01",
            "KeA already.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EA1")

    Jump("loc_3622")

    label("loc_2EA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_30BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3015")

    ChrTalk(
        0xE,
        (
            "#00303FIn terms of combined battle power,\x01",
            "Red Constellation is likely\x01",
            "stronger than we are, but...\x02\x03",
            "#00301FThose Ouroboros guys have those\x01",
            "doll weapons, not to mention that\x01",
            "ridiculously skilled spear expert.\x02\x03",
            "In terms of raw power, this won't\x01",
            "be an easy fight.\x02\x03",
            "#00303F...Anyway, they're not to be taken\x01",
            "lightly. Remember that, Lloyd.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_30B9")

    label("loc_3015")


    ChrTalk(
        0xE,
        (
            "#00303FLooking at it in terms of\x01",
            "raw power, winning against\x01",
            "Ouroboros won't be easy.\x02\x03",
            "#00301F...Anyway, they're not to\x01",
            "be taken lightly. Remember\x01",
            "that, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30B9")

    Jump("loc_3622")

    label("loc_30BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_3320")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_323F")

    ChrTalk(
        0xE,
        (
            "#00300FIf we broadcast the "invalidity\x01",
            "declaration", the state guard will at\x01",
            "least take a wait-and-see position...\x02\x03",
            "#00303FThe President is personally employing\x01",
            "Red Constellation, so they'll likely\x01",
            "fight us, the same as always.\x02\x03",
            "#00308FNo... They might have things in store\x01",
            "for us that are worse than before.\x02\x03",
            "#00300FAnyway, we have to be on our guard.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_331B")

    label("loc_323F")


    ChrTalk(
        0xE,
        (
            "#00303FEven after the invalidity declaration,\x01",
            "Red Constellation will likely fight us\x01",
            "as they have until now.\x02\x03",
            "#00301FIt's also possible they have something\x01",
            "in store for us. We have to be on our\x01",
            "guard going forward.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_331B")

    Jump("loc_3622")

    label("loc_3320")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_3405")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_333B")
    Call(1, 8)
    Jump("loc_3400")

    label("loc_333B")


    ChrTalk(
        0xE,
        (
            "#00300FIt's unlikely that Shirley or\x01",
            "uncle is with the Michelam\x01",
            "security force, but...\x02\x03",
            "#00303FI'm sure there's a leader on\x01",
            "Gareth's level with them. ...We've\x01",
            "got to make sure we're prepared.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3400")

    Jump("loc_3622")

    label("loc_3405")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_3622")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3420")
    Call(1, 7)
    Jump("loc_3622")

    label("loc_3420")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3566")

    ChrTalk(
        0xE,
        (
            "#00304FMireille and the others are working\x01",
            "with the people of Mainz, so there's\x01",
            "no need to worry about them right now.\x02\x03",
            "#00300FWe've got other things to do, so let's\x01",
            "focus on what's in front of us.\x02\x03",
            "#00309FRely one me as much as you want from\x01",
            "here on out. Your bro here 'll go on a\x01",
            "nice rampage for ya.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3622")

    label("loc_3566")


    ChrTalk(
        0xE,
        (
            "#00303FWe've got other things to do, so\x01",
            "let's focus on what's in front\x01",
            "of us.\x02\x03",
            "#00300FRely one me as much as you want\x01",
            "from here on out. Your bro here\x01",
            "'ll go on a nice rampage for ya.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3622")

    TalkEnd(0xFE)
    Return()

    # Function_6_27E0 end

    def Function_7_3626(): pass

    label("Function_7_3626")


    ChrTalk(
        0xE,
        (
            "#00309FI can't believe they even have\x01",
            "a workshop... This Merkabah is\x01",
            "just full of surprises.\x02\x03",
            "#00300FWith this, it looks like I can\x01",
            "finish my Berzerker\x01",
            "maintenance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FOh yeah. Master\x01",
            "Guillaume fixed it for\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#00304FYeah. But based on his advice,\x01",
            "I'm limiting my use of it.\x02\x03",
            "#00300FAnd old man Douglas taught me\x01",
            "this halberd. I can't let my\x01",
            "skills with it get rusty, now...\x02\x03",
            "#00300FI'll be two-timing going\x01",
            "forward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, your way of saying\x01",
            "it... That's very like\x01",
            "you, Randy.\x02\x03",
            "#00003FBut, Vice Commander\x01",
            "Douglas, huh... I wonder\x01",
            "how he's doing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#00303FI'm sure that old man's carrying\x01",
            "out his Vice Commander duties with\x01",
            "integrity, the same as always.\x02\x03",
            "#00301FBut, including the commander, I\x01",
            "really don't know if they approve\x01",
            "of the current situation.\x02\x03",
            "#00303FIf they didn't, they would have\x01",
            "rebelled like Mireille and the\x01",
            "others, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FI see... We need to find\x01",
            "out what the commanders\x01",
            "are thinking somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#00304FWell, there's a lot of things we\x01",
            "need to do. Let's just focus on\x01",
            "what's in front of us.\x02\x03",
            "#00300FRely one me as much as you want\x01",
            "from here on out. Your bro here\x01",
            "'ll go on a nice rampage for ya.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha... Got it. I'll be\x01",
            "counting on you, Randy.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D7, 1)
    Return()

    # Function_7_3626 end

    def Function_8_3AF3(): pass

    label("Function_8_3AF3")


    ChrTalk(
        0xD,
        (
            "#10703FA Red Constellation\x01",
            "force is in position at\x01",
            "Michelam.\x02\x03",
            "#10708F...I wonder if Bloody\x01",
            "Shirley is with them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#00303FNo. It's not in their\x01",
            "nature to guard a place\x01",
            "where VIPs are confined.\x02\x03",
            "#00300FSomeone else is there,\x01",
            "probably another leader.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#10703FI see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#00303FRixia... For now, let's\x01",
            "focus on saving Milady\x01",
            "and the others.\x02\x03",
            "#00300FNether uncle nor Shirley\x01",
            "would get stuck on guard\x01",
            "duty like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#10708F...Yes, you're right.\x01",
            "Sorry, Randy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#00309FHaha, you don't need to\x01",
            "apologize.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0xD, 0x10)
    SetScenarioFlags(0x0, 5)
    SetScenarioFlags(0x1, 0)
    Return()

    # Function_8_3AF3 end

    def Function_9_3D0C(): pass

    label("Function_9_3D0C")


    ChrTalk(
        0xE,
        (
            "#00303FShirley is a real man-eating tiger. Ever\x01",
            "since she was little, she's been unable\x01",
            "to find joy in anything but fighting.\x02\x03",
            "The only thing that can satisfy her is\x01",
            "the battlefield, where it's kill or be\x01",
            "killed...\x02\x03",
            "#00302FAgainst an opponent like that, Rixia\x01",
            "defeated her without killing her...\x01",
            "Shirley must be very confused.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FThat's right... Before\x01",
            "losing consciousness,\x01",
            "she looked dissatisfied.\x02\x03",
            "#00002FBut Randy, it looks like\x01",
            "you're worried about\x01",
            "her?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#00302F...Haha, I guess. The fact that\x01",
            "she did what she did doesn't\x01",
            "change the fact she's my cousin.\x02\x03",
            "#00303FHonestly, when I think about\x01",
            "what she did, I can't help but\x01",
            "think it was for revenge...\x02\x03",
            "#00300FI've got to thank Rixia again\x01",
            "for not killing her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FHaha... I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#00303F...I'll need to settle\x01",
            "things with my uncle, a\x01",
            "real monster, real soon.\x02\x03",
            "#00300FWhen that time comes,\x01",
            "I'll need you to lend me\x01",
            "your strength.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FSure, of course. We'll\x01",
            "combine our strength and\x01",
            "get through this.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D7, 2)
    Return()

    # Function_9_3D0C end

    def Function_10_40F1(): pass

    label("Function_10_40F1")


    ChrTalk(
        0xE,
        "#00303F*sigh*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FYour uncle... He had\x01",
            "such amazing strength.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#00302FYeah... I was only able to\x01",
            "hold out against him because\x01",
            "of your guys' help, y'know.\x02\x03",
            "#00306FHonestly, even if I were to\x01",
            "fight him again, I'm not\x01",
            "sure I could win.\x02\x03",
            "#00300FAs the strongest jaeger, his\x01",
            "Ogre Rosso name isn't just\x01",
            "for show.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F...If we combine our strengths,\x01",
            "I'm sure we could overpower him\x01",
            "any number of times.\x02\x03",
            "#00000FBecause you're with us, Randy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#00304F...Haha, that's right. That's the\x01",
            "strength I've obtained.\x02\x03",
            "#00300FFrom now on, I'll have to keep\x01",
            "showin' him the foothold I've\x01",
            "found...\x02\x03",
            "#00303FTo my late ol' man, and uncle, to\x01",
            "whom I'm somehow indebted. That'll\x01",
            "be the greatest duty I can do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00002FYeah... The rest of will do\x01",
            "our very best to cooperate\x01",
            "with you and achieve that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        "#00309FHaha, thanks.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D7, 3)
    Return()

    # Function_10_40F1 end

    def Function_11_443C(): pass

    label("Function_11_443C")


    ChrTalk(
        0xE,
        (
            "#00301FOur final opponents are the\x01",
            "slippery Mariabell and Ian, the\x01",
            "mastermind.\x02\x03",
            "#00303FOn the basis of fighting strength\x01",
            "alone, they're more dangerous\x01",
            "than uncle or ol' man Arios.\x02\x03",
            "#00301FBecause they're using Keddo, the\x01",
            "Sept-Terrion of Zero, they'll\x01",
            "definitely be trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008FYeah... This fight might\x01",
            "be even tougher than\x01",
            "Arios was.\x02\x03",
            "#00001FBut─\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#00304FThe whole truth is waiting\x01",
            "for us there─ We can't\x01",
            "back down now, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006FD-Don't finish my\x01",
            "sentences.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xE,
        (
            "#00309FHaha. We've hung out together\x01",
            "so long, I already knew what\x01",
            "you were going to say.\x02\x03",
            "#00304FOf course. I'm not planning\x01",
            "on taking a single step\x01",
            "backwards.\x02\x03",
            "#00302FI mean, our cute, beloved\x01",
            "daughter must be waiting for\x01",
            "her fathers, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah... You're right.\x01",
            "Let's go to KeA,\x01",
            "together!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D7, 4)
    Return()

    # Function_11_443C end

    def Function_12_4778(): pass

    label("Function_12_4778")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_492D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4796")
    Call(1, 14)
    Jump("loc_4928")

    label("loc_4796")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_489E")

    ChrTalk(
        0x10,
        (
            "#10100FNow that we've come this far, I\x01",
            "think all we have to do is\x01",
            "believe in ourselves and bust in.\x02\x03",
            "#10104FTo protect Crossbell going\x01",
            "forward... Let's do our best,\x01",
            "Lloyd.\x02\x03",
            "#10102FBefore police or CGF members, in\x01",
            "this place, we are friends!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4928")

    label("loc_489E")


    ChrTalk(
        0x10,
        (
            "#10100FTo protect Crossbell\x01",
            "going forward... Let's\x01",
            "do our best, Lloyd.\x02\x03",
            "Before police or CGF\x01",
            "members, in this place,\x01",
            "we are friends!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4928")

    Jump("loc_543C")

    label("loc_492D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_4AB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A37")

    ChrTalk(
        0x10,
        (
            "#10106FI was surprised when\x01",
            "that warship appeared...\x02\x03",
            "#10100FAnyhow, I'm glad we\x01",
            "arrived safely at this\x01",
            "Huge Tree.\x02\x03",
            "#10103FIt's just, it's not a\x01",
            "given that it won't\x01",
            "appear again.\x02\x03",
            "#10101FThe standby members have\x01",
            "to be on their guard.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4AB2")

    label("loc_4A37")


    ChrTalk(
        0x10,
        (
            "#10103FIt's not a given that\x01",
            "their warship won't\x01",
            "appear again.\x02\x03",
            "#10101FThe standby members have\x01",
            "to be on their guard.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AB2")

    Jump("loc_543C")

    label("loc_4AB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4CF0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C53")

    ChrTalk(
        0x10,
        (
            "#10103FWith Arios gone, it seems command\x01",
            "of the entire State Guard has\x01",
            "transferred to Commander Sonya.\x02\x03",
            "#10100FIt looks like they'll be dealing\x01",
            "with the chaos caused by appearance\x01",
            "of that Huge Tree for a while.\x02\x03",
            "#10104FI think it'll be difficult... But\x01",
            "if we leave it to Commander Sonya,\x01",
            "I'm sure it will be fine.\x02\x03",
            "#10100FLet's push onward, to the objective\x01",
            "right in front of us!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4CEB")

    label("loc_4C53")


    ChrTalk(
        0x10,
        (
            "#10104FIf we leave the State\x01",
            "Guard to Commander Sonya,\x01",
            "I'm sure it will be fine.\x02\x03",
            "#10100FLet's push onward, to the\x01",
            "objective right in front\x01",
            "of us!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CEB")

    Jump("loc_543C")

    label("loc_4CF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_4EFA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E33")

    ChrTalk(
        0x10,
        (
            "#10101FBoth the Temple of Moon and Tower\x01",
            "of Stargaze were ruins formerly\x01",
            "under CGF supervision.\x02\x03",
            "#10106FIf we had just grasped the true\x01",
            "nature of the bells, the situation\x01",
            "wouldn't have gotten this bad...\x02\x03",
            "#10103F...But nothing will come of\x01",
            "regret. Anyway, right now, I have\x01",
            "to face forward.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4EF5")

    label("loc_4E33")


    ChrTalk(
        0x10,
        (
            "#10108FIf we had grasped the true nature\x01",
            "of the bells, the situation\x01",
            "wouldn't have gotten this bad...\x02\x03",
            "#10103F...But nothing will come of\x01",
            "regret. Anyway, right now, I have\x01",
            "to face forward.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EF5")

    Jump("loc_543C")

    label("loc_4EFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_516F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5065")

    ChrTalk(
        0x10,
        (
            "#10103FIf the legality of the independent\x01",
            "state were shaken...\x02\x03",
            "#10101FThen the legality of the State\x01",
            "Guard itself would be shaken as\x01",
            "well.\x02\x03",
            "#10108FIf Commander Sonya handles it\x01",
            "well, considerable chaos could be\x01",
            "avoided.\x02\x03",
            "#10103F...In a way, it might be a relief\x01",
            "that the major powers are unable\x01",
            "to act due to civil war and panic.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_516A")

    label("loc_5065")


    ChrTalk(
        0x10,
        (
            "#10101FIf we deliver the invalidity declaration now,\x01",
            "forces are Bellguard and Tangram gates... and\x01",
            "everywhere else too will be rather confused...\x02\x03",
            "#10103F...In a way, it might be a relief that the\x01",
            "major powers are unable to act due to civil\x01",
            "war and panic.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_516A")

    Jump("loc_543C")

    label("loc_516F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_543C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_518A")
    Call(1, 13)
    Jump("loc_543C")

    label("loc_518A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_539F")

    ChrTalk(
        0x10,
        (
            "#10105FAh, L-Lloyd...\x02\x03",
            "#10111FUmm, I... I was surprised\x01",
            "you could say something like\x01",
            ""You'll be mine", but...\x02\x03",
            "#10106FUmm, you said you didn't\x01",
            "mean it in that way, and I\x01",
            "totally understand!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FUmm, "in that way"? Even\x01",
            "now, I'm not sure which\x01",
            "way I meant it, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x10,
        (
            "#10106F(I-I wonder if he meant it\x01",
            "seriously...)\x02\x03",
            "#10100F...Ahem, anyway. Let's think\x01",
            "of the capture of Michelam\x01",
            "right now, first and foremost!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, of course. I'll be\x01",
            "counting on you, Noｱl.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_543C")

    label("loc_539F")


    ChrTalk(
        0x10,
        (
            "#10100F...Ahem, anyway. Let's think\x01",
            "of the capture of Michelam\x01",
            "right now, first and foremost!\x02\x03",
            "I will do my best, for both\x01",
            "Elie and Chairman MacDowell!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_543C")

    TalkEnd(0xFE)
    Return()

    # Function_12_4778 end

    def Function_13_5440(): pass

    label("Function_13_5440")

    OP_4B(0x10, 0xFF)
    OP_4B(0xC, 0xFF)

    ChrTalk(
        0xC,
        (
            "#01912F*sigh*... I'm really\x01",
            "glad I got to reunite\x01",
            "with my sister again.\x02\x03",
            "#01911FOooh, I think I'm gonna\x01",
            "cry again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#10112FC'mon. Fran...\x02\x03",
            "#10104F...But, I'm really glad\x01",
            "your injury healed, Fran.\x02\x03",
            "#10109FAnd it looks like you're\x01",
            "working well with Lloyd\x01",
            "and Wazy. Haha, nice work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01906FC-C'mon Noｱl. How long are you gonna\x01",
            "treat me like a kid~...\x02\x03",
            "#01905F...Oh, right. You've come to the point\x01",
            "where Lloyd said "You'll be mine" to\x01",
            "you~.\x02\x03",
            "#01906FWell, it can't be helped if you still\x01",
            "see me as a kid now that you've stepped\x01",
            "and jumped straight to adulthood...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x10)

    ChrTalk(
        0x10,
        (
            "#10111FY-You dummy! What are\x01",
            "you saying Fran!?\x02\x03",
            "#10106FLloyd said it himself!\x01",
            "He didn't mean it in\x01",
            "that way!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01909FWawa, you're getting all\x01",
            "embarrassed remembering\x01",
            "it~.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F(...I don't know what they're talking\x01",
            "about, but... It's weirdly difficult\x01",
            "to get into their conversation.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D7, 5)
    OP_4C(0x10, 0xFF)
    OP_4C(0xC, 0xFF)
    ClearChrFlags(0x10, 0x10)
    ClearChrFlags(0xC, 0x10)
    Return()

    # Function_13_5440 end

    def Function_14_57E1(): pass

    label("Function_14_57E1")


    ChrTalk(
        0x10,
        (
            "#10101FThe end is finally here...\x02\x03",
            "#10103FNow that we've come this far, I\x01",
            "think all we have to do is\x01",
            "believe in ourselves and bust in.\x02\x03",
            "#10108FEven after this incident is over,\x01",
            "many difficulties lie ahead for\x01",
            "Crossbell...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FYeah... But in the end, all we\x01",
            "can do is handle the things in\x01",
            "front of us, one by one.\x02\x03",
            "#00000FThe resolution of this incident\x01",
            "itself is just the first step\x01",
            "towards protecting Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x10,
        (
            "#10109FHaha. If my father was\x01",
            "alive, I'm sure he'd say\x01",
            "the same thing.\x02\x03",
            "#10103FTo protect Crossbell\x01",
            "going forward... Let's\x01",
            "do our best, Lloyd.\x02\x03",
            "#10102FBefore police or CGF\x01",
            "members, in this place,\x01",
            "we are friends!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D7, 6)
    Return()

    # Function_14_57E1 end

    def Function_15_5A68(): pass

    label("Function_15_5A68")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_5CB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A86")
    Call(1, 18)
    Jump("loc_5CAD")

    label("loc_5A86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BDE")

    ChrTalk(
        0xA,
        (
            "#10404FI've felt this during the short time\x01",
            "I've been with you. The "bond" between\x01",
            "you all and KeA is the real thing.\x02\x03",
            "#10402FNo matter what happens, as long as you\x01",
            "guys continue your pursuit, I think\x01",
            "there's still hope.\x02\x03",
            "#10409FWell, if this is how it's going to be,\x01",
            "I'll stick with you 'til the end. For\x01",
            "cute KeA, too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_5CAD")

    label("loc_5BDE")


    ChrTalk(
        0xA,
        (
            "#10404FNo matter what happens, as long as\x01",
            "you guys continue your pursuit, I\x01",
            "think there's still hope.\x02\x03",
            "#10409FWell, if this is how it's going to\x01",
            "be, I'll stick with you 'til the\x01",
            "end. For cute KeA, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CAD")

    Jump("loc_75A0")

    label("loc_5CB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 7)), scpexpr(EXPR_END)), "loc_5DAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D8, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CCD")
    Call(1, 17)
    Jump("loc_5DA5")

    label("loc_5CCD")


    ChrTalk(
        0xA,
        (
            "#10404FI finally settled things with him in my own\x01",
            "way. ...I thank you.\x02\x03",
            "#10402FFrom here on, I'll be supporting you in my\x01",
            "capacity as a knight of the Gralsritter and\x01",
            "as a member of the Special Support Section.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DA5")

    Jump("loc_75A0")

    label("loc_5DAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 4)), scpexpr(EXPR_END)), "loc_5ED9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5DCA")
    Call(1, 55)
    Jump("loc_5ED4")

    label("loc_5DCA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_7B(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E53")

    ChrTalk(
        0xA,
        (
            "#10403FIt seems like "he" wants\x01",
            "to settle things with\x01",
            "me.\x02\x03",
            "#10400FLet's head for the\x01",
            "barrier once we're\x01",
            "ready.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5ED4")

    label("loc_5E53")


    ChrTalk(
        0xA,
        (
            "#10403FIt seems like "he" wants\x01",
            "to settle things with\x01",
            "me.\x02\x03",
            "#10400FPlace me in the search\x01",
            "party. Let's head for\x01",
            "the barrier.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5ED4")

    Jump("loc_75A0")

    label("loc_5ED9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_6085")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FEA")

    ChrTalk(
        0xA,
        (
            "#10404FNow then, it's finally time to\x01",
            "begin our exploration.\x02\x03",
            "#10401FIt's too bad we can't proceed\x01",
            "in the Merkabah... But "he" is\x01",
            "waiting for me ahead.\x02\x03",
            "#10403FI'll have to advance steadily,\x01",
            "and finally settle the things\x01",
            "I failed to before.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6080")

    label("loc_5FEA")


    ChrTalk(
        0xA,
        (
            "#10401FHe is waiting for us ahead\x01",
            "within the Huge Tree.\x02\x03",
            "#10403FI'll have to advance steadily,\x01",
            "and finally settle the things\x01",
            "I failed to before.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6080")

    Jump("loc_75A0")

    label("loc_6085")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_636A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6283")

    ChrTalk(
        0xA,
        (
            "#10403FNow that that Huge Tree appeared, it\x01",
            "looks like the Holy Nation of Arteria\x01",
            "is in an uproar as well.\x02\x03",
            "#10400FAnyhow, this is an "unexpected\x01",
            "miracle" that isn't recorded in any\x01",
            "of the Church's Testaments.\x02\x03",
            "#10408FThe Pillar of Salt was one of those\x01",
            "as well. The leaders can't help but\x01",
            "exercise caution...\x02\x03",
            "#10400FBut, as long as KeA is in there, we\x01",
            "can't take it easy.\x02\x03",
            "I'm taking responsibility. So if\x01",
            "you're going to the Huge Tree, please\x01",
            "feel free to tell Abbas for me.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6365")

    label("loc_6283")


    ChrTalk(
        0xA,
        (
            "#10404FAs long as KeA's over there, we don't\x01",
            "have time to wait for direction from\x01",
            "the Holy Nation of Arteria.\x02\x03",
            "#10400FI'm taking responsibility. So if\x01",
            "you're going to the Huge Tree, please\x01",
            "feel free to tell Abbas for me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6365")

    Jump("loc_75A0")

    label("loc_636A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_6629")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6539")

    ChrTalk(
        0xA,
        (
            "#10400FOur order and Ouroboros have fought many\x01",
            "times, outside the gaze of history. We\x01",
            "are fated opponents, so to speak.\x02\x03",
            "#10403FOur order has looked into them, but we\x01",
            "have especially little information on\x01",
            "the Fool and Steel Maiden.\x02\x03",
            "We'll have to come to grips with the\x01",
            "fact we've no effective way to oppose\x01",
            "them...\x02\x03",
            "#10402FNothing ventured, nothing gained, they\x01",
            "say. Anyway, let's dive in and see if\x01",
            "there's a chance at victory.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6624")

    label("loc_6539")


    ChrTalk(
        0xA,
        (
            "#10403FOur order has looked into Ouroboros, but\x01",
            "we have especially little information on\x01",
            "the Fool and Steel Maiden.\x02\x03",
            "#10402FNothing ventured, nothing gained, they\x01",
            "say. Anyway, let's dive in and see if\x01",
            "there's a chance at victory.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6624")

    Jump("loc_75A0")

    label("loc_6629")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_6806")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6797")

    ChrTalk(
        0xA,
        (
            "#10402FIt looks like there's especially\x01",
            "little security around the booster\x01",
            "site.\x02\x03",
            "#10404FIt's outside the State Guard and\x01",
            "jaegers' security zone, so if we head\x01",
            "there in the Merkabah, it looks like\x01",
            "we'll finish without interruption.\x02\x03",
            "#10408FWhat will this "invalidity\x01",
            "declaration" change...?\x02\x03",
            "#10409FHaha. Only the Goddess knows, huh.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6801")

    label("loc_6797")


    ChrTalk(
        0xA,
        (
            "#10404FWhat will this\x01",
            ""invalidity declaration"\x01",
            "change...?\x02\x03",
            "#10409FHaha. Only the Goddess\x01",
            "knows, huh.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6801")

    Jump("loc_75A0")

    label("loc_6806")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_6A9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69E5")

    ChrTalk(
        0xA,
        (
            "#10402FThe beach at Michelam, huh... To\x01",
            "think I'd be going there like\x01",
            "this.\x02\x03",
            "#10406FIf possible, I'd like to take a\x01",
            "leisurely vacation day on the\x01",
            "beach with everyone again, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FWe'll take back KeA...\x01",
            "And once everything's\x01",
            "over, I'm sure we will.\x02\x03",
            "#00000FAnd next time, let's\x01",
            "invite Chief, Abbas and\x01",
            "Commander Sonya as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10409FAhaha, that would be\x01",
            "great!\x02\x03",
            "#10400FI'll put forth every\x01",
            "effort to grab hold of\x01",
            "that day, too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6A99")

    label("loc_69E5")


    ChrTalk(
        0xA,
        (
            "#10404FThe beach at Michelam... Rather\x01",
            "than a day off, a hard fight is\x01",
            "waiting for us this time.\x02\x03",
            "#10400FI'll put forth every effort to\x01",
            "grab hold of peaceful days once\x01",
            "again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A99")

    Jump("loc_75A0")

    label("loc_6A9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_6E13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D30")

    ChrTalk(
        0xA,
        (
            "#10404FDamn, that Grace. She wants\x01",
            "to interview me no matter\x01",
            "what.\x02\x03",
            "Abbas will get mad so it's\x01",
            "not particularly a problem,\x01",
            "but...\x02\x03",
            "#10409FIf she's this enthusiastic,\x01",
            "I might need to feed her\x01",
            "some half-truths.\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xF, 0xA, 0)
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6C18")
    Jump("loc_6C62")

    label("loc_6C18")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6C38")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6C62")

    label("loc_6C38")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6C58")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6C62")

    label("loc_6C58")

    OP_52(0xF, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6C62")

    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xF, 0x10)

    ChrTalk(
        0xF,
        (
            "#02109FAh, that's no good,\x01",
            "Wazyyy. Just limit\x01",
            "yourself to the "truth"!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00006F(Abbas is having a hard\x01",
            "time too, huh...)\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xF, 0x0)
    SetScenarioFlags(0x0, 7)
    Jump("loc_6E0E")

    label("loc_6D30")


    ChrTalk(
        0xA,
        (
            "#10404FIn a word, Testaments is a play on the\x01",
            "word "scriptures", see.\x02\x03",
            "#10409FHonestly, Abbas is super annoying over\x01",
            "anything that I think is good. He's\x01",
            "the type to obsess over appearances.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    label("loc_6E0E")

    Jump("loc_75A0")

    label("loc_6E13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_718F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_70AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D8, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F8B")

    ChrTalk(
        0xA,
        (
            "#10403FIt looks like Rixia is on the\x01",
            "deck, lost in thought.\x02\x03",
            "Arc-en-Ciel, Heiyue, and Yin's\x01",
            "duty... There's probably a lot\x01",
            "she's worried about.\x02\x03",
            "#10402FHaha. If you like, why not\x01",
            "give her some advice?\x02\x03",
            "#10409FIt's possible you'll trigger\x01",
            "some kind of flag, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI-I won't speak to her\x01",
            "with that kind of\x01",
            "ulterior motive.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70A5")

    label("loc_6F8B")


    ChrTalk(
        0xA,
        (
            "#10403FIt looks like Rixia is on the\x01",
            "deck, lost in thought.\x02\x03",
            "Arc-en-Ciel, Heiyue, and Yin's\x01",
            "duty... There's probably a lot\x01",
            "she's worried about.\x02\x03",
            "#10402FHaha, then... If you speak\x01",
            "with her, maybe you'll trigger\x01",
            "some kind of flag?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FT-That kind of thing\x01",
            "doesn't exist.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_70A5")

    SetScenarioFlags(0x0, 7)
    Jump("loc_718A")

    label("loc_70AD")


    ChrTalk(
        0xA,
        (
            "#10404FEven so, Rixia... The clothes she's\x01",
            "wearing now aside, you can't really\x01",
            "tell that she's Yin, can you?\x02\x03",
            "#10400FHehe. Because her personality is so\x01",
            "normal, I could say it's only\x01",
            "natural if you didn't notice it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_718A")

    Jump("loc_75A0")

    label("loc_718F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_7348")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72B1")

    ChrTalk(
        0xA,
        (
            "#10400FNow that Tio and the others are\x01",
            "here, we'll be able to make\x01",
            "efficient use of this ship.\x02\x03",
            "#10404FEven if we find Gaps, there's a\x01",
            "limit to what we can do on our own.\x01",
            "This is a big step forward for us.\x02\x03",
            "#10400FHaha, this might be the guidance of\x01",
            "Aidios.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_7343")

    label("loc_72B1")


    ChrTalk(
        0xA,
        (
            "#10404FFirst, we went to St. Ursula\x01",
            "Hospital and rendezvoused\x01",
            "with Tio and the others...\x02\x03",
            "#10400FHaha, this might be the\x01",
            "guidance of Aidios.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7343")

    Jump("loc_75A0")

    label("loc_7348")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_75A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7363")
    Call(1, 16)
    Jump("loc_75A0")

    label("loc_7363")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_74FF")

    ChrTalk(
        0xA,
        (
            "#10406FThings are looking pretty grim... But for\x01",
            "right now, we've got to keep a steady pace.\x02\x03",
            "#10400F...Oh, that's right. I don't mind if you\x01",
            "use the facilities onboard freely.\x02\x03",
            "There are equipment, accessory and workshop\x01",
            "facilities─ And if you go to the upper deck\x01",
            "corridor there's a nap room you can use.\x02\x03",
            "#10409FWhy don't you go to check them out while\x01",
            "also having a look at the crew?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_75A0")

    label("loc_74FF")


    ChrTalk(
        0xA,
        (
            "#10400FI don't mind if you use\x01",
            "the facilities onboard the\x01",
            "Merkabah freely.\x02\x03",
            "#10409FWhy don't you go to check\x01",
            "them out while also having\x01",
            "a look at the crew?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_75A0")

    TalkEnd(0xFE)
    Return()

    # Function_15_5A68 end

    def Function_16_75A4(): pass

    label("Function_16_75A4")


    ChrTalk(
        0xA,
        (
            "#10403FFor starters, we found a gap at the\x01",
            "St. Ursula Byroad sandbank before\x01",
            "anything strange occurred, but...\x02\x03",
            "#10400FFrom now on, we'll need to detect\x01",
            "Gaps where it looks like we can\x01",
            "land.\x02\x03",
            "#10406FThe Merkabah is short of crew, and\x01",
            "things are looking pretty grim.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...Even so, let's proceed one\x01",
            "step at a time.\x02\x03",
            "#00001FWe need to get our friends and\x01",
            "KeA back... I know all too\x01",
            "well that it won't be easy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10402FHaha, got it. For now,\x01",
            "we've got to keep up a\x01",
            "steady pace.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D7, 7)
    Return()

    # Function_16_75A4 end

    def Function_17_7796(): pass

    label("Function_17_7796")


    ChrTalk(
        0xA,
        "#10402FHey, nice work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FNice work yourself...\x01",
            "How are you feeling?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10404FOh, no need to worry. As\x01",
            "you can see, I'm taking a\x01",
            "break.\x02\x03",
            "#10408FThe recoil was huge. It's a\x01",
            "much power as I can\x01",
            "normally muster, you see...\x02\x03",
            "#10404FHaha. It's been a while\x01",
            "since I got so fired up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYou gave everything you\x01",
            "had to defeat Wald...\x02\x03",
            "I guess you needed to do\x01",
            "that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10404FYeah, exactly.\x02\x03",
            "#10408F...If I had used my full power\x01",
            "from the start, maybe he wouldn't\x01",
            "have tormented himself so much.\x02\x03",
            "#10403FI'm probably completely\x01",
            "responsible in that respect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FBut...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10402FHehe, it's ok. I don't\x01",
            "regret it, but it'll have to\x01",
            "learn from it going forward.\x02\x03",
            "#10404FIn any case... I finally\x01",
            "settled things with him in\x01",
            "my own way.\x02\x03",
            "Now, the duty of Wazy\x01",
            "Hemisphere, the Testaments\x01",
            "leader, is finished.\x02\x03",
            "#10402FAllow me to thank all of\x01",
            "you, who saw this through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha... You're welcome.\x02\x03",
            "#00000FThough strong enemies are\x01",
            "waiting for us ahead... Let's\x01",
            "work together once again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10402FHehe. Roger that, leader.\x02\x03",
            "#10404FFrom here on, I'll be supporting you in my\x01",
            "capacity as a knight of the Gralsritter and\x01",
            "as a member of the Special Support Section.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D8, 1)
    Return()

    # Function_17_7796 end

    def Function_18_7C45(): pass

    label("Function_18_7C45")


    ChrTalk(
        0xA,
        (
            "#10400FWe got some information out of the Divine\x01",
            "Blade of Wind, but several mysteries\x01",
            "remain.\x02\x03",
            "#10403FThe Azure-Zero Plan... Mr. Beardy Bear\x01",
            "planned the whole thing.\x02\x03",
            "#10408FMariabell must have known the capabilities\x01",
            "of KeA, the Sept-Terrion of Zero, but just\x01",
            "how is she planning on using them?\x02\x03",
            "#10406FIt seems our only way forward is to\x01",
            "question her directly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FYeah... I'm sure we'll\x01",
            "understand if we make\x01",
            "our way to them.\x02\x03",
            "#00008FMaybe even the reason\x01",
            "why KeA joined them...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10404F...Well, there's no need to worry.\x02\x03",
            "#10402FI've felt this during the short time\x01",
            "I've been with you. The "bond" between\x01",
            "you all and KeA is the real thing.\x02\x03",
            "#10409FNo matter what happens, as long as you\x01",
            "guys continue your pursuit, I think\x01",
            "there's still hope.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000F...Right. I'm sure\x01",
            "everything will go well.\x02\x03",
            "#00005FBut, you talk like you're\x01",
            "not one of us. Aren't you\x01",
            "part of that "bond"?\x02\x03",
            "#00004FI'm sure KeA would think\x01",
            "so too... Let's all make\x01",
            "our way to her together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10404F...Haha, well aren't you the\x01",
            "charmer?\x02\x03",
            "#10402FWell, if this is how it's going\x01",
            "to be, I'll stick with you 'til\x01",
            "the end. For cute KeA, too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D8, 2)
    Return()

    # Function_18_7C45 end

    def Function_19_80B6(): pass

    label("Function_19_80B6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_82D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_80D4")
    Call(1, 21)
    Jump("loc_82D0")

    label("loc_80D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8210")

    ChrTalk(
        0xD,
        (
            "#10708FYin and the path of the artist...\x01",
            "I haven't concretely decided which\x01",
            "I'll follow going forward...\x02\x03",
            "#10704FRight now, I feel I want to\x01",
            "protect Crossbell... The place\x01",
            "Ilya and the others live.\x02\x03",
            "#10702FTo protect "that which is\x01",
            "important"... I will do all I can,\x01",
            "together with all of you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_82D0")

    label("loc_8210")


    ChrTalk(
        0xD,
        (
            "#10704FRight now, I feel I want to\x01",
            "protect Crossbell... The place\x01",
            "Ilya and the others live.\x02\x03",
            "#10702FTo protect "that which is\x01",
            "important"... I will do all I\x01",
            "can, together with all of you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_82D0")

    Jump("loc_8F64")

    label("loc_82D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 3)), scpexpr(EXPR_END)), "loc_839A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D8, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_82F0")
    Call(1, 20)
    Jump("loc_8395")

    label("loc_82F0")


    ChrTalk(
        0xD,
        (
            "#10703FThanks to all of you, I\x01",
            "was finally able to\x01",
            "settle things with her.\x02\x03",
            "#10702FTo repay that favor... I\x01",
            "will stick with you until\x01",
            "the end of this incident.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8395")

    Jump("loc_8F64")

    label("loc_839A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 5)), scpexpr(EXPR_END)), "loc_84EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D8, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_83BA")
    Call(1, 54)
    Jump("loc_84E6")

    label("loc_83BA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_7B(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_845B")

    ChrTalk(
        0xD,
        (
            "#10703F...I'm ready. Let's head\x01",
            "for the barrier\x01",
            "immediately.\x02\x03",
            "#10701FTo discover the way\x01",
            "forward as well... I\x01",
            "must see her once again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_84E6")

    label("loc_845B")


    ChrTalk(
        0xD,
        (
            "#10703F...I'm ready. Please\x01",
            "include me in the search\x01",
            "party.\x02\x03",
            "#10701FTo discover the way\x01",
            "forward as well... I\x01",
            "must see her once again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_84E6")

    Jump("loc_8F64")

    label("loc_84EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_864E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_85B8")

    ChrTalk(
        0xD,
        (
            "#10703F...We've finally come this\x01",
            "far.\x02\x03",
            "Many masters are lined up\x01",
            "for us, "her" included.\x02\x03",
            "#10701FLet us harden our resolve.\x01",
            "To grab hold of that which\x01",
            "is precious to us...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8649")

    label("loc_85B8")


    ChrTalk(
        0xD,
        (
            "#10703FMany masters are lined up\x01",
            "for us, "her" included.\x02\x03",
            "#10701FLet us harden our resolve.\x01",
            "To grab hold of that which\x01",
            "is precious to us...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8649")

    Jump("loc_8F64")

    label("loc_864E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_8A04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_886C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_87B3")

    ChrTalk(
        0xD,
        (
            "#10703FFor my own reasons as well... I\x01",
            "must settle things with "her".\x01",
            "She waits in the Huge Tree.\x02\x03",
            "#10701F...My mind is made up. Let us\x01",
            "depart once preparations are\x01",
            "complete.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(Now that Arc-en-Ciel is\x01",
            "free, possibly...)\x02\x03",
            "(Before heading to the Huge\x01",
            "Tree, maybe I should take\x01",
            "Rixia to see "that person"?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8867")

    label("loc_87B3")


    ChrTalk(
        0xD,
        (
            "#10703FFor my own reasons as well... I\x01",
            "must settle things with "her".\x01",
            "She waits in the Huge Tree.\x02\x03",
            "#10701F...My mind is made up. Let us\x01",
            "depart once preparations are\x01",
            "complete.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8867")

    Jump("loc_89FF")

    label("loc_886C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8970")

    ChrTalk(
        0xD,
        (
            "#10704FNow that Ilya has given me\x01",
            "courage, I have nothing to\x01",
            "fear.\x02\x03",
            "#10701FLater, for my own reasons as\x01",
            "well, I must settle things\x01",
            "with "her".\x02\x03",
            "#10702F...My mind is made up. Once\x01",
            "preparations are complete, let\x01",
            "us head for the Huge Tree.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_89FF")

    label("loc_8970")


    ChrTalk(
        0xD,
        (
            "#10704FNow that Ilya has given\x01",
            "me courage, I have\x01",
            "nothing to fear.\x02\x03",
            "#10702FOnce preparations are\x01",
            "complete, let us head\x01",
            "for the Huge Tree.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_89FF")

    Jump("loc_8F64")

    label("loc_8A04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_8BE7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B08")

    ChrTalk(
        0xD,
        (
            "#10708FTo think I, Yin, would help\x01",
            "save Crossbell...\x02\x03",
            "#10703FIt is a bit late for this, but\x01",
            "I feel it is a role I do not\x01",
            "deserve.\x02\x03",
            "#10701F...But, to free Crossbell City\x01",
            "and Arc-en-Ciel... I shall do\x01",
            "my very best for all of you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8BE2")

    label("loc_8B08")


    ChrTalk(
        0xD,
        (
            "#10708FTo think I, Yin, would help save\x01",
            "Crossbell. I feel it is a role that\x01",
            "is more than I deserve.\x02\x03",
            "#10701FBut, now that Crossbell City and Arc-\x01",
            "en-Ciel have been freed... I shall do\x01",
            "my very best for all of you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8BE2")

    Jump("loc_8F64")

    label("loc_8BE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_8C8A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C02")
    Call(1, 8)
    Jump("loc_8C85")

    label("loc_8C02")


    ChrTalk(
        0xD,
        (
            "#10708FBloody Shirley... Her\x01",
            "attitude bothers me,\x01",
            "but...\x02\x03",
            "#10703F...For right now, let's\x01",
            "focus on saving Elie and\x01",
            "the others.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C85")

    Jump("loc_8F64")

    label("loc_8C8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_8F64")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E89")

    ChrTalk(
        0xD,
        (
            "#10705FH-Honestly, I'd like you\x01",
            "not to write an article\x01",
            "about Yin.\x02\x03",
            "#10706FI'm worried about it for\x01",
            "some reason...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02103FThe real story behind everyone's favorite\x01",
            "theatrical troupe! The history and truth behind\x01",
            "the legendary Yin! Rixia Mao's three sizes!\x02\x03",
            "#02109FYou won't get many chances like this. C'mon,\x01",
            "tell me everything~♪\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xD, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0xD,
        "#10706FOooh, Lloyd~...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FDodge her questions the\x01",
            "best you can somehow...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xF, 0x0)
    SetScenarioFlags(0x1, 0)
    Jump("loc_8F64")

    label("loc_8E89")


    ChrTalk(
        0xD,
        (
            "#10706FIt's always been the troupe chief who cut\x01",
            "her short for me at the proper time...\x01",
            "T-To think she was this persistent...\x02\x03",
            "#10709FReally, I'd like you not to write an\x01",
            "article... I'm somehow worried about\x01",
            "it...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F64")

    TalkEnd(0xFE)
    Return()

    # Function_19_80B6 end

    def Function_20_8F68(): pass

    label("Function_20_8F68")


    ChrTalk(
        0xD,
        (
            "#10703FBloody Shirley...\x02\x03",
            "Like her name says, her\x01",
            "path must be dyed with\x01",
            "blood.\x02\x03",
            "She lives for that\x01",
            "purpose, and to derive\x01",
            "joy from battlefields...\x02\x03",
            "#10708FAs Yin, I do not view\x01",
            "that as someone else's\x01",
            "problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00001FRixia...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#10704FBut... I feel I have finally\x01",
            "changed.\x02\x03",
            "#10702FIlya, Lloyd and everyone else,\x01",
            "too... I feel I've changed\x01",
            "through the people I've met.\x02\x03",
            "#10703FTo the extent that she and I, who\x01",
            "are so similar, ended up walking\x01",
            "on completely different paths...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FBy meeting people...\x02\x03",
            "#00000FIf you think about it,\x01",
            "maybe all of this was\x01",
            "fate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#10702FYes... I believe that's\x01",
            "true.\x02\x03",
            "#10704FThanks to all of you, I\x01",
            "was finally able to\x01",
            "settle things with her.\x02\x03",
            "#10702FTo repay that favor... I\x01",
            "will stick with you until\x01",
            "the end of this incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, we're counting on\x01",
            "you, Rixia.\x02\x03",
            "We'll save KeA\x01",
            "together... And bring a\x01",
            "smile to Ilya's face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#10709FHaha, right.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D8, 5)
    Return()

    # Function_20_8F68 end

    def Function_21_9303(): pass

    label("Function_21_9303")


    ChrTalk(
        0xD,
        (
            "#10708F...The end of this\x01",
            "journey grows close.\x02\x03",
            "#10703FI don't know how useful\x01",
            "Yin's power will be\x01",
            "against Mariabell, but...\x02\x03",
            "#10701FAnyway, I will do\x01",
            "everything I am able,\x01",
            "together with all of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah... I'm counting on you.\x02\x03",
            "#00009FHaha, maybe I'm late in saying this,\x01",
            "but... Fighting, cooperating with each\x01",
            "other... We've been through a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#10709FA-Ahaha... Thank you for that.\x02\x03",
            "#10703FYin and the path of the artist...\x01",
            "I haven't concretely decided which\x01",
            "I'll follow going forward...\x02\x03",
            "#10702FRight now, I feel I want to\x01",
            "protect Crossbell... The place\x01",
            "Ilya and the others live.\x02\x03",
            "#10704FIf the power I have as Yin is of\x01",
            "use, then... I shall display it\x01",
            "without hesitation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FThanks, Rixia... We'll\x01",
            "be counting on you.\x02\x03",
            "#00000FLet's do our best\x01",
            "together, to protect\x01",
            "what is precious to us!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#10702FYes!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D8, 6)
    Return()

    # Function_21_9303 end

    def Function_22_9651(): pass

    label("Function_22_9651")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_9822")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_966F")
    Call(1, 23)
    Jump("loc_981D")

    label("loc_966F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9759")

    ChrTalk(
        0x13,
        (
            "#01203F#3COnce, Demiurgos, the Sept-\x01",
            "Terrion of Mirage, chose\x01",
            "to annihilate itself...\x02\x03",
            "#01200FI can't say that KeA won't\x01",
            "arrive at the same\x01",
            "conclusion.\x02\x03",
            "Child of man, take KeA\x01",
            "back and stop that from\x01",
            "happening.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_981D")

    label("loc_9759")


    ChrTalk(
        0x13,
        (
            "#01203F#3CI can't say it's impossible that KeA\x01",
            "will arrived at the same conclusion of\x01",
            "Demiurgos, the Sept-Terrion of Mirage.\x02\x03",
            "#01200FChild of man, take KeA back and stop\x01",
            "that from happening.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_981D")

    Jump("loc_A683")

    label("loc_9822")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_9992")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9912")

    ChrTalk(
        0x13,
        (
            "#01203F#3CThere's no doubt that KeA is\x01",
            "somewhere inside this Huge\x01",
            "Tree.\x02\x03",
            "#01200FPerhaps she is in its deepest\x01",
            "place... with that Crois clan\x01",
            "woman and mastermind lawyer.\x02\x03",
            "Call me any time if you need\x01",
            "my help.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_998D")

    label("loc_9912")


    ChrTalk(
        0x13,
        (
            "#01203F#3CThere's no doubt that\x01",
            "KeA is somewhere inside\x01",
            "this Huge Tree.\x02\x03",
            "#01200FCall me any time if you\x01",
            "need my help.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_998D")

    Jump("loc_A683")

    label("loc_9992")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_9B93")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9AB4")

    ChrTalk(
        0x13,
        (
            "#01200F#3CI haven't the slightest idea\x01",
            "how much you'll be able to do\x01",
            "in that Huge Tree.\x02\x03",
            "She has power rivaling that of\x01",
            "the Goddess... and that is no\x01",
            "exaggeration.\x02\x03",
            "#01203FTo think the deep-rooted\x01",
            "delusions of the children of\x01",
            "man could lead to this point...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_9B8E")

    label("loc_9AB4")


    ChrTalk(
        0x13,
        (
            "#01200F#3CIt wouldn't be an exaggeration to say\x01",
            "that... In that Huge Tree, she has\x01",
            "power rivaling that of the Goddess.\x02\x03",
            "#01203FTo think the deep-rooted delusions of\x01",
            "the children of man could lead to\x01",
            "this point...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9B8E")

    Jump("loc_A683")

    label("loc_9B93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_9E1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9D47")

    ChrTalk(
        0x13,
        (
            "#01203F#3CThe bells in Crossbell are things\x01",
            "that create a "place" to amplify\x01",
            "the Sept-Terrion's power...\x02\x03",
            "#01200FIf we reference this to the\x01",
            "present situation, we can\x01",
            "probably believe Jｶrg's results.\x02\x03",
            "#01203FHowever, creating that cult's\x01",
            "cradle... To think the children\x01",
            "of man succeeded in such an act.\x02\x03",
            "#01200FOnce again, the alchemists of the\x01",
            "Crois clan seem to have some\x01",
            "absurd deep-rooted delusions.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_9E1A")

    label("loc_9D47")


    ChrTalk(
        0x13,
        (
            "#01203F#3CHowever, creating that cult's\x01",
            "cradle... To think the children\x01",
            "of man succeeded in such an act.\x02\x03",
            "#01200FOnce again, the alchemists of\x01",
            "the Crois clan seem to have some\x01",
            "absurd deep-rooted delusions.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9E1A")

    Jump("loc_A683")

    label("loc_9E1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_A050")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9E3A")
    Call(1, 4)
    Jump("loc_A04B")

    label("loc_9E3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F76")

    ChrTalk(
        0x13,
        (
            "#01203F#3CAs you're now, you don't need\x01",
            "my protection.\x02\x03",
            "#01200FLike before, I'll stay behind\x01",
            "and you can call me in the\x01",
            "time of need.\x02\x03",
            "From now on, I'll come running\x01",
            "to battle in my original form.\x02\x03",
            "#01203FHu hu, if these are the kind\x01",
            "of monsters roaming around, it\x01",
            "seems they'll be easy prey.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_A04B")

    label("loc_9F76")


    ChrTalk(
        0x13,
        (
            "#01200F#3CIf you'll call me in your time of\x01",
            "need, From now on, I'll come running\x01",
            "to battle in my original form.\x02\x03",
            "#01203FHu hu, if these are the kind of\x01",
            "monsters roaming around, it seems\x01",
            "they'll be easy prey.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A04B")

    Jump("loc_A683")

    label("loc_A050")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_A310")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A25F")

    ChrTalk(
        0x13,
        (
            "#01200F#3CLeave diverting the jaegers to me. If I\x01",
            "return to my original form, I should be\x01",
            "able to draw in quite a number of them...\x02\x03",
            "During that time, drive away their\x01",
            "dispersed forces and head to where Elie\x01",
            "and the Chairman are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FWe're up against jaegers. I\x01",
            "think they'll be very dangerous\x01",
            "for you as well, Zeit...\x02\x03",
            "#00001FPlease, be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01203F#3CHaha, do not worry. I\x01",
            "don't plan to go down so\x01",
            "easily.\x02\x03",
            "#01200FI swear on my divine\x01",
            "wolf pride that I'll\x01",
            "make sport of them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_A30B")

    label("loc_A25F")


    ChrTalk(
        0x13,
        (
            "#01203F#3CIf I return to my original\x01",
            "form, I should be able to draw\x01",
            "in quite a number of them...\x02\x03",
            "#01200FI swear on my divine wolf\x01",
            "pride that I'll make sport of\x01",
            "them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A30B")

    Jump("loc_A683")

    label("loc_A310")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_A3F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A32B")
    Call(1, 3)
    Jump("loc_A3EC")

    label("loc_A32B")


    ChrTalk(
        0x13,
        (
            "#01200F#3CMy family has been keeping an eye\x01",
            "on Crossbell for generations,\x01",
            "since the era Ursula lived in.\x02\x03",
            "They're probably somewhere\x01",
            "watching the situation\x01",
            "attentively. You needn't worry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A3EC")

    Jump("loc_A683")

    label("loc_A3F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_A683")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A5D4")

    ChrTalk(
        0x13,
        "#01200F#3C...That nurse woman...\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005FEhhm... I there\x01",
            "something wrong with\x01",
            "sister Cecil?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01203F#3C...Hehe, no, nothing. I\x01",
            "thought it was karma for\x01",
            "sure.\x02\x03",
            "It's nothing important,\x01",
            "pay it no mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01200F#3CIn any case, I could say\x01",
            "it was fortuitous to be\x01",
            "able to reunite with Tio.\x02\x03",
            "Now go to get back your\x01",
            "SSS friends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FY-Yeah. I don't\x01",
            "understand very well,\x01",
            "but... I'll do it.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_A683")

    label("loc_A5D4")


    ChrTalk(
        0x13,
        (
            "#01200F#3CIn any case, I could say it\x01",
            "was fortuitous to be able to\x01",
            "reunite with Tio.\x02\x03",
            "She seems kind of busy now,\x01",
            "but... Hehe, I guess I'll go\x01",
            "see how she's doing later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A683")

    TalkEnd(0xFE)
    Return()

    # Function_22_9651 end

    def Function_23_A687(): pass

    label("Function_23_A687")


    ChrTalk(
        0x13,
        (
            "#01200F#3COnce, Demiurgos, the Sept-\x01",
            "Terrion of Mirage, chose\x01",
            "to annihilate itself...\x02\x03",
            "I told you that, right\x01",
            "Lloyd?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FIt went berserk, and so, to defend\x01",
            "against hurting the people it should have\x01",
            "protected... It was like that, right?\x02\x03",
            "#00003F...Will even KeA, the Sept-Terrion of\x01",
            "Zero, end up like that...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01200F#3C...I don't know.\x02\x03",
            "However, KeA became the Sept-Terrion of Zero and\x01",
            "in the end she even brought forth this Azure\x01",
            "Tree with a power rivaling that of the Goddess.\x02\x03",
            "At present, there's no guarantee that she'll be\x01",
            "able to control such immense power in the\x01",
            "future.\x02\x03",
            "#01203FI can't say she won't arrive at the same\x01",
            "conclusion that Demiurgos, the Sept-Terrion of\x01",
            "Mirage did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FIs that so...\x02\x03",
            "#00001FWell, as long as we're\x01",
            "here, I won't let her!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x13,
        (
            "#01200F#3C...Hehe, that's why\x01",
            "you're you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D9, 0)
    Return()

    # Function_23_A687 end

    def Function_24_A9CA(): pass

    label("Function_24_A9CA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A9F1")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7F), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_A9F1")
    OP_50(0x6B, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1DE, 3)

    label("loc_A9F1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x6B), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AA0C")
    Call(1, 53)
    Jump("loc_B194")

    label("loc_AA0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_AAC6")

    ChrTalk(
        0x14,
        (
            "#00603FYou have your own character.\x01",
            "By growing that, you can\x01",
            "become an excellent detective.\x02\x03",
            "#00602FFrom now on, you should work\x01",
            "to find your own goal as a\x01",
            "detective.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B194")

    label("loc_AAC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_AC98")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AAE1")
    Call(1, 25)
    Jump("loc_AC93")

    label("loc_AAE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ABFB")

    ChrTalk(
        0x14,
        (
            "#00603FThe death of Guy Bannings... Three\x01",
            "years have passed since then, and the\x01",
            "real truth has finally come to light.\x02\x03",
            "All that's left is to resolve this\x01",
            "situation, in a real sense.\x02\x03",
            "#00602FGo, Bannings. Now is the time. Show\x01",
            "me you can surpass your brother.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_AC93")

    label("loc_ABFB")


    ChrTalk(
        0x14,
        (
            "#00603FAll that's left is to\x01",
            "resolve this situation,\x01",
            "in a real sense.\x02\x03",
            "#00602FGo, Bannings. Now is the\x01",
            "time. Show me you can\x01",
            "surpass your brother.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AC93")

    Jump("loc_B194")

    label("loc_AC98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_AEE9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AE05")

    ChrTalk(
        0x14,
        (
            "#00600FNever stop moving, Bannings. To arrive at\x01",
            "the truth, all you can do is take one step\x01",
            "at a time.\x02\x03",
            "#00603FAbove all, we need to resolve this incident\x01",
            "quickly. We don't know what impact this\x01",
            "Huge Tree will have on Crossbell.\x02\x03",
            "#00608FIan, Mariabell... They won't be easy\x01",
            "opponents to deal with, but I'm sure we can\x01",
            "overcome them.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_AEE4")

    label("loc_AE05")


    ChrTalk(
        0x14,
        (
            "#00600FWe need to resolve this incident\x01",
            "quickly. We don't know what impact\x01",
            "this Huge Tree will have on Crossbell.\x02\x03",
            "#00608FIan, Mariabell... They won't be easy\x01",
            "opponents to deal with, but I'm sure\x01",
            "we can overcome them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AEE4")

    Jump("loc_B194")

    label("loc_AEE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_B194")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B0AE")

    ChrTalk(
        0x14,
        (
            "#00608FI can't believe it... To\x01",
            "think Ian was the\x01",
            "mastermind...\x02\x03",
            "#00610FGuh. How pitiful,\x01",
            "considering how frequently\x01",
            "I visited his office.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003FMr. Dudley...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#00603F...Anyway, the only way forward is to\x01",
            "meet with Ian and Mariabell directly and\x01",
            "question their motives.\x02\x03",
            "#00601FThis is no longer a problem for the\x01",
            "Support Section alone. I will do whatever\x01",
            "it takes to grab hold of the truth!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FRight!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_B194")

    label("loc_B0AE")


    ChrTalk(
        0x14,
        (
            "#00603F...Anyway, the only way is to meet with\x01",
            "Ian and Mariabell direction and question\x01",
            "their motives.\x02\x03",
            "#00600FThis is no longer a problem for the\x01",
            "Support Section alone. I will do whatever\x01",
            "it takes to grab hold of the truth!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B194")

    TalkEnd(0xFE)
    Return()

    # Function_24_A9CA end

    def Function_25_B198(): pass

    label("Function_25_B198")


    ChrTalk(
        0x14,
        (
            "#00600FThe death of Guy Bannings... Three years\x01",
            "have passed since then, and the real\x01",
            "truth has finally come to light, huh.\x02\x03",
            "#00603FAnd MacLaine bore that heavy burden to\x01",
            "this day.\x02\x03",
            "#00608F...What a coward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FHe bore everything\x01",
            "himself, cut a way out\x01",
            "and proceeded forward...\x02\x03",
            "#00008FThat might be why Arios\x01",
            "is so strong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#00603F...But, that strength is\x01",
            "misguided.\x02\x03",
            "#00608FHe should understand that...\x01",
            "That's why he opened the way\x01",
            "for all of you.\x02\x03",
            "#00600FAnyway, Bannings. With this,\x01",
            "you're over Guy's death,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F...Yes. I'd like to sort it out\x01",
            "once again, but I'm good for\x01",
            "now.\x02\x03",
            "#00001FThis is the final Barrier...\x01",
            "I've got to focus on overcoming\x01",
            "Lawyer Ian and Mariabell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#00604FGood then.\x02\x03",
            "#00602FTo resolve this incident\x01",
            "in a real sense... you\x01",
            "need only advance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FRight!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D9, 2)
    Return()

    # Function_25_B198 end

    def Function_26_B4D5(): pass

    label("Function_26_B4D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B4E3")
    Call(0, 11)
    Return()

    label("loc_B4E3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B505")
    Call(1, 56)
    TalkEnd(0xFE)
    Return()

    label("loc_B505")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B65F")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B533")
    RunExpression(0xA, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TurnDirection(0x8, 0x0, 0)

    label("loc_B533")


    ChrTalk(
        0x8,
        (
            "#12100F...That's right. Since\x01",
            "you're here, I'll give\x01",
            "you this.\x02",
        )
    )

    CloseMessageWindow()
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "[Abbas' Account]\x07\x00\x01",
            "obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x28, 0)
    OP_E4(0x3)

    ChrTalk(
        0x101,
        (
            "#00000FA "Pom!" account? You\x01",
            "play too, Abbas?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12102FOnly when I'm free.\x02\x03",
            "#12100FIf you feel like taking\x01",
            "me on, send me a\x01",
            "challenge.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B65A")
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B65A")

    Jump("loc_B69C")

    label("loc_B65F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B675")
    Call(1, 28)
    Jump("loc_B69C")

    label("loc_B675")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B68B")
    Call(1, 29)
    Jump("loc_B69C")

    label("loc_B68B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B69C")
    Call(1, 30)

    label("loc_B69C")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B6AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D3E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_B6FD")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",               # 0
            "Move Merkabah\x01",      # 1
            "Change Party\x01",       # 2
            "Cancel\x01",             # 3
        )
    )

    MenuEnd(0x0)
    Jump("loc_B73C")

    label("loc_B6FD")


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",               # 0
            "Move Merkabah\x01",      # 1
            "Cancel\x01",             # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B73C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B73C")

    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B75B"),
        (1, "loc_D079"),
        (2, "loc_D3BD"),
        (SWITCH_DEFAULT, "loc_D3D9"),
    )


    label("loc_B75B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_B8B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B844")

    ChrTalk(
        0x8,
        (
            "#12100FWe might need to stick with\x01",
            "Red Constellation for a\x01",
            "while...\x02\x03",
            "But right now, resolving\x01",
            "this incident is more\x01",
            "important.\x02\x03",
            "You should make sure you're\x01",
            "prepared before heading to\x01",
            "the final battle.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_B8B4")

    label("loc_B844")


    ChrTalk(
        0x8,
        (
            "#12100FAs knights, we will\x01",
            "fulfill our duties to\x01",
            "the end.\x02\x03",
            "You all should make sure\x01",
            "you're fully prepared.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B8B4")

    Jump("loc_D074")

    label("loc_B8B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 7)), scpexpr(EXPR_END)), "loc_B943")

    ChrTalk(
        0x8,
        (
            "#12100F...I'm sure those Vipers\x01",
            "are worried about Wald\x01",
            "too.\x02\x03",
            "They'll probably grab\x01",
            "him once danger has left\x01",
            "Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D074")

    label("loc_B943")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_BC63")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BADA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BA39")

    ChrTalk(
        0x8,
        (
            "#12100FThe airframe has sustained\x01",
            "light damage. Flight won't\x01",
            "be a problem.\x02\x03",
            "The ship can withdraw from\x01",
            "the Huge Tree at any time.\x02\x03",
            "If you would like to\x01",
            "withdraw from the Huge\x01",
            "Tree, just say the word.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_BAD5")

    label("loc_BA39")


    ChrTalk(
        0x8,
        (
            "#12100FFor the time being, it\x01",
            "seems the Merkabah has\x01",
            "avoided significant damage.\x02\x03",
            "If you would like to\x01",
            "withdraw from the Huge\x01",
            "Tree, just say the word.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BAD5")

    Jump("loc_BC5E")

    label("loc_BADA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BBBF")

    ChrTalk(
        0x8,
        (
            "#12100FThe airframe has sustained\x01",
            "light damage. Flight won't\x01",
            "be a problem.\x02\x03",
            "We were able to secure a\x01",
            "safe route into the Azure\x01",
            "Tree.\x02\x03",
            "If you would like to once\x01",
            "again go to the Huge Tree,\x01",
            "just say the word.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_BC5E")

    label("loc_BBBF")


    ChrTalk(
        0x8,
        (
            "#12100FFor the time being, it\x01",
            "seems the Merkabah has\x01",
            "avoided significant damage.\x02\x03",
            "If you would like to once\x01",
            "again go to the Huge Tree,\x01",
            "just say the word.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BC5E")

    Jump("loc_D074")

    label("loc_BC63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_BE41")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BD95")

    ChrTalk(
        0x8,
        (
            "#12100FAs for the meaning of the\x01",
            "appearance of the Azure Tree, even\x01",
            "the church has no idea as of yet.\x02\x03",
            "When we enter, we have no idea\x01",
            "what could happen.\x02\x03",
            "It's possible that it could fall\x01",
            "on Crossbell, but...\x02\x03",
            "If there's something you have to\x01",
            "do, that might take precedence.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_BE3C")

    label("loc_BD95")


    ChrTalk(
        0x8,
        (
            "#12100FAs for the meaning of the\x01",
            "appearance of the Azure Tree, even\x01",
            "the church has no idea as of yet.\x02\x03",
            "At any rate, make sure you're\x01",
            "prepared before entering it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BE3C")

    Jump("loc_D074")

    label("loc_BE41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_C2F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 5)), scpexpr(EXPR_END)), "loc_C0C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BFF5")

    ChrTalk(
        0x8,
        (
            "#12100FOne of the bells we must stop...\x01",
            "is in the Tower of Stargaze on the\x01",
            "outskirts of St. Ursula Byroad.\x02\x03",
            "But the Steel Maiden, one of the\x01",
            "Anguis, and her subordinates the\x01",
            "Stahlritter lie in wait for you.\x02\x03",
            "Overcoming them will be next to\x01",
            "impossible...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001F...We have to do it.\x01",
            "We'll search for our\x01",
            "chance at victory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12102FHmm. Well said. If you\x01",
            "have made up your mind,\x01",
            "then go.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_C0C4")

    label("loc_BFF5")


    ChrTalk(
        0x8,
        (
            "#12100FThe Steel Maiden, one of the Anguis,\x01",
            "and her subordinates the Stahlritter\x01",
            "lie in wait for you.\x02\x03",
            "Overcoming them will be next to\x01",
            "impossible... But if you are\x01",
            "determined to overcome them, then go.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C0C4")

    Jump("loc_C2F0")

    label("loc_C0C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C24E")

    ChrTalk(
        0x8,
        (
            "#12100FOur first destination is the Temple\x01",
            "of Moon... a middle age ruin in the\x01",
            "Mainz region.\x02\x03",
            "According to Old Man Jｶrg, Fool\x01",
            "Campanella, one of the enforcers, is\x01",
            "waiting for you there.\x02\x03",
            "He normally works behind the scenes,\x01",
            "and we have hardly any information on\x01",
            "him. ...He's a mysterious character.\x02\x03",
            "I don't know what he has in store for\x01",
            "you. Be ready for anything.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_C2F0")

    label("loc_C24E")


    ChrTalk(
        0x8,
        (
            "#12100FFool Campanella, one of the\x01",
            "enforcers, is waiting for\x01",
            "you at the Temple of Moon...\x02\x03",
            "I don't know what he has in\x01",
            "store for you. Be ready for\x01",
            "anything.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C2F0")

    Jump("loc_D074")

    label("loc_C2F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_C568")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C49E")

    ChrTalk(
        0x8,
        (
            "#12100FIt seems the State Guard and jaegers on the\x01",
            "ground are on high alert because Chairman\x01",
            "MacDowell has been taken from them.\x02\x03",
            "Under these conditions, I don't think we\x01",
            "can land the Merkabah anywhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FI see... In that case, I\x01",
            "think we should focus on the\x01",
            "plan at the booster site.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100FYes. All that's left is\x01",
            "choose the plan's start\x01",
            "time.\x02\x03",
            "Speak to me once you're\x01",
            "ready.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_C563")

    label("loc_C49E")


    ChrTalk(
        0x8,
        (
            "#12100FBecause of the high\x01",
            "alert, we can't land the\x01",
            "Merkabah anywhere.\x02\x03",
            "You should focus on\x01",
            "making the plan at the\x01",
            "booster site a success.\x02\x03",
            "I'm ready on my end.\x01",
            "Speak to me once you're\x01",
            "ready.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C563")

    Jump("loc_D074")

    label("loc_C568")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_C85D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C744")

    ChrTalk(
        0x8,
        (
            "#12100FOnce you arrive at Michelam,\x01",
            "interception by jaegers will begin\x01",
            "immediately.\x02\x03",
            "To avoid anti-aircraft weapons\x01",
            "fire, the Merkabah will temporarily\x01",
            "hide itself high in the sky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FOnce we land, we can't return until we\x01",
            "save Elie and Chairman MacDowell, huh.\x01",
            "This is sure to be a tough fight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100FYes. Most likely worse than\x01",
            "you're imagining.\x02\x03",
            "Equipment, orbments,\x01",
            "restoratives... You should make\x01",
            "sure they're all in order.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_C858")

    label("loc_C744")


    ChrTalk(
        0x8,
        (
            "#12100FOnce the fighting starts at Michelam, this\x01",
            "ship will temporarily hide itself high in the\x01",
            "sky to avoid anti-aircraft weapons fire.\x02\x03",
            "You won't be able to return to the ship during\x01",
            "this time. You should make sure your weapons,\x01",
            "orbments and restoratives are in order.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C858")

    Jump("loc_D074")

    label("loc_C85D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_CA7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C9EE")

    ChrTalk(
        0x8,
        (
            "#12100FThat reporter seems to be\x01",
            "going into the details of\x01",
            "this Merkabah and Wazy.\x02\x03",
            "...Man. It's\x01",
            "unprecedented to have a\x01",
            "journalist aboard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FW-Well... I'm sure she's\x01",
            "just curious. Is it\x01",
            "going to be all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100F...Well, it's fine. Wazy\x01",
            "gave permission, after\x01",
            "all.\x02\x03",
            "If the worst happens,\x01",
            "I'll have you take\x01",
            "responsibility.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00006F(W-Why me...)\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_CA77")

    label("loc_C9EE")


    ChrTalk(
        0x8,
        (
            "#12100FMan, it's unprecedented for\x01",
            "one involved in journalism\x01",
            "to come aboard...\x02\x03",
            "Well, Wazy gave permission,\x01",
            "so it can't be helped.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CA77")

    Jump("loc_D074")

    label("loc_CA7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_CBFA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CB53")

    ChrTalk(
        0x8,
        (
            "#12100FThe CGF resistance is\x01",
            "acting on a different\x01",
            "belief than Heiyue, huh...\x02\x03",
            "They have both risen in\x01",
            "revolt and left the\x01",
            "President's side.\x02\x03",
            "If you're going, maybe you\x01",
            "should hurry.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_CBF5")

    label("loc_CB53")


    ChrTalk(
        0x8,
        (
            "#12100FEven if they're the CGF, they won't\x01",
            "hold out against the State Guard and\x01",
            "jaegers' battle strength for long.\x02\x03",
            "If you're going, maybe you should\x01",
            "hurry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CBF5")

    Jump("loc_D074")

    label("loc_CBFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_CE93")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CDA9")

    ChrTalk(
        0x8,
        (
            "#12100FThe Heaven's Wheel the Merkabah uses\x01",
            "for its engine was originally a\x01",
            "flight-capable artifact vehicle...\x02\x03",
            "After the orbal revolution, we\x01",
            "improved the shape to its current form\x01",
            "with the help of the foundation.\x02\x03",
            "In addition, we have a small part in\x01",
            "development of tactical orbments.\x02\x03",
            "...But in the end, it is unofficial to\x01",
            "the common people. Careful that this\x01",
            "information does not leak outside.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_CE8E")

    label("loc_CDA9")


    ChrTalk(
        0x8,
        (
            "#12100FBoth this Merkabah and tactical\x01",
            "orbments were born out of a partnership\x01",
            "between the church and foundation...\x02\x03",
            "...In the end, it is unofficial to the\x01",
            "common people. Careful that this\x01",
            "information does not leak outside.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CE8E")

    Jump("loc_D074")

    label("loc_CE93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_D074")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CEAE")
    Call(1, 27)
    Jump("loc_D074")

    label("loc_CEAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CFDC")

    ChrTalk(
        0x8,
        (
            "#12100FWhen we need to go somewhere new, I need to\x01",
            "be on guard against the Aions per Wazy's\x01",
            "orders, but the current system is sufficient.\x02\x03",
            "There's no need to worry about us. You should\x01",
            "get your gear and orbments in order.\x02\x03",
            "Speak with me once you're ready to head to\x01",
            "the surface.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_D074")

    label("loc_CFDC")


    ChrTalk(
        0x8,
        (
            "#12100FThere's no need to worry\x01",
            "about us. You should get your\x01",
            "gear and orbments in order.\x02\x03",
            "Speak with me once you're\x01",
            "ready to head to the surface.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D074")

    Jump("loc_D3E3")

    label("loc_D079")

    FadeToDark(300, 0, -1)
    OP_0D()
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)), "loc_D3AE")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D19C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D0D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D197")
    Call(0, 39)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D192")
    OP_50(0x1E, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, -1)
    OP_0D()
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D192")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)), "loc_D183")
    FadeToDark(500, 0, -1)
    Sleep(500)
    EventBegin(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D173")
    Call(0, 6)
    Jump("loc_D176")

    label("loc_D173")

    Call(0, 5)

    label("loc_D176")

    Call(0, 7)
    TalkEnd(0xFE)
    EventEnd(0x6)
    Jump("loc_D192")

    label("loc_D183")

    FadeToBright(0, 0)
    TalkEnd(0xFE)
    EventEnd(0x6)
    Return()

    label("loc_D192")

    Jump("loc_D0D2")

    label("loc_D197")

    Jump("loc_D3A8")

    label("loc_D19C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D283")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D1B9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D27E")
    Call(0, 23)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D279")
    OP_50(0x1E, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, -1)
    OP_0D()
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D279")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)), "loc_D26A")
    FadeToDark(500, 0, -1)
    Sleep(500)
    EventBegin(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D25A")
    Call(0, 6)
    Jump("loc_D25D")

    label("loc_D25A")

    Call(0, 5)

    label("loc_D25D")

    Call(0, 7)
    TalkEnd(0xFE)
    EventEnd(0x6)
    Jump("loc_D279")

    label("loc_D26A")

    FadeToBright(0, 0)
    TalkEnd(0xFE)
    EventEnd(0x6)
    Return()

    label("loc_D279")

    Jump("loc_D1B9")

    label("loc_D27E")

    Jump("loc_D3A8")

    label("loc_D283")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D36A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D2A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D365")
    Call(0, 21)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D360")
    OP_50(0x1E, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, -1)
    OP_0D()
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D360")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)), "loc_D351")
    FadeToDark(500, 0, -1)
    Sleep(500)
    EventBegin(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D341")
    Call(0, 6)
    Jump("loc_D344")

    label("loc_D341")

    Call(0, 5)

    label("loc_D344")

    Call(0, 7)
    TalkEnd(0xFE)
    EventEnd(0x6)
    Jump("loc_D360")

    label("loc_D351")

    FadeToBright(0, 0)
    TalkEnd(0xFE)
    EventEnd(0x6)
    Return()

    label("loc_D360")

    Jump("loc_D2A0")

    label("loc_D365")

    Jump("loc_D3A8")

    label("loc_D36A")

    FadeToDark(500, 0, -1)
    Sleep(500)
    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D386")
    Call(0, 12)

    label("loc_D386")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D39D")
    Call(0, 6)
    Jump("loc_D3A0")

    label("loc_D39D")

    Call(0, 5)

    label("loc_D3A0")

    Call(0, 7)
    TalkEnd(0xFE)
    EventEnd(0x6)

    label("loc_D3A8")

    Return()

    label("loc_D3AE")

    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_D3E3")

    label("loc_D3BD")

    OP_32(0xFF, 0xF9, 0x0)
    PartySelect(0)
    Fade(500)
    OP_0D()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D3E3")

    label("loc_D3D9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D3E3")

    Jump("loc_B6AD")

    label("loc_D3E8")

    OP_60(0x0)
    TalkEnd(0xFE)
    Return()

    # Function_26_B4D5 end

    def Function_27_D3EF(): pass

    label("Function_27_D3EF")


    ChrTalk(
        0x8,
        (
            "#12100FA communication came in just now.\x01",
            "Merkabah No. 5 has successfully\x01",
            "shaken off the Aion.\x02\x03",
            "Sir Graham and his crew are\x01",
            "uninjured.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004FI see... That's a relief.\x02\x03",
            "#00005F...Come to think of it,\x01",
            "Abbas. Is it ok for you to\x01",
            "be away from the controls?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100FNo need to worry... I can control most of the\x01",
            "Merkabah's functions from this seat.\x02\x03",
            "And, because we are high in the sky above a\x01",
            "Gap in automatic pilot mode, there's no need\x01",
            "to sit in the cockpit.\x02\x03",
            "When we need to go somewhere new, I need to\x01",
            "be on guard against the Aions per Wazy's\x01",
            "orders, but the current system is sufficient.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI see... That's indeed\x01",
            "highly efficient.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100FAnyway, make sure you're\x01",
            "ready while you're\x01",
            "aboard.\x02\x03",
            "Speak with me once\x01",
            "you're ready to head to\x01",
            "the surface.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D6, 3)
    Return()

    # Function_27_D3EF end

    def Function_28_D6FC(): pass

    label("Function_28_D6FC")


    ChrTalk(
        0x8,
        (
            "#12100FUsing the airframe's armor\x01",
            "and our anti-shock field\x01",
            "as a bulldozer...\x02\x03",
            "The airframe has sustained\x01",
            "light damage. Flight won't\x01",
            "be a problem.\x02\x03",
            "The ship can withdraw from\x01",
            "the Huge Tree at any time.\x02\x03",
            "If you would like to\x01",
            "withdraw from the Huge\x01",
            "Tree, just say the word.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D6, 5)
    Return()

    # Function_28_D6FC end

    def Function_29_D814(): pass

    label("Function_29_D814")


    ChrTalk(
        0x8,
        (
            "#12100FIt seems Wald is out of the\x01",
            "way.\x02\x03",
            "...I've known him for two\x01",
            "years, ever since I infiltrated\x01",
            "Crossbell with Wazy...\x02\x03",
            "Wazy seemed to be enjoying\x01",
            "himself ever since we formed\x01",
            "the Testaments for cover.\x02\x03",
            "Although a Revache plot made it\x01",
            "dangerous for a time...\x02\x03",
            "To Wazy, Wald was a good\x01",
            "fighting partner, and even a\x01",
            "good friend.\x02\x03",
            "#12102FI'm sure Wald thinks the same\x01",
            "of Wazy, of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FT-They certainly did\x01",
            "work well together,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100FThe fact that Wazy held\x01",
            "back might have been a\x01",
            "component of the cause.\x02\x03",
            "Well, even if Wazy doesn't\x01",
            "say it, I know it's the\x01",
            "truth, but...\x02\x03",
            "...This conversation is\x01",
            "pointless. Don't say a\x01",
            "word of it to anyone else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00000FS-Sure, I understand.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D6, 6)
    Return()

    # Function_29_D814 end

    def Function_30_DADF(): pass

    label("Function_30_DADF")


    ChrTalk(
        0x8,
        (
            "#12100F...Just now, when you\x01",
            "were fighting the Divine\x01",
            "Blade...\x02\x03",
            "Radar detected a flying\x01",
            "object entering this\x01",
            "Shrine.\x02\x03",
            "It appears to be Red\x01",
            "Constellation's airship,\x01",
            "the Beowulf.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00005FHuh... It was all\x01",
            "right!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100FYes. It set down at another\x01",
            "site, and withdrew from the\x01",
            "Huge Tree a while ago.\x02\x03",
            "Most likely, they were here\x01",
            "to collect Ogre Rosso and\x01",
            "Bloody Shirley.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FI see... As an\x01",
            "policeman, I wanted to\x01",
            "question them, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100FWell, it can't be helped.\x01",
            "The standby team couldn't do\x01",
            "anything to stop them alone.\x02\x03",
            "That way of retreating is\x01",
            "characteristic of jaegers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FIt's possible we might\x01",
            "meet again someday...\x02\x03",
            "#00001F...But right now, we need\x01",
            "to focus on resolution of\x01",
            "this incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100FYes, exactly.\x02\x03",
            "You should make sure you're\x01",
            "prepared before heading to\x01",
            "the final battle.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D6, 7)
    Return()

    # Function_30_DADF end

    def Function_31_DE43(): pass

    label("Function_31_DE43")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_DF02")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x6E), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DE6E")
    Call(1, 52)
    TalkEnd(0xC)
    Return()

    label("loc_DE6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_DF02")

    ChrTalk(
        0xC,
        (
            "#01909FPlease take good care of\x01",
            "that charm, ok?\x02\x03",
            "I made it while praying for\x01",
            "everyone's safety, so I'm\x01",
            "sure it will be effective!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xC)
    Return()

    label("loc_DF02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E145")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E021")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x0, 0)
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_DFAD")
    Jump("loc_DFF7")

    label("loc_DFAD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_DFCD")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DFF7")

    label("loc_DFCD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DFED")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DFF7")

    label("loc_DFED")

    OP_52(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DFF7")

    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)
    Jump("loc_E031")

    label("loc_E021")

    RunExpression(0xA, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TurnDirection(0xC, 0x0, 0)

    label("loc_E031")


    ChrTalk(
        0xC,
        (
            "#01900FEveryone, do you know about\x01",
            "the orbal game "Pom!"?\x02\x03",
            "#01909FHaha. Actually, I started\x01",
            "playing it too. If you like,\x01",
            "exchange accounts with me.\x02",
        )
    )

    CloseMessageWindow()
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "[Fran's Account]\x07\x00\x01",
            "obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x27, 4)
    OP_E4(0x3)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E137")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E12E")
    ClearChrFlags(0xC, 0x10)

    label("loc_E12E")

    SetChrSubChip(0xC, 0x0)
    Jump("loc_E140")

    label("loc_E137")

    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E140")

    Jump("loc_F876")

    label("loc_E145")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_E30D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E160")
    Call(1, 33)
    Jump("loc_E308")

    label("loc_E160")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E27E")

    ChrTalk(
        0xC,
        (
            "#01904FEven enduring the anxiety\x01",
            "is akin to fighting\x01",
            "together with all of you...\x02\x03",
            "#01902FIn that case, I need do\x01",
            "only one thing.\x02\x03",
            "#01909FI, Fran Seeker... will pray\x01",
            "here for the safety of my\x01",
            "sister and everyone!\x02\x03",
            "Please absolutely,\x01",
            "absolutely return safely,\x01",
            "ok!?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_E308")

    label("loc_E27E")


    ChrTalk(
        0xC,
        (
            "#01909FI, Fran Seeker... will\x01",
            "pray here for the safety\x01",
            "of my sister and everyone!\x02\x03",
            "Please absolutely,\x01",
            "absolutely return safely,\x01",
            "ok!?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E308")

    Jump("loc_F876")

    label("loc_E30D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_E502")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E458")

    ChrTalk(
        0xC,
        (
            "#01900FThe interior of this Huge\x01",
            "Tree is more beautiful\x01",
            "than I expected.\x02\x03",
            "#01904FIf it wasn't a time like\x01",
            "this, I feel like I could\x01",
            "enjoy the scenery forever.\x02\x03",
            "#01905F...No, I mustn't. I\x01",
            "mustn't let down my guard,\x01",
            "right?\x02\x03",
            "#01909FAnyway, do your best\x01",
            "everyone! I'll be rooting\x01",
            "for you from here, ok?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_E4FD")

    label("loc_E458")


    ChrTalk(
        0xC,
        (
            "#01906FThe interior of this Huge\x01",
            "Tree is pretty, but I\x01",
            "mustn't let down my guard.\x02\x03",
            "#01909FAnyway, do your best\x01",
            "everyone! I'll be rooting\x01",
            "for you from here, ok?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E4FD")

    Jump("loc_F876")

    label("loc_E502")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_E670")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E5ED")

    ChrTalk(
        0xC,
        (
            "#01905FThe idea that we're\x01",
            "infiltrating that Huge Tree\x01",
            "is a little scary, but...\x02\x03",
            "#01901FI'm a police officer too.\x01",
            "It's times like these that\x01",
            "I have to show my courage!\x02\x03",
            "#01909FLloyd, let's do our best!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_E66B")

    label("loc_E5ED")


    ChrTalk(
        0xC,
        (
            "#01901FI'm a police officer too.\x01",
            "It's times like these that\x01",
            "I have to show my courage!\x02\x03",
            "#01909FLloyd, let's do our best!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E66B")

    Jump("loc_F876")

    label("loc_E670")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_E875")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E7BA")

    ChrTalk(
        0xC,
        (
            "#01900FIf we do something about the barrier\x01",
            "and the white Aion, we'll be able to\x01",
            "start invading the city, right?\x02\x03",
            "#01904FThe invalidity declaration likely\x01",
            "reached Chief Sergei and the others in\x01",
            "the city, so they might be on the move.\x02\x03",
            "#01909FAnyway, this is the final push! Do your\x01",
            "best, you guys!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_E870")

    label("loc_E7BA")


    ChrTalk(
        0xC,
        (
            "#01900FIf we do something about the barrier\x01",
            "and the white Aion, we'll be able to\x01",
            "start invading the city, right?\x02\x03",
            "#01909FAnyway, this is the final push! Do\x01",
            "your best, you guys!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E870")

    Jump("loc_F876")

    label("loc_E875")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_EC51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EB64")

    ChrTalk(
        0xC,
        (
            "#01904F(*furious typing*)\x02\x03",
            "Ah, ah... Test, test...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FFran, what are you\x01",
            "doing?\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x101, 0)
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E977")
    Jump("loc_E9C1")

    label("loc_E977")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E997")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E9C1")

    label("loc_E997")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E9B7")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E9C1")

    label("loc_E9B7")

    OP_52(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E9C1")

    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)

    ChrTalk(
        0xC,
        (
            "#01902FOh, Lloyd. I was just testing the\x01",
            "microphone and camera.\x02\x03",
            "We can send the picture and sound from\x01",
            "the Merkabah's monitor system, through\x01",
            "the orbal net, to screens everywhere.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0x0)

    ChrTalk(
        0xC,
        (
            "#01904F"This is Fran Seeker. I\x01",
            "love my big sis so\x01",
            "much!"\x02\x03",
            "#01909F...Yeah, the speech\x01",
            "recognition is good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009F(Haha, no matter the\x01",
            "situation, Fran calms\x01",
            "you down...)\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x1, 4)
    Jump("loc_EC4C")

    label("loc_EB64")


    ChrTalk(
        0xC,
        (
            "#01902FWe can send the picture and sound from\x01",
            "the Merkabah's monitor system, through\x01",
            "the orbal net, to screens everywhere.\x02\x03",
            "#01909FI have to carefully check everything\x01",
            "so that Chairman MacDowell's voice can\x01",
            "reach the citizens.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EC4C")

    Jump("loc_F876")

    label("loc_EC51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_EDC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EC6C")
    Call(1, 13)
    Jump("loc_EDC2")

    label("loc_EC6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ED65")

    ChrTalk(
        0xC,
        (
            "#01912FHaha. I'm really happy\x01",
            "that Noｱl is back.\x02\x03",
            "#01901FLloyd... Please take\x01",
            "good care of my sister!\x02\x03",
            "#01909FBecause I'm secretly\x01",
            "rooting for you too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(H-Hmm... I feel like\x01",
            "there's some kind of\x01",
            "misunderstanding.)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_EDC2")

    label("loc_ED65")


    ChrTalk(
        0xC,
        (
            "#01901FPlease take care of my\x01",
            "sister!\x02\x03",
            "#01909FBecause I'm secretly\x01",
            "rooting for you too!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EDC2")

    Jump("loc_F876")

    label("loc_EDC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_EF50")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EEEB")

    ChrTalk(
        0xC,
        (
            "#01908FWest Crossbell\x01",
            "Highway... Bellguard\x01",
            "Gate is there.\x02\x03",
            "#01903FMy sister's probably\x01",
            "there too...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xC)

    ChrTalk(
        0xC,
        (
            "#01906F*sigh*, I can't be doing\x01",
            "this. I have to pull\x01",
            "myself together!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F(Fran. As expected,\x01",
            "she's worried about\x01",
            "Noｱl...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_EF4B")

    label("loc_EEEB")


    ChrTalk(
        0xC,
        (
            "#01908FMy sister's probably at\x01",
            "Bellguard Gate...\x02\x03",
            "#01906F...I don't know what I\x01",
            "should do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EF4B")

    Jump("loc_F876")

    label("loc_EF50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_F65C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F47A")

    ChrTalk(
        0xC,
        (
            "#01908F...If my sister decides\x01",
            "to oppose us, I'll have\x01",
            "to choose sides, huh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FYeah... To be honest, this\x01",
            "isn't any normal situation.\x02\x03",
            "#00003FIf Noｱl has made up her\x01",
            "mind, then...\x02\x03",
            "#00008FThis chain of incidents\x01",
            "makes me feel like we might\x01",
            "have a chance, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01903F...Probably...\x02\x03",
            "#01901FWhen I was little, I think\x01",
            "my dad died and left a\x01",
            "stump.\x02\x03",
            "#01908F...He was accidently shot\x01",
            "by a rifle during a\x01",
            "Republic military exercise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FHuh!?\x02\x03",
            "Your dad died ten years\x01",
            "ago due to an\x01",
            ""accident", right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01906FI was still small and don't remember the\x01",
            "details, but...\x02\x03",
            "#01908FDuring a Republic military exercise, there was\x01",
            "an accidental firing, and the shot happened to\x01",
            "hit my dad in the CGF... That's what they said.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...So that's what\x01",
            "happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01903FBut Crossbell being in the position\x01",
            "it is in, naturally couldn't regard\x01",
            "the matter as serious...\x02\x03",
            "#01908FAnd in the end, it was seen and\x01",
            "dealt with as an "accident."\x02\x03",
            "My mom was sad, but seemed to\x01",
            "accept it from the start as a risk\x01",
            "of a dangerous job...\x02\x03",
            "#01903F...But probably, my sister hasn't\x01",
            "accepted it. Not even now, after\x01",
            "all this time...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00008F...That may very well be true.\x02\x03",
            "#00003F(The reason for Noｱl's strong\x01",
            "desire to protect Crossbell... I\x01",
            "feel like I understand it now...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DB, 7)
    Jump("loc_F657")

    label("loc_F47A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F5DF")

    ChrTalk(
        0xC,
        (
            "#01908F...Sorry. For getting\x01",
            "all serious all of a\x01",
            "sudden.\x02\x03",
            "#01903FA CGF member who objects\x01",
            "to the current State\x01",
            "Guard...\x02\x03",
            "#01900FRight now, we must think\x01",
            "of meeting up with them\x01",
            "as our top priority.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FYeah... That's right.\x02\x03",
            "#00000FFran, thanks for backing\x01",
            "us up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01909FYes, sir! I'll do\x01",
            "everything I can for you\x01",
            "guys!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_F657")

    label("loc_F5DF")


    ChrTalk(
        0xC,
        (
            "#01903FA CGF member who objects\x01",
            "to the current State\x01",
            "Guard...\x02\x03",
            "#01900FIf they're not my\x01",
            "sister, just who are\x01",
            "they?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F657")

    Jump("loc_F876")

    label("loc_F65C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_F876")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F677")
    Call(1, 32)
    Jump("loc_F876")

    label("loc_F677")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F7AB")

    ChrTalk(
        0xC,
        (
            "#01900FWhile searching for Gaps, we\x01",
            "incidentally found a reaction from a\x01",
            "dangerous monster.\x02\x03",
            "I will take responsibility for\x01",
            "sending the official support request\x01",
            "information to the terminal.\x02\x03",
            "#01909FIf you defeat one of them, don't\x01",
            "forget to report using the terminal\x01",
            "in the cabin, ok!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_F876")

    label("loc_F7AB")


    ChrTalk(
        0xC,
        (
            "#01900FI am still inexperienced, but I\x01",
            "will do my very best to support\x01",
            "you onboard the Merkabah!\x02\x03",
            "#01909FEveryone, if you defeat a wanted\x01",
            "monster, please report using the\x01",
            "terminal in the cabin, ok!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F876")

    TalkEnd(0xC)
    Return()

    # Function_31_DE43 end

    def Function_32_F87A(): pass

    label("Function_32_F87A")


    ChrTalk(
        0xC,
        (
            "#01900FThe Merkabah is equipped with an\x01",
            "information terminal like the one at\x01",
            "the Support Section.\x02\x03",
            "#01909FFrom now on, I'll take responsibility\x01",
            "for sending support request\x01",
            "information to that terminal!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FWow, is that so. Indeed\x01",
            "there was a terminal in\x01",
            "the cabin...\x02\x03",
            "#00003FCome to think of it, can\x01",
            "you get that kind of\x01",
            "information from anywhere?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01905FI was interested in it, so I asked Abbas...\x02\x03",
            "#01904FIt seems that, while searching for Gaps I\x01",
            "incidentally found a reaction from a\x01",
            "dangerous monster.\x02\x03",
            "#01902FThey aren't an obstacle to the Merkabah's\x01",
            "strategic actions, but if possible, I'd like\x01",
            "to use this function to deal with them ASAP.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FI see... Indeed, they'd be dangerous\x01",
            "if left alone, so we'll take care of\x01",
            "them if there's a spare moment.\x02\x03",
            "#00009FBut your information, Fran... It's\x01",
            "been a while, and it really takes me\x01",
            "back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01909FHaha, that's right! I'm somehow deeply\x01",
            "moved, too.\x02\x03",
            "#01906FIt might take a bit of time to get the data\x01",
            "from the cabin terminal, but...\x02\x03",
            "#01900FWhen we get back to HQ, I'm sure it will be\x01",
            "seen as the right thing to do, so please\x01",
            "deal with them as you have up until now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00004F...Yeah, that's right.\x02\x03",
            "#00000FThen, please take care\x01",
            "of us as our operator\x01",
            "once again, Fran.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        "#01909FRoger that!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D9, 3)
    Return()

    # Function_32_F87A end

    def Function_33_FD7C(): pass

    label("Function_33_FD7C")


    ChrTalk(
        0xC,
        (
            "#01903FThis is really, really the final\x01",
            "climax...\x02\x03",
            "#01908FIn times like these, I know it's\x01",
            "pathetic to only be able to wait\x01",
            "in a safe place like this...\x02\x03",
            "#01906FI've also thought many times\x01",
            "about fighting alongside you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003FNonsense. Battle with our enemies isn't just\x01",
            "about "fighting".\x02\x03",
            "#00000FIt's precisely because you and everyone else\x01",
            "are waiting for us that we're able to do our\x01",
            "best.\x02\x03",
            "No matter what kind of painful thing happens,\x01",
            "we will absolutely return from that place...\x01",
            "I believe that from the bottom of my heart.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01900FLloyd... I understand.\x02\x03",
            "#01909FI, Fran Seeker... will\x01",
            "pray here for the safety\x01",
            "of my sister and everyone!\x02\x03",
            "Please absolutely,\x01",
            "absolutely return safely,\x01",
            "ok!?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00002FYeah!\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D9, 3)
    Return()

    # Function_33_FD7C end

    def Function_34_10057(): pass

    label("Function_34_10057")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_101A7")

    ChrTalk(
        0x9,
        (
            "#02305FOh yeah... You guys have a "Pom!"\x01",
            "account, right?\x02\x03",
            "#02304FHehe. Since I'm here, I think I'll gift\x01",
            "you with Master Jona's account.\x02\x03",
            "#02309FIf you think you can win against me,\x01",
            "who's been involved since the development\x01",
            "stage, just go ahead and try.\x02",
        )
    )

    CloseMessageWindow()
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "[Jona's Account]\x07\x00\x01",
            "obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x27, 7)
    OP_E4(0x3)
    Jump("loc_10A35")

    label("loc_101A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_102F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_101C2")
    Call(1, 36)
    Jump("loc_102F4")

    label("loc_101C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10285")

    ChrTalk(
        0x9,
        (
            "#02306FTch, I'm telling you.\x01",
            "Don't worry people so\x01",
            "much...\x02\x03",
            "#02300FHmph, well... At least\x01",
            "do your best.\x02\x03",
            "#02309FGive me back my\x01",
            "leisurely orbal net life\x01",
            "that I had before.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_102F4")

    label("loc_10285")


    ChrTalk(
        0x9,
        (
            "#02300FWell... At least do your\x01",
            "best.\x02\x03",
            "#02309FGive me back my\x01",
            "leisurely orbal net life\x01",
            "that I had before.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_102F4")

    Jump("loc_10A35")

    label("loc_102F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_104F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10462")

    ChrTalk(
        0x9,
        (
            "#02301FIt feels like the tree is sucking\x01",
            "in an infinite amount of light...\x01",
            "It reminds me of the orbal net.\x02\x03",
            "#02303FCome to think of it, the Crois\x01",
            "family used the orbal net in\x01",
            "their plot, didn't they.\x02\x03",
            "The form of that Huge Tree itself\x01",
            "was related to their "project".\x02\x03",
            "#02302F...Well, I'll leave any further\x01",
            "analysis to you guys.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_104F0")

    label("loc_10462")


    ChrTalk(
        0x9,
        (
            "#02303FThe form of that Huge Tree\x01",
            "itself might be related to\x01",
            "their "project".\x02\x03",
            "#02302FWell, I'll leave any\x01",
            "further analysis to you\x01",
            "guys.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_104F0")

    Jump("loc_10A35")

    label("loc_104F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_10673")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_105E5")

    ChrTalk(
        0x9,
        (
            "#02303FIt would have been better if I\x01",
            "returned to my Geofront base,\x01",
            "but...\x02\x03",
            "#02302FRight now, this place is more\x01",
            "interesting. Since I'm here, I'll\x01",
            "stick with you guys 'til the end.\x02\x03",
            "#02304FHehe, be grateful.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_1066E")

    label("loc_105E5")


    ChrTalk(
        0x9,
        (
            "#02302FRight now, this place is more\x01",
            "interesting. Since I'm here, I'll\x01",
            "stick with you guys 'til the end.\x02\x03",
            "#02304FHehe, be grateful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1066E")

    Jump("loc_10A35")

    label("loc_10673")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_10882")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_107E1")

    ChrTalk(
        0x9,
        (
            "#02302FThe orbal net hacking went better\x01",
            "than I expected.\x02\x03",
            "#02306FIt's just, the wireless booster\x01",
            "circuit was completely cut off, so\x01",
            "we can't do it again.\x02\x03",
            "#02309F...Hehe. Well, whatever. Right now,\x01",
            "we've just gotta scare the hell out\x01",
            "of those guys in the tower.\x02\x03",
            "#02302FLater we've got to liberate\x01",
            "Crossbell City and retake my base!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_1087D")

    label("loc_107E1")


    ChrTalk(
        0x9,
        (
            "#02300FIt looks like there's a\x01",
            "strong opponent, but I'm\x01",
            "counting on you.\x02\x03",
            "#02309FWe've got to hurry and\x01",
            "liberate Crossbell City\x01",
            "and take back my base!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1087D")

    Jump("loc_10A35")

    label("loc_10882")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_10A35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1089D")
    Call(1, 35)
    Jump("loc_10A35")

    label("loc_1089D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10996")

    ChrTalk(
        0x9,
        (
            "#02306FAnyway, I've got to get back at\x01",
            "those guys for locking me up in\x01",
            "a place there's no terminal.\x02\x03",
            "#02310FEspecially that Mariabell lady!\x01",
            "I'll teach that demon a lesson!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(Looks like he bears\x01",
            "quite the grudge...)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_10A35")

    label("loc_10996")


    ChrTalk(
        0x9,
        (
            "#02302FI'm ready to start the hacking\x01",
            "whenever you are!\x02\x03",
            "#02309FJust you watch! Terminals\x01",
            "throughout Crossbell will broadcast\x01",
            "the invalidity declaration!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10A35")

    TalkEnd(0xFE)
    Return()

    # Function_34_10057 end

    def Function_35_10A39(): pass

    label("Function_35_10A39")


    ChrTalk(
        0x9,
        (
            "#02305FHey, are we starting the\x01",
            "operation yet?\x02\x03",
            "I'm ready to start the\x01",
            "hacking whenever you\x01",
            "are!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FWell someone's\x01",
            "excited...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#02304FHehe. It's finally time to get back\x01",
            "at those guys who locked me in a\x01",
            "place there's no terminal.\x02\x03",
            "#02302FJust you watch! Terminals\x01",
            "throughout Crossbell will broadcast\x01",
            "that old man's face and voice!\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#00003FChairman MacDowell, you\x01",
            "mean.\x02\x03",
            "#00001FJona, even in times like\x01",
            "these, you have to use\x01",
            "proper politeness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#02306FAh, enough already.\x01",
            "You're annoying as\x01",
            "always.\x02\x03",
            "#02302FIt's fine, so just start\x01",
            "the operation already!\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D9, 6)
    Return()

    # Function_35_10A39 end

    def Function_36_10C9D(): pass

    label("Function_36_10C9D")


    ChrTalk(
        0x9,
        (
            "#02300FLooks like we're getting\x01",
            "close to the end.\x02\x03",
            "#02303F...Umm, are you ok? It looks\x01",
            "like that Mariabell chick is\x01",
            "waiting for you, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FWow, how strange...\x01",
            "You're actually worried\x01",
            "about us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#02305FO-Of course I am! Who\x01",
            "isn't worried in this\x01",
            "whacked-out situation!?\x02\x03",
            "#02306FTch, whatever. Just when\x01",
            "I...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00009FHaha, my bad.\x02\x03",
            "#00000F...Thanks, Jona. We'll\x01",
            "definitely return\x01",
            "safely.\x02\x03",
            "I'm counting on you to\x01",
            "make sure we're ready to\x01",
            "withdraw anytime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x9,
        (
            "#02303FHmph, I know that\x01",
            "already. At least do\x01",
            "your best.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D9, 6)
    Return()

    # Function_36_10C9D end

    def Function_37_10EBF(): pass

    label("Function_37_10EBF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_10ED0")
    Jump("loc_11431")

    label("loc_10ED0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_10EDE")
    Jump("loc_11431")

    label("loc_10EDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_10EEC")
    Jump("loc_11431")

    label("loc_10EEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_11097")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11023")

    ChrTalk(
        0xF,
        (
            "#02103FThe mysterious society Ouroboros... I\x01",
            "heard they were behind the strange\x01",
            "phenomena that occurred in Liberl.\x02\x03",
            "#02101FThough they haven't showed themselves\x01",
            "as much as last time, we've got to\x01",
            "protect the important points...\x02\x03",
            "#02106F...Just what could their goal\x01",
            "possibly be?\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_11092")

    label("loc_11023")


    ChrTalk(
        0xF,
        (
            "#02103FThe society of\x01",
            "Ouroboros...\x02\x03",
            "#02101FTheir mystery only\x01",
            "expands. Just what is\x01",
            "their true objective?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11092")

    Jump("loc_11431")

    label("loc_11097")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_1126E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_111AA")

    ChrTalk(
        0xF,
        (
            "#02102FThe "invalidity declaration"\x01",
            "plan is finally assembled.\x02\x03",
            "Now that Chairman MacDowell's\x01",
            "statement is ready, all that's\x01",
            "left is to deliver it...\x02\x03",
            "#02106F...Oooh, I'm getting so\x01",
            "excited! I wonder if I should\x01",
            "do voice training on the deck.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_11269")

    label("loc_111AA")


    ChrTalk(
        0xF,
        (
            "#02102FNow that Chairman MacDowell's\x01",
            "statement is ready, all that's\x01",
            "left is to deliver it...\x02\x03",
            "#02106F...Oooh, I'm getting so\x01",
            "excited! I wonder if I should\x01",
            "do voice training on the deck.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11269")

    Jump("loc_11431")

    label("loc_1126E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_11431")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11289")
    Call(1, 38)
    Jump("loc_11431")

    label("loc_11289")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_113D1")

    ChrTalk(
        0xF,
        (
            "#02109FNow then, Wazy and Rixia. Let's continue\x01",
            "our interview!\x02\x03",
            "I'm just an interested person! Of course\x01",
            "I won't write an article about this, so\x01",
            "don't hold back and tell me everything!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        "#10706FR-Right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10409FMan. To think she loves\x01",
            "gossip this much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(W-Will they be all\x01",
            "right...?)\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_11431")

    label("loc_113D1")


    ChrTalk(
        0xF,
        (
            "#02105F...Wow, is that so!?\x02\x03",
            "#02109FAh, I just love that\x01",
            "kind of behind-the-\x01",
            "scenes stuff!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11431")

    TalkEnd(0xFE)
    Return()

    # Function_37_10EBF end

    def Function_38_11435(): pass

    label("Function_38_11435")


    ChrTalk(
        0xF,
        (
            "#02104FTo be able to interview\x01",
            "this amazing lineup on\x01",
            "this amazing airship...\x02\x03",
            "#02109FAh, it just tickles my\x01",
            "journalist's soul!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FG-Grace... You're not\x01",
            "going to write an article\x01",
            "about all this, are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02102FNot a chance! Don't worry! In the\x01",
            "end, this is just for personal\x01",
            "interest.\x02\x03",
            "#02104FI've got to sort out the material\x01",
            "I got from the resistance. I\x01",
            "won't write an article about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006FR-Right...\x02\x03",
            "#00005F...By the way, what details\x01",
            "did you get from the\x01",
            "resistance?\x02\x03",
            "#00003FI think it was something\x01",
            "about a problem that's\x01",
            "occurring in Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02106FHmm. I guess. It's a bit of a long\x01",
            "story, but...\x02\x03",
            "#02101FActually, ever since the day\x01",
            "independence was declared, our articles\x01",
            "have been subject to censorship.\x02\x03",
            "We haven't been able to publish any\x01",
            "opposition faction articles critical of\x01",
            "the President at all...\x02\x03",
            "#02106FOn top of that, our use of\x01",
            "communications equipment and coverage\x01",
            "conduct themselves are regulated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00001FHe's nothing if not\x01",
            "thorough...\x02\x03",
            "#00003F...Well, it's President\x01",
            "Dieter after all. He could\x01",
            "be capable of anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02103FWell, that kind of stuff is very\x01",
            "far from my idea of journalism, so\x01",
            "I can't go along with it.\x02\x03",
            "#02102FI ignored the notices and continued\x01",
            "my coverage, and the State Guard\x01",
            "finally caught wind of it.\x02\x03",
            "#02104FCrossbell City was getting to be a\x01",
            "tough place to be, so I went over\x01",
            "to the resistance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FSo that's how it went\x01",
            "down... You did well to\x01",
            "stay safe this whole time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xF,
        (
            "#02109FThat's because Reins arranged an\x01",
            "escape route for me. I'm glad I have\x01",
            "such a skilled junior.\x02\x03",
            "#02100F...Anyway, because of the situation,\x01",
            "I'll cooperate with the liberation\x01",
            "of Crossbell City in my own way!\x02\x03",
            "#02109FThe say, "The pen is mightier than\x01",
            "the sword," and I won't lose to the\x01",
            "likes of the State Guard!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00012FHaha... We may be working\x01",
            "together, but I'll be counting\x01",
            "on you when the time comes.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D9, 7)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x10)
    Return()

    # Function_38_11435 end

    def Function_39_11BB1(): pass

    label("Function_39_11BB1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_11DF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11BCF")
    Call(1, 41)
    Jump("loc_11DF0")

    label("loc_11BCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11D07")

    ChrTalk(
        0x12,
        (
            "#02503FI can't do anything more to be useful to you\x01",
            "all.\x02\x03",
            "#02500FAt least, as the one who gave the invalidity\x01",
            "declaration, I shall continue to think of how to\x01",
            "deal with its influence on Crossbell's future.\x02\x03",
            "As Chairman of state congress... And above all,\x01",
            "as a citizen living in Crossbell.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_11DF0")

    label("loc_11D07")


    ChrTalk(
        0x12,
        (
            "#02503FAs the one who gave the invalidity declaration,\x01",
            "I shall continue to think of how to deal with\x01",
            "its influence on Crossbell's future.\x02\x03",
            "#02500FAs Chairman of state congress... And above all,\x01",
            "as a citizen living in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11DF0")

    Jump("loc_12099")

    label("loc_11DF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_12099")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11E10")
    Call(1, 40)
    Jump("loc_12099")

    label("loc_11E10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11FC2")

    ChrTalk(
        0x12,
        (
            "#02500FI am ready to deliver the\x01",
            ""Independence Invalidity Declaration"\x01",
            "anytime.\x02\x03",
            "#02503FAll that's left is how the declaration\x01",
            "will go over with the people of\x01",
            "Crossbell... Everything depends on it.\x02\x03",
            "#02500FI cannot give a performance as great\x01",
            "as Dieter's, but I shall endeavor to\x01",
            "convey my own sincerity.\x02\x03",
            "I must do this, to get each and every\x01",
            "person living in Crossbell to think\x01",
            "about the future of this land.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_12099")

    label("loc_11FC2")


    ChrTalk(
        0x12,
        (
            "#02503FThe "Independence Invalidity\x01",
            "Declaration"... I shall endeavor to\x01",
            "convey my own sincerity.\x02\x03",
            "#02500FI must do this, to get each and\x01",
            "every person living in Crossbell to\x01",
            "think about the future of this land.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12099")

    TalkEnd(0xFE)
    Return()

    # Function_39_11BB1 end

    def Function_40_1209D(): pass

    label("Function_40_1209D")


    ChrTalk(
        0x101,
        (
            "#00000FChairman MacDowell...\x01",
            "Are you ready?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#02500FYes. I can deliver the\x01",
            ""Independence Invalidity\x01",
            "Declaration" anytime.\x02\x03",
            "The declaration itself\x01",
            "leaves nothing to be\x01",
            "desired.\x02\x03",
            "#02503FOf course, it itself is\x01",
            "a reflection of Dieter's\x01",
            "words.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00003F...Thank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#02503FNo... Thanks are unnecessary.\x02\x03",
            "#02501FAll that's left is how the declaration\x01",
            "will go over with the people of\x01",
            "Crossbell... Everything depends on it.\x02\x03",
            "I cannot give a performance as great\x01",
            "as Dieter's, but I shall endeavor to\x01",
            "convey my own sincerity.\x02\x03",
            "#02503FI must do this, to get each and every\x01",
            "person living in Crossbell to think\x01",
            "about the future of this land.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FRight... I'm counting on\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DA, 1)
    Return()

    # Function_40_1209D end

    def Function_41_1235D(): pass

    label("Function_41_1235D")


    ChrTalk(
        0x12,
        "#02503F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FChairman MacDowell?\x02",
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x12, 0x10)
    TurnDirection(0x12, 0x101, 0)
    OP_52(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1243C")
    Jump("loc_12486")

    label("loc_1243C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1245C")
    OP_52(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_12486")

    label("loc_1245C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1247C")
    OP_52(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_12486")

    label("loc_1247C")

    OP_52(0x12, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12486")

    OP_52(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x12, 0x10)

    ChrTalk(
        0x12,
        (
            "#02505F...Oh, sorry. I was just thinking.\x02\x03",
            "#02503FThe Crossbell independence\x01",
            "invalidity declaration... Although\x01",
            "it will break the current stalemate,\x01",
            "is it really the right thing to do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00008F............\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#02503F...Most likely, this problem\x01",
            "does not have a "right"\x01",
            "answer.\x02\x03",
            "#02500FBut, I feel the act of seeking\x01",
            "the right answer is important,\x01",
            "in and of itself.\x02\x03",
            "As Chairman of state\x01",
            "congress... And above all, as\x01",
            "a citizen living in Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...Thank you very much.\x02\x03",
            "#00000FNow that the first stage is\x01",
            "complete, I'm sure we'll be\x01",
            "helping you too, Mr. Chairman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x12,
        (
            "#02509FHaha, and I thank you for\x01",
            "it. I'll be counting on\x01",
            "you when that time comes.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x10)
    SetScenarioFlags(0x1DA, 2)
    Return()

    # Function_41_1235D end

    def Function_42_1275E(): pass

    label("Function_42_1275E")

    Call(1, 43)
    Return()

    # Function_42_1275E end

    def Function_43_12762(): pass

    label("Function_43_12762")

    TalkBegin(0x15)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1276F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13B0E")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",               # 0
            "Buy Equipment\x01",      # 1
            "Buy Items\x01",          # 2
            "Cancel\x01",             # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_127D4")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_127D4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12854")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_127F3")
    OP_AF(0xD8)
    Jump("loc_12845")

    label("loc_127F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_12803")
    OP_AF(0xD7)
    Jump("loc_12845")

    label("loc_12803")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_12813")
    OP_AF(0xD6)
    Jump("loc_12845")

    label("loc_12813")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_12823")
    OP_AF(0xD5)
    Jump("loc_12845")

    label("loc_12823")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_12833")
    OP_AF(0xD4)
    Jump("loc_12845")

    label("loc_12833")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_12843")
    OP_AF(0xD3)
    Jump("loc_12845")

    label("loc_12843")

    OP_AF(0xD2)

    label("loc_12845")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13B09")

    label("loc_12854")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12874")
    OP_AF(0xDC)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13B09")

    label("loc_12874")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12888")
    Jump("loc_13B09")

    label("loc_12888")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13B09")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_12AF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12A3A")

    ChrTalk(
        0x15,
        (
            "The time has come for the battle\x01",
            "for the fate of Crossbell to\x01",
            "reach its conclusion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "I don't know what would have\x01",
            "happened if Church personnel weren't\x01",
            "already gathered here, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "We've managed to reach this point\x01",
            "somehow. Because it's you all, I'm\x01",
            "sure everything will be all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Come now. Be sure everything\x01",
            "is in order before heading\x01",
            "for the final battle.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_12AF2")

    label("loc_12A3A")


    ChrTalk(
        0x15,
        (
            "We've managed to reach this point.\x01",
            "Because it's you all, I'm sure\x01",
            "everything will be all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Come now. Be sure everything\x01",
            "is in order before heading\x01",
            "for the final battle.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12AF2")

    Jump("loc_13B09")

    label("loc_12AF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_12CC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12C12")

    ChrTalk(
        0x15,
        (
            "It looks like the path within\x01",
            "this Huge Tree continues\x01",
            "quite deeply inside...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "If things get dangerous,\x01",
            "it'll be important to return\x01",
            "periodically and resupply.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "The resolution of this incident\x01",
            "depends on you. Proceed as\x01",
            "carefully as possible.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_12CBF")

    label("loc_12C12")


    ChrTalk(
        0x15,
        (
            "If things get dangerous,\x01",
            "it'll be important to return\x01",
            "periodically and resupply.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "The resolution of this incident\x01",
            "depends on you. Proceed as\x01",
            "carefully as possible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12CBF")

    Jump("loc_13B09")

    label("loc_12CC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_12EE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12E1B")

    ChrTalk(
        0x15,
        (
            "You probably want to finish your\x01",
            "preparations before heading to the Huge\x01",
            "Tree, but what we have here is limited.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "For now, you probably want the\x01",
            "various facilities throughout\x01",
            "Crossbell, and your friends as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "I don't know what's going to\x01",
            "happen... But you've got to make\x01",
            "sure you've got no regrets.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_12EE1")

    label("loc_12E1B")


    ChrTalk(
        0x15,
        (
            "For now, you probably want the\x01",
            "various facilities throughout\x01",
            "Crossbell, and your friends as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "I don't know what's going to\x01",
            "happen... But you've got to make\x01",
            "sure you've got no regrets.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12EE1")

    Jump("loc_13B09")

    label("loc_12EE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_130AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13000")

    ChrTalk(
        0x15,
        (
            "Jｶrg Rosenberg... To think a\x01",
            "man of Ouroboros would give\x01",
            "us valuable information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "As a knight, it's a problem if I\x01",
            "just believe him, but the\x01",
            "information does not seem untrue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "I'm sure there's\x01",
            "different kinds of people\x01",
            "within the society...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_130A6")

    label("loc_13000")


    ChrTalk(
        0x15,
        (
            "Jｶrg Rosenberg... I can't simply\x01",
            "believe him, but the information\x01",
            "does not seem like lies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "I'm sure there's\x01",
            "different kinds of people\x01",
            "within the society...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_130A6")

    Jump("loc_13B09")

    label("loc_130AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_13280")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_131D1")

    ChrTalk(
        0x15,
        (
            "Once Chairman MacDowell gives the\x01",
            "independence invalidity declaration, its\x01",
            "effect will be felt throughout Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "I think it will become easier\x01",
            "for the resistance forces hiding\x01",
            "throughout Crossbell to act.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "...I feel a turning\x01",
            "point is drawing near.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_1327B")

    label("loc_131D1")


    ChrTalk(
        0x15,
        (
            "Once Chairman MacDowell gives the\x01",
            "independence invalidity declaration, its\x01",
            "effect will be felt throughout Crossbell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "...I feel a turning\x01",
            "point is drawing near.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1327B")

    Jump("loc_13B09")

    label("loc_13280")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_13492")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_133CF")

    ChrTalk(
        0x15,
        (
            "The mission to save Chairman MacDowell...\x01",
            "It's not like I'm participating in the\x01",
            "raid, but even so, I'm nervous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Your opponents are a Red Constellation company...\x01",
            "A fight that can't be compared to any you've\x01",
            "faced before is waiting for you down there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Please everyone. Come\x01",
            "back safely to us.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_1348D")

    label("loc_133CF")


    ChrTalk(
        0x15,
        (
            "Your opponents are a Red Constellation company...\x01",
            "A fight that can't be compared to any you've\x01",
            "faced before is waiting for you down there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Please everyone. Come\x01",
            "back safely to us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1348D")

    Jump("loc_13B09")

    label("loc_13492")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_1360E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1357D")

    ChrTalk(
        0x15,
        (
            "It sure is lively\x01",
            "onboard the Merkabah.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Normally it's just the staff\x01",
            "of our order. Even commoners\x01",
            "coming aboard is rare...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Just keep this between\x01",
            "you and me, but I don't\x01",
            "think this is too bad.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_13609")

    label("loc_1357D")


    ChrTalk(
        0x15,
        (
            "Commoners hardly ever\x01",
            "even come aboard the\x01",
            "Merkabah, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Just keep this between\x01",
            "you and me, but I don't\x01",
            "think this is too bad.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13609")

    Jump("loc_13B09")

    label("loc_1360E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_137A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13726")

    ChrTalk(
        0x15,
        (
            "Yin, the legendary\x01",
            "assassin... Even I've\x01",
            "heard the rumors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "But to think she's that\x01",
            "girl... This world isn't\x01",
            "something to be understood.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "...Well, I think it must have been\x01",
            "quite a shock too when you learned\x01",
            "Sir Hemisphere was a clergyman.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_1379D")

    label("loc_13726")


    ChrTalk(
        0x15,
        (
            "Yin, the legendary\x01",
            "assassin... To think she\x01",
            "was that girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Haha, the world isn't\x01",
            "something to be\x01",
            "understood.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1379D")

    Jump("loc_13B09")

    label("loc_137A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_1396D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13872")

    ChrTalk(
        0x15,
        (
            "So you've reunited with your\x01",
            "friends, huh... It seems\x01",
            "this is only the beginning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Still, there's nothing like\x01",
            "being well prepared in advance.\x01",
            "Stay safe in the future too.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_13968")

    label("loc_13872")


    ChrTalk(
        0x15,
        (
            "Thanks to Sir Hemisphere's magic, we'll\x01",
            "be able to visit the hospital for a while\x01",
            "without contacting the State Guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "However, just because the beginning was\x01",
            "good, it doesn't mean you can let down\x01",
            "your guard. Be careful as you proceed.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13968")

    Jump("loc_13B09")

    label("loc_1396D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_13B09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13988")
    Call(1, 44)
    Jump("loc_13B09")

    label("loc_13988")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13A8C")

    ChrTalk(
        0x15,
        (
            "Anyhow, we have plenty of\x01",
            "equipment and accessories, so\x01",
            "let me know when you need them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "...*sigh*, but even so, Sir\x01",
            "Hemisphere has been manipulating\x01",
            "you for a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "While we were away, I\x01",
            "think Abbas really stuck\x01",
            "with him.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_13B09")

    label("loc_13A8C")


    ChrTalk(
        0x15,
        (
            "Sir Hemisphere has been\x01",
            "manipulating you for a\x01",
            "long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "While we were away, I\x01",
            "think Abbas really stuck\x01",
            "with him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13B09")

    Jump("loc_1276F")

    label("loc_13B0E")

    TalkEnd(0x15)
    Return()

    # Function_43_12762 end

    def Function_44_13B12(): pass

    label("Function_44_13B12")


    ChrTalk(
        0x15,
        (
            "I'm Squire Ventos. I\x01",
            "handle management of the\x01",
            "shipboard facilities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "We have plenty of equipment and\x01",
            "accessories, so let me know when\x01",
            "you need them before the operation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FManage, you said...\x01",
            "You're short staffed, so\x01",
            "it must be difficult.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "Well, Sir Hemisphere\x01",
            "suddenly restarted\x01",
            "operations...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "We could only get a\x01",
            "minimum number of\x01",
            "personnel onboard.\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0x15, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x10)
    TurnDirection(0xA, 0x15, 0)
    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_13D1E")
    Jump("loc_13D68")

    label("loc_13D1E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_13D3E")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13D68")

    label("loc_13D3E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13D5E")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13D68")

    label("loc_13D5E")

    OP_52(0xA, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13D68")

    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x10)

    ChrTalk(
        0xA,
        (
            "#10404FHaha. Anyway, it's an urgent\x01",
            "situation.\x02\x03",
            "#10409FAlthough it's been two years,\x01",
            "I'm glad to be working with\x01",
            "you again, guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x15,
        (
            "...*sigh*, anyway, I've\x01",
            "got to do my best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F(Hmm, looks like he's\x01",
            "having a hard time...)\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x0)
    SetScenarioFlags(0x1DA, 3)
    Return()

    # Function_44_13B12 end

    def Function_45_13E85(): pass

    label("Function_45_13E85")

    Call(1, 46)
    Return()

    # Function_45_13E85 end

    def Function_46_13E89(): pass

    label("Function_46_13E89")

    TalkBegin(0x16)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13E96")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14FB8")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Talk\x01",                   # 0
            "Modify/Synthesize\x01",      # 1
            "Cancel\x01",                 # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13EF5")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_13EF5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13F15")
    OP_AF(0xDD)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_14FB3")

    label("loc_13F15")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13F29")
    Jump("loc_14FB3")

    label("loc_13F29")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14FB3")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_140FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14047")

    ChrTalk(
        0x16,
        (
            "Now that you've come\x01",
            "this far, I can say\x01",
            "nothing more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "The enemy standing in your way is\x01",
            "strong, but I am sure the Goddess\x01",
            "of the Sky will guide you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Please, be careful. May\x01",
            "the protection of the\x01",
            "Goddess be with you...\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_140F5")

    label("loc_14047")


    ChrTalk(
        0x16,
        (
            "The enemy standing in your way is\x01",
            "strong, but I am sure the Goddess\x01",
            "of the Sky will guide you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Please, be careful. May\x01",
            "the protection of the\x01",
            "Goddess be with you...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_140F5")

    Jump("loc_14FB3")

    label("loc_140FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_142F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1423C")

    ChrTalk(
        0x16,
        (
            "The Sept-Terrion of Zero... What was\x01",
            "brought forth in that space was nothing\x01",
            "other than an act of a goddess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "...We've come together this\x01",
            "far, but the fate of this\x01",
            "ship is in your hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "I can't do much for you, but\x01",
            "please speak with me whenever you\x01",
            "need to prepare your orbments.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_142EE")

    label("loc_1423C")


    ChrTalk(
        0x16,
        (
            "We've come together this\x01",
            "far, but the fate of this\x01",
            "ship is in your hands.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "I can't do much for you, but\x01",
            "please speak with me whenever you\x01",
            "need to prepare your orbments.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_142EE")

    Jump("loc_14FB3")

    label("loc_142F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_14449")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_143E7")

    ChrTalk(
        0x16,
        (
            "...I feel the tension onboard this airship\x01",
            "is even greater than it was before the\x01",
            "Crossbell City liberation operation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "We've finally reached the final\x01",
            "stage... May the protection of\x01",
            "the Goddess be with you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_14444")

    label("loc_143E7")


    ChrTalk(
        0x16,
        (
            "We've finally reached the final\x01",
            "stage... May the protection of\x01",
            "the Goddess be with you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14444")

    Jump("loc_14FB3")

    label("loc_14449")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1463D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14577")

    ChrTalk(
        0x16,
        (
            "Merkabah No. 5, outside\x01",
            "Crossbell, just received\x01",
            "the invalidity declaration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Sir Graham and the others are\x01",
            "preparing to assist us with the\x01",
            "liberation of Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "To receive their assistance, we\x01",
            "need to do something about the\x01",
            "white Aion and the Barrier.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_14638")

    label("loc_14577")


    ChrTalk(
        0x16,
        (
            "Sir Graham and the others are\x01",
            "preparing to assist us with the\x01",
            "liberation of Crossbell City.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "To receive their assistance, we\x01",
            "need to do something about the\x01",
            "white Aion and the Barrier.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14638")

    Jump("loc_14FB3")

    label("loc_1463D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_14832")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14774")

    ChrTalk(
        0x16,
        (
            "When it's time to begin the\x01",
            "hacking, I'll be assisting as well\x01",
            "from that terminal over there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Orbal networks are outside my\x01",
            "expertise, but I can at least assist\x01",
            "with the Merkabah's system features...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "For our order's mission\x01",
            "as well, I will give\x01",
            "this everything I have.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_1482D")

    label("loc_14774")


    ChrTalk(
        0x16,
        (
            "Orbal networks are outside my\x01",
            "expertise, but I can at least assist\x01",
            "with the Merkabah's system features...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "For our order's mission\x01",
            "as well, I will give\x01",
            "this everything I have.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1482D")

    Jump("loc_14FB3")

    label("loc_14832")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_149AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14902")

    ChrTalk(
        0x16,
        (
            "It looks like there are\x01",
            "no State Guard forces at\x01",
            "Michelam, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Even with just jaegers,\x01",
            "it's sure to be\x01",
            "dangerous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Please, make sure your\x01",
            "orbments are fully\x01",
            "ready.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_149A8")

    label("loc_14902")


    ChrTalk(
        0x16,
        (
            "It looks like State Guard forces\x01",
            "aren't at Michelam, but it's sure to\x01",
            "be dangerous even with just jaegers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Please, make sure your\x01",
            "orbments are fully\x01",
            "ready.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_149A8")

    Jump("loc_14FB3")

    label("loc_149AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_14B9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14AED")

    ChrTalk(
        0x16,
        (
            "That Berserker rifle Randy\x01",
            "has... It seems it hides\x01",
            "considerable firepower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "If Red Constellation, one of the strongest jaeger\x01",
            "corps on the continent, has showed up as our\x01",
            "opponents, things will be pretty difficult...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Just one look at that\x01",
            "weapon, and I understand\x01",
            "that somehow.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_14B97")

    label("loc_14AED")


    ChrTalk(
        0x16,
        (
            "That Berserker rifle Randy\x01",
            "has... It seems it hides\x01",
            "considerable firepower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "I understand what it means\x01",
            "to say Red Constellation has\x01",
            "turned up as our opponents.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14B97")

    Jump("loc_14FB3")

    label("loc_14B9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_14D8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14CE0")

    ChrTalk(
        0x16,
        (
            "You need a lot of faith to\x01",
            "oppose a large organization\x01",
            "like the State Guard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "They can't even resupply properly\x01",
            "and, in a way, it's like they're\x01",
            "betraying their former comrades.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "I don't know who the resistance leader\x01",
            "is, they're certain to be someone with\x01",
            "spirit and a strong heart.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_14D87")

    label("loc_14CE0")


    ChrTalk(
        0x16,
        (
            "To oppose the State\x01",
            "Guard, you need a lot of\x01",
            "faith.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "I don't know who the resistance leader\x01",
            "is, they're certain to be someone with\x01",
            "spirit and a strong heart.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14D87")

    Jump("loc_14FB3")

    label("loc_14D8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_14F1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14EAE")

    ChrTalk(
        0x16,
        (
            "Please don't enter that\x01",
            "engine room no matter\x01",
            "what happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "There's important things\x01",
            "that can't be shown to\x01",
            "commoners in there.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 4)), scpexpr(EXPR_END)), "loc_14E86")

    ChrTalk(
        0x101,
        (
            "#00005F(Could it be the Heaven's\x01",
            "Wheel artifact Abbas\x01",
            "mentioned earlier?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14EA6")

    label("loc_14E86")


    ChrTalk(
        0x101,
        "#00005F(What could it be?)\x02",
    )

    CloseMessageWindow()

    label("loc_14EA6")

    SetScenarioFlags(0x2, 2)
    Jump("loc_14F19")

    label("loc_14EAE")


    ChrTalk(
        0x16,
        (
            "I've got to perform\x01",
            "maintenance in the\x01",
            "engine room pretty soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "...Please don't peek\x01",
            "inside, ok?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14F19")

    Jump("loc_14FB3")

    label("loc_14F1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_14FB3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14F39")
    Call(1, 47)
    Jump("loc_14FB3")

    label("loc_14F39")


    ChrTalk(
        0x16,
        (
            "...Now that the society has\x01",
            "showed themselves, our order\x01",
            "cannot let this incident pass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "Let's both do our best.\x02",
    )

    CloseMessageWindow()

    label("loc_14FB3")

    Jump("loc_13E96")

    label("loc_14FB8")

    TalkEnd(0x16)
    Return()

    # Function_46_13E89 end

    def Function_47_14FBC(): pass

    label("Function_47_14FBC")


    ChrTalk(
        0x16,
        (
            "You're from the Crossbell\x01",
            "Police's Special Support\x01",
            "Section, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "I'm Juno, in charge of\x01",
            "the engine room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Just leave your quartz\x01",
            "synthesis and tactical\x01",
            "orbment modifications to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FWow... A squire can even\x01",
            "do that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        (
            "Haha. I have confidence in\x01",
            "myself when it comes to\x01",
            "tasks requiring dexterity.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    ChrTalk(
        0x16,
        (
            "...Now that the society has\x01",
            "showed themselves, our order\x01",
            "cannot let this incident pass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x16,
        "Let's both do our best.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FRight... I'll be\x01",
            "counting on you.\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DA, 4)
    Return()

    # Function_47_14FBC end

    def Function_48_151C6(): pass

    label("Function_48_151C6")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1KNap Room\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "Rest\x01",        # 0
            "Cancel\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15311")
    EventBegin(0x2)
    Fade(500)
    OP_68(2040, 1000, -91940, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x101, 1300, 0, -92030, 90)
    OP_0D()
    Sound(100, 0, 100, 0)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x0, 0xA, 0x1, 0x8)
    Sleep(500)

    def lambda_1527C():
        OP_95(0xFE, 4300, 0, -92030, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1527C)
    Sleep(1000)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    Sound(13, 0, 100, 0)
    OP_32(0xFF, 0xFF, 0x0)
    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    OP_70(0x3, 0x0)
    OP_68(1300, 1000, -92030, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x101, 1300, 0, -92030, 270)
    SetChrSubChip(0x101, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    EventEnd(0x3)

    label("loc_15311")

    TalkEnd(0xFF)
    Return()

    # Function_48_151C6 end

    def Function_49_15315(): pass

    label("Function_49_15315")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1532B")
    OP_C9(0x0, 0x4)
    OP_C9(0x0, 0x100)

    label("loc_1532B")

    OP_E5(0xA)
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_E5(0x5)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_15344")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_158FE")
    RunExpression(0x5, (scpexpr(EXPR_EXEC_OP, "OP_E5(0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_END)),
        (0, "loc_1537D"),
        (1, "loc_153AC"),
        (2, "loc_158E2"),
        (3, "loc_158EA"),
        (SWITCH_DEFAULT, "loc_158F9"),
    )


    label("loc_1537D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1539C")
    OP_2B(0x9A, 0x9B, 0x9C, 0x96, 0x97, 0x98, 0x99, 0xFFFF)
    Jump("loc_153A7")

    label("loc_1539C")

    OP_2B(0x96, 0x97, 0x98, 0x99, 0xFFFF)

    label("loc_153A7")

    Jump("loc_158F9")

    label("loc_153AC")

    SetMapFlags(0x40000000)
    OP_E5(0x7)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1549D")
    SetChrName("Announcement")

    AnonymousTalk(
        0xFF,
        (
            "This is Crossbell\x01",
            "Police.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E5(0x4)"), scpexpr(EXPR_END)), "loc_15475")

    AnonymousTalk(
        0xFF,
        (
            "I will receive your\x01",
            "report.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x8, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E5(0xC)
    SetChrName("Announcement")

    AnonymousTalk(
        0xFF,
        (
            "Report processing,\x01",
            "complete. Thank you for\x01",
            "your hard work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15498")

    label("loc_15475")


    AnonymousTalk(
        0xFF,
        (
            "There no reportable\x01",
            "requests.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15498")

    Jump("loc_158D4")

    label("loc_1549D")

    SetChrName("Receptionist Fran")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_154F4")
    Sound(3062, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            "Yes, this is Crossbell\x01",
            "Poliiice!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15529")

    label("loc_154F4")

    Sound(3061, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            "Everyone, thank you for\x01",
            "your hard wooork.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15529")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E5(0x4)"), scpexpr(EXPR_END)), "loc_157C4")
    Sound(3067, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        (
            "Then, I'll receive your\x01",
            "report, okaaay?\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x8, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E5(0xC)
    Jc((scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1572A")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_END)),
        (14, "loc_155AA"),
        (13, "loc_155F7"),
        (12, "loc_15640"),
        (SWITCH_DEFAULT, "loc_15685"),
    )


    label("loc_155AA")

    Sound(3075, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        (
            "1st Class!── Lloyd,\x01",
            "you're too amazing!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15685")

    label("loc_155F7")

    Sound(3074, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        (
            "2nd Class!── Lloyd,\x01",
            "you're amazing!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15685")

    label("loc_15640")

    Sound(3073, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        (
            "3rd Class!── Lloyd, you\x01",
            "did it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15685")

    label("loc_15685")

    Sound(3076, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        (
            "I will immediately send\x01",
            "over your special item!\x02",
        )
    )

    CloseMessageWindow()
    Sound(3077, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            "Thank you for your hard\x01",
            "wooork! I hope to be\x01",
            "working with you agaaain.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_157BC")

    label("loc_1572A")

    Sound(3078, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        (
            "That's all for your\x01",
            "report, right?\x02",
        )
    )

    CloseMessageWindow()
    Sound(3079, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            "Then, please contact me\x01",
            "again the next time you\x01",
            "complete a requeeest.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_157BC")

    SetScenarioFlags(0x2, 4)
    Jump("loc_158D4")

    label("loc_157C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_15849")
    Sound(3063, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        (
            "Oh... Didn't you just\x01",
            "report?\x02",
        )
    )

    CloseMessageWindow()
    Sound(3064, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            "Please do it again when\x01",
            "you complete a request.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_158D4")

    label("loc_15849")

    Sound(3065, 255, 100, 0)
    SetChrName("Receptionist Fran")

    AnonymousTalk(
        0xFF,
        (
            "Oh... It seems you don't\x01",
            "have any requests you\x01",
            "can repooort.\x02",
        )
    )

    CloseMessageWindow()
    Sound(3066, 255, 100, 0)

    AnonymousTalk(
        0xFF,
        (
            "Please, let's work\x01",
            "together agaaain.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_158D4")

    OP_57(0x0)
    OP_E5(0x8)
    ClearMapFlags(0x40000000)
    Jump("loc_158F9")

    label("loc_158E2")

    Call(1, 50)
    Jump("loc_158F9")

    label("loc_158EA")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_158F9")

    label("loc_158F9")

    Jump("loc_15344")

    label("loc_158FE")

    OP_E5(0x6)
    OP_C9(0x1, 0x4)
    OP_C9(0x1, 0x100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1593B")
    OP_E5(0xB)
    TalkEnd(0xFF)
    Call(1, 51)
    Return()

    label("loc_1593B")

    FadeToBright(1000, 0)
    OP_0D()
    OP_E5(0xB)
    TalkEnd(0xFF)
    Return()

    # Function_49_15315 end

    def Function_50_1594B(): pass

    label("Function_50_1594B")

    OP_E5(0x6)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 3)), scpexpr(EXPR_END)), "loc_1596D")
    SetScenarioFlags(0x2A, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1596D")
    ClearScenarioFlags(0x2A, 0)

    label("loc_1596D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 4)), scpexpr(EXPR_END)), "loc_1598A")
    SetScenarioFlags(0x2A, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1598A")
    ClearScenarioFlags(0x2A, 1)

    label("loc_1598A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 5)), scpexpr(EXPR_END)), "loc_159A7")
    SetScenarioFlags(0x2A, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_159A7")
    ClearScenarioFlags(0x2A, 2)

    label("loc_159A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 6)), scpexpr(EXPR_END)), "loc_159C4")
    SetScenarioFlags(0x2A, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_159C4")
    ClearScenarioFlags(0x2A, 3)

    label("loc_159C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 7)), scpexpr(EXPR_END)), "loc_159E1")
    SetScenarioFlags(0x2A, 4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_159E1")
    ClearScenarioFlags(0x2A, 4)

    label("loc_159E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 0)), scpexpr(EXPR_END)), "loc_159FE")
    SetScenarioFlags(0x2A, 5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_159FE")
    ClearScenarioFlags(0x2A, 5)

    label("loc_159FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 1)), scpexpr(EXPR_END)), "loc_15A0A")
    SetScenarioFlags(0x2A, 6)

    label("loc_15A0A")

    OP_24(0x1F2)
    RunExpression(0x9, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x10, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1F()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15A4F")
    Sound(498, 1, 50, 0)
    Jump("loc_15A55")

    label("loc_15A4F")

    Sound(498, 1, 100, 0)

    label("loc_15A55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15A85")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_15A85")

    Return()

    # Function_50_1594B end

    def Function_51_15A86(): pass

    label("Function_51_15A86")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrChipByIndex(0xB, 0x12)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0x8, 0x1A)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0xC, 0x1B)
    SetChrSubChip(0xC, 0x0)
    OP_4B(0xB, 0xFF)
    OP_4B(0x8, 0xFF)
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 0)), scpexpr(EXPR_END)), "loc_15AEF")
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    OP_4B(0x9, 0xFF)
    SetChrPos(0x9, 102700, 0, -102930, 180)

    label("loc_15AEF")

    OP_68(102970, 1000, -104740, 0)
    MoveCamera(40, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(14560, 0)
    SetChrPos(0x101, 103020, 100, -105800, 90)
    SetChrPos(0xB, 101590, 0, -105440, 90)
    SetChrPos(0xC, 101470, 0, -104110, 135)
    SetChrPos(0x8, 103000, 0, -104100, 180)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(
        0xB,
        (
            "#00205FOh...\x02\x03",
            "#00204FIt looks like you've won\x01",
            "against all "Pom!"\x01",
            "opponents, Lloyd.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#01905FWow, really!?\x02\x03",
            "#01909FThat Lloyd for you...\x01",
            "He's too amazing!!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 0)), scpexpr(EXPR_END)), "loc_15C4A")

    ChrTalk(
        0x9,
        (
            "#02302FHeh, that's right.\x01",
            "You're pretty good.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15C4A")

    SetChrSubChip(0x101, 0x1)

    ChrTalk(
        0x101,
        (
            "#00009FHaha, thanks. I just got\x01",
            "lucky, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100FNo. In puzzle games like that,\x01",
            "luck isn't the primary factor\x01",
            "that determines the winner.\x02\x03",
            "#12102FBannings, you are a true "Pom!\x01",
            "Master".\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00012F...T-Thank you for that.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xF0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15F3F")

    ChrTalk(
        0x8,
        (
            "#12100FHmm... That's right.\x02\x03",
            "If you like, please take\x01",
            "this.\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x0, 0x8, 0x0, 0x1F4, 0x5DC, 0x0)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xF0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0xF0, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x8,
        (
            "#12100FIt's a forbidden master quartz, jointly\x01",
            "developed by the church and Epstein\x01",
            "Foundation using ancient techniques.\x02\x03",
            "Being it too powerful and difficult to\x01",
            "handle it's something we hesitated to\x01",
            "use, but...\x02\x03",
            "#12102FBecause it is you, I'm sure you'll\x01",
            "handle it correctly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FSure, understood. I'll\x01",
            "put it to good use,\x01",
            "then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16018")

    label("loc_15F3F")


    ChrTalk(
        0x8,
        (
            "#12100FHmm... That's right.\x02\x03",
            "#12102FI'll give you this as a\x01",
            "prize.\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x0, 0x8, 0x0, 0x1F4, 0x5DC, 0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x67),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x67, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(500)

    ChrTalk(
        0x101,
        (
            "#00000FHaha, thanks. I'll put\x01",
            "it to good use.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_16018")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x2A, 7)
    OP_E0(0x35, 0x0)
    OP_E0(0x80, 0x0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x4)
    OP_D7(0x1E)
    EventEnd(0x5)
    SetScenarioFlags(0x24, 3)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_51_15A86 end

    def Function_52_1604A(): pass

    label("Function_52_1604A")

    EventBegin(0x0)
    Fade(500)
    OP_68(4130, -1100, 7060, 0)
    MoveCamera(47, 40, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(14590, 0)
    SetChrPos(0x101, 4000, -1500, 5730, 315)
    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x101, 0)
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_16121")
    Jump("loc_1616B")

    label("loc_16121")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_16141")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1616B")

    label("loc_16141")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16161")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1616B")

    label("loc_16161")

    OP_52(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1616B")

    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)
    OP_0D()

    ChrTalk(
        0xC,
        (
            "#6P#01905FLloyd... You look tired\x01",
            "somehow.\x02\x03",
            "Are you all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00005FYeah... In a manner of\x01",
            "speaking.\x02\x03",
            "#00003FI might be tired just\x01",
            "because a lot of things\x01",
            "happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#01906FUmm, please don't push\x01",
            "yourself too hard, ok?\x02\x03",
            "#01908FWhen I think what would happen\x01",
            "if you or my sister died... I\x01",
            "get really scared, y'know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00000FYeah, thanks. I'll be\x01",
            "careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#01901FJust being careful isn't enough!\x01",
            "You've got to get proper rest in\x01",
            "times like these!\x02\x03",
            "#01902FIf you like, shall I give you a\x01",
            "massage?\x02\x03",
            "#01909FIf I violently press the pressure\x01",
            "points affecting fatigue, you'll\x01",
            "get better like bam, you knooow?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00006F(T-That looks incredibly\x01",
            "painful, somehow...)\x02\x03",
            "#00002FU-Umm... I'm good. I\x01",
            "appreciate the thought.\x02\x03",
            "#00009FI feel refreshed just\x01",
            "talking to you somehow,\x01",
            "Fran.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#01905FHuh? ...R-Really?\x02\x03",
            "#01909FEhehe... I'm happy to\x01",
            "hear you say that.\x02\x03",
            "#01904FAs operator, it's my\x01",
            "duty to cheer up all of\x01",
            "you, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00009FHaha. I think this might be your\x01",
            "calling.\x02\x03",
            "#00004FAnd you don't even know how many\x01",
            "times your smile has healed us\x01",
            "through the terminal screen...\x02\x03",
            "#00000FAnd at HQ as well, I am sure are\x01",
            "many people guided by you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#01906FOoh. If you say that\x01",
            "much, I'll get all\x01",
            "embarrassed...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xC)

    ChrTalk(
        0xC,
        (
            "#6P#01904FBut you're right. I want\x01",
            "you to do your best from\x01",
            "here on out, ok Lloyd?\x02\x03",
            "#01902FIf you like, please take\x01",
            "this.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x39E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            " obtained.\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x39E, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    ChrTalk(
        0x101,
        (
            "#11P#00005FYou're giving this... to\x01",
            "me?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 4)), scpexpr(EXPR_END)), "loc_16913")

    ChrTalk(
        0xC,
        (
            "#6P#01909FYes, please take it.\x02\x03",
            "#01904FI mean, you might be my\x01",
            "brother-in-law in the\x01",
            "future...\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#11P#00011FW-Whaaat!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xC,
        (
            "#6P#01909FMuhuhu... If you need\x01",
            "info on my sister, I\x01",
            "know everything~.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        (
            "#11P#00012F(O-Okay, I give up. I'm\x01",
            "sure she saw the whole\x01",
            "thing...)\x02\x03",
            "#00000F...Umm, then I'll put it\x01",
            "to good use.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_169BD")

    label("loc_16913")


    ChrTalk(
        0xC,
        (
            "#6P#01909FYes, please take it.\x02\x03",
            "I made it while praying for\x01",
            "everyone's safety, so I'm\x01",
            "sure it will be effective!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#11P#00009FHaha, then I'll put it\x01",
            "to good use.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_169BD")


    ChrTalk(
        0xC,
        "#6P#01909FEhehe, take care~.\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x1D9, 4)
    SetScenarioFlags(0x1, 5)
    SetChrSubChip(0xC, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16A06")
    OP_E0(0x34, 0x0)

    label("loc_16A06")

    EventEnd(0x5)
    Return()

    # Function_52_1604A end

    def Function_53_16A09(): pass

    label("Function_53_16A09")

    EventBegin(0x0)
    Fade(500)
    OP_68(97920, 1000, 600, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15320, 0)
    SetChrPos(0x101, 97510, 0, -530, 0)
    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x14, 0x10)
    TurnDirection(0x14, 0x101, 0)
    OP_52(0x14, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_16AE0")
    Jump("loc_16B2A")

    label("loc_16AE0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_16B00")
    OP_52(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_16B2A")

    label("loc_16B00")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16B20")
    OP_52(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_16B2A")

    label("loc_16B20")

    OP_52(0x14, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_16B2A")

    OP_52(0x14, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x14, 0x10)
    OP_0D()

    ChrTalk(
        0x14,
        (
            "#5P#00603FHmm...\x02\x03",
            "#00600F...Bannings, you've\x01",
            "grown a bit.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(
        0x101,
        "#12P#00005FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5P#00603FI've come with you all this far,\x01",
            "but...\x02\x03",
            "Your investigation and reasoning\x01",
            "skills are sound. I'll call you\x01",
            "green no longer.\x02\x03",
            "You still haven't reached the\x01",
            "level of Guy or MacLaine when\x01",
            "they were on active duty, but...\x02\x03",
            "#00602FHmph. It was worth looking after\x01",
            "you as a detective first class.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x101,
        (
            "#12P#00012FU-Umm... What's this all\x01",
            "of a sudden?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        "#5P#00603FJust shut up and listen.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#12P#00006FY-Yes, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5P#00600F...I just name-dropped Guy and\x01",
            "MacLaine, but I won't tell you to\x01",
            "be a detective like they were.\x02\x03",
            "You have your own character. By\x01",
            "growing that, you can become an\x01",
            "excellent detective.\x02\x03",
            "#00604FFrom now on, you should work to\x01",
            "find your own goal as a\x01",
            "detective.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    ChrTalk(
        0x14,
        (
            "#5P#00605F...What, you got a\x01",
            "problem with that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00011FN-No... I'm just\x01",
            "surprised.\x02\x03",
            "#00006FIt's not like you to\x01",
            "have such a high opinion\x01",
            "of me, Detective Dudley.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5P#00603FWhat will happen to the State Guard\x01",
            "depends on how things unfold, but the\x01",
            "police will continue.\x02\x03",
            "#00600FWhen this chain of events concludes,\x01",
            "I'm sure at least you will return to\x01",
            "the police.\x02\x03",
            "To prepare you for that, I just thought\x01",
            "I'd give you some advice as the\x01",
            "detective in charge of Section One.\x02\x03",
            "#00603FThat's all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00000FIs that so...\x02\x03",
            "#00004F...Thank you very much.\x02\x03",
            "#00002FI'll work hard to live\x01",
            "up to your expectations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x14,
        (
            "#5P#00606FHmph, don't misunderstand.\x02\x03",
            "Everything I've told you is just based\x01",
            "on analysis and objective fact.\x02\x03",
            "#00600FAt the end of the day, we can't move on\x01",
            "to the next thing until we resolve this\x01",
            "incident and seize the truth of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#12P#00012F(Haha. As always, he\x01",
            "can't be honest with\x01",
            "himself, huh...)\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    ChrTalk(
        0x14,
        (
            "#5P#00601F...What's that grin on\x01",
            "your face?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    ChrTalk(
        0x101,
        "#12P#00011FN-No, it's nothing!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_172F9")
    Jump("loc_173A6")

    label("loc_172F9")

    Sleep(500)
    Sound(517, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "Lloyd and Dudley learned\x01",
            "Hearts of Iron Ⅱ.\x07\x00\x02",
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
            "Lloyd and Dudley's\x01",
            "Hearts of Iron has been\x01",
            "strengthened.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddCraft(0x9, 0x1AA)
    AddCraft(0x0, 0x1AA)

    label("loc_173A6")

    OP_E0(0x24, 0x0)
    OP_E0(0x80, 0x0)
    SetScenarioFlags(0x1D9, 1)
    SetScenarioFlags(0x1, 3)
    SetChrSubChip(0x14, 0x0)
    EventEnd(0x5)
    Return()

    # Function_53_16A09 end

    def Function_54_173B9(): pass

    label("Function_54_173B9")

    EventBegin(0x0)
    Fade(500)
    OP_68(96790, 1200, -101940, 0)
    MoveCamera(48, 33, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16250, 0)
    SetChrPos(0x101, 96960, 0, -100830, 180)
    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xD, 0x10)
    TurnDirection(0xD, 0x101, 0)
    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_17490")
    Jump("loc_174DA")

    label("loc_17490")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_174B0")
    OP_52(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_174DA")

    label("loc_174B0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_174D0")
    OP_52(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_174DA")

    label("loc_174D0")

    OP_52(0xD, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_174DA")

    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xD, 0x10)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained the\x01",
            "barrier to Rixia.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xD,
        (
            "#12P#10704F...It looks like I need\x01",
            "to go.\x02\x03",
            "#10701FShe is the person with\x01",
            "which I share a fate...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00003F...Say, Rixia.\x02\x03",
            "#00001FIf possible, I'd like\x01",
            "you to leave her to\x01",
            "me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xD,
        (
            "#12P#10706F─No.\x02\x03",
            "#10708FIn a way, both she and I\x01",
            "are the product of our\x01",
            "circumstances.\x02\x03",
            "I need to find the path\x01",
            "I'll take going forward\x01",
            "as well...\x02\x03",
            "#10701FShe and I must confront\x01",
            "each other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00006F...Understood.\x02\x03",
            "#00001FLet's go once we're\x01",
            "ready.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x1D8, 4)
    SetChrSubChip(0xD, 0x0)
    EventEnd(0x5)
    Return()

    # Function_54_173B9 end

    def Function_55_176FB(): pass

    label("Function_55_176FB")

    EventBegin(0x0)
    Fade(500)
    OP_68(101090, 1000, -93870, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16290, 0)
    SetChrPos(0x101, 100220, 0, -93940, 90)
    SetChrPos(0xA, 101370, 150, -94090, 270)
    SetChrSubChip(0xA, 0x0)
    OP_0D()
    SetChrName("")

    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Lloyd explained the\x01",
            "barrier to Wazy.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    ChrTalk(
        0xA,
        (
            "#10404FHmph... I see.\x02\x03",
            "#10408F...Damn. Why does he\x01",
            "have to obsess over a\x01",
            "blockhead like me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#6P#00008FWazy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xA,
        (
            "#10401FIt seems like "he" wants\x01",
            "to settle things with\x01",
            "me.\x02\x03",
            "#10403FLloyd, can I join the\x01",
            "search party?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#6P#00003FYeah, understood.\x02\x03",
            "#00000FLet's go once we're\x01",
            "ready.\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x1D8, 0)
    SetChrPos(0xA, 101790, 150, -93960, 90)
    EventEnd(0x5)
    Return()

    # Function_55_176FB end

    def Function_56_178C9(): pass

    label("Function_56_178C9")

    EventBegin(0x0)
    Fade(500)
    OP_68(-3010, -500, 6090, 0)
    MoveCamera(46, 33, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16290, 0)
    SetChrPos(0x101, -3520, -1500, 5560, 0)
    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x101, 0)
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_179A0")
    Jump("loc_179EA")

    label("loc_179A0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_179C0")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_179EA")

    label("loc_179C0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_179E0")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_179EA")

    label("loc_179E0")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_179EA")

    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)
    OP_93(0x8, 0x104, 0x0)
    EndChrThread(0x8, 0x0)
    OP_0D()

    ChrTalk(
        0xB,
        (
            "#00200FAbbas just showed me how to\x01",
            "use the terminal, but...\x02\x03",
            "#00203FIt seems like the Merkabah's\x01",
            "systems were made by the\x01",
            "Epstein Foundation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        "#00005FHuh... Really!?\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        (
            "#00200FYes, there's no mistake.\x02\x03",
            "#00203FLong ago, people from\x01",
            "the Church noticed the\x01",
            "foundation's HQ...\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x8, 0)
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_17BC8")
    Jump("loc_17C12")

    label("loc_17BC8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_17BE8")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_17C12")

    label("loc_17BE8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_17C08")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_17C12")

    label("loc_17C08")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_17C12")

    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)

    ChrTalk(
        0xB,
        (
            "#00200FMost likely, the foundation\x01",
            "and Church have been\x01",
            "cooperating ever since.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100F...Unofficially, though.\x02\x03",
            "This Merkabah was formerly the Heaven's\x01",
            "Wheel, a flight-capable artifact vehicle...\x02\x03",
            "After the orbal revolution, with the help of\x01",
            "the foundation, we used the Heaven's Wheel\x01",
            "mechanism, giving it its current form.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00005FHeaven's Wheel... It's a\x01",
            "name Zeit muttered when he\x01",
            "first saw the Merkabah.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100FI'll tell you this while I'm at it.\x01",
            "The church also participates in\x01",
            "development of tactical orbments.\x02\x03",
            "The "Orbal Arts" you all use were\x01",
            "formerly used through a skill\x01",
            "called Thaumaturgy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#00203FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(
        0x8,
        (
            "#12100FI think you already know this, but\x01",
            "this is a strictly informal matter.\x01",
            "Do not leak this information outside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0x101,
        (
            "#00000FYeah, of course we know\x01",
            "that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(
        0xB,
        "#00200FI understand as well.\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D6, 4)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0xB, 0x10)
    SetChrSubChip(0xB, 0x0)
    OP_93(0x8, 0x13B, 0x0)
    BeginChrThread(0x8, 0, 0, 0)
    EventEnd(0x5)
    Return()

    # Function_56_178C9 end

    SaveToFile()

Try(main)
