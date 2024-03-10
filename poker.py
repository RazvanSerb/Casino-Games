import menu as menu
import pygame
from pygame.locals import *
import random
import copy

icon = pygame.transform.scale(pygame.image.load('resources/ICON.png'), (223, 312))
cardBack = pygame.transform.scale(pygame.image.load('resources/CARDS/CARDBACK.png'), (223, 312))
Conny2 = pygame.transform.scale(pygame.image.load('resources/CARDS/02C.png'), (223, 312))
Robby2 = pygame.transform.scale(pygame.image.load('resources/CARDS/02R.png'), (223, 312))
Sam2 = pygame.transform.scale(pygame.image.load('resources/CARDS/02S.png'), (223, 312))
Vivi2 = pygame.transform.scale(pygame.image.load('resources/CARDS/02V.png'), (223, 312))
Conny3 = pygame.transform.scale(pygame.image.load('resources/CARDS/03C.png'), (223, 312))
Robby3 = pygame.transform.scale(pygame.image.load('resources/CARDS/03R.png'), (223, 312))
Sam3 = pygame.transform.scale(pygame.image.load('resources/CARDS/03S.png'), (223, 312))
Vivi3 = pygame.transform.scale(pygame.image.load('resources/CARDS/03V.png'), (223, 312))
Conny4 = pygame.transform.scale(pygame.image.load('resources/CARDS/04C.png'), (223, 312))
Robby4 = pygame.transform.scale(pygame.image.load('resources/CARDS/04R.png'), (223, 312))
Sam4 = pygame.transform.scale(pygame.image.load('resources/CARDS/04S.png'), (223, 312))
Vivi4 = pygame.transform.scale(pygame.image.load('resources/CARDS/04V.png'), (223, 312))
Conny5 = pygame.transform.scale(pygame.image.load('resources/CARDS/05C.png'), (223, 312))
Robby5 = pygame.transform.scale(pygame.image.load('resources/CARDS/05R.png'), (223, 312))
Sam5 = pygame.transform.scale(pygame.image.load('resources/CARDS/05S.png'), (223, 312))
Vivi5 = pygame.transform.scale(pygame.image.load('resources/CARDS/05V.png'), (223, 312))
Conny6 = pygame.transform.scale(pygame.image.load('resources/CARDS/06C.png'), (223, 312))
Robby6 = pygame.transform.scale(pygame.image.load('resources/CARDS/06R.png'), (223, 312))
Sam6 = pygame.transform.scale(pygame.image.load('resources/CARDS/06S.png'), (223, 312))
Vivi6 = pygame.transform.scale(pygame.image.load('resources/CARDS/06V.png'), (223, 312))
Conny7 = pygame.transform.scale(pygame.image.load('resources/CARDS/07C.png'), (223, 312))
Robby7 = pygame.transform.scale(pygame.image.load('resources/CARDS/07R.png'), (223, 312))
Sam7 = pygame.transform.scale(pygame.image.load('resources/CARDS/07S.png'), (223, 312))
Vivi7 = pygame.transform.scale(pygame.image.load('resources/CARDS/07V.png'), (223, 312))
Conny8 = pygame.transform.scale(pygame.image.load('resources/CARDS/08C.png'), (223, 312))
Robby8 = pygame.transform.scale(pygame.image.load('resources/CARDS/08R.png'), (223, 312))
Sam8 = pygame.transform.scale(pygame.image.load('resources/CARDS/08S.png'), (223, 312))
Vivi8 = pygame.transform.scale(pygame.image.load('resources/CARDS/08V.png'), (223, 312))
Conny9 = pygame.transform.scale(pygame.image.load('resources/CARDS/09C.png'), (223, 312))
Robby9 = pygame.transform.scale(pygame.image.load('resources/CARDS/09R.png'), (223, 312))
Sam9 = pygame.transform.scale(pygame.image.load('resources/CARDS/09S.png'), (223, 312))
Vivi9 = pygame.transform.scale(pygame.image.load('resources/CARDS/09V.png'), (223, 312))
Conny10 = pygame.transform.scale(pygame.image.load('resources/CARDS/10C.png'), (223, 312))
Robby10 = pygame.transform.scale(pygame.image.load('resources/CARDS/10R.png'), (223, 312))
Sam10 = pygame.transform.scale(pygame.image.load('resources/CARDS/10S.png'), (223, 312))
Vivi10 = pygame.transform.scale(pygame.image.load('resources/CARDS/10V.png'), (223, 312))
ConnyJ = pygame.transform.scale(pygame.image.load('resources/CARDS/12C.png'), (223, 312))
RobbyJ = pygame.transform.scale(pygame.image.load('resources/CARDS/12R.png'), (223, 312))
SamJ = pygame.transform.scale(pygame.image.load('resources/CARDS/12S.png'), (223, 312))
ViviJ = pygame.transform.scale(pygame.image.load('resources/CARDS/12V.png'), (223, 312))
ConnyQ = pygame.transform.scale(pygame.image.load('resources/CARDS/13C.png'), (223, 312))
RobbyQ = pygame.transform.scale(pygame.image.load('resources/CARDS/13R.png'), (223, 312))
SamQ = pygame.transform.scale(pygame.image.load('resources/CARDS/13S.png'), (223, 312))
ViviQ = pygame.transform.scale(pygame.image.load('resources/CARDS/13V.png'), (223, 312))
ConnyK = pygame.transform.scale(pygame.image.load('resources/CARDS/14C.png'), (223, 312))
RobbyK = pygame.transform.scale(pygame.image.load('resources/CARDS/14R.png'), (223, 312))
SamK = pygame.transform.scale(pygame.image.load('resources/CARDS/14S.png'), (223, 312))
ViviK = pygame.transform.scale(pygame.image.load('resources/CARDS/14V.png'), (223, 312))
ConnyA = pygame.transform.scale(pygame.image.load('resources/CARDS/01C.png'), (223, 312))
RobbyA = pygame.transform.scale(pygame.image.load('resources/CARDS/01R.png'), (223, 312))
SamA = pygame.transform.scale(pygame.image.load('resources/CARDS/01S.png'), (223, 312))
ViviA = pygame.transform.scale(pygame.image.load('resources/CARDS/01V.png'), (223, 312))
cardsPack = [ ConnyA, Conny2, Conny3, Conny4, Conny5, Conny6, Conny7, Conny8, Conny9, Conny10, ConnyJ, ConnyQ, ConnyK, \
          RobbyA, Robby2, Robby3, Robby4, Robby5, Robby6, Robby7, Robby8, Robby9, Robby10, RobbyJ, RobbyQ, RobbyK, \
          SamA, Sam2, Sam3, Sam4, Sam5, Sam6, Sam7, Sam8, Sam9, Sam10, SamJ, SamQ, SamK, \
          ViviA, Vivi2, Vivi3, Vivi4, Vivi5, Vivi6, Vivi7, Vivi8, Vivi9, Vivi10, ViviJ, ViviQ, ViviK ]
