from war_game_prep import Card, Deck, Player

player_one = Player("Jon")
player_two = Player("Alex")
play_deck = Deck()
play_deck.shuffle()

for x in range(26):
    player_one.add_cards(play_deck.deal_one())
    player_two.add_cards(play_deck.deal_one())

game_on = True
round_num = 0

while game_on:

    round_num += 1
    print(f"Round {round_num}")

    if len(player_one.all_cards) == 0:
        print("Jon out of cards! Game Over")
        print("Alex Wins!")
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print("Alex out of cards! Game Over")
        print("Jon Wins!")
        game_on = False
        break

    player_one_cards = [player_one.remove_one()]

    player_two_cards = [player_two.remove_one()]

    at_war = True

    while at_war:

        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False

        else:
            print('WAR!')
            if len(player_one.all_cards) < 5:
                print("Jon unable to play war! Game Over at War")
                print("Alex Wins! Jon Loses!")
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print("Alex unable to play war! Game Over at War")
                print("Jon Wins! Alex Loses!")
                game_on = False
                break

            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
