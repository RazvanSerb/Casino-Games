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
# getCardValue: return the value of the card
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
def getCardValue(card):
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
        return 10
    elif card in cardQ:
        return 10
    elif card in cardK:
        return 10
    elif card in cardA:
        return 11
    return 0
# startGame: return a list of lists of 2 cardsPack generates each for Player and Dealer
def startGame(cardsPack):
    cardsPlayer = []
    numCardAPlayer = 0
    cardsDealer = []
    numCardADealer = 0
    for _ in range(0, 2):
        cardPlayer = generateCard(cardsPack)
        if cardPlayer in cardA:
            numCardAPlayer += 1
        cardsPlayer.append(cardPlayer)
        cardDealer = generateCard(cardsPack)
        if cardDealer in cardA:
            numCardADealer += 1
        cardsDealer.append(cardDealer)
    return [[cardsPlayer, numCardAPlayer], [cardsDealer, numCardADealer]]
# finishGame: return the result of the game
def finishGame(sumCardsPlayer, sumCardsDealer):
    if sumCardsPlayer > 21:
        return 0
    if sumCardsDealer > 21:
        return 1
    if sumCardsPlayer >= sumCardsDealer:
        return 1
    return 0
# blackjack: the game API
black = (0, 0, 0)
white = (255, 255, 255)
green = (19, 85, 52)
def blackjack():
    pygame.init()
    pygame.display.set_icon(icon)
    pygame.display.set_caption('Blackjack')
    screen = pygame.display.set_mode((1024, 768))
    background = pygame.image.load("resources/BG.png")
    font = pygame.font.Font("resources/Arial.ttf", 42)
    MenuButton = pygame.draw.rect(background, green, (700, 670, 300, 50))
    MenuText = font.render('Main Menu', 1, black)
    HitButton = pygame.draw.rect(background, green, (20, 330, 150, 60))
    HitText = font.render('Hit', 1, white)
    StandButton = pygame.draw.rect(background, green, (190, 330, 150, 60))
    StandText = font.render('Stand', 1, white)
    pygame.draw.rect(background, green, (700, 10, 300, 200))
    BGCopy = copy.copy(background)
    numWins = 0
    numLosses = 0
    if True:
        cardsPackCopy = copy.copy(cardsPack)
        [[cardsPlayer, numCardAPlayer], [cardsDealer, numCardADealer]] = startGame(cardsPackCopy)
        sumCardsPlayer = getCardValue(cardsPlayer[0]) + getCardValue(cardsPlayer[1])
        sumCardsDealer = getCardValue(cardsDealer[0]) + getCardValue(cardsDealer[1])
        Stand = False
        GameOver = False
        screen.blit(background, (0, 0))
        screen.blit(HitText, (70, 330))
        screen.blit(StandText, (210, 330))
        if len(cardsPlayer) == 2 and sumCardsPlayer == 21:
            while sumCardsDealer < 17:
                card = generateCard(cardsPackCopy)
                cardsDealer.append(card)
                numCardADealer += card in cardA
                sumCardsDealer += getCardValue(card)
                while sumCardsDealer > 21 and numCardADealer > 0:
                    numCardADealer -= 1
                    sumCardsDealer -= 10
            if finishGame(sumCardsPlayer, sumCardsDealer) == 1:
                numWins = numWins + 1
            else:
                numLosses = numLosses + 1
            GameOver = True
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and MenuButton.collidepoint(pygame.mouse.get_pos()):
                menu.menu()
            elif event.type == pygame.MOUSEBUTTONDOWN and not (GameOver or Stand) and HitButton.collidepoint(pygame.mouse.get_pos()):
                card = generateCard(cardsPackCopy)
                cardsPlayer.append(card)
                numCardAPlayer += card in cardA
                sumCardsPlayer += getCardValue(card)
                while sumCardsPlayer > 21 and numCardAPlayer > 0:
                    numCardAPlayer -= 1
                    sumCardsPlayer -= 10
                if len(cardsPlayer) >= 5 or (sumCardsPlayer >= 21 and numCardAPlayer == 0):
                    while sumCardsDealer < 17:
                        card = generateCard(cardsPackCopy)
                        cardsDealer.append(card)
                        numCardADealer += card in cardA
                        sumCardsDealer += getCardValue(card)
                        while sumCardsDealer > 21 and numCardADealer > 0:
                            numCardADealer -= 1
                            sumCardsDealer -= 10
                    if finishGame(sumCardsPlayer, sumCardsDealer) == 1:
                        numWins = numWins + 1
                    else:
                        numLosses = numLosses + 1
                    GameOver = True
            elif event.type == pygame.MOUSEBUTTONDOWN and not GameOver and StandButton.collidepoint(pygame.mouse.get_pos()):
                Stand = True
                while len(cardsDealer) <= 5 and sumCardsDealer < 17:
                    card = generateCard(cardsPackCopy)
                    cardsDealer.append(card)
                    numCardADealer += card in cardA
                    sumCardsDealer += getCardValue(card)
                    while sumCardsDealer > 21 and numCardADealer > 0:
                        numCardADealer -= 1
                        sumCardsDealer -= 10
                if finishGame(sumCardsPlayer, sumCardsDealer) == 1:
                    numWins = numWins + 1
                else:
                    numLosses = numLosses + 1
                GameOver = True
            elif event.type == pygame.MOUSEBUTTONDOWN and GameOver and RestartButton.collidepoint(pygame.mouse.get_pos()):
                cardsPackCopy = copy.copy(cardsPack)
                [[cardsPlayer, numCardAPlayer], [cardsDealer, numCardADealer]] = startGame(cardsPackCopy)
                sumCardsPlayer = getCardValue(cardsPlayer[0]) + getCardValue(cardsPlayer[1])
                sumCardsDealer = getCardValue(cardsDealer[0]) + getCardValue(cardsDealer[1])
                Stand = False
                GameOver = False
                if len(cardsPlayer) == 2 and sumCardsPlayer == 21:
                    while sumCardsDealer < 17:
                        card = generateCard(cardsPackCopy)
                        cardsDealer.append(card)
                        numCardADealer += card in cardA
                        sumCardsDealer += getCardValue(card)
                        while sumCardsDealer > 21 and numCardADealer > 0:
                            numCardADealer -= 1
                            sumCardsDealer -= 10
                    if finishGame(sumCardsPlayer, sumCardsDealer) == 1:
                        numWins = numWins + 1
                    else:
                        numLosses = numLosses + 1
                    GameOver = True
        screen.blit(background, (0, 0))
        screen.blit(MenuText, (750, 665))
        screen.blit(HitText, (70, 330))
        screen.blit(StandText, (210, 330))
        WinsText = font.render('Wins: %i' % numWins, 1, black)
        screen.blit(WinsText, (790, 35))
        LossesText = font.render('Losses: %i' % numLosses, 1, black)
        screen.blit(LossesText, (770, 105))
        for card in cardsDealer:
            x = 10 + cardsDealer.index(card) * 110
            screen.blit(card, (x, 10))
        screen.blit(cardBack, (120, 10))
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
    blackjack()
