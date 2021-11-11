import requests

value = input("Please enter a username:\n")

print(f'Getting the stats for {value}')

stats = requests.get('https://api.hyperlandsmc.net/stats/{}'.format(value))
stats = stats.json()
online = stats['status']['online']
last_server = stats['status']['lastServer']
rank = stats['rankData']['rank']
level = stats['stats']['general']['level']
levelprogress = stats['stats']['general']['progress']
max_level_progress = stats['stats']['general']['maxProgress']
skywars_wins = stats['stats']['skywars']['wins']
skywars_kills = stats['stats']['skywars']['kills']
bedwars_wins = stats['stats']['bedwars']['wins']
bedwars_kills = stats['stats']['bedwars']['kills']
bedwars_finalkills = stats['stats']['bedwars']['finalKills']
bedwars_beds_broken = stats['stats']['bedwars']['bedsBroken']
bedwars_current_ws = stats['stats']['bedwars']['currentWinstreak']
bedwars_overall_ws = stats['stats']['bedwars']['bestWinstreak']
thebridge_wins = stats['stats']['thebridge']['wins']
thebridge_goals = stats['stats']['thebridge']['goals']
thebridge_current = stats['stats']['thebridge']['currentWinstreak']
thebridge_best = stats['stats']['thebridge']['bestWinstreak']
duels_wins = stats['stats']['duels']['buildUhcWins']
duels_potwins = stats['stats']['duels']['potWins']
duels_ironwins = stats['stats']['duels']['ironWins']
duels_archerwins = stats['stats']['duels']['archerWins']
duels_sumowis = stats['stats']['duels']['sumoWins']
duels_ws = stats['stats']['duels']['currentWinstreak']
duel_best_ws = stats['stats']['duels']['bestWinstreak']
duel_elo = stats['stats']['duels']['elo']
UHC_wins = stats['stats']['uhcmeetup']['wins']
UHC_kills = stats['stats']['uhcmeetup']['kills']

print(f'Online: {online}')
print(f'Rank: {rank}')
print(f'Last Seen: {last_server}')
print(f'Skywars Wins: {skywars_wins}')
print(f'Skywars Kills: {skywars_kills}')
print(f'Bedwars Wins: {bedwars_wins}')
print(f'Bedwars Kills: {bedwars_kills}')
print(f'Bedwars FinalKills: {bedwars_finalkills}')
print(f'Bedwars Beds Broken: {bedwars_beds_broken}')
print(f'Bedwars Current Winstreak: {bedwars_current_ws}')
print(f'Bedwars Best Winstreak: {bedwars_overall_ws}')
print(f'The Bridge Wins: {thebridge_wins}')
print(f'The Bridge Goals: {thebridge_goals}')
print(f'The Bridge Current Winstreak: {thebridge_current}')
print(f'The Bridge Best Winstreak: {thebridge_best}')
print(f'Duels BuildUHC Wins: {duels_wins}')
print(f'Duels PotPvP Wins: {duels_potwins}')
print(f'Duels Iron Wins: {duels_ironwins}')
print(f'Duels Archer Wins: {duels_archerwins}')
print(f'Duels Sumo Wins: {duels_sumowis}')
print(f'Duels Elo: {duel_elo}')
print(f'UHC Wins: {UHC_wins}')
print(f'UHC Kills: {UHC_kills}')
value2 = input("Please enter a username:\n")