# generateCard: generate a random card from pack
def generateCard(cardsPack):
    card = random.choice(cardsPack)
    cardsPack.remove(card)
    return card
# getCardCharacter: return the character on the card
cardC = [ ConnyA, Conny2, Conny3, Conny4, Conny5, Conny6, Conny7, Conny8, Conny9, Conny10, ConnyJ, ConnyQ, ConnyK]
cardR = [ RobbyA, Robby2, Robby3, Robby4, Robby5, Robby6, Robby7, Robby8, Robby9, Robby10, RobbyJ, RobbyQ, RobbyK]
cardS = [ SamA, Sam2, Sam3, Sam4, Sam5, Sam6, Sam7, Sam8, Sam9, Sam10, SamJ, SamQ, SamK]
cardV = [ ViviA, Vivi2, Vivi3, Vivi4, Vivi5, Vivi6, Vivi7, Vivi8, Vivi9, Vivi10, ViviJ, ViviQ, ViviK]
def getCardCharacter(card):
    if card in cardC:
        return "C"
    elif card in cardR:
        return "R"
    elif card in cardS:
        return "S"
    elif card in cardV:
        return "V"
    return "#"
# getCardNumber: return the number on the card
card2 = [ Conny2, Robby2, Sam2, Vivi2 ]
card3 = [ Conny3, Robby3, Sam3, Vivi3 ]
card4 = [ Conny4, Robby4, Sam4, Vivi4 ]
card5 = [ Conny5, Robby5, Sam5, Vivi5 ]
card6 = [ Conny6, Robby6, Sam6, Vivi6 ]
card7 = [ Conny7, Robby7, Sam7, Vivi7 ]
card8 = [ Conny8, Robby8, Sam8, Vivi8 ]
card9 = [ Conny9, Robby9, Sam9, Vivi9 ]
card10 = [ Conny10, Robby10, Sam10, Vivi10 ]
cardJ = [ ConnyJ, RobbyJ, SamJ, ViviJ ]
cardQ = [ ConnyQ, RobbyQ, SamQ, ViviQ ]
cardK = [ ConnyK, RobbyK, SamK, ViviK ]
cardA = [ ConnyA, RobbyA, SamA, ViviA ]
def getCardNumber(card):
    if card in card2:
        return 2
    elif card in card3:
        return 3
    elif card in card4:
        return 4
    elif card in card5:
        return 5
    elif card in card6:
        return 6
    elif card in card7:
        return 7
    elif card in card8:
        return 8
    elif card in card9:
        return 9
    elif card in card10:
        return 10
    elif card in cardJ:
        return 12
    elif card in cardQ:
        return 13
    elif card in cardK:
        return 14
    elif card in cardA:
        return 15
    return 0
# getCardValue: return the value of the card
def getCardValue(card):
    return [getCardCharacter(card), getCardNumber(card)]
# startGame: return a list of lists of 5 cards generates each for Player and Dealer
def startGame(cardsPack):
    cardsPlayer = []
    cardsDealer = []
    for _ in range(0, 5):
        cardsPlayer.append(generateCard(cardsPack))
        cardsDealer.append(generateCard(cardsPack))
    return [cardsPlayer, cardsDealer]
# finishGame: return the result of the game
def finishGame(cardsPlayer, cardsDealer):
    cardsValuesPlayer = []
    for card in cardsPlayer:
        cardsValuesPlayer.append(getCardValue(card))
    flushPlayer = []
    for character in ["C", "R", "S", "V"]:
        counter = sum(character in cardValue[0] for cardValue in cardsValuesPlayer)
        if counter == 5:
            flushPlayer.append(character)
    highCardValuePlayer = max(cardValue[1] for cardValue in cardsValuesPlayer)
    fourOfAKindPlayer = []
    threeOfAKindPlayer = []
    pairPlayer = []
    for cardNumber in range(2, 16):
        counter = sum(cardNumber == cardValue[1] for cardValue in cardsValuesPlayer)
        if counter == 4:
            fourOfAKindPlayer.append(cardNumber)
        if counter == 3:
            threeOfAKindPlayer.append(cardNumber)
        if counter == 2:
            pairPlayer.append(cardNumber)
    straightPlayer = []
    cardsValuesPlayer = sorted(cardsValuesPlayer, key=lambda x: x[1])
    if (cardsValuesPlayer[0][1] == cardsValuesPlayer[1][1] - 1) or (cardsValuesPlayer[0][1] == 10 and cardsValuesPlayer[1][1] == 12):
        if (cardsValuesPlayer[1][1] == cardsValuesPlayer[2][1] - 1) or (cardsValuesPlayer[1][1] == 10 and cardsValuesPlayer[2][1] == 12):
            if (cardsValuesPlayer[2][1] == cardsValuesPlayer[3][1] - 1) or (cardsValuesPlayer[2][1] == 10 and cardsValuesPlayer[3][1] == 12):
                if (cardsValuesPlayer[3][1] == cardsValuesPlayer[4][1] - 1) or (cardsValuesPlayer[3][1] == 10 and cardsValuesPlayer[4][1] == 12):
                    straightPlayer.append(cardsValuesPlayer[4][1])
    cardsValuesDealer = []
    for card in cardsDealer:
        cardsValuesDealer.append(getCardValue(card))
    flushDealer = []
    for character in ["C", "R", "S", "V"]:
        counter = sum(character in cardValue[0] for cardValue in cardsValuesDealer)
        if counter == 5:
            flushDealer.append(character)
    highCardValueDealer = max(cardValue[1] for cardValue in cardsValuesDealer)
    fourOfAKindDealer = []
    threeOfAKindDealer = []
    pairDealer = []
    for cardNumber in range(2, 16):
        counter = sum(cardNumber == cardValue[1] for cardValue in cardsValuesDealer)
        if counter == 4:
            fourOfAKindDealer.append(cardNumber)
        if counter == 3:
            threeOfAKindDealer.append(cardNumber)
        if counter == 2:
            pairDealer.append(cardNumber)
    straightDealer = []
    cardsValuesDealer = sorted(cardsValuesDealer, key=lambda x: x[1])
    if (cardsValuesDealer[0][1] == cardsValuesDealer[1][1] - 1) or (cardsValuesDealer[0][1] == 10 and cardsValuesDealer[1][1] == 12):
        if (cardsValuesDealer[1][1] == cardsValuesDealer[2][1] - 1) or (cardsValuesDealer[1][1] == 10 and cardsValuesDealer[2][1] == 12):
            if (cardsValuesDealer[2][1] == cardsValuesDealer[3][1] - 1) or (cardsValuesDealer[2][1] == 10 and cardsValuesDealer[3][1] == 12):
                if (cardsValuesDealer[3][1] == cardsValuesDealer[4][1] - 1) or (cardsValuesDealer[3][1] == 10 and cardsValuesDealer[4][1] == 12):
                    straightDealer.append(cardsValuesDealer[4][1])
    handRankPlayer = 10
    handRankDealer = 10
    # Royal Flush
    if len(flushPlayer) == 1 and len(straightPlayer) == 1 and highCardValuePlayer == 15:
        handRankPlayer = 1
    if len(flushPlayer) == 1 and len(straightDealer) == 1 and highCardValueDealer == 15:
        handRankDealer = 1
    if handRankPlayer == handRankDealer == 1:
        return 1
    elif handRankPlayer < handRankDealer:
        return 1
    elif handRankDealer < handRankPlayer:
        return 0
    # Straight Flush
    if len(flushPlayer) == 1 and len(straightPlayer) == 1:
        handRankPlayer = 2
    if len(flushPlayer) == 1 and len(straightDealer) == 1:
        handRankDealer = 2
    if handRankPlayer == handRankDealer == 2:
        if straightPlayer[0] >= straightDealer[0]:
            return 1
        return 0
    elif handRankPlayer < handRankDealer:
        return 1
    elif handRankDealer < handRankPlayer:
        return 0
    # Four of a Kind
    if len(fourOfAKindPlayer) == 1:
        handRankPlayer = 3
    if len(fourOfAKindDealer) == 1:
        handRankDealer = 3
    if handRankPlayer == handRankDealer == 3:
        if fourOfAKindPlayer[0] > fourOfAKindDealer[0]:
            return 1
        return 0
    elif handRankPlayer < handRankDealer:
        return 1
    elif handRankDealer < handRankPlayer:
        return 0
    # Full House
    if len(threeOfAKindPlayer) == 1 and len(pairPlayer) == 1:
        handRankPlayer = 4
    if len(threeOfAKindDealer) == 1 and len(pairDealer) == 1:
        handRankDealer = 4
    if handRankPlayer == handRankDealer == 4:
        if threeOfAKindPlayer[0] > threeOfAKindDealer[0]:
            return 1
        return 0
    elif handRankPlayer < handRankDealer:
        return 1
    elif handRankDealer < handRankPlayer:
        return 0
    # Flush
    if len(flushPlayer) == 1:
        handRankPlayer = 5
    if len(flushDealer) == 1:
        handRankDealer = 5
    if handRankPlayer == handRankDealer == 5:
        if highCardValuePlayer >= highCardValueDealer:
            return 1
        return 0
    elif handRankPlayer < handRankDealer:
        return 1
    elif handRankDealer < handRankPlayer:
        return 0
    # Straight
    if len(straightPlayer) == 1:
        handRankPlayer = 6
    if len(straightDealer) == 1:
        handRankDealer = 6
    if handRankPlayer == handRankDealer == 6:
        if straightPlayer[0] >= straightDealer[0]:
            return 1
        return 0
    elif handRankPlayer < handRankDealer:
        return 1
    elif handRankDealer < handRankPlayer:
        return 0
    # Three of a Kind
    if len(threeOfAKindPlayer) == 1:
        handRankPlayer = 7
    if len(threeOfAKindDealer) == 1:
        handRankDealer = 7
    if handRankPlayer == handRankDealer == 7:
        if threeOfAKindPlayer[0] > threeOfAKindDealer[0]:
            return 1
        return 0
    elif handRankPlayer < handRankDealer:
        return 1
    elif handRankDealer < handRankPlayer:
        return 0
    # Two pair
    if len(pairPlayer) == 2:
        handRankPlayer = 8
    if len(pairDealer) == 2:
        handRankDealer = 8
    if handRankPlayer == handRankDealer == 8:
        if max(pairPlayer) > max(pairDealer):
            return 1
        elif max(pairPlayer) < max(pairDealer):
            return 0
        elif sum(pairPlayer) > sum(pairDealer):
            return 1
        elif sum(pairPlayer) < sum(pairDealer):
            return 0
        elif highCardValuePlayer >= highCardValueDealer:
            return 1
        return 0
    elif handRankPlayer < handRankDealer:
        return 1
    elif handRankDealer < handRankPlayer:
        return 0
    # Pair
    if len(pairPlayer) == 1:
        handRankPlayer = 9
    if len(pairDealer) == 1:
        handRankDealer = 9
    if handRankPlayer == handRankDealer == 9:
        if pairPlayer[0] > pairDealer[0]:
            return 1
        elif pairPlayer[0] < pairDealer[0]:
            return 0
        elif highCardValuePlayer >= highCardValueDealer:
            return 1
        return 0
    elif handRankPlayer < handRankDealer:
        return 1
    elif handRankDealer < handRankPlayer:
        return 0
    # High card
    if highCardValuePlayer >= highCardValueDealer:
        return 1
    return 0
# poker: the game API
black = (0, 0, 0)
white = (255, 255, 255)
green = (19, 85, 52)
def poker():
    pygame.init()
    pygame.display.set_icon(icon)
    pygame.display.set_caption('Poker')
    screen = pygame.display.set_mode((1024, 768))
    background = pygame.image.load("resources/BG.png")
    font = pygame.font.Font("resources/Arial.ttf", 42)
    MenuButton = pygame.draw.rect(background, green, (700, 670, 300, 50))
    MenuText = font.render('Main Menu', 1, black)
    ChangeButton = pygame.draw.rect(background, green, (20, 330, 150, 60))
    ChangeText = font.render('Change', 1, white)
    StandButton = pygame.draw.rect(background, green, (190, 330, 150, 60))
    StandText = font.render('Stand', 1, white)
    pygame.draw.rect(background, green, (700, 10, 300, 200))
    card1Button = pygame.draw.rect(background, green, (10, 400, 110, 312))
    card2Button = pygame.draw.rect(background, green, (120, 400, 110, 312))
    card3Button = pygame.draw.rect(background, green, (230, 400, 110, 312))
    card4Button = pygame.draw.rect(background, green, (340, 400, 110, 312))
    card5Button = pygame.draw.rect(background, green, (450, 400, 223, 312))
    BGCopy = copy.copy(background)
    numWins = 0
    numLosses = 0
    if True:
        cardsPackCopy = copy.copy(cardsPack)
        [cardsPlayer, cardsDealer] = startGame(cardsPackCopy)
        card1Changed = False
        card2Changed = False
        card3Changed = False
        card4Changed = False
        card5Changed = False
        Stand = False
        GameOver = False
        screen.blit(background, (0, 0))
        screen.blit(ChangeText, (20, 330))
        screen.blit(StandText, (210, 330))
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and MenuButton.collidepoint(pygame.mouse.get_pos()):
                menu.menu()
            elif event.type == pygame.MOUSEBUTTONDOWN and not (GameOver or Stand or card1Changed) and card1Button.collidepoint(pygame.mouse.get_pos()):
                for card in cardsPlayer:
                    if (cardsPlayer.index(card) != 0):
                        x = 10 + cardsPlayer.index(card) * 110
                        screen.blit(card, (x, 400))
                    else:
                        screen.blit(cardBack, (10, 400))
                pygame.display.update()
                running = True
                while running:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        elif event.type == pygame.MOUSEBUTTONDOWN and ChangeButton.collidepoint(pygame.mouse.get_pos()):
                            cardsPlayer[0] = generateCard(cardsPackCopy)
                            card1Changed = True
                            running = False
                        elif event.type == pygame.MOUSEBUTTONDOWN and card1Button.collidepoint(pygame.mouse.get_pos()):
                            running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not (GameOver or Stand or card2Changed) and card2Button.collidepoint(pygame.mouse.get_pos()):
                for card in cardsPlayer:
                    if (cardsPlayer.index(card) != 1):
                        x = 10 + cardsPlayer.index(card) * 110
                        screen.blit(card, (x, 400))
                    else:
                        screen.blit(cardBack, (120, 400))
                pygame.display.update()
                running = True
                while running:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        elif event.type == pygame.MOUSEBUTTONDOWN and ChangeButton.collidepoint(pygame.mouse.get_pos()):
                            cardsPlayer[1] = generateCard(cardsPackCopy)
                            card2Changed = True
                            running = False
                        elif event.type == pygame.MOUSEBUTTONDOWN and card2Button.collidepoint(pygame.mouse.get_pos()):
                            running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not (GameOver or Stand or card3Changed) and card3Button.collidepoint(pygame.mouse.get_pos()):
                for card in cardsPlayer:
                    if (cardsPlayer.index(card) != 2):
                        x = 10 + cardsPlayer.index(card) * 110
                        screen.blit(card, (x, 400))
                    else:
                        screen.blit(cardBack, (230, 400))
                pygame.display.update()
                running = True
                while running:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        elif event.type == pygame.MOUSEBUTTONDOWN and ChangeButton.collidepoint(pygame.mouse.get_pos()):
                            cardsPlayer[2] = generateCard(cardsPackCopy)
                            card3Changed = True
                            running = False
                        elif event.type == pygame.MOUSEBUTTONDOWN and card3Button.collidepoint(pygame.mouse.get_pos()):
                            running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not (GameOver or Stand or card4Changed) and card4Button.collidepoint(pygame.mouse.get_pos()):
                for card in cardsPlayer:
                    if (cardsPlayer.index(card) != 3):
                        x = 10 + cardsPlayer.index(card) * 110
                        screen.blit(card, (x, 400))
                    else:
                        screen.blit(cardBack, (340, 400))
                pygame.display.update()
                running = True
                while running:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        elif event.type == pygame.MOUSEBUTTONDOWN and ChangeButton.collidepoint(pygame.mouse.get_pos()):
                            cardsPlayer[3] = generateCard(cardsPackCopy)
                            card4Changed = True
                            running = False
                        elif event.type == pygame.MOUSEBUTTONDOWN and card4Button.collidepoint(pygame.mouse.get_pos()):
                            running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not (GameOver or Stand or card5Changed) and card5Button.collidepoint(pygame.mouse.get_pos()):
                for card in cardsPlayer:
                    if (cardsPlayer.index(card) != 4):
                        x = 10 + cardsPlayer.index(card) * 110
                        screen.blit(card, (x, 400))
                    else:
                        screen.blit(cardBack, (450, 400))
                pygame.display.update()
                running = True
                while running:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        elif event.type == pygame.MOUSEBUTTONDOWN and ChangeButton.collidepoint(pygame.mouse.get_pos()):
                            cardsPlayer[4] = generateCard(cardsPackCopy)
                            card5Changed = True
                            running = False
                        elif event.type == pygame.MOUSEBUTTONDOWN and card5Button.collidepoint(pygame.mouse.get_pos()):
                            running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not (GameOver or Stand or card1Changed or card2Changed or card3Changed or card4Changed or card5Changed) and ChangeButton.collidepoint(pygame.mouse.get_pos()):
                cardsPlayer[0] = generateCard(cardsPackCopy)
                cardsPlayer[1] = generateCard(cardsPackCopy)
                cardsPlayer[2] = generateCard(cardsPackCopy)
                cardsPlayer[3] = generateCard(cardsPackCopy)
                cardsPlayer[4] = generateCard(cardsPackCopy)
                Stand = True
                if finishGame(cardsPlayer, cardsDealer) == 1:
                    numWins = numWins + 1
                else:
                    numLosses = numLosses + 1
                GameOver = True
            elif event.type == pygame.MOUSEBUTTONDOWN and not GameOver and StandButton.collidepoint(pygame.mouse.get_pos()):
                Stand = True
                if finishGame(cardsPlayer, cardsDealer) == 1:
                    numWins = numWins + 1
                else:
                    numLosses = numLosses + 1
                GameOver = True
            elif event.type == pygame.MOUSEBUTTONDOWN and GameOver and RestartButton.collidepoint(pygame.mouse.get_pos()):
                cardsPackCopy = copy.copy(cardsPack)
                [cardsPlayer, cardsDealer] = startGame(cardsPackCopy)
                card1Changed = False
                card2Changed = False
                card3Changed = False
                card4Changed = False
                card5Changed = False
                Stand = False
                GameOver = False
        screen.blit(background, (0, 0))
        screen.blit(MenuText, (750, 665))
        screen.blit(ChangeText, (20, 330))
        screen.blit(StandText, (210, 330))
        WinsText = font.render('Wins: %i' % numWins, 1, black)
        screen.blit(WinsText, (790, 35))
        LossesText = font.render('Losses: %i' % numLosses, 1, black)
        screen.blit(LossesText, (770, 105))
        for card in cardsDealer:
            x = 10 + cardsDealer.index(card) * 110
            screen.blit(cardBack, (x, 10))
        for card in cardsPlayer:
            x = 10 + cardsPlayer.index(card) * 110
            screen.blit(card, (x, 400))
        if GameOver:
            for card in cardsDealer:
                x = 10 + cardsDealer.index(card) * 110
                screen.blit(card, (x, 10))
            GameOverText = font.render('GAME OVER', 1, black)
            screen.blit(GameOverText, (400, 330))
            RestartButton = pygame.draw.rect(background, green, (700, 600, 300, 50))
            RestartText = font.render('Restart', 1, black)
            screen.blit(RestartText, (785, 595))
            background = copy.copy(BGCopy)
        pygame.display.update()

if __name__ == '__main__':
    poker()
